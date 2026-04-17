#!/opt/homebrew/bin/python3
"""
Fireflies Intel Collector
Fetches recent meetings from Fireflies, extracts key intel, updates Richie's memory.
"""
import subprocess, json, os
from datetime import datetime, timezone

FIREFLIES_API_KEY = "77caf62a-9202-473c-afe4-8a4c02bcba9a"
FIREFLIES_ENDPOINT = "https://api.fireflies.ai/graphql"
MEMORY_DIR = os.path.expanduser("~/.openclaw/workspace/memory")
PREV_TRANSCRIPT_FILE = os.path.expanduser("~/.openclaw/workspace/memory/.last_transcripts.json")

def gql_query(query, variables=None):
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    r = subprocess.run([
        "curl", "-s", "-X", "POST", FIREFLIES_ENDPOINT,
        "-H", f"Authorization: Bearer {FIREFLIES_API_KEY}",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(payload)
    ], capture_output=True, text=True, timeout=15)
    return json.loads(r.stdout)

def get_recent_transcripts(limit=20):
    q = "{ transcripts(limit: $limit) { id title date duration participants summary { overview short_summary bullet_gist } } }"
    result = gql_query(q, {"limit": limit})
    return result.get("data", {}).get("transcripts", [])

def load_last_seen():
    if os.path.exists(PREV_TRANSCRIPT_FILE):
        with open(PREV_TRANSCRIPT_FILE) as f:
            return set(json.load(f).get("ids", []))
    return set()

def save_last_seen(ids):
    with open(PREV_TRANSCRIPT_FILE, "w") as f:
        json.dump({"ids": list(ids)}, f)

def write_intel(transcripts):
    """Write new intel to daily memory file."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    mem_file = os.path.join(MEMORY_DIR, f"{today}.md")
    existing = ""
    if os.path.exists(mem_file):
        with open(mem_file) as f:
            existing = f.read()

    # Find new transcripts
    last_seen = load_last_seen()
    new = [t for t in transcripts if t["id"] not in last_seen]
    new_ids = [t["id"] for t in transcripts]
    save_last_seen(new_ids)

    if not new:
        print("No new Fireflies meetings.")
        return

    section = f"\n---\n\n## Fireflies Intel — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n\n"
    for t in new:
        ts = t.get("date", 0)
        try:
            dt = datetime.fromtimestamp(int(ts)/1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M")
        except:
            dt = str(ts)
        title = t.get("title", "Untitled")
        participants = t.get("participants", [])
        summary = t.get("summary", {}) or {}
        overview = summary.get("overview", "") or ""
        bullet_gist = summary.get("bullet_gist", "") or ""

        section += f"### Meeting: {title} — {dt}\n"
        section += f"Participants: {', '.join(participants)}\n\n"
        if bullet_gist:
            section += f"{bullet_gist}\n\n"
        elif overview:
            section += f"{overview[:300]}\n\n"

    with open(mem_file, "a") as f:
        f.write(section)

    print(f"Wrote intel for {len(new)} new meetings.")

if __name__ == "__main__":
    transcripts = get_recent_transcripts(20)
    write_intel(transcripts)