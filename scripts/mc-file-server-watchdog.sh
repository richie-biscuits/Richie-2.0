#!/bin/bash
# watchdog for mc-file-server — restart if not running
while true; do
    if ! lsof -ti :5001 >/dev/null 2>&1; then
        /opt/homebrew/bin/python3 -c "exec(open('/Users/openclaw_admin/.openclaw/workspace/scripts/mc-file-server.py').read())" &
        sleep 2
    fi
    sleep 30
done
