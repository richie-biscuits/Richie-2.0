# Weekly Skills & Agent Quality Audit
**Date:** Monday, April 27, 2026
**Auditor:** Dash (Systems & Quality Agent)
**Status:** 🟡 6 Issues Flagged

---

## 1. Integration Health

| Integration | Status | Notes |
|-------------|--------|-------|
| Fireflies API | ✅ OK | Marrs Coiro authenticated. Collector runs 3hrly. |
| Gmail / Email | ✅ OK | Richie can read/send. Recent threads visible. |
| Xero Accounting | ✅ OK | Token was expired; client-credentials refresh works. Invoices readable. |
| Orthogonal CLI | ✅ OK | Authenticated, $5.00 balance. Skills: find-skill, find-api installed. |
| Supabase DB | ✅ OK | All projects readable. Second Brain links table accessible. |
| Telegram | ✅ OK | Bots for Richie, Dash, Sage, Rosie, Scarlett, Harold all registered. |
| Slack | ✅ OK | Bot token active, main channel connected. |
| **Google Calendar** | ❌ **BROKEN** | OAuth client deleted. Token refresh failing since Apr 19. Needs Marrs to re-authorize. |
| OpenClaw Config | ⚠️ **Invalid** | 5 plugin entries reference non-existent plugins. Run `doctor --fix`. |

## 2. Cron Jobs — Error Summary

| Job | Schedule | Consecutive Errors | Last Error |
|-----|----------|-------------------:|------------|
| Hutcho Weekly Security | Weekly | 2 | Message too long (Telegram) |
| Daily Security Heartbeat | Daily | 2 | Missing Slack delivery target |
| Workspace GitHub Backup | Every 6hrs | **8** ⚠️ | Missing Slack delivery target |
| Rosie: Research Cycle | Nightly | **5** ⚠️ | Invalid Telegram target format |
| Daily Pipeline Review | Weekdays 8am | 1 | Missing Telegram chat ID |
| Skills & Agent Audit | Weekly Mon 9am | 1 (previous) | Delivery config missing |
| Google Calendar Refresh | Every 55min | N/A (task fails silently) | OAuth client deleted |

**Root cause:** Cron job delivery targets missing. Job runs succeed but delivery fails.

### Healthy Jobs (0 errors):
- Daily Northstar & Priorities
- Approved Task Processor (30min)
- Workspace Index Updater
- Weekly Rosie Stack Report
- Moonshot Aggressive Monitor
- Fireflies Intel Collector
- Dash Morning Check-in

## 3. Skills Inventory

### System Skills (48)
All standard OpenClaw skills present: apple-notes, clawhub, coding-agent, discord, gemini, github, healthcheck, himalaya, model-usage, openai-whisper, sag, session-logs, skill-creator, slack, tmux, trello, video-frames, weather, + 36 more.

### Installed Skills (3)
- `orthogonal-find-api` — Orthogonal API marketplace
- `orthogonal-find-skill` — Orthogonal skill search/install
- `skill-guard` — Security scanning for skills

### Workspace Skills (2) — Missing SKILL.md:
- `google-calendar/` — no SKILL.md
- `multi-search-engine/` — no SKILL.md

All skills cached and available in runtime. No package.json version tracking — updates not detectable via file inspection.

## 4. Agent Deployment Review

| Agent | Role | Status |
|-------|------|--------|
| Richie (main) | Primary operator | ✅ Full operational. Owns cron, Fireflies, integrations. |
| Dash | Systems & Quality | ✅ Workspace, SOUL.md, IDENTITY.md present. |
| Rosie | Cross-project research | ✅ Agent exists. Cron delivery broken. Last report: Apr 26. |
| Sage | Content pipeline | ✅ Agent exists. |
| Scarlett | Sales pipeline | ✅ Agent exists. No workspace SOUL.md docs found. |
| Harold | House agent | ✅ Narrow scope. Works as defined. |
| Moonshot | BTC trading | ✅ Monitor runs daily. |

## 5. Project Status (Supabase)

All projects active:
- **Second Brain (Dash)** — Active, 17 links. ⚠️ No purpose set.
- **Mission Control (Richie)** — Active. Meta-project for all 3 company goals.
- **Mission Control Builder (Richie)** — Active. Self-serve platform.
- **PAM Build (Richie)** — Active. Agent management factory.
- **Sales Pipeline (Scarlett)** — Active. $50k/mo target.
- **Content Pipeline (Sage)** — Active. 100k subscriber goal.
- **Polynize Brain (Rosie)** — Active. Cognition frameworks.
- **Moonshot** — Active. BTC trading.
- **Rosie Dreams** — Archived (replaced by Plan system).

## 6. Recommendations

### Critical
1. **Google Calendar OAuth** — Flag Marrs to re-authorize. No workaround.
2. **Fix cron delivery targets** — Update `jobs.json` with proper Slack channel IDs and Telegram chat IDs for 6 failing jobs.

### Important
3. **`openclaw doctor --fix`** — Remove 5 stale plugin entries from config.
4. **Define Second Brain project purpose** in Supabase.

### Nice-to-have
5. **Add SKILL.md files** to `google-calendar/` and `multi-search-engine/` workspace skills.
6. **Consider adding version tracking** to skill directories for update detection.
