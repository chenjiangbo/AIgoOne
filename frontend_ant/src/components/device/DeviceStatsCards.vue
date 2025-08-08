<template>
  <div class="stats-cards">
    <a-row :gutter="16">
      <!-- 总设备数 -->
      <a-col :xs="24" :sm="6">
        <div class="stat-card total">
          <div class="stat-icon">
            <a-avatar :size="40" style="background: var(--color-primary-500)">
              <template #icon>
                <DatabaseOutlined />
              </template>
            </a-avatar>
          </div>
          <div class="stat-content">
            <div class="stat-title">总设备</div>
            <div class="stat-value">{{ stats.total }}</div>
          </div>
        </div>
      </a-col>

      <!-- 在线设备 -->
      <a-col :xs="24" :sm="6">
        <div class="stat-card online">
          <div class="stat-icon">
            <a-avatar :size="40" style="background: var(--color-success-500)">
              <template #icon>
                <CheckCircleOutlined />
              </template>
            </a-avatar>
          </div>
          <div class="stat-content">
            <div class="stat-title">在线设备</div>
            <div class="stat-value">{{ stats.online }}</div>
          </div>
        </div>
      </a-col>

      <!-- 离线设备 -->
      <a-col :xs="24" :sm="6">
        <div class="stat-card offline">
          <div class="stat-icon">
            <a-avatar :size="40" style="background: var(--color-neutral-400)">
              <template #icon>
                <MinusCircleOutlined />
              </template>
            </a-avatar>
          </div>
          <div class="stat-content">
            <div class="stat-title">离线设备</div>
            <div class="stat-value">{{ stats.offline }}</div>
          </div>
        </div>
      </a-col>

      <!-- 验证失败设备 -->
      <a-col :xs="24" :sm="6">
        <div class="stat-card error">
          <div class="stat-icon">
            <a-avatar :size="40" style="background: var(--color-error-500)">
              <template #icon>
                <ExclamationCircleOutlined />
              </template>
            </a-avatar>
          </div>
          <div class="stat-content">
            <div class="stat-title">验证失败</div>
            <div class="stat-value">{{ stats.error }}</div>
          </div>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script setup lang="ts">
import {
  DatabaseOutlined,
  CheckCircleOutlined,
  MinusCircleOutlined,
  ExclamationCircleOutlined
} from '@ant-design/icons-vue'

interface DeviceStats {
  total: number
  online: number
  offline: number
  error: number
}

interface Props {
  stats: DeviceStats
}

withDefaults(defineProps<Props>(), {
  stats: () => ({
    total: 0,
    online: 0,
    offline: 0,
    error: 0
  })
})
</script>

<style scoped>
.stats-cards {
  padding: 16px 24px 0;
  background: var(--bg-primary);
}

.stat-card {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px;
  background: var(--bg-primary);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  transition: all 0.3s ease;
  height: 80px;
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  border-color: var(--color-primary-300);
}

.stat-icon {
  flex-shrink: 0;
}

.stat-content {
  flex: 1;
  min-width: 0;
}

.stat-title {
  font-size: 14px;
  color: var(--text-secondary);
  margin-bottom: 4px;
  line-height: 1;
}

.stat-value {
  font-size: 24px;
  font-weight: 600;
  color: var(--text-primary);
  line-height: 1;
}

/* 响应式调整 */
@media (max-width: 768px) {
  .stats-cards :deep(.ant-col) {
    margin-bottom: 12px;
  }
  
  .stat-card {
    height: 70px;
    padding: 16px;
  }
  
  .stat-value {
    font-size: 20px;
  }
  
  .stat-icon :deep(.ant-avatar) {
    width: 32px !important;
    height: 32px !important;
    font-size: 16px;
  }
}

/* 暗色主题适配 */
html.dark .stats-cards {
  background: var(--bg-secondary);
}

html.dark .stat-card {
  background: var(--bg-primary);
  border-color: var(--border-color-dark);
}

html.dark .stat-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  border-color: var(--color-primary-400);
}
</style>