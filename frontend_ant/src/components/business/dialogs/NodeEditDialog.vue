<template>
  <a-modal
    :open="visible"
    :title="mode === 'add' ? '添加节点' : '编辑节点'"
    :confirm-loading="loading"
    @ok="handleConfirm"
    @cancel="handleCancel"
  >
    <a-form
      ref="formRef"
      :model="formData"
      :rules="formRules"
      layout="vertical"
    >
      <a-form-item
        label="父节点"
        name="parent"
      >
        <a-input
          :value="parentNodeName"
          disabled
          placeholder="根节点"
        >
          <template #prefix>
            <FolderOutlined />
          </template>
        </a-input>
      </a-form-item>

      <a-form-item
        label="节点名称"
        name="name"
        :help="mode === 'add' ? '节点名称在同一父节点下必须唯一，长度限制为1-64个字符' : undefined"
      >
        <a-input
          v-model:value="formData.name"
          placeholder="请输入节点名称"
          :maxlength="64"
          show-count
        >
          <template #prefix>
            <EditOutlined />
          </template>
        </a-input>
      </a-form-item>

      <a-form-item
        label="节点类型"
        name="nodeType"
      >
        <a-radio-group v-model:value="formData.nodeType" :disabled="mode === 'edit'">
          <a-radio value="branch">
            <FolderOutlined />
            分支节点
            <span class="type-description">（可以包含子节点）</span>
          </a-radio>
          <a-radio value="leaf">
            <FileOutlined />
            叶子节点
            <span class="type-description">（用于绑定视频源）</span>
          </a-radio>
        </a-radio-group>
      </a-form-item>

      <!-- 约束信息提示 -->
      <a-alert
        v-if="mode === 'add'"
        message="节点创建约束"
        type="info"
        show-icon
        style="margin-bottom: 16px;"
      >
        <template #description>
          <ul class="constraint-list">
            <li>业务树最大层级深度：<strong>5层</strong></li>
            <li>单个父节点下子节点数量上限：<strong>100个</strong></li>
            <li>当前层级：<strong>{{ currentDepth + 1 }}</strong></li>
            <li>当前父节点子节点数：<strong>{{ currentChildrenCount }}</strong></li>
          </ul>
        </template>
      </a-alert>

      <!-- 叶子节点绑定警告 -->
      <a-alert
        v-if="mode === 'edit' && node?.is_leaf && node?.bindingCount > 0"
        message="注意事项"
        type="warning"
        show-icon
        style="margin-bottom: 16px;"
      >
        <template #description>
          该叶子节点已绑定 {{ node.bindingCount }} 个视频源，修改节点名称不会影响已有绑定关系。
        </template>
      </a-alert>
    </a-form>
  </a-modal>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { message } from 'ant-design-vue'
import type { FormInstance } from 'ant-design-vue'
import {
  FolderOutlined,
  FileOutlined,
  EditOutlined
} from '@ant-design/icons-vue'

interface Props {
  visible: boolean
  node?: any
  mode: 'add' | 'edit'
}

interface Emits {
  (e: 'update:visible', value: boolean): void
  (e: 'success', data: any): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

const formRef = ref<FormInstance>()
const loading = ref(false)

// 表单数据
const formData = ref({
  name: '',
  nodeType: 'branch' as 'branch' | 'leaf'
})

// 表单验证规则
const formRules = {
  name: [
    { required: true, message: '请输入节点名称', trigger: 'blur' },
    { min: 1, max: 64, message: '节点名称长度应为1-64个字符', trigger: 'blur' },
    {
      validator: (rule: any, value: string) => {
        if (!value) return Promise.resolve()
        
        // 检查同级节点名称唯一性
        if (props.mode === 'add') {
          const siblings = props.node?.children || []
          const exists = siblings.some((child: any) => child.name === value)
          if (exists) {
            return Promise.reject('节点名称在同一父节点下必须唯一')
          }
        } else if (props.mode === 'edit' && props.node) {
          // 编辑模式下，检查除自己外的同级节点
          const parent = props.node.parent
          if (parent) {
            const siblings = parent.children || []
            const exists = siblings.some((child: any) => 
              child.id !== props.node.id && child.name === value
            )
            if (exists) {
              return Promise.reject('节点名称在同一父节点下必须唯一')
            }
          }
        }
        
        return Promise.resolve()
      },
      trigger: 'blur'
    }
  ]
}

// 计算属性
const parentNodeName = computed(() => {
  if (props.mode === 'add') {
    return props.node?.name || '根节点'
  } else {
    return props.node?.parent?.name || '根节点'
  }
})

const currentDepth = computed(() => {
  if (props.mode === 'add') {
    return (props.node?.depth || 0)
  } else {
    return (props.node?.depth || 1) - 1
  }
})

const currentChildrenCount = computed(() => {
  if (props.mode === 'add') {
    return props.node?.children?.length || 0
  } else {
    return props.node?.parent?.children?.length || 0
  }
})

// 方法
const validateConstraints = () => {
  if (props.mode === 'add') {
    // 检查层级深度
    if (currentDepth.value >= 5) {
      message.error('已达到最大层级深度限制（5层）')
      return false
    }
    
    // 检查子节点数量
    if (currentChildrenCount.value >= 100) {
      message.error('该父节点下的子节点数量已达到上限（100个）')
      return false
    }
  }
  
  return true
}

const handleConfirm = async () => {
  if (!formRef.value) return

  try {
    await formRef.value.validate()
    
    if (!validateConstraints()) {
      return
    }

    loading.value = true
    
    const nodeData = {
      name: formData.value.name,
      is_leaf: formData.value.nodeType === 'leaf',
      parent_id: props.mode === 'add' ? props.node?.id : props.node?.parent?.id
    }
    
    emit('success', nodeData)
    handleCancel()
  } catch (error) {
    console.error('Form validation failed:', error)
  } finally {
    loading.value = false
  }
}

const handleCancel = () => {
  emit('update:visible', false)
  formRef.value?.resetFields()
  formData.value = {
    name: '',
    nodeType: 'branch'
  }
}

// 监听弹窗显示状态
watch(() => props.visible, (visible) => {
  if (visible && props.node) {
    if (props.mode === 'edit') {
      formData.value.name = props.node.name
      formData.value.nodeType = props.node.is_leaf ? 'leaf' : 'branch'
    } else {
      formData.value.name = ''
      formData.value.nodeType = 'branch'
    }
  }
})
</script>

<style lang="less" scoped>
@import '@/styles/variables.less';

.type-description {
  color: var(--text-secondary);
  font-size: 12px;
  margin-left: 4px;
}

.constraint-list {
  margin: 0;
  padding-left: 16px;
  
  li {
    margin-bottom: 4px;
    color: var(--text-secondary);
    
    &:last-child {
      margin-bottom: 0;
    }
    
    strong {
      color: var(--color-primary);
      font-weight: 600;
    }
  }
}

:deep(.ant-form-item) {
  .ant-form-item-label > label {
    font-weight: 500;
  }
}

:deep(.ant-radio-group) {
  .ant-radio-wrapper {
    display: flex;
    align-items: center;
    margin-bottom: 8px;
    
    &:last-child {
      margin-bottom: 0;
    }
  }
}
</style>