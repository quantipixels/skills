# Create a slide deck

Use this as the creation entry point. It defines the stable deck-level job, not one HTML implementation.

## Establish the deck

Pin:

- primary audience and intended reader outcome: understand, learn, compare, review, decide, act, or another explicit job;
- delivery format and presentation context;
- source evidence/data and any citation obligations;
- brand/project constraints when they exist;
- approximate slide count or time budget; and
- export/viewport requirements.

Then create a slide map:

```text
slide
→ one job
→ message/content appropriate to that job
→ supporting evidence when applicable
→ visual relationship/form
→ transition or relationship to the surrounding deck
```

Use [layout patterns](layout-patterns.md) for the relationship, [slide strategies](slide-strategies.md) for sequence, and [copy patterns](copywriting-formulas.md) only when persuasive/claim-oriented copy shaping is actually needed.

## Tokens and implementation

Consume an existing project/brand token contract when one is relevant. Do not require `assets/design-tokens.*` or create a project token system for a standalone deck unless the user/project actually needs that durable contract.

For HTML, build the minimum semantic deck implementation needed for the current delivery: slide regions, explicit current state, accessible navigation/control labels, target aspect/layout behavior, overflow resilience, and reduced-motion handling when transitions exist. Add a chart dependency only when a chart is required and the host/native capability does not already own it.

For PowerPoint or another native presentation format, use the host's presentation capability rather than translating through an intermediate HTML template.

## Verification

Check the actual delivered format:

- every slide has one clear job and an appropriate readable heading/message;
- text/data/images fit at the target viewport/export without clipping or unreadable type;
- charts preserve units, scale meaning, labels and non-color distinction where needed;
- brand/current token relationships are respected when applicable;
- interactive HTML controls work by keyboard and do not require click-anywhere behavior;
- animation is non-blocking and reduced-motion aware when present; and
- source/evidence obligations remain traceable.

Do not add framework/CDN/template mechanics merely to make a deck look “complete.”