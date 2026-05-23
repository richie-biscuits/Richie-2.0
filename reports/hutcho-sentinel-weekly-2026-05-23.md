# Hutcho Sentinel — Weekly Security Assessment
**Date:** Saturday, May 23, 2026 — 08:43 AEST  
**Assessor:** Hutcho Sentinel (Richie cron)  
**Target:** OpenClaw deployment on Administrator’s Mac mini (macOS 26.3.1)  
**Protocol:** Frozen Cognition Protocol v1.0

---

## 🎯 Executive Summary

| Metric | Value |
|--------|-------|
| **Decision Band** | 🟡 CONDITIONAL / THAWING |
| **Security Score** | **67 / 100** |
| **Critical Findings** | 2 |
| **Warnings** | 4 |
| **Info** | 1 |
| **Status** | Operational but config drift detected. Security guarantees are degraded due to validation failures. |

**Bottom line:** The host is physically secure (FileVault ON, firewall active), but OpenClaw’s configuration layer is in a *thawed* state — validation errors are forcing best-effort config loading, which means stated auth policies may not be reliably enforced. This is the primary concern this week.

---

## 🧊 Frozen Cognition Protocol — Evaluation Criteria

The Frozen Cognition Protocol requires five pillars to be locked:

| Pillar | Requirement | Status | Notes |
|--------|-------------|--------|-------|
| **1. Config Integrity** | Config must load without validation errors | ❌ **FAIL** | `openclaw.json` fails validation on 8 plugin entries |
| **2. Auth Freeze** | Gateway auth must be deterministic and enforced | ⚠️ **DEGRADED** | Token present in config, but audit reports it missing due to best-effort fallback |
| **3. Agent Containment** | Sandbox/tool policies must restrict agent cognition | ⚠️ **PARTIAL** | 167 active sessions; tool policy permissive for extensions |
| **4. Visibility Lock** | Dashboard/control UI must not be exposed beyond trusted boundary | ✅ **PASS** | Gateway bound to loopback (127.0.0.1:18789); Tailscale OFF |
| **5. Patch Currency** | OS and runtime must be within 30 days of latest stable | ⚠️ **DEGRADED** | macOS 26.3.1 current; OpenClaw 2026.4.23 has update available (2026.5.20) |

---

## 🔍 System State Gathered

### Host Layer
- **OS:** macOS 26.3.1 (arm64) — Darwin 25.3.0
- **Last OS update:** March 22, 2026 (macOS Tahoe 26.3.1)
- **FileVault:** ON ✅
- **Application Firewall:** ON (blocking non-essential incoming) ✅
- **Signed software auto-allow:** ENABLED (standard macOS behavior)
- **Listening ports (relevant):**
  - `127.0.0.1:18789` — OpenClaw gateway (loopback-only) ✅
  - `*:3000`, `*:5000`, `*:5001`, `*:7000` — Local dev services (LM Studio, Python apps, Control Center)
  - `127.0.0.1:20241` — cloudflared
  - `127.0.0.1:1235` — LM Studio local inference
  - `127.0.0.1:41343` — LM Studio secondary
  - `[::1]:7679` — Google (Chrome/ChromeDriver)

### OpenClaw Runtime
- **Version:** 2026.4.23 (a979721)
- **Update status:** Available — 2026.5.20 published May 20
- **Gateway:** Local loopback, auth token configured
- **Model auth:** Using legacy auth-profiles fallback (runtime.modelAuth unavailable)
- **Tailscale:** OFF
- **Agents:** 7 configured, 167 active sessions
- **Heartbeat:** 30m for main; disabled for dash, harold, lorraine, rosie, sage, scarlett
- **Channels:** Telegram (6 bots), Slack (1 workspace)
- **Extensions:** 1 installed — `lossless-claw` v0.3.0 (npm-installed, errors on load)

### Active Cron Jobs (from memory — `openclaw cron list` failed due to config errors)
1. Fireflies Intel Collector — every 3hrs
2. Morning Briefing — 7:45am weekdays
3. Rosie research — 11:15pm nightly (reported ERROR on last run)
4. Dash morning check-in — 8am weekdays
5. Workspace backup — every 6hrs
6. Google Calendar token refresh — every 55m

### Subagent / Session State
- **Active subagents:** 0
- **Current session:** `agent:main:cron:14e7493f-2d03-4515-803e-57be04c27e0b`
- **Recent cron runs (last hour):** Multiple — Fireflies Intel Collector, Rosie research, others

---

## 🚨 Security Findings

### CRITICAL

#### C1. Config Validation Failure → Best-Effort Runtime
**Finding:** `openclaw.json` fails validation on 8 plugin entries:
```
plugins.entries.minimax: plugin not found
plugins.entries.openai: plugin not found
plugins.entries.moonshot: plugin not found
plugins.entries.anthropic: plugin not found
plugins.allow: plugin not found (×4)
```
**Impact:** OpenClaw falls back to best-effort config. This means stated security policies (auth, sandbox, tool allowlists) may not be the ones actually loaded. The security audit itself ran against this degraded config and reported missing gateway auth, even though `gateway.auth.token` exists in the file.
**Mitigation:** Run `openclaw doctor --fix`. Likely the plugin packages were removed or not properly linked after a version update, but their config entries remain.

#### C2. Browser Control Auth Uncertainty
**Finding:** Security audit reports "Browser control has no auth" — but config shows `gateway.auth.token` is set.
**Impact:** SSRF or local-process exploitation of browser control endpoints is possible if the auth token is not actually being enforced due to config fallback.
**Mitigation:** Fix C1 first, then re-run `openclaw security audit --deep` to confirm auth is actually enforced.

### WARNING

#### W1. Reverse Proxy Headers Not Trusted
**Finding:** `gateway.trustedProxies` is empty. If Control UI is ever exposed through a reverse proxy, client IP/context will not be trusted.
**Impact:** Low currently (loopback-only), but a forward-compatibility risk.

#### W2. Extension Plugin Tools Under Permissive Policy
**Finding:** `lossless-claw` extension is enabled under `default` tool policy, which is permissive. The extension itself errors on load (`api.registerContextEngine is not a function`), but if partial loading occurs, tool access may be broader than intended.
**Impact:** Agents handling untrusted input could potentially reach extension tools.

#### W3. 167 Active Sessions
**Finding:** 167 sessions active across 7 agents. This is elevated for a 7-agent deployment.
**Impact:** Session accumulation increases token/context exposure surface. Old sessions may retain elevated tool access or sensitive context.
**Mitigation:** Review and prune old sessions. Consider session TTL policies.

#### W4. Rosie Cron Job in Error State
**Finding:** Rosie research cron reported ERROR on last run (per MEMORY.md).
**Impact:** Failed cron jobs can leave partial state, retry storms, or unhandled exceptions that leak into logs.
**Mitigation:** Investigate Rosie cron error logs.

### INFO

#### I1. Update Available
OpenClaw 2026.5.20 is available (released May 20). Current: 2026.4.23. The 2026.5.x line may include config validation fixes.

---

## 📊 Scoring Breakdown

| Domain | Weight | Raw | Weighted |
|--------|--------|-----|----------|
| Host Hardening | 20% | 90 | 18.0 |
| Network Exposure | 20% | 85 | 17.0 |
| Config Integrity | 25% | 35 | 8.75 |
| Auth & Access Control | 20% | 50 | 10.0 |
| Patch Currency & Maintenance | 15% | 90 | 13.5 |
| **TOTAL** | **100%** | — | **67.25** |

---

## 🎬 Recommended Actions (Priority Order)

1. **URGENT — Fix Config Validation**
   ```bash
   openclaw doctor --fix
   ```
   Then re-run `openclaw security audit --deep` to confirm findings resolve.

2. **HIGH — Update OpenClaw**
   ```bash
   openclaw update
   ```
   2026.5.20 may resolve plugin validation issues.

3. **HIGH — Investigate Rosie Cron Error**
   Check `openclaw logs` for Rosie cron failure details. Fix or disable until resolved.

4. **MEDIUM — Prune Old Sessions**
   Review 167 active sessions. Kill stale ones to reduce exposure surface.

5. **MEDIUM — Review lossless-claw Extension**
   Either fix the extension load error (PR #41090 compatibility) or remove it if not needed.

6. **LOW — Set trustedProxies if reverse proxy planned**
   ```json
   "gateway": { "trustedProxies": ["your-proxy-ip"] }
   ```

---

## 📝 Audit Trail

- **Assessment initiated:** 2026-05-23 08:43 AEST
- **Commands run:** `session_status`, `openclaw security audit --deep`, `openclaw update status`, `openclaw status --deep`, `openclaw cron list`, `lsof -nP -iTCP -sTCP:LISTEN`, `sw_vers`, `fdesetup status`, `socketfilterfw`, `subagents list`, `sessions_list`
- **Config inspected:** `~/.openclaw/openclaw.json`
- **Memory consulted:** `memory/2026-05-23.md`, `MEMORY.md`
- **Report written to:** `reports/hutcho-sentinel-weekly-2026-05-23.md`

---

*Assessment complete. Next recommended scan: 2026-05-30 or immediately after `openclaw doctor --fix` to verify band improvement.*
