#!/usr/bin/env python3
"""Read-only structural diagnostics for one HTML artifact; not a security audit."""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Document(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[tuple[str, dict, int]] = []
        self.scripts: list[tuple[dict, str, int]] = []
        self.styles: list[str] = []
        self.titles: list[str] = []
        self.capture = None

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        self.tags.append((tag, values, self.getpos()[0]))
        if tag in {'script', 'style', 'title'}:
            self.capture = (tag, values, self.getpos()[0], [])

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data):
        if self.capture:
            self.capture[3].append(data)

    def handle_endtag(self, tag):
        if not self.capture or tag != self.capture[0]:
            return
        kind, attrs, line, pieces = self.capture
        text = ''.join(pieces)
        if kind == 'script':
            self.scripts.append((attrs, text, line))
        elif kind == 'style':
            self.styles.append(text)
        else:
            self.titles.append(text)
        self.capture = None


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON key: {key}')
        result[key] = value
    return result


def inspect_html(text: str, require_manifest: bool = False) -> dict:
    doc = Document()
    doc.feed(text)
    diagnostics = []

    def emit(level, code, message, line=None):
        diagnostics.append(dict(level=level, code=code, message=message, line=line))

    roots = [attrs for tag, attrs, _ in doc.tags if tag == 'html']
    if len(roots) != 1 or not nonempty(roots[0].get('lang')):
        emit('ERROR', 'language', 'Expected one html element with a nonempty lang.')
    if len(doc.titles) != 1 or not doc.titles[0].strip():
        emit('ERROR', 'title', 'Expected one nonempty title.')
    if not any(tag == 'meta' and (attrs.get('name') or '').lower() == 'viewport' and nonempty(attrs.get('content')) for tag, attrs, _ in doc.tags):
        emit('ERROR', 'viewport', 'Missing nonempty viewport metadata.')

    ids = Counter(attrs['id'] for _, attrs, _ in doc.tags if attrs.get('id'))
    for identity, count in ids.items():
        if count > 1:
            emit('ERROR', 'duplicate-id', f'ID {identity!r} occurs {count} times.')
    for _, attrs, line in doc.tags:
        href = attrs.get('href') or ''
        targets = [unquote(href[1:])] if href.startswith('#') and len(href) > 1 else []
        for attribute in ('aria-controls', 'aria-labelledby', 'aria-describedby'):
            targets.extend((attrs.get(attribute) or '').split())
        if attrs.get('data-view-target'):
            targets.append(attrs['data-view-target'])
        for target in targets:
            if target not in ids:
                emit('ERROR', 'missing-target', f'Target {target!r} is not present.', line)

    profile = roots[0].get('data-artifact-delivery', 'portable') if roots else 'portable'
    if profile not in {'portable', 'connected', 'host'}:
        emit('ERROR', 'delivery', f'Unknown delivery profile: {profile!r}.')
    manifests = [(attrs, body, line) for attrs, body, line in doc.scripts if attrs.get('id') == 'qp-artifact-manifest']
    manifest = None
    if len(manifests) > 1:
        emit('ERROR', 'manifest-count', 'Only one artifact manifest is allowed.')
    if require_manifest and not manifests:
        emit('ERROR', 'manifest-missing', 'The caller required a manifest.')
    if manifests:
        attrs, body, line = manifests[0]
        try:
            if attrs.get('type') != 'application/json':
                raise ValueError('manifest must have type application/json')
            value = json.loads(body, object_pairs_hook=unique_object)
            if not isinstance(value, dict):
                raise ValueError('manifest must be an object')
            if type(value.get('schemaVersion')) is not int or value['schemaVersion'] != 1:
                raise ValueError('unsupported schemaVersion')
            if not all(nonempty(value.get(key)) for key in ('artifactId', 'revision')):
                raise ValueError('artifactId and revision must be nonempty strings')
            if value.get('delivery') not in {'portable', 'connected', 'host'}:
                raise ValueError('invalid delivery')
            if roots and roots[0].get('data-artifact-delivery') and value['delivery'] != profile:
                raise ValueError('manifest and html delivery profiles disagree')
            if value.get('interactionState') not in {'transient', 'persistent'}:
                raise ValueError('invalid interactionState')
            for field, keys in [('sourceCut', ('id', 'revision')), ('dependencies', ('name', 'version', 'url'))]:
                entries = value.get(field)
                if not isinstance(entries, list) or any(not isinstance(entry, dict) or not all(nonempty(entry.get(key)) for key in keys) for entry in entries):
                    raise ValueError(f'{field} must contain objects with {keys}')
            manifest = value
            profile = value['delivery']
            if value['interactionState'] == 'persistent':
                emit('REVIEW', 'state-authority', 'Confirm the explicit persistence request, lifetime and reset contract.', line)
        except (ValueError, TypeError) as error:
            emit('ERROR', 'manifest-invalid', str(error), line)

    remote = []
    for tag, attrs, line in doc.tags:
        urls = []
        if tag in {'script', 'img', 'iframe', 'audio', 'video', 'source', 'embed', 'input'}:
            urls.append(attrs.get('src') or '')
        if tag == 'object':
            urls.append(attrs.get('data') or '')
        if tag == 'link' and set((attrs.get('rel') or '').lower().split()) & {'stylesheet', 'icon', 'preload', 'modulepreload'}:
            urls.append(attrs.get('href') or '')
        for url in filter(None, urls):
            try:
                parsed = urlsplit(url)
            except ValueError:
                emit('ERROR', 'resource-url', 'Malformed active resource URL.', line)
                continue
            if parsed.scheme in {'http', 'https'} or url.startswith('//'):
                remote.append(url)
                if profile == 'portable':
                    emit('ERROR', 'portable-remote', f'Portable artifact actively references {url!r}.', line)
            elif parsed.scheme == 'file' or re.match(r'^[A-Za-z]:[\\/]', url):
                emit('ERROR', 'machine-path', 'Active resource uses a machine-specific absolute path.', line)
            elif profile == 'portable' and url.startswith('/'):
                emit('ERROR', 'portable-root-path', 'Portable artifact uses a root-relative resource.', line)
        if attrs.get('srcset'):
            emit('REVIEW', 'srcset', 'Inspect responsive resource URLs; srcset is outside this URL parser.', line)
    if manifest:
        declared = {dep['url'] for dep in manifest['dependencies']}
        for url in remote:
            if url not in declared:
                emit('REVIEW', 'undeclared-resource', f'Remote resource is not declared: {url!r}.')
    for css in doc.styles:
        if re.search(r'(?:url\(|@import)[^;{}]*(?:https?:|//)', css, re.I):
            emit('REVIEW', 'css-resource', 'Inspect CSS remote resource use and offline claims.')
    for attrs, body, line in doc.scripts:
        if (attrs.get('type') or '').lower() in {'application/json', 'application/ld+json'}:
            continue
        if re.search(r'\b(?:localStorage|sessionStorage|indexedDB)\b|document\s*\.\s*cookie|history\s*\.\s*(?:pushState|replaceState)\s*\(', body):
            emit('REVIEW', 'state-api', 'Inline code mentions a state API; inspect execution and authority. This is not proof of a write.', line)
        if re.search(r'\b(?:fetch|WebSocket|EventSource)\s*\(|sendBeacon\s*\(', body):
            emit('REVIEW', 'network-api', 'Inspect the inline runtime data/connection boundary.', line)
    return dict(ok=not any(item['level'] == 'ERROR' for item in diagnostics), diagnostics=diagnostics,
                explicitRemoteResources=sorted(set(remote)),
                coverage='Structural checks only. Dynamic code/imports, CSS, factual truth, visual quality, accessibility and no-save behaviour require separate inspection/proof.')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('artifact', type=Path)
    parser.add_argument('--require-manifest', action='store_true')
    parser.add_argument('--json', action='store_true', dest='as_json')
    args = parser.parse_args()
    try:
        result = inspect_html(args.artifact.read_text(encoding='utf-8'), args.require_manifest)
    except (OSError, UnicodeError, ValueError) as error:
        print(json.dumps(dict(ok=False, error=str(error))))
        return 2
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print('Structural checks passed.' if result['ok'] else 'Structural checks failed.')
        for item in result['diagnostics']:
            print(f'{item["level"]} {item["code"]} (line {item["line"] or "?"}): {item["message"]}')
        print(result['coverage'])
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
