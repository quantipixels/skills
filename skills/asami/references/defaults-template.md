# Defaults file template

Write `~/.agents/AGENTS.md` (or the user's existing single source) in this shape. Keep it under about 40 lines or 4 KB. Delete any empty section.

```markdown
# My defaults

Rules that apply to all my work. Project facts live in each project's docs.

## How to talk to me
- <rule, one line>

## How to work
- <rule, one line>

## Proof and safety
- <rule, one line>
```

Rules:

- One line each, a plain instruction ("Give a short status at each milestone"), not a story.
- Keep the evidence (the quote, the date, the session) in the draft shown to the user, not in the file.
- No client names, hosts, data or secrets.

## Optional settings file

`~/.agents/qp.yaml`, written only when the user wants these defaults. Show the exact text first.

```yaml
models:            # override rows of asoju's model table by key, e.g.
  validator: { provider: claude, model: claude-opus-5-5, effort: medium }
specs: local       # local (records home) or git (docs/internal/specs)
tickets: local     # local (records home) or git (docs/internal/tickets)
plans: local       # local (records home) or git (docs/internal/plans)
docs: docs         # root for committed docs; internal/ and user/ go under it
sessions_keep_days: 90 # keep this many days of mined session history; default 90
```

## Pending proposals

`~/.agents/qp-pending.md` holds proposals the user has not answered yet. One block per proposal: the rule, the moment that shows it, where it came from (ironu, weekly run, manual), and the date. Remove a block when the user answers.
