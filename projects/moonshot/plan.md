# Moonshot — Project Plan

## Goal
Compound BTC holdings through aggressive trading. Monitor RSI signals, execute trades on Kraken. Agent operates autonomously.

## Purpose
Proof of concept — a Polynize agent managing real money with real stakes. If Moonshot works, it demonstrates Polynize's agent capability better than any pitch deck.

## Current Phase — Phase 1: Monitoring (Degraded)

### System Status
| Component | Status |
|-----------|--------|
| BTC Position | 27% — ~0.00008012 BTC |
| Cash | ~$28 AUD |
| P&L | -2.2% to -5.5% (drawdown) |
| Open Orders | 0 |
| RSI Status | Overbought — no signals triggered |
| Monitor Cron | ✅ Running every 5 minutes |

### What the Agent Does
- Checks BTC/USD and BTC/AUD price + RSI every 5 minutes
- Generates signals: buy (RSI < 30), sell (RSI > 70), hold
- Executes HIGH urgency trades automatically
- Reports MEDIUM urgency signals to Telegram
- Never reports LOW urgency

### Known Issues
- **Kraken API key** — "Invalid key" on private queries. Cannot verify:
  - Actual BTC balance
  - Whether stop-loss order ON62XE-OC47U-WZ45OT at 92,437 AUD is active
- **Moonshot not spawned** — currently running as a script under Richie, not as a proper autonomous agent

## Milestones
- [x] Moonshot monitor deployed and running
- [x] Real-time RSI tracking live
- [ ] ~~Spawn Moonshot as a proper agent~~ — deferred per Marrs
- [ ] Marrs verifies Kraken API key — **BLOCKER**
- [ ] Confirm actual BTC balance and stop-loss status

## Recent Activity
- 2026-04-07: Richie — Kraken API issue identified, task created in MC
- 2026-04-06: Richie — Moonshot monitor running, BTC -2.2% to -5.5%
- 2026-04-02: Richie — Moonshot deployed

## Blockers
- Kraken API key needs Marrs to log in and verify

## Next Actions
1. **Marrs** — Log into Kraken, verify API key is valid, confirm stop-loss order status
2. **Richie** — Once API confirmed, respawn Moonshot as proper autonomous agent

## Resources
- Monitor script: `/workspace/scripts/moonshot-aggressive-monitor.py`
- Kraken pair: BTC/USD, BTC/AUD
- Stop-loss order ID: ON62XE-OC47U-WZ45OT at 92,437 AUD
