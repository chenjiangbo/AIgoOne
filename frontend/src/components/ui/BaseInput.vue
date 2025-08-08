<template>
  <div :class="wrapperClasses">
    <!-- 输入框标签 -->
    <label v-if="label" class="base-input__label" :for="inputId">
      {{ label }}
      <span v-if="required" class="required-mark">*</span>
    </label>
    
    <!-- 输入框描述 -->
    <div v-if="description" class="base-input__description">
      {{ description }}
    </div>
    
    <!-- Element Plus 输入框 -->
    <el-input
      :id="inputId"
      :model-value="modelValue"
      :class="inputClasses"
      :type="type"
      :placeholder="placeholder"
      :disabled="disabled"
      :readonly="readonly"
      :clearable="clearable"
      :show-password="showPassword"
      :show-word-limit="showWordLimit"
      :maxlength="maxlength"
      :minlength="minlength"
      :size="size"
      :prefix-icon="prefixIcon"
      :suffix-icon="suffixIcon"
      :rows="rows"
      :autosize="autosize"
      :autocomplete="autocomplete"
      :name="name"
      :form="form"
      :validate-event="validateEvent"
      :input-style="inputStyle"
      :autofocus="autofocus"
      :formatter="formatter"
      :parser="parser"
      :resize="resize"
      @update:model-value="handleInput"
      @input="handleNativeInput"
      @change="handleChange"
      @focus="handleFocus"
      @blur="handleBlur"
      @clear="handleClear"
      @keydown="handleKeydown"
      @keyup="handleKeyup"
      @compositionstart="handleCompositionStart"
      @compositionupdate="handleCompositionUpdate"
      @compositionend="handleCompositionEnd"
    >
      <!-- 前缀插槽 -->
      <template v-if="$slots.prefix" #prefix>
        <slot name="prefix" />
      </template>
      
      <!-- 后缀插槽 -->
      <template v-if="$slots.suffix" #suffix>
        <slot name="suffix" />
      </template>
      
      <!-- 前置插槽 -->
      <template v-if="$slots.prepend" #prepend>
        <slot name="prepend" />
      </template>
      
      <!-- 后置插槽 -->
      <template v-if="$slots.append" #append>
        <slot name="append" />
      </template>
    </el-input>
    
    <!-- 帮助文本/错误信息 -->
    <div v-if="helpText || errorMessage" class="base-input__help">
      <div v-if="errorMessage" class="help-text help-text--error">
        <el-icon class="help-icon">
          <WarningFilled />
        </el-icon>
        {{ errorMessage }}
      </div>
      <div v-else-if="helpText" class="help-text help-text--normal">
        {{ helpText }}
      </div>
    </div>
    
    <!-- 字符计数 -->
    <div v-if="showCustomWordLimit && maxlength" class="base-input__count">
      <span :class="countClasses">
        {{ currentLength }} / {{ maxlength }}
      </span>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, useAttrs, nextTick } from 'vue'
import { WarningFilled } from '@element-plus/icons-vue'

// Props
const props = defineProps({
  // v-model
  modelValue: {
    type: [String, Number],
    default: ''
  },
  
  // 基础属性
  type: {
    type: String,
    default: 'text',
    validator: (value) => [
      'text', 'textarea', 'password', 'email', 'url', 'number', 
      'tel', 'search', 'date', 'time', 'datetime-local'
    ].includes(value)
  },
  placeholder: {
    type: String,
    default: ''
  },
  disabled: {
    type: Boolean,
    default: false
  },
  readonly: {
    type: Boolean,
    default: false
  },
  
  // 样式相关
  size: {
    type: String,
    default: 'default',
    validator: (value) => ['large', 'default', 'small'].includes(value)
  },
  variant: {
    type: String,
    default: 'outlined',
    validator: (value) => ['outlined', 'filled', 'standard'].includes(value)
  },
  
  // 功能特性
  clearable: {
    type: Boolean,
    default: false
  },
  showPassword: {
    type: Boolean,
    default: false
  },
  showWordLimit: {
    type: Boolean,
    default: false
  },
  showCustomWordLimit: {
    type: Boolean,
    default: false
  },
  maxlength: {
    type: [String, Number],
    default: undefined
  },
  minlength: {
    type: [String, Number],
    default: undefined
  },
  
  // 图标
  prefixIcon: {
    type: [String, Object],
    default: undefined
  },
  suffixIcon: {
    type: [String, Object],
    default: undefined
  },
  
  // 文本域相关
  rows: {
    type: Number,
    default: 2
  },
  autosize: {
    type: [Boolean, Object],
    default: false
  },
  resize: {
    type: String,
    default: 'vertical',
    validator: (value) => ['none', 'both', 'horizontal', 'vertical'].includes(value)
  },
  
  // 表单相关
  name: {
    type: String,
    default: undefined
  },
  form: {
    type: String,
    default: undefined
  },
  autocomplete: {
    type: String,
    default: 'off'
  },
  validateEvent: {
    type: Boolean,
    default: true
  },
  autofocus: {
    type: Boolean,
    default: false
  },
  
  // 格式化
  formatter: {
    type: Function,
    default: undefined
  },
  parser: {
    type: Function,
    default: undefined
  },
  
  // 自定义属性
  label: {
    type: String,
    default: ''
  },
  description: {
    type: String,
    default: ''
  },
  helpText: {
    type: String,
    default: ''
  },
  errorMessage: {
    type: String,
    default: ''
  },
  required: {
    type: Boolean,
    default: false
  },
  inputStyle: {
    type: Object,
    default: () => ({})
  }
})

// Emits
const emit = defineEmits([
  'update:modelValue',
  'input',
  'change',
  'focus',
  'blur',
  'clear',
  'keydown',
  'keyup',
  'compositionstart',
  'compositionupdate',
  'compositionend'
])

// 内部状态
const inputId = ref(`base-input-${Math.random().toString(36).substr(2, 9)}`)
const isFocused = ref(false)
const isComposing = ref(false)

// 计算属性
const currentLength = computed(() => {
  return String(props.modelValue || '').length
})

const wrapperClasses = computed(() => {
  const classes = ['base-input']
  
  classes.push(`base-input--${props.size}`)
  classes.push(`base-input--${props.variant}`)
  
  if (props.disabled) classes.push('is-disabled')
  if (props.readonly) classes.push('is-readonly')
  if (props.errorMessage) classes.push('is-error')
  if (isFocused.value) classes.push('is-focused')
  if (props.required) classes.push('is-required')
  
  return classes
})

const inputClasses = computed(() => {
  const classes = []
  
  if (props.variant === 'filled') classes.push('base-input__field--filled')
  if (props.variant === 'standard') classes.push('base-input__field--standard')
  
  return classes
})

const countClasses = computed(() => {
  const classes = ['count-text']
  
  if (props.maxlength && currentLength.value > props.maxlength * 0.8) {
    classes.push('count-text--warning')
  }
  
  if (props.maxlength && currentLength.value >= props.maxlength) {
    classes.push('count-text--error')
  }
  
  return classes
})

// 事件处理
const handleInput = (value) => {
  if (!isComposing.value) {
    emit('update:modelValue', value)
    emit('input', value)
  }
}

const handleNativeInput = (event) => {
  emit('input', event.target.value)
}

const handleChange = (value) => {
  emit('change', value)
}

const handleFocus = (event) => {
  isFocused.value = true
  emit('focus', event)
}

const handleBlur = (event) => {
  isFocused.value = false
  emit('blur', event)
}

const handleClear = () => {
  emit('clear')
  emit('update:modelValue', '')
}

const handleKeydown = (event) => {
  emit('keydown', event)
}

const handleKeyup = (event) => {
  emit('keyup', event)
}

const handleCompositionStart = (event) => {
  isComposing.value = true
  emit('compositionstart', event)
}

const handleCompositionUpdate = (event) => {
  emit('compositionupdate', event)
}

const handleCompositionEnd = (event) => {
  isComposing.value = false
  emit('compositionend', event)
  nextTick(() => {
    handleInput(event.target.value)
  })
}
</script>

<style scoped>
/* 基础包装器样式 */
.base-input {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-1);
  width: 100%;
}

/* 标签样式 */
.base-input__label {
  display: inline-block;
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
  margin-bottom: var(--spacing-1);
  cursor: pointer;
  user-select: none;
}

.required-mark {
  color: var(--color-error-500);
  margin-left: var(--spacing-0_5);
}

/* 描述样式 */
.base-input__description {
  font-size: var(--font-size-xs);
  color: var(--color-text-secondary);
  line-height: 1.4;
  margin-bottom: var(--spacing-1);
}

/* 输入框样式覆盖 */
:deep(.el-input) {
  --el-input-border-radius: var(--border-radius-md);
}

:deep(.el-input__wrapper) {
  border-radius: var(--border-radius-md);
  transition: var(--transition-all-fast);
  box-shadow: var(--shadow-sm);
}

:deep(.el-input__wrapper:hover) {
  box-shadow: var(--shadow-md);
}

:deep(.el-input.is-focus .el-input__wrapper) {
  box-shadow: 0 0 0 2px var(--color-primary-200);
}

/* 尺寸变体 */
.base-input--large :deep(.el-input__wrapper) {
  height: 48px;
  padding: 0 var(--spacing-4);
}

.base-input--large :deep(.el-input__inner) {
  font-size: var(--font-size-lg);
}

.base-input--default :deep(.el-input__wrapper) {
  height: 40px;
  padding: 0 var(--spacing-3);
}

.base-input--small :deep(.el-input__wrapper) {
  height: 32px;
  padding: 0 var(--spacing-2);
}

.base-input--small :deep(.el-input__inner) {
  font-size: var(--font-size-sm);
}

/* 变体样式 */
.base-input--filled :deep(.el-input__wrapper) {
  background: var(--color-bg-tertiary);
  border: 1px solid transparent;
}

.base-input--filled :deep(.el-input__wrapper:hover) {
  background: var(--color-bg-secondary);
}

.base-input--filled :deep(.el-input.is-focus .el-input__wrapper) {
  background: var(--color-bg-primary);
  border-color: var(--color-primary-500);
}

.base-input--standard :deep(.el-input__wrapper) {
  background: transparent;
  border: none;
  border-bottom: 2px solid var(--color-border-primary);
  border-radius: 0;
  box-shadow: none;
}

.base-input--standard :deep(.el-input__wrapper:hover) {
  border-bottom-color: var(--color-text-secondary);
  box-shadow: none;
}

.base-input--standard :deep(.el-input.is-focus .el-input__wrapper) {
  border-bottom-color: var(--color-primary-500);
  box-shadow: none;
}

/* 状态样式 */
.base-input.is-error :deep(.el-input__wrapper) {
  border-color: var(--color-error-500);
}

.base-input.is-error :deep(.el-input.is-focus .el-input__wrapper) {
  box-shadow: 0 0 0 2px var(--color-error-200);
}

.base-input.is-disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.base-input.is-disabled .base-input__label {
  cursor: not-allowed;
}

/* 帮助文本样式 */
.base-input__help {
  margin-top: var(--spacing-1);
}

.help-text {
  display: flex;
  align-items: center;
  gap: var(--spacing-1);
  font-size: var(--font-size-xs);
  line-height: 1.4;
}

.help-text--normal {
  color: var(--color-text-secondary);
}

.help-text--error {
  color: var(--color-error-500);
}

.help-icon {
  font-size: var(--font-size-sm);
  flex-shrink: 0;
}

/* 字符计数样式 */
.base-input__count {
  display: flex;
  justify-content: flex-end;
  margin-top: var(--spacing-1);
}

.count-text {
  font-size: var(--font-size-xs);
  color: var(--color-text-placeholder);
  font-variant-numeric: tabular-nums;
}

.count-text--warning {
  color: var(--color-warning-500);
}

.count-text--error {
  color: var(--color-error-500);
}

/* 文本域样式 */
:deep(.el-textarea .el-textarea__inner) {
  border-radius: var(--border-radius-md);
  resize: vertical;
  transition: var(--transition-all-fast);
  font-family: inherit;
}

:deep(.el-textarea.is-focus .el-textarea__inner) {
  box-shadow: 0 0 0 2px var(--color-primary-200);
}

/* 暗色主题适配 */
[data-theme="dark"] .base-input__label {
  color: var(--color-text-primary);
}

[data-theme="dark"] .base-input__description {
  color: var(--color-text-secondary);
}

[data-theme="dark"] .base-input--filled :deep(.el-input__wrapper) {
  background: var(--color-bg-secondary);
}

[data-theme="dark"] .base-input--filled :deep(.el-input__wrapper:hover) {
  background: var(--color-bg-tertiary);
}

[data-theme="dark"] .base-input--filled :deep(.el-input.is-focus .el-input__wrapper) {
  background: var(--color-bg-primary);
}
</style>