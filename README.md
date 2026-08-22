# QP Agent Skills

QP Agent Skills is a portable collection of focused skills for established codebases. It helps you make decisions, plan work, implement changes, review code, and craft portable HTML artifacts from durable records to interactive prototypes.

Skills are organized into exclusive Engineering, Design, Productivity, and Experimental source groups.

Browse the [QP Agent Skills documentation](https://quantipixels.com/skills).

## Portfolio shape

- Skills belong to one Engineering, Design, Productivity, or Experimental source group, with interactive group selection during installation.
- Test-first delivery stays with Alaga, maintainability review stays with Pare, skill portfolio auditing stays with Ko Skill, and stateful refactor-parity auditing stays with Àtúnwò.
- Alaga handles bounded features and supplied build jobs through integration, proof, documentation, and applicable review.

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
| `atona` | Architecture or migration work needs one live plan through delivery |
| `atunwo` | `broad`, `defect-only`, or read-only refactor-parity `audit` is needed in `general` local/supplied or `provider` PR/MR mode; broad review consumes Pare `review` evidence |
| `irinse` | A companion engineering tool needs selection, setup, safe use, or removal |
| `ko-skill` | Creates, revises, or validates one skill through one workflow; bounded portfolio audits remain read-only |
| `pare` | Read-only `audit` or `review` finds material simplifications and classifies implementation, dependency, support-artifact, and test cleanup candidates |
| `se-triage` | One issue or bug report needs supplied-evidence-first assessment before implementation |
| `seda-pr` | A bounded current-branch change needs commit, push, and a clear ready-for-review GitHub PR or GitLab MR; invoke the skill explicitly |
| `seda-ticket` | Supplied work needs consumable vertical tickets with blockers, acceptance, and lifecycle state |
| `wo-pr` | An open PR or MR needs active CI and feedback stewardship through readiness and later changes until explicit stop or closure; invoke the skill explicitly |

## Design skills

Use `apere` when a design request is broad, ambiguous, or spans several deliverables; invoke the narrowest owner directly for focused work:

| Skill | Use when |
| --- | --- |
| `apere` | Broad or multi-deliverable design work needs owner selection, prerequisites, dependency order, shared constraints, or an approval boundary |
| `amoye-ui-ux` | UI/UX direction needs searchable styles, palettes, typography, accessibility, charts, stack rules, or a persisted MASTER/page direction |
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
| `arojinle` | A material plan or design needs a complete decision tree, durable records, and final confirmation |
| `ayewo-igba-ise` | A coding-agent session or bounded multi-session corpus needs an evidence-backed friction and recurrence analysis |
| `handoff` | A conversation needs a compact handoff for another agent or session |
| `html-artifact` | Supplied results, purpose-fit reports, analysis, data, decisions, or designs need a portable visual explanation for a zero-context reader |
| `iwadi` | A question needs high-trust research from primary sources, captured in a Markdown file |
| `ro-wo` | A material premise needs a brief evidence-backed check before agreement or disagreement |
| `salaye` | One user-supplied subject needs a plain-language explanation for a first-time reader |
| `technical-writing` | Developer documentation, technical communication, or applicable human-facing artifact copy needs layered structure and sentence-level clarity |
| `yo-slop` | Human- or agent-facing prose needs a final pass for AI tells, filler, vague abstraction, or instruction noise without changing meaning |

## Experimental skills

Experimental skills must be selected explicitly during installation.

| Skill | Use when |
| --- | --- |
| `olofofo` | A literal agent session needs quiet continuity, proportionate quality nudges, and reusable cross-session wisdom |

## Optional agent instructions

Add any of these snippets to your `AGENTS.md`, `CLAUDE.md`, or equivalent agent-instruction file.

### Default Olofofo companion

Copy the exact managed block from [Olofofo global activation](skills/experimental/olofofo/references/global-activation.md) into the supported global instruction file for your agent. This activates Olofofo after the first material task in each literal session. Olofofo keeps one living record, nudges only for material quality gaps, and curates global OGBON wisdom as evidence without becoming the task owner or changing EMI instructions.

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
