/**
 * 设备管理 API
 */

import { request } from './request'

export interface Device {
  id: number
  name?: string
  device_type?: string
  api_base_url: string
  status: 'online' | 'offline' | 'error'
  business_node_id?: string
  device_sn?: string
  version?: string
  register_status?: string
  system_update?: string
  system_time?: string
  network_setting?: string
  last_sync_at?: string
  last_heartbeat?: string
  sync_error?: string
  created_at?: string
  updated_at?: string
}

export interface DeviceCreate {
  name?: string
  api_base_url: string
  username: string
  password: string
}

export interface DeviceListResponse {
  success: boolean
  data: {
    items: Device[]
    total: number
    page: number
    page_size: number
  }
}

export interface DeviceResponse {
  success: boolean
  data: Device
}

export interface DeviceStats {
  total: number
  online: number
  offline: number
  error: number
}

export interface DeviceSyncResult {
  success: boolean
  message: string
  data?: any
}

export interface DeviceBatchSyncResponse {
  success: boolean
  message: string
  results: Array<{
    device_id: number
    success: boolean
    message: string
  }>
}

export interface DeviceBatchImport {
  devices: DeviceCreate[]
}

export interface DeviceBatchImportResponse {
  success: boolean
  message: string
  imported_count: number
  failed_count: number
  failed_devices: Array<{
    device: DeviceCreate
    error: string
  }>
}

export interface DeviceSource {
  id: number
  name: string
  source_type: string
  url: string
  status: string
  resolution?: string
  thumbnail_url?: string
  description?: string
}

// 获取设备列表
export const getDevices = (params: {
  page?: number
  page_size?: number
  status?: string
  device_type?: string
  search?: string
} = {}) => {
  return request.get<DeviceListResponse>('/devices/', { params })
}

// 获取设备详情
export const getDevice = (deviceId: number) => {
  return request.get<DeviceResponse>(`/devices/${deviceId}`)
}

// 添加设备
export const addDevice = (data: DeviceCreate) => {
  return request.post<DeviceResponse>('/devices/', data)
}

// 更新设备
export const updateDevice = (deviceId: number, data: DeviceCreate) => {
  return request.put<DeviceResponse>(`/devices/${deviceId}`, data)
}

// 删除设备
export const deleteDevice = (deviceId: number) => {
  return request.delete(`/devices/${deviceId}`)
}

// 同步设备信息
export const syncDevice = (deviceId: number) => {
  return request.post<DeviceSyncResult>(`/devices/${deviceId}/sync`)
}

// 批量同步设备
export const batchSyncDevices = (deviceIds: number[]) => {
  return request.post<DeviceBatchSyncResponse>('/devices/batch-sync', { device_ids: deviceIds })
}

// 批量删除设备
export const batchDeleteDevices = (deviceIds: number[]) => {
  return request.delete('/devices/batch-delete', { data: { device_ids: deviceIds } })
}

// 批量导入设备
export const batchImportDevices = (devices: DeviceCreate[]) => {
  return request.post<DeviceBatchImportResponse>('/devices/batch-import', { devices })
}

// 获取设备统计
export const getDeviceStats = () => {
  return request.get<DeviceStats>('/devices/stats/overview')
}

// 获取设备视频源
export const getDeviceSources = (deviceId: number, sourceType?: string) => {
  const params = sourceType ? { source_type: sourceType } : {}
  return request.get<{
    success: boolean
    data: DeviceSource[]
    total: number
  }>(`/devices/${deviceId}/sources`, { params })
}