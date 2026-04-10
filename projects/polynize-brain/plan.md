# Polynize Brain — Plan

## Project Goal
Extract and install cognition frameworks into AI agents.

## Recent Activity
- 2026-04-10: Rosie — Initial research cycle, framework analysis

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
