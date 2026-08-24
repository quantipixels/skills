# Keep scripts with outcome owners

Status: Accepted

QP will keep a skill-local script only when it implements deterministic behavior that the skill must own. A skill will use the active platform’s native capability when that capability already owns project discovery, configuration, compatibility, and updates. Legacy platform support remains an on-demand research path in the owning skill; QP will not preserve a generator merely to encode one platform generation.

This decision removes the shadcn/ui and Tailwind configuration wrappers from `asa-oju-ibanisoro`. The skill will detect the installed versions and use the project package manager, native shadcn CLI, and version-appropriate Tailwind configuration. It also removes Brand’s misleading image-color wrapper and cross-skill token synchronizer. `brand` owns confirmed brand meaning and a structured handoff; `eto-apere` owns token reconciliation, generation, validation, replacement, and readback.

`amoye-ui-ux` will return one structured recommendation with one Markdown rendering. The calling workflow owns durable state and presentation. The skill will not maintain a parallel design-system directory, master file, or page-override lifecycle. Small wrappers and flags that advertise no distinct behavior will be removed. Provider trust, credential isolation, pagination, state, locking, retries, and candidate-proof scripts remain with their independently installable outcome owners.

Keeping the helpers was rejected because it duplicated fast-moving platform behavior and gave several skills overlapping ownership of the same project files. A shared script runtime was rejected because independently installed skills must retain their own safety and execution contracts. A blanket size limit was rejected because line count does not distinguish essential deterministic behavior from accidental workflow machinery.

The removals are intentional compatibility breaks. Current human-facing safety expectations move into the owning skills; wrapper-specific tests and private persistence expectations become obsolete. Future helpers must justify their own outcome boundary, deterministic proof, and maintenance cost instead of serving as aliases for native tools.
