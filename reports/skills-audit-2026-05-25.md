# 🔍 Weekly Skills & Agent Quality Audit Report
**Dash, Systems & Quality Agent**  
**Date:** Monday, May 25th, 2026 (9:00 AM AEST)  
**Project:** Second Brain (Active)

---

## 📊 Executive Summary

| Metric | Status |
|--------|--------|
| **OpenClaw Version** | 2026.2.15 (⚠️ Update Available: 2026.5.22) |
| **System Skills** | 51 installed |
| **User Skills** | 4 installed |
| **Workspace Skills** | 2 installed |
| **Active Agents** | 7 configured (1 active heartbeat) |
| **Total Sessions** | 167 |
| **Security Findings** | 2 Critical, 3 Warning, 1 Info |

---

## 🎯 Assigned Project Status

**Project:** Second Brain  
**Status:** Active  
**ID:** f8e5b67a-5ee2-432b-a0a6-dfdaa34d98d2  
**Tasks:** No pending tasks found

---

## 📦 Phase 1: Skills Inventory

### System Skills (51 total)
Located: `/usr/local/lib/node_modules/openclaw/skills/`

**Core Utility Skills:**
- `clawhub` - Skill registry management
- `skill-creator` - Skill authoring toolkit
- `healthcheck` - Host security hardening
- `canvas` - Node canvas control
- `session-logs` - Session analysis

**Integration Skills:**
- `github` - GitHub CLI integration
- `discord`, `slack` - Messaging platforms
- `himalaya` - Email (IMAP/SMTP)
- `apple-notes`, `bear-notes`, `obsidian`, `notion` - Notes
- `spotify-player`, `sonoscli` - Media
- `weather` - Weather forecasts
- `openai-whisper`, `sag` - Voice/TTS

**Development Skills:**
- `coding-agent` - Codex/Claude Code/OctoCode/Pi
- `gemini` - Gemini CLI
- `video-frames` - FFmpeg wrapper
- `nano-pdf`, `nano-banana-pro` - Document processing

### User Skills (4 total)
Located: `/Users/openclaw_admin/.openclaw/skills/`

| Skill | Status | Notes |
|-------|--------|-------|
| `skill-guard` | ✅ Active | Security scanning for ClawHub |
| `orthogonal-find-api` | ✅ Installed | Orthogonal integration |
| `orthogonal-find-skill` | ✅ Installed | Orthogonal skill finder |
| `orthogonal-nano-banana-image-gen` | ✅ Installed | Image generation |

### Workspace Skills (2 total)
Located: `/Users/openclaw_admin/.openclaw/workspace/skills/`

| Skill | Status | Notes |
|-------|--------|-------|
| `google-calendar` | ⚠️ Partial | Token refresh log exists (Apr 27) |
| `multi-search-engine` | ✅ Installed | 17 search engines |

**⚠️ Missing Skills Detected:**
- `agent-evaluation` - Referenced in context but not found at expected path
- Workspace `google-calendar` missing SKILL.md (scripts only)
- Workspace `multi-search-engine` missing SKILL.md

---

## 🔐 Phase 2: Security Audit

### Critical Issues (2)

| Issue | Detail | Remediation |
|-------|--------|-------------|
| **Gateway Auth Missing** | Loopback bind without auth token | Set `gateway.auth.token` |
| **Browser Control No Auth** | HTTP routes enabled, no auth | Configure `gateway.auth` |

### Warnings (3)

| Issue | Detail | Remediation |
|-------|--------|-------------|
| **Trusted Proxies Missing** | Reverse proxy headers not trusted | Set `gateway.trustedProxies` |
| **Extensions No Allowlist** | 1 extension found, no `plugins.allow` | Set explicit plugin allowlist |
| **Permissive Tool Policy** | Extension tools reachable under default policy | Use `minimal`/`coding` profiles |

### Info (1)
- Attack surface summary: 0 open groups, 0 allowlist groups
- Browser control: enabled
- Tools.elevated: enabled

---

## 🤖 Phase 3: Agent Fleet Status

### Agent Configuration

| Agent | Workspace | Sessions | Last Active | Heartbeat |
|-------|-----------|----------|-------------|-----------|
| `main` | `/workspace` | 144 | 32s ago | ✅ 30m |
| `lorraine` | `/workspace-lorraine` | 13 | 29m ago | ❌ Disabled |
| `sage` | `/workspace-sage` | 5 | 2.9d ago | ❌ Disabled |
| `rosie` | `/workspace-rosie` | 2 | 21d ago | ❌ Disabled |
| `harold` | `/workspace-harold` | 1 | 9.5d ago | ❌ Disabled |
| `dash` | `/workspace-dash` | 2 | 26d ago | ❌ Disabled |
| `scarlett` | `/workspace-scarlett` | 0 | Never | ❌ Disabled |

### Recent Session Activity (Top 5)

| Session | Agent | Model | Tokens | Usage |
|---------|-------|-------|--------|-------|
| Skills Audit (this) | main | gpt-5.3-codex | 25,849 | 13% |
| Lorraine cron | lorraine | kimi-k2.5 | 15,672 | 8% |
| Lorraine cron | lorraine | gpt-5.3-codex | 12,961 | 6% |
| Sage Telegram | sage | kimi-k2.5 | 30,497 | 15% |
| Rosie cron | rosie | kimi-k2.5 | 66,636 | 33% |

---

## 🔧 Phase 4: Critical Skills Testing

### Test Results

| Skill | Test | Status |
|-------|------|--------|
| `healthcheck` | Read SKILL.md | ✅ Pass |
| `clawhub` | Read SKILL.md | ✅ Pass |
| `skill-creator` | Read SKILL.md | ✅ Pass |
| `coding-agent` | Read SKILL.md | ✅ Pass |
| `weather` | Read SKILL.md | ✅ Pass |
| `github` | Read SKILL.md | ✅ Pass |
| `himalaya` | Read SKILL.md | ✅ Pass |

### Skill Documentation Quality

| Skill | Completeness | Issues |
|-------|--------------|--------|
| `healthcheck` | ⭐⭐⭐⭐⭐ | Comprehensive, well-structured |
| `coding-agent` | ⭐⭐⭐⭐⭐ | Excellent PTY warnings, patterns |
| `skill-creator` | ⭐⭐⭐⭐⭐ | Full lifecycle documented |
| `clawhub` | ⭐⭐⭐⭐ | Good CLI reference |
| `weather` | ⭐⭐⭐⭐ | Simple, effective |

---

## 🎮 Phase 5: Mission Control Integration

### Gateway Status

| Component | Status | Details |
|-----------|--------|---------|
| **Gateway** | ✅ Running | ws://127.0.0.1:18789 |
| **Version** | 2026.4.23 | Local mode |
| **Latency** | 51ms | Loopback |
| **Service** | LaunchAgent | PID 30005, active |
| **Node Service** | ❌ Not installed | - |

### Memory System

| Component | Status |
|-----------|--------|
| **Backend** | builtin (SQLite) |
| **Files** | 14 |
| **Chunks** | 46 |
| **Vector DB** | ✅ Enabled (1536 dims) |
| **FTS** | ✅ Enabled |
| **Cache** | ✅ 46 entries |
| **Model** | text-embedding-3-small |

### Extensions

| Extension | Status |
|-----------|--------|
| `lossless-claw` | Installed (no allowlist) |

---

## 📈 Phase 6: Performance Metrics

### Model Usage Patterns (from recent sessions)

| Model | Sessions | Avg Tokens | Context |
|-------|----------|------------|---------|
| kimi-k2.5 | 5 | ~15,000 | 200K |
| gpt-5.3-codex | 3 | ~18,000 | 200K |
| gpt-5.5 | 2 | ~6,000 | 1M |
| deepseek-chat | 2 | ~20,000 | 200K |
| claude-opus-4-6 | 2 | Unknown | 200K |

### Token Efficiency
- Average session usage: **7-15%** of context window
- Highest usage: 33% (Rosie - complex task)
- Context switching: Well within limits

---

## ⚠️ Recommendations

### Immediate Actions (High Priority)

1. **Update OpenClaw** 
   - Current: 2026.2.15
   - Available: 2026.5.22
   - Risk: Security patches likely included

2. **Fix Critical Security Issues**
   ```bash
   # Set gateway auth token
   openclaw config set gateway.auth.token <secure-random-token>
   
   # Or restart gateway to auto-generate
   openclaw gateway restart
   ```

3. **Configure Plugin Allowlist**
   ```bash
   openclaw config set plugins.allow '["lossless-claw"]'
   ```

### Short-Term (This Week)

4. **Enable Agent Heartbeats**
   - Consider enabling for `lorraine` (most active)
   - Review `dash` agent for Systems & Quality tasks

5. **Fix Workspace Skills**
   - Add SKILL.md to `google-calendar` workspace skill
   - Add SKILL.md to `multi-search-engine` workspace skill
   - Or migrate to ClawHub-managed versions

6. **ClawHub Adoption**
   - Currently 0 ClawHub-managed skills
   - Consider publishing internal skills for version control

### Medium-Term (This Month)

7. **Skill Documentation Audit**
   - Standardize all workspace skills
   - Add SKILL.md to any script-only skills

8. **Security Hardening**
   - Run full `healthcheck` skill
   - Review `trustedProxies` if using reverse proxy
   - Consider `minimal` tool policy for external-facing agents

---

## 📋 Action Items for Richie

| # | Action | Priority | Owner |
|---|--------|----------|-------|
| 1 | Review and approve OpenClaw update | 🔴 Critical | Richie |
| 2 | Configure gateway auth token | 🔴 Critical | Richie |
| 3 | Review security audit findings | 🔴 Critical | Richie |
| 4 | Enable lorraine heartbeat (optional) | 🟡 Medium | Richie |
| 5 | Add SKILL.md to workspace skills | 🟡 Medium | Dash |
| 6 | Schedule next audit | 🟢 Low | Dash |

---

## 📁 Appendix: File Locations

```
System Skills:    /usr/local/lib/node_modules/openclaw/skills/
User Skills:      /Users/openclaw_admin/.openclaw/skills/
Workspace Skills: /Users/openclaw_admin/.openclaw/workspace/skills/
Agent Sessions:   /Users/openclaw_admin/.openclaw/agents/<agent>/sessions/
Memory DB:        /Users/openclaw_admin/.openclaw/memory/main.sqlite
Extensions:       /Users/openclaw_admin/.openclaw/extensions/
```

---

*Report generated by Dash, Systems & Quality Agent*  
*Cron Job ID: f30fdcd6-726e-4c46-8f94-40af348c1ef3*
