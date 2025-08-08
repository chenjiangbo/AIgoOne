<template>
  <a-button
    :type="type"
    :size="size"
    :loading="loading"
    :disabled="disabled"
    :danger="danger"
    :ghost="ghost"
    :block="block"
    :icon="icon"
    @click="handleClick"
    :class="`app-button ${customClass}`"
  >
    <template v-if="icon && !loading" #icon>
      <component :is="icon" />
    </template>
    <slot></slot>
  </a-button>
</template>

<script setup lang="ts">
import type { Component } from 'vue'

interface Props {
  type?: 'primary' | 'ghost' | 'dashed' | 'link' | 'text' | 'default'
  size?: 'large' | 'middle' | 'small'
  loading?: boolean
  disabled?: boolean
  danger?: boolean
  ghost?: boolean
  block?: boolean
  icon?: Component
  customClass?: string
}

withDefaults(defineProps<Props>(), {
  type: 'default',
  size: 'middle',
  loading: false,
  disabled: false,
  danger: false,
  ghost: false,
  block: false,
  customClass: ''
})

const emit = defineEmits<{
  'click': [event: MouseEvent]
}>()

const handleClick = (event: MouseEvent) => {
  emit('click', event)
}
</script>

<style lang="less" scoped>
.app-button {
  border-radius: 6px;
  font-weight: 500;
  transition: all 0.3s;
  
  &.ant-btn-primary {
    box-shadow: 0 2px 0 rgba(5, 145, 255, 0.1);
    
    &:hover {
      box-shadow: 0 2px 0 rgba(5, 145, 255, 0.2);
    }
  }
}</style>