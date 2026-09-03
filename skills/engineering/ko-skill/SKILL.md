---
name: ko-skill
description: Author, revise, or validate one portable agent skill, or audit a bounded skill portfolio. Focus on one owned outcome, deep-module composition, the smallest adequate capability/resource placement, selectively loaded expert depth, and proportionate proof.
---

# Kọ Skill

Create, revise, or validate one exact skill. Mutation requires explicit authority; validation and portfolio audit are read-only. Never infer installation, activation, synchronization, publication, provider, or other external mutation authority from source changes. For a bounded portfolio audit, read [portfolio audit](references/portfolio-audit.md).

## 1. Own one outcome

Read the candidate package plus affected repository/host instructions and integration metadata. Pin the operation, exact candidate, desired outcome, triggers, exclusions, authority, adjacent owners, and relevant `source | installed | active | published` evidence.

Grow capability depth faster than public surface area. A public skill must own an independently useful result, authority/artifact/acceptance boundary, failure mode, or reusable steering contract **and** make direct selection/use materially simpler than keeping the capability behind an existing owner. Do not remove a useful lightweight steering contract merely because a capable model can perform the underlying act.

Frame the owner at the natural level of its outcome. Do not narrow a broadly useful result to a historical repository/software/tool context, and do not broaden a domain-specific owner beyond the evidence, authority, or capability needed to produce its result. Generalize the mechanism, never the authority.

Protect the **material decision surface**. Compression, folding, or generalization must not turn a previously owned constraint, evidence requirement, authority boundary, or consequential choice into unlabeled model inference. A material choice that can change accepted behavior, safety, compatibility, ownership/lifecycle, architecture, authority, or consequential risk/cost must be determined by current evidence/contract, explicitly owned, or surfaced as unresolved. Leave ordinary implementation and tool mechanics to the capable agent.

Curate frameworks **into** reasoning. Preserve a named model, standard, or concept when its vocabulary, conceptual structure, authority, or retrieval value materially improves this owner's judgment. State the QP-relevant subset and boundary directly; the name does not import the whole framework. Remove framework names that add only prestige, ceremony, generic templates, or stale implementation knowledge.

Use the smallest control shape that preserves correctness:

- **lightweight** — consequential invariants can directly produce the result;
- **workflow** — correctness genuinely depends on ordered stages, durable/external state, stale/partial recovery, multiple actors/candidates, or distinct side-effect authorities.

Do not add lifecycle, statuses, receipts, schemas, or ceremony merely because the outcome is important.

### Admit only behavior-bearing instruction

A capable agent's default behavior is not automatically the desired behavior. Keep a consequential instruction only when its trigger, failure prevented, forced behavioral difference, value, and recurring cost justify occupying default context.

Prefer replacing or sharpening existing guidance over appending another rule. Before adding a paragraph, reference, or public owner, try one precise invariant, one discriminating question, or one strong `Good / Bad` boundary. Use a selective reference only when branch-specific non-obvious judgment would otherwise burden the hot path.

## 2. Compose and place capability

Treat skills as deep modules. Pass only the bounded input, current evidence/identity, authority, and caller-owned acceptance another owner needs. The callee retains its native procedure, resources, proof, persistence/representation mechanics, and result. Supporting owners and references must not originate or redefine the consumer/parent's normative expectations, lifecycle, freshness, priorities, verdicts, acceptance, or authority.

Do not project semantic units one-to-one onto operational containers unless the destination contract requires it. Requirements, tickets, phases, proof obligations, and capability boundaries describe meaning; commits, candidates, branches, PRs/MRs, test files, browser runs, and agent sessions are chosen for their own integration, review, rollback, ownership, release, or evidence value.

Write for a capable agent. State semantic behavior, invariants, authority, and completion. Leave ordinary search, shell/filesystem work, Git use, editing, tool discovery, and host-specific delegation mechanics adaptable. Prescribe isolation only when bounded independent/noisy work must leave the primary context to protect focus, continuity, or independent observation.

Before adding or retaining commands, references, scripts, templates, data, assets, libraries, or another public owner, read [capability and resource placement](references/resource-placement.md). Use [reference quality](references/reference-quality.md) for substantial expert depth, [script boundary](references/script-boundary.md) when executable code still appears necessary, and [knowledge catalogues](references/knowledge-catalogues.md) only when maintained researched knowledge is itself part of the useful outcome.

Keep one canonical semantic contract across hosts. Host manifests, rules, hooks, or command adapters should be the thinnest projection required by actual loader semantics and mechanically checked when drift would be consequential. Name modes only when behavior or authority truly differs. Cross-skill references use the exact frontmatter `name` trigger in backticks.

For human-facing artifacts, match proof to the owned result: representation/document structure does not earn browser/UI assurance unless rendered experience is itself material to acceptance.

## 3. Prove the exact candidate

Use the smallest evidence that can falsify the changed contract. Structural/package validation is baseline; add realistic forward behavior only when selection, authority, safety, state, branching, composition, resource choice, or output remains materially uncertain. Re-run only proof invalidated by later changes.

For compression, consolidation, framework/reference removal, ownership moves, or domain generalization, compare the same realistic bounded goal before/after when material uncertainty remains. Prove that removed material was not uniquely behavior-bearing **and** that the new shape does not enlarge the material decision surface or lose useful conceptual/retrieval anchors.

For model-steering changes with material uncertainty, compare the same bounded task/candidate/context under the prior/no contract and changed contract. Verify the intended behavioral delta plus preserved correctness, safety, authority, and output. Keep temporary steering proof temporary unless recurring stable risk earns regression coverage.

Do not claim saved LOC, tokens, cost, latency, time, or quality without an observed comparable baseline. Structural reduction is simplification evidence, never the acceptance target.

For validation classify material obligations as `proved | defect | evidence gap | not applicable`. Return `VERIFIED` only when required proof passes against the exact candidate, `CHANGES_REQUIRED` for a proved defect, and `INSUFFICIENT_EVIDENCE` for a material proof gap. Validation does not authorize repair.

## 4. Integrate and report

With mutation authority, reconcile only affected metadata/manifests/routes, direct resource links, deterministic tests/CI, and release surfaces. Preserve unrelated work.

Report the exact candidate, owned outcome/control shape, material owner/capability/resource changes, decision-surface effects, proof/gaps, and relevant external state.
