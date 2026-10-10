# QP Skills

Agent skills for planning, research, engineering, design, and writing, by Oluwaseyi Sobande. Each skill gives your agent a method for a particular kind of work, with supporting references and tools where needed.

Everything starts with **Alárinà (`alarina`)**, the working rules that keep Claude and Codex on your outcome:

- It uses SIGIDI's tools (delegation, worktrees, PR watching, inline pages, previews) instead of rebuilding them.
- It proves results on the real product.
- It never pushes, merges, deploys or deletes without you.

Install the whole collection as a Codex or Claude Code plugin, or pick individual skills with Skills CLI.

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

Alárinà's full workflow needs all QP skills. Each skill also works on its own, but install the companions your work needs. For example, HTML plans from `atona` use `ojuiwe`.

Skills CLI installs skills only. Use the Claude Code plugin if you also want Alárinà as a native agent.

## Use the skills

You never need a skill's name. Describe what you want in plain words; Alárinà and your agent pick the skill that owns it. The names (Yorùbá words) are only labels.

Alárinà runs the default path by itself: each step hands to the next, and it stops only for your decisions, your stop point, or anything risky such as pushing, merging or deleting. Short tasks start at the first step not already settled.

| Step | What you want | Skill |
| --- | --- | --- |
| Start | Work on your outcome with SIGIDI, real proof and no harmful actions; follow the default path and route to the skills below. | [Alárinà · `alarina`](skills/alarina/SKILL.md) |
| 1 | Work out what you want and settle the important choices through an interview. | [Ìbéèrè · `ibeere`](skills/ibeere/SKILL.md) |
| 1b | Get ideas and alternative directions when there is no clear way forward. | [Àbá · `aba`](skills/aba/SKILL.md) |
| 2 | Write the spec: the problem, who it is for, and checks that prove it is done. | [Ṣẹ̀dá spec · `seda-spec`](skills/seda-spec/SKILL.md) |
| 3 | Try ideas as throwaway prototypes before deciding; three distinct UI versions by default. | [Àdánwò · `adanwo`](skills/adanwo/SKILL.md) |
| 4 | Plan how to build it, in order, with risks. | [Atọ́nà · `atona`](skills/atona/SKILL.md) |
| 5 | Cut the work into tickets, each a thin end-to-end slice you can check on its own. | [Ṣẹ̀dá ticket · `seda-ticket`](skills/seda-ticket/SKILL.md) |
| 6 | Build or fix a change, with proof. | [Akọ́lé · `akole`](skills/akole/SKILL.md) |
| 6 | Triage a report, find why something fails or is slow, or recover an incident. | [Àyẹ̀wò · `ayewo`](skills/ayewo/SKILL.md) |
| 6 | Measure and benchmark a change, and decide keep or revert. | [Ìwọ̀n · `iwon`](skills/iwon/SKILL.md) |
| 6 | Hand slices to subagents in parallel and pick each one's model and effort. | [Aṣojú · `asoju`](skills/asoju/SKILL.md) |
| 7 | Create or maintain a project skill that drives the real product and keeps evidence. | [Ìjẹ́rìísí · `ijerisi`](skills/ijerisi/SKILL.md) |
| 7 | Use the product like its users before shipping, and fix what breaks. | [Lò ó wò · `loowo`](skills/loowo/SKILL.md) |
| 8 | Review a change, a codebase, its structure or a supplied fix, and give a verdict. | [Àtúnwò · `atunwo`](skills/atunwo/SKILL.md) |
| 9 | Open and steer a PR/MR through CI and feedback to your merge decision. | [Ṣẹ̀dá PR · `seda-pr`](skills/seda-pr/SKILL.md) |
| 10 | Keep a lesson that matters in the project's docs, and reflect on a session. | [Ìrònú · `ironu`](skills/ironu/SKILL.md) |

Used along the way:

| What you want | Skill |
| --- | --- |
| Survey, design or document structure and interfaces. | [Ìgbékalẹ̀ · `igbekale`](skills/igbekale/SKILL.md) |
| Pin down domain terms, rules and lifecycles; keep decision records and the README's non-goals. | [Ìtumọ̀ · `itumo`](skills/itumo/SKILL.md) |
| Research with sources, or dissect a whole repository into a reference document. | [Ìwádìí · `iwadi`](skills/iwadi/SKILL.md) |
| Teach a concept or a piece of the codebase so it sticks. | [Kọ́ mi · `komi`](skills/komi/SKILL.md) |
| Show it with the smallest view: a tree, pseudocode, a diagram, a table or a diff. | [Fíhàn mi · `fihanmi`](skills/fihanmi/SKILL.md) |
| Turn a report into an HTML page, or build a prototype or interactive view, inline in SIGIDI or as a file. | [Ojú-ìwé · `ojuiwe`](skills/ojuiwe/SKILL.md) |
| Write, review or simplify prose for people. | [Ọ̀rọ̀ · `oro`](skills/oro/SKILL.md) |
| Write or fix skills, prompts and agent instructions. | [Ìlànà · `ilana`](skills/ilana/SKILL.md) |
| Keep docs, lessons included, true to the code. | [Akọ̀wé · `akowe`](skills/akowe/SKILL.md) |
| Build and keep your personal defaults from your instructions and recent sessions, read by every agent host. | [Àṣà mi · `asami`](skills/asami/SKILL.md) |
| Remove comments that repeat the code; move real rules into code. | [Ìmọ́tótó · `imototo`](skills/imototo/SKILL.md) |

Browse [`skills/`](skills/) for the rest: Yorùbá language guidance, macOS disk cleanup and private local sharing.

## Where things are saved

Records that should last with the code are committed in your repo:

```text
your-repo/
├── docs/
│   ├── internal/            for maintainers
│   │   ├── solutions/       lessons from solved work
│   │   ├── decisions/       decisions and why
│   │   └── operations/      runbooks: deploy, backup, restore
│   └── user/                guides for people using the project
├── README.md                includes a "Non-goals" section
└── .qp -> ~/.qp/<owner>/<repo>/    link to your working records (never committed)
```

If your repo already keeps these somewhere else, such as `docs/adr/`, the skills use that place.

Working records stay outside the repo, so every worktree of the repo shares them and deleting a worktree loses nothing:

```text
~/.qp/<owner>/<repo>/
├── specs/
├── tickets/
├── plans/
├── prototypes/
└── reports/
```

Scratch files go to your temp folder.

### Change the defaults

Settings are optional: tell the agent, or add a `qp.yaml` file. See [settings](docs/user/settings.md) for every key.

## Non-goals

- One central controller that owns every specialist's outcome, skips an owner's approval steps, or needs one provider's runtime.
- Rigid generic templates for READMEs, APIs, OpenAPI files, changelogs or ADRs.
- A new public skill when an existing one can own the outcome cleanly.

## Update

Update through the manager you installed with:

| Host | Commands, in order |
| --- | --- |
| Codex | `codex plugin marketplace upgrade qp-skills` then `codex plugin add qp-skills@qp-skills` |
| Claude Code | `claude plugin marketplace update qp-skills` then `claude plugin update qp-skills@qp-skills` |
| Skills CLI | `npx skills add quantipixels/skills --agent <host> --skill '<names>'` with the same scope you installed with |

Start a new session after updating. A running conversation keeps the instructions it already loaded. Avoid an unqualified `npx skills update` if you only mean to update QP, because it also updates unrelated skills.

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
