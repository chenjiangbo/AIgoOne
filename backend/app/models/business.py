"""
业务模型

定义业务树结构相关的表模型
"""

from sqlalchemy import Column, String, Integer, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship

from app.core.database import BaseModel


class BusinessNode(BaseModel):
    """业务节点模型
    
    用于构建业务树形结构，支持无限层级
    
    字段说明：
    - name: 节点名称
    - type: 节点类型 (company, district, group, parking等)
    - parent_id: 父节点ID
    - sort_order: 排序顺序
    - is_leaf: 是否叶子节点
    - device_count: 设备数量
    - description: 描述信息
    - config: 配置信息（JSON格式存储）
    """
    
    __tablename__ = "business_nodes"
    
    name = Column(String(100), nullable=False, comment="节点名称")
    type = Column(String(50), nullable=False, comment="节点类型")
    parent_id = Column(Integer, ForeignKey("business_nodes.id"), nullable=True, comment="父节点ID")
    sort_order = Column(Integer, default=0, comment="排序顺序")
    is_leaf = Column(Boolean, default=False, comment="是否叶子节点")
    device_count = Column(Integer, default=0, comment="设备数量")
    description = Column(Text, nullable=True, comment="描述信息")
    config = Column(Text, nullable=True, comment="配置信息JSON")
    
    # 建立自关联关系
    parent = relationship("BusinessNode", remote_side="BusinessNode.id", backref="children")
    
    def __str__(self):
        return f"BusinessNode(id={self.id}, name='{self.name}', type='{self.type}')"
    
    def __repr__(self):
        return self.__str__()
    
    def to_tree_dict(self):
        """转换为前端树形结构格式"""
        return {
            "id": str(self.id),
            "name": self.name,
            "type": self.type,
            "isLeaf": self.is_leaf,
            "deviceCount": self.device_count,
            "description": self.description,
            "children": [] if self.is_leaf else None
        }