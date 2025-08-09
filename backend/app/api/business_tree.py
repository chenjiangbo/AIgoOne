from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.services.business_tree_service import BusinessTreeService
from app.services.device_service import DeviceService


router = APIRouter(tags=["business-tree"])


# Pydantic模型
class CreateNodeRequest(BaseModel):
    parent_id: int
    name: str = Field(..., min_length=1, max_length=64)
    visible_roles: Optional[List[str]] = None


class UpdateNodeRequest(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=64)
    visible_roles: Optional[List[str]] = None


class MoveNodeRequest(BaseModel):
    new_parent_id: int


class BindSourcesRequest(BaseModel):
    sources: List[Dict[str, Any]]


class UnbindSourcesRequest(BaseModel):
    mapping_ids: List[int]


class BatchSaveRequest(BaseModel):
    deleted: Optional[List[int]] = []
    added: Optional[List[Dict[str, Any]]] = []
    updated: Optional[List[Dict[str, Any]]] = []
    moved: Optional[List[Dict[str, Any]]] = []
    bindings: Optional[List[Dict[str, Any]]] = []


def require_admin(current_user: User = Depends(get_current_user)):
    """要求管理员权限"""
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="需要管理员权限"
        )
    return current_user


@router.get("")
async def get_business_tree(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    获取完整业务树（根据用户角色过滤）
    """
    try:
        print(f"DEBUG: 当前用户信息 - ID: {current_user.id}, username: {current_user.username}, role: {current_user.role}")
        user_roles = [current_user.role] if current_user.role else []
        print(f"DEBUG: 构造的用户角色列表: {user_roles}")
        tree = BusinessTreeService.get_tree(db, user_roles)
        print(f"DEBUG: 获取到的树数据: {tree}")
        return {"success": True, "data": tree}
    except Exception as e:
        import traceback
        print(f"DEBUG: 获取业务树时出错: {str(e)}")
        print(f"DEBUG: 错误栈: {traceback.format_exc()}")
        return {"success": False, "message": f"获取业务树失败: {str(e)}", "traceback": traceback.format_exc(), "data": None}


@router.get("/nodes/{node_id}")
async def get_node_detail(
    node_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    获取节点详情
    """
    node = BusinessTreeService.get_node_by_id(db, node_id)
    
    # 检查用户是否有权限查看该节点
    user_roles = [current_user.role] if current_user.role else []
    if not any(role in node.visible_roles for role in user_roles):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权访问该节点"
        )
    
    return {"success": True, "data": node.to_dict()}


@router.post("/nodes")
async def create_node(
    request: CreateNodeRequest,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    """
    创建新节点（需要管理员权限）
    """
    node = BusinessTreeService.create_node(
        db,
        parent_id=request.parent_id,
        name=request.name,
        user_id=current_user.id,
        visible_roles=request.visible_roles
    )
    
    return {"success": True, "data": node.to_dict()}


@router.put("/nodes/{node_id}")
async def update_node(
    node_id: int,
    request: UpdateNodeRequest,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    """
    更新节点信息（需要管理员权限）
    """
    node = BusinessTreeService.update_node(
        db,
        node_id=node_id,
        name=request.name,
        visible_roles=request.visible_roles,
        user_id=current_user.id
    )
    
    return {"success": True, "data": node.to_dict()}


@router.delete("/nodes/{node_id}")
async def delete_node(
    node_id: int,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    """
    删除节点（需要管理员权限）
    """
    success = BusinessTreeService.delete_node(db, node_id)
    return {"success": success, "message": "节点已删除"}


@router.post("/nodes/{node_id}/move")
async def move_node(
    node_id: int,
    request: MoveNodeRequest,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    """
    移动节点（需要管理员权限）
    """
    node = BusinessTreeService.move_node(
        db,
        node_id=node_id,
        new_parent_id=request.new_parent_id,
        user_id=current_user.id
    )
    
    return {"success": True, "data": node.to_dict()}


@router.get("/nodes/{node_id}/sources")
async def get_node_sources(
    node_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    获取节点绑定的视频源
    """
    # 检查节点权限
    node = BusinessTreeService.get_node_by_id(db, node_id)
    user_roles = [current_user.role] if current_user.role else []
    if not any(role in node.visible_roles for role in user_roles):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权访问该节点"
        )
    
    sources = BusinessTreeService.get_node_sources(db, node_id)
    return {"success": True, "data": sources}


@router.post("/nodes/{node_id}/bind")
async def bind_sources(
    node_id: int,
    request: BindSourcesRequest,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    """
    绑定视频源到节点（需要管理员权限）
    """
    mappings = BusinessTreeService.bind_sources(
        db,
        node_id=node_id,
        sources=request.sources
    )
    
    return {
        "success": True,
        "data": [mapping.to_dict() for mapping in mappings],
        "message": f"成功绑定 {len(mappings)} 个视频源"
    }


@router.delete("/nodes/{node_id}/unbind")
async def unbind_sources(
    node_id: int,
    request: UnbindSourcesRequest,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    """
    解绑视频源（需要管理员权限）
    """
    success = BusinessTreeService.unbind_sources(
        db,
        node_id=node_id,
        mapping_ids=request.mapping_ids
    )
    
    return {
        "success": success,
        "message": f"成功解绑 {len(request.mapping_ids)} 个视频源"
    }


@router.post("/nodes/{node_id}/sync")
async def sync_source_status(
    node_id: int,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    """
    同步视频源状态（需要管理员权限）
    """
    device_service = DeviceService()
    updated_mappings = BusinessTreeService.sync_source_status(
        db,
        node_id=node_id,
        device_service=device_service
    )
    
    return {
        "success": True,
        "data": updated_mappings,
        "message": f"已同步 {len(updated_mappings)} 个视频源状态"
    }


@router.post("/batch-save")
async def batch_save_changes(
    request: BatchSaveRequest,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    """
    批量保存所有更改（需要管理员权限）
    """
    result = BusinessTreeService.batch_save_changes(
        db,
        changes=request.dict(),
        user_id=current_user.id
    )
    
    return {
        "success": True,
        "data": result,
        "message": "批量保存成功"
    }


@router.get("/validate")
async def validate_tree(
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    """
    验证树结构合法性（需要管理员权限）
    """
    # 调用业务服务进行树结构验证
    validation_result = BusinessTreeService.validate_tree_structure(db)
    
    return {
        "success": True,
        "valid": validation_result["valid"],
        "message": validation_result["message"],
        "errors": validation_result.get("errors", [])
    }