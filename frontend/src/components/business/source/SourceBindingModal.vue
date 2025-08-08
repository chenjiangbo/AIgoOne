<template>
  <BaseDialog
    v-model:visible="dialogVisible"
    title="绑定视频源"
    :subtitle="`为节点 '${node?.name}' 绑定视频源`"
    width="800px"
    :show-default-footer="false"
  >
    <div class="binding-modal-content">
      <!-- 第一步：选择设备 -->
      <div class="step-section mb-6">
        <h4 class="step-title flex items-center mb-4">
          <el-icon class="mr-2"><Monitor /></el-icon>
          步骤 1：选择设备
        </h4>
        <el-select
          v-model="selectedDeviceId"
          placeholder="请选择设备"
          filterable
          clearable
          @change="handleDeviceChange"
          class="w-full"
        >
          <el-option
            v-for="device in deviceList"
            :key="device.id"
            :label="`${device.name} (${device.url})`"
            :value="device.id"
            :disabled="device.status !== 'online'"
          >
            <div class="flex items-center justify-between w-full">
              <span>{{ device.name }}</span>
              <el-tag 
                :type="device.status === 'online' ? 'success' : 'danger'"
                size="small"
              >
                {{ device.status === 'online' ? '在线' : '离线' }}
              </el-tag>
            </div>
          </el-option>
        </el-select>
      </div>
      
      <!-- 第二步：选择视频源 -->
      <div v-if="selectedDeviceId" class="step-section">
        <h4 class="step-title flex items-center mb-4">
          <el-icon class="mr-2"><VideoCamera /></el-icon>
          步骤 2：选择视频源
        </h4>
        
        <!-- 视频源类型筛选 -->
        <div class="source-filters mb-4">
          <el-radio-group v-model="sourceTypeFilter" @change="loadDeviceSources">
            <el-radio-button label="">全部</el-radio-button>
            <el-radio-button label="camera">摄像头</el-radio-button>
            <el-radio-button label="video">视频文件</el-radio-button>
          </el-radio-group>
          
          <el-input
            v-model="sourceSearchText"
            placeholder="搜索视频源..."
            :prefix-icon="Search"
            clearable
            class="ml-4"
            style="width: 200px"
          />
        </div>
        
        <!-- 加载状态 -->
        <div v-if="loadingSources" class="text-center py-8">
          <el-icon class="animate-spin text-2xl text-gray-400 mb-2">
            <Loading />
          </el-icon>
          <p class="text-gray-500">正在获取视频源...</p>
        </div>
        
        <!-- 视频源列表 -->
        <div v-else-if="filteredSources.length > 0" class="sources-selection">
          <div class="selection-toolbar flex items-center justify-between mb-4">
            <el-checkbox 
              v-model="selectAllSources" 
              :indeterminate="isSourceIndeterminate"
              @change="handleSelectAllSources"
            >
              全选 ({{ filteredSources.length }} 个)
            </el-checkbox>
            <span class="text-sm text-gray-500">
              已选择: {{ selectedSources.length }} 个
            </span>
          </div>
          
          <div class="sources-grid grid grid-cols-1 gap-2 max-h-60 overflow-y-auto">
            <div
              v-for="source in filteredSources"
              :key="source.id"
              :class="[
                'source-item flex items-center p-3 border rounded-lg cursor-pointer transition-colors',
                selectedSources.includes(source) ? 'border-primary-500 bg-primary-50' : 'border-gray-200 hover:bg-gray-50',
                source.isAlreadyBound ? 'opacity-60' : ''
              ]"
              @click="toggleSourceSelection(source)"
            >
              <el-checkbox 
                :model-value="selectedSources.includes(source)"
                @change="toggleSourceSelection(source)"
                class="mr-3"
              />
              
              <el-icon 
                :class="[
                  'mr-2',
                  source.type === 'camera' ? 'text-blue-600' : 'text-green-600'
                ]"
              >
                <VideoCamera v-if="source.type === 'camera'" />
                <Film v-else />
              </el-icon>
              
              <div class="flex-1">
                <div class="font-medium">{{ source.name || source.id }}</div>
                <div class="text-sm text-gray-500">
                  {{ source.type === 'camera' ? '摄像头' : '视频文件' }}
                  {{ source.description ? ` - ${source.description}` : '' }}
                </div>
              </div>
              
              <div class="flex items-center gap-2">
                <el-tag 
                  v-if="source.isAlreadyBound"
                  type="warning"
                  size="small"
                >
                  已绑定
                </el-tag>
                <el-tag 
                  :type="source.status === 'normal' ? 'success' : 'danger'"
                  size="small"
                >
                  {{ source.status === 'normal' ? '正常' : '异常' }}
                </el-tag>
              </div>
            </div>
          </div>
        </div>
        
        <!-- 空状态 -->
        <div v-else-if="!loadingSources" class="empty-sources text-center py-8">
          <el-icon size="48" class="text-gray-400 mb-4">
            <VideoCamera />
          </el-icon>
          <p class="text-gray-500">该设备没有可绑定的视频源</p>
        </div>
      </div>
    </div>
    
    <!-- 底部操作 -->
    <template #footer>
      <div class="flex justify-between items-center w-full">
        <div class="text-sm text-gray-500">
          <span v-if="selectedSources.length > 0">
            已选择 {{ selectedSources.length }} 个视频源
            <span v-if="selectedAlreadyBoundSources.length > 0" class="text-orange-600">
              (其中 {{ selectedAlreadyBoundSources.length }} 个已被绑定)
            </span>
          </span>
        </div>
        <div class="flex gap-2">
          <el-button @click="handleCancel">取消</el-button>
          <el-button 
            type="primary"
            :disabled="selectedSources.length === 0"
            @click="handleConfirm"
          >
            确定绑定
          </el-button>
        </div>
      </div>
    </template>
  </BaseDialog>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { 
  Monitor, VideoCamera, Search, Loading, Film
} from '@element-plus/icons-vue'
import BaseDialog from '@/components/ui/BaseDialog.vue'
import axios from 'axios'

const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  },
  node: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['update:visible', 'confirm'])

// 对话框状态
const dialogVisible = computed({
  get: () => props.visible,
  set: (val) => emit('update:visible', val)
})

// 设备列表
const deviceList = ref([])
const selectedDeviceId = ref(null)

// 视频源相关
const deviceSources = ref([])
const selectedSources = ref([])
const selectAllSources = ref(false)
const loadingSources = ref(false)
const sourceTypeFilter = ref('')
const sourceSearchText = ref('')

// 已绑定的视频源集合
const boundSources = ref(new Set())

// 计算属性
const filteredSources = computed(() => {
  let sources = deviceSources.value
  
  // 类型筛选
  if (sourceTypeFilter.value) {
    sources = sources.filter(s => s.type === sourceTypeFilter.value)
  }
  
  // 搜索筛选
  if (sourceSearchText.value) {
    const searchText = sourceSearchText.value.toLowerCase()
    sources = sources.filter(s => 
      (s.name || s.id).toLowerCase().includes(searchText) ||
      (s.description || '').toLowerCase().includes(searchText)
    )
  }
  
  return sources
})

const isSourceIndeterminate = computed(() => {
  return selectedSources.value.length > 0 && selectedSources.value.length < filteredSources.value.length
})

const selectedAlreadyBoundSources = computed(() => {
  return selectedSources.value.filter(s => s.isAlreadyBound)
})

// 监听对话框显示
watch(dialogVisible, (val) => {
  if (val) {
    loadDeviceList()
    resetForm()
  }
})

// 监听设备变化
watch(selectedDeviceId, (deviceId) => {
  if (deviceId) {
    loadDeviceSources()
  } else {
    deviceSources.value = []
    selectedSources.value = []
  }
})

// 加载设备列表
const loadDeviceList = async () => {
  try {
    const token = localStorage.getItem('token')
    const response = await axios.get('http://localhost:8000/api/devices', {
      headers: { Authorization: `Bearer ${token}` }
    })
    
    if (response.data.success) {
      deviceList.value = response.data.data || []
    }
  } catch (error) {
    console.error('加载设备列表失败:', error)
    ElMessage.error('加载设备列表失败')
  }
}

// 加载设备视频源
const loadDeviceSources = async () => {
  if (!selectedDeviceId.value) return
  
  loadingSources.value = true
  try {
    const token = localStorage.getItem('token')
    const params = sourceTypeFilter.value ? { source_type: sourceTypeFilter.value } : {}
    
    const response = await axios.get(
      `http://localhost:8000/api/devices/${selectedDeviceId.value}/sources`,
      {
        headers: { Authorization: `Bearer ${token}` },
        params
      }
    )
    
    if (response.data.success) {
      deviceSources.value = (response.data.data || []).map(source => ({
        ...source,
        isAlreadyBound: boundSources.value.has(`${selectedDeviceId.value}_${source.id}`)
      }))
    } else {
      ElMessage.error(response.data.message || '获取视频源失败')
      deviceSources.value = []
    }
  } catch (error) {
    console.error('加载视频源失败:', error)
    if (error.response?.status === 503) {
      ElMessage.error('设备离线，无法获取视频源')
    } else {
      ElMessage.error('获取视频源失败: ' + (error.response?.data?.message || error.message))
    }
    deviceSources.value = []
  } finally {
    loadingSources.value = false
  }
}

// 处理设备变化
const handleDeviceChange = () => {
  selectedSources.value = []
  selectAllSources.value = false
}

// 切换视频源选择
const toggleSourceSelection = (source) => {
  const index = selectedSources.value.findIndex(s => s.id === source.id)
  if (index > -1) {
    selectedSources.value.splice(index, 1)
  } else {
    selectedSources.value.push(source)
  }
  
  selectAllSources.value = selectedSources.value.length === filteredSources.value.length
}

// 全选/取消全选
const handleSelectAllSources = (val) => {
  if (val) {
    selectedSources.value = [...filteredSources.value]
  } else {
    selectedSources.value = []
  }
}

// 重置表单
const resetForm = () => {
  selectedDeviceId.value = null
  deviceSources.value = []
  selectedSources.value = []
  selectAllSources.value = false
  sourceTypeFilter.value = ''
  sourceSearchText.value = ''
}

// 处理取消
const handleCancel = () => {
  dialogVisible.value = false
}

// 处理确认
const handleConfirm = async () => {
  if (selectedSources.value.length === 0) {
    ElMessage.warning('请选择要绑定的视频源')
    return
  }
  
  // 检查是否有已绑定的视频源
  if (selectedAlreadyBoundSources.value.length > 0) {
    try {
      await ElMessageBox.confirm(
        `您选择的 ${selectedAlreadyBoundSources.value.length} 个视频源已绑定到其他业务节点，确认继续吗？`,
        '确认绑定',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }
      )
    } catch {
      return
    }
  }
  
  // 格式化绑定数据
  const bindingSources = selectedSources.value.map(source => ({
    device_id: selectedDeviceId.value,
    source_id: source.id,
    source_type: source.type,
    source_name: source.name
  }))
  
  emit('confirm', bindingSources)
  dialogVisible.value = false
  resetForm()
}
</script>

<style scoped>
.binding-modal-content {
  padding: 20px;
}

.step-section {
  border: 1px solid var(--color-border-secondary);
  border-radius: 8px;
  padding: 16px;
  background: var(--color-bg-secondary);
}

.step-title {
  font-size: 16px;
  font-weight: 600;
  color: var(--color-text-primary);
  margin: 0;
}

.source-filters {
  display: flex;
  align-items: center;
}

.sources-selection {
  border: 1px solid var(--color-border-light);
  border-radius: 6px;
  padding: 12px;
  background: var(--color-bg-primary);
}

.selection-toolbar {
  border-bottom: 1px solid var(--color-border-light);
  padding-bottom: 8px;
  margin-bottom: 12px;
}

.source-item {
  background: var(--color-bg-primary);
  transition: all 0.2s;
}

.source-item:hover {
  background: var(--color-bg-secondary);
}

.source-item.border-primary-500 {
  border-color: var(--color-primary-500);
  background: var(--color-primary-50);
}

/* 暗色主题适配 */
:global(.dark) .step-section {
  background: var(--color-neutral-900);
  border-color: var(--color-border-secondary);
}

:global(.dark) .sources-selection {
  background: var(--color-neutral-800);
  border-color: var(--color-border-secondary);
}

:global(.dark) .source-item {
  background: var(--color-neutral-800);
  border-color: var(--color-border-secondary);
}

:global(.dark) .source-item:hover {
  background: var(--color-neutral-700);
}
</style>