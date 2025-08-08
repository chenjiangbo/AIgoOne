<template>
  <a-modal
    v-model:open="visible"
    title="批量同步进度"
    width="600px"
    :closable="false"
    :mask-closable="false"
    class="batch-sync-modal"
  >
    <div class="sync-progress-content">
      <!-- 进度总览 -->
      <div class="progress-overview">
        <a-progress
          :percent="progressPercent"
          :status="progressStatus"
          :stroke-width="8"
          class="main-progress"
        />
        
        <div class="progress-stats">
          <a-row :gutter="16" justify="space-around">
            <a-col>
              <a-statistic
                title="总数"
                :value="progress.total"
                class="stat-item"
              />
            </a-col>
            <a-col>
              <a-statistic
                title="成功"
                :value="progress.success"
                :value-style="{ color: '#52c41a' }"
                class="stat-item"
              />
            </a-col>
            <a-col>
              <a-statistic
                title="失败"
                :value="progress.failed"
                :value-style="{ color: '#ff4d4f' }"
                class="stat-item"
              />
            </a-col>
            <a-col>
              <a-statistic
                title="进度"
                :value="progress.current"
                :suffix="`/ ${progress.total}`"
                class="stat-item"
              />
            </a-col>
          </a-row>
        </div>
      </div>

      <!-- 当前同步设备 -->
      <div v-if="progress.currentDevice && !isCompleted" class="current-device">
        <div class="current-device-header">
          <LoadingOutlined class="loading-icon" />
          <span class="current-text">正在同步：</span>
          <span class="device-name">
            {{ progress.currentDevice.name || progress.currentDevice.api_base_url }}
          </span>
        </div>
      </div>

      <!-- 同步日志 -->
      <div class="sync-logs">
        <div class="logs-header">
          <h4>同步日志</h4>
          <a-button
            type="text"
            size="small"
            @click="scrollToBottom"
          >
            <template #icon>
              <VerticalAlignBottomOutlined />
            </template>
            滚动到底部
          </a-button>
        </div>
        
        <div ref="logsContainer" class="logs-container">
          <div
            v-for="(log, index) in progress.logs"
            :key="index"
            class="log-item"
            :class="`log-${log.type}`"
          >
            <a-tag
              :color="getLogTagColor(log.type)"
              class="log-tag"
            >
              {{ getLogTagText(log.type) }}
            </a-tag>
            <span class="log-message">{{ log.message }}</span>
            <span class="log-time">{{ formatTime(new Date()) }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 底部按钮 -->
    <template #footer>
      <div class="modal-footer">
        <template v-if="!isCompleted">
          <a-button @click="handleCancel">
            取消同步
          </a-button>
        </template>
        
        <template v-else>
          <a-button type="primary" @click="handleClose">
            完成
          </a-button>
        </template>
      </div>
    </template>
  </a-modal>
</template>

<script setup lang="ts">
import { ref, computed, watch, nextTick } from 'vue'
import {
  LoadingOutlined,
  VerticalAlignBottomOutlined
} from '@ant-design/icons-vue'

interface SyncProgress {
  current: number
  total: number
  success: number
  failed: number
  status: '' | 'success' | 'exception'
  currentDevice: any
  logs: Array<{
    type: 'info' | 'success' | 'error'
    message: string
  }>
}

interface Props {
  visible: boolean
  progress: SyncProgress
}

const props = withDefaults(defineProps<Props>(), {
  visible: false,
  progress: () => ({
    current: 0,
    total: 0,
    success: 0,
    failed: 0,
    status: '',
    currentDevice: null,
    logs: []
  })
})

const emit = defineEmits<{
  'update:visible': [value: boolean]
  close: []
  cancel: []
}>()

const logsContainer = ref<HTMLElement>()

const visible = computed({
  get: () => props.visible,
  set: (value: boolean) => emit('update:visible', value)
})

// 进度百分比
const progressPercent = computed(() => {
  if (props.progress.total === 0) return 0
  return Math.round((props.progress.current / props.progress.total) * 100)
})

// 进度状态
const progressStatus = computed(() => {
  if (props.progress.status === 'success') return 'success'
  if (props.progress.status === 'exception') return 'exception'
  if (props.progress.current < props.progress.total) return 'active'
  return 'normal'
})

// 是否已完成
const isCompleted = computed(() => {
  return props.progress.current >= props.progress.total && props.progress.status !== ''
})

// 获取日志标签颜色
const getLogTagColor = (type: string) => {
  switch (type) {
    case 'info':
      return 'blue'
    case 'success':
      return 'green'
    case 'error':
      return 'red'
    default:
      return 'default'
  }
}

// 获取日志标签文本
const getLogTagText = (type: string) => {
  switch (type) {
    case 'info':
      return '信息'
    case 'success':
      return '成功'
    case 'error':
      return '错误'
    default:
      return '未知'
  }
}

// 格式化时间
const formatTime = (date: Date) => {
  return date.toLocaleTimeString('zh-CN', {
    hour12: false,
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  })
}

// 滚动到底部
const scrollToBottom = () => {
  nextTick(() => {
    if (logsContainer.value) {
      logsContainer.value.scrollTop = logsContainer.value.scrollHeight
    }
  })
}

// 关闭对话框
const handleClose = () => {
  emit('close')
}

// 取消同步
const handleCancel = () => {
  emit('cancel')
}

// 监听日志变化，自动滚动到底部
watch(() => props.progress.logs.length, () => {
  scrollToBottom()
}, { immediate: true })
</script>

<style scoped>
.sync-progress-content {
  padding: 8px 0;
}

.progress-overview {
  margin-bottom: 24px;
}

.main-progress {
  margin-bottom: 16px;
}

.progress-stats {
  padding: 16px;
  background: var(--bg-secondary);
  border-radius: 8px;
}

.stat-item :deep(.ant-statistic-title) {
  font-size: 12px;
  color: var(--text-secondary);
}

.stat-item :deep(.ant-statistic-content) {
  font-size: 20px;
  font-weight: 600;
}

.current-device {
  padding: 12px 16px;
  background: var(--color-primary-50);
  border: 1px solid var(--color-primary-200);
  border-radius: 8px;
  margin-bottom: 16px;
}

.current-device-header {
  display: flex;
  align-items: center;
  gap: 8px;
}

.loading-icon {
  color: var(--color-primary-500);
}

.current-text {
  font-weight: 500;
  color: var(--text-secondary);
}

.device-name {
  font-weight: 600;
  color: var(--text-primary);
}

.sync-logs {
  border: 1px solid var(--border-color);
  border-radius: 8px;
  overflow: hidden;
}

.logs-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border-color);
}

.logs-header h4 {
  margin: 0;
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
}

.logs-container {
  height: 240px;
  overflow-y: auto;
  background: var(--bg-primary);
  padding: 8px;
}

.log-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 6px 8px;
  border-radius: 4px;
  margin-bottom: 4px;
  font-size: 13px;
  transition: background-color 0.2s ease;
}

.log-item:hover {
  background: var(--hover-bg);
}

.log-item:last-child {
  margin-bottom: 0;
}

.log-tag {
  flex-shrink: 0;
  font-size: 11px;
  border-radius: 12px;
}

.log-message {
  flex: 1;
  color: var(--text-primary);
  line-height: 1.4;
}

.log-time {
  flex-shrink: 0;
  font-size: 11px;
  color: var(--text-secondary);
  font-family: monospace;
}

.log-info {
  border-left: 3px solid var(--color-primary-300);
}

.log-success {
  border-left: 3px solid var(--color-success-400);
}

.log-error {
  border-left: 3px solid var(--color-error-400);
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}

/* 自定义滚动条 */
.logs-container::-webkit-scrollbar {
  width: 6px;
}

.logs-container::-webkit-scrollbar-track {
  background: var(--bg-secondary);
  border-radius: 3px;
}

.logs-container::-webkit-scrollbar-thumb {
  background: var(--color-neutral-400);
  border-radius: 3px;
}

.logs-container::-webkit-scrollbar-thumb:hover {
  background: var(--color-neutral-500);
}

/* 暗色主题适配 */
html.dark .progress-stats {
  background: var(--bg-tertiary);
}

html.dark .current-device {
  background: var(--color-primary-900);
  border-color: var(--color-primary-700);
}

html.dark .sync-logs {
  border-color: var(--border-color-dark);
}

html.dark .logs-header {
  background: var(--bg-tertiary);
  border-bottom-color: var(--border-color-dark);
}

html.dark .logs-container {
  background: var(--bg-secondary);
}

html.dark .log-item:hover {
  background: var(--hover-bg-dark);
}
</style>