<template>
  <a-modal
    :open="visible"
    title="绑定视频源"
    :width="800"
    :confirm-loading="loading"
    @ok="handleConfirm"
    @cancel="handleCancel"
  >
    <div class="binding-modal-content">
      <!-- 设备选择 -->
      <div class="device-selection">
        <label class="form-label">选择设备：</label>
        <a-select
          v-model:value="selectedDeviceId"
          placeholder="请选择设备"
          style="width: 100%;"
          show-search
          :filter-option="filterDeviceOption"
          :loading="devicesLoading"
          @change="handleDeviceChange"
        >
          <a-select-option
            v-for="device in devices"
            :key="device.id"
            :value="device.id"
          >
            <div class="device-option">
              <span class="device-name">{{ device.name }}</span>
              <span class="device-url">({{ device.api_base_url }})</span>
            </div>
          </a-select-option>
        </a-select>
      </div>

      <!-- 视频源列表 -->
      <div class="source-selection" v-if="selectedDeviceId">
        <label class="form-label">可用视频源：</label>
        <div class="source-list-container">
          <a-spin :spinning="sourcesLoading">
            <div v-if="availableSources.length === 0" class="empty-sources">
              <a-empty description="该设备暂无可用视频源" />
            </div>
            <div v-else class="source-list">
              <div
                v-for="source in availableSources"
                :key="source.id"
                class="source-item"
                :class="{ 
                  'selected': selectedSources.includes(source.id),
                  'already-bound': source.isAlreadyBound
                }"
                @click="toggleSource(source)"
              >
                <div class="source-item-left">
                  <a-checkbox
                    :checked="selectedSources.includes(source.id)"
                    @change="(e) => toggleSource(source, e.target.checked)"
                    @click.stop
                  />
                  <div class="source-info">
                    <div class="source-name">
                      <VideoCameraOutlined />
                      <span>{{ source.name }}</span>
                      <a-tag v-if="source.isAlreadyBound" color="orange" size="small">
                        已绑定
                      </a-tag>
                      <a-tag v-else color="green" size="small">
                        新
                      </a-tag>
                    </div>
                    <div class="source-url">{{ source.stream_url }}</div>
                  </div>
                </div>
                <div class="source-item-right">
                  <a-tag :color="source.status === 'online' ? 'green' : 'red'">
                    {{ source.status === 'online' ? '在线' : '离线' }}
                  </a-tag>
                </div>
              </div>
            </div>
          </a-spin>
        </div>
      </div>

      <!-- 选择总结 -->
      <div v-if="selectedSources.length > 0" class="selection-summary">
        <a-alert
          :message="`已选择 ${selectedSources.length} 个视频源`"
          :description="getSelectionDescription()"
          type="info"
          show-icon
        />
      </div>
    </div>
  </a-modal>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { message, Modal } from 'ant-design-vue'
import { VideoCameraOutlined } from '@ant-design/icons-vue'
import businessTreeAPI from '@/api/business-tree'
import { getDevices, getDeviceSources } from '@/api/device'

interface Props {
  visible: boolean
  node?: any
}

interface Emits {
  (e: 'update:visible', value: boolean): void
  (e: 'success'): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

// 响应式数据
const selectedDeviceId = ref<string>()
const selectedSources = ref<string[]>([])
const loading = ref(false)
const devicesLoading = ref(false)
const sourcesLoading = ref(false)

// 设备数据
const devices = ref<any[]>([])

// 视频源数据
const availableSources = ref<any[]>([])
const existingBindings = ref<string[]>([])

// 计算属性
const hasAlreadyBoundSources = computed(() => {
  return selectedSources.value.some(sourceId => {
    const source = availableSources.value.find(s => s.id === sourceId)
    return source?.isAlreadyBound
  })
})

// 方法
const filterDeviceOption = (input: string, option: any) => {
  const device = devices.value.find(d => d.id === option.value)
  if (!device) return false
  
  return (
    device.alias.toLowerCase().includes(input.toLowerCase()) ||
    device.url.toLowerCase().includes(input.toLowerCase())
  )
}

const loadDevices = async () => {
  try {
    devicesLoading.value = true
    const response = await getDevices()
    devices.value = response.data?.items || []
  } catch (error: any) {
    message.error(`加载设备列表失败: ${error.message}`)
  } finally {
    devicesLoading.value = false
  }
}

const handleDeviceChange = async (deviceId: string) => {
  selectedSources.value = []
  if (!deviceId) {
    availableSources.value = []
    return
  }

  try {
    sourcesLoading.value = true
    const response = await getDeviceSources(parseInt(deviceId))
    const sources = response.data || []
    
    // 标记已绑定的视频源
    availableSources.value = sources.map((source: any) => ({
      ...source,
      stream_url: source.url || source.stream_url,
      isAlreadyBound: existingBindings.value.includes(`${deviceId}_${source.id}`)
    }))
  } catch (error: any) {
    message.error(`获取视频源列表失败: ${error.message}`)
    availableSources.value = []
  } finally {
    sourcesLoading.value = false
  }
}

const toggleSource = (source: any, checked?: boolean) => {
  const isChecked = checked !== undefined ? checked : !selectedSources.value.includes(source.id)
  
  if (isChecked) {
    if (!selectedSources.value.includes(source.id)) {
      selectedSources.value.push(source.id)
    }
  } else {
    selectedSources.value = selectedSources.value.filter(id => id !== source.id)
  }
}

const getSelectionDescription = () => {
  const newSources = selectedSources.value.filter(sourceId => {
    const source = availableSources.value.find(s => s.id === sourceId)
    return !source?.isAlreadyBound
  }).length

  const boundSources = selectedSources.value.length - newSources

  let desc = `新绑定 ${newSources} 个视频源`
  if (boundSources > 0) {
    desc += `，重复绑定 ${boundSources} 个视频源`
  }
  
  return desc
}

const handleConfirm = async () => {
  if (!selectedDeviceId.value) {
    message.error('请选择设备')
    return
  }

  if (selectedSources.value.length === 0) {
    message.error('请至少选择一个视频源')
    return
  }

  if (!props.node?.id) {
    message.error('节点信息错误')
    return
  }

  // 如果有重复绑定的视频源，给出警告
  if (hasAlreadyBoundSources.value) {
    const shouldContinue = await new Promise((resolve) => {
      Modal.confirm({
        title: '重复绑定确认',
        content: '您选择的部分视频源已绑定到其他业务节点，确认继续吗？',
        okText: '确认',
        cancelText: '取消',
        onOk: () => resolve(true),
        onCancel: () => resolve(false)
      })
    })

    if (!shouldContinue) return
  }

  try {
    loading.value = true
    
    // 构造绑定数据
    const sources = selectedSources.value.map(sourceId => {
      const source = availableSources.value.find(s => s.id === sourceId)
      return {
        device_id: parseInt(selectedDeviceId.value!),
        source_id: sourceId,
        source_type: source?.source_type || 'camera',
        source_name: source?.name || ''
      }
    })
    
    await businessTreeAPI.bindSources(props.node.id, { sources })
    emit('success')
    handleCancel()
  } catch (error: any) {
    message.error(`绑定失败: ${error.message}`)
  } finally {
    loading.value = false
  }
}

const handleCancel = () => {
  emit('update:visible', false)
  // 重置状态
  selectedDeviceId.value = undefined
  selectedSources.value = []
  availableSources.value = []
}

// 监听弹窗显示状态
watch(() => props.visible, (visible) => {
  if (visible) {
    // 弹窗打开时的初始化逻辑
    loadDevices()
    // TODO: 加载已有绑定信息用于标记重复绑定
  } else {
    // 弹窗关闭时的清理逻辑
    selectedDeviceId.value = undefined
    selectedSources.value = []
    availableSources.value = []
  }
})
</script>

<style lang="less" scoped>
@import '@/styles/variables.less';

.binding-modal-content {
  .form-label {
    display: block;
    margin-bottom: 8px;
    font-weight: 500;
    color: var(--text-primary);
  }

  .device-selection {
    margin-bottom: 24px;

    .device-option {
      display: flex;
      align-items: center;
      justify-content: space-between;

      .device-name {
        font-weight: 500;
      }

      .device-url {
        color: var(--text-secondary);
        font-size: 12px;
      }
    }
  }

  .source-selection {
    margin-bottom: 24px;

    .source-list-container {
      border: 1px solid var(--border-light);
      border-radius: 6px;
      max-height: 300px;
      overflow-y: auto;

      .empty-sources {
        padding: 40px 20px;
        display: flex;
        align-items: center;
        justify-content: center;
      }

      .source-list {
        .source-item {
          padding: 12px 16px;
          border-bottom: 1px solid var(--border-light);
          cursor: pointer;
          transition: all 0.2s ease;
          display: flex;
          align-items: center;
          justify-content: space-between;

          &:last-child {
            border-bottom: none;
          }

          &:hover {
            background: var(--bg-hover);
          }

          &.selected {
            background: var(--color-primary-light);
          }

          &.already-bound {
            background: #fff7e6;
            
            &.selected {
              background: #ffe7ba;
            }
          }

          .source-item-left {
            display: flex;
            align-items: center;
            gap: 12px;
            flex: 1;

            .source-info {
              flex: 1;

              .source-name {
                display: flex;
                align-items: center;
                gap: 8px;
                margin-bottom: 4px;
                font-weight: 500;
                color: var(--text-primary);
              }

              .source-url {
                font-size: 12px;
                color: var(--text-secondary);
                font-family: 'Courier New', monospace;
              }
            }
          }

          .source-item-right {
            flex-shrink: 0;
          }
        }
      }
    }
  }

  .selection-summary {
    :deep(.ant-alert) {
      border-radius: 6px;
    }
  }
}
</style>