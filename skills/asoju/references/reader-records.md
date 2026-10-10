# Reader records

A long read costs the most when an expensive model does it. Before a long task, or any child that must read a lot, a cheap reader reads once and writes a record; the expensive models (planner, builder, reviewer, judge) work from the record.

## When

- Before a long-horizon task that needs grounding in a large source: a long thread or past sessions, a large or unfamiliar repository, many docs or logs, a PR's history.
- When a reviewer or judge would otherwise read the whole source.
- Skip it when the source is short, or when the decision needs exact reading of the source itself (security, money, legal, a precise forensic timeline): then the expensive model reads the source.

## The reader

Use the model set's `cheap` row (Luna at medium; its fallbacks are on the models page). The reader extracts; it does not judge or recommend. Every line cites a position (`file:line`, thread position or item id, commit). It writes section by section and saves after each. It ends with a coverage note: what it read fully, skimmed, or could not read, and claims it could not verify.

## Record shapes

- **Session:** timeline of user requests and decisions; user corrections with what the agent had just done; failures and near-misses; host and tool facts found; delegation log (model, task, timing, checkpoints, outcome); reversed decisions; open items; coverage.
- **Repository:** inventory of parts and entry points; how to build, run and test; owners and boundaries; config; where the area of the task lives; known traps; coverage. (A full reference document is a dissection, which is deeper.)
- **Change:** files touched and what changed in each; behaviour before and after; risks and consumers; tests touched or missing; coverage.
- **Docs or logs:** the questions the task asks, the passages that answer them with positions, contradictions, gaps; coverage.

## Using a record

- Work from the record. Spot-check the source only for a gap the record names or a claim the decision depends on, and log each spot-check.
- Save the record as a working record (report), stamped with the commit or thread position it reflects. A later task reuses it while the stamp is current, instead of re-reading.
- Track record size against source size and spot-checks per use. Rising spot-checks mean the record shape needs fixing.
