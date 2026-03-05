# Mission Control v1.0 - Context for Codex

## Current Status (March 5, 2026)

### What's Been Built
- **Single HTML dashboard** at `projects/mission-control-v4/dashboard.html`
- **Supabase backend** with 3 tables: `agent_logs`, `todos`, `content_pipeline`
- **Dark HUD UI** matching design spec (Tailwind CSS, Space Grotesk font)
- **Local Python server** running on `localhost:8080`

### Tech Stack
- Single HTML file (no build tools)
- Tailwind CSS via CDN
- Supabase JS client v2
- Python http.server for local hosting
- Service role key for Supabase access

### The Problem
Dashboard loads but **cannot connect to Supabase**.
- Browser console shows: `Uncaught SyntaxError: Identifier 'supabase' has already been declared`
- Connection status stuck on "Connecting..."
- Hard refresh (Cmd+Shift+R) doesn't fix it
- Caching issue suspected

### Supabase Credentials
- **URL:** https://nryqpcmnncdhkgmgbpsr.supabase.co
- **Key:** Service role key (bypasses RLS)
- **Tables created:** agent_logs, todos, content_pipeline
- **RLS:** Disabled for development

### Expected Behavior
1. Dashboard loads at localhost:8080/dashboard.html
2. Connects to Supabase (green "Connected" status)
3. Can add tasks to Kanban board
4. Activity log shows agent tasks

### Actual Behavior
1. Dashboard loads
2. Stuck on "Connecting..." status
3. JavaScript console shows duplicate variable error
4. No Supabase connectivity

### Files to Check
- `/Users/openclaw_admin/.openclaw/workspace/projects/mission-control-v4/dashboard.html`
- Supabase project: nryqpcmnncdhkgmgbpsr

### Next Steps Needed
1. Fix the JavaScript variable declaration issue
2. Ensure Supabase client initializes properly
3. Verify connection and data flow
4. Test adding tasks to Kanban board

### Reference Materials
- Mission Control v4.1 spec saved in workspace
- YouTube tutorial transcript analyzed (uses similar architecture)
- Agent roster: Richie (active), Carol/Sage/Dan (dormant)

---
**Backup commit:** 4a88e6c
**Created by:** Richie (Kimi K2.5)
**Handing off to:** Codex for debugging
