# QP Agent Skills

QP Agent Skills is a portable collection of focused skills for established codebases. It helps you make decisions, plan work, implement changes, review code, and craft checked HTML artifacts from durable records to interactive prototypes.

Read the public documentation at [quantipixels.com/skills](https://quantipixels.com/skills).

## Install

```bash
npx skills add quantipixels/skills --global
```

Install one or more named skills with `--skill <name>`.

## Uninstall

Remove an installed skill by name:

```bash
npx skills remove <skill-name>
```

Add `--global` when you installed the skill globally.

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
| `seda-pr` | A GitHub PR or GitLab MR needs a clear zero-context title, narrative, and bounded metadata |
| `wo-pr` | An open PR or MR needs active CI and feedback stewardship until it is ready for a human merge decision |
| `tunmo-pr` | A PR or MR needs a read-only explanation for a first-time reviewer |
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

## Optional agent instruction

Add this to your agent instructions when you want QP's companion-tool routing available by default:

```text
Use Irinṣẹ when a companion tool could materially improve the result. If the required tool is unavailable, explain its benefit and ask before installing or configuring it.
```
