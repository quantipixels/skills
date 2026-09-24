# QP Skills

Agent skills for planning, research, engineering, design, and writing, by Oluwaseyi Sobande. Each skill gives your agent a method for a particular kind of work, with supporting references and tools where needed.

Start with **Alárinà (`alarina`)** to coordinate work across skills, or name a specialist when you know what you need. Install the complete collection as a Codex or Claude Code plugin, or choose individual skills through Skills CLI.

[Public docs](https://quantipixels.com/skills) · [Install](#install) · [Use the skills](#use-the-skills) · [Update](#update) · [Uninstall](#uninstall)

## Install

Choose one installation method per host to avoid duplicate skills. Native plugins include all QP skills; Skills CLI lets you choose which skills to install.

### Codex plugin

With Codex installed, run:

```bash
codex plugin marketplace add quantipixels/skills
codex plugin add qp-skills@qp-skills
```

Restart Codex. In the Codex app, you can instead add `quantipixels/skills` as a custom marketplace in **Plugins**, install `qp-skills`, and restart.

### Claude Code plugin

With Claude Code installed, run:

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

Restart Claude Code, or run `/reload-plugins` where supported. This plugin includes all QP skills and the [Alárinà agent](agents/alarina.md).

### Skills CLI

With Node.js and npm available, run this from your project to install all skills for Codex:

```bash
npx skills add quantipixels/skills --agent codex --skill '*'
```

- Add `--global` to install for your user instead of the current project.
- Replace `--agent codex` with `--agent claude-code` for Claude Code.
- Replace `'*'` with a skill name to install selectively. For example:

```bash
npx skills add quantipixels/skills --agent codex --skill oro
```

Alárinà's complete workflow requires all QP skills. You can use specialists independently of Alárinà, but install any companions required by the work you choose. For example, initiative planning with `atona` also needs `html-artifact`.

Skills CLI installs skills only. Use the Claude Code plugin if you also want Alárinà as a native agent.

### Main skills

| Skill | What it helps you do |
| --- | --- |
| [Alárinà · `alarina`](skills/alarina/SKILL.md) | Choose an engineering playbook and coordinate the relevant skills through completion. |
| [Àròjinlẹ̀ · `arojinle`](skills/arojinle/SKILL.md) | Work out what you want and resolve consequential choices through an interview. |
| [Atọ́nà · `atona`](skills/atona/SKILL.md) | Turn an ambitious or unclear idea into a workable direction and carry it through with a living HTML plan. |
| [Alága · `alaga`](skills/alaga/SKILL.md) | Diagnose failures, recover incidents, or implement and verify an accepted coding change. |
| [Àtúnwò · `atunwo`](skills/atunwo/SKILL.md) | Review code changes or an existing system for correctness, maintainability, and regressions. |
| [Architect · `architect`](skills/architect/SKILL.md) | Survey, design, review, or document technical structure and interfaces. |
| [Amọ̀ṣẹ́ · `amose`](skills/amose/SKILL.md) | Clarify domain terms, rules, lifecycles, and ownership, and maintain durable project decisions. |
| [Ìwádìí · `iwadi`](skills/iwadi/SKILL.md) | Research a question and produce an answer grounded in evidence and references. |
| [Àdánwò · `adanwo`](skills/adanwo/SKILL.md) | Build disposable prototypes so you can try and compare ideas before deciding. |
| [Ọ̀rọ̀ · `oro`](skills/oro/SKILL.md) | Write, review, or simplify prose and instructions for people or agents. |
| [Akọ̀wé · `akowe`](skills/akowe/SKILL.md) | Audit or update documentation against implementation and accepted decisions. |
| [Fihanmi · `fihanmi`](skills/fihanmi/SKILL.md) | Make supplied material easier to understand, inspect, and act on. |
| [HTML Artifact · `html-artifact`](skills/html-artifact/SKILL.md) | Create accessible HTML plans, explanations, and comparisons from supplied material. |
| [Seda PR · `seda-pr`](skills/seda-pr/SKILL.md) | Draft, publish, or manage a PR/MR through CI and feedback to a human merge decision. |

Browse [`skills/`](skills/) for the full collection, including postmortems, Yorùbá language guidance, macOS disk cleanup, and private local sharing. Each `SKILL.md` explains when to use the skill and how it works.

## Update

Ask your agent explicitly:

```text
Use qp-update to update my existing QP skills installation.
```

`qp-update` reads the current update procedure and uses your existing installation manager. It preserves pins, installation scope, and local changes, and reports any activation steps still needed. QP does not invoke it automatically or change your host's auto-update settings.

Plugin updates include additions, retirements, and replacements within the bundle. Selective Skills CLI installations keep their selection; installing all current skills with `--skill '*'` does not subscribe you to future additions. Avoid an unqualified `npx skills update` if you only intend to update QP, because it may include unrelated skills.

For manual plugin updates:

| Host | Commands, in order |
| --- | --- |
| Codex | `codex plugin marketplace upgrade qp-skills` then `codex plugin add qp-skills@qp-skills` |
| Claude Code | `claude plugin marketplace update qp-skills` then `claude plugin update qp-skills@qp-skills` |

Restart the host if the update is not active, or use its supported reload in the current session. Updating files from another terminal does not refresh instructions already loaded in a conversation. An older updater may need one manual manager update to acquire the current procedure.

See [update lifecycle and activation](skills/qp-update/references/lifecycle.md) for details about selective installs, local modifications, and verification.

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
