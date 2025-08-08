<template>
  <div class="event-alerts">
    <!-- 页面头部 -->
    <div class="page-header">
      <div class="header-left">
        <h2 class="page-title">事件告警</h2>
        <p class="page-description">实时监控系统事件和告警信息</p>
      </div>
      <div class="header-actions">
        <a-button @click="refreshAlerts">
          <template #icon><ReloadOutlined /></template>
          刷新
        </a-button>
        <a-button @click="clearAllAlerts" :disabled="alerts.length === 0">
          <template #icon><ClearOutlined /></template>
          清空全部
        </a-button>
      </div>
    </div>

    <!-- 告警统计卡片 -->
    <a-row :gutter="16" class="stats-row">
      <a-col :span="6">
        <a-card>
          <a-statistic title="总告警数" :value="alertStats.total" />
        </a-card>
      </a-col>
      <a-col :span="6">
        <a-card>
          <a-statistic title="严重" :value="alertStats.critical" value-style="color: #cf1322" />
        </a-card>
      </a-col>
      <a-col :span="6">
        <a-card>
          <a-statistic title="警告" :value="alertStats.warning" value-style="color: #d46b08" />
        </a-card>
      </a-col>
      <a-col :span="6">
        <a-card>
          <a-statistic title="信息" :value="alertStats.info" value-style="color: #1890ff" />
        </a-card>
      </a-col>
    </a-row>

    <!-- 筛选器 -->
    <div class="filter-bar">
      <a-space size="middle">
        <span>筛选条件：</span>
        <a-select
          v-model:value="filters.level"
          placeholder="告警级别"
          style="width: 120px"
          allow-clear
        >
          <a-select-option value="critical">严重</a-select-option>
          <a-select-option value="warning">警告</a-select-option>
          <a-select-option value="info">信息</a-select-option>
        </a-select>
        
        <a-select
          v-model:value="filters.type"
          placeholder="事件类型"
          style="width: 150px"
          allow-clear
        >
          <a-select-option value="system">系统事件</a-select-option>
          <a-select-option value="device">设备异常</a-select-option>
          <a-select-option value="algorithm">算法事件</a-select-option>
          <a-select-option value="security">安全事件</a-select-option>
        </a-select>
        
        <a-select
          v-model:value="filters.status"
          placeholder="处理状态"
          style="width: 120px"
          allow-clear
        >
          <a-select-option value="unread">未读</a-select-option>
          <a-select-option value="read">已读</a-select-option>
          <a-select-option value="resolved">已解决</a-select-option>
        </a-select>
        
        <a-range-picker
          v-model:value="filters.timeRange"
          show-time
          format="YYYY-MM-DD HH:mm:ss"
          placeholder="['开始时间', '结束时间']"
        />
        
        <a-button type="primary" @click="applyFilters">
          <template #icon><SearchOutlined /></template>
          查询
        </a-button>
        
        <a-button @click="resetFilters">重置</a-button>
      </a-space>
    </div>

    <!-- 告警列表 -->
    <div class="alert-list">
      <a-list
        :data-source="filteredAlerts"
        :loading="loading"
        item-layout="vertical"
        :pagination="{
          pageSize: 10,
          showSizeChanger: true,
          showQuickJumper: true,
          showTotal: (total) => `共 ${total} 条告警`
        }"
      >
        <template #renderItem="{ item }">
          <a-list-item
            :key="item.id"
            class="alert-item"
            :class="{ 'unread': item.status === 'unread' }"
            @click="handleAlertClick(item)"
          >
            <template #actions>
              <a-button
                v-if="item.status === 'unread'"
                size="small"
                @click.stop="markAsRead(item)"
              >
                标记已读
              </a-button>
              <a-button
                v-if="item.status !== 'resolved'"
                size="small"
                type="primary"
                @click.stop="markAsResolved(item)"
              >
                标记已解决
              </a-button>
              <a-button
                size="small"
                danger
                @click.stop="deleteAlert(item)"
              >
                删除
              </a-button>
            </template>
            
            <template #extra>
              <div class="alert-meta">
                <div class="alert-time">{{ formatTime(item.created_at) }}</div>
                <a-tag :color="getLevelTagColor(item.level)" size="small">
                  <template #icon>
                    <component :is="getLevelIcon(item.level)" />
                  </template>
                  {{ getLevelText(item.level) }}
                </a-tag>
              </div>
            </template>
            
            <a-list-item-meta>
              <template #title>
                <div class="alert-title">
                  <component :is="getTypeIcon(item.type)" :style="{ marginRight: '8px', color: getTypeColor(item.type) }" />
                  {{ item.title }}
                  <a-badge v-if="item.status === 'unread'" status="processing" />
                </div>
              </template>
              
              <template #description>
                <div class="alert-description">
                  <p>{{ item.message }}</p>
                  <div class="alert-details">
                    <a-tag size="small">{{ getTypeText(item.type) }}</a-tag>
                    <span v-if="item.source">来源: {{ item.source }}</span>
                    <span v-if="item.device_name">设备: {{ item.device_name }}</span>
                  </div>
                </div>
              </template>
            </a-list-item-meta>
          </a-list-item>
        </template>
      </a-list>
    </div>

    <!-- 告警详情抽屉 -->
    <a-drawer
      v-model:open="alertDetailsVisible"
      :title="currentAlert?.title || '告警详情'"
      width="600"
      placement="right"
    >
      <div v-if="currentAlert" class="alert-details-content">
        <a-descriptions title="基本信息" :column="1" bordered size="small">
          <a-descriptions-item label="告警标题">{{ currentAlert.title }}</a-descriptions-item>
          <a-descriptions-item label="告警级别">
            <a-tag :color="getLevelTagColor(currentAlert.level)">
              <template #icon>
                <component :is="getLevelIcon(currentAlert.level)" />
              </template>
              {{ getLevelText(currentAlert.level) }}
            </a-tag>
          </a-descriptions-item>
          <a-descriptions-item label="事件类型">
            <a-tag size="small">{{ getTypeText(currentAlert.type) }}</a-tag>
          </a-descriptions-item>
          <a-descriptions-item label="处理状态">
            <a-tag :color="getStatusTagColor(currentAlert.status)">
              {{ getStatusText(currentAlert.status) }}
            </a-tag>
          </a-descriptions-item>
          <a-descriptions-item label="发生时间">{{ formatTime(currentAlert.created_at) }}</a-descriptions-item>
          <a-descriptions-item label="事件来源">{{ currentAlert.source || '-' }}</a-descriptions-item>
          <a-descriptions-item label="相关设备">{{ currentAlert.device_name || '-' }}</a-descriptions-item>
          <a-descriptions-item label="告警消息">
            <div class="alert-message">{{ currentAlert.message }}</div>
          </a-descriptions-item>
        </a-descriptions>

        <a-divider />

        <a-descriptions title="详细信息" :column="1">
          <a-descriptions-item>
            <div class="alert-details-json">
              <pre v-if="currentAlert.details" class="details-content">{{ JSON.stringify(currentAlert.details, null, 2) }}</pre>
              <a-empty v-else description="暂无详细信息" />
            </div>
          </a-descriptions-item>
        </a-descriptions>

        <div class="alert-actions-panel">
          <a-space>
            <a-button
              v-if="currentAlert.status === 'unread'"
              type="primary"
              @click="markAsRead(currentAlert)"
            >
              标记已读
            </a-button>
            <a-button
              v-if="currentAlert.status !== 'resolved'"
              type="primary"
              @click="markAsResolved(currentAlert)"
            >
              标记已解决
            </a-button>
            <a-button danger @click="deleteAlert(currentAlert)">
              删除告警
            </a-button>
          </a-space>
        </div>
      </div>
    </a-drawer>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, computed, h } from 'vue'
import { message, Modal } from 'ant-design-vue'
import {
  ReloadOutlined,
  ClearOutlined,
  SearchOutlined,
  ExclamationCircleOutlined,
  WarningOutlined,
  InfoCircleOutlined,
  DesktopOutlined,
  ToolOutlined,
  BugOutlined,
  SafetyOutlined,
  BellOutlined,
  CheckCircleOutlined,
  CloseCircleOutlined
} from '@ant-design/icons-vue'
import type { Component } from 'vue'
import type { Dayjs } from 'dayjs'

// 告警接口定义
interface Alert {
  id: string
  title: string
  message: string
  level: 'critical' | 'warning' | 'info'
  type: 'system' | 'device' | 'algorithm' | 'security'
  status: 'unread' | 'read' | 'resolved'
  created_at: string
  source?: string
  device_name?: string
  details?: any
}

// 状态管理
const loading = ref(false)
const alerts = ref<Alert[]>([])
const alertDetailsVisible = ref(false)
const currentAlert = ref<Alert | null>(null)

// 筛选器
const filters = reactive({
  level: undefined as string | undefined,
  type: undefined as string | undefined,
  status: undefined as string | undefined,
  timeRange: undefined as [Dayjs, Dayjs] | undefined
})

// Mock数据
const mockAlerts: Alert[] = [
  {
    id: 'alert-1',
    title: '设备连接异常',
    message: '华东区域-01号设备连接超时，请检查网络连接',
    level: 'critical',
    type: 'device',
    status: 'unread',
    created_at: '2024-03-16 10:30:00',
    source: '设备监控系统',
    device_name: '华东区域-01号设备',
    details: {
      device_id: 'device-1',
      error_code: 'CONN_TIMEOUT',
      retry_count: 3,
      last_heartbeat: '2024-03-16 10:25:00'
    }
  },
  {
    id: 'alert-2',
    title: '算法检测异常',
    message: '车辆检测模型在入口摄像头-01上检测到异常行为',
    level: 'warning',
    type: 'algorithm',
    status: 'read',
    created_at: '2024-03-16 10:15:00',
    source: '算法引擎',
    device_name: '入口摄像头-01',
    details: {
      algorithm_id: 'algo-1',
      confidence: 0.85,
      detection_area: '入口区域',
      object_count: 15
    }
  },
  {
    id: 'alert-3',
    title: '系统性能告警',
    message: 'CPU使用率超过85%，建议检查系统负载',
    level: 'warning',
    type: 'system',
    status: 'resolved',
    created_at: '2024-03-16 09:45:00',
    source: '系统监控',
    details: {
      cpu_usage: 87.5,
      memory_usage: 76.3,
      disk_usage: 45.2
    }
  },
  {
    id: 'alert-4',
    title: '用户登录异常',
    message: '检测到异常登录尝试，IP地址: 192.168.1.999',
    level: 'critical',
    type: 'security',
    status: 'unread',
    created_at: '2024-03-16 09:30:00',
    source: '安全监控系统',
    details: {
      ip_address: '192.168.1.999',
      username: 'admin',
      failed_attempts: 5,
      location: '未知地区'
    }
  },
  {
    id: 'alert-5',
    title: '数据备份完成',
    message: '系统数据备份已成功完成',
    level: 'info',
    type: 'system',
    status: 'read',
    created_at: '2024-03-16 08:00:00',
    source: '备份服务',
    details: {
      backup_size: '2.5GB',
      backup_location: '/backup/2024-03-16',
      duration: '15分钟'
    }
  }
]

// 计算属性
const alertStats = computed(() => {
  const stats = { total: 0, critical: 0, warning: 0, info: 0 }
  alerts.value.forEach(alert => {
    stats.total++
    stats[alert.level]++
  })
  return stats
})

const filteredAlerts = computed(() => {
  let result = alerts.value

  if (filters.level) {
    result = result.filter(alert => alert.level === filters.level)
  }

  if (filters.type) {
    result = result.filter(alert => alert.type === filters.type)
  }

  if (filters.status) {
    result = result.filter(alert => alert.status === filters.status)
  }

  if (filters.timeRange && filters.timeRange.length === 2) {
    const [start, end] = filters.timeRange
    result = result.filter(alert => {
      const alertTime = new Date(alert.created_at).getTime()
      return alertTime >= start.valueOf() && alertTime <= end.valueOf()
    })
  }

  return result.sort((a, b) => new Date(b.created_at).getTime() - new Date(a.created_at).getTime())
})

// 工具方法
const getLevelText = (level: string) => {
  const texts = {
    critical: '严重',
    warning: '警告',
    info: '信息'
  }
  return texts[level as keyof typeof texts] || level
}

const getLevelTagColor = (level: string) => {
  const colors = {
    critical: 'error',
    warning: 'warning',
    info: 'processing'
  }
  return colors[level as keyof typeof colors] || 'default'
}

const getLevelIcon = (level: string): Component => {
  const icons: Record<string, Component> = {
    critical: ExclamationCircleOutlined,
    warning: WarningOutlined,
    info: InfoCircleOutlined
  }
  return icons[level] || InfoCircleOutlined
}

const getTypeText = (type: string) => {
  const texts = {
    system: '系统事件',
    device: '设备异常',
    algorithm: '算法事件',
    security: '安全事件'
  }
  return texts[type as keyof typeof texts] || type
}

const getTypeIcon = (type: string): Component => {
  const icons: Record<string, Component> = {
    system: ToolOutlined,
    device: DesktopOutlined,
    algorithm: BugOutlined,
    security: SafetyOutlined
  }
  return icons[type] || BellOutlined
}

const getTypeColor = (type: string) => {
  const colors = {
    system: '#1890ff',
    device: '#52c41a',
    algorithm: '#fa8c16',
    security: '#f5222d'
  }
  return colors[type as keyof typeof colors] || '#666666'
}

const getStatusText = (status: string) => {
  const texts = {
    unread: '未读',
    read: '已读',
    resolved: '已解决'
  }
  return texts[status as keyof typeof texts] || status
}

const getStatusTagColor = (status: string) => {
  const colors = {
    unread: 'processing',
    read: 'default',
    resolved: 'success'
  }
  return colors[status as keyof typeof colors] || 'default'
}

const formatTime = (timeString: string) => {
  if (!timeString) return ''
  return new Date(timeString).toLocaleString('zh-CN')
}

// 事件处理
const refreshAlerts = async () => {
  loading.value = true
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    alerts.value = [...mockAlerts]
    message.success('告警列表刷新成功')
  } catch (error: any) {
    message.error('刷新失败: ' + error.message)
  } finally {
    loading.value = false
  }
}

const clearAllAlerts = () => {
  Modal.confirm({
    title: '清空确认',
    content: '确定要清空所有告警吗？此操作不可恢复。',
    okText: '确定',
    cancelText: '取消',
    okType: 'danger',
    onOk: () => {
      alerts.value = []
      message.success('已清空所有告警')
    }
  })
}

const applyFilters = () => {
  // 筛选逻辑已在计算属性中实现
  message.success('筛选条件已应用')
}

const resetFilters = () => {
  Object.assign(filters, {
    level: undefined,
    type: undefined,
    status: undefined,
    timeRange: undefined
  })
  message.success('筛选条件已重置')
}

const handleAlertClick = (alert: Alert) => {
  currentAlert.value = alert
  alertDetailsVisible.value = true
  
  // 点击查看时自动标记为已读
  if (alert.status === 'unread') {
    markAsRead(alert, false) // 不显示消息提示
  }
}

const markAsRead = (alert: Alert, showMessage = true) => {
  alert.status = 'read'
  if (showMessage) {
    message.success('已标记为已读')
  }
}

const markAsResolved = (alert: Alert) => {
  alert.status = 'resolved'
  message.success('已标记为已解决')
}

const deleteAlert = (alert: Alert) => {
  Modal.confirm({
    title: '删除确认',
    content: `确定要删除告警 "${alert.title}" 吗？`,
    okText: '确定',
    cancelText: '取消',
    okType: 'danger',
    onOk: () => {
      const index = alerts.value.findIndex(a => a.id === alert.id)
      if (index !== -1) {
        alerts.value.splice(index, 1)
        message.success('删除成功')
        
        // 如果当前显示的是被删除的告警，关闭详情抽屉
        if (currentAlert.value?.id === alert.id) {
          alertDetailsVisible.value = false
          currentAlert.value = null
        }
      }
    }
  })
}

// 生命周期
onMounted(() => {
  refreshAlerts()
})
</script>

<style lang="less" scoped>
.event-alerts {
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

// 统计卡片
.stats-row {
  margin-bottom: 24px;
}

// 筛选栏
.filter-bar {
  padding: 16px;
  background: #fafafa;
  border-radius: 6px;
  margin-bottom: 24px;
}

// 告警列表
.alert-list {
  flex: 1;
  overflow: hidden;
  
  .alert-item {
    cursor: pointer;
    transition: background-color 0.3s;
    
    &:hover {
      background-color: #f5f5f5;
    }
    
    &.unread {
      background-color: #f6ffed;
      border-left: 4px solid #52c41a;
    }
  }
  
  .alert-title {
    display: flex;
    align-items: center;
    font-weight: 500;
  }
  
  .alert-meta {
    text-align: right;
    
    .alert-time {
      font-size: 12px;
      color: #666;
      margin-bottom: 8px;
    }
  }
  
  .alert-description {
    p {
      margin-bottom: 8px;
      color: #666;
    }
    
    .alert-details {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 12px;
      color: #999;
      
      span {
        color: #666;
      }
    }
  }
}

// 告警详情
.alert-details-content {
  .alert-message {
    padding: 8px;
    background: #f5f5f5;
    border-radius: 4px;
    border-left: 4px solid #1890ff;
    margin: 8px 0;
  }
  
  .alert-details-json {
    .details-content {
      background: #f5f5f5;
      border: 1px solid #d9d9d9;
      border-radius: 4px;
      padding: 12px;
      font-family: 'Courier New', monospace;
      font-size: 12px;
      line-height: 1.4;
      max-height: 300px;
      overflow-y: auto;
      margin: 0;
    }
  }
  
  .alert-actions-panel {
    margin-top: 24px;
    padding-top: 16px;
    border-top: 1px solid #f0f0f0;
  }
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
  
  .filter-bar {
    :deep(.ant-space) {
      flex-wrap: wrap;
    }
  }
}

@media (max-width: 768px) {
  .event-alerts {
    padding: 16px;
  }
  
  .stats-row {
    :deep(.ant-col) {
      margin-bottom: 16px;
    }
  }
  
  .filter-bar {
    :deep(.ant-space-item) {
      margin-bottom: 8px;
    }
  }
}
</style>