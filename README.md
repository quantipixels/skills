# QP Skills

Engineering methods for capable coding agents: reliable changes, fewer human corrections, and decisions and evidence people can inspect.

Start with the outcome, not an agent fleet. Use **alaga** for an accepted change, **atunwo** for independent review, or **atona** for an initiative and its decisions. **alarina** is optional cross-skill coordination. The host owns discovery, workers, permissions and model settings.

## Install

Use one installation manager per host. Native plugins include the complete linked skill package and the optional Alárinà agent.

### Codex

```bash
codex plugin marketplace add quantipixels/skills
codex plugin add qp-skills@qp-skills
```

Restart Codex. Alternatively add `quantipixels/skills` through the app's custom marketplace interface.

### Claude Code

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

Reload plugins or restart. Claude's plugin namespace applies to slash commands.

### Editable skill copies

```bash
npx skills add quantipixels/skills --agent codex --skill '*'
```

Use `--agent claude-code` for Claude and `--global` for a personal installation. Selective installations must include the linked companions needed by the chosen branch; links do not install dependencies. Source/reference checks are not proof of native discovery or invocation.

## Work directly

| Requested result | Useful owner |
| --- | --- |
| Diagnose, recover or implement and verify a change | `alaga` |
| Independent correctness or simplification judgment | `atunwo` |
| Intent, decision interview, plan or initiative delivery | `atona` |
| Structure and evolution; domain meaning; research | `architect`, `amose`, `iwadi` |
| Prototype/comparison; evidence-backed postmortem | `adanwo`, `ayewo-igba-ise` |
| Clear writing; human view including HTML; PR/MR work | `oro`, `fihanmi`, `seda-pr` |
| Optional composition and Codex execution profile | `alarina`, `codex-orchestra` |
| Explicit maintenance/access or focused utility | `qp-update`, `pese`, `system-cleanup`, `yoruba-glossary` |

A working brief for personal or project instructions:

```text
Use relevant QP methods directly. Keep settled work direct and preserve accepted decisions when resuming. Use atona for initiatives and fihanmi for one current HTML plan. Show what changed, decisive evidence and remaining limits. Do not expand authority or claim unexecuted work.
```

Personality and model preferences remain yours. The Codex-only Orchestra profile is optional policy guidance, not a configured concurrency limit, enforced model allowlist or proven saving. It does not apply to Claude or change host configuration.

## Explicit-only operations

Invoke `$qp-update` or `$pese` explicitly in Codex. In Claude invoke the installed plugin command, for example `/qp-skills:qp-update`. Natural-language mentions alone are not the supported trigger for these manual-only skills. They carry both hosts' invocation metadata and preserve scoped authority in their methods.

[Native controls and compatibility limits](docs/migration.md#host-behavior) explain what is declared versus what still requires runtime verification. QP does not automatically update itself, install managers or expose resources.

## Contribute and verify

```bash
python -m pip install -r requirements-dev.txt
python scripts/check_package.py
python -m unittest discover -s tests -v
python -m unittest discover -s scripts/plugins -p 'test_*.py' -v
python -m unittest discover -s proof -p 'test_*.py' -v
```

The last command needs a JDK for the Java acceptance controls. CI runs these model-free checks. `scripts/plugins/verify_native_install.py` remains an opt-in native-manager check; it does not establish fresh-session invocation.

[Proof](proof/README.md) separates package mechanics, behavioral acceptance and improvement claims. It keeps independent oracles and selected task boundaries without a general campaign runner. No model credentials are needed for package CI.

See [migration and design decisions](docs/migration.md), the [living rebuild record](docs/rebuild.html), and [evidence provenance](docs/evidence.md). The pre-rebuild repository is retained in Git history as experimental evidence, not an immutable specification. This is a breaking rebuild; it is not a claim of measured model improvement.
