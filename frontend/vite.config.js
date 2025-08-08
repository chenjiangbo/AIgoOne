import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'
import { visualizer } from 'rollup-plugin-visualizer'
import viteCompression from 'vite-plugin-compression'

export default defineConfig(({ command, mode }) => {
  // 加载环境变量
  const env = loadEnv(mode, process.cwd(), '')
  
  return {
    plugins: [
      vue({
        // Vue 3 优化
        template: {
          compilerOptions: {
            // 优化编译性能
            hoistStatic: true,
            cacheHandlers: true,
          }
        }
      }),
      AutoImport({
        resolvers: [ElementPlusResolver()],
        imports: [
          'vue',
          'vue-router',
          'pinia',
          {
            'element-plus': [
              'ElMessage',
              'ElMessageBox',
              'ElNotification',
              'ElLoading'
            ]
          }
        ],
        // 生成类型定义文件
        dts: true,
        // 只在开发环境生成
        eslintrc: {
          enabled: command === 'serve',
        },
      }),
      Components({
        resolvers: [ElementPlusResolver()],
        // 自动导入我们的UI组件
        dirs: ['src/components/ui', 'src/components/device'],
        // 生成类型定义文件
        dts: true,
      }),
      
      // 构建分析插件
      env.VITE_BUILD_ANALYZE === 'true' && visualizer({
        filename: 'dist/stats.html',
        open: true,
        gzipSize: true,
        brotliSize: true,
      }),
      
      // 压缩插件
      command === 'build' && env.VITE_BUILD_COMPRESS && viteCompression({
        algorithm: env.VITE_BUILD_COMPRESS,
        ext: `.${env.VITE_BUILD_COMPRESS}`,
        threshold: 1024,
        deleteOriginFile: false,
      }),
    ].filter(Boolean),
    
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src'),
        '@ui': path.resolve(__dirname, 'src/components/ui'),
        '@device': path.resolve(__dirname, 'src/components/device'),
        '@styles': path.resolve(__dirname, 'src/styles'),
      }
    },
    
    // CSS 处理优化
    css: {
      preprocessorOptions: {
        scss: {
          // 自动注入全局变量
          additionalData: `@import "@styles/tokens/index.css";`
        }
      },
      devSourcemap: command === 'serve',
    },
    
    // 开发服务器配置
    server: {
      port: 3000,
      host: true,
      open: false,
      cors: true,
      proxy: {
        '/api': {
          target: env.VITE_API_BASE_URL || 'http://localhost:8000',
          changeOrigin: true,
          secure: false,
          ws: true,
        }
      }
    },
    
    // 依赖优化
    optimizeDeps: {
      include: [
        'vue',
        'vue-router',
        'pinia',
        'element-plus/es',
        'element-plus/es/components/*/style/css',
        '@element-plus/icons-vue',
        'axios'
      ],
      exclude: ['vue-demi']
    },
    
    // 预览服务器配置
    preview: {
      port: 4173,
      host: true,
      cors: true,
    },
    
    // 定义全局常量
    define: {
      __VUE_OPTIONS_API__: true,
      __VUE_PROD_DEVTOOLS__: false,
      __APP_VERSION__: JSON.stringify(process.env.npm_package_version),
    },
    
    // ESBuild 配置
    esbuild: {
      // 生产环境下移除 console 和 debugger
      drop: command === 'build' && env.VITE_DROP_CONSOLE === 'true' ? ['console', 'debugger'] : [],
    },
    
    // 性能预警配置
    build: {
      ...((command === 'build') && {
        rollupOptions: {
          ...((command === 'build') && {
            output: {
              // 手动分割代码
              manualChunks: {
                // Vue 核心
                'vue-vendor': ['vue', 'vue-router', 'pinia'],
                // UI 框架
                'ui-vendor': ['element-plus'],
                // 工具库
                'utils-vendor': ['axios'],
                // 我们的UI组件库
                'ui-components': [
                  './src/components/ui/BaseButton.vue',
                  './src/components/ui/BaseCard.vue',
                  './src/components/ui/BaseDialog.vue',
                  './src/components/ui/BaseInput.vue'
                ],
                // 设备管理组件
                'device-components': [
                  './src/components/device/DeviceToolbar.vue',
                  './src/components/device/DeviceTable.vue',
                  './src/components/device/DeviceStatsCards.vue',
                  './src/components/device/AddDeviceDialog.vue',
                  './src/components/device/BatchSyncDialog.vue'
                ]
              },
              // 文件命名策略
              chunkFileNames: (chunkInfo) => {
                const facadeModuleId = chunkInfo.facadeModuleId
                if (facadeModuleId) {
                  const name = path.basename(facadeModuleId, path.extname(facadeModuleId))
                  return `js/${name}-[hash].js`
                }
                return 'js/[name]-[hash].js'
              },
              entryFileNames: 'js/[name]-[hash].js',
              assetFileNames: (assetInfo) => {
                const ext = path.extname(assetInfo.name)
                if (/\.(png|jpe?g|svg|gif|tiff|bmp|ico)$/i.test(assetInfo.name)) {
                  return 'images/[name]-[hash][ext]'
                }
                if (/\.(woff2?|eot|ttf|otf)$/i.test(assetInfo.name)) {
                  return 'fonts/[name]-[hash][ext]'
                }
                if (ext === '.css') {
                  return 'css/[name]-[hash][ext]'
                }
                return 'assets/[name]-[hash][ext]'
              }
            }
          })
        },
        
        // 资源内联限制
        assetsInlineLimit: 4096,
        
        // 清除输出目录
        emptyOutDir: true,
        
        // 报告压缩前后的大小
        reportCompressedSize: false,
        
        // 构建警告阈值
        chunkSizeWarningLimit: 1000,
      }),
      
      // 输出目录
      outDir: 'dist',
      assetsDir: 'assets',
      
      // 构建目标
      target: 'es2015',
      
      // 压缩选项
      minify: 'esbuild',
      
      // 生成 sourcemap
      sourcemap: command === 'build' && mode === 'development',
    }
  }
})