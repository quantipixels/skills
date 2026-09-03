# QP Agent Skills

Portable focused skills for demanding work across reasoning, planning, research, design, engineering, and delivery. QP aims for one independently useful outcome per public skill, deep references where judgment benefits, native capabilities for ordinary mechanics, and bundled code only for narrow deterministic kernels.

Browse the [documentation](https://quantipixels.com/skills).

## Portfolio principles

- Grow capability depth faster than public surface area. Deepen an existing owner when it can carry a capability coherently; add another public skill only when its independent identity materially simplifies direct selection or use.
- Frame each owner at the natural level of the outcome it owns: initiative, decision, candidate, project knowledge, artifact, implementation, software system, repository, runtime, or another exact subject. Do not let historical software/repository examples or persistence mechanics narrow a broadly useful outcome, and do not generalize a domain-specific owner beyond its real capability.
- Curate frameworks into reasoning. Preserve a named model, standard, or concept when its vocabulary, conceptual structure, authority, or retrieval value materially improves judgment; expose only the QP-relevant subset and do not import the whole framework as ceremony.
- Constrain material decision surfaces, not ordinary mechanics. A consequential choice that can change accepted behavior, safety, compatibility, ownership/lifecycle, architecture, authority, or material risk/cost must be grounded in current evidence/contract, explicitly owned, or surfaced as unresolved.
- Kọ Skill authors every capability/resource at the smallest adequate surface: guidance/reference → visible command → native/project/provider tool → focused library → deterministic script → engine only when it carries a substantial owned vertical.
- Use an obvious outcome owner directly. Use a router only when ownership is genuinely unclear or several independently useful owners need sequencing.
- Supporting composition belongs behind the active owner unless another owner's independently useful result or separate authority must become visible.
- Akọsílẹ̀ owns repository-scoped `.qp` mechanics when that persistence surface is selected; broadly useful owners must not require a repository merely because `.qp` is one available durable destination.
- HTML Artifact creates reader-specific projections of supplied material without duplicating source archives or originating conclusions.
- Generated `.qp` state stays outside Git by default.
- Small public skills may intentionally exist as reusable model-steering contracts when a narrow named behavior saves users from restating longer instructions and the public identity itself improves selection/use.
- Thin public convenience entrypoints may wrap native commands when one safe memorable invocation materially improves installation, removal, or other human-facing distribution UX.
- Experimental skills are first-party runtime candidates under their normal trigger, intent, authority, cost, safety, and host invocation gates. Experimental marks evidence/promotion maturity rather than adding a category-wide acceptance tax; experiments do not become unconditional prerequisites or redefine stable owners before promotion.

## Install

```bash
npx skills add quantipixels/skills --global
```

Local checkout:

```bash
npx skills add .
```

Claude Code:

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

Optional QP main agent after plugin installation:

```bash
claude --agent qp-skills:qp
```

The QP agent is a thin host adapter over `alarina`; direct skill invocation and skill-only hosts remain first-class.

## Uninstall

```bash
curl -fsSL https://raw.githubusercontent.com/quantipixels/skills/ori/scripts/uninstall.sh | bash
```

The entrypoint removes only globally installed skills whose lock-file source is `quantipixels/skills`; unrelated installed skills remain untouched.

## Repository-local workspace

```text
.qp/
├── settings.json                         optional
├── INDEX.md                              optional generated navigation
├── records/<owner>/<stable-subject>/     created on first record
└── artifacts/<stable-subject>/           created on first standalone artifact
```

The real `.qp` belongs to the non-bare main worktree. Linked worktrees expose `.qp` as a symlink to it. Existing dated record/artifact directories remain valid legacy identities.

The catalogue headings below mirror repository package organization, not semantic domain boundaries. Select by each skill's owned outcome/trigger: broadly useful planning, review, knowledge, specification, and delivery-decomposition owners may live under `engineering` without requiring a software task.

## Engineering

| Skill | Outcome |
| --- | --- |
| `akosile` | Repository-scoped `.qp` paths/worktrees, sparse settings, exact safe publication, generated index |
| `alaga` | Deliver one supplied software/build job through implementation, proof, review, and handoff |
| `amose` | Exact-current project/domain model and durable working knowledge across the project's natural sources of truth |
| `atona` | One initiative plan from Draft through delivery/closure |
| `atunwo` | Code defect/proof/state-parity review and provider review publication when authorized |
| `hitl-review` | Human-led walkthrough, review coverage, specialist discovery, final human decision |
| `irinse` | Select/ready/use/upgrade/remove one companion engineering tool and return bounded evidence |
| `ko-skill` | Author/revise/validate one skill or audit a bounded portfolio |
| `pare` | Read-only software-system simplification audit/review |
| `scope-guard` | Prevent coding scope drift and enforce the minimum sufficient mechanism/proof |
| `se-triage` | Supplied-evidence-first engineering issue/report assessment |
| `seda-pr` | Scoped commit/push and PR/MR creation/update |
| `seda-spec` | Confirmed implementation-independent behavior/operating specification |
| `seda-ticket` | Outcome-complete delivery tickets with dependencies, acceptance, and startable frontier |
| `seda-sigidi` | Draft or explicitly integrate one agent's durable identity/values/boundaries/voice into a known host configuration |
| `solution-architect` | Implementation-ready software-system architecture design/read-only review |
| `wo-pr` | Steward an open PR/MR through CI/conflict/feedback readiness |

## Design

Use the exact design specialist directly when one deliverable owner is clear. Use `apere` when design-specific multi-owner routing, prerequisites, dependency order, shared constraints, or approval boundaries are themselves needed.

| Skill | Outcome |
| --- | --- |
| `apere` | Route broad/multi-deliverable design work without becoming its delivery owner |
| `amoye-ui-ux` | UI/UX direction, proportionate design exploration, explicit affordance acceptance, and rendered convergence |
| `brand` | Durable brand voice/identity/logo/icon/assets source of truth |
| `social-graphics` | Feed/carousel/story/social campaign graphics |
| `eto-apere` | Project-specific token/component-spec contract and CSS realization |
| `asa-oju-ibanisoro` | Accessible responsive React/web UI implementation with native proof and rendered convergence |
| `banner-design` | Covers/headers/heroes/display ads/print banners |
| `slides` | Explanatory, instructional, status, review, strategic, or persuasive presentation design |

Banner Design and Social Graphics intentionally remain narrow steering owners even though they share graphic-design fundamentals: the separate selectors encode different surface/adaptation behavior without requiring users to restate it.

## Productivity

| Skill | Outcome |
| --- | --- |
| `alarina` | Route only when the correct owner is unclear or several independent owner results need sequencing |
| `arojinle` | Resolve consequential choices through a user-confirmed decision frontier |
| `ayewo-igba-ise` | Evidence-backed postmortem for completed/abandoned/disputed work, incidents, sessions, or corpora |
| `handoff` | Compact host-neutral fresh-session handoff packet |
| `html-artifact` | Selective traceable accessible HTML visualization of supplied material |
| `iwadi` | High-trust claim-appropriate research with high-threshold exact-version technical source escalation |
| `ro-wo` | Test one material premise before judgment |
| `salaye` | Reusable plain-language explanation behavior for a supplied subject |
| `system-cleanup` | Safe macOS storage audit, regenerable cleanup, worktree review, and external-drive offload |
| `technical-writing` | Technical communication structure/clarity from direct reader/job/syntax principles |
| `yo-slop` | Final prose cleanup / explicit pruning without contract change |

`salaye` is intentionally lightweight: its value is reliable reusable model steering, not hidden machinery.

## Experimental

Experimental skills participate in normal first-party routing when their owned outcome fits and host invocation metadata permits it. A skill may deliberately require direct user activation when its boundary is an intent island; this is a skill-specific gate, not category-wide isolation. Experiments exist to prove their utility and limits in real work, then be promoted, kept experimental, narrowed/folded, replaced, or removed. Do not invoke one merely to collect experiment data, and do not treat low raw invocation count as failure when the owned outcome is genuinely rare.

| Skill | Outcome |
| --- | --- |
| `dogfood` | Real-browser verification of changed user journeys |
| `fihan` | Explicitly activated private serving of one bounded local resource |
| `ideate` | Grounded mechanism-diverse possibilities before selection |
| `pepeye` | User-requested task supervision across QP or ordinary host/domain owners without a second lifecycle |
| `prototype` | Disposable truthful decision instrument |
| `root-cause` | Minimal evidence-backed causal mechanism/set for an observed failure |

Historical Akọ̀wé and Orísun experiments remain research evidence. Their useful methods now live behind Alága's implementation-counsel path and Ìwádìí's exact-source escalation instead of occupying public routing surface.

## Start

Use the obvious owner directly when the requested outcome is clear:

```text
Implement or fix code → alaga
Plan a material initiative → atona
Review a code candidate → atunwo
Resolve consequential choices → arojinle
Research a material claim → iwadi
Diagnose an observed failure → root-cause
```

Use `alarina` only when the correct owner is unclear or the request genuinely needs sequencing across several independently useful owner results.
