<template>
  <BaseDialog
    :visible="visible"
    title="批量同步进度"
    subtitle="正在同步选中的设备，请稍候..."
    width="600px"
    size="medium"
    type="info"
    icon="Setting"
    :close-on-click-modal="false"
    :close-on-press-escape="false"
    @update:visible="$emit('update:visible', $event)"
  >
    <div class="batch-sync-progress">
      <div class="progress-header">
        <span class="progress-text">正在同步设备 {{ progress.current }} / {{ progress.total }}</span>
        <span class="progress-percentage">{{ Math.round((progress.current / progress.total) * 100) }}%</span>
      </div>
      
      <el-progress 
        :percentage="Math.round((progress.current / progress.total) * 100)"
        :status="progress.status"
        stroke-width="8"
        class="sync-progress-bar"
      />
      
      <div class="current-device" v-if="progress.currentDevice">
        <span class="current-label">当前设备:</span>
        <span class="current-name">{{ progress.currentDevice.name || progress.currentDevice.api_base_url }}</span>
      </div>
      
      <div class="progress-stats">
        <div class="stat-item success">
          <span class="stat-label">成功:</span>
          <span class="stat-value">{{ progress.success }}</span>
        </div>
        <div class="stat-item error">
          <span class="stat-label">失败:</span>
          <span class="stat-value">{{ progress.failed }}</span>
        </div>
      </div>
      
      <div class="progress-log" v-if="progress.logs.length > 0">
        <div class="log-header">同步日志:</div>
        <div class="log-content">
          <div 
            v-for="(log, index) in progress.logs.slice(-5)" 
            :key="index"
            class="log-item"
            :class="log.type"
          >
            <el-icon v-if="log.type === 'success'"><CircleCheck /></el-icon>
            <el-icon v-else-if="log.type === 'error'"><CircleClose /></el-icon>
            <el-icon v-else><Loading /></el-icon>
            <span class="log-message">{{ log.message }}</span>
          </div>
        </div>
      </div>
    </div>
    
    <template #footer>
      <el-button 
        v-if="progress.status === 'success' || progress.status === 'exception'"
        type="primary" 
        @click="$emit('close')"
      >
        完成
      </el-button>
      <el-button 
        v-if="progress.status === ''"
        type="warning" 
        @click="$emit('cancel')"
      >
        取消同步
      </el-button>
    </template>
  </BaseDialog>
</template>

<script setup>
import { CircleCheck, CircleClose, Loading } from '@element-plus/icons-vue'
import BaseDialog from '../ui/BaseDialog.vue'

// Props
const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  },
  progress: {
    type: Object,
    default: () => ({
      current: 0,
      total: 0,
      success: 0,
      failed: 0,
      status: '', // '', 'success', 'exception'
      currentDevice: null,
      logs: []
    })
  }
})

// Emits
const emit = defineEmits(['update:visible', 'close', 'cancel'])
</script>

<style scoped>
.batch-sync-progress {
  padding: var(--spacing-4);
}

.progress-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-4);
}

.progress-text {
  font-size: var(--font-size-base);
  color: var(--color-text-primary);
}

.progress-percentage {
  font-size: var(--font-size-xl);
  font-weight: var(--font-weight-semibold);
  color: var(--color-primary-500);
}

.sync-progress-bar {
  margin-bottom: var(--spacing-4);
}

.current-device {
  margin-bottom: var(--spacing-4);
  padding: var(--spacing-3);
  background: var(--color-bg-tertiary);
  border-radius: var(--border-radius-md);
  border-left: 3px solid var(--color-primary-500);
}

.current-label {
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
  margin-right: var(--spacing-2);
}

.current-name {
  font-family: var(--font-family-mono);
  color: var(--color-text-primary);
  font-weight: var(--font-weight-medium);
}

.progress-stats {
  display: flex;
  gap: var(--spacing-4);
  margin-bottom: var(--spacing-4);
}

.stat-item {
  padding: var(--spacing-2) var(--spacing-3);
  border-radius: var(--border-radius-md);
  border: 1px solid var(--color-border-primary);
  display: flex;
  align-items: center;
  gap: var(--spacing-1);
}

.stat-item.success {
  background: rgba(103, 194, 58, 0.1);
  border-color: var(--color-success-300);
}

.stat-item.error {
  background: rgba(245, 108, 108, 0.1);
  border-color: var(--color-error-300);
}

.stat-label {
  font-weight: var(--font-weight-medium);
  color: var(--color-text-secondary);
}

.stat-value {
  font-weight: var(--font-weight-semibold);
  font-size: var(--font-size-lg);
}

.stat-item.success .stat-value {
  color: var(--color-success-500);
}

.stat-item.error .stat-value {
  color: var(--color-error-500);
}

.progress-log {
  border-top: 1px solid var(--color-border-primary);
  padding-top: var(--spacing-4);
}

.log-header {
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
  margin-bottom: var(--spacing-3);
}

.log-content {
  max-height: 120px;
  overflow-y: auto;
  padding: var(--spacing-2);
  background: var(--color-bg-tertiary);
  border-radius: var(--border-radius-md);
  border: 1px solid var(--color-border-primary);
}

.log-item {
  display: flex;
  align-items: center;
  gap: var(--spacing-2);
  padding: var(--spacing-0_5) 0;
  font-size: var(--font-size-sm);
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}

.log-item:last-child {
  border-bottom: none;
}

.log-item.success .log-message {
  color: var(--color-success-500);
}

.log-item.error .log-message {
  color: var(--color-error-500);
}

.log-item.info .log-message {
  color: var(--color-text-secondary);
}

.log-item .el-icon {
  font-size: var(--font-size-base);
  flex-shrink: 0;
}

.log-message {
  flex: 1;
  line-height: 1.4;
}

/* 暗色主题适配 */
[data-theme="dark"] .current-device {
  background: var(--color-bg-primary);
  border-left-color: var(--color-primary-400);
}

[data-theme="dark"] .current-name {
  color: var(--color-text-primary);
}

[data-theme="dark"] .log-content {
  background: var(--color-bg-primary);
  border-color: var(--color-border-secondary);
}
</style>