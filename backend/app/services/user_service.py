"""
用户服务
"""

from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import get_password_hash
from app.core.config import settings

def get_or_create_default_admin(db: Session):
    """检查并创建默认管理员用户"""
    admin_user = db.query(User).filter(User.username == settings.DEFAULT_ADMIN_USERNAME).first()
    if not admin_user:
        hashed_password = get_password_hash(settings.DEFAULT_ADMIN_PASSWORD)
        new_admin = User(
            username=settings.DEFAULT_ADMIN_USERNAME,
            hashed_password=hashed_password,
            is_superuser=True
        )
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
        return new_admin
    return admin_user
