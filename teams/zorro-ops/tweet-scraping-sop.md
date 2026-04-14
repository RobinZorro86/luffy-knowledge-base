# Zorro-Ops 推文抓注入库 SOP

> 版本：v1.0 | 2026-04-14
> 执行者：Zorro-Ops
> 触发：Robin 发链接 + "入库/学习" → Luffy 下放给 Zorro-Ops

---

## 触发条件

Robin 发了 X/Twitter 推文链接，并标注"入库/学习/整理" → Luffy 判断合规后 → delegate_task 给 Zorro-Ops

---

## 前置检查（Luffy 做）

| 检查项 | 标准 |
|--------|------|
| URL 有效 | 域名是 x.com 或 twitter.com |
| 不是已入库 | 检查 ~/wiki/twitter/ 下没有同作者+同日期的文件 |
| 格式合规 | 链接是单条推文或 thread |

Luffy 检查通过后，附上：
- 目标作者名（如"宝玉"）
- 入库路径（如 `~/wiki/twitter/宝玉/`）
- 是否有特殊处理要求

---

## Zorro-Ops 执行步骤

### Step 1：抓取推文

使用 Camofox（端口 9377）抓取：

```bash
# 1. 确认 Camofox 可用
curl -s http://localhost:9377/tabs

# 2. 创建 session 并加载 cookies
# cookies 路径：/home/um870/x_cookies.txt（Playwright格式）

# 3. 导航到推文页面
# URL 去掉查询参数，只保留 /status/ID

# 4. 等待 article 元素出现（最多等待15秒）

# 5. 提取内容：
# - 发推时间：time@datetime
# - 作者：data-testid="User-Name"
# - 正文：article 下的所有文本
```

详细抓取流程参考：
- `~/wiki/知识库规范/推文入库标准.md`

### Step 2：内容整理

按 `推文入库标准.md` 整理：

1. **Frontmatter**（必须5字段）：
   ```yaml
   ---
   title: "推文标题或概括"
   author: "作者名 (@username)"
   date: YYYY-MM-DD（发推日期）
   source: https://x.com/xxx/status/XXXXXXXX
   category: AI-Agent-Practices（按内容选分类）
   tags: [tag1, tag2, tag3]（≥3个）
   status: curated
   ---
   ```

2. **正文结构**：
   - `> 核心观点` 引言块
   - 推文正文（按原结构整理）
   - 长推文/thread 按序号分段
   - 末尾 `## 延伸参考` 关联已有 wiki

3. **文件名**：
   - `{年份}-{关键词}.md`
   - 如：`2026-AI-First战略可能大错特错.md`

### Step 3：质量自检

入库前自检清单：

- [ ] frontmatter 5字段齐全
- [ ] tags ≥ 3个
- [ ] 正文有 `> 核心观点` 引言块
- [ ] 正文 ≥ 200字
- [ ] 末尾有 `## 延伸参考`
- [ ] 文件命名符合规范
- [ ] 推文 URL 可访问

### Step 4：写入文件

- 路径：`~/wiki/twitter/{作者名}/{年份}-{关键词}.md`
- 作者名目录不存在时创建

### Step 5：结果报告

执行完成后，在 Telegram 发送：

```
✅ 推文入库完成

**作者**：@username
**标题**：...
**路径**：~/wiki/twitter/作者/文件名.md
**字数**：XXX字
**标签**：tag1 / tag2 / tag3

质量自检：5/5 通过
```

### 失败处理

| 失败情况 | 处理方式 |
|---------|---------|
| Camofox 连接失败 | 标记 `❌ Camofox 不可用`，通知 Luffy |
| 推文被删除/不可见 | 通知 Luffy，说明情况 |
| 抓取内容过短（<50字） | 通知 Luffy，确认是否继续 |
| 磁盘空间不足 | 立即通知 Luffy（P0） |

---

## 操作记录

每次执行后，写入 ops-log：

```markdown
## YYYY-MM-DD HH:MM — 推文入库：@username

**任务**：https://x.com/xxx/status/XXXXXXXX
**结果**：✅ 成功 / ❌ 失败
**详情**：文件路径、字数、标签数量
**失败原因**：（如有）
```

---

## 关联 SOP

- `~/wiki/知识库规范/推文入库标准.md` — 入库格式规范
- `~/wiki/hermes/teams/delegation-sop.md` — Luffy → Zorro 任务下放流程
