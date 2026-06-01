# 🔍 Weekly Skills & Agent Quality Audit Report
**Dash, Systems & Quality Agent**  
**Date:** Monday, June 1st, 2026 (9:00 AM AEST)  
**Project:** Second Brain (Active)

---

## 📊 Executive Summary

| Metric | This Week | Last Week | Change |
|--------|-----------|-----------|--------|
| **OpenClaw Version** | 2026.4.23 | 2026.4.23 | ↔️ No change |
| **System Skills** | 51 | 51 | ↔️ Stable |
| **User Skills** | 4 | 4 | ↔️ Stable |
| **Workspace Skills** | 2 | 2 | ⚠️ Still incomplete |
| **Active Agents** | 2 sandboxes | 7 configured | 🔄 Consolidated |
| **Security Findings** | 2 Critical, 4 Warning | 2 Critical, 3 Warning | ⚠️ +1 Warning |
| **Failed Integrations** | 1 | 1 | ↔️ Persistent |

---

## 🎯 Assigned Project Status

**Project:** Second Brain  
**Status:** Active  
**ID:** f8e5b67a-5ee2-432b-a0a6-dfdaa34d98d2  
**Tasks:** No pending tasks found (tasks table not accessible via current API key scope)

---

## 📦 Phase 1: Skills Inventory

### System Skills (51 total)
Located in sandboxes: `agent-dash-7aa57454`, `agent-main-f331f052`

**Core Utility Skills:**
- `clawhub` - Skill registry management ✅
- `skill-creator` - Skill authoring toolkit ✅
- `healthcheck` - Host security hardening ✅
- `session-logs` - Session analysis ✅
- `skill-guard` - Pre-install security scanning ✅

**Integration Skills:**
- `github` - GitHub CLI integration ✅
- `discord`, `slack` - Messaging platforms ✅
- `himalaya` - Email (IMAP/SMTP) ✅
- `apple-notes`, `bear-notes`, `obsidian`, `notion` - Notes ✅
- `spotify-player`, `sonoscli` - Media ✅
- `weather` - Weather forecasts ✅
- `openai-whisper`, `sag`, `sherpa-onnx-tts` - Voice/TTS ✅

**Development Skills:**
- `coding-agent` - Codex/Claude Code/OctoCode/Pi ✅
- `gemini` - Gemini CLI ✅
- `video-frames` - FFmpeg wrapper ✅
- `nano-pdf` - Document processing ✅

**Specialized Skills:**
- `1password` - Password manager ✅
- `bluebubbles`, `imsg` - iMessage ✅
- `openhue` - Philips Hue ✅
- `wacli` - WhatsApp CLI ✅
- `mcporter` - Mission Control porter ✅
- `taskflow`, `taskflow-inbox-triage` - Task management ✅
- `blogwatcher` - RSS monitoring ✅
- `xurl` - URL extraction ✅

### User Skills (4 total)
Located: `/Users/openclaw_admin/.openclaw/skills/`

| Skill | Status | Notes |
|-------|--------|-------|
| `skill-guard` | ✅ Active | mcp-scan security scanner |
| `orthogonal-find-api` | ✅ Installed | Orthogonal integration |
| `orthogonal-find-skill` | ✅ Installed | Orthogonal skill finder |
| `orthogonal-nano-banana-image-gen` | ✅ Installed | Image generation |

### Workspace Skills (2 total)
Located: `/Users/openclaw_admin/.openclaw/workspace/skills/`

| Skill | Status | Notes |
|-------|--------|-------|
| `google-calendar` | ❌ Broken | Token revoked since Apr 27. Needs full re-auth. Scripts only — no SKILL.md |
| `multi-search-engine` | ⚠️ Partial | Config JSON only — no SKILL.md. 17 engines defined but not tested |

**⚠️ Persistent Issues:**
- `agent-evaluation` - Referenced in context but **still not installed** (3+ weeks)
- Workspace `google-calendar` missing SKILL.md (scripts only)
- Workspace `multi-search-engine` missing SKILL.md (config only)

---

## 🔐 Phase 2: Security Audit

### Critical Issues (2) — UNCHANGED

| Issue | Detail | Remediation |
|-------|--------|-------------|
| **Gateway Auth Missing** | Loopback bind without auth token | Set `gateway.auth.token` |
| **Invalid Config** | Missing plugins: minimax, moonshot, anthropic | Run `openclaw doctor --fix` |

### Warnings (4) — +1 FROM LAST WEEK

| Issue | Detail | Remediation |
|-------|--------|-------------|
| **Trusted Proxies Missing** | Reverse proxy headers not trusted | Set `gateway.trustedProxies` |
| **Extensions No Allowlist** | Plugin allowlist references missing plugins | Fix config then set allowlist |
| **Permissive Tool Policy** | Extension tools reachable under default policy | Use `minimal`/`coding` profiles |
| **Service PATH Warning** | Version managers in gateway PATH | Run `openclaw doctor --repair` |

### Info (1)
- Gateway running as LaunchAgent with non-standard config
- Other gateway-like services detected: `com.polynize.lead-realtime-watchdog`, `com.polynize.lead-realtime`, `io.polynize.mc-file-server`, `io.polynize.mission-control-serve`

---

## 🤖 Phase 3: Agent Fleet Status

### Agent Configuration

| Agent | Workspace | Status | Last Active |
|-------|-----------|--------|-------------|
| `main` | `/workspace` | ✅ Active | Current session |
| `dash` | `/workspace-dash` | ⚠️ Sandbox only | 5+ weeks |
| `lorraine` | `/workspace-lorraine` | ❌ Not visible | - |
| `sage` | `/workspace-sage` | ❌ Not visible | - |
| `rosie` | `/workspace-rosie` | ❌ Not visible | - |
| `harold` | `/workspace-harold` | ❌ Not visible | - |
| `scarlett` | `/workspace-scarlett` | ❌ Not visible | - |

**Note:** Only `main` and sandboxed `dash` agents are currently visible in this environment. Other agents may be running on different hosts or configurations.

---

## 🔧 Phase 4: Critical Skills Testing

### Functional Tests

| Skill | Test | Status | Details |
|-------|------|--------|---------|
| `weather` | Live API call | ✅ Pass | Sunny +8°C, Melbourne |
| `github` | Auth check | ✅ Pass | richie-biscuits, full scopes |
| `skill-guard` | Read SKILL.md | ✅ Pass | mcp-scan ready, uv installed |
| `clawhub` | Search registry | ✅ Pass | Registry responsive |
| `healthcheck` | Read SKILL.md | ✅ Pass | Documentation complete |
| `google-calendar` | Token refresh | ❌ FAIL | 401 Unauthorized since Apr 27 |
| `multi-search-engine` | Config read | ⚠️ Partial | JSON valid, no SKILL.md wrapper |
| `orthogonal-find-api` | Path check | ✅ Pass | Files present |
| `orthogonal-find-skill` | Path check | ✅ Pass | Files present |

### Skill Documentation Quality

| Skill | Completeness | Issues |
|-------|--------------|--------|
| `skill-guard` | ⭐⭐⭐⭐⭐ | Excellent security docs |
| `healthcheck` | ⭐⭐⭐⭐⭐ | Comprehensive |
| `coding-agent` | ⭐⭐⭐⭐⭐ | PTY warnings, patterns |
| `clawhub` | ⭐⭐⭐⭐ | Good CLI reference |
| `weather` | ⭐⭐⭐⭐ | Simple, effective |
| `google-calendar` (workspace) | ⭐ | No SKILL.md, scripts only |
| `multi-search-engine` (workspace) | ⭐ | No SKILL.md, config only |

---

## 🎮 Phase 5: Mission Control Integration

### Gateway Status

| Component | Status | Details |
|-----------|--------|---------|
| **Gateway** | ✅ Running | ws://127.0.0.1:18789 |
| **Version** | 2026.4.23 | Local mode |
| **Service** | LaunchAgent | PID 31312, active |
| **Config Health** | ❌ Invalid | Missing plugin refs |
| **RPC Probe** | ⚠️ Blocked | Auth token required |

### Mission Control Services Detected

| Service | Status | Plist Location |
|---------|--------|----------------|
| `io.polynize.mission-control-serve` | Detected | `~/Library/LaunchAgents/io.polynize.mission-control-serve.plist` |
| `io.polynize.mc-file-server` | Detected | `~/Library/LaunchAgents/io.polynize.mc-file-server.plist` |
| `com.polynize.lead-realtime` | Detected | `~/Library/LaunchAgents/com.polynize.lead-realtime.plist` |
| `com.polynize.lead-realtime-watchdog` | Detected | `~/Library/LaunchAgents/com.polynize.lead-realtime-watchdog.plist` |

### Supabase Integration

| Component | Status |
|-----------|--------|
| **Endpoint** | cmqzawbdtnkynizughqq.supabase.co |
| **Project Query** | ✅ Working (anon key) |
| **Task Query** | ❌ Failed — `public.tasks` table not found |
| **Assigned Project** | Second Brain (active) |

---

## 📈 Phase 6: Performance & Dependencies

### Dependency Versions

| Tool | Version | Status |
|------|---------|--------|
| Node.js | v25.6.1 | ✅ Current |
| `uv` | 0.10.12 | ✅ Installed |
| `clawhub` | Latest | ✅ Working |
| `gh` CLI | Latest | ✅ Authenticated |
| `openclaw` | 2026.4.23 | ⚠️ Check for updates |

### Environment

| Component | Value |
|-----------|-------|
| **OS** | Darwin 25.3.0 (arm64) |
| **Host** | Administrator's Mac mini |
| **Shell** | zsh |
| **Model** | moonshot/kimi-k2.6 |

---

## ⚠️ Recommendations

### Immediate Actions (High Priority)

1. **Fix Google Calendar Integration**
   ```bash
   # The refresh token has been revoked since Apr 27
   # 1. Go to https://console.cloud.google.com/apis/credentials
   # 2. Generate new OAuth refresh token
   # 3. Update secrets.env
   ```
   **Impact:** Blocking calendar-based agent workflows

2. **Fix OpenClaw Config**
   ```bash
   openclaw doctor --fix
   # Then:
   openclaw doctor --repair
   ```
   **Impact:** Resolves plugin errors and service PATH warnings

3. **Set Gateway Auth Token**
   ```bash
   openclaw config set gateway.auth.token $(openssl rand -hex 32)
   openclaw gateway restart
   ```
   **Impact:** Secures local gateway from unauthorized access

### Short-Term (This Week)

4. **Install `agent-evaluation` Skill**
   - Referenced for 3+ weeks but never installed
   - Needed for proper agent benchmarking
   - Available on ClawHub or create custom

5. **Fix Workspace Skills**
   - Add SKILL.md to `google-calendar` workspace skill
   - Add SKILL.md to `multi-search-engine` workspace skill
   - Or migrate to ClawHub-managed versions

6. **Investigate Missing Agents**
   - `lorraine`, `sage`, `rosie`, `harold`, `scarlett` not visible
   - Check if running on different hosts/configs

### Medium-Term (This Month)

7. **ClawHub Adoption**
   - Currently 0 ClawHub-managed skills in workspace
   - Consider publishing internal skills for version control
   - Use `clawhub update --all` for automated updates

8. **Mission Control Health Check**
   - Verify `io.polynize.mission-control-serve` is healthy
   - Check service logs for errors
   - Ensure lead-realtime services are functioning

---

## 📋 Action Items for Richie

| # | Action | Priority | Owner | Deadline |
|---|--------|----------|-------|----------|
| 1 | Fix Google Calendar OAuth (revoked token) | 🔴 Critical | Richie | This week |
| 2 | Run `openclaw doctor --fix && --repair` | 🔴 Critical | Richie | Today |
| 3 | Set gateway auth token | 🔴 Critical | Richie | Today |
| 4 | Install `agent-evaluation` skill | 🟡 Medium | Richie/Dash | This week |
| 5 | Add SKILL.md to workspace skills | 🟡 Medium | Dash | This week |
| 6 | Verify Mission Control services healthy | 🟡 Medium | Richie | This week |
| 7 | Schedule next audit | 🟢 Low | Dash | Jun 8 |

---

## 📁 Appendix: File Locations

```
System Skills:    /usr/local/lib/node_modules/openclaw/skills/
User Skills:      /Users/openclaw_admin/.openclaw/skills/
Workspace Skills: /Users/openclaw_admin/.openclaw/workspace/skills/
Agent Sessions:   /Users/openclaw_admin/.openclaw/agents/<agent>/sessions/
Agent Sandboxes:  /Users/openclaw_admin/.openclaw/sandboxes/
Memory DB:        /Users/openclaw_admin/.openclaw/memory/main.sqlite
Extensions:       /Users/openclaw_admin/.openclaw/extensions/
Reports:          /Users/openclaw_admin/.openclaw/workspace/reports/
Config:           /Users/openclaw_admin/.openclaw/openclaw.json
```

---

## 📊 Change Log (vs May 25 Audit)

| Item | May 25 | Jun 1 | Status |
|------|--------|-------|--------|
| OpenClaw version | 2026.2.15 → 2026.5.22 available | 2026.4.23 | Updated but not to latest? |
| Google Calendar | Token refresh log (Apr 27) | Still failing 401 | ❌ No progress |
| Security findings | 2 Critical, 3 Warning | 2 Critical, 4 Warning | ⚠️ Worse (+PATH warning) |
| Agent heartbeats | 1 active | Consolidated to sandboxes | 🔄 Architecture changed |
| Workspace skills | Missing SKILL.md | Still missing SKILL.md | ❌ No progress |
| Agent-evaluation skill | Missing | Still missing | ❌ No progress |

---

*Report generated by Dash, Systems & Quality Agent*  
*Cron Job ID: f30fdcd6-726e-4c46-8f94-40af348c1ef3*  
*Next audit scheduled: Monday, June 8th, 2026*
