# Settings

Everything works without settings. Use them to change a default for one project or for all your work.

## Where settings come from

The first one found wins:

| Order | Where | Scope |
| --- | --- | --- |
| 1 | Your instructions to the agent (in the session, the project's instructions, or your personal defaults) | anything |
| 2 | `.agents/qp.yaml` in the repo | the project, shared with your team |
| 3 | `~/.agents/qp.yaml` | you, in every project |

Agents read whichever file exists and never create one unless you ask. `asami` writes `~/.agents/qp.yaml` for you after showing the exact text.

## Keys

```yaml
models:              # pick another model for a kind of work (keys below)
  validator: { provider: claude, model: claude-opus-5-5, effort: medium }
specs: local         # local (~/.qp) or git (docs/internal/specs); same for tickets and plans
tickets: local
plans: local
docs: docs           # root for committed docs; internal/ and user/ go under it
```

## Model keys

Each kind of delegated work has a key. Override any of them under `models:`; `race` takes a list of two.

| Key | Work | Default |
| --- | --- | --- |
| `build` | build, fix | Sol, xhigh |
| `writing` | writing for people, one-source research | Sonnet, medium |
| `design` | UI and interface design | Sonnet, medium |
| `design-new` | ground-breaking design | Opus, low |
| `judgment` | plans, judgment, review, conflicting evidence | Opus, medium |
| `validator` | checking flags, critiquing writing, scoring a fixed rubric | Opus, low |
| `independent` | judging work written by the lead's own model | Sol, xhigh |
| `cheap` | reading, scanning, exploring, running tests | Luna, medium |
| `cheap-browser` | driving a browser, Claude-only tools | Haiku, medium |
| `tests` | writing tests and evals | Sol, medium |
| `race` | prototype race | Sol xhigh and Opus low |

When a key's model is the model already leading your session, the lead does that work itself instead of handing it off, unless it needs an independent view, would flood the lead's context, or runs in parallel.
