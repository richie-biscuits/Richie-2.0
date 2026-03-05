# Mission Control v1.1.1 Bug Fixes & Hierarchy

## Bugs Reported by Marrs (URGENT)

### Bug 1: "No Tasks Yet" Blocking Tasks
**Issue:** The "No Tasks Yet" empty state message is physically blocking drag & drop into empty columns.
**Fix:** Remove or make non-blocking. Empty state should be placeholder only, not prevent drops.

### Bug 2: Task Duplication
**Issue:** Creating one task creates two identical tasks.
**Fix:** Check if addTodo() is being called twice (event listener issue or Supabase realtime triggering local insert again).

### Bug 3: Tasks Not Siloed By Agent
**Issue:** Adding task to Marrs board also adds to Richie board. Tasks not filtering properly by `assigned_to`.
**Fix:** 
- Verify `assigned_to` field is being set correctly on insert
- Verify query filters by `assigned_to = currentAgent`
- Check that agent selector actually changes the filter

### Bug 4: Remove "Day 7 of 30"
**Issue:** Hardcoded sprint tracker in header doesn't make sense yet.
**Fix:** Remove from header entirely.

## New Feature: Task Board Hierarchy

### Current Structure (broken)
```
Tasks Tab
└── Agent List (Marrs, Richie, Darren, Carol)
    └── Each has one Kanban
```

### New Structure Needed
```
Tasks Tab
├── Marrs Boards (multiple projects)
│   ├── Project A (Kanban)
│   ├── Project B (Kanban)
│   └── [+ New Board]
│
└── Agent Boards
    ├── Richie (Kanban)
    ├── Darren (Kanban)
    └── Carol (Kanban)
```

### Database Changes Needed

**Option A: Add board_id to todos table**
```sql
ALTER TABLE todos ADD COLUMN IF NOT EXISTS board_id TEXT DEFAULT 'default';
ALTER TABLE todos ADD COLUMN IF NOT EXISTS board_name TEXT DEFAULT 'Default Board';
```

**Query pattern:**
- Marrs Project A: `assigned_to = 'Marrs' AND board_id = 'project-a'`
- Richie board: `assigned_to = 'Richie'` (no board_id filter needed for agents)

### UI Flow

**Tasks Tab Landing:**
Shows two sections:

**Section 1: My Boards (Marrs)**
- Card for each board Marrs has created
- Shows board name + task count
- Click → open that board
- "+ New Board" button

**Section 2: Agent Boards**
- Card for each agent (Richie, Darren, Carol)
- Shows agent name + their task count
- Click → open agent's board
- Cannot create new boards here (agents have one board each)

**When adding task:**
- If on Marrs board → task assigned_to Marrs + board_id = current board
- If on Richie board → task assigned_to Richie (no board_id)

## Implementation Priority

1. **Fix blocking bugs first** (duplication, siloing, empty state)
2. **Remove Day 7/30** 
3. **Add board hierarchy**

## Keep It Simple
- Don't over-engineer the board hierarchy
- Marrs boards = just filtered views with a board_id
- Simple card grid for board selector
- One "New Board" flow: prompt for name, create with empty kanban

## Files
- `/Users/openclaw_admin/.openclaw/workspace/projects/mission-control-v4/dashboard.html`
- Run SQL in Supabase for new columns

## Testing Checklist
- [ ] Can create task on Marrs board, only appears there
- [ ] Can create task on Richie board, only appears there
- [ ] No task duplication
- [ ] Can drag into empty columns
- [ ] Can create new Marrs board
- [ ] Tasks stay in correct board after refresh
- [ ] "Day 7 of 30" removed from header
