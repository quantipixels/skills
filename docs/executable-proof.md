# Executable proof inventory

QP keeps executable code only at deterministic/mechanical seams or as a thin human-facing distribution utility. This inventory records the current executable surface and the proof that protects it; it is not a runtime registry and does not authorize adding scripts.

| Executable | Owned mechanical result | Candidate proof | Platform claim |
| --- | --- | --- | --- |
| `skills/engineering/akosile/scripts/safe-write.py` | containment-aware candidate/target CAS publication and atomic readback | focused Akọsílẹ̀ unit tests; `Portable mechanics` matrix | Linux, macOS, Windows |
| `skills/engineering/akosile/scripts/render-index.py` | pure deterministic `.qp` index rendering | focused Akọsílẹ̀ unit tests; `Portable mechanics` matrix | Linux, macOS, Windows |
| `skills/engineering/ko-skill/scripts/validate-package.py` | package/frontmatter/resource integrity | `Skill package`; `Portable mechanics` matrix | Linux, macOS, Windows |
| `skills/engineering/ko-skill/scripts/validate-plugin-agents.py` | host-manifest/agent-preload structural integrity | `Skill package`; `Portable mechanics` matrix | Linux, macOS, Windows |
| `skills/productivity/ayewo-igba-ise/scripts/session-evidence.py` | read-only local Codex/Claude session inventory and structural evidence normalization | focused synthetic tests; `Portable mechanics` matrix | Linux, macOS, Windows parser/package mechanics; real host stores remain host-owned |
| `scripts/uninstall.sh` | source-aware removal of globally installed QP skills only | fake-HOME/fake-lock/fake-`npx` smoke with post-removal verification | Linux, macOS; not claimed on Windows |

`skills/engineering/ko-skill/scripts/requirements.txt` is dependency input, not an executable owner. `test_*.py` files are proof harnesses, not runtime capability.

## Release rule

When an executable is added, removed, or materially changes its safety/compatibility boundary, update the nearest owning proof and this inventory in the same logical change. The inventory does not justify retaining an executable whose capability belongs in native/project/provider tooling or instructions.

Do not infer runtime portability from source language alone. Windows proof applies only to the Python/package mechanics actually exercised by the matrix. The `system-cleanup` skill is explicitly macOS-specific but currently adds no bundled executable to this inventory.
