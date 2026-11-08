# G0-SHADOW preflight — immutable source and measurement rules

Status: **CANDIDATE / NOT DISPATCHED / PHYSICAL EVIDENCE NOT RUN**. Subordinate to `lukeeterna/venture-os/docs/fabric/CANONICAL.md`; not a new VOS authorization or protocol.

## Exact base provenance
- Shadow repository: `lukeeterna/g0-shadow-neutral`
- Starting Git commit SHA-1: `3122adada48afab564362e5d1c4f6238490f0193`
- `base_sha` in VOS mandate: `4918568f03feaef0444f009be12112af077f78a524c19853aae7bc3920b199d1` (SHA-256 **of the domain-separated Git commit identifier**, not the native Git commit hash or the full tree contents).
- Derivation uses the UTF-8 bytes of EXACTLY this string, including final LF:
```text
VOS-G0-SHADOW-BASE-V1
repository=lukeeterna/g0-shadow-neutral
git_commit_sha1=3122adada48afab564362e5d1c4f6238490f0193
```
- Formula: `sha256(the bytes above)`. Keep both identifiers; never represent SHA-1 as a 64-character Git commit.
- A full source/tree integrity proof would additionally require independently fetching the exact Git commit and files, then preserving their blob identities.

## Intake and guardrails
- Staged candidate is at `experiments/G0-SHADOW-PREFLIGHT-20261108-001/inbox/G0-SHADOW-PREFLIGHT-20261108-001.json` on `experiment/g0-frontier-local-judge-20261108`.
- **This is NOT the live VOS inbox.** Original VOS ingress reads `lukeeterna/venture-os/control/inbox/<mandate_id>.json`; no live central inbox entry has been published as part of this preflight.
- No project manifest or engineering plan has been certified on the iMac; `WAITING_PROJECT` / `WAITING_PLAN` are possible, not claims of observed runtime status.
- The malformed prior candidate `experiments/G0-FRONTIER-LOCAL-20261108-001/mandate.json` is preserved unmodified as a regression case.
- No GitHub Actions workflow dispatch, no PR representing worker output, no worker emulation, no install, no production effect, no API purchase. The original manually gated G0-SHADOW workflow remains untouched.

## Physical experiment and required timestamp log
This experiment must NOT be marked PASS based on GitHub-only results. On the authorized physical iMac, with an already qualified VOS installation and no effect on FLUXION/ARGOS, independent receipts must record:

1. `preflight_utc`, `preflight_monotonic_ns`, physical host/model/OS, active launchd bridge identity and exact installed VOS runtime SHA, and any STOP reason.
2. Idle samples: at least 5 pairs (`utc`, `monotonic_ns`) with CPU, RAM, swap, bridge `control_sync/latest.json` sequence and `synced_at_utc`.
3. Local model-load samples: the same metrics, with Ollama localhost model digest and actual response `eval_count`, `eval_duration`, `load_duration` and `total_duration`. No model pull; if no safe model already installed, `STOP_LOCAL_MODEL_NOT_AVAILABLE`.
4. Bridge ingestion: record exact control commit, mandate and plan digests, before/after bridge receipt, idempotent replay, and time from commit to actual receipt. No inferred latency from the nominal polling interval.
5. Energy: real plug-meter before/after watt-hours if available; otherwise `INCREMENTAL_KWH=UNKNOWN` and `MEASUREMENT_INSTRUMENT=NONE`. Calculate operating cost only from measured consumption and explicit electricity tariff.
6. Terminal receipt: JSONL/JSON with exact source SHA-256, timestamps, sampler versions, per-phase counts, RED/STOP/PASS values and a digest of the receipt bytes.

Maximum additional paid/API charges: 0. Benchmark data is not production certification. If isolation, authority, process limits or exact identity is not proved, STOP.
