# Mission Control v1.1 Spec

## Current State
- Dashboard connected to Supabase
- Basic Kanban working with add/move/delete
- XSS and error handling fixed by Darren

## New Features Required

### 1. Agent-Based Task Boards
**Current:** Single Tasks tab with one Kanban
**New:** Tasks tab shows agent selector, then agent-specific board

**Flow:**
```
Sidebar Tasks icon clicked
↓
Shows: Marrs | Richie | Darren | Carol (agent cards)
↓
Click agent → Show that agent's Kanban board
↓
Add Task button → Creates task FOR that agent
```

**Database Change:**
- `todos` table already has `assigned_to` field
- Use this to filter tasks per agent

### 2. Modal Task Editor
**Current:** Browser prompt() for title only
**New:** Modal popup with full edit capabilities

**Modal Fields:**
- Title (text input)
- Notes/description (textarea)
- Priority (dropdown: urgent/high/normal/low)
- Due date (date picker)
- Status (dropdown: todo/doing/done)
- Delete button

**Trigger:** Click any task card

### 3. Drag & Drop
**Requirements:**
- Drag between columns (status change)
- Drag within column (reorder by priority)
- Visual feedback during drag

**Implementation:**
- HTML5 Drag and Drop API
- Add `position` integer field to `todos` table
- Sort by position within each status column
- Update positions on drop

### 4. Real-time Updates
**Current:** Manual refresh needed
**New:** Supabase realtime subscriptions

**Implementation:**
```javascript
supabase
  .channel('todos-changes')
  .on('postgres_changes', { event: '*', schema: 'public', table: 'todos' }, callback)
  .subscribe()
```

### 5. UI Polish
- Add favicon (remove 404 error)
- Better empty states ("No tasks yet" with icon)
- Loading states for async operations
- Priority colors: urgent=red, high=orange, normal=blue, low=gray

## Database Schema Updates

### Table: todos (existing, add field)
```sql
ALTER TABLE todos ADD COLUMN IF NOT EXISTS position INTEGER DEFAULT 0;
```

### Default Positions
When creating task: set position to max+1 in that status column

## Files to Modify
- `/Users/openclaw_admin/.openclaw/workspace/projects/mission-control-v4/dashboard.html`

## Success Criteria
1. Tasks tab shows agent selector (4 cards: Marrs, Richie, Darren, Carol)
2. Click agent → see their personal Kanban
3. Can add task to specific agent
4. Click task → modal opens with full edit
5. Can drag task between columns (status changes)
6. Can drag task within column (reorders)
7. Changes sync in real-time across tabs/devices
8. No console errors
9. Responsive design maintained

## Keep It Simple
- Don't over-engineer the drag & drop
- Use native HTML5 API, not heavy libraries
- Modal can be simple overlay div
- Agent selector is 4 clickable cards, nothing fancy

## Testing Checklist for Darren
- [ ] Add task as Marrs, appears in Marrs board only
- [ ] Add task as Richie, appears in Richie board only
- [ ] Drag task from todo → doing → done
- [ ] Drag task up/down within column to reorder
- [ ] Click task, modal opens, edit notes, save
- [ ] Change priority in modal, see color update
- [ ] Delete task from modal
- [ ] Open two browser tabs, add task in one, see it appear in other
- [ ] No JavaScript console errors

## Current Supabase Credentials (unchanged)
- URL: https://nryqpcmnncdhkgmgbpsr.supabase.co
- Using service_role key (embedded in file)

## When Done
- Commit changes with message: "v1.1: Agent task boards, drag-drop, modal editor, realtime sync"
- Report what works and any bugs found
