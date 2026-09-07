"""One-time migration for the approved #111 candidate; removes itself."""
from pathlib import Path
import shutil
import json
import re
import subprocess
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path.cwd()
assert (ROOT / '.git').exists()
assert subprocess.check_output(['git', 'branch', '--show-current'], text=True).strip() == 'greenfield-focused-skills'
assert (ROOT / 'skills/engineering/ko-skill/SKILL.md').is_file(), 'Candidate is already migrated or has a different layout'
INPUT = ROOT / '.github/greenfield/out'
DATA = {str(p.relative_to(INPUT)): {'text': p.read_text(encoding='utf-8'), 'mode': p.stat().st_mode & 0o777}
        for p in INPUT.rglob('*') if p.is_file()}
Path('/tmp/qp-final-validate.yml').write_text(DATA['.github/workflows/validate.yml']['text'], encoding='utf-8')


def put(path):
    file = ROOT / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(DATA[path]['text'], encoding='utf-8')
    file.chmod(DATA[path]['mode'])


def edit(path, old, new, count=-1):
    file = ROOT / path
    text = file.read_text(encoding='utf-8')
    assert old in text, f'Missing transformation anchor: {path}: {old[:100]}'
    file.write_text(text.replace(old, new, count), encoding='utf-8')


def commit(message):
    subprocess.run(['git', 'add', '-A'], check=True)
    subprocess.run(['git', 'diff', '--cached', '--check'], check=True)
    assert not subprocess.check_output(['git', 'diff', '--cached', '--name-only', '--', '.github/workflows'], text=True).strip(), 'Workflow edits remain for the final connector commit'
    subprocess.run(['git', 'commit', '-m', message], check=True)


original = []
experimental = []
for group in ('engineering', 'design', 'productivity', 'experimental'):
    directory = ROOT / 'skills' / group
    if not directory.exists():
        continue
    for skill in sorted(directory.iterdir()):
        assert skill.is_dir() and (skill / 'SKILL.md').is_file(), skill
        target = ROOT / 'skills' / skill.name
        assert not target.exists(), target
        original.append(skill.name)
        if group == 'experimental': experimental.append(skill.name)
        skill.rename(target)
    directory.rmdir()
assert len(original) == 39 and len(set(original)) == len(original)

url = re.compile(r'https?://[^\s<>"\x27`)]+')
for file in ROOT.rglob('*'):
    if not file.is_file() or '.git' in file.parts or file.name == 'CHANGELOG.md': continue
    if file.is_relative_to(ROOT / '.github/workflows') or file.is_relative_to(ROOT / '.github/greenfield'): continue
    if file.suffix not in {'.md', '.py', '.yml', '.yaml', '.json', '.sh', '.html', '.toml', '.txt'}: continue
    text = file.read_text(encoding='utf-8')
    urls = []
    def protect(match):
        urls.append(match.group()); return f'__QP_SOURCE_URL_{len(urls)-1}__'
    revised = url.sub(protect, text)
    revised = re.sub(r'skills/(engineering|design|productivity|experimental)/', 'skills/', revised)
    for index, value in enumerate(urls): revised = revised.replace(f'__QP_SOURCE_URL_{index}__', value)
    if revised != text: file.write_text(revised, encoding='utf-8')

for name in experimental:
    path = ROOT / 'skills' / name / 'SKILL.md'
    text = path.read_text(encoding='utf-8')
    header, body = text.split('---', 2)[1:]
    assert '\nmetadata:' not in header, name
    path.write_text('---' + header + 'metadata:\n  maturity: experimental\n---' + body, encoding='utf-8')

plugin = ROOT / '.claude-plugin/plugin.json'
manifest = json.loads(plugin.read_text())
manifest.pop('skills', None)
plugin.write_text(json.dumps(manifest, indent=2) + '\n')

meta = ROOT / 'skills/ko-skill/scripts/package_metadata.py'
meta.write_text(meta.read_text() + '''\n\ndef skill_directories(repo: Path) -> list[Path]:
    """The native skills directory is the single discovery source."""
    root = repo / "skills"
    return sorted(p for p in root.iterdir() if p.is_dir() and p.name != "__pycache__") if root.is_dir() else []
''')
vp = 'skills/ko-skill/scripts/validate-package.py'
edit(vp, 'from package_metadata import UniqueKeyLoader, read_frontmatter', 'from package_metadata import UniqueKeyLoader, read_frontmatter, skill_directories')
edit(vp, 'GROUPS = ("engineering", "design", "productivity", "experimental")\n', '')
edit(vp, 'if len(relative_dir.parts) != 3 or relative_dir.parts[:1] != ("skills",) or relative_dir.parts[1] not in GROUPS:', 'if len(relative_dir.parts) != 2 or relative_dir.parts[:1] != ("skills",):')
edit(vp, 'skill must be directly under one canonical group', 'skill must be directly under skills/')
file = ROOT / vp
text = file.read_text()
start, end = text.index('def inventory('), text.index('\ndef main()')
text = text[:start] + '''def inventory(repo: Path) -> list[Path]:
    return [p for p in skill_directories(repo) if (p / "SKILL.md").is_file()]


def validate_inventory(repo: Path, skills: list[Path]) -> list[Finding]:
    expected = {path / "SKILL.md" for path in skills}
    findings = []
    for path in (repo / "skills").rglob("SKILL.md"):
        if "__pycache__" not in path.parts and path not in expected:
            findings.append(Finding("skill.layout", str(path.relative_to(repo)), "entrypoint must use skills/<name>/SKILL.md"))
    for directory in skill_directories(repo):
        if not (directory / "SKILL.md").is_file():
            findings.append(Finding("skill.missing", str(directory.relative_to(repo)), "missing SKILL.md"))
    return findings


def validate_manifest(repo: Path, skills: list[Path]) -> list[Finding]:
    path = repo / ".claude-plugin" / "plugin.json"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        return [Finding("manifest.invalid", str(path.relative_to(repo)), str(error))]
    if not isinstance(manifest, dict):
        return [Finding("manifest.invalid", str(path.relative_to(repo)), "manifest must be an object")]
    if manifest.get("skills", "./skills") not in ("./skills", ["./skills"]):
        return [Finding("manifest.inventory", str(path.relative_to(repo)), "use native skills/ discovery instead of a second inventory")]
    return []

''' + text[end:]
file.write_text(text)
vpa = 'skills/ko-skill/scripts/validate-plugin-agents.py'
edit(vpa, 'from package_metadata import read_frontmatter', 'from package_metadata import read_frontmatter, skill_directories')
edit(vpa, 'GROUPS = ("engineering", "design", "productivity", "experimental")\n', '')
file = ROOT / vpa
text = file.read_text()
start, end = text.index('    for group in GROUPS:'), text.index('    return result', text.index('def skill_metadata'))
text = text[:start] + '''    for skill_dir in skill_directories(repo):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            continue
        metadata = read_frontmatter(skill_file)
        name = metadata.get("name")
        if isinstance(name, str):
            if name in result:
                raise ValueError(f"duplicate public skill identity {name!r}")
            result[name] = (skill_dir, metadata)
''' + text[end:]
file.write_text(text)

for name in ('scripts/install.sh', 'scripts/uninstall.sh', 'scripts/distribution.py', 'scripts/test_distribution.py',
             '.github/tests/test_package_integrity.py', 'AGENTS.md', 'README.md'):
    put(name)
for name in ('scripts/test_install.py', 'scripts/test_uninstall.py'):
    (ROOT / name).unlink(missing_ok=True)
shutil.rmtree(ROOT / '.github/greenfield')
edit('.github/tests/test_validate_workflow.py', 'scripts/test_uninstall.py', 'scripts/test_distribution.py')
for file in (ROOT / 'skills/ko-skill/references').glob('*.md'):
    text = file.read_text().replace('`skills/experimental`', '`metadata.maturity: experimental`')
    file.write_text(text)
for name in ('embed-html-artifact-logo', 'focused-initiative-composition', 'guard-global-cleanup', 'native-skills-installer',
             'skill-composition-by-reference', 'standalone-artifact-branding'):
    (ROOT / '.changeset' / (name + '.md')).unlink(missing_ok=True)
(ROOT / '.changeset/greenfield-skill-library.md').write_text('''---
"qp-skills": major
---

Use one flat native-discovery skill library with optional Pepeye. Preserve all specialist resources and skill names, compose skills directly, make ordinary planning and persistence proportional, and replace third-party installer ownership coupling with verified QP snapshots and exact host links. Existing native-manager installations require explicit migration; source paths change without changing skill invocations.
''')
commit('refactor!: use native skill discovery and ownership-safe snapshot installation')

atona = ROOT / 'skills/atona/SKILL.md'
formal = atona.read_text().split('---', 2)[2]
formal = re.sub(r'\]\(references/([^)]*)\)', r'](\1)', formal)
formal = formal.replace('](templates/', '](../templates/')
(ROOT / 'skills/atona/references/managed-initiative.md').write_text('''# Managed initiative lifecycle

Use this branch only when the governing workflow needs named readiness states, coordinated multi-candidate delivery, or a maintained lifecycle record. Ordinary plans use the main skill directly. These gates preserve formal consumers; they are not mandatory stages of every task.
''' + formal)
for name in ('skills/atona/SKILL.md', 'skills/alarina/SKILL.md', 'skills/scope-guard/SKILL.md',
             'agents/pepeye.md', 'agents/codex/pepeye.config.toml', 'docs/verification.md', 'docs/compatibility.md'):
    put(name)
edit('skills/akosile/SKILL.md', '# Akọsílẹ̀\n', '# Akọsílẹ̀\n\nUse this workspace only when shared repository state or protected concurrent publication is actually needed and selected. Ordinary plans, reviews, and artifacts can stay in the conversation or an existing project destination. Do not create `.qp` merely because another skill contributes to the task.\n', 1)
edit('skills/alaga/SKILL.md', 'Respect explicit owner/tool choices and consume another owner\'s result only when delivery actually depends on an independently useful decision, architecture, specification, diagnosis, or lifecycle result.', 'Respect explicit choices and use relevant skills when they improve delivery. Preserve a distinct decision, architecture, specification, diagnosis, or review result when the job actually depends on it.')
expert = ROOT / 'skills/alaga/references/expert-implementation-counsel.md'
text = expert.read_text()
start = text.index('Before independent review, compare')
expert.write_text(text[:start] + 'Apply relevant counsel as implementation changes. Resolve material evidence gaps that can still change code or proof before independent review; do not create a separate counsel ledger or classify every ordinary implementation choice.\n')

for file in list((ROOT / 'docs').rglob('*')):
    if file.is_file() and 'adr' not in file.relative_to(ROOT / 'docs').parts and file.name not in {'compatibility.md', 'verification.md'}:
        file.unlink()
for directory in sorted((ROOT / 'docs').rglob('*'), reverse=True):
    if directory.is_dir() and not any(directory.iterdir()): directory.rmdir()
for file in (ROOT / 'skills').rglob('*.md'):
    text = file.read_text()
    for path in ('docs/executable-proof.md', 'docs/release-stabilization.md'):
        text = text.replace(path, 'docs/verification.md')
    file.write_text(text)
assert sorted(p.name for p in (ROOT / 'skills').iterdir() if p.is_dir()) == sorted(original)
assert (ROOT / 'skills/arojinle/SKILL.md').read_text().count('Use `amose`.') == 1
commit('refactor(skills): focus ordinary plans and compose expertise without ceremony')

brand_url = 'https://quantipixels.com/assets/brand/logo-full-white.svg'
try:
    request = urllib.request.Request(brand_url, headers={'User-Agent': 'QP-skills-candidate-review'})
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read(1_000_001)
    assert len(raw) <= 1_000_000
    svg = raw.decode('utf-8')
    tree = ET.fromstring(svg)
    assert tree.tag.endswith('svg') and tree.get('viewBox')
    assert not re.search(r'<script|\son[a-z]+\s*=|(?:href|src)\s*=|<!ENTITY|<!DOCTYPE', svg, re.I)
    svg = re.sub(r'(fill|stroke)=("|\')(?i:#fff(?:fff)?|white)\2', r'\1="currentColor"', svg)
    svg = re.sub(r'<\?xml[^>]*>\s*', '', svg).strip()
    svg = re.sub(r'\s(?:role|aria-label)="[^"]*"', '', svg)
    svg = re.sub(r'<svg\b', '<svg role="img" aria-label="Quanti Pixels"', svg, count=1)
    assert 'fill="currentColor"' in svg
    asset = ROOT / 'skills/html-artifact/assets/base.html'
    template, count = re.subn(r'(<div class="artifact-brand">\s*)<svg\b.*?</svg>', lambda m: m[1] + svg, asset.read_text(), count=1, flags=re.S)
    assert count == 1
    test = ROOT / '.github/browser/test_controls.py'
    proof = test.read_text().replace("self.assertAlmostEqual(box['width'] / box['height'], 500 / 132, places=2)",
                                    "view = [float(v) for v in logo.get_attribute('viewBox').replace(',', ' ').split()]\n            self.assertAlmostEqual(box['width'] / box['height'], view[2] / view[3], places=2)")
    proof = proof.replace("page.locator('.artifact-brand text')", "page.locator('.artifact-brand [fill=\"currentColor\"]').first")
    proof = proof.replace("        expect(page.locator('.artifact-brand g[stroke]')).to_have_css('stroke', 'rgb(17, 17, 17)')\n", '')
    anchor = '    def test_base_template_opens_alone_without_javascript_or_companions(self):'
    assert anchor in proof
    proof = proof.replace(anchor, "    def test_embedded_wordmark_matches_source_asset(self):\n        self.assertIn((ASSETS / 'brand.svg').read_text().strip(), (ASSETS / 'base.html').read_text())\n\n" + anchor)
except (OSError, ValueError, AssertionError, ET.ParseError) as error:
    print('CANONICAL_BRAND_UNVERIFIED:', type(error).__name__, str(error))
else:
    asset.write_text(template)
    (asset.parent / 'brand.svg').write_text(svg + '\n')
    test.write_text(proof)
    asset.write_text(asset.read_text().replace('<div class="artifact-brand">', '<!-- Wordmark source: ' + brand_url + '; geometry preserved; white foreground uses currentColor. -->\n      <div class="artifact-brand">', 1))
    (ROOT / '.changeset/canonical-artifact-brand.md').write_text('---\n"qp-skills": patch\n---\n\nUse the official Quantipixels wordmark from the approved site rather than the earlier reconstructed drawing. Keep it embedded and adapt only its white foreground for legible printing.\n')
    print('CANONICAL_BRAND_RETRIEVED', brand_url, len(raw))
    commit('fix(html-artifact): preserve authoritative brand artwork in standalone output')

print('MIGRATED_SKILLS', len(original), 'EXPERIMENTAL', ','.join(experimental))
print('FINAL_HEAD', subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip())
