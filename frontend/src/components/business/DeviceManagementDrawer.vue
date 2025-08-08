<template>
  <el-drawer
    :model-value="visible"
    @update:model-value="$emit('update:visible', $event)"
    title="设备管理"
    size="70%"
    direction="rtl"
    :before-close="handleClose"
    :modal="true"
    :modal-class="'device-drawer-overlay'"
    :show-close="false"
    class="device-management-drawer"
  >
    <!-- 自定义头部 -->
    <template #header="{ close, titleId, titleClass }">
      <div class="drawer-header">
        <div class="header-left">
          <el-icon class="header-icon"><Monitor /></el-icon>
          <div class="header-text">
            <h3 class="drawer-title">设备管理</h3>
            <p class="drawer-subtitle">管理AI算法平台设备，同步设备信息和状态</p>
          </div>
        </div>
        
        <div class="header-actions">
          <el-tooltip content="关闭" placement="bottom">
            <el-button 
              type="text" 
              class="header-btn close-btn"
              @click="handleClose"
            >
              <el-icon><Close /></el-icon>
            </el-button>
          </el-tooltip>
        </div>
      </div>
    </template>

    <!-- 抽屉内容 -->
    <div class="drawer-content">
      <!-- 工具栏 -->
      <DeviceToolbar
        :refreshing="refreshing"
        :batch-syncing="batchSyncing"
        :selected-count="selectedDevices.length"
        @search="handleSearch"
        @filter="handleFilter"
        @refresh="refreshDevices"
        @batch-sync="batchSyncDevicesHandler"
        @batch-delete="batchDeleteDevicesHandler"
        @import-devices="showImportDevicesDialog"
        @add-device="showAddDeviceDialog"
      />

      <!-- 设备统计卡片 -->
      <DeviceStatsCards :stats="deviceStats" />

      <!-- 设备列表 -->
      <DeviceTable
        ref="deviceTableRef"
        :devices="filteredDevices"
        :loading="loading"
        :height="tableHeight"
        @selection-change="handleSelectionChange"
        @sync="syncDeviceHandler"
        @edit="editDevice"
        @view-details="viewDeviceDetails"
        @delete="deleteDeviceHandler"
      />
    </div>

    <!-- 添加设备对话框 -->
    <AddDeviceDialog
      v-model:visible="addDeviceVisible"
      :loading="addingDevice"
      :is-dark-theme="isDarkTheme"
      @submit="handleAddDevice"
    />

    <!-- 编辑设备对话框 -->
    <EditDeviceDialog
      v-model:visible="editDeviceVisible"
      :loading="editingDevice"
      :device="currentEditDevice"
      :is-dark-theme="isDarkTheme"
      @submit="handleEditDevice"
    />

    <!-- 导入设备对话框 -->
    <ImportDevicesDialog
      v-model:visible="importDevicesVisible"
      :is-dark-theme="isDarkTheme"
      @import-success="handleImportSuccess"
    />

    <!-- 设备详情对话框 -->
    <DeviceDetailsDialog 
      v-model:visible="deviceDetailsVisible"
      :device="currentDevice"
      :is-dark-theme="isDarkTheme"
    />

    <!-- 批量同步进度对话框 -->
    <BatchSyncDialog
      v-model:visible="batchSyncProgressVisible"
      :progress="syncProgress"
      @close="closeBatchSyncProgress"
      @cancel="cancelBatchSync"
    />
  </el-drawer>
</template>

<script setup>
import { ref, reactive, computed, watch, onMounted, nextTick } from 'vue'
import { ElMessage, ElMessageBox, ElNotification } from 'element-plus'
import { Monitor, Close } from '@element-plus/icons-vue'

// 导入拆分的组件
import {
  DeviceToolbar,
  DeviceStatsCards,  
  DeviceTable,
  AddDeviceDialog,
  EditDeviceDialog,
  ImportDevicesDialog,
  BatchSyncDialog
} from '@/components/device'
import DeviceDetailsDialog from './DeviceDetailsDialog.vue'

// 导入API
import { getDevices, addDevice, updateDevice, deleteDevice, syncDevice, batchImportDevices, batchDeleteDevices } from '@/api/device.js'

// Props
const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  },
  isDarkTheme: {
    type: Boolean,
    default: false
  }
})

// Emits
const emit = defineEmits(['update:visible'])

// 响应式状态
const loading = ref(false)
const refreshing = ref(false)
const devices = ref([])
const selectedDevices = ref([])
const batchSyncing = ref(false)
const tableHeight = ref(400)

// 筛选和搜索
const searchKeyword = ref('')
const statusFilter = ref('')
const typeFilter = ref('')

// 添加设备相关
const addDeviceVisible = ref(false)
const addingDevice = ref(false)
const deviceTableRef = ref()

// 编辑设备相关
const editDeviceVisible = ref(false)
const editingDevice = ref(false)
const currentEditDevice = ref(null)

// 导入设备相关
const importDevicesVisible = ref(false)

// 设备详情相关
const deviceDetailsVisible = ref(false)
const currentDevice = ref(null)

// 批量同步进度相关
const batchSyncProgressVisible = ref(false)
const syncCancelled = ref(false)
const syncProgress = reactive({
  current: 0,
  total: 0,
  success: 0,
  failed: 0,
  status: '', // '', 'success', 'exception'
  currentDevice: null,
  logs: []
})


// 计算属性
const filteredDevices = computed(() => {
  let result = devices.value
  
  // 搜索过滤
  if (searchKeyword.value) {
    const keyword = searchKeyword.value.toLowerCase()
    result = result.filter(device => 
      (device.name && device.name.toLowerCase().includes(keyword)) ||
      (device.api_base_url && device.api_base_url.toLowerCase().includes(keyword)) ||
      (device.device_sn && device.device_sn.toLowerCase().includes(keyword))
    )
  }
  
  // 状态过滤
  if (statusFilter.value) {
    result = result.filter(device => device.status === statusFilter.value)
  }
  
  // 类型过滤
  if (typeFilter.value) {
    result = result.filter(device => device.device_type === typeFilter.value)
  }
  
  return result
})

const deviceStats = computed(() => {
  const stats = {
    total: devices.value.length,
    online: 0,
    offline: 0,
    error: 0
  }
  
  devices.value.forEach(device => {
    stats[device.status] = (stats[device.status] || 0) + 1
  })
  
  return stats
})

// 监听抽屉可见性
watch(() => props.visible, (newVisible) => {
  if (newVisible) {
    nextTick(() => {
      calculateTableHeight()
      loadDevices()
    })
  }
})

// 事件处理
const handleClose = () => {
  emit('update:visible', false)
}

const handleSearch = (keyword) => {
  searchKeyword.value = keyword
}

const handleFilter = (filters) => {
  statusFilter.value = filters.status
  typeFilter.value = filters.type
}

const handleSelectionChange = (selection) => {
  selectedDevices.value = selection
}

const calculateTableHeight = () => {
  // 计算表格高度
  const windowHeight = window.innerHeight
  const headerHeight = 60
  const toolbarHeight = 60
  const statsHeight = 80
  const padding = 40
  
  tableHeight.value = windowHeight - headerHeight - toolbarHeight - statsHeight - padding
}

const loadDevices = async () => {
  loading.value = true
  try {
    const response = await getDevices()
    devices.value = response.data.items || []
  } catch (error) {
    console.error('加载设备失败:', error)
    ElMessage.error('加载设备失败: ' + (error.response?.data?.message || error.message))
  } finally {
    loading.value = false
  }
}

const refreshDevices = async () => {
  refreshing.value = true
  try {
    await loadDevices()
    ElMessage.success('设备列表刷新成功')
  } catch (error) {
    ElMessage.error('刷新失败: ' + (error.response?.data?.message || error.message))
  } finally {
    refreshing.value = false
  }
}

const showAddDeviceDialog = () => {
  addDeviceVisible.value = true
}

const handleAddDevice = async (formData) => {
  addingDevice.value = true;
  try {
    await addDevice(formData);
    ElMessage.success('设备添加成功！正在后台同步信息...');
    addDeviceVisible.value = false;
    await refreshDevices();
  } catch (error) {
    const errorMessage = error.response?.data?.detail || error.message || '添加设备失败';
    ElMessage.error(errorMessage);
  } finally {
    addingDevice.value = false;
  }
}

const editDevice = (device) => {
  currentEditDevice.value = device
  editDeviceVisible.value = true
}

const handleEditDevice = async (formData) => {
  if (!currentEditDevice.value) return
  
  editingDevice.value = true;
  try {
    await updateDevice(currentEditDevice.value.id, formData);
    ElMessage.success('设备信息更新成功！');
    editDeviceVisible.value = false;
    currentEditDevice.value = null;
    await refreshDevices();
  } catch (error) {
    const errorMessage = error.response?.data?.detail || error.message || '编辑设备失败';
    ElMessage.error(errorMessage);
  } finally {
    editingDevice.value = false;
  }
}

const syncDeviceHandler = async (device) => {
  if (!device.api_base_url) {
    ElMessage.warning('设备地址不能为空')
    return
  }
  
  // 设置同步状态
  device.syncing = true
  
  // 显示开始同步的消息
  ElMessage.info(`正在同步设备 ${device.name || device.api_base_url}...`)
  
  try {
    const response = await syncDevice(device.id)
    
    if (response.data.success) {
      // 同步成功的简单通知
      ElNotification({
        type: 'success',
        title: '同步成功',
        message: `${device.name || device.api_base_url} 信息已更新`,
        duration: 2000,
        position: 'bottom-right'
      })
      
      // 刷新设备列表以显示最新信息
      await loadDevices()
      
      // 高亮显示刚同步的设备行（通过添加CSS类）
      device.justSynced = true
      setTimeout(() => {
        device.justSynced = false
      }, 3000) // 3秒后移除高亮
      
    } else {
      ElMessage({
        type: 'error', 
        message: `同步失败: ${response.data.message}`,
        duration: 5000,
        showClose: true
      })
    }
  } catch (error) {
    const errorMsg = error.response?.data?.detail || error.message || '同步过程中发生未知错误'
    ElMessage({
      type: 'error',
      message: `同步失败: ${errorMsg}`,
      duration: 5000,
      showClose: true
    })
    
    // 设置设备状态为错误
    device.status = 'error'
    device.sync_error = errorMsg
  } finally {
    device.syncing = false
  }
}

const batchSyncDevicesHandler = async () => {
  if (selectedDevices.value.length === 0) return
  
  // 初始化进度状态
  Object.assign(syncProgress, {
    current: 0,
    total: selectedDevices.value.length,
    success: 0,
    failed: 0,
    status: '',
    currentDevice: null,
    logs: []
  })
  
  syncCancelled.value = false
  batchSyncProgressVisible.value = true
  batchSyncing.value = true
  
  try {
    // 逐个同步设备以显示进度
    for (let i = 0; i < selectedDevices.value.length; i++) {
      if (syncCancelled.value) {
        syncProgress.logs.push({
          type: 'error',
          message: '用户取消了批量同步操作'
        })
        break
      }
      
      const device = selectedDevices.value[i]
      syncProgress.currentDevice = device
      syncProgress.logs.push({
        type: 'info',
        message: `开始同步 ${device.name || device.api_base_url}...`
      })
      
      try {
        const response = await syncDevice(device.id)
        
        if (response.data.success) {
          syncProgress.success++
          syncProgress.logs.push({
            type: 'success',
            message: `${device.name || device.api_base_url} 同步成功`
          })
        } else {
          syncProgress.failed++
          syncProgress.logs.push({
            type: 'error',
            message: `${device.name || device.api_base_url} 同步失败: ${response.data.message}`
          })
        }
      } catch (error) {
        syncProgress.failed++
        syncProgress.logs.push({
          type: 'error',
          message: `${device.name || device.api_base_url} 同步失败: ${error.response?.data?.detail || error.message}`
        })
      }
      
      syncProgress.current = i + 1
      
      // 添加短暂延迟以便用户看到进度
      await new Promise(resolve => setTimeout(resolve, 500))
    }
    
    // 设置最终状态
    if (syncCancelled.value) {
      syncProgress.status = 'exception'
    } else if (syncProgress.failed === 0) {
      syncProgress.status = 'success'
    } else if (syncProgress.success === 0) {
      syncProgress.status = 'exception'
    } else {
      syncProgress.status = 'success'
    }
    
    // 刷新设备列表
    await refreshDevices()
    
    // 清空选择
    if (deviceTableRef.value) {
      deviceTableRef.value.clearSelection()
    }
    
  } catch (error) {
    syncProgress.status = 'exception'
    syncProgress.logs.push({
      type: 'error',
      message: '批量同步过程中发生错误: ' + (error.response?.data?.detail || error.message)
    })
  } finally {
    batchSyncing.value = false
  }
}

const viewDeviceDetails = (device) => {
  currentDevice.value = device
  deviceDetailsVisible.value = true
}

const deleteDeviceHandler = (device) => {
  ElMessageBox.confirm(
    `确定要删除设备 "${device.name || device.api_base_url}" 吗？`,
    '删除确认',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
      center: true,
      appendTo: document.body,
      customClass: 'custom-confirm-box',
      closeOnClickModal: false
    }
  ).then(async () => {
    try {
      await deleteDevice(device.id)
      ElMessage.success('删除成功')
      await loadDevices()
    } catch (error) {
      ElMessage.error('删除失败: ' + (error.response?.data?.detail || error.message))
    }
  }).catch(() => {
    // 取消删除
  })
}

const closeBatchSyncProgress = () => {
  batchSyncProgressVisible.value = false
  syncProgress.logs = []
}

const cancelBatchSync = () => {
  syncCancelled.value = true
  syncProgress.logs.push({
    type: 'error',
    message: '正在取消批量同步...'
  })
}

const showImportDevicesDialog = () => {
  importDevicesVisible.value = true
}

const handleImportSuccess = async () => {
  await refreshDevices()
}

const batchDeleteDevicesHandler = async () => {
  if (selectedDevices.value.length === 0) return
  
  const deviceNames = selectedDevices.value.map(device => device.name || device.api_base_url).join('、')
  
  try {
    await ElMessageBox.confirm(
      `确定要删除以下 ${selectedDevices.value.length} 个设备吗？\n\n${deviceNames}`,
      '批量删除确认',
      {
        confirmButtonText: '确定删除',
        cancelButtonText: '取消',
        type: 'warning',
        center: true,
        appendTo: document.body,
        customClass: 'custom-confirm-box',
        closeOnClickModal: false
      }
    )
    
    const deviceIds = selectedDevices.value.map(device => device.id)
    
    try {
      const response = await batchDeleteDevices(deviceIds)
      
      if (response.data.success) {
        ElMessage.success(`成功删除 ${response.data.deleted_count} 个设备`)
      } else {
        ElMessage.warning(`批量删除完成：成功 ${response.data.deleted_count} 个，失败 ${response.data.failed_count} 个`)
      }
      
      // 清空选择并刷新列表
      if (deviceTableRef.value) {
        deviceTableRef.value.clearSelection()
      }
      await refreshDevices()
      
    } catch (error) {
      ElMessage.error('批量删除失败: ' + (error.response?.data?.detail || error.message))
    }
    
  } catch (error) {
    // 用户取消删除
  }
}

// 监听窗口大小变化
onMounted(() => {
  window.addEventListener('resize', calculateTableHeight)
})
</script>

<style scoped>
/* 使用设计Token的简化样式 */

/* 抽屉覆盖层 */
:deep(.device-drawer-overlay) {
  background: var(--color-bg-overlay);
  backdrop-filter: blur(var(--backdrop-blur-sm));
}

/* 抽屉样式 */
.device-management-drawer {
  --el-drawer-padding-primary: 0;
}

:deep(.device-management-drawer .el-drawer) {
  border-radius: var(--border-radius-lg) 0 0 var(--border-radius-lg);
  overflow: hidden;
}

:deep(.device-management-drawer .el-drawer__body) {
  padding: 0;
  overflow: hidden;
}

/* 自定义头部 */
.drawer-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 60px;
  padding: 0 var(--spacing-6);
  background: var(--color-primary-500);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  color: white;
}

.header-left {
  display: flex;
  align-items: center;
  gap: var(--spacing-4);
}

.header-icon {
  font-size: var(--font-size-3xl);
  color: rgba(255, 255, 255, 0.9);
}

.header-text {
  flex: 1;
}

.drawer-title {
  margin: 0;
  font-size: var(--font-size-xl);
  font-weight: var(--font-weight-semibold);
  line-height: 1;
}

.drawer-subtitle {
  margin: var(--spacing-1) 0 0 0;
  font-size: var(--font-size-sm);
  color: rgba(255, 255, 255, 0.8);
  line-height: 1;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: var(--spacing-2);
}

.header-btn {
  width: 32px;
  height: 32px;
  padding: 0;
  color: rgba(255, 255, 255, 0.8);
  border: none;
  background: transparent;
  transition: var(--transition-all-fast);
}

.header-btn:hover {
  color: white;
  background: rgba(255, 255, 255, 0.1);
}

.close-btn:hover {
  background: var(--color-error-500) !important;
  color: white !important;
}

/* 抽屉内容 */
.drawer-content {
  height: 100%;
  display: flex;
  flex-direction: column;
  background: var(--color-bg-primary);
  overflow: hidden;
}

/* 暗色主题适配 */
[data-theme="dark"] .drawer-header {
  background: var(--color-neutral-800);
}

[data-theme="dark"] .drawer-content {
  background: var(--color-bg-secondary);
}
</style>