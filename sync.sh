#!/bin/bash
# Luffy 知识库自动同步脚本
# 路径：~/luffy-knowledge-base/sync.sh
# 用法：bash ~/luffy-knowledge-base/sync.sh
# 建议：每天 20:00 cron 自动运行

set -e

SRC_WIKI="$HOME/wiki"
SRC_SKILLS="$HOME/.hermes/skills"
DEST="$HOME/luffy-knowledge-base"

echo "=== Luffy 知识库同步 — $(date '+%Y-%m-%d %H:%M') ==="

# 1. 同步 teams/
echo "[1/5] 同步 teams/..."
cp -r "$SRC_WIKI/hermes/teams/"* "$DEST/teams/" 2>/dev/null || true

# 2. 同步知识库规范/
echo "[2/5] 同步 knowledge-base/..."
mkdir -p "$DEST/knowledge-base"
cp -r "$SRC_WIKI/知识库规范/" "$DEST/knowledge-base/" 2>/dev/null || true

# 3. 同步 skills（优化后版本）
echo "[3/5] 同步 skills/..."
for skill in zorro-ops zorro-research zorro-edu; do
    if [ -f "$SRC_SKILLS/$skill/SKILL.md" ]; then
        mkdir -p "$DEST/skills/$skill"
        cp "$SRC_SKILLS/$skill/SKILL.md" "$DEST/skills/$skill/"
        echo "  ✓ $skill/SKILL.md"
    fi
done

# 4. 同步 scripts/
echo "[4/5] 同步 scripts/..."
if [ -f "$HOME/.hermes/scripts/wiki-validate.py" ]; then
    cp "$HOME/.hermes/scripts/wiki-validate.py" "$DEST/scripts/"
    echo "  ✓ wiki-validate.py"
fi

# 5. Git 提交 + 推送
echo "[5/5] Git 提交..."
cd "$DEST"
git add -A

if git diff --cached --quiet; then
    echo "✅ 无变更，跳过"
else
    COMMIT_MSG="sync: $(date '+%Y-%m-%d %H:%M') — 自动同步"
    git commit -m "$COMMIT_MSG"
    git push
    echo "✅ 已推送：$COMMIT_MSG"
fi

echo "=== 同步完成 ==="
