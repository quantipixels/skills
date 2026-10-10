# Markdown source, HTML reading view

Reports, plans, specs, comparisons, reviews, PR tours, incident reports and explainers are written once in Markdown. Agents read and edit that source. People get generated HTML when a spatial, visual or interactive view helps. Commit the Markdown; generate HTML on demand. Commit an HTML copy only when it must be shared as a file, and regenerate it rather than editing both versions.

## Generate

The bundled Python scripts use only the standard library. Anchor the installed skill, then run them:

```bash
SKILL_DIR="<absolute path of the directory containing the SKILL.md you just read>";
python3 "$SKILL_DIR/scripts/md_to_html.py" name.md
python3 "$SKILL_DIR/scripts/verify_artifact.py" name.html
```

By default `name.md` produces `name.html` beside it. `--output` chooses a different HTML path. Input text, source filename, options and bundled assets determine the bytes; there is no clock, network or random ID. Metadata includes the source basename and supplied revision, or a source hash when revision is absent. A supplied date is shown in the footer; the converter does not fabricate one. It reads the stylesheet and mark from the assets and embeds the plain-JS controls it needs.

## Supported source

ATX headings (`#` through `######`) get unique anchors and an index. Paragraphs, `*emphasis*`, `**strong**`, inline code, ordinary Markdown links, ordered/bullet lists, nested indented lists, task lists, pipe tables, block quotes and backtick/tilde code fences are supported. Front matter is a flat set of `key: value` lines; quoted strings are accepted. Every field is shown as visible metadata. Raw HTML is escaped. This is a documented document subset, not a complete CommonMark implementation; images, link-reference definitions and complex YAML are outside it.

Fenced extensions keep their content in the Markdown source. A fence containing other fences uses more backticks outside than inside, for example four outside and three inside.

| Fence info | Body | HTML result |
| --- | --- | --- |
| `details Optional depth` | Markdown | Native `details`/`summary`, keyboard accessible and expanded for print |
| `tabs Code examples` | Two or more `## Label` sections, each containing Markdown | Keyboard tabs; all panels remain in source and print |
| `chart` | JSON object shown below | Static inline SVG plus a data table; no runtime renderer |
| `timeline Milestones` | JSON array of `time`, `title`, optional `text` strings | A labelled ordered timeline |
| `callout Note` or `tldr Decision` | Markdown | A highlighted reading note with a visible title |
| `mermaid Diagram title` | Mermaid source | Escaped source and an explicit rendering-off note by default |

A chart object uses `type` (`bars`, `lines` or `sparkline`), `title`, `labels`, `values` and optional `unit`:

```json
{"type":"bars","title":"Illustrative checks","unit":"checks","labels":["A","B"],"values":[3,5]}
```

A chart of numeric durations uses `type: "timeline"`, a title, optional units and `events` with `label`, `start` and `end`. Values must be finite numbers; labels and values have equal length; timeline end is at least start. The helper is intended for small charts; numeric timelines accept up to twelve rows.

```json
{"type":"timeline","title":"Illustrative work","unit":"minutes","events":[{"label":"Draft","start":0,"end":20},{"label":"Review","start":20,"end":35}]}
```

The milestone `timeline` fence instead uses text timestamps:

```json
[{"time":"09:00","title":"Draft","text":"Record the evidence."},{"time":"09:20","title":"Review"}]
```

[Sample Markdown](../assets/sample.md) exercises every extension. Generate it to a temp output to try the page. Duplicate keys, invalid chart data and unclosed fences fail with a diagnostic before writing the output.

`--mermaid` selects the pinned remote renderer for a disposable connected preview only. Default generation does not contact a service or fetch a library. For a kept diagram page, render once to SVG and inline it; keep the Markdown source. See [dependency policy](dependency-policy.md).

## Meaning and design

Use the QP mark, [QP tokens](design-tokens.md), a readable column, visible source/revision metadata and footer. Adapt layout, type and density to fit the report. An explicit user direction or named project identity governs adaptation within the palette limits. Body prose is about 72 characters wide; tables/code scroll in their own box rather than overflowing the page.

Semantic headings, `section`, `article`, `dl`, `table`, `details` and `time` preserve reading order. Stable IDs also appear in visible text. Charts and diagrams add to complete prose or numbers, never replace them. Escape supplied content in HTML/JSON/SVG; private review pages load no remote executable code.

## Inline in SIGIDI

Use the native HTML preview/render tools when available. Pass the whole self-contained page, log `ready` after controls/renderers finish, inspect the console in both themes, and publish with the measured content height. Use fluid width, fixed pixel chart heights, no viewport heights and no outer card or horizontal padding. The starter detects the host and removes its standalone header/footer/toggle; source metadata remains in the body. Background/text follow the injected theme; QP accent/status/chart colours remain QP. No theme stylesheet is reordered.

For phones check about 390px wide. If native inline tools are unavailable, use an available local browser preview and return the HTML path with that limitation. Verify keyboard focus, print, no-script reading and useful offline output. A generator pass proves structure and reproducibility, not factual truth or human understanding.
