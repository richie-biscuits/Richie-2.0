# PAM Build - Plan

## Project Goal
Research agent build patterns and tools.

## Research Notes — 2026-05-17

- [Agent Frameworks — 2026 Production Data]: LangGraph now dominates production — 44% usage, 81% satisfaction, +210% YoY growth; LangChain 68% usage (as integration layer), 62% satisfaction; AutoGen 31% usage, 74% satisfaction, +180% YoY; CrewAI 28% usage, 69% satisfaction, +340% YoY — AgileSoftLabs May 2026 analysis
- [Agent Frameworks]: LangGraph checkpointing enables true state persistence — survives server restarts, rate limits, user interruptions; human-in-the-loop via interrupt_before parameter; cycles support self-correcting agents — production-grade features
- [Agent Frameworks]: LangGraph + LangChain are complementary — LangGraph nodes use LangChain tools/models; LangChain is integration layer, LangGraph is orchestration layer
- [Build Patterns]: Hybrid architecture pattern confirmed — LangGraph for orchestration layer, CrewAI for role-based subtasks, AutoGen for conversational tools — operational cost is managing 3 SDKs
- [Cost Optimization]: Real-time usage monitoring reduces infrastructure waste 30%; pre-implementation technical audit ($500-$2,000) can save 10x in avoided rework — Reinventing.ai

## Research Notes — 2026-05-15

- [Agent Frameworks]: LangGraph (90k stars) — stateful workflows, explicit control flow, time-travel debugging, best $/result for cost-sensitive workloads (~$0.04/task) — ExamCert.ai
- [Agent Frameworks]: CrewAI (28k stars) — role-based multi-agent orchestration, strong out-of-box prompts, 30-50% token overhead vs hand-tuned, fastest prototype velocity — ExamCert.ai
- [Agent Frameworks]: AutoGen 0.5+ (42k stars) — event-driven runtime rebuilt 2025, excellent for conversational agents and code execution, ~$0.09/task, Azure Foundry integration — ExamCert.ai
- [Agent Frameworks]: Framework overhead is rounding error — token cost dominates; debuggability is #1 reason teams switch frameworks in year 2 — ExamCert.ai
- [Build Patterns]: Common hybrid pattern emerging — LangGraph for orchestration layer, CrewAI for role-based subtasks, AutoGen for conversational tools — cost is operational (3 SDKs)
- [Cost Optimization]: Real-time usage monitoring reduces infrastructure waste 30%; pre-implementation technical audit ($500-$2,000) can save 10x in avoided rework — Reinventing.ai

## Research Notes — 2026-04-26

- [OpenAI Codex MCP Tool Support - April 25]: Codex now supports MCP (Model Context Protocol) tools — allows agents to connect to external APIs and data sources. This is the protocol layer standardization PAM should build on. MCP adoption accelerating: Codex, Claude, OpenClaw all support it now. (Source: openai.com/codex, April 25 2026)

## Research Notes — 2026-04-22
- [Hermes Agent v0.10 - Build Reference for Self-Improving Agents]: Nous Research's Hermes Agent v0.10 (April 16) is the first production-ready self-improving open-source agent. GEPA mechanism (ICLR 2026 Oral) makes agents with 20+ self-generated skills 40% faster on repeated tasks. Three-layer memory (short-term, long-term FTS5, procedural skills). 118 skills bundled. For PAM: this is the reference implementation for self-improving agents - study GEPA architecture. (Source: innobu.com, April 2026)

## Research Notes — 2026-04-19
- [Agent Framework Landscape - 2026 State of Play]: awesome-ai-agents-2026 lists 20+ agent frameworks, 10+ agent memory solutions, 10+ agent protocols. LangChain (90k+ stars) dominates ecosystem, CrewAI (20k+ stars) leads multi-agent. Notable new entrant: Devstral 2 (Mistral's open-source coding agent). Key insight: frameworks are fragmenting, memory is consolidating as its own category - PAM should build to this landscape. (Source: github.com/Zijian-Ni/awesome-ai-agents-2026)
- [Model Context Reaching 1M Tokens]: GPT-5.4 (March 2026) and Claude Opus 4.6 (Feb 2026) both support 1M token context windows. This changes the latency/cost calculus for memory architecture - full context is now viable for some use cases. PAM should benchmark against this new baseline: is selective memory still worth the engineering complexity when full context is cheap? (Source: awesome-ai-agents-2026)

## Research Notes — 2026-04-14
- [Mem0 v2.0.0-beta]: Python SDK v2.0.0b0 (April 13) + v2.0.0b1 (April 14) - major breaking changes: removed enable_graph parameter, deprecated params stripped across LLMs/embeddings/vector stores/graphs. LLM-hallucinated ID crashes fixed (was issue #3931). Azure OpenAI structured output support added. DeepSeek LLM provider added to Node SDK. If building PAM against Mem0, expect migration work. (Source: mem0ai/mem0 GitHub releases)
- [LOCOMO Full Data]: Full-context: 72.9% accuracy but 9.87s median latency, ~26k tokens/conv. Mem0g: 68.4% at 1.09s. Mem0: 66.9% at 0.71s. P95 latency: Mem0g 1.44s vs full-context 17.12s. Key lesson: accuracy ceiling comes with categorical latency cost. PAM memory architecture should target ~1s median, <2s p95 as production baseline. (Source: mem0.ai/blog/state-of-ai-agent-memory-2026)
- [13-Framework Integration]: Mem0 now integrates with 13 frameworks: LangChain, LangGraph, LlamaIndex, CrewAI, AutoGen, Agno, CAMEL AI, Dify, Flowise, Google ADK, OpenAI Agents SDK, Mastra. No single winner yet - integration breadth matters more than depth for PAM tool selection. (Source: mem0.ai/blog/state-of-ai-agent-memory-2026)

## Research Notes — 2026-04-13
- [Mem0 v1.0.0]: Major release with API modernization, improved vector store support, GCP integration. Mem0 claims +26% accuracy vs OpenAI Memory on LOCOMO benchmark, 91% faster responses, 90% lower token usage. Graph memory still paywalled on Pro tier. (Source: mem0ai/mem0 GitHub)
- [Memory Benchmark Gap]: Independent benchmarks show 15-point accuracy gap between Zep (63.8%) and Mem0 (49.0%) on temporal retrieval. Zep uses temporal knowledge graph with validity windows; Mem0 lacks temporal fact modeling. Consider Zep for PAM if temporal reasoning matters. (Source: Atlan.com, vectorize.io benchmark)
- [LOCOMO Benchmark Full Data]: State of AI Agent Memory 2026 report reveals full LOCOMO results: Full-context 72.9% accuracy but 9.87s median latency (~26k tokens/conv); Mem0 66.9% at 0.71s; Mem0g (graph) 68.4% at 1.09s. Key insight: accuracy ceiling vs latency tradeoff is real - Mem0g with 1.44s p95 vs full-context's 17.12s p95. Full-context is "categorically unusable in production." (Source: mem0.ai/blog/state-of-ai-agent-memory-2026, April 1 2026)
- [Agent Framework Landscape]: 13 agent frameworks now have Mem0 integrations: LangChain, LangGraph, LlamaIndex, CrewAI, AutoGen, Agno, CAMEL AI, Dify, Flowise, Google ADK, OpenAI Agents SDK, Mastra. No single framework has won - integration breadth matters. (Source: mem0.ai/blog/state-of-ai-agent-memory-2026)

## Research Notes — 2026-04-11
- [Agent Attribution]: Linux kernel now has official AI contributor guidance - uses "Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL1]" tags for AI contributions. This formalizes how agent contributions get documented. Relevant for PAM build patterns. (Source: torvalds/linux kernel docs)

## Research Notes — 2026-04-15
- [Mem0 v2.0.0-beta.1 Full Changelog]: Node SDK v3.0.0-beta.1 + Python SDK v2.0.0b1 both shipped April 14. Key: DeepSeek LLM provider added to Node SDK, Azure OpenAI structured output support added (Python), LLM-hallucinated ID crashes fixed (issue #3931), telemetry sampling at 10% for hot-path events. enable_graph removed across all APIs - any PAM integration against Mem0 OSS will need migration from v1.x patterns. (Source: mem0ai/mem0 GitHub releases, April 14 2026)
- [Claude Code Routines - HN #1 Story]: 664 points, 375 comments. Routines feature allows structured agent procedures/policies. Key PAM insight: comments reveal strong preference for portable, non-provider-locked patterns. "I want a commodity, not a platform" sums up developer sentiment. PAM design should avoid Anthropic-specific patterns. (Source: HN #47768133)

## Research Notes — 2026-04-18
- [Build Reference - CognitiveBlueprint Architecture for PAM]: Complete open-source implementation (March 2026) of CognitiveBlueprint with dataclass components: BlueprintIdentity, BlueprintMemory ( SHORT_TERM/EPISODIC/PERSISTENT, window_size, summarize_after), BlueprintPlanning (SEQUENTIAL/HIERARCHICAL/REACTIVE strategies), BlueprintValidation (require_reasoning, forbidden_phrases). PAM's cognition installation should output artifacts in this format. YAML-based blueprint loading is runtime-portable. (Source: marktechpost.com, March 7 2026)
- [Build Reference - AI Agent Benchmarks Published]: AI Agent Square published 7-dimension benchmarks (task completion, accuracy, hallucination rate, latency p50/p95, cost/task, satisfaction, real deployments). Benchmark methodology could inform PAM testing/validation. Could also be used as marketing benchmark for PAM performance claims. (Source: aiagentsquare.com/blog/ai-agent-benchmarks-2026.html)

## Research Notes — 2026-04-17
- [Build Pattern - Android CLI as Reference Implementation]: Google's Android CLI (released April 17) uses Skills (SKILL.md format) that auto-trigger based on prompt metadata matching. It reduced agent token usage by 70% and task completion time by 3x. This is the exact pattern PAM should follow: lightweight CLI interface + auto-triggering Skills + explicit SDK management. (Source: android-developers.googleblog.com)
- [Build Pattern - Codex Background Execution + Memory]: Codex now supports background computer use (multiple agents on Mac in parallel), persistent memory, scheduled future work, and MCP plugins. This is the production reference for what a fully-capable agent desktop assistant looks like. PAM's feature set should map to this as a baseline. (Source: openai.com/codex

## Blockers
- None

## Next Actions

1. **Framework decision matrix** — Create client selection guide: LangGraph (stateful/production), CrewAI (role-based/fastest prototype), AutoGen (conversational/multi-agent) — based on Rosie May 2026 research
2. **Hybrid architecture guide** — Document when to use LangGraph + CrewAI + AutoGen together vs single framework
3. **Checkpointing implementation** — Add LangGraph state persistence to PAM for production reliability

## Recent Activity

- 2026-05-17: Rosie added 2026 framework production data — LangGraph dominates (44% usage, 81% satisfaction), clear framework domains established
- 2026-04-26: Rosie added OpenAI Codex MCP support research
- 2026-04-22: Rosie researched Hermes Agent v0.10 for self-improving patterns