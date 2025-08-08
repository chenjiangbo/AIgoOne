/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  
  // 暗色模式配置
  darkMode: ['class', '[data-theme="dark"]'],
  
  theme: {
    extend: {
      // 颜色系统 - 与设计Token保持一致
      colors: {
        // 主色调 - 使用Element Plus的蓝色作为主色
        primary: {
          50: 'rgb(var(--color-primary-50-rgb, 239 246 255))',
          100: 'rgb(var(--color-primary-100-rgb, 219 234 254))',
          200: 'rgb(var(--color-primary-200-rgb, 191 219 254))',
          300: 'rgb(var(--color-primary-300-rgb, 147 197 253))',
          400: 'rgb(var(--color-primary-400-rgb, 96 165 250))',
          500: 'rgb(var(--color-primary-500-rgb, 64 158 255))', // Element Plus 主色 #409eff
          600: 'rgb(var(--color-primary-600-rgb, 37 99 235))',
          700: 'rgb(var(--color-primary-700-rgb, 29 78 216))',
          800: 'rgb(var(--color-primary-800-rgb, 30 64 175))',
          900: 'rgb(var(--color-primary-900-rgb, 30 58 138))',
        },
        
        // 功能色彩
        success: {
          500: 'rgb(var(--color-success-500-rgb, 103 194 58))',
        },
        warning: {
          500: 'rgb(var(--color-warning-500-rgb, 230 162 60))',
        },
        error: {
          500: 'rgb(var(--color-error-500-rgb, 245 108 108))',
        },
        info: {
          500: 'rgb(var(--color-info-500-rgb, 144 147 153))',
        },
        
        // 中性色
        neutral: {
          50: 'rgb(var(--color-neutral-50-rgb, 250 250 250))',
          100: 'rgb(var(--color-neutral-100-rgb, 245 245 245))',
          200: 'rgb(var(--color-neutral-200-rgb, 229 229 229))',
          300: 'rgb(var(--color-neutral-300-rgb, 212 212 212))',
          400: 'rgb(var(--color-neutral-400-rgb, 163 163 163))',
          500: 'rgb(var(--color-neutral-500-rgb, 115 115 115))',
          600: 'rgb(var(--color-neutral-600-rgb, 82 82 82))',
          700: 'rgb(var(--color-neutral-700-rgb, 64 64 64))',
          800: 'rgb(var(--color-neutral-800-rgb, 38 38 38))',
          900: 'rgb(var(--color-neutral-900-rgb, 23 23 23))',
        },
        
        // 背景色 - 引用CSS变量
        bg: {
          primary: 'var(--color-bg-primary)',
          secondary: 'var(--color-bg-secondary)',
          tertiary: 'var(--color-bg-tertiary)',
          overlay: 'var(--color-bg-overlay)',
        },
        
        // 文本色
        text: {
          primary: 'var(--color-text-primary)',
          secondary: 'var(--color-text-secondary)',
          tertiary: 'var(--color-text-tertiary)',
          placeholder: 'var(--color-text-placeholder)',
          inverse: 'var(--color-text-inverse)',
        },
        
        // 边框色
        border: {
          primary: 'var(--color-border-primary)',
          secondary: 'var(--color-border-secondary)',
          tertiary: 'var(--color-border-tertiary)',
        }
      },
      
      // 字体系统
      fontFamily: {
        sans: 'var(--font-family-sans)',
        serif: 'var(--font-family-serif)',
        mono: 'var(--font-family-mono)',
      },
      
      // 字体尺寸 - 引用设计Token
      fontSize: {
        'xs': ['var(--font-size-xs)', { lineHeight: 'var(--line-height-tight)' }],
        'sm': ['var(--font-size-sm)', { lineHeight: 'var(--line-height-normal)' }],
        'base': ['var(--font-size-base)', { lineHeight: 'var(--line-height-normal)' }],
        'lg': ['var(--font-size-lg)', { lineHeight: 'var(--line-height-normal)' }],
        'xl': ['var(--font-size-xl)', { lineHeight: 'var(--line-height-relaxed)' }],
        '2xl': ['var(--font-size-2xl)', { lineHeight: 'var(--line-height-relaxed)' }],
        '3xl': ['var(--font-size-3xl)', { lineHeight: 'var(--line-height-relaxed)' }],
      },
      
      // 字重
      fontWeight: {
        light: 'var(--font-weight-light)',
        normal: 'var(--font-weight-normal)',
        medium: 'var(--font-weight-medium)',
        semibold: 'var(--font-weight-semibold)',
        bold: 'var(--font-weight-bold)',
      },
      
      // 间距系统 - 引用设计Token
      spacing: {
        '0.5': 'var(--spacing-0_5)',
        '1': 'var(--spacing-1)',
        '1.5': 'var(--spacing-1_5)',
        '2': 'var(--spacing-2)',
        '3': 'var(--spacing-3)',
        '4': 'var(--spacing-4)',
        '5': 'var(--spacing-5)',
        '6': 'var(--spacing-6)',
        '8': 'var(--spacing-8)',
        '10': 'var(--spacing-10)',
        '12': 'var(--spacing-12)',
        '16': 'var(--spacing-16)',
        '20': 'var(--spacing-20)',
        '24': 'var(--spacing-24)',
      },
      
      // 圆角
      borderRadius: {
        'sm': 'var(--border-radius-sm)',
        'md': 'var(--border-radius-md)',
        'lg': 'var(--border-radius-lg)',
        'xl': 'var(--border-radius-xl)',
        'full': 'var(--border-radius-full)',
      },
      
      // 阴影
      boxShadow: {
        'sm': 'var(--shadow-sm)',
        'md': 'var(--shadow-md)',
        'lg': 'var(--shadow-lg)',
        'xl': 'var(--shadow-xl)',
      },
      
      // 背景模糊
      backdropBlur: {
        'sm': 'var(--backdrop-blur-sm)',
        'md': 'var(--backdrop-blur-md)',
        'lg': 'var(--backdrop-blur-lg)',
      },
      
      // 过渡效果
      transitionDuration: {
        'fast': 'var(--transition-duration-fast)',
        'normal': 'var(--transition-duration-normal)',
        'slow': 'var(--transition-duration-slow)',
      },
      
      // 动画
      animation: {
        'fade-in': 'fadeIn var(--transition-duration-normal) ease-in-out',
        'slide-down': 'slideDown var(--transition-duration-fast) ease-out',
        'slide-up': 'slideUp var(--transition-duration-fast) ease-out',
        'scale-in': 'scaleIn var(--transition-duration-fast) ease-out',
        'spin-slow': 'spin 2s linear infinite',
        'pulse-slow': 'pulse 3s ease-in-out infinite',
      },
      
      // 关键帧动画
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' }
        },
        slideDown: {
          '0%': { transform: 'translateY(-10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' }
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' }
        },
        scaleIn: {
          '0%': { transform: 'scale(0.95)', opacity: '0' },
          '100%': { transform: 'scale(1)', opacity: '1' }
        }
      },
      
      // Z-index 层级
      zIndex: {
        'dropdown': '1000',
        'sticky': '1020',
        'fixed': '1030',
        'modal': '1040',
        'popover': '1050',
        'tooltip': '1060',
        'notification': '1070',
      }
    },
  },
  
  plugins: [
    // 自定义工具类插件
    function({ addUtilities, theme }) {
      const newUtilities = {
        // 文本省略
        '.text-ellipsis': {
          overflow: 'hidden',
          'text-overflow': 'ellipsis',
          'white-space': 'nowrap',
        },
        '.text-ellipsis-2': {
          display: '-webkit-box',
          '-webkit-line-clamp': '2',
          '-webkit-box-orient': 'vertical',
          overflow: 'hidden',
        },
        '.text-ellipsis-3': {
          display: '-webkit-box',
          '-webkit-line-clamp': '3',
          '-webkit-box-orient': 'vertical',
          overflow: 'hidden',
        },
        
        // Flex 布局快捷类
        '.flex-center': {
          display: 'flex',
          'align-items': 'center',
          'justify-content': 'center',
        },
        '.flex-between': {
          display: 'flex',
          'align-items': 'center',
          'justify-content': 'space-between',
        },
        '.flex-start': {
          display: 'flex',
          'align-items': 'center',
          'justify-content': 'flex-start',
        },
        '.flex-end': {
          display: 'flex',
          'align-items': 'center',
          'justify-content': 'flex-end',
        },
        
        // 滚动条样式
        '.scrollbar-thin': {
          'scrollbar-width': 'thin',
        },
        '.scrollbar-none': {
          'scrollbar-width': 'none',
          '-ms-overflow-style': 'none',
          '&::-webkit-scrollbar': {
            display: 'none',
          },
        },
      }
      
      addUtilities(newUtilities)
    }
  ],
  
  // 确保与 Element Plus 兼容
  corePlugins: {
    // 禁用预设样式，避免与Element Plus冲突
    preflight: false,
  },
  
  // 重要性配置
  important: false,
  
  // 分离器配置
  separator: ':',
}