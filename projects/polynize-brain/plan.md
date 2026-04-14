# Polynize Brain — Plan

## Project Goal
Extract and install cognition frameworks into AI agents.

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

## Recent Activity
- 2026-04-14: Rosie — Cross-project research cycle (Mem0 v2.0.0-beta, Skill Graph operational, OpenClaw plugin v1.0.6)
- 2026-04-13: Rosie — Cross-project research cycle (Mem0 OpenClaw plugin production-ready, Dream gate feature)

## Next Actions
- [ ] Document the MCP+Skills hybrid pattern for cognition installation (Rosie)
- [ ] Map Polynize Brain's framework installation approach to the "knowledge layer + connector layer" model
- [ ] Investigate Dream gate for automatic cognition framework consolidation (Rosie)

## Blockers
- None identified

## Research Notes — 2026-04-10
- [Cognition Transfer]: MCP preferred over Skills for service integration. Skills work for knowledge/context. Best approach: "knowledge layer on top of connector layer" — use MCP for actual service connections, Skills to teach gotchas and patterns discovered during sessions. (Source: david.coffee "I Still Prefer MCP Over Skills")
- [Cognition Patterns]: Research-driven agents (reading papers/studying forks before coding) find optimizations that code-only agents miss. The pattern of "discover gotchas, then package into a Skill" is directly applicable to cognition installation. (Source: blog.skypilot.co "Research-Driven Agents")

## Notes
- MCP = connectors (service interfaces)
- Skills = manuals (knowledge, context, gotchas)
- The optimal pattern: MCP handles connection, Skills capture learned patterns/gotchas
