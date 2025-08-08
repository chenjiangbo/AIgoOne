"""
认证相关的Pydantic模式

定义用户认证、注册等数据结构
"""

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class LoginRequest(BaseModel):
    """登录请求模式"""
    username: str
    password: str


class Token(BaseModel):
    """JWT令牌响应模式"""
    access_token: str
    token_type: str
    expires_in: int


class UserBase(BaseModel):
    """用户基础模式"""
    username: str
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    role: Optional[str] = "user"
    is_active: Optional[bool] = True


class UserCreate(UserBase):
    """用户创建模式"""
    password: str


class UserResponse(UserBase):
    """用户响应模式"""
    id: int
    created_at: datetime
    is_superuser: bool
    
    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    """用户更新模式"""
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None