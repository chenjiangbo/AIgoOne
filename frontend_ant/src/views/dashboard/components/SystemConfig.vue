<template>
  <div class="system-config">
    <!-- 页面头部 -->
    <div class="page-header">
      <div class="header-left">
        <h2 class="page-title">系统配置</h2>
        <p class="page-description">管理系统参数和配置选项</p>
      </div>
      <div class="header-actions">
        <a-button @click="refreshConfig">
          <template #icon><ReloadOutlined /></template>
          刷新
        </a-button>
        <a-button type="primary" @click="saveAllConfig" :loading="saving">
          <template #icon><SaveOutlined /></template>
          保存所有配置
        </a-button>
      </div>
    </div>

    <a-row :gutter="24">
      <!-- 左侧配置分类 -->
      <a-col :span="6">
        <a-card title="配置分类" size="small">
          <a-menu 
            v-model:selectedKeys="selectedCategory" 
            mode="inline"
            @click="handleCategoryClick"
          >
            <a-menu-item key="basic">
              <template #icon><SettingOutlined /></template>
              基础配置
            </a-menu-item>
            <a-menu-item key="algorithm">
              <template #icon><BugOutlined /></template>
              算法配置
            </a-menu-item>
            <a-menu-item key="device">
              <template #icon><DesktopOutlined /></template>
              设备配置
            </a-menu-item>
            <a-menu-item key="storage">
              <template #icon><DatabaseOutlined /></template>
              存储配置
            </a-menu-item>
            <a-menu-item key="network">
              <template #icon><GlobalOutlined /></template>
              网络配置
            </a-menu-item>
            <a-menu-item key="security">
              <template #icon><SafetyOutlined /></template>
              安全配置
            </a-menu-item>
            <a-menu-item key="notification">
              <template #icon><BellOutlined /></template>
              通知配置
            </a-menu-item>
          </a-menu>
        </a-card>
      </a-col>

      <!-- 右侧配置内容 -->
      <a-col :span="18">
        <div class="config-content">
          <!-- 基础配置 -->
          <a-card v-if="selectedCategory[0] === 'basic'" title="基础配置" size="small">
            <a-form :label-col="{ span: 8 }" :wrapper-col="{ span: 16 }">
              <a-form-item label="系统名称">
                <a-input v-model:value="config.basic.systemName" />
              </a-form-item>
              <a-form-item label="系统版本">
                <a-input v-model:value="config.basic.systemVersion" disabled />
              </a-form-item>
              <a-form-item label="系统描述">
                <a-textarea v-model:value="config.basic.systemDescription" :rows="3" />
              </a-form-item>
              <a-form-item label="默认语言">
                <a-select v-model:value="config.basic.defaultLanguage">
                  <a-select-option value="zh-CN">简体中文</a-select-option>
                  <a-select-option value="en-US">English</a-select-option>
                </a-select>
              </a-form-item>
              <a-form-item label="时区设置">
                <a-select v-model:value="config.basic.timezone">
                  <a-select-option value="Asia/Shanghai">Asia/Shanghai</a-select-option>
                  <a-select-option value="UTC">UTC</a-select-option>
                </a-select>
              </a-form-item>
              <a-form-item label="自动备份">
                <a-switch v-model:checked="config.basic.autoBackup" />
              </a-form-item>
            </a-form>
          </a-card>

          <!-- 算法配置 -->
          <a-card v-else-if="selectedCategory[0] === 'algorithm'" title="算法配置" size="small">
            <a-form :label-col="{ span: 8 }" :wrapper-col="{ span: 16 }">
              <a-form-item label="默认检测阈值">
                <a-slider v-model:value="config.algorithm.detectionThreshold" :min="0" :max="1" :step="0.01" />
                <span>{{ config.algorithm.detectionThreshold }}</span>
              </a-form-item>
              <a-form-item label="最大并发任务数">
                <a-input-number v-model:value="config.algorithm.maxConcurrentTasks" :min="1" :max="20" />
              </a-form-item>
              <a-form-item label="模型存储路径">
                <a-input v-model:value="config.algorithm.modelStoragePath" />
              </a-form-item>
              <a-form-item label="推理设备">
                <a-select v-model:value="config.algorithm.inferenceDevice">
                  <a-select-option value="cpu">CPU</a-select-option>
                  <a-select-option value="gpu">GPU</a-select-option>
                  <a-select-option value="auto">自动选择</a-select-option>
                </a-select>
              </a-form-item>
              <a-form-item label="启用模型缓存">
                <a-switch v-model:checked="config.algorithm.enableModelCache" />
              </a-form-item>
            </a-form>
          </a-card>

          <!-- 设备配置 -->
          <a-card v-else-if="selectedCategory[0] === 'device'" title="设备配置" size="small">
            <a-form :label-col="{ span: 8 }" :wrapper-col="{ span: 16 }">
              <a-form-item label="设备连接超时(秒)">
                <a-input-number v-model:value="config.device.connectionTimeout" :min="5" :max="300" />
              </a-form-item>
              <a-form-item label="心跳间隔(秒)">
                <a-input-number v-model:value="config.device.heartbeatInterval" :min="10" :max="600" />
              </a-form-item>
              <a-form-item label="最大重试次数">
                <a-input-number v-model:value="config.device.maxRetryCount" :min="1" :max="10" />
              </a-form-item>
              <a-form-item label="自动设备发现">
                <a-switch v-model:checked="config.device.autoDiscovery" />
              </a-form-item>
              <a-form-item label="设备同步间隔(分钟)">
                <a-input-number v-model:value="config.device.syncInterval" :min="1" :max="60" />
              </a-form-item>
            </a-form>
          </a-card>

          <!-- 存储配置 -->
          <a-card v-else-if="selectedCategory[0] === 'storage'" title="存储配置" size="small">
            <a-form :label-col="{ span: 8 }" :wrapper-col="{ span: 16 }">
              <a-form-item label="数据存储路径">
                <a-input v-model:value="config.storage.dataStoragePath" />
              </a-form-item>
              <a-form-item label="日志存储路径">
                <a-input v-model:value="config.storage.logStoragePath" />
              </a-form-item>
              <a-form-item label="最大存储容量(GB)">
                <a-input-number v-model:value="config.storage.maxStorageSize" :min="10" :max="10000" />
              </a-form-item>
              <a-form-item label="日志保留天数">
                <a-input-number v-model:value="config.storage.logRetentionDays" :min="7" :max="365" />
              </a-form-item>
              <a-form-item label="自动清理">
                <a-switch v-model:checked="config.storage.autoCleanup" />
              </a-form-item>
            </a-form>
          </a-card>

          <!-- 网络配置 -->
          <a-card v-else-if="selectedCategory[0] === 'network'" title="网络配置" size="small">
            <a-form :label-col="{ span: 8 }" :wrapper-col="{ span: 16 }">
              <a-form-item label="HTTP端口">
                <a-input-number v-model:value="config.network.httpPort" :min="1000" :max="65535" />
              </a-form-item>
              <a-form-item label="HTTPS端口">
                <a-input-number v-model:value="config.network.httpsPort" :min="1000" :max="65535" />
              </a-form-item>
              <a-form-item label="启用HTTPS">
                <a-switch v-model:checked="config.network.enableHttps" />
              </a-form-item>
              <a-form-item label="允许的IP范围">
                <a-textarea v-model:value="config.network.allowedIpRange" placeholder="例: 192.168.1.0/24" :rows="3" />
              </a-form-item>
              <a-form-item label="API请求限制(次/分钟)">
                <a-input-number v-model:value="config.network.apiRateLimit" :min="10" :max="10000" />
              </a-form-item>
            </a-form>
          </a-card>

          <!-- 安全配置 -->
          <a-card v-else-if="selectedCategory[0] === 'security'" title="安全配置" size="small">
            <a-form :label-col="{ span: 8 }" :wrapper-col="{ span: 16 }">
              <a-form-item label="密码最小长度">
                <a-input-number v-model:value="config.security.minPasswordLength" :min="6" :max="20" />
              </a-form-item>
              <a-form-item label="会话超时(分钟)">
                <a-input-number v-model:value="config.security.sessionTimeout" :min="10" :max="1440" />
              </a-form-item>
              <a-form-item label="最大登录失败次数">
                <a-input-number v-model:value="config.security.maxLoginAttempts" :min="3" :max="10" />
              </a-form-item>
              <a-form-item label="账户锁定时间(分钟)">
                <a-input-number v-model:value="config.security.lockoutDuration" :min="5" :max="60" />
              </a-form-item>
              <a-form-item label="启用两步验证">
                <a-switch v-model:checked="config.security.enableTwoFactor" />
              </a-form-item>
              <a-form-item label="审计日志">
                <a-switch v-model:checked="config.security.enableAuditLog" />
              </a-form-item>
            </a-form>
          </a-card>

          <!-- 通知配置 -->
          <a-card v-else-if="selectedCategory[0] === 'notification'" title="通知配置" size="small">
            <a-form :label-col="{ span: 8 }" :wrapper-col="{ span: 16 }">
              <a-form-item label="邮件服务器">
                <a-input v-model:value="config.notification.emailServer" />
              </a-form-item>
              <a-form-item label="邮件端口">
                <a-input-number v-model:value="config.notification.emailPort" :min="25" :max="65535" />
              </a-form-item>
              <a-form-item label="发送邮箱">
                <a-input v-model:value="config.notification.senderEmail" />
              </a-form-item>
              <a-form-item label="邮箱密码">
                <a-input-password v-model:value="config.notification.emailPassword" />
              </a-form-item>
              <a-form-item label="启用邮件通知">
                <a-switch v-model:checked="config.notification.enableEmailNotification" />
              </a-form-item>
              <a-form-item label="启用短信通知">
                <a-switch v-model:checked="config.notification.enableSmsNotification" />
              </a-form-item>
              <a-form-item label="Webhook URL">
                <a-input v-model:value="config.notification.webhookUrl" />
              </a-form-item>
            </a-form>
          </a-card>
        </div>

        <!-- 操作按钮 -->
        <div class="config-actions">
          <a-space>
            <a-button @click="resetCurrentConfig">重置当前配置</a-button>
            <a-button type="primary" @click="saveCurrentConfig" :loading="saving">
              保存当前配置
            </a-button>
          </a-space>
        </div>
      </a-col>
    </a-row>

    <!-- 导入导出配置 -->
    <a-card title="配置管理" size="small" style="margin-top: 24px">
      <a-space>
        <a-button @click="exportConfig">
          <template #icon><ExportOutlined /></template>
          导出配置
        </a-button>
        <a-upload
          :before-upload="importConfig"
          :show-upload-list="false"
          accept=".json"
        >
          <a-button>
            <template #icon><ImportOutlined /></template>
            导入配置
          </a-button>
        </a-upload>
        <a-button @click="resetAllConfig" danger>
          <template #icon><RestOutlined /></template>
          恢复默认配置
        </a-button>
      </a-space>
    </a-card>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { message, Modal } from 'ant-design-vue'
import {
  ReloadOutlined,
  SaveOutlined,
  SettingOutlined,
  BugOutlined,
  DesktopOutlined,
  DatabaseOutlined,
  GlobalOutlined,
  SafetyOutlined,
  BellOutlined,
  ExportOutlined,
  ImportOutlined,
  RestOutlined
} from '@ant-design/icons-vue'

// 状态管理
const saving = ref(false)
const selectedCategory = ref(['basic'])

// 配置数据
const config = reactive({
  basic: {
    systemName: 'AIgoOne算法管理平台',
    systemVersion: 'v1.0.0',
    systemDescription: '基于AI的智能算法管理平台',
    defaultLanguage: 'zh-CN',
    timezone: 'Asia/Shanghai',
    autoBackup: true
  },
  algorithm: {
    detectionThreshold: 0.5,
    maxConcurrentTasks: 5,
    modelStoragePath: '/opt/models',
    inferenceDevice: 'auto',
    enableModelCache: true
  },
  device: {
    connectionTimeout: 30,
    heartbeatInterval: 60,
    maxRetryCount: 3,
    autoDiscovery: true,
    syncInterval: 10
  },
  storage: {
    dataStoragePath: '/opt/data',
    logStoragePath: '/opt/logs',
    maxStorageSize: 1000,
    logRetentionDays: 30,
    autoCleanup: true
  },
  network: {
    httpPort: 8080,
    httpsPort: 8443,
    enableHttps: false,
    allowedIpRange: '192.168.0.0/16\n10.0.0.0/8',
    apiRateLimit: 1000
  },
  security: {
    minPasswordLength: 8,
    sessionTimeout: 120,
    maxLoginAttempts: 5,
    lockoutDuration: 15,
    enableTwoFactor: false,
    enableAuditLog: true
  },
  notification: {
    emailServer: 'smtp.example.com',
    emailPort: 587,
    senderEmail: 'noreply@example.com',
    emailPassword: '',
    enableEmailNotification: false,
    enableSmsNotification: false,
    webhookUrl: ''
  }
})

// 默认配置备份
const defaultConfig = JSON.parse(JSON.stringify(config))

// 事件处理
const handleCategoryClick = ({ key }: { key: string }) => {
  selectedCategory.value = [key]
}

const refreshConfig = async () => {
  try {
    // 模拟从服务器加载配置
    await new Promise(resolve => setTimeout(resolve, 1000))
    message.success('配置刷新成功')
  } catch (error: any) {
    message.error('刷新配置失败: ' + error.message)
  }
}

const saveCurrentConfig = async () => {
  saving.value = true
  try {
    // 模拟保存当前配置分类
    await new Promise(resolve => setTimeout(resolve, 1000))
    message.success('当前配置保存成功')
  } catch (error: any) {
    message.error('保存配置失败: ' + error.message)
  } finally {
    saving.value = false
  }
}

const saveAllConfig = async () => {
  saving.value = true
  try {
    // 模拟保存所有配置
    await new Promise(resolve => setTimeout(resolve, 2000))
    message.success('所有配置保存成功')
  } catch (error: any) {
    message.error('保存配置失败: ' + error.message)
  } finally {
    saving.value = false
  }
}

const resetCurrentConfig = () => {
  Modal.confirm({
    title: '重置确认',
    content: '确定要重置当前配置分类到默认值吗？',
    okText: '确定',
    cancelText: '取消',
    onOk: () => {
      const category = selectedCategory.value[0]
      if (category && defaultConfig[category as keyof typeof defaultConfig]) {
        Object.assign(config[category as keyof typeof config], defaultConfig[category as keyof typeof defaultConfig])
        message.success('当前配置已重置')
      }
    }
  })
}

const resetAllConfig = () => {
  Modal.confirm({
    title: '恢复默认配置',
    content: '确定要恢复所有配置到默认值吗？此操作不可撤销。',
    okText: '确定',
    cancelText: '取消',
    okType: 'danger',
    onOk: () => {
      Object.assign(config, JSON.parse(JSON.stringify(defaultConfig)))
      message.success('已恢复所有默认配置')
    }
  })
}

const exportConfig = () => {
  try {
    const configJson = JSON.stringify(config, null, 2)
    const blob = new Blob([configJson], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `system-config-${new Date().toISOString().split('T')[0]}.json`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
    message.success('配置导出成功')
  } catch (error: any) {
    message.error('配置导出失败: ' + error.message)
  }
}

const importConfig = (file: File) => {
  const reader = new FileReader()
  reader.onload = (e) => {
    try {
      const importedConfig = JSON.parse(e.target?.result as string)
      
      Modal.confirm({
        title: '导入配置确认',
        content: '确定要导入新的配置吗？这将覆盖当前的配置。',
        okText: '确定',
        cancelText: '取消',
        onOk: () => {
          Object.assign(config, importedConfig)
          message.success('配置导入成功')
        }
      })
    } catch (error: any) {
      message.error('配置文件格式错误: ' + error.message)
    }
  }
  reader.readAsText(file)
  return false // 阻止默认上传行为
}

// 生命周期
onMounted(() => {
  refreshConfig()
})
</script>

<style lang="less" scoped>
.system-config {
  height: 100%;
  display: flex;
  flex-direction: column;
  padding: 24px;
  background: #fff;
}

// 页面头部
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 24px;
}

.header-left {
  flex: 1;
}

.page-title {
  font-size: 24px;
  font-weight: 600;
  color: #2c3e50;
  margin: 0 0 8px 0;
}

.page-description {
  font-size: 14px;
  color: #6b7280;
  margin: 0;
}

.header-actions {
  display: flex;
  gap: 12px;
  flex-shrink: 0;
}

// 配置内容
.config-content {
  min-height: 400px;
  margin-bottom: 24px;
}

.config-actions {
  text-align: right;
  padding-top: 16px;
  border-top: 1px solid #f0f0f0;
}

// 响应式设计
@media (max-width: 1024px) {
  .page-header {
    flex-direction: column;
    gap: 16px;
  }
  
  .header-actions {
    align-self: stretch;
    justify-content: flex-end;
  }
}

@media (max-width: 768px) {
  .system-config {
    padding: 16px;
  }
  
  :deep(.ant-col-6) {
    width: 100%;
    margin-bottom: 16px;
  }
  
  :deep(.ant-col-18) {
    width: 100%;
  }
}
</style>