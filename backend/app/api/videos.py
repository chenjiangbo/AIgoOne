"""
视频源管理API

处理视频流和视频文件的管理
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user_id

router = APIRouter()


@router.get("/", summary="获取视频源列表")
async def get_video_sources(
    source_type: str = "stream",
    business_node_id: int = None,
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """获取视频源列表"""
    # TODO: 实现视频源列表查询
    return {
        "success": True,
        "message": "获取视频源成功",
        "data": []
    }


@router.post("/", summary="添加视频源")
async def create_video_source(
    # source_data: VideoSourceCreate,
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """添加新的视频源"""
    # TODO: 实现视频源创建
    return {
        "success": True,
        "message": "视频源添加成功",
        "data": None
    }