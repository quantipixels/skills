#!/usr/bin/env node
/** Render a validated data-only graph to a self-contained HTML candidate on stdout. */
import { readFile, stat } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, join, resolve } from 'node:path';
import { parseArgs } from 'node:util';
import { build } from 'esbuild';
import { validate, escapeHtml as h } from './model.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const marker = '<!-- QP_GRAPH -->';
const standaloneCss = 'body { margin: 0; } [data-theme-toggle] { margin: .75rem; } html[data-theme=dark] body { color: #eef3fa; background: #161e29; }';
const policy = "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'";
const css = `
[data-qp-graph] { color: var(--graph-text,#172033); background: var(--graph-bg,#fff); font: 1rem/1.6 system-ui,sans-serif; padding: clamp(1rem,4vw,2.5rem); max-width: 90rem; margin: auto; overflow-wrap: anywhere; }
[data-qp-graph] * { box-sizing: border-box; }
[data-qp-graph] [hidden] { display: none !important; }
[data-qp-graph] :focus-visible { outline: 3px solid #16457a; outline-offset: 3px; }
[data-graph-controls] { display: flex; flex-wrap: wrap; gap: .75rem; align-items: center; }
[data-graph-controls] button, [data-graph-controls] select { font: inherit; min-height: 2.75rem; max-width: 100%; }
[data-graph-view] { width: 100%; height: min(60vh,40rem); min-height: 20rem; border: 1px solid #52687e; margin-top: 1rem; }
[data-qp-graph] a { color: var(--graph-link,#16457a); }
[data-graph-view] { background: #fff; }
html[data-theme=dark] [data-qp-graph] { --graph-text: #eef3fa; --graph-bg: #161e29; --graph-link: #aacff7; }
[data-qp-graph] pre { white-space: pre-wrap; }
@media print { [data-graph-controls], [data-graph-view] { display: none !important; } }
`;

export async function renderGraph(input, shell) {
  const model = validate(input);
  const manifest = JSON.parse(await readFile(join(here, 'package.json'), 'utf8'));
  const cytoscapePackage = JSON.parse(await readFile(join(here, 'node_modules/cytoscape/package.json'), 'utf8'));
  const esbuildPackage = JSON.parse(await readFile(join(here, 'node_modules/esbuild/package.json'), 'utf8'));
  for (const [name, installed] of [['cytoscape', cytoscapePackage], ['esbuild', esbuildPackage]]) {
    if (manifest.dependencies[name] !== installed.version) throw new Error(`${name} differs from the committed pin; run npm ci`);
  }
  const licence = await readFile(join(here, 'node_modules/cytoscape/LICENSE'), 'utf8');
  const bundle = await build({ absWorkingDir: here, entryPoints: ['browser.mjs'], bundle: true, write: false, platform: 'browser', format: 'iife', minify: true, legalComments: 'inline', target: ['es2020'], logLevel: 'silent' });
  const runtime = bundle.outputFiles[0].text.replace(/<\/script/gi, '<\\/script');
  const normalized = JSON.stringify(model);
  const identity = createHash('sha256').update(normalized).digest('hex');
  const runtimeIdentity = createHash('sha256').update(runtime).digest('hex');
  const heading = shell === undefined ? 'h1' : 'h2';
  const subheading = shell === undefined ? 'h2' : 'h3';
  const data = normalized.replace(/</g, '\\u003c').replace(/\u2028/g, '\\u2028').replace(/\u2029/g, '\\u2029');
  const nodes = model.elements.filter(({ data: item }) => item.source === undefined);
  const edges = model.elements.filter(({ data: item }) => item.source !== undefined);
  const labels = new Map(nodes.map(({ data: item }) => [item.id, item.label]));
  const sourceLink = (item) => item.href ? `<a href="${h(item.href)}">${h(item.label)}</a>` : h(item.label);
  const fragment = `<style>${css}</style>
<section data-qp-graph aria-label="${h(model.title)}">
<${heading}>${h(model.title)}</${heading}><p>${h(model.summary)}</p>
<p>Source: ${sourceLink(model.source)}.</p>
<p>${model.directed ? 'Directed relationships: source → target.' : 'Undirected relationships: connected endpoints, no causal direction implied.'} Layout positions are for navigation, not additional evidence.</p>
<div data-graph-controls hidden>
<label>Select a node <select><option value="">All nodes</option>${nodes.map(({ data: item }) => `<option value="${h(item.id)}">${h(item.label)} (${h(item.id)})</option>`).join('')}</select></label>
<button type="button" data-graph-fit>Fit graph</button><button type="button" data-graph-zoom="1.2">Zoom in</button><button type="button" data-graph-zoom="0.8333333333">Zoom out</button>
</div>
<div data-graph-view role="img" aria-label="Interactive graph; full relationships are listed below" hidden></div>
<p data-graph-status role="status" aria-live="polite">Interactive enhancement has not loaded. Full text is available below.</p>
<${subheading}>Nodes</${subheading}><ul>${nodes.map(({ data: item }) => `<li>${sourceLink(item)} <code>${h(item.id)}</code></li>`).join('')}</ul>
<${subheading}>Relationships</${subheading}><ul>${edges.map(({ data: item }) => `<li>${h(labels.get(item.source))} ${model.directed ? '→' : '↔'} ${h(labels.get(item.target))}: ${sourceLink(item)} <code>${h(item.id)}</code> (${h(item.source)} / ${h(item.target)})</li>`).join('') || '<li>No relationships supplied.</li>'}</ul>
<details><summary>Renderer identity and licence</summary><p>Cytoscape ${h(cytoscapePackage.version)}; esbuild ${h(esbuildPackage.version)} (build time). Single HTML; embedded runtime; static data; linked sources only when supplied. No runtime network access is needed.</p><p>Normalized input SHA-256: <code>${identity}</code></p><p>Embedded runtime SHA-256: <code>${runtimeIdentity}</code></p><pre>${h(licence)}</pre></details>
<script type="application/json" data-graph-data>${data}</script>
</section><script>${runtime}</script>`;
  if (shell !== undefined) {
    if (typeof shell !== 'string' || shell.split(marker).length !== 2) throw new Error('the trusted document shell must contain exactly one QP_GRAPH marker');
    return shell.replace(marker, () => fragment);
  }
  const foundation = await readFile(join(here, '../../assets/visual-foundation.css'), 'utf8');
  const theme = await readFile(join(here, '../../assets/theme-control.html'), 'utf8');
  return `<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="${h(policy)}"><title>${h(model.title)}</title><style>${foundation}\n${standaloneCss}</style></head><body>${theme}${fragment}</body></html>\n`;
}

async function main() {
  const { values } = parseArgs({ options: { input: { type: 'string' }, shell: { type: 'string' } }, strict: true });
  if (!values.input) throw new Error('usage: node render.mjs --input graph.json [--shell trusted-owner.html] > candidate.html');
  if ((await stat(values.input)).size > 2 * 1024 * 1024) throw new Error('input exceeds the 2 MiB graph-view limit');
  const raw = await readFile(values.input);
  if (raw.length > 2 * 1024 * 1024) throw new Error('input exceeds the 2 MiB graph-view limit');
  const shell = values.shell ? await readFile(values.shell, 'utf8') : undefined;
  process.stdout.write(await renderGraph(JSON.parse(raw.toString('utf8')), shell));
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  main().catch((error) => { console.error(`graph renderer: ${error.message}`); process.exitCode = 1; });
}
