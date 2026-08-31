---
name: ko-skill
description: Author, revise, or validate one portable agent skill, or audit a bounded skill portfolio. Focus on one owned outcome, deep-module composition, the smallest adequate capability/resource placement, selectively loaded expert depth, and proportionate proof.
---

# Kọ Skill

Create, revise, or validate one exact skill. Mutation requires explicit authority; validation and portfolio audit are read-only. Never infer installation, activation, synchronization, publication, provider, or other external mutation authority from source changes. For a bounded portfolio audit, read [portfolio audit](references/portfolio-audit.md).

## 1. Own one outcome

Read the candidate package plus affected repository/host instructions and integration metadata. Pin the operation, exact candidate, desired outcome, triggers, exclusions, authority, adjacent owners, and relevant `source | installed | active | published` evidence.

Revise an existing owner instead of creating a competitor. A public skill earns its place when it owns a recurring independently useful outcome, authority/artifact/acceptance boundary, failure mode, or useful reusable model-steering contract. Do not remove a lightweight skill merely because the base model can perform the act when the named contract reliably saves users from restating material behavior.

Use the smallest control shape that preserves correctness:

- **lightweight** — consequential invariants can directly produce the result;
- **workflow** — correctness genuinely depends on ordered stages, durable/external state, stale/partial recovery, multiple actors/candidates, or distinct side-effect authorities.

Do not add lifecycle, statuses, receipts, schemas, or ceremony merely because the outcome is important.

### Admit deliberate behavior, not only minimal prose

A capable agent's default behavior is not automatically the desired behavior for a skill. Keep an instruction when it deliberately overrides a likely default tendency and the resulting cost materially improves this owner's outcome.

For each consequential instruction, establish:

- **default tendency** — what a capable agent would likely do without it;
- **failure prevented** — the material miss, ambiguity, context loss, unsafe effect, premature inference, weak proof, or other owner-specific failure that tendency creates;
- **override** — the exact different behavior the instruction forces;
- **value** — completeness, clarity, focus, human visibility, correctness, safety, authority, convergence, or another owned improvement;
- **cost** — user interruption, context, latency, delegation, artifact/persistence, review, proof, or ceremony;
- **trigger** — why the override is active for this branch; and
- **composition** — whether adjacent owner rules reinforce the result or accidentally create a harmful loop.

Do not optimize away deliberate friction merely because a base model could proceed with less of it. A relentless decision frontier, an independently safe provider contract, a human-facing projection, negative scope boundaries, adversarial review, or context-isolating delegation may be load-bearing when that behavior is part of the useful result. Conversely, a valuable mechanism with an over-broad trigger is still defective.

## 2. Compose and place capability

Treat skills as deep modules. A caller supplies only the bounded input, reason/freshness/authority and caller-owned acceptance needed by the callee. The callee retains its procedure, internal state, resources, verification, persistence/representation mechanics, and native result. Do not copy lifecycle/result schemas across owner boundaries; repeat only independently required safety, trust, authority, acceptance, or owner-specific steering rules.

Write for a capable agent. State semantic behavior, invariants, authority and completion; let the agent adapt ordinary search, shell/filesystem work, Git use, editing, tool discovery, and equivalent orchestration to its available environment. Do not pre-author capability fallback trees the agent can infer. Ordinary delegation is likewise agent-owned, but an owner may prescribe delegation/isolation when moving bounded independent or noisy work out of the primary context is itself necessary to preserve context quality, focus, continuity, or independent observation.

Concrete mechanics earn instruction space when the mechanism establishes correctness, authority, determinism, non-obvious safety, a machine/external protocol, or a compatibility boundary, or when a small operational anchor materially reduces recurring rediscovery of how to enter a **selected concrete capability**. After the tool, provider, protocol, runtime, or other concrete interface is selected, an anchor may point to authoritative current documentation or a canonical interface and include one representative invocation or discovery command. Do not use operational anchors to preselect or cache open-ended source, vendor, library, framework, host, inspiration, or candidate inventories; keep those as selection criteria and current discovery. Keep volatile details subject to revalidation instead of expanding an anchor into a command catalogue.

Before adding or retaining commands, references, scripts, templates, data, assets, or another public owner, read [capability and resource placement](references/resource-placement.md). Prefer the natural owner and the smallest adequate surface. Keep `SKILL.md` focused on the universally required contract and load branch-specific depth only where needed.

When material expert judgment belongs outside `SKILL.md`, use [reference quality](references/reference-quality.md). If executable code still appears necessary after placement, apply [script boundary](references/script-boundary.md). Use [knowledge catalogues](references/knowledge-catalogues.md) only when a maintained researched corpus is itself part of the useful outcome.

For multi-host portability, keep one canonical semantic contract in the skill/owning source. Host manifests, rules, hooks, or command adapters should be the thinnest projection needed by actual loader semantics; do not maintain divergent handwritten copies of the behavior. Mechanically verify projections when an adapter exists and semantic drift would be consequential. Do not add host adapters merely to claim compatibility that current installation/distribution already provides.

Name modes only when behavior or authority truly differs. Prefer current project/provider/framework/tool truth over cached command catalogues or starter defaults.

Reference another repository skill by its exact frontmatter `name` trigger in backticks, for example `alarina`. Do not use another skill's localized/display title as a cross-skill identifier. A skill may use its own display name inside its own package, headings, and prose. Within this repository, `skill`, `route`, `owner`, `specialist`, and similar terms already refer to the portfolio; do not add a redundant repository namespace prefix unless a real external namespace must be distinguished.

### Format for execution

Use Markdown to expose semantic structure, not to decorate prose:

- use **prose** for connected explanation, rationale, nuance, and invariants that must be understood together;
- use **bullets** for parallel inputs, requirements, constraints, checks, outputs, or independent obligations;
- use **numbered lists** only when execution order matters;
- use **tables** when finite states, modes, mappings, or comparison dimensions are easier to scan side by side;
- use **fenced blocks** for exact schemas, command shapes, state shapes, or output contracts; and
- split a paragraph when it hides several independently actionable obligations that the agent would otherwise need to reconstruct as a checklist.

Do not turn every sentence into a bullet or add headings that do not improve navigation. Dense prose is not simpler when the reader must recover a latent list before acting.

## 3. Prove the exact candidate

Use the smallest evidence that can falsify the changed contract. Structural/package validation is baseline; add realistic forward behavior only when selection, authority, safety, state, branching, composition, resource choice, or output remains materially uncertain. Re-run only proof invalidated by later changes.

For behavior corrections, use pinned pre-change evidence when it already proves the failure; otherwise exercise the smallest safe realistic baseline. For compression, script/catalogue/template removal, ownership moves, or skill consolidation, compare the same realistic goal before/after when material uncertainty remains. Prove both that removed material was not uniquely behavior-bearing and that the smaller placement preserves result quality, authority, proof, discoverability, and any useful operational anchor.

For a skill whose primary value is model steering rather than deterministic mechanics, use **steering-effect proof** only when material behavioral uncertainty remains: run the same realistic bounded task/candidate/context against the prior/no contract and the changed contract, verify the target judgment/behavior changes in the intended direction, and separately verify correctness/safety/required output did not regress. Keep this proof temporary and proportionate; persist a behavioral regression only when recurring stable risk justifies maintaining it.

Do not claim saved LOC, tokens, cost, latency, time, or quality improvement without an observed comparable baseline. The unbuilt counterfactual is not a measurement. Structural reduction is evidence of simplification, never proof of productivity savings.

Do not build standing prompt-evaluation suites merely to defend wording. Match proof to the actual control shape and consequence.

For validation classify material obligations as `proved | defect | evidence gap | not applicable`. Return `VERIFIED` only when required proof passes against the exact candidate, `CHANGES_REQUIRED` for a proved defect, and `INSUFFICIENT_EVIDENCE` for a material proof gap. Validation does not authorize repair.

## 4. Integrate and report

With mutation authority, reconcile only affected metadata/manifests/routes, direct resource links, deterministic tests/CI, and release surfaces. Preserve unrelated work.

Report the exact candidate, owned outcome/control shape, material capability/resource or owner-boundary changes, proof/gaps, and relevant external state. Size reduction is evidence of simplification, never the acceptance target.
