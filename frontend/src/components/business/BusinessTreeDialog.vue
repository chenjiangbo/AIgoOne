<template>
  <BaseDialog
    v-model:visible="dialogVisible"
    title="业务树管理"
    subtitle="配置业务层级结构和视频源绑定"
    :width="'75%'"
    :show-maximize="false"
    :show-default-footer="false"
    :close-on-click-modal="false"
    :close-on-press-escape="false"
    :before-close="handleBeforeClose"
    :draggable="true"
    :overflow="true"
    class="business-tree-dialog"
  >
    <!-- 工具栏 -->
    <div class="toolbar flex items-center justify-between p-3 border-b bg-gray-50">
      <div class="flex items-center gap-3">
        <el-button-group>
          <el-button 
            size="default"
            type="success"
            :icon="Plus"
            @click="handleAddRootChild"
            :disabled="!selectedNode"
            title="添加子节点"
          >
            添加
          </el-button>
          <el-button 
            size="default"
            type="primary"
            :icon="Edit"
            @click="handleEditNode"
            :disabled="!selectedNode"
            title="编辑节点"
          >
            编辑
          </el-button>
          <el-button 
            size="default"
            type="danger"
            :icon="Delete"
            @click="handleDeleteNode" 
            :disabled="!selectedNode || selectedNode.id === 1"
            title="删除节点"
          >
            删除
          </el-button>
        </el-button-group>
        <el-button
          size="default"
          :icon="RefreshRight"
          @click="handleRefresh"
          title="刷新"
        >
          刷新
        </el-button>
      </div>
      <div class="flex items-center gap-2">
        <!-- 调试信息 -->
        <span v-if="selectedNode" class="text-xs text-gray-500 mr-2">
          {{ selectedNode.name }} ({{ selectedNode.is_leaf ? '叶子' : '非叶子' }})
        </span>
        <el-button 
          v-if="selectedNode && selectedNode.is_leaf"
          type="primary" 
          :icon="Link"
          @click="handleBindVideoSources"
          title="绑定视频源"
        >
          绑定视频源
        </el-button>
      </div>
    </div>
    
    <!-- 主体内容 -->
    <div class="main-content flex gap-4 p-4" style="height: 450px;">
      <!-- 左侧：业务树面板 -->
      <div class="tree-panel w-1/3 h-full overflow-hidden bg-white rounded-lg shadow-md border border-gray-200">
        <BusinessTreePanel 
          @node-select="handleNodeSelect"
          @node-change="handleNodeChange"
        />
      </div>
      
      <!-- 右侧：视频源绑定面板 -->
      <div class="source-panel w-2/3 h-full overflow-hidden bg-white rounded-lg shadow-md border border-gray-200">
        <SourceBindingPanel 
          ref="sourcePanelRef"
          :node="selectedNode"
          @bind-sources="handleBindSources"
          @unbind-sources="handleUnbindSources"
        />
      </div>
    </div>
    
    <!-- 底部操作栏 -->
    <template #footer>
      <div class="flex justify-between items-center w-full">
        <div class="flex items-center gap-4">
          <el-tag v-if="hasChanges" type="warning" size="default">
            有未保存的更改
          </el-tag>
          <div class="text-sm text-gray-600">
            节点总数: {{ nodeCount }} | 叶子节点: {{ leafNodeCount }}
          </div>
        </div>
        <div class="flex gap-2">
          <el-button @click="handleCancel">取消</el-button>
          <el-button 
            type="primary" 
            :loading="saving"
            @click="handleSaveAndClose"
            :disabled="!hasChanges"
          >
            保存并关闭
          </el-button>
        </div>
      </div>
    </template>
  </BaseDialog>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Plus, Check, RefreshRight, FolderOpened, Edit, Delete, Link } from '@element-plus/icons-vue'
import { useBusinessTreeStore } from '@/store/businessTree'
import BaseDialog from '@/components/ui/BaseDialog.vue'
import BusinessTreePanel from './tree/BusinessTreePanel.vue'
import SourceBindingPanel from './source/SourceBindingPanel.vue'

const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:visible'])

const businessTreeStore = useBusinessTreeStore()

// 对话框显示状态
const dialogVisible = computed({
  get: () => props.visible,
  set: (val) => emit('update:visible', val)
})

// 选中的节点
const selectedNode = ref(null)

// 子组件引用
const sourcePanelRef = ref(null)

// 保存状态
const saving = computed(() => businessTreeStore.saving)

// 是否有未保存的更改
const hasChanges = computed(() => businessTreeStore.hasChanges)

// 节点统计
const nodeCount = computed(() => {
  const countNodes = (nodes) => {
    let count = 0
    for (const node of nodes) {
      count++
      if (node.children && node.children.length > 0) {
        count += countNodes(node.children)
      }
    }
    return count
  }
  return countNodes(businessTreeStore.treeData)
})

const leafNodeCount = computed(() => {
  return businessTreeStore.leafNodes.length
})

// 监听对话框显示状态
watch(dialogVisible, (val) => {
  if (val) {
    // 打开对话框时加载数据
    businessTreeStore.loadTree()
  }
})

// 处理节点选择
const handleNodeSelect = (node) => {
  selectedNode.value = node
  businessTreeStore.setSelectedNode(node)
}

// 处理节点变更
const handleNodeChange = () => {
  // 节点变更时的处理（如拖拽、编辑等）
}

// 添加子节点
const handleAddRootChild = () => {
  if (!selectedNode.value || selectedNode.value.is_leaf) {
    ElMessage.warning('请选择一个非叶子节点')
    return
  }
  
  ElMessageBox.prompt('请输入节点名称', '添加子节点', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    inputPattern: /^.{1,64}$/,
    inputErrorMessage: '节点名称长度应在1-64个字符之间',
    customClass: 'business-tree-prompt'
  }).then(({ value }) => {
    businessTreeStore.createNode(selectedNode.value.id, value)
    ElMessage.success('节点已添加到待保存列表')
  }).catch(() => {})
}

// 编辑节点
const handleEditNode = () => {
  if (!selectedNode.value) {
    ElMessage.warning('请选择一个节点')
    return
  }
  
  ElMessageBox.prompt('请输入新的节点名称', '编辑节点', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    inputValue: selectedNode.value.name,
    inputPattern: /^.{1,64}$/,
    inputErrorMessage: '节点名称长度应在1-64个字符之间',
    customClass: 'business-tree-prompt'
  }).then(({ value }) => {
    businessTreeStore.updateNode(selectedNode.value.id, { name: value })
    ElMessage.success('节点已修改，等待保存')
  }).catch(() => {})
}

// 删除节点
const handleDeleteNode = () => {
  if (!selectedNode.value) {
    ElMessage.warning('请选择一个节点')
    return
  }
  
  if (selectedNode.value.id === 1) {
    ElMessage.warning('根节点不能删除')
    return
  }
  
  ElMessageBox.confirm(`确定要删除节点"${selectedNode.value.name}"吗？`, '删除确认', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning',
    customClass: 'business-tree-prompt'
  }).then(() => {
    businessTreeStore.deleteNode(selectedNode.value.id)
    ElMessage.success('节点已删除，等待保存')
  }).catch(() => {})
}

// 处理绑定视频源
const handleBindSources = (sources) => {
  if (!selectedNode.value) return
  businessTreeStore.bindSources(selectedNode.value.id, sources)
  ElMessage.success('视频源绑定已添加到待保存列表')
}

// 处理解绑视频源
const handleUnbindSources = (mappingIds) => {
  if (!selectedNode.value) return
  businessTreeStore.unbindSources(selectedNode.value.id, mappingIds)
  ElMessage.success('视频源解绑已添加到待保存列表')
}

// 保存更改
const handleSave = async () => {
  await businessTreeStore.saveChanges()
}

// 保存并关闭
const handleSaveAndClose = async () => {
  await businessTreeStore.saveChanges()
  if (!businessTreeStore.saving) {
    dialogVisible.value = false
  }
}

// 刷新数据
const handleRefresh = async () => {
  if (hasChanges.value) {
    await ElMessageBox.confirm(
      '您有未保存的更改，刷新将丢失这些更改，是否继续？',
      '确认刷新',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }
    )
  }
  businessTreeStore.clearPendingChanges()
  await businessTreeStore.loadTree()
  ElMessage.success('数据已刷新')
}

// 取消
const handleCancel = () => {
  if (hasChanges.value) {
    ElMessageBox.confirm(
      '您有未保存的更改，确定要关闭吗？',
      '确认关闭',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }
    ).then(() => {
      businessTreeStore.clearPendingChanges()
      dialogVisible.value = false
    }).catch(() => {})
  } else {
    dialogVisible.value = false
  }
}

// 关闭前的处理
const handleBeforeClose = (done) => {
  if (hasChanges.value) {
    confirmTitle.value = '确认关闭'
    confirmMessage.value = '您有未保存的更改，确定要关闭吗？'
    confirmDetails.value = '所有未保存的修改将被丢弃。'
    confirmType.value = 'warning'
    confirmButtonText.value = '关闭'
    confirmAction.value = () => {
      businessTreeStore.clearPendingChanges()
      done()
    }
    showConfirmDialog.value = true
  } else {
    done()
  }
}

// 节点编辑对话框处理
const handleNodeEditConfirm = (value) => {
  if (nodeEditMode.value === 'add' && nodeEditTargetNode.value) {
    businessTreeStore.createNode(nodeEditTargetNode.value.id, value)
    ElMessage.success('节点已添加到待保存列表')
  } else if (nodeEditMode.value === 'edit' && nodeEditTargetNode.value) {
    businessTreeStore.updateNode(nodeEditTargetNode.value.id, { name: value })
    ElMessage.success('节点已修改，等待保存')
  }
  
  // 清理状态
  nodeEditMode.value = ''
  nodeEditTargetNode.value = null
}

const handleNodeEditCancel = () => {
  // 清理状态
  nodeEditMode.value = ''
  nodeEditTargetNode.value = null
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

// 处理绑定视频源按钮点击
const handleBindVideoSources = () => {
  if (selectedNode.value && selectedNode.value.is_leaf && sourcePanelRef.value) {
    sourcePanelRef.value.showBindingModal = true
  }
}
</script>

<style scoped>
.business-tree-dialog {
  --dialog-padding: 0;
}

:deep(.el-dialog__body) {
  padding: 0 !important;
}

.toolbar {
  background: var(--color-bg-secondary);
}

.main-content {
  background: var(--color-bg-primary);
}

.tree-panel {
  background: var(--color-bg-primary);
  overflow-y: auto;
}

.source-panel {
  background: var(--color-bg-primary);
  overflow-y: auto;
}

/* 暗色主题适配 */
:global(.dark) .toolbar {
  background: var(--color-neutral-900);
  border-color: var(--color-border-secondary);
}

:global(.dark) .tree-panel,
:global(.dark) .source-panel {
  background: var(--color-neutral-800);
  border-color: var(--color-border-secondary);
}
</style>