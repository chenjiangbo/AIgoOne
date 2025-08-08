<template>
  <div class="business-tree-panel h-full flex flex-col bg-white">
    <!-- 树形控件 -->
    <div class="tree-container flex-1 p-4 overflow-y-auto">
      <el-tree
        ref="treeRef"
        :data="treeData"
        :props="treeProps"
        :filter-node-method="filterNode"
        :allow-drag="allowDrag"
        :allow-drop="allowDrop"
        @node-drag-end="handleDragEnd"
        @node-click="handleNodeClick"
        @node-contextmenu="handleContextMenu"
        node-key="id"
        :default-expand-all="true"
        :expand-on-click-node="false"
        draggable
        class="business-tree"
      >
        <template #default="{ node, data }">
          <div class="tree-node flex items-center w-full">
            <!-- 节点图标 -->
            <el-icon 
              :class="[
                'node-icon mr-2 text-lg',
                getNodeIconClass(data)
              ]"
              :style="{
                color: getNodeIconColor(data)
              }"
            >
              <component :is="getNodeIcon(data)" />
            </el-icon>
            
            <!-- 节点标签 -->
            <span 
              :class="[
                'node-label flex-1',
                { 'text-blue-600': data.id === selectedNodeId }
              ]"
            >
              {{ node.label }}
            </span>
            
            <!-- 节点状态标识 -->
            <div class="node-badges flex items-center gap-1 ml-2">
              <!-- 叶子节点标识 -->
              <el-tag 
                v-if="data.is_leaf" 
                type="success" 
                size="small"
                class="text-xs"
              >
                叶子
              </el-tag>
              
              <!-- 视频源数量 -->
              <el-badge 
                v-if="data.is_leaf && data.source_count > 0"
                :value="data.source_count"
                type="info"
                class="ml-1"
              >
                <el-icon><VideoCamera /></el-icon>
              </el-badge>
              
              <!-- 待保存状态 -->
              <el-icon 
                v-if="isPendingNode(data.id)"
                color="orange"
                class="ml-1"
              >
                <Clock />
              </el-icon>
            </div>
          </div>
        </template>
      </el-tree>
    </div>
    
    <!-- 右键菜单 -->
    <el-dropdown
      ref="contextMenuRef"
      :show-timeout="0"
      :hide-timeout="0"
      trigger="contextmenu"
      @command="handleMenuCommand"
    >
      <div></div>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item 
            command="add"
            :disabled="!contextNode || contextNode.is_leaf"
            :icon="Plus"
          >
            添加子节点
          </el-dropdown-item>
          <el-dropdown-item 
            command="rename"
            :disabled="!contextNode"
            :icon="Edit"
          >
            重命名
          </el-dropdown-item>
          <el-dropdown-item 
            command="delete"
            :disabled="!contextNode || !contextNode.parent_id"
            :icon="Delete"
            divided
          >
            删除节点
          </el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
    
    <!-- 节点编辑对话框 -->
    <NodeEditDialog
      v-model:visible="showNodeEditDialog"
      :title="nodeEditTitle"
      :default-value="nodeEditDefaultValue"
      @confirm="handleNodeEditConfirm"
      @cancel="handleNodeEditCancel"
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
import { ref, computed, watch, nextTick } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { 
  Search, Plus, Edit, Delete, Clock, VideoCamera,
  OfficeBuilding, MapLocation, Collection, Place, FolderOpened
} from '@element-plus/icons-vue'
import { useBusinessTreeStore } from '@/store/businessTree'
import NodeEditDialog from '../dialogs/NodeEditDialog.vue'
import ConfirmDialog from '../dialogs/ConfirmDialog.vue'

const emit = defineEmits(['node-select', 'node-change'])

const businessTreeStore = useBusinessTreeStore()

// 模板引用
const treeRef = ref(null)
const contextMenuRef = ref(null)

// 搜索文本
const searchText = ref('')

// 选中的节点ID
const selectedNodeId = ref(null)

// 右键菜单上下文节点
const contextNode = ref(null)

// 节点编辑对话框
const showNodeEditDialog = ref(false)
const nodeEditTitle = ref('')
const nodeEditDefaultValue = ref('')
const nodeEditMode = ref('') // 'add' | 'rename'
const nodeEditTargetNode = ref(null)

// 确认对话框
const showConfirmDialog = ref(false)
const confirmTitle = ref('')
const confirmMessage = ref('')
const confirmDetails = ref('')
const confirmType = ref('warning')
const confirmButtonText = ref('确定')
const confirmAction = ref(null)

// 树配置
const treeProps = {
  children: 'children',
  label: 'name'
}

// 树数据
const treeData = computed(() => businessTreeStore.treeData)

// 树节点过滤
const filterNode = (value, data) => {
  if (!value) return true
  return data.name.toLowerCase().includes(value.toLowerCase())
}

// 处理搜索
const handleSearch = (value) => {
  if (treeRef.value) {
    treeRef.value.filter(value)
  }
}

// 允许拖拽的判断
const allowDrag = (node) => {
  // 只允许叶子节点拖拽
  return node.data.is_leaf
}

// 允许放置的判断
const allowDrop = (draggingNode, dropNode, type) => {
  // 只能放置到非叶子节点内部
  if (dropNode.data.is_leaf) return false
  if (type !== 'inner') return false
  // 检查层级限制（最多5层）
  if (dropNode.level >= 4) return false
  return true
}

// 处理拖拽结束
const handleDragEnd = (draggingNode, dropNode, dropType) => {
  if (dropType === 'inner' && dropNode) {
    // 执行移动操作
    businessTreeStore.moveNode(draggingNode.data.id, dropNode.data.id)
    emit('node-change')
    ElMessage.success('节点移动已添加到待保存列表')
  }
}

// 处理节点点击
const handleNodeClick = (data, node) => {
  selectedNodeId.value = data.id
  emit('node-select', data)
}

// 处理右键菜单
const handleContextMenu = (event, data, node) => {
  event.preventDefault()
  contextNode.value = data
  
  // 显示右键菜单
  nextTick(() => {
    if (contextMenuRef.value) {
      contextMenuRef.value.handleClick()
    }
  })
}

// 处理菜单命令
const handleMenuCommand = (command) => {
  if (!contextNode.value) return
  
  switch (command) {
    case 'add':
      handleAddNode()
      break
    case 'rename':
      handleRenameNode()
      break
    case 'delete':
      handleDeleteNode()
      break
  }
}

// 添加子节点
const handleAddNode = () => {
  const parentNode = contextNode.value
  if (!parentNode || parentNode.is_leaf) {
    ElMessage.warning('只能在非叶子节点下添加子节点')
    return
  }
  
  nodeEditMode.value = 'add'
  nodeEditTitle.value = '添加子节点'
  nodeEditDefaultValue.value = ''
  nodeEditTargetNode.value = parentNode
  showNodeEditDialog.value = true
}

// 重命名节点
const handleRenameNode = () => {
  const node = contextNode.value
  if (!node) return
  
  nodeEditMode.value = 'rename'
  nodeEditTitle.value = '重命名节点'
  nodeEditDefaultValue.value = node.name
  nodeEditTargetNode.value = node
  showNodeEditDialog.value = true
}

// 删除节点
const handleDeleteNode = () => {
  const node = contextNode.value
  if (!node) return
  
  if (!node.parent_id) {
    ElMessage.error('不能删除根节点')
    return
  }
  
  if (node.children && node.children.length > 0) {
    ElMessage.error('请先删除所有子节点')
    return
  }
  
  const sourceCount = node.source_count || 0
  let message = `确定要删除节点 "${node.name}" 吗？`
  let details = '删除后无法恢复，请谨慎操作。'
  
  if (sourceCount > 0) {
    message = `节点 "${node.name}" 已绑定 ${sourceCount} 个视频源，是否确认删除？`
    details = '删除后将解除所有绑定关系，且无法恢复。'
  }
  
  confirmTitle.value = '确认删除'
  confirmMessage.value = message
  confirmDetails.value = details
  confirmType.value = 'danger'
  confirmButtonText.value = '删除'
  confirmAction.value = () => {
    businessTreeStore.deleteNode(node.id)
    emit('node-change')
    ElMessage.success('节点删除已添加到待保存列表')
  }
  showConfirmDialog.value = true
}

// 获取节点图标
const getNodeIcon = (data) => {
  if (data.is_leaf) {
    return Place // 叶子节点用地点图标
  }
  
  // 根据层级返回不同图标
  switch (data.depth) {
    case 0: return OfficeBuilding  // 根节点
    case 1: return MapLocation     // 第一层
    case 2: return Collection      // 第二层
    default: return FolderOpened   // 其他层级
  }
}

// 获取节点图标颜色
const getNodeIconColor = (data) => {
  if (data.is_leaf) {
    return '#f97316'  // 叶子节点橙色
  }
  
  switch (data.depth) {
    case 0: return '#2563eb'    // 根节点蓝色
    case 1: return '#16a34a'    // 第一层绿色
    case 2: return '#9333ea'    // 第二层紫色
    default: return '#6b7280'   // 其他层级灰色
  }
}

// 获取节点图标样式类
const getNodeIconClass = (data) => {
  return ''  // 不再使用类，直接使用内联样式
}

// 检查是否为待处理节点
const isPendingNode = (nodeId) => {
  const changes = businessTreeStore.pendingChanges
  return changes.added.some(n => n.id === nodeId) ||
         changes.updated.some(n => n.id === nodeId) ||
         changes.deleted.includes(nodeId) ||
         changes.moved.some(n => n.node_id === nodeId)
}

// 监听搜索文本变化
watch(searchText, (val) => {
  if (treeRef.value) {
    treeRef.value.filter(val)
  }
})

// 节点编辑对话框处理
const handleNodeEditConfirm = (value) => {
  if (nodeEditMode.value === 'add' && nodeEditTargetNode.value) {
    businessTreeStore.createNode(nodeEditTargetNode.value.id, value)
    emit('node-change')
    ElMessage.success('节点已添加到待保存列表')
  } else if (nodeEditMode.value === 'rename' && nodeEditTargetNode.value) {
    if (value !== nodeEditTargetNode.value.name) {
      businessTreeStore.updateNode(nodeEditTargetNode.value.id, { name: value })
      emit('node-change')
      ElMessage.success('节点重命名已添加到待保存列表')
    }
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
</script>

<style scoped>
.business-tree-panel {
  background: var(--color-bg-primary);
}

.search-bar {
  background: var(--color-bg-secondary);
  border-bottom: 1px solid var(--color-border-secondary);
}

.tree-container {
  flex: 1;
  overflow-y: auto;
}

:deep(.business-tree) {
  background: transparent;
}

:deep(.business-tree .el-tree-node__content) {
  height: 36px;
  padding: 0 8px;
  border-radius: 6px;
  margin: 1px 0;
  transition: all 0.2s;
}

:deep(.business-tree .el-tree-node__content:hover) {
  background: var(--color-bg-secondary);
}

:deep(.business-tree .el-tree-node.is-current > .el-tree-node__content) {
  background: var(--color-primary-50);
  border: 1px solid var(--color-primary-200);
}

.tree-node {
  width: 100%;
  user-select: none;
}

.node-icon {
  font-size: 16px;
  flex-shrink: 0;
}

.node-label {
  font-size: 14px;
  line-height: 1.2;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.node-badges {
  flex-shrink: 0;
}

/* 拖拽样式 */
:deep(.business-tree .el-tree-node.is-drop-inner) {
  background: var(--color-primary-50);
  border: 2px dashed var(--color-primary-300);
}

:deep(.business-tree .el-tree-node__content.is-dragging) {
  opacity: 0.5;
  transform: rotate(5deg);
}

/* 暗色主题适配 */
:global(.dark) .search-bar {
  background: var(--color-neutral-900);
  border-color: var(--color-border-secondary);
}

:global(.dark) .business-tree-panel {
  background: var(--color-neutral-800);
}

:global(.dark) :deep(.business-tree .el-tree-node__content:hover) {
  background: var(--color-neutral-700);
}

:global(.dark) :deep(.business-tree .el-tree-node.is-current > .el-tree-node__content) {
  background: var(--color-primary-900);
  border-color: var(--color-primary-600);
}
</style>