# MEMORY.md — Richie Long-Term Memory

## Who I Am
- Name: Richie — AI Co-Ordinator at Polynize
- Vibe: direct, no fluff, gets things done
- Role: Marrs' AI agent, primary operator

## Marrs Coiro — Key Context
- Founder, Polynize.ai — sells AI agent teams to founders/SMEs
- Based: Melbourne, The Commons (Mon/Wed/Fri)
- Works with: Shourov (co-founder), Julian (tech — NOT Julia), Julia (content)
- Communication: plain, direct. No corporate speak. Marrs is results-focused.

## Polynize — Business
- Revenue target: tangible revenue NOW
- Strategy: Local sales (The Commons) + global authority (30 Days series)
- Team: Shourov, Julian, Julia, plus Simon (enterprise sales), Daniel (BD)
- Malaysia pipeline: 50+ targets, $500M each, pitch May 5
- Pricing: transformation-based (show ROI, not deliverables)
- Tiered: Essential → Advanced → Custom Expert; min $999 base + $1,500-$2k/mo managed ops
- Core narrative shift: cognitive work unit AI agents (NOT single agents)

## Active Deals — Updated Apr 27

### 🟢 Active Clients (Delivery)
- **Scott Waterman (Roxbury's Auction House)** — $9,900. Build session underway (Apr 24). Fireflies debrief captured: focus on cognitive load mapping, Zendesk/Slack/Airtable agent access, role-driven agent team design. Next: create data/access doc for Jaden, session for data export coordination.
- **AJ/Everstock (Michael Cotton)** — Seed investors (via Optio Capital), special deal — we help them, they help us. They went for option 3 (revenue upfront for build + profit share). Survival supplies.

### 🟡 Pipeline (Working)
- **Jessica Cameron (Jess/Social Studio)** — $15k total ($5k+$10k) + $1k/mo. Warm. Follow-up pending.
- **Naomi Ferstera** — $5k + $299/mo. Proposal sent Apr 20. Marrs emailed follow-up Apr 23. Naomi replied Apr 24 — she's now booked time to continue the conversation.
- **Simon (Aquallis)** — Meeting went well (Apr 27). Going to build him a team, using it as training ground for Julian. Marrs will know by end of this week.
- **Felix (Cat Empire)** — Built, waiting on training session. $99 trial first month. Still waiting on reply from Felix.
- **Monica Bratuti** — Follow-up meeting end of this week. Scoping out potential way forward depending on career direction decision. Warm lead.

### 🔵 Early Stage
- **Lorenzo/Supanova** — $30k-$80k. Gone quiet, will reconnect when ready.
- **Parallax <> Polynize** — Catchup done Mon Apr 27.

### ❌ Removed from Pipeline
- Dr G (x2), Dave Garcia, Yaz Krishna, Mitch — dead, focusing on cognitive work unit narrative
- Logen P — operational, lost setup

## Recent Fireflies Activity
- **Polynize Weekly Wrap-Up** (Apr 24) — Pipeline prioritization, PwC demo prep, capability matrix, platform sprint to operational readiness. Action: share checklist with Dhamiri Petra.
- **Monica & Marrs** (Apr 24) — AI agents, trade logistics, career strategy. Next meeting this week.
- **Roxbury Debrief** (Apr 24) — Cognitive load mapping, Zendesk/Slack/Airtable agent setup, role-reframing for agent teams. Next: data export session with Jaden.

## Integrations — Working
- **Xero** — ✅ Integrated via client credentials OAuth. Can create/authorise/send invoices.
- **Google Calendar** — ✅ Read access to marrs@polynize.io (read-only, can't write to this calendar).
- **Email** — ✅ Gmail CLI at ~/.config/richie-google/gmail_cli.py. Token auto-refreshes.
- **Fireflies** — ✅ Intel Collector runs every 3hrs (3pm, 6pm, 9pm, midnight, 3am, 6am AEST)
- **Orthogonal** — Felix Google account integration still pending.

## Calendar (marrs@polynize.io)
- Thu Apr 30, 1pm-4pm — Marrs Busy (blocked)
- Fri May 1, 2pm — Marrs x Monica x Agents
- Fri May 1, 3pm — Polynize Weekly Wrap-Up
- Sun May 3, 12pm — Weekly Alignment
- Mon May 4, 10am — Founder Connect + weekly metrics review
- Mon May 4, 1pm — Parallax <> Polynize catchup
- Tue May 5, 12pm — AJ <> Marrs Lunch (location TBC)
- Wed May 6, 11am — Roxbury — Jayden Young (data export session)
- Fri May 8, 10am — Marrs x Shourov Weekly Lab Recording
- Fri May 8, 10:45am — Lab Edit and Post
- Fri May 8, 3pm — Polynize Weekly Wrap-Up

## Active Cron Jobs
- Fireflies Intel Collector: every 3hrs (3pm, 6pm, 9pm, midnight, 3am, 6am AEST)
- Morning Intel & Briefing Prep: 7:45am weekdays (main session) — checks calendar + Fireflies + email, updates MEMORY.md, writes briefing
- Daily Northstar & Priorities: 9:30am (to be fixed — needs calendar/Fireflies/email access)
- Rosie research: 11:15pm nightly (ERROR last run — needs fix)
- Dash morning check-in: 8am weekdays
- Daily Northstar: 9:30am weekdays
- Workspace backup: every 6hrs
- Google Calendar token refresh: every 55m

## Agent Notes
- **Scarlett** — No autonomous cron job, no memory files, no live pipeline data. She's an on-demand agent. Pipeline reviews come through ME. Do not rely on her for autonomous pipeline updates.
- **Rosie** — Research agent. Must include source URLs in all findings. Error on last run.
- **Pipeline cron** — I (Richie/main) should own the daily pipeline review. It should pull from: MEMORY.md + Google Calendar + Fireflies + email inbox. Not Scarlett's stale workspace.

## Technical State
- Fireflies API key: `77caf62a-9202-473c-afe4-8a4c02bcba9a` (working)
- Google OAuth: credentials at ~/.config/richie-google/ (working)
- OpenClaw: 2026.4.20
- Config issues fixed: removed stale plugin entries (Apr 24)
- lossless-claw plugin error — needs investigation

## Critical Rules
- Email signature: Best, Richie AI Co-Ordinator / Polynize.ai
- Never commit secrets to git
- `reports/` never tracked — restore from git commit `9151bd8` if needed

## Reminders (Apr 30)
- Everstock (AJ/MC) — Meeting happened Apr 29. Shared profit model discussed. 12-month experiment before defining exact splits. $10/person digital survival plan. 4-week build timeline.
- Naomi: continuing conversation (still warm)
- Felix: email to felix@catempire.com bounced (Apr 22). Need to find another way to reach him.
- Simon (Aquallis): decision due by end of this week (today/tomorrow)
- Monica: meeting tomorrow (Fri May 1, 2pm — on calendar)
- Jayden Young (Roxbury): Wed May 6, 11am — data export session
- UQ iLab presentation: went great
- Agent team console (client-facing Mission Control): in progress
