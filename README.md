# QP Agent Skills

QP Agent Skills is a portable collection of focused skills for established codebases. It helps you make decisions, plan work, implement changes, review code, and craft portable HTML artifacts from durable records to interactive prototypes.

Skills are organized into exclusive Engineering, Design, Productivity, and Experimental source groups.

Read the public documentation at [quantipixels.com/skills](https://quantipixels.com/skills).

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

Read the detailed [v1 changelog](CHANGELOG.md) for the public baseline and release scope.

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
| `audit-refactor-behavior` | A refactor or rewrite needs a behavior-parity ledger |
| `irinse` | A companion engineering tool needs selection, setup, safe use, or removal |
| `ko-skill` | `one-skill` mode creates, revises, or validates a skill; `portfolio-audit` mode audits a bounded portfolio |
| `pare` | Read-only `audit` or `review` finds material simplifications and classifies implementation, dependency, support-artifact, and test cleanup candidates |
| `qp-code-review` | `broad` or `defect-only` review is needed in `general` local/supplied or `provider` PR/MR mode; broad review consumes Pare `review` evidence |
| `seda-pr` | A bounded current-branch change needs commit, push, and a clear ready-for-review GitHub PR or GitLab MR |
| `seda-ticket` | Supplied work needs consumable vertical tickets with blockers, acceptance, and lifecycle state |
| `triage-issue` | One issue or bug report needs supplied-evidence-first assessment before implementation |
| `wo-pr` | An open PR or MR needs active CI and feedback stewardship through readiness and later changes until explicit stop or closure |

## Design skills

Use `apere` as the end-to-end router, or invoke the narrowest owner directly:

| Skill | Use when |
| --- | --- |
| `apere` | A visual request spans specialists or needs its built-in `logo`, `corporate identity program`, `icons`, or `social graphics` mode |
| `amoye-ui-ux` | UI/UX recommendations need searchable styles, palettes, typography, accessibility, charts, or stack rules |
| `brand` | Brand voice, identity, assets, or consistency needs a source of truth |
| `eto-apere` | Tokens, CSS variables, component specs, or theme architecture need definition |
| `asa-oju-ibanisoro` | Components and responsive interfaces need accessible Tailwind/shadcn implementation, with an explicit UI-library choice |
| `banner-design` | Social, ad, web hero, cover, or print banners need exact platform constraints |
| `slides` | Presentations and pitch decks need narrative, layout, and chart guidance |

For React UI work, `asa-oju-ibanisoro` asks for an explicit component-library decision and keeps the local 14-library inventory in `skills/design/asa-oju-ibanisoro/references/ui-component-libraries.md`.

## Productivity skills

| Skill | Use when |
| --- | --- |
| `alarina` | You need to choose the shortest QP route for a request |
| `arojinle` | A material plan or design needs a complete decision tree, durable records, and final confirmation |
| `ayewo-igba-ise` | A coding-agent session or bounded multi-session corpus needs an evidence-backed friction and recurrence analysis |
| `google-developer-style` | Developer documentation or technical communication in any language needs drafting, revision, or review with applicable Google style principles |
| `handoff` | A conversation needs a compact handoff for another agent or session |
| `html-artifact` | Supplied results, purpose-fit reports, analysis, data, decisions, or designs need a portable visual explanation for a zero-context reader |
| `iwadi` | A question needs high-trust research from primary sources, captured in a Markdown file |
| `ro-wo` | A material premise needs a brief evidence-backed check before agreement or disagreement |
| `salaye` | One user-supplied subject needs a plain-language explanation for a first-time reader |

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
Use `irinse` when a companion tool could materially improve the result. If the required tool is unavailable, explain its benefit and ask before installing or configuring it.
```

### Google developer style for documentation and communication

```text
Use `google-developer-style` when drafting, revising, or reviewing developer documentation or technical communication in any language. Apply the language community's conventions, project-specific style, channel conventions, product truth, and code conventions first. Transfer the guide's ideas about clarity, tone, audience, terminology, structure, and accessibility; do not impose English grammar, spelling, capitalization, politeness, or sentence patterns on another language. For communication outside documentation, apply only the principles that fit the channel. Do not generalize language-specific, documentation-only, or product-specific rules.
```

### Clear mode names

```text
Name new or changed skill modes with the shortest clear verb or verb phrase. Prefer names such as `audit`, `review`, `clean`, and `deep-clean`. Do not repeat the skill name, target artifact, implementation detail, or other context that the owning skill already supplies. Add a qualifier only when it changes authority, risk, or outcome and the unqualified name would be ambiguous.
```

### Consider before judgment

```text
Use `ro-wo` before agreeing or disagreeing with a material premise. Test the evidence, strongest credible alternative, changed boundaries, and failure paths. Withhold judgment when evidence is insufficient. Do not manufacture objections or reopen settled decisions without new material evidence.
```
