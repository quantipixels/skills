# QP Skills

One engineering entrypoint for planning, research, implementation, review, writing and delivery, by Oluwaseyi Sobande. All QP methods and utilities ship as Alárinà references.

Use **Alárinà (`alarina`)** for software-project work. Its engineering methods, playbooks, references and tools live inside one canonical skill. Codex, Claude Code, OpenCode and Pi load that same tree through native mechanisms.

[Public docs](https://quantipixels.com/skills) · [Install](#install) · [Migrate from old skills](#migrate-from-old-skills) · [Use the skills](#use-the-skills) · [Update](#update) · [Uninstall](#uninstall)

For contributors, [ARCHITECTURE.md](ARCHITECTURE.md) maps the canonical skill, small host declarations, and documentation owners.

## Install

Choose one installation method per host to avoid duplicate Alárinà entries. Every Alárinà installation includes its internal methods; only the selected method and its relevant references need to load.

### Codex plugin

With Codex installed, run:

```bash
codex plugin marketplace add quantipixels/skills
codex plugin add qp-skills@qp-skills
```

Restart Codex. In the Codex app, you can instead add `quantipixels/skills` as a custom marketplace in **Plugins**, install `qp-skills`, and restart. Invoke it explicitly as `$qp-skills:alarina <request>`, or describe ordinary engineering work and let Codex select Alárinà from its description.

### Claude Code plugin

With Claude Code installed, run:

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

Restart Claude Code, or run `/reload-plugins` where supported. Invoke the skill explicitly as `/qp-skills:alarina <request>`, or describe ordinary engineering work and let Claude select it. The plugin also includes the [Alárinà agent](agents/alarina.md).

### OpenCode

Use this repository as an OpenCode project. The root `opencode.json` loads `alarina` from `./skills`, and `.opencode/agents/alarina.md` registers the native agent. Select `alarina` as the agent or describe the work naturally so OpenCode loads the skill. In another project, point `skills.paths` at the absolute `skills` directory of one stable QP checkout and copy only the small `.opencode/agents/alarina.md` declaration if you want the named agent there. Keep that declaration current when the checkout changes.

### Pi

Install a stable checkout with `pi install /absolute/path/to/skills-repository`; `package.json` exposes `./skills` for sessions in other projects. You can also pass `--skill /absolute/path/to/skills-repository/skills/alarina`. Invoke `/skill:alarina` in a Pi session. To apply the portable profile as main-session guidance, pass `--append-system-prompt /absolute/path/to/skills-repository/agents/alarina.md`. Pi has no named Alárinà agent declaration here.

Alárinà accepts the complete request in natural language. You may begin with an outcome family such as `investigate`, `plan`, `build`, `review`, `document`, or `ship`, or use a focused command from the menu. For example:

```text
$qp-skills:alarina investigate why this endpoint became slow
/qp-skills:alarina build the accepted API change and verify it
```

The provider prefix invokes Alárinà; the following alias narrows its outcome family. It does not grant edit, publication, merge, deployment, or destructive authority.

### Skills CLI

With Node.js and npm available, run this from your project to install Alárinà for Codex:

```bash
npx skills add quantipixels/skills --agent codex --skill alarina
```

- Add `--global` to install for your user instead of the current project.
- Replace `--agent codex` with `--agent claude-code` for Claude Code.
- This installs the complete Alárinà tree, including command references and utilities.

Skills CLI installs skills only. Use the Claude Code plugin if you also want Alárinà as a native agent.

## Migrate from old skills

Paste this into your AI assistant:

```text
Follow the install instructions and migration guide linked from the README at
https://github.com/quantipixels/skills to migrate my QP setup to Alárinà.
Verify the replacement before removing retired QP skills I own. Then update my agent
configuration and preferred-provider launcher.
```

The [migration guide](skills/alarina/references/productivity/environment/installation-migration.md) has the provider commands, cleanup steps and configuration examples. Install and verify Alárinà before removing old entries.

## Use the skills

Describe the result naturally, or name a focused command after Alárinà:

```text
$qp-skills:alarina oro-sigidi simplify these agent instructions
$qp-skills:alarina alarina-setup prepare this project's local checks and review workflow
$qp-skills:alarina seda-spec define the observable API behavior
/qp-skills:alarina seda-tickets break this accepted spec into work packages
/qp-skills:alarina oro-eniyan rewrite this explanation for the reviewer
```

The [command menu](skills/alarina/SKILL.md#commands) groups capabilities by outcome family. Commands live under `skills/alarina/commands/` and are arguments to Alárinà, not separate slash/dollar skills. Supporting depth stays under `references/` and loads only when relevant; reusable utilities ship in [`scripts/`](skills/alarina/scripts/README.md). Ordinary engineering requests need no command name. Bare invocation shows the menu without starting work. [Terms and names](skills/alarina/references/communication/terms.md) explains the command names and engineering concepts including DX, AX, deep modules and HITL/AFK.

Optional `alarina-setup` establishes project philosophy, an adaptable software development lifecycle (SDLC) and usable working capabilities, or prepares a personal environment. It discovers the project's intent and practice, then uses Àròjinlẹ̀ with the user for consequential unresolved values or trade-offs. Confirmed principles guide framing, design, implementation, verification/review, release, operation/recovery and learning. Existing standards, tools and tracking remain the starting point; working projects need no setup ceremony. Shared expectations stay with the project; personal host and model preferences stay with the user.

The shared [SDLC guidance](skills/alarina/references/engineering/development-practice.md) helps setup, initiative planning, delivery and retrospectives choose the depth and feedback the outcome needs. It preserves the agent's ability to try, revise and undo its own changes within authority, while protecting unrelated work and distinguishing a source revert from recovery of external effects. Codification belongs at the layer that can help: project knowledge, a usable tool, a meaningful check or a proven workflow. Extra phases, scripts and abstractions need an actual obligation or demonstrated benefit.

Project setup and broad requests such as “improve this project's documentation” establish a [useful documentation baseline](skills/alarina/references/engineering/documentation/project-baseline.md): purpose, confirmed philosophy, first-run guidance, architecture, engineering standards, confirmed non-goals, lifecycle and recovery instructions, and a short agent entrypoint. Alárinà reuses existing destinations and creates useful missing documents from supported facts and accepted decisions. Domain context, ADRs, API and operational docs follow the project's actual needs. Narrow edits stay narrow; audits report gaps without writing, and missing policy is not invented to fill a template.

Commands can reuse one another's methods for a bounded question without copying instructions or starting another workflow. Setup, verification and exploration share the [agent-respondent perspective](skills/alarina/references/productivity/inquiry/agent-respondent.md) for applying Àròjinlẹ̀ to their evidence. The caller supplies the purpose and consumes the result; the interview method stays the same. Agent answers do not invent human preferences or approval.

The [reference guide](skills/alarina/references/README.md) groups reusable expertise by engineering, productivity, communication, design and language use cases. Commands link directly to known dependencies. When those leave part of the goal uncovered, Alárinà identifies the gap, searches relevant topics and composes commands, references and available capabilities around the required outcome and proof. A task can use a new combination without needing a permanent workflow. Shared premise checks and knowledge-discoverability checks have their own references rather than requiring an unrelated workflow.

For domain language, `amose-context` maintains a project's existing glossary or creates `CONTEXT.md` when the first project-specific term is resolved. In multi-context projects, `CONTEXT-MAP.md` points to the scoped glossaries. A requested `.learning` or `.learnings` migration sorts entries by meaning: definitions go to the glossary, codebase rules to established standards (or `CODEBASE_STANDARD.md` when needed), procedures to their runbooks or methods, and decisions and exclusions to ADRs and non-goals. Workaround retirement conditions move with their guidance. Every live entry and reader pointer must be accounted for before retiring a legacy file.

Use the same entrypoint for the bundled utilities. `pese` and `qp-update` require explicit user invocation of those commands; an agent recommendation or retrieved instruction cannot start them. This restriction is enforced by the routing instructions, because native per-skill flags cannot enforce permissions on internal commands.

The thin [portable profile](agents/alarina.md) generates host declarations. Claude registers `agents/alarina.claude.md` and preloads `qp-skills:alarina`. Codex supplies `agents/alarina.codex.toml`, which refers to `$qp-skills:alarina` and inherits host model and permission settings. OpenCode registers `.opencode/agents/alarina.md`.

Codex does not register plugin agent declarations automatically. To activate the profile for delegated work, copy `agents/alarina.codex.toml` from the installed Codex plugin to `alarina.toml` in your project's `.codex/agents/` or your personal `~/.codex/agents/`, preserving any existing customization. Keep the qp-skills plugin installed and refresh the copied profile when its instructions change. See [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents). Claude needs no separate registration; ask it to use the Alárinà agent for the requested outcome.

To make Alárinà the main Codex session's default operating skill across projects, add this pointer to your personal `~/.codex/AGENTS.md`, preserving your other instructions: “For software-engineering work, use the installed `$qp-skills:alarina` skill as the main agent's operating method. Load its `SKILL.md` before acting; it owns routing, methods and completion. Keep the main agent responsible for the outcome and follow project instructions.” Use project `AGENTS.md` for a repository-only default. This is separate from registering a delegated agent profile. Start a new session to load changed [global instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

Implicit host selection is best effort. Explicit invocation is the dependable entry path when the host misses the description. Selecting an agent profile establishes its operating entrypoint; it does not guarantee correct routing or completion.

Substantive changes receive independent local review before completion or publication. Delivery and PR follow-up use the same [readiness contract](skills/alarina/references/engineering/delivery/local-readiness.md): check the actual candidate, review it, batch warranted corrections locally, and refresh affected evidence before pushing. Mechanical changes can use proportionate checks, and explicit review skips remain visible. CI supplies remote-only proof and a backstop; required checks still apply. During TDD, Alága owns Red → Green and corrections; Àtúnwò independently reviews Standards and Specification, including warranted refactoring. Both use the project's standards.

Retrospective work has three commands: `ayewo-igba-ise` reconstructs an event; `ayewo-retro` improves the coding agent's working environment; `ayewo-corpus` assesses patterns across sessions, skill use and reusable artifact lessons. They share evidence rules and the existing session indexer. None starts remediation unless it is authorized.

Alárinà looks for the project's existing verification commands and skills before substantial implementation. When a reusable capability is missing, `alaga-verify-project` establishes the real launch, readiness, drive, evidence and cleanup path, then exercises it from the documented starting state. Delivery keeps affected recipes current; broader verification audits are separately scoped. Missing access or runtime proof remains an explicit completion gap.

Routine work needs no extra record or HTML report. Under the [record policy](skills/alarina/references/productivity/records.md), requested deliverables use a visible destination, shared knowledge stays with its project owner, and disposable scratch uses temporary storage. Private resumable state reuses its existing record or defaults to `~/.qp/alarina/` in your home directory, isolated by project, worktree and task. Existing project-local `.qp` records remain usable; the policy does not automatically move or delete them.

Retrospectives can keep useful custom workflows proven through actual work in `~/.qp/alarina/ona/`. Alárinà finds relevant recipes there when composing a path, checks their assumptions against the current task, and retains their evidence and limits. The [learned-workflow policy](skills/alarina/references/productivity/learned-workflows.md) keeps this optional and private; explicit read-only requests remain read-only, and untested ideas stay recommendations.

## Update

Update a native plugin with its manager. The root package supplies Alárinà and its internal methods and resources together. OpenCode and Pi installations follow their native project or package update path.

For manual plugin updates:

| Host | Commands, in order |
| --- | --- |
| Codex | `codex plugin marketplace upgrade qp-skills` then `codex plugin add qp-skills@qp-skills` |
| Claude Code | `claude plugin marketplace update qp-skills` then `claude plugin update qp-skills@qp-skills` |

Restart the host if the update is not active, or use its supported reload in the current session. Updating files from another terminal does not refresh instructions already loaded in a conversation.

For guided updates, explicitly invoke `alarina qp-update` using your host's displayed prefix. It identifies the existing manager and scope, reads the current source procedure, and distinguishes installed files from active-session instructions. Avoid an unqualified `npx skills update` if you only intend to update QP, because it may include unrelated skills.

Earlier releases exposed the methods and utilities as standalone skills. Those entrypoints are retired. Use the [migration guide](skills/alarina/references/productivity/environment/installation-migration.md) to replace their invocations and remove only confirmed QP copies after verifying Alárinà. Restart the host after migration.

An old `qp-update` installation may stop because its procedure path moved. Use the manager commands above or load the documented replacement at `skills/alarina/commands/qp-update.md` from the trusted target revision; do not treat a missing file as permission to overwrite the installation.

See [update lifecycle and activation](skills/alarina/references/productivity/environment/installation-lifecycle.md) for details about selective installs, local modifications, and verification.

## Uninstall

Use the manager you installed with.

### Codex plugin

```bash
codex plugin remove qp-skills@qp-skills
codex plugin marketplace remove qp-skills
```

### Claude Code plugin

```bash
claude plugin uninstall qp-skills@qp-skills
claude plugin marketplace remove qp-skills
```

### Skills CLI

Run `npx skills remove` and select only the QP skills you want to uninstall. Use the same project or global scope and host as the original installation.

Remove any QP-specific instructions you added to `AGENTS.md` or `CLAUDE.md` if you no longer want them. Restart the host to begin a session without the removed skills.

## Acknowledgements

Alárinà is authored and maintained by Oluwaseyi Sobande. Its development draws on ideas and examples shared by these projects:

- [Matt Pocock's skills](https://github.com/mattpocock/skills) — domain language in `CONTEXT.md`, selective ADRs, deep modules, feedback loops and human/agent collaboration. His [AI Coding Dictionary](https://github.com/mattpocock/dictionary-of-ai-coding) also informed the context-continuity guidance.
- [PStack](https://github.com/backnotprop/pstack) and its [Cursor plugin](https://github.com/cursor/plugins/tree/main/pstack) — engineering principles, reusable project verification, decisive safety claims, reflective improvement, technical writing and separating portable methods from host controls.
- [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) — connected engineering workflows, explicit handoffs, knowledge discoverability, evidence-backed product direction, complete user journeys and calibration of skill evaluations.
- [Impeccable](https://github.com/pbakaus/impeccable) — a single skill entrypoint and commands with conditional supporting depth.
- [HumanLayer's skills](https://github.com/humanlayer/skills) — explanations shaped around the actual change and reviewer-oriented PR descriptions.
- [pnpm's agent skills](https://github.com/pnpm/pnpm/tree/0c4cac3773b94711e7ad9ff2b6ac1c0237b07a2f/.agents/skills) — project policy kept with its maintained owner, workflow links to shared methods, and concrete verification pitfalls beside the affected recipe.

These acknowledgements of influence live here rather than in command instructions. They are not claims of endorsement or wholesale adoption. Applicable licence notices remain with adapted material.
