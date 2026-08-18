# Portfolio audit

Use only in Ko Skill `audit`. Produce one read-only, evidence-backed audit of a declared portfolio. Keep changes and deep single-skill judgment with `author` or `validate`.

## Pin the inventory

Record the outcome, observation time, roots, repositories, package sources, active catalog, published surfaces, exclusions, and authority. Resolve supplied paths before counting.

Track each state separately:

- `source`: maintained candidate and repository integration;
- `installed`: physical runtime copy;
- `active`: skill exposed by the current runtime or enabled package;
- `published`: version on a confirmed distribution surface.

Build one canonical inventory row per distinct skill: name, source/package identity, observed states, observation time, version or digest, and evidence. Deduplicate symlinks, caches, aliases, and identical package versions. State every count's denominator and exclusions. Any source, package, manifest, catalog, installation, activation, or publication change makes dependent parity evidence stale.

## Check the portfolio

Run deterministic structural checks across the declared inventory before semantic review:

- frontmatter, metadata, references, scripts, templates, and resources;
- package, manifest, catalog, router, and canonical-name consistency;
- exact identity or digest for every claimed state parity;
- each provider-capable owner's complete applicable repository safety contract; and
- deterministic ownership or route collisions.

Classify each row as `no finding in declared checks | finding | evidence gap | excluded | not applicable`. Structural success does not prove behavioral quality.

Inspect semantic content by stated risk: collisions, missing owners, stale references, state drift, security-sensitive behavior, and broad or duplicated contracts. For a large portfolio, check all structural surfaces and disclose semantic sampling; never claim unsampled skills are behaviorally sound.

## Map ownership

Map user outcomes to primary owners and explicit supporting relationships. Classify each relationship:

- `core`: the primary cannot complete its outcome without the behavior;
- `specialist`: separate authority, artifact, lifecycle, or acceptance boundary;
- `optional`: useful enrichment with a safe fallback; or
- `duplicate`: the same unqualified outcome and completion boundary.

Keep vendor-neutral core behavior in the primary owner. Preserve specialists as handoffs and optional work as optional. Consolidate duplicates only when current behavior and caller evidence prove replacement without loss. Use direct invocation of the primary when material uncertainty justifies behavioral proof.

Report a missing skill only from durable evidence of a recurring valuable outcome with no adequate owner. Reject one incident, repository policy, a small check, or an implementation detail; prefer extending the existing owner. Preserve overlaps when authority, provider, lifecycle, artifact, or completion differs, and prefer the smallest routing correction.

## Verify and report

Verify every finding against exact-current files and observed states. Separate defects from optimizations, deduplicate by mechanism, and rank by user impact, recurrence, safety, reachability, and correction cost. Assign an owner and `do now | defer | needs evidence | no action`; preserve accepted deferrals.

Return the evidence boundary, normalized inventory and denominators, structural results, state-drift matrix, capability/route map, confirmed findings, evidence gaps, rejected recommendations, prioritized actions, and limitations. “No finding” means no issue found within declared checks, not that every skill is optimal.
