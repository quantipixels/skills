# Variants of a confirmed cause

Use after the causal mechanism is established and related instances are in scope. Start with the known failing revision or an equivalent preserved example, the enabling conditions and the behavior that proves the defect. If only a suspicious pattern is known, return to diagnosis.

1. Choose text, structural, resolved-symbol or data-flow search from the confirmed causal mechanism. Calibrate against the known instance before trusting negative results; account for a fixed or moved example rather than silently searching the wrong revision.
2. Generalize one dimension at a time: identifier, type, representation, caller, operation or missing guard. Inspect the effect of each expansion. Prefer bounded likely consumers and shared implementations; widen only when the mechanism or requested coverage justifies it.
3. Check related entry points and representations, including adapters, batch paths and alternate units where relevant. A spelling match is neither necessary nor sufficient for the same bug.
4. For each candidate, trace trigger, enabling conditions, effect and existing containment against the original cause. Record source evidence or a safe reproducer sufficient to support the classification. Similar syntax with a different precondition may be a look-alike.

Return confirmed variants separately from rejected look-alikes, unresolved candidates and unassessed areas. Include the decisive search scope and limits; a bounded search does not prove repository-wide absence. Stop when further expansion cannot usefully discriminate candidates within scope. No mandatory report, agents, regression rule or CI change follows from finding a variant. Correction remains a separately authorized delivery result.
