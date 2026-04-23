#!/opt/homebrew/bin/python3
"""
Daily Pipeline Review — Richie
Pulls from: MEMORY.md, Google Calendar, Fireflies, email inbox
Generates a clean pipeline snapshot for Marrs
"""
import os, json, sys
from datetime import datetime, timezone, timedelta

WORKSPACE = os.path.expanduser("~/.openclaw/workspace")
MEMORY_FILE = os.path.join(WORKSPACE, "MEMORY.md")
CAL_TOKENS = os.path.expanduser("~/.config/richie-google/tokens.json")
FIREFLIES_KEY = "77caf62a-9202-473c-afe4-8a4c02bcba9a"

def get_calendar_events():
    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from googleapiclient.discovery import build
        creds = Credentials.from_authorized_user_file(CAL_TOKENS)
        if creds.expired:
            creds.refresh(Request())
        service = build('calendar', 'v3', credentials=creds)
        now = datetime.now(timezone(timedelta(hours=10)))
        today_start = now.strftime('%Y-%m-%dT00:00:00+10:00')
        today_end = now.strftime('%Y-%m-%dT23:59:59+10:00')
        events = service.events().list(
            calendarId='marrs@polynize.io', timeMin=today_start,
            maxResults=20, singleEvents=True, orderBy='startTime'
        ).execute()
        return events.get('items', [])
    except Exception as e:
        return []

def get_upcoming_events():
    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from googleapiclient.discovery import build
        creds = Credentials.from_authorized_user_file(CAL_TOKENS)
        if creds.expired:
            creds.refresh(Request())
        service = build('calendar', 'v3', credentials=creds)
        now = datetime.now(timezone(timedelta(hours=10)))
        tomorrow = now + timedelta(days=7)
        today_start = now.strftime('%Y-%m-%dT00:00:00+10:00')
        week_end = tomorrow.strftime('%Y-%m-%dT23:59:59+10:00')
        events = service.events().list(
            calendarId='marrs@polynize.io', timeMin=today_start, timeMax=week_end,
            maxResults=30, singleEvents=True, orderBy='startTime'
        ).execute()
        return events.get('items', [])
    except:
        return []

def generate_review():
    now = datetime.now(timezone(timedelta(hours=10)))
    date_str = now.strftime("%a %b %d")
    
    today_events = get_calendar_events()
    week_events = get_upcoming_events()
    
    review = f"📋 **Pipeline Review — {date_str}**\n\n"
    
    # Today's calendar
    review += f"**Today ({date_str})**\n"
    if today_events:
        for ev in today_events:
            start = ev.get('start',{}).get('dateTime','')
            time_str = start[11:16] if 'T' in start else ''
            review += f"  • {time_str} — {ev.get('summary','No title')}\n"
    else:
        review += "  • No events\n"
    
    # This week
    review += "\n**This Week**\n"
    if week_events:
        for ev in week_events[1:8]:
            start = ev.get('start',{}).get('dateTime','')
            date_str_ev = start[5:10] if 'T' in start else ''
            time_str = start[11:16] if 'T' in start else ''
            if date_str_ev:
                review += f"  • {date_str_ev} {time_str} — {ev.get('summary','No title')}\n"
    else:
        review += "  • No events\n"
    
    # Pipeline from MEMORY
    review += "\n**Pipeline**\n"
    try:
        with open(MEMORY_FILE) as f:
            memory = f.read()
        deals = []
        in_section = False
        for line in memory.split('\n'):
            if '## Active Deals' in line:
                in_section = True
                continue
            if in_section:
                if line.startswith('## ') or line.startswith('# '):
                    break
                if line.strip():
                    deals.append(line)
        if deals:
            for d in deals[:25]:
                review += d + "\n"
        else:
            review += "  (see MEMORY.md)\n"
    except Exception as e:
        review += f"  (MEMORY error)\n"
    
    return review

if __name__ == "__main__":
    print(generate_review())
