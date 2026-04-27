# Google Calendar - Token Errors

## 2026-04-28 05:59 AEST
- Refresh token returned HTTP 401 Unauthorized
- The refresh token may have expired or been revoked
- Manual re-authentication (OAuth flow) is needed to get a new refresh token
- Run the auth flow: `source ~/.config/google-calendar/secrets.env && python3 /Users/openclaw_admin/.openclaw/workspace/skills/google-calendar/scripts/auth_flow.py` (or whichever script handles initial auth)
