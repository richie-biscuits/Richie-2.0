# Polynize Brain — Plan

## Project Goal
Extract and install cognition frameworks into AI agents.

## Research Notes — 2026-04-19
- [Agent Memory Landscape — awesome-ai-agents-2026]: New comprehensive curated list covers 10+ agent memory solutions, 20+ agent frameworks, 10+ protocols (MCP/A2A). Key finding: memory category is now distinct from frameworks — Mem0, Zep, Graphiti all listed separately. Polynize Brain's "framework installation" positioning fits between memory (layer) and frameworks (tools). (Source: github.com/Zijian-Ni/awesome-ai-agents-2026)
- [Agent Frameworks — LangChain Dominates, CrewAI Leads Multi-Agent]: LangChain leads ecosystem (90k+ GitHub stars), CrewAI leads multi-agent collaboration (20k+ stars). Both have mature memory systems. New entrant: Devstral 2 (Mistral, best open-source coding agent). Framework landscape confirms: no single winner, integration breadth matters. (Source: alphamatch.ai "Top 7 Agentic AI Frameworks 2026")
- [Model Context Windows Hit 1M Tokens]: GPT-5.4 (March 2026) and Claude Opus 4.6 (Feb 2026) both offer 1M token context. This raises the bar for what "memory" means — agents with 1M token windows don't need the same memory architecture as 128K-context models. Polynize Brain should consider: are we building for models that forget, or models that remember everything? (Source: awesome-ai-agents-2026)

## Research Notes — 2026-04-14
- [Memory Architecture]: Mem0 v2.0.0-beta.0/1 released (April 13-14) — major breaking changes: removed enable_graph/enableGraph deprecated params across all APIs. Python SDK v2.0.0b1 and Node SDK v3.0.0-beta.1 both pushed. Telemetry improvements across all tools. Graph memory remains on Pro tier ($249/mo). (Source: mem0ai/mem0 GitHub releases)
- [Skill Graph]: Mem0 Skill Graph now fully operational — Claude Code, Cursor, and Codex all have in-context mem0 knowledge via dedicated skills. Three skills: mem0 Core Skill (SDK reference), mem0-cli Skill (terminal reference), mem0-vercel-ai-sdk Skill (Vercel provider). This is the mechanism Polynize Brain should use for framework installation — install as a Skill, not MCP. (Source: docs.mem0.ai/changelog/highlights)
- [OpenClaw Plugin v1.0.6]: Released April 11 — telemetry hardening (persistent per-machine hash, $identify events, beforeExit flush). API calls now include source:"OPENCLAW" in all provider calls. Plugin is production-grade. Dream gate feature (automatic memory consolidation during idle periods) remains a key differentiator. (Source: mem0ai/mem0 GitHub releases)

## Research Notes — 2026-04-13
- [Memory Architecture]: Mem0 v1.0.0 just released — hybrid vector+graph+KV architecture, +26% accuracy vs OpenAI Memory on LOCOMO benchmark, 91% faster, 90% fewer tokens. Graph memory on Pro tier ($249/mo). Key insight: no temporal fact modeling — memories timestamped at creation but no validity windows. (Source: mem0ai/mem0 GitHub, Atlan comparison)
- [Temporal Memory]: Zep/Graphiti leads on temporal knowledge graph — stores facts with validity windows ("Kendra loves Adidas (as of March 2026)"). Scores 63.8% on LongMemEval vs Mem0's 49.0%. This temporal modeling gap is architecturally significant for cognition frameworks. (Source: Atlan.com benchmark comparison)
- [OpenClaw Plugin v1.0.4]: Mem0 OpenClaw plugin is now production-ready (v1.0.4). New features: Dream gate — automatic memory consolidation during idle periods; skills-based extraction with batched processing and domain-aware triage. Plugin went from v1.0.0 → v1.0.4 in one week. Polynize Brain could leverage Dream gate for automatic cognition framework consolidation. (Source: docs.mem0.ai/changelog/highlights, 2026-04-04)
- [Skill Graph Launch]: Mem0 launched "Skill Graph" for AI coding agents (Claude Code, Cursor, Codex) — in-context documentation directly inside agent workflows. Three skills: mem0 Core Skill, mem0-cli Skill, mem0-vercel-ai-sdk Skill. This is directly relevant to Polynize Brain's framework installation concept — Skills as the cognition installation mechanism. (Source: docs.mem0.ai/changelog/highlights, 2026-04-06)

## Research Notes — 2026-04-11
- [Agent Attribution]: Linux kernel now has official AI contributor guidance — uses "Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL1]" tags for AI contributions. First major open-source project to formalize AI agent attribution. This formalization could influence how agent cognition/framework attribution gets documented. (Source: torvalds/linux kernel docs)

## Research Notes — 2026-04-15
- [Claude Code Routines + Lock-in Backlash]: HN's #1 story (664 pts) — Anthropic's new "Routines" feature for structured agent procedures. Comments reveal major developer backlash: ToS changes blocking third-party CLI use, provider-specific memory that doesn't persist in git repos, forced subscription features. One commenter moved away from Claude Code entirely; another using stub MEMORY.md files for portability. Key signal: developers actively seeking escape routes from provider lock-in. Polynize Brain's open, portable cognition installation angle is increasingly timely. (Source: HN #47768133, April 15 2026)
- [Provider Diversification Trend]: Multiple HN comments recommend OpenCode + Claude models via GitHub/Bedrock as alternative to Claude Code lock-in. Also noted: Google Gemma 4 running natively on iPhone (105 pts) signals push toward on-device/portable AI. The market is fragmenting away from single-provider stacks — Polynize's multi-agent, portable cognition framework aligns with this direction. (Source: HN front page, April 15 2026)

## Research Notes — 2026-04-18
- [Cognitive Blueprint Pattern Validates Polynize Brain Architecture]: A March 2026 tutorial describes "CognitiveBlueprint" framework with identity, goals, constraints, tools, memory, planning, and validation components — all defined in YAML and loaded at runtime. Key insight: the blueprint IS the cognition installation artifact. This is exactly what Polynize Brain aims to do: define cognition frameworks as portable, installable artifacts. Blueprint portability is emerging as the core concept. (Source: marktechpost.com, March 7 2026)
- [Cognitive Blueprint — Architecture Components]: BlueprintMemory (type, window_size, summarize_after), BlueprintPlanning (strategy: sequential/hierarchical/reactive, max_steps, max_retries), BlueprintValidation (require_reasoning, min_response_length, forbidden_phrases). This component model maps directly to what Polynize Brain's framework extraction should produce. (Source: marktechpost.com, March 7 2026)

## Research Notes — 2026-04-17
- [Cognition Installation — Android Skills Validates SKILL.md Pattern]: Google just released official Android Skills for AI agents (github.com/google/android-studio-skills) — modular markdown (SKILL.md) instruction sets that trigger automatically when prompt matches skill metadata. This is direct validation of Polynize Brain's SKILL.md-based cognition framework installation concept from the largest tech company in the world. Skills are now being adopted by Google, Mem0, and the broader agent ecosystem. (Source: android-developers.googleblog.com, April 17 2026)
- [Codex Memory = Direct Competitor]: OpenAI's Codex now has memory that "allows re-using existing conversation threads, preserving context previously built up" and can "remember useful context from previous experience, including personal preferences, corrections and information that took time to gather." This is the same value proposition as Polynize Brain. Codex memory is now live for 3M+ users. Urgency for Polynize Brain to differentiate (portable, open, non-platform-locked) just increased. (Source: openai.com/codex, April 17 2026)

## Research Notes — 2026-04-16
- [Cognition Installation — Skills > MCP for Knowledge]: Deep comparison of 8 AI agent frameworks (Claude Agent SDK, OpenAI Agents SDK, Google ADK, LangGraph, CrewAI, Smolagents, Pydantic AI, AutoGen) confirms the MCP+Skills pattern — MCP for connectors, Skills for knowledge/context. The article specifically recommends Skills for teaching agents "gotchas and patterns discovered during sessions" — directly aligns with Polynize Brain's cognition framework installation concept. (Source: morphllm.com/ai/agent-framework)
- [Provider Lock-in Momentum]: Developer backlash to Claude Code Routines (HN #47768133, 664 pts) continues to build. "I want a commodity, not a platform" sentiment strengthens Polynize Brain's portable cognition installation positioning. The market is actively seeking escape routes from provider lock-in. (Source: HN, April 15-16 2026)

## Research Notes — 2026-04-20
- [OMEGA Memory — New Top Performer on LongMemEval]: OMEGA scores 95.4% on LongMemEval (highest published), with 25 MCP tools, zero external dependencies, SQLite + ONNX embeddings, AES-256 encryption, and "intelligent forgetting." This is a new entrant that Polynize Brain should evaluate — zero-dependency architecture is the opposite of Mem0's cloud-first approach. Local-first positioning aligns with "portable cognition." (Source: omegamax.co, April 2026)
- [MemoryLake — "Memory Passport for Agents"]: Emerging cross-agent memory infrastructure positions itself as platform-neutral, detaching agent memory from LLM providers/orchestration frameworks. Multimodal support (docs, images, audio). Strong enterprise governance (provenance, traceability, deletion controls). Directly competitive with Polynize Brain's portable cognition concept. (Source: powerdrill.ai, April 8 2026)
- [Memory Framework Benchmark Summary]: OMEGA 95.4% | Zep 63.8-71.2% | Mem0 49.0%. Mem0's self-editing model resolves conflicts on write without duplicates. Zep leads on temporal reasoning with validity windows. Both Mem0 Pro ($249/mo) and Zep Enterprise gate graph features. Self-hosting: Mem0 fully self-hostable (Apache 2.0); Zep requires Graphiti + Neo4j. (Source: Atlan, Vectorize, OMEGA comparisons)

## Research Notes — 2026-04-21
- [OMEGA vs Mem0 Full Comparison — April 2026]: OMEGA leads on benchmarks (95.4% LME, 25 MCP tools, zero deps) vs Mem0 (47.3K stars, no published LME score, cloud-first, $249/mo Pro). Key insight for Polynize Brain: OMEGA and Mem0 are solving the same problem (memory) with opposite architectures — local-first vs cloud-first. Polynize Brain's "cognition installation" is a different layer entirely. The memory wars are real, but Polynize is playing above them. (Source: omegamax.co/guides/best-ai-agent-memory-frameworks-2026, April 2026)
- [Memory Architecture Tier Guide — Solo/Startup/Enterprise]: Practical guide confirms three-tier architecture pattern: solo (Hmem/Engram, SQLite, $0), startup (Mem0 hybrid, SQLite+vector DB, $50-500/mo), enterprise (scope-chain, on-prem). Key insight: most indie projects don't need a vector database — SQLite+FTS5 handles <100K memories at sub-ms query speed. Polynize Brain framework extraction should target the solo→startup transition. (Source: shareuhack.com AI agent memory architecture guide, April 19 2026)
- [Web Search Still Blocked]: DuckDuckGo CAPTCHA blocking most queries (content, framework searches). Memory queries worked. Brave API key still needed. (Source: research cycle)

## Recent Activity
- 2026-04-21: Rosie — Cross-project research cycle (OMEGA vs Mem0 full comparison, memory architecture tier guide confirms SQLite-first for indie, web search still blocked)
- 2026-04-20: Rosie — Cross-project research cycle (OMEGA memory scores 95.4% LongMemEval — new top performer, MemoryLake emerges as cross-agent competitor)
- 2026-04-19: Rosie — Cross-project research cycle (awesome-ai-agents-2026 landscape map, model context hitting 1M tokens — memory architecture implications for Polynize Brain)
- 2026-04-18: Rosie — Cross-project research cycle (Cognitive Blueprint pattern validates Polynize Brain architecture — blueprint portability is emerging as key concept)
- 2026-04-17: Rosie — Cross-project research cycle (Google Android skills validates SKILL.md cognition installation pattern, Codex memory = direct competitor to Polynize Brain concept)
- 2026-04-16: Rosie — Cross-project research cycle (8-framework comparison validates Skills>MCP for cognition installation, lock-in backlash continues building)
- 2026-04-15: Rosie — Cross-project research cycle (Claude Code Routines launch + HN lock-in backlash signal, Mem0 v2.0.0-beta migration details)
- 2026-04-14: Rosie — Cross-project research cycle (Mem0 v2.0.0-beta, Skill Graph operational, OpenClaw plugin v1.0.6)
- 2026-04-13: Rosie — Cross-project research cycle (Mem0 OpenClaw plugin production-ready, Dream gate feature)

## Next Actions
- [ ] Evaluate OMEGA vs Mem0 — "OMEGA stores memory, Polynize installs cognition" is the differentiation angle (Rosie)
- [ ] Document the "memory vs cognition" positioning: OMEGA/Mem0/Zep store what happened, Polynize installs how to think (Rosie)
- [ ] Target the startup segment ($50-500/mo budget) with "missing cognition layer" positioning (Rosie)
- [ ] Document the MCP+Skills hybrid pattern for cognition installation (Rosie)
- [ ] Draft positioning statement leveraging "commodity not platform" developer sentiment (Rosie)
- [ ] Map Polynize Brain's framework installation approach to the "knowledge layer + connector layer" model
- [ ] Investigate Dream gate for automatic cognition framework consolidation (Rosie)
- [ ] Use Claude Code Routines backlash as positioning hook — market wants portable, non-locked-in cognition (Rosie)
- [ ] Analyze Codex memory (3M+ users) as direct competitor — Polynize Brain differentiation angle must sharpen NOW (Rosie)
- [ ] Evaluate Polynize Brain positioning against 1M-token context models — does "cognition framework" still matter when models have perfect recall? (Rosie)
- [ ] Evaluate Polynize Brain positioning against 1M-token context models — does "cognition framework" still matter when models have perfect recall? (Rosie)
- [ ] Align Polynize Brain output format with CognitiveBlueprint pattern — identity/goals/memory/planning/validation components (Rosie)

## Blockers
- None identified

## Research Notes — 2026-04-10
- [Cognition Transfer]: MCP preferred over Skills for service integration. Skills work for knowledge/context. Best approach: "knowledge layer on top of connector layer" — use MCP for actual service connections, Skills to teach gotchas and patterns discovered during sessions. (Source: david.coffee "I Still Prefer MCP Over Skills")
- [Cognition Patterns]: Research-driven agents (reading papers/studying forks before coding) find optimizations that code-only agents miss. The pattern of "discover gotchas, then package into a Skill" is directly applicable to cognition installation. (Source: blog.skypilot.co "Research-Driven Agents")

## Notes
- MCP = connectors (service interfaces)
- Skills = manuals (knowledge, context, gotchas)
- The optimal pattern: MCP handles connection, Skills capture learned patterns/gotchas
