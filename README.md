# QP Agent Skills

QP Agent Skills is a portable collection of focused skills for established codebases. It helps agents make decisions, plan and deliver work, review code, keep reusable local records, and create selective HTML artifacts.

Skills belong to one Engineering, Design, Productivity, or Experimental install group.

Browse the [QP Agent Skills documentation](https://quantipixels.com/skills).

## Portfolio shape

- Akọsílẹ̀ owns the repository-local `.qp` workspace: root/path resolution, owner-first paths, safe writes, sparse settings, and one generated index. Semantic owners retain record meaning, native states, evidence, and provider authority.
- Solution Architect owns technical architecture design/read-only review. Atọ́nà owns initiative planning through delivery and closure.
- Every material Atọ́nà initiative has one continuously maintained HTML human view from early `Draft` through `Closed`; lifecycle transitions may change its focus, tone, density, layout, and governing representation.
- Supporting skills keep detailed results with their native owners and return compact receipts to an active plan.
- `html-artifact` derives reader-specific views from owner records and linked evidence instead of copying complete source material.
- Generated `.qp` records, projections, receipts, and evidence stay outside Git by default.

## Repository-local workspace

```text
.qp/
├── settings.json
├── INDEX.md
├── records/<canonical-skill-name>/<record-id>/
└── artifacts/<artifact-id>/
```

`settings.json` contains sparse, skill-documented preferences. `INDEX.md` is rebuilt from record frontmatter; records remain authoritative. For generated resources intended for direct use, Akọsílẹ̀ returns both the resolved absolute path and the repository-relative `.qp/...` path.

## Install

```bash
npx skills add quantipixels/skills --global
```

Follow the Skills CLI prompts to choose skills and target agents. The command does not remove retired skills.

### Local checkout

```bash
npx skills add .
```

### Claude Code

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

## Uninstall

```bash
curl -fsSL https://raw.githubusercontent.com/quantipixels/skills/ori/scripts/uninstall.sh | bash
```

## Releases

Read the [latest GitHub release](https://github.com/quantipixels/skills/releases/latest) and [changelog](CHANGELOG.md).

## Start

```text
Use alarina to choose the right QP skill for this request:

[describe the outcome you need]
```

## Engineering skills

| Skill | Use when |
| --- | --- |
| `akosile` | Repository-local `.qp` setup, owner-record/artifact paths, safe writes, settings, index rebuilding, or workspace repair is the task |
| `alaga` | `test-first` handles one bounded feature/fix; `job` handles a supplied build job through integration, proof, and review |
| `amose` | Project terms, `CONTEXT.md`, `.learnings`, `.nongoals`, or ADRs need clarification/reconciliation |
| `atona` | Unclear feature, migration, or initiative work needs one exact-current plan and accessible HTML view through delivery/closure |
| `atunwo` | Defect review or stateful refactor-parity audit is needed for a local/supplied or provider candidate |
| `hitl-review` | A human wants to review one exact candidate interactively, classify its review needs, and surface matching specialist skills |
| `irinse` | A companion engineering tool needs selection, setup, safe use, upgrade, or removal |
| `ko-skill` | One skill needs creation, revision, validation, or bounded portfolio audit |
| `pare` | Read-only audit/review should identify material simplifications and cleanup candidates |
| `se-triage` | One issue/report needs supplied-evidence-first assessment before implementation |
| `seda-pr` | A bounded branch change needs commit, push, and a GitHub PR or GitLab MR |
| `seda-ticket` | Supplied work needs consumable vertical tickets with blockers and acceptance |
| `seda-sigidi` | An AI agent needs a named soul installed, ported, or refreshed |
| `solution-architect` | Technical architecture needs implementation design or read-only sufficiency review |
| `wo-pr` | An open PR/MR needs CI and feedback stewardship through readiness |

## Design skills

Use `apere` when the design owner is unclear or several deliverables must be coordinated.

| Skill | Use when |
| --- | --- |
| `apere` | Broad/multi-deliverable design work needs owner selection, prerequisites, dependency order, or approval boundaries |
| `amoye-ui-ux` | UI/UX direction needs styles, palettes, typography, accessibility, charts, or stack guidance |
| `brand` | Brand voice, identity, logos, corporate identity, or custom icon language needs a durable source of truth |
| `social-graphics` | Feed posts, carousels, stories, templates, or campaign variants are needed |
| `eto-apere` | Tokens, CSS variables, component specifications, or theme architecture need definition/migration |
| `asa-oju-ibanisoro` | Components, responsive interfaces, or product icons need accessible implementation |
| `banner-design` | A cover, header, hero, ad, or print banner needs constrained design |
| `slides` | A presentation or pitch deck needs narrative, layout, and chart guidance |

For multi-deliverable production, `apere` returns the route packet and `alaga` owns the integrated build job.

## Productivity skills

| Skill | Use when |
| --- | --- |
| `alarina` | You need the shortest QP route for a request |
| `arojinle` | One consequential product, plan, or design decision needs a complete interview and confirmation |
| `ayewo-igba-ise` | A coding-agent session or bounded corpus needs evidence-backed friction/recurrence analysis |
| `handoff` | A conversation needs a compact handoff for another agent/session |
| `html-artifact` | Supplied records/results need a selective, traceable portable HTML view |
| `iwadi` | A question needs high-trust primary-source research captured in Markdown |
| `ro-wo` | A material premise needs an evidence-backed check before judgment |
| `salaye` | One supplied subject needs a plain-language explanation |
| `technical-writing` | Technical communication needs layered structure and clarity |
| `yo-slop` | Prose needs cleanup or explicit verbosity pruning without changing its contract |

## Experimental skills

Experimental skills must be selected explicitly. Stable skills may recommend them but do not depend on them.

| Skill | Use when |
| --- | --- |
| `akowe-java` | Java 17–26 implementation, review, or refactoring needs experimental expert language and JDK guidance through 105 progressively disclosed rules |
| `akowe-spring` | Spring Framework or Spring Boot code needs experimental version-aware expert guidance on container, web, data, security, concurrency, testing, operations, or AOT concerns |
| `dogfood` | One branch, PR, or candidate needs real-browser functional and experiential verification of its changed user journeys |
| `ideate` | A grounded opportunity needs several materially different possibilities generated, challenged, and reduced before selection |
| `pepeye` | A task needs provider-neutral lifecycle control across playbooks, leaf owners, proof, pause/pickup, and learning |
| `prototype` | One consequential interaction, flow, interface, API, or message needs a disposable artifact to settle how it should work or feel |
| `root-cause` | One reproducible or directly observed failure needs a complete causal chain rather than issue triage or implementation |

## Optional agent instructions

### Default Pepeye lifecycle mode

Copy the managed block from [Pepeye portable activation](skills/experimental/pepeye/references/portable-activation.md) into a supported instruction file. Explicit invocation remains the fallback.

`olofofo` is retired and no longer published.

### Companion-tool routing

```text
Use `irinse` when a companion tool could materially improve the result.
```

### Technical writing and prose cleanup

```text
Use `technical-writing` and `yo-slop` for communication.
```

### Consider before judgment

```text
Use `ro-wo` before agreeing or disagreeing with a material premise.
```
