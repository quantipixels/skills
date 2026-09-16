# Engineering playbook comparisons

This standard-library kit prepares bounded control/QP-guidance comparisons without making model or network calls. It contains no provider registry, credentials, SDK, or agent framework.

Use `prepare --guidance-root /path/to/frozen/skills` to compare source revisions with the same tasks, prompts, fixtures and oracles. Prepare a separate study per revision with matching host settings; the chosen directory must contain the case's required skill packages. Each guidance arm freezes and protects their copied content. `source_revision` identifies the harness checkout, `guidance_source` records the input location, and each run's protected hashes identify the actual guidance. A path or Git label alone does not attest its contents. Keep controls and incomplete cells visible, and distinguish decision probes from executed tasks.

For framework invocation, mixed-version compatibility, abrupt recovery, authorization across callers, measured resource cost and architecture alternatives, use the [project-backed scenario protocols](scenarios/README.md). These require prepared real project environments and independent acceptance probes; they are not executable harness profiles or completed model trials.

The opt-in `existing-code` profile pairs the two existing-code coding trials: settlement repair and collection API reuse. It prepares four cells, one control and one current-Alága arm per case, with opposite arm order across cases. Historical screening observations in `observations/` remain separate from newly prepared studies; preparing a profile does not create model-performance evidence.

The `reuse` task asks actors to find existing behavior under different terminology, preserve public domain values, and integrate API/admin/worker consumers. Its oracle checks persistence/reopen, legacy values, worker eligibility, admin interoperability, and rejection behavior. Inspect returned diffs separately for justified reuse and unnecessary machinery: functional acceptance does not prove implementation simplicity or complete consumer discovery.

Prepare this comparison explicitly:

```bash
python3 evals/engineering/evaluate.py prepare \
  --profile existing-code \
  --output .qp/alaga-engineering/existing-code-1 \
  --host native-host --model exact-model-id --reasoning medium \
  --max-seconds 600 --max-tool-calls 12
```

Use `--profile existing-code --case reuse` for just the additive-feature pair. Existing reuse test files are protected; actors may add focused root `test_*.py` files and edit the named production files. The feature gate requires nonzero passing candidate tests, passing full acceptance, and preserved baseline tests. A separate frozen `reuse-actions` probe must pass on the candidate and specifically assert both missing API actions on the original. Only `ValueError("unknown action")` from dispatch on a valid account becomes that explicit missing-behavior assertion; imports, setup failures, other runtime errors, and unrelated assertions cannot supply the proof. Full acceptance and returned tests also run against the original, where their expected runtime errors remain reported as `error` diagnostics. They are never relabelled as assertion failures or used as feature acceptance proof. The repair gate remains unchanged.

The default `historical` profile retains the completed eight-run Astra screening study shape: settlement retry/legacy-data compatibility and partial-batch preservation, each with control/current-Alága arms and two repetitions. The existing batching cells remain the ordinary implementation reference where an extra engineering method is not warranted.

Prepare all eight frozen cells from the repository root:

```bash
python3 evals/engineering/evaluate.py prepare \
  --output .qp/alaga-engineering/study-1 \
  --host native-host --model exact-model-id --reasoning medium \
  --max-seconds 600 --max-tool-calls 12
```

The opt-in `playbooks` profile prepares six cells, one control and one guidance arm for each new case:

```bash
python3 evals/engineering/evaluate.py prepare \
  --profile playbooks \
  --output .qp/alaga-engineering/playbooks-1 \
  --host native-host --model exact-model-id --reasoning medium \
  --max-seconds 600 --max-tool-calls 12
```

Use repeated `--case` options to run a smaller paired comparison, for example `--profile playbooks --case profile`. Selection never adds a case to the historical default.

The three playbook cases exercise different evidence boundaries:

- `verification` builds a reusable driver for a real local CLI-over-HTTP journey. The oracle owns protected service startup, restart, termination, and the hidden SQLite path. It inspects the protected service's request log and persisted item state after candidate-driven public write/read operations, while the candidate owns client-process and local-work cleanup. This bounded case does not test agent-authored service lifecycle logic or provide hostile same-user isolation.
- `migration` upgrades a populated SQLite snapshot whose sparse account IDs and insertion order differ from login order. The oracle checks exact relationship mapping, schema/version state, idempotent reopen, and rejection of an unsupported version.
- `profile` reduces a synthetic weighted-stack artifact into `diagnosis.json`. This controlled interpretation fixture is not a recorded native-profiler session. Its oracle derives quantities and source attribution from the artifact and requires an unproved diagnosis plus a probe that can distinguish one large parse from repeated parsing. A hotspot alone cannot pass as a confirmed root cause.

Guidance arms freeze the relevant installed guidance inside the actor directory: Alága plus Ọ̀rọ̀ for `verification`, Alága for `migration`, and Alága plus Irinṣẹ for `profile`. Control arms receive the same task and host settings without optional QP guidance.

Each run contains `actor/` and `private/`. Give the acting model only `actor/` and prefer a host-enforced isolated sandbox. If the host provides assignment-only separation, record `isolated_host_sandbox: false`; filesystem separation in this kit is not a security boundary. Keep the same host configuration and common instructions in both arms; only the guidance arm receives the case's frozen QP guidance. Each generated prompt names its editable source or evidence artifact. Executable cases also allow root `workspace/test_*.py` files; every case allows `workspace/RESULT.md`. The actor must not see the private original or oracle.

Enforce the manifest's per-run time/tool-call budget in the native model host and disable automatic retries. The `check --timeout` value only bounds each local test/oracle subprocess; it does not enforce the actor's declared model-run budget.

On POSIX hosts, each checker command owns a process group that is terminated on timeout and after completion. Other hosts receive direct-child cleanup only; use native host controls for descendant isolation and cleanup there.

After each attempt, save the trace outside `actor/`. Copy `record.template.json` to `record.json`, set `record_kind` to `model-run`, and fill actual provenance and available measurements. A model run requires the frozen host/model/reasoning values, a boolean `isolated_host_sandbox` disclosure, and a trace locator. Use `replay` for historical returned artifacts and `mechanical-validation` for harness probes; neither counts as fresh model evidence. Preserve failures and incomplete attempts. Do not relabel them or retry automatically.

Run the local checks and produce a summary at new paths:

```bash
python3 evals/engineering/evaluate.py check \
  --study .qp/alaga-engineering/study-1 \
  --output .qp/alaga-engineering/study-1-checks.json

python3 evals/engineering/evaluate.py summary \
  --study .qp/alaga-engineering/study-1 \
  --checks .qp/alaga-engineering/study-1-checks.json \
  --output .qp/alaga-engineering/study-1-summary.json
```

For repair cases, `check` runs returned tests, the independently frozen acceptance oracle, returned tests against the original defective implementation, and baseline tests against the candidate source in disposable directories. A successful repair requires nonzero passing returned tests, passing acceptance, an assertion failure against the original, and preserved baseline tests. For the `profile` evidence-artifact case, returned tests are explicitly not applicable; the corrected artifact must pass the capture-derived oracle while the supplied overconfident original fails it. Import/execution errors, assertion failures, timeouts, missing runs, and unrun runs remain distinct. Protected task, prompt, project fixture, raw evidence, guidance, or private-oracle changes invalidate the cell. On the native POSIX evaluation host, each checker command runs in its own process session; timeout and final cleanup terminate remaining descendants with bounded waits. Other hosts retain direct-child cleanup. This process ownership is resource hygiene, not a security boundary. The checker executes trusted returned Python; use the host sandbox for untrusted model-generated code.

A cell with neither `record.json` nor `RESULT.md` is unrun. If only one exists, it is incomplete; a valid record and its measurements remain in the report even when `RESULT.md` is missing. A zero exit from `check` or `summary` means the report was written successfully, not that every task passed.

The summary always includes every cell selected in the frozen manifest. The historical default therefore retains all eight cells. Summaries keep model runs, replays, and mechanical validations separate and list assignment-only and unknown-isolation cells as limitations. Those cells do not support a clean-room or causal claim. A summary does not select an arm from pass counts. Give the actual artifacts and available traces to an independent reviewer, hiding arm labels where feasible and disclosing any leakage, to assess correctness, unsupported causal claims, unnecessary machinery, explanation quality, interventions, and resource cost before making a comparative judgment. Unknown measurements remain unknown.

The historical fixtures and oracle retain the original study’s Python/SQLite provider contract, existing-data requirement, task text, defective implementations, baseline tests, and functional acceptance cases. The playbook fixtures are new evaluation inputs and have no claimed model results. The existing-code profile reuses the settlement and reuse fixtures without turning archived screens into fresh trials. This kit does not reproduce historical attempts as fresh trials or authenticate trace/model/billing claims.
