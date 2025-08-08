import { theme } from 'ant-design-vue'
import type { ThemeConfig } from 'ant-design-vue/es/config-provider/context'

// 基础主题配置（通用设置）
const baseThemeConfig: ThemeConfig = {
  token: {
    // 圆角
    borderRadius: 6,
    borderRadiusLG: 8,
    borderRadiusSM: 4,
    
    // 字体
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
    fontSize: 14,
    fontSizeLG: 16,
    fontSizeSM: 12,
    
    // 控件高度
    controlHeight: 36,
    controlHeightLG: 40,
    controlHeightSM: 28,
    
    // 间距
    padding: 16,
    paddingLG: 24,
    paddingSM: 12,
    paddingXS: 8,
    
    // 动画
    motionDurationSlow: '0.3s',
    motionDurationMid: '0.2s',
    motionDurationFast: '0.1s'
  },
  components: {
    Button: {
      borderRadius: 6,
      fontWeight: 500
    },
    Modal: {
      borderRadiusLG: 8,
      paddingContentHorizontalLG: 24
    },
    Card: {
      borderRadiusLG: 8,
      paddingLG: 24
    },
    Table: {
      borderRadius: 8
    },
    Input: {
      borderRadius: 6
    },
    Select: {
      borderRadius: 6
    },
    Tree: {
      borderRadius: 4
    },
    Menu: {
      borderRadius: 6
    }
  }
}

// 亮色主题配置
export const lightThemeConfig: ThemeConfig = {
  ...baseThemeConfig,
  algorithm: theme.defaultAlgorithm,
  token: {
    ...baseThemeConfig.token,
    // 主要颜色
    colorPrimary: '#3b82f6',
    colorSuccess: '#52c41a',
    colorWarning: '#faad14',
    colorError: '#f5222d',
    colorInfo: '#3b82f6',
    
    // 背景色
    colorBgContainer: '#ffffff',
    colorBgElevated: '#ffffff',
    colorBgLayout: '#f5f7fa',
    colorBgSpotlight: '#fafafa',
    
    // 文字颜色
    colorText: '#2c3e50',
    colorTextSecondary: '#666666',
    colorTextTertiary: '#909399',
    colorTextQuaternary: '#c0c4cc',
    
    // 边框颜色
    colorBorder: '#e4e7ed',
    colorBorderSecondary: '#f0f0f0'
  }
}

// 暗色主题配置
export const darkThemeConfig: ThemeConfig = {
  ...baseThemeConfig,
  algorithm: theme.darkAlgorithm,
  token: {
    ...baseThemeConfig.token,
    // 主要颜色（暗色主题下稍微调亮）
    colorPrimary: '#60a5fa',
    colorSuccess: '#34d399',
    colorWarning: '#fbbf24',
    colorError: '#f87171',
    colorInfo: '#60a5fa',
    
    // 背景色
    colorBgContainer: '#1f2937',
    colorBgElevated: '#1f2937',
    colorBgLayout: '#111827',
    colorBgSpotlight: '#374151',
    
    // 文字颜色
    colorText: '#f3f4f6',
    colorTextSecondary: '#d1d5db',
    colorTextTertiary: '#9ca3af',
    colorTextQuaternary: '#6b7280',
    
    // 边框颜色
    colorBorder: '#4b5563',
    colorBorderSecondary: '#374151'
  }
}

// 为了兼容旧代码，保留原来的导出
export const themeConfig = lightThemeConfig