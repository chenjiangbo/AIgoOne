from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, JSON, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base


class BusinessTreeNode(Base):
    __tablename__ = "business_tree_nodes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    parent_id = Column(Integer, ForeignKey("business_tree_nodes.id", ondelete="CASCADE"))
    depth = Column(Integer, default=0, nullable=False)
    is_leaf = Column(Boolean, default=False, nullable=False)
    path = Column(String(255))
    visible_roles = Column(JSON, default=lambda: ["admin", "operator", "viewer"])
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(Integer, ForeignKey("users.id"))
    updated_by = Column(Integer, ForeignKey("users.id"))
    
    # 关系
    parent = relationship("BusinessTreeNode", remote_side=[id], backref="children")
    creator = relationship("User", foreign_keys=[created_by])
    updater = relationship("User", foreign_keys=[updated_by])
    source_mappings = relationship("NodeSourceMapping", back_populates="node", cascade="all, delete-orphan")
    
    # 约束
    __table_args__ = (
        CheckConstraint('depth <= 5', name='check_depth'),
        UniqueConstraint('parent_id', 'name', name='unique_name_per_parent'),
    )
    
    def to_dict(self, include_children=False):
        data = {
            "id": self.id,
            "name": self.name,
            "parent_id": self.parent_id,
            "depth": self.depth,
            "is_leaf": self.is_leaf,
            "path": self.path,
            "visible_roles": self.visible_roles,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
        if include_children:
            data["children"] = [child.to_dict(include_children=True) for child in self.children]
        return data


class NodeSourceMapping(Base):
    __tablename__ = "node_source_mappings"
    
    id = Column(Integer, primary_key=True, index=True)
    node_id = Column(Integer, ForeignKey("business_tree_nodes.id", ondelete="CASCADE"), nullable=False)
    device_id = Column(Integer, ForeignKey("devices.id", ondelete="CASCADE"), nullable=False)
    source_id = Column(String(255), nullable=False)
    source_type = Column(String(20))  # camera/video
    source_name = Column(String(255))  # 缓存视频源名称
    status = Column(String(20), default="normal")  # normal/invalid
    last_sync_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # 关系
    node = relationship("BusinessTreeNode", back_populates="source_mappings")
    device = relationship("Device", backref="source_mappings")
    
    # 约束
    __table_args__ = (
        UniqueConstraint('node_id', 'device_id', 'source_id', name='unique_source_per_node'),
    )
    
    def to_dict(self):
        return {
            "id": self.id,
            "node_id": self.node_id,
            "device_id": self.device_id,
            "source_id": self.source_id,
            "source_type": self.source_type,
            "source_name": self.source_name,
            "status": self.status,
            "last_sync_at": self.last_sync_at.isoformat() if self.last_sync_at else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "device_name": self.device.name if self.device else None,
            "device_url": self.device.url if self.device else None,
        }