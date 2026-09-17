# Executable engineering comparisons

Use this opt-in standard-library kit when the question requires actual coding outcomes. For ordinary instruction checks, start with the [simple prompt recipe](../README.md). The native host runs models; this kit freezes tasks, checks returned artifacts and summarizes evidence.

## Select a bounded profile

| Profile | Cases | Prepared cells |
| --- | --- | --- |
| `historical` | Settlement retry/legacy data and partial batching | Control/guidance pairs, two repetitions: eight cells |
| `existing-code` | Settlement repair and collection API reuse | One pair per case: four cells |
| `playbooks` | Project verification, populated-data migration and profile interpretation | One pair per case: six cells |

Choose `--profile` explicitly; preparation no longer silently selects an eight-cell study. Use repeated `--case` options to narrow it. The historical profile preserves the original study shape; preparing it does not recreate that study's model evidence.

```bash
python3 evals/engineering/evaluate.py prepare \
  --profile existing-code --case reuse \
  --output .qp/alaga-engineering/reuse-1 \
  --host native-host --model exact-model-id --reasoning medium \
  --max-seconds 600 --max-tool-calls 12
```

Use `--guidance-root` to supply an exact skills directory. Required guidance is validated, hashed and copied before study creation; the manifest identifies protected inputs and permitted edits. Give actors only their `actor/` directory, keeping `private/` and judging criteria inaccessible through host isolation where available. Record assignment-only separation honestly; these directories are not a sandbox.

Use `adanwo`'s [agent-evaluation method](../../skills/adanwo/references/agent-evaluation.md) for experimental controls and outcome judgment. Enforce the declared actor budget in the native host with no automatic retries. The checker's `--timeout` bounds each local subprocess, not model execution.

## Record and check

After an attempt, keep its trace outside `actor/`, copy `record.template.json` to `record.json`, and fill available provenance and measurements. Use `model-run` only for actual runs; it requires matching frozen host/model/reasoning, a trace locator and boolean `isolated_host_sandbox`. Historical artifacts use `replay`; harness probes use `mechanical-validation`. Unknown measurements stay unknown.

```bash
python3 evals/engineering/evaluate.py check \
  --study .qp/alaga-engineering/reuse-1 \
  --output .qp/alaga-engineering/reuse-1-checks.json
python3 evals/engineering/evaluate.py summary \
  --study .qp/alaga-engineering/reuse-1 \
  --checks .qp/alaga-engineering/reuse-1-checks.json \
  --output .qp/alaga-engineering/reuse-1-summary.json
```

The checker executes trusted returned Python in disposable copies. POSIX subprocess groups receive bounded termination and descendant cleanup; other hosts get direct-child cleanup only. Use host isolation for untrusted code.

| Gate | Required evidence |
| --- | --- |
| Repair | Nonzero passing returned tests, passing independent acceptance, returned tests that assertion-fail against the original, and preserved baseline tests |
| Additive reuse feature | Passing candidate tests, full acceptance and baseline tests; the frozen `reuse-actions` probe must pass the candidate and specifically reject both missing original API actions |
| Profile artifact | Capture-derived oracle passes the candidate and rejects the original overconfident diagnosis; returned code tests are not applicable |
| Input integrity | Protected task, prompt, guidance, fixtures and private oracle stay unchanged; unexpected files or symlinks invalidate the cell |

The feature probe recognizes only `ValueError("unknown action")` from valid-account dispatch as the explicit missing-action assertion. Other original-runtime errors remain diagnostics, never regression proof. Import/setup errors, assertion failures, zero tests, timeouts and cleanup failures remain distinct.

No record or result on an untouched cell means unrun; partial submissions are incomplete. Reports preserve every selected cell, record kind and isolation limit. A zero checker exit means the report was written, not that all cells passed. Summaries reject changed inputs and stale checked artifacts and never infer a winner from pass counts.

## Case boundaries

- Settlement and batching preserve the historical Python/SQLite contract, defective originals and baseline tests.
- Reuse checks persistence/reopen, legacy values and API/admin/worker interoperability. Inspect diffs separately for unnecessary machinery and actual reuse.
- Verification checks a real local CLI-over-HTTP journey. The oracle owns service lifecycle and hidden SQLite state; this does not test actor-authored lifecycle management or hostile same-user isolation.
- Migration checks sparse identity relationships, exact mapping, schema/version state, idempotent reopen and unsupported-version rejection.
- Profile uses synthetic weighted stacks, not a native capture. A hotspot does not establish root cause.
- [Project-backed scenarios](scenarios/README.md) cover real framework, compatibility, interruption, authorization, resource and architecture boundaries. They are protocols, not runnable profiles or completed trials.

Historical results remain in [observations/](observations/). Preparation, replay and mechanical checks make no fresh model-performance claim.
