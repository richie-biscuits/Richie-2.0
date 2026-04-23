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

## Active Deals — Updated Apr 23
- **Scott Waterman (Roxbury's Auction House)** — ✅ DEAL CLOSED $9,900. Build starts Fri Apr 24. Meeting confirmed 10am.
- **AJ/Everstock (Michael Cotton)** — ✅ DEAL CLOSED $28k setup + <$2k/mo. Survival supplies.
- **Jess/Social Studio** — $15k total ($5k+$10k) + $1k/mo. Still warm, Marrs re-engaged her Apr 23.
- **Naomi Ferstera** — $5k + $299/mo. Proposal sent, waiting. Marrs will nudge tomorrow (Apr 24).
- **Felix (Cat Empire)** — Built. Training session needed this week. Marrs to book weekend.
- **Simon (Aquallis)** — Meeting booked early next week (calendar shows no specific time yet).
- **Lorenzo/Supanova** — $30k-$80k. Gone quiet, will resurface when ready.
- **AJay Nevastok (Ajay from Everstock)** — Booked in Mon afternoon (see calendar).

## Integrations — Working
- **Xero** — ✅ Integrated via client credentials OAuth. Can create/authorise/send invoices. Token auto-refreshes.
- **Google Calendar** — ✅ Read access to marrs@polynize.io (read-only, can't write events to this calendar).
- **Email** — ✅ Gmail CLI at ~/.config/richie-google/gmail_cli.py. Token auto-refreshes.
- **Orthogonal** — Felix Google account integration still pending.

## Calendar (marrs@polynize.io)
- Roxbury build session: Fri Apr 24, 10am
- Jess meeting: Fri Apr 24, 1pm
- AJay Nevastok meeting: Mon Apr 27, 4pm
- Simon (Aquallis): early next week (time TBD)
- UQ iLab presentation: Tue Apr 28, 10:30am
- Queensland Uni presentation prep: Tue Apr 28 (Presentation Prep slot)

## Active Cron Jobs
- Fireflies Intel Collector: every 3hrs (3pm, 6pm, 9pm, midnight, 3am, 6am AEST)
- Rosie research: 11:15pm
- Scarlett sales review: 8am weekdays
- Dash morning check-in: 8am
- Daily Northstar: 9:30am
- Moonshot monitor: 9am daily
- Workspace backup: every 6hrs
- Google Calendar token refresh: every 55m
- Weekly Skills audit: Mondays 9am (error — needs fix)

## Technical State
- Fireflies API key: `77caf62a-9202-473c-afe4-8a4c02bcba9a` (working)
- Google OAuth: credentials at ~/.config/richie-google/ (working, read+write for richie calendar, read for marrs calendar)
- OpenClaw: upgraded to 2026.4.20 (Apr 22)
- Xero: client credentials OAuth working (token refreshes every ~25min)

## Critical Rules
- Email signature: Best, Richie AI Co-Ordinator / Polynize.ai
- Never commit secrets to git
- `reports/` never tracked — restore from git commit `9151bd8` if needed

## Reminders
- UQ iLab presentation: Tue Apr 28 morning — prep needed
- Naomi nudge: tomorrow Fri Apr 24
- Felix training session: book on weekend
- Agent team console (client-facing Mission Control): in progress — part of website infrastructure build
