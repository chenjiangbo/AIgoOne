import { request } from './request'

export interface BusinessTreeNode {
  id: number
  name: string
  parent_id?: number
  depth: number
  is_leaf: boolean
  path: string
  visible_roles: string[]
  created_at?: string
  updated_at?: string
  children?: BusinessTreeNode[]
  source_count?: number
}

export interface NodeSourceMapping {
  id: number
  node_id: number
  device_id: number
  source_id: string
  source_type?: string
  source_name?: string
  status: 'normal' | 'invalid'
  last_sync_at?: string
  created_at?: string
  device_name?: string
  device_url?: string
}

export interface CreateNodeRequest {
  parent_id: number
  name: string
  visible_roles?: string[]
}

export interface UpdateNodeRequest {
  name?: string
  visible_roles?: string[]
}

export interface MoveNodeRequest {
  new_parent_id: number
}

export interface BindSourcesRequest {
  sources: Array<{
    device_id: number
    source_id: string
    source_type?: string
    source_name?: string
  }>
}

export interface UnbindSourcesRequest {
  mapping_ids: number[]
}

export interface BatchSaveRequest {
  deleted?: number[]
  added?: Array<{
    parent_id: number
    name: string
    visible_roles?: string[]
  }>
  updated?: Array<{
    id: number
    name?: string
    visible_roles?: string[]
  }>
  moved?: Array<{
    node_id: number
    new_parent_id: number
  }>
  bindings?: Array<{
    action: 'bind' | 'unbind'
    node_id: number
    sources?: Array<{
      device_id: number
      source_id: string
      source_type?: string
      source_name?: string
    }>
    mapping_ids?: number[]
  }>
}

class BusinessTreeAPI {
  // 获取完整业务树
  async getBusinessTree(): Promise<BusinessTreeNode> {
    const response = await request.get('/business-tree')
    return response.data.data  // 注意这里需要取.data.data，因为后端返回格式是 {success: true, data: {...}}
  }

  // 获取节点详情
  async getNodeDetail(nodeId: number): Promise<BusinessTreeNode> {
    const response = await request.get(`/business-tree/nodes/${nodeId}`)
    return response.data
  }

  // 创建节点
  async createNode(data: CreateNodeRequest): Promise<BusinessTreeNode> {
    const response = await request.post('/business-tree/nodes', data)
    return response.data
  }

  // 更新节点
  async updateNode(nodeId: number, data: UpdateNodeRequest): Promise<BusinessTreeNode> {
    const response = await request.put(`/business-tree/nodes/${nodeId}`, data)
    return response.data
  }

  // 删除节点
  async deleteNode(nodeId: number): Promise<void> {
    await request.delete(`/business-tree/nodes/${nodeId}`)
  }

  // 移动节点
  async moveNode(nodeId: number, data: MoveNodeRequest): Promise<BusinessTreeNode> {
    const response = await request.post(`/business-tree/nodes/${nodeId}/move`, data)
    return response.data
  }

  // 获取节点绑定的视频源
  async getNodeSources(nodeId: number): Promise<NodeSourceMapping[]> {
    const response = await request.get(`/business-tree/nodes/${nodeId}/sources`)
    return response.data
  }

  // 绑定视频源
  async bindSources(nodeId: number, data: BindSourcesRequest): Promise<NodeSourceMapping[]> {
    const response = await request.post(`/business-tree/nodes/${nodeId}/bind`, data)
    return response.data
  }

  // 解绑视频源
  async unbindSources(nodeId: number, data: UnbindSourcesRequest): Promise<void> {
    await request.delete(`/business-tree/nodes/${nodeId}/unbind`, { data })
  }

  // 同步视频源状态
  async syncSourceStatus(nodeId: number): Promise<NodeSourceMapping[]> {
    const response = await request.post(`/business-tree/nodes/${nodeId}/sync`)
    return response.data
  }

  // 批量保存更改
  async batchSave(data: BatchSaveRequest): Promise<any> {
    const response = await request.post('/business-tree/batch-save', data)
    return response.data
  }

  // 验证树结构
  async validateTree(): Promise<{
    valid: boolean
    message: string
    issues?: string[]
  }> {
    const response = await request.get('/business-tree/validate')
    return response.data
  }
}

export default new BusinessTreeAPI()