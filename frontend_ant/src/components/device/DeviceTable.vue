<template>
  <div class="device-table-container">
    <a-table
      :data-source="devices"
      :columns="columns"
      :loading="loading"
      :pagination="paginationConfig"
      :row-selection="rowSelection"
      :scroll="{ y: tableHeight, x: 'max-content' }"
      size="middle"
      class="device-table"
      row-key="id"
    >
      <!-- 设备信息列 -->
      <template #deviceInfo="{ record }">
        <div class="device-info" :class="`device-status-${record.status}`">
          <div class="device-name" :data-status="record.status">
            {{ record.name || '未命名设备' }}
          </div>
          <div class="device-meta">
            <div class="meta-item">
              <span class="meta-label">地址:</span>
              <span class="meta-value">{{ truncateUrl(record.api_base_url) }}</span>
            </div>
            <div class="meta-item" v-if="record.device_sn">
              <span class="meta-label">SN:</span>
              <span class="meta-value">{{ record.device_sn }}</span>
            </div>
          </div>
        </div>
      </template>

      <!-- 设备类型列 -->
      <template #deviceType="{ record }">
        <a-tag v-if="record.device_type" color="blue">
          {{ record.device_type }}
        </a-tag>
        <span v-else class="text-secondary">-</span>
      </template>

      <!-- 软件版本列 -->
      <template #version="{ record }">
        <div v-if="record.version" class="version-info">
          <pre class="version-text">{{ formatVersion(record.version) }}</pre>
        </div>
        <span v-else class="text-secondary">-</span>
      </template>

      <!-- 状态列 -->
      <template #status="{ record }">
        <div class="status-cell" :class="{ syncing: (record as any).syncing, 'just-synced': (record as any).justSynced }">
          <a-badge
            :status="getStatusBadge(record.status)"
            :text="getStatusText(record.status)"
          />
          <LoadingOutlined v-if="(record as any).syncing" class="sync-loading" />
        </div>
      </template>

      <!-- 最后同步时间列 -->
      <template #lastSync="{ record }">
        <div v-if="record.last_sync_at" class="sync-time">
          {{ formatTime(record.last_sync_at) }}
        </div>
        <span v-else class="text-secondary">从未同步</span>
      </template>

      <!-- 操作列 -->
      <template #action="{ record }">
        <div class="action-buttons">
          <div class="action-row">
            <a-button
              type="text"
              size="small"
              :loading="(record as any).syncing"
              @click="$emit('sync', record)"
              class="action-btn"
            >
              <template #icon>
                <SyncOutlined />
              </template>
              同步
            </a-button>

            <a-button
              type="text"
              size="small"
              @click="$emit('edit', record)"
              class="action-btn"
            >
              <template #icon>
                <EditOutlined />
              </template>
              编辑
            </a-button>
          </div>
          
          <div class="action-row">
            <a-button
              type="text"
              size="small"
              @click="$emit('view-details', record)"
              class="action-btn"
            >
              <template #icon>
                <EyeOutlined />
              </template>
              详情
            </a-button>

            <a-button
              type="text"
              size="small"
              danger
              @click="$emit('delete', record)"
              class="action-btn"
            >
              <template #icon>
                <DeleteOutlined />
              </template>
              删除
            </a-button>
          </div>
        </div>
      </template>
    </a-table>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import type { TableColumnsType } from 'ant-design-vue'
import {
  SyncOutlined,
  EditOutlined,
  EyeOutlined,
  DeleteOutlined,
  LoadingOutlined
} from '@ant-design/icons-vue'
import type { Device } from '@/api/device'

interface Props {
  devices: Device[]
  loading?: boolean
  height?: number
}

const props = withDefaults(defineProps<Props>(), {
  devices: () => [],
  loading: false,
  height: 400
})

const emit = defineEmits<{
  'selection-change': [selectedDevices: Device[]]
  sync: [device: Device]
  edit: [device: Device]
  'view-details': [device: Device]
  delete: [device: Device]
}>()

const selectedRowKeys = ref<number[]>([])

// 表格列配置
const columns: TableColumnsType = [
  {
    title: '设备信息',
    dataIndex: 'deviceInfo',
    key: 'deviceInfo',
    width: 250,
    ellipsis: true,
    slots: { customRender: 'deviceInfo' }
  },
  {
    title: '设备类型',
    dataIndex: 'device_type',
    key: 'device_type',
    width: 120,
    align: 'center',
    slots: { customRender: 'deviceType' }
  },
  {
    title: '软件版本',
    dataIndex: 'version',
    key: 'version',
    width: 220,
    ellipsis: true,
    slots: { customRender: 'version' }
  },
  {
    title: '状态',
    dataIndex: 'status',
    key: 'status',
    width: 120,
    align: 'center',
    slots: { customRender: 'status' }
  },
  {
    title: '最后同步',
    dataIndex: 'last_sync_at',
    key: 'last_sync_at',
    width: 140,
    slots: { customRender: 'lastSync' }
  },
  {
    title: '操作',
    key: 'action',
    width: 180,
    fixed: 'right',
    align: 'center',
    slots: { customRender: 'action' }
  }
]

// 行选择配置
const rowSelection = computed(() => ({
  selectedRowKeys: selectedRowKeys.value,
  onChange: (keys: number[], selectedRows: Device[]) => {
    selectedRowKeys.value = keys
    emit('selection-change', selectedRows)
  },
  getCheckboxProps: (record: Device) => ({
    disabled: (record as any).syncing
  })
}))

// 分页配置
const paginationConfig = computed(() => ({
  total: props.devices.length,
  pageSize: 20,
  showSizeChanger: true,
  showQuickJumper: true,
  showTotal: (total: number, range: [number, number]) =>
    `第 ${range[0]}-${range[1]} 项，共 ${total} 项`,
  pageSizeOptions: ['10', '20', '50', '100']
}))

// 表格高度 - 自动计算，确保充满容器
const tableHeight = computed(() => {
  return 'calc(70vh - 200px)' // 70%视口高度减去头部和工具栏
})

// 清除选择
const clearSelection = () => {
  selectedRowKeys.value = []
  emit('selection-change', [])
}

// 获取状态徽章类型
const getStatusBadge = (status: string) => {
  switch (status) {
    case 'online':
      return 'success'
    case 'offline':
      return 'default'
    case 'error':
      return 'error'
    default:
      return 'default'
  }
}

// 获取状态文本
const getStatusText = (status: string) => {
  switch (status) {
    case 'online':
      return '在线'
    case 'offline':
      return '离线'
    case 'error':
      return '验证失败'
    default:
      return '未知'
  }
}

// 格式化版本信息 - 参考原前端实现
const formatVersion = (version: string) => {
  if (!version) return '-'
  try {
    const parsed = JSON.parse(version);
    const versions = [];
    if (parsed.Engine) {
      versions.push(`Engine: ${parsed.Engine}`);
    }
    if (parsed.Inflet) {
      versions.push(`Inflet: ${parsed.Inflet}`);
    }
    if (parsed.Web) {
      versions.push(`Web: ${parsed.Web}`);
    }
    return versions.join('\n') || '-';
  } catch (e) {
    return version.split('\n')[0] || version
  }
}

// 截断URL显示
const truncateUrl = (url: string) => {
  if (!url) return '-'
  return url.length > 35 ? url.substring(0, 35) + '...' : url
}

// 格式化时间
const formatTime = (timestamp: string) => {
  if (!timestamp) return '-'
  const date = new Date(timestamp)
  return date.toLocaleString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  })
}

// 暴露方法给父组件
defineExpose({
  clearSelection
})
</script>

<style scoped>
.device-table-container {
  flex: 1;
  padding: 24px 24px 24px;
  background: var(--bg-primary);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.device-table {
  flex: 1;
}

:deep(.ant-table-wrapper) {
  height: 100%;
}

:deep(.ant-table) {
  height: 100%;
}

:deep(.ant-table-container) {
  height: calc(100% - 60px); /* 减去分页组件的高度 */
}

:deep(.ant-table-tbody) {
  min-height: 200px;
}

.device-info {
  padding: 6px 0;
  position: relative;
}

.device-info .device-name {
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 8px;
  font-size: 15px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.device-info .device-name::before {
  content: '';
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-neutral-400);
  flex-shrink: 0;
  transition: all 0.3s ease;
  animation: pulse 2s infinite;
}

/* 基于设备状态的动态指示器 */
.device-name[data-status="online"]::before {
  background: var(--color-success-500);
  box-shadow: 0 0 8px rgba(82, 196, 26, 0.6);
}

.device-name[data-status="offline"]::before {
  background: var(--color-neutral-400);
  box-shadow: none;
  animation: none;
}

.device-name[data-status="error"]::before {
  background: var(--color-error-500);
  box-shadow: 0 0 8px rgba(255, 77, 79, 0.6);
  animation: pulse-error 1.5s infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
    transform: scale(1);
  }
  50% {
    opacity: 0.7;
    transform: scale(1.1);
  }
}

@keyframes pulse-error {
  0%, 100% {
    opacity: 1;
    transform: scale(1);
    box-shadow: 0 0 8px rgba(255, 77, 79, 0.6);
  }
  50% {
    opacity: 0.8;
    transform: scale(1.15);
    box-shadow: 0 0 12px rgba(255, 77, 79, 0.8);
  }
}

/* 设备状态相关样式 */
.device-status-online {
  border-left: 2px solid var(--color-success-200);
}

.device-status-offline {
  border-left: 2px solid var(--color-neutral-200);
}

.device-status-error {
  border-left: 2px solid var(--color-error-200);
}

.device-meta {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  padding: 1px 0;
  transition: all 0.2s ease;
}

.meta-item:hover {
  background: rgba(64, 169, 255, 0.05);
  border-radius: 4px;
  padding: 2px 6px;
}

.meta-label {
  color: var(--text-secondary);
  min-width: 32px;
  font-size: 12px;
  font-weight: 500;
}

.meta-value {
  color: var(--text-tertiary);
  font-family: 'JetBrains Mono', 'Consolas', monospace;
  font-size: 12px;
  background: rgba(0, 0, 0, 0.05);
  padding: 1px 4px;
  border-radius: 3px;
  transition: all 0.2s ease;
}

html.dark .meta-value {
  background: rgba(255, 255, 255, 0.1);
}

.version-info {
  font-family: monospace;
  font-size: 13px;
}

.status-cell {
  position: relative;
  transition: all 0.3s ease;
}

.status-cell.syncing {
  background: rgba(24, 144, 255, 0.1);
  border-radius: 4px;
  padding: 2px 8px;
}

.status-cell.just-synced {
  background: rgba(82, 196, 26, 0.1);
  border-radius: 4px;
  padding: 2px 8px;
  animation: highlight 2s ease-out;
}

.sync-loading {
  margin-left: 8px;
  color: var(--color-primary-500);
}

.version-text {
  margin: 0;
  padding: 6px 8px;
  white-space: pre-line;
  line-height: 1.4;
  font-family: 'JetBrains Mono', 'Consolas', monospace;
  font-size: 12px;
  color: var(--text-tertiary);
  background: var(--bg-secondary);
  border-radius: 6px;
  border-left: 3px solid var(--color-primary-300);
  transition: all 0.2s ease;
}

.version-text:hover {
  background: var(--color-primary-50);
  border-left-color: var(--color-primary-500);
  transform: translateX(2px);
}

html.dark .version-text {
  background: var(--bg-tertiary);
  border-left-color: var(--color-primary-600);
}

html.dark .version-text:hover {
  background: var(--color-primary-900);
  border-left-color: var(--color-primary-400);
}

.sync-time {
  font-size: 13px;
  color: var(--text-secondary);
}

.text-secondary {
  color: var(--text-secondary);
}

/* 操作按钮样式 */
.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 4px;
  align-items: center;
}

.action-row {
  display: flex;
  gap: 4px;
  justify-content: center;
}

.action-btn {
  font-size: 12px;
  height: 28px;
  padding: 0 8px;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.action-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

@keyframes highlight {
  0% {
    background: rgba(82, 196, 26, 0.3);
  }
  100% {
    background: rgba(82, 196, 26, 0.1);
  }
}

/* 表格样式优化 */
:deep(.ant-table-thead > tr > th) {
  background: linear-gradient(135deg, var(--bg-secondary), var(--bg-tertiary));
  border-bottom: 2px solid var(--color-primary-200);
  font-weight: 600;
  color: var(--text-primary);
  transition: all 0.3s ease;
}

:deep(.ant-table-tbody > tr > td) {
  border-bottom: 1px solid var(--border-color);
  transition: all 0.2s ease;
}

:deep(.ant-table-tbody > tr) {
  transition: all 0.2s ease;
}

:deep(.ant-table-tbody > tr:hover) {
  background: linear-gradient(135deg, var(--color-primary-25), var(--color-primary-50)) !important;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(64, 169, 255, 0.15);
}

:deep(.ant-table-tbody > tr:hover > td) {
  border-bottom-color: var(--color-primary-200);
}

:deep(.ant-table-row-selected > td) {
  background: linear-gradient(135deg, var(--color-primary-50), var(--color-primary-100)) !important;
  border-left: 4px solid var(--color-primary-500);
}

html.dark :deep(.ant-table-thead > tr > th) {
  background: linear-gradient(135deg, var(--bg-tertiary), var(--bg-quaternary));
  border-bottom-color: var(--color-primary-700);
}

html.dark :deep(.ant-table-tbody > tr:hover) {
  background: linear-gradient(135deg, var(--color-primary-950), var(--color-primary-900)) !important;
  box-shadow: 0 4px 12px rgba(64, 169, 255, 0.25);
}

html.dark :deep(.ant-table-row-selected > td) {
  background: linear-gradient(135deg, var(--color-primary-900), var(--color-primary-800)) !important;
}

/* 暗色主题适配 */
html.dark .device-table-container {
  background: var(--bg-secondary);
}

html.dark :deep(.ant-table-thead > tr > th) {
  background: var(--bg-tertiary);
  border-bottom-color: var(--border-color-dark);
}

html.dark :deep(.ant-table-tbody > tr > td) {
  border-bottom-color: var(--border-color-dark);
}

html.dark :deep(.ant-table-tbody > tr:hover > td) {
  background: var(--hover-bg-dark);
}

html.dark :deep(.ant-table-row-selected > td) {
  background: var(--color-primary-900);
}

/* 响应式调整 */
@media (max-width: 768px) {
  .device-table-container {
    padding: 0 16px 16px;
  }
  
  :deep(.ant-table-action-column) {
    width: 240px !important;
  }
  
  :deep(.ant-space) {
    flex-wrap: wrap;
  }
}
</style>