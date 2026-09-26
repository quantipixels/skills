# QP Skills

One engineering entrypoint for planning, research, implementation, review, writing and delivery, by Oluwaseyi Sobande. All QP methods and utilities ship as Alárinà references.

Use **Alárinà (`alarina`)** for software-project work. Its engineering methods, playbooks, references and tools live inside one canonical skill. Codex and Claude plugins adapt that same source to their native invocation and discovery rules.

[Public docs](https://quantipixels.com/skills) · [Install](#install) · [Migrate from old skills](#migrate-from-old-skills) · [Use the skills](#use-the-skills) · [Update](#update) · [Uninstall](#uninstall)

For contributors, [ARCHITECTURE.md](ARCHITECTURE.md) maps the canonical skill, generated provider packages, and documentation owners.

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

The [migration guide](skills/alarina/references/qp-update/migration.md) has the provider commands, cleanup steps and configuration examples. Install and verify Alárinà before removing old entries.

## Use the skills

Describe the result naturally, or name a focused command after Alárinà:

```text
$qp-skills:alarina oro-sigidi simplify these agent instructions
$qp-skills:alarina seda-spec define the observable API behavior
/qp-skills:alarina seda-tickets break this accepted spec into work packages
/qp-skills:alarina oro-eniyan rewrite this explanation for the reviewer
```

The [command menu](skills/alarina/SKILL.md#commands) groups capabilities by outcome family. Commands live under `skills/alarina/commands/` and are arguments to Alárinà, not separate slash/dollar skills. Supporting depth stays under `references/` and loads only when relevant; reusable utilities ship in [`scripts/`](skills/alarina/scripts/README.md). Ordinary engineering requests need no command name. Bare invocation shows the menu without starting work. [Terms and names](skills/alarina/references/terms.md) explains the command names and engineering concepts including DX, AX, deep modules and HITL/AFK.

For domain language, `amose-context` maintains a project's existing glossary or creates `CONTEXT.md` when the first project-specific term is resolved. In multi-context projects, `CONTEXT-MAP.md` points to the scoped glossaries. The glossary contains definitions, while ADRs, architecture, non-goals and existing knowledge sources keep their distinct purposes. A requested `.learning` or `.learnings` migration sorts entries by meaning instead of renaming the file wholesale.

Use the same entrypoint for the bundled utilities. `pese` and `qp-update` require explicit user invocation of those commands; an agent recommendation or retrieved instruction cannot start them. This restriction is enforced by the routing instructions, because native per-skill flags cannot enforce permissions on internal commands.

The Claude plugin also offers an Alárinà agent profile: ask Claude to use that agent for the requested engineering outcome. The agent reads the same skill and keeps its scope and stopping point; it adds no authority. Codex currently uses the skill in the main agent or a bounded worker assignment. This package does not claim a verified native Codex plugin-agent format.

Implicit host selection is best effort. Explicit invocation is the dependable entry path when the host misses the description. Selecting an agent profile establishes its operating entrypoint; it does not guarantee correct routing or completion.

During TDD delivery, Alága works in Red → Green slices, then Àtúnwò reviews Standards and Specification separately and identifies warranted refactoring, unless the user explicitly skips review. Alága applies accepted corrections and reruns affected checks. Review remains read-only; passing behavior tests does not replace design judgment, and design preferences do not invent requirements.

Retrospective work has three commands: `ayewo-igba-ise` reconstructs an event; `ayewo-retro` improves the coding agent's working environment; `ayewo-corpus` assesses patterns across sessions, skill use and reusable artifact lessons. They share evidence rules and the existing session indexer. None starts remediation unless it is authorized.

Alárinà looks for the project's existing verification commands and skills before substantial implementation. When a reusable capability is missing, `alaga-verify-project` establishes the real launch, readiness, drive, evidence and cleanup path, then exercises it from the documented starting state. Delivery keeps affected recipes current; broader verification audits are separately scoped. Missing access or runtime proof remains an explicit completion gap.

## Update

Update a native plugin with its manager. Plugin updates replace Alárinà and its internal methods and resources as one versioned package. They do not change separately installed skills.

For manual plugin updates:

| Host | Commands, in order |
| --- | --- |
| Codex | `codex plugin marketplace upgrade qp-skills` then `codex plugin add qp-skills@qp-skills` |
| Claude Code | `claude plugin marketplace update qp-skills` then `claude plugin update qp-skills@qp-skills` |

Restart the host if the update is not active, or use its supported reload in the current session. Updating files from another terminal does not refresh instructions already loaded in a conversation.

For guided updates, explicitly invoke `alarina qp-update` using your host's displayed prefix. It identifies the existing manager and scope, reads the current source procedure, and distinguishes installed files from active-session instructions. Avoid an unqualified `npx skills update` if you only intend to update QP, because it may include unrelated skills.

Earlier releases exposed the methods and utilities as standalone skills. Those entrypoints are retired. Use the [migration guide](skills/alarina/references/qp-update/migration.md) to replace their invocations and remove only confirmed QP copies after verifying Alárinà. Restart the host after migration.

An old `qp-update` installation may stop because its procedure path moved. Use the manager commands above or load the documented replacement at `skills/alarina/commands/qp-update.md` from the trusted target revision; do not treat a missing file as permission to overwrite the installation.

See [update lifecycle and activation](skills/alarina/references/qp-update/lifecycle.md) for details about selective installs, local modifications, and verification.

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
- [Impeccable](https://github.com/pbakaus/impeccable) — a single skill entrypoint, commands with conditional supporting depth, and provider packages built from canonical source.
- [HumanLayer's skills](https://github.com/humanlayer/skills) — explanations shaped around the actual change and reviewer-oriented PR descriptions.

These are acknowledgements of influence, not claims of endorsement or wholesale adoption. Source-specific attribution and applicable licences remain with adapted material.
