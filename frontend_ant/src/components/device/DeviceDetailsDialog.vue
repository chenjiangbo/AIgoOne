<template>
  <a-modal
    v-model:open="visible"
    title="设备详情"
    width="800px"
    :footer="null"
    :draggable="true"
    class="device-details-modal"
  >
    <div v-if="device" class="device-details-content">
      <!-- 设备基本信息 -->
      <div class="device-info-section">
        <h3 class="section-title">
          <MonitorOutlined />
          设备信息
        </h3>
        
        <a-row :gutter="16" class="info-grid">
          <a-col :xs="24" :sm="12">
            <div class="info-item">
              <label>设备别名：</label>
              <span>{{ device.name || '未命名设备' }}</span>
            </div>
          </a-col>
          <a-col :xs="24" :sm="12">
            <div class="info-item">
              <label>设备地址：</label>
              <span class="url-text">{{ device.api_base_url }}</span>
            </div>
          </a-col>
          <a-col :xs="24" :sm="12">
            <div class="info-item">
              <label>设备类型：</label>
              <a-tag v-if="device.device_type" color="blue">
                {{ device.device_type }}
              </a-tag>
              <span v-else class="text-secondary">-</span>
            </div>
          </a-col>
          <a-col :xs="24" :sm="12">
            <div class="info-item">
              <label>设备状态：</label>
              <a-badge
                :status="getStatusBadge(device.status)"
                :text="getStatusText(device.status)"
              />
            </div>
          </a-col>
          <a-col :xs="24" :sm="12">
            <div class="info-item">
              <label>设备序列号：</label>
              <span>{{ device.device_sn || '-' }}</span>
            </div>
          </a-col>
          <a-col :xs="24" :sm="12">
            <div class="info-item">
              <label>最后同步时间：</label>
              <span>{{ formatTime(device.last_sync_at) }}</span>
            </div>
          </a-col>
        </a-row>

        <!-- 软件版本信息 -->
        <div v-if="device.version" class="version-section">
          <label>软件版本：</label>
          <a-typography-paragraph
            :code="true"
            :copyable="{ text: device.version }"
            class="version-info"
          >
            <pre>{{ formatVersion(device.version) }}</pre>
          </a-typography-paragraph>
        </div>

        <!-- 错误信息 -->
        <div v-if="device.sync_error" class="error-section">
          <label>同步错误：</label>
          <a-alert
            :message="device.sync_error"
            type="error"
            show-icon
            class="error-alert"
          />
        </div>
      </div>

      <a-divider />

      <!-- 算法应用列表 -->
      <div class="apps-section">
        <h3 class="section-title">
          <AppstoreOutlined />
          算法应用
          <a-button
            type="text"
            size="small"
            :loading="loadingApps"
            @click="loadDeviceApps"
          >
            <template #icon>
              <ReloadOutlined />
            </template>
            刷新
          </a-button>
        </h3>

        <!-- 搜索框 -->
        <div class="apps-toolbar">
          <a-input
            v-model:value="appSearchKeyword"
            placeholder="搜索算法名称"
            allow-clear
            style="width: 280px"
          >
            <template #prefix>
              <SearchOutlined />
            </template>
          </a-input>
        </div>

        <!-- 算法列表 -->
        <a-table
          :data-source="filteredApps"
          :columns="appColumns"
          :loading="loadingApps"
          :pagination="appPagination"
          size="middle"
          class="apps-table"
          row-key="id"
        >
          <!-- 算法名称列 -->
          <template #appName="{ record }">
            <div class="app-name">
              <a-typography-text strong>{{ record.name }}</a-typography-text>
              <div class="app-type">{{ record.type }}</div>
            </div>
          </template>

          <!-- 路数使用情况列 -->
          <template #usage="{ record }">
            <div class="usage-info">
              <a-progress
                :percent="getUsagePercent(record.used, record.limit)"
                :size="[120, 6]"
                :status="getUsageStatus(record.used, record.limit)"
                :show-info="false"
              />
              <span class="usage-text">
                {{ record.used }} / {{ record.limit }}
              </span>
            </div>
          </template>

          <!-- 到期时间列 -->
          <template #expiredAt="{ record }">
            <div class="expire-info">
              <span :class="getExpireClass(record.expired_at)">
                {{ formatExpireTime(record.expired_at) }}
              </span>
            </div>
          </template>
        </a-table>
      </div>
    </div>
  </a-modal>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { message } from 'ant-design-vue'
import {
  MonitorOutlined,
  AppstoreOutlined,
  ReloadOutlined,
  SearchOutlined
} from '@ant-design/icons-vue'
import type { TableColumnsType } from 'ant-design-vue'
import type { Device } from '@/api/device'
import { getDeviceSources } from '@/api/device'

interface Props {
  visible: boolean
  device: Device | null
}

const props = withDefaults(defineProps<Props>(), {
  visible: false,
  device: null
})

const emit = defineEmits<{
  'update:visible': [value: boolean]
}>()

const loadingApps = ref(false)
const deviceApps = ref<any[]>([])
const appSearchKeyword = ref('')

const visible = computed({
  get: () => props.visible,
  set: (value: boolean) => emit('update:visible', value)
})

// 算法表格列配置
const appColumns: TableColumnsType = [
  {
    title: '算法信息',
    dataIndex: 'name',
    key: 'name',
    width: 200,
    slots: { customRender: 'appName' }
  },
  {
    title: '路数使用',
    key: 'usage',
    width: 180,
    align: 'center',
    slots: { customRender: 'usage' }
  },
  {
    title: '授权到期时间',
    dataIndex: 'expired_at',
    key: 'expired_at',
    width: 150,
    slots: { customRender: 'expiredAt' }
  }
]

// 过滤后的算法列表
const filteredApps = computed(() => {
  if (!appSearchKeyword.value) {
    return deviceApps.value
  }
  return deviceApps.value.filter(app =>
    app.name.toLowerCase().includes(appSearchKeyword.value.toLowerCase())
  )
})

// 算法列表分页配置
const appPagination = computed(() => ({
  total: filteredApps.value.length,
  pageSize: 10,
  showSizeChanger: true,
  showQuickJumper: true,
  showTotal: (total: number, range: [number, number]) =>
    `第 ${range[0]}-${range[1]} 项，共 ${total} 项`,
  pageSizeOptions: ['5', '10', '20', '50']
}))

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

// 格式化时间
const formatTime = (timestamp?: string) => {
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

// 格式化版本信息
const formatVersion = (version: string) => {
  if (!version) return '-'
  try {
    const versionObj = JSON.parse(version)
    return JSON.stringify(versionObj, null, 2)
  } catch {
    return version
  }
}

// 获取使用率百分比
const getUsagePercent = (used: number, limit: number) => {
  if (limit === 0) return 0
  return Math.round((used / limit) * 100)
}

// 获取使用率状态
const getUsageStatus = (used: number, limit: number) => {
  const percent = getUsagePercent(used, limit)
  if (percent >= 90) return 'exception'
  if (percent >= 70) return 'active'
  return 'success'
}

// 获取到期时间样式类
const getExpireClass = (expiredAt: string) => {
  if (!expiredAt) return 'text-secondary'
  
  const expireDate = new Date(expiredAt)
  const now = new Date()
  const daysLeft = Math.ceil((expireDate.getTime() - now.getTime()) / (1000 * 60 * 60 * 24))
  
  if (daysLeft < 0) return 'expire-overdue'
  if (daysLeft <= 7) return 'expire-warning'
  if (daysLeft <= 30) return 'expire-soon'
  return 'expire-normal'
}

// 格式化到期时间
const formatExpireTime = (expiredAt: string) => {
  if (!expiredAt) return '永久授权'
  
  const expireDate = new Date(expiredAt)
  const now = new Date()
  const daysLeft = Math.ceil((expireDate.getTime() - now.getTime()) / (1000 * 60 * 60 * 24))
  
  if (daysLeft < 0) return '已过期'
  if (daysLeft === 0) return '今天到期'
  if (daysLeft <= 30) return `${daysLeft}天后到期`
  
  return expireDate.toLocaleDateString('zh-CN')
}

// 加载设备算法应用
const loadDeviceApps = async () => {
  if (!props.device) return
  
  loadingApps.value = true
  try {
    // 这里暂时使用模拟数据，实际应该调用获取设备算法应用的API
    // const response = await getDeviceApps(props.device.id)
    
    // 模拟数据
    await new Promise(resolve => setTimeout(resolve, 1000))
    deviceApps.value = [
      {
        id: 1,
        name: '人员检测算法',
        type: '检测算法',
        limit: 10,
        used: 3,
        expired_at: '2024-12-31T23:59:59'
      },
      {
        id: 2,
        name: '车辆识别算法',
        type: '识别算法',
        limit: 5,
        used: 5,
        expired_at: '2024-09-15T23:59:59'
      },
      {
        id: 3,
        name: '烟火检测算法',
        type: '检测算法',
        limit: 8,
        used: 1,
        expired_at: null
      }
    ]
    
    message.success('算法列表加载成功')
  } catch (error: any) {
    console.error('加载算法列表失败:', error)
    message.error('加载算法列表失败')
    deviceApps.value = []
  } finally {
    loadingApps.value = false
  }
}

// 监听对话框打开
watch(visible, (newVisible) => {
  if (newVisible && props.device) {
    loadDeviceApps()
  } else {
    deviceApps.value = []
    appSearchKeyword.value = ''
  }
})
</script>

<style scoped>
.device-details-content {
  padding: 8px 0;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 16px 0;
  font-size: 16px;
  font-weight: 600;
  color: var(--text-primary);
}

.section-title .anticon {
  color: var(--color-primary-500);
}

.info-grid {
  margin-bottom: 16px;
}

.info-item {
  margin-bottom: 12px;
}

.info-item label {
  display: inline-block;
  width: 120px;
  font-weight: 500;
  color: var(--text-secondary);
}

.info-item span {
  color: var(--text-primary);
}

.url-text {
  font-family: monospace;
  font-size: 13px;
  word-break: break-all;
}

.version-section {
  margin-top: 16px;
}

.version-section label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: var(--text-secondary);
}

.version-info {
  margin-bottom: 0 !important;
}

.version-info pre {
  margin: 0;
  font-size: 12px;
  max-height: 120px;
  overflow-y: auto;
}

.error-section {
  margin-top: 16px;
}

.error-section label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: var(--text-secondary);
}

.error-alert {
  border-radius: 6px;
}

.apps-toolbar {
  margin-bottom: 16px;
}

.apps-table {
  margin-top: 16px;
}

.app-name .app-type {
  font-size: 12px;
  color: var(--text-secondary);
  margin-top: 2px;
}

.usage-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.usage-text {
  font-size: 12px;
  color: var(--text-secondary);
}

.expire-info {
  text-align: center;
}

.expire-normal {
  color: var(--color-success-500);
}

.expire-soon {
  color: var(--color-warning-500);
}

.expire-warning {
  color: var(--color-error-500);
  font-weight: 500;
}

.expire-overdue {
  color: var(--color-error-500);
  font-weight: 600;
  text-decoration: line-through;
}

.text-secondary {
  color: var(--text-secondary);
}

:deep(.ant-typography-copy) {
  color: var(--color-primary-500);
}

/* 响应式调整 */
@media (max-width: 768px) {
  .info-item label {
    width: 100px;
    font-size: 13px;
  }
  
  .apps-toolbar {
    text-align: center;
  }
  
  .apps-toolbar .ant-input {
    width: 100% !important;
  }
}
</style>