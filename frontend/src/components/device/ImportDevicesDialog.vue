<template>
  <BaseDialog
    :visible="visible"
    title="批量导入设备"
    subtitle="从Excel或CSV文件导入设备信息"
    width="700px"
    size="large"
    type="default"
    icon="Upload"
    :draggable="true"
    :append-to-body="true"
    :modal="false"
    @update:visible="$emit('update:visible', $event)"
  >
    <div class="import-devices-content">
      <!-- 文件上传区域 -->
      <div class="upload-section">
        <div class="upload-header">
          <h4>选择文件</h4>
          <p>支持 .xlsx、.xls、.csv 格式文件</p>
        </div>
        
        <el-upload
          ref="uploadRef"
          :file-list="fileList"
          :auto-upload="false"
          :on-change="handleFileChange"
          :on-remove="handleFileRemove"
          :before-upload="beforeUpload"
          accept=".xlsx,.xls,.csv"
          drag
          class="upload-dragger"
        >
          <div class="upload-content">
            <el-icon class="upload-icon"><UploadFilled /></el-icon>
            <div class="upload-text">
              <p>将文件拖到此处，或<em>点击上传</em></p>
              <p class="upload-hint">请上传包含设备信息的Excel或CSV文件</p>
            </div>
          </div>
        </el-upload>
      </div>

      <!-- 文件格式说明 -->
      <div class="format-section">
        <el-alert
          title="文件格式要求"
          type="info"
          :closable="false"
          show-icon
        >
          <template #default>
            <p>文件应包含以下3列数据（需要表头）：</p>
            <ul class="format-list">
              <li><strong>api_base_url</strong>：设备API地址，如 http://192.168.1.100:8080</li>
              <li><strong>username</strong>：设备登录用户名</li>
              <li><strong>password</strong>：设备登录密码</li>
            </ul>
            <p class="format-note">注意：导入的设备不会检测连通性，初始状态为离线</p>
          </template>
        </el-alert>
      </div>

      <!-- 数据预览 -->
      <div v-if="previewData.length > 0" class="preview-section">
        <div class="preview-header">
          <h4>数据预览</h4>
          <p>共 {{ previewData.length }} 条记录，点击"导入设备"开始导入</p>
        </div>
        
        <el-table
          :data="previewData.slice(0, 10)"
          size="small"
          class="preview-table"
          max-height="300"
        >
          <el-table-column prop="api_base_url" label="设备地址" width="200" show-overflow-tooltip />
          <el-table-column prop="username" label="用户名" width="120" />
          <el-table-column prop="password" label="密码" width="120">
            <template #default>
              <span>******</span>
            </template>
          </el-table-column>
          <el-table-column prop="status" label="状态" width="80">
            <template #default>
              <el-tag type="info" size="small">离线</el-tag>
            </template>
          </el-table-column>
        </el-table>
        
        <div v-if="previewData.length > 10" class="preview-more">
          <p>还有 {{ previewData.length - 10 }} 条记录未显示...</p>
        </div>
      </div>

      <!-- 导入结果 -->
      <div v-if="importResult" class="result-section">
        <el-alert
          :title="importResult.success ? '导入成功' : '导入失败'"
          :type="importResult.success ? 'success' : 'error'"
          :closable="false"
          show-icon
        >
          <template #default>
            <p v-if="importResult.success">
              成功导入 {{ importResult.success_count }} 个设备，
              失败 {{ importResult.failure_count }} 个设备
            </p>
            <p v-else>{{ importResult.message }}</p>
            
            <!-- 显示失败详情 -->
            <div v-if="importResult.failures && importResult.failures.length > 0" class="failure-details">
              <p><strong>失败记录：</strong></p>
              <ul class="failure-list">
                <li v-for="(failure, index) in importResult.failures.slice(0, 5)" :key="index">
                  第{{ failure.row }}行: {{ failure.error }}
                </li>
              </ul>
              <p v-if="importResult.failures.length > 5" class="failure-more">
                还有 {{ importResult.failures.length - 5 }} 条失败记录...
              </p>
            </div>
          </template>
        </el-alert>
      </div>
    </div>
    
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="$emit('update:visible', false)">
          {{ importResult ? '关闭' : '取消' }}
        </el-button>
        <el-button 
          v-if="!importResult"
          type="primary" 
          :loading="importing" 
          :disabled="previewData.length === 0"
          @click="handleImport"
        >
          {{ importing ? '导入中...' : `导入设备 (${previewData.length})` }}
        </el-button>
      </div>
    </template>
  </BaseDialog>
</template>

<script setup>
import { ref, reactive, watch } from 'vue'
import { ElMessage } from 'element-plus'
import { UploadFilled, Upload } from '@element-plus/icons-vue'
import BaseDialog from '../ui/BaseDialog.vue'
import * as XLSX from 'xlsx'

// Props
const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  },
  isDarkTheme: {
    type: Boolean,
    default: false
  }
})

// Emits
const emit = defineEmits(['update:visible', 'import-success'])

// 响应式状态
const uploading = ref(false)
const importing = ref(false)
const fileList = ref([])
const previewData = ref([])
const importResult = ref(null)
const uploadRef = ref()

// 文件处理
const handleFileChange = (file) => {
  const isExcel = file.name.endsWith('.xlsx') || file.name.endsWith('.xls')
  const isCsv = file.name.endsWith('.csv')
  
  if (!isExcel && !isCsv) {
    ElMessage.error('只支持 Excel (.xlsx, .xls) 和 CSV (.csv) 格式文件')
    return false
  }
  
  // 读取文件内容
  parseFile(file.raw)
}

const handleFileRemove = () => {
  previewData.value = []
  importResult.value = null
}

const beforeUpload = () => {
  return false // 阻止自动上传
}

// 解析文件
const parseFile = (file) => {
  const reader = new FileReader()
  
  reader.onload = (e) => {
    try {
      let data = []
      const result = e.target.result
      
      if (file.name.endsWith('.csv')) {
        // 解析CSV
        data = parseCSV(result)
      } else {
        // 解析Excel
        const workbook = XLSX.read(result, { type: 'binary' })
        const sheetName = workbook.SheetNames[0]
        const worksheet = workbook.Sheets[sheetName]
        data = XLSX.utils.sheet_to_json(worksheet)
      }
      
      // 验证数据格式
      const validatedData = validateAndFormatData(data)
      previewData.value = validatedData
      
      if (validatedData.length === 0) {
        ElMessage.warning('文件中没有有效的设备数据')
      } else {
        ElMessage.success(`成功解析 ${validatedData.length} 条设备记录`)
      }
      
    } catch (error) {
      console.error('文件解析失败:', error)
      ElMessage.error('文件解析失败，请检查文件格式')
    }
  }
  
  if (file.name.endsWith('.csv')) {
    reader.readAsText(file)
  } else {
    reader.readAsBinaryString(file)
  }
}

// 解析CSV
const parseCSV = (csvText) => {
  const lines = csvText.split('\n')
  if (lines.length < 2) return []
  
  const headers = lines[0].split(',').map(h => h.trim().replace(/"/g, ''))
  const data = []
  
  for (let i = 1; i < lines.length; i++) {
    const line = lines[i].trim()
    if (!line) continue
    
    const values = line.split(',').map(v => v.trim().replace(/"/g, ''))
    const record = {}
    
    headers.forEach((header, index) => {
      record[header] = values[index] || ''
    })
    
    data.push(record)
  }
  
  return data
}

// 验证和格式化数据
const validateAndFormatData = (data) => {
  const validData = []
  const requiredFields = ['api_base_url', 'username', 'password']
  
  data.forEach((row, index) => {
    // 检查必需字段
    const hasAllFields = requiredFields.every(field => row[field] && row[field].toString().trim())
    
    if (hasAllFields) {
      validData.push({
        api_base_url: row.api_base_url.toString().trim(),
        username: row.username.toString().trim(),
        password: row.password.toString().trim()
      })
    }
  })
  
  return validData
}

// 导入设备
const handleImport = async () => {
  if (previewData.value.length === 0) {
    ElMessage.warning('没有要导入的数据')
    return
  }
  
  importing.value = true
  importResult.value = null
  
  try {
    const response = await fetch('/api/devices/batch-import', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      },
      body: JSON.stringify({
        devices: previewData.value
      })
    })
    
    if (!response.ok) {
      throw new Error('导入请求失败')
    }
    
    const result = await response.json()
    importResult.value = result
    
    if (result.success) {
      ElMessage.success(`成功导入 ${result.success_count} 个设备`)
      emit('import-success')
    } else {
      ElMessage.error(`导入失败: ${result.message}`)
    }
    
  } catch (error) {
    console.error('导入失败:', error)
    ElMessage.error('导入失败: ' + error.message)
    importResult.value = {
      success: false,
      message: error.message
    }
  } finally {
    importing.value = false
  }
}

// 重置状态
const resetDialog = () => {
  fileList.value = []
  previewData.value = []
  importResult.value = null
  importing.value = false
  
  if (uploadRef.value) {
    uploadRef.value.clearFiles()
  }
}

// 监听对话框关闭
watch(() => props.visible, (newVisible) => {
  if (!newVisible) {
    setTimeout(resetDialog, 300) // 延迟重置，避免动画问题
  }
})

// 导出方法给父组件使用
defineExpose({
  resetDialog
})
</script>

<style scoped>
.import-devices-content {
  padding: var(--spacing-5);
}

/* 上传区域 */
.upload-section {
  margin-bottom: var(--spacing-6);
}

.upload-header {
  margin-bottom: var(--spacing-4);
}

.upload-header h4 {
  margin: 0 0 var(--spacing-1) 0;
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
}

.upload-header p {
  margin: 0;
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
}

.upload-dragger {
  width: 100%;
}

:deep(.el-upload-dragger) {
  width: 100%;
  height: 180px;
  border: 2px dashed var(--color-border-secondary);
  border-radius: var(--border-radius-lg);
  background: var(--color-bg-tertiary);
  transition: var(--transition-all-fast);
}

:deep(.el-upload-dragger:hover) {
  border-color: var(--color-primary-500);
  background: var(--color-primary-50);
}

.upload-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: var(--spacing-4);
}

.upload-icon {
  font-size: 48px;
  color: var(--color-text-placeholder);
  margin-bottom: var(--spacing-3);
}

.upload-text p {
  margin: 0;
  color: var(--color-text-secondary);
}

.upload-text p:first-child {
  font-size: var(--font-size-base);
  margin-bottom: var(--spacing-1);
}

.upload-text em {
  color: var(--color-primary-500);
  font-style: normal;
}

.upload-hint {
  font-size: var(--font-size-sm);
  color: var(--color-text-placeholder);
}

/* 格式说明 */
.format-section {
  margin-bottom: var(--spacing-6);
}

.format-list {
  margin: var(--spacing-2) 0;
  padding-left: var(--spacing-4);
}

.format-list li {
  margin: var(--spacing-1) 0;
  font-size: var(--font-size-sm);
}

.format-note {
  margin: var(--spacing-2) 0 0 0;
  font-size: var(--font-size-sm);
  color: var(--color-warning-600);
}

/* 数据预览 */
.preview-section {
  margin-bottom: var(--spacing-6);
}

.preview-header {
  margin-bottom: var(--spacing-4);
}

.preview-header h4 {
  margin: 0 0 var(--spacing-1) 0;
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text-primary);
}

.preview-header p {
  margin: 0;
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
}

.preview-table {
  width: 100%;
  border: 1px solid var(--color-border-primary);
  border-radius: var(--border-radius-md);
}

.preview-more {
  text-align: center;
  padding: var(--spacing-3);
  background: var(--color-bg-tertiary);
  border-radius: 0 0 var(--border-radius-md) var(--border-radius-md);
  border: 1px solid var(--color-border-primary);
  border-top: none;
}

.preview-more p {
  margin: 0;
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
}

/* 导入结果 */
.result-section {
  margin-bottom: var(--spacing-4);
}

.failure-details {
  margin-top: var(--spacing-3);
}

.failure-list {
  margin: var(--spacing-2) 0;
  padding-left: var(--spacing-4);
}

.failure-list li {
  margin: var(--spacing-1) 0;
  font-size: var(--font-size-sm);
  font-family: var(--font-family-mono);
}

.failure-more {
  margin: var(--spacing-2) 0 0 0;
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
}

/* 对话框底部 */
.dialog-footer {
  padding: var(--spacing-4) var(--spacing-5);
  text-align: right;
  gap: var(--spacing-3);
  display: flex;
  justify-content: flex-end;
  margin: 0 calc(var(--spacing-5) * -1) calc(var(--spacing-5) * -1);
  border-radius: 0 0 var(--border-radius-lg) var(--border-radius-lg);
}
</style>