# PAM Build — Plan

## Project Goal
Research agent build patterns and tools.

## Research Notes — 2026-04-19
- [Agent Framework Landscape — 2026 State of Play]: awesome-ai-agents-2026 lists 20+ agent frameworks, 10+ agent memory solutions, 10+ agent protocols. LangChain (90k+ stars) dominates ecosystem, CrewAI (20k+ stars) leads multi-agent. Notable new entrant: Devstral 2 (Mistral's open-source coding agent). Key insight: frameworks are fragmenting, memory is consolidating as its own category — PAM should build to this landscape. (Source: github.com/Zijian-Ni/awesome-ai-agents-2026)
- [Model Context Reaching 1M Tokens]: GPT-5.4 (March 2026) and Claude Opus 4.6 (Feb 2026) both support 1M token context windows. This changes the latency/cost calculus for memory architecture — full context is now viable for some use cases. PAM should benchmark against this new baseline: is selective memory still worth the engineering complexity when full context is cheap? (Source: awesome-ai-agents-2026)

## Research Notes — 2026-04-14
- [Mem0 v2.0.0-beta]: Python SDK v2.0.0b0 (April 13) + v2.0.0b1 (April 14) — major breaking changes: removed enable_graph parameter, deprecated params stripped across LLMs/embeddings/vector stores/graphs. LLM-hallucinated ID crashes fixed (was issue #3931). Azure OpenAI structured output support added. DeepSeek LLM provider added to Node SDK. If building PAM against Mem0, expect migration work. (Source: mem0ai/mem0 GitHub releases)
- [LOCOMO Full Data]: Full-context: 72.9% accuracy but 9.87s median latency, ~26k tokens/conv. Mem0g: 68.4% at 1.09s. Mem0: 66.9% at 0.71s. P95 latency: Mem0g 1.44s vs full-context 17.12s. Key lesson: accuracy ceiling comes with categorical latency cost. PAM memory architecture should target ~1s median, <2s p95 as production baseline. (Source: mem0.ai/blog/state-of-ai-agent-memory-2026)
- [13-Framework Integration]: Mem0 now integrates with 13 frameworks: LangChain, LangGraph, LlamaIndex, CrewAI, AutoGen, Agno, CAMEL AI, Dify, Flowise, Google ADK, OpenAI Agents SDK, Mastra. No single winner yet — integration breadth matters more than depth for PAM tool selection. (Source: mem0.ai/blog/state-of-ai-agent-memory-2026)

## Research Notes — 2026-04-13
- [Mem0 v1.0.0]: Major release with API modernization, improved vector store support, GCP integration. Mem0 claims +26% accuracy vs OpenAI Memory on LOCOMO benchmark, 91% faster responses, 90% lower token usage. Graph memory still paywalled on Pro tier. (Source: mem0ai/mem0 GitHub)
- [Memory Benchmark Gap]: Independent benchmarks show 15-point accuracy gap between Zep (63.8%) and Mem0 (49.0%) on temporal retrieval. Zep uses temporal knowledge graph with validity windows; Mem0 lacks temporal fact modeling. Consider Zep for PAM if temporal reasoning matters. (Source: Atlan.com, vectorize.io benchmark)
- [LOCOMO Benchmark Full Data]: State of AI Agent Memory 2026 report reveals full LOCOMO results: Full-context 72.9% accuracy but 9.87s median latency (~26k tokens/conv); Mem0 66.9% at 0.71s; Mem0g (graph) 68.4% at 1.09s. Key insight: accuracy ceiling vs latency tradeoff is real — Mem0g with 1.44s p95 vs full-context's 17.12s p95. Full-context is "categorically unusable in production." (Source: mem0.ai/blog/state-of-ai-agent-memory-2026, April 1 2026)
- [Agent Framework Landscape]: 13 agent frameworks now have Mem0 integrations: LangChain, LangGraph, LlamaIndex, CrewAI, AutoGen, Agno, CAMEL AI, Dify, Flowise, Google ADK, OpenAI Agents SDK, Mastra. No single framework has won — integration breadth matters. (Source: mem0.ai/blog/state-of-ai-agent-memory-2026)

## Research Notes — 2026-04-11
- [Agent Attribution]: Linux kernel now has official AI contributor guidance — uses "Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL1]" tags for AI contributions. This formalizes how agent contributions get documented. Relevant for PAM build patterns. (Source: torvalds/linux kernel docs)

## Research Notes — 2026-04-15
- [Mem0 v2.0.0-beta.1 Full Changelog]: Node SDK v3.0.0-beta.1 + Python SDK v2.0.0b1 both shipped April 14. Key: DeepSeek LLM provider added to Node SDK, Azure OpenAI structured output support added (Python), LLM-hallucinated ID crashes fixed (issue #3931), telemetry sampling at 10% for hot-path events. enable_graph removed across all APIs — any PAM integration against Mem0 OSS will need migration from v1.x patterns. (Source: mem0ai/mem0 GitHub releases, April 14 2026)
- [Claude Code Routines — HN #1 Story]: 664 points, 375 comments. Routines feature allows structured agent procedures/policies. Key PAM insight: comments reveal strong preference for portable, non-provider-locked patterns. "I want a commodity, not a platform" sums up developer sentiment. PAM design should avoid Anthropic-specific patterns. (Source: HN #47768133)

## Research Notes — 2026-04-18
- [Build Reference — CognitiveBlueprint Architecture for PAM]: Complete open-source implementation (March 2026) of CognitiveBlueprint with dataclass components: BlueprintIdentity, BlueprintMemory ( SHORT_TERM/EPISODIC/PERSISTENT, window_size, summarize_after), BlueprintPlanning (SEQUENTIAL/HIERARCHICAL/REACTIVE strategies), BlueprintValidation (require_reasoning, forbidden_phrases). PAM's cognition installation should output artifacts in this format. YAML-based blueprint loading is runtime-portable. (Source: marktechpost.com, March 7 2026)
- [Build Reference — AI Agent Benchmarks Published]: AI Agent Square published 7-dimension benchmarks (task completion, accuracy, hallucination rate, latency p50/p95, cost/task, satisfaction, real deployments). Benchmark methodology could inform PAM testing/validation. Could also be used as marketing benchmark for PAM performance claims. (Source: aiagentsquare.com/blog/ai-agent-benchmarks-2026.html)

## Research Notes — 2026-04-17
- [Build Pattern — Android CLI as Reference Implementation]: Google's Android CLI (released April 17) uses Skills (SKILL.md format) that auto-trigger based on prompt metadata matching. It reduced agent token usage by 70% and task completion time by 3x. This is the exact pattern PAM should follow: lightweight CLI interface + auto-triggering Skills + explicit SDK management. (Source: android-developers.googleblog.com)
- [Build Pattern — Codex Background Execution + Memory]: Codex now supports background computer use (multiple agents on Mac in parallel), persistent memory, scheduled future work, and MCP plugins. This is the production reference for what a fully-capable agent desktop assistant looks like. PAM's feature set should map to this as a baseline. (Source: openai.com/codex)

## Research Notes — 2026-04-16
- [Agent Framework Comparison — 8 SDKs]: Deep comparison article covers Claude Agent SDK, OpenAI Agents SDK, Google ADK, LangGraph, CrewAI, Smolagents, Pydantic AI, AutoGen. Key insight: MCP/A2A protocols covered as connector layer, Skills as knowledge/context layer. The article reinforces the "MCP for connections, Skills for patterns" architecture — validates this as the right pattern for PAM. (Source: morphllm.com/ai/agent-framework)
- [Morph Tools for Coding Agents]: New tool category emerging — Morph SDK with subagents: Fast Apply (AI code merge), WarpGrep (sub-6s AI search), Compact (context compaction for long agents), Glance (auto-test PRs with video). All via OpenAI-compatible API + Anthropic/Vercel AI SDK support. Notable: MCP connectivity to Claude/Cursor/VS Code. (Source: morphllm.com)

## Research Notes — 2026-04-20
- [OMEGA — 95.4% LongMemEval, Zero Dependencies]: New top performer on independent benchmarks. SQLite + ONNX embeddings, AES-256 encryption, 25 MCP tools, "intelligent forgetting." Local-first with no external infrastructure. For PAM, OMEGA could replace Mem0 cloud-dependency — same memory problem, zero-deps solution. (Source: omegamax.co, April 2026)
- [MemoryLake — Cross-Agent Memory Infrastructure Reference]: Platform-neutral "memory passport for agents." Cross-session + cross-agent portable memory, multimodal (docs, images, audio). Strong enterprise governance (provenance, traceability, deletion). PAM could use MemoryLake architecture as reference for how to build portable cross-agent memory, not just per-agent memory. (Source: powerdrill.ai, April 8 2026)
- [Memory Benchmark Summary for PAM]: OMEGA 95.4% (zero deps) | Zep 63.8-71.2% (temporal reasoning, needs Neo4j) | Mem0 49.0% (cloud-first, graph behind $249/mo paywall). PAM memory architecture decision: local-first (OMEGA) vs cloud-managed (Mem0) vs temporal-graph (Zep). OMEGA's zero-deps最适合 self-hosted PAM deployments. (Source: Atlan, Vectorize, OMEGA comparisons)

## Research Notes — 2026-04-23
- [Microsoft Agent Governance Toolkit — OWASP Top 10 Coverage, Sub-Millisecond]: Microsoft released Agent Governance Toolkit (April 2) under MIT license — first open-source toolkit addressing all 10 OWASP agentic AI risks. Seven packages: agent-os (stateless policy engine <0.1ms p99), agent-mesh (DID identity + behavioral trust scoring), agent-sre (circuit breakers + SLO enforcement), CMVK (cross-model verification with majority voting). Works with LangChain, CrewAI, Google ADK, OpenAI Agents SDK, Haystack, PydanticAI. Python/TypeScript/Rust/Go/.NET. Key for PAM: security is now a first-class build concern, not an afterthought. (Source: opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit)
- [New Framework — Claw Code Hit 72K Stars in First Days]: Claw Code launched April 2026 as open-source AI coding agent framework with 72,000 GitHub stars in first days. Emerged since last cycle — competitive with Claude Code. PAM should monitor Claw Code's trajectory. (Source: financialcontent.com, April 2026)

## Research Notes — 2026-04-22
- [Hermes Agent v0.10 — Build Reference for Self-Improving Agents]: Nous Research's Hermes Agent v0.10 (April 16) is the first production-ready self-improving open-source agent. GEPA mechanism (ICLR 2026 Oral) makes agents with 20+ self-generated skills 40% faster on repeated tasks. Three-layer memory (short-term, long-term FTS5, procedural skills). 118 skills bundled. For PAM: this is the reference implementation for self-improving agents — study GEPA architecture. (Source: innobu.com, April 2026)
- [Hermes Agent — Zero CVEs vs OpenClaw 9]: Hermes has zero known CVEs; OpenClaw had 9 in March 2026 (CVE-2026-25253 CVSS 8.8) plus ClawHavoc supply chain attack (341 malicious skills). For PAM build: security architecture lesson — smaller footprint + strict vetting > broad ecosystem with security gaps. (Source: innobu.com, April 2026)
- [OpenAI Agents SDK — Indie Maker Guide April 2026]: ShareUHack published practical guide to OpenAI Agents SDK (April 19). Key content: harness/compute separation, sandbox vendors (E2B vs Modal vs Daytona), cost modeling, Manifest anti-lock-in strategies. $20-50/month budget target. For PAM: this is the indie dev segment we're building for — understand their stack. (Source: shareuhack.com, April 19 2026)
- [Claude Code 30+ Releases, Anthropic Managed Agent Cloud]: Claude Code shipped 30+ updates in 5 weeks. Anthropic launched managed agent cloud service. OpenClaw "Dreaming" release. The agent infrastructure race is accelerating — PAM must keep pace with framework evolution. (Source: af.net, April 15 2026)

## Research Notes — 2026-04-21
- [OMEGA 95.4% LME — Build Decision Point]: Full comparison confirms OMEGA vs Mem0 tradeoffs: OMEGA (95.4% LME, 25 MCP tools, zero deps, AES-256, SQLite+ONNX) vs Mem0 (47.3K stars, 4-9 MCP tools, cloud-first, $249/mo Pro). For PAM: OMEGA's self-hosted story is the strongest fit — zero infrastructure overhead, highest benchmark score. Mem0 v2.0.0-beta migration complexity (enable_graph removed) is an additional argument for evaluating OMEGA as the PAM memory layer. (Source: omegamax.co/guides/best-ai-agent-memory-frameworks-2026, April 2026)
- [Memory Architecture Tier Guide — Three Build Paths]: ShareUHack guide (April 19) confirms practical build paths: solo (Hmem/Engram, SQLite MCP, no Docker), startup (Mem0 hybrid, SQLite+vector DB), enterprise (scope-chain, on-prem). Key build insight: SQLite+FTS5 handles <100K memories at sub-ms speed — most PAM deployments don't need a vector database. PAM's memory architecture should default to SQLite-first, with vector DB as an upgrade path. (Source: shareuhack.com AI agent memory architecture guide)
- [Four Memory Types Taxonomy — Build Reference]: Complete memory taxonomy from LangChain/LangMem: Working (LLM native), Episodic (conversation history, SQLite/checkpointer), Semantic (facts/concepts, vector/FTS5), Procedural (SOPs, markdown/SKILL.md). For PAM: procedural memory IS the cognition framework — SKILL.md files are procedural memory. This confirms the Polynize Brain extraction approach maps directly to the "procedural memory" layer. (Source: shareuhack.com, LangChain documentation)
- [Web Search Still Blocked for Framework Research]: DuckDuckGo blocking AI agent framework release queries. Brave API key still needed. (Source: research cycle)

## Research Notes — 2026-04-25
- [Build Reference — Mem0 New Token-Efficient Algorithm Sets New Memory Baseline]: Mem0's April 16 release achieves 91.6 LoCoMo (+28% from old 71.4), 93.4 LongMemEval, 64.1 BEAM (1M), 48.6 BEAM (10M), all at under 7K tokens/query. Architectural changes: single-pass ADD-only extraction (eliminates costly reconciliation step, preserves full state history), entity linking (proper nouns/quoted text/compound noun phrases), multi-signal retrieval (semantic + keyword + entity parallel scoring, fused via rank). For PAM: this is the production memory baseline PAM should target — sub-7K tokens, ADD-only extraction, multi-signal retrieval. The old Mem0 benchmark data in PAM plan (49.0% LME) is now obsolete — Mem0's new algorithm at 93.4% is competitive with OMEGA's 95.4%, and Mem0 has no published BEAM score. (Source: mem0.ai/blog/mem0-the-token-efficient-memory-algorithm)
- [Build Reference — DeepSeek V4 Agent-Aware Architecture]: DeepSeek V4 Preview (April 24) integrated with Claude Code, OpenClaw, OpenCode. Dedicated optimizations for agentic coding — novel attention with token-wise compression + DSA (DeepSeek Sparse Attention). For PAM: the model layer is now explicitly agent-optimized. PAM architecture should assume agent-aware models are the baseline, not the exception. (Source: api-docs.deepseek.com)
- [Google $40B Anthropic Investment — AI Infrastructure Investment Validates Market]: While not directly a build reference, $40B investment signals that AI agent infrastructure is a $ multi-billion market. For PAM: the build investment is justified — this is not a niche. (Source: bloomberg.com)
- [Mem0 Kimi K2.6 Memory Analysis — Multi-Agent Memory Architecture Reference]: Mem0 published "Reading the Traces: What Two Charts Tell Us About Kimi K2.6's Memory" (April 23). Technical deep dive into how a leading multi-agent system manages memory. PAM should study this as reference architecture for multi-agent memory orchestration. (Source: mem0.ai/blog)
- [Microsoft Agent Framework 1.0 GA — April 3, 2026 — Build Reference]: GA'd April 3, 2026. Unifies Semantic Kernel + AutoGen (75K+ combined stars) into single .NET + Python SDK. Five-layer architecture: Connectors (6 providers) → Kernel (DI) → Agents (first-class) → Orchestration (multi-agent patterns) → Interop (MCP + A2A). Multi-agent patterns: round-robin, supervisor, hierarchical, dynamic hand-off. DevUI local debugger included. OpenTelemetry native. MIT license. For PAM: this is the new enterprise baseline — PAM should integrate with Agent Framework 1.0 via A2A. Source: digitalapplied.com, April 18, 2026
- [Agent Framework 1.0 — A2A Enables Cross-Framework Coordination]: A2A 1.0 protocol lets Agent Framework agents coordinate with agents in other frameworks (Hermes Agent, LangChain, custom). This makes cross-framework agent communication a reality — PAM's portable cognition layer fits into this ecosystem. Source: digitalapplied.com
- [MemNexus Validates Cross-Framework Memory Gap for PAM Architecture]: MemNexus article (April 7) confirms: LangChain memory stays in LangGraph, CrewAI memory stays in CrewAI, AutoGen has no built-in memory. "The frameworks treat memory as a feature of the framework; the actual problem is memory as infrastructure that works across all of them." This is the exact problem PAM should solve. Source: memnexus.ai/blog/2026-04-07-agentic-framework-memory-comparison
- [Web Search Recovered — Framework Research Restored]: DuckDuckGo no longer blocking queries. Web search functional for first time since April 13. Previous blocker resolved. Source: research cycle

## Recent Activity
- 2026-04-25: Rosie — Cross-project research cycle (Mem0 new algorithm 93.4 LME under 7K tokens = new PAM memory baseline, ADD-only extraction architecture, DeepSeek V4 agent-aware model, Google $40B Anthropic validates market)
- 2026-04-25 (earlier): Rosie — Cross-project research cycle (Microsoft Agent Framework 1.0 GA = new enterprise build baseline with A2A, MemNexus validates cross-framework memory gap for PAM architecture, web search restored)
- 2026-04-23: Rosie — Cross-project research cycle (Microsoft Agent Governance Toolkit addresses all 10 OWASP agentic AI risks, Claw Code hits 72K stars in first days)
- 2026-04-22: Rosie — Cross-project research cycle (Hermes Agent GEPA self-improvement architecture, OpenClaw security gap vs Hermes zero CVEs, OpenAI Agents SDK indie guide, Anthropic managed cloud launched)
- 2026-04-21: Rosie — Cross-project research cycle (OMEGA vs Mem0 full comparison for PAM memory decision, SQLite-first architecture confirmed practical, four memory types taxonomy maps SKILL.md to procedural memory)
- 2026-04-20: Rosie — Cross-project research cycle (OMEGA 95.4% LME = new top memory performer, zero-deps architecture ideal for PAM, MemoryLake cross-agent reference)
- 2026-04-19: Rosie — Cross-project research cycle (20+ framework landscape map from awesome-ai-agents-2026, 1M token context baseline shifts memory architecture calculus)
- 2026-04-18: Rosie — Cross-project research cycle (Cognitive Blueprint framework = reference architecture for PAM cognition, AI Agent Benchmarks 2026 published)
- 2026-04-17: Rosie — Cross-project research cycle (Android CLI validates agent-first SDK pattern, Codex = production reference for memory + background execution)
- 2026-04-16: Rosie — Cross-project research cycle (8-framework comparison validates PAM architecture, Morph subagent tools)
- 2026-04-15: Rosie — Cross-project research cycle (Mem0 v2.0.0-beta.1 full changelog, Claude Code Routines HN analysis)
- 2026-04-14: Rosie — Cross-project research cycle (Mem0 v2.0.0-beta breaks enable_graph, LOCOMO benchmark latency targets, 13-framework integration landscape)
- 2026-04-13: Rosie — Cross-project research cycle (Mem0 State of AI Agent Memory 2026 report, LOCOMO benchmark data)

## Research Notes — 2026-04-26
- [Build Reference — Mem0 'Context Window vs Persistent Memory' — BEAM Benchmark Details]: Mem0's definitive blog post (April 8) on why 1M context isn't enough cites BEAM benchmark data showing quality correlation plummets from ~0.8 (2K context) to ~0.3 (128K) to near zero at 1M tokens. Key insight: as context grows, relevant information gets buried in noise — retrieval-augmented memory architectures are NOT optional even at 1M context. Full-context costs ~26K tokens/conv vs Mem0's ~1,800 — 14x cost difference. For PAM: this is the production architecture validation — PAM must use retrieval-based memory, not naive context stuffing. (Source: mem0.ai/blog/context-window-vs-persistent-memory-why-1m-tokens-isn-t-enough)
- [Build Reference — ChatGPT Solves Erdős Problem = Validation of AI Cognition Beyond Human Patterns]: The AI found a proof method "no human had thought of." For PAM: this validates the value of building agents with structured cognition frameworks that can explore solution spaces humans don't. PAM should incorporate "cognitive exploration" as a design pattern — agents that search solution spaces differently than humans would. (Source: Scientific American, April 24)
- [Build Reference — OpenAI Privacy Filter = New Data Privacy Architecture Pattern]: OpenAI's Privacy Filter (April 26) gives users control over data sent to AI. For PAM: privacy-aware agent architecture is becoming table stakes. PAM should include privacy filter capabilities from day one — not as an afterthought. (Source: openai.com)

## Recent Activity
- 2026-04-26: Rosie — Cross-project research cycle (Mem0 BEAM benchmark proves retrieval memory mandatory even at 1M context, ChatGPT Erdős validates cognitive exploration as PAM pattern, OpenAI Privacy Filter makes privacy-aware agents table stakes)

## Next Actions
- [ ] Evaluate Hermes Agent GEPA as reference architecture for self-improving PAM — study three-layer memory + skill generation loop (Rosie)
- [ ] RE-EVALUATE OMEGA vs Mem0 for PAM memory layer — Mem0 new algorithm at 93.4% LME closes the gap with OMEGA's 95.4%, and Mem0 has BEAM scores OMEGA lacks (Rosie)
- [ ] Default PAM memory architecture to SQLite+FTS5 first — vector DB is upgrade path only (Rosie)
- [ ] Map SKILL.md procedural memory extraction to the "procedural memory" layer in the four memory types taxonomy (Rosie)
- [ ] Evaluate Microsoft Agent Governance Toolkit for PAM security architecture — OWASP Top 10 coverage is now baseline for production agents (Rosie)
- [ ] Monitor Claw Code trajectory — new framework hitting 72K stars in first days (competitive with Claude Code) (Rosie)
- [ ] Study Mem0 new algorithm architecture (ADD-only extraction, multi-signal retrieval) as PAM memory reference implementation (Rosie)
- [ ] Evaluate DeepSeek V4 agent-aware architecture — assumes agent-optimized models are the baseline (Rosie)
- [ ] Add "cognitive exploration" as PAM design pattern — agents that search solution spaces differently than humans (Rosie)

## Blockers
- Web search blocked

## Research Notes — 2026-04-10
- [Agent Architecture]: "MCP over Skills" for tool integration — MCP provides clean API abstraction (connector), Skills provide context/gotchas (manual). This is the pattern to follow for PAM tool design. (Source: david.coffee)
- [Agent Research Pattern]: Research-driven agents that study papers/forks before coding find significantly better optimizations. Cost: ~$29 for 5 optimizations in 3 hours across 4 VMs. Relevant for building self-improving agent systems. (Source: blog.skypilot.co)
- [Build Tool]: SkyPilot enables distributed agent experiments across cloud VMs with simple YAML config

## Notes
- Key insight: MCP = tool connection, Skills = tool documentation/context
- PAM tools should expose MCP interfaces, with Skills that capture discovered patterns
