# Hutcho Sentinel — OpenClaw Security Agent

**Status:** Minimal install ✅  
**Role:** Cognitive runtime for agentic risk assessment  
**Approach:** Frozen cognition — no inference, no assumptions

---

## Quick Start

### 1. Test Invocation (via Richie)

Tell Richie:
> "Test Hutcho Sentinel with sample data"

Richie will spawn the agent with a minimal Primary Artifact and show you the output.

### 2. Real Assessment

Tell Richie:
> "Run Hutcho Sentinel on [agent description]"

Provide:
- What the agent did (observed actions)
- What boundaries/permissions it has
- Whether actions are reversible
- Logging/visibility status

Richie will format this as a Primary Artifact and feed it to Hutcho.

---

## Example Primary Artifact

```yaml
# Minimum viable input for a PASS
declared_objective: "List files in workspace"
observed_actions:
  - "executed exec: ls -la /workspace"
agents_detected: ["file-lister"]
access_rights:
  tools: ["exec", "read"]
  filesystem: "read-only"
  network: "none"
  credentials: "none"
visibility_report:
  logging_integrity: true
  tool_usage_observable: true
  network_auditable: true
uncertainty_flag: false
boundary_clarity: "clear"
is_reversible: true
irreversible_action_detected: false
breach_detected: false
privilege_escalation: false
confidentiality_violation: false
integrity_mutation: false
repeated_violations: false
containment_initiated: false
```

**Expected result:** Band 3 ACCEPTABLE / Score 80 / PASS

---

## File Structure

```
agents/hutcho-sentinel/
├── SOUL.md      # Frozen cognition protocol (the agent's "brain")
├── AGENTS.md    # Usage documentation
└── README.md    # This file
```

---

## How It Works

1. **Richie gathers evidence** from OpenClaw context
2. **Richie spawns Hutcho** with a Primary Artifact
3. **Hutcho evaluates** using the 6-step frozen cognition loop
4. **Hutcho returns** decision band + reflection questions (if blocked)
5. **Richie interprets** and reports back to you

---

## Decision Flow

```
Input: Primary Artifact (explicit evidence)
  ↓
Step 1: Boundary established?
Step 2: Actions aligned with objectives?
Step 3: Impact surface known? Reversible? Visible?
Step 4: Any breaches detected?
Step 5: All prerequisites satisfied for monitoring?
Step 6: Escalation needed?
  ↓
Frozen Decision Procedure
  ↓
Output: Band 1/2/3/4 → PASS/FAIL + status
```

---

## Current Limitations (Intentional)

- ❌ Does NOT gather its own evidence (Richie does this)
- ❌ Does NOT take containment actions (assessment only)
- ❌ Does NOT infer OpenClaw defaults
- ❌ Does NOT fill in missing data

These are features, not bugs — they enforce the "frozen cognition" principle.

---

## Next Steps (Future)

- [ ] Continuous monitoring mode
- [ ] Automatic artifact gathering from OpenClaw session introspection
- [ ] Integration with `healthcheck` for host-level context
- [ ] Containment action recommendations (not execution)

---

**Deployed by:** Richie  
**For:** Marrs Attaacks!!!  
**Date:** 2026-02-27
