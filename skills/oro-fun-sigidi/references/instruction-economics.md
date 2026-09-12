# Instruction economics

Read when the shape or wording of agent-facing text may change selection, attention, context pressure, completion, or behaviour.

The goal is not minimum words. It is maximum behavioural leverage per unit of context.

## Use a small working vocabulary

Use compact terms when they let one word carry a recurring distinction:

- **pointer** — always-visible text that names deeper material and the condition for reaching it;
- **branch** — a genuinely different case that requires different behaviour;
- **hot path** — material every invocation needs;
- **bound** — the observable condition that makes a step/result complete;
- **no-op** — instruction that does not materially change useful behaviour from the model's default;
- **cache** — copied environment/repository fact that is cheaper and fresher to inspect at use time;
- **sediment** — stale guidance retained because adding felt safer than deleting.

Prefer established terms with strong model priors. Coin a new term or abbreviation only when repeated use will repay its definition/decoding cost.

## Spend the two loads deliberately

Agent-facing systems spend two different budgets:

- **context load** — text present whether or not it is useful now, such as descriptions and repository-level instructions;
- **human cognitive load** — things a person must remember to invoke or maintain because they are not automatically discoverable.

Model-reachable material spends more context to reduce human memory. Human-only material does the reverse. Neither load should be driven to zero; spend each where it buys useful control.

## Make pointers carry trigger information

A pointer succeeds only when the agent can tell when to follow it. A perfect reference behind a vague pointer is effectively hidden.

A good pointer names the material/capability and the distinct branches that should reach it. Front-load the discriminative term when possible. Do not spend words on synonyms for the same branch.

Good:

- `Database concurrency` — load when a change coordinates mutable shared state.
- `qp-setup` for installation, configuration, authentication, integration, or readiness.

Bad:

- `More guidance` — read when useful.
- `the setup owner` when the exact skill is already known.

## Use an information hierarchy

Place material according to how immediately it is needed:

1. **Hot-path instruction** — every invocation needs it to behave correctly.
2. **Local reference** — useful expertise commonly consulted within the same invocation.
3. **Conditional reference** — branch-specific depth behind a reliable pointer.

Progressive disclosure moves material down this hierarchy only when the load condition remains obvious. Do not hide universal authority, safety, evidence, or completion rules behind an optional reference merely to shorten the root.

Co-locate a concept's definition, rules, caveats, and examples when they normally need to be considered together. Scattering one concept across several files forces reconstruction even when no text is duplicated.

## Use leading words for semantic compression

A strong compact term can recruit useful model priors and replace repeated explanation. Prefer one stable term over repeatedly restating the same multi-clause idea.

Good:

- `no-op` instead of repeatedly saying “an instruction the capable model already follows without this guidance”.
- `cache` instead of repeatedly saying “a copied fact the agent can cheaply inspect from the repository”.
- `bound` instead of repeatedly saying “the condition that tells the agent the work is complete”.

Bad:

- inventing opaque acronyms merely to save characters;
- replacing precise domain terminology with a shorter but weaker synonym;
- using a fashionable metaphor whose behaviour is ambiguous.

A leading word must be stronger than the default behaviour it is trying to steer. “Be thorough” may be a no-op; a precise bound usually has more leverage.

## Give material work a clear and demanding bound

A bound has two useful properties:

- **clarity** — the agent can distinguish done from not-done;
- **demand** — reaching done requires enough of the intended work.

Good:

- Account for every changed public contract.
- Finish when each material finding is resolved, rejected with evidence, or explicitly accepted.

Bad:

- Review carefully.
- Continue until the implementation looks good.

Sharpen a fuzzy bound before adding more workflow. Add extra sequencing or isolation only when the task actually suffers from premature completion.

## Prefer positive steering

State the behaviour you want. Negation can make the unwanted behaviour more salient and often carries less steering weight than a concrete positive target.

Good: `Name the exact skill and its useful variant.`

Weak: `Do not use vague owner language.`

Keep prohibitions for hard boundaries or demonstrated failure modes; pair them with the positive target when useful.

## Respect harness-native capability

Before adding agent instructions, separate a semantic gap from behaviour the current model or host harness already performs reliably.

For multi-agent work, instructions should tune **when/how much** delegation, independence, evidence, capability, or escalation is useful. Leave spawn syntax, concurrency, scheduling, joins, lifecycle, retries, Code Mode, teams, and equivalent mechanics to the harness.

Use host policy for durable user-editable delegation/model/reasoning preferences. Shape each worker through its assignment. Use ordinary host/tool configuration only for hard runtime settings the user actually needs. Do not create another model registry, worker taxonomy, or setup surface merely to mirror controls the host already exposes.

When high-volume context would waste expensive capability, use cheaper workers to collate the surface and preserve exact locators. Give stronger workers compact evidence handoffs and let them reopen decisive material before consequential judgment. Do not fork conversation history as a context shortcut.

Do not add “discover relevant skills”, “parallelize independent work”, “wait for all workers”, or similar generic rules unless evidence shows the target host/model fails without them. A familiar-sounding instruction still has to beat the no-op baseline.

## Delete what no longer earns load

Hunt these deliberately:

- **no-op** — model already behaves this way without the instruction;
- **cache** — environment/repository already answers it cheaply;
- **duplication** — same meaning lives authoritatively in more than one place;
- **sediment** — once-useful text no longer bears on the owned result;
- **superseded mechanism** — a better abstraction, skill, tool, or runtime capability now owns it;
- **exposition without consequence** — explanation that changes neither judgment nor execution.

Remove the whole instruction when its meaning no longer earns load. Do not merely shorten a no-op.

For a frontier-capability claim, compare realistic work with and without the guidance. A capable baseline can justify deleting generic scaffolding; it does not prove specialist expertise, topology, or a hard boundary unnecessary.

## Evolve deliberately, not conservatively

Before a material refactor, pin the current semantics so loss is visible. Then classify each meaningful behaviour as:

- **retain** — still necessary and already well expressed;
- **strengthen** — still necessary but under-specified;
- **relocate** — still necessary but on the wrong information tier;
- **replace** — a better abstraction/tool/skill now expresses it;
- **retire** — it no longer earns behavioural value.

The purpose is not to preserve the old contract. It is to distinguish deliberate evolution from accidental regression.

Stop pruning when the next cut would force consequential guessing about behaviour, authority, evidence, coverage, or recovery. Otherwise keep cutting.

Record only material retired/replaced semantics in the PR or review discussion; do not create a permanent dossier merely to justify simplification.
