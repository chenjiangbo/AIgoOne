import { test, expect } from '@playwright/test';

test('基础连接测试', async ({ page }) => {
  // 测试前端是否可访问
  await page.goto('http://localhost:5173');
  
  // 检查页面是否加载
  const title = await page.title();
  console.log('页面标题:', title);
  
  // 截图
  await page.screenshot({ path: 'test-results/screenshots/home.png' });
  
  // 检查是否重定向到登录页
  await page.waitForTimeout(2000);
  const url = page.url();
  console.log('当前URL:', url);
  
  expect(url).toContain('login');
});

test('登录测试', async ({ page }) => {
  // 访问登录页
  await page.goto('http://localhost:5173/login');
  await page.waitForTimeout(1000);
  
  // 截图登录页
  await page.screenshot({ path: 'test-results/screenshots/login-page.png' });
  
  // 查找用户名输入框
  const usernameInput = page.locator('input').first();
  const passwordInput = page.locator('input[type="password"]');
  const submitButton = page.locator('button[type="submit"]');
  
  // 检查元素是否存在
  await expect(usernameInput).toBeVisible();
  await expect(passwordInput).toBeVisible();
  await expect(submitButton).toBeVisible();
  
  // 填写登录表单
  await usernameInput.fill('admin');
  await passwordInput.fill('admin123');
  
  // 截图填写后的表单
  await page.screenshot({ path: 'test-results/screenshots/login-filled.png' });
  
  // 点击登录
  await submitButton.click();
  
  // 等待导航
  await page.waitForTimeout(3000);
  
  // 检查是否登录成功
  const afterLoginUrl = page.url();
  console.log('登录后URL:', afterLoginUrl);
  
  // 截图登录后的页面
  await page.screenshot({ path: 'test-results/screenshots/after-login.png' });
  
  expect(afterLoginUrl).not.toContain('login');
});