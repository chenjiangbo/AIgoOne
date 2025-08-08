<template>
  <div class="source-binding-panel h-full flex flex-col">
    <!-- 头部信息 -->
    <div class="panel-header p-4">
      <div v-if="!node" class="empty-state text-center py-12">
        <p class="text-gray-400 text-sm">请选择一个节点</p>
      </div>
      <div v-else class="node-info">
        <div class="flex items-center justify-between mb-2">
          <div class="flex items-center gap-4">
            <div class="flex items-center">
              <el-icon class="text-green-600 mr-2"><Place /></el-icon>
              <h3 class="text-lg font-semibold">{{ node.name }}</h3>
            </div>
            <div class="flex items-center gap-4 text-sm text-gray-600">
              <span class="flex items-center">
                <el-icon class="mr-1"><VideoCamera /></el-icon>
                已绑定: {{ sourceList.length }} 个视频源
              </span>
              <span v-if="invalidSources.length > 0" class="text-orange-600 flex items-center">
                <el-icon class="mr-1"><Warning /></el-icon>
                失效: {{ invalidSources.length }} 个
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- 视频源列表 -->
    <div v-if="node && node.is_leaf" class="source-list flex-1 p-4 overflow-y-auto">
      <div v-if="loading" class="text-center py-8">
        <el-icon class="animate-spin text-2xl text-gray-400 mb-2">
          <Loading />
        </el-icon>
        <p class="text-gray-500">加载中...</p>
      </div>
      
      <div v-else-if="sourceList.length === 0" class="empty-sources text-center py-8">
        <el-icon size="48" class="text-gray-400 mb-4">
          <VideoCamera />
        </el-icon>
        <p class="text-gray-500 mb-4">该节点尚未绑定视频源</p>
        <el-button type="primary" @click="showBindingModal = true">
          立即绑定
        </el-button>
      </div>
      
      <div v-else class="sources-table">
        <!-- 操作工具栏 -->
        <div class="table-toolbar flex items-center justify-between mb-4">
          <div class="flex items-center gap-2">
            <el-checkbox 
              v-model="selectAll" 
              :indeterminate="isIndeterminate"
              @change="handleSelectAll"
            >
              全选
            </el-checkbox>
            <el-button 
              v-if="selectedSources.length > 0"
              type="danger"
              size="small"
              :icon="Delete"
              @click="handleBatchUnbind"
            >
              批量解绑 ({{ selectedSources.length }})
            </el-button>
          </div>
          <div class="flex items-center gap-2">
            <el-button 
              :icon="Refresh"
              size="small"
              @click="handleSyncStatus"
            >
              同步状态
            </el-button>
            <el-input
              v-model="searchText"
              placeholder="搜索视频源..."
              size="small"
              style="width: 200px"
              clearable
            />
          </div>
        </div>
        
        <!-- 视频源表格 -->
        <el-table
          :data="filteredSources"
          :row-key="row => row.id"
          @selection-change="handleSelectionChange"
          stripe
          size="small"
        >
          <el-table-column type="selection" width="55" />
          
          <el-table-column 
            prop="source_name" 
            label="视频源名称"
            min-width="150"
          >
            <template #default="{ row }">
              <div class="flex items-center">
                <el-icon 
                  :class="[
                    'mr-2',
                    row.source_type === 'camera' ? 'text-blue-600' : 'text-green-600'
                  ]"
                >
                  <VideoCamera v-if="row.source_type === 'camera'" />
                  <Film v-else />
                </el-icon>
                <span>{{ row.source_name || row.source_id }}</span>
              </div>
            </template>
          </el-table-column>
          
          <el-table-column 
            prop="source_type" 
            label="类型"
            width="80"
          >
            <template #default="{ row }">
              <el-tag 
                :type="row.source_type === 'camera' ? 'primary' : 'success'"
                size="small"
              >
                {{ row.source_type === 'camera' ? '摄像头' : '视频文件' }}
              </el-tag>
            </template>
          </el-table-column>
          
          <el-table-column 
            prop="device_name" 
            label="所属设备"
            min-width="120"
          >
            <template #default="{ row }">
              <el-tooltip :content="row.device_url" placement="top">
                <span>{{ row.device_name }}</span>
              </el-tooltip>
            </template>
          </el-table-column>
          
          <el-table-column 
            prop="status" 
            label="状态"
            width="80"
          >
            <template #default="{ row }">
              <el-tag 
                :type="row.status === 'normal' ? 'success' : 'warning'"
                size="small"
              >
                {{ row.status === 'normal' ? '正常' : '失效' }}
              </el-tag>
            </template>
          </el-table-column>
          
          <el-table-column 
            prop="last_sync_at" 
            label="最后同步"
            width="120"
          >
            <template #default="{ row }">
              <span class="text-xs text-gray-500">
                {{ formatDate(row.last_sync_at) }}
              </span>
            </template>
          </el-table-column>
          
          <el-table-column label="操作" width="100">
            <template #default="{ row }">
              <el-button
                type="danger"
                size="small"
                text
                @click="handleUnbindSingle(row)"
              >
                解绑
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
    
    <!-- 视频源绑定弹窗 -->
    <SourceBindingModal
      v-model:visible="showBindingModal"
      :node="node"
      @confirm="handleBindConfirm"
    />
    
    <!-- 确认对话框 -->
    <ConfirmDialog
      v-model:visible="showConfirmDialog"
      :title="confirmTitle"
      :message="confirmMessage"
      :details="confirmDetails"
      :type="confirmType"
      :confirm-text="confirmButtonText"
      @confirm="handleConfirmDialogConfirm"
      @cancel="handleConfirmDialogCancel"
    />
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { 
  FolderOpened, Collection, Place, Link, VideoCamera, Warning,
  Loading, Delete, Refresh, Film
} from '@element-plus/icons-vue'
import { useBusinessTreeStore } from '@/store/businessTree'
import SourceBindingModal from './SourceBindingModal.vue'
import ConfirmDialog from '../dialogs/ConfirmDialog.vue'

const props = defineProps({
  node: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['bind-sources', 'unbind-sources'])

const businessTreeStore = useBusinessTreeStore()

// 视频源列表
const sourceList = ref([])
const loading = ref(false)
const searchText = ref('')

// 选择状态
const selectedSources = ref([])
const selectAll = ref(false)

// 绑定弹窗
const showBindingModal = ref(false)

// 确认对话框
const showConfirmDialog = ref(false)
const confirmTitle = ref('')
const confirmMessage = ref('')
const confirmDetails = ref('')
const confirmType = ref('warning')
const confirmButtonText = ref('确定')
const confirmAction = ref(null)

// 计算属性
const filteredSources = computed(() => {
  if (!searchText.value) return sourceList.value
  return sourceList.value.filter(source => 
    (source.source_name || source.source_id)
      .toLowerCase()
      .includes(searchText.value.toLowerCase())
  )
})

const invalidSources = computed(() => {
  return sourceList.value.filter(source => source.status === 'invalid')
})

const isIndeterminate = computed(() => {
  return selectedSources.value.length > 0 && selectedSources.value.length < sourceList.value.length
})

// 监听节点变化
watch(() => props.node, async (newNode) => {
  selectedSources.value = []
  selectAll.value = false
  
  if (newNode && newNode.is_leaf) {
    await loadSources()
  } else {
    sourceList.value = []
  }
}, { immediate: true })

// 加载视频源
const loadSources = async () => {
  if (!props.node || !props.node.is_leaf) return
  
  loading.value = true
  try {
    const sources = await businessTreeStore.loadNodeSources(props.node.id)
    sourceList.value = sources || []
  } catch (error) {
    console.error('加载视频源失败:', error)
    sourceList.value = []
  } finally {
    loading.value = false
  }
}

// 获取节点路径
const getNodePath = () => {
  return props.node?.path || '/'
}

// 处理全选
const handleSelectAll = (val) => {
  if (val) {
    selectedSources.value = [...sourceList.value]
  } else {
    selectedSources.value = []
  }
}

// 处理选择变化
const handleSelectionChange = (selection) => {
  selectedSources.value = selection
  selectAll.value = selection.length === sourceList.value.length
}

// 批量解绑
const handleBatchUnbind = () => {
  if (selectedSources.value.length === 0) {
    ElMessage.warning('请选择要解绑的视频源')
    return
  }
  
  confirmTitle.value = '确认解绑'
  confirmMessage.value = `确定要解绑选中的 ${selectedSources.value.length} 个视频源吗？`
  confirmDetails.value = '解绑后这些视频源将不再属于当前节点。'
  confirmType.value = 'warning'
  confirmButtonText.value = '解绑'
  confirmAction.value = () => {
    const mappingIds = selectedSources.value.map(source => source.id)
    emit('unbind-sources', mappingIds)
    
    // 更新本地列表
    sourceList.value = sourceList.value.filter(
      source => !mappingIds.includes(source.id)
    )
    selectedSources.value = []
    selectAll.value = false
  }
  showConfirmDialog.value = true
}

// 解绑单个视频源
const handleUnbindSingle = (row) => {
  confirmTitle.value = '确认解绑'
  confirmMessage.value = `确定要解绑视频源 "${row.source_name || row.source_id}" 吗？`
  confirmDetails.value = '解绑后该视频源将不再属于当前节点。'
  confirmType.value = 'warning'
  confirmButtonText.value = '解绑'
  confirmAction.value = () => {
    emit('unbind-sources', [row.id])
    
    // 更新本地列表
    const index = sourceList.value.findIndex(source => source.id === row.id)
    if (index !== -1) {
      sourceList.value.splice(index, 1)
    }
  }
  showConfirmDialog.value = true
}

// 同步状态
const handleSyncStatus = async () => {
  if (!props.node) return
  
  loading.value = true
  try {
    ElMessage.success('状态同步完成')
    await loadSources()
  } catch (error) {
    ElMessage.error('状态同步失败')
  } finally {
    loading.value = false
  }
}

// 处理绑定确认
const handleBindConfirm = (sources) => {
  emit('bind-sources', sources)
  
  // 更新本地列表
  sourceList.value.push(...sources)
  ElMessage.success(`成功添加 ${sources.length} 个视频源到待保存列表`)
}

// 格式化日期
const formatDate = (dateStr) => {
  if (!dateStr) return '-'
  const date = new Date(dateStr)
  return date.toLocaleString('zh-CN', {
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  })
}

// 确认对话框处理
const handleConfirmDialogConfirm = () => {
  if (confirmAction.value) {
    confirmAction.value()
  }
  showConfirmDialog.value = false
  
  // 清理状态
  confirmAction.value = null
}

const handleConfirmDialogCancel = () => {
  // 清理状态
  confirmAction.value = null
}
</script>

<style scoped>
.source-binding-panel {
  background: var(--color-bg-primary);
}

.panel-header {
  background: var(--color-bg-secondary);
  border-bottom: 1px solid var(--color-border-secondary);
}

.source-list {
  flex: 1;
  overflow-y: auto;
}

.table-toolbar {
  padding-bottom: 16px;
  border-bottom: 1px solid var(--color-border-secondary);
  margin-bottom: 16px;
}

:deep(.el-table) {
  background: transparent;
}
</style>