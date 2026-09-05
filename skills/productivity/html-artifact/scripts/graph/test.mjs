import { test } from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtemp, writeFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { validate, link } from './model.mjs';
import { renderGraph } from './render.mjs';

export const input = () => ({ title: 'Service relationships', summary: 'Supplied architecture, not a diagnosis.', directed: true, source: { label: 'Accepted design', href: '#evidence' }, elements: [
  { data: { id: 'api', label: 'API' } }, { data: { id: 'db', label: 'Database' } },
  { data: { id: 'write', label: 'writes', source: 'api', target: 'db' } },
] });

test('native elements retain supplied direction and values', () => {
  assert.deepEqual(validate(input()), input());
  const undirected = input(); undirected.directed = false;
  assert.equal(validate(undirected).directed, false);
});

test('invalid identity, missing endpoints and unknown fields fail without inference', () => {
  for (const mutate of [
    (x) => delete x.directed,
    (x) => x.elements.push(x.elements[0]),
    (x) => x.elements[2].data.target = 'missing',
    (x) => x.elements[0].data.label = '',
    (x) => x.elements[0].style = { label: 'invented' },
    (x) => x.score = 99,
  ]) {
    const x = input(); mutate(x); assert.throws(() => validate(x));
  }
});

test('source links reject executable schemes, credentials and disguised network paths', () => {
  for (const href of ['javascript:alert(1)', 'data:text/html,bad', '//other.test', 'https://user:secret@other.test', '\\other', 'https://other.test/\n']) {
    assert.throws(() => link(href), undefined, href);
  }
  for (const href of ['#source', '../evidence/report.html', 'https://example.test/evidence']) assert.equal(link(href), href);
});

test('data is escaped in both HTML and script contexts; output is deterministic', async () => {
  const x = input(); x.title = '</script><script>alert("payload")</script>'; x.elements[0].data.label = '<img src=x onerror=alert(1)>';
  const first = await renderGraph(x);
  const second = await renderGraph(x);
  assert.equal(first, second);
  assert.ok(first.includes('&lt;img src=x onerror=alert(1)&gt;'));
  assert.ok(first.includes('\\u003c/script>'));
  assert.ok(!first.includes('<script>alert("payload")</script>'));
  assert.ok(first.includes('Content-Security-Policy'));
  assert.ok(first.includes('Full text is available below.'));
  assert.ok(first.includes('Embedded runtime SHA-256'));
});

test('full text and legal disclosure survive without enhancement; shell needs one marker', async () => {
  const html = await renderGraph(input());
  assert.ok(html.includes('API → Database: writes'));
  assert.ok(html.includes('Permission is hereby granted'));
  const shell = '<!doctype html><html><body><h1>Owner explanation</h1><!-- QP_GRAPH --></body></html>';
  const embedded = await renderGraph(input(), shell);
  assert.ok(embedded.includes('<h1>Owner explanation</h1>'));
  assert.ok(embedded.includes('<h2>Service relationships</h2>'));
  assert.equal(embedded.match(/<!doctype html>/g).length, 1);
  await assert.rejects(renderGraph(input(), '<html>No marker</html>'));
  await assert.rejects(renderGraph(input(), '<!-- QP_GRAPH --><!-- QP_GRAPH -->'));
});

test('invalid CLI input returns failure and no document bytes', async () => {
  const directory = await mkdtemp(join(tmpdir(), 'qp-graph-'));
  try {
    const path = join(directory, 'input.json'); await writeFile(path, '{}');
    const result = spawnSync(process.execPath, [fileURLToPath(new URL('./render.mjs', import.meta.url)), '--input', path], { encoding: 'utf8' });
    assert.notEqual(result.status, 0); assert.equal(result.stdout, ''); assert.match(result.stderr, /graph renderer/);
  } finally { await rm(directory, { recursive: true, force: true }); }
});
