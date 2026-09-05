/** A bounded, data-only subset of Cytoscape elements; no semantic inference. */
export function text(value, name) {
  if (typeof value !== 'string' || !value.trim()) throw new Error(`${name} must be non-empty text`);
  return value;
}

export function link(value) {
  if (value === undefined) return undefined;
  text(value, 'source link');
  if (/[\u0000-\u0020\u007f\\]/u.test(value) || value.startsWith('//')) {
    throw new Error('source links cannot contain whitespace, controls, or backslashes');
  }
  const url = new URL(value, 'https://qp-artifact.invalid/');
  if (!['http:', 'https:'].includes(url.protocol) || url.username || url.password) {
    throw new Error('source links must be HTTP(S), relative, or fragment references without credentials');
  }
  return value;
}

function object(value, name) {
  if (!value || typeof value !== 'object' || Array.isArray(value)) throw new Error(`${name} must be an object`);
  return value;
}

function knownKeys(value, keys, name) {
  for (const key of Object.keys(value)) {
    if (!keys.includes(key)) throw new Error(`unsupported ${name} field: ${key}`);
  }
}

export function validate(input) {
  object(input, 'graph');
  knownKeys(input, ['title', 'summary', 'directed', 'source', 'elements'], 'graph');
  const title = text(input.title, 'title');
  const summary = text(input.summary, 'summary');
  if (typeof input.directed !== 'boolean') throw new Error('directed must explicitly be true or false');
  const source = object(input.source, 'source');
  knownKeys(source, ['label', 'href'], 'source');
  const evidence = { label: text(source.label, 'source.label'), href: link(source.href) };
  if (!Array.isArray(input.elements) || !input.elements.length || input.elements.length > 2000) {
    throw new Error('supply 1–2000 elements; split larger views or select another renderer');
  }
  const ids = new Set();
  const elements = input.elements.map((element) => {
    object(element, 'element');
    knownKeys(element, ['data'], 'element');
    const data = object(element.data, 'element.data');
    knownKeys(data, ['id', 'label', 'source', 'target', 'href'], 'element.data');
    const id = text(data.id, 'element id');
    if (ids.has(id)) throw new Error(`duplicate element id: ${id}`);
    ids.add(id);
    const result = { id, label: text(data.label, 'element label') };
    if (data.source !== undefined || data.target !== undefined) {
      result.source = text(data.source, 'edge source');
      result.target = text(data.target, 'edge target');
    }
    if (data.href !== undefined) result.href = link(data.href);
    return { data: result };
  });
  const nodes = new Set(elements.filter((element) => element.data.source === undefined).map((element) => element.data.id));
  if (!nodes.size) throw new Error('graph must contain a node');
  for (const { data } of elements) {
    if (data.source !== undefined && (!nodes.has(data.source) || !nodes.has(data.target))) {
      throw new Error(`edge ${data.id} references a missing node`);
    }
  }
  // Stable input order is retained. Layout position has no additional semantic meaning.
  return { title, summary, directed: input.directed, source: evidence, elements };
}

export function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char]));
}
