# Alága engineering comparison

This standard-library kit prepares the same bounded comparison as the completed eight-run Astra screening study: settlement retry/legacy-data compatibility and partial-batch preservation, each with control/current-Alága arms and two repetitions. It makes no model or network calls and contains no provider registry, credentials, SDK, or agent framework.

Prepare all eight frozen cells from the repository root:

```bash
python3 evals/engineering/evaluate.py prepare \
  --output .qp/alaga-engineering/study-1 \
  --host native-host --model exact-model-id --reasoning medium \
  --max-seconds 600 --max-tool-calls 12
```

Each run contains `actor/` and `private/`. Give the acting model only `actor/` and prefer a host-enforced isolated sandbox. If the host provides assignment-only separation, record `isolated_host_sandbox: false`; filesystem separation in this kit is not a security boundary. Keep the same host configuration and common instructions in both arms; the treatment arm alone receives the frozen current `skills/alaga` guidance. The actor may edit only the task production source, root `test_*.py` files, and `RESULT.md`. It must not see the private original or oracle.

Enforce the manifest's per-run time/tool-call budget in the native model host and disable automatic retries. The `check --timeout` value only bounds each local test/oracle subprocess; it does not enforce the actor's declared model-run budget.

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

`check` runs returned tests, the independently frozen acceptance oracle, and returned tests against the original defective implementation in a disposable directory. A successful repair requires nonzero passing returned tests, passing acceptance, and an assertion failure against the original. Import/execution errors, assertion failures, timeouts, missing runs, and unrun runs remain distinct. Protected task, prompt, provider, guidance, or private-oracle changes invalidate the cell. The checker executes trusted returned Python with a timeout; use the host sandbox for untrusted model-generated code.

A cell with neither `record.json` nor `RESULT.md` is unrun. If only one exists, it is incomplete; a valid record and its measurements remain in the report even when `RESULT.md` is missing. A zero exit from `check` or `summary` means the report was written successfully, not that every repair passed.

The summary always includes all eight expected cells, keeps model runs, replays, and mechanical validations separate, and lists assignment-only and unknown-isolation cells as limitations. Those cells do not support a clean-room or causal claim. It does not select an arm from pass counts. Give the actual artifacts and available traces to an independent reviewer, hiding arm labels where feasible and disclosing any leakage, to assess unnecessary state/tables, compatibility and API scope, architecture, explanation quality, interventions, and resource cost before making a comparative judgment. Unknown measurements remain unknown.

The fixtures and oracle faithfully retain the original study’s Python/SQLite provider contract, existing-data requirement, task text, defective implementations, baseline tests, and functional acceptance cases. This kit does not reproduce the historical eight attempts as fresh trials or authenticate trace/model/billing claims.
