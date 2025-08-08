<template>
  <div class="device-toolbar">
    <div class="toolbar-left">
      <el-input
        v-model="searchKeyword"
        placeholder="搜索设备名称、地址、SN..."
        prefix-icon="Search"
        clearable
        class="search-input"
        @input="handleSearch"
      />
      
      <el-select 
        v-model="statusFilter" 
        placeholder="状态筛选" 
        clearable
        class="status-filter"
        @change="handleFilter"
      >
        <el-option label="全部状态" value="" />
        <el-option label="在线" value="online" />
        <el-option label="离线" value="offline" />
        <el-option label="错误" value="error" />
      </el-select>

      <el-select 
        v-model="typeFilter" 
        placeholder="设备类型" 
        clearable
        class="type-filter"
        @change="handleFilter"
      >
        <el-option label="全部类型" value="" />
        <el-option label="边缘盒子" value="edge_box" />
        <el-option label="摄像服务器" value="camera_server" />
        <el-option label="AI盒子" value="ai_box" />
      </el-select>
    </div>
    
    <div class="toolbar-right">
      <el-button @click="$emit('refresh')" :loading="refreshing">
        <el-icon><Refresh /></el-icon>
        刷新
      </el-button>
      
      <el-button 
        type="warning" 
        :disabled="selectedCount === 0"
        @click="$emit('batchSync')"
        :loading="batchSyncing"
      >
        <el-icon><Download /></el-icon>
        批量同步 ({{ selectedCount }})
      </el-button>
      
      <el-button 
        type="danger" 
        :disabled="selectedCount === 0"
        @click="$emit('batchDelete')"
      >
        <el-icon><Delete /></el-icon>
        批量删除 ({{ selectedCount }})
      </el-button>
      
      <el-button type="success" @click="$emit('importDevices')">
        <el-icon><Upload /></el-icon>
        导入设备
      </el-button>
      
      <el-button type="primary" @click="$emit('addDevice')">
        <el-icon><Plus /></el-icon>
        添加设备
      </el-button>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { Plus, Refresh, Download, Delete, Upload } from '@element-plus/icons-vue'

// Props
const props = defineProps({
  refreshing: {
    type: Boolean,
    default: false
  },
  batchSyncing: {
    type: Boolean,
    default: false
  },
  selectedCount: {
    type: Number,
    default: 0
  }
})

// Emits
const emit = defineEmits(['search', 'filter', 'refresh', 'batchSync', 'batchDelete', 'importDevices', 'addDevice'])

// 响应式数据
const searchKeyword = ref('')
const statusFilter = ref('')
const typeFilter = ref('')

// 方法
const handleSearch = () => {
  emit('search', searchKeyword.value)
}

const handleFilter = () => {
  emit('filter', {
    status: statusFilter.value,
    type: typeFilter.value
  })
}

// 监听过滤条件变化
watch([statusFilter, typeFilter], () => {
  handleFilter()
}, { deep: true })
</script>

<style scoped>
.device-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--spacing-4);
  background: var(--color-bg-secondary);
  border-bottom: 1px solid var(--color-border-primary);
  flex-shrink: 0;
}

.toolbar-left {
  display: flex;
  align-items: center;
  gap: var(--spacing-3);
}

.toolbar-right {
  display: flex;
  align-items: center;
  gap: var(--spacing-3);
}

.search-input {
  width: 300px;
}

.status-filter {
  width: 130px;
}

.type-filter {
  width: 140px;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .device-toolbar {
    flex-direction: column;
    gap: var(--spacing-3);
    align-items: stretch;
  }
  
  .toolbar-left, 
  .toolbar-right {
    justify-content: space-between;
  }
  
  .search-input {
    width: 100%;
  }
}
</style>