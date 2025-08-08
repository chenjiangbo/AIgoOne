<template>
  <div class="video-sources-panel">
    <!-- 视频源类型切换和操作栏 -->
    <div class="panel-header">
      <div class="type-selector">
        <a-radio-group v-model:value="sourceType" @change="handleTypeChange" button-style="solid">
          <a-radio-button value="stream">视频流</a-radio-button>
          <a-radio-button value="file">视频文件</a-radio-button>
        </a-radio-group>
      </div>
      
      <div class="header-actions">
        <a-input
          v-model:value="searchText"
          placeholder="搜索视频源..."
          allow-clear
          style="width: 240px; margin-right: 16px"
        >
          <template #prefix>
            <SearchOutlined />
          </template>
        </a-input>
        
        <a-button type="primary" @click="fetchVideoSources">
          <template #icon><ReloadOutlined /></template>
          获取视频源
        </a-button>
        
        <a-button @click="refreshSources">
          <template #icon><ReloadOutlined /></template>
        </a-button>
      </div>
    </div>
    
    <!-- 视频源卡片网格 -->
    <div class="sources-grid" v-loading="loading">
      <a-card
        v-for="source in filteredSources"
        :key="source.id"
        class="source-card"
        :hoverable="true"
        size="small"
        @click="previewSource(source)"
      >
        <!-- 视频截图/缩略图 -->
        <div class="source-thumbnail">
          <img 
            v-if="source.thumbnail" 
            :src="source.thumbnail" 
            :alt="source.name"
            @error="handleImageError"
          />
          <div v-else class="placeholder-thumbnail">
            <VideoCameraOutlined style="font-size: 40px" />
            <span>暂无预览</span>
          </div>
          
          <!-- 状态指示器 -->
          <div class="status-indicator">
            <a-tag :color="getStatusTagColor(source.status)" size="small">
              <template #icon>
                <component :is="getStatusIcon(source.status)" />
              </template>
              {{ getStatusText(source.status) }}
            </a-tag>
          </div>
          
          <!-- 播放按钮覆盖层 -->
          <div class="play-overlay">
            <PlayCircleOutlined style="font-size: 30px" />
          </div>
        </div>
        
        <!-- 卡片信息 -->
        <template #actions>
          <a-tooltip title="查看详情">
            <EyeOutlined @click.stop="viewDetails(source)" class="action-btn view-btn" />
          </a-tooltip>
          <a-tooltip title="编辑">
            <EditOutlined @click.stop="editSource(source)" class="action-btn edit-btn" />
          </a-tooltip>
          <a-tooltip title="删除">
            <DeleteOutlined @click.stop="deleteSource(source)" class="action-btn delete-btn" />
          </a-tooltip>
        </template>
        
        <div class="source-info">
          <a-typography-title :level="5" class="source-name" :ellipsis="{ tooltip: source.name }">
            {{ source.name }}
          </a-typography-title>
          <a-typography-text class="source-url" type="secondary" :ellipsis="{ tooltip: source.url }">
            {{ source.url }}
          </a-typography-text>
          
          <div class="source-meta">
            <a-space size="small">
              <span class="meta-item">
                <ClockCircleOutlined style="margin-right: 4px" />
                {{ source.lastUpdate }}
              </span>
              <span class="meta-item" v-if="sourceType === 'stream'">
                <DesktopOutlined style="margin-right: 4px" />
                {{ source.resolution }}
              </span>
            </a-space>
          </div>
        </div>
      </a-card>
      
      <!-- 空状态 -->
      <a-empty 
        v-if="filteredSources.length === 0 && !loading" 
        class="empty-state"
        :image="Empty.PRESENTED_IMAGE_SIMPLE"
        :description="`暂无${sourceType === 'stream' ? '视频流' : '视频文件'}`"
      >
        <a-button type="primary" @click="fetchVideoSources">
          获取视频源
        </a-button>
      </a-empty>
    </div>
    
    <!-- 视频预览弹窗 -->
    <a-modal
      v-model:open="previewVisible"
      :title="currentSource?.name || '视频预览'"
      width="1000px"
      :footer="null"
      :destroy-on-close="true"
      @cancel="handlePreviewClose"
    >
      <div class="video-preview-content">
        <div class="video-player-wrapper">
          <video
            ref="videoPlayerRef"
            :src="currentSource?.url"
            controls
            autoplay
            muted
            class="video-player"
          >
            您的浏览器不支持视频播放
          </video>
          
          <div class="video-overlay" v-if="!videoPlaying">
            <a-spin size="large" tip="加载中..." />
          </div>
        </div>
        
        <!-- 视频信息面板 -->
        <div class="video-info-panel">
          <!-- URL 地址行 -->
          <div class="url-section">
            <LinkOutlined class="url-icon" />
            <a-typography-text code class="url-text" :ellipsis="{ tooltip: currentSource?.url }">
              {{ currentSource?.url }}
            </a-typography-text>
            <a-button 
              size="small" 
              type="text" 
              class="copy-btn"
              @click="copyUrl"
              :title="copySuccess ? '已复制!' : '复制地址'"
            >
              <template #icon>
                <CheckOutlined v-if="copySuccess" style="color: #52c41a" />
                <CopyOutlined v-else />
              </template>
            </a-button>
          </div>
          
          <!-- 参数信息行 -->
          <div class="params-section">
            <a-space size="large" wrap>
              <div class="param-item">
                <component :is="getStatusIcon(currentSource?.status)" 
                  :style="{ color: getStatusIconColor(currentSource?.status), marginRight: '4px' }" />
                <span>状态: {{ getStatusText(currentSource?.status) }}</span>
              </div>
              
              <div class="param-item">
                <DesktopOutlined style="margin-right: 4px" />
                <span>分辨率: {{ currentSource?.resolution }}</span>
              </div>
              
              <div class="param-item">
                <VideoCameraOutlined style="margin-right: 4px" />
                <span>类型: {{ sourceType === 'stream' ? '视频流' : '视频文件' }}</span>
              </div>
              
              <div class="param-item">
                <span>帧率: {{ currentSource?.fps || '25fps' }}</span>
              </div>
              
              <div class="param-item">
                <span>编码: {{ currentSource?.codec || 'H.264' }}</span>
              </div>
              
              <div class="param-item">
                <span>码率: {{ currentSource?.bitrate || '2Mbps' }}</span>
              </div>
            </a-space>
          </div>
        </div>
      </div>
    </a-modal>
    
    <!-- 添加/编辑弹窗 -->
    <a-modal
      v-model:open="dialogVisible"
      :title="`${isEditing ? '编辑' : '添加'}${sourceType === 'stream' ? '视频流' : '视频文件'}`"
      width="600px"
      :confirm-loading="saving"
      @ok="saveSource"
      @cancel="dialogVisible = false"
    >
      <a-form
        ref="sourceFormRef"
        :model="sourceForm"
        :rules="sourceFormRules"
        :label-col="{ span: 6 }"
        :wrapper-col="{ span: 18 }"
      >
        <a-form-item label="名称" name="name">
          <a-input v-model:value="sourceForm.name" placeholder="请输入视频源名称" />
        </a-form-item>
        
        <a-form-item label="地址" name="url">
          <a-input 
            v-model:value="sourceForm.url" 
            :placeholder="sourceType === 'stream' ? '请输入视频流地址(RTSP/HTTP)' : '请输入视频文件地址'"
          />
        </a-form-item>
        
        <a-form-item label="描述" name="description">
          <a-textarea 
            v-model:value="sourceForm.description" 
            :rows="3"
            placeholder="请输入描述信息"
          />
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted, nextTick, h } from 'vue'
import { message, Modal, Empty } from 'ant-design-vue'
import {
  PlusOutlined,
  ReloadOutlined,
  SearchOutlined,
  VideoCameraOutlined,
  PlayCircleOutlined,
  ClockCircleOutlined,
  DesktopOutlined,
  EyeOutlined,
  EditOutlined,
  DeleteOutlined,
  LinkOutlined,
  CopyOutlined,
  CheckOutlined,
  CheckCircleOutlined,
  CloseCircleOutlined,
  ExclamationCircleOutlined
} from '@ant-design/icons-vue'
import type { FormInstance, Rule } from 'ant-design-vue/es/form'
import type { Component } from 'vue'

// 视频源接口定义
interface VideoSource {
  id: string
  name: string
  url: string
  status: 'online' | 'offline' | 'error' | 'available'
  resolution: string
  fps?: string
  codec?: string
  bitrate?: string
  lastUpdate: string
  thumbnail?: string
  description?: string
}

const props = defineProps<{
  businessUnit?: {
    id: string
    name: string
    isLeaf: boolean
  }
}>()

const emit = defineEmits<{
  refresh: []
}>()

// 状态管理
const loading = ref(false)
const sourceType = ref<'stream' | 'file'>('stream')
const searchText = ref('')

// 对话框状态
const dialogVisible = ref(false)
const previewVisible = ref(false)
const isEditing = ref(false)
const saving = ref(false)

// 引用
const sourceFormRef = ref<FormInstance>()
const videoPlayerRef = ref<HTMLVideoElement>()

// 当前数据
const currentSource = ref<VideoSource | null>(null)
const videoSources = ref<VideoSource[]>([])
const videoPlaying = ref(false)
const copySuccess = ref(false)

// 表单数据
const sourceForm = reactive({
  name: '',
  url: '',
  description: ''
})

// 表单验证规则
const sourceFormRules: Record<string, Rule[]> = {
  name: [
    { required: true, message: '请输入视频源名称', trigger: 'blur' }
  ],
  url: [
    { required: true, message: '请输入视频源地址', trigger: 'blur' }
  ]
}

// Mock数据
const mockStreamSources: VideoSource[] = [
  {
    id: 'stream-1',
    name: '入口摄像头-01',
    url: 'rtsp://192.168.1.100:554/stream1',
    status: 'online',
    resolution: '1920x1080',
    fps: '30fps',
    codec: 'H.264',
    bitrate: '4Mbps',
    lastUpdate: '1分钟前',
    thumbnail: undefined
  },
  {
    id: 'stream-2',
    name: '出口摄像头-01',
    url: 'rtsp://192.168.1.101:554/stream1',
    status: 'online',
    resolution: '1920x1080',
    fps: '25fps',
    codec: 'H.265',
    bitrate: '3.5Mbps',
    lastUpdate: '2分钟前',
    thumbnail: 'https://picsum.photos/320/180?random=1'
  },
  {
    id: 'stream-3',
    name: '内场监控-A区',
    url: 'rtsp://192.168.1.102:554/stream1',
    status: 'offline',
    resolution: '1280x720',
    fps: '25fps',
    codec: 'H.264',
    bitrate: '2Mbps',
    lastUpdate: '10分钟前',
    thumbnail: 'https://picsum.photos/320/180?random=2'
  },
  {
    id: 'stream-4',
    name: '内场监控-B区',
    url: 'rtsp://192.168.1.103:554/stream1',
    status: 'error',
    resolution: '1920x1080',
    fps: '30fps',
    codec: 'H.264',
    bitrate: '4Mbps',
    lastUpdate: '5分钟前',
    thumbnail: 'https://picsum.photos/320/180?random=3'
  }
]

const mockFileSources: VideoSource[] = [
  {
    id: 'file-1',
    name: '测试视频-车辆识别',
    url: '/videos/test-car-detection.mp4',
    status: 'available',
    resolution: '1920x1080',
    fps: '30fps',
    codec: 'H.264',
    bitrate: '5Mbps',
    lastUpdate: '昨天',
    thumbnail: 'https://picsum.photos/320/180?random=4'
  },
  {
    id: 'file-2',
    name: '演示视频-停车场',
    url: '/videos/parking-demo.mp4',
    status: 'available',
    resolution: '1280x720',
    fps: '25fps',
    codec: 'H.264',
    bitrate: '3Mbps',
    lastUpdate: '3天前',
    thumbnail: 'https://picsum.photos/320/180?random=5'
  }
]

// 计算属性
const filteredSources = computed(() => {
  const sources = videoSources.value
  if (!searchText.value) return sources
  
  return sources.filter(source => 
    source.name.toLowerCase().includes(searchText.value.toLowerCase()) ||
    source.url.toLowerCase().includes(searchText.value.toLowerCase())
  )
})

// 方法
const handleTypeChange = () => {
  loadSources()
}

const loadSources = async () => {
  loading.value = true
  try {
    await new Promise(resolve => setTimeout(resolve, 500))
    
    if (sourceType.value === 'stream') {
      videoSources.value = [...mockStreamSources]
    } else {
      videoSources.value = [...mockFileSources]
    }
  } catch (error) {
    message.error('加载视频源失败')
  } finally {
    loading.value = false
  }
}

const getStatusText = (status: string) => {
  const statusMap = {
    online: '在线',
    offline: '离线',
    error: '错误',
    available: '可用'
  }
  return statusMap[status as keyof typeof statusMap] || status
}

const getStatusTagColor = (status: string) => {
  const colorMap = {
    online: 'success',
    offline: 'default',
    error: 'error',
    available: 'processing'
  }
  return colorMap[status as keyof typeof colorMap] || 'default'
}

const getStatusIcon = (status: string): Component => {
  const iconMap: Record<string, Component> = {
    online: CheckCircleOutlined,
    offline: CloseCircleOutlined,
    error: ExclamationCircleOutlined,
    available: CheckCircleOutlined
  }
  return iconMap[status] || CheckCircleOutlined
}

const getStatusIconColor = (status: string) => {
  const colorMap = {
    online: '#52c41a',
    offline: '#d9d9d9',
    error: '#ff4d4f',
    available: '#1890ff'
  }
  return colorMap[status as keyof typeof colorMap] || '#d9d9d9'
}

const copyUrl = async () => {
  if (currentSource.value?.url) {
    try {
      await navigator.clipboard.writeText(currentSource.value.url)
      copySuccess.value = true
      message.success('地址已复制到剪贴板')
      setTimeout(() => {
        copySuccess.value = false
      }, 2000)
    } catch (error) {
      // 备用方案
      try {
        const textArea = document.createElement('textarea')
        textArea.value = currentSource.value.url
        textArea.style.position = 'fixed'
        textArea.style.left = '-999999px'
        textArea.style.top = '-999999px'
        document.body.appendChild(textArea)
        textArea.focus()
        textArea.select()
        document.execCommand('copy')
        document.body.removeChild(textArea)
        copySuccess.value = true
        message.success('地址已复制到剪贴板')
        setTimeout(() => {
          copySuccess.value = false
        }, 2000)
      } catch (fallbackError) {
        message.error('复制失败，请手动复制')
      }
    }
  }
}

const handleImageError = (e: Event) => {
  const target = e.target as HTMLImageElement
  target.style.display = 'none'
  const placeholder = target.parentNode?.querySelector('.placeholder-thumbnail') as HTMLElement
  if (placeholder) {
    placeholder.style.display = 'flex'
  }
}

const previewSource = (source: VideoSource) => {
  currentSource.value = source
  previewVisible.value = true
  videoPlaying.value = false
  
  nextTick(() => {
    if (videoPlayerRef.value) {
      videoPlayerRef.value.addEventListener('playing', () => {
        videoPlaying.value = true
      })
      videoPlayerRef.value.addEventListener('waiting', () => {
        videoPlaying.value = false
      })
      videoPlayerRef.value.addEventListener('loadstart', () => {
        videoPlaying.value = false
      })
    }
  })
}

const handlePreviewClose = () => {
  previewVisible.value = false
  videoPlaying.value = false
  if (videoPlayerRef.value) {
    videoPlayerRef.value.pause()
  }
}

const fetchVideoSources = async () => {
  loading.value = true
  try {
    message.info('正在获取视频源...')
    
    // 模拟从设备或服务器获取视频源
    await new Promise(resolve => setTimeout(resolve, 1500))
    
    // 模拟获取到的新视频源
    const newSources: VideoSource[] = [
      {
        id: `auto-${Date.now()}-1`,
        name: `自动发现-摄像头${Math.floor(Math.random() * 100)}`,
        url: `rtsp://192.168.1.${Math.floor(Math.random() * 200 + 100)}:554/stream1`,
        status: Math.random() > 0.3 ? 'online' : 'offline',
        resolution: Math.random() > 0.5 ? '1920x1080' : '1280x720',
        fps: '25fps',
        codec: 'H.264',
        bitrate: '2Mbps',
        lastUpdate: '刚刚',
        thumbnail: Math.random() > 0.5 ? `https://picsum.photos/320/180?random=${Date.now()}` : undefined
      },
      {
        id: `auto-${Date.now()}-2`,
        name: `自动发现-摄像头${Math.floor(Math.random() * 100)}`,
        url: `rtsp://192.168.1.${Math.floor(Math.random() * 200 + 100)}:554/stream1`,
        status: Math.random() > 0.3 ? 'online' : 'offline',
        resolution: Math.random() > 0.5 ? '1920x1080' : '1280x720',
        fps: '30fps',
        codec: 'H.265',
        bitrate: '3Mbps',
        lastUpdate: '刚刚',
        thumbnail: Math.random() > 0.5 ? `https://picsum.photos/320/180?random=${Date.now() + 1}` : undefined
      }
    ]
    
    // 添加到现有列表
    videoSources.value.unshift(...newSources)
    message.success(`成功获取 ${newSources.length} 个视频源`)
    emit('refresh')
  } catch (error) {
    message.error('获取视频源失败')
  } finally {
    loading.value = false
  }
}

const showAddDialog = () => {
  isEditing.value = false
  Object.assign(sourceForm, {
    name: '',
    url: '',
    description: ''
  })
  dialogVisible.value = true
}

const editSource = (source: VideoSource) => {
  isEditing.value = true
  Object.assign(sourceForm, {
    name: source.name,
    url: source.url,
    description: source.description || ''
  })
  currentSource.value = source
  dialogVisible.value = true
}

const saveSource = async () => {
  if (!sourceFormRef.value) return
  
  try {
    await sourceFormRef.value.validate()
    saving.value = true
    
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    if (isEditing.value && currentSource.value) {
      const index = videoSources.value.findIndex(s => s.id === currentSource.value!.id)
      if (index !== -1) {
        videoSources.value[index] = {
          ...videoSources.value[index],
          ...sourceForm
        }
      }
      message.success('视频源更新成功')
    } else {
      const newSource: VideoSource = {
        id: `${sourceType.value}-${Date.now()}`,
        ...sourceForm,
        status: sourceType.value === 'stream' ? 'offline' : 'available',
        resolution: '1920x1080',
        lastUpdate: '刚刚',
        thumbnail: undefined
      }
      videoSources.value.unshift(newSource)
      message.success('视频源添加成功')
    }
    
    dialogVisible.value = false
    emit('refresh')
  } catch (error: any) {
    if (error.errorFields) {
      return
    }
    message.error('保存失败')
  } finally {
    saving.value = false
  }
}

const viewDetails = (source: VideoSource) => {
  message.info(`查看详情: ${source.name}`)
}

const deleteSource = (source: VideoSource) => {
  Modal.confirm({
    title: '删除确认',
    content: `确定要删除视频源 "${source.name}" 吗？`,
    okText: '确定',
    cancelText: '取消',
    okType: 'danger',
    onOk: () => {
      const index = videoSources.value.findIndex(s => s.id === source.id)
      if (index !== -1) {
        videoSources.value.splice(index, 1)
        message.success('删除成功')
        emit('refresh')
      }
    }
  })
}

const refreshSources = () => {
  message.info('刷新视频源列表')
  loadSources()
}

// 生命周期
onMounted(() => {
  loadSources()
})
</script>

<style lang="less" scoped>
// 导入全局CSS变量
@import '@/styles/variables.less';

.video-sources-panel {
  height: 100%;
  display: flex;
  flex-direction: column;
  background: var(--bg-primary);
}

// 面板头部
.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 0;
  border-bottom: 1px solid var(--border-light);
  margin-bottom: 20px;
}

.type-selector {
  display: flex;
  align-items: center;
}

.header-actions {
  display: flex;
  align-items: center;
}

// 视频源网格 - 每行5个卡片
.sources-grid {
  flex: 1;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 20px;
  overflow-y: auto;
  padding: 0 4px;
  
  // 响应式调整
  @media (max-width: 1600px) {
    grid-template-columns: repeat(4, 1fr);
  }
  
  @media (max-width: 1200px) {
    grid-template-columns: repeat(3, 1fr);
  }
  
  @media (max-width: 900px) {
    grid-template-columns: repeat(2, 1fr);
  }
  
  @media (max-width: 600px) {
    grid-template-columns: 1fr;
  }
}

// 视频源卡片
.source-card {
  position: relative;
  cursor: pointer;
  border-radius: 12px !important;
  border: 1px solid var(--border-base) !important;
  box-shadow: var(--shadow-light);
  transition: all 0.3s ease;
  
  &:hover {
    border-color: var(--color-primary) !important;
    box-shadow: var(--shadow-base);
    transform: translateY(-2px);
  }
  
  :deep(.ant-card) {
    border-radius: 12px !important;
    overflow: hidden;
  }
  
  :deep(.ant-card-body) {
    padding: 0;
    border-radius: 12px;
    overflow: hidden;
  }
}

.source-thumbnail {
  position: relative;
  width: 100%;
  height: 140px; // 减小高度，更接近正方形
  background: var(--bg-secondary);
  overflow: hidden;
  border-top-left-radius: 12px;
  border-top-right-radius: 12px;
  
  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
}

.placeholder-thumbnail {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: var(--text-placeholder);
  font-size: 14px;
  gap: 8px;
}

// 状态指示器
.status-indicator {
  position: absolute;
  top: 8px;
  left: 8px;
}

// 播放覆盖层
.play-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 60px;
  height: 60px;
  background: rgba(0, 0, 0, 0.6);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  opacity: 0;
  transition: opacity 0.3s;
}

.source-card:hover .play-overlay {
  opacity: 1;
}

// 卡片信息
.source-info {
  padding: 16px;
}

.source-name {
  margin: 0 0 8px 0 !important;
}

.source-url {
  display: block;
  margin-bottom: 12px;
  font-size: 12px;
}

.source-meta {
  .meta-item {
    display: flex;
    align-items: center;
    font-size: 12px;
    color: var(--text-secondary);
  }
}

// 卡片操作按钮
:deep(.ant-card-actions) {
  background: var(--bg-primary);
  border-top: 1px solid var(--border-light);
  border-bottom-left-radius: 12px;
  border-bottom-right-radius: 12px;
  
  & > li {
    margin: 8px 0;
    
    .action-btn {
      font-size: 16px;
      transition: all 0.2s ease;
      
      &.view-btn {
        color: var(--color-info);
        
        &:hover {
          color: var(--color-primary);
          transform: scale(1.2);
        }
      }
      
      &.edit-btn {
        color: var(--color-success);
        
        &:hover {
          color: #389e0d;
          transform: scale(1.2);
        }
      }
      
      &.delete-btn {
        color: var(--color-error);
        
        &:hover {
          color: #cf1322;
          transform: scale(1.2);
        }
      }
    }
    
    // 确保悬停时有适当的背景色
    &:hover {
      background-color: var(--bg-hover);
    }
  }
}

// 空状态
.empty-state {
  grid-column: 1 / -1;
  padding: 60px 20px;
}

// 视频预览内容
.video-preview-content {
  display: flex;
  flex-direction: column;
}

.video-player-wrapper {
  position: relative;
  background: #000;
  margin-bottom: 16px;
}

.video-player {
  width: 100%;
  height: 450px;
  background: #000;
  display: block;
}

.video-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
}

// 视频信息面板
.video-info-panel {
  background: var(--bg-tertiary);
  border: 1px solid var(--border-light);
  border-radius: 6px;
  padding: 16px;
}

.url-section {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--border-light);
}

.url-icon {
  color: var(--color-success);
  flex-shrink: 0;
}

.url-text {
  flex: 1;
  font-size: 12px;
}

.copy-btn {
  flex-shrink: 0;
}

.params-section {
  .param-item {
    display: flex;
    align-items: center;
    font-size: 14px;
    color: var(--text-secondary);
  }
}

// 响应式设计
@media (max-width: 768px) {
  .panel-header {
    flex-direction: column;
    align-items: stretch;
    gap: 16px;
  }
  
  .header-actions {
    justify-content: space-between;
    
    .ant-input {
      width: 200px !important;
    }
  }
  
  .video-player {
    height: 280px !important;
  }
}
</style>