<template>
  <a-card
    :title="title"
    :bordered="bordered"
    :hoverable="hoverable"
    :loading="loading"
    :class="`app-card ${customClass}`"
  >
    <template v-if="$slots.extra" #extra>
      <slot name="extra"></slot>
    </template>
    <slot></slot>
  </a-card>
</template>

<script setup lang="ts">
interface Props {
  title?: string
  bordered?: boolean
  hoverable?: boolean
  loading?: boolean
  customClass?: string
}

withDefaults(defineProps<Props>(), {
  title: '',
  bordered: false,
  hoverable: false,
  loading: false,
  customClass: ''
})
</script>

<style lang="less" scoped>
.app-card {
  border-radius: 8px;
  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.03), 0 1px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px 0 rgba(0, 0, 0, 0.02);
  
  :deep(.ant-card-head) {
    border-bottom: 1px solid #f0f0f0;
    font-weight: 600;
  }
  
  :deep(.ant-card-body) {
    padding: 20px;
  }
}</style>