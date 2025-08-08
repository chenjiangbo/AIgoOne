# AI算法管理平台 - 后端API

基于FastAPI + SQLite的后端服务，提供统一的设备管理和API聚合功能。

## 🚀 快速开始

### 1. 激活虚拟环境

```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 初始化数据库

```bash
python init_db.py
```

### 4. 启动开发服务器

```bash
python main.py
```

或者使用uvicorn：

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## 📚 API文档

启动服务器后访问：

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🔐 默认账户

- 用户名: `admin`
- 密码: `admin123`

## 🏗️ 项目结构

```
backend/
├── app/
│   ├── api/              # API路由
│   │   ├── auth.py       # 认证API
│   │   ├── business.py   # 业务管理API  
│   │   ├── devices.py    # 设备管理API
│   │   └── videos.py     # 视频源API
│   ├── core/             # 核心配置
│   │   ├── config.py     # 应用配置
│   │   ├── database.py   # 数据库配置
│   │   └── security.py   # 安全认证
│   ├── models/           # 数据模型
│   │   ├── user.py       # 用户模型
│   │   ├── business.py   # 业务模型
│   │   └── device.py     # 设备模型
│   └── schemas/          # Pydantic模式
│       └── auth.py       # 认证模式
├── tests/                # 测试文件
├── main.py              # 应用入口
├── init_db.py           # 数据库初始化
└── requirements.txt     # 依赖清单
```

## 🔧 技术栈

- **框架**: FastAPI 0.104.1
- **数据库**: SQLite + SQLAlchemy
- **认证**: JWT Token
- **服务器**: Uvicorn
- **数据验证**: Pydantic

## 🌐 API 概览

### 认证相关
- `POST /api/auth/login` - 用户登录
- `POST /api/auth/register` - 用户注册  
- `GET /api/auth/me` - 获取当前用户信息
- `POST /api/auth/logout` - 用户登出

### 业务管理
- `GET /api/business/tree` - 获取业务树
- `POST /api/business/nodes` - 创建业务节点

### 设备管理
- `GET /api/devices/` - 获取设备列表
- `GET /api/devices/status` - 设备状态监控

### 视频源管理  
- `GET /api/videos/` - 获取视频源列表
- `POST /api/videos/` - 添加视频源

## 📝 开发说明

### 环境配置

复制 `.env.example` 为 `.env` 并修改相应配置：

```bash
cp .env.example .env
```

### 数据库迁移

暂时使用SQLAlchemy自动创建表，后续可集成Alembic进行版本管理。

### API开发规范

1. 所有API返回格式统一：
```json
{
  "success": true,
  "message": "操作成功",
  "data": {}
}
```

2. 错误处理统一通过FastAPI的异常处理机制

3. 认证Required的接口需要使用 `Depends(get_current_user_id)`