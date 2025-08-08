<template>
  <a-drawer
    v-model:open="visible"
    title="设备管理"
    placement="right"
    :width="1200"
    :closable="false"
    :mask-closable="false"
    class="device-management-drawer"
  >
    <template #title>
      <div class="drawer-header">
        <div class="header-left">
          <a-avatar class="header-icon" :size="40" style="background-color: var(--navbar-bg)">
            <template #icon>
              <MonitorOutlined />
            </template>
          </a-avatar>
          <div class="header-text">
            <h3 class="drawer-title">设备管理</h3>
            <p class="drawer-subtitle">管理AI算法平台设备，同步设备信息和状态</p>
          </div>
        </div>
        <a-button 
          type="text" 
          class="header-close-btn"
          @click="handleClose"
        >
          <template #icon>
            <CloseOutlined />
          </template>
        </a-button>
      </div>
    </template>

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
      @submit="handleAddDevice"
    />

    <!-- 编辑设备对话框 -->
    <EditDeviceDialog
      v-model:visible="editDeviceVisible"
      :loading="editingDevice"
      :device="currentEditDevice"
      @submit="handleEditDevice"
    />

    <!-- 导入设备对话框 -->
    <ImportDevicesDialog
      v-model:visible="importDevicesVisible"
      @import-success="handleImportSuccess"
    />

    <!-- 设备详情对话框 -->
    <DeviceDetailsDialog 
      v-model:visible="deviceDetailsVisible"
      :device="currentDevice"
    />

    <!-- 批量同步进度对话框 -->
    <BatchSyncDialog
      v-model:visible="batchSyncProgressVisible"
      :progress="syncProgress"
      @close="closeBatchSyncProgress"
      @cancel="cancelBatchSync"
    />
  </a-drawer>
</template>

<script setup lang="ts">
import { ref, reactive, computed, watch, nextTick } from 'vue'
import { message, Modal, notification } from 'ant-design-vue'
import { MonitorOutlined, CloseOutlined } from '@ant-design/icons-vue'

// 导入子组件
import DeviceToolbar from './DeviceToolbar.vue'
import DeviceStatsCards from './DeviceStatsCards.vue'
import DeviceTable from './DeviceTable.vue'
import AddDeviceDialog from './AddDeviceDialog.vue'
import EditDeviceDialog from './EditDeviceDialog.vue'
import ImportDevicesDialog from './ImportDevicesDialog.vue'
import DeviceDetailsDialog from './DeviceDetailsDialog.vue'
import BatchSyncDialog from './BatchSyncDialog.vue'

// 导入API
import {
  type Device,
  type DeviceCreate,
  getDevices,
  addDevice,
  updateDevice,
  deleteDevice,
  syncDevice,
  batchSyncDevices,
  batchDeleteDevices
} from '@/api/device'

// Props
interface Props {
  visible: boolean
}

const props = withDefaults(defineProps<Props>(), {
  visible: false
})

// Emits
const emit = defineEmits<{
  'update:visible': [value: boolean]
}>()

// 响应式状态
const loading = ref(false)
const refreshing = ref(false)
const devices = ref<Device[]>([])
const selectedDevices = ref<Device[]>([])
const batchSyncing = ref(false)

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
const currentEditDevice = ref<Device | null>(null)

// 导入设备相关
const importDevicesVisible = ref(false)

// 设备详情相关
const deviceDetailsVisible = ref(false)
const currentDevice = ref<Device | null>(null)

// 批量同步进度相关
const batchSyncProgressVisible = ref(false)
const syncCancelled = ref(false)
const syncProgress = reactive({
  current: 0,
  total: 0,
  success: 0,
  failed: 0,
  status: '', // '', 'success', 'exception'
  currentDevice: null as Device | null,
  logs: [] as Array<{ type: 'info' | 'success' | 'error'; message: string }>
})

// 计算属性
const visible = computed({
  get: () => props.visible,
  set: (value: boolean) => emit('update:visible', value)
})

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
    if (device.status === 'online') {
      stats.online++
    } else if (device.status === 'offline') {
      stats.offline++
    } else if (device.status === 'error') {
      stats.error++
    }
  })
  
  return stats
})

// 监听抽屉可见性
watch(() => props.visible, (newVisible) => {
  if (newVisible) {
    nextTick(() => {
      loadDevices()
    })
  }
})

// 事件处理
const handleClose = () => {
  visible.value = false
}

const handleSearch = (keyword: string) => {
  searchKeyword.value = keyword
}

const handleFilter = (filters: { status?: string; type?: string }) => {
  statusFilter.value = filters.status || ''
  typeFilter.value = filters.type || ''
}

const handleSelectionChange = (selection: Device[]) => {
  selectedDevices.value = selection
}

const loadDevices = async () => {
  loading.value = true
  try {
    const response = await getDevices()
    // 后台直接返回 DeviceListResponse，包含 items 数组
    devices.value = response.data?.items || []
  } catch (error: any) {
    console.error('加载设备失败:', error)
    message.error('加载设备失败: ' + (error.response?.data?.detail || error.message || '未知错误'))
    devices.value = []
  } finally {
    loading.value = false
  }
}

const refreshDevices = async () => {
  refreshing.value = true
  try {
    await loadDevices()
    message.success('设备列表刷新成功')
  } catch (error: any) {
    message.error('刷新失败: ' + (error.response?.data?.detail || error.message))
  } finally {
    refreshing.value = false
  }
}

const showAddDeviceDialog = () => {
  addDeviceVisible.value = true
}

const handleAddDevice = async (formData: DeviceCreate) => {
  addingDevice.value = true
  try {
    await addDevice(formData)
    message.success('设备添加成功！正在后台同步信息...')
    addDeviceVisible.value = false
    await refreshDevices()
  } catch (error: any) {
    const errorMessage = error.response?.data?.detail || error.message || '添加设备失败'
    message.error(errorMessage)
  } finally {
    addingDevice.value = false
  }
}

const editDevice = (device: Device) => {
  currentEditDevice.value = device
  editDeviceVisible.value = true
}

const handleEditDevice = async (formData: DeviceCreate) => {
  if (!currentEditDevice.value) return
  
  editingDevice.value = true
  try {
    await updateDevice(currentEditDevice.value.id, formData)
    message.success('设备信息更新成功！')
    editDeviceVisible.value = false
    currentEditDevice.value = null
    await refreshDevices()
  } catch (error: any) {
    const errorMessage = error.response?.data?.detail || error.message || '编辑设备失败'
    message.error(errorMessage)
  } finally {
    editingDevice.value = false
  }
}

const syncDeviceHandler = async (device: Device) => {
  if (!device.api_base_url) {
    message.warning('设备地址不能为空')
    return
  }
  
  // 设置同步状态
  ;(device as any).syncing = true
  
  message.info(`正在同步设备 ${device.name || device.api_base_url}...`)
  
  try {
    const response = await syncDevice(device.id)
    
    if (response.data.success) {
      notification.success({
        message: '同步成功',
        description: `${device.name || device.api_base_url} 信息已更新`,
        duration: 2,
        placement: 'bottomRight'
      })
      
      await loadDevices()
      
      // 高亮显示刚同步的设备行
      ;(device as any).justSynced = true
      setTimeout(() => {
        ;(device as any).justSynced = false
      }, 3000)
      
    } else {
      message.error({
        content: `同步失败: ${response.data.message}`,
        duration: 5
      })
    }
  } catch (error: any) {
    const errorMsg = error.response?.data?.detail || error.message || '同步过程中发生未知错误'
    message.error({
      content: `同步失败: ${errorMsg}`,
      duration: 5
    })
    
    ;(device as any).status = 'error'
    ;(device as any).sync_error = errorMsg
  } finally {
    ;(device as any).syncing = false
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
      } catch (error: any) {
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
    
  } catch (error: any) {
    syncProgress.status = 'exception'
    syncProgress.logs.push({
      type: 'error',
      message: '批量同步过程中发生错误: ' + (error.response?.data?.detail || error.message)
    })
  } finally {
    batchSyncing.value = false
  }
}

const viewDeviceDetails = (device: Device) => {
  currentDevice.value = device
  deviceDetailsVisible.value = true
}

const deleteDeviceHandler = (device: Device) => {
  Modal.confirm({
    title: '删除确认',
    content: `确定要删除设备 "${device.name || device.api_base_url}" 吗？`,
    okText: '确定',
    cancelText: '取消',
    okType: 'danger',
    centered: true,
    onOk: async () => {
      try {
        await deleteDevice(device.id)
        message.success('删除成功')
        await loadDevices()
      } catch (error: any) {
        message.error('删除失败: ' + (error.response?.data?.detail || error.message))
      }
    }
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
  
  Modal.confirm({
    title: '批量删除确认',
    content: `确定要删除以下 ${selectedDevices.value.length} 个设备吗？\n\n${deviceNames}`,
    okText: '确定删除',
    cancelText: '取消',
    okType: 'danger',
    centered: true,
    onOk: async () => {
      try {
        const deviceIds = selectedDevices.value.map(device => device.id)
        const response = await batchDeleteDevices(deviceIds)
        
        if (response.data.success) {
          message.success(`成功删除 ${response.data.deleted_count} 个设备`)
        } else {
          message.warning(`批量删除完成：成功 ${response.data.deleted_count} 个，失败 ${response.data.failed_count} 个`)
        }
        
        // 清空选择并刷新列表
        if (deviceTableRef.value) {
          deviceTableRef.value.clearSelection()
        }
        await refreshDevices()
        
      } catch (error: any) {
        message.error('批量删除失败: ' + (error.response?.data?.detail || error.message))
      }
    }
  })
}
</script>

<style scoped>
.device-management-drawer {
  --drawer-header-bg: var(--navbar-bg);
}

:deep(.ant-drawer-header) {
  padding: 0;
  border-bottom: none;
}

.drawer-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 70px;
  padding: 0 24px;
  background: var(--drawer-header-bg);
  color: white;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 16px;
}

.header-icon {
  color: rgba(255, 255, 255, 0.9);
}

.header-text {
  flex: 1;
}

.drawer-title {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
  line-height: 1;
  color: white;
}

.drawer-subtitle {
  margin: 4px 0 0 0;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);
  line-height: 1;
}

.header-close-btn {
  color: rgba(255, 255, 255, 0.8);
  border: none;
  background: transparent;
  width: 32px;
  height: 32px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.header-close-btn:hover {
  color: white;
  background: rgba(255, 255, 255, 0.1);
}

.drawer-content {
  height: 100%;
  display: flex;
  flex-direction: column;
  background: var(--bg-primary);
  overflow: hidden;
}

:deep(.ant-drawer-body) {
  padding: 0;
  overflow: hidden;
}

html.dark .drawer-header {
  background: var(--color-neutral-800);
}

html.dark .drawer-content {
  background: var(--bg-secondary);
}
</style>