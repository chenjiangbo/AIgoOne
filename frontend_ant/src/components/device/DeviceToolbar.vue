<template>
  <div class="device-toolbar">
    <div class="toolbar-left">
      <!-- 搜索框 -->
      <a-input
        v-model:value="searchValue"
        placeholder="搜索设备名称、地址或序列号"
        allow-clear
        class="search-input"
        @change="handleSearch"
      >
        <template #prefix>
          <SearchOutlined />
        </template>
      </a-input>

      <!-- 筛选器 -->
      <a-space>
        <a-select
          v-model:value="statusFilter"
          placeholder="状态筛选"
          allow-clear
          style="width: 120px"
          @change="handleFilter"
        >
          <a-select-option value="online">在线</a-select-option>
          <a-select-option value="offline">离线</a-select-option>
          <a-select-option value="error">验证失败</a-select-option>
        </a-select>

        <a-select
          v-model:value="typeFilter"
          placeholder="类型筛选"
          allow-clear
          style="width: 120px"
          @change="handleFilter"
        >
          <a-select-option value="edge">边缘设备</a-select-option>
          <a-select-option value="server">算力服务器</a-select-option>
        </a-select>
      </a-space>
    </div>

    <div class="toolbar-right">
      <a-space>
        <!-- 刷新按钮 -->
        <a-button
          type="text"
          :loading="refreshing"
          @click="$emit('refresh')"
        >
          <template #icon>
            <ReloadOutlined />
          </template>
          刷新
        </a-button>

        <!-- 批量操作按钮 -->
        <template v-if="selectedCount > 0">
          <a-button
            type="primary"
            ghost
            :loading="batchSyncing"
            @click="$emit('batch-sync')"
          >
            <template #icon>
              <SyncOutlined />
            </template>
            批量同步 ({{ selectedCount }})
          </a-button>

          <a-button
            danger
            @click="$emit('batch-delete')"
          >
            <template #icon>
              <DeleteOutlined />
            </template>
            批量删除
          </a-button>
        </template>

        <!-- 导入设备按钮 -->
        <a-button
          type="default"
          @click="$emit('import-devices')"
        >
          <template #icon>
            <UploadOutlined />
          </template>
          导入设备
        </a-button>

        <!-- 添加设备按钮 -->
        <a-button
          type="primary"
          @click="$emit('add-device')"
        >
          <template #icon>
            <PlusOutlined />
          </template>
          添加设备
        </a-button>
      </a-space>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import {
  SearchOutlined,
  ReloadOutlined,
  SyncOutlined,
  DeleteOutlined,
  UploadOutlined,
  PlusOutlined
} from '@ant-design/icons-vue'

interface Props {
  refreshing?: boolean
  batchSyncing?: boolean
  selectedCount?: number
}

const props = withDefaults(defineProps<Props>(), {
  refreshing: false,
  batchSyncing: false,
  selectedCount: 0
})

const emit = defineEmits<{
  search: [keyword: string]
  filter: [filters: { status?: string; type?: string }]
  refresh: []
  'batch-sync': []
  'batch-delete': []
  'import-devices': []
  'add-device': []
}>()

const searchValue = ref('')
const statusFilter = ref<string | undefined>()
const typeFilter = ref<string | undefined>()

const handleSearch = () => {
  emit('search', searchValue.value)
}

const handleFilter = () => {
  emit('filter', {
    status: statusFilter.value,
    type: typeFilter.value
  })
}

// 监听筛选条件变化
watch([statusFilter, typeFilter], () => {
  handleFilter()
})
</script>

<style scoped>
.device-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  background: var(--bg-primary);
  border-bottom: 1px solid var(--border-color);
}

.toolbar-left {
  display: flex;
  align-items: center;
  gap: 16px;
  flex: 1;
}

.search-input {
  width: 280px;
}

.toolbar-right {
  flex-shrink: 0;
}

html.dark .device-toolbar {
  background: var(--bg-secondary);
  border-bottom-color: var(--border-color-dark);
}
</style>