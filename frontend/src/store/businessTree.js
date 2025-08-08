import { defineStore } from 'pinia'
import { ElMessage } from 'element-plus'
import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000/api'

// 获取token
const getToken = () => {
  return localStorage.getItem('token')
}

// 创建axios实例
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器添加token
api.interceptors.request.use(config => {
  const token = getToken()
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export const useBusinessTreeStore = defineStore('businessTree', {
  state: () => ({
    // 树数据
    treeData: [],
    originalTreeData: null,  // 原始数据，用于比较变化
    
    // 选中状态
    selectedNode: null,
    expandedNodes: [],
    
    // 视频源绑定
    nodeSourceMappings: {},  // { nodeId: [sources] }
    
    // 编辑状态
    pendingChanges: {
      added: [],      // 新增节点
      updated: [],    // 修改节点
      deleted: [],    // 删除节点
      moved: [],      // 移动节点
      bindings: []    // 绑定变更
    },
    
    // UI状态
    loading: false,
    saving: false,
    hasUnsavedChanges: false
  }),
  
  getters: {
    // 获取可拖拽节点（只有叶子节点可拖拽）
    draggableNodes: (state) => {
      const getDraggableNodes = (nodes) => {
        let result = []
        for (const node of nodes) {
          if (node.is_leaf) {
            result.push(node.id)
          }
          if (node.children && node.children.length > 0) {
            result = result.concat(getDraggableNodes(node.children))
          }
        }
        return result
      }
      return getDraggableNodes(state.treeData)
    },
    
    // 获取所有叶子节点
    leafNodes: (state) => {
      const getLeafNodes = (nodes) => {
        let result = []
        for (const node of nodes) {
          if (node.is_leaf) {
            result.push(node)
          }
          if (node.children && node.children.length > 0) {
            result = result.concat(getLeafNodes(node.children))
          }
        }
        return result
      }
      return getLeafNodes(state.treeData)
    },
    
    // 检查是否有未保存的更改
    hasChanges: (state) => {
      const changes = state.pendingChanges
      return changes.added.length > 0 || 
             changes.updated.length > 0 || 
             changes.deleted.length > 0 || 
             changes.moved.length > 0 || 
             changes.bindings.length > 0
    }
  },
  
  actions: {
    // 加载树数据
    async loadTree() {
      this.loading = true
      try {
        const response = await api.get('/business-tree')
        if (response.data.success) {
          // 将树数据转换为数组（根节点作为第一个元素）
          this.treeData = response.data.data ? [response.data.data] : []
          this.originalTreeData = JSON.parse(JSON.stringify(this.treeData))
          this.clearPendingChanges()
        }
      } catch (error) {
        console.error('加载业务树失败:', error)
        ElMessage.error('加载业务树失败: ' + (error.response?.data?.message || error.message))
      } finally {
        this.loading = false
      }
    },
    
    // 创建节点
    async createNode(parentId, name, visibleRoles = null) {
      try {
        const tempNode = {
          id: `temp_${Date.now()}`,
          name,
          parent_id: parentId,
          is_leaf: false,  // 新建节点默认为非叶子，可以继续添加子节点
          children: [],
          visible_roles: visibleRoles || ['admin', 'operator', 'viewer']
        }
        
        // 添加到待保存列表
        this.pendingChanges.added.push({
          parent_id: parentId,
          name,
          visible_roles: tempNode.visible_roles
        })
        
        // 更新本地树数据
        this.addNodeToTree(parentId, tempNode)
        this.hasUnsavedChanges = true
        
        return tempNode
      } catch (error) {
        ElMessage.error('创建节点失败: ' + error.message)
        throw error
      }
    },
    
    // 更新节点
    updateNode(nodeId, updates) {
      const node = this.findNodeById(nodeId)
      if (!node) {
        ElMessage.error('节点不存在')
        return
      }
      
      // 更新本地数据
      Object.assign(node, updates)
      
      // 添加到待更新列表
      const existingUpdate = this.pendingChanges.updated.find(n => n.id === nodeId)
      if (existingUpdate) {
        Object.assign(existingUpdate, updates)
      } else {
        this.pendingChanges.updated.push({
          id: nodeId,
          ...updates
        })
      }
      
      this.hasUnsavedChanges = true
    },
    
    // 删除节点
    deleteNode(nodeId) {
      const node = this.findNodeById(nodeId)
      if (!node) {
        ElMessage.error('节点不存在')
        return
      }
      
      if (node.children && node.children.length > 0) {
        ElMessage.error('请先删除所有子节点')
        return
      }
      
      // 如果是临时节点，从added列表中移除
      if (String(nodeId).startsWith('temp_')) {
        const index = this.pendingChanges.added.findIndex(n => n.id === nodeId)
        if (index !== -1) {
          this.pendingChanges.added.splice(index, 1)
        }
      } else {
        // 添加到待删除列表
        this.pendingChanges.deleted.push(nodeId)
      }
      
      // 从树中移除节点
      this.removeNodeFromTree(nodeId)
      this.hasUnsavedChanges = true
    },
    
    // 移动节点
    moveNode(nodeId, newParentId) {
      const node = this.findNodeById(nodeId)
      const newParent = this.findNodeById(newParentId)
      
      if (!node || !newParent) {
        ElMessage.error('节点不存在')
        return
      }
      
      if (!node.is_leaf) {
        ElMessage.error('只能移动叶子节点')
        return
      }
      
      if (newParent.is_leaf) {
        ElMessage.error('不能移动到叶子节点下')
        return
      }
      
      // 记录移动操作
      this.pendingChanges.moved.push({
        node_id: nodeId,
        new_parent_id: newParentId
      })
      
      // 更新本地树结构
      this.removeNodeFromTree(nodeId)
      node.parent_id = newParentId
      this.addNodeToTree(newParentId, node)
      
      this.hasUnsavedChanges = true
    },
    
    // 获取节点的视频源
    async loadNodeSources(nodeId) {
      try {
        const response = await api.get(`/business-tree/nodes/${nodeId}/sources`)
        if (response.data.success) {
          this.nodeSourceMappings[nodeId] = response.data.data
          return response.data.data
        }
      } catch (error) {
        console.error('加载视频源失败:', error)
        ElMessage.error('加载视频源失败')
        return []
      }
    },
    
    // 绑定视频源
    bindSources(nodeId, sources) {
      // 添加到待保存的绑定变更
      this.pendingChanges.bindings.push({
        action: 'bind',
        node_id: nodeId,
        sources
      })
      
      // 更新本地映射
      if (!this.nodeSourceMappings[nodeId]) {
        this.nodeSourceMappings[nodeId] = []
      }
      this.nodeSourceMappings[nodeId].push(...sources)
      
      this.hasUnsavedChanges = true
    },
    
    // 解绑视频源
    unbindSources(nodeId, mappingIds) {
      // 添加到待保存的绑定变更
      this.pendingChanges.bindings.push({
        action: 'unbind',
        node_id: nodeId,
        mapping_ids: mappingIds
      })
      
      // 更新本地映射
      if (this.nodeSourceMappings[nodeId]) {
        this.nodeSourceMappings[nodeId] = this.nodeSourceMappings[nodeId].filter(
          source => !mappingIds.includes(source.id)
        )
      }
      
      this.hasUnsavedChanges = true
    },
    
    // 批量保存所有更改
    async saveChanges() {
      if (!this.hasChanges) {
        ElMessage.info('没有需要保存的更改')
        return
      }
      
      this.saving = true
      try {
        const response = await api.post('/business-tree/batch-save', this.pendingChanges)
        if (response.data.success) {
          ElMessage.success('保存成功')
          // 重新加载树数据
          await this.loadTree()
          this.clearPendingChanges()
          this.hasUnsavedChanges = false
        }
      } catch (error) {
        console.error('保存失败:', error)
        ElMessage.error('保存失败: ' + (error.response?.data?.message || error.message))
      } finally {
        this.saving = false
      }
    },
    
    // 清空待保存的更改
    clearPendingChanges() {
      this.pendingChanges = {
        added: [],
        updated: [],
        deleted: [],
        moved: [],
        bindings: []
      }
      this.hasUnsavedChanges = false
    },
    
    // 辅助方法：在树中查找节点
    findNodeById(nodeId, nodes = this.treeData) {
      for (const node of nodes) {
        if (node.id === nodeId) {
          return node
        }
        if (node.children && node.children.length > 0) {
          const found = this.findNodeById(nodeId, node.children)
          if (found) return found
        }
      }
      return null
    },
    
    // 辅助方法：向树中添加节点
    addNodeToTree(parentId, newNode) {
      const parent = this.findNodeById(parentId)
      if (parent) {
        if (!parent.children) {
          parent.children = []
        }
        parent.children.push(newNode)
        // 父节点不再是叶子节点
        if (parent.is_leaf) {
          parent.is_leaf = false
        }
      }
    },
    
    // 辅助方法：从树中移除节点
    removeNodeFromTree(nodeId, nodes = this.treeData) {
      for (let i = 0; i < nodes.length; i++) {
        if (nodes[i].id === nodeId) {
          nodes.splice(i, 1)
          return true
        }
        if (nodes[i].children && nodes[i].children.length > 0) {
          if (this.removeNodeFromTree(nodeId, nodes[i].children)) {
            // 如果子节点被删除且没有其他子节点，更新为叶子节点
            if (nodes[i].children.length === 0) {
              nodes[i].is_leaf = true
            }
            return true
          }
        }
      }
      return false
    },
    
    // 设置选中的节点
    setSelectedNode(node) {
      this.selectedNode = node
      if (node && node.is_leaf) {
        // 如果是叶子节点，加载其视频源
        this.loadNodeSources(node.id)
      }
    }
  }
})