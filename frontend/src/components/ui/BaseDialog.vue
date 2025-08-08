<template>
  <el-dialog
    :model-value="visible"
    :class="dialogClasses"
    :width="width"
    :top="top"
    :modal="modal"
    :modal-class="modalClass"
    :append-to-body="appendToBody"
    :lock-scroll="lockScroll"
    :close-on-click-modal="closeOnClickModal"
    :close-on-press-escape="closeOnPressEscape"
    :show-close="false"
    :before-close="handleBeforeClose"
    :destroy-on-close="destroyOnClose"
    :center="center"
    :draggable="draggable"
    :overflow="overflow"
    @update:model-value="$emit('update:visible', $event)"
    @open="$emit('open')"
    @opened="$emit('opened')"
    @close="$emit('close')"
    @closed="$emit('closed')"
  >
    <!-- 自定义头部 -->
    <template #header="{ close, titleId, titleClass }">
      <div class="base-dialog__header">
        <div class="dialog-header__content">
          <slot name="header">
            <div class="dialog-title-wrapper">
              <el-icon v-if="iconComponent" class="dialog-icon">
                <component :is="iconComponent" />
              </el-icon>
              <div class="dialog-title-group">
                <h3 class="dialog-title-text">{{ title }}</h3>
                <span v-if="subtitle" class="dialog-subtitle">{{ subtitle }}</span>
              </div>
            </div>
          </slot>
        </div>
        
        <div class="dialog-header__actions">
          <slot name="header-actions" />
          <el-button
            v-if="showMaximize"
            type="text"
            class="dialog-action-btn"
            @click="handleMaximize"
            :title="maximizeText"
          >
            <el-icon><FullScreen /></el-icon>
          </el-button>
          <el-button
            v-if="showClose"
            type="text"
            class="dialog-close-btn"
            @click="handleClose"
            :title="closeText"
          >
            <el-icon><Close /></el-icon>
          </el-button>
        </div>
      </div>
    </template>

    <!-- 对话框主体内容 -->
    <div class="base-dialog__body" :style="bodyStyle">
      <div v-if="loading" class="dialog-loading">
        <el-icon class="loading-icon">
          <Loading />
        </el-icon>
        <span class="loading-text">{{ loadingText }}</span>
      </div>
      <slot v-else />
    </div>

    <!-- 自定义底部 -->
    <template v-if="$slots.footer || showDefaultFooter" #footer>
      <div class="base-dialog__footer">
        <slot name="footer">
          <div v-if="showDefaultFooter" class="dialog-footer-default">
            <el-button @click="handleCancel">{{ cancelText }}</el-button>
            <el-button 
              type="primary" 
              :loading="confirmLoading"
              @click="handleConfirm"
            >
              {{ confirmText }}
            </el-button>
          </div>
        </slot>
      </div>
    </template>
  </el-dialog>
</template>

<script setup>
import { computed } from 'vue'
import { 
  Close, 
  Loading, 
  FullScreen,
  Plus,
  VideoCamera,
  Edit,
  View,
  InfoFilled,
  Setting,
  Document,
  Monitor,
  Upload
} from '@element-plus/icons-vue'

// Props
const props = defineProps({
  // 基础对话框属性
  visible: {
    type: Boolean,
    default: false
  },
  title: {
    type: String,
    default: ''
  },
  subtitle: {
    type: String,
    default: ''
  },
  width: {
    type: [String, Number],
    default: '50%'
  },
  top: {
    type: String,
    default: '15vh'
  },
  
  // 对话框行为
  modal: {
    type: Boolean,
    default: true
  },
  appendToBody: {
    type: Boolean,
    default: false
  },
  lockScroll: {
    type: Boolean,
    default: true
  },
  closeOnClickModal: {
    type: Boolean,
    default: true
  },
  closeOnPressEscape: {
    type: Boolean,
    default: true
  },
  destroyOnClose: {
    type: Boolean,
    default: false
  },
  center: {
    type: Boolean,
    default: false
  },
  draggable: {
    type: Boolean,
    default: false
  },
  overflow: {
    type: Boolean,
    default: false
  },
  
  // 样式相关
  size: {
    type: String,
    default: 'medium',
    validator: (value) => ['small', 'medium', 'large', 'fullscreen'].includes(value)
  },
  type: {
    type: String,
    default: 'default',
    validator: (value) => ['default', 'info', 'success', 'warning', 'danger'].includes(value)
  },
  
  // 头部相关
  icon: {
    type: [String, Object],
    default: null
  },
  showClose: {
    type: Boolean,
    default: true
  },
  closeText: {
    type: String,
    default: '关闭'
  },
  showMaximize: {
    type: Boolean,
    default: false
  },
  maximizeText: {
    type: String,
    default: '最大化'
  },
  
  // 内容相关
  loading: {
    type: Boolean,
    default: false
  },
  loadingText: {
    type: String,
    default: '加载中...'
  },
  bodyStyle: {
    type: Object,
    default: () => ({})
  },
  
  // 底部相关
  showDefaultFooter: {
    type: Boolean,
    default: false
  },
  cancelText: {
    type: String,
    default: '取消'
  },
  confirmText: {
    type: String,
    default: '确定'
  },
  confirmLoading: {
    type: Boolean,
    default: false
  },
  
  // 自定义样式类
  modalClass: {
    type: String,
    default: ''
  },
  beforeClose: {
    type: Function,
    default: null
  }
})

// Emits
const emit = defineEmits([
  'update:visible',
  'open',
  'opened', 
  'close',
  'closed',
  'confirm',
  'cancel',
  'maximize'
])

// 图标映射
const iconMap = {
  Plus,
  VideoCamera,
  Edit,
  View,
  InfoFilled,
  Setting,
  Document,
  Monitor,
  Loading,
  Close,
  FullScreen,
  Upload
}

// 计算图标组件
const iconComponent = computed(() => {
  if (!props.icon) return null
  if (typeof props.icon === 'string') {
    return iconMap[props.icon] || null
  }
  return props.icon
})

// 计算对话框样式类
const dialogClasses = computed(() => {
  const classes = ['base-dialog']
  
  // 尺寸样式
  classes.push(`base-dialog--${props.size}`)
  
  // 类型样式
  classes.push(`base-dialog--${props.type}`)
  
  return classes.join(' ')
})

// 事件处理
const handleClose = () => {
  emit('update:visible', false)
  emit('close')
}

const handleCancel = () => {
  emit('cancel')
  handleClose()
}

const handleConfirm = () => {
  emit('confirm')
}

const handleMaximize = () => {
  emit('maximize')
}

const handleBeforeClose = (done) => {
  if (props.beforeClose) {
    props.beforeClose(done)
  } else {
    done()
  }
}
</script>

<style scoped>
/* 全局对话框样式 */
:deep(.base-dialog) {
  --dialog-border-radius: var(--border-radius-lg);
  border-radius: var(--dialog-border-radius);
  overflow: hidden;
}

:deep(.base-dialog .el-dialog) {
  border-radius: var(--dialog-border-radius);
  margin: 0 !important;
}

:deep(.base-dialog .el-dialog__header) {
  padding: 0 !important;
  margin: 0 !important;
  border-bottom: none;
}

:deep(.base-dialog .el-dialog__body) {
  padding: 0 !important;
  color: var(--color-text-primary);
}

:deep(.base-dialog .el-dialog__footer) {
  padding: 0 !important;
  border-top: none;
}

/* 尺寸变体 */
:deep(.base-dialog--small .el-dialog) {
  --dialog-padding: var(--spacing-4);
}

:deep(.base-dialog--medium .el-dialog) {
  --dialog-padding: var(--spacing-5);
}

:deep(.base-dialog--large .el-dialog) {
  --dialog-padding: var(--spacing-6);
}

:deep(.base-dialog--fullscreen .el-dialog) {
  --dialog-padding: var(--spacing-6);
  margin: var(--spacing-4) !important;
  max-height: calc(100vh - var(--spacing-8));
}

/* 类型变体 */
:deep(.base-dialog--info .el-dialog) {
  border-left: 4px solid var(--color-info-500);
}

:deep(.base-dialog--success .el-dialog) {
  border-left: 4px solid var(--color-success-500);
}

:deep(.base-dialog--warning .el-dialog) {
  border-left: 4px solid var(--color-warning-500);
}

:deep(.base-dialog--danger .el-dialog) {
  border-left: 4px solid var(--color-error-500);
}

/* 对话框头部 */
.base-dialog__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 48px;
  padding: 0 var(--spacing-4);
  margin: calc(var(--spacing-5) * -1) calc(var(--spacing-5) * -1) 0;
  background: var(--color-primary-500);
  border-bottom: 1px solid var(--color-border-secondary);
  color: white;
  border-radius: var(--dialog-border-radius) var(--dialog-border-radius) 0 0;
  user-select: none;
}

/* 浅色主题标题栏 */
html:not(.dark) .base-dialog__header {
  background: var(--color-primary-500);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

/* 暗色主题标题栏 */
html.dark .base-dialog__header {
  background: var(--color-neutral-800);
  border-bottom: 1px solid var(--color-border-secondary);
}

.dialog-header__content {
  flex: 1;
  min-width: 0;
}

.dialog-title-wrapper {
  display: flex;
  align-items: center;
  gap: var(--spacing-3);
  height: 100%;
}

.dialog-title-group {
  display: flex;
  align-items: baseline;
  gap: var(--spacing-3);
  flex: 1;
  min-width: 0;
}

.dialog-icon {
  font-size: 20px;
  color: rgba(255, 255, 255, 0.9);
  display: flex;
  align-items: center;
  flex-shrink: 0;
}

html.dark .dialog-icon {
  color: var(--color-primary-400);
}

.dialog-title-text {
  margin: 0;
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-semibold);
  color: white;
  line-height: 1.2;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.dialog-subtitle {
  font-size: var(--font-size-sm);
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.2;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  flex-shrink: 0;
}

.dialog-subtitle::before {
  content: '•';
  margin: 0 var(--spacing-2);
  color: rgba(255, 255, 255, 0.5);
}

.dialog-header__actions {
  display: flex;
  align-items: center;
  gap: var(--spacing-2);
  margin-left: var(--spacing-4);
}

.dialog-action-btn,
.dialog-close-btn {
  width: 32px;
  height: 32px;
  padding: 0;
  color: rgba(255, 255, 255, 0.8);
  border: none;
  background: rgba(255, 255, 255, 0.1);
  border-radius: var(--border-radius-md);
  transition: var(--transition-all-fast);
  margin-left: var(--spacing-1);
}

.dialog-action-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  color: white;
}

.dialog-close-btn:hover {
  background: var(--color-error-500);
  color: white;
}

/* 对话框主体 */
.base-dialog__body {
  padding: var(--dialog-padding, var(--spacing-5));
  background: var(--color-bg-primary);
  max-height: 60vh;
  overflow-y: auto;
}

/* 加载状态 */
.dialog-loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-8);
  gap: var(--spacing-4);
  color: var(--color-text-secondary);
}

.loading-icon {
  font-size: var(--font-size-2xl);
  animation: loading-rotate 1s linear infinite;
}

@keyframes loading-rotate {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-text {
  font-size: var(--font-size-base);
}

/* 对话框底部 */
.base-dialog__footer {
  padding: var(--dialog-padding, var(--spacing-5));
  background: var(--color-bg-primary);
  border-top: 1px solid var(--color-border-secondary);
}

.dialog-footer-default {
  display: flex;
  justify-content: flex-end;
  gap: var(--spacing-3);
}

/* 响应式调整 */
@media (max-width: 768px) {
  :deep(.base-dialog .el-dialog) {
    margin: var(--spacing-4) !important;
    width: calc(100% - var(--spacing-8)) !important;
  }
  
  .base-dialog__header {
    flex-direction: column;
    align-items: stretch;
    gap: var(--spacing-3);
  }
  
  .dialog-header__actions {
    margin-left: 0;
    justify-content: flex-end;
  }
  
  .dialog-footer-default {
    flex-direction: column-reverse;
  }
  
  .dialog-footer-default .el-button {
    width: 100%;
  }
}

/* 对话框底部 */
.base-dialog__footer {
  padding: var(--dialog-padding, var(--spacing-5));
  background: var(--color-bg-primary);
  border-top: 1px solid var(--color-border-secondary);
  margin: 0 calc(var(--dialog-padding, var(--spacing-5)) * -1) calc(var(--dialog-padding, var(--spacing-5)) * -1);
  border-radius: 0 0 var(--dialog-border-radius) var(--dialog-border-radius);
}


[data-theme="dark"] .base-dialog__body,
[data-theme="dark"] .base-dialog__footer {
  background: var(--color-bg-secondary);
  border-color: var(--color-border-secondary);
}

/* 模态框遮罩层优化 */
:deep(.el-dialog__wrapper) {
  backdrop-filter: blur(var(--backdrop-blur-sm));
}

/* 特殊对话框类型的图标颜色 */
:deep(.base-dialog--info) .dialog-icon {
  color: var(--color-info-500);
}

:deep(.base-dialog--success) .dialog-icon {
  color: var(--color-success-500);
}

:deep(.base-dialog--warning) .dialog-icon {
  color: var(--color-warning-500);
}

:deep(.base-dialog--danger) .dialog-icon {
  color: var(--color-error-500);
}
</style>