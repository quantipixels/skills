---
name: ko-skill
description: Author, revise, or validate one portable agent skill, or audit a bounded skill portfolio. Focus on one owned outcome, deep-module composition, the smallest behavior-bearing contract, selectively loaded expert depth, and proportionate proof.
---

# Kọ Skill

Create, revise, or validate one exact skill. Mutation requires explicit authority; validation and portfolio audit are read-only. For a bounded portfolio audit, read [portfolio audit](references/portfolio-audit.md).

Never infer installation, activation, synchronization, publication, provider, or other external mutation authority from source changes.

## 1. Pin the owned outcome

Read repository/host instructions, the complete candidate skill package, and affected metadata, manifest, catalog, router, and decision records. Pin the requested operation, exact candidate, desired outcome, triggers, exclusions, mutation authority, adjacent owners, and current `source | installed | active | published` evidence when relevant.

Revise an existing outcome owner instead of creating a competitor. Create a skill only when it owns a recurring independently useful outcome, decision, or failure mode that ordinary documentation or an existing owner does not already close.

For a behavior correction, use pinned existing evidence when it proves the failure; otherwise exercise the pre-change candidate with the smallest safe realistic goal. Preserve accepted behavior that the new evidence does not contradict. When authorized retrospective evidence is needed, consume an exact-current `ayewo-igba-ise` result rather than mining unrelated history directly.

## 2. Choose the smallest control shape

Classify the skill from the control its outcome actually requires:

- **lightweight** — a few consequential invariants can produce the native result; no internal lifecycle, ordered multi-stage recovery, or several independently authorized side effects are required;
- **workflow** — correctness depends on ordered stages, durable/external state, stale or partial results, recovery/retry, multiple candidates/actors, or distinct side-effect authorities.

Broad reach or importance does not make a skill a workflow. Do not add phases, statuses, schemas, receipts, failure taxonomies, or authority ceremony unless they change correctness, safety, authority, recovery, or completion. Simplify an existing workflow when those controls no longer affect the outcome.

## 3. Compose skills as deep modules

A skill owns one native result. Keep the dependency boundary narrow in both directions.

A **caller** may specify why the result is needed, the bounded input/candidate, freshness, caller-owned acceptance, authority, recovery, and stop conditions. It should normally say the outcome it needs and consume the native result.

A **callee** owns its procedure, internal stages/statuses, resources, scripts, verification, persistence mechanics, representation mechanics, and native result shape. Do not make it expose a caller-specific receipt/envelope dialect merely because one orchestrator consumes it.

Therefore:

- do not copy a supporting skill's procedure, checks, statuses, lifecycle, resource-loading rules, output schema, or verification into callers;
- do not copy a caller's plan/job/phase schema into the supporting skill;
- pass exact identity/freshness and only the context needed to perform the owned result;
- keep detailed evidence with its native owner and link or reference it instead of cloning it;
- repeat only independently required safety, trust, authority, or acceptance rules;
- let routing skills describe owners when route selection is itself their outcome.

Prefer directional composition such as `Use <skill> to <owned outcome>` or `Use <skill> to visualise <semantic result>`. For `html-artifact`, callers normally state what should be visualised, the audience or primary-view role when material, and supply the semantic source; HTML Artifact owns layout, artifact lifecycle, implementation, accessibility, and verification. For `akosile`, semantic owners supply the record/artifact kind, stable subject, and semantic content; Akọsílẹ̀ owns paths, safe writes, and indexing.

Treat a duplicated procedure or caller-specific result dialect as an ownership defect unless evidence proves that the repeated contract is independently necessary at that boundary.

## 4. Write the smallest useful contract and preserve expert depth

Treat user constraints as the target contract. Map the candidate's material capabilities across selection, owned outcome, control flow, authority/safety, state/recovery, proof, integrations, and completion. Mark each `retain | change | move | remove`; use capabilities, not sentence count, to prove preservation.

Before adding a rule, first try to delete, merge, replace, or move existing prose. Give every behavior one shortest clear owner. Keep a second representation when it adds a distinct decision, safety, authority, recovery, verification, owner boundary, or material calibration that the primary form does not carry well.

Keep `SKILL.md` focused on the owned outcome, trigger, universally required behavior, control flow, authority, and completion boundary. Use progressively disclosed references for cohesive expertise that materially improves recurring judgment. A substantial reference is valid when its branch is selective and its knowledge is non-obvious; do not optimize reference size or file count as an end in itself.

When adding, expanding, splitting, moving, or removing an ordinary skill reference, read [reference quality](references/reference-quality.md). It owns the distinction between decision-bearing expert depth, over-compression, duplicated documentation, and disguised catalogues.

When deciding whether substantial skill depth belongs in guidance, native/project tooling, a focused library, a bundled script, or a deterministic engine, read [deep capability placement](references/deep-capabilities.md). Choose placement from the owned outcome and natural capability boundary rather than equating depth with executable code.

Write for a capable agent:

- front-load the owned outcome, trigger, and exclusions in the description;
- keep selector-facing metadata about this skill rather than its implementation dependencies;
- keep universally required behavior in `SKILL.md` and load branch-specific references only at the branch that needs them;
- use judgment for variable work and precision only where a wrong interpretation is consequential;
- point to discoverable environment facts, commands, configuration, schemas, and project tooling instead of caching them in prose;
- use concise examples, counterexamples, `Good / Bad`, `Prefer / Avoid`, or similar calibration when they sharpen a recurring non-obvious distinction or prevent a plausible wrong interpretation; and
- remove rationale, history, generic advice, repeated summaries, and reference-owned procedure that does not change execution or judgment.

Name a mode only when distinct behavior/authority requires one; use the shortest clear verb or verb phrase.

When adding, keeping, expanding, moving, or replacing a bundled script, read [bundled-script boundary](references/script-boundary.md). A script must own one necessary mechanical `input → deterministic output` seam; semantic judgment stays in the skill.

When the skill is a broad researched knowledge catalogue or resolver companion, read [researched knowledge catalogues](references/knowledge-catalogues.md) and prefer progressive disclosure over a custom retrieval runtime. Do not classify an execution companion or ordinary deep reference as a catalogue merely because its subject or reference is broad.

Follow repository provider policy for provider-capable owners. Do not propagate provider procedure into non-provider callers.

Set invocation policy only from the selection/authority boundary. Use explicit-only invocation when automatic selection itself would cross a material authority or opt-in boundary; keep equivalent host metadata consistent.

## 5. Prove the exact candidate

Use the smallest proof that can falsify the changed contract:

- **structural** — metadata, paths, references, packaging, manifest/router parity, deterministic invariants;
- **baseline** — pre-change evidence only when correcting behavior or claiming behavioral equivalence;
- **forward** — one or a few fresh realistic goals only when selection, authority, safety, state, branching, composition, reference retrieval, or output remains materially uncertain;
- **final** — reread the exact final candidate and rerun only proof invalidated by the change.

Match proof to control shape. A lightweight skill does not need workflow-shaped scenarios. A workflow must prove only the transitions, stale/partial states, authority boundaries, and recovery paths that can change its result.

For a compression, reference-depth, or ownership refactor, compare the same goal/candidate before and after when material uncertainty remains. Prove both directions when relevant: removed material was not behavior-bearing, and newly deepened material changes a plausible judgment without forcing unrelated context. Hide the expected answer and deny mutation/credentials unless a disposable scenario explicitly authorizes them.

Do not create prompt-evaluation suites to defend wording. Follow repository policy for deterministic tests and package validation. Add an independent reviewer only when consequence or ambiguity justifies it.

For validation, classify every material obligation as `proved`, `defect`, `evidence gap`, or `not applicable`. Return `VERIFIED` only when required proof passes against the exact candidate, `CHANGES_REQUIRED` for a proved defect, and `INSUFFICIENT_EVIDENCE` for a material proof gap. Validation does not authorize repair.

## 6. Integrate and report

With mutation authority, reconcile affected host metadata, package/release surfaces, catalog/router entries, and direct references. Preserve unrelated work. Changes to installation, activation, synchronization, publication, or provider state require their own authority.

Report the operation, exact candidate, owned outcome/control shape, changed files, material capability moves/removals, reference dispositions when applicable, dependency-boundary changes, script dispositions when applicable, proof and gaps, and observed `source | installed | active | published` state. For substantial simplification, include before/after size only as evidence of change, never as the acceptance target.
