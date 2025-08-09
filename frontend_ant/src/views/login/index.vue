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

    <!-- 动态元素 -->
    <div class="dynamic-elements">
      <!-- 扫描线 -->
      <div class="scanning-line"></div>
      
      <!-- 旋转环 -->
      <div class="rotating-ring"></div>
      
      <!-- 六边形图案 -->
      <div class="hex-pattern">
        <div v-for="i in 12" :key="i" class="hex" :style="getHexStyle(i)"></div>
      </div>
      
      <!-- 能量波 -->
      <div class="energy-waves">
        <div v-for="i in 3" :key="i" class="wave" :style="{ animationDelay: i * 2 + 's' }"></div>
      </div>
    </div>

    <!-- 主要内容 -->
    <div class="login-content">
      <!-- 左侧品牌区 -->
      <div class="brand-section">
        <div class="brand-content">
          <div class="brand-logo">
            <div class="tech-diamond">
              <div class="diamond-core"></div>
              <div class="diamond-ring"></div>
              <div v-for="i in 3" :key="i" class="diamond-dot" :class="`dot-${i + 1}`"></div>
              <div class="scan-beam"></div>
            </div>
            
            <h1 class="platform-title">
              <span class="title-main">AIgoOne</span>
              <span class="title-sub">算法管理平台</span>
            </h1>
          </div>
          
          <div class="platform-description">
            <p class="desc-text">
              统一管理多设备算法应用平台<br/>
              实时监控 · 智能调度 · 高效运维
            </p>
          </div>
          
          <div class="feature-list">
            <div class="feature-item">
              <div class="feature-icon">
                <span class="icon-wrapper">🔧</span>
              </div>
              <div class="feature-content">
                <h4>设备集中管理</h4>
                <p>统一纳管所有边缘计算设备</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon">
                <span class="icon-wrapper">📊</span>
              </div>
              <div class="feature-content">
                <h4>实时数据监控</h4>
                <p>全方位掌控算法运行状态</p>
              </div>
            </div>
            <div class="feature-item">
              <div class="feature-icon">
                <span class="icon-wrapper">⚡</span>
              </div>
              <div class="feature-content">
                <h4>智能任务调度</h4>
                <p>自动化管理提升运营效率</p>
              </div>
            </div>
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
              style="margin-bottom: 1.5rem"
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
import { login, getUserInfo } from '@/api/auth'
import { useUserStore } from '@/store'

const router = useRouter()
const loginFormRef = ref<FormInstance>()
const userStore = useUserStore()

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
    { min: 6, max: 20, message: '密码长度在 6 到 20 个字符', trigger: 'blur' }
  ]
}

const isLoading = ref(false)
const errorMessage = ref('')

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
      console.log('登录成功，获得token:', response.access_token.substring(0, 20) + '...')
      // 保存token到store
      userStore.setToken(response.access_token)
      
      try {
        console.log('开始获取用户信息...')
        // 获取完整用户信息
        const userInfoResponse = await getUserInfo()
        console.log('getUserInfo API返回:', userInfoResponse)
        console.log('获取到的用户信息:', userInfoResponse.data)
        userStore.setUserInfo(userInfoResponse.data)
        
        message.success('登录成功！')
        router.push('/dashboard')
      } catch (userInfoError) {
        console.error('获取用户信息失败:', userInfoError)
        console.error('错误详情:', userInfoError.response?.data)
        // 即使获取用户信息失败，也允许继续登录，只是使用基本信息
        const fallbackUser = { 
          username: loginForm.username,
          role: 'user' // 默认角色
        }
        console.log('使用fallback用户信息:', fallbackUser)
        userStore.setUserInfo(fallbackUser)
        message.success('登录成功！')
        router.push('/dashboard')
      }
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

// 生成六边形样式
const getHexStyle = (index: number) => {
  const positions = [
    { left: '10%', top: '20%' },
    { left: '80%', top: '15%' },
    { left: '15%', top: '60%' },
    { left: '85%', top: '70%' },
    { left: '30%', top: '80%' },
    { left: '70%', top: '30%' },
    { left: '50%', top: '10%' },
    { left: '20%', top: '40%' },
    { left: '60%', top: '85%' },
    { left: '90%', top: '45%' },
    { left: '5%', top: '85%' },
    { left: '75%', top: '55%' }
  ]
  
  const pos = positions[index % positions.length]
  const delay = Math.random() * 6
  
  return {
    ...pos,
    animationDelay: `${delay}s`
  }
}

onMounted(() => {
  // 检查是否已登录
  const token = localStorage.getItem('token')
  if (token) {
    router.push('/dashboard')
  }
})
</script>

<style scoped>
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

/* 新增动态元素 */
.dynamic-elements {
  position: absolute;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
}

.scanning-line {
  position: absolute;
  top: 0;
  left: -100%;
  width: 2px;
  height: 100%;
  background: linear-gradient(to bottom, transparent, #00ffff, transparent);
  animation: scanLeft 8s ease-in-out infinite;
  box-shadow: 0 0 20px #00ffff;
}

.rotating-ring {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 300px;
  height: 300px;
  border: 1px solid rgba(0, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: #00ffff;
  transform: translate(-50%, -50%);
  animation: rotate 15s linear infinite;
}

.hex-pattern {
  position: absolute;
  width: 100%;
  height: 100%;
}

.hex {
  position: absolute;
  width: 20px;
  height: 20px;
  border: 1px solid rgba(0, 150, 255, 0.6);
  transform: rotate(45deg);
  animation: hexFloat 6s ease-in-out infinite;
}

.energy-waves {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.wave {
  position: absolute;
  width: 200px;
  height: 200px;
  border: 1px solid rgba(0, 255, 255, 0.2);
  border-radius: 50%;
  animation: waveExpand 6s ease-out infinite;
}

/* 主要内容 */
.login-content {
  display: flex;
  width: 80%;
  max-width: 1100px;
  height: 600px;
  position: relative;
  z-index: 1;
  align-items: center;
  justify-content: center;
}

/* 品牌区域 */
.brand-section {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  color: white;
}

.brand-content {
  text-align: center;
  max-width: 500px;
}

.brand-logo {
  margin-bottom: 3rem;
}

.tech-diamond {
  position: relative;
  width: 120px;
  height: 120px;
  margin: 0 auto 2rem;
}

.diamond-core {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 40px;
  height: 40px;
  background: rgba(0, 255, 255, 0.3);
  transform: translate(-50%, -50%) rotate(45deg);
  border: 2px solid #00ffff;
  animation: diamondPulse 3s ease-in-out infinite;
}

.diamond-ring {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 80px;
  height: 80px;
  border: 1px solid rgba(0, 255, 255, 0.5);
  transform: translate(-50%, -50%) rotate(-45deg);
  animation: ringRotate 8s linear infinite;
}

.diamond-dot {
  position: absolute;
  width: 6px;
  height: 6px;
  background: #00ffff;
  border-radius: 50%;
  animation: dotGlow 2s ease-in-out infinite;
}

.dot-1 {
  top: -3px;
  left: 50%;
  transform: translateX(-50%);
  animation-delay: 0s;
}

.dot-2 {
  top: 50%;
  right: -3px;
  transform: translateY(-50%);
  animation-delay: 0.7s;
}

.dot-3 {
  bottom: -3px;
  left: 50%;
  transform: translateX(-50%);
  animation-delay: 1.4s;
}

.scan-beam {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 120px;
  height: 2px;
  background: linear-gradient(90deg, transparent, #00ffff, transparent);
  transform: translate(-50%, -50%);
  animation: scanRotate 4s linear infinite;
  opacity: 0.6;
}

.platform-title {
  margin: 0;
}

.title-main {
  display: block;
  font-size: 2.5rem;
  font-weight: bold;
  background: linear-gradient(45deg, #00ffff, #0099ff);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 0.5rem;
}

.title-sub {
  display: block;
  font-size: 1rem;
  color: #88ccff;
  font-weight: normal;
  letter-spacing: 1px;
}

.platform-description {
  margin: 2rem 0;
}

.desc-text {
  font-size: 1.1rem;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.85);
  letter-spacing: 0.5px;
}

.feature-list {
  margin-top: 3rem;
  text-align: left;
}

.feature-item {
  display: flex;
  align-items: flex-start;
  margin: 1.5rem 0;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 12px;
  border: 1px solid rgba(59, 130, 246, 0.1);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.feature-item:hover {
  background: rgba(255, 255, 255, 0.06);
  border-color: rgba(59, 130, 246, 0.3);
  transform: translateX(5px);
}

.feature-icon {
  margin-right: 1rem;
  flex-shrink: 0;
}

.icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: rgba(59, 130, 246, 0.15);
  border-radius: 10px;
  font-size: 1.3rem;
}

.feature-content h4 {
  margin: 0 0 0.3rem 0;
  font-size: 1rem;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.95);
}

.feature-content p {
  margin: 0;
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.4;
}

/* 右侧登录表单 */
.login-form-wrapper {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.form-container {
  width: 100%;
  max-width: 320px;
  padding: 2rem;
  background: rgba(17, 24, 39, 0.7);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(59, 130, 246, 0.2);
  border-radius: 16px;
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.3),
    0 0 60px rgba(59, 130, 246, 0.1),
    inset 0 0 0 1px rgba(59, 130, 246, 0.1);
}

.form-header {
  text-align: center;
  margin-bottom: 2rem;
}

.form-title {
  color: white;
  font-size: 1.8rem;
  font-weight: 600;
  margin: 0 0 1rem 0;
}

.title-line {
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, #00ffff, #0099ff);
  margin: 0 auto;
  border-radius: 2px;
}

.login-form {
  margin-bottom: 2rem;
}

:deep(.tech-input .ant-input-affix-wrapper) {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 8px;
  color: white;
  font-size: 16px;
  padding: 12px 16px;
}

:deep(.tech-input .ant-input-affix-wrapper:hover) {
  border-color: rgba(0, 255, 255, 0.5);
  box-shadow: 0 0 10px rgba(0, 255, 255, 0.2);
}

:deep(.tech-input .ant-input-affix-wrapper.ant-input-affix-wrapper-focused) {
  border-color: #00ffff;
  box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
}

:deep(.tech-input .ant-input) {
  background: transparent;
  color: white;
  font-size: 16px;
}

:deep(.tech-input .ant-input::placeholder) {
  color: rgba(255, 255, 255, 0.6);
}

:deep(.tech-input .anticon) {
  color: rgba(255, 255, 255, 0.7);
}

.full-width-btn {
  height: 50px;
  font-size: 1.1rem;
  font-weight: 600;
  background: linear-gradient(135deg, #00ffff, #0099ff);
  border: none;
  border-radius: 8px;
  color: white;
  transition: all 0.3s ease;
}

.full-width-btn:hover {
  background: linear-gradient(135deg, #00cccc, #0077cc);
  box-shadow: 0 5px 20px rgba(0, 255, 255, 0.3);
  transform: translateY(-2px);
}

.form-footer {
  text-align: center;
  margin-top: 2rem;
}

.tech-divider {
  width: 100%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  margin-bottom: 1rem;
}

.copyright {
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.6);
  margin: 0;
  letter-spacing: 0.5px;
}

/* 动画定义 */
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

@keyframes scanLeft {
  0% { left: -100%; }
  50% { left: 50%; }
  100% { left: 150%; }
}

@keyframes rotate {
  0% { transform: translate(-50%, -50%) rotate(0deg); }
  100% { transform: translate(-50%, -50%) rotate(360deg); }
}

@keyframes hexFloat {
  0%, 100% { 
    transform: rotate(45deg) translateY(0px);
    opacity: 0.6;
  }
  50% { 
    transform: rotate(45deg) translateY(-10px);
    opacity: 1;
  }
}

@keyframes waveExpand {
  0% {
    transform: scale(0.5);
    opacity: 0.8;
  }
  100% {
    transform: scale(2);
    opacity: 0;
  }
}

@keyframes diamondPulse {
  0%, 100% {
    box-shadow: 
      0 0 20px rgba(0, 255, 255, 0.8),
      0 0 40px rgba(0, 255, 255, 0.4);
    transform: translate(-50%, -50%) rotate(45deg) scale(1);
  }
  50% {
    box-shadow: 
      0 0 30px rgba(0, 255, 255, 1),
      0 0 60px rgba(0, 255, 255, 0.6);
    transform: translate(-50%, -50%) rotate(45deg) scale(1.1);
  }
}

@keyframes ringRotate {
  0% {
    transform: translate(-50%, -50%) rotate(-45deg);
  }
  100% {
    transform: translate(-50%, -50%) rotate(315deg);
  }
}

@keyframes dotGlow {
  0%, 100% {
    opacity: 0.6;
    transform: scale(1);
    box-shadow: 0 0 12px rgba(0, 255, 255, 0.8);
  }
  50% {
    opacity: 1;
    transform: scale(1.3);
    box-shadow: 0 0 20px rgba(0, 255, 255, 1);
  }
}

@keyframes scanRotate {
  0% {
    transform: translate(-50%, -50%) rotate(0deg);
  }
  100% {
    transform: translate(-50%, -50%) rotate(360deg);
  }
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .login-content {
    width: 90%;
    max-width: 900px;
  }
  
  .feature-list {
    margin-top: 2rem;
  }
  
  .feature-item {
    padding: 0.8rem;
    margin: 1rem 0;
  }
}

@media (max-width: 768px) {
  .login-content {
    flex-direction: column;
    height: auto;
    width: 95%;
    max-width: none;
  }
  
  .brand-section {
    flex: none;
    padding: 2rem 1rem;
  }
  
  .brand-logo {
    margin-bottom: 1.5rem;
  }
  
  .tech-diamond {
    width: 80px;
    height: 80px;
    margin-bottom: 1rem;
  }
  
  .title-main {
    font-size: 2rem;
  }
  
  .platform-description {
    display: none;
  }
  
  .feature-list {
    display: none;
  }
  
  .login-form-wrapper {
    flex: none;
    padding: 1rem;
  }
  
  .form-container {
    padding: 2rem;
    background: rgba(17, 24, 39, 0.9);
  }
}
</style>