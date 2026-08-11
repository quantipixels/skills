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
| `audit-refactor-behavior` | A refactor or rewrite needs a behavior-parity ledger |
| `html-artifact` | A report, visualization, prototype, demo, or bounded interactive tool needs one checked HTML artifact |

## Specialists and utilities

| Skill | Use when |
| --- | --- |
| `alarina` | You need to choose the shortest QP route for a request |
| `alakowe` | Repository documentation, lightweight ADRs, or `.nongoal` need reconciliation |
| `simplify` | Changed code or code-local comments need a read-only maintainability review |
| `handoff` | A conversation needs a compact handoff for another agent or session |
| `ayewo-igba-ise` | A coding-agent session needs an evidence-backed friction analysis |
| `iwadi` | A question needs high-trust research from primary sources, captured in a Markdown file |
| `ko-skill` | A portable agent skill needs creation or revision |
| `qp-setup` | A coding-agent baseline needs communication instructions and companion-tool choices |
