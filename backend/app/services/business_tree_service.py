from typing import List, Dict, Optional, Any
from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import HTTPException
from datetime import datetime

from app.models.business_tree import BusinessTreeNode, NodeSourceMapping
from app.models.device import Device
from app.services.device_service import DeviceService


class BusinessTreeService:
    
    @staticmethod
    def initialize_root_node(db: Session) -> BusinessTreeNode:
        """初始化根节点"""
        root = db.query(BusinessTreeNode).filter(
            BusinessTreeNode.parent_id == None
        ).first()
        
        if not root:
            root = BusinessTreeNode(
                name="业务管理",
                parent_id=None,
                depth=0,
                is_leaf=False,
                path="/",
                visible_roles=["admin", "operator", "viewer"]
            )
            db.add(root)
            db.commit()
            db.refresh(root)
        
        return root
    
    @staticmethod
    def get_tree(db: Session, user_roles: List[str]) -> Dict:
        """获取完整业务树（根据用户角色过滤）"""
        print(f"DEBUG: BusinessTreeService.get_tree 被调用，user_roles = {user_roles}")
        
        # 获取根节点
        root = db.query(BusinessTreeNode).filter(
            BusinessTreeNode.parent_id == None
        ).first()
        
        print(f"DEBUG: 找到根节点: {root.name if root else 'None'}")
        
        if not root:
            root = BusinessTreeService.initialize_root_node(db)
        
        # 递归构建树
        def build_tree(node: BusinessTreeNode) -> Dict:
            print(f"DEBUG: build_tree 处理节点: {node.name}, visible_roles: {node.visible_roles}")
            
            # 检查节点是否对用户可见
            visible_roles = node.visible_roles or []
            # 如果用户是管理员，或者节点没有权限限制，或者用户角色匹配，则可见
            has_admin = "admin" in user_roles
            has_matching_role = any(role in visible_roles for role in user_roles)
            
            print(f"DEBUG: 权限检查 - has_admin: {has_admin}, has_matching_role: {has_matching_role}, visible_roles: {visible_roles}")
            
            if visible_roles and not has_admin and not has_matching_role:
                print(f"DEBUG: 节点 {node.name} 权限检查失败，返回 None")
                return None
            
            node_dict = node.to_dict()
            children = []
            
            for child in node.children:
                child_dict = build_tree(child)
                if child_dict:
                    children.append(child_dict)
            
            node_dict['children'] = children
            node_dict['source_count'] = len(node.source_mappings) if node.is_leaf else 0
            
            return node_dict
        
        return build_tree(root)
    
    @staticmethod
    def get_node_by_id(db: Session, node_id: int) -> BusinessTreeNode:
        """根据ID获取节点"""
        node = db.query(BusinessTreeNode).filter(
            BusinessTreeNode.id == node_id
        ).first()
        
        if not node:
            raise HTTPException(status_code=404, detail="节点不存在")
        
        return node
    
    @staticmethod
    def create_node(
        db: Session,
        parent_id: int,
        name: str,
        user_id: int,
        visible_roles: List[str] = None
    ) -> BusinessTreeNode:
        """创建新节点"""
        # 获取父节点
        parent = BusinessTreeService.get_node_by_id(db, parent_id)
        
        # 检查父节点是否为叶子节点
        if parent.is_leaf:
            raise HTTPException(status_code=400, detail="不能在叶子节点下创建子节点")
        
        # 检查层级限制
        if parent.depth >= 4:
            raise HTTPException(status_code=400, detail="已达到最大层级限制（5层）")
        
        # 检查同级节点名称唯一性
        existing = db.query(BusinessTreeNode).filter(
            and_(
                BusinessTreeNode.parent_id == parent_id,
                BusinessTreeNode.name == name
            )
        ).first()
        
        if existing:
            raise HTTPException(status_code=400, detail="同级节点名称已存在")
        
        # 检查子节点数量限制
        children_count = db.query(BusinessTreeNode).filter(
            BusinessTreeNode.parent_id == parent_id
        ).count()
        
        if children_count >= 100:
            raise HTTPException(status_code=400, detail="子节点数量已达上限（100个）")
        
        # 创建新节点
        new_node = BusinessTreeNode(
            name=name,
            parent_id=parent_id,
            depth=parent.depth + 1,
            is_leaf=True,  # 新创建的节点默认是叶子节点
            path=f"{parent.path}{parent.id}/",
            visible_roles=visible_roles or ["admin", "operator", "viewer"],
            created_by=user_id,
            updated_by=user_id
        )
        
        # 如果父节点原本是叶子节点，更新为非叶子节点
        if parent.is_leaf:
            parent.is_leaf = False
        
        db.add(new_node)
        db.commit()
        db.refresh(new_node)
        
        return new_node
    
    @staticmethod
    def update_node(
        db: Session,
        node_id: int,
        name: Optional[str] = None,
        visible_roles: Optional[List[str]] = None,
        user_id: Optional[int] = None
    ) -> BusinessTreeNode:
        """更新节点信息"""
        node = BusinessTreeService.get_node_by_id(db, node_id)
        
        if name and name != node.name:
            # 检查同级节点名称唯一性
            existing = db.query(BusinessTreeNode).filter(
                and_(
                    BusinessTreeNode.parent_id == node.parent_id,
                    BusinessTreeNode.name == name,
                    BusinessTreeNode.id != node_id
                )
            ).first()
            
            if existing:
                raise HTTPException(status_code=400, detail="同级节点名称已存在")
            
            node.name = name
        
        if visible_roles is not None:
            node.visible_roles = visible_roles
        
        if user_id:
            node.updated_by = user_id
        
        node.updated_at = datetime.utcnow()
        
        db.commit()
        db.refresh(node)
        
        return node
    
    @staticmethod
    def delete_node(db: Session, node_id: int) -> bool:
        """删除节点"""
        node = BusinessTreeService.get_node_by_id(db, node_id)
        
        # 不能删除根节点
        if node.parent_id is None:
            raise HTTPException(status_code=400, detail="不能删除根节点")
        
        # 检查是否有子节点
        if node.children:
            raise HTTPException(status_code=400, detail="请先删除所有子节点")
        
        # 获取父节点
        parent = node.parent
        
        # 删除节点
        db.delete(node)
        
        # 如果父节点没有其他子节点了，将其更新为叶子节点
        remaining_children = db.query(BusinessTreeNode).filter(
            and_(
                BusinessTreeNode.parent_id == parent.id,
                BusinessTreeNode.id != node_id
            )
        ).count()
        
        if remaining_children == 0:
            parent.is_leaf = True
        
        db.commit()
        
        return True
    
    @staticmethod
    def move_node(
        db: Session,
        node_id: int,
        new_parent_id: int,
        user_id: int
    ) -> BusinessTreeNode:
        """移动节点到新的父节点下"""
        node = BusinessTreeService.get_node_by_id(db, node_id)
        new_parent = BusinessTreeService.get_node_by_id(db, new_parent_id)
        
        # 检查是否为叶子节点
        if not node.is_leaf:
            raise HTTPException(status_code=400, detail="只能移动叶子节点")
        
        # 检查新父节点是否为叶子节点
        if new_parent.is_leaf:
            raise HTTPException(status_code=400, detail="不能移动到叶子节点下")
        
        # 检查是否移动到自己或子节点下
        if new_parent_id == node_id or new_parent.path.startswith(f"{node.path}{node.id}/"):
            raise HTTPException(status_code=400, detail="不能移动到自己或子节点下")
        
        # 检查新父节点的层级限制
        if new_parent.depth >= 4:
            raise HTTPException(status_code=400, detail="目标位置已达到最大层级限制")
        
        # 检查新父节点下的名称唯一性
        existing = db.query(BusinessTreeNode).filter(
            and_(
                BusinessTreeNode.parent_id == new_parent_id,
                BusinessTreeNode.name == node.name
            )
        ).first()
        
        if existing:
            raise HTTPException(status_code=400, detail="目标位置已存在同名节点")
        
        # 更新原父节点的叶子状态
        old_parent = node.parent
        
        # 更新节点信息
        node.parent_id = new_parent_id
        node.depth = new_parent.depth + 1
        node.path = f"{new_parent.path}{new_parent.id}/"
        node.updated_by = user_id
        node.updated_at = datetime.utcnow()
        
        # 如果原父节点没有其他子节点了，将其更新为叶子节点
        remaining_children = db.query(BusinessTreeNode).filter(
            and_(
                BusinessTreeNode.parent_id == old_parent.id,
                BusinessTreeNode.id != node_id
            )
        ).count()
        
        if remaining_children == 0:
            old_parent.is_leaf = True
        
        # 如果新父节点原本是叶子节点，更新为非叶子节点
        if new_parent.is_leaf:
            new_parent.is_leaf = False
        
        db.commit()
        db.refresh(node)
        
        return node
    
    @staticmethod
    def get_node_sources(db: Session, node_id: int) -> List[Dict]:
        """获取节点绑定的视频源"""
        node = BusinessTreeService.get_node_by_id(db, node_id)
        
        if not node.is_leaf:
            return []
        
        mappings = db.query(NodeSourceMapping).filter(
            NodeSourceMapping.node_id == node_id
        ).all()
        
        return [mapping.to_dict() for mapping in mappings]
    
    @staticmethod
    def bind_sources(
        db: Session,
        node_id: int,
        sources: List[Dict[str, Any]]
    ) -> List[NodeSourceMapping]:
        """绑定视频源到节点"""
        node = BusinessTreeService.get_node_by_id(db, node_id)
        
        if not node.is_leaf:
            raise HTTPException(status_code=400, detail="只能为叶子节点绑定视频源")
        
        created_mappings = []
        
        for source in sources:
            # 检查是否已绑定
            existing = db.query(NodeSourceMapping).filter(
                and_(
                    NodeSourceMapping.node_id == node_id,
                    NodeSourceMapping.device_id == source['device_id'],
                    NodeSourceMapping.source_id == source['source_id']
                )
            ).first()
            
            if existing:
                continue
            
            # 创建新的绑定关系
            mapping = NodeSourceMapping(
                node_id=node_id,
                device_id=source['device_id'],
                source_id=source['source_id'],
                source_type=source.get('source_type', 'camera'),
                source_name=source.get('source_name', ''),
                status='normal'
            )
            
            db.add(mapping)
            created_mappings.append(mapping)
        
        db.commit()
        
        return created_mappings
    
    @staticmethod
    def unbind_sources(
        db: Session,
        node_id: int,
        mapping_ids: List[int]
    ) -> bool:
        """解绑视频源"""
        node = BusinessTreeService.get_node_by_id(db, node_id)
        
        deleted_count = db.query(NodeSourceMapping).filter(
            and_(
                NodeSourceMapping.node_id == node_id,
                NodeSourceMapping.id.in_(mapping_ids)
            )
        ).delete(synchronize_session=False)
        
        db.commit()
        
        return deleted_count > 0
    
    @staticmethod
    async def sync_source_status(
        db: Session,
        node_id: int,
        device_service: DeviceService
    ) -> List[Dict]:
        """同步视频源状态"""
        mappings = db.query(NodeSourceMapping).filter(
            NodeSourceMapping.node_id == node_id
        ).all()
        
        updated_mappings = []
        
        for mapping in mappings:
            try:
                # 调用设备API检查视频源是否存在
                device = db.query(Device).filter(Device.id == mapping.device_id).first()
                if device:
                    sources = await device_service.get_device_sources(device.id)
                    source_exists = any(s['id'] == mapping.source_id for s in sources)
                    
                    if source_exists:
                        mapping.status = 'normal'
                    else:
                        mapping.status = 'invalid'
                else:
                    mapping.status = 'invalid'
                
                mapping.last_sync_at = datetime.utcnow()
                updated_mappings.append(mapping.to_dict())
                
            except Exception:
                mapping.status = 'invalid'
                mapping.last_sync_at = datetime.utcnow()
                updated_mappings.append(mapping.to_dict())
        
        db.commit()
        
        return updated_mappings
    
    @staticmethod
    def batch_save_changes(
        db: Session,
        changes: Dict[str, Any],
        user_id: int
    ) -> Dict[str, Any]:
        """批量保存所有更改"""
        try:
            result = {
                'deleted': 0,
                'added': 0,
                'updated': 0,
                'moved': 0,
                'bindings_changed': 0
            }
            
            # 1. 处理删除
            if 'deleted' in changes:
                for node_id in changes['deleted']:
                    try:
                        BusinessTreeService.delete_node(db, node_id)
                        result['deleted'] += 1
                    except Exception:
                        pass
            
            # 2. 处理新增
            if 'added' in changes:
                for node_data in changes['added']:
                    try:
                        BusinessTreeService.create_node(
                            db,
                            parent_id=node_data['parent_id'],
                            name=node_data['name'],
                            user_id=user_id,
                            visible_roles=node_data.get('visible_roles')
                        )
                        result['added'] += 1
                    except Exception:
                        pass
            
            # 3. 处理更新
            if 'updated' in changes:
                for node_data in changes['updated']:
                    try:
                        BusinessTreeService.update_node(
                            db,
                            node_id=node_data['id'],
                            name=node_data.get('name'),
                            visible_roles=node_data.get('visible_roles'),
                            user_id=user_id
                        )
                        result['updated'] += 1
                    except Exception:
                        pass
            
            # 4. 处理移动
            if 'moved' in changes:
                for move_data in changes['moved']:
                    try:
                        BusinessTreeService.move_node(
                            db,
                            node_id=move_data['node_id'],
                            new_parent_id=move_data['new_parent_id'],
                            user_id=user_id
                        )
                        result['moved'] += 1
                    except Exception:
                        pass
            
            # 5. 处理绑定关系
            if 'bindings' in changes:
                for binding_change in changes['bindings']:
                    if binding_change['action'] == 'bind':
                        BusinessTreeService.bind_sources(
                            db,
                            node_id=binding_change['node_id'],
                            sources=binding_change['sources']
                        )
                        result['bindings_changed'] += len(binding_change['sources'])
                    elif binding_change['action'] == 'unbind':
                        BusinessTreeService.unbind_sources(
                            db,
                            node_id=binding_change['node_id'],
                            mapping_ids=binding_change['mapping_ids']
                        )
                        result['bindings_changed'] += len(binding_change['mapping_ids'])
            
            return result
            
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"批量保存失败: {str(e)}")