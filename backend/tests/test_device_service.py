
import pytest
import httpx
from unittest.mock import MagicMock, AsyncMock
from sqlalchemy.orm import Session

from app.services.device_service import DeviceService
from app.schemas.device import DeviceCreate
from app.models.device import Device

# 使用pytest的mark来异步运行所有测试
pytestmark = pytest.mark.asyncio

@pytest.fixture
def db_session_mock():
    """模拟数据库会-话"""
    db = MagicMock(spec=Session)
    db.query.return_value.filter.return_value.first.return_value = None
    return db

@pytest.fixture
def device_service(db_session_mock):
    """创建DeviceService实例"""
    return DeviceService(db=db_session_mock)


async def test_create_device_and_sync_happy_path(device_service, db_session_mock, respx_mock):
    """测试创建设备并首次成功同步的完整流程"""

    # 1. 准备测试数据
    device_create_data = DeviceCreate(
        api_base_url="http://test-device.com",
        business_node_id="node-123",
        username="admin",
        password="password123"
    )

    # 2. 模拟外部API的响应
    # 模拟登录成功
    respx_mock.post("http://test-device.com/api/inflet/v1/login").mock(
        return_value=httpx.Response(
            200,
            json={"token": "fake-permanent-token"}
        )
    )
    # 模拟获取设备信息成功
    respx_mock.get("http://test-device.com/api/inflet/v1/device/info").mock(
        return_value=httpx.Response(
            200,
            json={
                "device_sn": "test-sn-123",
                "software_version": "v1.1.0",
                "name": "Test Device 1"
            }
        )
    )

    # 3. 模拟数据库行为
    # 创建时，模拟设备在数据库中不存在
    db_session_mock.query.return_value.filter.return_value.first.return_value = None
    
    # 当调用sync_device_info时，让查询返回我们正在处理的设备
    def- query_side_effect(*args, **kwargs):
        # 模拟Device模型
        new_device = Device(
            id=1,
            api_base_url=device_create_data.api_base_url,
            auth_username=device_create_data.username,
            auth_password_hash="hashed_password", # 假设已被哈希
            status="unknown",
            is_deleted=False
        )
        new_device.raw_password = device_create_data.password # 模拟附加的原始密码
        return new_device

    db_session_mock.query.return_value.filter.return_value.first.side_effect = query_side_effect

    # 4. 执行被测试的函数
    created_device_response = await device_service.create_device(device_create_data)


    # 5. 断言结果
    # 检查返回的设备信息是否正确
    assert created_device_response is not None
    assert created_device_response.api_base_url == "http://test-device.com"
    assert created_device_response.status == "online" # 同步后状态应为online
    assert created_device_response.device_sn == "test-sn-123"
    assert created_device_response.version == "v1.1.0"
    assert created_device_response.name == "Test Device 1"
    # 验证token是否被存储和返回
    assert created_device_response.auth_token == "fake-permanent-token"

    # 验证数据库交互
    db_session_mock.add.assert_called_once() # 验证设备被添加到会话中
    assert db_session_mock.commit.call_count >= 2 # 创建和同步至少调用两次commit


async def test_sync_with_existing_token(device_service, db_session_mock, respx_mock):
    """测试当设备已有Token时，直接使用Token进行同步，不再执行登录"""
    
    # 1. 准备一个已存在token的设备
    existing_device = Device(
        id=2,
        api_base_url="http://existing-device.com",
        auth_username="user",
        auth_password_hash="hashed_password",
        auth_token="existing-permanent-token", # 已存在的Token
        status="online",
        is_deleted=False
    )
    
    # 2. 模拟数据库查询返回这个设备
    db_session_mock.query.return_value.filter.return_value.first.return_value = existing_device

    # 3. 模拟获取设备信息的API
    get_info_mock = respx_mock.get("http://existing-device.com/api/inflet/v1/device/info").mock(
        return_value=httpx.Response(200, json={"name": "Updated Name"})
    )
    # 这个测试不应该T触发登录，所以我们不模拟登录接口。
    # 如果测试代码尝试调用登录接口，respx会抛出错误，从而使测试失败。

    # 4. 执行同步
    sync_result = await device_service.sync_device_info(device_id=2)

    # 5. 断言
    assert sync_result.success is True
    assert sync_result.message == "同步成功"
    assert sync_result.data["name"] == "Updated Name"

    # 确认获取设备信息的接口被调用
    assert get_info_mock.called

    # 确认数据库中的设备信息被更新
    assert existing_device.name == "Updated Name"
    db_session_mock.commit.assert_called() # 验证有数据被提交到数据库
