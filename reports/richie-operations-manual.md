# RICHIE OPERATIONS MANUAL — Mission Control v4.3

**Last updated:** April 2026
**System:** Mission Control — Single-file vanilla HTML/CSS/JS dashboard
**Frontend:** https://mc.marrs-mc.com (served via `npx serve -s .` on Mac Mini)
**API Server:** https://api.marrs-mc.com (Flask on port 5001, Cloudflare Tunnel)
**Backend:** Supabase (project: cmqzawbdtnkynizughqq)

---

## 1. CONNECTION DETAILS

### Supabase
- **Project URL:** https://cmqzawbdtnkynizughqq.supabase.co
- **Anon key:** eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNtcXphd2JkdG5reW5penVnaHFxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI2NzI1MTQsImV4cCI6MjA4ODI0ODUxNH0.Ha0-nnKHmCPBbfHYaebCcbjmeKZLrXYfGxTjuVlmLw8
- **RLS:** "Allow all access" policies on all tables

### API Server
- **URL:** https://api.marrs-mc.com
- **Endpoints:** GET /list?path=X (list files), GET /file?path=X (read file)
- **Security:** Cloudflare Access (marrs@polynize.io only). Browser requests use cookie auth. Local requests (localhost:5001) bypass Cloudflare.
- **CORS:** flask-cors with supports_credentials=True, origins=['https://mc.marrs-mc.com']
- **Server script:** scripts/mc-file-server.py

### Infrastructure
- **Cloudflare Tunnel ID:** 92adb04f-f536-439c-8d92-95e870179cad
- **Config:** ~/.cloudflared/config.yml
- **Routes:** mc.marrs-mc.com → localhost:3000, api.marrs-mc.com → localhost:5001

### Auto-start Services (launchd)
| Service | Plist | What it does |
|---------|-------|-------------|
| Web server | io.polynize.mission-control-serve.plist | npx serve on port 3000 |
| Cloudflare tunnel | io.polynize.mission-control-tunnel.plist | cloudflared tunnel |
| File API server | io.polynize.mc-file-server.plist | Flask on port 5001 |

All plists in ~/Library/LaunchAgents/. KeepAlive=true on all three.

---

## 2. SUPABASE TABLES

### todos (tasks)
| Column | Type | Notes |
|--------|------|-------|
| id | uuid PK | auto-generated |
| title | text | NOT NULL — task description |
| status | text | **todo, doing, blocked, done** |
| assigned_to | text | Agent name or 'Marrs' |
| board_id | text | Which board it appears on |
| board_name | text | Display name of board |
| due_date | date | Optional |
| notes | text | Free text, file paths, context |
| urgency | integer | 1-10 scale |
| approved | boolean | Agent tasks need Marrs approval |
| subtasks | jsonb | Array of {text, done} objects |
| project_id | uuid | Links to projects table |
| created_at | timestamptz | auto |
| completed_at | timestamptz | Set when status → done |

### projects
| Column | Type | Notes |
|--------|------|-------|
| id | uuid PK | auto-generated |
| name | text | NOT NULL |
| purpose | text | Why the project exists |
| description | text | Details, scope |
| status | text | **active, paused, completed, archived** |
| assigned_to | text | Lead agent name |
| color | text | Hex colour for card |
| priority | integer | 1-10, sorts cards left-to-right |
| created_at | timestamptz | auto |
| updated_at | timestamptz | auto |

### crm_contacts
| Column | Type | Notes |
|--------|------|-------|
| id | uuid PK | auto-generated |
| name | text | Contact name |
| company | text | |
| email | text | |
| phone | text | |
| stage | text | 16-stage pipeline |
| stage_group | text | prospecting, negotiating, delivery, inactive |
| notes | text | Timestamped log, newest first |
| value | numeric | Deal value |
| source | text | Lead source |
| last_activity_at | timestamptz | |
| created_at | timestamptz | auto |

### content_pieces
| Column | Type | Notes |
|--------|------|-------|
| id | uuid PK | auto-generated |
| title | text | NOT NULL |
| source_meeting | text | Meeting name |
| source_date | date | Meeting date |
| type | text | **newsletter, linkedin, twitter, video_script, image_concept** |
| extract_text | text | Raw Sage output |
| draft_text | text | Edited/approved version |
| status | text | **extracted, drafted, review, approved, scheduled, sent, dismissed** |
| tags | text[] | Content tags |
| scheduled_at | timestamptz | |
| sent_at | timestamptz | |
| dismissed_at | timestamptz | |
| created_by | text | 'sage' or 'marrs' |
| created_at | timestamptz | auto |
| updated_at | timestamptz | auto |

### newsletter_subscribers
| Column | Type | Notes |
|--------|------|-------|
| id | uuid PK | auto-generated |
| contact_id | uuid | FK → crm_contacts |
| email | text | NOT NULL |
| name | text | |
| tag | text | **lead, client, vip** |
| subscribed | boolean | Toggle on/off |
| created_at | timestamptz | auto |

### newsletter_sends
| Column | Type | Notes |
|--------|------|-------|
| id | uuid PK | auto-generated |
| subject | text | NOT NULL |
| body | text | NOT NULL |
| recipient_count | integer | |
| status | text | **draft, sending, sent** |
| sent_at | timestamptz | |
| created_at | timestamptz | auto |

### notes
| Column | Type | Notes |
|--------|------|-------|
| id | uuid PK | auto-generated |
| title | text | |
| content | text | |
| created_at | timestamptz | auto |
| updated_at | timestamptz | auto |

### analytics
| Column | Type | Notes |
|--------|------|-------|
| id | uuid PK | auto-generated |
| platform | text | youtube, linkedin, twitter, instagram, tiktok |
| date | date | |
| followers | integer | |
| views, likes, comments, shares | integer | |
| content_title | text | |
| content_id | text | |
| stream | text | |
| Unique | | (platform, date, content_id) |

### links
| Column | Type | Notes |
|--------|------|-------|
| id | uuid PK | auto-generated |
| space | text | Polynize, Marrs, Richie Bot, Netta World |
| collection | text | Group name |
| name | text | Link display name |
| url | text | |
| favicon | text | |
| position | integer | Sort order |
| created_at | timestamptz | auto |

---

## 3. AGENT ROSTER

| Agent | Colour | Role | Board ID |
|-------|--------|------|----------|
| Richie | #60a5fa | Coordinator | Richie |
| Rosie | #f472b6 | Research & Data | Rosie |
| Sage | #a78bfa | Social & Copy | Sage |
| Scarlett | #facc15 | Sales & Strategy | Scarlett |
| Dash | #fb923c | Developer | Dash |
| Moonshot | #f59e0b | Trading & Markets | Moonshot |

All agents have embedded low-poly origami portrait images in Mission Control.

---

## 4. MARRS BOARDS (My Tasks tab)

| Board ID | Name | Icon |
|----------|------|------|
| marrs-mits | MITs | 🎯 |
| marrs-agent-build | Agent Builds | 🔧 |
| marrs-admin | Admin | 💳 |
| marrs-events | Events | 📅 |
| marrs-editing | Content | 🎬 |

**NEVER invent new board_id values.** Valid board_ids are the 5 Marrs boards above plus the 6 agent names (Richie, Rosie, Sage, Scarlett, Dash, Moonshot).

---

## 5. TABS (11 total, order is user-configurable via drag)

| Tab | Description |
|-----|-------------|
| ◈ Dashboard | Copy Meeting Link, growth stats, pipeline/CRM summary, agent status rows, notification bell |
| ◈ Projects | Project cards with priority sorting, lead agent, filtered kanban per project |
| ☰ My Tasks | 5 Marrs boards (draggable tiles), kanban columns |
| ⚡ Agents | 6 agent tiles (draggable), kanban per agent |
| ✦ Content | Content Compiler — 5-column kanban (Extract→Draft→Review→Approved→Sent) |
| 📈 Analytics | Platform selector, overview cards, charts |
| ◉ CRM | 16-stage pipeline, contact detail with timestamped notes |
| 📁 Files | File browser — folder tree + file viewer, reads from api.marrs-mc.com |
| ✎ Notes | Brain dump with titles, chronological feed |
| 🔗 Links | 4 spaces, draggable collections and cards |
| ✉ Newsletter | Subscriber list synced from CRM, composer, send via Richie |

All tabs are draggable — Marrs can reorder them. Order persists in localStorage.

---

## 6. TASK WORKFLOW

### Creating Tasks
```sql
INSERT INTO todos (title, assigned_to, board_id, board_name, status, urgency)
VALUES ('Task description', 'AgentName', 'AgentName', 'AgentName', 'todo', 5);
```

### Task Statuses
- **todo** → task is queued
- **doing** → actively being worked on
- **blocked** → stuck, needs attention (pulses red in UI, shows in notification bell)
- **done** → completed

### Approval System
- Agent tasks in 'todo' have an approval checkbox
- Only Marrs can approve tasks
- Agents MUST check approved = true before executing
- NEVER self-approve tasks

### Urgency Scale (1-10)
- 1-4: Low priority (grey)
- 5-7: Medium priority (amber)
- 8-10: High priority (red) — shows in notification bell

### Blocked Task Protocol
When setting a task to blocked:
1. Set status = 'blocked'
2. Add reason in the notes field
3. The task will pulse red in the UI
4. It will appear in the notification bell dropdown
5. Immediately notify Marrs and Richie

### Subtasks
Stored as jsonb array in the subtasks column:
```json
[{"text": "Do step 1", "done": false}, {"text": "Do step 2", "done": true}]
```

---

## 7. PROJECTS

### How Projects Work
- Projects are higher-level containers that group tasks
- Each project has a lead agent (assigned_to)
- Tasks link to projects via the project_id column on todos
- project_id is a UUID matching a project's id in the projects table
- Projects are sorted by priority (highest first, left-to-right)

### Creating a Project
```sql
INSERT INTO projects (name, purpose, description, status, assigned_to, color, priority)
VALUES ('Project Name', 'Why it exists', 'Details', 'active', 'Rosie', '#f472b6', 7);
```

### Linking Tasks to Projects
```sql
-- Step 1: Find the project UUID
SELECT id, name, assigned_to FROM projects WHERE name ILIKE '%project name%';

-- Step 2: Create a task linked to the project
-- Use the project's assigned_to as the agent AND board_id
INSERT INTO todos (title, assigned_to, board_id, board_name, status, project_id, urgency)
VALUES ('Build onboarding flow', 'Rosie', 'Rosie', 'Rosie', 'todo', '<project-uuid>', 6);
```

The task appears in BOTH the agent's kanban board AND the project's filtered kanban.

### Important: board_id vs project_id
- **board_id** = which kanban board the task appears on (agent name or Marrs board ID)
- **project_id** = which project the task belongs to (UUID from projects table)
- These are TWO DIFFERENT SYSTEMS. Never use board_id to create "project boards".

---

## 8. CONTENT COMPILER

### Pipeline Flow
Fireflies transcript → Sage extracts → content_pieces table → MC shows in kanban

### Status Flow
extracted → drafted → review → approved → scheduled → sent

### How Sage Creates Content Pieces
```sql
INSERT INTO content_pieces (title, source_meeting, source_date, type, extract_text, status, created_by)
VALUES ('Key insight from meeting', 'Marrs x Client', '2026-04-01', 'newsletter', 'Extract text...', 'extracted', 'sage');
```

When Sage drafts content:
```sql
UPDATE content_pieces SET draft_text = 'Draft content...', status = 'drafted' WHERE id = '<id>';
```

Marrs reviews in MC and moves through: review → approved → sent.

---

## 9. NEWSLETTER

### Workflow
1. Subscribers synced from CRM contacts with emails
2. Marrs composes in the Newsletter tab
3. "Send via Richie" creates a task for Richie with full content and email list
4. Richie handles actual sending

---

## 10. FILE PREVIEW

- Tasks with file paths in notes show a 📄 Report button on the card
- Clicking opens a slide-in panel fetching from api.marrs-mc.com
- Detected patterns: memory/, reports/, scripts/, workspace/, or .md/.json/.csv/.txt files
- When creating tasks with associated files, ALWAYS include the file path in notes

---

## 11. NOTIFICATION BELL

Top bar, next to the clock. Red badge shows count of:
- Blocked tasks (status = 'blocked')
- High urgency tasks (urgency >= 8, status = 'todo')
- Overdue tasks (due_date in the past, status != 'done')

---

## 12. DRAG & DROP

| Element | Persists to |
|---------|------------|
| Main tabs | localStorage |
| Marrs board tiles | localStorage |
| Agent tiles | localStorage |
| Project cards | localStorage |
| Link cards | Supabase |
| Link collections | localStorage |

---

## 13. INFRASTRUCTURE

### File Locations
| What | Path |
|------|------|
| Dashboard HTML | ~/.openclaw/workspace/projects/mission-control-v4/index.html |
| Cloudflare config | ~/.cloudflared/config.yml |
| File server | ~/.openclaw/workspace/scripts/mc-file-server.py |
| LaunchAgents | ~/Library/LaunchAgents/io.polynize.*.plist |

### Cloudflare Access
- Both mc.marrs-mc.com and api.marrs-mc.com under one Access application
- Policy: "Marrs Only" (marrs@polynize.io)
- DO NOT remove mc.marrs-mc.com from the application
- DO NOT remove CORS config from Flask
- DO NOT modify Cloudflare Access settings without Marrs

### If API Returns 502
Flask server on port 5001 has stopped:
```bash
lsof -i :5001 | grep LISTEN
# If nothing:
launchctl unload ~/Library/LaunchAgents/io.polynize.mc-file-server.plist
launchctl load ~/Library/LaunchAgents/io.polynize.mc-file-server.plist
```

---

## 14. CRITICAL RULES

1. NEVER execute unapproved tasks — check approved: true first
2. NEVER self-approve tasks — only Marrs approves
3. NEVER invent new board_id values — use only the 11 valid IDs
4. NEVER give out the Supabase service role key
5. NEVER modify Cloudflare Access settings without Marrs
6. ALWAYS use valid status values — todo, doing, blocked, done
7. ALWAYS link tasks to projects via project_id, not board_id
8. ALWAYS include file paths in task notes when tasks reference reports
9. ALWAYS set urgency 8-10 for genuinely urgent tasks
10. WHEN BLOCKED: set status='blocked', add reason to notes, notify Marrs+Richie
