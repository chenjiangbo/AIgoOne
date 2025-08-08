<template>
  <button
    :class="buttonClasses"
    :disabled="disabled || loading"
    :type="htmlType"
    @click="handleClick"
  >
    <el-icon v-if="loading" class="btn-loading">
      <Loading />
    </el-icon>
    <el-icon v-else-if="icon" class="btn-icon">
      <component :is="icon" />
    </el-icon>
    
    <span v-if="$slots.default" class="btn-content">
      <slot />
    </span>
  </button>
</template>

<script setup>
import { computed } from 'vue'
import { Loading } from '@element-plus/icons-vue'

// Props
const props = defineProps({
  // 按钮类型
  type: {
    type: String,
    default: 'default',
    validator: (value) => ['default', 'primary', 'success', 'warning', 'danger', 'info', 'text', 'link'].includes(value)
  },
  // 按钮尺寸
  size: {
    type: String,
    default: 'medium',
    validator: (value) => ['large', 'medium', 'small', 'mini'].includes(value)
  },
  // 是否禁用
  disabled: {
    type: Boolean,
    default: false
  },
  // 是否加载中
  loading: {
    type: Boolean,
    default: false
  },
  // 图标
  icon: {
    type: [String, Object],
    default: null
  },
  // HTML type属性
  htmlType: {
    type: String,
    default: 'button',
    validator: (value) => ['button', 'submit', 'reset'].includes(value)
  },
  // 是否圆角
  round: {
    type: Boolean,
    default: false
  },
  // 是否圆形
  circle: {
    type: Boolean,
    default: false
  },
  // 是否朴素按钮
  plain: {
    type: Boolean,
    default: false
  },
  // 是否块级元素
  block: {
    type: Boolean,
    default: false
  }
})

// Emits
const emit = defineEmits(['click'])

// 计算按钮样式类
const buttonClasses = computed(() => {
  const classes = ['base-btn']
  
  // 类型样式
  classes.push(`base-btn--${props.type}`)
  
  // 尺寸样式
  classes.push(`base-btn--${props.size}`)
  
  // 状态样式
  if (props.disabled) classes.push('is-disabled')
  if (props.loading) classes.push('is-loading')
  if (props.round) classes.push('is-round')
  if (props.circle) classes.push('is-circle')
  if (props.plain) classes.push('is-plain')
  if (props.block) classes.push('is-block')
  
  return classes
})

// 事件处理
const handleClick = (event) => {
  if (!props.disabled && !props.loading) {
    emit('click', event)
  }
}
</script>

<style scoped>
/* 基础按钮样式 */
.base-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-1);
  padding: var(--spacing-2) var(--spacing-4);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  line-height: 1;
  border: 1px solid transparent;
  border-radius: var(--border-radius-md);
  cursor: pointer;
  transition: var(--transition-all-fast);
  outline: none;
  user-select: none;
  white-space: nowrap;
  box-sizing: border-box;
}

.base-btn:focus {
  outline: 2px solid var(--color-primary-200);
  outline-offset: 2px;
}

/* 尺寸变体 */
.base-btn--large {
  padding: var(--spacing-3) var(--spacing-6);
  font-size: var(--font-size-lg);
  height: 48px;
}

.base-btn--medium {
  padding: var(--spacing-2) var(--spacing-4);
  font-size: var(--font-size-base);
  height: 40px;
}

.base-btn--small {
  padding: var(--spacing-1_5) var(--spacing-3);
  font-size: var(--font-size-sm);
  height: 32px;
}

.base-btn--mini {
  padding: var(--spacing-1) var(--spacing-2);
  font-size: var(--font-size-xs);
  height: 24px;
}

/* 类型变体 */
.base-btn--default {
  background: var(--color-neutral-50);
  border-color: var(--color-border-primary);
  color: var(--color-text-primary);
}

.base-btn--default:hover:not(.is-disabled):not(.is-loading) {
  background: var(--color-neutral-100);
  border-color: var(--color-primary-500);
  color: var(--color-primary-500);
}

.base-btn--primary {
  background: var(--color-primary-500);
  border-color: var(--color-primary-500);
  color: white;
}

.base-btn--primary:hover:not(.is-disabled):not(.is-loading) {
  background: var(--color-primary-600);
  border-color: var(--color-primary-600);
}

.base-btn--success {
  background: var(--color-success-500);
  border-color: var(--color-success-500);
  color: white;
}

.base-btn--success:hover:not(.is-disabled):not(.is-loading) {
  background: var(--color-success-600);
  border-color: var(--color-success-600);
}

.base-btn--warning {
  background: var(--color-warning-500);
  border-color: var(--color-warning-500);
  color: white;
}

.base-btn--warning:hover:not(.is-disabled):not(.is-loading) {
  background: var(--color-warning-600);
  border-color: var(--color-warning-600);
}

.base-btn--danger {
  background: var(--color-error-500);
  border-color: var(--color-error-500);
  color: white;
}

.base-btn--danger:hover:not(.is-disabled):not(.is-loading) {
  background: var(--color-error-600);
  border-color: var(--color-error-600);
}

.base-btn--info {
  background: var(--color-info-500);
  border-color: var(--color-info-500);
  color: white;
}

.base-btn--info:hover:not(.is-disabled):not(.is-loading) {
  background: var(--color-info-600);
  border-color: var(--color-info-600);
}

.base-btn--text {
  background: transparent;
  border-color: transparent;
  color: var(--color-primary-500);
  padding: var(--spacing-1) var(--spacing-2);
}

.base-btn--text:hover:not(.is-disabled):not(.is-loading) {
  background: var(--color-primary-50);
  color: var(--color-primary-600);
}

.base-btn--link {
  background: transparent;
  border-color: transparent;
  color: var(--color-primary-500);
  text-decoration: underline;
  padding: var(--spacing-1) var(--spacing-2);
}

.base-btn--link:hover:not(.is-disabled):not(.is-loading) {
  color: var(--color-primary-600);
}

/* 朴素按钮变体 */
.base-btn--primary.is-plain {
  background: var(--color-primary-50);
  border-color: var(--color-primary-200);
  color: var(--color-primary-500);
}

.base-btn--primary.is-plain:hover:not(.is-disabled):not(.is-loading) {
  background: var(--color-primary-500);
  border-color: var(--color-primary-500);
  color: white;
}

.base-btn--success.is-plain {
  background: var(--color-success-50);
  border-color: var(--color-success-200);
  color: var(--color-success-500);
}

.base-btn--success.is-plain:hover:not(.is-disabled):not(.is-loading) {
  background: var(--color-success-500);
  border-color: var(--color-success-500);
  color: white;
}

.base-btn--warning.is-plain {
  background: var(--color-warning-50);
  border-color: var(--color-warning-200);
  color: var(--color-warning-500);
}

.base-btn--warning.is-plain:hover:not(.is-disabled):not(.is-loading) {
  background: var(--color-warning-500);
  border-color: var(--color-warning-500);
  color: white;
}

.base-btn--danger.is-plain {
  background: var(--color-error-50);
  border-color: var(--color-error-200);
  color: var(--color-error-500);
}

.base-btn--danger.is-plain:hover:not(.is-disabled):not(.is-loading) {
  background: var(--color-error-500);
  border-color: var(--color-error-500);
  color: white;
}

/* 状态变体 */
.base-btn.is-disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

.base-btn.is-loading {
  cursor: default;
}

.base-btn.is-round {
  border-radius: calc(var(--border-radius-full) / 2);
}

.base-btn.is-circle {
  border-radius: var(--border-radius-full);
  padding: var(--spacing-2);
  width: 40px;
  height: 40px;
}

.base-btn--large.is-circle {
  width: 48px;
  height: 48px;
}

.base-btn--small.is-circle {
  width: 32px;
  height: 32px;
}

.base-btn--mini.is-circle {
  width: 24px;
  height: 24px;
}

.base-btn.is-block {
  width: 100%;
}

/* 图标和内容样式 */
.btn-icon,
.btn-loading {
  font-size: 1em;
}

.btn-loading {
  animation: loading-rotate 1s linear infinite;
}

@keyframes loading-rotate {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.btn-content {
  display: inline-block;
}

.base-btn--circle .btn-content {
  display: none;
}

/* 暗色主题适配 */
[data-theme="dark"] .base-btn--default {
  background: var(--color-neutral-800);
  border-color: var(--color-border-secondary);
  color: var(--color-text-primary);
}

[data-theme="dark"] .base-btn--default:hover:not(.is-disabled):not(.is-loading) {
  background: var(--color-neutral-700);
  border-color: var(--color-primary-400);
  color: var(--color-primary-400);
}

[data-theme="dark"] .base-btn--text:hover:not(.is-disabled):not(.is-loading) {
  background: rgba(64, 158, 255, 0.1);
  color: var(--color-primary-400);
}
</style>