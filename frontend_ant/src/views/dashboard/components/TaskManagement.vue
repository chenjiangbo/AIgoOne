<template>
  <div class="task-management">
    <!-- 页面头部 -->
    <div class="page-header">
      <div class="header-left">
        <h2 class="page-title">任务管理</h2>
        <p class="page-description">管理和监控算法任务的执行状态</p>
      </div>
      <div class="header-actions">
        <a-button @click="refreshTasks">
          <template #icon><ReloadOutlined /></template>
          刷新
        </a-button>
        <a-button type="primary" @click="showCreateTaskDialog">
          <template #icon><PlusOutlined /></template>
          创建任务
        </a-button>
      </div>
    </div>

    <!-- 任务统计卡片 -->
    <a-row :gutter="16" class="stats-row">
      <a-col :span="6">
        <a-card>
          <a-statistic title="总任务数" :value="taskStats.total" />
        </a-card>
      </a-col>
      <a-col :span="6">
        <a-card>
          <a-statistic title="运行中" :value="taskStats.running" value-style="color: #3f8600" />
        </a-card>
      </a-col>
      <a-col :span="6">
        <a-card>
          <a-statistic title="已完成" :value="taskStats.completed" value-style="color: #1890ff" />
        </a-card>
      </a-col>
      <a-col :span="6">
        <a-card>
          <a-statistic title="失败" :value="taskStats.failed" value-style="color: #cf1322" />
        </a-card>
      </a-col>
    </a-row>

    <!-- 任务列表 -->
    <div class="task-list">
      <a-table 
        :dataSource="tasks" 
        :columns="taskColumns"
        :loading="loading"
        row-key="id"
        size="middle"
        :pagination="{
          showSizeChanger: true,
          showQuickJumper: true,
          showTotal: (total) => `共 ${total} 条记录`
        }"
      />
    </div>

    <!-- 创建任务对话框 -->
    <a-modal
      v-model:open="createTaskVisible"
      title="创建任务"
      width="600px"
      :confirmLoading="creating"
      @ok="handleCreateTask"
      @cancel="createTaskVisible = false"
    >
      <a-form
        ref="createTaskFormRef"
        :model="createTaskForm"
        :rules="createTaskRules"
        :label-col="{ span: 6 }"
        :wrapper-col="{ span: 18 }"
      >
        <a-form-item label="任务名称" name="name">
          <a-input v-model:value="createTaskForm.name" placeholder="请输入任务名称" />
        </a-form-item>
        
        <a-form-item label="任务类型" name="type">
          <a-select v-model:value="createTaskForm.type" placeholder="请选择任务类型">
            <a-select-option value="detection">目标检测</a-select-option>
            <a-select-option value="recognition">图像识别</a-select-option>
            <a-select-option value="tracking">目标跟踪</a-select-option>
            <a-select-option value="analysis">行为分析</a-select-option>
          </a-select>
        </a-form-item>
        
        <a-form-item label="视频源" name="video_source_id">
          <a-select v-model:value="createTaskForm.video_source_id" placeholder="请选择视频源">
            <a-select-option
              v-for="source in availableVideoSources"
              :key="source.id"
              :value="source.id"
            >
              {{ source.name }}
            </a-select-option>
          </a-select>
        </a-form-item>
        
        <a-form-item label="算法模型" name="algorithm_id">
          <a-select v-model:value="createTaskForm.algorithm_id" placeholder="请选择算法模型">
            <a-select-option
              v-for="algo in availableAlgorithms"
              :key="algo.id"
              :value="algo.id"
            >
              {{ algo.name }} ({{ algo.version }})
            </a-select-option>
          </a-select>
        </a-form-item>
        
        <a-form-item label="任务描述" name="description">
          <a-textarea 
            v-model:value="createTaskForm.description" 
            :rows="3"
            placeholder="请输入任务描述"
          />
        </a-form-item>
      </a-form>
    </a-modal>

    <!-- 任务详情抽屉 -->
    <a-drawer
      v-model:open="taskDetailsVisible"
      :title="currentTask?.name || '任务详情'"
      width="600"
      placement="right"
    >
      <div v-if="currentTask" class="task-details-content">
        <a-descriptions title="基本信息" :column="1" bordered size="small">
          <a-descriptions-item label="任务名称">{{ currentTask.name }}</a-descriptions-item>
          <a-descriptions-item label="任务类型">
            <a-tag :color="getTypeTagColor(currentTask.type)">{{ getTypeText(currentTask.type) }}</a-tag>
          </a-descriptions-item>
          <a-descriptions-item label="执行状态">
            <a-tag :color="getStatusTagColor(currentTask.status)">
              <template #icon>
                <component :is="getStatusIcon(currentTask.status)" />
              </template>
              {{ getStatusText(currentTask.status) }}
            </a-tag>
          </a-descriptions-item>
          <a-descriptions-item label="创建时间">{{ formatTime(currentTask.created_at) }}</a-descriptions-item>
          <a-descriptions-item label="开始时间">{{ formatTime(currentTask.started_at) || '-' }}</a-descriptions-item>
          <a-descriptions-item label="结束时间">{{ formatTime(currentTask.finished_at) || '-' }}</a-descriptions-item>
          <a-descriptions-item label="执行进度">
            <a-progress :percent="currentTask.progress" size="small" />
          </a-descriptions-item>
          <a-descriptions-item label="任务描述">{{ currentTask.description || '-' }}</a-descriptions-item>
        </a-descriptions>

        <a-divider />

        <a-descriptions title="执行日志" :column="1">
          <a-descriptions-item>
            <div class="task-logs">
              <pre v-if="currentTask.logs" class="log-content">{{ currentTask.logs }}</pre>
              <a-empty v-else description="暂无日志信息" />
            </div>
          </a-descriptions-item>
        </a-descriptions>
      </div>
    </a-drawer>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, computed, h } from 'vue'
import { message, Modal } from 'ant-design-vue'
import {
  PlusOutlined,
  ReloadOutlined,
  PlayCircleOutlined,
  PauseCircleOutlined,
  StopOutlined,
  EyeOutlined,
  DeleteOutlined,
  CheckCircleOutlined,
  CloseCircleOutlined,
  ClockCircleOutlined,
  ExclamationCircleOutlined,
  SyncOutlined
} from '@ant-design/icons-vue'
import type { FormInstance, Rule } from 'ant-design-vue/es/form'
import type { TableColumnsType } from 'ant-design-vue'
import type { Component } from 'vue'

// 任务接口定义
interface Task {
  id: string
  name: string
  type: 'detection' | 'recognition' | 'tracking' | 'analysis'
  status: 'pending' | 'running' | 'completed' | 'failed' | 'stopped'
  progress: number
  video_source_id?: string
  video_source_name?: string
  algorithm_id?: string
  algorithm_name?: string
  created_at: string
  started_at?: string
  finished_at?: string
  description?: string
  logs?: string
}

// 状态管理
const loading = ref(false)
const tasks = ref<Task[]>([])
const createTaskVisible = ref(false)
const creating = ref(false)
const taskDetailsVisible = ref(false)
const currentTask = ref<Task | null>(null)

// 表单
const createTaskFormRef = ref<FormInstance>()
const createTaskForm = reactive({
  name: '',
  type: '',
  video_source_id: '',
  algorithm_id: '',
  description: ''
})

// 表单验证规则
const createTaskRules: Record<string, Rule[]> = {
  name: [
    { required: true, message: '请输入任务名称', trigger: 'blur' }
  ],
  type: [
    { required: true, message: '请选择任务类型', trigger: 'change' }
  ],
  video_source_id: [
    { required: true, message: '请选择视频源', trigger: 'change' }
  ],
  algorithm_id: [
    { required: true, message: '请选择算法模型', trigger: 'change' }
  ]
}

// Mock数据
const mockTasks: Task[] = [
  {
    id: 'task-1',
    name: '入口车辆检测',
    type: 'detection',
    status: 'running',
    progress: 75,
    video_source_id: 'stream-1',
    video_source_name: '入口摄像头-01',
    algorithm_id: 'algo-1',
    algorithm_name: 'YOLOv8车辆检测',
    created_at: '2024-03-16 09:30:00',
    started_at: '2024-03-16 09:31:00',
    description: '检测入口处的车辆并进行计数',
    logs: '2024-03-16 09:31:00 [INFO] 任务启动\n2024-03-16 09:31:05 [INFO] 模型加载完成\n2024-03-16 09:31:10 [INFO] 开始处理视频流\n2024-03-16 10:15:30 [INFO] 已检测车辆: 245辆'
  },
  {
    id: 'task-2',
    name: '停车场行为分析',
    type: 'analysis',
    status: 'completed',
    progress: 100,
    video_source_id: 'stream-3',
    video_source_name: '内场监控-A区',
    algorithm_id: 'algo-2',
    algorithm_name: '行为识别模型v2.1',
    created_at: '2024-03-16 08:00:00',
    started_at: '2024-03-16 08:01:00',
    finished_at: '2024-03-16 09:00:00',
    description: '分析停车场内的异常行为',
    logs: '2024-03-16 08:01:00 [INFO] 任务启动\n2024-03-16 08:01:05 [INFO] 模型加载完成\n2024-03-16 09:00:00 [INFO] 任务完成，检测到3起异常行为'
  },
  {
    id: 'task-3',
    name: '车牌识别测试',
    type: 'recognition',
    status: 'failed',
    progress: 30,
    video_source_id: 'stream-2',
    video_source_name: '出口摄像头-01',
    algorithm_id: 'algo-3',
    algorithm_name: '车牌识别OCR',
    created_at: '2024-03-16 07:30:00',
    started_at: '2024-03-16 07:31:00',
    finished_at: '2024-03-16 07:35:00',
    description: '识别出入口车辆的车牌号码',
    logs: '2024-03-16 07:31:00 [INFO] 任务启动\n2024-03-16 07:31:05 [ERROR] 模型加载失败\n2024-03-16 07:35:00 [ERROR] 任务异常终止'
  }
]

const availableVideoSources = ref([
  { id: 'stream-1', name: '入口摄像头-01' },
  { id: 'stream-2', name: '出口摄像头-01' },
  { id: 'stream-3', name: '内场监控-A区' },
  { id: 'stream-4', name: '内场监控-B区' }
])

const availableAlgorithms = ref([
  { id: 'algo-1', name: 'YOLOv8车辆检测', version: 'v1.0' },
  { id: 'algo-2', name: '行为识别模型', version: 'v2.1' },
  { id: 'algo-3', name: '车牌识别OCR', version: 'v1.5' }
])

// 计算属性
const taskStats = computed(() => {
  const stats = { total: 0, running: 0, completed: 0, failed: 0 }
  tasks.value.forEach(task => {
    stats.total++
    switch (task.status) {
      case 'running':
        stats.running++
        break
      case 'completed':
        stats.completed++
        break
      case 'failed':
        stats.failed++
        break
    }
  })
  return stats
})

// 表格列定义
const taskColumns: TableColumnsType<Task> = [
  {
    title: '任务名称',
    dataIndex: 'name',
    key: 'name',
    width: 200
  },
  {
    title: '任务类型',
    dataIndex: 'type',
    key: 'type',
    width: 120,
    customRender: ({ text }) => {
      return h('a-tag', {
        color: getTypeTagColor(text),
        size: 'small'
      }, getTypeText(text))
    }
  },
  {
    title: '执行状态',
    dataIndex: 'status',
    key: 'status',
    width: 120,
    customRender: ({ text }) => {
      return h('a-tag', {
        color: getStatusTagColor(text),
        size: 'small'
      }, [
        h(getStatusIcon(text), { style: { marginRight: '4px' } }),
        getStatusText(text)
      ])
    }
  },
  {
    title: '进度',
    dataIndex: 'progress',
    key: 'progress',
    width: 150,
    customRender: ({ text }) => {
      return h('a-progress', {
        percent: text,
        size: 'small',
        showInfo: true
      })
    }
  },
  {
    title: '视频源',
    dataIndex: 'video_source_name',
    key: 'video_source_name',
    width: 150,
    customRender: ({ text }) => text || '-'
  },
  {
    title: '创建时间',
    dataIndex: 'created_at',
    key: 'created_at',
    width: 150,
    customRender: ({ text }) => formatTime(text)
  },
  {
    title: '操作',
    key: 'action',
    width: 200,
    fixed: 'right',
    customRender: ({ record }) => {
      const actions = []
      
      if (record.status === 'pending') {
        actions.push(
          h('a-button', {
            size: 'small',
            onClick: () => startTask(record)
          }, {
            icon: () => h(PlayCircleOutlined),
            default: () => '启动'
          })
        )
      }
      
      if (record.status === 'running') {
        actions.push(
          h('a-button', {
            size: 'small',
            onClick: () => pauseTask(record)
          }, {
            icon: () => h(PauseCircleOutlined),
            default: () => '暂停'
          })
        )
        actions.push(
          h('a-button', {
            size: 'small',
            danger: true,
            onClick: () => stopTask(record)
          }, {
            icon: () => h(StopOutlined),
            default: () => '停止'
          })
        )
      }
      
      actions.push(
        h('a-button', {
          size: 'small',
          onClick: () => viewTaskDetails(record)
        }, {
          icon: () => h(EyeOutlined),
          default: () => '详情'
        })
      )
      
      if (['completed', 'failed', 'stopped'].includes(record.status)) {
        actions.push(
          h('a-button', {
            size: 'small',
            danger: true,
            onClick: () => deleteTask(record)
          }, {
            icon: () => h(DeleteOutlined),
            default: () => '删除'
          })
        )
      }
      
      return h('a-space', { size: 'small' }, actions)
    }
  }
]

// 工具方法
const getStatusText = (status: string) => {
  const texts = {
    pending: '等待中',
    running: '执行中',
    completed: '已完成',
    failed: '失败',
    stopped: '已停止'
  }
  return texts[status as keyof typeof texts] || status
}

const getStatusTagColor = (status: string) => {
  const colors = {
    pending: 'default',
    running: 'processing',
    completed: 'success',
    failed: 'error',
    stopped: 'warning'
  }
  return colors[status as keyof typeof colors] || 'default'
}

const getStatusIcon = (status: string): Component => {
  const icons: Record<string, Component> = {
    pending: ClockCircleOutlined,
    running: SyncOutlined,
    completed: CheckCircleOutlined,
    failed: CloseCircleOutlined,
    stopped: ExclamationCircleOutlined
  }
  return icons[status] || ClockCircleOutlined
}

const getTypeText = (type: string) => {
  const texts = {
    detection: '目标检测',
    recognition: '图像识别',
    tracking: '目标跟踪',
    analysis: '行为分析'
  }
  return texts[type as keyof typeof texts] || type
}

const getTypeTagColor = (type: string) => {
  const colors = {
    detection: 'blue',
    recognition: 'green',
    tracking: 'orange',
    analysis: 'purple'
  }
  return colors[type as keyof typeof colors] || 'default'
}

const formatTime = (timeString: string) => {
  if (!timeString) return ''
  return new Date(timeString).toLocaleString('zh-CN')
}

// 事件处理
const refreshTasks = async () => {
  loading.value = true
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    tasks.value = [...mockTasks]
    message.success('任务列表刷新成功')
  } catch (error: any) {
    message.error('刷新失败: ' + error.message)
  } finally {
    loading.value = false
  }
}

const showCreateTaskDialog = () => {
  createTaskVisible.value = true
  Object.assign(createTaskForm, {
    name: '',
    type: '',
    video_source_id: '',
    algorithm_id: '',
    description: ''
  })
}

const handleCreateTask = async () => {
  if (!createTaskFormRef.value) return
  
  try {
    await createTaskFormRef.value.validate()
    creating.value = true
    
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    const newTask: Task = {
      id: `task-${Date.now()}`,
      ...createTaskForm,
      status: 'pending',
      progress: 0,
      created_at: new Date().toISOString(),
      video_source_name: availableVideoSources.value.find(s => s.id === createTaskForm.video_source_id)?.name,
      algorithm_name: availableAlgorithms.value.find(a => a.id === createTaskForm.algorithm_id)?.name
    }
    
    tasks.value.unshift(newTask)
    message.success('任务创建成功！')
    createTaskVisible.value = false
  } catch (error: any) {
    if (error.errorFields) {
      return
    }
    message.error('创建任务失败: ' + error.message)
  } finally {
    creating.value = false
  }
}

const startTask = async (task: Task) => {
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    task.status = 'running'
    task.started_at = new Date().toISOString()
    message.success(`任务 ${task.name} 已启动`)
  } catch (error: any) {
    message.error('启动任务失败: ' + error.message)
  }
}

const pauseTask = async (task: Task) => {
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    task.status = 'stopped'
    message.success(`任务 ${task.name} 已暂停`)
  } catch (error: any) {
    message.error('暂停任务失败: ' + error.message)
  }
}

const stopTask = async (task: Task) => {
  Modal.confirm({
    title: '停止确认',
    content: `确定要停止任务 "${task.name}" 吗？`,
    okText: '确定',
    cancelText: '取消',
    okType: 'danger',
    onOk: async () => {
      try {
        await new Promise(resolve => setTimeout(resolve, 1000))
        task.status = 'stopped'
        task.finished_at = new Date().toISOString()
        message.success(`任务 ${task.name} 已停止`)
      } catch (error: any) {
        message.error('停止任务失败: ' + error.message)
      }
    }
  })
}

const viewTaskDetails = (task: Task) => {
  currentTask.value = task
  taskDetailsVisible.value = true
}

const deleteTask = (task: Task) => {
  Modal.confirm({
    title: '删除确认',
    content: `确定要删除任务 "${task.name}" 吗？`,
    okText: '确定',
    cancelText: '取消',
    okType: 'danger',
    onOk: () => {
      const index = tasks.value.findIndex(t => t.id === task.id)
      if (index !== -1) {
        tasks.value.splice(index, 1)
        message.success('删除成功')
      }
    }
  })
}

// 生命周期
onMounted(() => {
  refreshTasks()
})
</script>

<style lang="less" scoped>
.task-management {
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

// 任务列表
.task-list {
  flex: 1;
  overflow: hidden;
}

// 任务详情
.task-details-content {
  .task-logs {
    .log-content {
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
  .task-management {
    padding: 16px;
  }
  
  .stats-row {
    :deep(.ant-col) {
      margin-bottom: 16px;
    }
  }
}
</style>