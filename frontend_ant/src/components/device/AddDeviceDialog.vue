<template>
  <a-modal
    v-model:open="visible"
    title="添加设备"
    :confirm-loading="loading"
    :mask-closable="false"
    :draggable="true"
    @ok="handleSubmit"
    @cancel="handleCancel"
  >
    <a-form
      ref="formRef"
      :model="formData"
      :rules="rules"
      layout="vertical"
      class="add-device-form"
    >

      <a-form-item
        label="设备地址"
        name="api_base_url"
      >
        <a-input
          v-model:value="formData.api_base_url"
          placeholder="算法应用平台的访问地址，格式：http://192.168.1.100:8000"
          :maxlength="255"
        >
          <template #prefix>
            <GlobalOutlined />
          </template>
        </a-input>
      </a-form-item>

      <a-form-item
        label="用户名"
        name="username"
      >
        <a-input
          v-model:value="formData.username"
          placeholder="用于登录算法应用平台的用户名"
          :maxlength="100"
        >
          <template #prefix>
            <UserOutlined />
          </template>
        </a-input>
      </a-form-item>

      <a-form-item
        label="密码"
        name="password"
      >
        <a-input-password
          v-model:value="formData.password"
          placeholder="用于登录算法应用平台的密码"
          :maxlength="255"
        >
          <template #prefix>
            <LockOutlined />
          </template>
        </a-input-password>
      </a-form-item>

      <a-alert
        message="添加提示"
        description="添加设备时，系统会立即尝试连接并验证凭证。请确保设备地址可访问且用户名密码正确。"
        type="info"
        show-icon
        class="form-alert"
      />
    </a-form>
  </a-modal>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import type { FormInstance, Rule } from 'ant-design-vue/es/form'
import { GlobalOutlined, UserOutlined, LockOutlined } from '@ant-design/icons-vue'
import type { DeviceCreate } from '@/api/device'

interface Props {
  visible: boolean
  loading?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  visible: false,
  loading: false
})

const emit = defineEmits<{
  'update:visible': [value: boolean]
  submit: [data: DeviceCreate]
}>()

const formRef = ref<FormInstance>()
const formData = ref<DeviceCreate>({
  name: '',
  api_base_url: '',
  username: '',
  password: ''
})

const visible = computed({
  get: () => props.visible,
  set: (value: boolean) => emit('update:visible', value)
})

// 表单验证规则
const rules: Record<string, Rule[]> = {
  api_base_url: [
    { required: true, message: '请输入设备地址' },
    {
      pattern: /^https?:\/\/.+/,
      message: '请输入有效的URL地址，格式：http://ip:port'
    }
  ],
  username: [
    { required: true, message: '请输入用户名' }
  ],
  password: [
    { required: true, message: '请输入密码' }
  ]
}

// 重置表单
const resetForm = () => {
  formData.value = {
    name: '',
    api_base_url: '',
    username: '',
    password: ''
  }
  formRef.value?.resetFields()
}

// 处理提交
const handleSubmit = async () => {
  try {
    await formRef.value?.validate()
    emit('submit', { ...formData.value })
  } catch (error) {
    console.log('表单验证失败:', error)
  }
}

// 处理取消
const handleCancel = () => {
  visible.value = false
  resetForm()
}

// 监听对话框关闭，重置表单
watch(visible, (newValue) => {
  if (!newValue) {
    resetForm()
  }
})
</script>

<style scoped>
.add-device-form {
  padding-top: 16px;
}

.form-alert {
  margin-top: 16px;
}

:deep(.ant-form-item-explain) {
  font-size: 12px;
  color: var(--text-secondary);
}

:deep(.ant-input-affix-wrapper .ant-input-prefix) {
  color: var(--text-secondary);
}

:deep(.ant-alert) {
  border-radius: 8px;
}
</style>