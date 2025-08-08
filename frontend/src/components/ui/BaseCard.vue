<template>
  <div
    :class="cardClasses"
    :style="cardStyle"
  >
    <!-- 卡片头部 -->
    <div v-if="$slots.header || title || $slots.extra" class="base-card__header">
      <div class="base-card__header-content">
        <slot name="header">
          <h3 v-if="title" class="base-card__title">{{ title }}</h3>
        </slot>
      </div>
      <div v-if="$slots.extra" class="base-card__extra">
        <slot name="extra" />
      </div>
    </div>
    
    <!-- 卡片主体 -->
    <div class="base-card__body">
      <slot />
    </div>
    
    <!-- 卡片底部 -->
    <div v-if="$slots.footer" class="base-card__footer">
      <slot name="footer" />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

// Props
const props = defineProps({
  // 卡片标题
  title: {
    type: String,
    default: ''
  },
  // 卡片尺寸
  size: {
    type: String,
    default: 'medium',
    validator: (value) => ['small', 'medium', 'large'].includes(value)
  },
  // 是否有边框
  bordered: {
    type: Boolean,
    default: true
  },
  // 是否有阴影
  shadow: {
    type: String,
    default: 'always',
    validator: (value) => ['always', 'hover', 'never'].includes(value)
  },
  // 是否可悬浮
  hoverable: {
    type: Boolean,
    default: false
  },
  // 自定义样式
  bodyStyle: {
    type: Object,
    default: () => ({})
  },
  // 头部样式
  headerStyle: {
    type: Object,
    default: () => ({})
  },
  // 是否加载中
  loading: {
    type: Boolean,
    default: false
  }
})

// 计算卡片样式类
const cardClasses = computed(() => {
  const classes = ['base-card']
  
  // 尺寸样式
  classes.push(`base-card--${props.size}`)
  
  // 边框样式
  if (props.bordered) classes.push('is-bordered')
  
  // 阴影样式
  classes.push(`is-shadow-${props.shadow}`)
  
  // 悬浮样式
  if (props.hoverable) classes.push('is-hoverable')
  
  // 加载状态
  if (props.loading) classes.push('is-loading')
  
  return classes
})

// 计算卡片样式
const cardStyle = computed(() => {
  return {
    '--card-body-style': JSON.stringify(props.bodyStyle),
    '--card-header-style': JSON.stringify(props.headerStyle)
  }
})
</script>

<style scoped>
/* 基础卡片样式 */
.base-card {
  position: relative;
  background: var(--color-bg-primary);
  border-radius: var(--border-radius-lg);
  transition: var(--transition-all-fast);
  overflow: hidden;
}

/* 边框变体 */
.base-card.is-bordered {
  border: 1px solid var(--color-border-primary);
}

/* 阴影变体 */
.base-card.is-shadow-always {
  box-shadow: var(--shadow-sm);
}

.base-card.is-shadow-hover {
  box-shadow: none;
}

.base-card.is-shadow-hover:hover {
  box-shadow: var(--shadow-md);
}

.base-card.is-shadow-never {
  box-shadow: none;
}

/* 悬浮效果 */
.base-card.is-hoverable {
  cursor: pointer;
  transition: all 0.2s ease;
}

.base-card.is-hoverable:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

/* 尺寸变体 */
.base-card--small .base-card__body {
  padding: var(--spacing-3);
}

.base-card--small .base-card__header {
  padding: var(--spacing-3) var(--spacing-3) 0;
}

.base-card--small .base-card__footer {
  padding: 0 var(--spacing-3) var(--spacing-3);
}

.base-card--medium .base-card__body {
  padding: var(--spacing-4);
}

.base-card--medium .base-card__header {
  padding: var(--spacing-4) var(--spacing-4) 0;
}

.base-card--medium .base-card__footer {
  padding: 0 var(--spacing-4) var(--spacing-4);
}

.base-card--large .base-card__body {
  padding: var(--spacing-6);
}

.base-card--large .base-card__header {
  padding: var(--spacing-6) var(--spacing-6) 0;
}

.base-card--large .base-card__footer {
  padding: 0 var(--spacing-6) var(--spacing-6);
}

/* 卡片头部 */
.base-card__header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  border-bottom: 1px solid var(--color-border-secondary);
  margin-bottom: var(--spacing-4);
  padding-bottom: var(--spacing-4);
}

.base-card__header-content {
  flex: 1;
  min-width: 0;
}

.base-card__title {
  margin: 0;
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
  line-height: 1.2;
}

.base-card__extra {
  flex-shrink: 0;
  margin-left: var(--spacing-4);
}

/* 卡片主体 */
.base-card__body {
  flex: 1;
  min-height: 0;
}

/* 卡片底部 */
.base-card__footer {
  border-top: 1px solid var(--color-border-secondary);
  margin-top: var(--spacing-4);
  padding-top: var(--spacing-4);
}

/* 加载状态 */
.base-card.is-loading {
  position: relative;
  overflow: hidden;
}

.base-card.is-loading::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(
    90deg,
    transparent,
    var(--color-primary-500),
    transparent
  );
  animation: loading-sweep 2s infinite;
  z-index: 1;
}

@keyframes loading-sweep {
  0% { left: -100%; }
  100% { left: 100%; }
}

/* 响应式调整 */
@media (max-width: 768px) {
  .base-card__header {
    flex-direction: column;
    align-items: stretch;
    gap: var(--spacing-3);
  }
  
  .base-card__extra {
    margin-left: 0;
  }
  
  .base-card--large .base-card__body,
  .base-card--large .base-card__header,
  .base-card--large .base-card__footer {
    padding-left: var(--spacing-4);
    padding-right: var(--spacing-4);
  }
}

/* 暗色主题适配 */
[data-theme="dark"] .base-card {
  background: var(--color-bg-secondary);
  border-color: var(--color-border-secondary);
}

[data-theme="dark"] .base-card.is-bordered {
  border-color: var(--color-border-secondary);
}

[data-theme="dark"] .base-card__header {
  border-bottom-color: var(--color-border-tertiary);
}

[data-theme="dark"] .base-card__footer {
  border-top-color: var(--color-border-tertiary);
}

[data-theme="dark"] .base-card__title {
  color: var(--color-text-primary);
}

/* 特殊卡片类型 */
.base-card--stat {
  text-align: center;
}

.base-card--stat .base-card__body {
  padding: var(--spacing-6) var(--spacing-4);
}

.base-card--stat .stat-value {
  font-size: var(--font-size-3xl);
  font-weight: var(--font-weight-bold);
  color: var(--color-primary-500);
  line-height: 1;
  margin-bottom: var(--spacing-2);
}

.base-card--stat .stat-label {
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
  margin: 0;
}

.base-card--feature {
  border: 2px solid transparent;
  background-clip: padding-box;
}

.base-card--feature.is-active {
  border-color: var(--color-primary-500);
  background: var(--color-primary-50);
}

[data-theme="dark"] .base-card--feature.is-active {
  background: rgba(64, 158, 255, 0.1);
}
</style>