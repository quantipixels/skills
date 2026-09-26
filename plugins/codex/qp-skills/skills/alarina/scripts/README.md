# Shared runtime scripts

These Python 3 utilities ship with Alárinà. Resolve their paths from the loaded `SKILL.md`; no launcher, installation step or third-party Python package is required. Run a utility only when its owning method calls for its result.

| Utility | Input and result | Method and limits |
| --- | --- | --- |
| [verify_artifact.py](verify_artifact.py) | One HTML file → structural diagnostics; exit 0 passes, 1 finds defects, 2 cannot read input. | [HTML Artifact](../commands/html-artifact.md) owns acceptance. No JavaScript execution, network access, semantic or visual verdict. |
| [session-evidence.py](session-evidence.py) | Local session stores and optional filters → JSON structural inventory on stdout. | [Session evidence](../references/ayewo-igba-ise/local-session-evidence.md) owns sampling and interpretation. Read-only; no raw transcript text in output and no inferred quality verdict. |

Keep one implementation per operation here so commands and playbooks can reuse it. Keep domain-specific interpretation, examples and limits with the owning reference. Repository build tools and tests belong outside this installed directory. Add code only for a valuable deterministic operation that existing tools do not already provide.
