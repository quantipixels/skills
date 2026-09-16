# Guidance simplification rebuild

The user authorized reconstructing the accepted simplification after the earlier cloud candidate could not be transferred. Baseline: `3f04bcf57e8d4f05659517f59b7c5e73ff37dae6`. This record covers the local reconstruction; the handoff's earlier trials are not proof of this candidate.

## Acceptance and bounded comparison

Retain the 18 public skills and ten first-party playbook files, preserve invocation permissions, and add only explicitly invoked `qp-update`. Remove discoverable exposition and duplicated procedure while preserving deep-module design, independent owner use, authority, recovery and completion boundaries. The file-level plan proposes 27 supporting-file removals; disposition counts are descriptive, not acceptance quotas.

The intended comparison used the existing `reuse` Python/SQLite/API/admin/worker task and independent oracle with frozen baseline and candidate guidance, model `gpt-5.6-sol`, reasoning `high`, and assignment budgets of 600 seconds and 12 tool calls. One attempt ran per guidance condition; no-guidance controls remain unrun. Collaboration dispatch limits forced the candidate onto an ephemeral Codex CLI host, so host conditions were not held constant. Both original runs were invalid; no paired execution or performance conclusion is available.

Use C09 and C10 for matched decision probes (20 requests per revision), and C11 for the updater's eight installation states. These measure proposed choices, not executed engineering or update workflows. Actor assignments exclude private oracles and other answers; the native host does not provide enforced filesystem isolation or hard per-actor tool budgets here. Record observed violations or overruns rather than treating assignment text as enforcement.

## Mechanical evidence

The engineering harness now accepts a frozen guidance root while preserving tasks and oracles. Regression checks compare protected inputs across roots, check copied guidance identity and tamper rejection, and reject a missing skill before creating a study.

The existing timeout tests failed on the unchanged baseline under macOS/Python 3.14: process-group probing could encounter `EPERM` for an unreaped exited leader and misclassify timeout as execution error. The correction reaps the leader before group probes, waits after forced termination, and closes owned pipes on fallback/error paths. The full 34-test engineering suite passed with ResourceWarnings enabled and no warnings; the session-evidence regression also passed. Independent review reran four focused cleanup tests. An additional tracemalloc-instrumented attempt exceeded an existing test's short fixture-startup window; the normal warning-enabled suite passed.

## Invocation policy basis

`qp-update` uses Codex's `policy.allow_implicit_invocation: false` and Claude's `disable-model-invocation: true`, with user invocation available. Their semantics were checked against [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude's skill documentation](https://code.claude.com/docs/en/skills) on 16 September 2026. Metadata inspection is not a native invocation trial.

## Current state

The final skill/harness candidate is `7ef5672`. Independent review accepted it after repairing two findings: process cleanup completeness and preservation of HTML renderer provenance/licensing. All existing skill frontmatter and invocation YAML are unchanged; the ten playbook files are byte-identical to baseline. Repository-relative Markdown links resolve and `git diff --check` passes. The package has 115 tracked files (140 minus 27 removed references plus the updater's two files). Packaged Markdown has 37,481 whitespace-delimited words versus 67,609 at baseline, including the new updater: 44.6% less source text, not a measurement of tokens, loaded context or runtime savings. A generic skill validator rejects pre-existing metadata keys in three unchanged skills; direct YAML/name and metadata-preservation checks passed.

The fresh baseline `reuse` actor delegated API pause/resume to the existing persisted hold/release owner, but placed its new test at the actor root outside the permitted `workspace/` boundary. The checker correctly returned `invalid` for the unexpected file (and its root cache). The actor's reported local passes do not override that rejection; its artifacts were not repaired or relabelled. Baseline control remains `unrun`. A valid paired execution comparison is therefore unavailable from this attempt.

The fresh candidate likewise reused the persisted owner and placed its changes and tests inside `workspace/`. Unexpected actor-root `.tldr` files caused the checker to reject the original run. The trace contains no tldr command; host hooks are the likely source. Original artifacts and the invalid verdict remain intact. A separate, explicitly labelled artifact replay copied only `api.py`, `test_api_pause_resume.py` and `RESULT.md` into a newly prepared study. That replay passed returned tests, independent feature/owner/legacy/admin/rejection oracles, and original baseline tests; its new test failed against the original implementation. This proves the returned code's bounded behavior, not a successful fresh actor run. An initially incomplete replay record was rejected for missing host metadata; the complete replay record and second checker output are retained.

Local execution locators: `/tmp/qp-rebuild-baseline-checks-20260916.json`, `/tmp/qp-rebuild-candidate-checks-20260916.json`, and `/tmp/qp-candidate-artifact-replay-checks-v2-20260916.json`. Candidate trace: `/tmp/qp-rebuild-candidate-native-trace-20260916.jsonl`. CLI-reported usage was 263,789 input tokens (including 226,432 cached) and 4,506 output tokens; ten tool operations were observed. These single-host totals support no comparative cost or latency claim. Other unmeasured usage remains unknown. Temporary evidence is local and is not included in the installable package.

The baseline C09/C10 probe's 20 answers and candidate C11 updater probe's eight answers were inspected against their decision boundaries. No material authority/evidence failure or unsafe update choice was observed. The candidate C09/C10 CLI probe read global installed Alárinà/Ọ̀rọ̀ guidance before reading its assignment, violating the supplied-guidance-only boundary. Its answers can inform diagnostic inspection only; they cannot validate an isolated candidate comparison. The initial CLI attempt without user configuration failed authentication before actor work; the configured-host attempt is separately traced at `/tmp/qp-candidate-decision-trace-v2-20260916.jsonl`. These are decision-only observations, not executed workflow or native-update proof.

The living HTML plan rendered successfully; the theme toggle, local anchor integrity and 390px page overflow check passed. A deep link to a skill initially left that target's own details closed; the local HTML now opens the target as well as ancestor disclosures, and a browser recheck passed. This does not establish observed reader comprehension or a full accessibility audit.

No live installation, real update, JVM integration or valid comparative resource measurement has been performed. Publication is separate from these verification claims.
