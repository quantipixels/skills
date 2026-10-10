# Models for delegated work

Resolve each task to a row. The user's or project's instructions win over every row, then the optional settings file (`.agents/qp.yaml` in the project, `~/.agents/qp.yaml` for the user), then this table. In the settings file, override a row by its key under `models:`, in the same shape as the settings example: `validator: { provider: claude, model: claude-opus-5-5, effort: medium }`; `race` takes a list of two.

The defaults are tuned for an Opus lead, but no row assumes one: each compares the row's model with the lead's.

| Key | Work | Model | Effort |
| --- | --- | --- | --- |
| `build` | Build, fix | Sol (`gpt-6.1-sol`) | xhigh |
| `writing` | Writing for people (docs, skill text, PR bodies, reports), one-source research | Sonnet | medium |
| `design` | UI and interface design | Sonnet | medium |
| `design-new` | New, ground-breaking design with no settled pattern to follow | Opus | low |
| `judgment` | Plans, judgment, review, synthesis of conflicting evidence | Opus | medium |
| `validator` | Validating positioned flags, critiquing writing, scoring against a fixed rubric (race or design pick), deduping findings | Opus | low |
| `independent` | Judge, validator, critic or peer of work the lead's own model wrote | Sol (`gpt-6.1-sol`) | xhigh |
| `cheap` | Readers, explorers, scanners, gauntlet workers; code and repo reading; harness and test runs | Luna (`gpt-6-luna`) | medium |
| `cheap-browser` | Browser drives (`preview_*`), screenshots, and tools only Claude has | Haiku (`claude-haiku-5-5`) | medium |
| `tests` | Writing and designing tests and evals (a `cheap` runner runs them) | Sol (`gpt-6.1-sol`) | medium |
| `race` | Prototype race for an abstraction, interface or feature, one version each | Sol and Opus | Sol xhigh, Opus low |

- **Same model as the lead: the lead does it.** When a row resolves to the lead's own model, the lead does the job itself. Delegate it anyway, at the row's effort, only when the job must be independent of the lead (a race entry the lead will judge, a peer to a verdict the lead froze), when it would flood the lead's context (then a `cheap` reader writes a record and the lead works from it), or when it runs alongside other work and time matters.
- `judgment` (medium or higher) stays on plans, conflicting evidence, root causes, security, money and data correctness, and anything that ships unchecked. `validator` at low is for narrow questions whose answer is checked afterwards.
- If Luna or Haiku is unavailable, use the other; if both are, use Sol or Sonnet at low and say so.
- On SIGIDI, confirm provider, model IDs and effort names with `orchestrator_capabilities` before the first launch. If a model is missing, use the closest one and say so. An explicit user pin is never swapped silently: ask or stop.
- Off SIGIDI, use the host's subagents and their model options (Claude Code subagents, Codex agents); map each row to the nearest option there.
- Report each child's requested and served model when the host shows it.
