"""
AI算法管理平台 - FastAPI应用入口

主要功能：
- 统一管理AI边缘设备算法应用
- 业务树形结构管理
- 用户认证与权限控制
- 设备状态监控与API聚合
"""
import logging
import logging.handlers
import os
import sys
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.database import create_tables, SessionLocal
from app.services.user_service import get_or_create_default_admin
from app.api import auth, business, devices, videos, business_tree

# --- 日志配置 ---
# 日志文件将保存在 backend/logs/app.log
# 注意：我们假设服务是从 backend 目录启动的。
# 如果从根目录启动，路径需要调整为 'backend/logs'
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_file_path = os.path.join(log_dir, "app.log")

# 移除所有现有的处理器，以避免重复日志
# 这对于 uvicorn 的 reload=True 模式很重要，可以防止日志重复输出
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# 设置全局日志级别
log_level = logging.DEBUG if settings.DEBUG else logging.INFO

# 1. 配置日志记录到文件（支持轮转）
#    - maxBytes=10*1024*1024: 每个日志文件最大10MB
#    - backupCount=5: 保留最近5个日志文件
file_handler = logging.handlers.RotatingFileHandler(
    log_file_path, maxBytes=10*1024*1024, backupCount=5, encoding='utf-8'
)
file_handler.setLevel(log_level)

# 2. 配置日志记录到控制台
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(log_level)

# 定义所有处理器的统一日志格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 将配置好的处理器添加到根日志记录器
# 注意：不再使用 basicConfig 的 stream 参数，而是使用 handlers
logging.basicConfig(
    level=log_level,
    handlers=[file_handler, stream_handler]
)

logger = logging.getLogger(__name__)
# ---

@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时创建数据库表
    create_tables()
    # 检查并创建默认管理员
    db = SessionLocal()
    try:
        get_or_create_default_admin(db)
    finally:
        db.close()
    yield
    # 关闭时的清理工作（如果需要）


# 创建FastAPI应用实例
app = FastAPI(
    title="AI算法管理平台 API",
    description="统一管理AI边缘设备算法应用的企业级管理平台API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# 配置CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Vue开发服务器
        "http://127.0.0.1:3000",
        "http://localhost:5173",  # Vite开发服务器
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 全局异常处理器
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail,
            "data": None
        }
    )


# @app.exception_handler(Exception)
# async def general_exception_handler(request, exc):
#     # 对于一般异常，记录更详细的错误信息
#     logger.exception("An unexpected error occurred:")
#     return JSONResponse(
#         status_code=500,
#         content={
#             "success": False,
#             "message": f"内部服务器错误: {str(exc)}",
#             "data": None
#         }
#     )


# 注册路由
app.include_router(auth.router, prefix="/api/auth", tags=["认证"])
app.include_router(business.router, prefix="/api/business", tags=["业务管理"])
app.include_router(devices.router, prefix="/api/devices", tags=["设备管理"])
app.include_router(videos.router, prefix="/api/videos", tags=["视频源管理"])
app.include_router(business_tree.router, prefix="/api/business-tree", tags=["业务树管理"])


@app.get("/", summary="根路径")
async def root():
    """API根路径，返回系统信息"""
    return {
        "success": True,
        "message": "AI算法管理平台 API",
        "data": {
            "version": "1.0.0",
            "docs": "/docs",
            "status": "running"
        }
    }


@app.get("/health", summary="健康检查")
async def health_check():
    """健康检查接口"""
    return {
        "success": True,
        "message": "系统运行正常",
        "data": {
            "status": "healthy",
            "timestamp": "2024-01-01T00:00:00Z"
        }
    }


if __name__ == "__main__":
    # uvicorn的log_level会覆盖basicConfig的设置，所以我们在这里统一
    uvicorn_log_level = "debug" if settings.DEBUG else "info"
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level=uvicorn_log_level
    )