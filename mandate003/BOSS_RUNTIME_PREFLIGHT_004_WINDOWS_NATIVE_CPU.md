# VOS LOCAL WORKER — Runtime qualification 004 (physical preflight)

Date: 2026-11-13
Scope: read-only research + isolated, unprivileged installation of upstream artifacts; **no inference or coding benchmark claimed**.

## Upstream pinned
- Source: official `ggml-org/llama.cpp`, latest-master commit `9daa0aa22b8aa0143344d7549dee1f0e32f048bb`.
- Source tarball on MacBook: SHA256 `e89047b054610199bf287f779b4ce1c48e20c7f9513d1d20d1a65f35ef0977b8`, 38,915,160 bytes.
- Official release: `b12360`, published 2026-11-13, upstream GitHub release.
- Official Mac x64 archive: SHA256 `ed329ff7f4048dbfbc401909926a6c6f49114fc7cb7860ed9c7976fadcc11a34`, 12,661,476 bytes, matching GitHub release digest. Mach-O x86_64 binary requires **macOS 13.3** (LC_BUILD_VERSION), incompatible with installed MacBook macOS 11.7.11; **do not execute**.
- Official Windows CPU x64 archive: SHA256 `eae1726047e0eaa707b1302929d196c999b96c2f243b21aea6e93bcebacc4e17`, 25,097,627 bytes, matching GitHub release digest. Windows user-space unzip only; no OS/firmware changes.

## MacBook physical results
- Hardware: MacBookPro11,1, Intel i5-4278U AVX2, macOS 11.7.11, 8 GiB RAM; Apple Clang 13, CMake 4.3.1.
- CPU-only CMake configure **PASS** with `-DGGML_METAL=OFF -DGGML_NATIVE=ON -DGGML_OPENMP=OFF -DLLAMA_CURL=OFF -DCMAKE_OSX_DEPLOYMENT_TARGET=11.0`.
- Configuration log SHA256: `8dd3e4ae6c70cf996e246b645b779ddf9dfa303648a29fe15db967c0084ad17a`.
- Single-job compile **STOP_RESOURCE_SWAP**. Swap increased from 4.25 MiB to about 551 MiB during build; bounded process was automatically terminated at >512 MiB growth. No successful built CLI; do not claim current-source compatibility. Upstream build unexpectedly provisioned embedded UI assets via Hugging Face; the next build would require disabling `LLAMA_USE_PREBUILT_UI` and `LLAMA_BUILD_APP`, but is not authorized in this lab after resource STOP.
- Lab: `~/Documents/VOS-LOCAL-CPU-LLAMACPP-004-20261113`, no global install.

## Windows physical results
- Host: `AlessiaManuel`, reachable by strict-host-key SSH through the iMac despite Desktop Commander reporting Offline.
- CPU i5-4210U, Intel Haswell 2C/4T, AVX2 per official Intel specifications; RAM 7.93 GiB with 2.91 GiB free in post-test sample.
- Local-only release unpack in `C:\Users\gianluca\Documents\VOS-LLAMACPP-CPU-QUAL-004-20261113`.
- `llama-cli.exe --version` **PASS**, exit 0; version 1.0.0-dev, build 12360, commit short `2d8a32502`, compiled by Clang 20.1.8 x64.
- `llama-bench.exe --version` **PASS**, exit 0; successfully loaded `ggml-cpu-haswell.dll`, confirmed CPU backend.
- CLI executable SHA256: `e38af6de029a856886356ab2569b7ca62611c2d4f0df38798830b9834de1d4dc`.
- Bench executable SHA256: `832aa64a358a75cc3c3eb0e390becbd35acc491dfc42b06ffaf1a30107203f15`.
- FLUXION actions.runner service Running after tests; sshd Running. No model loaded; no hardware performance, accuracy or RAM consumption under inference measured.

## Decision
**PASS_SCOPED_NATIVE_WINDOWS_CPU_RUNTIME** for the pinned official `llama.cpp` release; **NOT A WORKER PASS**.
Next admissible physical step is a **single** small quantized model with proven licensing/provenance, model+KV memory and swap budget, using Windows as worker and MacBook as independent Judge. Do not select a 3B/4B model merely from nominal disk size: the protected runner and 2.91 GiB sampled free memory require admission controls.
Linux migration, VOS production integration, and any changes to FLUXION remain **NOT_AUTHORIZED**.
No hosted GitHub Actions, no paid APIs, no purchases, no production source writes. Additional spend: USD 0.
