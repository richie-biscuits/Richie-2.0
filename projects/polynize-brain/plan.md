# Polynize Brain - Plan

## Project Goal
Extract and install cognition frameworks into AI agents.

## Research Notes — 2026-05-17

- [Cognition Governance]: Enterprise agent governance frameworks now define 5-tier authorization model (Tier 0 Observe → Tier 4 Autonomous) — agents start at Tier 1, promote after <2% error rate for 30 days, demote on safety incidents — Thinking Inc analysis
- [Cognition Governance]: Action boundary specifications critical — allowlists preferred over blocklists, programmatic enforcement layer required (34% of incidents occur with prompt-only boundaries) — BCG 2025 analysis
- [Cognition Governance]: Escalation rules now standard — mandatory triggers include financial thresholds, external stakeholder impact, confidence below threshold, PII encounters — audit trails required for regulatory compliance

## Research Notes — 2026-05-15

- [Cognition Frameworks]: LangGraph leads production deployments (Klarna, LinkedIn, Uber) with 90k+ GitHub stars — stateful workflows, explicit control flow, time-travel debugging, lowest $/task (~$0.04) — ExamCert.ai analysis
- [Cognition Frameworks]: CrewAI optimized for role-based multi-agent orchestration (28k stars) — ships with strong prompts, 30-50% token overhead vs hand-tuned but faster prototype velocity — ExamCert.ai analysis
- [Cognition Frameworks]: AutoGen 0.5+ rebuilt with event-driven runtime in 2025 — best for conversational agents and code execution, but multi-turn inflates costs (~$0.09/task) — ExamCert.ai analysis
- [Cognition Frameworks]: Debuggability is #1 reason teams switch frameworks in year 2 — LangGraph wins on incident postmortems with inspectable state, LangSmith traces, time-travel replay — ExamCert.ai analysis

## Research Notes — 2026-05-08

Latest research findings go here.

## Research Notes — 2026-04-19
- [Agent Memory Landscape - awesome-ai-agents-2026]: New comprehensive curated list covers 10+ agent memory solutions, 20+ agent frameworks, 10+ protocols (MCP/A2A). Key finding: memory category is now distinct from frameworks - Mem0, Zep, Graphiti all listed separately. Polynize Brain's "framework installation" positioning fits between memory (layer) and frameworks (tools). (Source: github.com/Zijian-Ni/awesome-ai-agents-2026)
- [Agent Frameworks - LangChain Dominates, CrewAI Leads Multi-Agent]: LangChain leads ecosystem (90k+ GitHub stars), CrewAI leads multi-agent collaboration (20k+ stars). Both have mature memory systems. New entrant: Devstral 2 (Mistral, best open-source coding agent). Framework landscape confirms: no single winner, integration breadth matters. (Source: alphamatch.ai "Top 7 Agentic AI Frameworks 2026")
- [Model Context Windows Hit 1M Tokens]: GPT-5.4 (March 2026) and Claude Opus 4.6 (Feb 2026) both offer 1M token context. This raises the bar for what "memory" means - agents with 1M token windows don't need the same memory architecture as 128K-context models. Polynize Brain should consider: are we building for models that forget, or models that remember everything? (Source: awesome-ai-agents-2026)

## Research Notes — 2026-04-14
- [Memory Architecture]: Mem0 v2.0.0-beta.0/1 released (April 13-14) - major breaking changes: removed enable_graph/enableGraph deprecated params across all APIs. Python SDK v2.0.0b1 and Node SDK v3.0.0-beta.1 both pushed. Telemetry improvements across all tools. Graph memory remains on Pro tier ($249/mo). (Source: mem0ai/mem0 GitHub releases)
- [Skill Graph]: Mem0 Skill Graph now fully operational - Claude Code, Cursor, and Codex all have in-context mem0 knowledge via dedicated skills. Three skills: mem0 Core Skill (SDK reference), mem0-cli Skill (terminal reference), mem0-vercel-ai-sdk Skill (Vercel provider). This is the mechanism Polynize Brain should use for framework installation - install as a Skill, not MCP. (Source: docs.mem0.ai/changelog/highlights)
- [OpenClaw Plugin v1.0.6]: Released April 11 - telemetry hardening (persistent per-machine hash, $identify events, beforeExit flush). API calls now include source:"OPENCLAW" in all provider calls. Plugin is production-grade. Dream gate feature (automatic memory consolidation during idle periods) remains a key differentiator. (Source: mem0ai/mem0 GitHub releases)

## Research Notes — 2026-04-13
- [Memory Architecture]: Mem0 v1.0.0 just released - hybrid vector+graph+KV architecture, +26% accuracy vs OpenAI Memory on LOCOMO benchmark, 91% faster, 90% fewer tokens. Graph memory on Pro tier ($249/mo). Key insight: no temporal fact modeling - memories timestamped at creation but no validity windows. (Source: mem0ai/mem0 GitHub, Atlan comparison)
- [Temporal Memory]: Zep/Graphiti leads on temporal knowledge graph - stores facts with validity windows ("Kendra loves Adidas (as of March 2026)"). Scores 63.8% on LongMemEval vs Mem0's 49.0%. This temporal modeling gap is architecturally significant for cognition frameworks. (Source: Atlan.com benchmark comparison)
- [OpenClaw Plugin v1.0.4]: Mem0 OpenClaw plugin is now production-ready (v1.0.4). New features: Dream gate - automatic memory consolidation during idle periods; skills-based extraction with batched processing and domain-aware triage. Plugin went from v1.0.0 → v1.0.4 in one week. Polynize Brain could leverage Dream gate for automatic cognition framework consolidation. (Source: docs.mem0.ai/changelog/highlights, 2026-04-04)
- [Skill Graph Launch]: Mem0 launched "Skill Graph" for AI coding agents (Claude Code, Cursor, Codex) - in-context documentation directly inside agent workflows. Three skills: mem0 Core Skill, mem0-cli Skill, mem0-vercel-ai-sdk Skill. This is directly relevant to Polynize Brain's framework installation concept - Skills as the cognition installation mechanism. (Source: docs.mem0.ai/changelog/highlights, 2026-04-06)

## Research Notes — 2026-04-11
- [Agent Attribution]: Linux kernel now has official AI contributor guidance - uses "Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL1]" tags for AI contributions. First major open-source project to formalize AI agent attribution. This formalization could influence how agent cognition/framework attribution gets documented. (Source: torvalds/linux kernel docs)

## Research Notes — 2026-04-15
- [Claude Code Routines + Lock-in Backlash]: HN's #1 story (664 pts) - Anthropic's new "Routines" feature for structured agent procedures. Comments reveal major developer backlash: ToS changes blocking third-party CLI use, provider-specific memory that doesn't persist in git repos, forced subscription features. One commenter moved away from Claude Code entirely; another using stub MEMORY.md files for portability. Key signal: developers actively seeking escape routes from provider lock-in. Polynize Brain's open, portable cognition installation angle is increasingly timely. (Source: HN #47768133, April 15 2026)
- [Provider Diversification Trend]: Multiple HN comments recommend OpenCode + Claude models via GitHub/Bedrock as alternative to Claude Code lock-in. Also noted: Google Gemma 4 running natively on iPhone (105 pts) signals push toward on-device/portable AI. The market is fragmenting away from single-provider stacks - Polynize's multi-agent, portable cognition framework aligns with this direction. (Source: HN front page, April 15 2026)

## Research Notes — 2026-04-18
- [Cognitive Blueprint Pattern Validates Polynize Brain Architecture]: A March 2026 tutorial describes "CognitiveBlueprint" framework with identity, goals, constraints, tools, memory, planning, and validation components - all defined in YAML and loaded at runtime. Key insight: the blueprint IS the cognition installation artifact. This is exactly what Polynize Brain aims to do: define cognition frameworks as portable, installable artifacts. Blueprint portability is emerging as the core concept. (Source: marktechpost.com, March 7 2026)
- [Cognitive Blueprint - Architecture Components]: BlueprintMemory (type, window_size, summarize_after), BlueprintPlanning (strategy: sequential/hierarchical/reactive, max_steps, max_retries), BlueprintValidation (require_reasoning, min_response_length, forbidden_phrases). This component model maps directly to what Polynize Brain's framework extraction should produce. (Source: marktechpost.com, March 7 2026)

## Research Notes — 2026-04-17
- [Cognition Installation - Android Skills Validates SKILL.md Pattern]: Google just released official Android Skills for AI agents (github.com/google/android-studio-skills) - modular markdown (SKILL.md) instruction sets that trigger automatically when prompt matches skill metadata. This is direct validation of Polynize Brain's SKILL.md-based cognition framework installation concept from the largest tech company in the world. Skills are now being adopted by Google, Mem0, and the broader agent ecosystem. (Source: android-developers.googleblog.com, April 17 2026)
- [Codex Memory = Direct Competitor]: OpenAI's Codex now has memory that "allows re-using existing conversation threads, preserving context previously built up" and can "remember useful context from previous experience, including personal preferences, corrections and information that took time to gather." This is the same value proposition as Polynize Brain. Codex memory is now live for 3M+ users. Urgency for Polynize Brain to differentiate (portable, open, non-platform-locked) just increased. (Source: openai.com/codex, April 17 2026)

## Research Notes — 2026-04-16
- [Cognition Installation - Skills > MCP for Knowledge]: Deep comparison of 8 AI agent frameworks (Claude Agent SDK, OpenAI Agents SDK, Google ADK, LangGraph, CrewAI, Smolagents, Pydantic AI, AutoGen) confirms the MCP+Skills pattern - MCP for connectors, Skills for knowledge/context. The article specifically recommends Skills for teaching agents "gotchas and patterns discovered during sessions" - directly aligns with Polynize Brain's cognition framework installation concept. (Source: morphllm.com/ai/agent-framework)
- [Provider Lock-in Momentum]: Developer backlash to Claude Code Routines (HN #47768133, 664 pts) continues to build. "I want a commodity, not a platform" sentiment strengthens Polynize Brain's portable cognition installation positioning. The market is actively seeking escape routes from provider lock-in. (Source: HN, April 15-16 2026)

## Research Notes — 2026-04-23
- [Persona Protocol - 7-Layer Cognitive Identity Architecture]: New framework (personaprotocol.ai) defines PAC2 - Personalized Augmented Collaborators with Context. Seven distinct cognitive identity layers define how AI characters think, change, and maintain continuity. Directly competitive with Polynize Brain's cognition installation concept - same problem space, different terminology. Key signal: the identity/persona layer is becoming its own architectural category. (Source: personaprotocol.ai)
- [Nuwa Skill - AI Persona Distillation Framework]: PyShine published Zhang Xuefeng Skill (April 20) using Nuwa framework to distill public figures into installable AI personas with mental models, decision heuristics, and expression DNA - turning thinking into a runnable cognitive operating system. This is EXACTLY the Polynize Brain concept in market right now. Nuwa's "cognitive operating system" phrasing is a strong positioning match. (Source: pyshine.com/blog/2026/04/20/Zhang-Xuefeng-Skill-AI-Persona-Distillation/)
- [RASA - Persona-Driven YAML Agent Framework]: New open-source Python framework (github.com/vedanta/rasa) for persona-driven, memory-aware AI agents with declarative YAML configuration. Define personality, multi-layered memory, domain-specific reasoning. Accessible via API, CLI, or Python. This is the same "cognition as YAML artifact" concept Polynize Brain is building - independent validation of the architecture. (Source: github.com/vedanta/rasa)
- [Persona Cognitive Architecture - Three Memory Types + Cognitive Cycle]: DeepWiki article on persona cognitive architecture (crcresearch/agentic_collab) describes three memory types + four-stage cognitive cycle. Each persona operates autonomously on this architecture. Could serve as reference architecture for Polynize Brain's framework extraction output format. (Source: deepwiki.com/crcresearch/agentic_collab/2.2-persona-cognitive-architecture)

## Research Notes — 2026-04-22
- [Hermes Agent v0.10 - 103K Stars, Self-Improving, 118 Skills]: Nous Research released Hermes Agent v0.10 on April 16, 2026. In 7 weeks it passed 103K GitHub stars (faster than LangChain + AutoGen combined). Key differentiator: GEPA (Genetic-Pareto) self-improvement - agents with 20+ self-generated skills are 40% faster on repeated tasks. MIT license, 15+ LLM providers, runs on $5/mo VPS. Polynize Brain positioning: Hermes generates skills from experience, Polynize INSTALLS structured cognition frameworks (persona, goals, validation logic) - different layers. (Source: innobu.com, April 2026)
- [OpenClaw 9 CVEs, Hermes Zero - Security Gap]: OpenClaw had 9 CVEs in March 2026 including CVE-2026-25253 (CVSS 8.8), plus ClawHavoc with 341 malicious skills. Hermes Agent has zero known CVEs. This security gap is documented - relevant for Polynize Brain's OpenClaw-based architecture. (Source: innobu.com, April 2026)
- [Claude Code 30+ Releases, Anthropic Managed Agent Cloud]: Claude Code shipped 30+ updates in 5 weeks (rendering cycles, enterprise cloud, Linux process isolation). Anthropic launched managed agent cloud service. OpenClaw released "Dreaming" version (advanced memory + security hardening). Agent infrastructure race accelerating. (Source: af.net, April 15 2026)

## Research Notes — 2026-04-20
- [OpenAI Codex - GitHub Repository Context Now Default]: Codex now automatically includes GitHub repository context by default (opt-out in Personal Settings → GitHub → "Include GitHub repository context"). This is a major change - Codex is now "aware" of your entire codebase when you chat with it. For cognition framework extraction, this means Codex can read SOUL.md, USER.md, TOOLS.md, SKILL.md files automatically and apply that context. Major upgrade to extraction quality. (Source: help.github.com/en/copilot/customizing-copilot/copilot-code-review)
- [Skill Framework Standardization Update]: SKILL.md format now supported by: Mem0 (Skill Graph), Google (Android Studio Skills), OpenClaw (ClawHub), Hermes (skills/ folder). The standard is converging: YAML frontmatter with metadata, markdown body with instructions/examples, optional attachments/ folder. Polynize Brain should adopt this exact format for cognition framework artifacts. (Source: multiple project docs, April 20 2026)

## Research Notes — 2026-05-18

- [Production Agent Patterns]: Frameworks have consolidated around 3 winners: LangGraph (stateful workflows), AutoGen (multi-agent conversation), CrewAI (role-based crews) — 68% of new agent projects in 2025 used a framework rather than raw SDK calls — Forde Studios analysis
- [Production Failure Modes]: 4 patterns break agents in production: (1) tool output schema drift, (2) context window exhaustion, (3) cost runaway without circuit breakers, (4) non-deterministic replay — none are framework bugs, they're integration failures — Forde Studios
- [Cognition Transfer Insight]: Teams that operate agents reliably treat workflows like distributed systems — retries with backoff, timeouts, fallback paths, dead-letter queues for failed runs — the framework is not the hard part, production resilience is
- [Skill Installation > Framework]: LlamaIndex evolved to dominate the retrieval layer, not orchestration — the pattern is emerging: separate knowledge/cognition (Skills) from orchestration (frameworks) — aligns with Polynize Brain's SKILL.md approach

## Research Notes — 2026-05-20

- [Market Size — Agent Memory Now $52B Category]: AI agent memory market: $7.84B (2025) → $52.62B by 2030 (46.3% CAGR). 88% of organizations use AI in at least one function, but only 6% qualify as "AI high performers" (>5% EBIT from AI). The gap = agents that don't retain what they learn — Vektor Memory analysis
- [Memory Architecture — Four Dimensions]: Complete memory systems must handle: (1) Storage — where memories live, (2) Curation — contradiction/duplicate handling, (3) Retrieval — multi-strategy search, (4) Lifecycle — consolidation/promotion/retirement. No single approach solves all four — this is the architectural opportunity space
- [Production Reality — Full Context Unusable]: Full-context memory (dumping entire history) delivers highest accuracy ceiling BUT 9.87s median latency, 17.12s p95, ~26k tokens/conv. "Categorically unusable in production" — selective memory is the only viable path for real deployments
- [Benchmark Leadership — Mem0 New Algorithm]: Mem0's April 2026 token-efficient algorithm: 92.5 LoCoMo, 94.4 LongMemEval, ~6,900 tokens/query. Biggest gains: +29.6 points temporal reasoning, +23.1 multi-hop. Driven by single-pass ADD-only extraction + multi-signal retrieval — Mem0 ECAI 2025 + 2026 update
- [Integration Breadth — 21 Frameworks]: Memory layer that locks to one framework won't scale. Current coverage: LangChain, LangGraph, LlamaIndex, CrewAI, AutoGen, Agno, CAMEL AI, Dify, Flowise, Google ADK, OpenAI Agents SDK, Mastra (TypeScript), plus voice agents (ElevenLabs, LiveKit, Pipecat) — Mem0 docs

## Blockers
- None

## Next Actions

### Immediate (This Week)
1. **Update Polynize positioning** — Shift from "external team" to "cognition direction" (Marrs)
2. **Task cost data** — Add per-task execution costs to client proposals (Dash)
3. **Framework selection guidance** — Create decision matrix for clients: LangGraph (control flow), CrewAI (role-based), AutoGen (conversational) — based on Rosie research
4. **Governance layer design** — Add 5-tier authorization model to cognition framework spec (Rosie research → Marrs)
5. **Production resilience messaging** — Update sales materials to emphasize distributed systems reliability over framework features (Rosie research → Marrs)
6. **Market sizing narrative** — Incorporate $52B memory market growth into investor/pitch materials (Rosie research → Marrs)
7. **Four dimensions framework** — Build cognition extraction around Storage/Curation/Retrieval/Lifecycle model (Rosie research → Marrs/Julian)

### Short Term (Next 2 Weeks)
1. **Framework extraction v2** — Implement enhanced extraction with SOUL.md format
2. **Install mechanism** — Build SKILL.md installer
3. **Validation system** — Add framework verification post-install
4. **Cognition framework failure modes** — Document 4 production failure patterns (schema drift, context exhaustion, cost runaway, non-determinism) as part of framework extraction (Rosie → Marrs)

## Research Notes — 2026-05-19

- [Memory Architecture — Institutional vs Personalization Split]: The agent memory landscape is bifurcating into two distinct categories: (1) Personalization memory (conversation history, user preferences) and (2) Institutional knowledge (extracted, structured understanding that compounds over time). Most frameworks handle personalization well; institutional memory is the harder problem and the differentiation opportunity. Frameworks like Hindsight are emerging specifically for institutional knowledge capture — turning raw interaction history into structured, actionable domain knowledge — Vectorize analysis
- [Memory Retrieval — Multi-Strategy Required]: Vector-only retrieval fails on terminology mismatches (e.g., "template" vs "format"). Production memory systems need multi-strategy retrieval: vector similarity + entity-aware graph + keyword index. If retrieval misses facts, summarization has nothing to work with — retrieval architecture, not post-processing, determines effectiveness — Vectorize analysis
- [Cognition Transfer — The Amnesia Problem]: Most AI agents have no persistent memory — every session starts from scratch. The real value of cognition frameworks is preventing institutional knowledge loss: a procurement agent shouldn't repeat the same mistakes and require the same corrections every session. This is the core problem Polynize Brain solves — Vectorize analysis

## Recent Activity

- 2026-05-20: Rosie added market sizing research — $7.84B → $52.62B by 2030, four memory dimensions framework, full-context latency unsuitable for production, Mem0 benchmark leadership data — Vektor Memory + Mem0 analysis
- 2026-05-19: Rosie added memory architecture bifurcation research — institutional vs personalization memory split, multi-strategy retrieval requirement, institutional knowledge as core value prop — Vectorize analysis
- 2026-05-18: Rosie added production agent pattern research — 3 framework winners consolidated, 4 production failure modes identified, cognition transfer = distributed systems thinking — Forde Studios analysis
- 2026-05-17: Rosie added enterprise governance framework research — 5-tier authorization model, action boundaries, escalation rules — cognition installation must include governance layer
- 2026-05-15: Rosie added framework comparison research — LangGraph, CrewAI, AutoGen production patterns and costs
- 2026-05-08: Rosie completed framework extraction phase 1 (20 frameworks → 6 high-priority)
- 2026-05-05: Initial memory schema drafted and committed
