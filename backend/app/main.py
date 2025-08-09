from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import engine, Base
from app.models import user, device, business_tree
from app.api import auth, business_tree as business_tree_api

# 创建数据库表并初始化数据
from app.core.database import create_tables
create_tables()

# 创建默认用户
def create_default_user():
    from app.core.database import SessionLocal
    from app.models.user import User
    from app.core.security import get_password_hash
    
    db = SessionLocal()
    try:
        # 检查是否已存在用户
        existing_user = db.query(User).filter(User.username == "admin").first()
        if not existing_user:
            # 创建默认管理员用户
            default_user = User(
                username="admin",
                email="admin@example.com",
                hashed_password=get_password_hash("admin123"),
                full_name="系统管理员",
                is_active=True,
                is_superuser=True,
                role="admin",
                description="默认管理员账户"
            )
            db.add(default_user)
            db.commit()
            print("默认用户创建成功：用户名=admin, 密码=admin123")
        else:
            # 更新现有用户的角色为admin（修复数据）
            if existing_user.role != "admin":
                existing_user.role = "admin"
                existing_user.is_superuser = True
                db.commit()
                print("已更新现有管理员用户的角色为admin")
    finally:
        db.close()

create_default_user()

# 创建 FastAPI 应用
app = FastAPI(
    title="AIgoOne 算法管理平台",
    description="AI算法管理平台后端API",
    version="1.0.0"
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该限制具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(auth.router, prefix="/api/auth", tags=["认证"])
app.include_router(business_tree_api.router, prefix="/api/business-tree", tags=["业务树管理"])

@app.get("/")
async def root():
    return {"message": "AIgoOne 算法管理平台 API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/debug/tree-nodes")
async def debug_tree_nodes():
    """调试接口：检查数据库中的业务树节点"""
    from app.core.database import SessionLocal
    from app.models.business_tree import BusinessTreeNode
    
    db = SessionLocal()
    try:
        nodes = db.query(BusinessTreeNode).all()
        return {
            "total_nodes": len(nodes),
            "nodes": [
                {
                    "id": node.id,
                    "name": node.name,
                    "parent_id": node.parent_id,
                    "depth": node.depth,
                    "visible_roles": node.visible_roles
                }
                for node in nodes
            ]
        }
    finally:
        db.close()

@app.get("/debug/business-tree-raw")
async def debug_business_tree_raw():
    """调试接口：直接测试业务树服务"""
    from app.core.database import SessionLocal
    from app.services.business_tree_service import BusinessTreeService
    
    db = SessionLocal()
    try:
        # 使用admin角色测试
        user_roles = ["admin"]
        tree = BusinessTreeService.get_tree(db, user_roles)
        return {
            "user_roles": user_roles,
            "tree_data": tree
        }
    except Exception as e:
        import traceback
        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }
    finally:
        db.close()

@app.get("/debug/admin-user")
async def debug_admin_user():
    """调试接口：检查admin用户信息"""
    from app.core.database import SessionLocal
    from app.models.user import User
    
    db = SessionLocal()
    try:
        admin_user = db.query(User).filter(User.username == "admin").first()
        if admin_user:
            return {
                "found": True,
                "id": admin_user.id,
                "username": admin_user.username,
                "role": admin_user.role,
                "is_superuser": admin_user.is_superuser,
                "is_active": admin_user.is_active,
                "created_at": admin_user.created_at
            }
        else:
            return {"found": False, "message": "admin用户不存在"}
    finally:
        db.close()

# 临时测试接口 - 不需要身份验证
@app.get("/test-tree")
async def get_business_tree_test():
    """临时测试接口，返回模拟的业务树数据，不需要身份验证"""
    return {
        "success": True,
        "data": {
            "id": 1,
            "name": "根节点",
            "parent_id": None,
            "depth": 0,
            "is_leaf": False,
            "path": "/",
            "visible_roles": [],
            "source_count": 0,
            "children": [
                {
                    "id": 2,
                    "name": "华东区域",
                    "parent_id": 1,
                    "depth": 1,
                    "is_leaf": False,
                    "path": "/华东区域",
                    "visible_roles": [],
                    "source_count": 0,
                    "children": [
                        {
                            "id": 3,
                            "name": "上海分公司",
                            "parent_id": 2,
                            "depth": 2,
                            "is_leaf": True,
                            "path": "/华东区域/上海分公司",
                            "visible_roles": [],
                            "source_count": 5,
                            "children": []
                        }
                    ]
                }
            ]
        }
    }