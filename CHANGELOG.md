# Changelog

This file records released, user-visible changes to QP Agent Skills. Version `1.0.0` is the clean public baseline. Earlier internal history is intentionally not included.

## 2.0.0

### Major Changes

- [#18](https://github.com/quantipixels/skills/pull/18) [`2b086b7`](https://github.com/quantipixels/skills/commit/2b086b708a9a12521c694fe25cc3f4f25b1dfe41) Thanks [@mosobande](https://github.com/mosobande)! - Retire the public `audit-refactor-behavior` identifier. Use `atunwo` in `audit` scope for read-only behavior-parity audits and pass its exact-current ledger and guardrails to `alaga` for refactor implementation.

- [#15](https://github.com/quantipixels/skills/pull/15) [`4755809`](https://github.com/quantipixels/skills/commit/47558096034432c4231055d6525a249215ff8d3d) Thanks [@mosobande](https://github.com/mosobande)! - Retire `tdd`, `simplify`, and `skill-portfolio-audit` as standalone skills. Preserve test-first delivery under Alaga, maintainability review under `atunwo`, and portfolio auditing under Ko Skill through conditional references that load only for the applicable mode. Teach Alarina to select and report modes for multimode skills, restore tone marks in displayed Yorùbá skill headings, and make HTML Artifact request material input gaps and produce visual explanations for zero-context readers instead of prose-heavy reports.

- [#15](https://github.com/quantipixels/skills/pull/15) [`1cc948d`](https://github.com/quantipixels/skills/commit/1cc948db70a52320ed2de881bdbacaaa6667564e) Thanks [@mosobande](https://github.com/mosobande)! - Move every skill into one exclusive Engineering, Design, Productivity, or Experimental source group. Add combinable group installer flags, recommend Engineering plus Productivity, document interactive selection through the Skills CLI, keep Experimental opt-in outside `--all`, and remove only retired identifiers that the Skills CLI attributes to the QP repository.

- [#18](https://github.com/quantipixels/skills/pull/18) [`29b0752`](https://github.com/quantipixels/skills/commit/29b0752e29ebeea10a1ca31685d749e75ef18f39) Thanks [@mosobande](https://github.com/mosobande)! - Rename the public `qp-code-review` skill identifier to `atunwo` and `triage-issue` to `se-triage`. Display the skills as Àtúnwò and Ṣe Triage while keeping exact identifiers ASCII-safe for routing and invocation.

### Minor Changes

- [#8](https://github.com/quantipixels/skills/pull/8) [`c067486`](https://github.com/quantipixels/skills/commit/c0674868ce5f6755d6523188d2eff883d2f3bff0) Thanks [@mosobande](https://github.com/mosobande)! - Make Alaga the builder for one supplied job with one or many delivery units. Alaga now selects useful capabilities from current evidence, composes specialist-owned results through one job envelope, returns overlapping work to an active ancestor instead of invoking it again, preserves explicit authority and candidate identities, continues safe independent work through a confirmed continuation boundary and partial blockers, and closes only after job-level proof and the review required for each candidate type. Ko Skill owns agent-skill verification. Qualifying jobs keep one concise living HTML report under a deterministic structural, continuity, authority, and risk threshold; Alaga owns job-state decisions, the report is their authoritative durable record, and HTML Artifact owns its representation and file lifecycle.

- [#15](https://github.com/quantipixels/skills/pull/15) [`ce402a1`](https://github.com/quantipixels/skills/commit/ce402a14cc19b8b4fecf6d4d152f3c23ab32bea0) Thanks [@mosobande](https://github.com/mosobande)! - Give Amose a visible, vendor-neutral `CONTEXT.md` contract for canonical domain language and separate that responsibility from `.learnings`.

- [#15](https://github.com/quantipixels/skills/pull/15) [`b67219b`](https://github.com/quantipixels/skills/commit/b67219b70bb6048987c5252a168b7cb5d49a305d) Thanks [@mosobande](https://github.com/mosobande)! - Extend Àyẹ̀wò Ìgbà Iṣẹ́ from one-session retrospectives to bounded multi-session corpus analysis with explicit evidence units, request coverage, sampling, recurrence proof, counterevidence, per-project dossiers, and corpus reporting.

- [#3](https://github.com/quantipixels/skills/pull/3) [`146048c`](https://github.com/quantipixels/skills/commit/146048c37772e212ebc83fdb1145502bcb0599b1) Thanks [@mosobande](https://github.com/mosobande)! - Add Amọ̀ṣẹ́ as the shared owner for domain-model clarification, evidence-backed `.learnings`, authorized `.nongoals`, and lightweight ADR lifecycle. Distinguish durable project exclusions from deferrals, implemented behavior, and task-local boundaries before updating `.nongoals`. Add Irinṣẹ as the shared owner for companion-tool selection, setup, safe bounded use, verification, and removal, with progressive references for tldr-code, ast-grep, Semgrep, and IntelliJ MCP. Replace the superseded Alakowe and QP Setup routes, keep ordinary documentation with its outcome owner, and validate skill behavior through exact-candidate headless and independent sessions. Make Ko Skill gate every author-owned change on behavioral benefit, write descriptions for skill selection, and use examples only when they improve agent behavior or proof.

- [#8](https://github.com/quantipixels/skills/pull/8) [`c067486`](https://github.com/quantipixels/skills/commit/c0674868ce5f6755d6523188d2eff883d2f3bff0) Thanks [@mosobande](https://github.com/mosobande)! - Clarify Alarina's build, implementation, and independent-outcome routing. Preserve direct specialist builders when one published owner fully covers the artifact, route skill validation to Ko Skill, keep prose for selection-critical overlap and authority rules, use one complete route table for simple recommendations, make triage supplied-evidence-first, and reconcile the public catalog with the current Irinṣẹ and Olofofo inventory.

- [#18](https://github.com/quantipixels/skills/pull/18) [`2539497`](https://github.com/quantipixels/skills/commit/2539497d4a50c6ff09a27c92189b566552809199) Thanks [@mosobande](https://github.com/mosobande)! - Make `ko-skill` the explicit skill-authoring owner and replace its ambiguous modes with `author`, read-only `validate`, and read-only portfolio `audit`. Add capability-ledger compression, layered proof, exact state receipts, and a smaller portfolio audit; update public routing and correct Pare metadata to match its read-only boundary.

- [#15](https://github.com/quantipixels/skills/pull/15) [`ce402a1`](https://github.com/quantipixels/skills/commit/ce402a14cc19b8b4fecf6d4d152f3c23ab32bea0) Thanks [@mosobande](https://github.com/mosobande)! - Keep Arojinle's complete decision-tree interview concise while composing Amọ̀ṣẹ́ and HTML Artifact without repeating their contracts. Streamline Ko Skill integration and verification while retaining host-schema, provider-safety, final-diff, and lifecycle-state checks.

- [#15](https://github.com/quantipixels/skills/pull/15) [`b67219b`](https://github.com/quantipixels/skills/commit/b67219b70bb6048987c5252a168b7cb5d49a305d) Thanks [@mosobande](https://github.com/mosobande)! - Require substantial HTML reports to reconcile supplied content coverage and whole-record consistency before delivery.

- [#15](https://github.com/quantipixels/skills/pull/15) [`ce402a1`](https://github.com/quantipixels/skills/commit/ce402a14cc19b8b4fecf6d4d152f3c23ab32bea0) Thanks [@mosobande](https://github.com/mosobande)! - Remove dependency-owned workflow detail from `atona` and `pare` while preserving their plan integration and simplification judgments. Teach `ko-skill` to keep dependency procedures, resources, checks, statuses, output schemas, and lifecycle derivations with their owners while retaining caller-owned inputs, result freshness, integration, acceptance, authority, recovery, and stop gates. Use exact skill identifiers in operational prose and preserve display names for headings. Preserve independently required safety and trust contracts.

- [#15](https://github.com/quantipixels/skills/pull/15) [`1cc948d`](https://github.com/quantipixels/skills/commit/1cc948db70a52320ed2de881bdbacaaa6667564e) Thanks [@mosobande](https://github.com/mosobande)! - Make HTML Artifact reports select and retain one industry, exact purpose-fit format, and executive, working, or archival density profile from a compact family model that covers product design, project management, PRDs, business plans, evidence, research, audits, experiments, decisions, technical assessments, performance analytics, comparisons, incidents, presentations, and case studies. Resolve overlaps by the primary reader's decision and keep secondary purposes in supporting sections or appendices. Lead with scan-critical content, use conceptual visuals where they clarify the result, segment and collapse non-critical logs, split materially large raw logs into accepted companion bundles, space sections clearly, bound table columns, and wrap long identifiers without changing their values. Add stable deep-link disclosure, complete print expansion with screen-state restoration, and informative log summaries.

- [#15](https://github.com/quantipixels/skills/pull/15) [`b67219b`](https://github.com/quantipixels/skills/commit/b67219b70bb6048987c5252a168b7cb5d49a305d) Thanks [@mosobande](https://github.com/mosobande)! - Make material handoff transitions explicit and propagate accepted project decisions while their evidence is current.

- [#5](https://github.com/quantipixels/skills/pull/5) [`2e18a79`](https://github.com/quantipixels/skills/commit/2e18a79b03e4cdc0b703b5a1d218706171c28f91) Thanks [@mosobande](https://github.com/mosobande)! - Add `seda-pr` and `wo-pr` for PR and MR publication and stewardship. `seda-pr` commits scoped work, pushes the current branch without force, and creates or updates a ready item. `wo-pr` monitors an open item and handles bounded branch, CI, and feedback work. Neither skill approves or merges.

- [#6](https://github.com/quantipixels/skills/pull/6) [`d8df677`](https://github.com/quantipixels/skills/commit/d8df67760942a37c9872451afb6130865156a9d9) Thanks [@mosobande](https://github.com/mosobande)! - Make `ko-skill` validation proportionate: check structural surfaces directly, use the smallest fresh-session proof that resolves material behavioral uncertainty, and stop for direction before validation scope expands materially. Require behavior-preserving compression across the complete skill and linked references, semantic rule-owner comparison, compact procedural workflows, and evidence that clarity and safety remain intact. Make `seda-pr` invocation authorize bounded staging, commit, and non-force push while preserving its zero-context third-party narrative. Require `seda-pr` and `wo-pr` to reject custom provider hosts before network contact until the exact normalized host receives separate trust, and prohibit fixed readiness windows in `wo-pr`. Correct the Claude Code instruction import and keep the README release claim within the changelog's actual scope.

- [#5](https://github.com/quantipixels/skills/pull/5) [`7645b8b`](https://github.com/quantipixels/skills/commit/7645b8ba7fe6980a9538af208a55edd8317c1956) Thanks [@mosobande](https://github.com/mosobande)! - Add `se-triage` for local-first assessment of one issue or bug report before implementation. Supplied evidence is the default boundary; source inspection, GitHub or GitLab reads, and one evidence-backed provider comment require separate explicit authority. Confirmed handoffs use durable behavioral briefs, matching local artifacts resume established facts without repeated questions, and authorized source reads check existing behavior and prior project decisions by domain concept.

  Remove committed prompt eval suites and the repository skill validator. Verify skill metadata, the public catalog, and Alarina routing directly during exact-candidate review. Material behavior now uses exact-candidate headless sessions and independent scenario review outside repository source.

  Replace the Wo PR state engine with a small observer checkpoint. Remove its deterministic state-engine test only with the deleted `watch_core.py` owner; retain and run the provider normalization tests. The removed fixed settle window, persistent lease and takeover protocol, stored mutation authority and failure classifications, and claimed-feedback state machine are obsolete. Current lifecycle, authority, provider, retry, receipt, and readiness expectations live in the Wo PR skill and provider references.

- [#15](https://github.com/quantipixels/skills/pull/15) [`ce402a1`](https://github.com/quantipixels/skills/commit/ce402a14cc19b8b4fecf6d4d152f3c23ab32bea0) Thanks [@mosobande](https://github.com/mosobande)! - Add `pare` for complete read-only repository audits with explicit subsystem coverage, honest partial states, bounded reviews, independently verified simplification findings, adversarial audit validation, and dependency-aware priorities.

- [`0b2ab74`](https://github.com/quantipixels/skills/commit/0b2ab741c01c4642a6db378670234bce1ecdcf90) - Add `olofofo` as a quiet default session companion with optional global and project EMI steering, one adaptive global HTML artifact, proportionate evidence-backed quality nudges, curated global OGBON wisdom, explicit title permission, and no workflow-controller role. OGBON stays a compact, selectively loaded, conflict-safe evidence store; EMI remains user-controlled steering and project learning remains with Amọ̀ṣẹ́. Include a narrow portable global activation payload without adding a daemon, hook, or shared setup runtime.

  Replace the unreleased `tunmo-pr` candidate with `salaye`, a minimal skill for explaining one user-supplied subject from its available evidence in plain language for a first-time reader.

- [#15](https://github.com/quantipixels/skills/pull/15) [`b67219b`](https://github.com/quantipixels/skills/commit/b67219b70bb6048987c5252a168b7cb5d49a305d) Thanks [@mosobande](https://github.com/mosobande)! - Add `ro-wo`, a brief evidence-backed premise check used before agreeing or disagreeing with a material opinion, proposal, assumption, scenario, recommendation, or decision-shaping hypothetical.

- [#15](https://github.com/quantipixels/skills/pull/15) [`ce402a1`](https://github.com/quantipixels/skills/commit/ce402a14cc19b8b4fecf6d4d152f3c23ab32bea0) Thanks [@mosobande](https://github.com/mosobande)! - Ship a read-only Alaga helper that partitions intended and ambient worktree changes, records exact Git and filesystem state, hashes present content, detects concurrent drift, and emits a stable candidate digest for uncommitted review candidates.

- [#15](https://github.com/quantipixels/skills/pull/15) [`ce402a1`](https://github.com/quantipixels/skills/commit/ce402a14cc19b8b4fecf6d4d152f3c23ab32bea0) Thanks [@mosobande](https://github.com/mosobande)! - Streamline HTML Artifact around supplied-content fidelity, accessible visual rendering, safe portable resources, opt-in non-UI verification, and direct delivery while preserving its conditional report and prototype contracts. Keep primary information visible, collapse logs and secondary detail, and ship reusable style-neutral theme, visual-foundation, and carousel controls.

- [#8](https://github.com/quantipixels/skills/pull/8) [`c067486`](https://github.com/quantipixels/skills/commit/c0674868ce5f6755d6523188d2eff883d2f3bff0) Thanks [@mosobande](https://github.com/mosobande)! - Clarify that Seda Ticket defaults to outcome-complete vertical slices and permits non-vertical tickets only with a necessary, independently testable exception and a named green integration boundary. Make Atona prefer deep modules at clean seams, apply the deletion test, and reject speculative or pass-through modules without a proven ownership, integration, lifecycle, policy, or testing reason.

- [#6](https://github.com/quantipixels/skills/pull/6) [`174fc7b`](https://github.com/quantipixels/skills/commit/174fc7b4140b6d9c1a1e5273b49bdebf182a2f61) Thanks [@mosobande](https://github.com/mosobande)! - Refocus `html-artifact` on translating supplied material and design specifications into portable visual HTML without originating content, product or editorial design, candidates, recommendations, or decisions. Default to a layperson with no prior topic context. Add resilient Tailwind and Mermaid enhancements, semantic code diffs, report and supplied-variant patterns, opt-in non-UI verification, portability status, and direct-path delivery through concise branch references. Omit default-prompt metadata.

### Patch Changes

- [#7](https://github.com/quantipixels/skills/pull/7) [`73e84f9`](https://github.com/quantipixels/skills/commit/73e84f91d16360f9f7c96a1904367a0fa3493acb) Thanks [@mosobande](https://github.com/mosobande)! - Deepen internal skill modules without changing their public outcomes: localize `atunwo` provider publication, split Amọ̀ṣẹ́ durable destinations, and move Atona delivery tracking and status-specific handoffs behind direct conditional references. Restore Ko Skill guards for exact reference triggers, cohesive conditional rules, purposeful and compressive examples, exact-candidate proof, and the limits of structural validation. Compress high-value guidance in Alaga, Handoff, HTML Artifact, Simplify, and TDD without weakening its owning rules.

- [#10](https://github.com/quantipixels/skills/pull/10) [`50cadb3`](https://github.com/quantipixels/skills/commit/50cadb3f274fa7d2e0eba4fcbf79dc3730d7393e) Thanks [@mosobande](https://github.com/mosobande)! - Harden `atunwo` provider operations with explicit custom-host trust, credential isolation, complete GitHub pagination, exact-head refresh before every write, and durable per-write readback receipts. Reconcile the public 1.0 changelog with the current Alaga, Irinṣẹ, and Ko Skill boundaries.

- [#4](https://github.com/quantipixels/skills/pull/4) [`7426359`](https://github.com/quantipixels/skills/commit/74263594af9b96a26ff779aa7d37e25f89711a1f) Thanks [@mosobande](https://github.com/mosobande)! - Add a source-aware global uninstall script with batch removal and post-removal verification, and document its executable command.

- [#15](https://github.com/quantipixels/skills/pull/15) [`b67219b`](https://github.com/quantipixels/skills/commit/b67219b70bb6048987c5252a168b7cb5d49a305d) Thanks [@mosobande](https://github.com/mosobande)! - Reduce Ṣàlàyé to plain-language explanation of one user-supplied subject for a first-time reader, and clarify the boundaries between living session continuity and point-in-time handoff, including contract transitions and unavailable-source recovery.

- [#15](https://github.com/quantipixels/skills/pull/15) [`b67219b`](https://github.com/quantipixels/skills/commit/b67219b70bb6048987c5252a168b7cb5d49a305d) Thanks [@mosobande](https://github.com/mosobande)! - Require Alaga to pin one real acceptance path and to track accepted multi-surface visual references through implementation and visual verification.

- [#15](https://github.com/quantipixels/skills/pull/15) [`b67219b`](https://github.com/quantipixels/skills/commit/b67219b70bb6048987c5252a168b7cb5d49a305d) Thanks [@mosobande](https://github.com/mosobande)! - Bound every Seda PR provider CLI command to 120 seconds. Treat timeout writes as unknown state and require exact-target readback before any retry.

- [#4](https://github.com/quantipixels/skills/pull/4) [`7426359`](https://github.com/quantipixels/skills/commit/74263594af9b96a26ff779aa7d37e25f89711a1f) Thanks [@mosobande](https://github.com/mosobande)! - Require TDD workflows to remove temporary smoke proof after green unless it provides distinct durable regression coverage.

- [#4](https://github.com/quantipixels/skills/pull/4) [`7426359`](https://github.com/quantipixels/skills/commit/74263594af9b96a26ff779aa7d37e25f89711a1f) Thanks [@mosobande](https://github.com/mosobande)! - Make Arojinle and Iwadi follow active delegation policy, and give existing repository research conventions precedence over Iwadi's fallback path.

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
