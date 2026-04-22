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

## Active Deals — Updated Apr 22
- **AJ/Everstock (Michael Cotton)** — $28k setup + <$2k/mo. Survival supplies. Decision today.
- **Naomi Ferstera** — $5k + $299/mo. Proposal sent, waiting on response.
- **Jess/Social Studio** — $15k total ($5k+$10k) + $1k/mo. Went well.
- **Scott Waterman (Roxbury)** — ~$10k first build, 10-20 agents. Meeting TODAY. Post-auction comms AI.
- **Felix (Cat Empire)** — Built. Training session needed this week → then invoice.
- **Simon (Aquallis)** — Blocked waiting on account details.
- **Lorenzo/Supanova** — $30k-$80k. quoting.

## Integrations Needed
- **Xero** — Need Polynize Xero account integrated for invoices
- **Google Calendar** — Richie needs read access
- **Email** — gmail_cli.py exists at ~/.config/richie-google/ but not fully integrated
- **Orthogonal** — Felix Google account integration still pending

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
- Google OAuth: fresh credentials at ~/.config/richie-google/
- OpenClaw: upgraded to 2026.4.20 (Apr 22)

## Critical Rules
- Email signature: Best, Richie AI Co-Ordinator / Polynize.ai
- Never commit secrets to git
- `reports/` never tracked — restore from git commit `9151bd8` if needed
