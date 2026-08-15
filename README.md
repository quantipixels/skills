# QP Agent Skills

QP Agent Skills is a portable collection of focused skills for established codebases. It helps you make decisions, plan work, implement changes, review code, and craft checked HTML artifacts from durable records to interactive prototypes.

The design skills are maintained locally in this repository and run from their bundled guidance and resources.

Read the public documentation at [quantipixels.com/skills](https://quantipixels.com/skills).

## Install

```bash
npx skills add quantipixels/skills --global
```

Install one or more named skills with `--skill <name>`.

## Uninstall

Remove all globally installed QP skills:

```bash
curl -fsSL https://raw.githubusercontent.com/quantipixels/skills/ori/scripts/uninstall.sh | bash
```

## Releases

Read the detailed [v1 changelog](CHANGELOG.md) for the public baseline, release scope, and future Changesets policy.

## Start

Use Alarina when you need help to choose the right skill:

```text
Use alarina to choose the right QP skill for this request:

[describe the outcome you need]
```

## Outcome processes

| Skill | Use when |
| --- | --- |
| `arojinle` | A plan or decision needs a complete decision tree and confirmation |
| `atona` | Architecture or migration work needs one live plan through delivery |
| `alaga` | One feature candidate needs clarification, test-backed implementation, and broad review |
| `tdd` | A feature or bug fix needs a test-first implementation loop |
| `qp-code-review` | Bounded code or a PR/MR needs broad or defect-only review |
| `seda-pr` | A ready-for-review GitHub PR or GitLab MR needs a clear zero-context title, narrative, and bounded metadata |
| `wo-pr` | An open PR or MR needs active CI and feedback stewardship through readiness and later changes until explicit stop or closure |
| `salaye` | An idea, plan, decision, document, or code candidate needs conversational exploration, explanation, investigation, research, analysis, or evaluation |
| `triage-issue` | One issue or bug report needs local-first evidence assessment before implementation |
| `seda-ticket` | Supplied work needs consumable vertical tickets with blockers, acceptance, and lifecycle state |
| `audit-refactor-behavior` | A refactor or rewrite needs a behavior-parity ledger |
| `html-artifact` | Supplied content, evidence, decisions, diagrams, or design specifications need translation into a checked, portable, highly visual browser artifact |

## Specialists and utilities

| Skill | Use when |
| --- | --- |
| `alarina` | You need to choose the shortest QP route for a request |
| `amose` | Project terms, domain rules, `.learnings`, `.nongoals`, or ADRs need clarification or reconciliation |
| `simplify` | Changed code or code-local comments need a read-only maintainability review |
| `handoff` | A conversation needs a compact handoff for another agent or session |
| `ayewo-igba-ise` | A coding-agent session needs an evidence-backed friction analysis |
| `iwadi` | A question needs high-trust research from primary sources, captured in a Markdown file |
| `ko-skill` | A portable agent skill needs creation or revision |
| `qp-setup` | A coding-agent baseline needs communication instructions and companion-tool choices |

## Design skills

Use `apere` as the end-to-end router, or invoke the narrowest owner directly:

| Skill | Use when |
| --- | --- |
| `apere` | A visual request spans brand, UI, graphics, logos, mockups, social assets, or icons |
| `amoye-ui-ux` | UI/UX recommendations need searchable styles, palettes, typography, accessibility, charts, or stack rules |
| `brand` | Brand voice, identity, assets, or consistency needs a source of truth |
| `eto-apere` | Tokens, CSS variables, component specs, or theme architecture need definition |
| `asa-oju-ibanisoro` | Components and responsive interfaces need accessible Tailwind/shadcn implementation, with an explicit UI-library choice |
| `banner-design` | Social, ad, web hero, cover, or print banners need exact platform constraints |
| `slides` | Presentations and pitch decks need narrative, layout, and chart guidance |

For React UI work, `asa-oju-ibanisoro` asks for an explicit component-library decision and keeps the local 14-library inventory in `skills/asa-oju-ibanisoro/references/ui-component-libraries.md`.
| `irinse` | A companion engineering tool needs selection, setup, safe use, or removal |
| `olofofo` | A literal agent session needs quiet continuity, proportionate quality nudges, and reusable cross-session wisdom |

## Optional agent instructions

Add any of these snippets to your `AGENTS.md`, `CLAUDE.md`, or equivalent agent-instruction file.

### Default Olofofo companion

Copy the exact managed block from [Olofofo global activation](skills/olofofo/references/global-activation.md) into the supported global instruction file for your agent. This activates Olofofo after the first material task in each literal session. Olofofo keeps one living record, nudges only for material quality gaps, and curates global OGBON wisdom as evidence without becoming the task owner or changing EMI instructions.

### Companion-tool routing

```text
Use Irinṣẹ when a companion tool could materially improve the result. If the required tool is unavailable, explain its benefit and ask before installing or configuring it.
```

### Critical judgment

```text
When the user asks for an opinion, test the premise critically and adversarially, state material counterarguments, and recommend from evidence instead of defaulting to agreement.
```
