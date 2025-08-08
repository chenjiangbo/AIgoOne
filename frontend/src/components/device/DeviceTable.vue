<template>
  <div class="device-table-container">
    <el-table 
      ref="tableRef"
      :data="devices" 
      v-loading="loading"
      stripe 
      @selection-change="handleSelectionChange"
      class="device-table"
      empty-text="暂无设备数据"
      :height="height"
      :row-class-name="getRowClassName"
      table-layout="fixed"
    >
      <el-table-column type="selection" width="50" fixed="left" />
      
      <el-table-column label="设备信息" width="380" fixed="left">
        <template #default="{ row }">
          <div class="device-info">
            <div class="device-header">
              <div class="device-name">
                <el-icon class="device-icon" :style="{ color: getStatusColor(row.status) }">
                  <Monitor />
                </el-icon>
                <span class="name-text">{{ row.name || '未知设备' }}</span>
              </div>
              <el-tag 
                :type="getStatusTagType(row.status)" 
                size="small"
                class="status-tag"
              >
                {{ getStatusText(row.status) }}
              </el-tag>
            </div>
            <div class="device-meta">
              <div class="meta-item">
                <span class="meta-label">地址:</span>
                <span class="meta-value">{{ truncateUrl(row.api_base_url) }}</span>
              </div>
              <div class="meta-item">
                <span class="meta-label">SN:</span>
                <span class="meta-value">{{ row.device_sn || '-' }}</span>
              </div>
            </div>
          </div>
        </template>
      </el-table-column>
      
      <el-table-column prop="device_type" label="设备类型" width="110">
        <template #default="{ row }">
          <el-tag :type="getTypeTagType(row.device_type)" size="small">
            {{ getTypeText(row.device_type) }}
          </el-tag>
        </template>
      </el-table-column>
      
      <el-table-column prop="version" label="软件版本" min-width="280">
        <template #default="{ row }">
          <div v-if="row.version" class="version-info">
            <pre class="version-text">{{ getVersionFirstLine(row.version) }}</pre>
          </div>
          <span v-else class="no-data">-</span>
        </template>
      </el-table-column>
      
      <el-table-column prop="last_sync_at" label="最后同步">
        <template #default="{ row }">
          <div class="sync-info">
            <span v-if="row.last_sync_at" class="sync-time">
              {{ formatTime(row.last_sync_at) }}
            </span>
            <span v-else class="no-sync">从未同步</span>
          </div>
        </template>
      </el-table-column>
      
      <el-table-column label="操作" width="130" fixed="right">
        <template #default="{ row }">
          <div class="action-icons">
            <el-tooltip content="同步设备信息" placement="top">
              <el-button 
                type="text" 
                class="action-icon-btn sync-btn"
                @click="$emit('sync', row)"
                :loading="row.syncing"
                :disabled="!row.api_base_url"
              >
                <el-icon><Download /></el-icon>
              </el-button>
            </el-tooltip>
            
            <el-tooltip content="编辑设备" placement="top">
              <el-button 
                type="text" 
                class="action-icon-btn edit-btn"
                @click="$emit('edit', row)"
              >
                <el-icon><Edit /></el-icon>
              </el-button>
            </el-tooltip>
            
            <el-tooltip content="查看详情" placement="top">
              <el-button 
                type="text" 
                class="action-icon-btn details-btn"
                @click="$emit('viewDetails', row)"
              >
                <el-icon><View /></el-icon>
              </el-button>
            </el-tooltip>
            
            <el-tooltip content="删除设备" placement="top">
              <el-button 
                type="text" 
                class="action-icon-btn delete-btn"
                @click="$emit('delete', row)"
              >
                <el-icon><Delete /></el-icon>
              </el-button>
            </el-tooltip>
          </div>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Monitor, View, Edit, Delete, Download } from '@element-plus/icons-vue'

// Props
const props = defineProps({
  devices: {
    type: Array,
    default: () => []
  },
  loading: {
    type: Boolean,
    default: false
  },
  height: {
    type: Number,
    default: 400
  }
})

// Emits
const emit = defineEmits(['selectionChange', 'sync', 'edit', 'viewDetails', 'delete'])

// 模板引用
const tableRef = ref()

// 工具方法
const getStatusColor = (status) => {
  const colors = {
    online: 'var(--color-success-500)',
    offline: 'var(--color-info-500)',
    error: 'var(--color-error-500)'
  }
  return colors[status] || 'var(--color-warning-500)'
}

const getStatusTagType = (status) => {
  const types = {
    online: 'success',
    offline: 'info',
    error: 'danger'
  }
  return types[status] || 'warning'
}

const getStatusText = (status) => {
  const texts = {
    online: '在线',
    offline: '离线',
    error: '错误'
  }
  return texts[status] || '未知'
}

const getTypeTagType = (type) => {
  const types = {
    edge_box: '',
    camera_server: 'success',
    ai_box: 'warning'
  }
  return types[type] || 'info'
}

const getTypeText = (type) => {
  const texts = {
    edge_box: '边缘盒子',
    camera_server: '摄像服务器',
    ai_box: 'AI盒子'
  }
  return texts[type] || type || '未知'
}

const truncateUrl = (url) => {
  if (!url) return '-'
  return url.length > 30 ? url.substring(0, 30) + '...' : url
}

const getVersionFirstLine = (version) => {
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
    return version.split('\n')[0]
  }
}

const formatTime = (timeString) => {
  if (!timeString) return null
  try {
    const date = new Date(timeString);
    if (isNaN(date.getTime())) {
      return timeString;
    }
    return date.toLocaleString('zh-CN', {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
    })
  } catch (error) {
    return timeString;
  }
}

const getRowClassName = ({ row }) => {
  let className = `status-${row.status}`
  if (row.justSynced) {
    className += ' just-synced'
  }
  return className
}

// 事件处理
const handleSelectionChange = (selection) => {
  emit('selectionChange', selection)
}

// 公开方法给父组件调用
const clearSelection = () => {
  if (tableRef.value) {
    tableRef.value.clearSelection()
  }
}

// 导出方法给父组件使用
defineExpose({
  clearSelection
})
</script>

<style scoped>
.device-table-container {
  flex: 1;
  padding: 0 var(--spacing-4) var(--spacing-6) var(--spacing-4);
  overflow: hidden;
}

.device-table {
  width: 100%;
  border-radius: var(--border-radius-lg);
  overflow: hidden;
}

/* 设备信息样式 */
.device-info {
  padding: var(--spacing-1) 0;
}

.device-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--spacing-2);
}

.device-name {
  display: flex;
  align-items: center;
  gap: var(--spacing-2);
}

.device-icon {
  font-size: var(--font-size-lg);
}

.name-text {
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
}

.status-tag {
  margin-left: var(--spacing-2);
}

.device-meta {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-1);
}

.meta-item {
  display: flex;
  align-items: center;
  gap: var(--spacing-1);
  font-size: var(--font-size-sm);
}

.meta-label {
  color: var(--color-text-secondary);
  min-width: 30px;
}

.meta-value {
  color: var(--color-text-tertiary);
  font-family: var(--font-family-mono);
}

/* 版本信息 */
.version-info {
  font-family: var(--font-family-mono);
  font-size: var(--font-size-xs);
}

.version-text {
  margin: 0;
  padding: 0;
  white-space: pre-line;
  line-height: 1.4;
  font-family: var(--font-family-mono);
  font-size: var(--font-size-sm);
  color: var(--color-text-tertiary);
}

/* 同步信息 */
.sync-info {
  font-size: var(--font-size-sm);
}

.sync-time {
  color: var(--color-text-secondary);
}

.no-sync {
  color: var(--color-error-500);
}

.no-data {
  color: var(--color-text-placeholder);
}

/* 操作按钮 */
.action-icons {
  display: flex;
  align-items: center;
  gap: var(--spacing-1);
  justify-content: center;
}

.action-icon-btn {
  width: 28px;
  height: 28px;
  padding: 0;
  border-radius: var(--border-radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition-all-fast);
}

.action-icon-btn:hover {
  transform: scale(1.1);
}

.sync-btn:hover {
  background-color: rgba(64, 158, 255, 0.1);
  color: var(--color-primary-500);
}

.edit-btn:hover {
  background-color: rgba(255, 193, 7, 0.1);
  color: var(--color-warning-500);
}

.details-btn:hover {
  background-color: rgba(103, 194, 58, 0.1);
  color: var(--color-success-500);
}

.delete-btn:hover {
  background-color: rgba(245, 108, 108, 0.1);
  color: var(--color-error-500);
}

/* 行状态样式 */
:deep(.el-table__row.status-online) {
  background-color: rgba(103, 194, 58, 0.05);
}

:deep(.el-table__row.status-offline) {
  background-color: rgba(144, 147, 153, 0.05);
}

:deep(.el-table__row.status-error) {
  background-color: rgba(245, 108, 108, 0.05);
}

:deep(.el-table__row.just-synced) {
  background-color: rgba(34, 197, 94, 0.15) !important;
  animation: syncSuccess 3s ease-out;
}

@keyframes syncSuccess {
  0% {
    background-color: rgba(34, 197, 94, 0.3);
    transform: scale(1.01);
  }
  50% {
    background-color: rgba(34, 197, 94, 0.25);
  }
  100% {
    background-color: rgba(34, 197, 94, 0.15);
    transform: scale(1);
  }
}
</style>