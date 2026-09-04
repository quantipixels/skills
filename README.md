# QP Agent Skills

Portable focused skills for demanding work across reasoning, planning, research, design, engineering, and delivery. QP aims for one independently useful outcome per public skill, deep references where judgment benefits, native capabilities for ordinary mechanics, and bundled code only for narrow deterministic kernels.

Browse the [documentation](https://quantipixels.com/skills). See [compatibility claims](docs/compatibility.md) for the exact host/install paths QP currently proves rather than relying on a blanket portability claim.

## Portfolio principles

- Grow capability depth faster than public surface area. Deepen an existing owner when it can carry a capability coherently; add another public skill only when its independent identity materially simplifies direct selection or use.
- Frame each owner at the natural level of the outcome it owns: initiative, decision, candidate, project knowledge, artifact, implementation, software system, repository, runtime, or another exact subject. Do not let historical software/repository examples or persistence mechanics narrow a broadly useful outcome, and do not generalize a domain-specific owner beyond its real capability.
- Curate frameworks into reasoning. Preserve a named model, standard, or concept when its vocabulary, conceptual structure, authority, or retrieval value materially improves judgment; expose only the QP-relevant subset and do not import the whole framework as ceremony.
- Constrain material decision surfaces, not ordinary mechanics. A consequential choice that can change accepted behavior, safety, compatibility, ownership/lifecycle, architecture, authority, or material risk/cost must be grounded in current evidence/contract, explicitly owned, or surfaced as unresolved.
- Kọ Skill authors every capability/resource at the smallest adequate surface: guidance/reference → visible command → native/project/provider tool → focused library → deterministic script → engine only when it carries a substantial owned vertical.
- Use an obvious outcome owner directly. Use a router only when ownership is genuinely unclear or several independently useful owners need sequencing.
- Supporting composition belongs behind the active owner unless another owner's independently useful result or separate authority must become visible.
- Akọsílẹ̀ owns repository-scoped workspace mechanics when that persistence surface is selected; broadly useful owners must not require a repository merely because the workspace is one available durable destination.
- HTML Artifact creates reader-specific projections of supplied material without duplicating source archives or originating conclusions.
- Generated workspace state stays outside Git by default.
- Small public skills may intentionally exist as reusable model-steering contracts when a narrow named behavior saves users from restating longer instructions and the public identity itself improves selection/use.
- Thin public convenience entrypoints may wrap native commands when one safe memorable invocation materially improves installation, removal, or other human-facing distribution UX.
- Experimental skills are first-party runtime candidates under their normal trigger, intent, authority, cost, safety, and host invocation gates. Experimental marks evidence/promotion maturity rather than adding a category-wide acceptance tax; experiments do not become unconditional prerequisites or redefine stable owners before promotion.

## Install

```bash
npx skills add quantipixels/skills --global
```

This is the portable Skills CLI entrypoint; the exact destination/loading behavior is owned by the current CLI and selected agent. QP release CI currently proves repository discovery and Codex project installation, while other host paths remain bounded by the [compatibility matrix](docs/compatibility.md).

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

Canonical repository state lives under Git's shared common directory:

```text
<git-common-dir>/qp/
├── settings.json                         optional
├── INDEX.md                              optional generated navigation
├── records/<owner>/<stable-subject>/     created on first record
└── artifacts/<stable-subject>/           created on first standalone artifact
```

A registered worktree may expose `.qp` as a reconstructible symlink to that shared store. No worktree is privileged as the physical owner, and a bare repository may own state without a worktree alias. Existing dated record/artifact directories remain valid legacy identities.

The catalogue headings below mirror repository package organization, not semantic domain boundaries. Select by each skill's owned outcome/trigger: broadly useful planning, review, knowledge, specification, and delivery-decomposition owners may live under `engineering` without requiring a software task.

## Engineering

| Skill | Outcome |
| --- | --- |
| `akosile` | Repository-scoped Git-common workspace, worktree aliases/migration, sparse settings, exact safe publication, generated index |
| `alaga` | Deliver one supplied software/build job through implementation, proof, review, and handoff, including UI delivery depth when the job materially changes product interfaces |
| `amose` | Active project/domain model clarification with exceptional durable knowledge reconciliation |
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
| `architect` | Technical-structure design/review from consequential module seams through system architecture; implementation-readiness gate when needed |
| `wo-pr` | Steward an open PR/MR through CI/conflict/feedback readiness |

## Productivity

| Skill | Outcome |
| --- | --- |
| `alarina` | Inventory available skills and route when ownership is unclear or several independent owner results need sequencing |
| `arojinle` | Resolve consequential choices through a user-confirmed decision frontier |
| `ayewo-igba-ise` | Evidence-backed postmortem for completed/abandoned/disputed work, incidents, sessions, or corpora |
| `fihanmi` | Visual understanding of supplied/current material through the smallest faithful representation |
| `handoff` | Compact host-neutral fresh-session handoff packet |
| `html-artifact` | Selective traceable accessible HTML visualization of supplied material |
| `iwadi` | High-trust claim-appropriate research with high-threshold exact-version technical source escalation |
| `ro-wo` | Test one material premise before judgment |
| `salaye` | Reusable plain-language explanation behavior for a supplied subject |
| `slides` | Explanatory, instructional, status, review, strategic, or persuasive presentation design |
| `system-cleanup` | Safe macOS storage audit, regenerable cleanup, worktree review, and external-drive offload |
| `technical-writing` | Technical communication structure/clarity from direct reader/job/syntax principles |
| `yo-slop` | Final prose cleanup / explicit pruning without contract change |

`salaye` is intentionally lightweight: its value is reliable reusable model steering, not hidden machinery.

Fihànmí is likewise deliberately thin: its selected result is visual legibility itself. It uses pseudocode, trees, shaped diffs, Mermaid, aligned comparisons, or a whole target shape as appropriate without becoming another semantic analyst. Use Ṣàlàyé for newcomer-oriented plain-language explanation, HTML Artifact for substantial standalone browser projections, and Slides for presentation/deck outcomes.

## Experimental

Experimental skills participate in normal first-party routing when their owned outcome fits and host invocation metadata permits it. A skill may deliberately require direct user activation when its boundary is an intent island; this is a skill-specific gate, not category-wide isolation. Experiments exist to prove their utility and limits in real work, then be promoted, kept experimental, narrowed/folded, replaced, or removed. Do not invoke one merely to collect experiment data, and do not treat low raw invocation count as failure when the owned outcome is genuinely rare.

| Skill | Outcome |
| --- | --- |
| `amoye-ui-ux` | UI/UX direction, proportionate design exploration, explicit affordance acceptance, and rendered convergence |
| `brand` | Durable brand voice/identity/logo/icon/assets source of truth |
| `dogfood` | Real-browser verification of changed user journeys |
| `ideate` | Grounded mechanism-diverse possibilities before selection |
| `pepeye` | User-requested task supervision across skill or ordinary host/domain owners without a second lifecycle |
| `pese` | Explicitly activated private serving of one bounded local resource |
| `prototype` | Disposable truthful decision instrument |
| `root-cause` | Minimal evidence-backed causal mechanism/set for an observed failure |

Pèsè is the renamed private-serving owner and retains Fihàn's explicit activation/security boundary.

Amọ̀ye and Brand remain independent judgment/semantic outcomes while their portfolio maturity is exercised. UI implementation and reusable token/component realization are internal delivery depth behind Alága rather than separate public owners. Banner/social surface taxonomies and design-only routing are retired; ordinary host/image/design capability remains available when no skill materially improves the result.

Historical Akọ̀wé and Orísun experiments remain research evidence. Their useful methods now live behind Alága's implementation-counsel path and Ìwádìí's exact-source escalation instead of occupying public routing surface.

## Start

Use the obvious owner directly when the requested outcome is clear:

```text
Implement or fix code → alaga
Plan a material initiative → atona
Review a code candidate → atunwo
Resolve consequential choices → arojinle
Research a material claim → iwadi
Show a current relationship visually → fihanmi
Diagnose an observed failure → root-cause
```

Use `alarina` when the user asks which skills are available, when the correct owner is unclear, or when the request genuinely needs sequencing across several independently useful owner results.
