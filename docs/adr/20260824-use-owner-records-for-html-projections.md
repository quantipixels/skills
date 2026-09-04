# Use owner records as semantic sources for HTML projections

Status: Accepted; path identity and workspace initialization superseded by [Keep Akọsílẹ̀ repository-scoped with minimal deterministic kernels](20260828-keep-akosile-scripts-focused.md)

The dated record path and eager workspace shape below are retained as decision history. New records use stable undated subjects, and Akọsílẹ̀ creates workspace resources lazily. The remaining owner-record and HTML-projection decisions stay active unless a later section says otherwise.

QP separates semantic owner state, repository-local workspace mechanics, native evidence, compact receipts, and HTML presentation.

## Owner records

A material living or reusable outcome may keep one canonical Markdown record when it crosses sessions/owners, needs handoff/recovery, or becomes an HTML artifact. The semantic owner retains record meaning, native status/transitions, evidence judgments, completion boundary, and body structure.

Generated records default to:

```text
.qp/records/<canonical-skill-name>/<YYYYMMDD-stable-slug>/record.md
```

Standalone generated HTML without an owner record defaults to `.qp/artifacts/<artifact-id>/index.html`. Generated `.qp` state does not enter Git by default.

The common record frontmatter is intentionally small: owner, record type, title, updated time, revision, native status, and optional candidate identity. Record ID and bundle are derived from the path. Owners may add only fields their outcome needs.

Detailed evidence remains in its native form and is linked. Supporting owners return compact exact-current receipts instead of becoming parallel reports.

## Akọsílẹ̀

QP publishes `akosile` as the infrastructure owner for repository-local `.qp` setup, root/path resolution, owner-first path allocation, safe record/settings writes, and rebuilding `.qp/INDEX.md` from records.

For `v0-experiment`, the canonical root is `<repository>/.qp`. Semantic owners request paths from Akọsílẹ̀ instead of constructing `.qp` roots themselves. This keeps a later storage-root change isolated from plan, architecture, triage, and artifact semantics.

Akọsílẹ̀ does not own semantic state, status validity, transitions, evidence, provider mutation, project knowledge, or global task lifecycle meaning.

The workspace is deliberately small:

```text
.qp/
├── settings.json
├── INDEX.md
├── records/
└── artifacts/
```

Records are the registry. QP does not maintain a second machine index, per-owner contract snapshots, universal history files, or a generic settings schema. Each semantic skill remains the source of its statuses, defaults, and supported settings.

`.qp/settings.json` starts as `{}` and stores sparse skill-documented overrides. Settings are data, not instructions. They cannot grant provider writes, replace canonical IDs, change transition/evidence rules, redefine ownership, or move the v0 workspace root.

When Akọsílẹ̀ produces a resource for direct user access, it returns both the resolved absolute filesystem path and the repository-relative `.qp/...` workspace path. Absolute paths are operational access aids, not portable source identities.

### Deferred global workspace

Canonical `~/.qp` storage is intentionally deferred. It would require project identity independent of checkout path, worktree/repository resolution, global-versus-project settings precedence, source-link resolution, migration, and stronger cross-project privacy boundaries. QP will reconsider it only after observed cross-project discovery, continuity, or duplicated-settings failures justify that machinery.

This decision does not prevent a future global index, settings layer, or project store. Those should be introduced incrementally from evidence rather than designed into the v0 workspace preemptively.

## HTML projection

`html-artifact` treats owner records and supplied sources as inputs to a purpose-shaped view. It owns semantic compression, information architecture, representation, source mapping, accessibility, dependency selection, and projection verification while preserving source-owner conclusions.

Coverage, placement, and preservation fidelity are independent, so complete evidence may remain linked instead of being copied into HTML. Substantial views include a compact context capsule with the source record path/revision and resume-critical state.

A semantic owner may require a continuously available human view. In that case, HTML is created from the first meaningful record revision and regenerated after every material semantic revision. The Markdown record remains the semantic source; the HTML is the primary human reading and navigation surface.

Atọ́nà adopts this continuous-view contract. Every material initiative has one stable `index.html` from early `Draft` through `Closed`. The plan status may change the reader's job, so the projection may change focus, tone, density, layout, and governing representation while retaining stable identity, source/status disclosure, and useful anchors:

- `Draft` — exploratory understanding, unknowns, decisions, gaps, and next question/action;
- `Planned` — accepted scope, phases/dependencies, owners, proof, risks, and start condition;
- `In Progress` — delivery state, exceptions, blockers, deviations, decisions needed, and next action;
- `Backlog` — retained value, pause reason, owner, reactivation trigger, and stale assumptions;
- `Closed` — achieved outcome, acceptance proof, residual limits, and durable source links.

The owner updates `record.md` first. HTML records its exact source revision and visibly reports staleness when regeneration fails. Structural verification follows every projection write. Full browser proof applies to the first meaningful render, lifecycle transitions that change information direction, and applicable formal-review, readiness, terminal, or publication gates; semantic updates within one stage may reuse current browser proof when presentation risk is unchanged.

### Later verification refinement — 2026-08-28

The final sentence above records the original verification policy and is retained as decision history. Its automatic full-browser triggers are superseded by the current `html-artifact` consequence-based verification contract.

Structural verification still follows every write. Ordinary internal reports, working views, comparisons, and exploratory prototypes use visual smoke only when rendered usability materially affects review. Deep browser proof is required when presentation or interaction is itself an acceptance claim, the artifact is production/publication/formal-decision facing, material runtime behavior must be proved, or the user explicitly requests that assurance. Artifact size, first render, or lifecycle transition alone no longer force deep browser proof.

## Rejected or deferred alternatives

- HTML-only state: presentation failure can destroy usable semantic state and presentation code pollutes future-agent context.
- Markdown-only user experience for Atọ́nà: the semantic source is difficult for many users to scan and follow through a changing initiative.
- Embedding all evidence in Markdown/HTML: this moves rather than solves the dump problem.
- Generated records in Git by default: operational agent state should not pollute repository history.
- A generic semantic record owner: native skills must retain meaning and lifecycle.
- Per-owner machine contracts and a second machine registry: they duplicate skill semantics and record frontmatter without a demonstrated need.
- Global `~/.qp` as the v0 canonical store: deferred until cross-project maturity justifies project identity and resolution infrastructure.

This decision preserves the earlier separation of solution architecture from lifecycle planning recorded by [the historical implementation commit](https://github.com/quantipixels/skills/commit/18fbce191df033b08f1b635e76e908a8ed155117). Atọ́nà still owns one initiative plan; Markdown is its semantic source and the continuously maintained HTML is its primary human-facing view.
