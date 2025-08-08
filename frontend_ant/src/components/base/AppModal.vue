<template>
  <a-modal
    v-model:open="visible"
    :title="title"
    :width="width"
    :centered="centered"
    :mask-closable="maskClosable"
    :destroy-on-close="destroyOnClose"
    :confirm-loading="confirmLoading"
    :ok-text="okText"
    :cancel-text="cancelText"
    @ok="handleOk"
    @cancel="handleCancel"
    :class="`app-modal ${customClass}`"
  >
    <slot></slot>
    <template v-if="$slots.footer" #footer>
      <slot name="footer"></slot>
    </template>
  </a-modal>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  modelValue?: boolean
  title?: string
  width?: string | number
  centered?: boolean
  maskClosable?: boolean
  destroyOnClose?: boolean
  confirmLoading?: boolean
  okText?: string
  cancelText?: string
  customClass?: string
}

const props = withDefaults(defineProps<Props>(), {
  modelValue: false,
  title: '',
  width: 520,
  centered: true,
  maskClosable: false,
  destroyOnClose: true,
  confirmLoading: false,
  okText: '确定',
  cancelText: '取消',
  customClass: ''
})

const emit = defineEmits<{
  'update:modelValue': [value: boolean]
  'ok': []
  'cancel': []
}>()

const visible = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
})

const handleOk = () => {
  emit('ok')
}

const handleCancel = () => {
  emit('cancel')
  visible.value = false
}
</script>

<style lang="less" scoped>
.app-modal {
  :deep(.ant-modal-header) {
    border-bottom: 1px solid #f0f0f0;
  }
  
  :deep(.ant-modal-footer) {
    border-top: 1px solid #f0f0f0;
    padding: 12px 24px;
  }
}</style>