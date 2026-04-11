# RICHIE OPERATIONS MANUAL — Mission Control v4.3

**Last updated:** April 12, 2026
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
| Web server | io.polynize.mission-control-serve.plist | npx serve on port 3000 (launchd bootstrap, no wrapper script) |
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
| board_id | text | Which board it appears on — MUST be a valid ID (see §4) |
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
| project_plan | text | **APEX Plan** — strategic brief read by lead agent for autonomous execution. Lives between Description and Priority in project modal. |
| status | text | **active, paused, completed, archived** |
| assigned_to | text | Lead agent — owns execution, escalation, and updates |
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
| stage | text | **8-stage pipeline**: new_lead, contacted, discovery, proposal_sent, negotiating, won, client, lost |
| stage_group | text | **lead, active, closing, wrapped** |
| notes | text | Timestamped log, newest first |
| value | numeric | Deal value |
| source | text | Lead source |
| last_activity_at | timestamptz | |
| next_action | text | Free-text next step for this contact. Defaults to stage's defaultNextAction. |
| last_contact_date | date | Last time contact was reached out to |
| heat | smallint | **Heat scale 1–4**: 1=blue (cold), 2=yellow (warm), 3=orange (hot), 4=red (very hot). NULL=untagged. Visual dot on action queue and pipeline rows. |
| created_at | timestamptz | auto |

**Stage Migration (auto on MC load):**
- targeting → new_lead | qualified → contacted | meeting → discovery
- proposal → proposal_sent | negotiation → negotiating | won → won
- kickoff → client | lost → lost | paused → wrapped

**Stage Groups:**
| Group | Stages |
|-------|--------|
| lead | new_lead, contacted |
| active | discovery, proposal_sent |
| closing | negotiating, won |
| wrapped | client, lost |

### content_pieces
| Column | Type | Notes |
|--------|------|-------|
| id | uuid PK | auto-generated |
| title | text | NOT NULL |
| source_meeting | text | Meeting name |
| source_date | date | Meeting date |
| type | text | **newsletter, linkedin, twitter, video_script, image_concept** |
| brief | text | **Brief / Notes for Sage** — context, key points, client background |
| extract_text | text | Raw Sage output — "Draft Script" in UI |
| transcript | text | Video transcript (when type = video_script) |
| draft_text | text | Edited/approved version — "Post Text" in UI |
| status | text | **extracted, drafted, review, approved, scheduled, sent, dismissed** |
| tags | text[] | Content tags |
| scheduled_at | date | **Date-only (YYYY-MM-DD).** Indicates which day to post. Sage decides optimal posting time. PostgreSQL strips any time component if provided. |
| pillar | text | Content pillar/theme |
| format | text | **video, image, text** |
| video_url | text | Source video URL |
| image_prompt | text | Prompt used to generate image |
| image_url | text | URL of generated image |
| target_platforms | text[] | Platforms this piece targets |
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
| space | text | **Agentic, Content, Admin** — only these 3 values are valid in the UI |
| collection | text | Group name |
| name | text | Link display name |
| url | text | |
| favicon | text | |
| position | integer | Sort order |
| created_at | timestamptz | auto |

---

## 3. AGENT ROSTER

| Agent | Colour | Role | Board ID | Telegram |
|-------|--------|------|----------|---------|
| Richie | #60a5fa | Coordinator | Richie | @Richie (default account) |
| Rosie | #f472b6 | Research & Data | Rosie | @Polynize_Rosie_bot |
| Sage | #a78bfa | Social & Copy | Sage | @Polynize_Sage_bot |
| Scarlett | #facc15 | Sales & Strategy | Scarlett | — |
| Dash | #fb923c | Developer | Dash | @Marrs_Dash_bot |
| Moonshot | #f59e0b | Trading & Markets | Moonshot | — |

All agents have embedded low-poly origami portrait images in Mission Control.

---

## 4. VALID BOARD IDS (IMPORTANT)

**NEVER invent new board_id values.** Only use these 11 valid IDs:

**Agent boards (6):** Richie, Rosie, Sage, Scarlett, Dash, Moonshot
**Marrs boards (5):** marrs-mits, marrs-agent-build, marrs-admin, marrs-events, marrs-editing

When creating a task, the board_id determines which kanban the card appears on. Use the agent's name as board_id for agent tasks, or one of the 5 Marrs boards for personal tasks.

---

## 5. MARRS BOARDS (My Tasks tab)

| Board ID | Name | Icon |
|----------|------|------|
| marrs-mits | MITs | 🎯 |
| marrs-agent-build | Agent Builds | 🔧 |
| marrs-admin | Admin | 💳 |
| marrs-events | Events | 📅 |
| marrs-editing | Content | 🎬 |

---

## 6. TABS

| Tab | Description |
|-----|-------------|
| ◈ Dashboard | Growth stats, pipeline/CRM summary, agent status rows, notification bell |
| ◈ Projects | Project cards (priority sorted), APEX plan, lead agent — horizontal scroll on mobile, kanban stacks vertically on mobile |
| ☰ My Tasks | 5 Marrs boards (draggable tiles), kanban columns |
| ⚡ Agents | 6 agent tiles (draggable), kanban per agent |
| ✦ Content | Content Compiler — 5-column kanban (Extract → Draft → Review → Approved → Sent), drag-and-drop between columns |
| 📈 Analytics | Platform selector, overview cards, charts |
| ◉ CRM | Action Queue (sorted by overdue) + Pipeline table (collapsible groups). Heat dots, next_action, last_contact_date, stage migration |
| 📁 Files | File browser — folder tree + file viewer, reads from api.marrs-mc.com |
| ✎ Notes | Brain dump with titles, chronological feed |
| 🔗 Links | 3 spaces: Agentic, Content, Admin. Collections draggable onto different spaces. |
| ✉ Newsletter | Subscriber list synced from CRM, composer, send via Richie |

All tabs are draggable. Order persists in localStorage.

---

## 7. TASK WORKFLOW

### Creating Tasks
```sql
INSERT INTO todos (title, assigned_to, board_id, board_name, status, urgency)
VALUES ('Task description', 'AgentName', 'AgentName', 'AgentName', 'todo', 5);
```

### Task Statuses
- **todo** → task is queued
- **doing** → actively being worked on
- **blocked** → stuck, needs attention (pulses red in UI, notification bell)
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

## 8. PROJECTS

### How Projects Work
- Projects are higher-level containers that group tasks
- Each project has a lead agent (assigned_to)
- Tasks link to projects via the project_id column on todos
- project_id is a UUID matching a project's id in the projects table
- Projects are sorted by priority (highest first, left-to-right)

### APEX Plan
The `project_plan` field contains the **APEX Plan** — a strategic brief the lead agent reads before taking action. It sits between Description and Priority in the project modal.

Format: strategy, success criteria, agent instructions, context. The lead agent uses this to operate autonomously without needing to ask for direction on every decision.

### Creating a Project
```sql
INSERT INTO projects (name, purpose, description, project_plan, status, assigned_to, color, priority)
VALUES ('Project Name', 'Why it exists', 'Details', 'APEX plan text...', 'active', 'Rosie', '#f472b6', 7);
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

### board_id vs project_id
- **board_id** = which kanban board the task appears on (agent name or Marrs board ID)
- **project_id** = which project the task belongs to (UUID from projects table)
- These are TWO DIFFERENT SYSTEMS. Never use board_id to create "project boards".

---

## 9. CONTENT COMPILER (Sage Pipeline)

### Pipeline Flow
Fireflies transcript → Sage extracts → content_pieces table → MC kanban

### Status Flow
extracted → drafted → review → approved → scheduled → sent

### UI Field Names vs Database Columns
| Database column | MC UI label |
|-----------------|-------------|
| brief | Brief / Notes for Sage |
| extract_text | Draft Script |
| transcript | Video Transcript (video_script only) |
| draft_text | Post Text |

### New Fields on content_pieces
- `pillar` — content theme/topic
- `format` — video / image / text
- `video_url` — source video link
- `image_prompt` — image generation prompt
- `image_url` — generated image URL
- `target_platforms` — text[] of platforms

### Sage's Workflow
1. Read `brief` (Brief / Notes for Sage)
2. Write draft script into `extract_text` — "Draft Script" in UI
3. For video: record transcript, save to `transcript` — "Video Transcript"
4. Write post copy into `draft_text` — "Post Text"
5. Marrs reviews in MC: review → approved
6. Sage sets `scheduled_at` to target day (date only)
7. Sage executes posting via social-media-agent skill

### Scheduling (scheduled_at)
- `scheduled_at` is a **date-only field** (YYYY-MM-DD). It signals which DAY to post.
- **Sage decides the optimal posting time** based on platform and audience insights.
- Never write a full timestamp to `scheduled_at` — PostgreSQL will strip the time portion.
- When moving to `status='scheduled'`, set `scheduled_at` to the target day.

### How Sage Creates Content Pieces
```sql
INSERT INTO content_pieces (title, source_meeting, source_date, type, brief, status, created_by)
VALUES ('Key insight from meeting', 'Marrs x Client', '2026-04-01', 'newsletter', 'Context and key points...', 'extracted', 'sage');
```

When Sage drafts content:
```sql
UPDATE content_pieces SET extract_text = 'Draft script...', draft_text = 'Post copy...', status = 'drafted' WHERE id = '<id>';
```

Marrs reviews in MC and moves through: review → approved → scheduled → sent.

---

## 10. CRM

### Action Queue
The CRM tab opens to the Action Queue — contacts sorted by overdue next action. Use this as the daily working view.

Clicking the ✓ button on a contact marks it as contacted today:
- Sets `last_contact_date` to today
- Optionally moves stage forward (new_lead → contacted, discovery → proposal_sent, etc.)
- Records the interaction in `notes`

### Pipeline Table
Collapsible view grouped by stage_group (lead / active / closing / wrapped). Shows all contacts across all stages.

### Heat Scale
`heat` field on crm_contacts: 1–4 + NULL (untagged)
| Value | Label | Colour | Meaning |
|-------|-------|--------|---------|
| 1 | Cold | 🔵 blue | Early stage, no traction |
| 2 | Warm | 🟡 yellow | Active interest |
| 3 | Hot | 🟠 orange | Strong intent, near decision |
| 4 | Very Hot | 🔴 red | Close to signing |
| NULL | Untagged | ⚪ grey | Not yet scored |

Set heat by clicking the coloured dot on action queue or pipeline rows.

### next_action Field
Free-text field on each contact. Defaults to the stage's default next action but can be overridden. Shows in the action queue as the primary call-to-action for each contact.

---

## 11. NEWSLETTER

### Workflow
1. Subscribers synced from CRM contacts with emails
2. Marrs composes in the Newsletter tab
3. "Send via Richie" creates a task for Richie with full content and email list
4. Richie handles actual sending

---

## 12. FILE PREVIEW

- Tasks with file paths in notes show a 📄 Report button on the card
- Clicking opens a slide-in panel fetching from api.marrs-mc.com
- Detected patterns: memory/, reports/, scripts/, workspace/, or .md/.json/.csv/.txt files
- When creating tasks with associated files, ALWAYS include the file path in notes

---

## 13. NOTIFICATION BELL

Top bar, next to the clock. Red badge shows count of:
- Blocked tasks (status = 'blocked')
- High urgency tasks (urgency >= 8, status = 'todo')
- Overdue tasks (due_date in the past, status != 'done')

---

## 14. DRAG & DROP

| Element | Persists to |
|---------|------------|
| Main tabs | localStorage |
| Marrs board tiles | localStorage |
| Agent tiles | localStorage |
| Project cards | localStorage |
| Content compiler cards | Supabase (status column) |
| Link cards | Supabase |
| Link collections | Supabase (space field) |

---

## 15. INFRASTRUCTURE

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

## 16. GIT SAFETY RULES

The workspace git repo is the source of truth. Destructive git operations can destroy work.

### NEVER run in the workspace:
- `git reset --hard`
- `git clean -fdx`
- `git checkout <branch> -- .` (force overwrite)
- Any operation that discards uncommitted local changes

### Safe git workflow:
```bash
cd ~/.openclaw/workspace
git fetch origin
git merge --ff-only origin/main   # only moves forward, never destroys
git add <files>
git commit -m "message"
git push origin main
```

### Why --ff-only?
If local and remote have diverged, `--ff-only` aborts instead of creating a merge commit or resetting. This prevents accidental rollback.

---

## 17. CRITICAL RULES

1. NEVER execute unapproved tasks — check approved: true first
2. NEVER self-approve tasks — only Marrs approves
3. NEVER invent new board_id values — use only the 11 valid IDs (§4)
4. NEVER give out the Supabase service role key
5. NEVER modify Cloudflare Access settings without Marrs
6. ALWAYS use valid status values — todo, doing, blocked, done
7. ALWAYS link tasks to projects via project_id, not board_id
8. ALWAYS include file paths in task notes when tasks reference reports
9. ALWAYS set urgency 8-10 for genuinely urgent tasks
10. WHEN BLOCKED: set status='blocked', add reason to notes, notify Marrs+Richie
11. NEVER run `git reset --hard` in the workspace repo
12. scheduled_at on content_pieces is DATE ONLY — never write a full timestamp
