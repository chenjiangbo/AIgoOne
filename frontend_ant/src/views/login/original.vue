<template>
  <div class="login-container">
    <!-- 粒子波浪背景 -->
    <div class="particle-waves-bg">
      <div class="wave-container">
        <div v-for="i in 200" :key="i" class="wave-particle" :style="getWaveParticleStyle(i)"></div>
      </div>
      <div class="flowing-waves">
        <div v-for="i in 3" :key="i" class="wave-line" :style="getWaveLineStyle(i)"></div>
      </div>
    </div>

    <!-- 主要内容 -->
    <div class="login-content">
      <!-- 左侧品牌区 -->
      <div class="brand-section">
        <div class="brand-content">
          <div class="brand-logo">
            <!-- 核心算法象征 -->
            <div class="algorithm-core">
              <div class="core-ring"></div>
              <div class="data-flow" v-for="i in 4" :key="i" :class="`flow-${i}`"></div>
            </div>
            
            <div class="logo-text">AIgoOne</div>
            <div class="logo-subtitle">算法管理平台</div>
          </div>
          
          <div class="brand-slogan">
            <p class="slogan-text">智能 · 高效 · 可靠</p>
            <p class="slogan-sub">Next Generation Algorithm Management Platform</p>
          </div>
        </div>
      </div>

      <!-- 右侧登录表单 -->
      <div class="login-form-wrapper">
        <div class="form-container">
          <div class="form-header">
            <h2 class="form-title">系统登录</h2>
            <div class="title-line"></div>
          </div>
          
          <a-form
            ref="loginFormRef"
            :model="loginForm"
            :rules="loginRules"
            class="login-form"
            size="large"
            @finish="handleLogin"
          >
            <a-form-item name="username">
              <a-input
                v-model:value="loginForm.username"
                placeholder="请输入用户名"
                size="large"
                allow-clear
                class="tech-input"
              >
                <template #prefix>
                  <UserOutlined />
                </template>
              </a-input>
            </a-form-item>
            
            <a-form-item name="password">
              <a-input-password
                v-model:value="loginForm.password"
                placeholder="请输入密码"
                size="large"
                allow-clear
                class="tech-input"
              >
                <template #prefix>
                  <LockOutlined />
                </template>
              </a-input-password>
            </a-form-item>

            <!-- 错误提示区域 -->
            <a-alert
              v-if="errorMessage"
              :message="errorMessage"
              type="error"
              show-icon
              closable
              style="margin-bottom: 24px"
              class="error-alert"
              @close="errorMessage = ''"
            />

            <a-form-item>
              <a-button
                type="primary"
                html-type="submit"
                :loading="isLoading"
                block
                size="large"
                class="full-width-btn"
              >
                {{ isLoading ? '登录中...' : '登录' }}
              </a-button>
            </a-form-item>
          </a-form>

          <!-- 底部信息 -->
          <div class="form-footer">
            <div class="remember-me">
              <a-checkbox v-model:checked="rememberMe">记住我</a-checkbox>
            </div>
            <a class="forgot-password" href="#">忘记密码？</a>
          </div>
          
          <div class="copyright-footer">
            <div class="tech-divider"></div>
            <p class="copyright">© 2025 RealEasyInfo Inc. All rights reserved.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { message } from 'ant-design-vue'
import { UserOutlined, LockOutlined } from '@ant-design/icons-vue'
import type { FormInstance, Rule } from 'ant-design-vue/es/form'
import { login } from '@/api/auth'

const router = useRouter()
const loginFormRef = ref<FormInstance>()

// 表单数据
const loginForm = reactive({
  username: '',
  password: ''
})

// 表单验证规则
const loginRules: Record<string, Rule[]> = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 3, max: 20, message: '用户名长度在 3 到 20 个字符', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码长度不能少于 6 个字符', trigger: 'blur' }
  ]
}

const isLoading = ref(false)
const errorMessage = ref('')
const rememberMe = ref(false)

// 处理登录
const handleLogin = async () => {
  isLoading.value = true
  errorMessage.value = ''
  
  try {
    // 调用真实的登录API
    const response = await login({
      username: loginForm.username,
      password: loginForm.password
    })
    
    if (response.access_token) {
      // 保存token
      localStorage.setItem('token', response.access_token)
      localStorage.setItem('user', JSON.stringify({ username: loginForm.username }))
      
      if (rememberMe.value) {
        localStorage.setItem('username', loginForm.username)
      }
      
      message.success('登录成功')
      router.push('/dashboard')
    } else {
      errorMessage.value = '登录失败，请检查用户名和密码'
    }
  } catch (error: any) {
    console.error('登录失败:', error)
    errorMessage.value = error.response?.data?.detail || '用户名或密码错误'
  } finally {
    isLoading.value = false
  }
}

// 生成波浪粒子样式
const getWaveParticleStyle = (index: number) => {
  const x = (index % 20) * 5
  const y = Math.floor(index / 20) * 10
  const delay = Math.random() * 5
  const duration = 3 + Math.random() * 2
  
  return {
    left: `${x}%`,
    top: `${y}%`,
    animationDelay: `${delay}s`,
    animationDuration: `${duration}s`
  }
}

// 生成波浪线样式
const getWaveLineStyle = (index: number) => {
  const delay = index * 2
  const opacity = 0.1 + (index * 0.1)
  
  return {
    animationDelay: `${delay}s`,
    opacity: opacity
  }
}

onMounted(() => {
  // 如果记住了用户名，自动填充
  const savedUsername = localStorage.getItem('username')
  if (savedUsername) {
    loginForm.username = savedUsername
    rememberMe.value = true
  }
})
</script>

<style lang="less" scoped>
.login-container {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: linear-gradient(135deg, #1a365d 0%, #2d5a87 30%, #1e40af 70%, #1e3a8a 100%);
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 粒子波浪背景 */
.particle-waves-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  overflow: hidden;
}

.wave-container {
  position: absolute;
  width: 100%;
  height: 100%;
}

.wave-particle {
  position: absolute;
  width: 3px;
  height: 3px;
  background: rgba(59, 130, 246, 0.6);
  border-radius: 50%;
  box-shadow: 0 0 6px rgba(59, 130, 246, 0.8);
  animation: particleWave 5s ease-in-out infinite;
}

.flowing-waves {
  position: absolute;
  width: 100%;
  height: 100%;
}

.wave-line {
  position: absolute;
  width: 100%;
  height: 200px;
  background: linear-gradient(45deg, 
    transparent 30%, 
    rgba(59, 130, 246, 0.1) 50%, 
    transparent 70%);
  transform-origin: left center;
  animation: waveFlow 8s ease-in-out infinite;
}

@keyframes particleWave {
  0%, 100% {
    transform: translateY(0px) scale(1);
    opacity: 0.6;
  }
  50% {
    transform: translateY(-15px) scale(1.2);
    opacity: 1;
  }
}

@keyframes waveFlow {
  0% {
    transform: translateX(-100%) rotate(-5deg);
    opacity: 0;
  }
  50% {
    opacity: 0.3;
  }
  100% {
    transform: translateX(100%) rotate(5deg);
    opacity: 0;
  }
}

// 主要内容
.login-content {
  position: relative;
  width: 85%;
  max-width: 1100px;
  height: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1;
  margin: 0 auto;
}

// 左侧品牌区
.brand-section {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
}

.brand-content {
  text-align: center;
  color: white;
  transform: translateY(-40px);
}

.brand-logo {
  margin-bottom: 50px;
}

.logo-icon {
  margin-bottom: 20px;
}

.icon-diamond {
  position: relative;
  width: 80px;
  height: 80px;
  margin: 0 auto;
}

.diamond-core {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 35px;
  height: 35px;
  background: rgba(59, 130, 246, 0.3);
  border: 2px solid #3b82f6;
  transform: translate(-50%, -50%) rotate(45deg);
  animation: diamondPulse 3s ease-in-out infinite;
}

.diamond-ring {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 60px;
  height: 60px;
  border: 1px solid rgba(59, 130, 246, 0.5);
  transform: translate(-50%, -50%) rotate(45deg);
  animation: ringRotate 8s linear infinite;
}

@keyframes diamondPulse {
  0%, 100% {
    box-shadow: 0 0 20px rgba(59, 130, 246, 0.6);
    transform: translate(-50%, -50%) rotate(45deg) scale(1);
  }
  50% {
    box-shadow: 0 0 30px rgba(59, 130, 246, 0.8);
    transform: translate(-50%, -50%) rotate(45deg) scale(1.1);
  }
}

@keyframes ringRotate {
  0% { transform: translate(-50%, -50%) rotate(45deg); }
  100% { transform: translate(-50%, -50%) rotate(405deg); }
}

.logo-text {
  font-size: 52px;
  font-weight: bold;
  margin-bottom: 10px;
  color: white;
  text-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  position: relative;
  z-index: 2;
  letter-spacing: 2px;
}

.logo-subtitle {
  font-size: 18px;
  color: #93c5fd;
  opacity: 0.9;
}

.brand-description {
  margin: 30px 0;
  
  .desc-main {
    font-size: 18px;
    color: rgba(255, 255, 255, 0.95);
    margin-bottom: 10px;
    font-weight: 500;
  }
  
  .desc-sub {
    font-size: 14px;
    color: rgba(255, 255, 255, 0.7);
    letter-spacing: 2px;
  }
}

.feature-list {
  margin-top: 40px;
  
  .feature-item {
    display: flex;
    align-items: center;
    margin: 15px 0;
    padding: 12px 20px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(59, 130, 246, 0.2);
    border-radius: 10px;
    transition: all 0.3s ease;
    
    &:hover {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(59, 130, 246, 0.4);
      transform: translateX(5px);
    }
    
    .feature-icon {
      font-size: 20px;
      margin-right: 12px;
    }
    
    span:last-child {
      font-size: 15px;
      color: rgba(255, 255, 255, 0.85);
    }
  }
}

// 右侧登录表单
.login-form-wrapper {
  width: 480px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
}

.form-container {
  width: 100%;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(248, 250, 252, 0.95) 100%);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-radius: 24px;
  padding: 45px;
  box-shadow: 
    0 30px 60px -15px rgba(0, 0, 0, 0.3),
    0 0 0 1px rgba(255, 255, 255, 0.2),
    inset 0 0 0 1px rgba(255, 255, 255, 0.5);
}

.form-header {
  text-align: center;
  margin-bottom: 40px;
}

.form-title {
  font-size: 28px;
  font-weight: 600;
  color: #1f2937;
  margin: 0 0 16px 0;
}

.title-line {
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, #3b82f6, #60a5fa);
  margin: 0 auto;
  border-radius: 2px;
  box-shadow: 0 0 10px rgba(59, 130, 246, 0.5);
}

.login-form {
  :deep(.ant-input-affix-wrapper) {
    background: rgba(255, 255, 255, 0.8);
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 14px 16px;
    height: 52px;
    transition: all 0.3s ease;
    
    &:hover {
      border-color: #3b82f6;
      background: rgba(255, 255, 255, 0.95);
    }
    
    &.ant-input-affix-wrapper-focused {
      border-color: #3b82f6;
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
      background: white;
    }
  }
  
  :deep(.ant-input) {
    background: transparent;
    color: #1f2937;
    font-size: 15px;
    
    &::placeholder {
      color: #9ca3af;
    }
  }
  
  :deep(.anticon) {
    color: #6b7280;
  }
  
  .tech-input {
    border-radius: 12px;
  }
}

.full-width-btn {
  height: 48px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 8px;
  background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);
  border: none;
  transition: all 0.3s ease;
  
  &:hover {
    background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
    box-shadow: 0 5px 20px rgba(59, 130, 246, 0.4);
    transform: translateY(-2px);
  }
}

.form-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
}

.remember-me {
  :deep(.ant-checkbox-wrapper) {
    color: #6b7280;
    
    .ant-checkbox-inner {
      background: white;
      border-color: #d1d5db;
    }
    
    .ant-checkbox-checked .ant-checkbox-inner {
      background: #3b82f6;
      border-color: #3b82f6;
    }
  }
}

.forgot-password {
  color: #3b82f6;
  text-decoration: none;
  transition: color 0.3s ease;
  font-weight: 500;
  
  &:hover {
    color: #2563eb;
    text-decoration: underline;
  }
}

.copyright-footer {
  margin-top: 30px;
  text-align: center;
  
  .tech-divider {
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, transparent, #e0e0e0, transparent);
    margin-bottom: 16px;
  }
  
  .copyright {
    font-size: 12px;
    color: #9ca3af;
    margin: 0;
    letter-spacing: 0.5px;
  }
}

// 错误提示样式
.error-alert {
  :deep(.ant-alert) {
    background: rgba(239, 68, 68, 0.1);
    border: 1px solid rgba(239, 68, 68, 0.3);
  }
  
  :deep(.ant-alert-message) {
    color: #fca5a5;
  }
}

// 算法核心装饰 - 象征算法处理数据的流程
.algorithm-core {
  position: relative;
  width: 120px;
  height: 120px;
  margin: 0 auto 25px;
  display: flex;
  align-items: center;
  justify-content: center;
}

// 核心处理器环
.core-ring {
  width: 80px;
  height: 80px;
  border: 3px solid rgba(59, 130, 246, 0.6);
  border-radius: 50%;
  position: relative;
  animation: coreProcess 3s ease-in-out infinite;
}

.core-ring::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 12px;
  height: 12px;
  background: #3b82f6;
  border-radius: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 0 15px rgba(59, 130, 246, 0.8);
}

// 数据流动线条
.data-flow {
  position: absolute;
  width: 60px;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.8), transparent);
  transform-origin: center;
}

.flow-1 {
  top: 50%;
  left: -30px;
  animation: dataFlow 2s ease-in-out infinite;
  animation-delay: 0s;
}

.flow-2 {
  top: -30px;
  left: 50%;
  transform: translateX(-50%) rotate(90deg);
  animation: dataFlow 2s ease-in-out infinite;
  animation-delay: 0.5s;
}

.flow-3 {
  top: 50%;
  right: -30px;
  transform: translateY(-50%) rotate(180deg);
  animation: dataFlow 2s ease-in-out infinite;
  animation-delay: 1s;
}

.flow-4 {
  bottom: -30px;
  left: 50%;
  transform: translateX(-50%) rotate(270deg);
  animation: dataFlow 2s ease-in-out infinite;
  animation-delay: 1.5s;
}

@keyframes coreProcess {
  0%, 100% {
    border-color: rgba(59, 130, 246, 0.6);
    box-shadow: 0 0 10px rgba(59, 130, 246, 0.3);
  }
  50% {
    border-color: rgba(59, 130, 246, 0.9);
    box-shadow: 0 0 25px rgba(59, 130, 246, 0.6);
  }
}

@keyframes dataFlow {
  0% {
    opacity: 0;
    transform: translateX(-20px);
  }
  50% {
    opacity: 1;
    transform: translateX(0);
  }
  100% {
    opacity: 0;
    transform: translateX(20px);
  }
}

// 响应式设计
@media (max-width: 768px) {
  .brand-section {
    display: none;
  }
  
  .login-form-wrapper {
    width: 100%;
    padding: 20px;
  }
  
  .form-container {
    padding: 30px 20px;
  }
}
</style>