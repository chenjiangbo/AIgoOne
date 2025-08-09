import { test, expect } from '@playwright/test';

test('业务树页面调试测试', async ({ page }) => {
  console.log('开始测试...');
  
  // 1. 登录
  console.log('步骤1: 访问登录页');
  await page.goto('http://localhost:5173/login');
  await page.screenshot({ path: 'test-results/screenshots/debug-1-login.png' });
  
  console.log('步骤2: 填写登录信息');
  await page.fill('input', 'admin');
  await page.fill('input[type="password"]', 'admin123');
  await page.screenshot({ path: 'test-results/screenshots/debug-2-filled.png' });
  
  console.log('步骤3: 点击登录');
  await page.click('button[type="submit"]');
  await page.waitForTimeout(2000);
  await page.screenshot({ path: 'test-results/screenshots/debug-3-after-login.png' });
  
  // 2. 导航到业务树管理
  console.log('步骤4: 导航到业务树管理');
  const currentUrl = page.url();
  console.log('当前URL:', currentUrl);
  
  await page.goto('http://localhost:5173/system/business-tree');
  await page.waitForTimeout(3000);
  await page.screenshot({ path: 'test-results/screenshots/debug-4-business-tree.png' });
  
  // 3. 检查页面元素
  console.log('步骤5: 检查页面元素');
  
  // 查找容器
  const container = page.locator('.business-tree-container');
  const containerExists = await container.count() > 0;
  console.log('容器存在:', containerExists);
  
  if (!containerExists) {
    // 尝试其他选择器
    const pageContent = await page.content();
    console.log('页面内容长度:', pageContent.length);
    
    // 查找任何包含"业务"的元素
    const businessElements = await page.locator('text=/业务/').count();
    console.log('包含"业务"的元素数量:', businessElements);
    
    // 查找所有的div
    const divCount = await page.locator('div').count();
    console.log('div元素数量:', divCount);
    
    // 查找具体的类名
    const classNames = [
      '.ant-layout',
      '.ant-layout-content',
      '.page-container',
      '.ant-tree',
      '.tree-container'
    ];
    
    for (const className of classNames) {
      const count = await page.locator(className).count();
      console.log(`${className} 数量:`, count);
    }
  }
  
  // 4. 检查树组件
  console.log('步骤6: 检查树组件');
  const tree = page.locator('.ant-tree');
  const treeExists = await tree.count() > 0;
  console.log('树组件存在:', treeExists);
  
  if (treeExists) {
    // 获取树节点
    const treeNodes = await page.locator('.ant-tree-node-content-wrapper').count();
    console.log('树节点数量:', treeNodes);
    
    // 获取第一个节点的文本
    if (treeNodes > 0) {
      const firstNodeText = await page.locator('.ant-tree-node-content-wrapper').first().textContent();
      console.log('第一个节点文本:', firstNodeText);
    }
  }
  
  // 5. 检查工具栏
  console.log('步骤7: 检查工具栏');
  const buttons = await page.locator('button').count();
  console.log('按钮数量:', buttons);
  
  // 获取所有按钮的文本
  for (let i = 0; i < Math.min(buttons, 10); i++) {
    const buttonText = await page.locator('button').nth(i).textContent();
    console.log(`按钮${i + 1}:`, buttonText);
  }
  
  // 6. 最终截图
  await page.screenshot({ path: 'test-results/screenshots/debug-final.png', fullPage: true });
  
  console.log('测试完成');
});