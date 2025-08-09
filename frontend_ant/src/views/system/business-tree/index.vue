<template>
  <div class="business-tree-management">
    <!-- 页面头部 -->
    <div class="page-header">
      <div class="header-left">
        <div class="title-with-logo">
          <div class="page-logo">
            <ApartmentOutlined />
          </div>
          <div class="title-content">
            <h1 class="page-title">业务树管理</h1>
            <p class="page-description">配置和管理业务树结构，建立视频源与业务单元的绑定关系</p>
          </div>
        </div>
      </div>
      <div class="header-right">
        <a-space>
          <a-button type="default" @click="handleCancel">取消</a-button>
          <a-button 
            type="primary" 
            :loading="saving" 
            :disabled="!hasUnsavedChanges"
            @click="handleSave"
          >
            保存
          </a-button>
        </a-space>
      </div>
    </div>

    <!-- 主内容区 -->
    <div class="main-content">
      <!-- 左侧业务树面板 -->
      <div class="tree-panel">
        <div class="panel-header">
          <h3>业务树结构</h3>
          <a-space>
            <a-tooltip title="添加子节点">
              <a-button
                type="text"
                size="small"
                :disabled="!selectedNode || (selectedNode.is_leaf && hasBindings)"
                @click="handleAddNode"
              >
                <PlusOutlined />
              </a-button>
            </a-tooltip>
            <a-tooltip title="编辑节点">
              <a-button
                type="text"
                size="small"
                :disabled="!selectedNode"
                @click="handleEditNode"
              >
                <EditOutlined />
              </a-button>
            </a-tooltip>
            <a-tooltip title="删除节点">
              <a-button
                type="text"
                size="small"
                danger
                :disabled="!selectedNode || selectedNode.id === 'root' || hasChildren"
                @click="handleDeleteNode"
              >
                <DeleteOutlined />
              </a-button>
            </a-tooltip>
          </a-space>
        </div>
        
        <div class="panel-content">
          <a-tree
            v-model:selectedKeys="selectedKeys"
            v-model:expandedKeys="expandedKeys"
            :tree-data="treeData"
            :field-names="{ title: 'name', key: 'id', children: 'children' }"
            show-icon
            block-node
            @select="handleNodeSelect"
          >
            <template #icon="{ dataRef }">
              <FolderOutlined v-if="!dataRef.is_leaf" style="color: #1890ff; font-size: 14px;" />
              <FileOutlined v-else style="color: #52c41a; font-size: 14px;" />
            </template>
            <template #title="{ dataRef }">
              <div class="tree-node-title">
                <span>{{ dataRef.name }}</span>
                <span v-if="dataRef.is_leaf && dataRef.source_count > 0" class="binding-count">
                  {{ dataRef.source_count }}
                </span>
              </div>
            </template>
          </a-tree>
        </div>
      </div>

      <!-- 右侧详情面板 -->
      <div class="detail-panel">
        <!-- 未选中节点时 -->
        <div v-if="!selectedNode" class="empty-state">
          <a-empty description="请选择左侧树节点进行配置">
            <template #image>
              <FolderOpenOutlined style="font-size: 64px; color: #d9d9d9;" />
            </template>
          </a-empty>
        </div>

        <!-- 选中非叶子节点时 -->
        <div v-else-if="!selectedNode.is_leaf" class="node-info">
          <h3>{{ selectedNode.name }}</h3>
          <a-descriptions :column="1" size="small">
            <a-descriptions-item label="节点类型">分支节点</a-descriptions-item>
            <a-descriptions-item label="子节点数">{{ selectedNode.children?.length || 0 }}</a-descriptions-item>
            <a-descriptions-item label="创建时间">{{ selectedNode.created_at || '-' }}</a-descriptions-item>
            <a-descriptions-item label="更新时间">{{ selectedNode.updated_at || '-' }}</a-descriptions-item>
          </a-descriptions>
          <a-alert
            message="分支节点信息"
            description="分支节点用于组织业务层级结构。选择叶子节点可以进行视频源绑定配置。"
            type="info"
            show-icon
            style="margin-top: 16px;"
          />
        </div>

        <!-- 选中叶子节点时 -->
        <div v-else class="leaf-node-detail">
          <div class="detail-header">
            <h3>{{ selectedNode.name }} - 视频源绑定</h3>
            <a-input
              v-model:value="searchText"
              placeholder="搜索视频源..."
              allow-clear
              style="width: 300px;"
            >
              <template #prefix>
                <SearchOutlined />
              </template>
            </a-input>
          </div>

          <div class="bound-sources">
            <div class="section-header">
              <h4>已绑定视频源 ({{ filteredBoundSources.length }})</h4>
              <a-space>
                <a-button type="primary" @click="showBindingModal">
                  <PlusOutlined /> 绑定视频源
                </a-button>
                <a-button 
                  type="default"
                  :disabled="selectedSources.length === 0"
                  @click="handleBatchUnbind"
                >
                  批量解绑
                </a-button>
              </a-space>
            </div>

            <div v-if="filteredBoundSources.length === 0" class="empty-sources">
              <a-empty description="暂无绑定的视频源">
                <a-button type="primary" @click="showBindingModal">
                  <PlusOutlined /> 立即绑定
                </a-button>
              </a-empty>
            </div>

            <div v-else class="sources-list">
              <a-list
                :data-source="filteredBoundSources"
                :pagination="false"
              >
                <template #renderItem="{ item }">
                  <a-list-item>
                    <template #actions>
                      <a-button type="text" size="small" danger @click="handleUnbind(item)">
                        <DeleteOutlined /> 解绑
                      </a-button>
                    </template>
                    <a-list-item-meta>
                      <template #avatar>
                        <a-checkbox 
                          :checked="selectedSources.includes(item.id)"
                          @change="toggleSourceSelection(item.id, $event.target.checked)"
                        />
                      </template>
                      <template #title>
                        <div class="source-title">
                          <VideoCameraOutlined />
                          <span>{{ item.source_name }}</span>
                        </div>
                      </template>
                      <template #description>
                        <div class="source-meta">
                          <a-tag color="blue">{{ item.device_name }}</a-tag>
                          <span class="source-url">{{ item.stream_url }}</span>
                        </div>
                      </template>
                    </a-list-item-meta>
                  </a-list-item>
                </template>
              </a-list>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 绑定视频源弹窗 -->
    <SourceBindingModal 
      v-model:visible="bindingModalVisible"
      :node="selectedNode"
      @success="handleBindingSuccess"
    />

    <!-- 节点编辑弹窗 -->
    <NodeEditModal
      v-model:visible="nodeEditVisible"
      :node="editingNode"
      :mode="editMode"
      @success="handleNodeEditSuccess"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { message, Modal } from 'ant-design-vue'
import {
  PlusOutlined,
  EditOutlined,
  DeleteOutlined,
  FolderOutlined,
  FileOutlined,
  FolderOpenOutlined,
  SearchOutlined,
  VideoCameraOutlined,
  ApartmentOutlined
} from '@ant-design/icons-vue'
import SourceBindingModal from '@/components/business/source/SourceBindingModal.vue'
import NodeEditModal from '@/components/business/dialogs/NodeEditDialog.vue'
import businessTreeAPI, { type BusinessTreeNode, type NodeSourceMapping } from '@/api/business-tree'

const router = useRouter()

// 响应式数据
const selectedKeys = ref<string[]>([])
const expandedKeys = ref<string[]>([])
const treeData = ref<BusinessTreeNode[]>([])
const selectedNode = ref<BusinessTreeNode | null>(null)
const searchText = ref('')
const selectedSources = ref<string[]>([])
const saving = ref(false)
const hasUnsavedChanges = ref(false)
const loading = ref(false)

// 弹窗状态
const bindingModalVisible = ref(false)
const nodeEditVisible = ref(false)
const editingNode = ref<BusinessTreeNode | null>(null)
const editMode = ref<'add' | 'edit'>('add')

// 视频源数据
const boundSources = ref<NodeSourceMapping[]>([])

// 计算属性
const hasChildren = computed(() => {
  return selectedNode.value?.children && selectedNode.value.children.length > 0
})

const hasBindings = computed(() => {
  return selectedNode.value?.source_count && selectedNode.value.source_count > 0
})

const filteredBoundSources = computed(() => {
  if (!selectedNode.value?.is_leaf) return []
  
  if (!searchText.value) return boundSources.value
  
  return boundSources.value.filter(source =>
    source.source_name?.toLowerCase().includes(searchText.value.toLowerCase()) ||
    source.device_name?.toLowerCase().includes(searchText.value.toLowerCase())
  )
})

// 数据加载
// 展开所有节点的通用函数
const expandAllNodes = (nodes: BusinessTreeNode[]): string[] => {
  let keys: string[] = []
  nodes.forEach(node => {
    if (!node.is_leaf) { // 只展开非叶子节点
      keys.push(node.id.toString())
    }
    if (node.children && node.children.length > 0) {
      keys = keys.concat(expandAllNodes(node.children))
    }
  })
  return keys
}

const loadTreeData = async () => {
  try {
    loading.value = true
    const tree = await businessTreeAPI.getBusinessTree()
    
    if (tree) {
      treeData.value = [tree]
      
      // 自动展开所有节点
      const newExpandedKeys = expandAllNodes(treeData.value)
      expandedKeys.value = newExpandedKeys
      console.log('展开的节点keys:', newExpandedKeys)
    }
  } catch (error: any) {
    message.error(`加载业务树失败: ${error.message}`)
  } finally {
    loading.value = false
  }
}

const loadNodeSources = async (nodeId: number) => {
  try {
    const sources = await businessTreeAPI.getNodeSources(nodeId)
    // 确保返回的是数组
    boundSources.value = Array.isArray(sources) ? sources : []
  } catch (error: any) {
    console.error('加载视频源失败:', error)
    message.error(`加载视频源失败: ${error.message}`)
    boundSources.value = []
  }
}

// 方法
const handleNodeSelect = async (selectedKeys: string[], { node }: any) => {
  if (!node || !node.dataRef) {
    console.warn('无效的节点数据:', node)
    return
  }
  
  selectedNode.value = node.dataRef
  selectedSources.value = []
  
  // 如果是叶子节点，加载其绑定的视频源
  if (selectedNode.value?.is_leaf && selectedNode.value.id) {
    await loadNodeSources(selectedNode.value.id)
  } else {
    boundSources.value = []
  }
}

const handleAddNode = () => {
  if (!selectedNode.value) {
    message.warning('请先选择父节点')
    return
  }
  
  editingNode.value = selectedNode.value
  editMode.value = 'add'
  nodeEditVisible.value = true
}

const handleEditNode = () => {
  if (!selectedNode.value) {
    message.warning('请先选择要编辑的节点')
    return
  }
  
  editingNode.value = selectedNode.value
  editMode.value = 'edit'
  nodeEditVisible.value = true
}

const handleDeleteNode = () => {
  if (!selectedNode.value) {
    message.warning('请先选择要删除的节点')
    return
  }
  
  if (selectedNode.value.parent_id === null) {
    message.warning('不能删除根节点')
    return
  }
  
  Modal.confirm({
    title: '确认删除',
    content: `确定要删除节点"${selectedNode.value.name}"吗？${hasBindings.value ? '删除后将解除所有绑定关系，' : ''}此操作不可恢复。`,
    okText: '确定',
    okType: 'danger',
    cancelText: '取消',
    async onOk() {
      try {
        await businessTreeAPI.deleteNode(selectedNode.value!.id)
        message.success('删除成功')
        await loadTreeData()
        selectedNode.value = null
      } catch (error: any) {
        message.error(`删除失败: ${error.message}`)
      }
    }
  })
}

const showBindingModal = () => {
  if (!selectedNode.value?.is_leaf) {
    message.warning('只能为叶子节点绑定视频源')
    return
  }
  
  bindingModalVisible.value = true
}

const handleBindingSuccess = async () => {
  message.success('绑定成功')
  
  // 重新加载当前节点的视频源
  if (selectedNode.value?.is_leaf) {
    await loadNodeSources(selectedNode.value.id)
    await loadTreeData() // 更新树数据中的source_count
  }
}

const handleUnbind = (source: NodeSourceMapping) => {
  Modal.confirm({
    title: '确认解绑',
    content: `确定要解绑视频源"${source.source_name}"吗？`,
    okText: '确定',
    okType: 'danger',
    cancelText: '取消',
    async onOk() {
      try {
        await businessTreeAPI.unbindSources(selectedNode.value!.id, {
          mapping_ids: [source.id]
        })
        message.success('解绑成功')
        await loadNodeSources(selectedNode.value!.id)
        await loadTreeData() // 更新树数据中的source_count
      } catch (error: any) {
        message.error(`解绑失败: ${error.message}`)
      }
    }
  })
}

const handleBatchUnbind = () => {
  if (selectedSources.value.length === 0) {
    message.warning('请先选择要解绑的视频源')
    return
  }
  
  Modal.confirm({
    title: '批量解绑',
    content: `确定要解绑选中的 ${selectedSources.value.length} 个视频源吗？`,
    okText: '确定',
    okType: 'danger',
    cancelText: '取消',
    async onOk() {
      try {
        const mappingIds = selectedSources.value.map(sourceId => 
          Number(sourceId)
        )
        
        await businessTreeAPI.unbindSources(selectedNode.value!.id, {
          mapping_ids: mappingIds
        })
        message.success('批量解绑成功')
        selectedSources.value = []
        await loadNodeSources(selectedNode.value!.id)
        await loadTreeData() // 更新树数据中的source_count
      } catch (error: any) {
        message.error(`批量解绑失败: ${error.message}`)
      }
    }
  })
}

const toggleSourceSelection = (sourceId: string, checked: boolean) => {
  if (checked) {
    selectedSources.value.push(sourceId)
  } else {
    selectedSources.value = selectedSources.value.filter(id => id !== sourceId)
  }
}

const handleNodeEditSuccess = async (nodeData: any) => {
  try {
    if (editMode.value === 'add') {
      await businessTreeAPI.createNode({
        parent_id: editingNode.value!.id,
        name: nodeData.name,
        visible_roles: nodeData.visible_roles || ['admin', 'operator', 'viewer']
      })
      message.success('添加成功')
    } else {
      await businessTreeAPI.updateNode(editingNode.value!.id, {
        name: nodeData.name,
        visible_roles: nodeData.visible_roles
      })
      message.success('更新成功')
    }
    
    await loadTreeData()
  } catch (error: any) {
    message.error(`${editMode.value === 'add' ? '添加' : '更新'}失败: ${error.message}`)
  }
}

const handleSave = async () => {
  try {
    saving.value = true
    // 这里可以实现批量保存逻辑
    // 目前我们是实时保存的，所以不需要特殊处理
    message.success('所有更改已保存')
    hasUnsavedChanges.value = false
  } catch (error: any) {
    message.error(`保存失败: ${error.message}`)
  } finally {
    saving.value = false
  }
}

const handleCancel = () => {
  router.back()
}

// 生命周期
onMounted(async () => {
  await loadTreeData()
})

// 监听路由变化提醒用户保存
watch(
  () => hasUnsavedChanges.value,
  (hasChanges) => {
    if (hasChanges) {
      window.addEventListener('beforeunload', (e) => {
        e.preventDefault()
        e.returnValue = '有未保存的更改，确定要离开吗？'
      })
    } else {
      window.removeEventListener('beforeunload', () => {})
    }
  }
)
</script>

<style lang="less" scoped>
@import '@/styles/variables.less';

.business-tree-management {
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: var(--bg-secondary);
  
  // 修复tooltip颜色问题
  :deep(.ant-tooltip) {
    .ant-tooltip-inner {
      color: white !important;
      background: rgba(0, 0, 0, 0.85) !important;
    }
  }
}

.page-header {
  padding: 8px 24px;
  background: #1890ff;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-shrink: 0;
  border-bottom: 1px solid var(--border-light);

  .header-left {
    .title-with-logo {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    
    .page-logo {
      font-size: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 40px;
      height: 40px;
      background: rgba(255, 255, 255, 0.15);
      border-radius: 8px;
      backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .title-content {
      flex: 1;
    }
    
    .page-title {
      margin: 4px 0 2px 0;
      font-size: 18px;
      font-weight: 600;
      color: white;
    }

    .page-description {
      margin: 0;
      color: rgba(255,255,255,0.9);
      font-size: 13px;
    }
  }

  .header-right {
    margin-top: 4px;
    
    
    :deep(.ant-btn) {
      &.ant-btn-primary {
        background: rgba(255,255,255,0.2);
        border-color: rgba(255,255,255,0.4);
        color: white;
        
        &:hover {
          background: rgba(255,255,255,0.3);
          border-color: rgba(255,255,255,0.6);
        }
        
        &:disabled {
          background: rgba(255,255,255,0.1);
          border-color: rgba(255,255,255,0.2);
          opacity: 0.6;
        }
      }
      
      &:not(.ant-btn-primary) {
        color: white;
        background: rgba(255,255,255,0.1);
        border-color: rgba(255,255,255,0.3);
        
        &:hover {
          background: rgba(255,255,255,0.2);
          border-color: rgba(255,255,255,0.5);
          color: white;
        }
      }
    }
  }
}

.main-content {
  flex: 1;
  display: flex;
  min-height: 0;
  padding: 16px;
  gap: 16px;
  background: var(--bg-secondary);
}

.tree-panel {
  width: 30%;
  background: var(--bg-primary);
  border: 1px solid var(--border-base);
  border-radius: 6px;
  box-shadow: var(--shadow-light);
  display: flex;
  flex-direction: column;
  overflow: hidden;

  .panel-header {
    padding: 16px;
    border-bottom: 1px solid var(--border-light);
    background: var(--bg-primary);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-shrink: 0;

    h3 {
      margin: 0;
      font-size: 16px;
      font-weight: 600;
      color: var(--text-primary);
    }
  }

  .panel-content {
    flex: 1;
    padding: 16px;
    overflow: auto;
    background: var(--bg-primary);

    :deep(.ant-tree) {
      .ant-tree-node-content-wrapper {
        height: 36px;
        display: flex;
        align-items: center;
        border-radius: 6px;
        margin-bottom: 2px;
        transition: all 0.2s ease;
        
        &:hover {
          background: var(--bg-hover);
        }
        
        &.ant-tree-node-selected {
          background: rgba(24, 144, 255, 0.1);
          color: var(--color-primary);
          font-weight: 500;
          border: 1px solid rgba(24, 144, 255, 0.3);
          
          .tree-node-title .binding-count {
            background: rgba(24, 144, 255, 0.2);
            color: var(--color-primary);
          }
        }
      }

      .tree-node-title {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;

        .binding-count {
          font-size: 12px;
          color: var(--color-primary);
          font-weight: 600;
          background: var(--color-primary-light);
          padding: 2px 6px;
          border-radius: 10px;
          min-width: 18px;
          text-align: center;
        }
      }
    }
  }
}

.detail-panel {
  flex: 1;
  background: var(--bg-primary);
  border: 1px solid var(--border-base);
  border-radius: 6px;
  box-shadow: var(--shadow-light);
  display: flex;
  flex-direction: column;
  overflow: hidden;

  .empty-state {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 40px 20px;
    
    :deep(.ant-empty) {
      .ant-empty-description {
        color: var(--text-secondary);
      }
    }
  }

  .node-info {
    padding: 24px;
    background: var(--bg-primary);

    h3 {
      margin-bottom: 16px;
      font-size: 18px;
      font-weight: 600;
      color: var(--text-primary);
    }
    
    :deep(.ant-descriptions) {
      .ant-descriptions-item-label {
        color: var(--text-secondary);
      }
      
      .ant-descriptions-item-content {
        color: var(--text-primary);
      }
    }
  }

  .leaf-node-detail {
    flex: 1;
    display: flex;
    flex-direction: column;

    .detail-header {
      padding: 16px 24px;
      border-bottom: 1px solid var(--border-light);
      background: var(--bg-primary);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-shrink: 0;

      h3 {
        margin: 0;
        font-size: 16px;
        font-weight: 600;
        color: var(--text-primary);
      }
    }

    .bound-sources {
      flex: 1;
      padding: 24px;
      display: flex;
      flex-direction: column;
      background: var(--bg-primary);

      .section-header {
        padding-bottom: 16px;
        margin-bottom: 16px;
        border-bottom: 1px solid var(--border-light);
        display: flex;
        justify-content: space-between;
        align-items: center;

        h4 {
          margin: 0;
          font-size: 14px;
          font-weight: 600;
          color: var(--text-primary);
        }
      }

      .empty-sources {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px dashed var(--border-base);
        border-radius: 6px;
        padding: 40px 20px;
        
        :deep(.ant-empty) {
          .ant-empty-description {
            color: var(--text-secondary);
          }
        }
      }

      .sources-list {
        flex: 1;
        overflow: auto;

        :deep(.ant-list-item) {
          border: 1px solid var(--border-light);
          border-radius: 6px;
          margin-bottom: 12px;
          padding: 16px !important;
          background: var(--bg-primary);
          
          &:hover {
            border-color: var(--border-base);
            box-shadow: var(--shadow-light);
          }
        }

        .source-title {
          display: flex;
          align-items: center;
          gap: 8px;

          span {
            font-weight: 500;
            color: var(--text-primary);
          }
          
          .anticon {
            color: var(--color-primary);
          }
        }

        .source-meta {
          display: flex;
          align-items: center;
          gap: 12px;
          margin-top: 4px;

          .source-url {
            font-family: 'Courier New', monospace;
            font-size: 12px;
            color: var(--text-tertiary);
            background: var(--bg-secondary);
            padding: 2px 6px;
            border-radius: 3px;
          }
          
          :deep(.ant-tag) {
            border-radius: 4px;
          }
        }
      }
    }
  }
}
</style>