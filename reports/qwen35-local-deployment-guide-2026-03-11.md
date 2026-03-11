# Qwen 3.5 Local Deployment Guide

**Prepared for:** Marrs at Polynize Labs  
**Date:** March 11, 2026  
**Researcher:** OpenClaw Research Agent  
**Target Hardware:** Mac Mini M4 (24GB+ unified memory), Mac Studio M4 Pro (48GB+ unified memory)

---

## Executive Summary

- **Qwen 3.5** is Alibaba Cloud's latest flagship multimodal LLM series (released February 2026), offering state-of-the-art performance in coding, reasoning, and vision-language tasks with up to **1M token context window**
- **Best models for M4 Macs:** Qwen3.5-9B (Mac Mini), Qwen3.5-27B (Mac Studio M4 Pro) — both run efficiently via LM Studio with MLX optimization
- **Cost savings:** Local deployment eliminates API costs for cron jobs and routine tasks — estimated **$50-200/month savings** for moderate usage vs. Kimi/OpenAI APIs
- **Dual-machine strategy:** Mac Mini handles lightweight cron jobs and quick queries; Mac Studio handles heavier reasoning, coding, and batch processing tasks
- **OpenClaw integration:** LM Studio's OpenAI-compatible API server allows seamless connection via custom provider configuration

---

## 1. What is Qwen 3.5?

### 1.1 Overview

Qwen3.5 is a large language model series developed by the Qwen Team at Alibaba Cloud, released in February 2026. It represents a significant advancement in multimodal AI capabilities.

**Key Innovations:**
- **Unified Vision-Language Foundation** — Early fusion training on trillions of multimodal tokens
- **Hybrid Architecture** — Gated Delta Networks + sparse Mixture-of-Experts (MoE)
- **Scalable RL Generalization** — Reinforcement learning across million-agent environments
- **Global Linguistic Coverage** — Support for 201 languages and dialects

### 1.2 Model Variants and Specifications

| Model | Parameters | Context | Best For | M4 Compatibility |
|-------|------------|---------|----------|------------------|
| **Qwen3.5-0.8B** | 0.8B | 262K | Ultra-fast inference, edge devices | ✅ Excellent |
| **Qwen3.5-2B** | 2B | 262K | Low-latency tasks | ✅ Excellent |
| **Qwen3.5-4B** | 4B | 262K | Balanced speed/quality | ✅ Excellent |
| **Qwen3.5-9B** | 9B | 262K / 1M ext. | **Mac Mini M4 sweet spot** | ✅ Very Good |
| **Qwen3.5-27B** | 27B | 262K / 1M ext. | **Mac Studio M4 Pro target** | ✅ Good (48GB+ RAM) |
| **Qwen3.5-35B-A3B** | 36B total | 262K | Complex reasoning | ⚠️ Requires 64GB+ |
| **Qwen3.5-122B-A10B** | 125B total | 262K | State-of-the-art | ❌ Too large |
| **Qwen3.5-397B-A17B** | 403B total | 262K | Research/enterprise | ❌ Too large |

### 1.3 Performance Benchmarks (Qwen3.5-27B)

**Language Tasks:**
- MMLU-Pro: 86.1 (compares favorably to GPT-5-mini: 83.7)
- GPQA Diamond: 85.5 (reasoning)
- SWE-bench Verified: 72.4 (software engineering)
- LiveCodeBench v6: 80.7 (coding)

**Vision-Language Tasks:**
- MMMU: 82.3 (multimodal reasoning)
- MathVision: 86.0 (visual math)
- VideoMME: 87.0 (video understanding)

### 1.4 Context Window

- **Native context:** 262,144 tokens (256K)
- **Extended context:** Up to 1,010,000 tokens (1M) with extrapolation
- **Recommendation for OpenClaw:** Set 128K minimum to preserve thinking capabilities

---

## 2. LM Studio Setup on Apple Silicon

### 2.1 System Requirements

**Minimum (Qwen 3.5 4B-9B):**
- macOS 14+ (macOS 15+ recommended for large models)
- Apple Silicon Mac (M1/M2/M3/M4)
- 16GB unified memory
- 20GB free storage

**Recommended (Qwen 3.5 27B):**
- macOS 15+
- M4 Pro/Max or M3 Max
- 48GB+ unified memory
- 50GB free storage

### 2.2 Installation Steps

**Step 1: Download LM Studio**
```bash
# Visit https://lmstudio.ai/download
# Or use direct download link for macOS ARM64
```

**Step 2: Install LM Studio**
- Open the `.dmg` file
- Drag LM Studio to Applications
- Launch and grant permissions

**Step 3: Configure Runtime (MLX)**
1. Open LM Studio
2. Press `⌘ + Shift + R` (or `Ctrl + Shift + R` on Windows/Linux)
3. Select **MLX** runtime for Apple Silicon
4. Enable GPU acceleration

### 2.3 Downloading Qwen 3.5 Models

**Via LM Studio GUI:**
1. Click "Search" icon
2. Type "Qwen3.5"
3. Select model (e.g., `Qwen/Qwen3.5-9B` or `Qwen/Qwen3.5-27B`)
4. Click Download

**Via LM Studio CLI (lms):**
```bash
# Install lms CLI
lms install

# Download Qwen 3.5 9B
lms download Qwen/Qwen3.5-9B

# Download Qwen 3.5 27B
lms download Qwen/Qwen3.5-27B
```

**Recommended Quantizations for Mac:**
- **4-bit (Q4_K_M):** Best balance of quality/speed for M4
- **8-bit (Q8_0):** Higher quality, requires more RAM
- **MLX native:** Best performance on Apple Silicon

### 2.4 MLX-Specific Models

For optimal Apple Silicon performance, look for MLX-converted models:
- `mlx-community/Qwen3.5-9B-MLX` (when available)
- Convert yourself: `mlx_lm.convert --model Qwen/Qwen3.5-9B -q`

---

## 3. Performance Benchmarks: M4 vs M4 Pro

### 3.1 Expected Token Generation Speeds

Based on r/LocalLLaMA community reports and MLX benchmarks:

| Model | Mac Mini M4 (24GB) | Mac Studio M4 Pro (48GB) | Notes |
|-------|-------------------|--------------------------|-------|
| Qwen3.5-4B | ~45 tok/s | ~55 tok/s | Very fast for simple tasks |
| Qwen3.5-9B | ~25-30 tok/s | ~35 tok/s | **Recommended for Mini** |
| Qwen3.5-27B | ~8-10 tok/s | ~15-18 tok/s | **Sweet spot for Studio** |
| Qwen3.5-35B-A3B | Not recommended | ~10-12 tok/s | Requires 48GB+ |

### 3.2 Context Length Impact

| Context | VRAM Required (9B) | VRAM Required (27B) |
|---------|-------------------|---------------------|
| 4K | ~6 GB | ~18 GB |
| 8K | ~8 GB | ~24 GB |
| 32K | ~14 GB | ~40 GB |
| 128K | ~28 GB | ~80 GB (swap needed) |

**Recommendation:** Start with 8K-32K context for optimal performance.

---

## 4. Memory Requirements and Storage

### 4.1 RAM Requirements by Model

| Model | FP16 Size | Q4 Size | Q8 Size | Recommended RAM |
|-------|-----------|---------|---------|-----------------|
| 4B | 8 GB | ~2.5 GB | ~4 GB | 16 GB |
| 9B | 18 GB | ~5.5 GB | ~9 GB | 24 GB |
| 27B | 54 GB | ~16 GB | ~27 GB | 48 GB |
| 35B-A3B | 36 GB (active) | ~11 GB | ~18 GB | 48 GB |

### 4.2 Storage Requirements

- **Per model (Q4):** 3-18 GB
- **Per model (Q8):** 5-30 GB
- **LM Studio + runtimes:** ~5 GB
- **Recommended free space:** 100 GB for multiple models

### 4.3 macOS Wired Memory Settings

For large models on macOS 15+, increase wired memory limit:

```bash
# Check current limit
sysctl iogpu.wired_limit_mb

# Set to 80% of total RAM (e.g., 40GB for 48GB machine)
sudo sysctl iogpu.wired_limit_mb=40960

# Make persistent
echo "iogpu.wired_limit_mb=40960" | sudo tee -a /etc/sysctl.conf
```

---

## 5. Step-by-Step Installation Guide

### 5.1 Mac Mini M4 Setup (24GB)

**Recommended Model:** Qwen3.5-9B-Q4

```bash
# 1. Install LM Studio (download from lmstudio.ai)

# 2. Download model via lms CLI
lms download Qwen/Qwen3.5-9B --quantization Q4_K_M

# 3. Start LM Studio server
lms server start --port 1234

# 4. Load the model
lms load Qwen/Qwen3.5-9B --gpu
```

**Configuration:**
- Context length: 8192 or 16384
- Temperature: 0.7
- GPU layers: All (MLX auto-optimizes)

### 5.2 Mac Studio M4 Pro Setup (48GB+)

**Recommended Model:** Qwen3.5-27B-Q4

```bash
# 1. Download model
lms download Qwen/Qwen3.5-27B --quantization Q4_K_M

# 2. Increase wired memory (macOS 15+)
sudo sysctl iogpu.wired_limit_mb=45056

# 3. Start server
lms server start --port 1234

# 4. Load model
lms load Qwen/Qwen3.5-27B --gpu
```

**Configuration:**
- Context length: 16384 or 32768
- Temperature: 0.7
- Enable speculative decoding if available

---

## 6. OpenClaw Integration

### 6.1 LM Studio API Server

LM Studio provides an OpenAI-compatible API endpoint:

**Start the server:**
```bash
# Via CLI
lms server start --port 1234

# Or enable in GUI: Developer tab → Start Server
```

**API endpoint:** `http://localhost:1234/v1`

### 6.2 OpenClaw Configuration

Add to `~/.openclaw/openclaw.json`:

```json5
{
  agents: {
    defaults: {
      model: {
        primary: "local/qwen35",
        fallbacks: ["moonshot/kimi-k2.5"],
      },
      models: {
        "local/qwen35": {
          alias: "LocalQwen",
          provider: "openai-compatible",
          baseUrl: "http://localhost:1234/v1",
          modelId: "qwen3.5-9b", // or qwen3.5-27b
        },
      },
    },
  },
}
```

### 6.3 Using Local Model in OpenClaw

Once configured:
```
/model LocalQwen
```

Or set as default in configuration.

### 6.4 Testing Connection

```bash
# Test API directly
curl http://localhost:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3.5-9b",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

---

## 7. Dual-Machine Setup Strategy

### 7.1 Recommended Distribution

| Task | Machine | Model | Reason |
|------|---------|-------|--------|
| Cron jobs, automation | Mac Mini M4 | Qwen3.5-9B | Always-on, power efficient |
| Quick queries | Mac Mini M4 | Qwen3.5-9B | Fast response |
| Code generation | Mac Studio | Qwen3.5-27B | Better reasoning |
| Complex analysis | Mac Studio | Qwen3.5-27B | Higher quality |
| Batch processing | Mac Studio | Qwen3.5-27B | Parallel capable |
| Vision tasks | Mac Studio | Qwen3.5-27B | Better VQA performance |

### 7.2 Network Configuration

**Option A: Direct IP (same network)**
```json5
// Mac Mini OpenClaw config pointing to Mac Studio
{
  models: {
    "studio/qwen35": {
      alias: "StudioQwen",
      baseUrl: "http://192.168.1.100:1234/v1",
    },
  },
}
```

**Option B: Tailscale (remote access)**
```json5
{
  models: {
    "studio/qwen35": {
      alias: "StudioQwen",
      baseUrl: "http://mac-studio.tailscale:1234/v1",
    },
  },
}
```

### 7.3 Sync Considerations

**Model Files:**
- Store models on each machine locally (don't sync)
- Re-download on each machine via LM Studio

**Configuration:**
- Sync `openclaw.json` via Git or cloud storage
- Use different model aliases for each machine

**Session State:**
- OpenClaw sessions are machine-specific
- No automatic sync between machines

---

## 8. Cost Comparison: Local vs API

### 8.1 Cost Analysis (Monthly Estimate)

| Usage Pattern | Kimi API | OpenAI GPT-4o | Local (Electricity) | Savings |
|--------------|----------|---------------|---------------------|---------|
| Light (1K req/mo) | $0 (free tier) | $20 | $5 | Breakeven |
| Moderate (10K req/mo) | $15 | $80 | $8 | $7-72 |
| Heavy (100K req/mo) | $120 | $400 | $15 | $105-385 |
| Cron-heavy (500K req/mo) | $500 | $1,500 | $25 | $475-1,475 |

*Assumptions: Average 2K tokens per request, electricity at $0.15/kWh, Mac Mini ~30W, Mac Studio ~60W under load*

### 8.2 Break-Even Analysis

| Hardware | Upfront Cost | API Savings/Month | Break-Even |
|----------|-------------|-------------------|------------|
| Mac Mini M4 (24GB) | $999 | $50-100 | 10-20 months |
| Mac Studio M4 Pro (48GB) | $2,499 | $100-200 | 12-25 months |

**Non-financial benefits:**
- Zero latency for local tasks
- No API rate limits
n- Full data privacy
- Works offline

---

## 9. Gotchas and Limitations

### 9.1 Known Issues

| Issue | Workaround |
|-------|------------|
| **macOS 15+ required** for large models | Upgrade macOS or use smaller models |
| **MLX vision support** may lag behind text | Use text-only mode or wait for updates |
| **Tool calling** varies by model size | Use 9B+ for reliable tool use |
| **Context folding** needed for very long chats | Implement manual context management |
| **Memory pressure** with large contexts | Reduce context or use quantized models |

### 9.2 OpenClaw-Specific Considerations

1. **Session persistence** — Local models don't retain state between OpenClaw sessions
2. **Model switching latency** — Loading/unloading models takes 10-30 seconds
3. **Concurrent requests** — LM Studio supports limited concurrent requests; queue may form
4. **Error handling** — Local model failures need graceful fallbacks configured

### 9.3 Optimization Tips

**For Faster Inference:**
- Use Q4 quantization for 2x speedup vs Q8
- Reduce context length to minimum needed
- Enable speculative decoding (if available)
- Close other memory-heavy apps

**For Better Quality:**
- Use Q8 quantization for final outputs
- Increase context for complex reasoning
- Enable "thinking mode" (default in Qwen 3.5)
- Use 27B+ model for code generation

---

## 10. Actionable Recommendations

### 10.1 Immediate Actions

1. **Install LM Studio on both machines**
   - Mac Mini: Start with Qwen3.5-9B-Q4
   - Mac Studio: Install Qwen3.5-27B-Q4

2. **Test OpenClaw integration**
   - Configure custom provider pointing to LM Studio
   - Test `/model` switching between local and cloud

3. **Benchmark your workloads**
   - Measure token/s for typical cron jobs
   - Compare quality vs. cloud APIs

### 10.2 Short-Term (1-2 weeks)

1. **Implement dual-machine routing**
   - Light tasks → Mac Mini
   - Heavy tasks → Mac Studio

2. **Set up fallback chain**
   ```json5
   fallbacks: ["local/qwen35-27b", "local/qwen35-9b", "moonshot/kimi-k2.5"]
   ```

3. **Optimize context lengths**
   - Cron jobs: 4K context
   - Interactive: 16K context
   - Code review: 32K context

### 10.3 Long-Term (1 month)

1. **Monitor cost savings**
   - Track API usage reduction
   - Calculate actual electricity costs

2. **Fine-tune for specific tasks**
   - Consider Qwen3.5-4B for ultra-fast cron jobs
   - Keep 27B for high-quality outputs

3. **Evaluate fine-tuning**
   - Use UnSloth or LLaMA-Factory
   - Create task-specific variants

---

## Appendix A: Quick Reference Commands

```bash
# LM Studio CLI basics
lms server start --port 1234                    # Start API server
lms download Qwen/Qwen3.5-9B --quantization Q4  # Download model
lms load Qwen/Qwen3.5-9B --gpu                  # Load model to GPU
lms unload                                       # Unload current model
lms status                                       # Show loaded model

# MLX conversion (optional)
pip install mlx-lm
mlx_lm.convert --model Qwen/Qwen3.5-9B -q --upload-repo mlx-community/my-qwen

# macOS memory optimization
sudo sysctl iogpu.wired_limit_mb=45056
```

## Appendix B: Model Selection Flowchart

```
Task Type?
├── Simple automation/cron → Qwen3.5-4B (Mac Mini)
├── Quick chat responses → Qwen3.5-9B (Mac Mini)
├── Code generation → Qwen3.5-27B (Mac Studio)
├── Complex reasoning → Qwen3.5-27B (Mac Studio)
├── Vision + text → Qwen3.5-27B (Mac Studio)
└── Batch processing → Qwen3.5-27B (Mac Studio)
```

## Appendix C: Resources

- **Qwen GitHub:** https://github.com/QwenLM/Qwen3.5
- **Qwen Chat (official):** https://chat.qwen.ai
- **LM Studio:** https://lmstudio.ai
- **MLX Community:** https://huggingface.co/mlx-community
- **r/LocalLLaMA:** https://reddit.com/r/LocalLLaMA
- **OpenClaw Docs:** https://docs.openclaw.ai

---

*Report compiled by OpenClaw Research Agent on March 11, 2026.*
