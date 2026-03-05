# Mission Control v4.1 — Build Specification Summary

**Source:** Claude.ai Artifact (c8bc5ce3-5d6e-4ee0-835d-0c4559a8c0d8)  
**Date:** 2026-03-05  
**Status:** Comprehensive spec received — needs prioritization

---

## The Vision

**Mission Control** = Dark HUD interface for managing a multi-agent content operation across two brands:
- **Marrs Attacks (MA)** — Personal brand
- **Polynize Labs (PL)** — Company/product

---

## Agent Architecture (4 Agents)

| Agent | Role | Status | Spawn Timing |
|-------|------|--------|--------------|
| **Richie** | Primary — orchestrator, task manager, router | ALWAYS ACTIVE | Day 1 |
| **Carol** | Copywriter — transcription, copy, hooks, scripts, YouTube packaging | SPAWN ON DEMAND | Day 2 |
| **Sage** | Social Media Manager — publishing queue, scheduling | SPAWN ON DEMAND | Day 3-4 |
| **Dan** | Data Analyst — platform APIs, performance, weekly digest | SPAWN ON DEMAND | Day 7-10 |

**Key Rule:** Richie is the ONLY agent Marrs talks to directly. Subagents never message directly.

---

## Content Streams (3)

### Stream 1: 30 Days of OpenClaw
- **Channel:** Marrs Attacks
- **Cadence:** Daily short-form
- **Agent Chain:** Carol → Sage
- **Workflow:** Record → Edit → Transcribe → Write Copy → Approve → Schedule → Live

### Stream 2: Thinking Protocol Use Case
- **Channel:** Polynize Labs
- **Cadence:** TBD
- **Agent Chain:** Carol → Sage
- **Workflow:** Concept → Script → Record → Edit → Package → Approve → Schedule

### Stream 3: Think Better Podcast
- **Channel:** Polynize Labs
- **Cadence:** Monthly (film last Friday, publish mid-month)
- **Agent Chain:** Carol → Sage → Clips loop
- **Workflow:** Script → Record → Edit → Transcribe → Clip ID → Package → Approve → Schedule → Clips pipeline

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Agent Backend** | OpenClaw (self-hosted) — multi-agent routing via sessions_spawn |
| **Frontend** | Next.js (React, TypeScript) — the Mission Control HUD |
| **Styling** | Tailwind CSS + Shadcn/ui — dark mode native |
| **State** | richie-state.json in Google Drive (source of truth) |
| **Files** | Google Drive API — scoped to Mission Control folder |
| **Analytics** | Platform APIs (YouTube, LinkedIn, TikTok, Instagram, X) |
| **Mobile** | Telegram (voice messages supported natively) |
| **Weather** | wttr.in API (free, no key) |
| **Intel** | Future: web search skill for Daily Intel Feed |

---

## UI Tabs (6 + Expandable)

1. **Dashboard** — Status, briefing, metrics, agent cards
2. **Tasks** — Marrs tab (personal) + Richie tab (agent tasks)
3. **Market Push** — Stream cards, phase trackers, approval workflow
4. **Analytics** — Platform panels, A/B tracking, weekly digest
5. **Files** — System, Local, Google Drive
6. **[+] Add Module** — Expandable slot for future modules

**Future Modules:** Newsletter, Outreach CRM, Lab Notes, Marketplace tracker, Daily Intel Feed

---

## Key Architectural Decisions

### State Management
- **richie-state.json** — Live operational state, read on startup, written after changes
- **Location:** ~/Google Drive/Mission Control/
- **Backup:** richie-state-backup.json (written before every state update)
- **Schema:** Includes dailyTracker, contentPipeline, activeAgents, waitingOn

### File Handoff
```
FCP export → Mission Control Drive/stream1/ → Carol pulls → writes outputs → Sage reads
```

### Approval Workflow
1. Carol completes → writes to Drive → notifies Richie
2. Richie notifies Marrs (Telegram or Mission Control)
3. Marrs approves (reply "approved" or button click)
4. State updates → Sage notified → phase tracker advances

### Notification Routing
- **Failure alerts:** Immediate Telegram
- **Urgent tasks:** Immediate Telegram
- **Approval requests:** Immediate Telegram with Drive link
- **Routine completions:** Batched to morning briefing (08:00)

---

## Model Selection (Cost-Optimized)

| Task | Model | Rationale |
|------|-------|-----------|
| Transcription (Carol) | haiku | Structured output, no reasoning |
| Platform copy (Carol) | sonnet | Voice matching + writing |
| Scripts/Strategy (Carol) | opus | Flagship content |
| YouTube packaging (Carol) | sonnet | SEO + writing |
| Queue management (Sage) | haiku | Simple structured tasks |
| Analytics digest (Dan) | sonnet or gemini | Data interpretation |
| Routine admin | haiku or deepseek | Low cost |
| Key decisions | opus | Never compromise |

---

## Build Phases (Realistic Timeline)

### Phase 1: Foundation (Days 1-2)
- [ ] Configure OpenClaw with all prompts
- [ ] Connect Telegram
- [ ] Connect Google Drive
- [ ] Validate morning briefing
- [ ] Add wttr.in weather endpoint

### Phase 2: Carol Activation (Days 3-4)
- [ ] Spawn Carol
- [ ] Run Stream 1 on OpenClaw native UI
- [ ] Validate transcription + copy workflow

### Phase 3: Sage + Dan Activation (Days 5-10)
- [ ] Spawn Sage
- [ ] Connect platform APIs
- [ ] Spawn Dan
- [ ] Validate full pipeline on native UI

### Phase 4: Custom Frontend (Weeks 3-4)
- [ ] Next.js frontend build starts
- [ ] Dashboard + Tasks tabs first

### Phase 5: Full UI (Weeks 5-6)
- [ ] Market Push tab with phase trackers
- [ ] Analytics tab with data feeds
- [ ] Files tab

---

## Critical Dependencies

### API Credentials Needed (Server .env)
- YouTube API (MA + PL channels)
- LinkedIn Marketing API
- TikTok Business API
- Instagram Graph API
- X/Twitter API v2
- Google Drive service account

### Token Maintenance
- LinkedIn: 60-day refresh
- TikTok: 30-day refresh (highest maintenance)
- Instagram: 60-day refresh
- Twitter: Bearer token (no expiry)
- YouTube: Refresh token (indefinite)

---

## Red Flags / Challenges

1. **Scope is MASSIVE** — This is 6+ weeks of full-time work
2. **API maintenance burden** — TikTok tokens every 30 days
3. **Platform API rate limits** — Need careful management
4. **Custom frontend is a big build** — Next.js + WebSocket + Drive API
5. **Real-time requirements** — Weather, analytics, notifications
6. **Shourov dependency** — Frontend build requires him

---

## Immediate Value vs Full Build

**Option A: Full Spec (6+ weeks)**
- Complete Mission Control HUD
- All 4 agents spawned
- Full platform API integration
- Custom Next.js frontend

**Option B: MVP First (1-2 weeks)**
- Richie only (already active)
- Telegram-based workflow (no custom UI yet)
- Google Drive file handoff
- Manual approval via Telegram replies
- Carol spawned for transcription/copy
- Basic state tracking in richie-state.json

**Recommendation:** Start with Option B. Prove the workflow, THEN build the HUD.

---

## Next Steps

1. **Install Codex 5.3** (today)
2. **Create richie-state.json** schema in Google Drive
3. **Spawn Carol** with copywriter prompt
4. **Run one Stream 1 content piece** end-to-end on OpenClaw native
5. **Document what works** before building custom UI

---

*Stored: 2026-03-05*  
*Next Action: Discuss MVP vs Full Build with Marrs*
