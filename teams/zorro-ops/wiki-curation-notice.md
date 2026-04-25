# Wiki 入库质量规范 — 紧急更新通知

> **发布者**：Luffy（经 Robin 授权）  
> **发布时间**：2026-04-24 20:20 JST  
> **生效日期**：立即生效  
> **优先级**：🔴 高 — 必须立即执行

---

## 背景

2026-04-24 Cron 报警发现 8 个阻塞入库文件，根源是：
1. 入库执行者未遵循 frontmatter 规范
2. 验证脚本存在 bug（已修复）
3. 无明确的入库前自检流程

**Robin 明确指令**：入库规范必须严格执行，所有子 Agent 必须遵守。

---

## 新规范文件（必须阅读）

| 文件 | 路径 | 说明 |
|------|------|------|
| 主规范 | `~/wiki/hermes/knowledge/wiki-curation-standards.md` | 完整的入库质量规范 |
| Skill | `~/.hermes/skills/ops/wiki-curation/SKILL.md` | 简明 checklist |
| 验证脚本 | `~/.hermes/scripts/wiki-validate.py` | 自动检查工具 |

---

## 核心要求（必须遵守）

### 入库前自检（入库即执行）

入库任何文件前，逐项确认：

- [ ] **文件名**：`YYYY-MM-DD-{id或slug}.md`，以日期开头
- [ ] **Frontmatter 必填**：title, date, source, type, tags（≥3个）, status
- [ ] **tags 格式**：YAML list 格式（`- item`），**不是**逗号分隔字符串
- [ ] **引言块**：正文第一段是 `> 核心观点：...`
- [ ] **延伸参考**：正文末尾有 `## 延伸参考` + `[[wiki/...]]` 双链
- [ ] **status**：只能是 `curated` 或 `raw`
- [ ] **推文**：必须有 `url` 字段指向原始推文

### 任何入库操作后

- 立即运行：`python3 ~/.hermes/scripts/wiki-validate.py`
- 发现 ❌ 阻塞项 → **立即修复**，不等 cron
- 不要把问题留给每晚的自动报告

---

## 对 Zorro-Ops 的具体要求

### 验证脚本维护
- `wiki-validate.py` 今日已修复 2 个 bug：
  - YAML 多行列表（`- item`）解析
  - `key:` 空值解析
  - `REQUIRED_FRONTMATTER_TWITTER` 移除 category 必填
- 发现脚本 bug 必须立即修复，不能绕过
- 脚本更新后通知 Zorro-Research 和 Zorro-Edu

### Cron 报警处理
- 每日 20:00 报警中的 ❌ 阻塞项，必须**当日清零**
- 不能将问题留到第二天
- 当前已无阻塞项（10/10 通过）

---

## 对 Zorro-Research 的具体要求（已同步通知）

- 推文入库后立即自检，不依赖 cron 才发现问题
- 延伸参考必须关联已有 wiki 条目
- 自动入库的文件也必须符合本规范

---

## 对 Zorro-Edu 的具体要求（已同步通知）

- 儿童教育资源入库同样适用本规范
- 素材库路径：`~/wiki/research/AI教育/素材库/`

---

## 验证通过状态（截至 2026-04-24 20:16）

✅ 所有文件通过验证（10/10），汇总：**✅ 10 | ⚠️ 0 | ❌ 0**

---

## 规范变更记录

| 日期 | 版本 | 变更 |
|------|------|------|
| 2026-04-24 | v1.0 | 初始版本，建立完整入库规范体系 |

---

*本通知已同步到 Robin Z，等待确认。*
