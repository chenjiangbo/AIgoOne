"""
设备相关的Pydantic模式

定义设备管理相关的数据结构
"""

from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import datetime


class DeviceBase(BaseModel):
    """设备基础模式"""
    name: Optional[str] = None
    device_type: Optional[str] = None
    api_base_url: str
    business_node_id: Optional[str] = None


class DeviceCreate(BaseModel):
    """设备创建模式"""
    api_base_url: str
    username: str
    password: str


class DeviceUpdate(BaseModel):
    """设备更新模式"""
    name: Optional[str] = None
    device_type: Optional[str] = None
    api_base_url: Optional[str] = None
    business_node_id: Optional[str] = None
    status: Optional[str] = None


class DeviceResponse(DeviceBase):
    """设备响应模式"""
    id: int
    status: str
    device_sn: Optional[str] = None
    version: Optional[str] = None
    register_status: Optional[str] = None
    system_update: Optional[str] = None
    system_time: Optional[str] = None
    network_setting: Optional[str] = None
    last_sync_at: Optional[datetime] = None
    last_heartbeat: Optional[datetime] = None
    sync_error: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class DeviceListResponse(BaseModel):
    """设备列表响应模式"""
    items: List[DeviceResponse]
    total: int
    page: int = 1
    page_size: int = 50


class DeviceSync(BaseModel):
    """设备同步模式"""
    device_ids: List[int]


class DeviceBatchImport(BaseModel):
    """批量导入设备模式"""
    devices: List[DeviceCreate]


class DeviceImportResult(BaseModel):
    """设备导入结果"""
    row: int
    success: bool
    message: str
    device_id: Optional[int] = None


class DeviceBatchImportResponse(BaseModel):
    """批量导入响应模式"""
    success: bool
    message: str
    success_count: int
    failure_count: int
    results: List[DeviceImportResult]
    failures: List[dict] = []


class DeviceSyncResult(BaseModel):
    """设备同步结果"""
    device_id: int
    success: bool
    message: str
    data: Optional[dict] = None


class DeviceBatchSyncResponse(BaseModel):
    """批量同步响应模式"""
    success: bool
    message: str
    results: List[DeviceSyncResult]
    success_count: int
    failure_count: int


class DeviceStats(BaseModel):
    """设备统计模式"""
    total: int
    online: int
    offline: int
    error: int
    unknown: int


# 设备API相关模式（调用外部设备时使用）
class DeviceLoginRequest(BaseModel):
    """设备登录请求"""
    username: str
    password: str


class DeviceLoginResponse(BaseModel):
    """设备登录响应"""
    token: str
    user: dict


class DeviceInfoResponse(BaseModel):
    """设备信息响应"""
    device_name: Optional[str] = None
    device_type: Optional[str] = None
    device_sn: Optional[str] = None
    software_version: Optional[str] = None
    register_status: Optional[str] = None
    system_update: Optional[str] = None
    system_time: Optional[str] = None
    network_setting: Optional[str] = None