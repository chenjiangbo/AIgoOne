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
            <div class="logo-text">AIgoOne</div>
            <div class="logo-subtitle">算法管理平台</div>
          </div>
          <div class="brand-slogan">
            <p>智能算法，高效管理</p>
            <p>开启AI驱动的未来</p>
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
          
          <el-form 
            ref="loginFormRef" 
            :model="loginForm" 
            :rules="loginRules" 
            class="login-form"
            size="large"
            @keyup.enter="handleLogin"
          >
            <el-form-item prop="username">
              <el-input 
                v-model="loginForm.username" 
                placeholder="请输入用户名"
                prefix-icon="User"
                clearable
                class="tech-input"
              >
                <template #prefix>
                  <el-icon><User /></el-icon>
                </template>
              </el-input>
            </el-form-item>
            
            <el-form-item prop="password">
              <el-input 
                v-model="loginForm.password" 
                type="password" 
                placeholder="请输入密码"
                prefix-icon="Lock"
                show-password
                clearable
                class="tech-input"
              >
                <template #prefix>
                  <el-icon><Lock /></el-icon>
                </template>
              </el-input>
            </el-form-item>

            <!-- 错误提示区域 -->
            <el-alert 
              v-if="errorMessage"
              :title="errorMessage"
              type="error"
              :closable="true"
              show-icon
              style="margin-bottom: 1rem;"
              @close="errorMessage = ''"
            />

            <el-form-item class="login-btn-item">
              <el-button 
                type="primary" 
                :loading="isLoading" 
                class="full-width-btn"
                @click="handleLogin"
                size="large"
                block
              >
                <span v-if="!isLoading">登录</span>
                <span v-else>登录中...</span>
              </el-button>
            </el-form-item>
          </el-form>

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

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { User, Lock } from '@element-plus/icons-vue'
import { login } from '@/api/auth.js';

const router = useRouter()

// 表单ref
const loginFormRef = ref()

// 表单数据
const loginForm = reactive({
  username: '',
  password: ''
})

// 验证规则
const loginRules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 3, max: 20, message: '用户名长度在 3 到 20 个字符', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, max: 20, message: '密码长度在 6 到 20 个字符', trigger: 'blur' }
  ]
}

// 加载状态
const isLoading = ref(false)

// 错误信息
const errorMessage = ref('')

// 登录处理
const handleLogin = async () => {
  if (!loginFormRef.value) return;

  try {
    await loginFormRef.value.validate();
    isLoading.value = true;
    errorMessage.value = ''; // 清除之前的错误信息

    const response = await login({
      username: loginForm.username,
      password: loginForm.password,
    });

    if (response.data.access_token) {
      ElMessage.success({
        message: '登录成功！',
        duration: 2000
      });
      localStorage.setItem('token', response.data.access_token);
      localStorage.setItem('user', JSON.stringify({ name: loginForm.username }));
      router.push('/dashboard');
    } else {
      errorMessage.value = '登录失败，请检查您的凭据。';
    }
  } catch (error) {
    // 根据错误类型显示不同的提示信息
    if (error.response) {
      // 服务器响应了错误状态码
      if (error.response.status === 401) {
        errorMessage.value = '用户名或密码错误！';
      } else if (error.response.status === 500) {
        errorMessage.value = '服务器内部错误，请稍后再试。';
      } else {
        errorMessage.value = error.response.data?.detail || '登录失败，请重试。';
      }
    } else if (error.request) {
      // 请求已发出但没有收到响应（网络错误）
      errorMessage.value = '无法连接到服务器，请检查网络连接或联系管理员。';
    } else {
      // 其他错误
      errorMessage.value = '发生未知错误，请重试。';
    }
  } finally {
    isLoading.value = false;
  }
};

// 生成波浪粒子样式
const getWaveParticleStyle = (index) => {
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
const getWaveLineStyle = (index) => {
  const delay = index * 2
  const opacity = 0.1 + (index * 0.1)
  
  return {
    animationDelay: `${delay}s`,
    opacity: opacity
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

.floating-particles {
  position: absolute;
  width: 100%;
  height: 100%;
}

.particle {
  position: absolute;
  width: 2px;
  height: 2px;
  background: #00ffff;
  border-radius: 50%;
  animation: float 5s ease-in-out infinite;
  box-shadow: 0 0 10px #00ffff;
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
  width: 90%;
  max-width: 1200px;
  height: 70%;
  position: relative;
  z-index: 1;
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

.logo-text {
  font-size: 4rem;
  font-weight: 300;
  letter-spacing: 2px;
  margin-bottom: 0.5rem;
  background: linear-gradient(135deg, #ffffff, #3b82f6);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 30px rgba(59, 130, 246, 0.3);
}

.logo-subtitle {
  font-size: 1.5rem;
  font-weight: 300;
  letter-spacing: 3px;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 2rem;
}

.brand-slogan {
  opacity: 0.7;
}

.brand-slogan p {
  font-size: 1.1rem;
  font-weight: 300;
  margin: 0.5rem 0;
  letter-spacing: 1px;
}

.logo-icon {
  position: relative;
  margin-bottom: 2rem;
  width: 200px;
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 2rem auto;
}

.tech-core {
  position: relative;
  width: 140px;
  height: 140px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

.core-diamond {
  position: relative;
  width: 30px;
  height: 30px;
  background: #00ffff;
  transform: rotate(45deg);
  box-shadow: 
    0 0 20px rgba(0, 255, 255, 0.8),
    0 0 40px rgba(0, 255, 255, 0.4);
  animation: diamondPulse 2.5s ease-in-out infinite;
  z-index: 3;
}

.inner-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 50px;
  height: 50px;
  background: radial-gradient(circle, rgba(0, 255, 255, 0.3), transparent);
  transform: translate(-50%, -50%) rotate(-45deg);
  animation: glowPulse 3s ease-in-out infinite;
}

.orbit-ring {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100px;
  height: 100px;
  border: 1px solid rgba(0, 255, 255, 0.3);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  animation: ringRotate 8s linear infinite;
}

.orbit-dot {
  position: absolute;
  width: 6px;
  height: 6px;
  background: #00ffff;
  border-radius: 50%;
  box-shadow: 0 0 12px rgba(0, 255, 255, 0.8);
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
  max-width: 420px;
  padding: 3rem;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(25px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.2),
    0 0 0 1px rgba(255, 255, 255, 0.05);
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

:deep(.tech-input .el-input__wrapper) {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  backdrop-filter: blur(10px);
  transition: all 0.3s;
}

:deep(.tech-input .el-input__wrapper:hover) {
  border-color: #00ffff;
  box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
}

:deep(.tech-input .el-input__wrapper.is-focus) {
  border-color: #00ffff;
  box-shadow: 0 0 20px rgba(0, 255, 255, 0.4);
}

:deep(.tech-input .el-input__inner) {
  color: white;
}

:deep(.tech-input .el-input__inner::placeholder) {
  color: rgba(255, 255, 255, 0.6);
}

:deep(.tech-input .el-icon) {
  color: #00ffff;
}

.login-btn-item {
  margin-bottom: 0 !important;
}

.login-btn-item {
  margin-top: 1rem;
}

.full-width-btn {
  width: 100%;
  height: 45px;
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
}

.full-width-btn:hover {
  background: linear-gradient(135deg, #2563eb, #1e40af);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
}

.full-width-btn:focus {
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
}

.form-footer {
  text-align: center;
}

.tech-divider {
  width: 100%;
  height: 1px;
  background: linear-gradient(90deg, transparent, #00ffff, transparent);
  margin-bottom: 1rem;
}

.copyright {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.9rem;
  margin: 0;
  line-height: 1.5;
}

/* 动画 */
@keyframes circuitPulse {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.6; }
}

@keyframes gridMove {
  0% { transform: translate(0, 0); }
  100% { transform: translate(50px, 50px); }
}

@keyframes float {
  0%, 100% { 
    transform: translateY(0px) rotate(0deg);
    opacity: 0.7;
  }
  50% { 
    transform: translateY(-20px) rotate(180deg);
    opacity: 1;
  }
}

@keyframes pulse {
  0% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 1;
  }
  100% {
    transform: translate(-50%, -50%) scale(1.5);
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

@keyframes iconPulse {
  0%, 100% { 
    transform: scale(1);
    opacity: 1;
  }
  50% { 
    transform: scale(1.1);
    opacity: 0.8;
  }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes diamondPulse {
  0%, 100% {
    box-shadow: 
      0 0 20px rgba(0, 255, 255, 0.8),
      0 0 40px rgba(0, 255, 255, 0.4);
    transform: rotate(45deg) scale(1);
  }
  50% {
    box-shadow: 
      0 0 30px rgba(0, 255, 255, 1),
      0 0 60px rgba(0, 255, 255, 0.6);
    transform: rotate(45deg) scale(1.1);
  }
}

@keyframes glowPulse {
  0%, 100% {
    opacity: 0.3;
    transform: translate(-50%, -50%) rotate(-45deg) scale(1);
  }
  50% {
    opacity: 0.6;
    transform: translate(-50%, -50%) rotate(-45deg) scale(1.2);
  }
}

@keyframes ringRotate {
  0% {
    transform: translate(-50%, -50%) rotate(0deg);
  }
  100% {
    transform: translate(-50%, -50%) rotate(360deg);
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

/* 响应式设计 */
@media (max-width: 768px) {
  .login-content {
    flex-direction: column;
    height: auto;
    padding: 1rem;
  }
  
  .left-decoration {
    padding: 1rem;
  }
  
  .title-main {
    font-size: 2rem;
  }
  
  .form-container {
    padding: 2rem;
    margin-top: 1rem;
  }
}

/* 修复消息提示层级问题 */
:global(.el-message) {
  z-index: 9999 !important;
}

:global(.el-loading-mask) {
  z-index: 9998 !important;
}
</style>
