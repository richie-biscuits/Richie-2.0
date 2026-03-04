# TOOLS.md — Model Routing Configuration

## Available Models (as of 2026-03-04)

| Model | Provider | Alias | Best For | Cost | Context |
|-------|----------|-------|----------|------|---------|
| **Kimi K2.5** | Moonshot | `Kimi` | General tasks, long context, cheap | $0 | 256K |
| **Claude 3.5 Sonnet** | Anthropic | `Sonnet` | Coding, reasoning, creative writing | $3/$15 | 200K |
| **Claude 3 Opus** | Anthropic | `Opus` | Complex analysis, security, high-stakes | $15/$75 | 200K |

---

## Auto-Router Logic

I automatically select the best model based on task type:

```
IF task involves coding/development:
  → Sonnet (best code reasoning)
  
IF task involves security analysis (Hutcho, audits):
  → Opus (highest reasoning quality)
  
IF task involves creative writing/copy:
  → Sonnet (nuanced voice)
  
IF task requires >100K context:
  → Kimi (256K window, cheapest)
  
IF task is quick Q&A or simple:
  → Kimi (fast, cheap, good enough)
  
DEFAULT:
  → Kimi (current default)
```

---

## Manual Model Selection

You can override auto-router anytime:

```
/model Sonnet    # Switch to Claude 3.5 Sonnet
/model Opus      # Switch to Claude 3 Opus  
/model Kimi      # Switch back to Kimi
```

---

## Cost Awareness

| Model | Input | Output | Cache Read | Cache Write |
|-------|-------|--------|------------|-------------|
| Kimi | $0 | $0 | $0 | $0 |
| Sonnet | $3/million | $15/million | $0.30/million | $3.75/million |
| Opus | $15/million | $75/million | $1.50/million | $18.75/million |

**Strategy:** Use Kimi for 80% of tasks, Sonnet for coding/creative, Opus only when absolutely necessary.

---

## Fallback Chain

If primary model fails:
1. Kimi → Sonnet
2. Sonnet → Kimi
3. Opus → Sonnet

---

*Last updated: 2026-03-04*
