# Mission Control — Project Plan

## Goal
Build and maintain a Mission Control system where Polynize's agent team operates autonomously, in alignment with company goals, and continuously improves.

## Purpose (Source of Truth)
META-PROJECT — ALL work serves 3 permanent company goals:
1. **Each agent is working autonomously** on a real project, making measurable change
2. **Each agent is self-improving** daily
3. **The system as a whole is integrated, secure, self-healing, and sustainable**

This project is the forcing function — if other projects drift from these goals, this project brings them back.

## Current Phase — Phase 1: Foundation Audit & Cleanup

### Milestones
- [x] Audit complete — 4 critical issues identified 2026-04-07
- [x] Rosie's Dream Cycle timeout fixed — timeout increased to 20min
- [x] Sage MC access confirmed working
- [x] Supabase key inconsistency resolved (not a real issue)
- [x] 23-task approval backlog cleared
- [ ] ~~Spawn Moonshot as a real agent~~ — deferred, not current priority
- [ ] Assign self-improvement loops to all agents — Scarlett, Dash, Moonshot

### Phase 1 Blockers
- Kraken API key verification — Marrs needs to log in and confirm key is valid

## Recent Activity
- 2026-04-07: Richie — Full MC audit complete. 4 week-1 tasks resolved. Task backlog cleared.
- 2026-04-07: Richie — Rosie's Dream Cycle timeout increased from 10min to 20min
- 2026-04-07: Richie — Agent-task-creator.py built and tested — agents can now create their own MC tasks

## Next Actions
1. **Marrs** — Verify Kraken API key (blocks Moonshot autonomy)
2. **Richie** — Design and implement self-improvement loops for Scarlett and Dash
3. **Richie** — Design project plan system (this system) and migrate all projects
4. **All agents** — Adopt project plan read/write protocol

## System Status
| System | Status |
|--------|--------|
| Rosie Dream Cycle | ✅ Running (timeout fixed) |
| Sage Content Pipeline | ✅ Live |
| Task Processor | ✅ Unblocked |
| Moonshot | ⚠️ API key issue |
| Dash Systems Review | ✅ Running daily |

## Resources
- MC Supabase: `cmqzawbdtnkynizughqq`
- Scripts: `/workspace/scripts/`
- This plan: `/workspace/projects/mission-control/plan.md`
