# Portfolio audit

Use only for a bounded read-only portfolio audit. Reapply Kọ Skill's normal authoring model to existing packages; do not edit, install, activate, synchronize, or publish skills.

## Pin the inventory

Record declared roots/repositories, observation time, package/router surfaces, exclusions, and authority. Track `source`, `installed`, `active`, and `published` evidence independently. Any source/package/manifest/router/installation/publication change stales dependent parity evidence.

## Structural health

Run applicable deterministic checks across the inventory:

- frontmatter, metadata, nested Markdown/resource links, scripts, templates, data and assets;
- package/manifest/router/group/canonical-name consistency;
- exact identity/digest for claimed state parity;
- provider-capable owners against repository provider policy; and
- deterministic ownership/routing collisions.

Structural success proves only those structures, not behavioral quality.

## Outcome ownership and public surface

Classify each skill `lightweight | workflow`. Map each recurring public outcome to one primary owner and only necessary support results. Preserve a public skill when it has a distinct independently useful outcome, authority, artifact, lifecycle, acceptance boundary, installability value, or useful reusable model-steering contract.

Do not retire a lightweight skill merely because the base model can perform the act. Test whether the skill reliably invokes a useful behavior users would otherwise need to restate at length; `salaye` is a valid steering-style counterexample.

Flag public splits driven mostly by taxonomy/output type when one owner could express variants with a cleaner trigger. Any merge/removal requires before/after realistic prompt proof with selection/result/authority/proof preserved.

Inspect both composition directions:

- caller leakage — caller reproduces callee procedure/stages/checks/resources/scripts/result schema;
- callee leakage — callee reproduces a caller-specific plan/job/receipt lifecycle.

Keep independently required safety/trust/authority rules even when they repeat across separately installed provider owners.

## References and knowledge shape

Apply [reference quality](reference-quality.md). Look for healthy deep references, over-compressed recurring judgment, missing calibration, dumps/catalogues, duplicates, wrong owner, poor trigger, and freshness gaps.

Do not remove long references merely for size. Do remove or reshape framework/tool manuals, volatile inventories, generic style taxonomies, or CSV/Markdown duplicate representations that current project/tool/primary-source truth supplies better.

For genuine researched catalogues, apply [knowledge catalogues](knowledge-catalogues.md).

## Capability/resource placement

Apply [capability and resource placement](resource-placement.md) to each operational skill, not only those with scripts.

### Skill-runtime executables

For every executable that carries skill/runtime capability, apply [script boundary](script-boundary.md) and return:

`KEEP | SHRINK | REPLACE_WITH_GUIDANCE | REPLACE_WITH_NATIVE | REPLACE_WITH_LIBRARY | MOVE_TO_OWNER | PROMOTE_TO_ENGINE | REMOVE | NEEDS_EVIDENCE`.

For retained scripts, run the mandatory compression pass and name the exact remaining kernel.

### Human-facing convenience entrypoints

Audit public install/bootstrap/uninstall/helper wrappers separately from internal skill runtimes. Do not remove one merely because its mechanics could be written as several shell commands. Ask whether one stable safe invocation materially improves recurring user ergonomics while delegating the underlying operation to native tooling.

Return `KEEP ENTRYPOINT | SHRINK ENTRYPOINT | REPLACE_WITH_COMMAND | REMOVE | NEEDS_EVIDENCE`, and verify safe scope/defaults, portability, transparent native delegation, and absence of hidden semantic state. `scripts/uninstall.sh` is the canonical counterexample to over-aggressive command replacement.

### Scriptless command affordances

Identify repeated evidence/provider/tool mechanics a capable agent has to rediscover each run. Add a bounded command palette only when it materially clarifies an evidence/authority boundary or removes repeated operational ambiguity. Do not create command catalogues.

### Templates

Return `KEEP | SHRINK | MOVE_TO_REFERENCE | REPLACE_WITH_NATIVE | REMOVE | NEEDS_EVIDENCE`.

Flag default-heavy starters, duplicate templates for one artifact, implementation boilerplate, workflow procedure, volatile commands, and optional empty sections. Keep neutral semantic scaffolds only when stable shape prevents material omission/drift.

### Data/catalogues

Verify bundled data is itself part of the useful knowledge outcome. Flag volatile ecosystem caches, style/industry/font/component inventories, and duplicate searchable representations whose semantic value already exists in references or current primary sources.

### Reusable assets

Separate universal resilience from branch-specific behavior. Flag theme toggles, carousels, print controls, or similar assets made mandatory when most outputs do not use their behavior.

### Support infrastructure

Challenge eagerly created empty files/directories/default state. Prefer lazy creation when absence already represents the empty state and no consumer requires a seeded file.

## Drift and deterministic maintenance

Search nested references/resources for deleted scripts/templates/assets and obsolete command names. Reconcile deterministic CI/tests only to retained runtime kernels. Separate current runtime guidance from historical/superseded research so retrieval cannot mistake old conclusions for active contracts.

## Healthy duplication

Do not optimize repetition that is independently load-bearing, for example:

- provider host trust, credential isolation, pagination, pre-write refresh and readback in separately installed provider owners;
- distinct durable knowledge destinations with different semantic consequences;
- deep expert references whose judgment is not duplicated elsewhere;
- explicit experimental isolation from stable ownership;
- a thin public convenience entrypoint whose value is one safe memorable invocation over native tools.

## Report

Verify every finding against exact-current files and states. Separate defects, optimizations, evidence gaps, and proof-gated consolidation candidates. Deduplicate by mechanism and rank by user impact, recurrence, safety, reachability, stale-risk, and correction cost.

Return:

- evidence boundary and inventory/state matrix;
- control-shape and ownership/route map;
- structural/resource-drift results;
- reference/depth/catalogue findings;
- skill-runtime script, public-entrypoint, and command-affordance dispositions;
- template/data/asset/support-infrastructure findings;
- public-owner consolidation candidates and required proof;
- healthy repetition explicitly retained;
- prioritized actions, rejected recommendations, gaps, and limitations.

“No finding” means no issue found within declared checks, not that every skill is optimal.
