# Exact code-change views

Use for supplied patches, old/new files or pinned PR/MR evidence. Present the supplied review; originating findings and verdicts belongs to the review owner.

Pin the actual contents behind a URL. For repository correspondence, record repository, base/head revisions and identity of uncommitted content; a moving branch or PR number alone is insufficient. Preserve source cutoff and file/hunk coverage. Label partial selection, truncation and unavailable, binary, generated, renamed or deleted files explicitly.

Lead with candidate identity, purpose, coverage and supplied material findings or risks. Keep exact source retrievable. Include supplied behavioral context when needed to understand consequences; do not infer architecture or a verdict from patch shape or size.

Choose native code blocks, aligned before/after, unified/split diffs or a file index according to the reading task. Preserve filenames, old/new line numbers, additions/deletions, order and annotations. Bind annotations to source identity and side/line; show stale or unmapped targets. Label conceptual sketches separately from exact hunks.

Treat all repository content as escaped data. Never execute it or load remote executable code in a private review document. Selection and navigation do not imply approval, resolution or provider mutation.

Use a focused renderer only when its capability earns the dependency under [dependency policy](dependency-policy.md). Preserve exact-code fallback and candidate context if it fails. Pin package identity and derive any cache identity from the actual candidate. A renderer neither fetches the review nor establishes completeness.

Verify rendered file/hunk identities and coverage against the supplied evidence, annotation mappings, escaped content, dependency boundaries and fallback. Preserve keyboard navigation, old/new meaning at narrow widths and non-colour change cues. Apply the main skill's bounded browser checks only to material rendering or interaction claims.
