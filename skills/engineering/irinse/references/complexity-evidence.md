# Complexity evidence

Use when a consuming owner needs deterministic or IDE/static-analysis evidence about code complexity/hotspots. The result is evidence only.

## Prefer current project tooling

Inspect existing build/plugins/config first. Examples include:

- Java/JVM: PMD, Sonar/SonarLint, SpotBugs-adjacent metrics, IntelliJ inspections, ArchUnit for architecture boundaries;
- Kotlin: detekt complexity rules, IntelliJ inspections, Sonar where established;
- Elixir: Credo refactor/complexity/nesting checks;
- Python: Radon or repository-selected analyzers;
- cross-language: lizard or another repository-approved analyzer when its language coverage is suitable.

Do not install a new tool merely because it can output a cyclomatic number if source inspection or an existing tool answers the bounded question.

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
