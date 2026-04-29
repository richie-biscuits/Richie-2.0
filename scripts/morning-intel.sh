#!/bin/bash
# Morning Intel — gathers calendar events, Fireflies transcripts, and email
# Called by the Morning Intel cron job
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
import json
from google.auth.transport.requests import Request

with open('tokens.json') as f:
    data = json.load(f)
creds = Credentials.from_authorized_user_info(data, scopes=data.get('scopes', []))
if creds.expired:
    creds.refresh(Request())
    with open('tokens.json', 'w') as f:
        f.write(creds.to_json())

service = build('gmail', 'v1', credentials=creds)
results = service.users().messages().list(userId='me', q='is:unread newer_than:2d').execute()
messages = results.get('messages', [])
print(f'UNREAD:{len(messages)}')
for msg in (messages or [])[:15]:
    meta = service.users().messages().get(userId='me', id=msg['id'], format='metadata', metadataHeaders=['From','Subject','Date']).execute()
    headers = {h['name']: h['value'] for h in meta['payload']['headers']}
    print(f\"{headers.get('Date','')[:25]}|{headers.get('From','')[:50]}|{headers.get('Subject','')[:100]}\")
"
