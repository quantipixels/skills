# Code-change review

Use when supplied code-change evidence must become an HTML review view. Input may be a patch, exact old/new contents, a pinned comparison, or a materialized PR/MR snapshot; a provider URL alone does not establish contents.

## Candidate and coverage

Pin repository/source identity, base/head revisions, a digest or equivalent for uncommitted content, provider identity/retrieval time, changed-file and hunk coverage, omissions/provider limits, source-owner findings/status, and evidence cutoff. A moving branch, HEAD or item number is not an exact candidate. Label selected files/hunks Partial; show binary, generated, renamed, deleted, oversized and unavailable content rather than dropping it.

Treat repository/provider content as untrusted data and render escaped text. Never execute supplied markup or expose credentials.

## Review composition

Open with candidate, purpose/disposition, old/new relation, coverage state, material supplied findings and a path into changed files. Keep the exact patch or old/new sources retrievable. Use pinned surrounding context or owner-supplied architecture/behavior only when needed; HTML Artifact does not originate those conclusions.

Choose the smallest useful exact view: semantic code block, aligned before/after, unified or split diff, or file index with isolated diffs. Preserve filenames, line numbers, patch order, additions/deletions/renames and annotations. Map feedback to stable path/side/line where available and mark stale/unmapped targets. Filtering or collapsing never implies approval, resolution, severity, ownership or provider mutation.

Keep code order meaningful in the DOM, distinguish changes without color alone, preserve keyboard/focus and long-line/narrow-width usability. A diff is evidence, not a complete review: retain supplied behavior, tests, risks, limits and disposition.

Use a current specialized diff renderer such as Pierre Diffs only when syntax-aware multi-file views, annotations, selection, virtualization or comparable interaction earns it. Revalidate current package identity/API/license, bundle or staticize it for standalone output, and retain readable semantic fallback plus the complete pinned source locator. The renderer does not fetch a PR, establish completeness, perform review or publish comments; avoid experimental editing/merge surfaces unless separately requested and proved.

## Verify

Against the exact candidate, compare rendered file/hunk identities and counts, expose omissions/partial coverage, validate annotation mappings/staleness, confirm escaped content, dependency identity and absence of unrequested runtime hosts, and preserve candidate identity/change meaning/retrieval in fallback. Use only the smallest browser check needed to falsify a material renderer or interaction claim.
