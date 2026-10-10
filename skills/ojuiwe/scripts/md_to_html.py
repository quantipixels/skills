#!/usr/bin/env python3
"""Generate one offline QP HTML document from Markdown, using only the standard library.

The supported Markdown subset and fenced extension formats are documented in
references/document-pages.md. Raw HTML is escaped, never executed. Generation is
stable for identical source text, filename, options and bundled assets.
"""
from __future__ import annotations

import argparse
import hashlib
from html import escape
import json
import math
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import urlsplit

ASSETS = Path(__file__).resolve().parent.parent / 'assets'


def esc(value: object) -> str:
    return escape(str(value), quote=True)


def unique_json(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON key: {key}')
        result[key] = value
    return result


def json_data(text: str):
    return json.loads(text, object_pairs_hook=unique_json)


def link_url(value: str) -> str:
    if any(ord(char) < 32 for char in value) or '\\' in value:
        raise ValueError('link contains a control character or backslash')
    parsed = urlsplit(value)
    if parsed.scheme.lower() not in {'', 'http', 'https', 'mailto'} or value.startswith('//'):
        raise ValueError(f'unsupported link scheme: {value}')
    return esc(value)


# Delimited spans are parsed before escaping; every text leaf is escaped once.
INLINE = re.compile(r'\\([\\`*_\[\]()!|])|(`+)(.+?)\2|\[([^\]\n]+)\]\(([^\s)]+)\)|\*\*(.+?)\*\*|__(.+?)__|\*([^*\n]+)\*|_([^_\n]+)_', re.S)


def inline(text: str) -> str:
    out, position = [], 0
    for match in INLINE.finditer(text):
        out.append(esc(text[position:match.start()]))
        literal, ticks, code, label, href, strong, strong_alt, emphasis, emphasis_alt = match.groups()
        if literal is not None:
            out.append(esc(literal))
        elif ticks:
            out.append(f'<code>{esc(code)}</code>')
        elif href:
            out.append(f'<a href="{link_url(href)}">{inline(label)}</a>')
        elif strong is not None or strong_alt is not None:
            out.append(f'<strong>{inline(strong if strong is not None else strong_alt)}</strong>')
        else:
            out.append(f'<em>{inline(emphasis if emphasis is not None else emphasis_alt)}</em>')
        position = match.end()
    out.append(esc(text[position:]))
    return ''.join(out)


def frontmatter(text: str):
    lines = text.splitlines()
    if not lines or lines[0] != '---':
        return {}, text
    try:
        end = lines.index('---', 1)
    except ValueError as error:
        raise ValueError('unclosed front matter') from error
    metadata = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        match = re.fullmatch(r'([A-Za-z][\w-]*):\s*(.*)', line)
        if not match:
            raise ValueError('front matter supports flat key: value lines only')
        key, value = match.groups()
        if key in metadata:
            raise ValueError(f'duplicate front-matter key: {key}')
        if value.startswith('"'):
            value = json.loads(value)
            if not isinstance(value, str):
                raise ValueError('quoted metadata must be text')
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        metadata[key] = value
    return metadata, '\n'.join(lines[end + 1:])


def chart_svg(config: dict) -> str:
    if not isinstance(config, dict):
        raise ValueError('chart must be a JSON object')
    kind, title = config.get('type'), config.get('title')
    if kind not in {'bars', 'lines', 'sparkline', 'timeline'} or not isinstance(title, str) or not title.strip():
        raise ValueError('chart needs type (bars/lines/sparkline/timeline) and title')
    def finite(value):
        return type(value) in {int, float} and math.isfinite(value)
    def number(value):
        return format(value, '.6g')
    out = [f'<svg class="chart-svg" viewBox="0 0 640 240" role="img" aria-label="{esc(title)}"><title>{esc(title)}</title>']
    ink = 'var(--qp-chart-1)'
    def label(x, y, text, anchor='middle'):
        out.append(f'<text x="{number(x)}" y="{number(y)}" fill="currentColor" font-size="13" text-anchor="{anchor}">{esc(text)}</text>')
    if kind == 'timeline':
        events = config.get('events')
        if not isinstance(events, list) or not 1 <= len(events) <= 12 or any(not isinstance(e, dict) or not isinstance(e.get('label'), str) or not finite(e.get('start')) or not finite(e.get('end')) or e['end'] < e['start'] for e in events):
            raise ValueError('chart timeline needs 1-12 events with label and numeric start/end')
        low, high = min(e['start'] for e in events), max(e['end'] for e in events)
        if not math.isfinite(high - low):
            raise ValueError('timeline numeric range is too large')
        def x(value):
            return 160 + (value - low) / (high - low or 1) * 455
        for i, event in enumerate(events):
            y = 24 + i * 180 / len(events)
            label(150, y + 5, event['label'], 'end')
            out.append(f'<line x1="{number(x(event["start"]))}" x2="{number(x(event["end"]))}" y1="{number(y)}" y2="{number(y)}" stroke="{ink}" stroke-width="8" stroke-linecap="round"><title>{esc(event["label"])}: {esc(event["start"])} to {esc(event["end"])}</title></line>')
        label(160, 229, low, 'start')
        label(615, 229, high, 'end')
    else:
        values, labels = config.get('values'), config.get('labels')
        if not isinstance(values, list) or not values or not isinstance(labels, list) or len(values) != len(labels) or any(not finite(v) for v in values) or any(not isinstance(v, str) for v in labels):
            raise ValueError('chart needs equally sized labels and finite numeric values')
        low, high = min(0, *values), max(0, *values)
        if not math.isfinite(high - low):
            raise ValueError('chart numeric range is too large')
        def y(value):
            return 195 - (value - low) / (high - low or 1) * 160
        def x(i):
            return 48 + (i + .5) / len(values) * 576
        if kind != 'sparkline':
            out.append(f'<path d="M48 20V{number(y(0))}H624" fill="none" stroke="var(--page-border)"/>')
        if kind == 'bars':
            width = 576 / len(values) * .65
            for i, value in enumerate(values):
                out.append(f'<rect x="{number(x(i)-width/2)}" y="{number(min(y(0),y(value)))}" width="{number(width)}" height="{number(abs(y(value)-y(0)))}" fill="{ink}"><title>{esc(labels[i])}: {esc(value)}</title></rect>')
                label(x(i), y(value) + (17 if value < 0 else -7), value)
        else:
            points = ' '.join(f'{number(x(i))},{number(y(value))}' for i, value in enumerate(values))
            out.append(f'<polyline points="{points}" fill="none" stroke="{ink}" stroke-width="3"/>')
            for i, value in enumerate(values):
                out.append(f'<circle cx="{number(x(i))}" cy="{number(y(value))}" r="3" fill="{ink}"><title>{esc(labels[i])}: {esc(value)}</title></circle>')
        if kind != 'sparkline':
            for i, text in enumerate(labels):
                label(x(i), 229, text)
    return ''.join(out) + '</svg>'


def chart_table(config):
    if config['type'] == 'timeline':
        heads, rows = ['Event', 'Start', 'End'], [[e['label'], e['start'], e['end']] for e in config['events']]
    else:
        heads, rows = ['Label', config.get('unit', 'Value')], zip(config['labels'], config['values'])
    head = ''.join(f'<th scope="col">{esc(value)}</th>' for value in heads)
    body = ''.join('<tr>' + ''.join(f'<td>{esc(value)}</td>' for value in row) + '</tr>' for row in rows)
    return f'<div data-table-wrap><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def cells(line):
    # Pipes in inline code and escaped pipes stay inside the cell.
    result, current, ticks = [], [], 0
    i = 0
    line = line.strip().strip('|')
    while i < len(line):
        if line[i:i+2] == '\\|':
            current.append('\\|')
            i += 2
            continue
        if line[i] == '`':
            end = i
            while end < len(line) and line[end] == '`':
                end += 1
            count = end - i
            ticks = 0 if ticks == count else (count if not ticks else ticks)
            current.append(line[i:end])
            i = end
            continue
        if line[i] == '|' and not ticks:
            result.append(''.join(current).strip())
            current = []
        else:
            current.append(line[i])
        i += 1
    return result + [''.join(current).strip()]


HEADING = re.compile(r'^(#{1,6})\s+(.+?)(?:\s+#+)?$')
FENCE = re.compile(r'^\s{0,3}(`{3,}|~{3,})(.*)$')
LIST = re.compile(r'^( *)([-+*]|\d+[.)])\s+(.*)$')


class Markdown:
    def __init__(self, mermaid=False):
        self.mermaid = mermaid
        self.ids = {'artifact-top', 'artifact-content'}
        self.headings = []
        self.serial = 0
        self.has_h1 = False

    def identity(self, value):
        normalized = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode()
        stem = re.sub(r'[^a-z0-9]+', '-', normalized.lower()).strip('-') or 'section'
        result, suffix = stem, 2
        while result in self.ids:
            result = f'{stem}-{suffix}'
            suffix += 1
        self.ids.add(result)
        return result

    def extension(self, kind, label, body):
        if kind in {'callout', 'tldr'}:
            title = label or ('TL;DR' if kind == 'tldr' else 'Note')
            return f'<aside class="callout"><strong>{esc(title)}</strong>{self.render(body)}</aside>'
        if kind == 'details':
            return f'<details data-collapsible data-print-expand><summary>{inline(label or "Details")}</summary>{self.render(body)}</details>'
        if kind == 'tabs':
            parts, fence, content = [''], None, []
            for line in body.splitlines():
                marker = FENCE.match(line)
                if fence:
                    if re.fullmatch(r'\s{0,3}' + re.escape(fence[0]) + '{' + str(len(fence)) + r',}\s*', line):
                        fence = None
                elif marker:
                    fence = marker[1]
                elif re.fullmatch(r'##\s+.+', line):
                    parts[-1] = '\n'.join(content)
                    parts.extend([line[3:].strip(), ''])
                    content = []
                    continue
                content.append(line)
            parts[-1] = '\n'.join(content)
            if parts[0].strip() or len(parts) < 5:
                raise ValueError('tabs needs at least two ## Label sections')
            self.serial += 1
            group = self.identity(f'tabs-{self.serial}')
            buttons, panels = [], []
            for i in range(1, len(parts), 2):
                name, text = parts[i], parts[i+1]
                button = self.identity(f'{group}-tab-{i//2+1}')
                panel = self.identity(f'{group}-panel-{i//2+1}')
                buttons.append(f'<button type="button" id="{button}" data-tab-target="{panel}">{esc(name)}</button>')
                panels.append(f'<section id="{panel}" data-tab-panel tabindex="0"><h3>{inline(name)}</h3>{self.render(text)}</section>')
            return f'<div data-tabs><div class="cluster" data-tab-list aria-label="{esc(label or "Examples")}" hidden>{"".join(buttons)}</div>{"".join(panels)}</div>'
        if kind == 'chart':
            config = json_data(body)
            svg = chart_svg(config)
            return f'<figure data-chart><div class="chart-box" data-chart-output>{svg}</div><figcaption>{esc(config["title"])}{(" · " + esc(config["unit"])) if config.get("unit") else ""}</figcaption>{chart_table(config)}</figure>'
        if kind == 'timeline':
            events = json_data(body)
            if not isinstance(events, list) or not events or any(not isinstance(e, dict) or not all(isinstance(e.get(key), str) and e[key].strip() for key in ('time', 'title')) for e in events):
                raise ValueError('timeline needs a JSON array of time/title/text entries')
            items = ''.join(f'<li><strong>{esc(e["time"])}</strong> — {esc(e["title"])}{("<p>" + inline(str(e["text"])) + "</p>") if e.get("text") else ""}</li>' for e in events)
            return f'<ol class="timeline" aria-label="{esc(label or "Timeline")}">{items}</ol>'
        if kind == 'mermaid':
            note = 'Opt-in renderer selected; source remains the offline fallback.' if self.mermaid else 'Diagram source; runtime rendering is off. Use a Markdown host or explicitly opt in for a disposable preview.'
            opt = ' data-mermaid-opt-in="true"' if self.mermaid else ''
            return f'<figure{opt}><pre class="mermaid"><code>{esc(body)}</code></pre><div data-diagram-output></div><figcaption>{esc(label or "Diagram")} <span data-diagram-status role="status">{note}</span></figcaption></figure>'
        return f'<pre><code class="language-{esc(kind)}">{esc(body)}</code></pre>'

    @staticmethod
    def table_start(lines, i):
        return i+1 < len(lines) and '|' in lines[i] and all(re.fullmatch(r':?-{3,}:?', cell.strip()) for cell in cells(lines[i+1]))

    def starts(self, lines, i):
        line = lines[i]
        return bool(HEADING.match(line) or FENCE.match(line) or LIST.match(line) or line.lstrip().startswith('>') or re.fullmatch(r'\s*(?:---+|\*\*\*+)\s*', line) or self.table_start(lines, i))

    def render(self, text):
        lines, out, i = text.splitlines(), [], 0
        while i < len(lines):
            line = lines[i]
            if not line.strip():
                i += 1
                continue
            fence = FENCE.match(line)
            if fence:
                marker, info = fence.groups()
                end = i + 1
                close = re.compile(r'^\s{0,3}' + re.escape(marker[0]) + '{' + str(len(marker)) + r',}\s*$')
                while end < len(lines) and not close.fullmatch(lines[end]):
                    end += 1
                if end == len(lines):
                    raise ValueError(f'unclosed fence at line {i+1}')
                pieces = info.strip().split(maxsplit=1)
                kind, label = (pieces + ['', ''])[:2]
                out.append(self.extension(kind, label, '\n'.join(lines[i+1:end])))
                i = end + 1
                continue
            heading = HEADING.match(line)
            if heading:
                hashes, title = heading.groups()
                level = len(hashes)
                self.has_h1 |= level == 1
                identity = self.identity(title)
                self.headings.append((level, title, identity))
                out.append(f'<h{level} id="{identity}">{inline(title)}</h{level}>')
                i += 1
                continue
            if self.table_start(lines, i):
                header, alignment = cells(line), cells(lines[i+1])
                if len(header) != len(alignment):
                    raise ValueError('table header and separator lengths differ')
                heads = ''.join(f'<th scope="col">{inline(cell)}</th>' for cell in header)
                i += 2
                rows = []
                while i < len(lines) and lines[i].strip() and '|' in lines[i]:
                    values = cells(lines[i])
                    if len(values) != len(header):
                        raise ValueError('table row length differs from header')
                    rows.append('<tr>' + ''.join(f'<td>{inline(cell)}</td>' for cell in values) + '</tr>')
                    i += 1
                out.append(f'<div data-table-wrap><table><thead><tr>{heads}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>')
                continue
            if line.lstrip().startswith('>'):
                quote = []
                while i < len(lines) and lines[i].lstrip().startswith('>'):
                    quote.append(re.sub(r'^\s*> ?', '', lines[i]))
                    i += 1
                out.append(f'<blockquote>{self.render(chr(10).join(quote))}</blockquote>')
                continue
            item = LIST.match(line)
            if item:
                indent, marker, _ = item.groups()
                ordered = marker[0].isdigit()
                tag = 'ol' if ordered else 'ul'
                start = f' start="{int(marker[:-1])}"' if ordered else ''
                items = []
                while i < len(lines):
                    item = LIST.match(lines[i])
                    if not item or len(item[1]) != len(indent) or item[2][0].isdigit() != ordered:
                        break
                    width = item.start(3)
                    contents = [item[3]]
                    i += 1
                    while i < len(lines):
                        following = LIST.match(lines[i])
                        if following and len(following[1]) <= len(indent):
                            break
                        if not lines[i].strip():
                            # A blank line belongs to this item only if the next text is indented.
                            if i+1 < len(lines) and len(lines[i+1]) - len(lines[i+1].lstrip()) > len(indent):
                                contents.append('')
                                i += 1
                                continue
                            break
                        if len(lines[i]) - len(lines[i].lstrip()) <= len(indent):
                            break
                        contents.append(lines[i][min(width, len(lines[i])-len(lines[i].lstrip())):])
                        i += 1
                    task = re.match(r'^\[([ xX])\]\s+(.*)$', contents[0])
                    prefix = ''
                    if task:
                        contents[0] = task[2]
                        prefix = f'<input type="checkbox" disabled{" checked" if task[1].lower() == "x" else ""} aria-label="{esc(task[2])}"> '
                    rendered_item = self.render(chr(10).join(contents))
                    if prefix:
                        rendered_item = rendered_item.replace('<p>', '<p class="task-item">' + prefix, 1)
                    items.append(f'<li>{rendered_item}</li>')
                out.append(f'<{tag}{start}>{"".join(items)}</{tag}>')
                continue
            if re.fullmatch(r'\s*(?:---+|\*\*\*+)\s*', line):
                out.append('<hr>')
                i += 1
                continue
            paragraph = [line.strip()]
            i += 1
            while i < len(lines) and lines[i].strip() and not self.starts(lines, i):
                paragraph.append(lines[i].strip())
                i += 1
            out.append(f'<p>{inline(" ".join(paragraph))}</p>')
        return '\n'.join(out)


def asset_script(name):
    text = (ASSETS / name).read_text(encoding='utf-8')
    return '\n'.join(f'<script>{body}</script>' for body in re.findall(r'<script>(.*?)</script>', text, re.S))


def document(text: str, filename: str, mermaid=False) -> str:
    metadata, body = frontmatter(text)
    parser = Markdown(mermaid)
    rendered = parser.render(body)
    title = metadata.get('title') or next((title for level, title, _ in parser.headings if level == 1), Path(filename).stem)
    revision = metadata.get('revision') or hashlib.sha256(text.encode('utf-8')).hexdigest()[:12]
    heading_title = next((value for level, value, _ in parser.headings if level == 1), title)
    visible = {'Source': filename, 'Revision': revision}
    for key, value in metadata.items():
        if key == 'revision' or (key == 'title' and value == heading_title):
            continue
        visible[key] = value
    meta = '<dl class="metadata">' + ''.join(f'<div><dt>{esc(key)}</dt><dd>{esc(value)}</dd></div>' for key, value in visible.items()) + '</dl>'
    index = '<nav aria-label="On this page"><h2>On this page</h2><ul>' + ''.join(f'<li><a href="#{identity}">{inline(title)}</a></li>' for level, title, identity in parser.headings if level > 1) + '</ul></nav>' if any(level > 1 for level, _, _ in parser.headings) else ''
    first_heading = re.search(r'<h1\b.*?</h1>', rendered, re.S)
    heading = first_heading[0] if first_heading else f'<h1>{esc(title)}</h1>'
    if first_heading:
        rendered = rendered[:first_heading.start()] + rendered[first_heading.end():]
    content = heading + meta + index + rendered
    template = (ASSETS / 'base.html').read_text(encoding='utf-8')
    template = re.sub(r'<title>.*?</title>', lambda _: f'<title>{esc(title)}</title>', template, count=1, flags=re.S)
    template = re.sub(r'<!-- qp:content:start -->.*?<!-- qp:content:end -->', lambda _: content, template, count=1, flags=re.S)
    footer = f'<p>Generated from <code>{esc(filename)}</code> · Revision: {esc(revision)} · By <code>ojuiwe</code>. Edit the Markdown source to update this page.</p>'
    if metadata.get('date'):
        footer += f'<p>Source date: <time datetime="{esc(metadata["date"])}">{esc(metadata["date"])}</time></p>'
    template = re.sub(r'<!-- qp:footer:start -->.*?<!-- qp:footer:end -->', lambda _: footer, template, count=1, flags=re.S)
    scripts = '\n'.join(asset_script(name) for name in ('tabs-control.html', 'collapsible-control.html', 'report-control.html'))
    if mermaid:
        template = template.replace('data-artifact-delivery="portable"', 'data-artifact-delivery="connected"', 1)
        scripts += '\n' + asset_script('renderer-control.html')
        template = template.replace('Single HTML file; static data;', 'Single HTML file; opt-in Mermaid 12.1.0 runtime from CDN; static data;')
    template = re.sub(r'<!-- qp:controls:start -->.*?<!-- qp:controls:end -->', lambda _: scripts, template, count=1, flags=re.S)
    if mermaid and 'data-mermaid-opt-in="true"' in rendered:
        template = template.replace("<script>console.log('ready');</script>", '')
    # Copy the shipped QP mark rather than maintaining another generated copy.
    brand = (ASSETS / 'brand.svg').read_text(encoding='utf-8').strip()
    template = re.sub(r'<svg class="brand-logo".*?</svg>', lambda _: brand, template, count=1, flags=re.S)
    return template


def main() -> int:
    args_parser = argparse.ArgumentParser(description=__doc__)
    args_parser.add_argument('source', type=Path)
    args_parser.add_argument('--output', '-o', type=Path, help='Default: source path with .html suffix')
    args_parser.add_argument('--mermaid', action='store_true', help='Explicitly allow the pinned remote renderer for a disposable connected preview')
    args = args_parser.parse_args()
    output = args.output or args.source.with_suffix('.html')
    try:
        if args.source.suffix.lower() not in {'.md', '.markdown'} or output.suffix.lower() != '.html' or output.resolve() == args.source.resolve():
            raise ValueError('source must be Markdown and output a separate .html file')
        html = document(args.source.read_text(encoding='utf-8'), args.source.name, args.mermaid)
        with output.open('w', encoding='utf-8', newline='\n') as handle:
            handle.write(html)
    except (OSError, ValueError, TypeError, KeyError, OverflowError, RecursionError) as error:
        print(f'Cannot generate page: {error}', file=sys.stderr)
        return 1
    print(f'Generated {output} ({len(html.encode("utf-8"))} bytes)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
