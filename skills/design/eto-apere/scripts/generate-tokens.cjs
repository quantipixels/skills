#!/usr/bin/env node
/**
 * Generate CSS variables from design tokens JSON
 *
 * Usage:
 *   node generate-tokens.cjs --config tokens.json -o tokens.css
 *   node generate-tokens.cjs --config tokens.json --format tailwind
 */

const fs = require('fs');
const path = require('path');

/**
 * Parse command line arguments
 */
function parseArgs() {
  const args = process.argv.slice(2);
  const options = {
    config: null,
    output: null,
    format: 'css' // css | tailwind
  };

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--config' || args[i] === '-c') {
      options.config = args[++i];
    } else if (args[i] === '--output' || args[i] === '-o') {
      options.output = args[++i];
    } else if (args[i] === '--format' || args[i] === '-f') {
      options.format = args[++i];
    } else if (args[i] === '--help' || args[i] === '-h') {
      console.log(`
Usage: node generate-tokens.cjs [options]

Options:
  -c, --config <file>   Input JSON token file (required)
  -o, --output <file>   Output file (default: stdout)
  -f, --format <type>   Output format: css | tailwind (default: css)
  -h, --help            Show this help
      `);
      process.exit(0);
    }
  }

  return options;
}

const PRIMITIVE_CATEGORY_NAMES = {
  spacing: 'space',
  fontSize: 'font-size',
  fontWeight: 'font-weight',
  fontFamily: 'font-family',
  lineHeight: 'line-height',
};

function toKebab(value) {
  return String(value)
    .replace(/([a-z0-9])([A-Z])/g, '$1-$2')
    .replace(/_/g, '-')
    .toLowerCase();
}

/** Convert a source token path to its canonical CSS custom-property name. */
function toCssVarName(sourcePath) {
  let parts = [...sourcePath];
  if (parts[0] === 'dark') parts = parts.slice(1);

  if (parts[0] === 'primitive') {
    const category = PRIMITIVE_CATEGORY_NAMES[parts[1]] || toKebab(parts[1]);
    parts = [category, ...parts.slice(2)];
  } else if (parts[0] === 'semantic' || parts[0] === 'component') {
    parts = parts.slice(1);
  }

  return '--' + parts.map(toKebab).join('-');
}

function collectTokenNodes(obj, prefix = [], nodes = new Map()) {
  for (const [key, value] of Object.entries(obj || {})) {
    const currentPath = [...prefix, key];
    if (value && typeof value === 'object' && value.$value !== undefined) {
      nodes.set(currentPath.join('.'), value);
    } else if (value && typeof value === 'object') {
      collectTokenNodes(value, currentPath, nodes);
    }
  }
  return nodes;
}

function validateTokenGraph(tokens) {
  const nodes = new Map();
  collectTokenNodes(tokens.primitive, ['primitive'], nodes);
  collectTokenNodes(tokens.semantic, ['semantic'], nodes);
  collectTokenNodes(tokens.component, ['component'], nodes);
  collectTokenNodes(tokens.dark, ['dark'], nodes);

  const names = new Map();
  for (const sourcePath of nodes.keys()) {
    const cssName = toCssVarName(sourcePath.split('.'));
    const normalizedSource = sourcePath.replace(/^dark\./, '');
    if (names.has(cssName) && names.get(cssName) !== normalizedSource) {
      throw new Error(`CSS token name collision: ${sourcePath} and ${names.get(cssName)} -> ${cssName}`);
    }
    names.set(cssName, normalizedSource);
  }

  const visiting = new Set();
  const visited = new Set();
  function visit(sourcePath) {
    if (visited.has(sourcePath)) return;
    if (visiting.has(sourcePath)) throw new Error(`Circular token reference: ${sourcePath}`);
    visiting.add(sourcePath);
    const value = nodes.get(sourcePath)?.$value;
    const match = typeof value === 'string' ? /^\{([^{}]+)\}$/.exec(value) : null;
    if (match) {
      if (!nodes.has(match[1])) throw new Error(`Unresolved token reference: ${value}`);
      visit(match[1]);
    }
    visiting.delete(sourcePath);
    visited.add(sourcePath);
  }
  for (const sourcePath of nodes.keys()) visit(sourcePath);
}

function cssValue(value) {
  const match = typeof value === 'string' ? /^\{([^{}]+)\}$/.exec(value) : null;
  return match ? `var(${toCssVarName(match[1].split('.'))})` : value;
}

/**
 * Flatten tokens into CSS variables
 */
function flattenTokens(obj, prefix = [], result = {}) {
  for (const [key, value] of Object.entries(obj)) {
    const currentPath = [...prefix, key];

    if (value && typeof value === 'object') {
      if (value.$value !== undefined) {
        // This is a token
        const cssVar = toCssVarName(currentPath);
        result[cssVar] = cssValue(value.$value);
      } else {
        // Recurse into nested object
        flattenTokens(value, currentPath, result);
      }
    }
  }

  return result;
}

/**
 * Generate CSS output
 */
function generateCSS(tokens) {
  validateTokenGraph(tokens);
  const primitive = flattenTokens(tokens.primitive || {}, ['primitive']);
  const semantic = flattenTokens(tokens.semantic || {}, ['semantic']);
  const component = flattenTokens(tokens.component || {}, ['component']);
  const darkSemantic = flattenTokens(tokens.dark?.semantic || {}, ['dark', 'semantic']);

  let css = `/* Design Tokens - Auto-generated */
/* Do not edit directly - modify tokens.json instead */

/* === PRIMITIVES === */
:root {
${Object.entries(primitive).map(([k, v]) => `  ${k}: ${v};`).join('\n')}
}

/* === SEMANTIC === */
:root {
${Object.entries(semantic).map(([k, v]) => `  ${k}: ${v};`).join('\n')}
}

/* === COMPONENTS === */
:root {
${Object.entries(component).map(([k, v]) => `  ${k}: ${v};`).join('\n')}
}
`;

  if (Object.keys(darkSemantic).length > 0) {
    css += `
/* === DARK MODE === */
.dark {
${Object.entries(darkSemantic).map(([k, v]) => `  ${k}: ${v};`).join('\n')}
}
`;
  }

  return css;
}

/**
 * Generate Tailwind config output
 */
function generateTailwind(tokens) {
  validateTokenGraph(tokens);
  const semantic = flattenTokens(tokens.semantic || {}, ['semantic']);

  // Extract colors for Tailwind
  const colors = {};
  for (const [key, value] of Object.entries(semantic)) {
    if (key.includes('color')) {
      const name = key.replace('--color-', '').replace(/-/g, '.');
      colors[name] = `var(${key})`;
    }
  }

  return `// Tailwind color config - Auto-generated
// Add to tailwind.config.ts theme.extend.colors

module.exports = {
  colors: ${JSON.stringify(colors, null, 2).replace(/"/g, "'")}
};
`;
}

/**
 * Main
 */
function main() {
  const options = parseArgs();

  if (!options.config) {
    console.error('Error: --config is required');
    process.exit(1);
  }

  // Resolve config path
  const configPath = path.resolve(process.cwd(), options.config);

  if (!fs.existsSync(configPath)) {
    console.error(`Error: Config file not found: ${configPath}`);
    process.exit(1);
  }

  // Read and parse tokens
  const tokens = JSON.parse(fs.readFileSync(configPath, 'utf-8'));

  // Generate output
  let output;
  if (options.format === 'tailwind') {
    output = generateTailwind(tokens);
  } else {
    output = generateCSS(tokens);
  }

  // Write output
  if (options.output) {
    const outputPath = path.resolve(process.cwd(), options.output);
    fs.mkdirSync(path.dirname(outputPath), { recursive: true });
    fs.writeFileSync(outputPath, output);
    console.log(`Generated: ${outputPath}`);
  } else {
    console.log(output);
  }
}

main();
