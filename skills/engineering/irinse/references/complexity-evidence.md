# Complexity evidence

Use when a consuming owner needs deterministic or IDE/static-analysis evidence about code complexity/hotspots. The result is evidence only.

## Prefer current project tooling

Inspect the repository's build, plugins, configuration, IDE/static-analysis setup, scripts, CI, and documented engineering conventions first. Prefer an analyzer already established for the exact project/language/candidate when it can answer the bounded question.

Do not maintain a language-by-language analyzer catalogue. If no project tool owns the needed signal, select a current suitable tool from the available environment or owning documentation only when the evidence is materially useful and direct source inspection is insufficient. Installing or changing tooling still follows Irinṣẹ́'s normal authority boundary.

Do not introduce a tool merely because it can output a complexity number.

## Collect enough context to interpret later

Return:

```text
Metric/signal:
Tool/version:
Configuration/rule identity:
Analyzed candidate/path:
Raw value/location:
Tool threshold/severity, if configured:
Coverage/limitations:
```

Where feasible include supporting signals such as nesting, method/function size, fan-out, duplicated branches, churn, or test/fixture volume. Do not combine them into a homemade quality score.

## Important limits

- Cyclomatic complexity counts control paths; it does not distinguish coherent explicit state machines from accidental branching.
- Cognitive-complexity formulas vary by tool/version.
- Extracting methods/classes can lower a local score without reducing semantic decisions.
- Generated code and framework glue may require exclusions already defined by the repository.
- A threshold crossing is an investigation trigger. `pare` decides whether complexity is essential/accidental and whether a smaller design exists.
