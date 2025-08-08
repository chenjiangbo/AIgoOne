import { defineStore } from 'pinia'

// 用户状态管理
export const useUserStore = defineStore('user', {
  state: () => ({
    token: localStorage.getItem('token') || '',
    userInfo: null,
    permissions: []
  }),
  
  getters: {
    isLoggedIn: (state) => !!state.token
  },
  
  actions: {
    login(token, userInfo) {
      this.token = token
      this.userInfo = userInfo
      localStorage.setItem('token', token)
    },
    
    logout() {
      this.token = ''
      this.userInfo = null
      this.permissions = []
      localStorage.removeItem('token')
    }
  }
})

// 业务树状态管理
export const useBusinessTreeStore = defineStore('businessTree', {
  state: () => ({
    treeData: [],
    selectedNode: null,
    expandedKeys: []
  }),
  
  actions: {
    setTreeData(data) {
      this.treeData = data
    },
    
    setSelectedNode(node) {
      this.selectedNode = node
    },
    
    setExpandedKeys(keys) {
      this.expandedKeys = keys
    }
  }
})

// 主题状态管理
export const useThemeStore = defineStore('theme', {
  state: () => ({
    isDark: localStorage.getItem('theme') === 'dark' || false
  }),
  
  actions: {
    toggleTheme() {
      this.isDark = !this.isDark
      localStorage.setItem('theme', this.isDark ? 'dark' : 'light')
      this.applyTheme()
    },
    
    applyTheme() {
      if (this.isDark) {
        document.documentElement.classList.add('dark')
      } else {
        document.documentElement.classList.remove('dark')
      }
    }
  }
})