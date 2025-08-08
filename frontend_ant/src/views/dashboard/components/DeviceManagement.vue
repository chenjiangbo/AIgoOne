<template>
  <div class="device-management">
    <!-- 页面头部 -->
    <div class="page-header">
      <div class="header-left">
        <h2 class="page-title">设备管理</h2>
        <p class="page-description">管理AI算法平台设备，同步设备信息和状态</p>
      </div>
      <div class="header-actions">
        <a-button @click="refreshDevices">
          <template #icon><ReloadOutlined /></template>
          刷新
        </a-button>
        <a-button type="primary" @click="showAddDeviceDialog">
          <template #icon><PlusOutlined /></template>
          添加设备
        </a-button>
        <a-button 
          type="default" 
          :disabled="selectedDevices.length === 0"
          @click="batchSyncDevices"
          :loading="batchSyncing"
        >
          <template #icon><DownloadOutlined /></template>
          批量同步 ({{ selectedDevices.length }})
        </a-button>
      </div>
    </div>

    <!-- 设备列表 -->
    <div class="device-list">
      <a-table 
        :dataSource="devices" 
        :columns="tableColumns"
        :rowSelection="rowSelection"
        :loading="loading"
        :scroll="{ x: 1200 }"
        :expandable="expandableConfig"
        row-key="id"
        size="middle"
        :pagination="{
          showSizeChanger: true,
          showQuickJumper: true,
          showTotal: (total) => `共 ${total} 条记录`
        }"
      />
    </div>

    <!-- 添加设备对话框 -->
    <a-modal
      v-model:open="addDeviceVisible"
      title="添加设备"
      width="600px"
      :confirmLoading="addingDevice"
      @ok="handleAddDevice"
      @cancel="handleAddDeviceClose"
    >
      <a-form
        ref="addDeviceFormRef"
        :model="addDeviceForm"
        :rules="addDeviceRules"
        :label-col="{ span: 6 }"
        :wrapper-col="{ span: 18 }"
      >
        <a-form-item label="设备地址" name="api_base_url">
          <a-input 
            v-model:value="addDeviceForm.api_base_url" 
            placeholder="请输入设备API地址，如: http://192.168.1.100:8080"
          />
          <div class="form-tip">
            请输入算法应用平台的完整地址，包含协议和端口
          </div>
        </a-form-item>
        
        <a-form-item label="用户名" name="username">
          <a-input v-model:value="addDeviceForm.username" placeholder="请输入设备登录用户名" />
        </a-form-item>
        
        <a-form-item label="密码" name="password">
          <a-input-password 
            v-model:value="addDeviceForm.password" 
            placeholder="请输入设备登录密码"
          />
        </a-form-item>
        
        <a-form-item label="业务节点" name="business_node_id">
          <a-select 
            v-model:value="addDeviceForm.business_node_id" 
            placeholder="请选择关联的业务节点"
          >
            <a-select-option
              v-for="node in leafBusinessNodes"
              :key="node.id"
              :value="node.id"
            >
              {{ node.name }}
            </a-select-option>
          </a-select>
        </a-form-item>
      </a-form>
    </a-modal>

    <!-- 设备详情对话框 -->
    <a-modal
      v-model:open="deviceDetailsVisible"
      :title="currentDevice?.name || '设备详情'"
      width="800px"
      :footer="null"
    >
      <div v-if="currentDevice" class="device-info-panel">
        <a-row :gutter="[16, 16]">
          <a-col :span="24">
            <a-card title="基本信息" size="small">
              <a-descriptions :column="2" size="small">
                <a-descriptions-item label="设备名称">
                  {{ currentDevice.name || '-' }}
                </a-descriptions-item>
                <a-descriptions-item label="设备类型">
                  {{ currentDevice.device_type || '-' }}
                </a-descriptions-item>
                <a-descriptions-item label="设备SN">
                  {{ currentDevice.device_sn || '-' }}
                </a-descriptions-item>
                <a-descriptions-item label="注册状态">
                  {{ currentDevice.register_status || '-' }}
                </a-descriptions-item>
              </a-descriptions>
            </a-card>
          </a-col>
          
          <a-col :span="24">
            <a-card title="网络信息" size="small">
              <a-descriptions :column="2" size="small">
                <a-descriptions-item label="设备地址">
                  {{ currentDevice.api_base_url || '-' }}
                </a-descriptions-item>
                <a-descriptions-item label="网络设置">
                  {{ currentDevice.network_setting || '-' }}
                </a-descriptions-item>
                <a-descriptions-item label="连接状态">
                  <a-tag :color="getStatusColor(currentDevice.status)">
                    {{ getStatusText(currentDevice.status) }}
                  </a-tag>
                </a-descriptions-item>
                <a-descriptions-item label="最后同步">
                  {{ currentDevice.last_sync_at ? formatTime(currentDevice.last_sync_at) : '从未同步' }}
                </a-descriptions-item>
              </a-descriptions>
            </a-card>
          </a-col>
          
          <a-col :span="24">
            <a-card title="系统信息" size="small">
              <a-descriptions :column="1" size="small">
                <a-descriptions-item label="系统时间">
                  {{ currentDevice.system_time || '-' }}
                </a-descriptions-item>
                <a-descriptions-item label="系统更新">
                  {{ currentDevice.system_update || '-' }}
                </a-descriptions-item>
                <a-descriptions-item label="软件版本">
                  <pre class="version-detail">{{ currentDevice.version || '-' }}</pre>
                </a-descriptions-item>
              </a-descriptions>
            </a-card>
          </a-col>
        </a-row>
      </div>
    </a-modal>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, computed, h } from 'vue'
import { message, Modal } from 'ant-design-vue'
import {
  PlusOutlined,
  ReloadOutlined,
  DownloadOutlined,
  DesktopOutlined,
  EyeOutlined,
  DeleteOutlined,
  CheckCircleOutlined,
  CloseCircleOutlined,
  ClockCircleOutlined
} from '@ant-design/icons-vue'
import type { FormInstance, Rule } from 'ant-design-vue/es/form'
import type { TableColumnsType, TableProps } from 'ant-design-vue'
import type { Component } from 'vue'

// 设备接口定义
interface Device {
  id: number
  name?: string
  api_base_url: string
  device_type?: string
  status: 'online' | 'offline' | 'error' | 'unknown'
  device_sn?: string
  version?: string
  register_status?: string
  system_update?: string
  system_time?: string
  network_setting?: string
  last_sync_at?: string
  business_node_id?: string
  syncing?: boolean
}

// 状态管理
const loading = ref(false)
const devices = ref<Device[]>([])
const selectedDevices = ref<Device[]>([])
const batchSyncing = ref(false)

// 添加设备相关
const addDeviceVisible = ref(false)
const addingDevice = ref(false)
const addDeviceFormRef = ref<FormInstance>()

// 设备详情相关
const deviceDetailsVisible = ref(false)
const currentDevice = ref<Device | null>(null)

// 表单数据
const addDeviceForm = reactive({
  api_base_url: '',
  username: '',
  password: '',
  business_node_id: ''
})

// 表单验证规则
const addDeviceRules: Record<string, Rule[]> = {
  api_base_url: [
    { required: true, message: '请输入设备API地址', trigger: 'blur' },
    {
      pattern: /^https?:\/\/.+/, 
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
const mockDevices: Device[] = [
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
    last_sync_at: undefined,
    business_node_id: 'parking-3'
  }
]

// 表格列定义
const tableColumns: TableColumnsType<Device> = [
  {
    title: '设备名称',
    dataIndex: 'name',
    key: 'name',
    width: 200,
    customRender: ({ record }) => {
      return h('div', { class: 'device-name' }, [
        h(DesktopOutlined, { 
          style: { 
            color: getStatusColor(record.status),
            marginRight: '8px' 
          }
        }),
        h('span', record.name || '未知设备')
      ])
    }
  },
  {
    title: '设备地址',
    dataIndex: 'api_base_url',
    key: 'api_base_url',
    width: 200,
    customRender: ({ text }) => {
      return h('a', {
        href: text,
        target: '_blank',
        style: { fontSize: '12px' }
      }, text)
    }
  },
  {
    title: '设备类型',
    dataIndex: 'device_type',
    key: 'device_type',
    width: 120,
    customRender: ({ text }) => {
      return h('a-tag', {
        color: getTypeTagColor(text),
        size: 'small'
      }, text || '未知')
    }
  },
  {
    title: '状态',
    dataIndex: 'status',
    key: 'status',
    width: 100,
    customRender: ({ text }) => {
      return h('a-tag', {
        color: getStatusColor(text),
        size: 'small'
      }, [
        h(getStatusIcon(text), { style: { marginRight: '4px' } as any }),
        getStatusText(text)
      ])
    }
  },
  {
    title: '设备SN',
    dataIndex: 'device_sn',
    key: 'device_sn',
    width: 150,
    customRender: ({ text }) => {
      return h('span', { class: 'device-sn' }, text || '-')
    }
  },
  {
    title: '软件版本',
    dataIndex: 'version',
    key: 'version',
    width: 120,
    customRender: ({ text }) => {
      if (!text) return '-'
      const firstLine = text.split('\n')[0]
      const truncated = firstLine.length > 20 ? firstLine.substring(0, 20) + '...' : firstLine
      return h('a-tooltip', {
        title: text,
        placement: 'top'
      }, {
        default: () => h('span', { class: 'version-text' }, truncated)
      })
    }
  },
  {
    title: '最后同步',
    dataIndex: 'last_sync_at',
    key: 'last_sync_at',
    width: 150,
    customRender: ({ text }) => {
      if (text) {
        return h('span', { class: 'sync-time' }, formatTime(text))
      }
      return h('span', { class: 'no-sync' }, '从未同步')
    }
  },
  {
    title: '操作',
    key: 'action',
    width: 240,
    fixed: 'right',
    customRender: ({ record }) => {
      return h('a-space', { size: 'small' }, [
        h('a-button', {
          size: 'small',
          loading: record.syncing,
          disabled: !record.api_base_url,
          onClick: () => syncDevice(record)
        }, {
          icon: () => h(DownloadOutlined),
          default: () => '同步'
        }),
        h('a-button', {
          size: 'small',
          onClick: () => viewDeviceDetails(record)
        }, {
          icon: () => h(EyeOutlined),
          default: () => '详情'
        }),
        h('a-button', {
          size: 'small',
          danger: true,
          onClick: () => deleteDevice(record)
        }, {
          icon: () => h(DeleteOutlined),
          default: () => '删除'
        })
      ])
    }
  }
]

// 表格行选择配置
const rowSelection: TableProps['rowSelection'] = {
  onChange: (selectedRowKeys: any[], selectedRows: Device[]) => {
    selectedDevices.value = selectedRows
  }
}

// 表格展开配置
const expandableConfig = {
  expandedRowRender: (record: Device) => {
    return h('div', { class: 'device-details' }, [
      h('a-descriptions', { column: 2, size: 'small', bordered: true }, [
        h('a-descriptions-item', { label: '注册状态' }, record.register_status || '未知'),
        h('a-descriptions-item', { label: '系统更新' }, record.system_update || '-'),
        h('a-descriptions-item', { label: '系统时间' }, record.system_time || '-'),
        h('a-descriptions-item', { label: '网络设置' }, record.network_setting || '-'),
        h('a-descriptions-item', { label: '软件版本详情', span: 2 }, 
          h('pre', { class: 'version-detail' }, record.version || '暂无版本信息')
        )
      ])
    ])
  }
}

// 工具方法
const getStatusColor = (status: string) => {
  const colors = {
    online: 'success',
    offline: 'default',
    error: 'error',
    unknown: 'warning'
  }
  return colors[status as keyof typeof colors] || colors.unknown
}

const getStatusText = (status: string) => {
  const texts = {
    online: '在线',
    offline: '离线',
    error: '错误',
    unknown: '未知'
  }
  return texts[status as keyof typeof texts] || texts.unknown
}

const getStatusIcon = (status: string): Component => {
  const icons: Record<string, Component> = {
    online: CheckCircleOutlined,
    offline: CloseCircleOutlined,
    error: CloseCircleOutlined,
    unknown: ClockCircleOutlined
  }
  return icons[status] || icons.unknown
}

const getTypeTagColor = (type: string) => {
  const colors = {
    edge_box: 'blue',
    camera_server: 'green',
    ai_box: 'orange'
  }
  return colors[type as keyof typeof colors] || 'default'
}

const formatTime = (timeString: string) => {
  if (!timeString) return ''
  return new Date(timeString).toLocaleString('zh-CN')
}

// 事件处理
const refreshDevices = async () => {
  loading.value = true
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    devices.value = [...mockDevices]
    message.success('设备列表刷新成功')
  } catch (error: any) {
    message.error('刷新失败: ' + error.message)
  } finally {
    loading.value = false
  }
}

const showAddDeviceDialog = () => {
  addDeviceVisible.value = true
  Object.assign(addDeviceForm, {
    api_base_url: '',
    username: '',
    password: '',
    business_node_id: ''
  })
}

const handleAddDevice = async () => {
  if (!addDeviceFormRef.value) return
  
  try {
    await addDeviceFormRef.value.validate()
    addingDevice.value = true
    
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    message.success('设备添加成功！')
    addDeviceVisible.value = false
    refreshDevices()
  } catch (error: any) {
    if (error.errorFields) {
      // 表单验证错误
      return
    }
    message.error('添加设备失败: ' + error.message)
  } finally {
    addingDevice.value = false
  }
}

const handleAddDeviceClose = () => {
  addDeviceVisible.value = false
}

const syncDevice = async (device: Device) => {
  if (!device.api_base_url) {
    message.warning('设备地址不能为空')
    return
  }
  
  device.syncing = true
  try {
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    device.last_sync_at = new Date().toISOString()
    device.status = 'online'
    
    message.success(`设备 ${device.name || device.api_base_url} 同步成功`)
  } catch (error: any) {
    message.error(`同步失败: ${error.message}`)
  } finally {
    device.syncing = false
  }
}

const batchSyncDevices = async () => {
  if (selectedDevices.value.length === 0) return
  
  batchSyncing.value = true
  try {
    await new Promise(resolve => setTimeout(resolve, 3000))
    
    message.success(`批量同步 ${selectedDevices.value.length} 台设备成功`)
    refreshDevices()
  } catch (error: any) {
    message.error('批量同步失败: ' + error.message)
  } finally {
    batchSyncing.value = false
  }
}

const viewDeviceDetails = (device: Device) => {
  currentDevice.value = device
  deviceDetailsVisible.value = true
}

const deleteDevice = (device: Device) => {
  Modal.confirm({
    title: '删除确认',
    content: `确定要删除设备 "${device.name || device.api_base_url}" 吗？`,
    okText: '确定',
    cancelText: '取消',
    okType: 'danger',
    onOk: () => {
      const index = devices.value.findIndex(d => d.id === device.id)
      if (index !== -1) {
        devices.value.splice(index, 1)
        message.success('删除成功')
      }
    }
  })
}

// 生命周期
onMounted(() => {
  refreshDevices()
})
</script>

<style lang="less" scoped>
.device-management {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: 24px;
  background: #fff;
}

// 页面头部
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

// 设备列表
.device-list {
  flex: 1;
  overflow: hidden;
}

.device-name {
  display: flex;
  align-items: center;
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

// 设备详情展开
.device-details {
  padding: 16px;
  background: #f8fafc;
  border-radius: 8px;
  margin: 8px 0;
}

.version-detail {
  font-family: 'Courier New', monospace;
  font-size: 12px;
  color: #4b5563;
  white-space: pre-wrap;
  line-height: 1.4;
  margin: 0;
  padding: 8px;
  background: #f3f4f6;
  border-radius: 4px;
  border: 1px solid #e5e7eb;
}

// 表单提示
.form-tip {
  font-size: 12px;
  color: #6b7280;
  margin-top: 4px;
}

// 设备详情面板
.device-info-panel {
  max-height: 600px;
  overflow-y: auto;
}

// 响应式设计
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
}
</style>