# Luffy 任务看板

> 维护：Luffy
> 更新：每次任务状态变化时更新，每日 09:30 自动同步
> 路径：`~/wiki/hermes/teams/luffy-task-board.md`
> 版本：v1.1（新增：时间戳/来源/变更历史/自动更新）

---

## 当前周期：2026年4月14日这一周

---

## 🔴 P0（阻塞性）

| 任务 | 状态 | 负责人 | 来源 | 创建时间 | 最后更新 | 备注 |
|------|------|--------|------|---------|---------|------|
| — | — | — | — | — | — | 暂无 P0 阻塞 |

---

## 🟡 P1（当日必须）

| 任务 | 状态 | 上次成功 | 负责人 | 来源 | 完成标准 |
|------|------|---------|--------|------|---------|
| 每日推文发现（10:00） | ⚠️ 待验证 | — | Zorro-Research | cron | 发现 ≥1 条推荐入库 |
| 每日推文发现（16:00） | ⚠️ 待验证 | — | Zorro-Research | cron | 发现 ≥1 条推荐入库 |
| 每日新闻快报（17:00） | ⚠️ 待验证 | — | Zorro-Research | cron | 每板块 ≥2 条 |
| Wiki 质量门禁（20:00） | ⚠️ 待验证 | — | Zorro-Ops | cron | 脚本执行无错 |

---

## 🔵 P2（本周内）

| 任务 | 状态 | 负责人 | 来源 | 创建时间 | 截止 | 备注 |
|------|------|--------|------|---------|------|------|
| 知识库 frontmatter 补全（zorro/） | pending | Zorro-Ops | delegation-sop | 2026-04-14 | 2026-04-18 | 批量处理 |
| Zorro-Edu 主动课程规划 | pending | Zorro-Edu | Robin指令 | 2026-04-14 | 2026-04-20 | 等待细化需求 |

---

## ⚪ P3（有空再做）

| 任务 | 状态 | 来源 | 说明 |
|------|------|------|------|
| 研究 baoyu / Camofox 双工具协同 | pending | Luffy提议 | 探索性 |
| 尝试新的 Agent 架构 | pending | Luffy提议 | 探索性 |
| 非紧急 wiki 结构重组 | pending | Luffy提议 | 可延后 |

---

## ✅ 已完成（本周期）

| 任务 | 完成日期 | 结果 | 质量评级 |
|------|---------|------|---------|
| P0 每日系统自检 cron | 2026-04-14 | ✅ | pass |
| P0 ops-log.md 建立 | 2026-04-14 | ✅ | pass |
| P0 任务完成标准文档 | 2026-04-14 | ✅ | pass |
| P1 每日推文发现 cron | 2026-04-14 | ✅ | pass |
| P1 Wiki 入库质量门禁 | 2026-04-14 | ✅ | pass |
| P2 Luffy 角色升级文档 | 2026-04-14 | ✅ | pass |
| P2 Feature Flag 任务分级制度 | 2026-04-14 | ✅ | pass |
| P2 Luffy → Zorro 任务下放 SOP | 2026-04-14 | ✅ | pass |
| P2 Zorro-Ops 推文抓取 SOP | 2026-04-14 | ✅ | pass |

---

## 字段说明

| 字段 | 含义 | 更新规则 |
|------|------|---------|
| **状态** | pending / active / done / blocked / cancelled | 任务完成/取消时更新 |
| **上次成功** | YYYY-MM-DD HH:MM | cron任务执行成功后由执行者写入 ops-log.md，Luffy 每日汇总同步 |
| **来源** | cron / delegation-sop / Robin指令 / Luffy提议 | 任务进入看板时填写 |
| **创建时间** | YYYY-MM-DD | 任务进入看板时填写 |
| **最后更新** | YYYY-MM-DD HH:MM | 任何状态变化时更新 |
| **质量评级** | pass / warn / fail | 任务完成后按任务完成标准.md 评级 |

---

## 变更历史

| 时间 | 任务 | 变更内容 | 操作者 |
|------|------|---------|--------|
| 2026-04-14 | 初始化看板 | 初始化看板，创建周期 | Luffy |
| 2026-04-14 | luffy-task-board v1.1 | 新增字段（来源/时间戳/变更历史）| Luffy |

---

## 自动更新机制

### cron 任务状态同步

每日 09:30 Luffy 读取以下来源，自动更新看板：

```
1. Zorro-Ops ops-log.md → 更新 P1 cron 任务的"上次成功"时间戳
2. Zorro-Research tweet-discovery-log.md → 更新 P1 推文发现任务状态
3. hermes cron list → 确认 cron 数量是否与看板一致
```

### 跨周期切换规则

每周一 09:00（周报 cron 执行后）：

```
1. 将上周 P2 未完成且仍在有效的任务 → 移入本周 P2
2. 将上周 P2 已过时/取消的任务 → 归档（移到已完成或删除）
3. 重置看板周期标题
4. 变更历史截断（保留最近2周的记录）
```

### 看板维护 SOP

| 触发 | 操作 |
|------|------|
| 新任务下放时 | 在对应优先级列追加行，填写所有字段 |
| cron 任务执行成功后 | 执行者写入 ops-log.md，Luffy 每日汇总同步"上次成功" |
| cron 任务失败时 | 在备注标注 ❌ + 失败原因，下次数同步时更新 |
| 任务完成时 | 移到"已完成"，填写完成日期和质量评级 |
| P0 阻塞发生时 | 立即在 P0 列创建行，通知 Robin |

---

## 关联 SOP

- `task-prioritization.md` — 优先级判定
- `delegation-sop.md` — 任务下放流程
- `luffy-role.md` — Luffy 架构师职责
- `~/wiki/hermes/teams/zorro-ops/ops-log.md` — Zorro-Ops 执行日志（cron 状态来源）
- `~/wiki/hermes/teams/zorro-research/tweet-discovery-log.md` — Zorro-Research 日志（推文发现状态来源）

## Related

- [[hermes/index]] — Hermes 架构文档总索引
