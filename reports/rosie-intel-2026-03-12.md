# ROSIE Intelligence Report: OpenClaw Community Research
**Date:** 2026-03-12  
**Time Period:** Past 24 hours  
**Researcher:** ROSIE (Research Intelligence Specialist)

## Executive Summary

- **Critical Bug Reports:** Multiple significant bugs reported in GitHub issues, including configuration errors, cron job timeouts, and agent message handling issues affecting user experience
- **Community Engagement:** Active discussions in r/LocalLLaMA about OpenClaw integration with Jan for fully local deployment and performance comparisons between inference engines
- **Feature Development:** Community members building advanced integrations like the Agent Passport System MCP with cryptographic identity and intent networking
- **Deployment Challenges:** Users reporting update failures and container rebuild issues, particularly affecting Docker deployments and git-based installations
- **Growing Ecosystem:** OpenClaw gaining traction in self-hosted AI communities with discussions about enterprise vs personal agent use cases

## Key Findings

### 1. Critical Bug Reports (GitHub Issues)

**Configuration Bug (#43728):**
- Heartbeat config incorrectly written to `gateway.heartbeat` instead of `agents.defaults.heartbeat`
- Causes gateway startup failures with schema validation errors
- Workaround requires running `openclaw doctor --fix` but issue recurs

**Cron Job Bug (#43721):**
- Cron jobs with `sessionTarget: isolated` timeout after 30 seconds
- Direct subagent spawning works fine (3 seconds), only cron with isolated mode fails
- Affects automated task scheduling functionality

**Agent Message Bug (#43716):**
- Agent incorrectly sets assistant message content to `null` when empty string
- Causes LLM API token validation errors: "Messages token length must be in (0, 1048576], but got 0"
- Regression that worked before, now fails in v2026.3.8

**Update Failure Bug (#43712):**
- v2026.3.11 update fails on live git install at `/usr/lib/node_modules/openclaw`
- Build succeeds in clean checkout but fails in existing install
- TypeScript compilation errors with A2UI/lit dependencies

**Control UI Bug (#43706):**
- Control UI loses gateway token after container rebuild
- Requires manual token re-entry after every upgrade
- Token stored only in session/memory, not persisted

### 2. Feature Requests & Enhancements

**Feishu Bitable Enhancement (#43729):**
- Request for native attachment upload and record deletion support in Feishu Bitable
- Currently requires custom scripts for file uploads and API calls for deletions
- Use case: Automating data entry flows with file attachments (PDFs, receipts, images)

**Feishu Streaming Card Bug (#43704):**
- Streaming card merges unrelated replies when agent produces multiple final messages
- Results in duplicate content displayed to users
- Root cause in `mergeStreamingText` function concatenating unrelated content

### 3. Community Discussions (r/LocalLLaMA)

**Jan Integration Announcement:**
- Jan now supports one-click install for OpenClaw with direct integration with Jan-v3-base model
- "Everything stays inside your computer - privately"
- Posted by Alan, a member of Jan team and author of Jan models

**Performance Discussions:**
- Thread comparing "SGLang vs vLLM vs llama.cpp for OpenClaw / Clawdbot"
- Discussion about "Personal Agents (OpenClaw) vs Enterprise Agents"
- Community sharing best practices for local LLM hosting and optimization

### 4. Advanced Integrations & Showcases

**Agent Passport System MCP (#43705):**
- Community-built MCP server providing cryptographic identity for agents
- Features: Ed25519 passports, Intent Network for agent-to-agent matching
- 61 tools, 534 tests, 17 protocol modules
- Built by 3 AI agents and 1 human, running on OpenClaw
- Enables verifiable identity and networking where agents find each other based on human needs

### 5. User Requests & Support

**iOS TestFlight Access (#43722):**
- User requesting access to iOS TestFlight beta for OpenClaw
- Currently running OpenClaw v2026.3.11 on Mac Mini (Apple Silicon)
- Using as personal AI assistant with Feishu integration

## Notable Discussions (with Links)

### GitHub Issues (Past 24 Hours):
1. **#43729** - [Feature Request] feishu_bitable: native attachment upload and record deletion support
   - https://github.com/openclaw/openclaw/issues/43729

2. **#43728** - Heartbeat config written to invalid `gateway.heartbeat` location
   - https://github.com/openclaw/openclaw/issues/43728

3. **#43722** - Request iOS TestFlight Access
   - https://github.com/openclaw/openclaw/issues/43722

4. **#43721** - Bug: Cron job execution timeout with isolated sessionTarget
   - https://github.com/openclaw/openclaw/issues/43721

5. **#43716** - Bug: Agent incorrectly sets assistant message content to null
   - https://github.com/openclaw/openclaw/issues/43716

6. **#43712** - Bug: v2026.3.11 update fails on live git install
   - https://github.com/openclaw/openclaw/issues/43712

7. **#43706** - Bug/UX: Control UI loses gateway token after container rebuild
   - https://github.com/openclaw/openclaw/issues/43706

8. **#43705** - Showcase: Agent Passport System MCP
   - https://github.com/openclaw/openclaw/issues/43705

9. **#43704** - Bug: Feishu streaming card merges unrelated replies
   - https://github.com/openclaw/openclaw/issues/43704

### Reddit Discussions:
1. **OpenClaw is now supported in Jan - totally local!**
   - https://www.reddit.com/r/LocalLLaMA/comments/1rrh72g/openclaw_is_now_supported_in_jan_totally_local/

2. **SGLang vs vLLM vs llama.cpp for OpenClaw / Clawdbot**
   - https://www.reddit.com/r/LocalLLaMA/comments/1rq37ko/sglang_vs_vllm_vs_llamacpp_for_openclaw_clawdbot/

3. **Personal Agents (OpenClaw) vs Enterprise Agents**
   - https://www.reddit.com/r/LocalLLaMA/comments/1rq1rym/personal_agents_openclaw_vs_enterprise_agents/

## Trending Topics

1. **Local Deployment & Privacy:** Growing interest in fully local OpenClaw deployments using Jan integration
2. **Performance Optimization:** Community discussions about inference engine comparisons (SGLang vs vLLM vs llama.cpp)
3. **Enterprise vs Personal Use:** Differentiation between personal agent use cases and enterprise deployments
4. **Mobile Accessibility:** User demand for iOS/mobile access via TestFlight
5. **Advanced Agent Networking:** Emergence of cryptographic identity and agent-to-agent networking systems
6. **Configuration Stability:** Multiple reports of configuration and update issues affecting production deployments
7. **Feishu Integration Maturity:** Feature requests and bug reports indicating heavy Feishu platform usage

## Raw Intelligence (Interesting Snippets)

### From GitHub Issues:
- "When configuring heartbeat settings, OpenClaw writes the configuration to gateway.heartbeat which is not a valid schema key. This causes the gateway to abort on startup with a schema validation error."
- "Cron jobs with sessionTarget: isolated always timeout after 30 seconds. Direct subagent spawning works fine (3 seconds), only cron with isolated mode fails."
- "Agent incorrectly sets assistant message content to null when it is empty string, causing token validation error: 'Messages token length must be in (0, 1048576], but got 0'"
- "Updating OpenClaw from 2026.3.8 to v2026.3.11 failed on my live Linux git install at /usr/lib/node_modules/openclaw, even though the same tag built successfully in a clean throwaway checkout."
- "After every container rebuild (upgrade, restart), the Control UI desktop app loses connection and displays: unauthorized: gateway token mismatch. The user must manually re-enter the gateway token each time."

### From Reddit:
- "Jan now supports one-click install for OpenClaw with direct integration with Jan-v3-base model. Everything stays inside your computer - privately."
- "Disclosure: I'm Alan, a member of Jan team and author of Jan models."

### From Community Showcase:
- "We built an MCP server on top of OpenClaw that gives agents cryptographic identity and a networking protocol for connecting people through their agents."
- "The Agent Passport System MCP server (v2.8.0, 61 tools) provides: Cryptographic Identity — Every agent gets an Ed25519 passport. Every action is signed."
- "Intent Network (brand new) — Agents publish IntentCards describing what their human needs, offers, and is open to. Other agents search, match by relevance, and broker introductions."
- "534 tests. 17 protocol modules. Apache 2.0. Built by 3 AI agents and 1 human, running on OpenClaw."

## Recommendations

1. **Prioritize Bug Fixes:** Address critical configuration and cron job bugs affecting user deployments
2. **Improve Update Reliability:** Investigate and fix update failures in git-based installations
3. **Enhance Documentation:** Provide clearer guidance for local deployments with Jan and other inference engines
4. **Consider Mobile Strategy:** Evaluate demand for iOS/mobile access and potential TestFlight expansion
5. **Engage with Community Builders:** Recognize and potentially integrate advanced community projects like Agent Passport System
6. **Strengthen Feishu Integration:** Address streaming card bugs and implement requested Bitable enhancements
7. **Improve Configuration Management:** Fix heartbeat configuration location and token persistence issues

## Conclusion

The OpenClaw community shows strong engagement with active bug reporting, feature requests, and advanced integrations. Key themes include growing interest in local/private deployments, performance optimization discussions, and emerging agent networking capabilities. Several critical bugs require immediate attention to maintain user confidence, particularly around configuration management and update reliability. The community is actively building on top of OpenClaw with sophisticated extensions, indicating a healthy ecosystem development.