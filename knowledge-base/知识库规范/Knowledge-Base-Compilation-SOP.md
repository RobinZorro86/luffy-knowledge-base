---
source: Luffy
title: "知识库定期编译方案"
date: 2026-04-21
type: sop
status: draft
---

# 知识库定期编译 SOP

> **版本**：v1.0 | **制定日期**：2026-04-21 | **维护者**：Luffy
> **背景**：2026-04-21全知识库扫描发现多层编译缺口，制定系统性预防方案

---

## 一、问题根因分析

### 今日发现的具体缺口

| 缺口类型 | 根因 | 后果 |
|---------|------|------|
| **Hermes Wiki 38个RAW零编译** | 一次性大量入库，无后续处理 | 知识无法导航，变成"死数据" |
| **Articles 3篇漏编** | 人工入库后依赖自觉，无触发机制 | 素材堆积变废弃 |
| **Summaries无统一导航** | 34篇摘要各自为政 | 无法快速检索 |
| **AI教育素材3天断层** | 编译依赖人工触发 | 最新素材与知识库脱节 |

### 根本原因

1. **无分层设计**：RAW → summaries → 索引 → 知识库 四层职责不清
2. **无编译触发机制**：依赖人工想起或出错后补救
3. **无负责人归属**：各目录不知谁负责编译
4. **无编译节奏标准**：不知道该多久编译一次
5. **无囤积检测**：RAW目录文件只增不减，无人清理

---

## 二、分层编译架构

### 四层职责

```
Layer 0: 原始入库（Raw Collection）
  └─ 来源：cron每日收集、人工入库、X抓取
  └─ 存储：~/wiki/raw/{domain}/
  └─ 负责人：各自的cron/子Agent

Layer 1: 素材库（Source Library）
  └─ 来源：RAW筛选后入库
  └─ 存储：~/wiki/{domain}/素材库/ 或 ~/wiki/summaries/
  └─ 负责人：各自的cron（已完成每日收集的，AI教育/Polymarket已自动）

Layer 2: 编译摘要（Compiled Abstracts）
  └─ 来源：Layer 1素材的深度编译
  └─ 存储：~/wiki/{domain}/教育资源/ 或 ~/wiki/summaries/
  └─ 触发：每周编译sweep

Layer 3: 知识库索引（Knowledge Index）
  └─ 来源：Layer 2 + 原始索引文件
  └─ 存储：各目录的index.md + ~/wiki/summaries/index.md
  └─ 触发：每月索引更新

Layer 4: 跨域综合（Cross-Domain Synthesis）
  └─ 来源：多目录知识整合
  └─ 存储：~/wiki/{主题}/wiki/
  └─ 触发：按需，不定期
```

### 各目录编译归属

| 目录 | Layer | 负责人 | 编译节奏 |
|------|-------|--------|---------|
| `research/AI教育/素材库/` | 1 | Zorro-Edu（cron每日收集） | 每日收集→每周编译摘要 |
| `summaries/` | 1→2 | Zorro-Research | 有新summaries时自然更新index |
| `raw/hermes-wiki/` | 0→2 | Zorro-Ops | **每周扫描一次**检查未编译文件 |
| `raw/articles/` | 0→2 | Zorro-Research | **每周扫描一次**检查未编译文件 |
| `raw/tweets/` | 1 | （已是摘要格式） | 无需编译，但需去重 |
| `twitter/weekly-ai-insights/` | 1 | Zorro-Research cron | 每周生成周报，已自动 |
| `投资/polymarket/` | 1→2 | Zorro-Research cron | 日报/周报已自动 |
| `zorro/knowledge/` | 2→3 | 各sub-agent | 按需 |
| `hermes/` | 2→3 | Zorro-Ops | 架构文档变动时更新 |

---

## 三、编译触发机制

### 每日自动（已有）

| Cron | 任务 | 产出 |
|------|------|------|
| AI儿童教育素材收集 | Zorro-Edu | `素材库/` 5个分类 |
| Polymarket日报 | Zorro-Research | pred101.com日报 |
| AI信源周报 | Zorro-Research | `twitter/weekly-ai-insights/WXX-weekly-report.md` |
| 每日推文自动入库 | Zorro-Research（v1.4） | `~/wiki/twitter/{author}/` |

**维护规则**：这些cron自带质量门禁，产出直接进Layer 1，无需额外触发。

---

### 3.2 每周编译 Sweep（新增核心机制）

**执行时间**：每周五 18:00 JST（或工作日最后一天）

**Cron Job ID**：`knowledge-compilation-weekly`

**扫描范围**：
```
~/wiki/raw/hermes-wiki/      — 检查未编译文件（>7天无动作）
~/wiki/raw/articles/         — 检查未编译文件（>7天无动作）
~/wiki/research/AI教育/素材库/ — 检查Layer 2编译断层（>7天）
~/wiki/summaries/             — 检查index.md更新（>7天无更新）
```

**囤积检测阈值**：
- RAW文件在目录中存在 >7天 → 触发编译
- Layer 1素材 >14天无Layer 2编译 → 触发编译
- 任意index.md >30天无更新 → 触发审查

**编译流程**：
```
1. 扫描四个目录
2. 识别囤积文件列表
3. 判断文件数量：
   - ≤3个文件 → 直接编译（单一子Agent）
   - 4-10个文件 → 委托子Agent编译
   - >10个文件 → 报告Robin，由Robin决定优先级
4. 执行编译
5. 更新对应index.md
6. 记录编译日志 → ~/wiki/hermes/teams/zorro-ops/knowledge-compilation-log.md
```

---

### 3.3 每月索引审查

**执行时间**：每月最后一个周五 18:00 JST

**任务**：
1. 扫描所有 `index.md` 文件
2. 检查交叉引用是否过期
3. 识别孤立文件（无任何文档引用）
4. 生成 `~/wiki/知识库健康报告-YYYY-MM.md`

---

## 四、编译标准

### 4.1 RAW → Layer 1（入库）

**判断标准**：
- 有实质内容（≥500字 or 有独特洞察）
- 非重复信息（去重检查）
- 来源可信

**Frontmatter必须字段**：
```yaml
source: 来源名称
url: 原文链接
date: YYYY-MM-DD
type: paper|article|report|course|tool|summary
tags: [标签1, 标签2]
status: raw|curated
```

---

### 4.2 Layer 1 → Layer 2（编译摘要）

**编译深度**：
| 内容类型 | 摘要长度 | 必须包含 |
|---------|---------|---------|
| 论文/报告 | 800-1500字 | 核心结论、数据来源、对Robin的实用价值 |
| 文章/博客 | 400-800字 | 核心观点、关键洞察、行动建议 |
| 课程案例 | 500-1000字 | 课程目标、适用年龄、关键资源链接 |
| 工具介绍 | 300-500字 | 功能描述、适用场景、使用限制 |

**交叉引用要求**：
- 必须关联已有Layer 2/Layer 3文档
- 标注补充/修正/扩展了哪些已有认知
- 高价值内容进入"核心文件速查"表

---

### 4.3 Layer 2+ → Layer 3（索引）

**Index.md必须包含**：
```yaml
---
source: compilation
date: YYYY-MM-DD  # 必须是最后更新时间
status: organized
---
```

**每条索引条目格式**：
```
### [文件名](相对路径)
日期：YYYY-MM-DD | 类型：xxx | 一句话描述
关联：→ 相关文档1 | → 相关文档2
```

---

## 五、囤积检测与上报

### 5.1 检测脚本

路径：`~/.hermes/scripts/knowledge-stale-check.sh`

```bash
#!/bin/bash
# 检查囤积文件，输出未编译文件列表
echo "=== RAW目录囤积检测 ==="
for dir in ~/wiki/raw/hermes-wiki ~/wiki/raw/articles; do
    echo "--- $dir ---"
    find "$dir" -name "*.md" -mtime +7 -printf "%f\n"
done
echo "=== 编译断层检测 ==="
# Layer 1 → Layer 2 断层检查（AI教育素材库）
find ~/wiki/research/AI教育/素材库/ -name "*.md" -mtime +14 | grep -v "index.md" | grep -v "教育资源/"
```

### 5.2 上报格式

当检测到囤积时，在cron执行结果中自动输出：

```
⚠️ 知识库囤积预警 — YYYY-MM-DD
检测时间：{timestamp}
囤积目录：
  - raw/hermes-wiki: N个文件（>7天未编译）
  - raw/articles: N个文件（>7天未编译）
  - 素材库: N个文件（>14天无编译摘要）
建议行动：[立即编译 / 周末处理 / Robin决策]
```

---

## 六、编译日志规范

路径：`~/wiki/hermes/teams/zorro-ops/knowledge-compilation-log.md`

格式：
```markdown
## YYYY-MM-DD 编译记录

### 执行者：Zorro-Ops / Zorro-Research
### 范围：每周Sweep

**处理文件：**
- `raw/hermes-wiki/xxx.md` → `hermes/xxx-index.md`
- `raw/articles/xxx.md` → `summaries/xxx-S00X.md`
- `research/AI教育/素材库/xxx.md` → `教育资源/08-xxx.md`

**产出文件：**
- index.md 更新：xxx, xxx

**遗留问题：**
- [未处理文件及原因]

**下次待办：**
- [如果有任何延迟任务]
```

---

## 七、变更记录

| 版本 | 日期 | 变更内容 |
|------|------|---------|
| v1.0 | 2026-04-21 | 初始版本，基于2026-04-21全知识库扫描结果制定 |

---

## 八、Robin确认决策（2026-04-21）

| 问题 | 决策 | 状态 |
|------|------|------|
| 每周编译Sweep cron | ✅ 已建立（job_id: 046a530046e0） | 每周五18:00 JST |
| 囤积阈值 | ✅ 确认：RAW >7天，Layer1 >14天 | 生效 |
| 超10个囤积文件时 | ✅ 自动处理，不上报Robin | 生效 |
| 每月索引审查cron | ✅ 独立cron（job_id: 821b9e0855cb） | 每月末周五18:00 JST |

