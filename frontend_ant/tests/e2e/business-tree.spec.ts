import { test, expect, Page } from '@playwright/test';

// 测试数据
const TEST_DATA = {
  admin: {
    username: 'admin',
    password: 'admin123'
  },
  testNode: {
    name: '自动测试节点',
    editedName: '已编辑的测试节点',
    roles: ['admin', 'operator', 'viewer']
  }
};

// 辅助函数
class BusinessTreePage {
  constructor(private page: Page) {}

  async login(username: string, password: string) {
    await this.page.goto('/login');
    await this.page.fill('input[placeholder*="用户名"]', username);
    await this.page.fill('input[type="password"]', password);
    await this.page.click('button[type="submit"]');
    await this.page.waitForURL('**/home');
  }

  async navigateToBusinessTree() {
    await this.page.goto('/system/business-tree');
    await this.page.waitForSelector('.business-tree-container', { timeout: 10000 });
  }

  async waitForTreeLoad() {
    await this.page.waitForSelector('.ant-tree', { timeout: 10000 });
    await this.page.waitForTimeout(500); // 等待动画完成
  }

  async expandAllNodes() {
    const expandButton = this.page.locator('button').filter({ hasText: /展开|Expand/i }).first();
    if (await expandButton.isVisible()) {
      await expandButton.click();
      await this.page.waitForTimeout(300);
    }
  }

  async selectNode(nodeName: string) {
    const node = this.page.locator('.ant-tree-node-content-wrapper').filter({ hasText: nodeName }).first();
    await node.click();
    await this.page.waitForTimeout(300);
  }

  async clickAddButton() {
    await this.page.click('button:has-text("添加")');
    await this.page.waitForSelector('.ant-modal', { state: 'visible' });
  }

  async clickEditButton() {
    await this.page.click('button:has-text("编辑")');
    await this.page.waitForSelector('.ant-modal', { state: 'visible' });
  }

  async clickDeleteButton() {
    await this.page.click('button:has-text("删除")');
  }

  async fillNodeForm(name: string) {
    await this.page.fill('input[placeholder*="节点名称"]', name);
  }

  async submitForm() {
    await this.page.click('.ant-modal-footer button.ant-btn-primary');
    await this.page.waitForTimeout(500);
  }

  async confirmDelete() {
    // 等待确认对话框
    await this.page.waitForSelector('.ant-popconfirm', { state: 'visible' });
    await this.page.click('.ant-popconfirm button.ant-btn-primary');
    await this.page.waitForTimeout(500);
  }

  async checkNodeExists(nodeName: string) {
    return await this.page.locator('.ant-tree-node-content-wrapper').filter({ hasText: nodeName }).count() > 0;
  }

  async checkMessage(type: 'success' | 'error') {
    const messageSelector = type === 'success' ? '.ant-message-success' : '.ant-message-error';
    return await this.page.locator(messageSelector).isVisible();
  }

  async takeScreenshot(name: string) {
    await this.page.screenshot({ 
      path: `test-results/screenshots/${name}.png`,
      fullPage: true 
    });
  }
}

// 测试套件
test.describe('业务树管理功能测试', () => {
  let treePage: BusinessTreePage;

  test.beforeEach(async ({ page }) => {
    treePage = new BusinessTreePage(page);
    
    // 登录
    await treePage.login(TEST_DATA.admin.username, TEST_DATA.admin.password);
    
    // 导航到业务树管理页面
    await treePage.navigateToBusinessTree();
    
    // 等待树加载
    await treePage.waitForTreeLoad();
  });

  test('页面加载和初始状态', async ({ page }) => {
    // 检查页面标题
    await expect(page.locator('.page-header h2')).toContainText('业务树管理');
    
    // 检查工具栏按钮
    await expect(page.locator('button:has-text("添加")')).toBeVisible();
    await expect(page.locator('button:has-text("编辑")')).toBeVisible();
    await expect(page.locator('button:has-text("删除")')).toBeVisible();
    await expect(page.locator('button:has-text("刷新")')).toBeVisible();
    
    // 检查树组件
    await expect(page.locator('.ant-tree')).toBeVisible();
    
    // 检查根节点
    await expect(page.locator('.ant-tree-node-content-wrapper').first()).toContainText('业务管理');
    
    // 截图保存初始状态
    await treePage.takeScreenshot('initial-state');
  });

  test('展开和折叠树节点', async ({ page }) => {
    // 展开所有节点
    await treePage.expandAllNodes();
    
    // 检查是否有展开的节点
    const expandedNodes = await page.locator('.ant-tree-treenode-switcher-open').count();
    expect(expandedNodes).toBeGreaterThan(0);
    
    // 折叠第一个可折叠的节点
    const firstSwitch = page.locator('.ant-tree-switcher').first();
    await firstSwitch.click();
    await page.waitForTimeout(300);
    
    // 验证折叠
    const collapsedNodes = await page.locator('.ant-tree-treenode-switcher-close').count();
    expect(collapsedNodes).toBeGreaterThan(0);
    
    await treePage.takeScreenshot('tree-expanded-collapsed');
  });

  test('添加新节点', async ({ page }) => {
    // 展开树
    await treePage.expandAllNodes();
    
    // 选择父节点
    await treePage.selectNode('业务管理');
    
    // 点击添加按钮
    await treePage.clickAddButton();
    
    // 填写表单
    await treePage.fillNodeForm(TEST_DATA.testNode.name);
    
    // 提交
    await treePage.submitForm();
    
    // 验证成功消息
    await expect(page.locator('.ant-message-success')).toBeVisible();
    
    // 验证节点已添加
    await page.waitForTimeout(1000);
    const nodeExists = await treePage.checkNodeExists(TEST_DATA.testNode.name);
    expect(nodeExists).toBeTruthy();
    
    await treePage.takeScreenshot('node-added');
  });

  test('编辑节点', async ({ page }) => {
    // 首先添加一个测试节点
    await treePage.expandAllNodes();
    await treePage.selectNode('业务管理');
    await treePage.clickAddButton();
    await treePage.fillNodeForm('待编辑节点');
    await treePage.submitForm();
    await page.waitForTimeout(1000);
    
    // 选择刚添加的节点
    await treePage.selectNode('待编辑节点');
    
    // 点击编辑按钮
    await treePage.clickEditButton();
    
    // 清空并填写新名称
    await page.fill('input[placeholder*="节点名称"]', '');
    await treePage.fillNodeForm(TEST_DATA.testNode.editedName);
    
    // 提交
    await treePage.submitForm();
    
    // 验证成功消息
    await expect(page.locator('.ant-message-success')).toBeVisible();
    
    // 验证节点名称已更新
    await page.waitForTimeout(1000);
    const nodeExists = await treePage.checkNodeExists(TEST_DATA.testNode.editedName);
    expect(nodeExists).toBeTruthy();
    
    await treePage.takeScreenshot('node-edited');
  });

  test('删除节点', async ({ page }) => {
    // 首先添加一个测试节点
    await treePage.expandAllNodes();
    await treePage.selectNode('业务管理');
    await treePage.clickAddButton();
    await treePage.fillNodeForm('待删除节点');
    await treePage.submitForm();
    await page.waitForTimeout(1000);
    
    // 选择刚添加的节点
    await treePage.selectNode('待删除节点');
    
    // 点击删除按钮
    await treePage.clickDeleteButton();
    
    // 确认删除
    await treePage.confirmDelete();
    
    // 验证成功消息
    await expect(page.locator('.ant-message-success')).toBeVisible();
    
    // 验证节点已删除
    await page.waitForTimeout(1000);
    const nodeExists = await treePage.checkNodeExists('待删除节点');
    expect(nodeExists).toBeFalsy();
    
    await treePage.takeScreenshot('node-deleted');
  });

  test('刷新功能', async ({ page }) => {
    // 点击刷新按钮
    const refreshButton = page.locator('button:has-text("刷新")');
    await refreshButton.click();
    
    // 等待加载指示器（如果有）
    await page.waitForTimeout(500);
    
    // 验证树重新加载
    await expect(page.locator('.ant-tree')).toBeVisible();
    await expect(page.locator('.ant-tree-node-content-wrapper').first()).toContainText('业务管理');
    
    await treePage.takeScreenshot('after-refresh');
  });

  test('节点选择状态', async ({ page }) => {
    await treePage.expandAllNodes();
    
    // 选择一个节点
    const firstChild = page.locator('.ant-tree-node-content-wrapper').nth(1);
    await firstChild.click();
    
    // 验证选中状态
    await expect(firstChild).toHaveClass(/ant-tree-node-selected/);
    
    // 验证操作按钮启用状态
    await expect(page.locator('button:has-text("编辑")')).toBeEnabled();
    await expect(page.locator('button:has-text("删除")')).toBeEnabled();
    
    await treePage.takeScreenshot('node-selected');
  });

  test('空树状态处理', async ({ page }) => {
    // 这个测试检查如果树为空时的处理
    // 由于我们总有根节点，这里主要检查错误处理
    
    // 尝试删除根节点（应该失败）
    await treePage.selectNode('业务管理');
    
    // 删除按钮对根节点应该被禁用或显示错误
    const deleteButton = page.locator('button:has-text("删除")');
    
    // 如果按钮未禁用，点击后应该显示错误
    if (await deleteButton.isEnabled()) {
      await deleteButton.click();
      // 可能会有确认对话框
      const confirmButton = page.locator('.ant-popconfirm button.ant-btn-primary');
      if (await confirmButton.isVisible()) {
        await confirmButton.click();
        // 应该显示错误消息
        await expect(page.locator('.ant-message-error')).toBeVisible();
      }
    }
    
    await treePage.takeScreenshot('root-node-protection');
  });

  test('表单验证', async ({ page }) => {
    // 选择节点
    await treePage.selectNode('业务管理');
    
    // 打开添加对话框
    await treePage.clickAddButton();
    
    // 尝试提交空表单
    await treePage.submitForm();
    
    // 应该显示验证错误
    await expect(page.locator('.ant-form-item-explain-error')).toBeVisible();
    
    // 输入过长的名称
    const longName = 'a'.repeat(100);
    await treePage.fillNodeForm(longName);
    
    // 截图验证状态
    await treePage.takeScreenshot('form-validation');
    
    // 关闭对话框
    await page.keyboard.press('Escape');
  });

  test('响应式布局', async ({ page }) => {
    // 测试不同视口大小
    const viewports = [
      { width: 1920, height: 1080, name: 'desktop' },
      { width: 768, height: 1024, name: 'tablet' },
      { width: 375, height: 667, name: 'mobile' }
    ];
    
    for (const viewport of viewports) {
      await page.setViewportSize({ width: viewport.width, height: viewport.height });
      await page.waitForTimeout(500);
      
      // 验证关键元素仍然可见
      await expect(page.locator('.business-tree-container')).toBeVisible();
      await expect(page.locator('.ant-tree')).toBeVisible();
      
      await treePage.takeScreenshot(`responsive-${viewport.name}`);
    }
  });
});

// 性能测试
test.describe('性能测试', () => {
  test('页面加载性能', async ({ page }) => {
    const startTime = Date.now();
    
    await page.goto('/login');
    await page.fill('input[placeholder*="用户名"]', TEST_DATA.admin.username);
    await page.fill('input[type="password"]', TEST_DATA.admin.password);
    await page.click('button[type="submit"]');
    await page.waitForURL('**/dashboard');
    
    await page.goto('/system/business-tree');
    await page.waitForSelector('.ant-tree', { timeout: 10000 });
    
    const loadTime = Date.now() - startTime;
    
    // 页面加载应该在5秒内完成
    expect(loadTime).toBeLessThan(5000);
    
    console.log(`页面加载时间: ${loadTime}ms`);
  });
});

// 错误处理测试
test.describe('错误处理', () => {
  test('网络错误处理', async ({ page, context }) => {
    const treePage = new BusinessTreePage(page);
    
    // 登录
    await treePage.login(TEST_DATA.admin.username, TEST_DATA.admin.password);
    
    // 模拟网络错误
    await context.route('**/api/business-tree/**', route => {
      route.abort('failed');
    });
    
    // 尝试导航到页面
    await page.goto('/system/business-tree');
    
    // 应该显示错误消息或加载失败状态
    const errorVisible = await page.locator('.ant-message-error, .ant-empty').isVisible();
    expect(errorVisible).toBeTruthy();
    
    await treePage.takeScreenshot('network-error');
  });
});