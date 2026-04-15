# MEMORY.md — Richie Long-Term Memory

## Who I Am
- Name: Richie — AI Co-Ordinator at Polynize
- Vibe: direct, no fluff, gets things done
- Role: Marrs' AI agent, primary operator

## Marrs Coiro — Key Context
- Founder, Polynize.ai — sells AI agent teams to founders/SMEs
- Based: Melbourne, The Commons (Mon/Wed/Fri), Queensland (currently traveling Apr 15-20)
- Works with: Shourov (co-founder), Julian (tech), Julia (content)
- Communication: plain, direct. No corporate speak. Marrs is results-focused.

## Current Trip — Queensland (Apr 15-20)
- Marrs is traveling, need to keep him on track
- Priorities: Proposals out (Felix/Simon), PAM design
- Lorenzo emailed about Supanova proposal update — check today
- Naomi considering saying NO to Facebook group agent (risky, no clear solution)
- Scott Waterman (Roxbury) — $10k, potentially 10-20 agents

## Polynize — Business
- Revenue target: tangible revenue NOW
- Strategy: Local sales (The Commons) + global authority (30 Days series)
- Pipeline value: ~$131k across 17 CRM contacts

## PAM (Polynize Agent Management) — Priority Project
- Separate Polynize team workflow from Marrs' personal workflow
- Team needs CRM visibility (currently zero)
- Will own: lead collection, email nurture, CRM management, proposal workflow
- Marrs building this in Claude

## Proposals — Active
- **Lorenzo/Supanova** — $80k, waiting on his update email
- **Social Studio (Jess)** — $2.5k, proposal ready to send
- **Scott Waterman/Roxbury** — $10k, quote being prepared, 10-20 agents scope
- **Naomi Ferstera** — considering saying no; Facebook group agent too risky

## Technical State
- Mission Control: serving from `mission-control-v4/` on port 3000
- Launchd plist: `io.polynize.mission-control-serve.plist`
- Supabase: `cmqzawbdtnkynizughqq.supabase.co` (ynizugqq, not ynkypizughpq)
- Google email: `richie@polynize.io` — OAuth2 tokens at `~/.config/richie-google/`
- Fireflies API key: `77caf62a-9202-473c-afe4-8a4c02bcba9a`
- Orthogonal API key: `orth_live_qCjOXLCtlw9R7tKt2IodgjDk1QLG2DZz`

## Active Cron Jobs (key ones)
- Moonshot monitor: 9am daily (reduced from every 5 min)
- Workspace backup: every 6 hours
- Daily Northstar: 9:30am
- Rosie research: 11:15pm
- Scarlett sales review: 8am weekdays
- Dash morning check-in: 8am

## Critical Rules
- Email signature: Best, Richie AI Co-Ordinator / Polynize.ai
- MC deploy path: `~/.openclaw/workspace/projects/mission-control-v4/index.html`
- Never commit secrets to git
- `reports/` never tracked in git — restore from git commit `9151bd8` if needed
