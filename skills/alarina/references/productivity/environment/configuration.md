# Configuration and deterministic mechanics

Use during setup, when resolving a record destination, or when repeatable local verification/workflow tooling is needed. Resolve the installed script from the loaded `SKILL.md`; core operations need Python 3.10+ and no third-party Python package. The optional `ci-drift` operation uses project-provided PyYAML to parse actual workflows and reports a missing dependency without installing it. Local check process isolation currently requires macOS or Linux; use the project's native runner on other platforms. Commands, policies and workflows own judgment. The utility owns bounded mechanical results.

## One configuration contract

Optional JSON files declare only values consumed by the utility:

| Owner | Location | Allowed fields |
| --- | --- | --- |
| Personal | `~/.qp/alarina/config.json` | `version`, `state_root`, `contribution_suggestions` |
| Shared project | `<repository>/.alarina.json` | `version`, `doc_root`, `checks`, `required_tools`, `remote_checks`, `policy_sources`, `workflow_roots` |
| Personal to this checkout | `<repository>/.alarina.local.json` | `version`, `state_root`, `contribution_suggestions` |

Every file has `"version": 1`. Defaults apply first, then personal, shared project and checkout-personal values. Personal layers cannot replace team checks, standards pointers or the team's document fallback. Ignore `.alarina.local.json` in version control when using it. Unknown fields, duplicate JSON keys, unsupported versions and unsafe paths fail closed. An absent file uses defaults; an invalid file does not.

Settings hold mechanical inputs, not a second policy hierarchy. Read the actual instructions and linked standards. `policy_sources` makes existing owners discoverable; it does not copy or reinterpret their rules. User instructions and project/host authority govern conflicts. Models, reasoning, subagent preferences, permissions, secrets, merge rules and deployment authority are not configuration keys; keep them in the existing `AGENTS.md`, equivalent host instructions and enforced provider settings.

For shared paths (`doc_root`, `policy_sources`, `workflow_roots`, check working directories and JUnit reports), use repository-relative paths. Reject `..`, absolute paths, Git metadata, project-root document storage and symlink escapes. Personal `state_root` is an absolute path or starts with `~/`; the resolver always appends project/worktree/task namespaces. Its default is `~/.qp/alarina`. The personal config file itself stays at the fixed discovery location even when the state root changes.

`doc_root` defaults to the isolated task's `artifacts/` directory described by [records](../records.md). An explicit current-request path or established owner takes precedence. An override for new deliverables does not relocate project standards or private task state.

## Register real project checks

Example `.alarina.json` for a Python project; use the project's actual runner and commands. It leaves `doc_root` unset, so the record policy determines the destination:

```json
{
  "version": 1,
  "policy_sources": ["AGENTS.md", "CONTRIBUTING.md"],
  "checks": [
    {
      "id": "unit",
      "argv": ["python3", "-m", "unittest", "discover", "-s", "tests"],
      "cwd": ".",
      "timeout_seconds": 300,
      "proof": {"type": "unittest"}
    }
  ],
  "required_tools": ["python3", "git"],
  "remote_checks": ["Hosted deployment smoke check in the isolated preview environment"],
  "workflow_roots": ["docs/engineering/workflows"]
}
```

Register existing working checks and policy files only. Do not add placeholder commands or claim an illustrative configuration is ready. Set `"doc_root": "docs/reports"` only if that is the project's chosen fallback for new human deliverables; it means `<repository>/docs/reports`, and explicit destinations and established owners still take precedence. The example's workflow root is also a choice, not a required destination.

Each check requires a unique `id`, literal `argv` array and explicit `proof.type`. Optional `cwd` defaults to the repository root; `timeout_seconds` defaults to 300 (1–3600). The runner invokes commands directly with no shell interpolation. A deliberately configured shell can still execute shell code: inspect the command and its effects before authorized execution. Prefer native argument arrays. Configuration presence never grants runtime, network, installation or destructive authority.

The runner owns the check's process group until completion and cleans it on success, timeout or interruption. Keep long-lived services in the project's verification lifecycle with explicit start/readiness/teardown ownership; do not depend on a background child surviving a completed check. Processes that deliberately detach into a new session need project-owned cleanup.

| Proof type | Mechanical meaning |
| --- | --- |
| `exit` | A command exited successfully. Suitable for lint/build/structural checks; no test-count claim. |
| `unittest` | Python unittest summaries with positive passing-test counts. |
| `pytest` | Pytest result summaries with positive passing-test counts. |
| `tap` | A complete top-level TAP plan and matching results. |
| `junit` | A freshly produced XML report at the project-relative `proof.path`, with consistent testcase outcomes. |

Test proof rejects zero selected/all-skipped tests, failures and malformed or stale summaries. Counts establish execution, not useful assertions or whole-product acceptance. Other runners should emit JUnit or use their own maintained evidence adapter; do not relabel tests as `exit` to hide missing execution proof. Required live journeys, independent review and genuinely remote proof retain their own owners.

For coverage against CI, use [CI/local equivalence](../../engineering/verification/ci-local-equivalence.md). A complete configured gate can omit a relevant CI obligation. Neither `doctor` nor a passing receipt proves that the inventory is adequate, that another operating system passed, or that independent review occurred.

## Inspect, execute and recheck

```sh
python3 <alarina-directory>/scripts/alarina.py config --project <checkout> --task <stable-task-id>
python3 <alarina-directory>/scripts/alarina.py doctor --project <checkout> --task <stable-task-id>
python3 <alarina-directory>/scripts/alarina.py verify --project <checkout> --task <stable-task-id> --base <integration-base>
python3 <alarina-directory>/scripts/alarina.py freshness --project <checkout> <receipt.json> --base <current-integration-base>
```

`config` returns effective values, source files and record locations. `doctor` checks declared paths/executables and reports missing local gates; it never runs project commands, installs tools or calls a configured service. Its `configured` status means discoverable prerequisites, not a verified project. Package-script suggestions are unexecuted leads.

`verify` runs registered gates once and saves private logs and a receipt under the task's `checks/<run-id>/`. Use `--check <id>` repeatedly for an affected subset. Successful selected checks return `selected_status: passed` and `gate_status: partial`, with exit 0 for the requested subset; omitted checks remain visible and the result cannot stand for the full gate. Only a successful complete configured gate returns `gate_status: passed`. `--output <new-directory>` explicitly chooses another run destination. Existing output is never overwritten. Output inside the project must be ignored and untracked so evidence cannot change the candidate it describes. Retain required evidence before temporary-run cleanup.

Receipts bind executed checks to the configuration digest and Git candidate (HEAD, selected base, index, tracked/untracked contents and modes). Candidate changes during execution invalidate the combined result. `freshness` compares current state; it does not turn a failed run into a pass or replace independent review. Ignored/generated artifacts, submodule interiors, external environments and changed requirements need their applicable proof. Non-Git checks can run, with missing candidate guarantees explicit.

Commands return JSON. Exit 0 means the requested mechanical operation succeeded; 1 means reported gaps, failed/incomplete checks, stale evidence or inspection findings; 2 means invalid input or a blocked operation. Inspect the result and its limits. A successful command never authorizes publication or establishes standards compliance.

## Continuity and CI facts

When resuming prior work, use the native host's scoped history/search to select the relevant existing task and record. The read-only inspector then checks those explicit sources and receipts against the current checkout:

```sh
python3 <alarina-directory>/scripts/alarina.py resume-inspect --project <checkout> --record /absolute/existing/plan.md --receipt /absolute/checks/receipt.json
```

Repeat `--record` or `--receipt` for relevant sources, or supply the existing `--task` identity to locate its private `plan.md`. Missing records remain gaps; explicit alternatives can still be inspected. Goal/scope/next-action excerpts remain attributed historical claims, and linked chat IDs are leads. The inspector does not search unrelated history, select a task by recency, infer authority or convert a stored worker ID into observed live state. A current failed/partial receipt remains failed/partial. Files and state are never written.

For CI reconciliation, inspect real workflow bodies with the optional YAML parser and optionally fetch current GitHub branch rules through `gh`:

```sh
python3 <alarina-directory>/scripts/alarina.py ci-drift --project <checkout> --repo OWNER/REPO --branch BRANCH
python3 <alarina-directory>/scripts/alarina.py ci-drift --project <checkout> --baseline /absolute/prior-ci-inspection.json
```

The JSON output can be retained at the existing verification record. Comparison reports changed inventories, workflow content and provider facts, with conditions, matrices and unresolved reusable workflows visible. Literal command matches are navigation leads, not executed coverage. Missing provider access remains unknown; observed empty requirements are distinct. The owner traces wrappers, conditional paths and product obligations before accepting equivalence or changing checks. Without `--repo` and `--branch`, no network is used. Exit 1 means attention or drift; exit 2 means invalid or unavailable inspection. Neither is a reason to weaken a check.

## Existing-container verification

Use the existing running container's actual hex ID, mounted checkout and container-side verifier path:

```sh
python3 <alarina-directory>/scripts/alarina.py verify-container --container HEX_ID --project <checkout> --workspace /work/project --runner /work/project/skills/alarina/scripts/alarina.py
```

The adapter requires exactly one existing `.devcontainer/devcontainer.json` or `.devcontainer.json`, a complete Git candidate, Python 3.10+ and a writable bind mount of this checkout. It records config, runtime, mounts and runner identity, invokes the existing full verifier, compares host/container source inventories and executable bits, and checks receipt freshness. Read/write permission differences are tolerated. A runner outside the workspace needs `--expected-runner-sha SHA256` from a trusted installation. The runner's dependent modules and configured checks remain trusted project inputs; a matching entry-file digest is not a sandbox or code review.

The configured gate must already work inside the container. Its fresh run output goes below the checkout's ignored `.qp/container-verification/`; the existing runner rejects tracked/unignored evidence. Preserve the returned receipt and environment JSON through the usual evidence owner. The adapter never creates, starts, rebuilds or stops containers. On client timeout, container-side check state is unknown; inspect the named container and run directory before retrying. Native macOS/Windows and hosted identity/signing remain separate proof. This adapter requires a POSIX host and container; use the native project verifier on unsupported platforms.

## Personal preferences

```json
{
  "version": 1,
  "state_root": "~/.qp/alarina",
  "contribution_suggestions": true
}
```

The suggestion preference defaults to `false`. Enabling it permits an occasional relevant suggestion under [contribution guidance](../contributing-improvements.md), not transmission or background mining. Use the [user-owned delegation example](delegation-example.md) for model preferences instead of adding a model roster to this file.
