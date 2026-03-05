# Mission Control Build Plan v1.0
## Current Status & Darren's Checklist

**Last Updated:** March 5, 2026  
**Current Phase:** Foundation (Step 4-5)  
**Dashboard Status:** ✅ Connected to Supabase, basic Kanban working

---

## Phase 1: Foundation Checklist

### ✅ COMPLETED
- [x] Supabase project created (nryqpcmnncdhkgmgbpsr)
- [x] Database tables: agent_logs, todos, content_pipeline
- [x] Codex 5.3 installed and running
- [x] Dashboard v1.0 HTML file built and connected
- [x] Supabase connection working (Darren fixed redeclaration bug)

### 🔄 IN PROGRESS (Darren's Current Tasks)

#### Task 1: Verify Core Functionality
- [ ] Test adding task via Kanban board
- [ ] Verify task appears in Supabase `todos` table
- [ ] Test moving task through states (todo → doing → done)
- [ ] Verify completed tasks show in "Done" column
- [ ] Check that task counts update in stats panel

#### Task 2: Test Agent Logging
- [ ] Verify agent_logs table structure
- [ ] Test manual insert to agent_logs (simulate Richie logging a task)
- [ ] Confirm activity log displays recent entries
- [ ] Check that model_used field captures correctly

#### Task 3: Error Handling & Edge Cases
- [ ] Test dashboard behavior when Supabase is unreachable
- [ ] Verify graceful error messages (not crashes)
- [ ] Test browser refresh mid-task-add
- [ ] Check mobile responsiveness (basic)

#### Task 4: Content Pipeline UI (Prep for Next Phase)
- [ ] Review content_pipeline table schema
- [ ] Design UI mockup for content tracking (30 Days, Protocols, Podcast)
- [ ] Identify what's needed for "Add Content" workflow
- [ ] Note any schema changes needed

#### Task 5: Carol Integration Prep
- [ ] Document what Carol needs to write to agent_logs
- [ ] Plan how Carol outputs get to Mission Control
- [ ] Identify file handoff workflow (Google Drive → Dashboard)

---

## Phase 2: Agent Activation (Next)

### Spawn Carol (Copywriter Agent)
**When:** After dashboard v1.0 is verified stable
**Mission:** 
- Transcribe 30 Days video
- Write platform copy (LinkedIn, X, etc.)
- Log all activity to Mission Control

**Integration Points:**
- Carol writes to `agent_logs` table
- Dashboard shows Carol's activity in real-time
- File handoff via Google Drive Mission Control folder

### Spawn Sage (Social Media Manager)
**When:** After Carol successfully completes 2-3 content pieces
**Mission:**
- Publishing queue management
- Schedule approved content
- Log publishing activity

### Spawn Dan (Data Analyst)
**When:** 5+ content pieces published
**Mission:**
- Pull platform API data
- Weekly digest generation
- Performance alerts

---

## Phase 3: Content Workflow Test

### End-to-End Test: One 30 Days Video
1. Marrs records Day X video → drops in Drive
2. Carol transcribes, writes copy → logs to agent_logs
3. Marrs approves via dashboard
4. Sage schedules to platforms
5. Dan monitors performance
6. Dashboard shows complete pipeline

---

## What Darren Should Report Back

1. **Bugs Found:** Any issues in current dashboard
2. **Fixes Applied:** What was changed and why
3. **Verified Working:** What's confirmed functional
4. **Blockers:** Anything preventing Phase 2
5. **Recommendations:** What to build next

---

## Success Criteria for v1.0

- ✅ Dashboard loads at localhost:8080
- ✅ Shows "Connected" to Supabase
- ✅ Can add/move/delete tasks in Kanban
- ✅ Tasks persist in Supabase
- ✅ Activity log shows agent activity
- ✅ Stats panel updates in real-time
- ✅ No console errors on normal usage

---

## Files to Check

- `/Users/openclaw_admin/.openclaw/workspace/projects/mission-control-v4/dashboard.html`
- `/Users/openclaw_admin/.openclaw/workspace/projects/mission-control-v4/HANDOFF.md`
- Supabase Tables: agent_logs, todos, content_pipeline

**Git Status:** All changes should be committed with clear messages
