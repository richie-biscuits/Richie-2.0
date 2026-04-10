# PAM Build — Plan

## Project Goal
Research agent build patterns and tools.

## Recent Activity
- 2026-04-10: Rosie — Initial research cycle, found MCP vs Skills architecture insight

## Next Actions
- [ ] Apply "knowledge layer + connector layer" pattern to PAM tool architecture (Rosie)
- [ ] Research if Mem0/LOCOMO have released updates this month

## Blockers
- Web search blocked

## Research Notes — 2026-04-10
- [Agent Architecture]: "MCP over Skills" for tool integration — MCP provides clean API abstraction (connector), Skills provide context/gotchas (manual). This is the pattern to follow for PAM tool design. (Source: david.coffee)
- [Agent Research Pattern]: Research-driven agents that study papers/forks before coding find significantly better optimizations. Cost: ~$29 for 5 optimizations in 3 hours across 4 VMs. Relevant for building self-improving agent systems. (Source: blog.skypilot.co)
- [Build Tool]: SkyPilot enables distributed agent experiments across cloud VMs with simple YAML config

## Notes
- Key insight: MCP = tool connection, Skills = tool documentation/context
- PAM tools should expose MCP interfaces, with Skills that capture discovered patterns
