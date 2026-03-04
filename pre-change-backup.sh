#!/bin/bash
# pre-change-backup.sh - Backup workspace before risky operations
# Usage: ./pre-change-backup.sh "Description of what we're about to do"

cd /Users/openclaw_admin/.openclaw/workspace

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
MESSAGE="Pre-change backup: $1 [$TIMESTAMP]"

# Check if there are any changes (staged or unstaged)
if [[ -n $(git status --porcelain) ]]; then
    git add -A
    git commit -m "$MESSAGE"
    echo "✅ Pre-change backup committed: $MESSAGE"
else
    echo "ℹ️ No changes to backup"
fi
