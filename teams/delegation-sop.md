# Luffy → Zorro 团队 任务下放 SOP

> 版本：v1.0 | 2026-04-14
> 目的：明确哪些任务交给 Zorro 执行，哪些 Luffy 保留

---

## Luffy 保留的任务（架构师职责）

| 任务类型 | 说明 | 理由 |
|---------|------|------|
| **Cron 管理** | 创建/修改/删除 cron | Cron 是系统骨架，架构师管理 |
| **SOP 设计** | 写/更新 操作规范文档 | 架构师核心输出 |
| **批判性评估** | 评估 Zorro 输出质量，决定是否交付 | 架构师把关 |
| **阻塞上报** | P0/P1 阻塞时上报 Robin | 分诊官职责 |
| **自我进化任务** | hermes-weekly-maintenance / luffy-biweekly-evolution | Luffy 专属 |
| **复杂新任务** | 从没处理过的任务类型 | 需要 Luffy 先判断怎么处理 |
| **Robin 专属指令** | "帮我做分析"/"给个建议" 类 | 需要 Luffy 自身判断 |
| **Luffy 周报** | 每周一 09:00 | Luffy 主动报告职责 |
| **任务看板维护** | 更新 luffy-task-board.md | 分诊官职责 |

---

## 交给 Zorro-Ops 的任务

### A. 标准化执行任务（已下放）

| 任务 | 触发方式 | cron/agent |
|------|---------|-----------|
| **Camofox 推文抓取入库** | Robin 发链接 + "入库" → Luffy 下放 | Zorro-Ops（按 SOP 执行） |
| **Wiki frontmatter 补全** | 积压或手动触发 | Zorro-Ops |
| **Wiki 质量门禁检查** | 每天 20:00 cron | ✅ 已下放 |
| **Zorro-Ops 每日系统自检** | 每天 09:00 cron | ✅ 已下放 |
| **Zorro-Edu 课程文件整理** | Zorro-Edu 产出内容后 | Zorro-Ops |

### B. 推文抓取 SOP

**SOP 文件**：`~/wiki/hermes/teams/zorro-ops/tweet-scraping-sop.md`

触发流程：
```
Robin 发链接 → Luffy 前置检查 → delegate_task 给 Zorro-Ops → Zorro-Ops 执行入库 → Telegram 结果报告
```

---

## 交给 Zorro-Research 的任务

| 任务 | 触发方式 | 状态 |
|------|---------|------|
| **每日全球热点新闻快报** | 每天 17:00 cron | ✅ 已下放 |
| **每日AI行业新闻快报** | 每天 17:00 cron | ✅ 已下放 |
| **推文发现推荐** | 每天 10:00/16:00 cron | ✅ 已下放 |

---

## 交给 Zorro-Edu 的任务

| 任务 | 触发方式 | 执行者 |
|------|---------|--------|
| **儿童 AI 课程内容编写** | Robin 下发 | Zorro-Edu |
| **课程进度追踪** | 每天自检时顺便检查 | Zorro-Edu |
| **教育资源整理** | 有新资源时 | Zorro-Edu |

---

## 任务下放检查清单

当 Luffy 收到一个新任务时，按以下顺序判断：

```
1. 这个任务是 P0 吗？
   → YES：Luffy 立即处理，不下放

2. 这个任务涉及创建新的 SOP 或修改系统架构吗？
   → YES：Luffy 处理，处理完将同类任务标准化后下放

3. 这个任务有明确的执行 SOP 吗？
   → YES：→ 第4步
   → NO：Luffy 先写 SOP，再下放

4. 这个任务属于 Zorro-Ops/Research/Edu 的职责范围吗？
   → YES：delegate_task 下放
   → NO：Luffy 处理

5. 这个任务需要 Luffy 自身判断（如分析、建议）吗？
   → YES：Luffy 处理
   → NO：→ 第4步
```

---

---

## 🔗 架构文档交叉引用

- **核心架构**：[../ARCHITECTURE-INDEX.md](../ARCHITECTURE-INDEX.md) — 38 个架构文档总索引
- [multi-agent-architecture](../raw/hermes-wiki/multi-agent-architecture.md) — Delegate Task 机制详解
- [parallel-tool-execution](../raw/hermes-wiki/parallel-tool-execution.md) — 并行执行与并发控制
- [toolsets-system](../raw/hermes-wiki/toolsets-system.md) — 工具集配置

## 变更记录

- v1.0 (2026-04-14): 初始版本，定义 Luffy 保留任务 / Zorro-Ops/Research/Edu 接管任务
