<template>
  <a-layout class="dashboard-container">
    <!-- 顶部导航栏 -->
    <a-layout-header class="top-navbar">
      <div class="navbar-left">
        <a-button 
          type="text" 
          class="sidebar-toggle-btn"
          @click="toggleSidebar"
        >
          <MenuFoldOutlined v-if="!sidebarCollapsed" />
          <MenuUnfoldOutlined v-else />
        </a-button>
        
        <div class="brand-logo">
          <div class="logo-icon">
            <img src="/logo.svg" alt="AIgoOne Logo" style="width: 32px; height: 32px;" />
          </div>
          <div class="logo-text" v-if="!sidebarCollapsed">
            <span class="brand-name">AIgoOne</span>
            <span class="brand-subtitle">算法管理平台</span>
          </div>
        </div>
      </div>
      
      <div class="navbar-right">
        <a-dropdown>
          <a-button type="text" class="nav-btn">
            <SettingOutlined />
            <span>系统配置</span>
            <DownOutlined />
          </a-button>
          <template #overlay>
            <a-menu @click="handleSystemMenuClick">
              <a-menu-item key="config">
                <SettingOutlined /> 系统配置
              </a-menu-item>
              <a-menu-item key="logs">
                <FileTextOutlined /> 系统日志
              </a-menu-item>
            </a-menu>
          </template>
        </a-dropdown>
        
        <a-button type="text" class="nav-btn" @click="showDeviceManagement">
          <DesktopOutlined />
          <span>设备管理</span>
        </a-button>
        
        <!-- 主题切换按钮 -->
        <a-tooltip :title="`切换到${appStore.isDarkTheme ? '亮色' : '暗色'}主题`">
          <a-button type="text" class="nav-btn theme-toggle-btn" @click="toggleTheme">
            <BulbOutlined v-if="!appStore.isDarkTheme" />
            <BulbFilled v-else />
          </a-button>
        </a-tooltip>
        
        <a-divider type="vertical" />
        
        <a-dropdown>
          <a-avatar :size="36" :src="userAvatar" class="user-avatar">
            <template #icon>
              <UserOutlined />
            </template>
          </a-avatar>
          <template #overlay>
            <a-menu @click="handleUserMenuClick">
              <a-menu-item key="profile">
                <UserOutlined /> 个人设置
              </a-menu-item>
              <a-menu-item key="theme-toggle">
                <template #icon>
                  <BulbOutlined v-if="!appStore.isDarkTheme" />
                  <BulbFilled v-else />
                </template>
                {{ appStore.isDarkTheme ? '切换到亮色主题' : '切换到暗色主题' }}
              </a-menu-item>
              <a-menu-item key="preferences">
                <SettingOutlined /> 偏好设置
              </a-menu-item>
              <a-menu-divider />
              <a-menu-item key="logout">
                <LogoutOutlined /> 退出登录
              </a-menu-item>
            </a-menu>
          </template>
        </a-dropdown>
      </div>
    </a-layout-header>
    
    <a-layout class="main-layout">
      <!-- 左侧业务树 -->
      <a-layout-sider 
        v-model:collapsed="sidebarCollapsed"
        :trigger="null"
        collapsible
        :width="350"
        :collapsed-width="0"
        class="business-tree-panel"
      >
        <div class="tree-header">
          <div class="tree-title-row">
            <div class="title-search-container">
              <Transition name="search-expand">
                <a-input
                  v-if="searchExpanded"
                  ref="searchInputRef"
                  v-model:value="treeSearchText"
                  placeholder="搜索业务节点..."
                  size="default"
                  allow-clear
                  class="expanded-search"
                  @blur="handleSearchBlur"
                  @keyup.escape="closeSearch"
                >
                  <template #prefix>
                    <SearchOutlined />
                  </template>
                </a-input>
              </Transition>
              
              <h3 class="tree-title" :class="{ 'invisible': searchExpanded }">业务管理</h3>
              
              <a-button 
                type="text" 
                size="small"
                class="search-expand-btn"
                :class="{ 'invisible': searchExpanded }"
                @click="expandSearch"
              >
                <SearchOutlined />
              </a-button>
            </div>
          </div>
        </div>
        
        <div class="tree-content">
          <a-tree
            v-model:selectedKeys="selectedKeys"
            v-model:expandedKeys="expandedKeys"
            :tree-data="businessTreeData"
            :field-names="{ title: 'name', key: 'id', children: 'children' }"
            @select="handleNodeClick"
            show-icon
          >
            <template #icon="{ dataRef }">
              <ApartmentOutlined v-if="dataRef.type === 'company'" style="color: #3b82f6; font-size: 16px;" />
              <GlobalOutlined v-else-if="dataRef.type === 'district'" style="color: #10b981; font-size: 16px;" />
              <TeamOutlined v-else-if="dataRef.type === 'group'" style="color: #f59e0b; font-size: 16px;" />
              <VideoCameraOutlined v-else-if="dataRef.type === 'parking'" style="color: #ef4444; font-size: 16px;" />
            </template>
          </a-tree>
        </div>
        
        <div class="tree-footer">
          <a-dropdown>
            <a-button type="text" block>
              <SettingOutlined /> 设置与帮助
            </a-button>
            <template #overlay>
              <a-menu @click="handleSettingsClick">
                <a-menu-item key="business-tree">
                  <BankOutlined /> 业务树管理
                </a-menu-item>
                <a-menu-divider />
                <a-menu-item key="theme-toggle">
                  <template #icon>
                    <BulbOutlined v-if="!appStore.isDarkTheme" />
                    <BulbFilled v-else />
                  </template>
                  {{ appStore.isDarkTheme ? '亮色主题' : '暗色主题' }}
                </a-menu-item>
                <a-menu-divider />
                <a-menu-item key="help">
                  <QuestionCircleOutlined /> 帮助
                </a-menu-item>
                <a-menu-item key="about">
                  <InfoCircleOutlined /> 关于
                </a-menu-item>
              </a-menu>
            </template>
          </a-dropdown>
        </div>
      </a-layout-sider>
      
      <!-- 右侧内容区域 -->
      <a-layout-content class="content-area">
        <div v-if="!selectedBusinessUnit" class="welcome-content">
          <a-empty description="请在左侧选择一个业务单元来开始管理">
            <template #image>
              <FolderOpenOutlined style="font-size: 80px; color: #c0c4cc" />
            </template>
          </a-empty>
        </div>
        
        <div v-else class="tabs-container">
          <div class="tabs-header">
            <h2 class="business-unit-name">{{ selectedBusinessUnit.name }}</h2>
          </div>
          
          <a-tabs v-model:activeKey="activeTab" @change="handleTabChange">
            <a-tab-pane v-if="!selectedBusinessUnit.isLeaf" key="dashboard" tab="仪表盘">
              <div class="dashboard-overview">
                <a-row :gutter="[16, 16]">
                  <a-col :xs="24" :sm="12" :md="6">
                    <a-card class="stat-card">
                      <a-statistic title="总设备数" :value="56" />
                    </a-card>
                  </a-col>
                  <a-col :xs="24" :sm="12" :md="6">
                    <a-card class="stat-card">
                      <a-statistic title="在线设备" :value="48" value-style="color: #52c41a" />
                    </a-card>
                  </a-col>
                  <a-col :xs="24" :sm="12" :md="6">
                    <a-card class="stat-card">
                      <a-statistic title="活跃警报" :value="3" value-style="color: #f5222d" />
                    </a-card>
                  </a-col>
                  <a-col :xs="24" :sm="12" :md="6">
                    <a-card class="stat-card">
                      <a-statistic title="管理区域" :value="2" />
                    </a-card>
                  </a-col>
                </a-row>
              </div>
            </a-tab-pane>
            
            <a-tab-pane v-if="selectedBusinessUnit.isLeaf" key="video-sources" tab="视频源">
              <VideoSourcesPanel :business-unit="selectedBusinessUnit" @refresh="handleRefresh" />
            </a-tab-pane>
            
            <a-tab-pane v-if="selectedBusinessUnit.isLeaf" key="device-management" tab="设备管理">
              <DeviceManagement />
            </a-tab-pane>
            
            <a-tab-pane v-if="selectedBusinessUnit.isLeaf" key="task-management" tab="任务管理">
              <TaskManagement />
            </a-tab-pane>
            
            <a-tab-pane v-if="selectedBusinessUnit.isLeaf" key="event-alerts" tab="事件告警">
              <EventAlerts />
            </a-tab-pane>
          </a-tabs>
        </div>
      </a-layout-content>
    </a-layout>
    
    <!-- 系统配置模态框 -->
    <a-modal
      v-model:open="systemConfigVisible"
      title="系统配置"
      width="1200px"
      :footer="null"
      :destroy-on-close="true"
    >
      <SystemConfig />
    </a-modal>
    
    <!-- 系统日志模态框 -->
    <a-modal
      v-model:open="systemLogsVisible"
      title="系统日志"
      width="1200px"
      :footer="null"
      :destroy-on-close="true"
    >
      <SystemLogs />
    </a-modal>
    
    <!-- 设备管理抽屉 -->
    <DeviceManagementDrawer v-model:visible="deviceManagementVisible" />
  </a-layout>
</template>

<script setup lang="ts">
import { ref, onMounted, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import { message, Modal } from 'ant-design-vue'
import {
  MenuFoldOutlined,
  MenuUnfoldOutlined,
  UserOutlined,
  SettingOutlined,
  LogoutOutlined,
  SearchOutlined,
  ApartmentOutlined,
  GlobalOutlined,
  TeamOutlined,
  VideoCameraOutlined,
  DesktopOutlined,
  FileTextOutlined,
  FolderOpenOutlined,
  QuestionCircleOutlined,
  InfoCircleOutlined,
  BankOutlined,
  DownOutlined,
  BulbOutlined,
  BulbFilled
} from '@ant-design/icons-vue'
import { useAppStore, useUserStore } from '@/store'
import VideoSourcesPanel from './components/VideoSourcesPanel.vue'
import DeviceManagement from './components/DeviceManagement.vue'
import TaskManagement from './components/TaskManagement.vue'
import EventAlerts from './components/EventAlerts.vue'
import SystemConfig from './components/SystemConfig.vue'
import SystemLogs from './components/SystemLogs.vue'
import { DeviceManagementDrawer } from '@/components/device'

const router = useRouter()
const appStore = useAppStore()
const userStore = useUserStore()

// UI状态
const sidebarCollapsed = ref(false)
const searchExpanded = ref(false)
const selectedKeys = ref<string[]>([])
const expandedKeys = ref<string[]>(['company-1', 'district-1', 'district-2', 'group-1', 'group-2']) // 全部展开
const selectedBusinessUnit = ref<any>(null)
const activeTab = ref('video-sources')

// 搜索相关
const searchInputRef = ref()
const treeSearchText = ref('')

// 弹窗状态
const systemConfigVisible = ref(false)
const systemLogsVisible = ref(false)
const deviceManagementVisible = ref(false)

// 用户信息
const userAvatar = ref('/avatar-default.svg')

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

// 切换侧边栏
const toggleSidebar = () => {
  sidebarCollapsed.value = !sidebarCollapsed.value
  appStore.toggleSidebar()
}

// 节点点击处理
const handleNodeClick = (selectedKeys: string[], { node }: any) => {
  selectedBusinessUnit.value = node.dataRef
  if (node.dataRef.isLeaf) {
    activeTab.value = 'video-sources'
  } else {
    activeTab.value = 'dashboard'
  }
}

// 标签页切换
const handleTabChange = (key: string) => {
  console.log('切换标签页:', key)
}

// 顶部导航功能
const handleSystemMenuClick = ({ key }: any) => {
  switch (key) {
    case 'config':
      systemConfigVisible.value = true
      break
    case 'logs':
      systemLogsVisible.value = true
      break
  }
}

const showDeviceManagement = () => {
  deviceManagementVisible.value = true
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
  // 这里可以添加树过滤的逻辑
}

// 主题切换
const toggleTheme = () => {
  appStore.toggleTheme()
  message.success(`已切换到${appStore.isDarkTheme ? '暗色' : '亮色'}主题`)
}

// 用户菜单处理
const handleUserMenuClick = ({ key }: any) => {
  switch (key) {
    case 'profile':
      message.info('个人设置功能开发中...')
      break
    case 'theme-toggle':
      appStore.toggleTheme()
      message.success(`已切换到${appStore.isDarkTheme ? '暗色' : '亮色'}主题`)
      break
    case 'preferences':
      message.info('偏好设置功能开发中...')
      break
    case 'logout':
      Modal.confirm({
        title: '确认退出',
        content: '确定要退出登录吗？',
        okText: '确定',
        cancelText: '取消',
        onOk: () => {
          userStore.logout()
          message.success('已退出登录')
          router.push('/login')
        }
      })
      break
  }
}

// 设置菜单处理
const handleSettingsClick = ({ key }: any) => {
  switch (key) {
    case 'business-tree':
      message.info('业务树管理功能开发中...')
      break
    case 'theme-toggle':
      appStore.toggleTheme()
      message.success(`已切换到${appStore.isDarkTheme ? '暗色' : '亮色'}主题`)
      break
    case 'help':
      message.info('帮助文档开发中...')
      break
    case 'about':
      Modal.info({
        title: '关于系统',
        content: 'AIgoOne 算法管理平台 v1.0'
      })
      break
  }
}

// 处理刷新事件
const handleRefresh = () => {
  console.log('刷新数据')
}

onMounted(() => {
  // 检查登录状态
  if (!userStore.isLoggedIn) {
    router.push('/login')
  }
})
</script>

<style lang="less" scoped>
// 导入全局CSS变量
@import '@/styles/variables.less';

.dashboard-container {
  width: 100vw;
  height: 100vh;
  background-color: var(--bg-secondary);
}

// 顶部导航栏
.top-navbar {
  background: var(--navbar-bg);
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
  line-height: 64px;
  border-bottom: 1px solid var(--border-light);
  
  .navbar-left {
    display: flex;
    align-items: center;
    
    .sidebar-toggle-btn {
      color: var(--navbar-text);
      font-size: 16px;
      margin-right: 16px;
      padding: 8px;
      
      &:hover {
        background-color: var(--navbar-hover);
      }
    }
    
    .brand-logo {
      display: flex;
      align-items: center;
      gap: 12px;
      
      .logo-icon {
        display: flex;
        align-items: center;
        justify-content: center;
      }
      
      .logo-text {
        display: flex;
        flex-direction: column;
        line-height: 1.2;
        
        .brand-name {
          font-size: 20px;
          font-weight: 600;
          line-height: 24px;
          background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #ffeaa7, #fab1a0);
          background-size: 400% 400%;
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          background-clip: text;
          animation: colorShift 3s ease-in-out infinite;
        }
        
        .brand-subtitle {
          font-size: 12px;
          color: var(--navbar-text);
          opacity: 0.8;
          line-height: 14px;
          margin-top: 2px;
        }
      }
    }
  }
  
  .navbar-right {
    display: flex;
    align-items: center;
    gap: 16px;
    
    .nav-btn {
      color: var(--navbar-text);
      
      &:hover {
        background-color: var(--navbar-hover);
      }
      
      // 主题切换按钮特殊样式
      &.theme-toggle-btn {
        transition: all 0.3s ease;
        
        &:hover {
          background-color: var(--navbar-hover);
          transform: scale(1.1);
        }
        
        &:active {
          transform: scale(0.95);
        }
      }
    }
    
    .user-avatar {
      cursor: pointer;
      background-color: var(--navbar-hover);
      
      &:hover {
        background-color: var(--navbar-hover);
        opacity: 0.8;
      }
    }
  }
}

// 主布局
.main-layout {
  height: calc(100vh - 64px);
}

// 左侧业务树
.business-tree-panel {
  background: var(--sidebar-bg);
  border-right: 1px solid var(--sidebar-border);
  display: flex;
  flex-direction: column;
  height: calc(100vh - 64px);
  position: relative;
  
  .tree-header {
    padding: 16px;
    border-bottom: 1px solid var(--sidebar-border);
    background: var(--sidebar-header-bg);
    flex-shrink: 0;
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
    color: var(--text-primary);
    
    &.invisible {
      visibility: hidden;
    }
  }
  
  .expanded-search {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    z-index: 10;
    border-radius: 18px;
    
    :deep(.ant-input) {
      border-radius: 18px;
      height: 36px;
    }
  }
  
  .search-expand-btn {
    color: var(--text-tertiary);
    padding: 8px;
    border-radius: 6px;
    transition: all 0.3s ease;
    
    &:hover {
      color: var(--color-primary);
      background-color: var(--bg-hover);
    }
    
    &.invisible {
      visibility: hidden;
    }
  }
  
  .tree-content {
    flex: 1;
    padding: 16px;
    padding-bottom: 57px; // 为绝对定位的footer留空间
    overflow: hidden; // 在收起动画时防止出现滚动条
    min-height: 0;
    
    // 只有当侧边栏完全展开时才显示滚动条
    &:not(.collapsed) {
      overflow-y: auto;
    }
    
    :deep(.ant-tree) {
      font-size: 14px;
      
      .ant-tree-treenode {
        margin-bottom: 4px;
      }
      
      .ant-tree-node-content-wrapper {
        font-size: 14px;
        padding: 4px 8px;
        height: 32px;
        display: flex;
        align-items: center;
      }
      
      .ant-tree-title {
        font-size: 14px;
        line-height: 24px;
      }
      
      .ant-tree-iconEle {
        margin-right: 8px;
      }
    }
  }
  
  .tree-footer {
    border-top: 1px solid var(--sidebar-border);
    background: var(--sidebar-footer-bg);
    padding: 8px;
    flex-shrink: 0;
    height: 57px;
    display: flex;
    align-items: center;
    justify-content: center;
    
    // 绝对定位到底部的关键：使用 position
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    
    :deep(.ant-btn) {
      color: var(--text-tertiary);
      font-size: 14px;
      width: 100%;
      justify-content: flex-start;
      
      &:hover {
        color: var(--color-primary);
        background-color: var(--bg-hover);
      }
    }
  }
}

// 右侧内容区域
.content-area {
  padding: 24px;
  background: var(--bg-secondary);
  overflow-y: auto;
  
  .welcome-content {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
  }
  
  .tabs-container {
    background: var(--bg-primary);
    border: 1px solid var(--border-light);
    border-radius: 8px;
    padding: 24px;
    box-shadow: var(--shadow-light);
    
    .tabs-header {
      margin-bottom: 24px;
      
      .business-unit-name {
        margin: 0;
        font-size: 20px;
        font-weight: 600;
        color: var(--text-primary);
      }
    }
    
    .dashboard-overview {
      .stat-card {
        height: 100%;
      }
    }
    
    .tab-content {
      min-height: 400px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #909399;
      font-size: 16px;
    }
  }
}

// 搜索展开动画
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

// 彩色变换动画
@keyframes colorShift {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
</style>