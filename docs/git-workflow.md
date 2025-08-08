# AIgoOne 项目 Git 协作工作流指南

## 分支策略

### 主要分支
- **`master/main`** - 生产环境代码，始终保持稳定
- **`develop`** - 开发主线，集成各个功能分支

### 功能分支
- **`feature/功能名称`** - 开发新功能
- **`bugfix/bug描述`** - 修复bug
- **`hotfix/紧急修复`** - 生产环境紧急修复

## 协作工作流程

### 1. 开始开发新功能

```bash
# 1. 确保本地代码最新
git checkout master
git pull origin master

# 2. 创建功能分支
git checkout -b feature/device-monitoring

# 3. 开发功能...
# 编写代码，提交更改

# 4. 推送分支到远程
git push -u origin feature/device-monitoring
```

### 2. 开发过程中

```bash
# 定期提交代码
git add .
git commit -m "feat: 添加设备状态监控功能"

# 推送到远程分支
git push
```

### 3. 功能开发完成

```bash
# 1. 确保代码最新
git checkout master
git pull origin master

# 2. 合并最新代码到功能分支
git checkout feature/device-monitoring
git merge master

# 3. 解决冲突（如果有）
# 4. 推送更新
git push

# 5. 在GitHub上创建Pull Request
```

### 4. 代码审查和合并

1. 在GitHub上创建Pull Request
2. 团队成员审查代码
3. 通过自动化测试
4. 合并到master分支
5. 删除功能分支

## 提交信息规范

```
类型(范围): 简短描述

详细描述（可选）

- feat: 新功能
- fix: bug修复
- docs: 文档更新
- style: 代码格式
- refactor: 重构
- test: 测试
- chore: 构建/工具

示例:
feat(device): 添加设备实时监控功能
fix(auth): 修复登录Token过期问题
docs: 更新API文档
```

## 冲突解决

当多人修改同一文件时：

```bash
# 1. 拉取最新代码
git pull origin master

# 2. 如果有冲突，手动编辑文件解决
# 文件中会显示：
# <<<<<<< HEAD
# 你的代码
# =======
# 他人的代码
# >>>>>>> branch-name

# 3. 解决后提交
git add .
git commit -m "resolve: 解决合并冲突"
```

## 日常命令速查

```bash
# 查看分支
git branch -a

# 切换分支
git checkout branch-name

# 创建并切换分支
git checkout -b new-branch

# 查看状态
git status

# 查看提交历史
git log --oneline --graph

# 推送分支
git push origin branch-name

# 拉取最新代码
git pull origin master
```

## 注意事项

1. **永远不要直接在master分支开发**
2. **功能分支要及时同步master的最新代码**
3. **提交信息要清晰明确**
4. **大功能要拆分成小的提交**
5. **Push前先Pull，避免冲突**