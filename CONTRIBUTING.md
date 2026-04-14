# CONTRIBUTING — Luffy Knowledge Base

> 本仓库由 **Luffy** 自动维护。
> Robin Z（Owner）可以直接指令 Luffy 进行变更。
>
> 本文件是 **Luffy 自管理规则的完整文档**，也是贡献规范。

---

## 📋 目录

1. [角色定义](#1-角色定义)
2. [贡献者类型](#2-贡献者类型)
3. [文件命名规范](#3-文件命名规范)
4. [目录结构规范](#4-目录结构规范)
5. [Commit 规范](#5-commit-规范)
6. [CHANGELOG 规范](#6-changelog-规范)
7. [同步规范](#7-同步规范)
8. [SOP 编写规范](#8-sop-编写规范)
9. [Skill 编写规范](#9-skill-编写规范)
10. [冲突处理](#10-冲突处理)

---

## 1. 角色定义

| 角色 | 身份 | 权限 |
|------|------|------|
| **Owner** | Robin Z（@RobinZorro86）| 最高权限，可直接指令 Luffy |
| **Maintainer** | Luffy（AI Agent）| 自动维护，遵循本 SOP |

**Luffy 职责：**
- 遵循本 CONTRIBUTING.md 的所有规范
- 主动维护 CHANGELOG
- 主动执行 sync.sh 同步
- 发现问题时主动报告 Robin

---

## 2. 贡献者类型

### Type A：Luffy（Maintainer，自动）

- 通过 cron 任务和 SOP 自动驱动
- 所有变更由 Luffy 发起 → Robin 指令或 Luffy 自主判断
- Luffy 是唯一有权直接提交（commit + push）的人

### Type B：Robin（Owner）

- 通过 Telegram 指令 Luffy 进行变更
- 不直接操作本仓库（由 Luffy 代为操作）
- 如在 GitHub 网页上直接修改 → 通知 Luffy 同步

---

## 3. 文件命名规范

### Markdown 文件

| 类型 | 规则 | 示例 |
|------|------|------|
| SOP 文档 | `xxx-sop.md` | `delegation-sop.md` |
| 角色定义 | `xxx-role.md` | `luffy-role.md` |
| 任务看板 | `xxx-task-board.md` | `luffy-task-board.md` |
| 制度文档 | `xxx-prioritization.md` | `task-prioritization.md` |
| 日志 | `xxx-log.md` 或 `xxx-log/` | `ops-log.md` |
| 规范 | `xxx标准.md` | `任务完成标准.md` |
| 入库文档 | `{年份}-{关键词}.md` | `2026-AI-Agent架构.md` |

### Skill 文件

| 类型 | 路径 | 命名 |
|------|------|------|
| Skill 主文件 | `~/.hermes/skills/{name}/SKILL.md` | 全小写，中划线 |
| Skill 目录 | `~/.hermes/skills/{name}/` | 同上 |
| Skill 引用文件 | `references/*.md` | 按用途命名 |

### 脚本文件

| 类型 | 规则 | 示例 |
|------|------|------|
| Shell 脚本 | `xxx.sh` | `sync.sh` |
| Python 脚本 | `xxx.py` | `wiki-validate.py` |

---

## 4. 目录结构规范

```
luffy-knowledge-base/
├── README.md              # 入口文档（不重复仓库内容）
├── CHANGELOG.md           # 更新日志（必读）
├── CONTRIBUTING.md        # 本文件
├── .gitignore             # 必读
│
├── teams/                 # Agent 团队规范（SOP/角色/看板）
│   ├── luffy-*.md             # Luffy 相关规范
│   ├── task-*.md              # 任务相关规范
│   ├── delegation-*.md        # 下放 SOP
│   ├── zorro-ops/            # Zorro-Ops 专属
│   ├── zorro-research/       # Zorro-Research 专属
│   └── zorro-edu/            # Zorro-Edu 专属
│
├── knowledge-base/        # 知识库（规范/模板）
│   └── 知识库规范/              # 知识库操作规范
│
├── skills/                # Skills（优化后镜像）
│   ├── {agent-name}/SKILL.md
│   └── {agent-name}/references/
│
├── scripts/               # 自动化脚本
│   ├── sync.sh               # 必读：同步脚本
│   └── *.py                  # Python 工具
│
└── references/           # 参考资料（不主动修改）
```

### 目录放置规则

| 内容 | 放置位置 | 原因 |
|------|---------|------|
| Luffy 自建 SOP | `teams/` | 团队管理文档 |
| Zorro 操作规范 | `teams/zorro-xxx/` | 归属明确 |
| 知识库规范 | `knowledge-base/` | 知识库操作规范 |
| Skill 镜像 | `skills/` | Hermes 运行态镜像 |
| 自动化脚本 | `scripts/` | 工具类 |
| 参考资料 | `references/` | 引用但不维护 |

---

## 5. Commit 规范

### 格式

```bash
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Type

| Type | 含义 | 使用场景 |
|------|------|---------|
| `feat` | 新功能 | 新增 SOP/Skill/脚本 |
| `fix` | 修复 | 修复规范错误/脚本bug |
| `update` | 更新 | 更新已有内容（不是新功能）|
| `docs` | 文档 | 文档变更（README/CHANGELOG/CONTRIBUTING）|
| `refactor` | 重构 | 重命名/移动/格式调整，无功能变化 |
| `chore` | 维护 | 同步/script/配置变更 |
| `test` | 测试 | 测试相关 |

### Scope（范围）

| Scope | 含义 |
|-------|------|
| `teams` | teams/ 目录下的变更 |
| `skills` | skills/ 目录下的变更 |
| `knowledge-base` | knowledge-base/ 目录下的变更 |
| `scripts` | scripts/ 目录下的变更 |
| `docs` | 文档类变更 |
| `sync` | 同步类变更 |
| `cron` | Cron 任务变更 |

### 示例

```
feat(teams): 新增 zorro-ops 推文抓取 SOP

- Camofox 抓取 → 整理 → 自检 → 入库全流程
- 包含边界处理矩阵和失败处理
Closes: #N（如果有关联issue）

docs(changelog): 更新 CHANGELOG 至 v1.0.0

chore(sync): 每日同步 — 2026-04-14

refactor(teams): 重命名 task-prioritization-v2.md → task-prioritization.md
```

### Commit 黄金规则

1. **每提交必有意义**：不要无意义的小提交（如只改一个错字就单独提交）
2. **描述要具体**：`update ops-log` → `update(teams): 补充 Camofox 边界处理到 ops-log`
3. **中文描述**：本仓库使用中文 commit message
4. **一行不超过72字**
5. **.body 描述为什么改**，不描述改了什么（改了什么看 diff）

---

## 6. CHANGELOG 规范

### 每次 Commit 后

在 `CHANGELOG.md` 的 `[Unreleased]` section 下追加变更：

```markdown
## [Unreleased]

### Added
- `teams/delivery-sop.md` — 新增任务下放 SOP

### Changed
- `teams/luffy-role.md` — Luffy 角色升级至 v1.1
```

### 版本发布

当有重要里程碑时（通常是每天或每周），将 `[Unreleased]` 转为正式版本：

```markdown
## [1.0.1] — 2026-04-15

[将 Unreleased 的内容移到这里]

---

## [Unreleased]
[新内容从这里开始]
```

### 版本号规则

```
[MAJOR.MINOR.PATCH]

MAJOR: 架构重构，角色定位根本改变
MINOR: 新增重要模块（SOP/Skill/工具链）
PATCH: 日常维护（文档修正/小优化/同步）
```

---

## 7. 同步规范

### 同步触发规则

| 触发 | 操作 |
|------|------|
| Skill 优化完成 | 立即 `sync.sh` + commit + push |
| 新建 SOP/规范 | 立即同步 |
| 新增 cron 任务 | 更新相关 SOP + 同步 |
| 每天 20:00 | `sync.sh` 自动同步 |
| 每周一 09:00 | 完整同步 + 周报 |

### 同步命令

```bash
# 推荐：使用同步脚本
bash ~/luffy-knowledge-base/sync.sh

# 手动同步
cd ~/luffy-knowledge-base
git add -A
git commit -m "type(scope): 描述"
git push
```

---

## 8. SOP 编写规范

### 必须包含的章节

```markdown
# {SOP名称}

> 版本：vx.x | YYYY-MM-DD
> 维护：{维护者}
> 目的：{一句话说明解决什么问题}

---

## 1. 触发条件
## 2. 前置要求
## 3. 执行步骤（编号）
## 4. 输出格式
## 5. 失败处理
## 6. 边界条件
## 7. 关联文档
## 8. 变更记录
```

### SOP 编写原则

1. **触发条件要明确**：什么情况下执行，什么情况下跳过
2. **步骤可验证**：每个步骤完成后能验证是否正确
3. **输出格式固定**：输出物格式必须固定
4. **失败有兜底**：失败了怎么办，谁来处理
5. **不写废话**：SOP 本身就是约束，不是说明书

---

## 9. Skill 编写规范

### 必须包含的 frontmatter

```yaml
---
name: skill-name
description: 一句话说明这个skill做什么
trigger: 触发场景（用 | 分隔）
version: v1.x
---
```

### 必须包含的章节

```markdown
# {Skill名称} SKILL.md

## 角色定义
## 核心职责（分模块）
## 协作协议
## 行为准则
## 关键文件路径
## 变更记录
```

---

## 10. 冲突处理

### 本地与 GitHub 冲突

**原因：** 在 GitHub 网页改了，或另一处改了。

**处理流程：**

```bash
# 1. 先拉取
cd ~/luffy-knowledge-base
git fetch origin

# 2. 查看差异
git diff HEAD origin/main

# 3. 评估：
#    → 本地更重要：继续，不 force push（除非确认）
#    → GitHub 更重要：git checkout -- 文件，放弃本地
#    → 两者都要：手动合并

# 4. 解决后
git add -A
git commit -m "fix: 解决冲突 — YYYY-MM-DD"
git push
```

### 冲突预防

1. **不要在 GitHub 网页直接改**（让 Luffy 同步）
2. **避免多设备同时操作**（当前单设备，无问题）
3. **同步脚本自动处理**（不会漏同步）

---

## ⚠️ 禁止事项

1. ❌ 不在 GitHub 网页直接编辑（跳过 Luffy 同步流程）
2. ❌ 不直接修改 `references/`（引用但不维护）
3. ❌ 不上传包含 API Key 的文件（.gitignore 已排除）
4. ❌ 不在 commit message 里写 API Key 或 Token
5. ❌ 不 force push（除非确认，如初始建仓阶段）

---

*本 CONTRIBUTING.md 由 Luffy 维护*
*最后更新：2026-04-14*
