import { createRouter, createWebHistory } from 'vue-router'
import { verifyToken } from '@/api/auth';

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/login/index.vue')
  },
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('@/views/dashboard/index.vue'),
    meta: { requiresAuth: true }
  },
  // 重定向到登录页
  {
    path: '/dashboard',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫
router.beforeEach(async (to, from, next) => {
  const token = localStorage.getItem('token');

  if (to.meta.requiresAuth) {
    if (token) {
      try {
        // 在访问需要认证的路由前，先验证token是否有效
        await verifyToken();
        next();
      } catch (error) {
        // token无效，清除本地存储并重定向到登录页
        localStorage.removeItem('token');
        next('/login');
      }
    } else {
      // 没有token，直接重定向到登录页
      next('/login');
    }
  } else if (to.path === '/login' && token) {
    // 如果用户已登录（本地有token），尝试访问登录页则直接重定向到首页
    next('/');
  } else {
    next();
  }
});

export default router
