# CHANGELOG — Luffy Knowledge Base

所有变更按日期倒序记录。格式遵循 [Keep a Changelog](https://keepachangelog.com/) 标准。

---

## [Unreleased]

### Added

- `CONTRIBUTING.md` — 完整的贡献规范：commit格式/SOP编写/Skill编写/冲突处理

### Changed

- `README.md` — 完整规范化：架构图/同步机制/文档索引/关联系统

---

## [1.0.0] — 2026-04-14

> 初始化仓库 — 完整重构 Luffy 知识管理体系

### Added

#### 团队规范（teams/）

| 文件 | 版本 | 说明 |
|------|------|------|
| `luffy-role.md` | v1.1 | Luffy 角色升级：架构师 + 分诊官，新增主动周报 + 批判性评估 + SOP设计职责 |
| `luffy-task-board.md` | v1.1 | 任务看板 v1.1：新增来源/时间戳/变更历史/自动更新机制 |
| `task-prioritization.md` | v1.0 | 任务分级制度：P0/P1/P2/P3 + 状态定义 + 阻塞上报 + Feature Flag思维 |
| `delegation-sop.md` | v1.0 | Luffy → Zorro 任务下放 SOP：保留任务 vs 下放任务清单 + 检查清单 |
| `zorro-ops/ops-log.md` | — | Zorro-Ops 执行日志 |
| `zorro-ops/tweet-scraping-sop.md` | v1.0 | 推文抓注入库 SOP：Camofox 抓取 → 整理 → 自检 → 入库全流程 |
| `zorro-research/tweet-discovery-log.md` | — | Zorro-Research 推文发现日志 |

#### 知识库规范（knowledge-base/）

| 文件 | 说明 |
|------|------|
| `知识库规范/任务完成标准.md` | 4类任务完成标准：新闻/推文入库/知识库/系统监控 + 质量评级 |
| `知识库规范/推文入库标准.md` | 推文入库格式规范：frontmatter 5字段 + 正文结构 |

#### Skills（skills/）

| Skill | 版本 | 主要内容 |
|-------|------|---------|
| `zorro-ops/SKILL.md` | v1.1 | 新增每日系统自检 + eBay凭证验证 + GitHub认证检查 + 完整边界处理矩阵 |
| `zorro-research/SKILL.md` | v1.1 | 新增日报缺口机读追踪 + KOL边界处理 + 内容产出量化标准 + 质量门禁 |
| `zorro-edu/SKILL.md` | — | 儿童AI教育课程研发Agent |

#### 脚本（scripts/）

| 脚本 | 说明 |
|------|------|
| `wiki-validate.py` | 入库质量验证脚本：检查 frontmatter 5字段 + tags≥3 + 引言块 + 延伸参考 |

#### 仓库管理

| 文件 | 说明 |
|------|------|
| `SELF-MANAGE-SOP.md` | Luffy 自管理 SOP：同步规则 + 冲突处理 + 维护周期 |
| `sync.sh` | 自动同步脚本：源文件 → 镜像 → GitHub push |
| `.gitignore` | Git 忽略规则 |

### Changed

#### 架构升级

- **Luffy 角色定位**：从执行者（v1.0）升级为架构师 + 分诊官（v1.1）
- **任务分配模式**：执行类任务全部下放 Zorro，Luffy 专注架构设计 + 质量把关
- **知识管理体系**：从本地散文件 → GitHub 版本控制 + 自动同步

#### Cron 任务体系

| 任务 | 原状态 | 现状态 |
|------|--------|--------|
| Zorro-Ops 每日系统自检 | 无 | ✅ 新建（每天 09:00）|
| Zorro-Research 推文发现 | 无 | ✅ 新建（每天 10:00 + 16:00）|
| 每日全球热点新闻快报 | 无 | ✅ 新建（每天 17:00）|
| 每日AI行业新闻快报 | 无 | ✅ 新建（每天 17:00）|
| Wiki 入库质量门禁 | 无 | ✅ 新建（每天 20:00）|
| Luffy 每日知识库同步 | 无 | ✅ 新建（每天 20:00）|
| Luffy 周报 | 无 | ✅ 新建（每周一 09:00）|

---

## [0.1.0] — 2026-04-14

> pre-initialization — 迁移前状态

### Historical Context

在此版本之前，Luffy 知识管理状态：
- Wiki 散落在 `~/wiki/`，无版本控制
- Skills 分散在 `~/.hermes/skills/` 和 `~/.claude/skills/`
- 无 SOP、无任务分级、无执行日志
- Zorro Agent 刚完成迁移，架构待完善

本次初始化将所有历史沉淀重组为版本化知识库。

---

## 版本命名规则

```
[MAJOR.MINOR.PATCH]

MAJOR：架构性重构（如角色定位根本改变）
MINOR：新增重要模块（SOP/Skill/工具链）
PATCH：日常维护（文档修正/小优化）
```

---

## 变更类型说明

| 类型 | 含义 |
|------|------|
| `Added` | 新增内容 |
| `Changed` | 已有内容的修改 |
| `Deprecated` | 已废弃（未来会删除）|
| `Removed` | 已删除内容 |
| `Fixed` | 修复的问题 |
| `Security` | 安全相关变更 |

---

## 提交格式规范

本仓库提交信息遵循 [Conventional Commits](https://www.conventionalcommits.org/)：

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Type：** `feat` / `fix` / `docs` / `style` / `refactor` / `perf` / `chore` / `test`

**示例：**
```
feat(teams): 新增 zorro-ops 推文抓取 SOP

- Camofox 抓取 → 整理 → 自检 → 入库全流程
- 包含边界处理矩阵
```

---

*CHANGELOG 由 Luffy 自动维护*
*格式参考：Keep a Changelog + Conventional Commits*
