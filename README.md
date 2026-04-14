# 🧠 Luffy Knowledge Base

> 版本控制的知识库 + Skills — AI Agent 团队运维经验沉淀
> 维护：Luffy（Robin Z 的专属 AI 助手）
> 仓库：https://github.com/RobinZorro86/luffy-knowledge-base

---

## 仓库结构

```
luffy-knowledge-base/
├── teams/                    # Agent 团队规范
│   ├── luffy-role.md         # Luffy 角色定义（架构师）
│   ├── luffy-task-board.md   # 任务看板
│   ├── task-prioritization.md # 任务分级制度（P0/P1/P2/P3）
│   ├── delegation-sop.md     # 任务下放 SOP
│   ├── zorro-ops/            # Zorro-Ops 规范
│   │   ├── ops-log.md
│   │   └── tweet-scraping-sop.md
│   ├── zorro-research/       # Zorro-Research 规范
│   │   └── memory/
│   └── zorro-edu/            # Zorro-Edu 规范
│
├── knowledge-base/           # 知识库（wiki）
│   ├── 知识库规范/
│   │   ├── 任务完成标准.md
│   │   ├── 推文入库标准.md
│   │   └── 推文发现标准.md
│   ├── twitter/              # 推文入库（按作者）
│   └── hermes/               # Hermes 相关知识
│       └── teams/
│
├── skills/                   # Hermes Skills（优化后版本）
│   ├── zorro-ops/SKILL.md
│   ├── zorro-research/SKILL.md
│   └── zorro-edu/SKILL.md
│
├── scripts/                  # 自动化脚本
│   └── wiki-validate.py      # 入库质量验证脚本
│
└── references/               # 参考资料
    ├── AGENTS.md             # Hermes 开发指南
    └── README.md             # 本文件
```

---

## 版本控制原则

| 类型 | 是否追踪 | 说明 |
|------|---------|------|
| 规范文档（SOP/角色/看板）| ✅ 严格 | 每次变更需记录 |
| 知识库正文 | ✅ 追踪 | 有实质内容更新才提交 |
| Skills | ✅ 严格 | 优化后立即提交 |
| 脚本 | ✅ 追踪 | 需有变更记录 |
| 推文入库 | ⚠️ 可选 | 大量文件可批量提交 |
| 临时文件 | ❌ 不追踪 | .gitignore 排除 |

---

## 提交规范

### Commit Message 格式

```
[type] 简短描述（≤50字）

[type] 可选详细说明（多行）
```

**Type 类型：**
- `feat`：新增功能/规范
- `fix`：修复问题
- `update`：更新内容
- `docs`：文档变更
- `refactor`：重构（无功能变化）
- `perf`：性能优化
- `chore`：维护性变更（脚本/CI/配置）

**示例：**
```
feat: 新增 zorro-ops 推文抓取 SOP

新增 Camofox 推文抓取入库全流程 SOP，
包含前置检查、执行步骤、质量自检。
```

---

## 协作协议

```
Robin（人类）
  ↓ 指令/任务
Luffy（架构师）
  ↓ 设计 SOP / 分配任务
Zorro-Ops / Zorro-Research / Zorro-Edu（执行者）
  ↓ 执行 / 记录
Luffy Knowledge Base（版本控制）
  ↓ 自动同步
GitHub（持久化备份）
```

- 所有规范变更 → Luffy 提交到本仓库
- 所有执行记录 → 写入 ops-log / tweet-discovery-log
- Luffy 周报 → 同步到本仓库

---

## 维护周期

| 周期 | 内容 | 时间 |
|------|------|------|
| 实时 | Skill 优化后立即提交 | — |
| 每日 | ops-log 同步到 teams/ | 20:00 |
| 每周 | Luffy 周报提交，wiki 整理 | 周一 |
| 有变更 | 规范/SOP 变更立即提交 | — |

---

## 联系方式

- **Owner**：Robin Z（@RobinZorro86）
- **Maintainer**：Luffy（AI Agent）
- **平台**：Telegram

---

*本仓库由 Luffy 自动维护，最后更新：2026-04-14*
