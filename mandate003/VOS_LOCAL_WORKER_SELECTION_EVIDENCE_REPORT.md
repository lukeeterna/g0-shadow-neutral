# VOS LOCAL WORKER SELECTION — EVIDENCE REPORT
Date: 2026-11-13
Mandate: BOSS/VOS PARALLEL 003
Scope: isolated Mac CPU inference and protected-services gate
Verdict: **REJECT qwen2.5:3b on iMac with protected VMs active; NEXT TEST on an independent node with resource headroom**
Status: **STOP_RESOURCE_PRESSURE**, not coding PASS, not autonomous worker PASS.

## Frozen upstream evidence
- Contract: CASEIFICIO_ORDINI_001 SHA256 d3d97d8a03a10548b5a27a846d0ac422ea52476815693f0c901124194ef4f8f7
- MacBook Judge SHA256 5b53d5f42137e9f7944796b2118062bb8cd61679104c894f4b375e68b11dc479
- MacBook AST source guard SHA256 876aa996e003a4b4ad84dc5fdb8868ea74be5e1aa874b816833a375a2614ee10
- Benchmark001 previous qwen2.5-coder:1.5b: two model-authored attempts invalid Python syntax; 16 acceptance tests NOT_RUN.
- Orchestration harness created in isolated user lab: SHA256 26e9ff1c954a08e3dce3b5251e8eca32675c1133f3577fed806c34b0e1a3a54b. This script is AI-frontier authored harness, NOT worker-authored application code.
- Local events.jsonl SHA256 ec46c03ae788c31c1746addea8bcabe6c3c329b908864e0f77a62426831e4494, preflight and pinned Judge only; this report is an accurate standalone readback summary.

## Device and transfer checks
- iMac13,1 macOS 12.7.4, 16 GiB, no AVX2. Ollama server 0.6.7 (CLI 0.5.11), model qwen2.5:3b already present, advertised local disk footprint 1.9 GB. Quantization: not independently extracted, NOT_VERIFIED.
- MacBookPro11,1, 8 GiB RAM; Python 3.14.4 available. Existing Ollama executable requires macOS 14 and fails to start.
- MacBook SSH ED25519 fingerprint matched directly at both endpoints: SHA256:MDy+flg7jzAzfRYehVX6RR8+FgHey//lFiNId521XA0. Authenticated SSH preflight passed with strict host checking and scoped known-hosts file.
- Judge code original on MacBook verified by byte SHA before model generation; no generated application source was transferred.
- Windows AlessiaManuel was offline and not modified.
- Protected VM PIDs 492 (vos-worker) and 497 (fluxion-staging) and runner 933 observed active before and after experiment; no claim of internal service health.

## Physical inference and resource stop
- First new candidate: qwen2.5:3b via local Ollama API, temperature=0, 4096 context, 2200 maximum predicted tokens, num_thread=2, keep_alive=0.
- Initial swap: 6144 MiB allocated, 4997.25 MiB used, 1146.75 MiB free.
- During inference: swap auto-expanded to 9216 MiB allocated, 8783.50 MiB used, 432.50 MiB free. This was observed, not inferred.
- Memory-pressure reported available percentages 60% to 85% while swap consumption increased: free-memory percentage alone is NOT an admission criterion.
- Model runner reached approximately 200% CPU, around 2 GiB RSS, before STOP.
- The lab's own process and dedicated model runner only were terminated with SIGTERM to protect VOS and FLUXION; the Ollama server, both VMs and FLUXION runner were left running.
- After termination, Ollama 'ps' showed no loaded models; swap still approximately 8399.50 MiB used out of 9216 MiB. This is not a proof of complete recovery.
- No completed model response, no orders.py and no model-authored application source existed at stop. Source SHA: N/A.
- Test results: 0/16 *executed*, NOT 0/16 failed. No Judge coding acceptance run. No correction attempt. No successful code artifact.

## Performance and commercial qualification
- Correct tasks: 0 demonstrated.
- Time per correct task: NOT_MEASURABLE.
- Token/s: NOT_MEASURED; interrupted before complete Ollama response.
- Peak RAM: NOT_MEASURED in a controlled time series; a process RSS sample was approximately 2 GiB.
- Swap risk: confirmed, runtime rejected in this deployment state.
- Manual application-code edits: zero; manual safety intervention: one SIGTERM decision.
- Additional spending: 0 USD.
- Commercial license: qwen2.5:3b tag-specific license NOT_VERIFIED during this lab; no commercial adoption claim.
- Linux hardware compatibility: DOCUMENTAL_ONLY; Windows-to-Linux migration prohibited by this mandate.

## Research First upstream notes
- antirez/ds4: narrow DeepSeek/GLM/Qwen Flash native engine principally for modern Apple Silicon Metal, CUDA, and ROCm; SSD streaming does not remove non-expert weights, activations, or KV requirement. NOT_INSTALLED.
- ggml-org/llama.cpp: suitable follow-up for reproducible Intel CPU builds with GGML_AVX2=OFF and small GGUF, mmap and llama-bench. NOT_EXECUTED.
- mostlygeek/llama-swap: TTL and concurrency controls; redundant to first controlled one-model Ollama experiment. NOT_INSTALLED.
- SWE-agent/mini-swe-agent: local LiteLLM support; tool-security and process isolation still require separate qualification. NOT_INSTALLED.
- Qwen3.5:2b/4b, Granite4.2:3b, Nemotron-3-Nano:4b and Ministral-3:3b: NOT_INSTALLED, NOT_BENCHMARKED. Available upstream footprints are not proof of CPU support or quality.

## Decision
**REJECT** the qwen2.5:3b inference configuration on the already-loaded iMac, under the observed resource pressure.
**NEXT TEST**: after verifying the protected node is stable, qualify a small GGUF CPU runtime and one compact coding model on a less-burdened host (MacBook first if compatible runtime is built without OS upgrade, or a separately authorized Windows-native CPU runner; Linux migration is a separate future decision). Start with an atomic coding task and an independent original Judge; preserve SHA and stop on swap growth.
**ADOPT**: none. Autonomous complete worker cycle, 16/16 acceptance, persistent local worker and end-to-end publisher are NOT_PROVEN.
GitHub Actions: NOT_USED. Main, production VOS/FLUXION/ARGOS: NOT_MODIFIED.
