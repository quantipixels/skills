#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const HELP = `Usage:
  node generate-tokens.cjs <tokens.json>
  node generate-tokens.cjs --config <tokens.json> [--output <file>] [--format css|tailwind]

The positional input and CSS on stdout are the current interface.
--config, --output, and --format tailwind are compatibility options for one release.`;

function fail(message) {
  console.error(`Error: ${message}\n\n${HELP}`);
  process.exit(2);
}

function parseArgs(args) {
  const options = { input: null, output: null, format: 'css', legacy: false, help: false };
  for (let index = 0; index < args.length; index += 1) {
    const arg = args[index];
    if (arg === '--help' || arg === '-h') {
      options.help = true;
    } else if (arg === '--config' || arg === '-c') {
      if (!args[index + 1]) fail(`${arg} requires a file`);
      if (options.input) fail('input was supplied more than once');
      options.input = args[++index];
      options.legacy = true;
    } else if (arg === '--output' || arg === '-o') {
      if (!args[index + 1]) fail(`${arg} requires a file`);
      options.output = args[++index];
      options.legacy = true;
    } else if (arg === '--format' || arg === '-f') {
      if (!args[index + 1]) fail(`${arg} requires css or tailwind`);
      options.format = args[++index];
      options.legacy = true;
    } else if (arg.startsWith('-')) {
      fail(`unknown option: ${arg}`);
    } else if (options.input) {
      fail('input was supplied more than once');
    } else {
      options.input = arg;
    }
  }
  if (options.help) return options;
  if (!options.input) fail('a token input file is required');
  if (!['css', 'tailwind'].includes(options.format)) fail(`unsupported format: ${options.format}`);
  return options;
}

const options = parseArgs(process.argv.slice(2));
if (options.help) {
  process.stdout.write(`${HELP}\n`);
  process.exit(0);
}
if (options.legacy) console.error('Deprecated: use positional input and redirect CSS stdout; legacy flags remain for one release.');

let tokens;
try {
  tokens = JSON.parse(fs.readFileSync(path.resolve(options.input), 'utf8'));
} catch (error) {
  fail(error.message);
}
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
    if (cssName(source.split('.')) === cssName(ref[1].split('.'))) {
      throw new Error(`Self-referential emitted CSS alias: ${source} -> ${ref[1]}`);
    }
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

function generateTailwind() {
  const colors = {};
  for (const key of Object.keys(semantic)) {
    if (key.includes('color')) colors[key.replace('--color-', '').replace(/-/g, '.')] = `var(${key})`;
  }
  return `// Deprecated compatibility output. Map the emitted CSS variables in the current project instead.\nmodule.exports = {\n  colors: ${JSON.stringify(colors, null, 2).replace(/"/g, "'")}\n};\n`;
}

const result = options.format === 'tailwind' ? generateTailwind() : css;
if (options.output) {
  const output = path.resolve(options.output);
  fs.mkdirSync(path.dirname(output), { recursive: true });
  fs.writeFileSync(output, result);
  process.stdout.write(`Generated: ${output}\n`);
} else {
  process.stdout.write(result);
}
