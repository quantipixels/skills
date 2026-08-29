---
name: ko-skill
description: Author, revise, or validate one portable agent skill, or audit a bounded skill portfolio. Focus on one owned outcome, deep-module composition, the smallest adequate capability/resource placement, selectively loaded expert depth, and proportionate proof.
---

# Kọ Skill

Create, revise, or validate one exact skill. Mutation requires explicit authority; validation and portfolio audit are read-only. For a bounded portfolio audit, read [portfolio audit](references/portfolio-audit.md).

Never infer installation, activation, synchronization, publication, provider, or other external mutation authority from source changes.

## 1. Pin the owned outcome

Read repository/host instructions, the complete candidate skill package, and affected metadata, manifest, router/catalog, and decision records. Pin the requested operation, exact candidate, desired outcome, triggers, exclusions, mutation authority, adjacent owners, and current `source | installed | active | published` evidence when relevant.

Revise an existing outcome owner instead of creating a competitor. Create a skill only when it owns a recurring independently useful outcome, authority/artifact/acceptance boundary, failure mode, or useful reusable model-steering contract that ordinary documentation or an existing owner does not already close. Do not remove a lightweight skill merely because the base model can perform the underlying act; a small skill such as `salaye` may still earn its place by reliably invoking one useful behavior without requiring users to restate a long instruction.

For a behavior correction, use pinned existing evidence when it proves the failure; otherwise exercise the pre-change candidate with the smallest safe realistic goal. Preserve accepted behavior that new evidence does not contradict.

## 2. Choose the smallest control shape

Classify the skill from the control its outcome actually requires:

- **lightweight** — a few consequential invariants can produce the native result; no internal lifecycle, ordered multi-stage recovery, or several independently authorized side effects are required;
- **workflow** — correctness depends on ordered stages, durable/external state, stale or partial results, recovery/retry, multiple candidates/actors, or distinct side-effect authorities.

Broad reach or importance does not make a skill a workflow. Do not add phases, statuses, schemas, receipts, failure taxonomies, or authority ceremony unless they change correctness, safety, authority, recovery, or completion.

## 3. Compose skills as deep modules

A skill owns one native result. Keep the dependency boundary narrow in both directions.

A caller may specify why the result is needed, bounded input/candidate, freshness, caller-owned acceptance, authority, recovery, and stop conditions. A callee owns its procedure, internal stages/statuses, resources, scripts, verification, persistence mechanics, representation mechanics, and native result shape.

Therefore:

- do not copy a supporting skill's procedure, checks, statuses, lifecycle, resource-loading rules, output schema, or verification into callers;
- do not copy a caller's plan/job/phase schema into the supporting skill;
- pass exact identity/freshness and only context required for the owned result;
- keep detailed evidence with its native owner and link it instead of cloning it;
- repeat only independently required safety, trust, authority, or acceptance rules;
- let routing skills describe owners only when route selection is itself their outcome.

For `html-artifact`, callers supply semantic source plus reader/audience intent when material; HTML Artifact owns representation and verification. For `akosile`, semantic owners supply record/artifact kind, stable subject, and semantic content; Akọsílẹ̀ owns canonical paths, safe publication, worktree mechanics, and indexing.

## 4. Place capabilities and resources before writing files

Before adding scripts, commands, templates, data, reusable assets, or another public owner, read [capability and resource placement](references/resource-placement.md). Decompose the outcome into material capabilities and select the first adequate surface:

```text
SKILL.md guidance / selective expert reference
→ literal command / short recipe
→ repository/project/provider/framework/IDE tool
→ focused library
→ narrow deterministic script kernel
→ engine only when deterministic machinery carries a substantial part of the owned outcome
```

Do this during ordinary skill creation/revision, not only during later audits. Then challenge every retained executable and support resource again before finalizing the candidate.

When substantial expert depth belongs in a reference, read [reference quality](references/reference-quality.md). When an executable is still proposed, read [script boundary](references/script-boundary.md). When a genuinely broad researched knowledge corpus is itself the result, read [knowledge catalogues](references/knowledge-catalogues.md). Use [deep capabilities](references/deep-capabilities.md) when deciding whether several mechanics genuinely form an engine-backed capability.

Keep `SKILL.md` focused on the owned outcome, trigger, universally required behavior, control flow, authority, and completion boundary. Load branch-specific references only at the branch that needs them.

Write for a capable agent:

- assume the agent can inspect its available tools/capabilities and adapt ordinary execution accordingly; state the semantic behavior or result rather than enumerating harness-specific capability fallbacks;
- do not spell out subagent/tool/orchestration fallback branches that a capable agent can derive from its environment; require a concrete mechanism only when it establishes a correctness invariant, authority boundary, deterministic result, non-obvious safety property, or compatibility constraint;
- point to discoverable environment facts, current commands/configuration/schemas, and project tooling instead of caching them in prose;
- use concise examples, counterexamples, `Good / Bad`, `Prefer / Avoid`, or stable vocabulary when they sharpen recurring non-obvious judgment;
- keep commands short and visible when they materially clarify an evidence/authority boundary;
- do not turn references into language/framework/tool manuals or command catalogues;
- use neutral templates only for stable recurring semantic shapes; existing project/native scaffolds outrank bundled starters;
- bundle data only when curated knowledge itself is part of the useful result; avoid duplicate CSV/Markdown representations and volatile ecosystem caches;
- make reusable assets conditional when their behavior is not universal; and
- remove rationale, history, generic advice, repeated summaries, default-heavy examples, and reference-owned procedure that does not change execution or judgment.

Name a mode only when distinct behavior/authority requires one; use the shortest clear verb or verb phrase.

Follow repository provider policy for provider-capable owners. Do not propagate provider procedure into non-provider callers.

## 5. Prove the exact candidate

Use the smallest proof that can falsify the changed contract:

- **structural** — metadata, paths, nested references/resources, packaging, manifest/router parity, deterministic invariants;
- **baseline** — pre-change evidence only when correcting behavior or claiming behavioral equivalence;
- **forward** — one or a few fresh realistic goals when selection, authority, safety, state, branching, composition, command use, reference retrieval, template/resource choice, or output remains materially uncertain;
- **final** — reread the exact final candidate and rerun only proof invalidated by the change.

Match proof to control shape. A lightweight skill does not need workflow-shaped scenarios. A workflow proves only transitions, stale/partial states, authority boundaries, and recovery paths that can change its result.

For compression, ownership, script replacement, catalogue reduction, template/resource reduction, or public-skill consolidation, compare the same realistic goal/candidate before and after when material uncertainty remains. Prove both directions: removed material was not behavior-bearing, and the smaller/new placement still produces the owned result without silently losing expertise, authority, proof, or discoverability.

Do not create prompt-evaluation suites merely to defend wording. Follow repository policy for deterministic tests and package validation. Add an independent reviewer only when consequence or ambiguity justifies it.

For validation, classify every material obligation as `proved`, `defect`, `evidence gap`, or `not applicable`. Return `VERIFIED` only when required proof passes against the exact candidate, `CHANGES_REQUIRED` for a proved defect, and `INSUFFICIENT_EVIDENCE` for a material proof gap. Validation does not authorize repair.

## 6. Integrate and report

With mutation authority, reconcile affected host metadata, package/release surfaces, router/catalog entries, direct references, deterministic tests, CI, and resource links. Preserve unrelated work. Installation, activation, synchronization, publication, or provider state require separate authority.

Report the operation, exact candidate, owned outcome/control shape, changed files, material capability/resource moves/removals, reference/script/template/data/asset dispositions when applicable, dependency-boundary changes, proof and gaps, and observed `source | installed | active | published` state. For substantial simplification, include before/after size only as evidence of change, never as the acceptance target.
