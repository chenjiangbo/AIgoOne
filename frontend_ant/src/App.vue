<template>
  <a-config-provider :theme="currentThemeConfig">
    <router-view />
  </a-config-provider>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { ConfigProvider } from 'ant-design-vue'
import { lightThemeConfig, darkThemeConfig } from '@/styles/theme'
import { useAppStore } from '@/store'

const appStore = useAppStore()

// 根据store状态计算当前主题配置
const currentThemeConfig = computed(() => {
  return appStore.isDarkTheme ? darkThemeConfig : lightThemeConfig
})

// 初始化主题
onMounted(() => {
  appStore.initTheme()
})
</script>

<style lang="less">
// 导入全局CSS变量
@import '@/styles/variables.less';

#app {
  width: 100%;
  height: 100%;
  background-color: var(--bg-secondary);
  color: var(--text-primary);
  
  // 确保全屏高度
  min-height: 100vh;
}</style>