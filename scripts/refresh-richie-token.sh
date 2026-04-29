#!/bin/bash
# Refresh richie@polynize.io Google OAuth tokens
# Called by cron every 55 minutes

cd ~/.config/richie-google && source venv/bin/activate && python3 -c "
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import json

with open('tokens.json') as f:
    data = json.load(f)

creds = Credentials.from_authorized_user_info(data, scopes=data.get('scopes', []))
if creds.expired:
    creds.refresh(Request())
    with open('tokens.json', 'w') as f:
        f.write(creds.to_json())
    print('REFRESHED')
else:
    print('OK')
" 2>&1
