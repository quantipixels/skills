# QP Skills

Portable agent skills for reasoning, engineering, design, and delivery. Each skill owns a focused result. Use `alarina` to coordinate the work, or invoke a specialist directly for a focused result.

Browse the public docs at [quantipixels.com/skills](https://quantipixels.com/skills).

## Install

Choose the native plugin for your host, or Skills CLI for editable skill copies. Use one installation method per host to avoid duplicate skills.

### Codex plugin

```bash
codex plugin marketplace add quantipixels/skills
codex plugin add qp-skills@qp-skills
```

Restart Codex, then ask it to use `alarina` with your requested outcome. The plugin installs all QP skills. You control the model and reasoning.


In the Codex app, add `quantipixels/skills` as a custom marketplace in Plugins, install `qp-skills`, and restart.

### Skills CLI

Install all skills for Codex in the current project:

```bash
npx skills add quantipixels/skills --agent codex --skill '*'
```

Add `--global` for a personal installation, or replace `'*'` with a skill name for a selective install. Alárinà's complete operating experience requires all QP skills. Individual skills can be used without Alárinà; include any companion required by the selected branch. For initiative planning with `atona`, also install `html-artifact`.

For Claude Code, replace `--agent codex` with `--agent claude-code`. Skills CLI installs skills; use the Claude plugin to include Alárinà as a native agent.

### Claude Code plugin

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

Restart Claude Code or run `/reload-plugins`. The plugin provides all QP skills and the Alárinà agent. Ask Claude to use `alarina` for your requested outcome.

Model, reasoning, and permissions remain under your control. Claude discovers the shared `skills/` and `agents/` directories natively; no setup script or separate agent configuration is needed.


## Start

### Give the agent a working brief

After installing the skills, copy this block into your personal or project `AGENTS.md` / `CLAUDE.md`, or paste it into a conversation for that session. Merge it with existing instructions. Keep, adapt or omit the final paragraph to fit your preferred personality; it is yours to choose.

```text
Use the installed `alarina` skill as the governing working method for carrying my requests through authorized completion. Load it, then select and apply relevant installed skills and playbooks as the work evolves. Read their instructions and applicable references; use their methods, not just their names. Keep settled work direct and preserve accepted decisions when resuming.

Choose available capabilities by the evidence the task needs. Use the project's and host's native interfaces for source structure, measurement semantics, effective use and readiness. Keep routine work direct and report material capability or coverage gaps.

When work needs planning, use `atona` to guide it and `html-artifact` for the human-readable plan. Keep the same document current through delivery, showing the direction, decisions, progress, evidence and remaining choices clearly enough for someone new to the work to follow. Keep me involved when my judgment is needed and carry on with work already authorized.

Be a steady workmate: warm, direct, resourceful and candid. Have a view and reconsider when evidence warrants it. Care about craft, follow through and keep me oriented. Match my language and tone; let humour arise naturally.
```

Then describe your work normally. Saved instructions apply when your host loads that file; a conversation paste applies to that session. This brief does not install tools, change permissions, select a model or create a worker. Personality stays in user-owned instructions, not in the skills.

The plugin bundles an [Alárinà agent definition](agents/alarina.md), but using its skill as a working method does not require creating a separate agent configuration. Codex does not automatically register bundled Markdown definitions as custom agents.

### Use a skill directly

If you know the skill you need, use it directly.

Common entrypoints:

| Skill | Use when |
| --- | --- |
| `arojinle` | A consequential choice or the user's real desired outcome needs to be resolved |
| `atona` | Material work needs one current plan and route to an outcome |
| `alaga` | An accepted coding change or fix needs implementation and proportionate proof |
| `atunwo` | A fixed code candidate or codebase snapshot needs independent judgment |
| `architect` | Technical structure, interfaces or technology choices need survey, design or review |
| `iwadi` | A question needs substantial current research or exact-source grounding |
| `yoruba-glossary` | Yorùbá language guidance, lessons, word formation, or glossary maintenance is needed |
| `oro` | Agent-facing instructions or human-facing technical prose needs writing, review, editing, or pruning |
| `akowe` | A documentation set needs a read-only audit or verified synchronization with implementation and accepted decisions |
| `adanwo` | Disposable prototypes help the user discover, compare and refine a direction |
| `alarina` | Select or use an engineering playbook, compose or resume work across owners, or find the starting owner |
| `fihanmi` | Supplied material needs a compact visual explanation or useful default presentation |
| `seda-pr` | A PR/MR needs a reviewer-facing description, creation, publication, or babysitting toward a human merge decision |

Alárinà uses installed skill definitions as the dynamic inventory.

Use [Akọ̀wé (`akowe`)](skills/akowe/SKILL.md) to audit or synchronize a scoped documentation set. For example: “Use akowe to audit the docs affected by this change; do not edit” or “Use akowe to sync the current setup guides with this branch; do not commit or push.” It checks relevant nested docs, examples and agent guidance without rewriting historical decisions or treating code regressions as new policy. Architecture stays with `architect`, domain meaning and ADR lifecycle with `amose`, and writing with `oro`. Selective installations need the companions required by the affected documents; no new host configuration is required.

`fihanmi` owns shared presentation and the visual-explanation method used by `oro`, `html-artifact`, and reviewer-facing PR work.

Use `seda-pr` in description mode to draft or improve a PR body without committing or pushing; publication and babysitting use the same skill. Its [reviewer brief](skills/seda-pr/references/reviewer-brief.md) leads with purpose, caveats and a change-shaped outline, supported by actual evidence and recovery limits. `seda-pr` replaces `wo-pr` without an alias; update explicit references and selective installations to the new name.

Atọ́nà maintains one living HTML plan, including decisions, evidence, progress and next action. It does not create an equivalent Markdown plan; independent specifications, architecture records and source evidence keep their useful existing formats.


With `alarina` active, describe the engineering outcome or name a playbook; it selects the path and coordinates the relevant skills.

## Update

Explicitly invoke `qp-update` to update the existing QP installation through its current manager. It first reads the current update procedure from your established source and permitted update channel, then continues the same request. Pins, scope, host placement and local changes are preserved; no separate updater installation or new manager is required. QP does not invoke this workflow automatically or change your host's auto-update settings.

A native plugin update includes ordinary additions, retirements and replacements inside the bundle. A selective Skills CLI installation keeps its selection; additional skills or removal of separate copies need applicable authorization. `qp-update` reports membership changes, protected local copies, and installation evidence separately from session activation. See the [lifecycle guidance](skills/qp-update/references/lifecycle.md).

An older installed updater needs one supported manager upgrade to acquire this bootstrap. Reading fresh instructions does not itself update installed files or replace instructions already in the conversation.

For a Git-backed Codex plugin installation:

```bash
codex plugin marketplace upgrade qp-skills
codex plugin add qp-skills@qp-skills
```

Use the installed client's supported activation path; restart Codex if the plugin update is not active and no usable reload is available.

For Skills CLI, use its supported named-skill update for the installed QP selection in the existing project/global scope. Inspect host-placement and source-wide side effects before running it: an unqualified `npx skills update` may include unrelated skills. Updating installed names does not subscribe to future repository skills; noninteractive updates can leave retired copies behind. `qp-update` reconciles those outcomes without silently expanding the selection or deleting local changes.

For Claude Code:

```bash
claude plugin marketplace update qp-skills
claude plugin update qp-skills@qp-skills
```

Check whether the update is already active. Otherwise run `/reload-plugins` in the current Claude Code session where supported, or restart. Respect any reload warning; updating from another terminal does not reload an existing conversation. For local skill copies, use the host's supported automatic discovery first, then its reload/restart fallback. The updater explicitly rereads changed instructions and references rather than treating a file update as a context refresh.

Claude plugin updates follow Git commits. The manifest intentionally omits `version`, so there is no version to synchronize with `package.json` releases.

## Uninstall

For the Codex plugin:

```bash
codex plugin remove qp-skills@qp-skills
codex plugin marketplace remove qp-skills
```

For Claude Code:

```bash
claude plugin uninstall qp-skills@qp-skills
claude plugin marketplace remove qp-skills
```

For Skills CLI, use `npx skills remove` and select the QP skills. Do not install the package through multiple managers at once.

## Project

Use [`AGENTS.md`](AGENTS.md) and `oro` for contribution and agent-instruction guidance. Change rationale and proof belong in PRs and CI.

### Repository boundaries

| Location | Responsibility |
| --- | --- |
| `skills/<name>/` | Independently installable capability and its supporting resources. Methods stay with their owner; Alárinà's playbooks coordinate work between owners. |
| `agents/`, `.codex-plugin/`, `.claude-plugin/` | Thin native host entrypoints and package declarations. Discover skills through the host. |
| `scripts/`, `tests/` | Executable package and host mechanics, with checks for meaningful failures. Skill-specific mechanics stay beside their consuming skill. |
| `evals/` | Optional behavioral cases, comparison method and historical observations. The engineering harness serves coding tasks that need executable oracles. |

Keep installed skills independent of this checkout's evaluation files. Use the [shared evaluation method](evals/README.md) only when a concrete behavior or comparative claim needs it; native hosts run the models. Case packs contain their unique inputs and expectations, without repeating the shared method or becoming mandatory CI campaigns.

To verify a checkout through disposable native manager state, run `python3 scripts/plugins/verify_native_install.py`. Use `--host codex` or `--host claude` to select one manager. The check reports the `qp-skills` package identity, observed skill/agent scope, source revision, and hashes for sampled files including every updater resource; it does not prove fresh-session invocation. For upgrade evidence, the same verifier supports a read-only comparison of saved before/after native plugin roots. See [native upgrade verification](scripts/plugins/README.md); snapshot agreement alone does not prove a manager transition, scope preservation or session activation.
