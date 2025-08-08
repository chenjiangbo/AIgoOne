# AIgoOne - AI算法管理平台

## 项目概述

AIgoOne 是一个企业级AI算法管理平台，用于统一管理AI边缘设备算法应用。

## 功能特性

- 🔧 **设备集中管理** - 统一纳管所有边缘计算设备
- 📊 **实时数据监控** - 全方位掌控算法运行状态  
- ⚡ **智能任务调度** - 自动化管理提升运营效率
- 🎯 **业务树管理** - 灵活的业务结构组织
- 🎥 **视频源管理** - 统一管理视频数据源
- 👥 **用户权限控制** - 完善的认证授权体系

## 技术栈

### 前端
- **框架**: Vue 3 + TypeScript
- **UI库**: Ant Design Vue  
- **状态管理**: Pinia
- **构建工具**: Vite

### 后端
- **框架**: FastAPI (Python)
- **数据库**: SQLite + SQLAlchemy
- **认证**: JWT
- **API文档**: Swagger UI

## 项目结构

```
AIgoOne/
├── frontend_ant/          # 新前端项目 (Ant Design Vue)
│   ├── src/
│   │   ├── api/          # API接口
│   │   ├── components/   # 通用组件
│   │   ├── views/        # 页面视图
│   │   ├── router/       # 路由配置
│   │   └── styles/       # 样式文件
│   └── package.json
├── frontend/             # 原前端项目 (Element Plus)
├── backend/              # 后端项目
│   ├── app/
│   │   ├── api/          # API路由
│   │   ├── core/         # 核心配置
│   │   ├── models/       # 数据模型
│   │   ├── schemas/      # Pydantic模式
│   │   └── services/     # 业务逻辑
│   ├── main.py           # 应用入口
│   └── requirements.txt
└── docs/                 # 项目文档
```

## 快速开始

### 前端开发

```bash
# 进入前端目录
cd frontend_ant

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

### 后端开发

```bash
# 进入后端目录
cd backend

# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# 安装依赖
pip install -r requirements.txt

# 启动开发服务器
python main.py
```

## 开发说明

### 环境要求
- Node.js >= 16.0.0
- Python >= 3.8.0

### API文档
启动后端服务后，访问 http://localhost:8000/docs 查看API文档。

### 默认账号
- 用户名: admin
- 密码: admin123

## 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 联系方式

- 项目维护者: chenjiangbo
- 邮箱: chenjiangbo.real@gmail.com
- GitHub: https://github.com/chenjiangbo/AIgoOne

## 版本历史

### v1.0.0 (2025-01-08)
- 初始版本发布
- 基础设备管理功能
- 用户认证系统
- 现代化UI界面