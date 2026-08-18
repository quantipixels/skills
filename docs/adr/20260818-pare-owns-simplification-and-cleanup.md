# Let Pare own simplification and cleanup

Status: Superseded by [Keep Pare read-only](20260818-keep-pare-read-only.md).

Pare owns independently useful simplification discovery and bounded cleanup through four short modes: `audit` for a read-only repository-wide audit, `review` for a read-only fixed-candidate maintainability review, `clean` for behavior-preserving removal of proved unnecessary implementation or tests, and `deep-clean` for explicitly authorized aggressive contract-focused test deletion. QP Code Review consumes exact-current Pare `review` evidence in broad review but retains defect discovery, blocking classification, verdicts, provider adaptation, and provider operations. Alaga retains behavior-changing delivery, Atona retains architecture decisions, and Audit Refactor Behavior retains stateful behavior parity.

This supersedes the earlier placement of maintainability-only review in QP Code Review and the longer Pare mode names. A single specialist improves locality across repository, candidate, implementation, and test simplification. Keeping verdict and provider authority in QP prevents Pare from becoming a second code-review owner. Short verb modes keep the interface clear; `deep-clean` is test-only because human authorization cannot prove production code unreachable.
