"""
安全相关功能

包含JWT token生成/验证、密码加密等安全功能
"""

from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from .config import settings

# 密码加密上下文
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT认证scheme
security = HTTPBearer()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """生成密码哈希"""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """创建JWT access token
    
    Args:
        data: 要编码的数据，通常包含用户ID、用户名等
        expires_delta: 过期时间，如果不提供则使用配置中的默认值
        
    Returns:
        JWT token字符串
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    """验证JWT token
    
    Args:
        credentials: HTTP Authorization credentials
        
    Returns:
        解码后的token数据
        
    Raises:
        HTTPException: token无效时抛出401异常
    """
    token = credentials.credentials
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="无效的认证令牌",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_user_id(token_data: dict = Security(verify_token)) -> int:
    """从token中获取当前用户ID
    
    Args:
        token_data: 解码后的token数据
        
    Returns:
        用户ID
        
    Raises:
        HTTPException: token中没有用户信息时抛出401异常
    """
    user_id = token_data.get("sub")
    if user_id is None:
        raise HTTPException(status_code=401, detail="无效的认证令牌")
    
    try:
        return int(user_id)
    except ValueError:
        raise HTTPException(status_code=401, detail="无效的用户信息")


def get_current_user(token_data: dict = Security(verify_token)):
    """获取当前用户对象
    
    这是一个FastAPI依赖函数，用于从JWT token中提取用户信息并返回用户对象
    
    Args:
        token_data: 解码后的token数据
        
    Returns:
        User对象，包含roles属性
        
    Raises:
        HTTPException: 用户不存在时抛出401异常
    """
    from app.core.database import SessionLocal
    from app.models.user import User
    
    user_id = token_data.get("sub")
    if user_id is None:
        raise HTTPException(status_code=401, detail="无效的认证令牌")
    
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == int(user_id)).first()
        if not user:
            raise HTTPException(
                status_code=401,
                detail="用户不存在"
            )
        return user
    finally:
        db.close()