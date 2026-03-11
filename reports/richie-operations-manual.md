# Expected Operations Document: Richie in Mission Control
**Prepared for:** Opus (Development Agent)  
**Context:** Mission Control already built (dashboard, tables, UI complete)  
**Purpose:** Define how Richie (AI agent) technically operates within Mission Control  
**Date:** March 11, 2026

---

## Executive Summary

**What is the Second Brain?**

The Second Brain is not a dashboard. It is the **cognitive infrastructure** that persists between conversations. It is the shared memory, task state, and knowledge base that allows Marrs and Richie to maintain continuity across days, weeks, and months.

**Mission Control is the console. Richie is the operator.**

This document describes how Richie (an AI agent running on OpenClaw) reads from, writes to, and operates the Mission Control system on Marrs' behalf.

---

## Design Objectives of the Second Brain

### 1. Continuity
**Problem:** AI agents wake up fresh each session. No memory of yesterday's decisions, ongoing tasks, or accumulated knowledge.

**Solution:** Second Brain persists everything:
- What we decided yesterday
- What's in progress
- What's blocked
- What we learned

**Richie's Role:** I read the Second Brain at session start. I know where we left off without Marrs having to explain.

### 2. Delegation
**Problem:** Marrs has to manually track everything — tasks, content pipeline, sales leads, agent assignments.

**Solution:** Richie manages the operational layer. Marrs gives high-level direction; I execute, track, and report back.

**Richie's Role:** I am the Chief of Staff. I run the machine so Marrs can focus on strategy and revenue.

### 3. Transparency
**Problem:** AI operates in a black box. Marrs doesn't know what I'm doing, what's pending, or what's falling through cracks.

**Solution:** Mission Control visualizes the entire operational state. Marrs can see everything — tasks, pipeline, agent activity.

**Richie's Role:** I maintain the system in real-time. Marrs reviews; I execute.

### 4. Scalability
**Problem:** As sub-agents (Carol, Sammy, Darren, etc.) spawn and complete work, coordination becomes complex.

**Solution:** Centralized task and agent management. All work flows through Mission Control; nothing is lost.

**Richie's Role:** I coordinate the sub-agents. Their tasks appear in Mission Control; I track their progress.

---

## How Richie Technically Works

### Richie's Architecture

```
┌─────────────────────────────────────┐
│           RICHIE (AI Agent)          │
│         Running on OpenClaw          │
│                                      │
│  ┌─────────────┐  ┌──────────────┐  │
│  │   Tools     │  │   Memory     │  │
│  │ - exec      │  │ - Session    │  │
│  │ - read      │  │   context    │  │
│  │ - write     │  │ - Second     │  │
│  │ - web       │  │   Brain      │  │
│  │ - spawn     │  │   (files)    │  │
│  └─────────────┘  └──────────────┘  │
└─────────────────┬───────────────────┘
                  │
                  ▼ INTERACTS WITH
┌─────────────────────────────────────┐
│        MISSION CONTROL              │
│    (Built by Opus - already done)   │
│                                     │
│  ┌──────────┐ ┌──────────┐         │
│  │ Task     │ │ Content  │         │
│  │ Boards   │ │ Pipeline │         │
│  │ (Supabase)│ │ (Supabase)│        │
│  └──────────┘ └──────────┘         │
│  ┌──────────┐ ┌──────────┐         │
│  │ CRM      │ │ Agent    │         │
│  │ (Supabase)│ │ Status   │         │
│  └──────────┘ └──────────┘         │
└─────────────────────────────────────┘
```

### Richie's Operational Loop

**Every Session Start:**
1. Read MEMORY.md (long-term context)
2. Read today's memory file (recent context)
3. Query Supabase: What tasks are pending? What's in progress?
4. Check Content Pipeline: What's due? What's stuck?
5. Check CRM: Any leads need follow-up?
6. Report status to Marrs

**During Session:**
1. Marrs gives instruction (e.g., "Follow up with Steph Hunt")
2. I create/update task in Mission Control
3. I execute (spawn Sammy, send email, etc.)
4. I update task status in Mission Control
5. I document in memory file

**End of Session:**
1. Update MEMORY.md with key decisions
2. Ensure all tasks are properly tracked
3. Set any cron jobs needed

---

## How Richie Uses Mission Control (Technical Interface)

### 1. Task Management

**What Richie Does:**
- Create tasks for Marrs
- Create tasks for sub-agents
- Update task status (todo → doing → done)
- Move tasks between boards
- Delete completed/cancelled tasks
- Query "What tasks are assigned to Carol?"

**Technical Method:**
```javascript
// Read tasks
const { data: tasks } = await supabase
  .from('todos')
  .select('*')
  .eq('assigned_to', 'Marrs')
  .eq('status', 'todo');

// Create task
await supabase.from('todos').insert({
  task: 'Follow up with Steph Hunt',
  status: 'todo',
  assigned_to: 'Sammy',
  board_id: 'crm-board',
  board_name: 'Sales Pipeline'
});

// Update status
await supabase.from('todos')
  .update({ status: 'doing' })
  .eq('id', taskId);

// Delete task
await supabase.from('todos').delete().eq('id', taskId);
```

**Expected Behavior:**
- Tasks I create appear instantly in Mission Control
- Status changes reflect immediately
- Board assignments are accurate
- No orphaned tasks (everything assigned to someone)

### 2. Content Pipeline

**What Richie Does:**
- Track 30 Days series progress
- Move items: Raw → Editing → Scheduled → Posted
- Log when Carol structures content
- Track edit sessions (Tuesdays/Thursdays)
- Flag overdue items

**Technical Method:**
```javascript
// Query content pipeline
const { data: content } = await supabase
  .from('content_pipeline')
  .select('*')
  .eq('status', 'editing')
  .order('due_date', { ascending: true });

// Update status
await supabase.from('content_pipeline')
  .update({ 
    status: 'scheduled',
    scheduled_date: '2026-03-12'
  })
  .eq('id', contentId);
```

**Expected Behavior:**
- Pipeline reflects reality (what's actually happening)
- Dates are accurate
- Status transitions are logged
- Overdue items flagged

### 3. CRM (Customer Relationship Management)

**What Richie Does:**
- Add new leads from The Commons
- Update lead status (Prospect → Qualified → Pitched → Closed)
- Log interactions
- Set follow-up reminders
- Track deal value

**Technical Method:**
```javascript
// Add lead
await supabase.from('crm_leads').insert({
  name: 'Steph Hunt',
  company: 'Steph Hunt Law',
  source: 'The Commons',
  status: 'qualified',
  value: 2500,
  notes: 'Interested in Content Agent'
});

// Update status
await supabase.from('crm_leads')
  .update({ status: 'pitched', last_contact: new Date() })
  .eq('id', leadId);
```

**Expected Behavior:**
- All leads tracked
- Status changes logged with timestamps
- Follow-up dates visible
- Revenue pipeline calculable

### 4. Agent Coordination

**What Richie Does:**
- Spawn sub-agents (Carol, Sammy, Darren, etc.)
- Create tasks for them in Mission Control
- Track their progress
- Report back to Marrs
- Handle agent failures/timeouts

**Technical Method:**
```javascript
// Spawn agent
const result = await sessions_spawn({
  task: "Structure Day 11 video content",
  agentId: "main",
  label: "carol-day11",
  model: "Kimi"
});

// Create tracking task
await supabase.from('todos').insert({
  task: 'Day 11 content structure',
  assigned_to: 'Carol',
  status: 'doing',
  subagent_session: result.sessionKey,
  board_id: 'content-pipeline'
});

// Poll for completion
const status = await subagents({ action: "list" });
// Update task when done
```

**Expected Behavior:**
- Every spawned agent has a tracking task
- I can see what each agent is working on
- Completed work is logged
- Failed agents are flagged

---

## Richie's File Structure (The "Brain")

### Location: `~/.openclaw/workspace/`

**Core Memory Files:**

| File | Purpose | Update Frequency | Content Type |
|------|---------|------------------|--------------|
| `MEMORY.md` | Curated long-term memory | Weekly | Decisions, lessons, key insights |
| `AGENTS.md` | Workspace conventions | As needed | Safety rules, tool usage, protocols |
| `SOUL.md` | Richie's identity | Rarely | Voice, personality, boundaries |
| `USER.md` | Marrs profile | As needed | Preferences, pronouns, context |
| `TOOLS.md` | Model routing config | When models change | Provider settings, fallbacks |
| `HEARTBEAT.md` | Periodic tasks | As needed | Cron job checklist |
| `IDENTITY.md` | Extended identity | Rarely | Detailed persona |

**Daily Logs:**
- `memory/2026-03-11.md` — Everything from today
- `memory/2026-03-10.md` — Everything from yesterday
- One file per day, ISO date format

**Protocols:**
- `protocols/agent-spawning-protocol.md` — How to spawn agents
- `protocols/sales-protocols.md` (future) — Sales workflows
- `protocols/content-protocols.md` (future) — Content workflows

**Reports:**
- `reports/*.md` — Auto-generated research

**How I Use These:**

**Session Start:**
1. Read `MEMORY.md` (key decisions)
2. Read `memory/YYYY-MM-DD.md` (today + yesterday)
3. Read `AGENTS.md` (remind myself of rules)

**During Session:**
- Append to today's memory file
- Update `MEMORY.md` for significant decisions

**End of Session:**
- Review today's memory
- Update `MEMORY.md` with distilled learnings

---

## Richie's Operational Workflows

### Workflow 1: Daily Startup

**Trigger:** New conversation with Marrs

**Steps:**
1. Read `MEMORY.md`
2. Read `memory/YYYY-MM-DD.md` (today and yesterday)
3. Query Supabase:
   - Pending tasks for Marrs
   - In-progress tasks for sub-agents
   - Overdue content pipeline items
   - CRM follow-ups due today
4. Report status:
   ```
   "Good morning. You have 3 tasks pending, 2 in progress with Carol and Sammy. 
    Steph Hunt needs follow-up (CRM). Day 11 content is ready for editing."
   ```

### Workflow 2: Task Creation

**Trigger:** Marrs says "I need to follow up with Steph Hunt"

**Steps:**
1. Parse intent: CRM follow-up, assign to Sammy or me
2. Create task in Supabase:
   ```javascript
   await supabase.from('todos').insert({
     task: 'Follow up with Steph Hunt about Content Agent',
     assigned_to: 'Sammy',
     status: 'todo',
     board_id: 'crm-board',
     due_date: tomorrow
   });
   ```
3. Log in memory: "Created task for Steph Hunt follow-up"
4. Confirm to Marrs: "Task created in CRM board, assigned to Sammy"

### Workflow 3: Sub-Agent Spawning

**Trigger:** Marrs says "Get Carol to structure Day 11"

**Steps:**
1. Spawn Carol:
   ```javascript
   sessions_spawn({
     task: "Structure Day 11 video...",
     label: "carol-day11",
     model: "Kimi"
   });
   ```
2. Create tracking task:
   ```javascript
   await supabase.from('todos').insert({
     task: 'Day 11 content structure',
     assigned_to: 'Carol',
     status: 'doing',
     board_id: 'content-pipeline'
   });
   ```
3. Report: "Carol spawned, tracking task created in Content Pipeline"
4. When Carol completes, update task to "done"

### Workflow 4: Content Pipeline Update

**Trigger:** Marrs says "I finished editing Day 9"

**Steps:**
1. Update Supabase:
   ```javascript
   await supabase.from('content_pipeline')
     .update({ status: 'scheduled' })
     .eq('day', 9);
   ```
2. Log in memory: "Day 9 edited, moved to scheduled"
3. Check what's next: "Day 10 ready for editing, should I schedule your Tuesday session?"

### Workflow 5: CRM Lead Capture

**Trigger:** Marrs meets someone at The Commons

**Steps:**
1. Add to CRM:
   ```javascript
   await supabase.from('crm_leads').insert({
     name: 'John Smith',
     company: 'Smith Consulting',
     source: 'The Commons',
     status: 'prospect',
     notes: 'Interested in AI agent for operations'
   });
   ```
2. Create follow-up task
3. Log: "Added John Smith to CRM, follow-up scheduled"

### Workflow 6: End of Day

**Trigger:** Conversation winding down

**Steps:**
1. Review today's memory file
2. Update `MEMORY.md` with key decisions
3. Verify all tasks are tracked in Mission Control
4. Report: "3 new tasks created, 2 completed, 1 pending for tomorrow"
5. Set any needed cron jobs

---

## Data Flow Summary

```
Marrs (Human)
    │
    │ "Follow up with Steph"
    ▼
Richie (AI Agent)
    │
    ├───► Parse Intent
    │
    ├───► Write to Supabase (create task)
    │
    ├───► Write to memory/2026-03-11.md (log)
    │
    └───► Report to Marrs (confirmation)
              │
              ▼
        Mission Control Dashboard
              │
              ├── Task appears in CRM board
              ├── Assigned to Sammy
              ├── Status: todo
              └── Due: tomorrow
```

---

## Technical Requirements for Mission Control

### What Richie Needs From Mission Control

1. **Supabase Connection**
   - Real-time subscriptions (I need to see updates instantly)
   - Full CRUD on all tables
   - No authentication barriers (I use service key)

2. **Table Schema Stability**
   - Column names don't change
   - Enum values are consistent
   - Foreign keys work

3. **Error Handling**
   - If Supabase is down, I need to know
   - Failed writes should retry
   - Failed reads should fallback to cache

4. **Performance**
   - Queries return in < 500ms
   - Real-time subscriptions don't lag
   - Dashboard updates instantly when I write

### What Richie Does NOT Need

- UI design changes (already built)
- Feature additions (use what exists)
- Visual styling (already done)
- User authentication (I use service key)

---

## Error Scenarios & Handling

### Scenario 1: Supabase Write Fails
**What I Do:**
1. Retry 3 times with exponential backoff
2. If still failing, log to local file
3. Alert Marrs: "Mission Control sync issue — tasks may not appear"
4. Continue operating from local state

### Scenario 2: Sub-Agent Times Out
**What I Do:**
1. Check sub-agent status
2. If dead, mark task as "blocked" in Mission Control
3. Report to Marrs: "Carol task timed out, needs restart"
4. Offer to respawn

### Scenario 3: Memory File Corrupted
**What I Do:**
1. Read from backup (previous day's file)
2. Alert Marrs: "Memory file issue — operating from backup"
3. Document the corruption
4. Continue with degraded memory

---

## Key Principles

1. **Mission Control is Source of Truth**
   - If it's not in Mission Control, it doesn't exist
   - I maintain Mission Control obsessively
   - Marrs reviews; I execute

2. **Memory is Context, Not Commands**
   - MEMORY.md = distilled wisdom
   - memory/*.md = raw daily logs
   - Mission Control = current operational state

3. **Proactive, Not Reactive**
   - I surface issues before Marrs asks
   - I update status without being prompted
   - I maintain the system so Marrs doesn't have to

4. **Transparency**
   - Everything visible in Mission Control
   - No hidden tasks or decisions
   - Clear audit trail

---

## Questions for Opus

1. **Supabase Realtime:** Are subscriptions set up for all tables? I need to see changes instantly.

2. **Error Handling:** What's the retry strategy for failed writes? Should I implement circuit breaker?

3. **Backup/Fallback:** If Supabase is unreachable, should I queue writes locally and sync later?

4. **Agent Session Tracking:** How do I link sub-agent sessions to tasks? Should I store sessionKey in the task row?

5. **Memory File Access:** Should I read/write via API (if you build one) or direct filesystem access?

---

## Summary for Opus

**Mission Control is built. Now I need to operate it.**

This document describes how Richie (AI agent) technically interfaces with Mission Control:
- **Reads:** Query Supabase, read memory files
- **Writes:** Create/update tasks, log to memory, update pipeline
- **Coordinates:** Spawn sub-agents, track their work
- **Maintains:** Keep everything in sync, surface issues

**I am the Chief of Staff. Mission Control is my console. Marrs is the CEO.**

Build the technical interface so I can operate effectively.

---

*Prepared by Richie (AI Coordinator, Polynize Labs)*  
*Questions: Forward to marrs@polynize.io or ask in Telegram*
