"""
用户模型

定义用户表结构和相关操作
"""

from sqlalchemy import Column, String, Boolean, Text
from sqlalchemy.orm import relationship

from app.core.database import BaseModel


class User(BaseModel):
    """用户模型
    
    字段说明：
    - username: 用户名，唯一
    - email: 邮箱，可选
    - hashed_password: 加密后的密码
    - full_name: 真实姓名
    - is_active: 是否激活
    - is_superuser: 是否超级管理员
    - role: 用户角色
    - description: 用户描述
    """
    
    __tablename__ = "users"
    
    username = Column(String(50), unique=True, index=True, nullable=False, comment="用户名")
    email = Column(String(100), unique=True, index=True, nullable=True, comment="邮箱")
    hashed_password = Column(String(255), nullable=False, comment="加密密码")
    full_name = Column(String(100), nullable=True, comment="真实姓名")
    is_active = Column(Boolean, default=True, comment="是否激活")
    is_superuser = Column(Boolean, default=False, comment="是否超级管理员")
    role = Column(String(50), default="user", comment="用户角色")  # user, admin, operator
    description = Column(Text, nullable=True, comment="用户描述")
    
    def __str__(self):
        return f"User(id={self.id}, username='{self.username}')"
    
    def __repr__(self):
        return self.__str__()