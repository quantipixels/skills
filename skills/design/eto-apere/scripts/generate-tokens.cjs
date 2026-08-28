#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const input = process.argv[2];
if (!input || process.argv.length !== 3) {
  console.error('usage: node generate-tokens.cjs <tokens.json>');
  process.exit(2);
}

const tokens = JSON.parse(fs.readFileSync(path.resolve(input), 'utf8'));
const CATEGORY = { spacing: 'space', fontSize: 'font-size', fontWeight: 'font-weight', fontFamily: 'font-family', lineHeight: 'line-height' };
const kebab = value => String(value).replace(/([a-z0-9])([A-Z])/g, '$1-$2').replace(/_/g, '-').toLowerCase();

function cssName(source) {
  let parts = [...source];
  if (parts[0] === 'dark') parts = parts.slice(1);
  if (parts[0] === 'primitive') parts = [CATEGORY[parts[1]] || kebab(parts[1]), ...parts.slice(2)];
  else if (parts[0] === 'semantic' || parts[0] === 'component') parts = parts.slice(1);
  return '--' + parts.map(kebab).join('-');
}

function collect(obj, prefix = [], nodes = new Map()) {
  for (const [key, value] of Object.entries(obj || {})) {
    const current = [...prefix, key];
    if (value && typeof value === 'object' && Object.prototype.hasOwnProperty.call(value, '$value')) nodes.set(current.join('.'), value);
    else if (value && typeof value === 'object') collect(value, current, nodes);
  }
  return nodes;
}

const nodes = new Map();
collect(tokens.primitive, ['primitive'], nodes);
collect(tokens.semantic, ['semantic'], nodes);
collect(tokens.component, ['component'], nodes);
collect(tokens.dark, ['dark'], nodes);

const names = new Map();
for (const source of nodes.keys()) {
  const name = cssName(source.split('.'));
  const normalized = source.replace(/^dark\./, '');
  if (names.has(name) && names.get(name) !== normalized) throw new Error(`CSS token name collision: ${source} and ${names.get(name)} -> ${name}`);
  names.set(name, normalized);
}

const visiting = new Set(), visited = new Set();
function visit(source) {
  if (visited.has(source)) return;
  if (visiting.has(source)) throw new Error(`Circular token reference: ${source}`);
  visiting.add(source);
  const value = nodes.get(source)?.$value;
  const ref = typeof value === 'string' ? /^\{([^{}]+)\}$/.exec(value) : null;
  if (ref) {
    if (!nodes.has(ref[1])) throw new Error(`Unresolved token reference: ${value}`);
    visit(ref[1]);
  }
  visiting.delete(source);
  visited.add(source);
}
for (const source of nodes.keys()) visit(source);

const cssValue = value => {
  const ref = typeof value === 'string' ? /^\{([^{}]+)\}$/.exec(value) : null;
  return ref ? `var(${cssName(ref[1].split('.'))})` : String(value);
};

function flatten(obj, prefix = [], result = {}) {
  for (const [key, value] of Object.entries(obj || {})) {
    const current = [...prefix, key];
    if (value && typeof value === 'object' && Object.prototype.hasOwnProperty.call(value, '$value')) result[cssName(current)] = cssValue(value.$value);
    else if (value && typeof value === 'object') flatten(value, current, result);
  }
  return result;
}

const emit = vars => Object.entries(vars).map(([key, value]) => `  ${key}: ${value};`).join('\n');
const primitive = flatten(tokens.primitive, ['primitive']);
const semantic = flatten(tokens.semantic, ['semantic']);
const component = flatten(tokens.component, ['component']);
const dark = flatten(tokens.dark?.semantic, ['dark', 'semantic']);

let css = '/* Generated from canonical design tokens. */\n:root {\n' + emit({ ...primitive, ...semantic, ...component }) + '\n}\n';
if (Object.keys(dark).length) css += '\n.dark {\n' + emit(dark) + '\n}\n';
process.stdout.write(css);
