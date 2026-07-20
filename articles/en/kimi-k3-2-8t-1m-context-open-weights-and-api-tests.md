---
title: "Kimi K3 Explained: 2.8T Parameters, 1M Context, Coding Results, API Pricing and Open Weights"
slug: "kimi-k3-2-8t-1m-context-open-weights-and-api-tests"
lang: "en"
source: "2026-07-20-auto-hot-topics-5"
live_url: "https://radarai.top/en/articles/kimi-k3-2.8万亿参数100万上下文开放权重与api实测"
mirror_only: false
---

> Live page: https://radarai.top/en/articles/kimi-k3-2.8万亿参数100万上下文开放权重与api实测

A source-linked guide to Kimi K3 capabilities, official coding results, one-million-token limits, API costs and the open-weight release timeline.

# Kimi K3 Explained: 2.8T Parameters, 1M Context, Coding Results, API Pricing and Open Weights

Last checked: 2026-07-20.

Moonshot released Kimi K3 on July 17, 2026. The official quickstart highlights key specs: 2.8 trillion parameters, Kimi Delta Attention, Attention Residuals, native multimodal (vision) support, and native 1M-token context. Validation focuses on evidence retrieval accuracy within long documents, citation precision, refusal behavior, and per-task cost — not just whether a million tokens *ingest*, but whether the model *uses* them effectively.

## Direct access
- [Kimi K3 API Quickstart](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart): Specs, architecture, and API endpoints.  
- [Kimi K3 Pricing](https://platform.kimi.ai/docs/pricing/chat-k3): Cache hit, cache miss, and output pricing.  
- [Kimi K3 OpenLM](https://openlm.ai/kimi-k3/): Open-weight initiative, model documentation, and official benchmark charts.  
- [Kimi Product Page](https://www.kimi.com/en): Consumer-facing K3 features.  
- [Kimi Code](https://www.kimi.com/code/en): Coding agent and CLI access.

> **Testing boundaries**: RadarAI verified five public pages and documented fields, but did *not* run the full 680K-token contract suite via paid API, nor replicate the official coding benchmarks. Price calculations here are fully reproducible; capability scores reflect official reports only — not independent replication.

## What Can K3 Do? Where Do Public Results Come From?

| Capability | Official Spec / Entry Point | Publicly Reported Results | RadarAI Assessment |
|---|---|---|---|
| Long Context | 1,048,576 tokens | Accepts million-token inputs; official docs do *not* validate end-of-context evidence recall | Must test effective context yourself using position-stratified questions |
| Code Generation | Kimi Code, CLI, API | Official chart shows DeepSWE 67.5, Terminal Bench 2.1 at 88.3, Program Bench 77.8 | Use only for initial filtering — not a substitute for in-house regression on your codebase |
| Native Vision | Explicitly listed in Quickstart | Supports mixed text+image inputs | Score OCR, chart understanding, and textual reference separately |
| MoE Inference | 2.8T total params, 16/896 experts activated | Official claim: ~2.5× scaling efficiency vs. K2 | Activated expert count informs architecture — *not* a direct proxy for API latency |
| API Cost | Per 1M tokens: $0.30 (cache hit), $3 (cache miss), $15 (output) | 680K-token miss ≈ $2.04; same prefix with cache hit ≈ $0.204 | Final bill also depends on retries, tool calls, and cache invalidation |

![Kimi K3 Official Coding Benchmark](/static/evidence/hot-topics-20260720/kimi-k3-benchmark.webp)

*Evidence type: Official benchmark chart. Source: [Kimi K3 OpenLM](https://openlm.ai/kimi-k3/), accessed July 20, 2026. Scores published by Kimi; RadarAI did not independently reproduce them.*

## Six Confirmed K3 Specifications

| Project | Confirmable Status as of 2026-07-20 | Boundaries to Preserve When Reading |
|---|---|---|
| Model | Kimi K3 — officially billed as the current flagship | Don’t conflate pricing or restrictions with older K2/K2.6 models |
| Scale | 2.8 trillion parameters | Deployment feasibility also depends on active parameters, quantization, and parallelization strategy |
| Context | Official docs state 1M tokens | Window size ≠ effective retrieval length |
| Architecture | KDA hybrid linear attention + Attention Residuals | Performance claims still require task-specific evaluation |
| Weight Status | Full weights scheduled for release before 2026-07-27 | As of July 20, the official release date hasn’t arrived yet |
| API Pricing | $0.30 per cache hit / $3 per cache miss / $15 per output token — all per 1M tokens | Retry and tool-use fees are billed separately |

K3 isn’t just a name drop. Official documentation already specifies: 2.8T total parameters, 1,048,576-token context window, 16/896 expert activation, Kimi Delta Attention (KDA), native multimodal vision support, and three-tiered API pricing. One critical distinction remains: full model weights are *scheduled* for release before July 27 — as of July 20, the page must not present this plan as an already-available download.

## K3 Integrates Long Context, Vision, and Agentic Coding in One Flagship

K3 unifies scale, long-context reasoning, visual understanding, and agentic coding under a single flagship model. The official Kimi website highlights use cases like multiplayer gaming, 3D generation, presentation building, and Swarm/Goal-style parallel task orchestration. The API quickstart guide focuses on developer-facing specs — architecture details and context fields — while openlm.ai hosts open-model documentation. These three entry points serve distinct audiences; consumer-facing features shouldn’t be assumed as guaranteed API behavior.

This launch warrants its own dedicated page because “Kimi 3” searches now simultaneously trigger questions about model specs, open weights, API usage, and deployment. Legacy pages — like old Kimi pricing or CLI docs — only cover fragments. The new page centers exclusively on K3: price updates, inference framework support, and model card revisions all converge here.

## 1 Million Tokens ≠ 1 Million Tokens of Reliable Reasoning

The “1 million token” figure is easily misinterpreted. It reflects the *maximum theoretical input length*, not guaranteed answer quality. Output accuracy is further affected by positional bias, content duplication, OCR noise, cross-document contradictions, and output token budget constraints. To verify performance: place evidence at the beginning, middle, and end of input; inject semantically similar distractor clauses; and avoid relying solely on summary outputs — those don’t prove the model actually located key passages.

A 2.8T model also defies assumptions based on consumer-grade GPUs. Full weights aren’t yet released (per official schedule); once available, teams must confirm weight precision, sharding strategy, recommended parallelism, supported inference frameworks, and license terms. For teams using only the API, priorities shift: focus instead on time-to-first-token, throughput, cache billing logic, retry behavior, and regional availability.

Native vision capability requires mixed-input testing: PDF scans, charts, screenshots, and text-based references to the same entities. Score visual accuracy, textual citation fidelity, and long-context retrieval *separately*. A strong explanation of one image doesn’t imply robust document-level multimodal reasoning.

| Evaluation Dimension | What to Record | What Not to Assume |
|---|---|---|
| Long Context | Hit rate, evidence location, conflict detection, and refusal behavior | Just confirming successful ingestion of 1M tokens |
| Open Weights | Model card, license, sharding, precision, and framework compatibility | Equating “open” with “runnable on a laptop” |
| API | Base URL, model ID, pricing tiers, cache logic, and rate limits | Reusing K2-era field names or defaults |
| Vision | Field-level accuracy and citation fidelity across charts/scans | Using a single demo image to represent full multimodal capability |
| Agent | Tool success rate, long-task recovery, and total cost per workflow | Judging solely by final output polish |

## What K3 Actually Changes for K2 Users

K3 is one of the few releases that simultaneously delivers a 3T-parameter open model, million-token context windows, and a production-ready agent interface to users. Teams can now evaluate long documents, visual materials, and multi-step coding tasks within a single candidate—but they shouldn’t rush to replace all existing models. When evidence retrieval is unstable, larger context windows make errors harder to spot; when open-weight deployment costs are prohibitively high, API access may remain the more pragmatic path.

## Case Study: A Dev Team Calculates Real-World Cost Using 240 Contracts

A legal operations team prepared 240 contracts and their attachments—roughly 680,000 tokens—and embedded 30 gold-standard questions across five categories: renewal terms, liability caps, data residency, termination notice periods, and version conflicts (6 questions each). Ten additional questions were added with *no answers present* in the materials—to test refusal behavior.

| Stage | Contract Review Action | Pass Criteria |
|---|---|---|
| **Loading** | Preserve filename, page number, and version date | All 240 documents must remain fully traceable |
| **Querying** | 40 fixed questions; supporting evidence scattered across documents | Each answer must include file name, page number, and version date |
| **Scoring** | Labeled as *fully supported*, *partially supported*, *not supported*, or *refused* | Evidence accuracy ≥ 90% |
| **Performance** | Log input tokens, cache usage, time-to-first-token, and total latency | Cost and latency must be independently reproducible |
| **Stopping** | Halt immediately if outdated clauses override newer ones—or if answers are fabricated where none exist | No further processing into legal workflows |

This case tests three things at once: whether 680K tokens load reliably, whether evidence location affects recall, and whether caching meaningfully reduces downstream query cost. Every answer must return filename, page number, and version date. If an older contract overrides a newer one—or if the system fabricates clauses where no evidence exists—even a million-token window disqualifies it from legal use.

## Five Most Common “False Successes” with Million-Token Context

- **Position Failure**: Evidence at the *end* of context is retrieved far less reliably than at the start—yet the model is still claimed to “support 1M tokens.”
- **Version Failure**: New and old contract versions are cited together—without flagging conflicts or effective dates.
- **Refusal Failure**: The system generates plausible-sounding clauses for questions with *no supporting evidence* in the source material.
- **Deployment Failure**: Weights are downloadable, but the target framework or hardware fails to load them stably.
- **Cost Failure**: Cache hits, retries, or ultra-long inputs aren’t reflected in per-task cost calculations.

“Request accepted” only signals *capacity success*—not *task success*. A drop in recall when evidence appears late in context, mixing conflicting clause versions, or failing to refuse unanswerable questions—all indicate *insufficient effective context*. Evaluation reports must separately track capacity, retrieval, citation, refusal, and cost. A single label like “supports 1M” cannot mask five distinct failure modes.

## Release Checklist: Key Items to Verify Around July 27

1. **Official Model Card**: Fill in activation parameters, license terms, training details, and evaluation methodology.  
2. **API Pricing**: Document input/output token costs, cache pricing, batch discounts, and long-context tiering.  
3. **Inference Frameworks**: Check official compatibility notes for vLLM, SGLang, and Transformers.  
4. **Quantized Versions**: Verify origin, precision (e.g., FP16, INT4), checksums, and quality degradation metrics.  
5. **Independent Long-Context Benchmark**: Require public disclosure of document construction, evidence placement strategy, and scoring scripts.

July 27 marks the first concrete refresh point for this article: verify whether full weights, model card, license, shard-level quantization specs, and recommended inference frameworks are *all available together*. On the API side, continue validating model ID, cache-hit definitions, and billing line-item transparency. Only documentation and files published on the *official organization page* can change “planned for release” into “now available.”

## How Precisely Can You Calculate K3’s Architecture, Weight Timeline, and API Cost?

The [Kimi K3 Official Quickstart Guide](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart) reveals far more than just “2.8T + 1M.” K3 uses Kimi Delta Attention and Attention Residuals; its Stable LatentMoE activates only 16 of 896 experts per token. Officially, this architecture—combined with training improvements—delivers ~`2.5x` overall scaling efficiency over K2. That 16/896 ratio reflects routing sparsity—not memory footprint. Full weights still contain *all* experts.

The “open model” still has a clear timeline as of July 20. The Quickstart guide states that the *full model weights* will be released by `2026-07-27`, and architecture, training, and evaluation details will follow in the technical report. So far, we can confirm the model release schedule, API availability, and weight release plan—but the full weight files are not yet due.

If this article publishes *after* July 27, editors **must** re-verify download links, license terms, sharding structure, and checksums—do *not* reuse future-tense phrasing from earlier drafts.

---

API pricing is now concrete and reproducible.  
[Kimi K3 Pricing Page](https://platform.kimi.ai/docs/pricing/chat-k3) quotes rates per 1 million tokens:  
- Input (cache hit): `$0.30`  
- Input (cache miss): `$3.00`  
- Output: `$15.00`  
- Context window: `1,048,576 tokens`

A 680K-token contract bundle would cost roughly `$2.04` for input on first (cache-miss) submission—and drop to `$0.204` if all subsequent queries hit cache with *identical* prefixes. Outputting 20,000 tokens costs about `$0.30`.  

But this is ideal arithmetic. Real-world cost rises with retries, file parsing overhead, tool calls, and partial cache misses—even tiny prefix changes break cache alignment. Cache testing requires *bit-for-bit identical prompts*, including system messages: changing just one word in the system prompt can drastically shift hit rates.

The pricing page also warns that `web_search` is under active revision and *should not be relied upon for production*. That warning directly impacts agent design: contract review must treat user-provided documents as a closed set—no stable web search fallback.  

K3 supports reasoning effort control, ToolCalls, JSON Mode, structured output, and dynamic tool loading—but each feature needs independent validation: schema compliance, tool mis-selection, and graceful cancellation/recovery.

---

## A 680K-token contract bundle’s cost record must *not* list a single flat rate

When running 40 questions sequentially, separate the *first load* from *follow-up queries*.  
- First request: almost always cache miss → full input cost.  
- Subsequent requests: only hit cache if *prefix*, *file order*, and *system prompt* remain unchanged.  
Even one small edit may alter billing.

Your cost log should include at minimum:  
- Prompt tokens  
- Cache-hit tokens  
- Output tokens  
- Retry count  
- Tool call fees  

Always reconcile local estimates against actual platform billing statements.

![Official Kimi API Platform Entry](/static/evidence/hot-topics-20260720/kimi-api-platform.png)

*Evidence type: Official webpage screenshot. Source: [Kimi K3 API Quickstart](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart), accessed on 2026-07-20. Exact model specs and pricing reflect fields in the linked documentation.*

## Frequently Asked Questions

### Are “Kimi 3” and “Kimi K3” the same?

Users often search for “Kimi 3”, but the official product name is **Kimi K3**. The page title accommodates both terms, but body text uses the official name.

### Does K3 really support a 1-million-token context?

Yes—the official Quickstart explicitly lists a `1M-token context window`. But effective usable length must be validated via retrieval tests—not assumed.

### Can the open weights run on a local laptop?

With a total scale of 2.8T parameters, it’s not a typical single-machine model. Local deployment feasibility depends on active parameter count, quantization level, memory capacity, and parallelization strategy.

### What’s the difference between Kimi App, Kimi Code, and Kimi API?

They serve distinct use cases:  
- **Kimi App**: Interactive knowledge work (chat UI)  
- **Kimi Code**: Coding agents (IDE-integrated, code-first workflows)  
- **Kimi API**: Programmatic access (backend integrations, batch jobs)  
Their features, quotas, and data handling paths are *not interchangeable*.

### What’s the most critical metric for long-document processing?

Track *all* of these together:  
- Evidence accuracy *under noise and conflict*  
- Refusal rate  
- Latency  
- Total cost  
Maximum input length is just a capacity field—not a performance guarantee.

## Official & Primary Sources

- [Kimi K3 API Quickstart](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart): Official specifications and API quickstart  
- [Kimi K3 Pricing](https://platform.kimi.ai/docs/pricing/chat-k3): Model ID, three-tier token pricing, and 1,048,576-context support  
- [Kimi K3 OpenLM](https://openlm.ai/kimi-k3/): Official open-model documentation  
- [Kimi Official Product Page](https://www.kimi.com/en): Consumer-facing and knowledge-worker entry point for K3  
- [Kimi Code](https://www.kimi.com/code/en): Entry point for the K3 coding agent  

All pages were accessed on July 20, 2026. News sources are used only to verify event timing and public statements. For version numbers, parameters, access points, company identity, and event schedules, official pages take precedence. Details not available on official pages are explicitly marked as *pending verification*—no assumptions are made based on search snippets.

## Read Next

- [Kimi Model Updates](/en/topics/kimi-model-updates)  
- [Kimi Code CLI](/en/articles/kimi-code-cli-and-ide-evaluation-for-builders)
