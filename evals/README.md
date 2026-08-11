# Skill eval cases

Keep one `evals/cases/<skill-name>.json` suite for every published skill. Cases use realistic user language and remain independent of a particular model runner.

Each suite contains:

- `skill`: the published skill name and filename stem;
- `cases`: the persistent evaluation cases;
- `id`: a suite-local stable identifier;
- `type`: `trigger`, `negative`, `behavior`, or `pressure`;
- `prompt`: raw user input without the intended answer or rationale;
- `expected_owner`: the expected primary QP route;
- `expect`: observable semantic requirements for the response or conduct.

Case types:

- `trigger` proves that a realistic direct request selects the suite skill.
- `negative` proves that an adjacent request selects a different published owner.
- `behavior` exercises a material branch after routing. Its expected owner normally remains the suite skill, but a router suite may name the route it must return.
- `pressure` exercises a credible failed-use, unsafe shortcut, stale-state, or authority scenario.

Every suite requires at least three triggers, two negatives, one behavior case, and one pressure case. Add more cases when a skill has material state transitions or authority branches.

Run `npm run validate:skills` for deterministic catalog, metadata, suite-shape, owner, identifier, and minimum-coverage checks. These checks do not prove model behavior. A model-backed runner should load the exact candidate with fresh context, execute each prompt, compare the result semantically with `expected_owner` and `expect`, and retain the candidate identity and runner limitations.
