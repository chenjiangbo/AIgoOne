"""
设备模型

定义设备和视频源相关的表模型
"""

from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.core.database import BaseModel


class Device(BaseModel):
    """设备模型"""
    
    __tablename__ = "devices"
    
    name = Column(String(100), nullable=True, comment="设备名称")
    device_type = Column(String(50), nullable=True, comment="设备类型")
    api_base_url = Column(String(255), nullable=False, comment="API基础URL")
    status = Column(String(20), nullable=False, default="unknown", comment="设备状态")
    business_node_id = Column(String(50), nullable=True, comment="业务节点ID")
    device_sn = Column(String(100), nullable=True, comment="设备序列号")
    version = Column(Text, nullable=True, comment="软件版本详情")
    register_status = Column(String(50), nullable=True, comment="注册状态")
    system_update = Column(String(100), nullable=True, comment="系统更新信息")
    system_time = Column(String(100), nullable=True, comment="系统时间")
    network_setting = Column(Text, nullable=True, comment="网络设置")
    auth_token = Column(Text, nullable=True, comment="设备认证Token")
    auth_username = Column(String(100), nullable=True, comment="认证用户名")
    auth_password_hash = Column(String(255), nullable=True, comment="认证密码哈希")
    last_sync_at = Column(DateTime, nullable=True, comment="最后同步时间")
    last_heartbeat = Column(DateTime, nullable=True, comment="最后心跳时间")
    sync_error = Column(Text, nullable=True, comment="同步错误信息")
    
    def __str__(self):
        return f"Device(id={self.id}, name='{self.name}', status='{self.status}')"
    
    def __repr__(self):
        return self.__str__()


class VideoSource(BaseModel):
    """视频源模型"""
    
    __tablename__ = "video_sources"
    
    name = Column(String(100), nullable=False, comment="视频源名称")
    source_type = Column(String(20), nullable=False, comment="类型")
    url = Column(String(500), nullable=False, comment="视频源地址")
    device_id = Column(Integer, ForeignKey("devices.id"), nullable=True, comment="关联设备ID")
    business_node_id = Column(Integer, ForeignKey("business_nodes.id"), nullable=False, comment="业务节点ID")
    status = Column(String(20), nullable=False, default="unknown", comment="状态")
    resolution = Column(String(20), nullable=True, comment="分辨率")
    thumbnail_url = Column(String(500), nullable=True, comment="缩略图地址")
    description = Column(Text, nullable=True, comment="描述信息")
    config = Column(Text, nullable=True, comment="配置信息JSON")
    
    device = relationship("Device", backref="video_sources")
    business_node = relationship("BusinessNode", backref="video_sources")
    
    def __str__(self):
        return f"VideoSource(id={self.id}, name='{self.name}', type='{self.source_type}')"
    
    def __repr__(self):
        return self.__str__()