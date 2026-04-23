#!/bin/bash
# Daily Pipeline Review — delivered to Marrs via Telegram
# Runs: 8am weekdays AEST

REVIEW=$(cd ~/.config/richie-google && source venv/bin/activate && python3 ~/.openclaw/workspace/scripts/pipeline-review.py 2>&1)

# Send to Marrs via Telegram
curl -s -X POST "https://api.telegram.org/bot$(cat ~/.openclaw/openclaw.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('channels',{}).get('telegram',{}).get('token',''))")/sendMessage" \
  -d chat_id="1760063827" \
  -d text="$REVIEW" \
  -d parse_mode="Markdown" \
  -d disable_web_page_preview="true" 2>/dev/null

echo "Pipeline review sent"
