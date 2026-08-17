# Portfolio audit

Produce one read-only, evidence-backed audit of a declared skill portfolio. Own inventory, cross-skill consistency, state drift, route overlap, missing capability ownership, and portfolio-level recommendations. Keep deep judgment and changes for one skill with Ko Skill's one-skill workflow.

## 1. Pin the portfolio

Record the requested outcome, time boundary, filesystem roots, repositories, package or plugin sources, active catalog, published surfaces, exclusions, and authority. Resolve each supplied path before counting it.

Define these states separately:

- **source**: the maintained skill candidate and its repository integration;
- **installed**: a physical copy available to an agent runtime;
- **active**: a skill exposed by the current runtime or enabled package;
- **published**: a version available from a confirmed distribution surface.

Do not infer active or published state from a cache, config entry, source checkout, or installed directory alone. When a state cannot be verified, record an evidence gap instead of parity.

Build a canonical inventory. Give every distinct skill one row with its canonical name, source and package identity, observed states, version or digest when available, and evidence location. Deduplicate symlinks, cache copies, aliases, resumed records, and identical package versions. Report the denominator and exclusions used by every portfolio count.

## 2. Check every inventory row

Run deterministic structural checks before semantic review. For each applicable skill, verify:

- required `SKILL.md` frontmatter and metadata;
- referenced files, scripts, templates, and resources resolve inside the skill contract;
- package, manifest, catalog, and router entries agree with the canonical name and user-reachable purpose;
- source, installed, active, and published identities or digests agree where parity is claimed;
- provider-capable skills retain their own authority, host trust, credential, pagination, readback, and untrusted-content rules;
- no description or route makes two skills primary owners of the same unqualified outcome without an explicit tie-break rule.

Classify every row as `no finding in declared checks`, `finding`, `evidence gap`, `excluded`, or `not applicable`. A successful parser or link check proves structure only; it does not prove behavioral quality.

Use risk-weighted semantic inspection for collisions, missing owners, stale references, state drift, security-sensitive behavior, and unusually broad or duplicated contracts. For a large portfolio, inspect all structural surfaces and sample semantic content by stated risk rules. Do not claim that unsampled skills are behaviorally sound.

## 3. Reconcile capabilities

Create one capability map from user outcomes to primary owners and explicit supporting relationships. Compare it with the active inventory and public catalog.

For each primary QP owner, inspect its declared workflow and sampled real use for complementary responsibilities supplied by another skill. Classify each relationship before recommending a change:

- **core requirement**: the primary skill cannot complete its own declared outcome correctly without the other skill's rules or result;
- **independent specialist**: the supporting result has its own authority, artifact, lifecycle, or acceptance boundary;
- **optional enrichment**: the supporting result can improve evidence or quality, but its absence does not prevent a correct primary outcome; or
- **duplicate ownership**: both skills claim the same unqualified outcome and completion boundary.

Require a QP-owned primary skill to contain the instructions needed for its core requirements. When an external skill supplies a missing core rule, recommend that the QP owner adopt the necessary vendor-neutral behavior; do not recommend changing, removing, or routing through the external skill. Preserve an independent specialist as an explicit handoff. Keep optional enrichment optional and require a safe fallback when its absence could otherwise block the workflow. Consolidate duplicate QP ownership only after current behavior and caller evidence show that one owner can replace the other without loss.

Test the ownership claim against a direct invocation of only the primary skill when behavioral evidence is justified and available. If the skill cannot complete its declared outcome, report the exact missing responsibility and evidence gap. Do not infer ownership from an installed path, name similarity, or one composed session.

Report a missing capability only when a material recurring outcome has no adequate owner. Require either two independent task records or another durable source that proves recurrence and value. State the records, eligible denominator when known, counterevidence, and why extension of an existing owner is insufficient.

Reject a proposed new skill when the need is one incident, a repository-specific rule, a small check for an existing owner, or an implementation detail. Return an accepted creation or correction to Ko Skill's one-skill workflow; this audit does not edit, install, remove, enable, publish, or synchronize skills.

For overlaps, preserve distinct owners when their authority, provider, lifecycle, artifact, or completion boundary differs. Recommend the smallest router or description correction that makes selection deterministic. Do not merge workflows only because their verbs are similar.

## 4. Verify findings and report

Verify every finding against the exact current file, package, catalog, runtime, or distribution state that supports it. Separate confirmed defects from optimization ideas. Deduplicate findings by owning mechanism and identify the smallest correction surface.

Rank recommendations by user impact, recurrence, safety, reachability, and correction cost. Give each one an owner and disposition: `do now`, `defer`, `needs evidence`, or `no action`. Preserve explicit user deferrals.

Return the evidence boundary; normalized inventory and denominators; structural results; source-installed-active-published drift matrix; route and capability map; confirmed findings; evidence gaps; rejected recommendations; prioritized actions; and limitations. State clearly that no finding means “no issue found within the declared checks,” not “all skills are optimal.”
