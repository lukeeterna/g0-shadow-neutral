# BOSS — NEXT SINGLE ACTION 004: MacBook Intel CPU runtime qualification
Date: 2026-11-13
Parent: VOS LOCAL WORKER SELECTION 003
Scope: research-and-scoped local preflight; no production or OS installation authority

## Evidence reviewed
- Original Mandate003 GitHub report commit: `77f00927c735933282d3c73ffdc08e964a1fbefa`, blob `bc2bbcd49232c2d3e985a90c9487a3c666423aaf`.
- iMac Qwen2.5:3b inference STOP_RESOURCE_PRESSURE: swap 4997.25 -> 8783.50 MiB used in experiment, no completed code, 0/16 NOT_RUN; protected VOS/FLUXION guest processes observed, internal health not certified.
- BOSS physical reconfirmation: iMac two protected guests Running; no loaded Ollama model; swap now sampled at 6877.75/8192 MiB (not fully recovered to experiment baseline); no more iMac inference admitted.
- BOSS physical MacBookPro11,1: Intel i5-4278U, 8 GiB, AVX2, macOS 11.7.11, SDK 12.1, Apple Clang 13, CMake 4.3.1, uid 501, ~22 GiB free, swap 4.25 MiB, macOS memory free percentage 70%; llama-cli and llama-bench absent in inspected PATH/known paths, and GGUF absent in inspected known caches; existing Ollama executable incompatible with macOS 11.
- BOSS physical Windows: Desktop Commander offline BUT strict-hostkey SSH from iMac PASS to AlessiaManuel. 7.93 GiB RAM; 2.94 GiB free sample; C: 145.9 GiB free; protected FLUXION GitHub runner Running and sshd Running; firmware virtualization disabled. Windows-native coding tests possible in future, but not the first candidate host given limited sampled free RAM.
- Original upstream llama.cpp build guide Git blob `e369aad01f499407ab4105154583bcc4b01fbfda`, CMakeLists blob `30aed5c914a901dd14dcff90f552d983bc6a6c27`. Upstream documents CMake CPU-only configuration and disabling default Metal: `-DGGML_METAL=OFF`. Never assert source compiles on macOS 11 until physically tested.

## Exactly one next experiment
1. On MacBook, isolated unprivileged new laboratory directory only: pin source revision for official ggml-org/llama.cpp; verify upstream license, exact commit, full SHA and no repo secrets; compile `llama-cli` and `llama-bench` with CPU-only CMake (`-DGGML_METAL=OFF -DGGML_NATIVE=ON`, no CUDA, no root, no Homebrew installs). Compiler SDK/version gate and executable launch proof before any model transfer.
2. Select ONE suitable Q4_K_M GGUF model with validated source, full-file SHA256, license and size, targeting <= 2.5 GiB weight footprint and <= 2048-token context initially. Prefer verified already present iMac Ollama blob for read-only LAN copy if it is a compatible GGUF and its model identity/license verified; otherwise separate explicit download/capacity admission. Do NOT infer that an Ollama model listing proves directly runnable GGUF.
3. Measure idle MacBook RAM, pressure, swap-in/out and swap occupancy BEFORE first inference. Set process/thread/memory/time limits and bounded prompt/output. STOP promptly if sustained swap growth or user/protected services affected. Do not launch inference on iMac.
4. First atomic coding test: independently freeze a corrected static Judge (permit necessary Python `ValueError`, string `format`, etc.), verify positive and deliberate-negative fixtures, then model executes. Keep original `CASEIFICIO_ORDINI_001` tests unchanged for later use; only attempt full 16 after atomic gate is valid.
5. During this experiment MacBook is WORKER, so iMac serves only as independent LIGHTWEIGHT JUDGE and publisher of allowlisted synthetic artifacts. Physical Judge role can be swapped transparently: never pretend MacBook is independent Judge of its own inference. Judge must not run AI inference or heavy VMs. For safety, if iMac Judge cannot be admitted, STOP.
6. Publish actual source, nonsecret build manifest, exact model provenance/SHA, measurements, Judge log and SHA-bound receipt in a new branch of `lukeeterna/g0-shadow-neutral`, using an authorized trusted publisher with no worker access to GitHub credentials; no cloud Actions, no production push.
7. Only after a successful 3B-class baseline consider an alternate compact model (e.g. Granite 3B / Qwen3.5 2B or 4B / Nemotron Nano 4B) one at a time. 1.5B original FAIL does not prove other sizes fail; equally, one finished generation does not prove usable coding accuracy.

## Explicit STOP gates
- No Windows Linux installation/partition/firmware or runner effects. Original recovery G1 STOP, Linux G0 NOT_ADMITTED.
- No upgrades to Big Sur or iMac; no global installations, no sudo, no external model inference service with secrets, no unverified releases.
- No more high-memory iMac inference in this lane. Do not stop protected VOS or FLUXION VMs or runners.
- No hidden code corrections by BOSS/ChatGPT. Any harness/Judge modifications must be versioned and independently tested before worker generation.
- Zero purchases, zero paid APIs, zero hosted Actions; `MAX_COST_USD=0`.
- Status today `DECISION_READY_RUNTIME_NOT_BUILT_MODEL_NOT_TESTED`; no claimed model adoption, no source-worker PASS or autonomy.
