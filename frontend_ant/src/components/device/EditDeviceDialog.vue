<template>
  <a-modal
    v-model:open="visible"
    title="编辑设备"
    :confirm-loading="loading"
    :mask-closable="false"
    @ok="handleSubmit"
    @cancel="handleCancel"
  >
    <a-form
      ref="formRef"
      :model="formData"
      :rules="rules"
      layout="vertical"
      class="edit-device-form"
    >
      <a-form-item
        label="设备别名"
        name="name"
        help="用于在AIgoOne中识别此设备的友好名称"
      >
        <a-input
          v-model:value="formData.name"
          placeholder="请输入设备别名，如：停车场A算力设备"
          :maxlength="100"
          show-count
        />
      </a-form-item>

      <a-form-item
        label="设备地址"
        name="api_base_url"
        help="算法应用平台的访问地址，格式：http://ip:port"
      >
        <a-input
          v-model:value="formData.api_base_url"
          placeholder="http://192.168.1.100:8000"
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
        help="用于登录算法应用平台的用户名"
      >
        <a-input
          v-model:value="formData.username"
          placeholder="请输入用户名"
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
        help="留空则保持原密码不变"
      >
        <a-input-password
          v-model:value="formData.password"
          placeholder="留空则保持原密码不变"
          :maxlength="255"
        >
          <template #prefix>
            <LockOutlined />
          </template>
        </a-input-password>
      </a-form-item>

      <a-alert
        message="编辑提示"
        description="修改设备信息后，系统会自动验证连接。如果修改了认证信息，请确保用户名密码正确。"
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
import type { Device, DeviceCreate } from '@/api/device'

interface Props {
  visible: boolean
  loading?: boolean
  device: Device | null
}

const props = withDefaults(defineProps<Props>(), {
  visible: false,
  loading: false,
  device: null
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
  ]
  // 编辑时密码不是必填项
}

// 初始化表单数据
const initFormData = () => {
  if (props.device) {
    formData.value = {
      name: props.device.name || '',
      api_base_url: props.device.api_base_url || '',
      username: '', // 编辑时不显示原用户名，需要重新输入
      password: '' // 编辑时不显示原密码，需要重新输入或留空
    }
  }
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

// 监听设备数据变化，初始化表单
watch(() => props.device, (newDevice) => {
  if (newDevice && props.visible) {
    initFormData()
  }
}, { immediate: true, deep: true })

// 监听对话框打开，初始化表单数据
watch(visible, (newValue) => {
  if (newValue && props.device) {
    initFormData()
  } else if (!newValue) {
    resetForm()
  }
})
</script>

<style scoped>
.edit-device-form {
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