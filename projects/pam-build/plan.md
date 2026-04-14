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

## Recent Activity
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
