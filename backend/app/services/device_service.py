"""
设备管理服务

处理设备的增删改查、同步等业务逻辑
"""

import httpx
import json
import logging
from datetime import datetime
from typing import List, Optional, Dict, Any, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.models.device import Device
from app.schemas.device import (
    DeviceCreate, DeviceResponse, DeviceSync,
    DeviceSyncResult, DeviceBatchSyncResponse,
    DeviceLoginRequest, DeviceInfoResponse,
    DeviceStats, DeviceImportResult, DeviceBatchImportResponse
)
from app.core.security import get_password_hash, verify_password

logger = logging.getLogger(__name__)

class _TokenExpiredError(Exception):
    """内部异常，用于触发Token刷新重试流程。"""
    pass

class DeviceService:
    """设备管理服务类"""
    
    def __init__(self, db: Session):
        self.db = db
    
    async def create_device(self, device_data: DeviceCreate) -> DeviceResponse:
        """创建新设备，采用"先验证、后入库"的逻辑"""
        
        # 标准化URL格式：移除尾部斜杠
        normalized_url = device_data.api_base_url.rstrip('/')
        
        # 从URL中提取主机和端口
        from urllib.parse import urlparse
        parsed_url = urlparse(normalized_url)
        host_port = f"{parsed_url.hostname}:{parsed_url.port if parsed_url.port else (443 if parsed_url.scheme == 'https' else 80)}"
        
        # 检查是否已存在相同主机和端口的设备
        all_devices = self.db.query(Device).all()
        for device in all_devices:
            device_parsed = urlparse(device.api_base_url.rstrip('/'))
            device_host_port = f"{device_parsed.hostname}:{device_parsed.port if device_parsed.port else (443 if device_parsed.scheme == 'https' else 80)}"
            if device_host_port == host_port:
                raise ValueError(f"该设备 ({host_port}) 已存在")

        try:
            token, device_info = await self._verify_and_get_info(
                device_data.api_base_url, 
                device_data.username, 
                device_data.password
            )
        except Exception as e:
            logger.error(f"添加设备失败：验证过程中发生错误。错误: {e}")
            raise ValueError(f"无法连接到设备或验证失败: {e}")

        new_device = Device(
            api_base_url=normalized_url,  # 使用标准化的URL
            auth_username=device_data.username,
            auth_password_hash=get_password_hash(device_data.password),
            auth_token=token,
            name=device_info.get("device_name"),
            device_type=device_info.get("device_type"),
            device_sn=device_info.get("device_sn"),
            version=device_info.get("software_version"),
            register_status=device_info.get("register_status"),
            system_update=device_info.get("system_update"),
            system_time=device_info.get("system_time"),
            network_setting=device_info.get("network_setting"),
            status="online",
            last_sync_at=datetime.utcnow()
        )
        
        self.db.add(new_device)
        self.db.commit()
        self.db.refresh(new_device)
        
        return DeviceResponse.from_orm(new_device)

    async def _verify_and_get_info(self, api_base_url: str, username: str, password: str) -> Tuple[str, Dict[str, Any]]:
        """
        在同一个HTTP会话中完成设备登录和信息获取。
        遵循设备独特的认证要求：Authorization头不带'Bearer'前缀。
        """
        async with httpx.AsyncClient(timeout=10.0) as client:
            try:
                login_url = f"{api_base_url.rstrip('/')}/api/inflet/v1/login"
                login_payload = {"username": username, "password": password}
                login_response = await client.post(login_url, json=login_payload)
                login_response.raise_for_status()
                token = login_response.json().get("token")
                if not token:
                    raise Exception("登录响应中不包含Token")
            except Exception as e:
                raise Exception(f"获取设备Token失败: {e}")

            try:
                info_url = f"{api_base_url.rstrip('/')}/api/inflet/v1/device/info"
                info_headers = {"Authorization": token}
                info_response = await client.get(info_url, headers=info_headers)
                info_response.raise_for_status()
                data = info_response.json()
                device_info = {
                    "device_sn": data.get("sn"),
                    "software_version": json.dumps(data.get("version")),
                    "device_name": data.get("name"),
                    "device_type": data.get("type"),
                    "register_status": data.get("register_status"),
                    "system_update": data.get("system_update"),
                    "system_time": data.get("system_time"),
                    "network_setting": json.dumps(data.get("network_setting")),
                }
                return token, device_info
            except Exception as e:
                raise Exception(f"请求设备信息失败: {e}")

    async def update_device(self, device_id: int, device_data: DeviceCreate) -> Optional[DeviceResponse]:
        """更新设备信息"""
        device = self.db.query(Device).filter(Device.id == device_id).first()
        if not device:
            return None
        
        # 标准化URL格式：移除尾部斜杠
        normalized_url = device_data.api_base_url.rstrip('/')
        
        # 从URL中提取主机和端口
        from urllib.parse import urlparse
        parsed_url = urlparse(normalized_url)
        host_port = f"{parsed_url.hostname}:{parsed_url.port if parsed_url.port else (443 if parsed_url.scheme == 'https' else 80)}"
        
        # 检查是否与其他设备冲突（排除当前设备）
        all_devices = self.db.query(Device).filter(Device.id != device_id).all()
        for other_device in all_devices:
            device_parsed = urlparse(other_device.api_base_url.rstrip('/'))
            device_host_port = f"{device_parsed.hostname}:{device_parsed.port if device_parsed.port else (443 if device_parsed.scheme == 'https' else 80)}"
            if device_host_port == host_port:
                raise ValueError(f"该设备 ({host_port}) 已存在")

        try:
            # 验证新的连接信息
            token, device_info = await self._verify_and_get_info(
                device_data.api_base_url, 
                device_data.username, 
                device_data.password
            )
        except Exception as e:
            logger.error(f"更新设备失败：验证过程中发生错误。错误: {e}")
            raise ValueError(f"无法连接到设备或验证失败: {e}")

        # 更新设备信息
        device.api_base_url = normalized_url
        device.auth_username = device_data.username
        device.auth_password_hash = get_password_hash(device_data.password)
        device.auth_token = token
        device.name = device_info.get("device_name")
        device.device_type = device_info.get("device_type")
        device.device_sn = device_info.get("device_sn")
        device.version = device_info.get("software_version")
        device.register_status = device_info.get("register_status")
        device.system_update = device_info.get("system_update")
        device.system_time = device_info.get("system_time")
        device.network_setting = device_info.get("network_setting")
        device.status = "online"
        device.last_sync_at = datetime.utcnow()
        device.sync_error = None
        
        self.db.commit()
        self.db.refresh(device)
        
        return DeviceResponse.from_orm(device)

    def get_devices(
        self, skip: int = 0, limit: int = 100,
        status_filter: Optional[str] = None, type_filter: Optional[str] = None, search: Optional[str] = None
    ) -> Dict[str, Any]:
        query = self.db.query(Device)
        if status_filter:
            query = query.filter(Device.status == status_filter)
        if type_filter:
            query = query.filter(Device.device_type == type_filter)
        if search:
            search_pattern = f"%{search}%"
            query = query.filter(
                (Device.name.ilike(search_pattern)) |
                (Device.api_base_url.ilike(search_pattern)) |
                (Device.device_sn.ilike(search_pattern))
            )
        total = query.count()
        devices = query.order_by(desc(Device.updated_at)).offset(skip).limit(limit).all()
        return {
            "items": [DeviceResponse.from_orm(device) for device in devices],
            "total": total, "page": (skip // limit) + 1, "page_size": limit
        }
    
    def get_device(self, device_id: int) -> Optional[DeviceResponse]:
        device = self.db.query(Device).filter(Device.id == device_id).first()
        return DeviceResponse.from_orm(device) if device else None
    
    def delete_device(self, device_id: int) -> bool:
        device = self.db.query(Device).filter(Device.id == device_id).first()
        if device:
            self.db.delete(device)
            self.db.commit()
            return True
        return False
    
    async def sync_device_info(self, device_id: int) -> DeviceSyncResult:
        device = self.db.query(Device).filter(Device.id == device_id).first()
        if not device:
            return DeviceSyncResult(device_id=device_id, success=False, message="设备不存在")
        
        try:
            # 使用存储的token直接获取设备信息
            async with httpx.AsyncClient(timeout=10.0) as client:
                info_url = f"{device.api_base_url.rstrip('/')}/api/inflet/v1/device/info"
                info_headers = {"Authorization": device.auth_token}
                info_response = await client.get(info_url, headers=info_headers)
                info_response.raise_for_status()
                data = info_response.json()
                
                device_info = {
                    "device_sn": data.get("sn"),
                    "software_version": json.dumps(data.get("version")),
                    "device_name": data.get("name"),
                    "device_type": data.get("type"),
                    "register_status": data.get("register_status"),
                    "system_update": data.get("system_update"),
                    "system_time": data.get("system_time"),
                    "network_setting": json.dumps(data.get("network_setting")),
                }
            
            device.name = device_info.get("device_name") or device.name
            device.device_type = device_info.get("device_type") or device.device_type
            device.device_sn = device_info.get("device_sn")
            device.version = device_info.get("software_version")
            device.status = "online"
            device.last_sync_at = datetime.utcnow()
            device.sync_error = None
            self.db.commit()
            return DeviceSyncResult(device_id=device_id, success=True, message="同步成功", data=device_info)

        except Exception as e:
            logger.warning(f"同步设备 {device.id} 失败: {e}")
            device.status = "error"
            device.sync_error = str(e)
            self.db.commit()
            return DeviceSyncResult(device_id=device.id, success=False, message=str(e))

    async def batch_sync_devices(self, device_ids: List[int]) -> DeviceBatchSyncResponse:
        results = [await self.sync_device_info(device_id) for device_id in device_ids]
        success_count = sum(1 for r in results if r.success)
        return DeviceBatchSyncResponse(
            success_count=success_count, failure_count=len(results) - success_count, results=results
        )
    
    def get_device_stats(self) -> DeviceStats:
        devices = self.db.query(Device).all()
        stats = DeviceStats(total=len(devices), online=0, offline=0, error=0, unknown=0)
        for device in devices:
            if hasattr(stats, device.status):
                setattr(stats, device.status, getattr(stats, device.status) + 1)
        return stats

    async def batch_import_devices(self, devices_data: List[DeviceCreate]) -> DeviceBatchImportResponse:
        """批量导入设备，不检测连通性，全部标记为离线"""
        results = []
        success_count = 0
        failure_count = 0
        failures = []
        
        for index, device_data in enumerate(devices_data, 1):
            try:
                # 标准化URL格式
                normalized_url = device_data.api_base_url.rstrip('/')
                
                # 从URL中提取主机和端口
                from urllib.parse import urlparse
                parsed_url = urlparse(normalized_url)
                host_port = f"{parsed_url.hostname}:{parsed_url.port if parsed_url.port else (443 if parsed_url.scheme == 'https' else 80)}"
                
                # 检查是否已存在相同主机和端口的设备
                all_devices = self.db.query(Device).all()
                for existing_device in all_devices:
                    device_parsed = urlparse(existing_device.api_base_url.rstrip('/'))
                    device_host_port = f"{device_parsed.hostname}:{device_parsed.port if device_parsed.port else (443 if device_parsed.scheme == 'https' else 80)}"
                    if device_host_port == host_port:
                        raise ValueError(f"设备 ({host_port}) 已存在")
                
                # 创建设备记录（不进行连通性检测）
                new_device = Device(
                    api_base_url=normalized_url,
                    auth_username=device_data.username,
                    auth_password_hash=get_password_hash(device_data.password),
                    auth_token=None,  # 导入时不设置token
                    name=None,  # 导入时不设置设备名
                    device_type=None,  # 导入时不设置设备类型
                    device_sn=None,  # 导入时不设置SN
                    version=None,  # 导入时不设置版本信息
                    register_status=None,
                    system_update=None,
                    system_time=None,
                    network_setting=None,
                    status="offline",  # 统一标记为离线
                    last_sync_at=None  # 导入时未同步
                )
                
                self.db.add(new_device)
                self.db.commit()
                self.db.refresh(new_device)
                
                results.append(DeviceImportResult(
                    row=index,
                    success=True,
                    message="导入成功",
                    device_id=new_device.id
                ))
                success_count += 1
                
            except Exception as e:
                logger.warning(f"导入第 {index} 行设备失败: {e}")
                results.append(DeviceImportResult(
                    row=index,
                    success=False,
                    message=str(e)
                ))
                failures.append({
                    "row": index,
                    "error": str(e)
                })
                failure_count += 1
                
                # 回滚当前事务
                self.db.rollback()
        
        success = failure_count == 0
        message = f"导入完成：成功 {success_count} 个，失败 {failure_count} 个"
        
        return DeviceBatchImportResponse(
            success=success,
            message=message,
            success_count=success_count,
            failure_count=failure_count,
            results=results,
            failures=failures
        )

    def batch_delete_devices(self, device_ids: List[int]) -> Dict[str, Any]:
        """批量删除设备"""
        deleted_count = 0
        failed_count = 0
        errors = []
        
        for device_id in device_ids:
            try:
                device = self.db.query(Device).filter(Device.id == device_id).first()
                if device:
                    self.db.delete(device)
                    self.db.commit()
                    deleted_count += 1
                else:
                    errors.append(f"设备 ID {device_id} 不存在")
                    failed_count += 1
            except Exception as e:
                logger.error(f"删除设备 {device_id} 失败: {e}")
                errors.append(f"删除设备 ID {device_id} 失败: {str(e)}")
                failed_count += 1
                self.db.rollback()
        
        success = failed_count == 0
        message = f"批量删除完成：成功删除 {deleted_count} 个设备"
        if failed_count > 0:
            message += f"，失败 {failed_count} 个"
        
        return {
            "success": success,
            "message": message,
            "deleted_count": deleted_count,
            "failed_count": failed_count,
            "errors": errors
        }
    
    async def get_device_sources(self, device_id: int, source_type: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        获取设备的视频源列表
        
        Args:
            device_id: 设备ID
            source_type: 视频源类型 (camera/video)，不指定则获取所有
        
        Returns:
            视频源列表
        """
        device = self.db.query(Device).filter(Device.id == device_id).first()
        if not device:
            raise ValueError(f"设备 ID {device_id} 不存在")
        
        if device.status != "online":
            raise ValueError(f"设备离线，无法获取视频源")
        
        try:
            # 构建请求URL
            url = f"{device.api_base_url}/v1/sources"
            params = {}
            if source_type:
                params["type"] = source_type
            
            # 发送请求
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(
                    url,
                    params=params,
                    headers={
                        "Authorization": f"Bearer {device.auth_token}" if device.auth_token else None
                    }
                )
                
                if response.status_code == 401:
                    # Token过期，尝试重新登录
                    await self._refresh_device_token(device)
                    # 重试请求
                    response = await client.get(
                        url,
                        params=params,
                        headers={
                            "Authorization": f"Bearer {device.auth_token}"
                        }
                    )
                
                response.raise_for_status()
                
                data = response.json()
                sources = data.get("items", [])
                
                # 格式化返回数据
                formatted_sources = []
                for source in sources:
                    formatted_sources.append({
                        "id": source.get("id"),
                        "name": source.get("name"),
                        "type": source.get("type", "camera"),
                        "url": source.get("url"),
                        "status": source.get("status", "normal"),
                        "description": source.get("description", "")
                    })
                
                return formatted_sources
                
        except httpx.HTTPStatusError as e:
            logger.error(f"获取设备 {device_id} 视频源失败: HTTP {e.response.status_code}")
            raise ValueError(f"获取视频源失败: {e.response.text}")
        except Exception as e:
            logger.error(f"获取设备 {device_id} 视频源失败: {e}")
            raise ValueError(f"获取视频源失败: {str(e)}")

def get_device_service(db: Session) -> DeviceService:
    return DeviceService(db)