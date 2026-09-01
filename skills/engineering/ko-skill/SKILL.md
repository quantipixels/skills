---
name: ko-skill
description: Author, revise, or validate one portable agent skill, or audit a bounded skill portfolio. Focus on one owned outcome, deep-module composition, the smallest adequate capability/resource placement, selectively loaded expert depth, and proportionate proof.
---

# Kọ Skill

Create, revise, or validate one exact skill. Mutation requires explicit authority; validation and portfolio audit are read-only. Never infer installation, activation, synchronization, publication, provider, or other external mutation authority from source changes. For a bounded portfolio audit, read [portfolio audit](references/portfolio-audit.md).

## 1. Own one outcome

Read the candidate package plus affected repository/host instructions and integration metadata. Pin the operation, exact candidate, desired outcome, triggers, exclusions, authority, adjacent owners, and relevant `source | installed | active | published` evidence.

Grow capability depth faster than public surface area. Revise an existing owner instead of creating a competitor when it can absorb the capability without weakening its outcome contract.

A public skill must pass both tests:

1. **Capability value** — it owns a recurring independently useful outcome, authority/artifact/acceptance boundary, failure mode, or useful reusable model-steering contract.
2. **Public identity value** — independent selection or direct invocation materially improves the interface for a user or genuinely independent caller through clearer selection, authority, result identity, reuse, or lower recurring instruction burden than keeping the capability behind an existing owner.

A useful capability can fail the second test. When folding it behind an existing owner preserves the benefit while reducing public/routing complexity, deepen that owner instead of exposing another name. Do not remove a lightweight skill merely because the base model can perform the act when its named public identity reliably saves users or independent callers from restating material behavior.

Use the smallest control shape that preserves correctness:

- **lightweight** — consequential invariants can directly produce the result;
- **workflow** — correctness genuinely depends on ordered stages, durable/external state, stale/partial recovery, multiple actors/candidates, or distinct side-effect authorities.

Do not add lifecycle, statuses, receipts, schemas, or ceremony merely because the outcome is important.

### Admit deliberate behavior, not only minimal prose

A capable agent's default behavior is not automatically the desired behavior for a skill. Keep an instruction when it deliberately overrides a likely default tendency and the resulting cost materially improves this owner's outcome.

For each consequential instruction, establish default tendency → failure prevented → forced override → value → cost → trigger → cross-owner composition. Do not optimize away deliberate friction merely because a base model could proceed with less of it; a valuable mechanism with an over-broad trigger is still defective.

Before creating a new skill/reference or appending another paragraph, try to express the missing behavior at its owning surface as one precise invariant or one discriminating `Good / Bad` example. Extract only when the result is independently useful or selectively loaded non-obvious judgment remains. Prefer replacing existing guidance over stacking another rule beside it.

## 2. Compose and place capability

Treat skills as deep modules. A caller supplies only the bounded input, reason/freshness/authority and caller-owned acceptance needed by the callee. The callee retains its procedure, internal state, resources, verification, persistence/representation mechanics, and native result. Do not copy lifecycle/result schemas across owner boundaries; repeat only independently required safety, trust, authority, acceptance, or owner-specific steering rules.

Write for a capable agent. State semantic behavior, invariants, authority and completion; let the agent adapt ordinary search, shell/filesystem work, Git use, editing, tool discovery, and equivalent orchestration to its available environment. Do not pre-author capability fallback trees the agent can infer. Ordinary delegation is agent-owned; prescribe isolation only when bounded independent/noisy work must leave the primary context to preserve focus, continuity, or independent observation.

Concrete mechanics earn instruction space when the mechanism establishes correctness, authority, determinism, non-obvious safety, a machine/external protocol, or a compatibility boundary, or when a small operational anchor materially reduces recurring rediscovery of how to enter a selected concrete capability. Do not use operational anchors to preselect/copy open-ended vendor/library/framework/source inventories; keep volatile details subject to current evidence.

Before adding or retaining commands, references, scripts, templates, data, assets, or another public owner, read [capability and resource placement](references/resource-placement.md). Keep `SKILL.md` focused on the universally required contract and load branch-specific depth only where needed. In prose, link package-local resources directly. When a local resource cannot reasonably be linked, make its base explicit as relative to the directory containing this `SKILL.md` (the skill root), for example `SKILL_ROOT/references/example.md`; do not leave bare `references/...`, `assets/...`, `templates/...`, or `scripts/...` paths whose base must be inferred.

For human-facing artifacts, distinguish **representation proof** from **experience proof**. HTML or ordinary document interactivity does not earn UI/browser assurance unless rendered experience itself is part of the owner's acceptance contract.

Good: a postmortem/report gets structural proof and, only when readability is materially uncertain, one bounded render smoke; a checkout prototype gets browser interaction proof because interaction is being evaluated.

Bad: a filterable report triggers viewport/theme/filter/accessibility browser matrices merely because it is polished or interactive.

When material expert judgment belongs outside `SKILL.md`, use [reference quality](references/reference-quality.md). If executable code still appears necessary after placement, apply [script boundary](references/script-boundary.md). Use [knowledge catalogues](references/knowledge-catalogues.md) only when a maintained researched corpus is itself part of the useful outcome.

For multi-host portability, keep one canonical semantic contract in the skill/owning source. Host manifests, rules, hooks, or command adapters should be the thinnest projection needed by actual loader semantics; do not maintain divergent handwritten copies of the behavior. Mechanically verify projections when an adapter exists and semantic drift would be consequential. Do not add host adapters merely to claim compatibility that current installation/distribution already provides.

Name modes only when behavior or authority truly differs. Prefer current project/provider/framework/tool truth over cached command catalogues or starter defaults.

Reference another repository skill by its exact frontmatter `name` trigger in backticks, for example `alarina`. Do not use another skill's localized/display title as a cross-skill identifier. Within this repository, `skill`, `route`, `owner`, `specialist`, and similar terms already refer to the portfolio; do not add a redundant repository namespace prefix unless a real external namespace must be distinguished.

### Format for execution

Use prose for connected rationale/invariants, bullets for parallel obligations, numbered lists only when order matters, tables for finite states/mappings/comparisons, and fenced blocks for exact schemas/commands/state/result shapes. Split dense prose when the agent would otherwise have to reconstruct a hidden checklist; do not create bullets/headings merely to make a file look structured.

## 3. Prove the exact candidate

Use the smallest evidence that can falsify the changed contract. Structural/package validation is baseline; add realistic forward behavior only when selection, authority, safety, state, branching, composition, resource choice, or output remains materially uncertain. Re-run only proof invalidated by later changes.

For behavior corrections, use pinned pre-change evidence when it already proves the failure; otherwise exercise the smallest safe realistic baseline. For compression, script/catalogue/template removal, ownership moves, or skill consolidation, compare the same realistic goal before/after when material uncertainty remains. Prove both that removed material was not uniquely behavior-bearing and that the smaller placement preserves result quality, authority, proof, discoverability, and any useful operational anchor.

For model-steering changes with material uncertainty, compare the same realistic bounded task/candidate/context under the prior/no contract and changed contract, verify the intended behavioral delta plus preserved correctness/safety/output, and keep the proof temporary unless recurring stable risk earns a regression suite.

Do not claim saved LOC, tokens, cost, latency, time, or quality improvement without an observed comparable baseline. Structural reduction is simplification evidence, never a productivity measurement. Do not build standing prompt-evaluation suites merely to defend wording.

For validation classify material obligations as `proved | defect | evidence gap | not applicable`. Return `VERIFIED` only when required proof passes against the exact candidate, `CHANGES_REQUIRED` for a proved defect, and `INSUFFICIENT_EVIDENCE` for a material proof gap. Validation does not authorize repair.

## 4. Integrate and report

With mutation authority, reconcile only affected metadata/manifests/routes, direct resource links, deterministic tests/CI, and release surfaces. Preserve unrelated work.

Report the exact candidate, owned outcome/control shape, material capability/resource or owner-boundary changes, proof/gaps, and relevant external state. Size reduction is evidence of simplification, never the acceptance target.
