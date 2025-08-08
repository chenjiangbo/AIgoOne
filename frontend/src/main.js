import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import App from './App.vue'
import { ElMessage } from 'element-plus'
// Tailwind CSS
import './assets/styles/main.css'
// 新的模块化样式系统
import './styles/index.css'
// 临时兼容性样式
import './style.css'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router)

// 配置Element Plus消息组件全局设置
app.config.globalProperties.$message = ElMessage

// 设置全局默认配置
ElMessage.closeAll = ElMessage.closeAll || (() => {})

// 包装ElMessage方法以设置默认配置
const originalMethods = {
  success: ElMessage.success,
  error: ElMessage.error,
  warning: ElMessage.warning,
  info: ElMessage.info
}

ElMessage.success = (options) => {
  const config = typeof options === 'string' ? { message: options } : options
  return originalMethods.success({
    showClose: false,
    duration: 2000,
    ...config
  })
}

ElMessage.error = (options) => {
  const config = typeof options === 'string' ? { message: options } : options
  return originalMethods.error({
    showClose: false,
    duration: 3000,
    ...config
  })
}

ElMessage.warning = (options) => {
  const config = typeof options === 'string' ? { message: options } : options
  return originalMethods.warning({
    showClose: false,
    duration: 3000,
    ...config
  })
}

ElMessage.info = (options) => {
  const config = typeof options === 'string' ? { message: options } : options
  return originalMethods.info({
    showClose: false,
    duration: 2000,
    ...config
  })
}

app.mount('#app')