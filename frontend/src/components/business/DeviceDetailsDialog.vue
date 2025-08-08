<template>
  <BaseDialog
    :visible="visible"
    title="设备详情"
    subtitle="查看设备的详细信息和状态"
    width="900px"
    size="large"
    type="default"
    icon="InfoFilled"
    :draggable="true"
    :append-to-body="true"
    :modal="false"
    :body-style="{ padding: 0, maxHeight: '85vh', overflow: 'auto' }"
    @update:visible="$emit('update:visible', $event)"
  >
    <div v-if="device" class="device-details-content">
      <!-- 设备概览 -->
      <div class="device-overview">
        <div class="device-header">
          <div class="device-main-info">
            <el-icon class="device-main-icon" :style="{ color: getStatusColor(device.status) }">
              <Monitor />
            </el-icon>
            <div class="device-title-info">
              <h3 class="device-title">{{ device.name || '未知设备' }}</h3>
              <p class="device-address">{{ device.api_base_url }}</p>
            </div>
          </div>
          <div class="device-status-info">
            <el-tag 
              :type="getStatusTagType(device.status)" 
              size="large"
              class="status-tag-large"
            >
              {{ getStatusText(device.status) }}
            </el-tag>
            <div class="last-sync">
              最后同步: {{ formatTime(device.last_sync_at) || '从未同步' }}
            </div>
          </div>
        </div>
      </div>

      <!-- 详细信息卡片 -->
      <div class="details-grid">
        <!-- 基本信息 -->
        <el-card class="detail-card">
          <template #header>
            <div class="card-header">
              <el-icon><InfoFilled /></el-icon>
              <span>基本信息</span>
            </div>
          </template>
          <div class="detail-content">
            <div class="detail-row">
              <label>设备名称:</label>
              <span>{{ device.name || '-' }}</span>
            </div>
            <div class="detail-row">
              <label>设备类型:</label>
              <el-tag :type="getTypeTagType(device.device_type)" size="small">
                {{ getTypeText(device.device_type) }}
              </el-tag>
            </div>
            <div class="detail-row">
              <label>设备SN:</label>
              <span class="sn-text">{{ device.device_sn || '-' }}</span>
            </div>
            <div class="detail-row">
              <label>注册状态:</label>
              <span>{{ device.register_status || '-' }}</span>
            </div>
          </div>
        </el-card>


        <!-- 系统信息 */
        <el-card class="detail-card">
          <template #header>
            <div class="card-header">
              <el-icon><Monitor /></el-icon>
              <span>系统信息</span>
            </div>
          </template>
          <div class="detail-content">
            <div class="detail-row">
              <label>系统时间:</label>
              <span>{{ formatTime(device.system_time) || '-' }}</span>
            </div>
            <div class="detail-row">
              <label>系统更新:</label>
              <span>{{ formatTime(device.system_update) || '-' }}</span>
            </div>
            <div class="detail-row">
              <label>运行时间:</label>
              <span>{{ device.uptime || '-' }}</span>
            </div>
            <div class="detail-row">
              <label>系统负载:</label>
              <span>{{ device.system_load || '-' }}</span>
            </div>
          </div>
        </el-card>

        <!-- 业务信息 -->
        <el-card class="detail-card">
          <template #header>
            <div class="card-header">
              <el-icon><OfficeBuilding /></el-icon>
              <span>业务信息</span>
            </div>
          </template>
          <div class="detail-content">
            <div class="detail-row">
              <label>创建时间:</label>
              <span>{{ formatTime(device.created_at) || '-' }}</span>
            </div>
            <div class="detail-row">
              <label>更新时间:</label>
              <span>{{ formatTime(device.updated_at) || '-' }}</span>
            </div>
            <div class="detail-row">
              <label>备注信息:</label>
              <span>{{ device.description || '-' }}</span>
            </div>
          </div>
        </el-card>
      </div>

      <!-- 软件版本信息 -->
      <el-card class="detail-card version-card">
        <template #header>
          <div class="card-header">
            <el-icon><Document /></el-icon>
            <span>软件版本信息</span>
          </div>
        </template>
        <div class="version-content">
          <div class="version-lines">
            <div v-for="(line, index) in getFormattedVersion(device.version)" :key="index" class="version-line">
              {{ line }}
            </div>
          </div>
        </div>
      </el-card>

    </div>

    <template #footer>
      <div class="dialog-footer">
        <el-button @click="$emit('update:visible', false)">关闭</el-button>
      </div>
    </template>
  </BaseDialog>
</template>

<script setup>
import { ref, computed } from 'vue'
import { ElMessage } from 'element-plus'
import BaseDialog from '@/components/ui/BaseDialog.vue'
import {
  Monitor,
  InfoFilled,
  Connection,
  OfficeBuilding,
  Document,
  Refresh,
  Edit,
  View,
  Close
} from '@element-plus/icons-vue'

// Props
const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  },
  device: {
    type: Object,
    default: null
  },
  isDarkTheme: {
    type: Boolean,
    default: false
  }
})

// Emits
const emit = defineEmits(['update:visible'])

// 响应式状态
const syncing = ref(false)



// 工具方法
const getStatusColor = (status) => {
  const colors = {
    online: '#67c23a',
    offline: '#909399', 
    error: '#f56c6c'
  }
  return colors[status] || '#e6a23c'
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

const getFormattedVersion = (version) => {
  if (!version) return ['暂无版本信息']
  try {
    const parsed = JSON.parse(version);
    const versions = [];
    if (parsed.Engine) versions.push(`Engine: ${parsed.Engine}`);
    if (parsed.Inflet) versions.push(`Inflet: ${parsed.Inflet}`);
    if (parsed.Web) versions.push(`Web: ${parsed.Web}`);
    return versions.length > 0 ? versions : ['暂无版本信息'];
  } catch (e) {
    return [version];
  }
}


// 事件处理
const syncDevice = async () => {
  if (!props.device) return
  
  syncing.value = true
  try {
    // TODO: 调用后端API同步设备
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    ElMessage.success('设备同步成功')
    
    // 更新设备信息
    props.device.last_sync_at = new Date().toISOString()
    props.device.status = 'online'
  } catch (error) {
    ElMessage.error(`同步失败: ${error.message}`)
  } finally {
    syncing.value = false
  }
}

const editDevice = () => {
  ElMessage.info('编辑设备功能开发中...')
  // TODO: 实现设备编辑功能
}
</script>

<style scoped>
.device-details-dialog {
  --el-dialog-padding-primary: 0;
}

:deep(.device-details-dialog .el-dialog__body) {
  padding: 0;
}

.device-details-content {
  padding: var(--spacing-4);
}

/* 设备概览 */
.device-overview {
  margin-bottom: var(--spacing-4);
}

.device-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: var(--spacing-4);
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: var(--border-radius-lg);
  color: white;
}

.device-main-info {
  display: flex;
  align-items: center;
  gap: 16px;
}

.device-main-icon {
  font-size: 32px;
  color: #dbeafe;
}

.device-title-info {
  flex: 1;
}

.device-title {
  margin: 0 0 8px 0;
  font-size: 20px;
  font-weight: 600;
}

.device-address {
  margin: 0;
  font-size: 14px;
  opacity: 0.9;
  font-family: 'Courier New', monospace;
}

.device-status-info {
  text-align: right;
}

.status-tag-large {
  margin-bottom: 8px;
  font-size: 14px;
  padding: 6px 12px;
}

.last-sync {
  font-size: 12px;
  opacity: 0.8;
}

/* 详情网格 */
.details-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--spacing-4);
  margin-bottom: var(--spacing-4);
}

@media (max-width: 1024px) {
  .details-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .details-grid {
    grid-template-columns: 1fr;
  }
}

.detail-card {
  border-radius: 8px;
  overflow: hidden;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
}

.detail-content {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-2);
}

.detail-row {
  display: flex;
  align-items: center;
  gap: var(--spacing-3);
}

.detail-row label {
  font-weight: 500;
  color: #374151;
  min-width: 80px;
  flex-shrink: 0;
}

.device-details-dialog:deep(html.dark) .detail-row label {
  color: #d1d5db;
}

.sn-text {
  font-family: 'Courier New', monospace;
  font-size: 13px;
  color: #4b5563;
}

.device-details-dialog:deep(html.dark) .sn-text {
  color: #d1d5db;
}

/* 版本信息卡片 */
.version-card {
  grid-column: 1 / -1;
  margin-top: var(--spacing-2);
}

.version-content {
  max-height: 120px;
  overflow-y: auto;
}

.version-lines {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-1);
}

.version-line {
  font-family: 'Courier New', monospace;
  font-size: var(--font-size-xs);
  color: #4b5563;
  padding: var(--spacing-2) var(--spacing-3);
  background: #f8fafc;
  border-radius: var(--border-radius-sm);
  border-left: 3px solid #3b82f6;
}

.device-details-dialog:deep(html.dark) .version-line {
  color: #d1d5db;
  background: #1f2937;
  border-left-color: #60a5fa;
}

.version-detail {
  font-family: 'Courier New', monospace;
  font-size: 12px;
  color: #4b5563;
  white-space: pre-wrap;
  line-height: 1.5;
  margin: 0;
  padding: 12px;
  background: #f8fafc;
  border-radius: 6px;
  border: 1px solid #e5e7eb;
}

.device-details-dialog:deep(html.dark) .version-detail {
  color: #d1d5db;
  background: #1f2937;
  border-color: #374151;
}



/* 对话框底部 */
.dialog-footer {
  display: flex;
  justify-content: flex-end;
  gap: var(--spacing-3);
  padding: var(--spacing-4);
  background: var(--color-bg-secondary);
  margin: 0 calc(var(--spacing-4) * -1) calc(var(--spacing-4) * -1);
  border-radius: 0 0 var(--border-radius-lg) var(--border-radius-lg);
}

.device-details-dialog:deep(html.dark) .dialog-footer {
  background: #1f2937;
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .details-grid {
    grid-template-columns: 1fr;
  }
  
  .device-header {
    flex-direction: column;
    gap: 16px;
    text-align: center;
  }
  
  .device-main-info {
    justify-content: center;
  }
  
  .device-status-info {
    text-align: center;
  }
}

@media (max-width: 768px) {
  .device-details-content {
    padding: 12px;
  }
  
  .detail-row {
    flex-direction: column;
    align-items: flex-start;
    gap: 4px;
  }
  
  .detail-row label {
    min-width: auto;
  }
  
  .dialog-footer {
    flex-direction: column;
    gap: 8px;
  }
  
  .dialog-footer .el-button {
    width: 100%;
  }
}
</style>