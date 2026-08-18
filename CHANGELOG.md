# Changelog

This file records released, user-visible changes to QP Agent Skills. Version `1.0.0` is the clean public baseline. Earlier internal history is intentionally not included.

## Unreleased

- Expand `pare` into one read-only simplification specialist with repository `audit` and bounded candidate `review` modes.
- Rename `qp-code-review` to `atunwo` and `triage-issue` to `se-triage`; use Àtúnwò and Ṣe Triage as their display names.
- Route maintainability-only work to Pare `review`; `atunwo` keeps broad and defect-only verdicts and consumes exact-current Pare evidence for broad review.
- Let `atunwo` return a read-only provider candidate handoff when another skill owns the requested code-review outcome.
- Move read-only stateful refactor parity audits into `atunwo`; keep refactor implementation with `alaga` and retire the standalone `audit-refactor-behavior` route.
- Send accepted Pare slices to Alaga with explicit proof and authority boundaries; route Ayewo recommendations to Pare only for evidenced codebase simplification.
- Require Ko Skill to reduce or relocate existing prose before adding a net-new rule.
- Replace Ko Skill's authority modes with one shared single-skill workflow, explicit mutation authority, semantic claim tracing, and a conditional read-only portfolio audit.

## 1.0.0

### Overview

- Establish QP Agent Skills as a portable collection of focused skills for established codebases.
- Provide one clean public baseline for decisions, architecture planning, implementation, test-backed delivery, review, and portable HTML artifacts.

### Decision and planning

- `arojinle` for complete decision interviews, explicit deferrals, confirmation, and durable decision records.
- `atona` for evidence-backed architecture and migration plans through delivery and closeout.

### Delivery and review

- `alaga` for bounded test-first changes and supplied build jobs with one or many delivery units, integrated proof, and the review required by each candidate type.
- `qp-code-review` for bounded maintainability-only, broad, or defect-only code review.
- `audit-refactor-behavior` for behavior-parity evidence during stateful refactors and rewrites.

### Artifacts and handoffs

- `html-artifact` for portable visual explanations, reports, prototypes, demos, and bounded interactive tools, with active input-gap requests, zero-context presentation, and evidence safeguards.
- `handoff` for compact, evidence-backed transfer to another agent or session.

### Toolkit operation

- `alarina` to select the shortest useful QP route.
- `irinse` for selecting, configuring, and safely using companion engineering tools.
- `ayewo-igba-ise` for coding-agent session friction analysis.
- `iwadi` for high-trust research from primary sources, captured in a Markdown file.
- `ko-skill` for portable skill creation, revision, exact-candidate validation, and bounded portfolio audits.
