# Expert implementation counsel

Load only when material implementation choices could be locally plausible yet wrong for the exact stack, lifecycle, compatibility boundary, ownership model, or proportionality of the current candidate. This is an Alága implementation path, not a second owner or review stage.

## Pin the counsel boundary

Pin the exact candidate/horizon, accepted architecture and domain constraints, material stack/runtime versions, touched mechanisms, proof expectations, and only the questions whose answers can change code or proof.

Use this authority order:

```text
system / developer / user / repository instructions
→ accepted task, architecture, domain, compatibility, and safety contracts
→ exact repository, runtime, and native-tool evidence
→ current owning specifications, documentation, release notes, source, and tests
→ relevant specialist results
→ cautious inference with an explicit evidence gap
```

Challenge consequential choices as they are made rather than producing a large up-front brief. A material counsel item must identify the exact seam and a concrete consequence: caller/operational failure, compatibility/lifecycle/safety/resource rule, stack-native improvement, removal of invalid state/hidden ownership/accidental complexity, or a proof seam for a material invariant.

## Close only material evidence gaps

Start with current repository, dependency, compiler, runtime, framework, IDE, and native-tool evidence. Do not begin from a fixed language/framework catalogue.

- Use `architect` when the missing result is material technical architecture.
- Use `amose` for domain invariants or durable project knowledge.
- Use `root-cause` when a reproducible failure still lacks a causal mechanism and different mechanisms imply different fixes.
- Use `ro-wo` when the alleged need for deeper research rests on a consequential premise; challenge the premise before paying for more evidence.
- Use `iwadi` when substantial primary-source research is independently needed. Let Ìwádìí decide whether ordinary research is sufficient or its high-cost exact-source path is earned.
- Use `irinse` only when bounded companion-tool evidence is itself needed.

For one/few task-local facts, perform the smallest direct primary-source read. Do not invoke another owner merely to fill a category or because more evidence exists.

## Load curated mechanism depth only from candidate cues

After establishing the exact stack, use a local mechanism reference only when the touched code exposes its trigger and the extra depth can change code or proof:

- Java concurrency/visibility, equality/ordering, absence/failure, or resource-lifetime semantics → [Java runtime mechanics](java-runtime-mechanics.md);
- Spring proxy/advice, transactions, JPA/Hibernate persistence, application lifecycle, or reactive execution semantics → [Spring runtime mechanics](spring-runtime-mechanics.md).

These references are compact calibration distilled from earlier QP research, not hidden language/framework catalogues and not substitutes for current source truth. Load neither merely because Java or Spring appears in the repository. Project contracts and exact-current first-party/runtime evidence override them; unfamiliar or version-sensitive behavior remains a bounded current-source question.

## Apply the proportionality gate

For each proposed abstraction, layer, dependency, queue, cache, interface, wrapper, pattern, or state object ask:

```text
What present contract or failure mechanism does it own?
Why are existing repository, language, platform, or framework mechanisms insufficient?
What state, dependency, navigation, migration, or operational burden does it add?
Is that burden proportionate to demonstrated risk?
What stable proof would justify it?
Can the same contract be expressed more directly?
```

No abstraction without a present responsibility. No pattern without a candidate-specific consequence. No dependency without a material capability gap. No research question that cannot change the implementation. No test without an invariant it proves.

Remove formatting preferences, speculative alternatives, deterministic tool concerns, and recommendations whose benefit cannot justify their cost.

## Refresh and finish

Refresh counsel only when the candidate, touched mechanism, stack/version, accepted contract, material premise, or controlling evidence changes. Return only what changed rather than regenerating a large brief.

Before independent review, compare the exact candidate with active counsel and classify material items as:

- `SATISFIED` — candidate follows the counsel;
- `DEPARTED` — deliberate evidence-backed departure;
- `STALE` — candidate/evidence change made the counsel irrelevant; or
- `UNRESOLVED` — a material implementation/proof gap remains.

Resolve `UNRESOLVED` items that can still change implementation/proof before review. This comparison is delivery evidence, never a defect, maintainability, parity, security, or final-review verdict.
