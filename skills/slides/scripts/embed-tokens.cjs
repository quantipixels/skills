#!/usr/bin/env node
/**
 * embed-tokens.cjs
 * Reads project assets/design-tokens.css and outputs embeddable inline CSS.
 * Use for standalone HTML slide artifacts owned by the slides skill.
 *
 * Usage:
 *   node embed-tokens.cjs           # Output full CSS
 *   node embed-tokens.cjs --minimal # Output only commonly used tokens
 *   node embed-tokens.cjs --style   # Wrap in <style> tags
 */

const fs = require('fs');
const path = require('path');

function findProjectRoot(startDir) {
  let dir = startDir;
  while (dir !== path.dirname(dir)) {
    if (fs.existsSync(path.join(dir, 'assets', 'design-tokens.css'))) return dir;
    dir = path.dirname(dir);
  }
  return null;
}

const projectRoot = findProjectRoot(process.cwd());
if (!projectRoot) {
  console.error('Error: Could not find assets/design-tokens.css');
  process.exit(1);
}

const tokensPath = path.join(projectRoot, 'assets', 'design-tokens.css');
const MINIMAL_TOKENS = [
  '--space-', '--font-size-', '--font-weight-', '--font-family-',
  '--line-height-', '--radius-', '--shadow-', '--gradient-', '--duration-', '--easing-',
  '--color-primary',
  '--color-secondary', '--color-accent', '--color-background', '--color-surface',
  '--color-foreground', '--color-border', '--card-', '--button-', '--slide-',
];

function extractTokens(css, minimal = false) {
  const rootMatches = css.match(/:root\s*\{([^}]+)\}/g);
  if (!rootMatches) return '';
  let variables = [];
  for (const block of rootMatches) {
    variables = variables.concat(block.match(/--[\w-]+:\s*[^;]+;/g) || []);
  }
  if (minimal) variables = variables.filter(variable => MINIMAL_TOKENS.some(token => variable.includes(token)));
  variables = [...new Set(variables)];
  return `:root {\n  ${variables.join('\n  ')}\n}`;
}

const args = process.argv.slice(2);
const minimal = args.includes('--minimal');
const wrapStyle = args.includes('--style');

try {
  const css = fs.readFileSync(tokensPath, 'utf-8');
  let output = extractTokens(css, minimal);
  output = wrapStyle
    ? `<style>\n/* Design Tokens (embedded for standalone HTML) */\n${output}\n</style>`
    : `/* Design Tokens (embedded for standalone HTML) */\n${output}`;
  console.log(output);
} catch (err) {
  console.error(`Error reading tokens: ${err.message}`);
  process.exit(1);
}
