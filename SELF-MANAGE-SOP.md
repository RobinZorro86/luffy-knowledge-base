# Luffy 知识库自管理 SOP

> 版本：v1.0 | 2026-04-14
> 维护：Luffy
> 仓库：https://github.com/RobinZorro86/luffy-knowledge-base

---

## 核心原则

### 源文件 vs 镜像文件

| 类型 | 路径 | 性质 | 谁修改 |
|------|------|------|--------|
| **源文件** | `~/wiki/` | 实际工作目录，读写在此 | Luffy / Zorro / Robin |
| **源文件** | `~/.hermes/skills/` | 实际 skills 目录，运行在此 | Luffy（Hermes 运行时读）|
| **镜像文件** | `~/luffy-knowledge-base/` | Git 备份，手动同步 | Luffy |

**规则：**
- 工作在源文件进行
- 有意义的变更（见下方）→ 同步到镜像 → GitHub 提交
- 不在镜像文件里直接工作（避免混乱）

---

## 同步触发条件

### 立即同步（必须）

| 场景 | 操作 |
|------|------|
| Skill 优化/更新 | 立即复制到镜像 → 立即 commit + push |
| 新建 SOP / 规范文档 | 立即同步 → commit + push |
| 新建 cron 任务 | 更新镜像中的相关 SOP → commit + push |
| 任务看板大幅调整 | 同步 → commit + push |

### 每日同步（自动）

| 时间 | 操作 | 方式 |
|------|------|------|
| 每天 20:00 | ops-log + tweet-discovery-log 同步到镜像 | cron 自动 |
| 每天 20:00 | `git add + git commit + git push` | cron 自动 |

### 每周同步（自动）

| 时间 | 操作 |
|------|------|
| 每周一 09:00（Luffy 周报后） | 完整同步所有变更 → push |
| 每周一 09:00 | wiki 中近期入库的推文同步到镜像 |

### 按需同步（手动）

| 场景 | 操作 |
|------|------|
| Robin 要求"保存当前状态" | 立即同步全部 → push |
| 发现本地与 GitHub 差异 | 评估冲突，决定保留哪边 |
| Zorro 团队新建了文件 | 立即同步到镜像 |

---

## 同步命令模板

### 同步单个文件

```bash
# 从源复制到镜像
cp ~/wiki/hermes/teams/luffy-task-board.md \
   ~/luffy-knowledge-base/teams/luffy-task-board.md

# 提交
cd ~/luffy-knowledge-base
git add teams/luffy-task-board.md
git commit -m "update: 任务看板状态同步 — YYYY-MM-DD"
git push
```

### 同步所有变更

```bash
#!/bin/bash
# ~/luffy-knowledge-base/sync.sh

set -e

SRC_WIKI="$HOME/wiki"
SRC_SKILLS="$HOME/.hermes/skills"
DEST="$HOME/luffy-knowledge-base"

DATE=$(date +%Y-%m-%d)

echo "=== 同步 wiki/teams ==="
cp -r "$SRC_WIKI/hermes/teams/"* "$DEST/teams/" 2>/dev/null || true

echo "=== 同步 wiki/知识库规范 ==="
cp -r "$SRC_WIKI/知识库规范/" "$DEST/knowledge-base/" 2>/dev/null || true

echo "=== 同步 skills ==="
for skill in zorro-ops zorro-research zorro-edu; do
    cp "$SRC_SKILLS/$skill/SKILL.md" "$DEST/skills/$skill/" 2>/dev/null || true
done

echo "=== Git 提交 ==="
cd "$DEST"
git add -A
if git diff --cached --quiet; then
    echo "无变更，跳过"
else
    git commit -m "sync: $(date +%Y-%m-%d\ %H:%M) — 自动同步"
    git push
    echo "✅ 已推送"
fi
```

---

## 冲突处理

### 场景1：GitHub 有变更，本地有变更（最常见）

**原因：** 可能在 GitHub 网页上改了，或者另一处（另一台设备）改了。

```
1. 拉取 GitHub 最新：
   git fetch origin

2. 查看差异：
   git diff HEAD origin/main

3. 评估：
   → 本地变更更重要：force push（不推荐，除非确认）
   → GitHub 变更更重要：放弃本地，用 GitHub 版本
   → 两者都要：手动合并

4. 合并示例：
   git stash
   git pull
   git stash pop
   → 手动解决冲突
```

### 场景2：删除了某文件但 GitHub 还有

```bash
git add -A
git commit -m "chore: 移除已删除的文件"
git push
```

---

## 不同步的内容

| 内容 | 原因 |
|------|------|
| `~/wiki/twitter/` 大批量推文 | 文件太多太杂，按需同步 |
| 临时文件 | .gitignore 已排除 |
| `~/.hermes/` 配置 | 包含 API Key，不上传 |
| `~/wiki/zorro/` 内容 | Zorro 自身知识库，另行管理 |
| 大型二进制文件 | .gitignore 已排除 |

---

## 自管理 SOP

Luffy 每隔以下周期自主检查：

### 每小时（轻量）

```
检查项：
- 有没有新的 ops-log 更新？（cat ops-log.md | tail -5）
- 有没有 commit 但没 push 的？（git status）

如果有 → 执行同步
```

### 每日（20:00 cron）

```
1. 运行 ~/luffy-knowledge-base/sync.sh
2. 确认推送成功
3. 确认 GitHub 上能看到最新
```

### 每周一（09:00 Luffy 周报后）

```
1. 完整同步所有源文件
2. 检查 GitHub 提交历史是否有异常
3. 如有新 Skill 优化，评估是否需要单独 commit
```

---

## 文件归属（谁管什么）

| 目录 | 主要管理者 | 同步频率 |
|------|----------|---------|
| `teams/` | Luffy | 有变更立即同步 |
| `knowledge-base/` | Luffy | 有变更立即同步 |
| `skills/` | Luffy（通过 Hermes）| Skill 优化后立即同步 |
| `scripts/` | Luffy | 有变更立即同步 |
| `references/` | Luffy | 按需 |

---

## 分支策略

**当前只有 main 分支。**

如需实验性变更：
```
1. 从 main 创建实验分支：
   git checkout -b experiment/xxx

2. 在实验分支工作

3. 实验成功 → 合并回 main：
   git checkout main
   git merge experiment/xxx
   git push

4. 实验失败 → 删除实验分支：
   git checkout main
   git branch -d experiment/xxx
```

---

## 仓库信息

| 项目 | 值 |
|------|-----|
| 仓库 | https://github.com/RobinZorro86/luffy-knowledge-base |
| 本地路径 | `~/luffy-knowledge-base/` |
| 默认分支 | main |
| 访问方式 | HTTPS（RobinZorro86 token）|

---

## 变更记录

- v1.0 (2026-04-14): 初始版本，定义自管理 SOP、同步规则、冲突处理
