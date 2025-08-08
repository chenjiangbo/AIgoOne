<template>
  <a-modal
    v-model:open="visible"
    title="批量导入设备"
    width="600px"
    :confirm-loading="importing"
    :mask-closable="false"
    :draggable="true"
    @ok="handleImport"
    @cancel="handleCancel"
  >
    <div class="import-content">
      <!-- 导入说明 -->
      <a-alert
        message="导入说明"
        type="info"
        show-icon
        class="import-alert"
      >
        <template #description>
          <div>
            <p>支持通过上传CSV文件批量导入设备，文件格式要求：</p>
            <ul>
              <li>文件编码：UTF-8</li>
              <li>必需列：url (设备地址), username (用户名), password (密码)</li>
              <li>设备地址格式：http://ip:port</li>
              <li>导入时不会验证设备连通性，设备将被标记为离线状态</li>
            </ul>
          </div>
        </template>
      </a-alert>

      <!-- 下载模板 -->
      <div class="template-section">
        <a-button
          type="link"
          @click="downloadTemplate"
        >
          <template #icon>
            <DownloadOutlined />
          </template>
          下载CSV模板文件
        </a-button>
      </div>

      <!-- 文件上传 -->
      <a-upload
        v-model:file-list="fileList"
        :before-upload="beforeUpload"
        :remove="handleRemove"
        accept=".csv"
        :max-count="1"
        class="upload-area"
      >
        <a-button>
          <template #icon>
            <UploadOutlined />
          </template>
          选择CSV文件
        </a-button>
      </a-upload>

      <!-- 预览数据 -->
      <div v-if="previewData.length > 0" class="preview-section">
        <a-divider>数据预览 (前5行)</a-divider>
        <a-table
          :data-source="previewData"
          :columns="previewColumns"
          :pagination="false"
          size="small"
          class="preview-table"
        />
        <div class="preview-info">
          共解析到 {{ totalRows }} 行数据，其中 {{ validRows }} 行有效，{{ invalidRows }} 行无效
        </div>
      </div>

      <!-- 错误信息 -->
      <div v-if="parseErrors.length > 0" class="error-section">
        <a-divider>解析错误</a-divider>
        <a-alert
          v-for="(error, index) in parseErrors"
          :key="index"
          :message="`第 ${error.row} 行：${error.message}`"
          type="error"
          show-icon
          style="margin-bottom: 8px"
        />
      </div>
    </div>
  </a-modal>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { message } from 'ant-design-vue'
import { DownloadOutlined, UploadOutlined } from '@ant-design/icons-vue'
import type { UploadFile, TableColumnsType } from 'ant-design-vue'
import type { DeviceCreate } from '@/api/device'
import { batchImportDevices } from '@/api/device'

interface Props {
  visible: boolean
}

const props = withDefaults(defineProps<Props>(), {
  visible: false
})

const emit = defineEmits<{
  'update:visible': [value: boolean]
  'import-success': []
}>()

const importing = ref(false)
const fileList = ref<UploadFile[]>([])
const previewData = ref<any[]>([])
const parseErrors = ref<Array<{ row: number; message: string }>>([])
const parsedDevices = ref<DeviceCreate[]>([])

const visible = computed({
  get: () => props.visible,
  set: (value: boolean) => emit('update:visible', value)
})

// 预览表格列
const previewColumns: TableColumnsType = [
  { title: '设备地址', dataIndex: 'url', width: 250, ellipsis: true },
  { title: '用户名', dataIndex: 'username', width: 120 },
  { title: '密码', dataIndex: 'password', width: 120, customRender: () => '******' },
  { title: '状态', dataIndex: 'valid', width: 80, customRender: ({ text }) => text ? '有效' : '无效' }
]

// 统计信息
const totalRows = computed(() => previewData.value.length)
const validRows = computed(() => previewData.value.filter(row => row.valid).length)
const invalidRows = computed(() => totalRows.value - validRows.value)

// 下载CSV模板
const downloadTemplate = () => {
  const csvContent = 'url,username,password\nhttp://192.168.1.100:8000,admin,admin123\nhttp://192.168.1.101:8000,admin,admin123'
  const blob = new Blob(['\ufeff' + csvContent], { type: 'text/csv;charset=utf-8' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'device_import_template.csv'
  a.click()
  URL.revokeObjectURL(url)
}

// 上传前处理
const beforeUpload = (file: UploadFile) => {
  const isCSV = file.type === 'text/csv' || file.name?.endsWith('.csv')
  if (!isCSV) {
    message.error('只能上传CSV文件！')
    return false
  }

  const isLt5M = file.size! / 1024 / 1024 < 5
  if (!isLt5M) {
    message.error('文件大小不能超过5MB！')
    return false
  }

  // 解析CSV文件
  parseCSVFile(file)
  return false // 阻止自动上传
}

// 解析CSV文件
const parseCSVFile = (file: UploadFile) => {
  const reader = new FileReader()
  reader.onload = (e) => {
    try {
      const text = e.target?.result as string
      parseCSVText(text)
    } catch (error) {
      message.error('文件解析失败，请检查文件格式')
    }
  }
  reader.readAsText(file as File, 'UTF-8')
}

// 解析CSV文本
const parseCSVText = (text: string) => {
  const lines = text.split('\n').filter(line => line.trim())
  if (lines.length < 2) {
    message.error('文件内容不能为空，至少需要包含表头和一行数据')
    return
  }

  const headers = lines[0].split(',').map(h => h.trim().replace(/"/g, ''))
  const requiredHeaders = ['url', 'username', 'password']
  
  // 检查必需的列
  const missingHeaders = requiredHeaders.filter(h => !headers.includes(h))
  if (missingHeaders.length > 0) {
    message.error(`缺少必需的列：${missingHeaders.join(', ')}`)
    return
  }

  const data: any[] = []
  const errors: Array<{ row: number; message: string }> = []
  const devices: DeviceCreate[] = []

  for (let i = 1; i < lines.length; i++) {
    const values = lines[i].split(',').map(v => v.trim().replace(/"/g, ''))
    const rowData: any = { index: i }
    let isValid = true
    let errorMessages: string[] = []

    // 解析每一列
    headers.forEach((header, index) => {
      rowData[header] = values[index] || ''
    })

    // 验证必填字段
    if (!rowData.url) {
      errorMessages.push('设备地址不能为空')
      isValid = false
    } else if (!/^https?:\/\/.+/.test(rowData.url)) {
      errorMessages.push('设备地址格式不正确')
      isValid = false
    }
    if (!rowData.username) {
      errorMessages.push('用户名不能为空')
      isValid = false
    }
    if (!rowData.password) {
      errorMessages.push('密码不能为空')
      isValid = false
    }

    rowData.valid = isValid

    if (errorMessages.length > 0) {
      errors.push({ row: i + 1, message: errorMessages.join('，') })
    }

    if (isValid) {
      devices.push({
        api_base_url: rowData.url,
        username: rowData.username,
        password: rowData.password
      })
    }

    data.push(rowData)
  }

  previewData.value = data.slice(0, 5) // 只显示前5行
  parseErrors.value = errors
  parsedDevices.value = devices

  if (devices.length === 0) {
    message.warning('没有找到有效的设备数据')
  } else {
    message.success(`成功解析 ${devices.length} 个有效设备`)
  }
}

// 移除文件
const handleRemove = () => {
  previewData.value = []
  parseErrors.value = []
  parsedDevices.value = []
  return true
}

// 执行导入
const handleImport = async () => {
  if (parsedDevices.value.length === 0) {
    message.warning('请先上传并解析CSV文件')
    return
  }

  importing.value = true
  try {
    const response = await batchImportDevices(parsedDevices.value)
    if (response.data.success) {
      message.success(`成功导入 ${response.data.imported_count} 个设备`)
      visible.value = false
      emit('import-success')
      resetForm()
    } else {
      message.warning(`导入完成：成功 ${response.data.imported_count} 个，失败 ${response.data.failed_count} 个`)
      if (response.data.failed_devices.length > 0) {
        console.log('失败的设备:', response.data.failed_devices)
      }
    }
  } catch (error: any) {
    message.error('导入失败: ' + (error.response?.data?.detail || error.message))
  } finally {
    importing.value = false
  }
}

// 取消导入
const handleCancel = () => {
  visible.value = false
  resetForm()
}

// 重置表单
const resetForm = () => {
  fileList.value = []
  previewData.value = []
  parseErrors.value = []
  parsedDevices.value = []
}
</script>

<style scoped>
.import-content {
  padding: 16px 0;
}

.import-alert {
  margin-bottom: 16px;
}

.import-alert :deep(.ant-alert-description) {
  margin-top: 8px;
}

.import-alert ul {
  margin: 8px 0 0 0;
  padding-left: 20px;
}

.import-alert li {
  margin-bottom: 4px;
}

.template-section {
  margin-bottom: 16px;
  text-align: center;
}

.upload-area {
  margin-bottom: 16px;
  text-align: center;
}

.preview-section {
  margin-top: 16px;
}

.preview-table {
  margin-bottom: 12px;
}

.preview-info {
  padding: 8px 12px;
  background: var(--bg-secondary);
  border-radius: 6px;
  font-size: 13px;
  color: var(--text-secondary);
}

.error-section {
  margin-top: 16px;
}

:deep(.ant-upload-list) {
  margin-top: 16px;
}

html.dark .preview-info {
  background: var(--bg-tertiary);
}
</style>