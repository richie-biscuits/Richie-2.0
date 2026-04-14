#!/usr/bin/env python3
"""
Fireflies Meeting Catalogue — hourly cron job
Checks for new meetings, stores metadata in Supabase notes, reports new ones.
"""
import json, urllib.request, os, sys
from datetime import datetime, timezone
from pathlib import Path

API_KEY = open(os.path.expanduser('~/.config/fireflies/config.json')).read().split('"api_key": "')[1].split('"')[0]
STATE_FILE = os.path.expanduser('~/.openclaw/logs/fireflies-meetings-state.json')
SUPABASE_URL = "https://cmqzawbdtnkynizughqq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNtcXphd2JkdG5reW5penVnaHFxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI2NzI1MTQsImV4cCI6MjA4ODI0ODUxNH0.Ha0-nnKHmCPBbfHYaebCcbjmeKZLrXYfGxTjuVlmLw8"

def gql_query(query_str, variables=None):
    query = json.dumps({'query': query_str, 'variables': variables or {}}).encode()
    req = urllib.request.Request(
        'https://api.fireflies.ai/graphql',
        data=query,
        headers={'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def get_recent_transcripts(limit=20):
    result = gql_query(
        'query($limit: Int) { transcripts(limit: $limit) { id title date duration } }',
        {'limit': limit}
    )
    return result['data']['transcripts']

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return set(json.load(f).get('seen_ids', []))
    return set()

def save_state(seen_ids):
    Path(STATE_FILE).parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, 'w') as f:
        json.dump({'seen_ids': list(seen_ids)}, f)

def get_transcript_summary(transcript_id):
    try:
        result = gql_query(
            '''query($id: String!) {
                transcript(id: $id) {
                    id title date duration
                    summary { overview action_items short_summary bullet_gist }
                    transcript_url
                }
            }''',
            {'id': transcript_id}
        )
        return result['data']['transcript']
    except Exception as e:
        return {'id': transcript_id, 'error': str(e)}

def store_in_supabase(meeting):
    """Store meeting as a note in Supabase."""
    data = json.dumps({
        'title': f"Fireflies: {meeting['title']}",
        'content': f"Duration: {meeting.get('duration',0):.0f}s\nURL: {meeting.get('transcript_url','N/A')}\n\nOverview:\n{meeting.get('summary',{}).get('overview','') or 'N/A'}",
    }).encode('utf-8')
    req = urllib.request.Request(
        f"{SUPABASE_URL}/rest/v1/notes",
        data=data,
        headers={
            'Content-Type': 'application/json',
            'apikey': SUPABASE_KEY,
            'Authorization': f'Bearer {SUPABASE_KEY}',
            'Prefer': 'return=minimal'
        },
        method='POST'
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status in (200, 201)
    except Exception:
        return False

def main():
    seen = load_state()
    transcripts = get_recent_transcripts(limit=20)
    new_ids = set()
    today_new = []
    
    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    
    for t in transcripts:
        tid = t['id']
        new_ids.add(tid)
        if tid not in seen:
            detail = get_transcript_summary(tid)
            detail['is_new'] = True
            dt = datetime.fromtimestamp(t['date']/1000, tz=timezone.utc)
            detail['date_dt'] = dt.isoformat()
            
            if dt >= today_start:
                today_new.append(detail)
    
    save_state(new_ids)
    
    if today_new:
        print(f"NEW MEETINGS TODAY: {len(today_new)}")
        for m in today_new:
            print(f"  - {m.get('title','No title')} | {m.get('date_dt','')[:16]}")
        send_telegram_alert(today_new)
    else:
        print("No new meetings today.")

def send_telegram_alert(meetings):
    bot_token = "8772606232:AAFXrpiqkhsKhtpHfaUWtarOzaQxR8ZH9mQ"
    chat_id = "1760063827"
    
    if len(meetings) == 1:
        m = meetings[0]
        overview = m.get('summary',{}).get('overview','') or ''
        msg = f"🗓️ *New Meeting: {m.get('title','No title')}*\n"
        msg += f"Time: {m.get('date_dt','')[:16]} UTC\n"
        if overview:
            msg += f"\n{overview[:200]}"
    else:
        msg = f"🗓️ *{len(meetings)} New Meetings Today:*\n"
        for m in meetings:
            msg += f"\n• {m.get('title','No title')} — {m.get('date_dt','')[:16]}"
    
    data = json.dumps({'chat_id': chat_id, 'text': msg, 'parse_mode': 'Markdown'}).encode()
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        data=data,
        headers={'Content-Type': 'application/json'}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            pass
    except Exception:
        pass

if __name__ == '__main__':
    main()
