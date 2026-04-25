#!/usr/bin/env python3
"""
Wiki 入库验证脚本
检查推文入库文件是否符合质量标准
"""
import os, sys, json, re, glob
from pathlib import Path
from datetime import datetime, timedelta

WIKI_ROOT = Path.home() / "wiki"
REPORT = []  # [(file, status, issues)]

REQUIRED_FRONTMATTER_BASE = ["title", "date", "source", "tags", "status"]
REQUIRED_FRONTMATTER_TWITTER = []  # category 已废除，type=tweet 已足够标识
REQUIRED_FRONTMATTER_ARTICLE = ["type"]       # article 类文件需要 type
REQUIRED_TAGS_MIN = 3

def check_file(path):
    """检查单个文件，返回 (file, status, issues)"""
    issues = []
    status = "pass"
    
    with open(path, encoding="utf-8") as f:
        content = f.read()
    
    # 1. Frontmatter 检查
    if not content.startswith("---"):
        issues.append("❌ 缺 frontmatter 头（未以 --- 开头）")
        status = "fail"
        return path.name, status, issues
    
    fm_end = content.find("\n---", 3)
    if fm_end == -1:
        issues.append("❌ frontmatter 格式错误（缺少结束 ---）")
        status = "fail"
        return path.name, status, issues
    
    fm_text = content[3:fm_end].strip()
    
    # 解析 frontmatter（支持YAML多行列表格式）
    fm = {}
    current_key = None
    in_list = False
    for line in fm_text.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        
        # 检测 list item（YAML多行格式）
        if stripped.startswith("- ") and current_key:
            val = stripped[2:].strip().strip('"').strip("'")
            if current_key not in fm:
                fm[current_key] = []
            if isinstance(fm[current_key], list):
                fm[current_key].append(val)
            in_list = True
        elif ": " in stripped or stripped.endswith(":"):
            # Handle both "key: value" and "key:" (with or without space before colon)
            if ": " in stripped:
                key, val = stripped.split(": ", 1)
            else:
                key = stripped.rstrip(":")
                val = ""
            current_key = key.strip().strip("-").strip('"').strip("'")
            val = val.strip().strip('"').strip("'")
            if val:  # key: value 格式
                fm[current_key] = val
            else:  # key: （后面是list）
                fm[current_key] = []
            in_list = False
        elif stripped == "---" and current_key == "":  # end of frontmatter marker
            break
    
    # 识别文件类型（基于 frontmatter 的 type 字段）
    is_twitter = fm.get("type") == "tweet"
    is_article = fm.get("type") in ("article", "long-article")

    # 根据文件类型确定必填字段
    # category 只在 type=tweet 且没有 type:long-article 时需要
    required_fields = list(REQUIRED_FRONTMATTER_BASE)
    if is_twitter and not is_article:
        # twitter 类型文件：type=tweet 时 category 可选（已有 type 标识）
        pass
    if is_twitter:
        required_fields.extend(REQUIRED_FRONTMATTER_TWITTER)
    if is_article:
        required_fields.extend(REQUIRED_FRONTMATTER_ARTICLE)

    # 检查必填字段
    for field in required_fields:
        if field not in fm:
            issues.append(f"❌ 缺字段：{field}")
            status = "fail"
        elif field == "tags" and isinstance(fm[field], list):
            if len(fm[field]) < REQUIRED_TAGS_MIN:
                issues.append(f"⚠️ tags 数量不足（{len(fm[field])} < {REQUIRED_TAGS_MIN}）")
                if status != "fail":
                    status = "warn"
        elif field == "tags" and isinstance(fm[field], str):
            # tags可能是逗号分隔的字符串
            tag_count = len([t for t in fm[field].split(",") if t.strip()])
            if tag_count < REQUIRED_TAGS_MIN:
                issues.append(f"⚠️ tags 数量不足（{tag_count} < {REQUIRED_TAGS_MIN}）")
                if status != "fail":
                    status = "warn"
        elif field == "status" and fm[field] not in ["curated", "raw"]:
            issues.append(f"⚠️ status 值异常：{fm[field]}（应为 curated 或 raw）")
            if status != "fail":
                status = "warn"
    
    # 2. 正文引言块检查（兼容"核心观点"和"主题"两种格式）
    has_quote = "> " in content
    has_keyword = "核心观点" in content or "主题：" in content
    if not has_quote or not has_keyword:
        issues.append("⚠️ 缺『> 核心观点』或『> 主题：』引言块")
        if status == "pass":
            status = "warn"
    
    # 3. 延伸参考检查（兼容延伸阅读/相关笔记等表述）
    has_extended = any(kw in content for kw in ["## 延伸参考", "## 相关笔记", "## 延伸阅读", "## 相关资源"])
    if not has_extended:
        issues.append("⚠️ 缺『## 延伸参考』或『## 相关笔记』章节")
        if status == "pass":
            status = "warn"
    
    # 4. 正文长度检查
    body = content[fm_end+4:].strip()
    char_count = len(body)
    if char_count < 200:
        issues.append(f"⚠️ 正文过短（{char_count} < 200 字）")
        if status == "pass":
            status = "warn"
    
    # 5. 文件名检查
    filename = path.name
    if not re.match(r"\d{4}-", filename):
        issues.append(f"⚠️ 文件名不符合规范（应以年份开头，如 2026-）")
        if status == "pass":
            status = "warn"
    
    return path.name, status, issues

def main():
    today = datetime.now()
    
    # 只检查最近2天修改的 twitter/ 文件
    twitter_dir = WIKI_ROOT / "twitter"
    if not twitter_dir.exists():
        print("❌ twitter/ 目录不存在")
        sys.exit(0)
    
    report_lines = [
        f"## 📋 入库质量验证报告 — {today.strftime('%Y-%m-%d %H:%M')}",
        "",
    ]
    
    pass_count = 0
    warn_count = 0
    fail_count = 0
    
    files_checked = []
    
    for subdir in twitter_dir.iterdir():
        if not subdir.is_dir():
            continue
        for md in subdir.glob("*.md"):
            mtime = datetime.fromtimestamp(md.stat().st_mtime)
            if (today - mtime) <= timedelta(days=2):
                files_checked.append(md)
    
    if not files_checked:
        report_lines.append("✅ 近2天无新增入库文件，跳过检查")
    else:
        for path in sorted(files_checked):
            name, status, issues = check_file(path)
            rel = path.relative_to(WIKI_ROOT)
            if status == "pass":
                pass_count += 1
                report_lines.append(f"✅ `{rel}` — 通过")
            elif status == "warn":
                warn_count += 1
                report_lines.append(f"⚠️ `{rel}` — 警告")
                for issue in issues:
                    report_lines.append(f"   {issue}")
            else:
                fail_count += 1
                report_lines.append(f"❌ `{rel}` — 不通过")
                for issue in issues:
                    report_lines.append(f"   {issue}")
        
        report_lines.append("")
        report_lines.append("---")
        report_lines.append(f"**汇总**：✅ {pass_count} | ⚠️ {warn_count} | ❌ {fail_count}")
    
    report = "\n".join(report_lines)
    print(report)
    
    # 写入 ops-log
    ops_log = WIKI_ROOT / "hermes/teams/zorro-ops/ops-log.md"
    if ops_log.exists():
        with open(ops_log, encoding="utf-8") as f:
            existing = f.read()
        new_content = report + "\n\n" + existing
        with open(ops_log, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"\n已追加到 ops-log")
    
    # 退出码：有问题返回1
    sys.exit(1 if (fail_count > 0) else 0)

if __name__ == "__main__":
    main()
