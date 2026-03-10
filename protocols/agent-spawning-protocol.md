# Agent Spawning Protocol v1.0

## Overview
A structured process for designing, building, and deploying autonomous AI agents. Extract expert intelligence and install it into deployable agent systems.

---

## The 6 Steps

### 1. PURPOSE
**What does this agent do?**

Define the single, clear job this agent performs.
- What problem does it solve?
- What outcome does it produce?
- What does "done" look like?

**Questions to answer:**
- What's the core function? (One sentence)
- Who benefits from this agent's work?
- How do we measure success?
- What's the scope? (What it does AND what it doesn't do)

**Example:**  
"Carol structures raw video transcripts into viral-ready content packages with narrative, hooks, and CTAs."

---

### 2. PROCESS
**What steps does the agent follow?**

Map the workflow from input to output.
- What triggers the agent?
- What decisions does it make?
- What are the step-by-step actions?
- What are the edge cases?

**Questions to answer:**
- What's the input format?
- What are the processing steps?
- What are the decision points?
- What's the output format?
- What happens when things go wrong?

**Example:**  
Carol's process: Receive transcript → Extract narrative arc → Generate 3 lesson hooks → Craft major insight → Write CTA → Return structured package

---

### 3. INTERFACE
**How do users interact with this agent?**

Design the touchpoints between human and agent.
- Where does the user give commands?
- Where does the agent deliver results?
- What does the interaction feel like?

**Options:**
- Telegram (chat-based, async)
- WhatsApp (chat-based, mobile-first)
- Email (formal, documented)
- Dashboard (visual, structured)
- Voice (hands-free, immediate)
- API (system-to-system)

**Questions to answer:**
- Where does the user already work?
- What's the natural interaction pattern?
- How urgent is the communication?
- What interface reduces friction?

**Example:**  
Carol lives in Telegram. User sends: "Carol, Day X idea: [raw thoughts]" → Carol returns structured package.

---

### 4. AGENT
**Who is this agent?**

Define personality, boundaries, and capabilities.
- What's their name?
- What's their voice/tone?
- What tools can they access?
- What are their constraints?

**Components:**
- **Name & Identity:** Who they are
- **Voice & Tone:** How they speak
- **Tools:** What they can do
- **Boundaries:** What they can't/won't do
- **Model:** What AI model powers them

**Example:**  
"Carol is a direct, no-BS video strategist. She challenges weak ideas. Uses Kimi K2.5. Has access to web search, file reading, and document creation."

---

### 5. COGNITION
**What intelligence does this agent need?**

Extract expert thinking and install it as structured protocols.
- What does an expert know that makes them good at this?
- How do they think through decisions?
- What frameworks do they use?

**Sources of cognition:**
- Expert interviews (extract thinking)
- Existing documentation (SOPs, playbooks)
- Pattern analysis (what works vs what doesn't)
- Iterative refinement (learn from feedback)

**Format:**
- Decision trees
- Rules and heuristics
- Examples and counter-examples
- Context triggers

**Example:**  
Hutcho Sentinel contains Simon's 25+ years of security thinking — frozen into assessment protocols.

---

### 6. INFRASTRUCTURE
**What does this agent need to run?**

Set up the physical or cloud environment.
- Where does the agent live?
- What are the compute requirements?
- How is it secured?
- What's the backup/continuity plan?

**Options:**
- Local machine (Mac Mini, PC)
- Cloud server (VPS, AWS, etc.)
- Hybrid (local + cloud sync)
- Containerized (Docker, etc.)

**Questions to answer:**
- Who has access?
- What's the security posture?
- What are the ongoing costs?
- How do we handle failures?
- What's the update process?

**Example:**  
Richie runs on local Mac Mini with OpenClaw gateway. Kimi via API. GitHub backup every 6 hours. Tailscale for remote access (planned).

---

## Using This Protocol

### To Spawn a New Agent:

1. **Work through all 6 steps in order**
2. **Document each step** (even if brief)
3. **Get explicit sign-off** before proceeding to next step
4. **Build iteratively** — start simple, add complexity only when needed
5. **Test before deploying** — validate the agent works as intended

### Template for Each Agent:

```markdown
# [Agent Name] — Spawn Document

## 1. Purpose
[Single sentence job description]

## 2. Process
[Step-by-step workflow]

## 3. Interface
[Where interactions happen]

## 4. Agent
- Name: 
- Voice: 
- Model: 
- Tools: 
- Boundaries: 

## 5. Cognition
[Expert thinking installed]

## 6. Infrastructure
- Location: 
- Security: 
- Backup: 
- Costs: 

## Status
- [ ] Purpose defined
- [ ] Process mapped
- [ ] Interface designed
- [ ] Agent configured
- [ ] Cognition installed
- [ ] Infrastructure deployed
- [ ] Tested and live
```

---

## Current Agents Using This Protocol

| Agent | Purpose | Status |
|-------|---------|--------|
| Richie | Coordinator, main interface | ✅ Live |
| Carol | Video structure | ✅ Live |
| Sammy | Sales outreach | 🔄 In training |
| Darren | Dev/coding | ✅ Live |
| DocBot | OpenClaw documentation | ✅ Live |
| Hutcho Sentinel | Security monitoring | ✅ Live |

---

*Version 1.0 — Created March 2026*
