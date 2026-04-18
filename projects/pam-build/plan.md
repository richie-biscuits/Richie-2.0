# PAM Build — Plan

## Project Goal
Research agent build patterns and tools.

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

## Recent Activity
- 2026-04-18: Rosie — Cross-project research cycle (Cognitive Blueprint framework = reference architecture for PAM cognition, AI Agent Benchmarks 2026 published)
- 2026-04-17: Rosie — Cross-project research cycle (Android CLI validates agent-first SDK pattern, Codex = production reference for memory + background execution)
- 2026-04-16: Rosie — Cross-project research cycle (8-framework comparison validates PAM architecture, Morph subagent tools)
- 2026-04-15: Rosie — Cross-project research cycle (Mem0 v2.0.0-beta.1 full changelog, Claude Code Routines HN analysis)
- 2026-04-14: Rosie — Cross-project research cycle (Mem0 v2.0.0-beta breaks enable_graph, LOCOMO benchmark latency targets, 13-framework integration landscape)
- 2026-04-13: Rosie — Cross-project research cycle (Mem0 State of AI Agent Memory 2026 report, LOCOMO benchmark data)

## Next Actions
- [ ] Evaluate Zep vs Mem0 for PAM memory architecture — Zep's temporal knowledge graph may be better suited for agent cognition that needs fact validity tracking (Rosie)
- [ ] Apply "knowledge layer + connector layer" pattern to PAM tool architecture (Rosie)
- [ ] Use LOCOMO benchmark latency data to set PAM memory performance targets (Rosie)

## Blockers
- Web search blocked

## Research Notes — 2026-04-10
- [Agent Architecture]: "MCP over Skills" for tool integration — MCP provides clean API abstraction (connector), Skills provide context/gotchas (manual). This is the pattern to follow for PAM tool design. (Source: david.coffee)
- [Agent Research Pattern]: Research-driven agents that study papers/forks before coding find significantly better optimizations. Cost: ~$29 for 5 optimizations in 3 hours across 4 VMs. Relevant for building self-improving agent systems. (Source: blog.skypilot.co)
- [Build Tool]: SkyPilot enables distributed agent experiments across cloud VMs with simple YAML config

## Notes
- Key insight: MCP = tool connection, Skills = tool documentation/context
- PAM tools should expose MCP interfaces, with Skills that capture discovered patterns
