# Retain and reuse learned workflows

Use when a retrospective finds a useful custom path worth repeating, or an uncovered task obligation may be served by a proven path. Keep project-bound recipes in the current project's library resolved by [records](records.md). The separate portable library is for explicitly qualified cross-project guidance. Never mix private recipes from unrelated projects in one global directory.

## Earn retention through use

Retain a workflow when actual execution reached its expected outcome with relevant proof, it contains a useful reusable choice or sequence, and existing methods do not already express it sufficiently. A plausible plan, a worker's success claim or a passing structural check alone does not establish that the workflow worked. One supported execution can justify a narrowly scoped recipe; broader applicability or improvement claims need their own evidence. Keep untested ideas as recommendations rather than promoted workflows.

After completing retrospective judgment, ordinary retrospective scope permits this bounded private knowledge capture. An explicit read-only, no-write or recommendation-only request still controls. Saving a workflow does not authorize changing project policy, modifying the skill, executing the recipe, installing tools or publishing it. Those actions retain their existing owners and authority.

Use a descriptive filename and the [recipe contract](templates/workflow-recipe.md): a first `alarina-workflow+json` fenced block followed by concise Markdown guidance. Keep outcome, scope, assumptions, method pointers, prerequisites/results, executed evidence, limits and retirement conditions. `draft` is an unproved candidate; `verified` requires an actual passing execution and its candidate/evidence locator; `retired` requires a reason and must not be selected for new work. The structural validator does not decide whether evidence is true or sufficient.

Prefer method pointers plus custom choices over copied instructions. A pointer must resolve to the actual current method; read its body and conditional references before use. A title, description, historical success or passing schema is not proof of current fit. Retain who owns each result, authority for external effects, accepting observation and recovery/cleanup path in the useful prose. Success in one project does not make a recipe portable. Keep private evidence private and omit secrets and transcripts.

Before saving, inspect relevant recipes and update the same owned recipe instead of creating a near duplicate. Reusable recipes use the metadata contract; ordinary project documents and task notes do not become workflow records. When collaborators need a recipe, use its shared project owner and configure that specific `workflow_roots` directory; the private copy must not become competing authority. Return its locator, scope and evidence. Do not create a separate registry, lifecycle service or history sweep.

## Discover and adapt to the current goal

The active owner can retrieve a relevant learned path when starting/resuming familiar work, choosing a consequential approach or investigating repeated failure; no user command is required. Use a known project pointer or the scoped inventory below only when it can affect that decision. Reuse a still-current discovery result during the task. After a bounded retrospective establishes a useful new path, retain or update it under the evidence and authority rules above, rather than waiting for the user to remember a separate save command.

Follow a known relevant recipe directly. For an identified gap, use scoped discovery:

```sh
python3 <alarina-directory>/scripts/alarina.py workflows --project <checkout>
python3 <alarina-directory>/scripts/alarina.py workflows --project <checkout> --path <recipe.md>
```

The inventory reads only the current project's private library, the explicitly portable library and declared project roots. Project libraries require `scope: project`; the portable library requires `scope: portable`. Misfiled recipes are invalid and are not offered as guidance. Missing optional directories are normal. Duplicate IDs, malformed records and symlink traversal are surfaced; resolve duplicates with their owners before selecting one by accident. Use an explicit `--root` only for an intended additional library; this explicit inspection has no inferred library scope. Do not scan other projects or all user history to fill a current gap.

Check its assumptions, authority, tool availability and proof against the current task. Reuse the useful parts, combine them with other commands or references, and retain the task owner's completion boundary. A historical success does not verify today's result or require replaying every step. Do not execute a saved workflow merely because it was discovered.

When reuse or a retrospective reveals a correction, narrower applicability or a retirement condition, revise the same recipe within write scope and rerun affected proof. Mark unsupported paths `draft` and obsolete paths `retired`; preserve useful provenance until dependent work no longer needs it. Deletion needs applicable authority. Ordinary success needs no append-only log.

## Compose, adopt and automate

Steps are reusable result contracts, not an executable agent roster. Connect a producer's actual `produces` evidence to the next step's `requires`, keep one initiative owner, and preserve each command's narrower authority. A custom sequence is usable without creating another public skill. Project-specific scripts should stay with the project until a stable cross-project contract earns packaging.

Before broader adoption, replay from documented setup, include a credible failure/recovery case, and check that evidence survives cleanup. Record the proved environment and limitations. At a later maturity boundary, compare useful outcomes (escaped defects, human corrections, repeated effort and operational cost), not recipe count. Revise or retire paths that stop earning their maintenance cost.

Automation is a deployment of an already useful on-demand recipe. When the user requests it, use the host's native scheduler with a named project, scoped inputs, bounded work, existing authority, evidence destination, overlap/resume behavior and notification condition. Avoid duplicate jobs; quiet unchanged results and report actionable failures. An absent durable host is a named capability gap. Do not implement a private scheduler or automatically install a recurring run.

For an enabled or requested upstream suggestion after useful local adoption, apply [contribution guidance](contributing-improvements.md). Prepare only curated, synthetic and reviewed material; recipe discovery never authorizes transmission.
