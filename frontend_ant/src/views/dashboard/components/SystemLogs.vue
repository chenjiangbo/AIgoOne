<template>
  <div class="system-logs">
    <!-- 页面头部 -->
    <div class="page-header">
      <div class="header-left">
        <h2 class="page-title">系统日志</h2>
        <p class="page-description">查看和管理系统运行日志</p>
      </div>
      <div class="header-actions">
        <a-button @click="refreshLogs">
          <template #icon><ReloadOutlined /></template>
          刷新
        </a-button>
        <a-button @click="clearLogs" danger>
          <template #icon><DeleteOutlined /></template>
          清空日志
        </a-button>
        <a-button @click="exportLogs">
          <template #icon><DownloadOutlined /></template>
          导出日志
        </a-button>
      </div>
    </div>

    <!-- 筛选器 -->
    <div class="filter-bar">
      <a-row :gutter="16" align="middle">
        <a-col :span="4">
          <a-select
            v-model:value="filters.level"
            placeholder="日志级别"
            allow-clear
          >
            <a-select-option value="DEBUG">DEBUG</a-select-option>
            <a-select-option value="INFO">INFO</a-select-option>
            <a-select-option value="WARN">WARN</a-select-option>
            <a-select-option value="ERROR">ERROR</a-select-option>
            <a-select-option value="FATAL">FATAL</a-select-option>
          </a-select>
        </a-col>
        
        <a-col :span="4">
          <a-select
            v-model:value="filters.module"
            placeholder="模块"
            allow-clear
          >
            <a-select-option value="system">系统</a-select-option>
            <a-select-option value="auth">认证</a-select-option>
            <a-select-option value="device">设备</a-select-option>
            <a-select-option value="algorithm">算法</a-select-option>
            <a-select-option value="api">API</a-select-option>
          </a-select>
        </a-col>
        
        <a-col :span="6">
          <a-range-picker
            v-model:value="filters.timeRange"
            show-time
            format="YYYY-MM-DD HH:mm:ss"
            placeholder="['开始时间', '结束时间']"
          />
        </a-col>
        
        <a-col :span="6">
          <a-input
            v-model:value="filters.keyword"
            placeholder="搜索关键词..."
            allow-clear
          >
            <template #prefix>
              <SearchOutlined />
            </template>
          </a-input>
        </a-col>
        
        <a-col :span="4">
          <a-space>
            <a-button type="primary" @click="applyFilters">
              查询
            </a-button>
            <a-button @click="resetFilters">
              重置
            </a-button>
          </a-space>
        </a-col>
      </a-row>
    </div>

    <!-- 日志统计 -->
    <a-row :gutter="16" class="stats-row">
      <a-col :span="4">
        <a-statistic title="总日志数" :value="logStats.total" />
      </a-col>
      <a-col :span="4">
        <a-statistic title="错误" :value="logStats.error" value-style="color: #cf1322" />
      </a-col>
      <a-col :span="4">
        <a-statistic title="警告" :value="logStats.warn" value-style="color: #d46b08" />
      </a-col>
      <a-col :span="4">
        <a-statistic title="信息" :value="logStats.info" value-style="color: #1890ff" />
      </a-col>
      <a-col :span="4">
        <a-statistic title="调试" :value="logStats.debug" value-style="color: #52c41a" />
      </a-col>
      <a-col :span="4">
        <a-switch 
          v-model:checked="autoRefresh" 
          checked-children="自动刷新" 
          un-checked-children="手动刷新"
          @change="handleAutoRefreshChange"
        />
      </a-col>
    </a-row>

    <!-- 日志列表 -->
    <div class="logs-container">
      <div class="logs-header">
        <a-space>
          <span>显示模式:</span>
          <a-radio-group v-model:value="viewMode" button-style="solid" size="small">
            <a-radio-button value="table">表格</a-radio-button>
            <a-radio-button value="text">文本</a-radio-button>
          </a-radio-group>
        </a-space>
      </div>

      <!-- 表格模式 -->
      <div v-if="viewMode === 'table'" class="logs-table">
        <a-table
          :dataSource="filteredLogs"
          :columns="logColumns"
          :loading="loading"
          :scroll="{ x: 1200, y: 400 }"
          size="small"
          row-key="id"
          :pagination="{
            pageSize: 50,
            showSizeChanger: true,
            showQuickJumper: true,
            showTotal: (total) => `共 ${total} 条日志`
          }"
        />
      </div>

      <!-- 文本模式 -->
      <div v-else class="logs-text">
        <div class="log-console" ref="logConsoleRef">
          <div 
            v-for="log in filteredLogs" 
            :key="log.id" 
            class="log-line"
            :class="'log-' + log.level.toLowerCase()"
          >
            <span class="log-timestamp">{{ formatTime(log.timestamp) }}</span>
            <span class="log-level" :class="'level-' + log.level.toLowerCase()">
              [{{ log.level }}]
            </span>
            <span class="log-module">[{{ log.module }}]</span>
            <span class="log-message">{{ log.message }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 日志详情抽屉 -->
    <a-drawer
      v-model:open="logDetailsVisible"
      title="日志详情"
      width="600"
      placement="right"
    >
      <div v-if="currentLog" class="log-details-content">
        <a-descriptions :column="1" bordered size="small">
          <a-descriptions-item label="时间戳">
            {{ formatTime(currentLog.timestamp) }}
          </a-descriptions-item>
          <a-descriptions-item label="日志级别">
            <a-tag :color="getLevelTagColor(currentLog.level)">
              {{ currentLog.level }}
            </a-tag>
          </a-descriptions-item>
          <a-descriptions-item label="模块">
            {{ currentLog.module }}
          </a-descriptions-item>
          <a-descriptions-item label="用户">
            {{ currentLog.user || '-' }}
          </a-descriptions-item>
          <a-descriptions-item label="IP地址">
            {{ currentLog.ip || '-' }}
          </a-descriptions-item>
          <a-descriptions-item label="消息">
            <div class="log-message-detail">
              {{ currentLog.message }}
            </div>
          </a-descriptions-item>
        </a-descriptions>

        <a-divider />

        <div v-if="currentLog.details" class="log-details-json">
          <h4>详细信息</h4>
          <pre class="details-content">{{ JSON.stringify(currentLog.details, null, 2) }}</pre>
        </div>

        <div v-if="currentLog.stackTrace" class="log-stack-trace">
          <h4>堆栈跟踪</h4>
          <pre class="stack-trace-content">{{ currentLog.stackTrace }}</pre>
        </div>
      </div>
    </a-drawer>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, onUnmounted, computed, nextTick, h } from 'vue'
import { message, Modal } from 'ant-design-vue'
import {
  ReloadOutlined,
  DeleteOutlined,
  DownloadOutlined,
  SearchOutlined,
  EyeOutlined
} from '@ant-design/icons-vue'
import type { TableColumnsType } from 'ant-design-vue'
import type { Dayjs } from 'dayjs'

// 日志接口定义
interface SystemLog {
  id: string
  timestamp: string
  level: 'DEBUG' | 'INFO' | 'WARN' | 'ERROR' | 'FATAL'
  module: string
  message: string
  user?: string
  ip?: string
  details?: any
  stackTrace?: string
}

// 状态管理
const loading = ref(false)
const logs = ref<SystemLog[]>([])
const autoRefresh = ref(false)
const viewMode = ref<'table' | 'text'>('table')
const logDetailsVisible = ref(false)
const currentLog = ref<SystemLog | null>(null)
const logConsoleRef = ref<HTMLElement>()

let autoRefreshTimer: number | null = null

// 筛选器
const filters = reactive({
  level: undefined as string | undefined,
  module: undefined as string | undefined,
  timeRange: undefined as [Dayjs, Dayjs] | undefined,
  keyword: ''
})

// Mock数据
const mockLogs: SystemLog[] = [
  {
    id: 'log-1',
    timestamp: '2024-03-16 10:30:15.123',
    level: 'ERROR',
    module: 'device',
    message: '设备连接失败: 华东区域-01号设备',
    user: 'admin',
    ip: '192.168.1.100',
    details: {
      device_id: 'device-1',
      error_code: 'CONNECTION_TIMEOUT',
      retry_count: 3
    },
    stackTrace: 'java.net.ConnectException: Connection timed out\n\tat java.net.PlainSocketImpl.socketConnect(Native Method)\n\tat java.net.AbstractPlainSocketImpl.doConnect(AbstractPlainSocketImpl.java:350)'
  },
  {
    id: 'log-2',
    timestamp: '2024-03-16 10:29:45.456',
    level: 'WARN',
    module: 'algorithm',
    message: 'CPU使用率过高: 85.6%',
    user: 'system',
    ip: 'localhost',
    details: {
      cpu_usage: 85.6,
      memory_usage: 76.3,
      task_count: 5
    }
  },
  {
    id: 'log-3',
    timestamp: '2024-03-16 10:29:30.789',
    level: 'INFO',
    module: 'auth',
    message: '用户登录成功',
    user: 'admin',
    ip: '192.168.1.200',
    details: {
      login_time: '2024-03-16 10:29:30',
      session_id: 'sess_123456'
    }
  },
  {
    id: 'log-4',
    timestamp: '2024-03-16 10:29:10.012',
    level: 'DEBUG',
    module: 'api',
    message: 'API请求处理: GET /api/devices',
    user: 'admin',
    ip: '192.168.1.200',
    details: {
      method: 'GET',
      path: '/api/devices',
      response_time: 156,
      status_code: 200
    }
  },
  {
    id: 'log-5',
    timestamp: '2024-03-16 10:28:55.345',
    level: 'FATAL',
    module: 'system',
    message: '数据库连接池耗尽',
    details: {
      active_connections: 100,
      max_connections: 100,
      pending_requests: 25
    },
    stackTrace: 'org.apache.commons.dbcp2.BasicDataSource$1.makeObject(BasicDataSource.java:2203)\n\tat org.apache.commons.pool2.impl.GenericObjectPool.create(GenericObjectPool.java:868)'
  }
]

// 计算属性
const logStats = computed(() => {
  const stats = { total: 0, error: 0, warn: 0, info: 0, debug: 0, fatal: 0 }
  logs.value.forEach(log => {
    stats.total++
    stats[log.level.toLowerCase() as keyof typeof stats]++
  })
  return stats
})

const filteredLogs = computed(() => {
  let result = logs.value

  if (filters.level) {
    result = result.filter(log => log.level === filters.level)
  }

  if (filters.module) {
    result = result.filter(log => log.module === filters.module)
  }

  if (filters.keyword) {
    const keyword = filters.keyword.toLowerCase()
    result = result.filter(log => 
      log.message.toLowerCase().includes(keyword) ||
      log.module.toLowerCase().includes(keyword) ||
      (log.user && log.user.toLowerCase().includes(keyword))
    )
  }

  if (filters.timeRange && filters.timeRange.length === 2) {
    const [start, end] = filters.timeRange
    result = result.filter(log => {
      const logTime = new Date(log.timestamp).getTime()
      return logTime >= start.valueOf() && logTime <= end.valueOf()
    })
  }

  return result.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime())
})

// 表格列定义
const logColumns: TableColumnsType<SystemLog> = [
  {
    title: '时间',
    dataIndex: 'timestamp',
    key: 'timestamp',
    width: 180,
    customRender: ({ text }) => formatTime(text)
  },
  {
    title: '级别',
    dataIndex: 'level',
    key: 'level',
    width: 80,
    customRender: ({ text }) => {
      return h('a-tag', {
        color: getLevelTagColor(text),
        size: 'small'
      }, text)
    }
  },
  {
    title: '模块',
    dataIndex: 'module',
    key: 'module',
    width: 100
  },
  {
    title: '用户',
    dataIndex: 'user',
    key: 'user',
    width: 100,
    customRender: ({ text }) => text || '-'
  },
  {
    title: 'IP地址',
    dataIndex: 'ip',
    key: 'ip',
    width: 120,
    customRender: ({ text }) => text || '-'
  },
  {
    title: '消息',
    dataIndex: 'message',
    key: 'message',
    ellipsis: true
  },
  {
    title: '操作',
    key: 'action',
    width: 80,
    fixed: 'right',
    customRender: ({ record }) => {
      return h('a-button', {
        size: 'small',
        onClick: () => viewLogDetails(record)
      }, {
        icon: () => h(EyeOutlined),
        default: () => '详情'
      })
    }
  }
]

// 工具方法
const getLevelTagColor = (level: string) => {
  const colors = {
    DEBUG: 'default',
    INFO: 'processing',
    WARN: 'warning',
    ERROR: 'error',
    FATAL: 'error'
  }
  return colors[level as keyof typeof colors] || 'default'
}

const formatTime = (timeString: string) => {
  if (!timeString) return ''
  return new Date(timeString).toLocaleString('zh-CN', { 
    fractionalSecondDigits: 3 
  } as any)
}

// 事件处理
const refreshLogs = async () => {
  loading.value = true
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    // 模拟实时日志数据
    const newLogs = [...mockLogs]
    if (logs.value.length > 0) {
      // 添加一些新的日志条目
      const newLog: SystemLog = {
        id: `log-${Date.now()}`,
        timestamp: new Date().toISOString().replace('T', ' ').replace('Z', ''),
        level: ['DEBUG', 'INFO', 'WARN', 'ERROR'][Math.floor(Math.random() * 4)] as any,
        module: ['system', 'auth', 'device', 'algorithm', 'api'][Math.floor(Math.random() * 5)],
        message: '实时日志消息 - ' + new Date().toLocaleTimeString(),
        user: 'admin',
        ip: '192.168.1.100'
      }
      newLogs.unshift(newLog)
    }
    
    logs.value = newLogs
    message.success('日志刷新成功')
    
    // 如果是文本模式，滚动到底部
    if (viewMode.value === 'text') {
      nextTick(() => {
        if (logConsoleRef.value) {
          logConsoleRef.value.scrollTop = logConsoleRef.value.scrollHeight
        }
      })
    }
  } catch (error: any) {
    message.error('刷新日志失败: ' + error.message)
  } finally {
    loading.value = false
  }
}

const clearLogs = () => {
  Modal.confirm({
    title: '清空日志确认',
    content: '确定要清空所有日志吗？此操作不可恢复。',
    okText: '确定',
    cancelText: '取消',
    okType: 'danger',
    onOk: () => {
      logs.value = []
      message.success('日志已清空')
    }
  })
}

const exportLogs = () => {
  try {
    const logsData = filteredLogs.value.map(log => ({
      时间: formatTime(log.timestamp),
      级别: log.level,
      模块: log.module,
      用户: log.user || '-',
      IP地址: log.ip || '-',
      消息: log.message
    }))
    
    const csvContent = [
      Object.keys(logsData[0]).join(','),
      ...logsData.map(row => Object.values(row).map(val => `"${val}"`).join(','))
    ].join('\n')
    
    const blob = new Blob(['\ufeff' + csvContent], { type: 'text/csv;charset=utf-8' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `system-logs-${new Date().toISOString().split('T')[0]}.csv`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
    message.success('日志导出成功')
  } catch (error: any) {
    message.error('日志导出失败: ' + error.message)
  }
}

const applyFilters = () => {
  message.success('筛选条件已应用')
}

const resetFilters = () => {
  Object.assign(filters, {
    level: undefined,
    module: undefined,
    timeRange: undefined,
    keyword: ''
  })
  message.success('筛选条件已重置')
}

const handleAutoRefreshChange = (checked: boolean) => {
  if (checked) {
    autoRefreshTimer = window.setInterval(() => {
      refreshLogs()
    }, 5000) // 每5秒刷新一次
    message.success('已开启自动刷新')
  } else {
    if (autoRefreshTimer) {
      clearInterval(autoRefreshTimer)
      autoRefreshTimer = null
    }
    message.success('已关闭自动刷新')
  }
}

const viewLogDetails = (log: SystemLog) => {
  currentLog.value = log
  logDetailsVisible.value = true
}

// 生命周期
onMounted(() => {
  refreshLogs()
})

onUnmounted(() => {
  if (autoRefreshTimer) {
    clearInterval(autoRefreshTimer)
  }
})
</script>

<style lang="less" scoped>
.system-logs {
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

// 筛选栏
.filter-bar {
  padding: 16px;
  background: #fafafa;
  border-radius: 6px;
  margin-bottom: 16px;
}

// 统计行
.stats-row {
  margin-bottom: 16px;
  padding: 16px;
  background: #f5f5f5;
  border-radius: 6px;
}

// 日志容器
.logs-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.logs-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid #f0f0f0;
}

// 表格模式
.logs-table {
  flex: 1;
  overflow: hidden;
}

// 文本模式
.logs-text {
  flex: 1;
  overflow: hidden;
}

.log-console {
  height: 100%;
  background: #1e1e1e;
  color: #f0f0f0;
  font-family: 'Courier New', monospace;
  font-size: 12px;
  line-height: 1.4;
  padding: 12px;
  overflow-y: auto;
  border-radius: 4px;
}

.log-line {
  margin-bottom: 2px;
  word-break: break-all;
}

.log-timestamp {
  color: #888;
  margin-right: 8px;
}

.log-level {
  margin-right: 8px;
  font-weight: bold;
  
  &.level-debug { color: #52c41a; }
  &.level-info { color: #1890ff; }
  &.level-warn { color: #faad14; }
  &.level-error { color: #ff4d4f; }
  &.level-fatal { color: #a61e69; }
}

.log-module {
  color: #40a9ff;
  margin-right: 8px;
}

.log-message {
  color: #f0f0f0;
}

// 日志详情
.log-details-content {
  .log-message-detail {
    padding: 8px;
    background: #f5f5f5;
    border-radius: 4px;
    border-left: 4px solid #1890ff;
  }
  
  .log-details-json,
  .log-stack-trace {
    margin-top: 16px;
    
    h4 {
      margin-bottom: 8px;
      color: #262626;
    }
    
    .details-content,
    .stack-trace-content {
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
    
    .stack-trace-content {
      background: #fff2f0;
      border-color: #ffccc7;
      color: #a8071a;
    }
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
    :deep(.ant-row) {
      flex-wrap: wrap;
      gap: 8px;
    }
  }
}

@media (max-width: 768px) {
  .system-logs {
    padding: 16px;
  }
  
  .stats-row {
    :deep(.ant-col) {
      margin-bottom: 8px;
    }
  }
}
</style>