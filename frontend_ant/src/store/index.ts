import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    token: localStorage.getItem('token') || '',
    userInfo: JSON.parse(localStorage.getItem('user') || 'null') as any
  }),
  
  getters: {
    isLoggedIn: (state) => !!state.token,
    isAdmin: (state) => state.userInfo?.role === 'admin' || state.userInfo?.is_superuser === true,
    currentUser: (state) => state.userInfo
  },
  
  actions: {
    setToken(token: string) {
      this.token = token
      localStorage.setItem('token', token)
    },
    
    setUserInfo(userInfo: any) {
      this.userInfo = userInfo
      localStorage.setItem('user', JSON.stringify(userInfo))
    },
    
    logout() {
      this.token = ''
      this.userInfo = null
      localStorage.removeItem('token')
      localStorage.removeItem('user')
    }
  }
})

export const useAppStore = defineStore('app', {
  state: () => ({
    sidebarCollapsed: false,
    isDarkTheme: localStorage.getItem('darkTheme') === 'true' || false,
    selectedBusinessUnit: null as any
  }),
  
  getters: {
    currentTheme: (state) => state.isDarkTheme ? 'dark' : 'light'
  },
  
  actions: {
    toggleSidebar() {
      this.sidebarCollapsed = !this.sidebarCollapsed
    },
    
    toggleTheme() {
      this.isDarkTheme = !this.isDarkTheme
      localStorage.setItem('darkTheme', this.isDarkTheme.toString())
      
      // 更新HTML根元素的class以支持CSS主题切换
      if (this.isDarkTheme) {
        document.documentElement.classList.add('dark')
      } else {
        document.documentElement.classList.remove('dark')
      }
    },
    
    setTheme(isDark: boolean) {
      this.isDarkTheme = isDark
      localStorage.setItem('darkTheme', isDark.toString())
      
      if (isDark) {
        document.documentElement.classList.add('dark')
      } else {
        document.documentElement.classList.remove('dark')
      }
    },
    
    initTheme() {
      // 初始化时应用主题
      if (this.isDarkTheme) {
        document.documentElement.classList.add('dark')
      } else {
        document.documentElement.classList.remove('dark')
      }
    },
    
    setSelectedBusinessUnit(unit: any) {
      this.selectedBusinessUnit = unit
    }
  }
})