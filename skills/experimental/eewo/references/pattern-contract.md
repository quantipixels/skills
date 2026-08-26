# Pattern contract

Use this contract for `eewo` pattern records and lifecycle decisions.

## Rule lifecycle

```text
observed -> candidate -> validated -> active -> superseded | retired
                     \-> rejected
```

- `observed`: pinned evidence exists; no general rule is asserted.
- `candidate`: a possible invariant, failure mechanism, scope, prohibition, and safe path have been formulated.
- `validated`: the candidate has enough evidence and counterexample checking to be considered for activation.
- `active`: may enter task guard packs.
- `superseded`: a named newer rule replaces it.
- `retired`: no longer useful or applicable.
- `rejected`: promotion failed; keep the reason when it prevents rediscovery churn.

Do not treat lifecycle progression as automatic. A one-off mistake can remain `observed` forever.

## Contribution lifecycle

Track publication independently:

```text
local_only -> draft -> submitted -> accepted | rejected
                                      \-> diverged
```

A local rule can be `active` while contribution is `local_only`, `submitted`, `rejected`, or `diverged`.

## Pattern record

Persist durable local patterns through `akosile` with `owner: eewo` and `record_type: pattern`. The semantic body should carry the following fields when applicable:

```yaml
pattern_id: <stable semantic id>
rule_status: observed | candidate | validated | active | superseded | retired | rejected
kind: prohibition | advisory

applicability:
  languages: []
  frameworks: []
  versions: []
  repositories: []
  paths: []
  phases: []

invariant: <property to preserve>
forbidden_behavior: <semantic bad behaviour>
failure_mechanism: <how the behaviour breaks the invariant>
safe_paths: []
exceptions: []

evidence:
  primary: []
  supporting: []
  local: []

enforcement:
  deterministic: []
  semantic_review_required: true | false

contribution:
  status: local_only | draft | submitted | accepted | rejected | diverged
  source_revision: <local revision or null>
  target: <repository/pack or null>
  proposal_identity: <digest/provider identity or null>
```

The common `akosile` record frontmatter still owns record revision, updated time, title, candidate identity, and owner-native status. Do not duplicate filesystem identity inside the semantic body.

## Promotion test

Promote only when the answer is sufficient for every material question:

1. What exact failure or risk is being prevented?
2. Why can it recur beyond the originating line or session?
3. What is the smallest correct scope?
4. Which invariant does the rule protect?
5. What safe implementation paths remain?
6. Which legitimate exceptions exist, and what proof permits them?
7. Can a deterministic tool enforce all or part of it?
8. Does an existing rule already own the same failure mechanism?
9. What evidence would prove this rule too broad, stale, or harmful?

Reject or retain as an observation when the rule is merely style, architecture fashion, a framework choice without a failure mechanism, a duplicated formatter/linter rule, or a one-off preference without durable authority.

## Rule quality

Prefer:

```text
Invariant -> prohibited behaviour -> failure mechanism -> safe path -> exception/proof
```

over:

```text
Never use <token/API/pattern>
```

A syntax-specific detector may support a semantic rule, but it must not become the semantic definition unless the syntax itself is the failure.

## Contribution snapshot

A contribution proposal is immutable relative to one local revision. Include only portable fields:

- stable pattern id and title;
- portable applicability;
- invariant;
- forbidden behaviour;
- failure mechanism;
- safe paths;
- public exceptions/proof;
- public sources;
- deterministic enforcement hints; and
- sanitized fixtures when useful.

Exclude private evidence by default. If the local rule changes after proposal creation, create a new proposal revision rather than silently changing the in-flight contribution.
