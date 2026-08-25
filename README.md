# QP Agent Skills

QP Agent Skills is a portable collection of focused skills for established codebases. It helps you make decisions, plan work, implement changes, review code, and craft portable HTML artifacts from durable records to interactive prototypes.

Skills are organized into exclusive Engineering, Design, Productivity, and Experimental source groups.

Browse the [QP Agent Skills documentation](https://quantipixels.com/skills).

## Portfolio shape

- Skills belong to one Engineering, Design, Productivity, or Experimental source group, with interactive group selection during installation.
- Test-first delivery stays with Alaga, maintainability review stays with Pare, skill portfolio auditing stays with Ko Skill, and stateful refactor-parity auditing stays with Àtúnwò.
- Alaga handles bounded features and supplied build jobs through integration, proof, documentation, and applicable review.
- Solution Architect owns portable technical architecture design and read-only review. Atọ́nà owns the wider initiative plan through delivery and closure.
- Under an active Atọ́nà plan, specialists return exact-current receipts to one HTML plan instead of creating parallel user-facing reports. Standalone outcomes keep their native records.

## Install

Install the QP skill portfolio globally:

```bash
npx skills add quantipixels/skills --global
```

Follow the Skills CLI prompts to choose skills and target agents. The command does not remove retired skills.

### Install from a local checkout

```bash
npx skills add .
```

The local selection groups the portfolio under `Qp Skills` (`qp-skills`). Its Claude display name and repository identity remain `quantipixels/skills`.

### Install in Claude Code

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

## Uninstall

Remove all globally installed QP skills:

```bash
curl -fsSL https://raw.githubusercontent.com/quantipixels/skills/ori/scripts/uninstall.sh | bash
```

## Releases

Read the [latest GitHub release](https://github.com/quantipixels/skills/releases/latest) and the repository [changelog](CHANGELOG.md).

## Start

Use Alarina when you need help to choose the right skill:

```text
Use alarina to choose the right QP skill for this request:

[describe the outcome you need]
```

## Engineering skills

| Skill | Use when |
| --- | --- |
| `alaga` | `test-first` mode handles one bounded feature or fix; `job` mode handles a supplied build job through integration, acceptance, reconciliation, and applicable review |
| `amose` | Project terms, `CONTEXT.md`, domain rules, `.learnings`, `.nongoals`, or ADRs need clarification or reconciliation |
| `atona` | Unclear feature, migration, or initiative work needs one exact-current plan through delivery and closure |
| `atunwo` | `broad`, `defect-only`, or read-only refactor-parity `audit` is needed in `general` local/supplied or `provider` PR/MR mode; broad review consumes Pare `review` evidence |
| `hitl-review` | One human needs a first-reader walkthrough, independent `atunwo` evidence, finding dispositions, and a final decision on one exact code candidate |
| `irinse` | A companion engineering tool needs selection, setup, safe use, or removal |
| `ko-skill` | Creates, revises, or validates one skill through one workflow; bounded portfolio audits remain read-only |
| `pare` | Read-only `audit` or `review` finds material simplifications and classifies implementation, dependency, support-artifact, and test cleanup candidates |
| `se-triage` | One issue or bug report needs supplied-evidence-first assessment before implementation |
| `seda-pr` | A bounded current-branch change needs commit, push, and a GitHub PR or GitLab MR; new items are ready by default, while draft creation or state transitions require an explicit request |
| `seda-ticket` | Supplied work needs consumable vertical tickets with blockers, acceptance, and lifecycle state |
| `seda-sigidi` | An AI agent needs a named soul installed into the config its host loads, ported across hosts, or refreshed from evidence |
| `solution-architect` | Technical architecture needs a portable implementation design or read-only sufficiency review across the active stack and domain |
| `wo-pr` | An open PR or MR needs active CI and feedback stewardship through readiness and later changes until explicit stop or closure |

## Design skills

Use `apere` when a design request is broad, ambiguous, or spans several deliverables; invoke the narrowest owner directly for focused work:

| Skill | Use when |
| --- | --- |
| `apere` | Broad or multi-deliverable design work needs owner selection, prerequisites, dependency order, shared constraints, or an approval boundary |
| `amoye-ui-ux` | UI/UX direction needs searchable styles, palettes, typography, accessibility, charts, stack rules, or one composable recommendation |
| `brand` | Brand voice, identity, logos, corporate identity assets, custom icon language, or consistency needs a durable source of truth |
| `social-graphics` | Feed posts, carousels, stories, reusable social templates, or multi-format social campaigns need exact platform variants |
| `eto-apere` | Tokens, CSS variables, component specs, generated configuration, or theme architecture need definition or migration |
| `asa-oju-ibanisoro` | Components, responsive interfaces, and product icons need accessible Tailwind/component-library implementation |
| `banner-design` | A cover, header, hero, display ad, or print banner needs confirmed current platform or custom constraints |
| `slides` | Presentations and pitch decks need narrative, layout, and chart guidance |

For multi-deliverable production, `apere` returns the design route packet and `alaga` owns the integrated build job. For React UI work, `asa-oju-ibanisoro` asks for an explicit component-library decision and keeps the local library inventory in `skills/design/asa-oju-ibanisoro/references/ui-component-libraries.md`.

## Productivity skills

| Skill | Use when |
| --- | --- |
| `alarina` | You need to choose the shortest QP route for a request |
| `arojinle` | One consequential product, plan, or design decision needs a complete interview, durable records, and final confirmation |
| `ayewo-igba-ise` | A coding-agent session or bounded multi-session corpus needs an evidence-backed friction and recurrence analysis |
| `handoff` | A conversation needs a compact handoff for another agent or session |
| `html-artifact` | Supplied results, purpose-fit reports, analysis, data, decisions, or designs need a portable visual explanation for a zero-context reader |
| `iwadi` | A question needs high-trust research from primary sources, captured in a Markdown file |
| `ro-wo` | A material premise needs a brief evidence-backed check before agreement or disagreement |
| `salaye` | One user-supplied subject needs a plain-language explanation for a first-time reader |
| `technical-writing` | Developer documentation, technical communication, or applicable human-facing artifact copy needs layered structure and sentence-level clarity |
| `yo-slop` | Human- or agent-facing prose needs cleanup or explicit verbosity pruning without changing its contract |

## Experimental skills

Experimental skills must be selected explicitly during installation.

| Skill | Use when |
| --- | --- |
| `pepeye` | A task needs provider-neutral lifecycle control across QP-native playbooks, leaf owners, proof, pause or pickup, and final learning |

## Optional agent instructions

Add any of these snippets to your `AGENTS.md`, `CLAUDE.md`, or equivalent agent-instruction file.

### Default Pepeye lifecycle mode

Copy the exact managed block from [Pepeye portable activation](skills/experimental/pepeye/references/portable-activation.md) into a supported global instruction file. This activates Pepeye as the task-wide controller when the host can expose the skill and current context. Explicit invocation remains the fallback. Pepeye selects and advances a playbook while leaf skills retain their specialist outcomes, procedures, and authority gates.

`olofofo` is retired and no longer published by this plugin. An installed copy can remain active until its host removes it. Replace an authorized Olofofo activation block through the migration branch in [Pepeye portable activation](skills/experimental/pepeye/references/portable-activation.md); preserve existing reports and OGBON evidence.

### Companion-tool routing

```text
Use `irinse` when a companion tool could materially improve the result.
```

### Technical writing and prose cleanup

```text
Use `technical-writing` and `yo-slop` for communication.
```

### Consider before judgment

```text
Use `ro-wo` before agreeing or disagreeing with a material premise.
```
