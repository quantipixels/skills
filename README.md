# QP Agent Skills

QP Agent Skills is a portable collection of focused skills for established codebases. It helps you make decisions, plan work, implement changes, review code, and craft checked HTML artifacts from durable records to interactive prototypes.

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
| `tunmo-pr` | A PR or MR needs a read-only explanation for a first-time reviewer |
| `triage-issue` | One issue or bug report needs local-first evidence assessment before implementation |
| `seda-ticket` | Settled phases and review candidates in an Atona-style HTML plan need a checked local ticket graph; use `html-artifact` for its bounded update |
| `audit-refactor-behavior` | A refactor or rewrite needs a behavior-parity ledger |
| `html-artifact` | A report, visualization, prototype, demo, or bounded interactive tool needs one checked HTML artifact |

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
| `irinse` | A companion engineering tool needs selection, setup, safe use, or removal |

## Optional agent instructions

Add any of these snippets to your `AGENTS.md`, `CLAUDE.md`, or equivalent agent-instruction file.

### Companion-tool routing

```text
Use Irinṣẹ when a companion tool could materially improve the result. If the required tool is unavailable, explain its benefit and ask before installing or configuring it.
```

### Critical judgment

```text
When the user asks for an opinion, test the premise critically and adversarially, state material counterarguments, and recommend from evidence instead of defaulting to agreement.
```
