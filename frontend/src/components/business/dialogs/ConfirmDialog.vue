<template>
  <BaseDialog
    v-model:visible="dialogVisible"
    :title="title"
    width="auto"
    :show-maximize="false"
    :show-default-footer="false"
    :close-on-click-modal="false"
    :close-on-press-escape="false"
    :type="dialogType"
    :icon="iconName"
    class="confirm-dialog"
  >
    <div class="dialog-content p-6" style="min-width: 360px; max-width: 500px; width: fit-content;">
      <div class="flex items-start gap-3 mb-3">
        <el-icon :size="20" :class="iconClass" class="flex-shrink-0 mt-0.5">
          <component :is="iconComponent" />
        </el-icon>
        <div class="text-base font-medium text-gray-900 flex-1 leading-relaxed">
          {{ message }}
        </div>
      </div>
      <div v-if="details" class="text-sm text-gray-600 ml-8 leading-relaxed">
        {{ details }}
      </div>
    </div>
    
    <template #footer>
      <div class="flex justify-end gap-3 p-4 bg-gray-50">
        <el-button @click="handleCancel">{{ cancelText }}</el-button>
        <el-button 
          :type="confirmButtonType" 
          @click="handleConfirm"
          :loading="loading"
        >
          {{ confirmText }}
        </el-button>
      </div>
    </template>
  </BaseDialog>
</template>

<script setup>
import { ref, computed } from 'vue'
import { Warning, QuestionFilled, CircleCheckFilled, CircleCloseFilled } from '@element-plus/icons-vue'
import BaseDialog from '@/components/ui/BaseDialog.vue'

const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  },
  title: {
    type: String,
    default: '确认操作'
  },
  message: {
    type: String,
    required: true
  },
  details: {
    type: String,
    default: ''
  },
  type: {
    type: String,
    default: 'warning',
    validator: (value) => ['info', 'success', 'warning', 'danger'].includes(value)
  },
  confirmText: {
    type: String,
    default: '确定'
  },
  cancelText: {
    type: String,
    default: '取消'
  },
  loading: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:visible', 'confirm', 'cancel'])

// 对话框显示状态
const dialogVisible = computed({
  get: () => props.visible,
  set: (val) => emit('update:visible', val)
})

// 根据类型确定对话框样式
const dialogType = computed(() => props.type)

const iconName = computed(() => {
  const iconMap = {
    'info': 'InfoFilled',
    'success': 'CircleCheckFilled',
    'warning': 'Warning',
    'danger': 'CircleCloseFilled'
  }
  return iconMap[props.type] || 'Warning'
})

const iconComponent = computed(() => {
  const iconMap = {
    'info': QuestionFilled,
    'success': CircleCheckFilled,
    'warning': Warning,
    'danger': CircleCloseFilled
  }
  return iconMap[props.type] || Warning
})

const iconClass = computed(() => {
  const classMap = {
    'info': 'text-blue-500',
    'success': 'text-green-500',
    'warning': 'text-yellow-500',
    'danger': 'text-red-500'
  }
  return classMap[props.type] || 'text-yellow-500'
})

const confirmButtonType = computed(() => {
  const typeMap = {
    'info': 'primary',
    'success': 'success',
    'warning': 'warning',
    'danger': 'danger'
  }
  return typeMap[props.type] || 'warning'
})

// 确认操作
const handleConfirm = () => {
  emit('confirm')
}

// 取消操作
const handleCancel = () => {
  emit('cancel')
  dialogVisible.value = false
}
</script>

<style scoped>
.confirm-dialog {
  --dialog-padding: 0;
}

:deep(.el-dialog__body) {
  padding: 0 !important;
}

.dialog-content {
  background: white;
}
</style>