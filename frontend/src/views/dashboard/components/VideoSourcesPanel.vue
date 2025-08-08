<template>
  <div class="video-sources-panel">
    <!-- 视频源类型切换和操作栏 -->
    <div class="panel-header">
      <div class="type-selector">
        <el-radio-group v-model="sourceType" @change="handleTypeChange">
          <el-radio-button label="stream">视频流</el-radio-button>
          <el-radio-button label="file">视频文件</el-radio-button>
        </el-radio-group>
      </div>
      
      <div class="header-actions">
        <el-input
          v-model="searchText"
          placeholder="搜索视频源..."
          prefix-icon="Search"
          clearable
          style="width: 240px; margin-right: 16px"
        />
        
        <el-button type="primary" @click="showAddDialog">
          <el-icon><Plus /></el-icon>
          添加{{ sourceType === 'stream' ? '视频流' : '视频文件' }}
        </el-button>
        
        <el-button @click="refreshSources">
          <el-icon><Refresh /></el-icon>
        </el-button>
      </div>
    </div>
    
    <!-- 视频源卡片网格 -->
    <div class="sources-grid" v-loading="loading">
      <div
        v-for="source in filteredSources"
        :key="source.id"
        class="source-card"
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
            <el-icon size="40"><VideoCamera /></el-icon>
            <span>暂无预览</span>
          </div>
          
          <!-- 状态指示器 -->
          <div class="status-indicator" :class="source.status">
            <span class="status-dot"></span>
            <span class="status-text">{{ getStatusText(source.status) }}</span>
          </div>
          
          <!-- 播放按钮覆盖层 -->
          <div class="play-overlay">
            <el-icon size="30"><VideoPlay /></el-icon>
          </div>
        </div>
        
        <!-- 卡片信息 -->
        <div class="source-info">
          <h4 class="source-name" :title="source.name">{{ source.name }}</h4>
          <p class="source-url" :title="source.url">{{ source.url }}</p>
          
          <div class="source-meta">
            <span class="meta-item">
              <el-icon><Clock /></el-icon>
              {{ source.lastUpdate }}
            </span>
            <span class="meta-item" v-if="sourceType === 'stream'">
              <el-icon><Monitor /></el-icon>
              {{ source.resolution }}
            </span>
          </div>
        </div>
        
        <!-- 操作按钮 -->
        <div class="source-actions">
          <el-button size="small" @click.stop="viewDetails(source)">
            <el-icon><View /></el-icon>
          </el-button>
          <el-button size="small" @click.stop="editSource(source)">
            <el-icon><Edit /></el-icon>
          </el-button>
          <el-button 
            size="small" 
            @click.stop="deleteSource(source)"
            class="delete-btn"
          >
            <el-icon style="color: #ef4444"><Delete /></el-icon>
          </el-button>
        </div>
      </div>
      
      <!-- 空状态 -->
      <div v-if="filteredSources.length === 0 && !loading" class="empty-state">
        <el-icon size="80"><VideoCamera /></el-icon>
        <h3>暂无{{ sourceType === 'stream' ? '视频流' : '视频文件' }}</h3>
        <p>点击上方按钮添加新的{{ sourceType === 'stream' ? '视频流' : '视频文件' }}</p>
      </div>
    </div>
    
    <!-- 视频预览弹窗 -->
    <BaseDialog
      :visible="previewVisible"
      :title="currentSource?.name || '视频预览'"
      subtitle="点击播放按钮开始播放视频"
      width="1000px"
      size="large"
      type="default"
      icon="VideoCamera"
      :show-maximize="true"
      :before-close="handlePreviewClose"
      :modal="true"
      :modal-class="'video-modal-overlay'"
      :append-to-body="true"
      :destroy-on-close="true"
      :draggable="true"
:body-style="{ padding: 0, maxHeight: '80vh', overflow: 'hidden' }"
      @update:visible="previewVisible = $event"
      @maximize="toggleFullscreen"
    >
      
      <!-- 视频内容区域 -->
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
            <div class="loading-animation">
              <div class="loading-circle"></div>
              <span>加载中...</span>
            </div>
          </div>
        </div>
        
        <!-- 视频信息面板 -->
        <div class="video-info-panel" :class="{ 'light-theme': !isDarkTheme }">
          <!-- URL 地址行 -->
          <div class="url-section">
            <el-icon class="url-icon"><Link /></el-icon>
            <code class="url-text" :title="currentSource?.url">{{ currentSource?.url }}</code>
            <div class="copy-btn-wrapper">
              <el-button 
                size="small" 
                type="text" 
                class="copy-btn"
                :class="{ 'copy-success': copySuccess }"
                @click="copyUrl"
                :title="copySuccess ? '已复制!' : '复制地址'"
              >
                <el-icon v-if="!copySuccess"><DocumentCopy /></el-icon>
                <el-icon v-else class="success-icon"><Check /></el-icon>
              </el-button>
              <span v-if="copySuccess" class="copy-text">已复制</span>
            </div>
          </div>
          
          <!-- 参数信息行 -->
          <div class="params-section">
            <div class="param-item">
              <el-icon class="param-icon status-icon" :class="'status-' + currentSource?.status">
                <component :is="getStatusIcon(currentSource?.status)" />
              </el-icon>
              <span class="param-text">
                <span class="param-label">状态</span>
                <span class="param-value" :class="'status-' + currentSource?.status">
                  {{ getStatusText(currentSource?.status) }}
                </span>
              </span>
            </div>
            
            <div class="param-divider"></div>
            
            <div class="param-item">
              <el-icon class="param-icon"><Monitor /></el-icon>
              <span class="param-text">
                <span class="param-label">分辨率</span>
                <span class="param-value">{{ currentSource?.resolution }}</span>
              </span>
            </div>
            
            <div class="param-divider"></div>
            
            <div class="param-item">
              <el-icon class="param-icon"><VideoCamera /></el-icon>
              <span class="param-text">
                <span class="param-label">类型</span>
                <span class="param-value">{{ sourceType === 'stream' ? '视频流' : '视频文件' }}</span>
              </span>
            </div>
            
            <div class="param-divider"></div>
            
            <div class="param-item">
              <el-icon class="param-icon"><Timer /></el-icon>
              <span class="param-text">
                <span class="param-label">帧率</span>
                <span class="param-value">{{ currentSource?.fps || '25fps' }}</span>
              </span>
            </div>
            
            <div class="param-divider"></div>
            
            <div class="param-item">
              <el-icon class="param-icon"><Setting /></el-icon>
              <span class="param-text">
                <span class="param-label">编码</span>
                <span class="param-value">{{ currentSource?.codec || 'H.264' }}</span>
              </span>
            </div>
            
            <div class="param-divider"></div>
            
            <div class="param-item">
              <el-icon class="param-icon"><DataAnalysis /></el-icon>
              <span class="param-text">
                <span class="param-label">码率</span>
                <span class="param-value">{{ currentSource?.bitrate || '2Mbps' }}</span>
              </span>
            </div>
          </div>
        </div>
      </div>
    </BaseDialog>
    
    <!-- 添加/编辑弹窗 -->
    <BaseDialog
      :visible="dialogVisible"
      :title="`${isEditing ? '编辑' : '添加'}${sourceType === 'stream' ? '视频流' : '视频文件'}`"
      subtitle="填写视频源的基本信息"
      width="600px"
      size="medium"
      type="default"
      icon="Edit"
      :draggable="true"
      @update:visible="dialogVisible = $event"
    >
      
      <el-form
        ref="sourceFormRef"
        :model="sourceForm"
        :rules="sourceFormRules"
        label-width="100px"
        style="padding: 20px;"
      >
        <el-form-item label="名称" prop="name">
          <el-input v-model="sourceForm.name" placeholder="请输入视频源名称" />
        </el-form-item>
        
        <el-form-item label="地址" prop="url">
          <el-input 
            v-model="sourceForm.url" 
            :placeholder="sourceType === 'stream' ? '请输入视频流地址(RTSP/HTTP)' : '请输入视频文件地址'"
          />
        </el-form-item>
        
        <el-form-item label="描述" prop="description">
          <el-input 
            v-model="sourceForm.description" 
            type="textarea"
            :rows="3"
            placeholder="请输入描述信息"
          />
        </el-form-item>
      </el-form>
      
      <template #footer>
        <div style="padding: 0 20px 20px;">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" :loading="saving" @click="saveSource">
            {{ isEditing ? '更新' : '添加' }}
          </el-button>
        </div>
      </template>
    </BaseDialog>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted, nextTick } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import BaseDialog from '@/components/ui/BaseDialog.vue'
import {
  Plus,
  Refresh,
  Search,
  VideoCamera,
  VideoPlay,
  Clock,
  Monitor,
  View,
  Edit,
  Delete,
  FullScreen,
  Close,
  InfoFilled,
  Link,
  DocumentCopy,
  CircleCheck,
  CircleClose,
  Warning,
  Timer,
  Setting,
  DataAnalysis,
  Check
} from '@element-plus/icons-vue'

const props = defineProps({
  businessUnit: {
    type: Object,
    required: true
  },
  isDarkTheme: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['refresh'])

// 状态管理
const loading = ref(false)
const sourceType = ref('stream') // stream | file
const searchText = ref('')

// 对话框状态
const dialogVisible = ref(false)
const previewVisible = ref(false)
const isEditing = ref(false)
const saving = ref(false)

// 引用
const sourceFormRef = ref()
const videoPlayerRef = ref()

// 当前数据
const currentSource = ref(null)
const videoSources = ref([])
const videoPlaying = ref(false)
const copySuccess = ref(false)

// 表单数据
const sourceForm = reactive({
  name: '',
  url: '',
  description: ''
})

// 表单验证规则
const sourceFormRules = {
  name: [
    { required: true, message: '请输入视频源名称', trigger: 'blur' }
  ],
  url: [
    { required: true, message: '请输入视频源地址', trigger: 'blur' }
  ]
}

// Mock数据
const mockStreamSources = [
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
    thumbnail: null
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

const mockFileSources = [
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
const handleTypeChange = (type) => {
  loadSources()
}

const loadSources = async () => {
  loading.value = true
  try {
    // 模拟API调用
    await new Promise(resolve => setTimeout(resolve, 500))
    
    if (sourceType.value === 'stream') {
      videoSources.value = [...mockStreamSources]
    } else {
      videoSources.value = [...mockFileSources]
    }
  } catch (error) {
    ElMessage.error('加载视频源失败')
  } finally {
    loading.value = false
  }
}

const getStatusText = (status) => {
  const statusMap = {
    online: '在线',
    offline: '离线',
    error: '错误',
    available: '可用'
  }
  return statusMap[status] || status
}

const getStatusIcon = (status) => {
  const iconMap = {
    online: CircleCheck,
    offline: CircleClose,
    error: Warning,
    available: CircleCheck
  }
  return iconMap[status] || CircleCheck
}

const copyUrl = async () => {
  if (currentSource.value?.url) {
    try {
      await navigator.clipboard.writeText(currentSource.value.url)
      // 显示复制成功的提示
      copySuccess.value = true
      setTimeout(() => {
        copySuccess.value = false
      }, 2000)
    } catch (error) {
      console.error('Copy failed:', error)
      // 备用方案：使用旧的API
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
        setTimeout(() => {
          copySuccess.value = false
        }, 2000)
      } catch (fallbackError) {
        console.error('Fallback copy failed:', fallbackError)
        ElMessage.error('复制失败，请手动复制')
      }
    }
  }
}

const handleImageError = (e) => {
  // 图片加载失败时的处理
  e.target.style.display = 'none'
  e.target.parentNode.querySelector('.placeholder-thumbnail').style.display = 'flex'
}

const previewSource = (source) => {
  currentSource.value = source
  previewVisible.value = true
  videoPlaying.value = false
  
  // 监听视频播放事件
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
  // 停止视频播放
  if (videoPlayerRef.value) {
    videoPlayerRef.value.pause()
  }
}

const toggleFullscreen = () => {
  if (videoPlayerRef.value) {
    if (videoPlayerRef.value.requestFullscreen) {
      videoPlayerRef.value.requestFullscreen()
    }
  }
}

const handleDragStart = (e) => {
  // 拖拽功能由Element Plus dialog内置处理
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

const editSource = (source) => {
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
    
    // 模拟API调用
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    if (isEditing.value) {
      // 更新现有源
      const index = videoSources.value.findIndex(s => s.id === currentSource.value.id)
      if (index !== -1) {
        videoSources.value[index] = {
          ...videoSources.value[index],
          ...sourceForm
        }
      }
      ElMessage.success('视频源更新成功')
    } else {
      // 添加新源
      const newSource = {
        id: `${sourceType.value}-${Date.now()}`,
        ...sourceForm,
        status: sourceType.value === 'stream' ? 'offline' : 'available',
        resolution: '1920x1080',
        lastUpdate: '刚刚',
        thumbnail: null
      }
      videoSources.value.unshift(newSource)
      ElMessage.success('视频源添加成功')
    }
    
    dialogVisible.value = false
    emit('refresh')
  } catch (error) {
    console.error('保存失败:', error)
  } finally {
    saving.value = false
  }
}

const viewDetails = (source) => {
  ElMessage.info(`查看详情: ${source.name}`)
  // 这里可以打开详情页面或抽屉
}

const deleteSource = (source) => {
  ElMessageBox.confirm(
    `确定要删除视频源 "${source.name}" 吗？`,
    '删除确认',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    }
  ).then(() => {
    const index = videoSources.value.findIndex(s => s.id === source.id)
    if (index !== -1) {
      videoSources.value.splice(index, 1)
      ElMessage.success('删除成功')
      emit('refresh')
    }
  }).catch(() => {
    // 取消删除
  })
}

const refreshSources = () => {
  ElMessage.info('刷新视频源列表')
  loadSources()
}

// 生命周期
onMounted(() => {
  loadSources()
})
</script>

<style scoped>
.video-sources-panel {
  height: 100%;
  display: flex;
  flex-direction: column;
}

/* 面板头部 */
.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 0;
  border-bottom: 1px solid #e4e7ed;
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

/* 视频源网格 */
.sources-grid {
  flex: 1;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 20px;
  overflow-y: auto;
  padding: 0 4px;
}

/* 视频源卡片 */
.source-card {
  background: #ffffff;
  border: 1px solid #e4e7ed;
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.3s;
  cursor: pointer;
  position: relative;
}

.source-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

.source-thumbnail {
  position: relative;
  width: 100%;
  height: 180px;
  background: #f5f7fa;
  overflow: hidden;
}

.source-thumbnail img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.placeholder-thumbnail {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #c0c4cc;
  font-size: 14px;
  gap: 8px;
}

/* 状态指示器 */
.status-indicator {
  position: absolute;
  top: 8px;
  left: 8px;
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 4px 8px;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  border-radius: 12px;
  font-size: 12px;
}

.status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
}

.status-indicator.online .status-dot {
  background: #67c23a;
}

.status-indicator.offline .status-dot {
  background: #909399;
}

.status-indicator.error .status-dot {
  background: #f56c6c;
}

.status-indicator.available .status-dot {
  background: #409eff;
}

/* 播放覆盖层 */
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

/* 卡片信息 */
.source-info {
  padding: 16px;
}

.source-name {
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
  margin: 0 0 8px 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.source-url {
  font-size: 12px;
  color: #909399;
  margin: 0 0 12px 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.source-meta {
  display: flex;
  gap: 16px;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  color: #666;
}

/* 操作按钮 */
.source-actions {
  position: absolute;
  top: 8px;
  right: 8px;
  display: flex;
  gap: 4px;
  opacity: 0;
  transition: opacity 0.3s;
}

.source-card:hover .source-actions {
  opacity: 1;
}

.source-actions .el-button {
  background: rgba(255, 255, 255, 0.9);
  border: none;
  width: 28px;
  height: 28px;
  padding: 0;
}

.source-actions .el-button:first-child {
  color: #3b82f6;
}

.source-actions .el-button:nth-child(2) {
  color: #10b981;
}

.delete-btn {
  color: #ef4444 !important;
}

/* 空状态 */
.empty-state {
  grid-column: 1 / -1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  color: #c0c4cc;
  text-align: center;
}

.empty-state h3 {
  margin: 16px 0 8px 0;
  color: #909399;
}

.empty-state p {
  margin: 0;
  color: #c0c4cc;
}


:deep(.video-modal-overlay) {
  backdrop-filter: blur(8px);
  background: rgba(0, 0, 0, 0.7);
}


/* 视频预览内容 */
.video-preview-content {
  display: flex;
  flex-direction: column;
  background: #000;
  overflow: hidden;
}

.video-player-wrapper {
  position: relative;
  background: #000;
  flex-shrink: 0;
}

.video-player {
  width: 100%;
  height: 450px;
  background: #000;
  display: block;
}

@media (min-width: 1200px) {
  .video-player {
    height: 500px;
  }
}

@media (max-height: 800px) {
  .video-player {
    height: 400px;
  }
}

@media (max-height: 700px) {
  .video-player {
    height: 350px;
  }
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

.loading-animation {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  color: #f3f4f6;
}

.loading-circle {
  width: 40px;
  height: 40px;
  border: 3px solid #374151;
  border-top: 3px solid #3b82f6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* 视频信息面板 - 紧凑横向布局 */
.video-info-panel {
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
  border-top: 1px solid #475569;
  flex-shrink: 0;
  position: relative;
  max-height: 80px;
  overflow: hidden;
}

/* 亮色主题 */
.video-info-panel.light-theme {
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  border-top: 1px solid #cbd5e1;
}

/* URL 区域 - 第一行 */
.url-section {
  display: flex;
  align-items: center;
  gap: var(--spacing-2);
  padding: var(--spacing-2) var(--spacing-5);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  height: 36px;
  justify-content: center;
  max-width: 100%;
}

.video-info-panel.light-theme .url-section {
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

.url-icon {
  font-size: 14px;
  color: #34d399;
  flex-shrink: 0;
}

.url-text {
  flex: 1;
  font-family: 'Courier New', monospace;
  font-size: var(--font-size-xs);
  color: #e2e8f0;
  line-height: 1.2;
  max-height: 20px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  text-align: center;
  padding: 0 var(--spacing-2);
}

.video-info-panel.light-theme .url-text {
  color: #1e293b;
}

.copy-btn {
  color: #60a5fa;
  min-width: 32px;
  height: 28px;
  border-radius: var(--border-radius-md);
  transition: all 0.2s ease;
  flex-shrink: 0;
  background: rgba(96, 165, 250, 0.1);
  border: 1px solid rgba(96, 165, 250, 0.2);
}

.copy-btn:hover {
  background: rgba(96, 165, 250, 0.2);
  color: #93c5fd;
  transform: scale(1.05);
}

.video-info-panel.light-theme .copy-btn {
  background: rgba(59, 130, 246, 0.1);
  border: 1px solid rgba(59, 130, 246, 0.2);
  color: #3b82f6;
}

.video-info-panel.light-theme .copy-btn:hover {
  background: rgba(59, 130, 246, 0.2);
  color: #2563eb;
}

/* 复制成功状态 */
.copy-btn.copy-success {
  background: rgba(16, 185, 129, 0.2) !important;
  border: 1px solid rgba(16, 185, 129, 0.3) !important;
  color: #10b981 !important;
}

.success-icon {
  color: #10b981 !important;
}

/* 复制按钮包装器 */
.copy-btn-wrapper {
  display: flex;
  align-items: center;
  gap: var(--spacing-2);
  flex-shrink: 0;
}

.copy-text {
  font-size: var(--font-size-xs);
  color: #10b981;
  font-weight: var(--font-weight-medium);
  white-space: nowrap;
  animation: fadeInScale 0.3s ease-out;
}

@keyframes fadeInScale {
  from {
    opacity: 0;
    transform: scale(0.8);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* 复制提示样式 - 放在右侧 */
.copy-tooltip {
  position: absolute;
  top: 50%;
  left: calc(100% + 8px);
  transform: translateY(-50%);
  background: #10b981;
  color: white;
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 500;
  white-space: nowrap;
  z-index: 9999;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  animation: slideInRight 0.3s ease-out;
}

.copy-tooltip::before {
  content: '';
  position: absolute;
  top: 50%;
  left: -4px;
  transform: translateY(-50%);
  width: 0;
  height: 0;
  border-top: 4px solid transparent;
  border-bottom: 4px solid transparent;
  border-right: 4px solid #10b981;
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateY(-50%) translateX(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(-50%) translateX(0);
  }
}

/* 如果右侧空间不够，就放在下方 */
@media (max-width: 640px) {
  .copy-tooltip {
    top: calc(100% + 8px);
    left: 50%;
    transform: translateX(-50%);
    animation: slideInDown 0.3s ease-out;
  }
  
  .copy-tooltip::before {
    top: -4px;
    left: 50%;
    transform: translateX(-50%);
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-bottom: 4px solid #10b981;
    border-top: none;
  }
}

@keyframes slideInDown {
  from {
    opacity: 0;
    transform: translateX(-50%) translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
  }
}

/* 参数区域 - 第二行 */
.params-section {
  display: flex;
  align-items: center;
  padding: 0 var(--spacing-5);
  height: 44px;
  gap: var(--spacing-4);
  overflow-x: auto;
  scrollbar-width: none;
  -ms-overflow-style: none;
  justify-content: center;
  flex-wrap: nowrap;
}

.params-section::-webkit-scrollbar {
  display: none;
}

.param-item {
  display: flex;
  align-items: center;
  gap: var(--spacing-2);
  flex-shrink: 0;
}

.param-icon {
  font-size: 16px;
  color: #64748b;
  flex-shrink: 0;
}

.param-icon.status-icon.status-online {
  color: #10b981;
}

.param-icon.status-icon.status-offline {
  color: #6b7280;
}

.param-icon.status-icon.status-error {
  color: #ef4444;
}

.param-icon.status-icon.status-available {
  color: #3b82f6;
}

.param-text {
  display: flex;
  flex-direction: column;
  gap: 1px;
}

.param-label {
  font-size: 10px;
  color: #94a3b8;
  font-weight: var(--font-weight-medium);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  line-height: 1;
}

.video-info-panel.light-theme .param-label {
  color: #64748b;
}

.param-value {
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-semibold);
  color: #f1f5f9;
  line-height: 1;
  white-space: nowrap;
}

.video-info-panel.light-theme .param-value {
  color: #1e293b;
}

/* 状态颜色 */
.param-value.status-online {
  color: #10b981;
}

.param-value.status-offline {
  color: #9ca3af;
}

.param-value.status-error {
  color: #f87171;
}

.param-value.status-available {
  color: #60a5fa;
}

/* 分割线 */
.param-divider {
  width: 1px;
  height: 24px;
  background: rgba(255, 255, 255, 0.2);
  flex-shrink: 0;
}

.video-info-panel.light-theme .param-divider {
  background: rgba(0, 0, 0, 0.2);
}

.info-item-url {
  display: flex;
  align-items: flex-start;
  gap: var(--spacing-3);
  width: 100%;
}

.info-value-url {
  flex: 1;
  word-break: break-all;
  font-family: 'Courier New', monospace;
  font-size: var(--font-size-sm);
  line-height: 1.4;
  color: #f3f4f6;
}

.video-info-panel.light-theme .info-value-url {
  color: #374151;
}

.info-item-row {
  display: flex;
  gap: var(--spacing-6);
  flex-wrap: wrap;
  justify-content: flex-start;
}

.info-item {
  display: flex;
  align-items: center;
  gap: var(--spacing-3);
  min-width: 0;
  flex-shrink: 0;
}

.info-label {
  color: #9ca3af;
  font-weight: 500;
  min-width: 48px;
  font-size: var(--font-size-sm);
  flex-shrink: 0;
}

.video-info-panel.light-theme .info-label {
  color: #6b7280;
}

.info-value {
  color: #f3f4f6;
  white-space: nowrap;
  font-size: var(--font-size-sm);
}

.video-info-panel.light-theme .info-value {
  color: #374151;
}

.info-value.status-online {
  color: #67c23a;
}

.info-value.status-offline {
  color: #909399;
}

.info-value.status-error {
  color: #f56c6c;
}

.info-value.status-available {
  color: #409eff;
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .params-section {
    gap: var(--spacing-3);
  }
}

@media (max-width: 768px) {
  .url-section {
    padding: var(--spacing-2) var(--spacing-4);
  }
  
  .params-section {
    padding: 0 var(--spacing-4);
    gap: var(--spacing-2);
    justify-content: space-between;
  }
  
  .param-text {
    min-width: 0;
  }
  
  .param-value {
    font-size: var(--font-size-xs);
  }
  
  .param-divider {
    display: none;
  }
}

@media (max-width: 640px) {
  .params-section {
    overflow-x: auto;
    justify-content: flex-start;
    gap: var(--spacing-3);
  }
  
  .param-divider {
    display: block;
    height: 20px;
  }
}

@media (max-width: 480px) {
  .url-section,
  .params-section {
    padding-left: var(--spacing-3);
    padding-right: var(--spacing-3);
  }
  
  .url-text {
    font-size: 10px;
  }
  
  .param-label {
    font-size: 8px;
  }
  
  .param-value {
    font-size: 11px;
  }
  
  .param-icon {
    font-size: 14px;
  }
}

/* 响应式设计 */
@media (max-width: 1440px) {
  .video-player {
    height: 420px !important;
  }
}

@media (max-width: 1200px) {
  .video-player {
    height: 380px !important;
  }
}

@media (max-width: 1024px) {
  .video-player {
    height: 320px !important;
  }
}

@media (max-width: 768px) {
  .sources-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  
  .panel-header {
    flex-direction: column;
    align-items: stretch;
    gap: 16px;
  }
  
  .header-actions {
    justify-content: space-between;
  }
  
  .header-actions .el-input {
    width: 200px !important;
  }
  
  .video-player {
    height: 280px !important;
  }
}

@media (max-height: 900px) {
  .video-player {
    height: 380px !important;
  }
}

@media (max-height: 800px) {
  .video-player {
    height: 320px !important;
  }
}

@media (max-height: 700px) {
  .video-player {
    height: 280px !important;
  }
}

@media (max-height: 600px) {
  .video-player {
    height: 240px !important;
  }
}

/* 复制消息样式 */
:deep(.copy-message) {
  z-index: 9999 !important;
  position: fixed !important;
  top: 80px !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  min-width: 200px !important;
  text-align: center !important;
}

/* 确保消息在弹窗之上 */
:deep(.el-message) {
  z-index: 9999 !important;
}

/* 针对弹窗内的消息 */
.base-dialog :deep(.copy-message) {
  z-index: 9999 !important;
  position: fixed !important;
}
</style>