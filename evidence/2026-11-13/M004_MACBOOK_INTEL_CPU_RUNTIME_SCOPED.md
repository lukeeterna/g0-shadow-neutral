# BOSS / VOS — M004 MacBook Intel CPU runtime qualification (scoped evidence)
Date: 2026-11-13
Parent: VOS LOCAL WORKER SELECTION 003
Status: RUNTIME_BUILT_LAUNCH_PASS / MODEL_NOT_ADMITTED / INFERENCE_NOT_RUN / JUDGE_NOT_RUN / NO_GO
Authority: laboratory-only; no production, OS upgrade, or runner authorization.

## Physical machine (Desktop Commander, direct MacBook)
- Host: MacBook-Pro-di-MacBook.local, macOS 11.7.11, x86_64, UID 501, 8 GiB physical RAM, 4 logical CPUs.
- Compiler: AppleClang 13.0.0.13000029; SDK 12.1; CMake 4.3.1.
- Disk free initial ~22.3 GiB; swap initial 4.25 MiB; memory-pressure free percentage initially 71%.
- Lab directory only: /Users/macbook/Documents/VOS-M004-CPU-Lab-20261113
- No sudo or global installer; no VOS/FLUXION repositories or protected guest changes.

## Official pinned source
- Git: https://github.com/ggml-org/llama.cpp
- Commit: 9daa0aa22b8aa0143344d7549dee1f0e32f048bb
- License: MIT; LICENSE Git blob e7dca554bcb802f98408383a864404e3aa4eacca.
- CMakeLists Git blob: 30aed5c914a901dd14dcff90f552d983bc6a6c27.
- docs/build.md Git blob: e369aad01f499407ab4105154583bcc4b01fbfda.
- Clean worktree on checkout, exact full commit SHA readback.

## Build manifest and deviations
- CPU-only CMake: CMAKE_BUILD_TYPE=Release; CMAKE_OSX_DEPLOYMENT_TARGET=11.0; GGML_METAL=OFF; GGML_NATIVE=ON; GGML_BLAS=OFF; GGML_OPENMP=OFF; GGML_CCACHE=OFF; LLAMA_CURL=OFF; LLAMA_BUILD_TESTS=OFF; LLAMA_BUILD_TOOLS=ON; BUILD_SHARED_LIBS=OFF.
- First build attempted target llama-cli while LLAMA_BUILD_SERVER=OFF and failed "No rule to make target llama-cli." This source revision gates tools/cli behind LLAMA_BUILD_SERVER.
- Reconfigured LLAMA_BUILD_SERVER=ON only to expose llama-cli; LLAMA_BUILD_APP=OFF and LLAMA_OPENSSL=OFF. Build targeted llama-cli and llama-bench only, --parallel 2, nice 10; no server launched.
- WARNING: This enabled llama-ui-assets dependency; upstream build tried a b1 Hugging Face URL, then downloaded and verified a fallback 'latest' UI tarball. This fallback was **not pinned in this mandate**. Build is not certified as offline/reproducible; dependency side effect must be addressed before promotion, without pretending it did not occur.
- Both targets reported built; process check found no residual cmake/clang/make processes.
- CMakeCache.txt local SHA256: a50d49522d2767efd400bdc7c7962a7ba5571817227e01e9ce9cb62c7f2676a7
- build-m004.log local SHA256: 9b8d1e19b3a0fddc3053cc8ea533e5674f89714e196678ce4c304a6b9b6b5303 (111539 bytes). These files remain on MacBook; hashes are observations, NOT assertions of uploaded immutable evidence.

## Launch evidence, no model
- llama-cli Mach-O x86_64, 20,846,720 bytes; SHA256 bf0134f2a3550750eb58c3efbf67ca1377f5150e0ce9740ffa5f5daf6a128330
- llama-bench Mach-O x86_64, 12,585,584 bytes; SHA256 be2e5aec74a0ce01f471fbbb4ea91ff6851a3d2349a807aa75b3ad46a59d5e49
- Both --version commands executed successfully, exit 0, printed '1.0.0-dev (build 1, commit 9daa0aa)' and 'built with AppleClang 13.0.0.13000029 for Darwin x86_64'.
- An earlier attempted /usr/bin/timeout wrapper did not exist on macOS 11, so it was not a launch proof. Subsequent direct --version checks passed.

## Safety/resource gate
- Swap before build 4.25 MiB; after build 624.75 MiB of 1,024 MiB allocated; post-version remained 624.75 MiB; free memory percentage 77% at post-build sample.
- Material swap growth; causation not proven. Fail closed: no model transfer, no inference, no benchmark; further admission requires independent stabilization check and bounded process guards.
- iMac was sampled read-only: swap used 5,589.50 MiB out of 7,168 MiB, free memory percentage 81%. This alone does NOT admit a trustworthy independent Judge.
- Windows and protected runners untouched; iMac AI inference prohibited.

## Candidate GGUF — READ-ONLY REJECTION FOR COMMERCIAL WORKER
- Existing iMac Ollama manifest 'qwen2.5/3b' model layer size 1,929,903,008 bytes, magic GGUF (47 47 55 46), manifest model digest sha256:5ee4f07cdb9beadbbb293e85803c569b01bd37ed059d2715faa7bb405f31caa6.
- **Observed license layer** is 'Qwen RESEARCH LICENSE AGREEMENT' with explicit non-commercial limitation and separate license requirement for commercial use. No permission for commercial deployment inferred. Full model file was not independently rehashed in this experiment, quantization metadata and full provenance not certified; do not call it an admitted model.
- No model copied or downloaded onto MacBook.

## Unrun gates and formal decision
- Judge freeze/positive/negative tests: NOT_RUN.
- CASEIFICIO_ORDINI_001 atomic and 16 original tests: NOT_RUN.
- MacBook inference, coding accuracy, throughput and adoption: NOT_RUN / NOT_PROVEN.
- GitHub Actions: NOT_USED. No cloud compute, no paid API or purchases.
- GitHub is trusted publisher, separate from worker device; worker received no GitHub credentials from this action.
- Scoped outcome: SOURCE_PINNED_PASS, CPU_CONFIGURE_PASS, MACHO_BUILD_PASS, EXECUTABLE_LAUNCH_PASS; REPRODUCIBILITY_STOP_UNPINNED_UI_ASSET, RESOURCE_ADMISSION_STOP_SWAP_GROWTH, MODEL_LICENSE_STOP, JUDGE_NOT_ADMITTED, OVERALL_NO_GO.
- This is an observation report, not a SHA-bound receipt produced by an independent on-device Judge. No independent Judge receipt claimed.
