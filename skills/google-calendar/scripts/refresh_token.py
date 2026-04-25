"""Refresh Google Calendar access token using OAuth2 refresh token."""
import os, json, urllib.request, sys, datetime

client_id = os.environ.get("GOOGLE_CLIENT_ID")
client_secret = os.environ.get("GOOGLE_CLIENT_SECRET")
refresh_token = os.environ.get("GOOGLE_REFRESH_TOKEN")
secrets_path = os.path.expanduser("~/.config/google-calendar/secrets.env")

if not all([client_id, client_secret, refresh_token]):
    print("Missing required env vars", file=sys.stderr)
    sys.exit(1)

data = urllib.parse.urlencode({
    "client_id": client_id,
    "client_secret": client_secret,
    "refresh_token": refresh_token,
    "grant_type": "refresh_token",
}).encode()

req = urllib.request.Request(
    "https://oauth2.googleapis.com/token",
    data=data,
    headers={"Content-Type": "application/x-www-form-urlencoded"},
)

try:
    resp = urllib.request.urlopen(req)
    body = json.loads(resp.read())
    new_access = body["access_token"]
    # Update the secrets file
    with open(secrets_path, "r") as f:
        content = f.read()
    import re
    content = re.sub(
        r'(export GOOGLE_ACCESS_TOKEN=).*',
        r'\1' + new_access,
        content
    )
    with open(secrets_path, "w") as f:
        f.write(content)
    ts = datetime.datetime.now().isoformat()
    log_msg = f"[{ts}] Token refreshed successfully\n"
    log_path = os.path.expanduser("~/.config/google-calendar/token_refresh.log")
    with open(log_path, "a") as f:
        f.write(log_msg)
    print("OK")
except Exception as e:
    ts = datetime.datetime.now().isoformat()
    err_msg = f"[{ts}] Token refresh failed: {e}\n"
    log_path = os.path.expanduser("~/.config/google-calendar/refresh_errors.log")
    with open(log_path, "a") as f:
        f.write(err_msg)
    print(f"FAILED: {e}", file=sys.stderr)
    sys.exit(1)
