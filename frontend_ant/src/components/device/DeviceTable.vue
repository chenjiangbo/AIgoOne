<template>
  <div class="device-table-container">
    <a-table
      :data-source="devices"
      :columns="columns"
      :loading="loading"
      :pagination="paginationConfig"
      :row-selection="rowSelection"
      :scroll="{ y: tableHeight }"
      size="middle"
      class="device-table"
      row-key="id"
    >
      <!-- 设备信息列 -->
      <template #deviceInfo="{ record }">
        <div class="device-info">
          <div class="device-name">
            {{ record.name || '未命名设备' }}
          </div>
          <div class="device-url">
            {{ record.api_base_url }}
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
        <a-tooltip v-if="record.version" :title="record.version">
          <span class="version-text">{{ formatVersion(record.version) }}</span>
        </a-tooltip>
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
        <a-space>
          <a-button
            type="text"
            size="small"
            :loading="(record as any).syncing"
            @click="$emit('sync', record)"
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
          >
            <template #icon>
              <EditOutlined />
            </template>
            编辑
          </a-button>

          <a-button
            type="text"
            size="small"
            @click="$emit('view-details', record)"
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
          >
            <template #icon>
              <DeleteOutlined />
            </template>
            删除
          </a-button>
        </a-space>
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
    width: 150,
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
    title: '最后同步时间',
    dataIndex: 'last_sync_at',
    key: 'last_sync_at',
    width: 180,
    slots: { customRender: 'lastSync' }
  },
  {
    title: '操作',
    key: 'action',
    width: 280,
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

// 表格高度
const tableHeight = computed(() => {
  return Math.max(props.height - 100, 300) // 减去表头和分页的高度
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

// 格式化版本信息
const formatVersion = (version: string) => {
  if (!version) return '-'
  try {
    const versionObj = JSON.parse(version)
    return versionObj.version || versionObj.app_version || '未知版本'
  } catch {
    return version.length > 20 ? version.substring(0, 20) + '...' : version
  }
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
  padding: 0 24px 24px;
  background: var(--bg-primary);
  overflow: hidden;
}

.device-table {
  height: 100%;
}

.device-info .device-name {
  font-weight: 500;
  color: var(--text-primary);
  margin-bottom: 2px;
}

.device-info .device-url {
  font-size: 12px;
  color: var(--text-secondary);
  font-family: monospace;
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
  font-family: monospace;
  font-size: 13px;
}

.sync-time {
  font-size: 13px;
  color: var(--text-secondary);
}

.text-secondary {
  color: var(--text-secondary);
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
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border-color);
  font-weight: 600;
}

:deep(.ant-table-tbody > tr > td) {
  border-bottom: 1px solid var(--border-color);
}

:deep(.ant-table-tbody > tr:hover > td) {
  background: var(--hover-bg);
}

:deep(.ant-table-row-selected > td) {
  background: var(--color-primary-50);
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