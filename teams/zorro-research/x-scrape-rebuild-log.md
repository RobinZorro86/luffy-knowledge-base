# X 推文抓取系统重建记录

**日期：** 2026-04-17
**操作人：** Luffy
**触发：** Robin 报告"推文抓取又失败了"

---

## 根本原因

| 问题 | 原因 |
|------|------|
| AI信源周报从未执行 | cron 任务的 prompt 说"用批量下载脚本"，但脚本早就不工作 |
| Zorro-Research X 抓取失败 | 配置了 Camofox 但没告诉它用哪个工具 |
| `x_batch_scrape.py` 从第一天就坏了 | 硬编码假凭证（`AUTH_TOKEN="6f2142...65fa"`），curl 方式不可行 |
| Cookie 文件 auth_token 是占位符 | 昨天配置时只填了头尾，中间是假的 |

**核心问题：配置了工具 ≠ sub-agent 会自动用。必须显式指定。**

---

## 解决方案

### 1. Cookie 同步机制

**从 Camofox 容器内导出真实 cookie：**
```bash
docker exec camofox cat /home/camoufox/cookies.txt
```

**同步脚本（新建）：**
```bash
bash ~/.hermes/scripts/sync-x-cookies.sh
```

**同步内容：**
- Camofox 容器内有 `/home/camoufox/cookies.txt`（JSON 格式）
- 包含真实的 `auth_token: 27289755b6a269e5b4ae85395da1dba098251fa1`（40位）
- 同步到 `~/.local/share/baoyu-skills/x-to-markdown/cookies.json`

**⚠️ Camofox 重启后必须重新同步一次**

### 2. 可用工具链（2026-04-17 验证通过）

| 工具 | 用途 | 命令 |
|------|------|------|
| `x_scrape.py` | Camofox 单条抓取（首选） | `python3 ~/.hermes/scripts/x_scrape.py <URL>` |
| `x_batch_download.py` | 批量下载（baoyu + cookie） | `python3 ~/.hermes/scripts/x_batch_download.py <URL1> <URL2> ...` |
| `sync-x-cookies.sh` | Cookie 同步（重启后必跑） | `bash ~/.hermes/scripts/sync-x-cookies.sh` |

### 3. 重建的文件

- **删除** `x_batch_scrape.py`（完全无用）
- **更新** `x-scraping-decision-tree` skill — 反映真实工具状态
- **更新** `ai-insights-weekly-pipeline` skill — 更新抓取命令
- **更新** `zorro-research` skill — 简化 Camofox 抓取说明
- **更新** `zorro-ops` skill — X cookie 检查改用 sync-x-cookies.sh
- **新建** `sync-x-cookies.sh` — cookie 同步脚本
- **更新** AI信源周报 cron（`a4257e772302`）— 完整重建 prompt

---

## 验证结果（2026-04-17 11:10 JST）

```
✅ Camofox 健康：{"ok":true, "browserRunning":true}
✅ Cookie auth_token: 27289755b6...(40位有效)
✅ x_scrape.py karpathy推文: 2611 chars（完整内容）
✅ x_batch_download.py 测试: 1成功 0失败
```

---

## Cron 任务重建

**Job ID:** `a4257e772302`
**名称:** AI信源周报-抓取阶段
**时间:** 每周日 20:00 JST
**脚本:** sync-x-cookies.sh（执行前先同步 cookie）

**新 workflow：**
```
搜索推文 URL（Web搜索）
    ↓
Cookie 同步（如需要）
    ↓
Camofox x_scrape.py 单条抓取
或 x_batch_download.py 批量下载
    ↓
LLM 筛选（P1/P2/P3）
    ↓
输出周报到 ~/wiki/twitter/weekly-ai-insights/
```

---

## 待观察

1. AI信源周报 cron 实际执行情况（`last_run_at` 是否从 null 变为实际时间）
2. Cookie 有效期约30天，下次需在到期前重新同步
3. Zorro-Ops 每日自检（09:00）会检查 cookie 有效性
