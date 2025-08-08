"""
数据库配置和连接管理

使用SQLAlchemy配置SQLite数据库连接
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from .config import settings

# 创建SQLite引擎
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False},  # SQLite特有配置
    echo=settings.DEBUG  # 调试模式下显示SQL语句
)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基础模型类
Base = declarative_base()


def get_db():
    """获取数据库会话

    这个函数将被FastAPI的Depends使用
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    """创建数据库表"""
    Base.metadata.create_all(bind=engine)
    
    # 初始化业务树根节点
    from app.services.business_tree_service import BusinessTreeService
    db = SessionLocal()
    try:
        BusinessTreeService.initialize_root_node(db)
    finally:
        db.close()


# 基础模型类，包含公共字段
class BaseModel(Base):
    """数据库模型基类
    
    包含所有表的公共字段：
    - id: 主键
    - created_at: 创建时间
    - updated_at: 更新时间
    - is_deleted: 软删除标记
    """
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True, comment="主键ID")
    created_at = Column(DateTime, default=datetime.utcnow, comment="创建时间")
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment="更新时间")
    is_deleted = Column(Boolean, default=False, comment="是否删除")
    
    def to_dict(self):
        """转换为字典格式"""
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }