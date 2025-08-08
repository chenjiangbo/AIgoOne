<template>
  <div class="dashboard-container">
    <!-- 顶部导航栏 -->
    <header class="top-navbar" :class="{ 'dark-theme': isDarkTheme }">
      <div class="navbar-left">
        <el-button 
          type="text" 
          class="sidebar-toggle-btn"
          @click="sidebarCollapsed = !sidebarCollapsed"
        >
          <el-icon><Fold v-if="!sidebarCollapsed" /><Expand v-else /></el-icon>
        </el-button>
        
        <div class="brand-logo">
          <div class="logo-icon">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <linearGradient id="logoGrad" x2="1" y2="1">
                  <stop offset="0%" stop-color="#3b82f6"/>
                  <stop offset="100%" stop-color="#1d4ed8"/>
                </linearGradient>
              </defs>
              <rect width="32" height="32" rx="6" fill="url(#logoGrad)"/>
              <polygon points="8,12 16,8 24,12 20,16 16,20 12,16" fill="#ffffff" opacity="0.9"/>
              <circle cx="16" cy="24" r="2" fill="#ffffff"/>
            </svg>
          </div>
          <div class="logo-text" v-if="!sidebarCollapsed">
            <span class="brand-name">AIgoOne</span>
            <span class="brand-subtitle">算法管理平台</span>
          </div>
        </div>
      </div>
      
      <div class="navbar-right">
        <el-button 
          type="text" 
          class="nav-btn"
          @click="showSystemConfig"
        >
          <el-icon><Setting /></el-icon>
          系统配置
        </el-button>
        
        <el-button 
          type="text" 
          class="nav-btn"
          @click="showDeviceManagement"
        >
          <el-icon><Monitor /></el-icon>
          设备管理
        </el-button>
        
        <el-button 
          type="text" 
          class="nav-btn"
          @click="showSystemLogs"
        >
          <el-icon><Document /></el-icon>
          系统日志
        </el-button>
        
        <el-divider direction="vertical" />
        
        
        <el-dropdown @command="handleUserCommand">
          <el-avatar :size="36" :src="userAvatar" class="user-avatar" />
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item command="profile">
                <el-icon><User /></el-icon> 个人设置
              </el-dropdown-item>
              <el-dropdown-item command="theme">
                <el-icon><Setting /></el-icon> 偏好设置
              </el-dropdown-item>
              <el-dropdown-item divided command="logout">
                <el-icon><SwitchButton /></el-icon> 退出登录
              </el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </header>
    
    <!-- 主要内容区域 -->
    <main class="main-content">
      <!-- 左侧业务树 -->
      <aside 
        class="business-tree-panel" 
        :class="{ 'collapsed': sidebarCollapsed, 'dark-theme': isDarkTheme }"
        v-show="!sidebarCollapsed"
      >
        <div class="tree-header">
          <div class="tree-title-row">
            <div class="title-search-container">
              <Transition name="search-expand">
                <el-input
                  v-if="searchExpanded"
                  ref="searchInputRef"
                  v-model="treeSearchText"
                  placeholder="搜索业务节点..."
                  size="default"
                  prefix-icon="Search"
                  clearable
                  class="expanded-search"
                  @blur="handleSearchBlur"
                  @keyup.escape="closeSearch"
                />
              </Transition>
              
              <h3 class="tree-title" :class="{ 'invisible': searchExpanded }">业务管理</h3>
              
              <el-button 
                type="text" 
                class="search-expand-btn"
                :class="{ 'invisible': searchExpanded }"
                @click="expandSearch"
              >
                <el-icon><Search /></el-icon>
              </el-button>
            </div>
          </div>
        </div>
        
        <div class="tree-content">
          <el-tree
            ref="businessTreeRef"
            :data="businessTreeData"
            :props="treeProps"
            :filter-node-method="filterNode"
            :allow-drag="allowDrag"
            :allow-drop="allowDrop"
            @node-drag-end="handleDragEnd"
            @node-click="handleNodeClick"
            node-key="id"
            default-expand-all
            draggable
            class="business-tree"
          >
            <template #default="{ node, data }">
              <div class="tree-node">
                <el-icon 
                  v-if="data.type === 'company'" 
                  class="node-icon company"
                  style="color: #3b82f6"
                >
                  <OfficeBuilding />
                </el-icon>
                <el-icon 
                  v-else-if="data.type === 'district'" 
                  class="node-icon district"
                  style="color: #10b981"
                >
                  <MapLocation />
                </el-icon>
                <el-icon 
                  v-else-if="data.type === 'group'" 
                  class="node-icon group"
                  style="color: #f59e0b"
                >
                  <Collection />
                </el-icon>
                <el-icon 
                  v-else-if="data.type === 'parking'" 
                  class="node-icon parking"
                  style="color: #ef4444"
                >
                  <Place />
                </el-icon>
                <span class="node-label">{{ node.label }}</span>
                <span v-if="data.deviceCount" class="device-count">({{ data.deviceCount }})</span>
              </div>
            </template>
          </el-tree>
        </div>
        
        <div class="tree-footer">
          <el-dropdown 
            @command="handleSettingsCommand" 
            trigger="hover"
            class="settings-dropdown"
          >
            <el-button 
              type="text" 
              class="settings-btn"
            >
              <el-icon><Setting /></el-icon>
              设置与帮助
            </el-button>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item command="business-tree">
                  <el-icon><OfficeBuilding /></el-icon>
                  <span>业务树管理</span>
                </el-dropdown-item>
                <el-dropdown-item command="theme" divided>
                  <el-icon><Moon /></el-icon>
                  <span>切换主题</span>
                </el-dropdown-item>
                <el-dropdown-item command="help">
                  <el-icon><QuestionFilled /></el-icon>
                  <span>帮助</span>
                </el-dropdown-item>
                <el-dropdown-item command="feedback">
                  <el-icon><ChatLineSquare /></el-icon>
                  <span>发送反馈</span>
                </el-dropdown-item>
                <el-dropdown-item command="about">
                  <el-icon><InfoFilled /></el-icon>
                  <span>关于</span>
                </el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </aside>
      
      <!-- 右侧内容区域 -->
      <section class="content-area">
        <div v-if="!selectedBusinessUnit" class="welcome-content">
          <div class="welcome-card">
            <div class="welcome-icon">
              <el-icon size="80"><FolderOpened /></el-icon>
            </div>
            <h2>欢迎使用 AIgoOne 算法管理平台</h2>
            <p>请在左侧选择一个业务单元来开始管理</p>
          </div>
        </div>
        
        <div v-else class="tabs-container" :class="{ 'dark-theme': isDarkTheme }">
          <div class="tabs-header">
            <h2 class="business-unit-name">{{ selectedBusinessUnit.name }}</h2>
          </div>
          
          <el-tabs 
            v-model="activeTab" 
            class="business-tabs"
            @tab-click="handleTabClick"
          >
            <el-tab-pane 
              v-if="!selectedBusinessUnit.isLeaf" 
              label="仪表盘" 
              name="dashboard"
            >
              <div class="dashboard-overview">
                <div class="overview-grid">
                  <el-card class="stat-card">
                    <div class="stat-content">
                      <div class="stat-number">{{ getTotalDevices() }}</div>
                      <div class="stat-label">总设备数</div>
                      <el-icon class="stat-icon"><Monitor /></el-icon>
                    </div>
                  </el-card>
                  
                  <el-card class="stat-card">
                    <div class="stat-content">
                      <div class="stat-number">{{ getOnlineDevices() }}</div>
                      <div class="stat-label">在线设备</div>
                      <el-icon class="stat-icon online"><VideoCamera /></el-icon>
                    </div>
                  </el-card>
                  
                  <el-card class="stat-card">
                    <div class="stat-content">
                      <div class="stat-number">{{ getActiveAlarms() }}</div>
                      <div class="stat-label">活跃警报</div>
                      <el-icon class="stat-icon warning"><Bell /></el-icon>
                    </div>
                  </el-card>
                  
                  <el-card class="stat-card">
                    <div class="stat-content">
                      <div class="stat-number">{{ getRegionCount() }}</div>
                      <div class="stat-label">管理区域</div>
                      <el-icon class="stat-icon"><MapLocation /></el-icon>
                    </div>
                  </el-card>
                </div>
                
                <div class="overview-charts">
                  <el-card class="chart-card">
                    <template #header>
                      <div class="chart-header">
                        <span>设备状态分布</span>
                      </div>
                    </template>
                    <div class="chart-placeholder">
                      <!-- 这里可以集成图表库如ECharts -->
                      <div class="mock-chart">
                        <div class="chart-item online">
                          <div class="chart-bar" style="height: 80%"></div>
                          <span>在线</span>
                        </div>
                        <div class="chart-item offline">
                          <div class="chart-bar" style="height: 15%"></div>
                          <span>离线</span>
                        </div>
                        <div class="chart-item error">
                          <div class="chart-bar" style="height: 5%"></div>
                          <span>错误</span>
                        </div>
                      </div>
                    </div>
                  </el-card>
                  
                  <el-card class="chart-card">
                    <template #header>
                      <div class="chart-header">
                        <span>区域设备分布</span>
                      </div>
                    </template>
                    <div class="region-list">
                      <div v-for="region in getRegionStats()" :key="region.id" class="region-item">
                        <div class="region-name">{{ region.name }}</div>
                        <div class="region-progress">
                          <el-progress 
                            :percentage="region.percentage" 
                            :color="region.color"
                            :show-text="false"
                            :stroke-width="8"
                          />
                          <span class="device-count">{{ region.devices }}台</span>
                        </div>
                      </div>
                    </div>
                  </el-card>
                </div>
              </div>
            </el-tab-pane>
            
            <el-tab-pane 
              v-if="selectedBusinessUnit.isLeaf" 
              label="视频源" 
              name="video-sources"
            >
              <VideoSourcesPanel 
                :business-unit="selectedBusinessUnit" 
                :is-dark-theme="isDarkTheme"
                @refresh="refreshData"
              />
            </el-tab-pane>
            
            <el-tab-pane 
              v-if="selectedBusinessUnit.isLeaf" 
              label="任务管理" 
              name="task-management"
            >
              <div class="tab-placeholder">
                <p>任务管理功能开发中...</p>
              </div>
            </el-tab-pane>
            
            <el-tab-pane 
              v-if="selectedBusinessUnit.isLeaf" 
              label="图像服务" 
              name="image-services"
            >
              <div class="tab-placeholder">
                <p>图像服务功能开发中...</p>
              </div>
            </el-tab-pane>
            
            <el-tab-pane 
              v-if="selectedBusinessUnit.isLeaf" 
              label="事件告警" 
              name="event-alerts"
            >
              <div class="tab-placeholder">
                <p>事件告警功能开发中...</p>
              </div>
            </el-tab-pane>
            
            <el-tab-pane 
              v-if="selectedBusinessUnit.isLeaf" 
              label="实时预览" 
              name="live-preview"
            >
              <div class="tab-placeholder">
                <p>实时预览功能开发中...</p>
              </div>
            </el-tab-pane>
          </el-tabs>
        </div>
      </section>
    </main>

    <!-- 设备管理抽屉 -->
    <DeviceManagementDrawer 
      v-model:visible="deviceManagementVisible"
      :is-dark-theme="isDarkTheme"
    />
    
    <!-- 业务树管理对话框 -->
    <BusinessTreeDialog
      v-model:visible="businessTreeDialogVisible"
    />
  </div>
</template>

<script setup>
import { ref, reactive, computed, watch, onMounted, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import {
  Setting,
  Monitor,
  Document,
  CaretBottom,
  OfficeBuilding,
  MapLocation,
  Collection,
  Place,
  FolderOpened,
  Search,
  Fold,
  Expand,
  Moon,
  Sunny,
  User,
  SwitchButton,
  QuestionFilled,
  VideoCamera,
  Bell,
  ChatLineSquare,
  InfoFilled
} from '@element-plus/icons-vue'

// 引入子组件
import VideoSourcesPanel from './components/VideoSourcesPanel.vue'
import DeviceManagementDrawer from '@/components/business/DeviceManagementDrawer.vue'
import BusinessTreeDialog from '@/components/business/BusinessTreeDialog.vue'

const router = useRouter()

// 用户信息
const userName = ref('系统管理员')
const userAvatar = ref('https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png')

// UI状态
const sidebarCollapsed = ref(false)
const searchExpanded = ref(false)
const isDarkTheme = ref(false)
const isMobile = ref(false)
const deviceManagementVisible = ref(false)
const businessTreeDialogVisible = ref(false)

// 业务树相关
const businessTreeRef = ref()
const searchInputRef = ref()
const treeSearchText = ref('')
const selectedBusinessUnit = ref(null)
const activeTab = ref('video-sources')

// 业务树配置
const treeProps = {
  children: 'children',
  label: 'name'
}

// Mock业务树数据
const businessTreeData = ref([
  {
    id: 'company-1',
    name: 'RealEasyInfo科技有限公司',
    type: 'company',
    children: [
      {
        id: 'district-1',
        name: '华东区域',
        type: 'district',
        children: [
          {
            id: 'group-1',
            name: '上海分组',
            type: 'group',
            children: [
              {
                id: 'parking-1',
                name: '虹桥机场T1停车场',
                type: 'parking',
                deviceCount: 12,
                isLeaf: true
              },
              {
                id: 'parking-2',
                name: '虹桥机场T2停车场',
                type: 'parking',
                deviceCount: 8,
                isLeaf: true
              }
            ]
          },
          {
            id: 'group-2',
            name: '杭州分组',
            type: 'group',
            children: [
              {
                id: 'parking-3',
                name: '萧山国际机场停车场',
                type: 'parking',
                deviceCount: 16,
                isLeaf: true
              }
            ]
          }
        ]
      },
      {
        id: 'district-2',
        name: '华北区域',
        type: 'district',
        children: [
          {
            id: 'parking-4',
            name: '首都机场T3停车场',
            type: 'parking',
            deviceCount: 20,
            isLeaf: true
          }
        ]
      }
    ]
  }
])

// 树节点过滤
const filterNode = (value, data) => {
  if (!value) return true
  return data.name.includes(value)
}

// 监听搜索文本变化
watch(treeSearchText, (val) => {
  businessTreeRef.value?.filter(val)
})

// 拖拽相关方法
const allowDrag = (draggingNode) => {
  // 只允许拖拽叶子节点（停车场）
  return draggingNode.data.isLeaf
}

const allowDrop = (draggingNode, dropNode, type) => {
  // 只允许放置到分组节点内部
  return dropNode.data.type === 'group' && type === 'inner'
}

const handleDragEnd = (draggingNode, dropNode, dropType) => {
  ElMessage.success(`已将 ${draggingNode.data.name} 移动到 ${dropNode.data.name} 下`)
}

// 节点点击处理
const handleNodeClick = (data) => {
  selectedBusinessUnit.value = data
  if (data.isLeaf) {
    activeTab.value = 'video-sources'
  } else {
    activeTab.value = 'dashboard'
  }
}

// 获取业务单元路径
const getBusinessUnitPath = (unit) => {
  // 这里应该递归查找父级路径，暂时简化
  return '华东区域 / 上海分组'
}

// 标签页切换
const handleTabClick = (tab) => {
  console.log('切换标签页:', tab.props.name)
}

// 顶部导航功能
const showSystemConfig = () => {
  ElMessage.info('系统配置功能开发中...')
}

const showDeviceManagement = () => {
  deviceManagementVisible.value = true
}

const showSystemLogs = () => {
  ElMessage.info('系统日志功能开发中...')
}

// 搜索功能
const expandSearch = () => {
  searchExpanded.value = true
  nextTick(() => {
    searchInputRef.value?.focus()
  })
}

const handleSearchBlur = () => {
  if (!treeSearchText.value) {
    closeSearch()
  }
}

const closeSearch = () => {
  searchExpanded.value = false
  treeSearchText.value = ''
  businessTreeRef.value?.filter('')
}

// 主题切换
const toggleTheme = () => {
  localStorage.setItem('darkTheme', isDarkTheme.value)
  document.documentElement.classList.toggle('dark', isDarkTheme.value)
  ElMessage.success(isDarkTheme.value ? '已切换到深色主题' : '已切换到浅色主题')
}

// 设置菜单处理
const handleSettingsCommand = (command) => {
  switch (command) {
    case 'business-tree':
      businessTreeDialogVisible.value = true
      break
    case 'theme':
      isDarkTheme.value = !isDarkTheme.value
      toggleTheme()
      break
    case 'help':
      ElMessageBox.alert(
        '这里是帮助文档的内容，包括如何使用系统的各项功能...',
        '帮助文档',
        { confirmButtonText: '我知道了' }
      )
      break
    case 'feedback':
      ElMessage.info('发送反馈功能开发中...')
      break
    case 'about':
      ElMessageBox.alert(
        'AIgoOne 算法管理平台 v1.0\n\n一个用于管理AI算法和视频处理的综合平台。',
        '关于系统',
        { confirmButtonText: '确定' }
      )
      break
  }
}

const handleUserCommand = (command) => {
  switch (command) {
    case 'profile':
      ElMessage.info('个人设置功能开发中...')
      break
    case 'theme':
      ElMessage.info('偏好设置功能开发中...')
      break
    case 'logout':
      ElMessageBox.confirm(
        '确定要退出登录吗？',
        '确认退出',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center: true,
          appendTo: document.body,
          customClass: 'custom-confirm-box',
          closeOnClickModal: false
        }
      ).then(() => {
        localStorage.removeItem('token')
        localStorage.removeItem('user')
        localStorage.removeItem('darkTheme')
        ElMessage.success({
          message: '已退出登录',
          duration: 2000
        })
        router.push('/login')
      }).catch(() => {
        // 取消退出
      })
      break
  }
}

// 仪表盘数据统计方法
const getTotalDevices = () => {
  let total = 0
  const countDevices = (nodes) => {
    nodes.forEach(node => {
      if (node.deviceCount) {
        total += node.deviceCount
      }
      if (node.children) {
        countDevices(node.children)
      }
    })
  }
  countDevices(businessTreeData.value)
  return total
}

const getOnlineDevices = () => {
  return Math.floor(getTotalDevices() * 0.85) // 假设85%在线
}

const getActiveAlarms = () => {
  return Math.floor(getTotalDevices() * 0.03) // 假设3%有警报
}

const getRegionCount = () => {
  return businessTreeData.value[0]?.children?.length || 0
}

const getRegionStats = () => {
  const stats = []
  const regions = businessTreeData.value[0]?.children || []
  
  regions.forEach(region => {
    let deviceCount = 0
    const countRegionDevices = (nodes) => {
      nodes.forEach(node => {
        if (node.deviceCount) {
          deviceCount += node.deviceCount
        }
        if (node.children) {
          countRegionDevices(node.children)
        }
      })
    }
    
    if (region.children) {
      countRegionDevices(region.children)
    }
    
    const total = getTotalDevices()
    stats.push({
      id: region.id,
      name: region.name,
      devices: deviceCount,
      percentage: total > 0 ? Math.round((deviceCount / total) * 100) : 0,
      color: region.id === 'district-1' ? '#3b82f6' : '#10b981'
    })
  })
  
  return stats
}

// 刷新数据
const refreshData = () => {
  console.log('刷新数据')
}

onMounted(() => {
  // 检查登录状态
  const token = localStorage.getItem('token')
  if (!token) {
    router.push('/')
    return
  }
  
  // 获取用户信息
  const user = JSON.parse(localStorage.getItem('user') || '{}')
  if (user.name) {
    userName.value = user.name
  }
  
  // 恢复主题设置
  const savedTheme = localStorage.getItem('darkTheme')
  if (savedTheme === 'true') {
    isDarkTheme.value = true
    document.documentElement.classList.add('dark')
  }
  
  // 检查屏幕尺寸
  const checkScreenSize = () => {
    isMobile.value = window.innerWidth < 768
    if (isMobile.value) {
      sidebarCollapsed.value = true
    }
  }
  checkScreenSize()
  window.addEventListener('resize', checkScreenSize)
})
</script>

<style scoped>
.dashboard-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: #f5f7fa;
}

/* 顶部导航栏 */
.top-navbar {
  height: 50px;
  background: #3b82f6;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  transition: all 0.3s ease;
}

.top-navbar.dark-theme {
  background: #111827;
  border-bottom-color: rgba(255, 255, 255, 0.05);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.navbar-left {
  display: flex;
  align-items: center;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-icon svg {
  width: 32px;
  height: 32px;
}

.logo-text {
  display: flex;
  flex-direction: column;
}

.sidebar-toggle-btn {
  margin-right: 16px;
  color: white;
  padding: 8px;
}

.sidebar-toggle-btn:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.brand-name {
  font-size: 20px;
  font-weight: 600;
  color: white;
  line-height: 1;
}

.brand-subtitle {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.8);
  line-height: 1;
}

.navbar-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.nav-btn {
  color: rgba(255, 255, 255, 0.9);
  font-size: 14px;
  padding: 8px 16px;
}

.nav-btn:hover {
  color: white;
  background-color: rgba(255, 255, 255, 0.1);
}

.user-avatar {
  cursor: pointer;
  border: 2px solid rgba(255, 255, 255, 0.3);
  transition: all 0.3s ease;
}

.user-avatar:hover {
  border-color: white;
  transform: scale(1.05);
}


/* 主要内容区域 */
.main-content {
  flex: 1;
  display: flex;
  overflow: hidden;
}

/* 左侧业务树 */
.business-tree-panel {
  width: 300px;
  background: #ffffff;
  border-right: 1px solid #e4e7ed;
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
}

.business-tree-panel.collapsed {
  width: 0;
  min-width: 0;
  border-right: none;
}

.business-tree-panel.dark-theme {
  background: #1f2937;
  border-right-color: #374151;
}

.tree-header {
  padding: 20px;
  border-bottom: 1px solid #e4e7ed;
}

.tree-title-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.title-search-container {
  position: relative;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.tree-title {
  margin: 0;
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
}

.business-tree-panel.dark-theme .tree-title {
  color: #f3f4f6;
}

.expanded-search {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  z-index: 10;
  border-radius: 18px;
}

.expanded-search :deep(.el-input__wrapper) {
  border-radius: 18px;
  height: 36px;
}

.invisible {
  visibility: hidden;
}

.search-expand-btn {
  color: #909399;
  padding: 8px;
  border-radius: 6px;
  transition: all 0.3s ease;
}

.search-expand-btn:hover {
  color: #3b82f6;
  background-color: rgba(59, 130, 246, 0.1);
}

/* 搜索展开动画 */
.search-expand-enter-active,
.search-expand-leave-active {
  transition: all 0.3s ease;
}

.search-expand-enter-from {
  opacity: 0;
  transform: translateX(50px);
}

.search-expand-leave-to {
  opacity: 0;
  transform: translateX(50px);
}

.tree-content {
  flex: 1;
  padding: 16px;
  overflow-y: auto;
}

.business-tree {
  background: transparent;
}

:deep(.business-tree .el-tree-node__content) {
  height: 40px;
  padding-left: 16px;
  border-radius: 6px;
  margin: 2px 0;
  transition: all 0.2s;
}

:deep(.business-tree .el-tree-node__content:hover) {
  background-color: #f0f9ff;
}

:deep(.business-tree .is-current > .el-tree-node__content) {
  background-color: #3b82f6;
  color: white;
}

.tree-node {
  display: flex;
  align-items: center;
  gap: 8px;
  flex: 1;
}

.tree-footer {
  padding: 12px 20px;
  border-top: 1px solid #e4e7ed;
  background: #f8fafc;
}

.business-tree-panel.dark-theme .tree-footer {
  border-top-color: #374151;
  background: #111827;
}

.settings-dropdown {
  width: 100%;
}

.settings-btn {
  width: 100%;
  color: #6b7280;
  font-size: 14px;
  justify-content: flex-start;
  height: 32px;
  padding: 6px 8px;
  border-radius: 6px;
  transition: all 0.3s ease;
  background: transparent !important;
  border: none !important;
}

.settings-btn:hover {
  color: #3b82f6 !important;
  background-color: rgba(59, 130, 246, 0.1) !important;
}

.business-tree-panel.dark-theme .settings-btn {
  color: #9ca3af;
  background: transparent !important;
}

.business-tree-panel.dark-theme .settings-btn:hover {
  color: #60a5fa !important;
  background-color: rgba(96, 165, 250, 0.1) !important;
}

.node-label {
  flex: 1;
  font-size: 14px;
}

.device-count {
  font-size: 12px;
  color: #909399;
}

/* 右侧内容区域 */
.content-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.welcome-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #ffffff;
}

.welcome-card {
  text-align: center;
  padding: 40px;
}

.welcome-icon {
  margin-bottom: 24px;
  color: #c0c4cc;
}

.welcome-card h2 {
  font-size: 24px;
  color: #2c3e50;
  margin: 0 0 16px 0;
}

.welcome-card p {
  font-size: 16px;
  color: #909399;
  margin: 0;
}

.tabs-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: #ffffff;
}

.tabs-container.dark-theme {
  background: #1f2937;
}

.tabs-header {
  padding: 20px 24px 16px;
}

.business-unit-name {
  font-size: 20px;
  font-weight: 600;
  color: #2c3e50;
  margin: 0;
}

.tabs-container.dark-theme .business-unit-name {
  color: #f3f4f6;
}

.business-tabs {
  flex: 1;
  padding: 0 24px;
}

:deep(.business-tabs .el-tabs__header) {
  margin: 0;
}

:deep(.business-tabs .el-tabs__content) {
  height: calc(100vh - 186px);
  overflow-y: auto;
}

.tab-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 200px;
  color: #909399;
  font-size: 16px;
}

/* 仪表盘样式 */
.dashboard-overview {
  padding: 20px;
  height: 100%;
  overflow-y: auto;
}

.overview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 24px;
}

.stat-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  border-radius: 12px;
  overflow: hidden;
}

.stat-card :deep(.el-card__body) {
  padding: 20px;
  background: transparent;
}

.stat-content {
  color: white;
  text-align: center;
  position: relative;
}

.stat-number {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 8px;
}

.stat-label {
  font-size: 14px;
  opacity: 0.9;
  margin-bottom: 12px;
}

.stat-icon {
  font-size: 20px;
  opacity: 0.8;
  position: absolute;
  top: 0;
  right: 0;
}

.stat-icon.online {
  color: #67c23a;
}

.stat-icon.warning {
  color: #f56c6c;
}

.overview-charts {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.chart-card {
  border-radius: 12px;
}

.chart-header {
  font-weight: 600;
  font-size: 16px;
}

.chart-placeholder {
  height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.mock-chart {
  display: flex;
  align-items: end;
  gap: 20px;
  height: 200px;
}

.chart-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.chart-bar {
  width: 40px;
  background: var(--el-color-primary);
  border-radius: 4px 4px 0 0;
  transition: all 0.3s ease;
}

.chart-item.online .chart-bar {
  background: #67c23a;
}

.chart-item.offline .chart-bar {
  background: #909399;
}

.chart-item.error .chart-bar {
  background: #f56c6c;
}

.region-list {
  padding: 20px 0;
}

.region-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
  padding: 12px 0;
  border-bottom: 1px solid #f0f0f0;
}

.region-name {
  font-weight: 500;
  color: #2c3e50;
  min-width: 120px;
}

.region-progress {
  display: flex;
  align-items: center;
  gap: 12px;
  flex: 1;
  max-width: 200px;
}

.device-count {
  font-size: 14px;
  color: #666;
  min-width: 40px;
}

/* 暗色主题下的仪表盘 */
html.dark .stat-card {
  background: linear-gradient(135deg, #374151 0%, #1f2937 100%);
}

html.dark .region-item {
  border-bottom-color: #374151;
}

html.dark .region-name {
  color: #f3f4f6;
}

/* 响应式调整 */
@media (max-width: 1024px) {
  .overview-charts {
    grid-template-columns: 1fr;
  }
  
  .overview-grid {
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  }
}

/* 响应式设计 */
@media (max-width: 768px) {
  .business-tree-panel {
    width: 250px;
  }
  
  .navbar-right .nav-btn span {
    display: none;
  }
  
  .brand-subtitle {
    display: none;
  }
}
</style>