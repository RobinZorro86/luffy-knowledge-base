# Zorro-Research 推文发现日志

## 2026-04-25 推文发现
扫描来源：行业文章提取推文URL + 预下载raw素材扫描
找到候选：3条
推荐入库：2条（评分≥4）
未入选原因：@not_racc 评分3.0（深度一般，短推为主，非直接实操内容）

### 入库详情
| # | 作者 | 主题 | 评分 | 文件路径 |
|---|------|------|------|----------|
| 1 | @Khazix0918 | 约束先行：Agent规则体系 | 4.9 | ~/wiki/twitter/Khazix0918/2026-04-25-2043886063106830741.md |
| 2 | @AlchainHust | 达尔文.skill：Skill进化系统 | 4.7 | ~/wiki/twitter/AlchainHust/2026-04-25-2043709317296361851.md |

### 扫描说明
- web_search 无法直接返回X推文（符合预期）
- 通过行业文章（博客园/CSDN）提取引用的推文URL
- 扫描 ~/wiki/twitter/weekly-ai-insights/raw/ 预下载素材
- Camofox 状态正常（9377端口），待后续直接抓取单条推文

## 2026-04-27 推文发现
扫描来源：weekly-ai-insights/raw/ 目录（预下载推文）
找到候选：11条
推荐入库：2条（自动）
未入选原因：大部分推文已入库；rauchg/zarazhangrui内容实操性偏弱；karpathy多个已入库

**入库详情：**
| # | 作者 | 主题 | 评分 | 时间 |
|---|------|------|------|------|
| 1 | @not_racc | AI取代不了的隐性知识（四大护城河） | 4.4 | 2026-04-17 |
| 2 | @karpathy | LLM知识库系统化工作流（详细thread） | 4.5 | 2026-04-02 |

**未入库说明：**
- @Khazix0918 约束先行：已于2026-04-25入库 ✅
- @AlchainHust 达尔文.skill：已于2026-04-25入库 ✅
- @karpathy 系统prompt学习/IDE notes/claude coding/autoresearch：均已入库 ✅
- @rauchg AI Cloud框架推演：实操性一般（仅3条推文，无实质方法）→ 3.2分
- @zarazhangrui Claude Skill做slides：工具介绍但缺具体实现细节 → 3.3分

## 2026-04-28 推文发现
扫描来源：weekly-ai-insights/raw/ 目录（预下载推文扫描）
找到候选：6条
入库：0条（已全部入库）
未入选原因：所有候选推文均已存在于 ~/wiki/twitter/{author}/ 目录中，无新推文需要入库

## 2026-04-29 推文发现
扫描来源：X搜索（行业媒体文章提推文URL） + 预下载素材扫描 + 目标账号排查
找到候选：5条
入库：2条（自动）
未入选原因：
  - @anchornode（Agent三次跃迁）：高分论点但属于高层次概述，实操性偏弱 → 3.4分不入库
  - 预下载 raw 目录推文：已全部入库（Khazix0918、alchainhust、karpathy等均已入库）
  - niceplugin/leopardracer：目录不存在或未收录

**入库详情：**
| # | 作者 | 主题 | 评分 | 时间 |
|---|------|------|------|------|
| 1 | @bozhou_ai | 上下文工程实战框架（Context Engineering五场景方案） | 4.3 | 2026-04-28 |
| 2 | @longdechen12 | Claude Code+Obsidian五步法，一个月涨粉1万 | 4.5 | 2026-04-28 |

**未入库说明：**
- @anchornode（Agent三次跃迁论）：3.4分 — 高层次概述，缺具体可执行内容
- @bozhou_ai：✅ 已入库（Context Engineering 工作台框架，有5种场景方案）
- @longdechen12：✅ 已入库（Claude Code+Obsidian 原创系统，5步骤+3指令+完整工作流）

## 2026-04-30 推文发现
扫描来源：X搜索 + 预下载素材扫描 + Camofox单条抓取验证 + 行业媒体搜索
找到候选：8条
入库：3条（自动）
未入选原因：
  - @zarazhangrui Claude Skill 做网页幻灯片：实用但与本周 AI Agent/知识管理主线相关性略低，留作周报素材 → 3.8分
  - @sama / @amasad 队列URL：Camofox 抓取返回空内容，跳过
  - 行业媒体结果：多为二次文章或泛化趋势，未发现可验证的高质量单条推文URL
  - 已入库重复：2040472969278042369、2039805659525644595、2027521323275325622 等已存在或已在周报收录

**入库详情：**
| # | 作者 | 主题 | 评分 | 时间 | 文件路径 |
|---|------|------|------|------|----------|
| 1 | @karpathy | Autoresearch：Agent 自主推进 LLM 训练实验 | 4.6 | 2026-03-07 | ~/wiki/twitter/karpathy/2026-03-07-2030371219518931079-autoresearch-agent-loop.md |
| 2 | @karpathy | System Prompt Learning：LLM 新学习范式 | 4.5 | 2025-05-11 | ~/wiki/twitter/karpathy/2025-05-11-1921368644069765486-system-prompt-learning.md |
| 3 | @karpathy | Idea File：Agent 时代的新交付物 | 4.4 | 2026-04-02 | ~/wiki/twitter/karpathy/2026-04-02-2040470801506541998-idea-file-agent-sharing.md |

**质量验证：**
- 3 个新入库文件均通过 `python3 ~/.hermes/scripts/wiki-validate.py`
- Camofox health 正常；已执行 cookie sync

## 2026-04-30 推文发现
扫描来源：X搜索 + 已下载 raw 候选 + 行业媒体
找到候选：16条 raw 推文候选；行业媒体搜索返回 Harness Engineering / Claude Code / Agent 趋势结果，未发现可直接入库的新单条推文 URL
入库：2条（自动）
未入选原因：多数 raw 候选已按 tweet_id 入库或只存在周报摘要；短推/趋势判断类内容深度不足；AI心理学候选已存在同 ID 完整入库版本。
验证：wiki-validate.py 对新增 2 个文件均显示 ✅ 通过；全局旧文件仍有历史警告但无阻塞项。
