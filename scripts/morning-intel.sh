#!/bin/bash
# Morning Intel — gathers calendar events, Fireflies transcripts, and all configured email accounts
# Called by the Morning Intel cron job (7:45am weekdays)
# Outputs: structured data for Richie to build the briefing

echo "=== CALENDAR ==="
cd ~/.config/richie-google && source venv/bin/activate && python3 -c "
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import json
from datetime import datetime, timedelta, timezone

with open('tokens.json') as f:
    data = json.load(f)
creds = Credentials.from_authorized_user_info(data, scopes=data.get('scopes', []))
from google.auth.transport.requests import Request
if creds.expired:
    creds.refresh(Request())
    with open('tokens.json', 'w') as f:
        f.write(creds.to_json())

today = datetime.now(timezone.utc).strftime('%Y-%m-%dT00:00:00+10:00')
week_end = (datetime.now(timezone.utc) + timedelta(days=7)).strftime('%Y-%m-%dT00:00:00+10:00')

service = build('calendar', 'v3', credentials=creds)
events = service.events().list(
    calendarId='marrs@polynize.io',
    maxResults=50,
    timeMin=today,
    timeMax=week_end,
    singleEvents=True,
    orderBy='startTime'
).execute()
for e in events.get('items', []):
    start = e['start'].get('dateTime', e['start'].get('date'))
    end = e['end'].get('dateTime', e['end'].get('date'))
    print(f\"{start[:16]}|{end[:16]}|{e.get('summary', 'No title')}\")
print(f'TOTAL:{len(events.get(\"items\", []))}')
"

echo ""
echo "=== FIREFLIES ==="
python3 /Users/openclaw_admin/.openclaw/workspace/scripts/fireflies-intel-collector.py 2>&1 | tail -20

echo ""
echo "=== EMAIL ==="
cd ~/.config/richie-google && source venv/bin/activate && python3 -c "
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import json, os, re, glob
from google.auth.transport.requests import Request

TOKEN_DIR = os.path.expanduser('~/.config/richie-google')

def check_account(email):
    slug = re.sub(r'[^a-z0-9]', '-', email.lower())
    token_file = os.path.join(TOKEN_DIR, f'tokens-{slug}.json')
    if not os.path.exists(token_file):
        return
    
    with open(token_file) as f:
        data = json.load(f)
    creds = Credentials.from_authorized_user_info(data, scopes=data.get('scopes', []))
    if creds.expired:
        try:
            creds.refresh(Request())
            with open(token_file, 'w') as f:
                f.write(creds.to_json())
        except:
            pass
    
    service = build('gmail', 'v1', credentials=creds)
    # Check recent unread and also just recent inbox for context
    for label, query in [('UNREAD', 'is:unread newer_than:2d'), ('RECENT_INBOX', 'newer_than:1d')]:
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])
        print(f'{label}({email}):{len(messages)}')
        for msg in (messages or [])[:10]:
            meta = service.users().messages().get(userId='me', id=msg['id'], format='metadata', metadataHeaders=['From','Subject','Date']).execute()
            headers = {h['name']: h['value'] for h in meta['payload']['headers']}
            print(f\"{headers.get('Date','')[:25]}|{headers.get('From','')[:50]}|{headers.get('Subject','')[:100]}\")

# Check all configured accounts
check_account('richie@polynize.io')
check_account('marrs@polynize.io')
"
