"""
设备管理API

处理设备的增删改查和状态监控
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List

from app.core.database import get_db
from app.core.security import get_current_user_id
from app.services.device_service import get_device_service
from app.schemas.device import (
    DeviceCreate, DeviceUpdate, DeviceResponse, DeviceListResponse,
    DeviceBatchSyncResponse, DeviceStats, DeviceSync,
    DeviceBatchImport, DeviceBatchImportResponse
)

router = APIRouter()


@router.get("/", response_model=DeviceListResponse, summary="获取设备列表")
async def get_devices(
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(50, ge=1, le=200, description="每页数量"),
    status: Optional[str] = Query(None, description="状态筛选"),
    device_type: Optional[str] = Query(None, description="设备类型筛选"),
    search: Optional[str] = Query(None, description="搜索关键词"),
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """获取设备列表"""
    device_service = get_device_service(db)
    
    skip = (page - 1) * page_size
    result = device_service.get_devices(
        skip=skip,
        limit=page_size,
        status_filter=status,
        type_filter=device_type,
        search=search
    )
    
    return DeviceListResponse(**result)


@router.post("/", response_model=DeviceResponse, summary="添加设备")
async def create_device(
    device_data: DeviceCreate,
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """添加新设备"""
    device_service = get_device_service(db)
    
    try:
        device = await device_service.create_device(device_data)
        return device
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"创建设备失败: {str(e)}")


@router.get("/{device_id}", response_model=DeviceResponse, summary="获取设备详情")
async def get_device(
    device_id: int,
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """获取设备详情"""
    device_service = get_device_service(db)
    device = device_service.get_device(device_id)
    
    if not device:
        raise HTTPException(status_code=404, detail="设备不存在")
    
    return device


@router.put("/{device_id}", response_model=DeviceResponse, summary="更新设备")
async def update_device(
    device_id: int,
    device_data: DeviceCreate,  # 重用DeviceCreate模式，包含认证信息
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """更新设备信息"""
    device_service = get_device_service(db)
    
    try:
        device = await device_service.update_device(device_id, device_data)
        if not device:
            raise HTTPException(status_code=404, detail="设备不存在")
        return device
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新设备失败: {str(e)}")


@router.delete("/{device_id}", summary="删除设备")
async def delete_device(
    device_id: int,
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """删除设备"""
    device_service = get_device_service(db)
    success = device_service.delete_device(device_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="设备不存在")
    
    return {
        "success": True,
        "message": "设备删除成功"
    }


@router.post("/{device_id}/sync", summary="同步设备信息")
async def sync_device(
    device_id: int,
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """同步单个设备信息"""
    device_service = get_device_service(db)
    result = await device_service.sync_device_info(device_id)
    
    return {
        "success": result.success,
        "message": result.message,
        "data": result.data
    }


@router.post("/batch-sync", response_model=DeviceBatchSyncResponse, summary="批量同步设备")
async def batch_sync_devices(
    sync_data: DeviceSync,
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """批量同步设备信息"""
    device_service = get_device_service(db)
    result = await device_service.batch_sync_devices(sync_data.device_ids)
    
    return result


@router.post("/batch-import", response_model=DeviceBatchImportResponse, summary="批量导入设备")
async def batch_import_devices(
    import_data: DeviceBatchImport,
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """批量导入设备，不检测连通性，标记为离线"""
    device_service = get_device_service(db)
    result = await device_service.batch_import_devices(import_data.devices)
    
    return result


@router.delete("/batch-delete", summary="批量删除设备")
async def batch_delete_devices(
    sync_data: DeviceSync,  # 重用DeviceSync结构，包含device_ids
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """批量删除设备"""
    device_service = get_device_service(db)
    result = device_service.batch_delete_devices(sync_data.device_ids)
    
    return {
        "success": result["success"],
        "message": result["message"],
        "deleted_count": result.get("deleted_count", 0),
        "failed_count": result.get("failed_count", 0)
    }


@router.get("/stats/overview", response_model=DeviceStats, summary="设备统计")
async def get_device_stats(
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """获取设备统计信息"""
    device_service = get_device_service(db)
    stats = device_service.get_device_stats()
    
    return stats


@router.get("/{device_id}/sources", summary="获取设备视频源")
async def get_device_sources(
    device_id: int,
    source_type: Optional[str] = None,
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """
    获取设备的视频源列表
    
    参数:
    - device_id: 设备ID
    - source_type: 视频源类型 (camera/video)，可选
    """
    device_service = get_device_service(db)
    
    try:
        sources = await device_service.get_device_sources(device_id, source_type)
        return {
            "success": True,
            "data": sources,
            "total": len(sources)
        }
    except ValueError as e:
        return {
            "success": False,
            "message": str(e),
            "data": []
        }