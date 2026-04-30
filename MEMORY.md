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

## Recent Fireflies & Intel Activity
- **Founder Align (Marrs x Shourov)** — Apr 30. Full transcript analysed. See Strategic Intel section below.
- **Polynize Weekly Wrap-Up** (Apr 24) — Pipeline prioritization, PwC demo prep, capability matrix, platform sprint to operational readiness.
- **Monica & Marrs** (Apr 24) — AI agents, trade logistics, career strategy.
- **Roxbury Debrief** (Apr 24) — Cognitive load mapping, Zendesk/Slack/Airtable agent setup.

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

## Strategic Intel — From Founder Align (Apr 30)

### Everstock Deal — Confirmed
- **Option 3 (Skin in the game):** $2k mapping + $8k install + $999/mo + profit share for 1st year (12-month experiment)
- Less than half the original quote, but special deal for seed investors (AJ/MC via Optio Capital)
- Everstock team is now prepping pricing structure detail + defining "what good looks like"
- Marrs creating systems map: what assets are being created vs not
- Timeline: mapping phase first, aiming for live within the month
- Plus $100/mo for AJ's 2 personal agents

### Roxbury — Cash Flow Detail
- Phase 1 invoice: $9k + GST (Scott forgot to pay GST — still owed)
- 2nd half: ~$4.5k + $900 GST = due within next month (certain)
- Phase 2: $17k across 4 more agents — timing depends on Scott's speed
- Monthly recurring ($999/mo) starts once mapping phase signed off
- **Roxbury Data Export Session:** Wed May 6, 11am — Jaden + Lacey (doing automation), Zendesk data export of ~1yr history. Marrs will design with Shourov's help on database architecture.
- Shourov invited — will try to move any clash.

### Simon (Aquallis) — Updated
- Will be one of Julian's training teams to build himself
- Shape: events management team → replicatable to other events management clients
- Decision due end of this week (today/tomorrow)

### PropleGig (Shourov's side)
- $4k coming in from PropleGig

### Tax Refund
- $5k back in tax

### PwC — Enterprise Signal
- Want to start commercial negotiations BEFORE evaluation is complete 🚀
- Need enterprise pricing model — Shourov has made a first effort, will show Marrs + Dhamiri

### Shourov's Pipeline (Enterprise Side)
- **Norviji** (via Avik): ~$30k — trying to close next week
- **Aldi** and others next week: small version (capability accelerator, 1-day) OR full pilot ($30-50k)
- **3 tiers:** small pilot → full pilot ($30-50k) → tier 1 engagement (PwC-style)
- **Dhamiri (Miri):** Now fully enabled to run full demos and close deals — started opening meetings
- Enterprise side getting energy

### Capability Mapping — Strategic Pivot
- **Marrs:** The mapping IS the value. "The prestige trick is the mapping." Don't need full proposals — just the map.
- **Shourov:** Will prototype an interactive UI: capabilities on left, dynamic team design on right, showing "before vs transformed" in one view
- **Marrs:** Mapping is foundational to the sales process, scalable (don't need deep expertise to run it), and everything (pricing, scope) flows from it
- **Cognitive Studio** branding: "Polynize Cognitive Studio" — the place where teams are built
- Client data gathering should happen inside the studio (not scattered across Google Drive)
- Live project documents (markdown, URL-accessible) as "gospel" — latest info that agents and humans can both reference

### Team Shape Taxonomy
- **Shourov's ask:** Create stripped-brand versions of active builds showing the shape/outcome, not the client name
  1. **Roxbury = Inbound Management / High Volume Operations** (funnel with lots of inbound → triage → important stuff at bottom)
  2. **Everstock = Market Research / Market Validation Team** (Shourov has market research contacts he could activate)
  3. **Simon = Events Management Team** (replicatable shape)
- Goal: Use these shapes to sell to other clients + get referrals (client reference + shape = powerful combo)
- **Key insight:** Outsourced functions (legal, accounting, etc.) already have budget allocated = easier sell than insourced (recruitment, cybersecurity) where you're replacing internal spend

### Build Process Upskill
- **Monday session planned:** Marrs + Shourov + Julian — whiteboard mapping the full build process in detail
- Marrs has 1 agent already live in Slack (Polynize team agents)
- Goal: identify where time is spent, what can be automated to 0, model the efficiency curve over 3 months
- Current: max 2 builds/month due to high cognitive load (everything is new)
- **2-month outlook:** 3-4x pricing, 10-20x less time per build (systems compounding)

### Revenue Forecast (Next 4 Weeks)
| Source | Amount | Certainty |
|--------|--------|-----------|
| Roxbury Phase 1 (remainder) | ~$5.4k | 100% |
| Everstock mapping | $2k | 100% |
| Everstock build (if within month) | $8k | High |
| Roxbury recurring (post-signoff) | $999/mo | High |
| Everstock recurring (post-build) | $999/mo | Medium |
| AJ's 2 agents | $100/mo | Medium |
| PropleGig (Shourov) | $4k | High |
| Tax refund | $5k | High |
| Norviji (Shourov) | ~$30k | Speculative |

### Product / Brand
- **Cursor** just released full agent team mode (every tile is an agent, async + pipelineable) — validating that "everyone wants the team workflow"
- **Sequoia diagram** discussed: outsourced vs insourced functions — outsourced has allocated budget = easier sell
- **HTML/Markdown > PDF** for deliverables (human+AI readable)
- Hidden agent instructions in white-on-white text (accidental discovery, promising)

## Key Actions & Reminders
- **Marrs:** Prepare Everstock mapping phase + systems map
- **Marrs:** Invite Shourov to Roxbury data export session (Wed May 6, 11am)
- **Marrs:** Send Shourov proposal links to Everstock/Roxbury (via Notion/my PS)
- **Marrs:** Prep stripped-brand team shape docs for: Inbound Management, Market Research, Events Management
- **Marrs:** Monday session — pipeline review + whiteboard build process with Shourov & Julian
- **Shourov:** Prototype interactive capability map UI in Claude
- **Shourov:** Work on enterprise pricing model, show to Marrs + Dhamiri
- **Felix:** Email to felix@catempire.com bounced. Need alternate contact.
- **Naomi:** Meeting booked to talk about niche coaching agent concept
- **Monica:** Meeting tomorrow (Fri May 1, 2pm)
