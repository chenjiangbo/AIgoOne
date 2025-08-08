<template>
  <div class="stats-cards">
    <div class="stat-card total">
      <div class="stat-content">
        <span class="stat-number">{{ stats.total }}</span>
        <span class="stat-label">总设备数</span>
      </div>
      <el-icon class="stat-icon"><Monitor /></el-icon>
    </div>
    
    <div class="stat-card online">
      <div class="stat-content">
        <span class="stat-number">{{ stats.online }}</span>
        <span class="stat-label">在线设备</span>
      </div>
      <el-icon class="stat-icon"><CircleCheck /></el-icon>
    </div>
    
    <div class="stat-card offline">
      <div class="stat-content">
        <span class="stat-number">{{ stats.offline }}</span>
        <span class="stat-label">离线设备</span>
      </div>
      <el-icon class="stat-icon"><CircleClose /></el-icon>
    </div>
    
    <div class="stat-card error">
      <div class="stat-content">
        <span class="stat-number">{{ stats.error }}</span>
        <span class="stat-label">异常设备</span>
      </div>
      <el-icon class="stat-icon"><Warning /></el-icon>
    </div>
  </div>
</template>

<script setup>
import { Monitor, CircleCheck, CircleClose, Warning } from '@element-plus/icons-vue'

// Props
const props = defineProps({
  stats: {
    type: Object,
    default: () => ({
      total: 0,
      online: 0,
      offline: 0,
      error: 0
    })
  }
})
</script>

<style scoped>
.stats-cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--spacing-4);
  padding: var(--spacing-4);
  flex-shrink: 0;
}

.stat-card {
  position: relative;
  padding: var(--spacing-3) var(--spacing-4);
  background: linear-gradient(135deg, var(--color-primary-500) 0%, var(--color-primary-600) 100%);
  border-radius: var(--border-radius-lg);
  color: white;
  display: flex;
  align-items: center;
  justify-content: space-between;
  overflow: hidden;
  transition: var(--transition-transform);
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.stat-card.total {
  background: linear-gradient(135deg, var(--color-primary-500) 0%, var(--color-primary-600) 100%);
}

.stat-card.online {
  background: linear-gradient(135deg, var(--color-success-400) 0%, var(--color-success-500) 100%);
}

.stat-card.offline {
  background: linear-gradient(135deg, var(--color-info-400) 0%, var(--color-info-500) 100%);
}

.stat-card.error {
  background: linear-gradient(135deg, var(--color-error-400) 0%, var(--color-error-500) 100%);
}

.stat-content {
  display: flex;
  align-items: baseline;
  gap: var(--spacing-2);
}

.stat-number {
  font-size: var(--font-size-3xl);
  font-weight: var(--font-weight-bold);
  line-height: 1;
}

.stat-label {
  font-size: var(--font-size-sm);
  opacity: 0.9;
  line-height: 1;
}

.stat-icon {
  font-size: var(--font-size-xl);
  opacity: 0.7;
  flex-shrink: 0;
}

/* 响应式设计 */
@media (max-width: 1200px) {
  .stats-cards {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .stats-cards {
    grid-template-columns: 1fr;
  }
}
</style>