# 组件库文档

AI Manager UI 组件库基于 Vue 3 + TypeScript 构建，采用设计Token系统确保视觉一致性。

## 设计原则

### 一致性 (Consistency)
- 统一的设计语言和视觉风格
- 一致的交互模式和用户体验
- 标准化的组件API设计

### 可访问性 (Accessibility)
- 支持键盘导航
- 语义化的HTML结构
- 合适的颜色对比度
- 屏幕阅读器友好

### 灵活性 (Flexibility)
- 可配置的主题系统
- 丰富的自定义选项
- 插槽系统支持内容扩展

### 性能优化 (Performance)
- 按需加载
- Tree-shaking 支持
- 轻量级实现

## 基础组件

### BaseButton

通用按钮组件，支持多种类型、尺寸和状态。

#### Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| type | string | 'default' | 按钮类型：default/primary/success/warning/danger/info/text/link |
| size | string | 'medium' | 按钮尺寸：large/medium/small/mini |
| disabled | boolean | false | 是否禁用 |
| loading | boolean | false | 是否加载中 |
| icon | string/Object | null | 图标 |
| round | boolean | false | 是否圆角 |
| circle | boolean | false | 是否圆形 |
| plain | boolean | false | 是否朴素按钮 |
| block | boolean | false | 是否块级元素 |

#### Events

| 事件名 | 说明 | 回调参数 |
|--------|------|----------|
| click | 点击事件 | event |

#### 使用示例

\`\`\`vue
<template>
  <!-- 基础用法 -->
  <BaseButton>默认按钮</BaseButton>
  
  <!-- 不同类型 -->
  <BaseButton type="primary">主要按钮</BaseButton>
  <BaseButton type="success">成功按钮</BaseButton>
  <BaseButton type="warning">警告按钮</BaseButton>
  <BaseButton type="danger">危险按钮</BaseButton>
  
  <!-- 不同尺寸 -->
  <BaseButton size="large">大按钮</BaseButton>
  <BaseButton size="medium">中按钮</BaseButton>
  <BaseButton size="small">小按钮</BaseButton>
  
  <!-- 加载状态 -->
  <BaseButton :loading="loading" @click="handleClick">
    提交
  </BaseButton>
  
  <!-- 带图标 -->
  <BaseButton icon="Plus">添加</BaseButton>
  <BaseButton type="primary" icon="Search" circle />
  
  <!-- 朴素按钮 -->
  <BaseButton type="primary" plain>朴素按钮</BaseButton>
</template>
\`\`\`

### BaseCard

卡片容器组件，用于内容分组展示。

#### Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| title | string | '' | 卡片标题 |
| size | string | 'medium' | 卡片尺寸：small/medium/large |
| bordered | boolean | true | 是否有边框 |
| shadow | string | 'always' | 阴影样式：always/hover/never |
| hoverable | boolean | false | 是否可悬浮 |
| loading | boolean | false | 是否加载中 |

#### Slots

| 插槽名 | 说明 |
|--------|------|
| default | 卡片内容 |
| header | 自定义头部 |
| extra | 头部右侧额外内容 |
| footer | 底部内容 |

#### 使用示例

\`\`\`vue
<template>
  <!-- 基础用法 -->
  <BaseCard title="基本信息">
    <p>这是卡片内容</p>
  </BaseCard>
  
  <!-- 自定义头部 -->
  <BaseCard>
    <template #header>
      <div class="flex items-center gap-2">
        <el-icon><User /></el-icon>
        <span>用户信息</span>
      </div>
    </template>
    <template #extra>
      <BaseButton type="text">编辑</BaseButton>
    </template>
    
    <p>卡片内容区域</p>
    
    <template #footer>
      <div class="text-right">
        <BaseButton>取消</BaseButton>
        <BaseButton type="primary">确定</BaseButton>
      </div>
    </template>
  </BaseCard>
  
  <!-- 悬浮效果 -->
  <BaseCard hoverable shadow="hover">
    <p>鼠标悬浮有动画效果</p>
  </BaseCard>
  
  <!-- 加载状态 -->
  <BaseCard loading title="加载中">
    <p>内容正在加载...</p>
  </BaseCard>
</template>
\`\`\`

### BaseDialog

对话框组件，用于承载表单、确认等交互内容。

#### Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| visible | boolean | false | 是否可见 |
| title | string | '' | 对话框标题 |
| subtitle | string | '' | 对话框副标题 |
| width | string/number | '50%' | 对话框宽度 |
| size | string | 'medium' | 对话框尺寸：small/medium/large/fullscreen |
| type | string | 'default' | 对话框类型：default/info/success/warning/danger |
| icon | string/Object | null | 标题图标 |
| showClose | boolean | true | 是否显示关闭按钮 |
| loading | boolean | false | 是否加载中 |
| showDefaultFooter | boolean | false | 是否显示默认底部按钮 |
| confirmLoading | boolean | false | 确认按钮加载状态 |

#### Events

| 事件名 | 说明 | 回调参数 |
|--------|------|----------|
| update:visible | 可见性变化 | visible |
| confirm | 确认按钮点击 | - |
| cancel | 取消按钮点击 | - |
| open | 对话框打开后 | - |
| close | 对话框关闭后 | - |

#### Slots

| 插槽名 | 说明 |
|--------|------|
| default | 对话框内容 |
| header | 自定义头部 |
| header-actions | 头部右侧操作区 |
| footer | 自定义底部 |

#### 使用示例

\`\`\`vue
<template>
  <!-- 基础用法 -->
  <BaseDialog 
    v-model:visible="dialogVisible"
    title="编辑信息"
    width="600px"
  >
    <p>对话框内容</p>
  </BaseDialog>
  
  <!-- 带图标和副标题 -->
  <BaseDialog
    v-model:visible="dialogVisible"
    title="删除确认"
    subtitle="此操作不可撤销，请谨慎操作"
    type="danger"
    icon="Warning"
    show-default-footer
    @confirm="handleConfirm"
    @cancel="dialogVisible = false"
  >
    <p>确定要删除这个项目吗？</p>
  </BaseDialog>
  
  <!-- 自定义头部和底部 -->
  <BaseDialog v-model:visible="dialogVisible">
    <template #header>
      <div class="flex items-center gap-2">
        <el-icon><Settings /></el-icon>
        <div>
          <h3>高级设置</h3>
          <p class="text-sm text-gray-500">配置系统参数</p>
        </div>
      </div>
    </template>
    
    <div class="space-y-4">
      <!-- 表单内容 -->
    </div>
    
    <template #footer>
      <div class="flex justify-between">
        <BaseButton type="text">重置</BaseButton>
        <div class="space-x-2">
          <BaseButton @click="dialogVisible = false">取消</BaseButton>
          <BaseButton type="primary" :loading="loading" @click="handleSave">
            保存
          </BaseButton>
        </div>
      </div>
    </template>
  </BaseDialog>
</template>
\`\`\`

### BaseInput

输入框组件，支持多种类型和验证状态。

#### Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| modelValue | string/number | '' | 输入值 |
| type | string | 'text' | 输入框类型 |
| placeholder | string | '' | 占位符 |
| disabled | boolean | false | 是否禁用 |
| readonly | boolean | false | 是否只读 |
| size | string | 'default' | 输入框尺寸：large/default/small |
| variant | string | 'outlined' | 输入框变体：outlined/filled/standard |
| label | string | '' | 标签文本 |
| description | string | '' | 描述文本 |
| helpText | string | '' | 帮助文本 |
| errorMessage | string | '' | 错误信息 |
| required | boolean | false | 是否必填 |
| clearable | boolean | false | 是否可清空 |
| showWordLimit | boolean | false | 是否显示字数统计 |
| maxlength | string/number | - | 最大长度 |

#### Events

| 事件名 | 说明 | 回调参数 |
|--------|------|----------|
| update:modelValue | 值变化 | value |
| input | 输入事件 | value |
| change | 值变化事件 | value |
| focus | 获得焦点 | event |
| blur | 失去焦点 | event |
| clear | 清空事件 | - |

#### Slots

| 插槽名 | 说明 |
|--------|------|
| prefix | 前缀内容 |
| suffix | 后缀内容 |
| prepend | 前置内容 |
| append | 后置内容 |

#### 使用示例

\`\`\`vue
<template>
  <!-- 基础用法 -->
  <BaseInput 
    v-model="form.name"
    label="姓名"
    placeholder="请输入姓名"
    required
  />
  
  <!-- 不同变体 -->
  <BaseInput v-model="value1" variant="outlined" placeholder="outlined" />
  <BaseInput v-model="value2" variant="filled" placeholder="filled" />
  <BaseInput v-model="value3" variant="standard" placeholder="standard" />
  
  <!-- 带验证状态 -->
  <BaseInput
    v-model="form.email"
    type="email"
    label="邮箱地址"
    placeholder="请输入邮箱"
    :error-message="errors.email"
    help-text="用于找回密码和接收通知"
  />
  
  <!-- 带前后缀 -->
  <BaseInput v-model="url" label="网站地址">
    <template #prepend>https://</template>
    <template #append>.com</template>
  </BaseInput>
  
  <!-- 文本域 -->
  <BaseInput
    v-model="content"
    type="textarea"
    label="内容"
    :rows="4"
    :maxlength="500"
    show-word-limit
    placeholder="请输入内容..."
  />
</template>
\`\`\`

## 设备管理组件

### DeviceToolbar

设备管理工具栏，包含搜索、筛选、操作按钮等功能。

#### Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| refreshing | boolean | false | 是否正在刷新 |
| batchSyncing | boolean | false | 是否正在批量同步 |
| selectedCount | number | 0 | 选中的设备数量 |

#### Events

| 事件名 | 说明 | 回调参数 |
|--------|------|----------|
| search | 搜索事件 | keyword |
| filter | 筛选事件 | filters |
| refresh | 刷新事件 | - |
| batch-sync | 批量同步事件 | - |
| add-device | 添加设备事件 | - |

### DeviceTable

设备列表表格组件。

#### Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| devices | array | [] | 设备列表数据 |
| loading | boolean | false | 是否加载中 |
| height | number | 400 | 表格高度 |

#### Events

| 事件名 | 说明 | 回调参数 |
|--------|------|----------|
| selection-change | 选择变化 | selection |
| sync | 同步设备 | device |
| view-details | 查看详情 | device |
| delete | 删除设备 | device |

### DeviceStatsCards

设备统计卡片组件。

#### Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| stats | object | {} | 统计数据 |

## 主题系统

### 设计Token

项目使用CSS自定义属性实现设计Token系统：

\`\`\`css
:root {
  /* 颜色系统 */
  --color-primary-500: #409eff;
  --color-success-500: #67c23a;
  --color-warning-500: #e6a23c;
  --color-error-500: #f56c6c;
  
  /* 间距系统 */
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-4: 16px;
  --spacing-6: 24px;
  
  /* 字体系统 */
  --font-size-sm: 12px;
  --font-size-base: 14px;
  --font-size-lg: 16px;
  --font-size-xl: 18px;
}
\`\`\`

### 主题切换

\`\`\`javascript
import { themeUtils } from '@ui'

// 获取当前主题
const currentTheme = themeUtils.getCurrentTheme()

// 切换主题
themeUtils.toggleTheme()

// 设置指定主题
themeUtils.setTheme('dark')
\`\`\`

### 自定义主题

可以通过覆盖CSS变量来自定义主题：

\`\`\`css
/* 自定义主题色 */
:root {
  --color-primary-500: #1890ff;
  --color-primary-600: #096dd9;
}

/* 暗色主题 */
[data-theme="dark"] {
  --color-bg-primary: #1f1f1f;
  --color-text-primary: #ffffff;
}
\`\`\`

## 最佳实践

### 组件使用

1. **按需导入**：只导入需要的组件，利用Tree-shaking减少包大小
2. **类型安全**：使用TypeScript获得更好的开发体验
3. **主题一致性**：使用设计Token保证视觉统一
4. **可访问性**：关注键盘导航和屏幕阅读器支持

### 性能优化

1. **懒加载**：大型组件使用动态导入
2. **缓存**：合理使用组件缓存
3. **虚拟滚动**：长列表使用虚拟滚动
4. **防抖节流**：输入和搜索添加防抖

### 代码规范

1. **命名规范**：组件使用PascalCase，属性使用camelCase
2. **文档注释**：为组件和方法添加JSDoc注释
3. **错误处理**：合理处理异步操作和错误状态
4. **测试覆盖**：为关键组件编写单元测试

## 更新日志

### v1.0.0

- ✨ 发布基础UI组件库
- ✨ 支持亮色/暗色主题切换
- ✨ 完整的TypeScript类型支持
- 🎨 基于设计Token的统一样式系统
- 📱 响应式设计支持
- ♿ 可访问性优化