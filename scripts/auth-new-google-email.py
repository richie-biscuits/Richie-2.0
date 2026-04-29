#!/opt/homebrew/bin/python3
"""
Authorize a new Google email account for Richie to read/send from.
Run this for each account (marrs@polynize.io, etc).

Usage: python3 auth-new-google-email.py

You'll be prompted to log in to Google in your browser.
The token is saved to ~/.config/richie-google/tokens-{slug}.json
"""

import json
import os
import re
import sys

from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRET_FILE = os.path.expanduser('~/.config/richie-google/client_secret.json')
TOKEN_DIR = os.path.expanduser('~/.config/richie-google/')

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.compose',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/calendar.events.readonly',
    'https://www.googleapis.com/auth/calendar.calendars.readonly',
]

def main():
    email = input("Enter the Gmail/Google Workspace email address: ").strip()
    if not email or '@' not in email:
        print("Invalid email address")
        sys.exit(1)
    
    # Create a file-safe slug from the email
    slug = re.sub(r'[^a-z0-9]', '-', email.lower())
    token_file = os.path.join(TOKEN_DIR, f'tokens-{slug}.json')
    
    print(f"\n🔐 Authorizing: {email}")
    print(f"📁 Token will be saved to: {token_file}")
    print("\nA browser window will open. Log in as {email} and grant permission.")
    print("If you're already logged into a different Google account in your browser,")
    print("you may need to log out first or use an incognito window.")
    print()
    input("Press Enter when ready to open the browser...")
    
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    creds = flow.run_local_server(port=0, prompt='consent')
    
    with open(token_file, 'w') as f:
        f.write(creds.to_json())
    
    os.chmod(token_file, 0o600)
    
    print(f"\n✅ Authorization complete!")
    print(f"✅ Tokens saved to: {token_file}")
    print(f"✅ Refresh token: {'PRESENT' if creds.refresh_token else 'MISSING — need to re-run with prompt=consent'}")
    print()
    print(f"Richie can now read and send email as {email}")

if __name__ == '__main__':
    main()
