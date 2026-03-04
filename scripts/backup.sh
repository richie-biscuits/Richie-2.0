#!/bin/bash
# Richie 2.0 Backup Script
# Automatically backs up workspace to GitHub

set -e

REPO_DIR="/Users/openclaw_admin/.openclaw/workspace"
LOG_FILE="/Users/openclaw_admin/.openclaw/logs/backup.log"

# Create logs directory if needed
mkdir -p "$(dirname "$LOG_FILE")"

# Timestamp
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting Richie 2.0 backup..." >> "$LOG_FILE"

cd "$REPO_DIR"

# Check for changes
if git diff-index --quiet HEAD -- && [ -z "$(git status --porcelain)" ]; then
    echo "[$DATE] No changes to backup" >> "$LOG_FILE"
    exit 0
fi

# Stage all changes
git add -A

# Commit with timestamp
COMMIT_MSG="Auto-backup: $DATE

Changes detected in workspace:
$(git status --short | head -20)"

git commit -m "$COMMIT_MSG" --quiet || true

# Push to GitHub
if git push origin main --quiet; then
    echo "[$DATE] ✅ Backup successful" >> "$LOG_FILE"
else
    echo "[$DATE] ❌ Backup failed" >> "$LOG_FILE"
    exit 1
fi
