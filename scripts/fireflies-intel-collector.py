#!/opt/homebrew/bin/python3
"""
Fireflies Intel Collector
Fetches recent meetings from Fireflies, extracts key intel, updates Richie's memory.
"""
import subprocess, json, os
from datetime import datetime, timezone

FIREFLIES_API_KEY = "77caf62a-9202-473c-afe4-8a4c02bcba9a"
FIREFLIES_ENDPOINT = "https://api.fireflies.ai/graphql"
MEMORY_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "memory")
PREV_TRANSCRIPT_FILE = os.path.join(MEMORY_DIR, ".last_transcripts.json")

def gql_query(query):
    payload = {"query": query}
    r = subprocess.run([
        "curl", "-s", "-X", "POST", FIREFLIES_ENDPOINT,
        "-H", f"Authorization: Bearer {FIREFLIES_API_KEY}",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(payload)
    ], capture_output=True, text=True, timeout=30)
    return json.loads(r.stdout)

def get_recent_transcripts(limit=20):
    q = ("{ transcripts(limit: %d) { "
         "id title date duration participants "
         "summary { overview short_summary bullet_gist } } }") % limit
    result = gql_query(q)
    return result.get("data", {}).get("transcripts", [])

def load_last_seen():
    if os.path.exists(PREV_TRANSCRIPT_FILE):
        with open(PREV_TRANSCRIPT_FILE) as f:
            d = json.load(f)
            return set(d.get("ids", []))
    return set()

def save_last_seen(ids):
    os.makedirs(os.path.dirname(PREV_TRANSCRIPT_FILE), exist_ok=True)
    with open(PREV_TRANSCRIPT_FILE, "w") as f:
        json.dump({"ids": list(ids)}, f)

def write_intel(meetings):
    """Write new intel to daily memory file."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    mem_file = os.path.join(MEMORY_DIR, f"{today}.md")
    os.makedirs(MEMORY_DIR, exist_ok=True)

    section = "\n---\n\n## Fireflies Intel — %s\n\n" % datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

    for t in meetings:
        ts = t.get("date", 0)
        try:
            dt = datetime.fromtimestamp(int(ts)/1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M")
        except:
            dt = str(ts)
        title = t.get("title", "Untitled")
        participants = t.get("participants", [])
        summary = t.get("summary") or {}
        overview = summary.get("overview", "") if summary else ""
        bullet_gist = summary.get("bullet_gist", "") if summary else ""

        section += "### Meeting: %s — %s\n" % (title, dt)
        section += "Participants: %s\n\n" % (', '.join(participants))
        if bullet_gist:
            section += "%s\n\n" % bullet_gist
        elif overview:
            section += "%s\n\n" % overview[:500]

    with open(mem_file, "a") as f:
        f.write(section)

    print("Wrote intel for %d new meetings." % len(meetings))

if __name__ == "__main__":
    transcripts = get_recent_transcripts(20)
    new_meetings = [t for t in transcripts if t["id"] not in load_last_seen()]
    all_ids = [t["id"] for t in transcripts]
    save_last_seen(all_ids)

    if not new_meetings:
        print("No new Fireflies meetings since last check.")
    else:
        write_intel(new_meetings)
        print("Written to: %s" % os.path.join(MEMORY_DIR, datetime.now(timezone.utc).strftime("%Y-%m-%d") + ".md"))
