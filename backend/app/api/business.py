"""
业务管理API

处理业务树结构的增删改查
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.core.security import get_current_user_id
from app.models.business import BusinessNode

router = APIRouter()


@router.get("/tree", summary="获取业务树")
async def get_business_tree(
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """获取完整的业务树结构"""
    # TODO: 实现业务树查询逻辑
    return {
        "success": True,
        "message": "获取业务树成功",
        "data": []
    }


@router.post("/nodes", summary="创建业务节点")
async def create_business_node(
    # node_data: BusinessNodeCreate,
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """创建新的业务节点"""
    # TODO: 实现节点创建逻辑
    return {
        "success": True,
        "message": "节点创建成功",
        "data": None
    }