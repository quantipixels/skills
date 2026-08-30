# QP Agent Skills

Portable focused skills for established codebases. QP aims for one independently useful outcome per public skill, deep references where judgment benefits, native commands/tools for ordinary mechanics, and bundled code only for narrow deterministic kernels.

Browse the [documentation](https://quantipixels.com/skills).

## Portfolio principles

- Kọ Skill authors every capability/resource at the smallest adequate surface: guidance/reference → visible command → native/project/provider tool → focused library → deterministic script → engine only when it carries a substantial owned vertical.
- Alárinà is the normal QP front door for generic `Use QP` intent: it selects the shortest current owner/flow and steps aside without becoming a task lifecycle or super-skill.
- Akọsílẹ̀ owns one repository-scoped `.qp`: the main worktree holds the real directory and linked worktrees expose symlinks. New records use stable semantic subjects; settings/index/record/artifact resources are created lazily.
- Supporting skills keep detailed results with their native owners rather than copying caller-specific receipt/lifecycle schemas.
- HTML Artifact creates reader-specific projections of supplied material without duplicating source archives or originating conclusions.
- Generated `.qp` state stays outside Git by default.
- Small public skills may intentionally exist as reusable model-steering contracts when a narrow named behavior saves users from restating longer instructions.
- Thin public convenience entrypoints may wrap native commands when one safe memorable invocation materially improves installation, removal, or other human-facing distribution UX.
- Experimental skills are explicit-only and do not replace stable owners.

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

## Engineering

| Skill | Outcome |
| --- | --- |
| `akosile` | Repository-scoped `.qp` paths/worktrees, sparse settings, exact safe publication, generated index |
| `alaga` | Deliver one supplied build job through implementation, proof, review, and handoff |
| `amose` | Exact-current project/domain knowledge, `.learnings`, `.nongoals`, ADRs, local craft |
| `atona` | One initiative plan from Draft through delivery/closure |
| `atunwo` | Code defect/proof/state-parity review and provider review publication when authorized |
| `hitl-review` | Human-led walkthrough, review coverage, specialist discovery, final human decision |
| `irinse` | Select/ready/use/upgrade/remove one companion engineering tool and return bounded evidence |
| `ko-skill` | Author/revise/validate one skill or audit a bounded portfolio |
| `pare` | Read-only simplification audit/review |
| `se-triage` | Supplied-evidence-first issue/report assessment |
| `seda-pr` | Scoped commit/push and PR/MR creation/update |
| `seda-spec` | Confirmed implementation-independent behavior specification |
| `seda-ticket` | Vertical delivery tickets with blockers/acceptance |
| `seda-sigidi` | Draft or explicitly integrate one agent's durable identity/values/boundaries/voice into a known host configuration |
| `solution-architect` | Implementation-ready technical architecture design/read-only review |
| `wo-pr` | Steward an open PR/MR through CI/conflict/feedback readiness |

## Design

Use the exact design specialist directly when one deliverable owner is clear. Use `apere` when design-specific multi-owner routing, prerequisites, dependency order, shared constraints, or approval boundaries are themselves needed.

| Skill | Outcome |
| --- | --- |
| `apere` | Route broad/multi-deliverable design work |
| `amoye-ui-ux` | Coherent UI/UX direction/review from current product evidence + curated judgment |
| `brand` | Durable brand voice/identity/logo/icon/assets source of truth |
| `social-graphics` | Feed/carousel/story/social campaign graphics |
| `eto-apere` | Project-specific token/component-spec contract and CSS realization |
| `asa-oju-ibanisoro` | Accessible responsive React/web UI implementation |
| `banner-design` | Covers/headers/heroes/display ads/print banners |
| `slides` | Presentation/pitch-deck narrative and visual composition |

Banner Design and Social Graphics intentionally remain narrow steering owners even though they share graphic-design fundamentals: the separate selectors encode different surface/adaptation behavior without requiring users to restate it.

## Productivity

| Skill | Outcome |
| --- | --- |
| `alarina` | QP front door: select the shortest current route without owning the task lifecycle |
| `arojinle` | Resolve consequential product/plan/design choices through user-confirmed decision frontier |
| `ayewo-igba-ise` | Evidence-backed coding-agent session/corpus retrospective |
| `handoff` | Compact fresh-session handoff |
| `html-artifact` | Selective traceable accessible HTML visualization of supplied material |
| `iwadi` | High-trust primary-source research record |
| `ro-wo` | Test one material premise before judgment |
| `salaye` | Reusable plain-language explanation behavior for a supplied subject |
| `system-cleanup` | Safe macOS storage audit, regenerable cleanup, worktree review, and external-drive offload |
| `technical-writing` | Technical communication structure/clarity |
| `yo-slop` | Final prose cleanup / explicit pruning without contract change |

`salaye` is intentionally lightweight: its value is reliable reusable model steering, not hidden machinery.

## Experimental

Experimental skills require explicit acceptance.

| Skill | Outcome |
| --- | --- |
| `akowe` | Exact-candidate adaptive expert implementation counsel |
| `dogfood` | Real-browser verification of changed user journeys |
| `fihan` | Serve one bounded local resource privately and return its exact HTTPS URL or Tailcat receiver invocation |
| `ideate` | Grounded mechanism-diverse possibilities before selection |
| `orisun` | Exact-version upstream source grounding for one bounded technical question |
| `pepeye` | Explicit task supervision without a second owner lifecycle |
| `prototype` | Disposable truthful decision instrument |
| `root-cause` | Minimal causal mechanism/set for an observed failure |

Historical `akowe-java`, `akowe-spring`, and catalogue experiments are research evidence only; Adaptive Akọ̀wé does not load those fixed catalogues at runtime.

## Start

For ordinary use, describe the outcome and invoke QP generically:

```text
Use QP for this:

[describe the outcome]
```

Alárinà routes that request to the shortest current owner/flow and steps aside. You can still invoke any exact skill directly when you already know the owner you want.
