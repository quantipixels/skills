# Default path, handoffs and save locations

## The default path

For "build X" and other end-to-end requests, run this path from the first step that is not already settled. You do not need the user to chain skills.

| Step | Skill | Hands on | Skip when |
|---|---|---|---|
| 1. Interview | `ibeere` | Settled decisions and open questions | Goal, scope and key choices are already clear |
| 1b. Ideas | `aba` | A direction the user picks | There is already a clear way forward |
| 2. Spec | `seda-spec` | What and why, with acceptance checks | The request already states these, or it is a small fix |
| 3. Prototype | `adanwo` | A direction the user confirmed (UI: three distinct versions; abstractions and interfaces: two raced versions) | Nothing about the experience, or about a critical abstraction or interface, is uncertain |
| 4. Plan | `atona` | How, in order, with risks | The change is small and obvious |
| 5. Tickets | `seda-ticket` | Vertical slices, each checkable on its own (wide refactors are the exception) | One slice covers it |
| 6. Build and test | `akole` (with `asoju` to hand slices to subagents; `ayewo` first when the cause of a failure is unknown; `iwon` when the claim is a measured gain) | Working change with proof | Never for code changes |
| 7. Real-surface proof | the project's verify skill (`ijerisi` creates or repairs it), `loowo` for a user-journey pass | Evidence on the running product | No user-facing surface changed |
| 8. Review | `atunwo` | Findings fixed or answered | Trivial change; the lead's own check is enough |
| 9. Pull request | `seda-pr` | A PR ready for the user's merge decision | The user did not ask to publish |
| 10. Reflection | `ironu` | A lesson kept only if it passes the bar | Nothing worth keeping, which is the usual case |

The path stops at the user's stop point: an answer; a plan; a change, which ends committed on a feature branch with its proof; or ship ("take it all the way"), which also runs review and opens the PR, or says what blocks it (for example no remote). It also stops at a decision only the user can make, and at anything on the do-no-harm list. Publishing, merging and deploying still need the user's go-ahead.

## Other paths

### Setup (new user, or moving from an older setup)

1. **Migrate**: if an older setup is installed (pepeye/pstack, the Alárinà plugin, older qp-skills), inventory what it installed and stored, show a plan of what moves, stays or retires, and after the user's yes back up, move and uninstall through each host's plugin manager.
2. **Retrospective** (`ironu`): over the last two weeks or month of sessions, the user's choice, using the reader and judge workflow below.
3. **Defaults** (`asami`): lessons about the user become a draft of their defaults; written only after a yes.
4. **Check the hosts**: a fresh agent on each host the user uses quotes one default and confirms the skills load.

### Reader and judge, and other model workflows

Long reads go to a cheap reader, and the expensive model works from its record (see `asoju`'s reader records). Use it whenever a step would otherwise read a large source:

| Work | Reader writes | Then |
|---|---|---|
| Review a large PR | change record | `atunwo` judges |
| Start in an unfamiliar repo | repository record | `atona` or `akole` |
| Incident or log diagnosis | logs record | `ayewo` |
| Research across many documents | docs record | `iwadi` |
| Session or period retrospective | session records | `ironu` judges |
| Migration | record of the old setup | the lead plans the move |
| Dependency or framework upgrade | changelog and usage record | `igbekale`, then `akole` |
| Explain a system to a person | explorers' slices | `komi` |
| Why something is the way it is | one investigator per source | `iwadi` synthesizes |
| Unsettled design or approach | race with a hidden rubric and a cross-judge | `adanwo` or `igbekale` |
| High-stakes review | two-model panel | `atunwo` reconciles |
| Large diff review | lens scanners flag, one validator | `atunwo` |
| Hard decision, second opinion | freeze own view, then one peer | the deciding skill |
| Many independent checks | gauntlet (swarm) of cheap workers | the lead aggregates |
| Tests, builds, lints, verify recipes, browser drives | scripted run by a cheap runner | the owning skill judges the evidence |
| Move a metric | hillclimb rounds | `iwon` verdicts |
| Writing that matters | draft, critique, revise | `oro` or `seda-pr` |

How each runs, with models: `asoju`'s model workflows.

## Handoffs

Skills do not call the next step. Each one returns its output to the router (`alarina`, or whoever called it), and the router starts the next step on this path.

- **Missing inputs.** A skill whose inputs are missing, or that gets a request that is not its job, returns at once and says what is missing. The router re-routes it or asks the user; nobody guesses and carries on.
- **Carry the result.** Hand the next skill the output and the decisions so far, not the whole conversation.
- **Detours.** A failing test, a design doubt or a new fact can send work back to an earlier step. Say so in one line and go.
- **Called directly.** When the user invokes a skill on its own, it still returns its output; the user decides what comes next.

## Where things are saved

Skills name a record's kind; this table maps kinds to places. A project's existing place wins (for example an existing `docs/adr/` or `docs/solutions/`); do not move records to match this table. `docs/` below is the `docs` setting when one is set.

| Kind | Where | In git |
|---|---|---|
| Lesson (committed, for maintainers) | `docs/internal/solutions/<category>/<name>.md` | Yes |
| Decision (committed, for maintainers) | `docs/internal/decisions/` | Yes |
| Runbook (committed: deploy, backup, restore, observability) | `docs/internal/operations/` | Yes |
| Guide (committed, for users) | `docs/user/` | Yes |
| Non-goal (committed) | "Non-goals" section of the README | Yes |
| Spec, ticket, plan (working) | records home: `specs/`, `tickets/`, `plans/` | Only if the user asks or settings say so; then `docs/internal/specs/`, `tickets/`, `plans/` |
| Prototype, report (working) | records home: `prototypes/`, `reports/` | No |
| Screenshots, scratch | OS temp | No |

**Records home.** Working records live outside the repo in `~/.qp/<owner>/<repo>/<kind>/`, never inside it. `<owner>/<repo>` comes from the git remote; with no remote, use the main checkout's folder name plus a short id. Every worktree of the repo shares the same folder. Nothing in it is committed.

Each checkout gets a `.qp` symlink to its records home, listed in `.git/info/exclude` (shared by all worktrees; never `.gitignore`). Before writing a record in a checkout, run the bundled script from the checkout; it creates or repairs the link and the exclude entry, refuses to replace real data, and prints the records home:

```bash
SKILL_DIR="<absolute path of the directory containing alarina's SKILL.md>";
python3 "$SKILL_DIR/scripts/qp_records.py"
```

If it fails, say why and write to the real path. Write through the link or the real path; either reaches the same files.

## Settings

Optional. Instructions in your context (session, project, user) always win; then the project file `.agents/qp.yaml` (committed, shared with the team); then the user file `~/.agents/qp.yaml`; then the skills' defaults. Read whichever exists; never create one unless the user asks.

```yaml
models:            # override rows of asoju's model table by key (build, writing, design, design-new,
                   # judgment, validator, independent, cheap, cheap-browser, tests, race)
  validator: { provider: claude, model: claude-opus-5-5, effort: medium }
  race: [{ provider: codex, model: gpt-6.1-sol, effort: xhigh }, { provider: claude, model: claude-opus-5-5, effort: low }]
specs: local       # local (records home) or git (docs/internal/specs)
tickets: local     # local (records home) or git (docs/internal/tickets)
plans: local       # local (records home) or git (docs/internal/plans)
docs: docs         # root for committed docs; internal/ and user/ go under it
sessions_keep_days: 90 # keep this many days of mined session history; default 90
```
