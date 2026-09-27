```alarina-workflow+json
{
  "version": 1,
  "id": "verify-changed-cli",
  "title": "Verify a changed CLI from a clean starting state",
  "scope": "project",
  "status": "draft",
  "assumptions": ["The project supplies an isolated CLI invocation and owned scratch storage."],
  "steps": [
    {"method": "commands/alaga-verify-project.md", "requires": ["Accepted CLI behavior and actual project commands"], "produces": ["Cold-start journey, effect observations and cleanup evidence"]},
    {"method": "commands/atunwo.md", "requires": ["Candidate and executed journey evidence"], "produces": ["Independent standards and specification judgment"]}
  ],
  "evidence": [],
  "retirement": "Revisit when the CLI contract, fixtures or supported runtime changes."
}
```

This specimen is unexecuted. Adapt its assumptions and exact commands to the project before use. Method paths above are relative to the loaded Alárinà directory, not this file. Project method paths should name their actual owner.

Record the entry condition, permitted effects, working directory, exact invocation, expected observations, owned cleanup handles and evidence destination. Supply only useful branches. Add actual evidence and set `verified` only after a successful run; a schema pass does not promote the recipe.
