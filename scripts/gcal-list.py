#!/usr/bin/env python3
"""List Google Calendar events for Richie workflows."""

from __future__ import annotations

import argparse
import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

TOKENS_FILE = os.path.expanduser("~/.config/richie-google/tokens.json")
TZ = ZoneInfo("Australia/Melbourne")


def calendar_service():
    creds = Credentials.from_authorized_user_file(TOKENS_FILE)
    return build("calendar", "v3", credentials=creds)


def fetch_events(start: datetime, end: datetime):
    svc = calendar_service()
    items = (
        svc.events()
        .list(
            calendarId="primary",
            timeMin=start.isoformat(),
            timeMax=end.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
        .get("items", [])
    )
    return items


def fmt_event(ev: dict) -> str:
    start_raw = ev.get("start", {}).get("dateTime") or ev.get("start", {}).get("date")
    end_raw = ev.get("end", {}).get("dateTime") or ev.get("end", {}).get("date")
    summary = ev.get("summary", "(No title)")

    if "T" in str(start_raw):
        s = datetime.fromisoformat(start_raw.replace("Z", "+00:00")).astimezone(TZ)
        e = datetime.fromisoformat(end_raw.replace("Z", "+00:00")).astimezone(TZ)
        return f"{s:%H:%M}-{e:%H:%M} {summary}"

    # all-day event
    return f"All day {summary}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--today", action="store_true", help="List events for today")
    parser.add_argument("--days", type=int, default=1, help="Days ahead from today")
    args = parser.parse_args()

    now = datetime.now(TZ)
    start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + timedelta(days=max(args.days, 1))

    events = fetch_events(start, end)
    if args.today:
        if not events:
            print("No events today.")
            return 0
        for ev in events:
            print(fmt_event(ev))
        return 0

    if not events:
        print("No events.")
        return 0

    for ev in events:
        print(fmt_event(ev))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
