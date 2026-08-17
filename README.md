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

Read the detailed [v1 changelog](CHANGELOG.md) for the public baseline and release scope.

## Start

Use Alarina when you need help to choose the right skill:

```text
Use alarina to choose the right QP skill for this request:

[describe the outcome you need]
```

## Outcome processes

| Skill | Use when |
| --- | --- |
| `arojinle` | A material plan or design needs a complete decision tree, durable records, and final confirmation |
| `atona` | Architecture or migration work needs one live plan through delivery |
| `alaga` | One supplied build job needs job-level integration, acceptance, documentation or knowledge reconciliation, or applicable candidate review |
| `tdd` | One bounded feature or bug fix needs an explicit test-first implementation loop without broader build-job stewardship |
| `qp-code-review` | Bounded code or a PR/MR needs broad or defect-only review |
| `seda-pr` | A bounded current-branch change needs commit, push, and a clear ready-for-review GitHub PR or GitLab MR |
| `wo-pr` | An open PR or MR needs active CI and feedback stewardship through readiness and later changes until explicit stop or closure |
| `salaye` | One user-supplied subject needs a plain-language explanation for a first-time reader |
| `triage-issue` | One issue or bug report needs supplied-evidence-first assessment before implementation |
| `seda-ticket` | Supplied work needs consumable vertical tickets with blockers, acceptance, and lifecycle state |
| `audit-refactor-behavior` | A refactor or rewrite needs a behavior-parity ledger |
| `html-artifact` | Supplied content, evidence, decisions, diagrams, or design specifications need translation into a checked, portable browser artifact |

## Specialists and utilities

| Skill | Use when |
| --- | --- |
| `alarina` | You need to choose the shortest QP route for a request |
| `amose` | Project terms, `CONTEXT.md`, domain rules, `.learnings`, `.nongoals`, or ADRs need clarification or reconciliation |
| `simplify` | Changed code or code-local comments need a read-only maintainability review |
| `pare` | An entire repository needs a read-only, coverage-complete audit for material simplifications |
| `skill-portfolio-audit` | A bounded skill portfolio needs a read-only audit of inventory, health, state drift, routes, or capability gaps |
| `handoff` | A conversation needs a compact handoff for another agent or session |
| `ayewo-igba-ise` | A coding-agent session or bounded multi-session corpus needs an evidence-backed friction and recurrence analysis |
| `iwadi` | A question needs high-trust research from primary sources, captured in a Markdown file |
| `ko-skill` | A portable agent skill needs creation, revision, or validation |
| `irinse` | A companion engineering tool needs selection, setup, safe use, or removal |
| `olofofo` | A literal agent session needs quiet continuity, proportionate quality nudges, and reusable cross-session wisdom |
| `ro-wo` | A material premise needs a brief evidence-backed check before agreement or disagreement |

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

## Optional agent instructions

Add any of these snippets to your `AGENTS.md`, `CLAUDE.md`, or equivalent agent-instruction file.

### Default Olofofo companion

Copy the exact managed block from [Olofofo global activation](skills/olofofo/references/global-activation.md) into the supported global instruction file for your agent. This activates Olofofo after the first material task in each literal session. Olofofo keeps one living record, nudges only for material quality gaps, and curates global OGBON wisdom as evidence without becoming the task owner or changing EMI instructions.

### Companion-tool routing

```text
Use `irinse` when a companion tool could materially improve the result. If the required tool is unavailable, explain its benefit and ask before installing or configuring it.
```

### Consider before judgment

```text
Use `ro-wo` before agreeing or disagreeing with a material premise. Test the evidence, strongest credible alternative, changed boundaries, and failure paths. Withhold judgment when evidence is insufficient. Do not manufacture objections or reopen settled decisions without new material evidence.
```
