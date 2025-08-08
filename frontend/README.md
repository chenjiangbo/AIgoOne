# AI Manager Frontend

AI算法管理平台前端项目，基于Vue 3 + TypeScript + Element Plus构建的现代化Web应用。

## 项目特性

✨ **现代技术栈**
- Vue 3 + Composition API
- TypeScript 支持
- Vite 构建工具
- Element Plus UI 框架

🎨 **设计系统**
- 基于 Design Token 的统一设计语言
- 响应式布局
- 亮色/暗色主题切换
- 一致的视觉风格

🏗️ **工程化**
- 组件化架构
- 代码分割和懒加载
- ESLint + Prettier 代码规范
- 自动化构建和部署

🚀 **性能优化**
- Tree-shaking
- 资源压缩
- 缓存策略
- Bundle 分析

## 快速开始

### 环境要求

- Node.js >= 16.0.0
- npm >= 8.0.0 或 yarn >= 1.22.0

### 安装依赖

\`\`\`bash
npm install
\`\`\`

### 开发环境

\`\`\`bash
# 启动开发服务器
npm run dev

# 启动 Mock 模式
npm run dev:mock
\`\`\`

开发服务器将在 \`http://localhost:3000\` 启动。

### 构建部署

\`\`\`bash
# 构建生产环境
npm run build

# 构建开发环境（包含 sourcemap）
npm run build:dev

# 构建并分析包大小
npm run build:analyze

# 预览构建结果
npm run preview
\`\`\`

### 代码规范

\`\`\`bash
# 代码检查
npm run lint

# 代码格式化
npm run format

# 类型检查
npm run type-check
\`\`\`

## 项目结构

\`\`\`
src/
├── components/          # 组件库
│   ├── ui/             # 基础UI组件
│   │   ├── BaseButton.vue
│   │   ├── BaseCard.vue
│   │   ├── BaseDialog.vue
│   │   ├── BaseInput.vue
│   │   └── index.js
│   ├── device/         # 设备管理组件
│   │   ├── DeviceToolbar.vue
│   │   ├── DeviceTable.vue
│   │   ├── DeviceStatsCards.vue
│   │   ├── AddDeviceDialog.vue
│   │   ├── BatchSyncDialog.vue
│   │   └── index.js
│   └── business/       # 业务组件
├── styles/             # 样式系统
│   ├── tokens/         # 设计Token
│   │   ├── colors.css
│   │   ├── spacing.css
│   │   ├── typography.css
│   │   ├── effects.css
│   │   └── index.css
│   ├── base/           # 基础样式
│   ├── components/     # 组件样式
│   ├── utilities/      # 工具样式
│   └── main.css
├── views/              # 页面组件
├── router/             # 路由配置
├── stores/             # 状态管理
├── api/                # API 接口
├── utils/              # 工具函数
├── types/              # TypeScript 类型定义
└── main.ts             # 应用入口
\`\`\`

## 设计系统

项目采用基于 Design Token 的设计系统，确保整个应用的视觉一致性。

### 设计Token

- **颜色系统**：主色、功能色、中性色
- **间距系统**：基于4px栅格的间距规范
- **字体系统**：字号、字重、行高规范
- **阴影系统**：统一的阴影效果
- **圆角系统**：一致的圆角规范

### 主题切换

支持亮色和暗色主题：

\`\`\`javascript
import { themeUtils } from '@/components/ui'

// 切换主题
themeUtils.toggleTheme()

// 设置指定主题
themeUtils.setTheme('dark')
\`\`\`

## 组件库

### 基础组件

- **BaseButton**: 按钮组件，支持多种类型和尺寸
- **BaseCard**: 卡片组件，支持头部、内容、底部插槽
- **BaseDialog**: 对话框组件，支持自定义头部和底部
- **BaseInput**: 输入框组件，支持多种变体和验证

### 使用示例

\`\`\`vue
<template>
  <BaseCard title="设备信息" shadow="hover">
    <BaseInput 
      v-model="form.name"
      label="设备名称"
      placeholder="请输入设备名称"
      required
    />
    <BaseButton 
      type="primary" 
      @click="handleSubmit"
      :loading="loading"
    >
      保存
    </BaseButton>
  </BaseCard>
</template>

<script setup>
import { BaseCard, BaseInput, BaseButton } from '@ui'
</script>
\`\`\`

## 环境配置

项目支持多环境配置：

- \`.env\` - 默认配置
- \`.env.development\` - 开发环境
- \`.env.production\` - 生产环境

### 关键环境变量

\`\`\`bash
# API配置
VITE_API_BASE_URL=http://localhost:8000
VITE_API_TIMEOUT=30000

# 功能开关
VITE_ENABLE_MOCK=false
VITE_ENABLE_DEVTOOLS=true

# 构建优化
VITE_BUILD_COMPRESS=gzip
VITE_DROP_CONSOLE=true
\`\`\`

## 性能优化

### 代码分割

- Vue 核心库单独打包
- Element Plus 单独打包
- 业务组件按功能分包
- 路由级别的懒加载

### 资源优化

- 图片压缩和格式优化
- 字体文件优化
- CSS 代码分割
- Gzip/Brotli 压缩

### 缓存策略

- 长期缓存静态资源
- 合理的文件指纹策略
- 服务端缓存配置

## 开发规范

### 代码风格

- 使用 ESLint + Prettier 统一代码风格
- Vue 3 Composition API 优先
- TypeScript 严格模式
- 组件命名采用 PascalCase

### 提交规范

采用 Conventional Commits 规范：

\`\`\`bash
feat: 新功能
fix: 修复问题
docs: 文档更新
style: 代码格式调整
refactor: 代码重构
test: 测试相关
chore: 构建配置等
\`\`\`

### Git工作流

- \`main\` - 主分支，对应生产环境
- \`develop\` - 开发分支
- \`feature/*\` - 功能分支
- \`hotfix/*\` - 紧急修复分支

## 部署

### 构建产物

\`\`\`
dist/
├── index.html
├── assets/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── fonts/
└── stats.html (分析报告)
\`\`\`

### 服务器配置

推荐使用 Nginx 作为静态文件服务器：

\`\`\`nginx
server {
    listen 80;
    server_name your-domain.com;
    root /path/to/dist;
    index index.html;
    
    # API 代理
    location /api {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    # SPA 路由支持
    location / {
        try_files $uri $uri/ /index.html;
    }
    
    # 静态资源缓存
    location ~* \.(js|css|png|jpg|jpeg|gif|svg|ico|woff|woff2)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
\`\`\`

## 故障排除

### 常见问题

1. **端口冲突**：修改 \`vite.config.js\` 中的端口配置
2. **依赖冲突**：删除 \`node_modules\` 和 \`package-lock.json\` 重新安装
3. **构建失败**：检查 TypeScript 类型错误
4. **样式问题**：确认 Tailwind CSS 配置正确

### 性能问题

1. 使用 \`npm run build:analyze\` 分析包大小
2. 检查组件是否正确懒加载
3. 优化图片资源大小
4. 启用 Gzip 压缩

## 贡献指南

1. Fork 项目
2. 创建功能分支 (\`git checkout -b feature/amazing-feature\`)
3. 提交更改 (\`git commit -m 'feat: add amazing feature'\`)
4. 推送到分支 (\`git push origin feature/amazing-feature\`)
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 联系我们

- 项目仓库：[GitHub](https://github.com/your-org/ai-manager)
- 问题反馈：[Issues](https://github.com/your-org/ai-manager/issues)
- 邮箱：dev@your-domain.com