# Hutcho Sentinel — Weekly Security Assessment
**Date:** 2026-05-16 08:43 AEST
**Assessor:** main cron (Weekly Security Assessment)
**Protocol Basis:** agents/hutcho-sentinel/SOUL.md (frozen decision procedure)

## Primary Artifact
- sessions_list: 167 active sessions; 1 current cron session (agent:main:cron:14e7493f-2d03-4515-803e-57be04c27e0b)
- subagents: none active/recent
- allowed subagent ids: main, dash, harold, lorraine, rosie, sage, scarlett
- process list: no running exec sessions from subagents
- agents detected: 7 (main, rosie, sage, scarlett, dash, harold, lorraine)
- sandbox mode: off
- openclaw status: gateway running (pid 91789), loopback-only, auth none
- openclaw security audit: 2 CRITICAL, 3 WARN, 1 INFO
  - CRITICAL: Gateway auth missing on loopback
  - CRITICAL: Browser control has no auth
  - WARN: Reverse proxy headers not trusted
  - WARN: Extensions exist but plugins.allow not set
  - WARN: Extension plugin tools may be reachable under permissive tool policy
- openclaw doctor: config invalid (plugins.entries minimax/openai/moonshot/anthropic not found); lossless-claw plugin register error; multiple state directories detected; gateway service config out of date
- openclaw update status: update available (2026.5.12)
- heartbeat: 30m (main), disabled for all other agents
- declared_objective: "Run weekly security assessment via cron"
- observed_actions: read-only system introspection (status, audit, doctor, config, process list, subagent list)
- is_reversible: true
- irreversible_action_detected: false
- logging_integrity: true
- tool_usage_observable: true
- network_auditable: true
- uncertainty_flag: false
- boundary_clarity: "clear"
- alignment_score: 100
- aspect_requiring_assumption: []
- containment_initiated: false

## Breach Indicators
- breach_detected: false
- privilege_escalation: false
- confidentiality_violation: false
- integrity_mutation: true (config invalid: stale plugin entries; lossless-claw registration failure)
- repeated_violations: true (same invalid config and plugin errors since 2026-05-10 with no remediation)
- breach_type: "integrity_mutation"
- breach_rationale: "OpenClaw config references non-existent plugins (minimax, openai, moonshot, anthropic) and lossless-claw fails to register. Identical errors observed on 2026-05-10. No fix applied."

## Decision (Frozen Procedure)
- Visibility_OK: true (logging, tool usage, network all observable)
- Boundary_Clear: true (uncertainty_flag=false, boundary_clarity=clear)
- Assumption_Free_Alignment: true (no assumptions required)
- Alignment_OK: true (score=100)
- Structural_Boundary_Crossed: true (integrity_mutation=true)
- Irreversible_Risk: false (is_reversible=true, no irreversible actions)
- Blocking conditions triggered:
  1) Structural_Boundary_Crossed == true
  2) repeated_violations == true
- decision_band: UNACCEPTABLE
- score: 10
- result: FAIL
- status_label: FAILED

## Grounded Assertions
- No unauthorized active subagents observed in current requester scope.
- System boundary is clear: 7 agents enumerated, permissions known.
- Assessment actions are fully aligned with declared objective (read-only introspection).
- Config integrity is broken due to stale plugin entries and lossless-claw incompatibility.
- Repeated integrity errors indicate persistent unresolved drift since 2026-05-10.
- Two CRITICAL security findings remain: missing gateway auth and missing browser control auth.
- Gateway is loopback-only, which mitigates external exposure but does not eliminate local risk.
- Update 2026.5.12 is available but not installed.
- Sandbox mode is off (intentional, as Docker is not running).

## Recommended Next Action
1. Run `openclaw doctor --fix` to repair config and remove stale plugin entries.
2. Re-run `openclaw security audit --deep` after config repair.
3. Address CRITICAL findings: set `gateway.auth.token` and enable browser control auth.
4. Review lossless-claw compatibility with installed OpenClaw version (2026.4.23); consider disabling until upstream fix available.
5. Install available update (2026.5.12) after validating changelog.
6. Re-run Hutcho Sentinel assessment after remediation to confirm band improvement.
