# Portfolio audit

Use only for a bounded read-only portfolio audit. Judge inventory, ownership, composition, state drift, structural health, and reference quality; do not edit, install, activate, synchronize, or publish skills.

## Pin the inventory

Record the declared roots/repositories, observation time, package/catalog surfaces, exclusions, and authority. Track each skill's `source`, `installed`, `active`, and `published` evidence independently and deduplicate aliases, caches, symlinks, and identical package copies.

Any source, package, manifest, catalog, installation, activation, or publication change makes dependent parity evidence stale.

## Check structural health

Run applicable deterministic checks across the declared inventory:

- frontmatter, metadata, references, scripts, templates, and resources;
- package, manifest, catalog, router, group, and canonical-name consistency;
- exact identity/digest for claimed state parity;
- provider-capable owners against the repository provider policy; and
- deterministic ownership or routing collisions.

Structural success proves only those structures, not behavioral quality.

## Audit ownership and composition

Classify each skill as `lightweight` or `workflow` using the Kọ Skill control-shape rule. Do not treat missing workflow machinery as a defect when a lightweight result is complete without it; do flag workflow machinery that has no consequence for correctness, authority, recovery, or completion.

Map each public outcome to one primary owner and necessary supporting results. Preserve a separate skill when it owns a distinct outcome, authority, artifact, lifecycle, acceptance boundary, or installation value.

For every supporting relationship, inspect both directions:

- **caller leakage** — the caller reproduces the callee's procedure, internal stages/statuses, checks, resources, scripts, verification, persistence/artifact mechanics, or native result schema instead of stating the result it needs;
- **callee leakage** — the callee reproduces a caller-specific plan/job/phase schema, receipt dialect, envelope, or orchestration lifecycle instead of returning one native result.

Do not flag caller-owned trigger/input, freshness, acceptance, authority, recovery, or stop conditions, nor independently required safety/trust rules. Routing skills may describe owners because routing is their result.

Treat `html-artifact` and `akosile` as deep-module checks: callers should normally supply semantic intent/content while those owners retain representation or workspace mechanics.

Check selector-facing descriptions separately. They should advertise the skill's owned outcome, trigger, and exclusions rather than implementation dependencies, except when choosing another owner is itself the skill's result.

## Audit reference quality and over-compression

Apply [reference quality](reference-quality.md) to material ordinary references and to skill-body rules whose non-obvious judgment may have been compressed too far.

Look for both excess and missing depth:

- **healthy deep reference** — coherent expert judgment, selective trigger, bounded owner-specific consequence;
- **over-compressed rule** — a short instruction leaves a recurring non-obvious distinction to be reconstructed or guessed;
- **missing calibration** — good/bad examples, counterexamples, or stable vocabulary would materially improve the same recurring judgment;
- **dump** — subject-taxonomy prose or examples whose applicability cannot be selected cheaply;
- **duplicate** — official docs, repository facts, another owner, or deterministic tooling already supplies the material more reliably;
- **wrong owner** — useful expertise exists but its decision consequence belongs elsewhere;
- **poor trigger** — a reference is useful but forces unrelated context on ordinary invocations;
- **freshness gap** — volatile guidance is preserved without a current evidence boundary.

Do not recommend `DEEPEN` because a skill or reference is short. Name the plausible decision error, recurrence or owner-wide consequence, and why a selectively loaded reference is the smallest prevention surface.

Do not recommend `REMOVE` because a reference is long. Name the duplication, irrelevance, stale evidence, wrong owner, or retrieval failure.

## Audit scripts and broad knowledge skills when present

For every bundled script, apply [bundled-script boundary](script-boundary.md) and return one disposition: `KEEP`, `SHRINK`, `REPLACE_WITH_NATIVE`, `REPLACE_WITH_LIBRARY`, `MOVE_TO_OWNER`, `REMOVE`, or `NEEDS_EVIDENCE`.

For broad researched catalogues or resolver companions, apply [researched knowledge catalogues](knowledge-catalogues.md). Verify progressive disclosure, evidence/freshness boundaries, bounded native output, and absence of unnecessary custom retrieval machinery.

## Report only evidenced findings

Verify every finding against exact-current files and observed states. Separate defects from optimizations and evidence gaps; deduplicate by mechanism and rank by user impact, recurrence, safety, reachability, and correction cost.

Recommend a new skill only from durable evidence of a recurring valuable outcome with no adequate owner. Recommend retirement only when evidence shows the route adds no independently useful outcome or completion boundary.

For material references return the applicable `KEEP | DEEPEN | SPLIT | MOVE | RESEARCH | REMOVE` disposition and its decision consequence.

Return the evidence boundary, inventory/state matrix, control-shape classification, structural results, ownership/route map, dependency-boundary findings, reference-depth findings, script dispositions, confirmed defects/optimizations, evidence gaps, rejected recommendations, prioritized actions, and limitations. “No finding” means no issue found within the declared checks, not that every skill is optimal.
