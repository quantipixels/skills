# QP Skills

**Alárinà helps your coding agent carry a software change from an unclear request to a verified result.** Describe what you want to achieve; it chooses the relevant planning, investigation, implementation, review and writing methods, then carries the work through the finish you requested.

It works with **Codex, Claude Code, OpenCode and Pi**, using your existing repository conventions and tools. One installed skill contains the methods and loads supporting guidance when needed.

[Get started](#install) · [Examples](#use-the-skills) · [Project setup](#configure-and-verify-a-project) · [Explore](#explore-the-project) · [Update](#update)

## What it adds to your workflow

- **Turn an incomplete request into actionable work.** Alárinà uses the conversation and project context, includes necessary steps, and asks when an unresolved choice would materially change the outcome.
- **Carry a change through delivery.** It connects implementation, relevant checks, independent review and affected documentation. The main agent remains responsible for integrating delegated work.
- **Resume with context.** It recovers the accepted goal, previous decisions, current candidate and remaining work from a plan, chat or project records, checking which evidence is still current.
- **Choose checks and recover from failures.** It discovers the project's verification path, compares local checks with CI and uses an existing suitable dev container when available.
- **Keep useful lessons close to the work.** It retrieves relevant prior guidance and recommends improvements when observed failures or repeated friction justify them.

Use it for a focused fix, a plan, a review or a longer initiative. You keep control of scope, model choices and permissions. A planning-only request stays a plan; publication, merge, deployment and destructive actions depend on your authorization. Autonomous work runs through the host's available capabilities, so continuing after a session ends requires host support.

## Install

Choose one installation method per host to avoid duplicate entries. You need the chosen coding agent installed; the methods can work with your existing project tools. Optional Python helpers have separate prerequisites described under [project setup](#configure-and-verify-a-project).

### Codex plugin

```bash
codex plugin marketplace add quantipixels/skills
codex plugin add qp-skills@qp-skills
```

Restart Codex, then try:

```text
$qp-skills:alarina inspect this project and explain how to run its checks; do not change files
```

In the Codex app, you can instead add `quantipixels/skills` as a custom marketplace in **Plugins**, install `qp-skills`, and restart.

### Claude Code plugin

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

Restart Claude Code, or use `/reload-plugins` where supported. Try `/qp-skills:alarina <request>`. The plugin also registers the [Alárinà agent](agents/alarina.md).

### OpenCode

In this checkout, `opencode.json` loads the skill from `./skills`, and `.opencode/agents/alarina.md` registers the agent. Select `alarina` or describe the work naturally. For another project, point `skills.paths` at the absolute `skills` directory of a stable QP checkout. Copy `.opencode/agents/alarina.md` into the project's matching directory if you also want the named agent, and refresh that declaration when the checkout changes.

### Pi

Install a stable checkout with `pi install /absolute/path/to/skills-repository`, then invoke `/skill:alarina`. Alternatively, pass `--skill /absolute/path/to/skills-repository/skills/alarina`. To use the portable profile as main-session guidance, pass `--append-system-prompt /absolute/path/to/skills-repository/agents/alarina.md`.

### Skills CLI

With Node.js and npm available, run this in your project:

```bash
npx skills add quantipixels/skills --agent codex --skill alarina
```

Use `--global` for a user-wide installation, or `--agent claude-code` for Claude Code. This installs the complete skill tree; use the native Claude plugin if you also want its registered agent.

## Use the skills

After loading Alárinà with your host's invocation above, describe the outcome in ordinary language. These examples use `alarina` as the portable name:

| You want to… | You can say… |
| --- | --- |
| Understand a failure | `alarina investigate why this endpoint became slow; give me the cause before changing code` |
| Plan a change | `alarina plan this migration, including risks and verification; do not implement` |
| Deliver a fix | `alarina implement and verify the accepted fix end to end; I’m AFK` |
| Open a PR | `alarina deliver this feature, run the checks and open a PR; work autonomously` |
| Resume earlier work | `alarina continue the work in this chat link; only verification remains` |
| Review a candidate | `alarina review this branch for correctness and missing tests` |
| Improve project guidance | `alarina make this README useful to someone trying the project for the first time` |
| Learn from experience | `alarina audit these sessions and recommend improvements; do not apply them yet` |

You do not need command names. Alárinà chooses methods from the outcome and current state. For precise selection, use a name from the [command menu](skills/alarina/SKILL.md#commands), such as `atona-plan` for planning or `atona` for ongoing delivery. These are internal methods within Alárinà. A bare invocation shows the menu without starting work.

Hands-off and AFK requests use the same workflow. Alárinà keeps a goal and current path for long-running work, continues within the agreed scope, and asks when a consequential decision needs your input. See [autonomous entry examples](skills/alarina/commands/atona.md#entry-examples). Explicit invocation is the dependable starting point when the host's automatic selection misses the skill.

### Make it your default in Codex

Add this pointer to your personal `~/.codex/AGENTS.md`, or the project's `AGENTS.md` for that repository only, preserving existing instructions:

```text
For software-engineering work, use the installed alarina skill as the main agent's operating method. Resolve its actual entry from the host's available skills and load its SKILL.md before acting. Keep the main agent responsible for the outcome and follow project instructions.
```

Start a new session to load changed instructions. To register an optional delegated agent, copy `agents/alarina.codex.toml` from the installed plugin to `.codex/agents/alarina.toml` in the project or `~/.codex/agents/alarina.toml` for your user. Preserve customizations and refresh the copy when its source changes; the plugin must remain installed. The default main-session pointer and delegated profile serve separate entry paths.

## Configure and verify a project

Start with the project's current conventions. If its setup needs work, ask:

```text
alarina prepare this project's local checks and review workflow
```

Setup connects existing commands, useful project guidance and real verification steps. The optional [configuration guide](skills/alarina/references/productivity/environment/configuration.md) explains `.alarina.json`, local check receipts and isolated task records. Models, effort and delegation preferences stay with your host or agent instructions.

You can also ask Alárinà to compare local checks with CI, inspect stale evidence before resuming, verify in an existing dev container, or check the installed package. Its helpers distinguish observed files, executed checks and active-session evidence. Core helpers require Python 3.10+; the process-isolating verifier supports macOS and Linux, and optional CI drift inspection uses project-provided PyYAML. Other platforms can use their native project checks.

## Explore the project

| Question | Start here |
| --- | --- |
| What can I ask it to do? | [Commands and playbooks](skills/alarina/SKILL.md) |
| What do the names mean? | [Terms and names](skills/alarina/references/communication/terms.md) |
| How does it check a project? | [Configuration and verification](skills/alarina/references/productivity/environment/configuration.md) |
| How do I run the helpers directly? | [Script reference](skills/alarina/scripts/README.md) |
| How does it retain and reuse lessons? | [Learned workflows](skills/alarina/references/productivity/learned-workflows.md) |
| Where does it keep records? | [Records and artifacts](skills/alarina/references/productivity/records.md) |
| Where are deeper methods? | [Reference guide](skills/alarina/references/README.md) |
| How do I contribute or verify this package? | [Architecture](ARCHITECTURE.md), [repository guidance](AGENTS.md) and [build checks](scripts/plugins/README.md) |
| What has been evaluated? | [Evaluation coverage and limits](evals/alarina/README.md), including [optional behavior trials](evals/alarina/behavior-trials.md) |

Package CI runs the same eight configured checks on Linux and macOS. Windows checks package contracts and declaration generation. Those checks establish package and helper behavior; native activation and model behavior need their own observations. The evaluation records state which scenarios were actually run. No comparative reliability advantage is claimed from the test count.

## Migrate from old skills

Earlier QP releases exposed standalone skills. Follow the [migration guide](skills/alarina/references/productivity/environment/installation-migration.md) to install and verify Alárinà, update your invocation/configuration and remove only confirmed retired QP copies. Restart the host afterward.

Or paste this into your coding agent:

```text
Follow the installation and migration guides linked from https://github.com/quantipixels/skills to migrate my QP setup to Alárinà. Verify the replacement before removing retired QP skills I own, and update my agent configuration and launcher.
```

## Update

Use the manager and scope you installed with:

| Host | Commands, in order |
| --- | --- |
| Codex | `codex plugin marketplace upgrade qp-skills` then `codex plugin add qp-skills@qp-skills` |
| Claude Code | `claude plugin marketplace update qp-skills` then `claude plugin update qp-skills@qp-skills` |
| OpenCode / Pi | Update the stable checkout or installed package using the host's normal path. |

For guided updates, explicitly invoke `alarina qp-update` with your host's displayed prefix. It checks the existing manager, scope and current procedure. Updating files does not refresh instructions already loaded in a chat: restart or use the host's supported reload. Avoid unqualified `npx skills update` when you intend to update only QP. See [installation and activation](skills/alarina/references/productivity/environment/installation-lifecycle.md) for selective updates and recovery from a moved legacy procedure.

## Uninstall

Use the original manager. For Codex, run `codex plugin remove qp-skills@qp-skills` and `codex plugin marketplace remove qp-skills`. For Claude Code, run `claude plugin uninstall qp-skills@qp-skills` and `claude plugin marketplace remove qp-skills`. For a Skills CLI install, run `npx skills remove` and select only QP entries in the original scope.

For OpenCode, remove the QP `skills.paths` entry and copied agent declaration. For Pi, remove the installed QP package through its package manager or remove the explicit launch flags. Remove QP pointers you added to agent instructions if you no longer want them, then restart the host.

## Acknowledgements

Alárinà is authored and maintained by Oluwaseyi Sobande. Its development draws on ideas and examples shared by these projects:

- [Matt Pocock's skills](https://github.com/mattpocock/skills) — domain language in `CONTEXT.md`, selective ADRs, deep modules, feedback loops and human/agent collaboration. His [AI Coding Dictionary](https://github.com/mattpocock/dictionary-of-ai-coding) also informed the context-continuity guidance.
- [PStack](https://github.com/backnotprop/pstack) and its [Cursor plugin](https://github.com/cursor/plugins/tree/main/pstack) — engineering principles, reusable project verification, decisive safety claims, reflective improvement, technical writing and separating portable methods from host controls.
- [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin) — connected engineering workflows, explicit handoffs, knowledge discoverability, evidence-backed product direction, complete user journeys and calibration of skill evaluations.
- [Impeccable](https://github.com/pbakaus/impeccable) — a single skill entrypoint and commands with conditional supporting depth.
- [HumanLayer's skills](https://github.com/humanlayer/skills) — explanations shaped around the actual change and reviewer-oriented PR descriptions.
- [pnpm's agent skills](https://github.com/pnpm/pnpm/tree/0c4cac3773b94711e7ad9ff2b6ac1c0237b07a2f/.agents/skills) — project policy kept with its maintained owner, workflow links to shared methods, and concrete verification pitfalls beside the affected recipe.

These acknowledgements of influence live here rather than in command instructions. They are not claims of endorsement or wholesale adoption. Applicable licence notices remain with adapted material.
