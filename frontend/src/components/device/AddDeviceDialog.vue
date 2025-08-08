<template>
  <BaseDialog
    :visible="visible"
    title="添加设备"
    subtitle="连接新的AI算法平台设备"
    width="550px"
    size="medium"
    type="default"
    icon="Plus"
    :draggable="true"
    :append-to-body="true"
    :modal="false"
    @update:visible="$emit('update:visible', $event)"
  >
    
    <el-form
      ref="formRef"
      :model="form"
      :rules="rules"
      label-width="120px"
      class="add-device-form"
    >
      <el-form-item label="设备地址" prop="api_base_url">
        <el-input 
          v-model="form.api_base_url" 
          placeholder="请输入设备API地址，如: http://192.168.1.100:8080"
        />
        <div class="form-tip">
          请输入算法应用平台的完整地址，包含协议和端口
        </div>
      </el-form-item>
      
      <el-form-item label="用户名" prop="username">
        <el-input v-model="form.username" placeholder="请输入设备登录用户名" />
      </el-form-item>
      
      <el-form-item label="密码" prop="password">
        <el-input 
          v-model="form.password" 
          type="password" 
          show-password 
          placeholder="请输入设备登录密码"
        />
      </el-form-item>
      
    </el-form>
    
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="$emit('update:visible', false)">取消</el-button>
        <el-button 
          type="primary" 
          :loading="loading" 
          @click="handleSubmit"
        >
          {{ loading ? '连接中...' : '添加设备' }}
        </el-button>
      </div>
    </template>
  </BaseDialog>
</template>

<script setup>
import { ref, reactive, watch } from 'vue'
import { Plus, Close } from '@element-plus/icons-vue'
import BaseDialog from '../ui/BaseDialog.vue'

// Props
const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  },
  loading: {
    type: Boolean,
    default: false
  },
  isDarkTheme: {
    type: Boolean,
    default: false
  },
})

// Emits
const emit = defineEmits(['update:visible', 'submit'])

// 模板引用
const formRef = ref()

// 表单数据
const form = reactive({
  api_base_url: '',
  username: '',
  password: ''
})

// 表单验证规则
const rules = {
  api_base_url: [
    { required: true, message: '请输入设备API地址', trigger: 'blur' },
    {
      pattern: /^https?:\/\/([a-zA-Z0-9.-]+)(:[0-9]{1,5})?(\/.*)?$/,
      message: '请输入有效的URL地址',
      trigger: 'blur'
    }
  ],
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' }
  ]
}

// 方法
const handleSubmit = async () => {
  if (!formRef.value) return;
  
  try {
    await formRef.value.validate();
    emit('submit', { ...form });
  } catch (error) {
    console.log('Validation failed:', error);
  }
};

const resetForm = () => {
  Object.assign(form, {
    api_base_url: '',
    username: '',
    password: ''
  })
  
  if (formRef.value) {
    formRef.value.resetFields()
  }
}

// 监听对话框关闭，重置表单
watch(() => props.visible, (newVisible) => {
  if (!newVisible) {
    resetForm()
  }
})

// 导出方法给父组件使用
defineExpose({
  resetForm
})
</script>

<style scoped>
.add-device-form {
  padding: var(--spacing-5);
}

.form-tip {
  font-size: var(--font-size-sm);
  color: var(--color-text-tertiary);
  margin-top: var(--spacing-1);
}

/* 组件专用样式 */
.dialog-footer {
  padding: var(--spacing-4) var(--spacing-5);
  text-align: right;
  gap: var(--spacing-3);
  display: flex;
  justify-content: flex-end;
  margin: 0 calc(var(--spacing-5) * -1) calc(var(--spacing-5) * -1);
  border-radius: 0 0 var(--border-radius-lg) var(--border-radius-lg);
}

/* 表单样式优化 */
:deep(.el-form-item__label) {
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
}

:deep(.el-input__wrapper) {
  border-radius: var(--border-radius-md);
}

:deep(.el-select .el-input__wrapper) {
  border-radius: var(--border-radius-md);
}

</style>