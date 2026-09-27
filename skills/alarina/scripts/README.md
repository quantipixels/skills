# Shared runtime scripts

These Python 3 utilities ship with Alárinà. Resolve their paths from the loaded `SKILL.md`; no launcher, installation step or third-party Python package is required. Run a utility only when its owning method calls for its result.

| Utility | Input and result | Method and limits |
| --- | --- | --- |
| [alarina.py](alarina.py) | `config`, `paths`, `doctor`, `verify`, `freshness`, `workflows`, `contribution-check` → JSON results and meaningful exit codes. | [Configuration](../references/productivity/environment/configuration.md), [records](../references/productivity/records.md) and [learned workflows](../references/productivity/learned-workflows.md) own application. Only `verify` executes configured commands; macOS/Linux process isolation, no shell interpolation. Other operations are read-only. |
| [pr_snapshot.py](pr_snapshot.py) | Explicit GitHub repository/PR → paginated threads/comments/reviews/checks and head/base currency. | [GitHub snapshot](../references/engineering/delivery/github-snapshot.md) owns use; needs `gh` and authorized read access. No provider writes, feedback bodies or readiness verdict. |
| [verify_artifact.py](verify_artifact.py) | One HTML file → declared delivery profile and structural diagnostics; exit 0 passes, 1 finds defects (including missing delivery), 2 cannot read input. | [HTML Artifact](../commands/html-artifact.md) owns acceptance. No JavaScript execution, network access, semantic or visual verdict. |
| [session-evidence.py](session-evidence.py) | Local session stores and optional filters → JSON structural inventory on stdout. | [Session evidence](../references/engineering/retrospectives/local-session-evidence.md) owns sampling and interpretation. Read-only; no raw transcript text in output and no inferred quality verdict. |

Keep one implementation per operation here so commands and playbooks can reuse it. Keep domain-specific interpretation, examples and limits with the owning reference. Repository build tools and tests belong outside this installed directory. Add code only for a valuable deterministic operation that existing tools do not already provide.

`alarina.py` composes [project_context.py](project_context.py), [local_checks.py](local_checks.py) and [workflow_tools.py](workflow_tools.py). These modules own configuration/path validation, candidate-bound execution evidence, and scoped recipe/privacy inspection respectively. They are not separate agent commands. Python 3.10+ is required for these helpers. Full candidate inventories stay in private receipts; stdout contains compact identity and check results. A passing helper is neither semantic acceptance nor publication authority.
