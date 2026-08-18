# Keep Pare read-only

Pare owns simplification discovery through repository `audit` and bounded candidate `review`. It classifies implementation, dependency, support-artifact, and test cleanup candidates; returns ranked implementation slices and future verification; and never edits files, runs tests or builds, changes Git state, executes cleanup, or uses provider writes.

Alaga `job` owns implementation of an accepted bounded Pare slice. A `deep-clean candidate` also requires explicit opt-in before the delivery owner may abandon non-contract test proof. Separating evidence from execution keeps repository-wide audits safe, preserves one simplification vocabulary, and makes mutation authority explicit.
