# Release stabilization

QP uses Changesets for versioning/release publication. Stabilization is a release-decision boundary around the generated release PR; it is not another version engine, release daemon, or committed lifecycle state.

## Enter stabilization

When the release owner explicitly declares a major/minor release candidate **STABILIZING** in the release PR (or equivalent provider-visible release record), pin:

- release PR/item identity;
- exact source candidate SHA/tree;
- intended release version/scope;
- included changeset boundary; and
- applicable behavioral, compatibility, and real-use evidence still required.

Do not infer stabilization merely because a Changesets release PR exists. Changesets may continue accumulating ordinary unreleased changes until a human release boundary is declared.

## Freeze the public release surface

After `STABILIZING`, keep the candidate on blocker/evidence correction rather than feature growth. Do not add, remove, rename, promote, or materially broaden a public owner; broaden compatibility claims; or introduce another consequential public behavior into that release candidate unless:

1. it fixes a release blocker or proved evidence defect; or
2. the release owner explicitly reopens feature scope.

Reopening feature scope ends the current stabilization epoch. Establish a new exact candidate and rerun only proof whose falsification boundary changed.

Do not manufacture empty release-candidate commits or version churn merely to count cycles.

## Candidate proof

A release candidate is accepting only when all applicable evidence is current for its exact candidate:

- aggregate `Validate` passes, including package, compatibility, portable-mechanics, and focused deterministic proof;
- required fresh-context behavioral critical waves pass for materially changed steering contracts;
- every new public owner has passed Kọ's positive/closest-adjacent-negative admission proof;
- Experimental promotion/removal/fold decisions have the real-use evidence Kọ requires for that disposition;
- compatibility documentation claims no more than the candidate-gated proof demonstrates;
- material independent review evidence is current for the exact candidate/base epoch where review is required; and
- release/changelog narrative matches the candidate rather than an earlier accumulated release-PR snapshot.

A green structural check does not substitute for a required behavioral or real-use proof row.

## Candidate progression

Treat the first stabilized observation as the baseline release candidate. If it exposes a blocker or causes a material source/evidence correction, that correction creates a new candidate epoch. Refresh affected proof and observe the corrected candidate before release.

A release may proceed when the current stabilized candidate has no release-blocking defect or material evidence gap and no later source/base change has invalidated its proof. Do not require a ceremonial second candidate when nothing changed; do require a new candidate after any correction capable of changing acceptance.

## Changesets boundary

`.github/workflows/release.yml` remains the release mechanism:

- pushes to `ori` let `changesets/action` update the generated version PR;
- `npm run version` remains the versioning command;
- `npx changeset tag` remains the configured publication/tag action.

Do not add a parallel version file, release-state database, bespoke changelog generator, or alternate publishing workflow to implement stabilization. If the release mechanism itself must change, treat that as a separate architecture/release-tooling decision and prove migration/recovery explicitly.

## After release

Once the release candidate is published/tagged, the stabilization epoch is complete. New work may resume under normal public-owner admission and evidence rules. Keep the release PR/provider history as the durable release record; do not copy its lifecycle into repository state.
