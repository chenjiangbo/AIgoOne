"""
认证相关API

处理用户登录、注册、token验证等功能
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app.core.database import get_db
from app.core.security import (
    verify_password, 
    get_password_hash, 
    create_access_token,
    get_current_user_id
)
from app.core.config import settings
from app.models.user import User
from app.schemas.auth import LoginRequest, Token, UserCreate, UserResponse

router = APIRouter()


@router.post("/login", response_model=Token, summary="用户登录")
async def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    """用户登录接口
    
    Args:
        login_data: 包含username和password的JSON数据
        db: 数据库会话
        
    Returns:
        包含access_token和token_type的Token对象
        
    Raises:
        HTTPException: 用户名或密码错误时返回401
    """
    # 查询用户
    user = db.query(User).filter(User.username == login_data.username).first()
    
    # 验证用户和密码
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 检查用户是否激活
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="账户已被禁用",
        )
    
    # 创建访问令牌
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id), "username": user.username},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    }


@router.post("/register", response_model=UserResponse, summary="用户注册")
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """用户注册接口
    
    Args:
        user_data: 用户注册数据
        db: 数据库会话
        
    Returns:
        创建的用户信息
        
    Raises:
        HTTPException: 用户名已存在时返回400
    """
    # 检查用户名是否已存在
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="用户名已存在"
        )
    
    # 检查邮箱是否已存在（如果提供了邮箱）
    if user_data.email:
        existing_email = db.query(User).filter(User.email == user_data.email).first()
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="邮箱已存在"
            )
    
    # 创建新用户
    hashed_password = get_password_hash(user_data.password)
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password,
        full_name=user_data.full_name,
        role=user_data.role or "user"
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.get("/me", response_model=UserResponse, summary="获取当前用户信息")
async def get_current_user_info(
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """获取当前登录用户的信息
    
    Args:
        current_user_id: 当前用户ID（从token中提取）
        db: 数据库会话
        
    Returns:
        当前用户信息
        
    Raises:
        HTTPException: 用户不存在时返回404
    """
    user = db.query(User).filter(User.id == current_user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    return user


@router.post("/logout", summary="用户登出")
async def logout(current_user_id: int = Depends(get_current_user_id)):
    """用户登出接口
    
    注意：JWT是无状态的，实际的登出逻辑需要在前端处理（删除token）
    这个接口主要用于记录日志或清理服务端缓存
    
    Args:
        current_user_id: 当前用户ID
        
    Returns:
        登出成功消息
    """
    # 这里可以添加登出日志记录
    return {"message": "登出成功"}