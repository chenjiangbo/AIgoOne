"""
数据库初始化脚本

创建初始用户和业务数据
"""

from sqlalchemy.orm import Session
from app.core.database import SessionLocal, create_tables
from app.core.security import get_password_hash
from app.models.user import User
from app.models.business import BusinessNode
from app.models.device import Device, VideoSource


def init_database():
    """初始化数据库"""
    print("创建数据库表...")
    create_tables()
    print("数据库表创建完成!")


def create_default_user():
    """创建默认管理员用户"""
    db: Session = SessionLocal()
    
    try:
        # 检查是否已存在管理员用户
        existing_admin = db.query(User).filter(User.username == "admin").first()
        if existing_admin:
            print("管理员用户已存在!")
            return
        
        # 创建默认管理员
        admin_user = User(
            username="admin",
            email="admin@example.com",
            hashed_password=get_password_hash("admin123"),
            full_name="系统管理员",
            is_active=True,
            is_superuser=True,
            role="admin"
        )
        
        db.add(admin_user)
        db.commit()
        print("默认管理员用户创建成功!")
        print("用户名: admin")
        print("密码: admin123")
        
    except Exception as e:
        print(f"创建用户失败: {e}")
        db.rollback()
    finally:
        db.close()


def create_sample_business_tree():
    """创建示例业务树数据"""
    db: Session = SessionLocal()
    
    try:
        # 检查是否已有业务数据
        existing_company = db.query(BusinessNode).filter(BusinessNode.type == "company").first()
        if existing_company:
            print("业务树数据已存在!")
            return
        
        # 创建公司节点
        company = BusinessNode(
            name="RealEasyInfo科技有限公司",
            type="company",
            parent_id=None,
            sort_order=1,
            is_leaf=False,
            device_count=0
        )
        db.add(company)
        db.flush()  # 获取ID
        
        # 创建区域节点
        region1 = BusinessNode(
            name="华东区域",
            type="district",
            parent_id=company.id,
            sort_order=1,
            is_leaf=False,
            device_count=0
        )
        region2 = BusinessNode(
            name="华北区域",
            type="district", 
            parent_id=company.id,
            sort_order=2,
            is_leaf=False,
            device_count=0
        )
        db.add_all([region1, region2])
        db.flush()
        
        # 创建分组节点（华东区域下）
        group1 = BusinessNode(
            name="上海分组",
            type="group",
            parent_id=region1.id,
            sort_order=1,
            is_leaf=False,
            device_count=0
        )
        group2 = BusinessNode(
            name="杭州分组", 
            type="group",
            parent_id=region1.id,
            sort_order=2,
            is_leaf=False,
            device_count=0
        )
        db.add_all([group1, group2])
        db.flush()
        
        # 创建停车场节点（叶子节点）
        parking1 = BusinessNode(
            name="虹桥机场T1停车场",
            type="parking",
            parent_id=group1.id,
            sort_order=1,
            is_leaf=True,
            device_count=12
        )
        parking2 = BusinessNode(
            name="虹桥机场T2停车场",
            type="parking", 
            parent_id=group1.id,
            sort_order=2,
            is_leaf=True,
            device_count=8
        )
        parking3 = BusinessNode(
            name="萧山国际机场停车场",
            type="parking",
            parent_id=group2.id,
            sort_order=1,
            is_leaf=True,
            device_count=16
        )
        parking4 = BusinessNode(
            name="首都机场T3停车场",
            type="parking",
            parent_id=region2.id,
            sort_order=1,
            is_leaf=True,
            device_count=20
        )
        
        db.add_all([parking1, parking2, parking3, parking4])
        db.commit()
        print("示例业务树创建成功!")
        
    except Exception as e:
        print(f"创建业务树失败: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print("开始初始化数据库...")
    init_database()
    create_default_user()
    create_sample_business_tree()
    print("数据库初始化完成!")