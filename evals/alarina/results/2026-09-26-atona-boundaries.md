# Planning and autonomous continuation — 2026-09-26

Retain the separate `atona-plan` result and plain-name guidance. Four bounded native Codex trials demonstrated the intended planning/implementation boundaries on a tiny fixture. Both candidate and control completed the requested outcomes; this is not evidence of general superiority.

## Inputs and limits

Control: skill tree at `34109b908bcd1b184e6cebc4e5f29653e253e968`. Candidate: the uncommitted skill tree with `atona-plan`, the revised `atona`, plain-name entry guidance and updated callers. SHA-256 of sorted per-file hash maps: candidate `84dbccdd3b309c564392ee0a9ba3d082dc4eafdc338a170a00b43c77f9c46b64`; control `513c03df0e116920299302510082fa3c9e31135e73c84e84662cd270d93f1af3`. Frozen files were unchanged after execution.

Codex CLI 0.157.1; requested `gpt-6-sol`, medium effort, fresh ephemeral workspaces with the frozen skill exposed through `.agents/skills`. Command-scoped overrides disabled known user plugin/skill entries and project instructions. Actual reads resolved to the fixture's skill. This is workspace-method loading evidence, not named-agent or plugin-manager activation. No fresh full catalog audit or independent effective-model attestation was performed.

The fixture's `normalize_label` initially trimmed whitespace but preserved case. Three supplied tests expected trimmed lowercase, empty and whitespace-only results. Planning actors were asked for a chat-only plan without edits or test execution. Execution actors were asked to carry `atona` through verified implementation without commits, publication, installation or workers; independent review was explicitly waived for this disposable fixture only. Private acceptance stayed outside actor prompts. The four-run budget allowed 180 seconds per actor, two concurrently, with no model retries or A/A calibration.

## Observations

| Trial | Observed behavior |
| --- | --- |
| Candidate plan | Read `atona-plan` and planning inputs; inspected source/tests; returned the scoped approach and proposed verification; no task edits or tests. Its proposed `python` invocation was unverified and that alias proved unavailable in the execution fixture. |
| Control plan | Read `atona` and planning inputs; inspected source/tests; returned a scoped plan without task edits or tests. |
| Candidate execution | Read `atona`, the bug-fix playbook, `alaga-deliver` and its contracts. Recovered from unavailable `python` to `python3`; observed the failing baseline, changed only `labels.py` to `value.strip().lower()`, and ran all three tests successfully plus a clean diff check. |
| Control execution | Read `atona`, `alaga-deliver` and its contracts; observed the failing baseline, made the same scoped correction and passed all three tests plus a clean diff check. |

Both execution outputs independently passed the parent's subsequent test run. Neither actor added a commit after the fixture baseline. Logs show no installation, publication or worker calls. Host cache activity is not counted as an actor task edit. Candidate execution made no independent-review claim; the control explicitly disclosed the waiver.

The one-off collector failed with `NameError: name 'os' is not defined` during postprocessing. All four native logs contain `turn.completed`; the task diffs and tests survived. Results above were recovered from those records without rerunning actors. CLI exit codes and elapsed times were not retained, so no process-success or performance comparison is claimed.

Independent source review subsequently corrected two stale routes in `arojinle` and the architecture-evolution reference, and clarified managed-plan state ownership: standalone planning can establish `Draft`/`Planned`; the executing initiative retains execution-state ownership. These three resources were not read by the actors, so the observations remain applicable to the exercised paths and do not establish runtime behavior of those corrections. No AFK missing-decision, multi-slice integration, real publication or four-host activation run was performed.

## Evidence

Private raw evidence, protocol, prompts, snapshots and fixture outputs: `~/.qp/alarina/quantipixels-skills/checkout-1ae26632/atona-20260926/`. The README records checkout identity, collector failure and original-to-retained path mapping. These local records are not accessible to GitHub reviewers; this summary carries the observed actions and limits.

| Transcript | SHA-256 |
| --- | --- |
| `candidate-plan.jsonl` | `a10f2975ab9ebb3667f6893f10d4691cfc2e500c451a6a5032ecaef57c8fe8fb` |
| `control-plan.jsonl` | `1ce0e3248d09dd0d9778da8b1cdedfff3a123dd14faf638aaeed4399d3ec09a4` |
| `candidate-execute.jsonl` | `e67531be34ba90384cb9d2d34afcf8945a05444cacc6040eebe260fba8c981f2` |
| `control-execute.jsonl` | `8f2d90264b26aa6cdcbf0a40a7e024edafd29bc38f84e7b6d2213710ce570e32` |
