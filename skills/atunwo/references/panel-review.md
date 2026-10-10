# Panel review

Optional. Use when the user asks for several models, or a high-stakes change makes one reviewer too thin. Not for routine reviews.

- Fix the scope, base and head, the requirement sources and the rubric once. Send every reviewer the same packet and rubric, so differences come from judgment and not from different inputs. Pick models by the host's model table.
- Reviewers stay read-only and return findings with location, mechanism and evidence.
- Merge the results: dedupe by mechanism, then record where reviewers agree, where they disagree, and what only one found.
- Judge each finding on its evidence, not on votes. A single defect that is proved (a correctness or security defect you can show) is not outvoted by reviewers who missed it. Several reviewers raising only nits is not proof the code is fine.
- Sort into act on, consider, noted, dismissed, with a line of reason each. Do not cap the count.
- Return one verdict in the usual form, with the agreement and disagreement shown. The panel does not apply fixes.
