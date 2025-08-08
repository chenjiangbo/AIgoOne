<template>
  <BaseDialog
    v-model:visible="dialogVisible"
    :title="title"
    :width="'400px'"
    :show-maximize="false"
    :show-default-footer="false"
    :close-on-click-modal="false"
    :close-on-press-escape="false"
    class="node-edit-dialog"
  >
    <div class="dialog-content p-4">
      <div class="mb-4">
        <label class="block text-sm font-medium text-gray-700 mb-2">
          节点名称
        </label>
        <el-input
          ref="nameInput"
          v-model="nodeName"
          placeholder="请输入节点名称"
          :maxlength="64"
          show-word-limit
          clearable
          @keyup.enter="handleConfirm"
        />
        <div v-if="errorMessage" class="text-red-500 text-sm mt-1">
          {{ errorMessage }}
        </div>
      </div>
    </div>
    
    <template #footer>
      <div class="flex justify-end gap-3 p-4">
        <el-button @click="handleCancel">取消</el-button>
        <el-button 
          type="primary" 
          @click="handleConfirm"
          :disabled="!isValid"
        >
          确定
        </el-button>
      </div>
    </template>
  </BaseDialog>
</template>

<script setup>
import { ref, computed, watch, nextTick } from 'vue'
import BaseDialog from '@/components/ui/BaseDialog.vue'

const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  },
  title: {
    type: String,
    default: '编辑节点'
  },
  defaultValue: {
    type: String,
    default: ''
  }
})

const emit = defineEmits(['update:visible', 'confirm', 'cancel'])

// 组件状态
const nodeName = ref('')
const errorMessage = ref('')
const nameInput = ref(null)

// 对话框显示状态
const dialogVisible = computed({
  get: () => props.visible,
  set: (val) => emit('update:visible', val)
})

// 验证节点名称
const isValid = computed(() => {
  const name = nodeName.value.trim()
  return name.length >= 1 && name.length <= 64
})

// 监听显示状态变化
watch(dialogVisible, (val) => {
  if (val) {
    // 打开对话框时重置状态
    nodeName.value = props.defaultValue
    errorMessage.value = ''
    
    // 聚焦输入框
    nextTick(() => {
      if (nameInput.value) {
        nameInput.value.focus()
        nameInput.value.select()
      }
    })
  }
})

// 监听节点名称变化
watch(nodeName, (val) => {
  const trimmed = val.trim()
  if (trimmed.length === 0) {
    errorMessage.value = '节点名称不能为空'
  } else if (trimmed.length > 64) {
    errorMessage.value = '节点名称长度不能超过64个字符'
  } else {
    errorMessage.value = ''
  }
})

// 确认操作
const handleConfirm = () => {
  const name = nodeName.value.trim()
  
  if (!isValid.value) {
    if (name.length === 0) {
      errorMessage.value = '节点名称不能为空'
    } else if (name.length > 64) {
      errorMessage.value = '节点名称长度不能超过64个字符'
    }
    return
  }
  
  emit('confirm', name)
  dialogVisible.value = false
}

// 取消操作
const handleCancel = () => {
  emit('cancel')
  dialogVisible.value = false
}
</script>

<style scoped>
.node-edit-dialog {
  --dialog-padding: 0;
}

:deep(.el-dialog__body) {
  padding: 0 !important;
}

.dialog-content {
  min-height: 80px;
}

:deep(.el-input__wrapper) {
  border-radius: 6px;
}

:deep(.el-input__wrapper:hover) {
  border-color: var(--el-color-primary);
}

:deep(.el-input__wrapper.is-focus) {
  border-color: var(--el-color-primary);
  box-shadow: 0 0 0 2px rgba(64, 158, 255, 0.2);
}
</style>