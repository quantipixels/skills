# QP Agent Skills

Portable focused skills for established codebases. QP aims for one independently useful outcome per public skill, deep references where judgment benefits, native commands/tools for ordinary mechanics, and bundled code only for narrow deterministic kernels.

Browse the [documentation](https://quantipixels.com/skills).

## Portfolio principles

- Kọ Skill authors every capability/resource at the smallest adequate surface: guidance/reference → visible command → native/project/provider tool → focused library → deterministic script → engine only when it carries a substantial owned vertical.
- Akọsílẹ̀ owns one repository-scoped `.qp`: the main worktree holds the real directory and linked worktrees expose symlinks. New records use stable semantic subjects; settings/index/record/artifact resources are created lazily.
- Supporting skills keep detailed results with their native owners rather than copying caller-specific receipt/lifecycle schemas.
- HTML Artifact creates reader-specific projections over owner records/evidence rather than duplicating source archives.
- Generated `.qp` state stays outside Git by default.
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

## Uninstall this repository's globally installed skills

Until the upstream Skills CLI exposes installation source as a direct filter, use the source metadata already stored in the global lock and pass only matching names to the native remover:

```bash
node <<'NODE' >/tmp/qp-skills.txt
const fs = require('fs');
const os = require('os');
const p = `${os.homedir()}/.agents/.skill-lock.json`;
const lock = JSON.parse(fs.readFileSync(p, 'utf8'));
const norm = s => String(s || '').replace(/^git\+/, '').replace(/^git@github\.com:/, 'https://github.com/').replace(/^ssh:\/\/git@github\.com\//, 'https://github.com/').replace(/^https?:\/\/github\.com\//, '').replace(/\.git\/?$/, '').replace(/\/$/, '');
for (const [name, entry] of Object.entries(lock.skills || {})) if (norm(entry.source) === 'quantipixels/skills') console.log(name);
NODE
mapfile -t qp_skills </tmp/qp-skills.txt
((${#qp_skills[@]})) && npx skills remove --global --yes "${qp_skills[@]}"
```

The recipe deliberately does not use a blanket `--all`; unrelated installed skills remain untouched.

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
| `seda-ticket` | Vertical delivery tickets with blockers/acceptance |
| `seda-sigidi` | Draft or explicitly integrate one agent's durable identity/values/boundaries/voice into a known host configuration |
| `solution-architect` | Implementation-ready technical architecture design/read-only review |
| `wo-pr` | Steward an open PR/MR through CI/conflict/feedback readiness |

## Design

Use the exact design specialist directly when one deliverable owner is clear. `apere` remains available for design-domain multi-owner routing while that independent boundary is being evaluated.

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

Public design-owner consolidation candidates are proof-gated; they are not removed merely because their mechanisms overlap.

## Productivity

| Skill | Outcome |
| --- | --- |
| `alarina` | Select the shortest route from currently available QP skill descriptions |
| `arojinle` | Resolve consequential product/plan/design choices through user-confirmed decision frontier |
| `ayewo-igba-ise` | Evidence-backed coding-agent session/corpus retrospective |
| `handoff` | Compact fresh-session handoff |
| `html-artifact` | Selective traceable accessible HTML projection |
| `iwadi` | High-trust primary-source research record |
| `ro-wo` | Test one material premise before judgment |
| `salaye` | Reusable plain-language explanation behavior for a supplied subject |
| `technical-writing` | Technical communication structure/clarity |
| `yo-slop` | Final prose cleanup / explicit pruning without contract change |

`salaye` is intentionally lightweight: its value is reliable reusable model steering, not hidden machinery.

## Experimental

Experimental skills require explicit acceptance.

| Skill | Outcome |
| --- | --- |
| `akowe` | Exact-candidate adaptive expert implementation counsel |
| `dogfood` | Real-browser verification of changed user journeys |
| `ideate` | Grounded mechanism-diverse possibilities before selection |
| `pepeye` | Explicit task supervision without a second owner lifecycle |
| `prototype` | Disposable truthful decision instrument |
| `root-cause` | Minimal causal mechanism/set for an observed failure |

Historical `akowe-java`, `akowe-spring`, and catalogue experiments are research evidence only; Adaptive Akọ̀wé does not load those fixed catalogues at runtime.

## Start

```text
Use alarina to choose the shortest QP route for this request:

[describe the outcome]
```
