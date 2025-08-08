// UI基础组件库
// 这些组件基于设计Token系统构建，提供统一的视觉风格和用户体验

// 基础组件导出
export { default as BaseButton } from './BaseButton.vue'
export { default as BaseCard } from './BaseCard.vue'
export { default as BaseDialog } from './BaseDialog.vue'
export { default as BaseInput } from './BaseInput.vue'

// 组件类型定义（用于TypeScript支持）
// 注意：这些是JSDoc注释，为IDE提供类型提示

/**
 * BaseButton - 基础按钮组件
 * @typedef {Object} BaseButtonProps
 * @property {'default'|'primary'|'success'|'warning'|'danger'|'info'|'text'|'link'} type - 按钮类型
 * @property {'large'|'medium'|'small'|'mini'} size - 按钮尺寸
 * @property {boolean} disabled - 是否禁用
 * @property {boolean} loading - 是否加载中
 * @property {string|Object} icon - 图标
 * @property {boolean} round - 是否圆角
 * @property {boolean} circle - 是否圆形
 * @property {boolean} plain - 是否朴素按钮
 * @property {boolean} block - 是否块级元素
 */

/**
 * BaseCard - 基础卡片组件
 * @typedef {Object} BaseCardProps
 * @property {string} title - 卡片标题
 * @property {'small'|'medium'|'large'} size - 卡片尺寸
 * @property {boolean} bordered - 是否有边框
 * @property {'always'|'hover'|'never'} shadow - 阴影样式
 * @property {boolean} hoverable - 是否可悬浮
 * @property {Object} bodyStyle - 自定义主体样式
 * @property {Object} headerStyle - 自定义头部样式
 * @property {boolean} loading - 是否加载中
 */

/**
 * BaseDialog - 基础对话框组件
 * @typedef {Object} BaseDialogProps
 * @property {boolean} visible - 是否可见
 * @property {string} title - 对话框标题
 * @property {string} subtitle - 对话框副标题
 * @property {string|number} width - 对话框宽度
 * @property {'small'|'medium'|'large'|'fullscreen'} size - 对话框尺寸
 * @property {'default'|'info'|'success'|'warning'|'danger'} type - 对话框类型
 * @property {string|Object} icon - 标题图标
 * @property {boolean} showClose - 是否显示关闭按钮
 * @property {boolean} loading - 是否加载中
 * @property {boolean} showDefaultFooter - 是否显示默认底部
 */

/**
 * BaseInput - 基础输入框组件
 * @typedef {Object} BaseInputProps
 * @property {string|number} modelValue - 输入值
 * @property {string} type - 输入框类型
 * @property {string} placeholder - 占位符
 * @property {boolean} disabled - 是否禁用
 * @property {boolean} readonly - 是否只读
 * @property {'large'|'default'|'small'} size - 输入框尺寸
 * @property {'outlined'|'filled'|'standard'} variant - 输入框变体
 * @property {boolean} clearable - 是否可清空
 * @property {string} label - 标签文本
 * @property {string} helpText - 帮助文本
 * @property {string} errorMessage - 错误信息
 * @property {boolean} required - 是否必填
 */

// 组件安装函数（用于全局注册）
export const install = (app) => {
  // 注册所有基础组件
  const components = {
    BaseButton,
    BaseCard,
    BaseDialog,
    BaseInput
  }
  
  Object.entries(components).forEach(([name, component]) => {
    app.component(name, component)
  })
}

// 默认导出（用于插件方式安装）
export default {
  install
}

// 组件版本信息
export const version = '1.0.0'

// 组件库元数据
export const metadata = {
  name: 'AI Manager UI Components',
  description: '基于设计Token系统的Vue 3组件库',
  version,
  author: 'AI Manager Team',
  license: 'MIT',
  dependencies: {
    vue: '^3.0.0',
    'element-plus': '^2.0.0'
  },
  features: [
    '基于设计Token的统一样式系统',
    '支持亮色/暗色主题切换',
    '完整的TypeScript类型支持',
    '响应式设计',
    '可访问性支持',
    '灵活的API设计'
  ]
}

// 工具函数 - 组件类名生成器
export const createComponentClass = (componentName, modifiers = {}) => {
  const baseClass = `base-${componentName}`
  const classes = [baseClass]
  
  Object.entries(modifiers).forEach(([key, value]) => {
    if (value === true) {
      classes.push(`${baseClass}--${key}`)
    } else if (value && typeof value === 'string') {
      classes.push(`${baseClass}--${key}-${value}`)
    }
  })
  
  return classes.join(' ')
}

// 主题工具函数
export const themeUtils = {
  // 获取当前主题
  getCurrentTheme() {
    return document.documentElement.getAttribute('data-theme') || 'light'
  },
  
  // 切换主题
  toggleTheme() {
    const current = this.getCurrentTheme()
    const newTheme = current === 'light' ? 'dark' : 'light'
    document.documentElement.setAttribute('data-theme', newTheme)
    return newTheme
  },
  
  // 设置主题
  setTheme(theme) {
    if (['light', 'dark'].includes(theme)) {
      document.documentElement.setAttribute('data-theme', theme)
    }
  }
}

// 设计Token访问器
export const tokens = {
  // 获取CSS变量值
  getCSSVar(name) {
    return getComputedStyle(document.documentElement).getPropertyValue(`--${name}`).trim()
  },
  
  // 设置CSS变量值
  setCSSVar(name, value) {
    document.documentElement.style.setProperty(`--${name}`, value)
  },
  
  // 获取颜色Token
  getColor(name) {
    return this.getCSSVar(`color-${name}`)
  },
  
  // 获取间距Token
  getSpacing(name) {
    return this.getCSSVar(`spacing-${name}`)
  },
  
  // 获取字体Token
  getFontSize(name) {
    return this.getCSSVar(`font-size-${name}`)
  },
  
  // 获取阴影Token
  getShadow(name) {
    return this.getCSSVar(`shadow-${name}`)
  }
}