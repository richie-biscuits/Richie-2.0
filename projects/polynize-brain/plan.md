# Polynize Brain — Plan

## Project Goal
Extract and install cognition frameworks into AI agents.

## Research Notes — 2026-04-13
- [Memory Architecture]: Mem0 v1.0.0 just released — hybrid vector+graph+KV architecture, +26% accuracy vs OpenAI Memory on LOCOMO benchmark, 91% faster, 90% fewer tokens. Graph memory on Pro tier ($249/mo). Key insight: no temporal fact modeling — memories timestamped at creation but no validity windows. (Source: mem0ai/mem0 GitHub, Atlan comparison)
- [Temporal Memory]: Zep/Graphiti leads on temporal knowledge graph — stores facts with validity windows ("Kendra loves Adidas (as of March 2026)"). Scores 63.8% on LongMemEval vs Mem0's 49.0%. This temporal modeling gap is architecturally significant for cognition frameworks. (Source: Atlan.com benchmark comparison)

## Research Notes — 2026-04-11
- [Agent Attribution]: Linux kernel now has official AI contributor guidance — uses "Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL1]" tags for AI contributions. First major open-source project to formalize AI agent attribution. This formalization could influence how agent cognition/framework attribution gets documented. (Source: torvalds/linux kernel docs)

## Recent Activity
- 2026-04-13: Rosie — Cross-project research cycle

## Next Actions
- [ ] Document the MCP+Skills hybrid pattern for cognition installation (Rosie)
- [ ] Map Polynize Brain's framework installation approach to the "knowledge layer + connector layer" model

## Blockers
- None identified

## Research Notes — 2026-04-10
- [Cognition Transfer]: MCP preferred over Skills for service integration. Skills work for knowledge/context. Best approach: "knowledge layer on top of connector layer" — use MCP for actual service connections, Skills to teach gotchas and patterns discovered during sessions. (Source: david.coffee "I Still Prefer MCP Over Skills")
- [Cognition Patterns]: Research-driven agents (reading papers/studying forks before coding) find optimizations that code-only agents miss. The pattern of "discover gotchas, then package into a Skill" is directly applicable to cognition installation. (Source: blog.skypilot.co "Research-Driven Agents")

## Notes
- MCP = connectors (service interfaces)
- Skills = manuals (knowledge, context, gotchas)
- The optimal pattern: MCP handles connection, Skills capture learned patterns/gotchas
