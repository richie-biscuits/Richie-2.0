# Hutcho Sentinel — Weekly Security Assessment
**Date:** Saturday, May 30, 2026 — 08:43 AEST  
**Assessor:** Hutcho Sentinel (cron:14e7493f-2d03-4515-803e-57be04c27e0b)  
**Target:** OpenClaw deployment on Administrator’s Mac mini (macOS 26.3.1)  
**Protocol:** Frozen Cognition Protocol v1.0

---

## 🎯 Executive Summary

| Metric | Value |
|--------|-------|
| **Decision Band (Frozen)** | 🔴 **UNACCEPTABLE — MONITORING DENIED** |
| **Frozen Score** | **10 / 100** |
| **Practical Security Score** | **66 / 100** |
| **Critical Findings** | 2 |
| **Warnings** | 4 |
| **Info** | 1 |
| **Status** | **Operational but NO FIX APPLIED since last assessment.** Config drift persists; security guarantees remain degraded. |

**Bottom line:** The host is physically secure (FileVault ON, firewall active, loopback-only gateway), but OpenClaw’s configuration layer is still in a *thawed* state — the exact same validation errors from May 23 remain unpatched. Under the frozen cognition protocol, this boundary uncertainty blocks monitoring authorization. Practical posture is unchanged at ~66/100.

---

## 🧊 Frozen Cognition Protocol — Strict Evaluation

### STEP 1 — Boundary Establishment

| Field | Evidence | Value |
|-------|----------|-------|
| agents_detected | `openclaw status` | 7 configured, 138 active sessions |
| access_rights | Config + audit | Tools per agent policy; filesystem access per sandbox config |
| visibility_report | Audit runs, logs exist, port scan available | Partial — audit runs against degraded config |
| uncertainty_flag | `openclaw.json` fails validation on 8 plugin entries; best-effort runtime active | **TRUE** |
| boundary_clarity | Config fallback means stated policies may not match loaded policies | **DEGRADED** |
| risk_elevation_action | None explicitly called for | None |

### STEP 2 — Behavioural Alignment and Ambiguity

| Field | Evidence | Value |
|-------|----------|-------|
| declared objectives | Standard OpenClaw agent operation | Normal cron + chat operations |
| observed actions | Sessions active, cron jobs firing, channels healthy | Normal |
| explicit link | N/A | N/A |
| alignment_score | Not explicitly provided | **null** |
| ambiguity_level | Not explicitly stated | **NOT_YET_SPECIFIED** |
| aspect_requiring_assumption | Config validation failure means actual enforced policy is unknown vs stated | **["config_enforcement_uncertainty"]"** |
| irreversible_action_detected | None explicitly stated | **null** |

### STEP 3 — Impact Surface and Visibility Check

| Field | Evidence | Value |
|-------|----------|-------|
| domain_affected | Local macOS host | Host filesystem, local network |
| is_reversible | Not explicitly stated | **null** |
| logging_integrity | `openclaw logs`, audit output available | **true** |
| tool_usage_observable | `openclaw security audit` executes | **true** |
| network_auditable | `lsof` confirms listening ports | **true** |
| visibility_confidence | Degraded by config fallback — audit may not reflect actual runtime | **DEGRADED** |

### STEP 4 — Boundary Breach / Drift Classification

| Field | Evidence | Value |
|-------|----------|-------|
| breach_detected | No explicit evidence | **false** |
| privilege_escalation | No explicit evidence | **false** |
| confidentiality_violation | No explicit evidence | **false** |
| integrity_mutation | No explicit evidence | **false** |
| repeated_violations | Config issue persists 7+ days; this is drift, not a violation event | **false** |
| breach_type | None | None |
| breach_rationale | None | None |

### STEP 5 — Monitoring Mode Finalization (Authorization Gate)

| Prerequisite | Satisfied? | Rationale |
|--------------|------------|-----------|
| boundary uncertainty not flagged AND boundary clarity explicitly clear/high/complete | **NO** | uncertainty_flag = **TRUE**; boundary_clarity = **DEGRADED** |
| reversibility explicitly true | **NO** | is_reversible = **null** |
| logging_integrity == true AND tool_usage_observable == true AND network_auditable == true | **YES** | All three = **true** |
| no breach indicators are true | **YES** | All breach booleans = **false** |
| ambiguity/alignment prerequisites explicitly satisfied OR explicit monitoring allowed | **NO** | alignment_score null; ambiguity NOT_YET_SPECIFIED |

**monitoring_permitted = FALSE**

### STEP 6 — Human Escalation Package

**Trigger:** monitoring_permitted == false AND uncertainty_flag == true

**Incident Summary:**
- Config validation has been failing for at least 7 days (since May 23 assessment).
- `openclaw.json` references 4 missing plugin packages (minimax, openai, moonshot, anthropic) in both `plugins.entries` and `plugins.allow`.
- Runtime operates in best-effort fallback mode.
- Security audit reports missing gateway auth and missing browser control auth, despite `gateway.auth.token` being present in config file — likely because the degraded config loader does not enforce it.
- **No remediation was applied since the last assessment.**

**awaiting_confirmation:** TRUE — operator (Marrs) should approve `openclaw doctor --fix` and re-run assessment.

---

## 🧊 Frozen Decision Procedure Result

**Derived booleans:**
- Visibility_OK = **true** (all three visibility booleans true)
- Boundary_Clear = **false** (uncertainty_flag true)
- Assumption_Free_Alignment = **false** (aspect_requiring_assumption non-empty)
- Alignment_OK = **missing evidence** (no explicit score)
- Structural_Boundary_Crossed = **false** (no breach indicators true)
- Irreversible_Risk = **missing evidence** (no explicit irreversible flag, is_reversible null)

**Blocking conditions checked:**
1. Structural_Boundary_Crossed == true → **FALSE**
2. repeated_violations == true → **FALSE**
3. Visibility_OK == false → **FALSE**
4. Irreversible_Risk == true → **FALSE** (not explicitly true)
5. Boundary_Clear == false AND containment_initiated != true → **TRUE** ⚠️

**Decision:**
- **Band:** 🔴 **UNACCEPTABLE**
- **Score:** **10 / 100**
- **Status:** **FAILED**
- **Monitoring Authorization:** **DENIED**

---

## 🔍 System State Gathered

### Host Layer
- **OS:** macOS 26.3.1 (arm64) — Darwin 25.3.0, build 25D2128
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
  - `*:59869` — Logi Options+ (Logitech software)

### OpenClaw Runtime
- **Version:** 2026.4.23 (a979721)
- **Update status:** Available — 2026.5.27 published May 27
- **Gateway:** Local loopback (`ws://127.0.0.1:18789`), auth token present in config but audit reports "auth none"
- **Model auth:** Using legacy auth-profiles fallback (`runtime.modelAuth` unavailable)
- **Tailscale:** OFF
- **Agents:** 7 configured, 138 active sessions (down from 167 on May 23)
- **Heartbeat:** 30m for main; disabled for dash, harold, lorraine, rosie, sage, scarlett
- **Channels:** Telegram (6 bots), Slack (1 workspace) — all healthy
- **Extensions:** 1 installed — `lossless-claw` v0.3.0 (npm-installed, errors on load with `api.registerContextEngine is not a function`)

### Active Cron Jobs (from `openclaw cron list` — failed due to config errors, inferred from memory)
1. Fireflies Intel Collector — every 3hrs
2. Morning Briefing — 7:45am weekdays
3. Rosie research — 11:15pm nightly
4. Dash morning check-in — 8am weekdays
5. Workspace backup — every 6hrs
6. Google Calendar token refresh — every 55m
7. Hutcho Sentinel Weekly Security Assessment — Saturdays 8:43am

### Subagent / Session State
- **Active subagents:** 0
- **Current session:** `agent:main:cron:14e7493f-2d03-4515-803e-57be04c27e0b`
- **Recent cron runs (last hour):** Multiple — Fireflies, Rosie research, others

---

## 🚨 Security Findings

### CRITICAL

#### C1. Config Validation Failure → Best-Effort Runtime (UNPATCHED — 7+ DAYS)
**Finding:** `openclaw.json` fails validation on the same 8 plugin entries as May 23:
```
plugins.entries.minimax: plugin not found
plugins.entries.openai: plugin not found
plugins.entries.moonshot: plugin not found
plugins.entries.anthropic: plugin not found
plugins.allow: plugin not found (×4)
```
**Impact:** OpenClaw continues to run in best-effort config fallback. Stated security policies (auth, sandbox, tool allowlists) may not be the ones actually enforced. This is a **structural boundary uncertainty** that violates the frozen cognition protocol.
**Mitigation:** Run `openclaw doctor --fix`. This was recommended on May 23 and remains unactioned.

#### C2. Browser Control Auth Uncertainty (UNPATCHED)
**Finding:** Security audit reports "Browser control has no auth" — config shows `gateway.auth.token` is set, but due to best-effort fallback, enforcement is uncertain.
**Impact:** SSRF or local-process exploitation of browser control endpoints is possible if auth is not actually being enforced.
**Mitigation:** Fix C1 first, then re-run `openclaw security audit --deep` to confirm auth enforcement.

### WARNING

#### W1. Reverse Proxy Headers Not Trusted
**Finding:** `gateway.trustedProxies` is empty. If Control UI is ever exposed through a reverse proxy, client IP/context will not be trusted.
**Impact:** Low currently (loopback-only), but a forward-compatibility risk.

#### W2. Extension Plugin Tools Under Permissive Policy
**Finding:** `lossless-claw` extension is enabled under `default` tool policy, which is permissive. The extension itself errors on load, but if partial loading occurs, tool access may be broader than intended.
**Impact:** Agents handling untrusted input could potentially reach extension tools.

#### W3. 138 Active Sessions
**Finding:** 138 sessions active across 7 agents. Down from 167 (improvement), but still elevated.
**Impact:** Session accumulation increases token/context exposure surface.
**Mitigation:** Continue pruning old/stale sessions.

#### W4. OpenClaw 5+ Weeks Behind Latest Stable
**Finding:** Current 2026.4.23; latest is 2026.5.27 (released May 27). The 2026.5.x line likely includes config validation fixes.
**Impact:** Missing potential security and stability patches.
**Mitigation:** `openclaw update`

### INFO

#### I1. Session Count Reduced
Active sessions decreased from 167 (May 23) to 138 (May 30), a ~17% reduction. No explicit pruning action was recorded; natural expiration.

---

## 📊 Practical Scoring Breakdown (Non-Frozen)

| Domain | Weight | Raw | Weighted |
|--------|--------|-----|----------|
| Host Hardening | 20% | 90 | 18.0 |
| Network Exposure | 20% | 85 | 17.0 |
| Config Integrity | 25% | 35 | 8.75 |
| Auth & Access Control | 20% | 50 | 10.0 |
| Patch Currency & Maintenance | 15% | 85 | 12.75 |
| **TOTAL** | **100%** | — | **66.5** |

---

## 🎬 Recommended Actions (Priority Order)

1. **URGENT — Fix Config Validation (SAME AS MAY 23)**
   ```bash
   openclaw doctor --fix
   ```
   Then re-run `openclaw security audit --deep` to confirm findings resolve. This has been pending for 7+ days.

2. **HIGH — Update OpenClaw**
   ```bash
   openclaw update
   ```
   2026.5.27 may resolve plugin validation issues.

3. **MEDIUM — Continue Pruning Old Sessions**
   Review 138 active sessions. Kill stale ones to reduce exposure surface.

4. **MEDIUM — Review lossless-claw Extension**
   Either fix the extension load error (PR #41090 compatibility) or remove it if not needed.

5. **LOW — Set trustedProxies if reverse proxy planned**
   ```json
   "gateway": { "trustedProxies": ["your-proxy-ip"] }
   ```

---

## 📝 Audit Trail

- **Assessment initiated:** 2026-05-30 08:43 AEST
- **Commands run:** `session_status`, `openclaw status --deep`, `openclaw security audit --deep`, `openclaw update status`, `openclaw cron list`, `openclaw agents list`, `lsof -nP -iTCP -sTCP:LISTEN`, `sw_vers`, `fdesetup status`, `socketfilterfw`
- **Config inspected:** `~/.openclaw/openclaw.json`
- **Memory consulted:** `memory/2026-05-23.md`, `reports/hutcho-sentinel-weekly-2026-05-23.md`
- **Report written to:** `reports/hutcho-sentinel-weekly-2026-05-30.md`

---

*Assessment complete. Next recommended scan: 2026-06-06 or immediately after `openclaw doctor --fix` to verify band improvement.*
