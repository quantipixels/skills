# Brand asset approval

Use for a brand-owned asset that is actually being considered for approval. Apply the current brand, project, and target-surface requirements; do not impose generic QP filename, size, dimension, color-ratio, or platform defaults.

Check only applicable areas:

- **Purpose and audience** — the asset supports the stated communication job.
- **Identity** — approved logo, icon, typography, color, and imagery rules are followed.
- **Copy** — brand voice, factual claims, CTA, and required notices are correct.
- **Accessibility** — applicable contrast, legibility, non-color meaning, labels, and reading order are sound.
- **Technical delivery** — requested dimensions, format, resolution, crop/safe area, performance, and editability requirements are satisfied.
- **Source and version** — the exact candidate/source/export identity and approval signal are recorded.

Use native/project evidence for technical properties, such as image inspection, `file`, byte counts, or an existing asset manifest. Verify volatile platform requirements from the current owning source when they materially affect acceptance.

Return `APPROVED | REVISIONS_REQUIRED | EVIDENCE_GAP` with exact asset identity, applicable contract, failed/unproved requirement, smallest correction/evidence needed, and approval receipt when present.

Do not claim production/platform acceptance from a generic checklist or mockup alone.
