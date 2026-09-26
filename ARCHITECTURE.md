# Architecture

This repository packages QP's engineering methods through one canonical Alárinà skill. The public installation and invocation paths are in [README.md](README.md); this overview describes where to change the package safely.

## Source and ownership

- [`skills/alarina/SKILL.md`](skills/alarina/SKILL.md) is the single discoverable entrypoint. It selects a focused command or playbook and does not make those methods separate installed skills.
- [`skills/alarina/routes.yaml`](skills/alarina/routes.yaml) owns command and playbook metadata. The command table in `SKILL.md` is generated from it.
- `skills/alarina/commands/` contains cohesive methods chosen by useful outcome and authority, not one command per technical responsibility. `skills/alarina/playbooks/` composes them for multi-stage outcomes. `skills/alarina/references/<use-case>/` holds supporting depth, templates and assets grouped by engineering, productivity, communication, design and language rather than former skills. Direct conditional links serve known callers; the [reference guide](skills/alarina/references/README.md) supports scoped discovery across command families when an outcome needs additional expertise. The entrypoint owns composition and acceptance when predefined methods leave gaps; references can be applied directly without a new command or permanent playbook.
- `skills/alarina/scripts/` holds shared installed utilities: HTML structural diagnostics and local session evidence indexing. Commands own interpretation and acceptance; scripts own their bounded mechanical result. Repository build and verification tooling remains outside the installed skill.
- The HTML Artifact base and control assets under `references/design/html/assets/` use Basecoat's standalone precompiled CSS for components and scoped CSS for document layout and fallback. Their existing jQuery scripts own control behavior. Connected documents load pinned assets; portable documents embed or bundle the selected files. This path has no direct Tailwind build step.
- [`agents/alarina.md`](agents/alarina.md) is the thin portable skill-delegation profile. Provider adapters render Claude Markdown with qualified skill preload and Codex standalone TOML with a qualified skill invocation. Both packages ship the profile; Claude registers it through the plugin, while Codex 0.156.1 requires separate project/user agent placement. The skill owns operating and terminology-maintenance instructions. No model, tool or permission overrides are generated.

Method ownership follows the result: Alága owns implementation and verification, including documentation affected by its change; Architect owns technical structure and `ARCHITECTURE.md`; Amọ̀ṣẹ́ owns domain meaning and its glossary, with separate qualification for ADRs and durable non-goals; Akọ̀wé reconciles a documentation set; Atọ́nà coordinates initiative scope and combined acceptance. [`amose-context`](skills/alarina/commands/amose-context.md) captures resolved terms in an established glossary or a lazily created `CONTEXT.md`; a `CONTEXT-MAP.md` locates scoped glossaries when multiple bounded contexts need them. Legacy learning migration routes codebase rules to established project standards (with `CODEBASE_STANDARD.md` as a lazy fallback), procedures to owning methods or runbooks, and other non-domain knowledge to its maintained source. Ọ̀rọ̀ or Akọ̀wé handles the corresponding text; Amọ̀ṣẹ́ does not absorb those responsibilities into the glossary. See the [feature delivery](skills/alarina/playbooks/feature-delivery.md) and [documentation maintenance](skills/alarina/playbooks/docs-maintenance.md) playbooks for their handoffs.

Knowledge authors share `references/productivity/knowledge-discoverability.md`: Amọ̀ṣẹ́ reaches it through the durable record contract, Ọ̀rọ̀ through the writing contract, and Akọ̀wé through documentation reconciliation. Each owner checks the affected reader path within its existing scope; knowledge stays in its established destination.

`references/engineering/documentation/project-baseline.md` owns useful documentation defaults shared by project setup and broad documentation improvement. Akọ̀wé coordinates existing or missing coverage, using Architect, Amọ̀ṣẹ́ and Ọ̀rọ̀ for their owned results. The baseline covers orientation, architecture, standards, confirmed exclusions, working/verification procedures and agent navigation without fixed file quotas or a new command. Read-only audits assess the same coverage; narrow edits and personal-environment setup do not trigger it.

Local review readiness has one owner in `references/engineering/delivery/local-readiness.md`, consumed by delivery, publication and PR stewardship. Substantive candidates need independent review and relevant local proof before completion or push, with proportionate mechanical-change exceptions and explicit user overrides. Corrections are batched locally; changed content or base invalidates dependent evidence. Remote-only checks and required provider checks remain separate obligations. During TDD, Alága owns Red → Green and corrections; Atúnwò independently judges Standards and Specification, including refactoring. Standards remain shared project knowledge; review stays read-only. Shared test-quality principles live in `references/engineering/verification/test-suite-improvement.md`.

Retrospective results have distinct command owners: `ayewo-igba-ise` for event reconstruction, `ayewo-retro` for coding-session environment improvement, and `ayewo-corpus` for cross-session and artifact-pattern evidence. They share `references/engineering/retrospectives/postmortem-method.md`; session/corpus/artifact depth loads conditionally. The read-only session indexer remains one shared runtime script. Historical command invocations route to the appropriate result without restoring separate installed skills.

Project verification is a capability consumed by delivery, diagnosis, comparison and review. Alága discovers existing project tools before building, identifies missing proof capability early, and uses `alaga-verify-project` for a justified reusable driver or recipe. That command owns launch/readiness, real-path driving, observable effects, surviving evidence and cleanup; `oro-sigidi` authors its agent-facing instructions. Delivery maintains affected recipes, while a requested full-map audit has broader source and runtime coverage. Source-derived recipes are distinct from executed proof.

`alarina-setup` optionally establishes project or personal environment readiness by composing existing owners. It reuses project knowledge, verification capability and host configuration rather than owning a new config format. Commands consume another command's bounded method with task-specific application directions at the caller. Setup, verification and exploration share `references/productivity/inquiry/agent-respondent.md` to apply Àròjinlẹ̀ with the agent as its user/respondent. The interview method stays with Àròjinlẹ̀; this participant assignment creates no new mode or human authority. `references/productivity/inquiry/premise-check.md` supplies the smaller claim check used by planning and the entrypoint without loading worker coordination.

`references/productivity/records.md` owns persistence defaults across commands: routine results stay in context, disposable output uses temporary storage, private resumable state uses an existing record or user-level Alárinà state, shared knowledge stays with its project owner, and requested deliverables stay visible. State is isolated by project/worktree/task, without a registry or new runtime service. Existing `.qp` records remain compatible inputs. Atọ́nà maintains one plan in the appropriate format; HTML is conditional rather than required for every plan.

## Build and distribution flow

```text
skills/alarina/ + agents/alarina.md + scripts/plugins/providers.yaml
                         │
                         ▼
           scripts/plugins/build_alarina_bundle.py
                    │                │
                    ▼                ▼
       plugins/codex/qp-skills/  plugins/claude/qp-skills/
                    │                │
                    ▼                ▼
       .agents/plugins/       .claude-plugin/
       marketplace.json       marketplace.json
```

The compiler builds self-contained native packages, validates links, menus, provider metadata and source provenance, then writes `bundle-manifest.json`. It adds provider-specific invocation metadata while retaining one canonical method tree. The marketplaces point to those generated packages. [`scripts/plugins/README.md`](scripts/plugins/README.md) documents build and native-install checks; [`scripts/skills/check_package.py`](scripts/skills/check_package.py) validates the source package. `evals/alarina/` holds behavioral cases and observations outside the installed skill.

The release boundary is the generated Codex and Claude packages. Other layouts in `providers.yaml` are candidates, not verified distribution targets. An installed package can prove file inventory and manager acceptance; model selection, command loading and task completion need separate runtime evidence.

## Change invariants

- Keep one public `SKILL.md`; add or change a method in `commands/` and its route metadata instead of recreating a standalone QP skill.
- Keep conditional expertise with the relevant command or reference, and workflow progression with its playbook. Preserve explicit-command-only restrictions for `pese` and `qp-update` when changing routes or provider metadata.
- Rebuild both provider packages after canonical-source changes and check generated output for drift. Verify the changed behavior at the relevant source, package, native-install or model boundary; one boundary does not prove another.
- Reconcile this overview when components, ownership, dependency direction or build/runtime flow change. Update affected claims against the final code and keep [README.md](README.md) and other reader instructions aligned without copying install steps here.
