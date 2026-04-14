# 🧠 Luffy Knowledge Base

> AI Agent 团队运维知识库 — 版本控制 + 持续沉淀
>
> **Maintainer**: Luffy（Robin Z 的专属 AI 助手）
> **Owner**: Robin Z（@RobinZorro86）
> **Repo**: https://github.com/RobinZorro86/luffy-knowledge-base
> **Last Sync**: 2026-04-14

---

## 📌 项目简介

本仓库是 **Luffy Knowledge Base** 的官方版本控制仓库，用于：

1. **沉淀** — AI Agent 团队（Robin + Luffy + Zorro-Ops/Research/Edu）的运维经验
2. **追踪** — 所有 SOP、规范、技能文档的变更历史
3. **协作** — Robin 与 Luffy 之间的知识共享
4. **备份** — 本地 `~/wiki/` 和 `~/.hermes/skills/` 的 GitHub 备份

---

## 📁 仓库结构

```
luffy-knowledge-base/
├── README.md              # 本文件
├── CHANGELOG.md           # 更新日志（按日期记录所有变更）
├── CONTRIBUTING.md        # 贡献指南（Luffy 自管理规则）
├── .gitignore             # Git 忽略规则
│
├── teams/                 # Agent 团队规范
│   ├── luffy-role.md          # Luffy 角色定义（v1.1）
│   ├── luffy-task-board.md    # 任务看板（v1.1）
│   ├── task-prioritization.md  # 任务分级制度 P0/P1/P2/P3
│   ├── delegation-sop.md       # 任务下放 SOP
│   │
│   ├── zorro-ops/
│   │   ├── ops-log.md         # 执行日志（每日更新）
│   │   └── tweet-scraping-sop.md  # 推文抓取 SOP
│   │
│   ├── zorro-research/
│   │   └── tweet-discovery-log.md  # 推文发现日志
│   │
│   └── zorro-edu/
│
├── knowledge-base/        # 知识库规范
│   └── 知识库规范/
│       ├── 任务完成标准.md    # 4类任务的完成标准 + 质量评级
│       └── 推文入库标准.md    # 推文入库格式规范
│
├── skills/                # Hermes Skills（优化后版本）
│   ├── zorro-ops/SKILL.md        # Zorro-Ops（v1.1）
│   ├── zorro-research/SKILL.md    # Zorro-Research（v1.1）
│   └── zorro-edu/SKILL.md         # Zorro-Edu
│
├── scripts/               # 自动化脚本
│   └── wiki-validate.py  # 入库质量验证脚本
│
└── references/           # 参考资料（待扩展）
```

---

## 🔗 关联系统

| 系统 | 路径 | 说明 |
|------|------|------|
| 本地 Wiki | `~/wiki/` | 实际工作目录 |
| 本地 Skills | `~/.hermes/skills/` | Hermes 运行时的 skills |
| GitHub 备份 | 本仓库 | 由 `sync.sh` 自动同步 |
| Cron 调度 | Hermes cron | 定时触发各 Agent 任务 |

---

## 📊 版本历史

| 版本 | 日期 | 主要内容 |
|------|------|---------|
| v0.1.0 | 2026-04-14 | 初始化仓库，首次推送 teams + skills + knowledge-base |
| — | — | 详见 [CHANGELOG.md](./CHANGELOG.md) |

---

## 🔄 同步机制

### 自动同步（cron）

| 时间 | 任务 | 交付 |
|------|------|------|
| 每天 20:00 | `sync.sh` 自动同步 | GitHub push |
| 每周一 09:00 | 完整同步 + 周报 | GitHub push |

### 手动同步

```bash
# 同步所有变更
bash ~/luffy-knowledge-base/sync.sh

# 或手动
cd ~/luffy-knowledge-base
git add -A
git commit -m "type: 描述"
git push
```

---

## 📋 团队架构

```
Robin Z（Owner）
  │
  ├── Luffy（架构师 / 分诊官）
  │     ├─ 角色定义：teams/luffy-role.md
  │     ├─ 任务看板：teams/luffy-task-board.md
  │     └─ 职责：SOP设计 / 任务分配 / 质量评估 / 阻塞上报
  │
  ├── Zorro-Ops（运维 + 执行专家）
  │     ├─ Skill：skills/zorro-ops/SKILL.md
  │     ├─ 日志：teams/zorro-ops/ops-log.md
  │     └─ 职责：系统运维 / Camofox抓取 / eBay自动化
  │
  ├── Zorro-Research（研究专家）
  │     ├─ Skill：skills/zorro-research/SKILL.md
  │     ├─ 日志：teams/zorro-research/tweet-discovery-log.md
  │     └─ 职责：Polymarket报告 / 知识库编译 / 内容创作
  │
  └── Zorro-Edu（教育课程研发）
        ├─ Skill：skills/zorro-edu/SKILL.md
        └─ 职责：儿童AI课程体系搭建
```

---

## 📖 文档索引

| 文档 | 用途 |
|------|------|
| [CHANGELOG.md](./CHANGELOG.md) | **必读** — 所有变更的详细记录 |
| [CONTRIBUTING.md](./CONTRIBUTING.md) | **必读** — Luffy 自管理规则 |
| [teams/luffy-role.md](./teams/luffy-role.md) | Luffy 角色升级定义（架构师 v1.1）|
| [teams/task-prioritization.md](./teams/task-prioritization.md) | 任务优先级制度 |
| [teams/delegation-sop.md](./teams/delegation-sop.md) | Luffy → Zorro 任务下放 SOP |
| [knowledge-base/知识库规范/推文入库标准.md](./knowledge-base/知识库规范/推文入库标准.md) | 推文入库格式规范 |
| [knowledge-base/知识库规范/任务完成标准.md](./knowledge-base/知识库规范/任务完成标准.md) | 4类任务完成标准 |

---

## 🛠 维护工具

| 工具 | 说明 |
|------|------|
| `sync.sh` | 自动同步脚本（源 → 镜像 → GitHub）|
| `wiki-validate.py` | 入库质量验证脚本 |
| Darwin Skill | Skill 质量优化（`darwin-skill`）|

---

## 📌 快速开始

### Luffy 日常工作流

```
1. 收到 Robin 指令
       ↓
2. 判断：P0/P1/P2/P3？
       ↓
3. 设计 SOP 或分配任务
       ↓
4. 评估 Zorro 输出
       ↓
5. 交付 Robin 或打回重做
       ↓
6. 变更同步到 GitHub（sync.sh）
```

### 查看当前任务状态

→ [teams/luffy-task-board.md](./teams/luffy-task-board.md)

---

## ⚠️ 重要原则

1. **源文件在 `~/wiki/`**，本仓库是镜像备份
2. **所有规范变更必须 commit + push**，不可直接改本仓库跳过同步
3. **Skill 优化后立即同步**，不让本地和 GitHub 版本脱节
4. **每日 20:00 自动同步**，保证 GitHub 始终是最新备份

---

*本仓库由 Luffy 自动维护*
*最后更新：2026-04-14*
