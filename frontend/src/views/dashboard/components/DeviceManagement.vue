<template>
  <div class="device-management">
    <!-- 页面头部 -->
    <div class="page-header">
      <div class="header-left">
        <h2 class="page-title">设备管理</h2>
        <p class="page-description">管理AI算法平台设备，同步设备信息和状态</p>
      </div>
      <div class="header-actions">
        <el-button @click="refreshDevices">
          <el-icon><Refresh /></el-icon>
          刷新
        </el-button>
        <el-button type="primary" @click="showAddDeviceDialog">
          <el-icon><Plus /></el-icon>
          添加设备
        </el-button>
        <el-button 
          type="warning" 
          :disabled="selectedDevices.length === 0"
          @click="batchSyncDevices"
          :loading="batchSyncing"
        >
          <el-icon><Download /></el-icon>
          批量同步 ({{ selectedDevices.length }})
        </el-button>
      </div>
    </div>

    <!-- 设备列表 -->
    <div class="device-list" v-loading="loading">
      <el-table 
        :data="devices" 
        stripe 
        @selection-change="handleSelectionChange"
        class="device-table"
        empty-text="暂无设备数据"
      >
        <el-table-column type="selection" width="50" />
        
        <el-table-column prop="name" label="设备名称" width="200">
          <template #default="{ row }">
            <div class="device-name">
              <el-icon class="device-icon" :style="{ color: getStatusColor(row.status) }">
                <Monitor />
              </el-icon>
              <span>{{ row.name || '未知设备' }}</span>
            </div>
          </template>
        </el-table-column>
        
        <el-table-column prop="api_base_url" label="设备地址" width="200">
          <template #default="{ row }">
            <el-link :href="row.api_base_url" target="_blank" style="font-size: 12px;">
              {{ row.api_base_url }}
            </el-link>
          </template>
        </el-table-column>
        
        <el-table-column prop="device_type" label="设备类型" width="120">
          <template #default="{ row }">
            <el-tag :type="getTypeTagType(row.device_type)" size="small">
              {{ row.device_type || '未知' }}
            </el-tag>
          </template>
        </el-table-column>
        
        <el-table-column prop="status" label="状态" width="100">
          <template #default="{ row }">
            <el-tag 
              :type="getStatusTagType(row.status)" 
              size="small"
              :icon="getStatusIcon(row.status)"
            >
              {{ getStatusText(row.status) }}
            </el-tag>
          </template>
        </el-table-column>
        
        <el-table-column prop="device_sn" label="设备SN" width="150">
          <template #default="{ row }">
            <span class="device-sn">{{ row.device_sn || '-' }}</span>
          </template>
        </el-table-column>
        
        <el-table-column prop="version" label="软件版本" width="120">
          <template #default="{ row }">
            <el-tooltip 
              v-if="row.version" 
              :content="row.version" 
              placement="top"
              effect="dark"
            >
              <span class="version-text">{{ truncateVersion(row.version) }}</span>
            </el-tooltip>
            <span v-else>-</span>
          </template>
        </el-table-column>
        
        <el-table-column prop="last_sync_at" label="最后同步" width="150">
          <template #default="{ row }">
            <span v-if="row.last_sync_at" class="sync-time">
              {{ formatTime(row.last_sync_at) }}
            </span>
            <span v-else class="no-sync">从未同步</span>
          </template>
        </el-table-column>
        
        <el-table-column label="操作" width="240" fixed="right">
          <template #default="{ row }">
            <div class="action-buttons">
              <el-button 
                size="small" 
                @click="syncDevice(row)"
                :loading="row.syncing"
                :disabled="!row.api_base_url"
              >
                <el-icon><Download /></el-icon>
                同步
              </el-button>
              <el-button size="small" @click="viewDeviceDetails(row)">
                <el-icon><View /></el-icon>
                详情
              </el-button>
              <el-button size="small" type="danger" @click="deleteDevice(row)">
                <el-icon><Delete /></el-icon>
                删除
              </el-button>
            </div>
          </template>
        </el-table-column>
        
        <!-- 展开行显示详细信息 -->
        <el-table-column type="expand">
          <template #default="{ row }">
            <div class="device-details">
              <div class="detail-grid">
                <div class="detail-item">
                  <label>注册状态:</label>
                  <span>{{ row.register_status || '未知' }}</span>
                </div>
                <div class="detail-item">
                  <label>系统更新:</label>
                  <span>{{ row.system_update || '-' }}</span>
                </div>
                <div class="detail-item">
                  <label>系统时间:</label>
                  <span>{{ row.system_time || '-' }}</span>
                </div>
                <div class="detail-item">
                  <label>网络设置:</label>
                  <span>{{ row.network_setting || '-' }}</span>
                </div>
                <div class="detail-item full-width">
                  <label>软件版本详情:</label>
                  <pre class="version-detail">{{ row.version || '暂无版本信息' }}</pre>
                </div>
              </div>
            </div>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <!-- 添加设备对话框 -->
    <el-dialog
      v-model="addDeviceVisible"
      title="添加设备"
      width="600px"
      :before-close="handleAddDeviceClose"
      center
    >
      <el-form
        ref="addDeviceFormRef"
        :model="addDeviceForm"
        :rules="addDeviceRules"
        label-width="120px"
        style="padding: 20px;"
      >
        <el-form-item label="设备地址" prop="api_base_url">
          <el-input 
            v-model="addDeviceForm.api_base_url" 
            placeholder="请输入设备API地址，如: http://192.168.1.100:8080"
          />
          <div class="form-tip">
            请输入算法应用平台的完整地址，包含协议和端口
          </div>
        </el-form-item>
        
        <el-form-item label="用户名" prop="username">
          <el-input v-model="addDeviceForm.username" placeholder="请输入设备登录用户名" />
        </el-form-item>
        
        <el-form-item label="密码" prop="password">
          <el-input 
            v-model="addDeviceForm.password" 
            type="password" 
            show-password 
            placeholder="请输入设备登录密码"
          />
        </el-form-item>
        
        <el-form-item label="业务节点" prop="business_node_id">
          <el-select 
            v-model="addDeviceForm.business_node_id" 
            placeholder="请选择关联的业务节点"
            style="width: 100%;"
          >
            <el-option
              v-for="node in leafBusinessNodes"
              :key="node.id"
              :label="node.name"
              :value="node.id"
            />
          </el-select>
        </el-form-item>
      </el-form>
      
      <template #footer>
        <div style="text-align: right;">
          <el-button @click="addDeviceVisible = false">取消</el-button>
          <el-button 
            type="primary" 
            :loading="addingDevice" 
            @click="handleAddDevice"
          >
            {{ addingDevice ? '连接中...' : '添加设备' }}
          </el-button>
        </div>
      </template>
    </el-dialog>

    <!-- 设备详情对话框 -->
    <el-dialog
      v-model="deviceDetailsVisible"
      :title="currentDevice?.name || '设备详情'"
      width="800px"
      center
    >
      <div v-if="currentDevice" class="device-info-panel">
        <div class="info-sections">
          <el-card header="基本信息" class="info-card">
            <div class="info-grid">
              <div class="info-item">
                <label>设备名称:</label>
                <span>{{ currentDevice.name || '-' }}</span>
              </div>
              <div class="info-item">
                <label>设备类型:</label>
                <span>{{ currentDevice.device_type || '-' }}</span>
              </div>
              <div class="info-item">
                <label>设备SN:</label>
                <span>{{ currentDevice.device_sn || '-' }}</span>
              </div>
              <div class="info-item">
                <label>注册状态:</label>
                <span>{{ currentDevice.register_status || '-' }}</span>
              </div>
            </div>
          </el-card>
          
          <el-card header="网络信息" class="info-card">
            <div class="info-grid">
              <div class="info-item">
                <label>设备地址:</label>
                <span>{{ currentDevice.api_base_url || '-' }}</span>
              </div>
              <div class="info-item">
                <label>网络设置:</label>
                <span>{{ currentDevice.network_setting || '-' }}</span>
              </div>
              <div class="info-item">
                <label>连接状态:</label>
                <el-tag :type="getStatusTagType(currentDevice.status)">
                  {{ getStatusText(currentDevice.status) }}
                </el-tag>
              </div>
              <div class="info-item">
                <label>最后同步:</label>
                <span>{{ formatTime(currentDevice.last_sync_at) || '从未同步' }}</span>
              </div>
            </div>
          </el-card>
          
          <el-card header="系统信息" class="info-card">
            <div class="info-grid">
              <div class="info-item">
                <label>系统时间:</label>
                <span>{{ currentDevice.system_time || '-' }}</span>
              </div>
              <div class="info-item">
                <label>系统更新:</label>
                <span>{{ currentDevice.system_update || '-' }}</span>
              </div>
              <div class="info-item full-width">
                <label>软件版本:</label>
                <pre class="version-detail">{{ currentDevice.version || '-' }}</pre>
              </div>
            </div>
          </el-card>
        </div>
      </div>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import {
  Plus,
  Refresh,
  Download,
  Monitor,
  View,
  Delete,
  CircleCheck,
  CircleClose,
  Clock
} from '@element-plus/icons-vue'

// Props
const props = defineProps({
  isDarkTheme: {
    type: Boolean,
    default: false
  }
})

// 状态管理
const loading = ref(false)
const devices = ref([])
const selectedDevices = ref([])
const batchSyncing = ref(false)

// 添加设备相关
const addDeviceVisible = ref(false)
const addingDevice = ref(false)
const addDeviceFormRef = ref()

// 设备详情相关
const deviceDetailsVisible = ref(false)
const currentDevice = ref(null)

// 表单数据
const addDeviceForm = reactive({
  api_base_url: '',
  username: '',
  password: '',
  business_node_id: null
})

// 表单验证规则
const addDeviceRules = {
  api_base_url: [
    { required: true, message: '请输入设备API地址', trigger: 'blur' },
    {
      pattern: /^https?:\/.+\/, 
      message: '请输入有效的URL地址',
      trigger: 'blur'
    }
  ],
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' }
  ],
  business_node_id: [
    { required: true, message: '请选择业务节点', trigger: 'change' }
  ]
}

// Mock业务节点数据（叶子节点）
const leafBusinessNodes = ref([
  { id: 'parking-1', name: '虹桥机场T1停车场' },
  { id: 'parking-2', name: '虹桥机场T2停车场' },
  { id: 'parking-3', name: '萧山国际机场停车场' },
  { id: 'parking-4', name: '首都机场T3停车场' }
])

// Mock设备数据
const mockDevices = [
  {
    id: 1,
    name: '华东区域-01号设备',
    api_base_url: 'http://192.168.1.100:8080',
    device_type: 'edge_box',
    status: 'online',
    device_sn: 'SN20240001',
    version: 'v2.1.0\nBuild: 20240315-1234\nKernel: Linux 5.4.0',
    register_status: '已注册',
    system_update: '2024-03-15 14:30:00',
    system_time: '2024-03-16 10:30:00',
    network_setting: 'DHCP自动获取',
    last_sync_at: '2024-03-16 09:15:30',
    business_node_id: 'parking-1'
  },
  {
    id: 2,
    name: '华东区域-02号设备',
    api_base_url: 'http://192.168.1.101:8080',
    device_type: 'camera_server',
    status: 'offline',
    device_sn: 'SN20240002',
    version: 'v2.0.5\nBuild: 20240301-5678\nKernel: Linux 5.4.0',
    register_status: '已注册',
    system_update: '2024-03-01 16:20:00',
    system_time: '2024-03-16 10:30:00',
    network_setting: '静态IP: 192.168.1.101',
    last_sync_at: '2024-03-15 18:45:22',
    business_node_id: 'parking-2'
  },
  {
    id: 3,
    name: '',
    api_base_url: 'http://192.168.1.102:8080',
    device_type: '',
    status: 'error',
    device_sn: '',
    version: '',
    register_status: '',
    system_update: '',
    system_time: '',
    network_setting: '',
    last_sync_at: null,
    business_node_id: 'parking-3'
  }
]

// 计算属性和方法
const getStatusColor = (status) => {
  const colors = {
    online: '#67c23a',
    offline: '#909399',
    error: '#f56c6c',
    unknown: '#e6a23c'
  }
  return colors[status] || colors.unknown
}

const getStatusTagType = (status) => {
  const types = {
    online: 'success',
    offline: 'info',
    error: 'danger',
    unknown: 'warning'
  }
  return types[status] || types.unknown
}

const getStatusIcon = (status) => {
  const icons = {
    online: CircleCheck,
    offline: CircleClose,
    error: CircleClose,
    unknown: Clock
  }
  return icons[status] || icons.unknown
}

const getStatusText = (status) => {
  const texts = {
    online: '在线',
    offline: '离线',
    error: '错误',
    unknown: '未知'
  }
  return texts[status] || texts.unknown
}

const getTypeTagType = (type) => {
  const types = {
    edge_box: '',
    camera_server: 'success',
    ai_box: 'warning'
  }
  return types[type] || 'info'
}

const truncateVersion = (version) => {
  if (!version) return '-'
  const firstLine = version.split('\n')[0]
  return firstLine.length > 20 ? firstLine.substring(0, 20) + '...' : firstLine
}

const formatTime = (timeString) => {
  if (!timeString) return null
  return new Date(timeString).toLocaleString('zh-CN')
}

// 事件处理
const handleSelectionChange = (selection) => {
  selectedDevices.value = selection
}

const refreshDevices = async () => {
  loading.value = true
  try {
    // TODO: 调用API获取设备列表
    await new Promise(resolve => setTimeout(resolve, 1000))
    devices.value = [...mockDevices]
    ElMessage.success('设备列表刷新成功')
  } catch (error) {
    ElMessage.error('刷新失败: ' + error.message)
  } finally {
    loading.value = false
  }
}

const showAddDeviceDialog = () => {
  addDeviceVisible.value = true
  // 重置表单
  Object.assign(addDeviceForm, {
    api_base_url: '',
    username: '',
    password: '',
    business_node_id: null
  })
}

const handleAddDevice = async () => {
  if (!addDeviceFormRef.value) return
  
  try {
    await addDeviceFormRef.value.validate()
    addingDevice.value = true
    
    // TODO: 调用后端API添加设备
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    ElMessage.success('设备添加成功！')
    addDeviceVisible.value = false
    refreshDevices()
  } catch (error) {
    ElMessage.error('添加设备失败: ' + error.message)
  } finally {
    addingDevice.value = false
  }
}

const handleAddDeviceClose = () => {
  addDeviceVisible.value = false
}

const syncDevice = async (device) => {
  if (!device.api_base_url) {
    ElMessage.warning('设备地址不能为空')
    return
  }
  
  device.syncing = true
  try {
    // TODO: 调用后端API同步设备信息
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    // 模拟同步成功后更新设备信息
    device.last_sync_at = new Date().toISOString()
    device.status = 'online'
    
    ElMessage.success(`设备 ${device.name || device.api_base_url} 同步成功`)
  } catch (error) {
    ElMessage.error(`同步失败: ${error.message}`)
  } finally {
    device.syncing = false
  }
}

const batchSyncDevices = async () => {
  if (selectedDevices.value.length === 0) return
  
  batchSyncing.value = true
  try {
    // TODO: 调用后端API批量同步
    await new Promise(resolve => setTimeout(resolve, 3000))
    
    ElMessage.success(`批量同步 ${selectedDevices.value.length} 台设备成功`)
    refreshDevices()
  } catch (error) {
    ElMessage.error('批量同步失败: ' + error.message)
  } finally {
    batchSyncing.value = false
  }
}

const viewDeviceDetails = (device) => {
  currentDevice.value = device
  deviceDetailsVisible.value = true
}

const deleteDevice = (device) => {
  ElMessageBox.confirm(
    `确定要删除设备 "${device.name || device.api_base_url}" 吗？`,
    '删除确认',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    }
  ).then(() => {
    // TODO: 调用后端API删除设备
    const index = devices.value.findIndex(d => d.id === device.id)
    if (index !== -1) {
      devices.value.splice(index, 1)
      ElMessage.success('删除成功')
    }
  }).catch(() => {
    // 取消删除
  })
}

// 生命周期
onMounted(() => {
  refreshDevices()
})
</script>

<style scoped>
.device-management {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: 24px;
  background: #ffffff;
}

.device-management.dark-theme {
  background: #1f2937;
}

/* 页面头部 */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 24px;
}

.header-left {
  flex: 1;
}

.page-title {
  font-size: 24px;
  font-weight: 600;
  color: #2c3e50;
  margin: 0 0 8px 0;
}

.page-description {
  font-size: 14px;
  color: #6b7280;
  margin: 0;
}

.header-actions {
  display: flex;
  gap: 12px;
  flex-shrink: 0;
}

/* 设备列表 */
.device-list {
  flex: 1;
  overflow: hidden;
}

.device-table {
  height: 100%;
}

.device-name {
  display: flex;
  align-items: center;
  gap: 8px;
}

.device-icon {
  font-size: 16px;
}

.device-sn {
  font-family: 'Courier New', monospace;
  font-size: 12px;
  color: #6b7280;
}

.version-text {
  font-family: 'Courier New', monospace;
  font-size: 12px;
  cursor: help;
}

.sync-time {
  font-size: 12px;
  color: #6b7280;
}

.no-sync {
  font-size: 12px;
  color: #ef4444;
}

.action-buttons {
  display: flex;
  gap: 4px;
}

/* 设备详情展开 */
.device-details {
  padding: 16px;
  background: #f8fafc;
  border-radius: 8px;
  margin: 8px 0;
}

.detail-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.detail-item {
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

.detail-item.full-width {
  grid-column: 1 / -1;
  flex-direction: column;
  align-items: flex-start;
}

.detail-item label {
  font-weight: 500;
  color: #374151;
  min-width: 80px;
  flex-shrink: 0;
}

.version-detail {
  font-family: 'Courier New', monospace;
  font-size: 12px;
  color: #4b5563;
  white-space: pre-wrap;
  line-height: 1.4;
  margin: 8px 0 0 0;
  padding: 8px;
  background: #f3f4f6;
  border-radius: 4px;
  border: 1px solid #e5e7eb;
}

/* 表单提示 */
.form-tip {
  font-size: 12px;
  color: #6b7280;
  margin-top: 4px;
}

/* 设备详情面板 */
.device-info-panel {
  max-height: 600px;
  overflow-y: auto;
}

.info-sections {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.info-card {
  margin-bottom: 0;
}

.info-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 8px;
}

.info-item.full-width {
  grid-column: 1 / -1;
  align-items: flex-start;
  flex-direction: column;
}

.info-item label {
  font-weight: 500;
  color: #374151;
  min-width: 80px;
  flex-shrink: 0;
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .page-header {
    flex-direction: column;
    gap: 16px;
  }
  
  .header-actions {
    align-self: stretch;
    justify-content: flex-end;
  }
}

@media (max-width: 768px) {
  .device-management {
    padding: 16px;
  }
  
  .detail-grid, .info-grid {
    grid-template-columns: 1fr;
  }
  
  .device-table {
    font-size: 12px;
  }
  
  .action-buttons {
    flex-direction: column;
    gap: 2px;
  }
  
  .action-buttons .el-button {
    font-size: 12px;
    padding: 4px 8px;
  }
}
</style>