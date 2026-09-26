# Architecture

This repository packages QP's engineering methods through one canonical Alárinà skill. The public installation and invocation paths are in [README.md](README.md); this overview describes where to change the package safely.

## Source and ownership

- [`skills/alarina/SKILL.md`](skills/alarina/SKILL.md) is the single discoverable entrypoint. It selects a focused command or playbook and does not make those methods separate installed skills.
- [`skills/alarina/routes.yaml`](skills/alarina/routes.yaml) owns command and playbook metadata. The command table in `SKILL.md` is generated from it.
- `skills/alarina/commands/` contains cohesive methods chosen by useful outcome and authority, not one command per technical responsibility. `skills/alarina/playbooks/` composes them for multi-stage outcomes. `skills/alarina/references/<domain>/` holds supporting depth, templates and assets that commands load when relevant.
- `skills/alarina/scripts/` holds shared installed utilities: HTML structural diagnostics and local session evidence indexing. Commands own interpretation and acceptance; scripts own their bounded mechanical result. Repository build and verification tooling remains outside the installed skill.
- The HTML Artifact base and control assets under `references/html-artifact/assets/` use Basecoat's standalone precompiled CSS for components and scoped CSS for document layout and fallback. Their existing jQuery scripts own control behavior. Connected documents load pinned assets; portable documents embed or bundle the selected files. This path has no direct Tailwind build step.
- [`agents/alarina.md`](agents/alarina.md) is the portable agent profile. The Claude package includes it as a native agent; the Codex package does not claim a native plugin agent.

Method ownership follows the result: Alága owns implementation and verification, including documentation affected by its change; Architect owns technical structure and `ARCHITECTURE.md`; Amọ̀ṣẹ́ owns domain meaning and its glossary, with separate qualification for ADRs and durable non-goals; Akọ̀wé reconciles a documentation set; Atọ́nà coordinates initiative scope and combined acceptance. [`amose-context`](skills/alarina/commands/amose-context.md) captures resolved terms in an established glossary or a lazily created `CONTEXT.md`; a `CONTEXT-MAP.md` locates scoped glossaries when multiple bounded contexts need them. Existing non-domain knowledge stays with its owning source rather than entering the glossary. See the [feature delivery](skills/alarina/playbooks/feature-delivery.md) and [documentation maintenance](skills/alarina/playbooks/docs-maintenance.md) playbooks for their handoffs.

TDD delivery separates Red → Green construction from deliberate refactoring assessment, respecting an explicit request to skip review. Alága implements one observable slice at a time; Atúnwò independently judges Standards and Specification against the working candidate, including warranted refactoring. Alága applies accepted corrections and refreshes affected proof. Standards remain shared project knowledge; Atúnwò owns review expertise and stays read-only. Playbooks reuse this review instead of creating a duplicate gate. Shared test-quality principles live in `references/alaga/test-suite-improvement.md` and inform both construction and review without transferring edit authority.

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
