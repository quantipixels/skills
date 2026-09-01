# Portfolio audit

Use only for a bounded read-only portfolio audit. Reapply Kọ Skill's normal authoring model to existing packages; do not edit, install, activate, synchronize, or publish skills.

## Pin the inventory

Record repository/root scope, package/router surfaces, exclusions, observation time, and authority. Track `source | installed | active | published` independently when relevant; changes to any observed surface stale dependent parity evidence.

## Structural and ownership health

Run applicable deterministic package/link/manifest/name checks. Structural success proves structure only, not behavioral quality.

Map recurring public outcomes to primary owners and necessary supporting results. Flag competing owners, caller copies of callee procedure/result schema, callee copies of caller lifecycle, and public splits driven mainly by taxonomy. Preserve independently required safety/trust/authority rules and useful named model-steering contracts.

Separate **capability value** from **public identity value** for every public owner. Flag a public name when its useful behavior could live behind a dominant existing owner without losing material independent selection, direct invocation, authority, result/artifact identity, acceptance, or reuse. Do not collapse an owner merely because another owner commonly calls it; the question is whether the separate public identity itself improves the interface for a user or genuinely independent caller.

Flag cross-skill references that use another skill's display/localized title instead of its exact frontmatter `name` trigger, omit backticks around that trigger, or add a redundant repository namespace prefix to ordinary skill/route/owner/specialist vocabulary. A skill may use its own display name inside its own package.

Classify control shape only when it helps expose unnecessary workflow ceremony. Importance alone does not justify lifecycle machinery.

## Behavioral instruction audit

Audit behavior before line count. For each consequential instruction or recurring cross-skill path, establish:

1. the capable-agent default tendency without the instruction;
2. the material owner-specific failure that tendency can create;
3. the deliberate override the instruction forces;
4. the value it buys: completeness, clarity, focus, human visibility, correctness, safety, authority, convergence, or another owned improvement;
5. the cost it imposes: interruption, context, latency, delegation, artifact/persistence, review, proof, or ceremony;
6. whether the trigger activates only where that failure mode matters; and
7. whether composition with adjacent owners produces useful defense-in-depth or an accidental loop.

Use these dispositions when they sharpen the finding:

- `ESSENTIAL_OVERRIDE` — default model behavior is materially wrong for this outcome;
- `HIGH_VALUE_CALIBRATION` — the model could do the act, but the instruction reliably improves the result;
- `SAFETY_AUTHORITY_INVARIANT` — independent invocation must preserve the rule;
- `CONTEXT_ISOLATION` — delegation, persistence, or representation deliberately protects reasoning/human context;
- `OPERATIONAL_ANCHOR` — a small concrete pointer prevents repeated rediscovery of a selected capability;
- `RECOVERABLE_DEFAULT` — a capable agent already performs it well enough without instruction;
- `WRONG_OWNER` — useful behavior, incorrect placement;
- `MIS_TRIGGERED` — valuable behavior activated too broadly/narrowly; or
- `HARMFUL` — the instruction predictably pushes the result in the wrong direction.

Do not classify deliberate friction as bloat merely because it is expensive. Relentless interviews, human-facing visual projections, negative scope boundaries, context-isolating delegation, independent provider safety rules, adversarial review, or reviewer-claim validation may be the mechanism that makes an owner useful. Challenge whether their trigger/cost still serves the outcome instead of optimizing them away by default.

Simulate representative end-to-end paths, not only isolated skills. Identify every owner invocation, user interruption, subagent/context boundary, persistent artifact, review, proof/test action, and external effect. Flag a cascade only when one of those steps does not independently protect the requested result or when repeated correction cannot converge without unauthorized scope expansion.

## Experimental portfolio judgment

Kọ Skill does not discover historical skill usage from repository structure, router metadata, or current package state. When an Experimental skill is being evaluated for portfolio disposition, consume verified real-use evidence supplied by the user, `ayewo-igba-ise` corpus analysis, Skill Doctor, or another source whose population, availability, and evidence boundary are explicit.

Use that evidence together with the current package and portfolio to judge:

- whether the owned capability remains useful and distinct;
- whether trigger, authority, cost, and adjacent-owner boundaries are healthy;
- whether the separate public identity materially improves selection, direct invocation, authority, result identity, or reuse;
- whether folding the useful behavior behind a dominant owner would preserve the benefit while reducing public/routing complexity; and
- when real-use evidence is sufficient, whether observed value and cost justify changing maturity or shape.

Capability value is not public-skill value. A method may prove useful while its separate name fails to earn stable public surface.

A useful evidence packet may include eligible-opportunity denominator, selected/missed/mis-triggered/unavailable cases, observed incremental value and cost, boundary-health observations, counterevidence, and coverage limits. Treat missing historical evidence as an evidence gap; do not infer invocation frequency, missed opportunities, recurrence, or incremental value from source structure.

Use one disposition when the available structural and real-use evidence supports it:

- `PROMOTE` — representative real-use evidence shows distinct recurring capability value **and** independent public-identity value, with healthy boundaries and justified cost;
- `KEEP_EXPERIMENTING` — the capability/public-identity hypothesis remains credible but real-use evidence is insufficient or sparse;
- `NARROW` — useful behavior is proved but trigger/scope is broader than justified;
- `FOLD` — useful behavior is proved but belongs behind another owner rather than as an independent public skill;
- `REPLACE` — the capability hypothesis remains useful but this public shape is not the best vehicle; or
- `REMOVE` — structural evidence proves the public owner is invalid/redundant, or real-use evidence proves no independent value, harmful/mis-triggered behavior, or unjustified recurring cost.

`PROMOTE` cannot be justified from structure alone or from capability usefulness alone. Likewise, do not remove a structurally credible experiment merely because usage evidence is absent or invocation count is low. Structural defects may still justify `NARROW`, `FOLD`, `REPLACE`, or `REMOVE` without historical usage when the defect itself is proved from current ownership/behavior boundaries.

Never invoke an experiment merely to manufacture graduation evidence. One success never authorizes stable-owner removal/narrowing by itself.

## Capability and knowledge placement

Apply [capability and resource placement](resource-placement.md) to material commands, references, scripts, templates, data, assets, libraries, and public owners.

In particular, challenge instructions that teach a capable agent ordinary search, Git, shell/filesystem, editing, tool discovery, generic delegation, or host-capability fallback choreography. Preserve delegation when isolation of bounded independent/noisy work materially protects the owner's context, focus, continuity, or independent observation. Preserve a small operational anchor when it materially reduces recurring rediscovery of a **selected concrete capability**; do not mistake removal of every usable pointer for simplification. Also flag the opposite overreach: candidate/vendor/source/library/framework/host lists presented as anchors even though the skill is actually meant to discover or choose among them. An anchor should remain smaller than a manual and leave volatile flags, versions, limits, and inventories to current authoritative evidence.

Apply [reference quality](reference-quality.md) to substantial expert references. Preserve recurring non-obvious judgment even when the model could reconstruct some of it; remove generic advice, stale framework/tool manuals, volatile inventories, duplicated representations, and wrong-owner material.

Apply [script boundary](script-boundary.md) only to executable capability that survives placement. Audit public convenience entrypoints separately from internal runtimes. Use [knowledge catalogues](knowledge-catalogues.md) only for genuine researched corpora.

Challenge templates/default state/support assets that exist for convenience rather than a stable recurring contract. Existing project/native scaffolds outrank bundled starters; optional behavior should remain conditional unless the representation itself is part of the owner contract; absence should represent empty state when no consumer requires seeded resources.

## Presentation shape

Audit whether Markdown exposes the structure the skill already expects the agent to execute:

- keep connected rationale, nuance, and invariants as prose;
- use bullets for parallel inputs, requirements, constraints, checks, outputs, or independent obligations;
- use numbered lists only where order is behavior-bearing;
- use tables for finite states, modes, mappings, or comparisons when side-by-side scanning improves clarity;
- use fenced blocks for exact command, schema, state, or result shapes; and
- flag dense paragraphs that force the reader to reconstruct a hidden checklist before acting.

Do not reward list count, short paragraphs, or extra headings by themselves. Reformat only when the information shape becomes clearer without changing authority, sequencing, conditions, or meaning.

## Drift and proof

Search for stale links to removed resources, obsolete commands/names, duplicate active guidance, and historical research presented as current contract. Keep deterministic CI/tests only for retained deterministic seams and package integrity.

For proposed compression/consolidation, require before/after realistic proof only where material uncertainty remains. For model-steering changes, use temporary steering-effect comparison when the behavioral delta is uncertain rather than assuming fewer instructions are better. Size reduction is not acceptance; preserve selection, result quality, authority, proof, discoverability, useful operational anchors, deliberate context/representation controls, behavior-bearing expertise, and justified public identity.

## Report

Verify findings against exact-current files/state. Separate defects, optimizations, evidence gaps, healthy repetition, deliberate friction retained, and proof-gated consolidation candidates. Deduplicate by mechanism and rank by user impact, recurrence, safety, stale-risk, and correction cost.

For an Experimental portfolio judgment, identify the verified evidence packet consumed, any missing real-use evidence, capability-value assessment, public-identity assessment, structural/boundary assessment, and the resulting disposition only to the extent the evidence supports it.

Return inventory/state boundary, ownership/control findings, behavioral instruction dispositions, structural/resource drift, capability/reference/script/template/data/asset dispositions, presentation-shape findings, composition-path findings, consolidation candidates with proof needs, healthy repetition/deliberate friction retained, prioritized actions, rejected recommendations, and limitations.

“No finding” means no issue found within the declared checks, not that every skill is optimal.
