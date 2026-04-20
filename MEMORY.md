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
- Back from Queensland April 19/20

## This Week (Apr 20-24)
- Naomi pitch — tonight — new pricing structure
- Everstock proposal — tomorrow
- Scott Waterman — tomorrow, book meeting today
- Jess proposal — tomorrow
- Felix — wrap up (Orthogonal + training) → invoice
- Simon (Aquallis) — blocked waiting on his account details

## Polynize — Business
- Revenue target: tangible revenue NOW
- Strategy: Local sales (The Commons) + global authority (30 Days series)
- Pipeline value: ~$131k across 17 CRM contacts

## PAM (Polynize Agent Management) — Priority Project
- Separate Polynize team workflow from Marrs' personal workflow
- Team needs CRM visibility (currently zero)
- Will own: lead collection, email nurture, CRM management, proposal workflow
- Marrs building this in Claude

## Active Proposals — Hot Pipeline (Apr 20)
- **Naomi** — pitch tonight, new pricing structure
- **Everstock (AJ/Michael Cotton)** — $30k, proposal tomorrow
- **Scott Waterman (Roxbury)** — ~$10k first build, potentially 10-20 agents, meeting to book today, proposal tomorrow
- **Jess (Social Studio)** — $30k, proposal tomorrow
- **Felix (Cat Empire)** — 90% done, needs Orthogonal Google integration + training → ready to invoice
- **Simon (Aquallis)** — blocked waiting on his account details
- **Lorenzo/Supanova** — $30k-$80k, quoting

## Technical State
- Kraken API keys: transferred to Dash (moonshot project now managed by Dash)
- Fireflies API key: `77caf62a-9202-473c-afe4-8a4c02bcba9a` (working, refreshed)
- Google OAuth: rotated — ignore any previous credential references
- Moonshot Supabase 404: resolved by Dash managing the project

## Active Cron Jobs (key ones)
- Moonshot monitor: 9am daily (reduced from every 5 min)
- Workspace backup: every 6 hours
- Daily Northstar: 9:30am
- Rosie research: 11:15pm
- Scarlett sales review: 8am weekdays
- Dash morning check-in: 8am

## Integrations Needed
- **Xero** — Polynize Xero account needs integrating so Richie can create and send invoices
- **Google Calendar** — Richie needs read access to Marrs' calendar
- **Email** — Richie needs to be able to read emails
- **Orthogonal** — Need to integrate Felix's Google account with Orthogonal

## Critical Rules
- Email signature: Best, Richie AI Co-Ordinator / Polynize.ai
- MC deploy path: `~/.openclaw/workspace/projects/mission-control-v4/index.html`
- Never commit secrets to git
- `reports/` never tracked in git — restore from git commit `9151bd8` if needed
