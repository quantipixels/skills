import { readFile, readdir } from "node:fs/promises";

const root = new URL("../", import.meta.url);
const skillsRoot = new URL("../skills/", import.meta.url);
const evalsRoot = new URL("../evals/cases/", import.meta.url);
const read = (path) => readFile(new URL(path, root), "utf8");

const skillNames = (await readdir(skillsRoot, { withFileTypes: true }))
  .filter((entry) => entry.isDirectory())
  .map((entry) => entry.name)
  .sort();

const readme = await read("README.md");
const router = await read("skills/alarina/SKILL.md");
const errors = [];

for (const name of skillNames) {
  const skillPath = `skills/${name}/SKILL.md`;
  const metadataPath = `skills/${name}/agents/openai.yaml`;
  let skill;
  let metadata;

  try {
    skill = await read(skillPath);
  } catch {
    errors.push(`${skillPath}: missing`);
    continue;
  }

  try {
    metadata = await read(metadataPath);
  } catch {
    errors.push(`${metadataPath}: missing`);
    continue;
  }

  const frontmatter = skill.match(/^---\n([\s\S]*?)\n---/u)?.[1] ?? "";
  if (!new RegExp(`^name: ["']?${name}["']?$`, "m").test(frontmatter)) {
    errors.push(`${skillPath}: frontmatter name must match its directory`);
  }
  if (!/^description:\s*\S/m.test(frontmatter)) {
    errors.push(`${skillPath}: description is required`);
  }
  if (!/display_name:\s*".+"/u.test(metadata) || !/short_description:\s*".+"/u.test(metadata)) {
    errors.push(`${metadataPath}: display_name and short_description are required`);
  }
  if (!readme.includes(`\`${name}\``)) {
    errors.push(`README.md: missing catalog entry for ${name}`);
  }
  if (!router.includes(`\`${name}\``)) {
    errors.push(`skills/alarina/SKILL.md: missing route for ${name}`);
  }
}

const requiredTypes = { trigger: 3, negative: 2, behavior: 1, pressure: 1 };
const evalFiles = (await readdir(evalsRoot)).filter((name) => name.endsWith(".json")).sort();
let evalCaseCount = 0;

for (const file of evalFiles) {
  const evalPath = `evals/cases/${file}`;
  const evalData = JSON.parse(await read(evalPath));
  const expectedSkill = file.slice(0, -".json".length);
  const ids = new Set();

  if (evalData.skill !== expectedSkill || !skillNames.includes(evalData.skill) || !Array.isArray(evalData.cases)) {
    errors.push(`${evalPath}: skill must match the filename and cases must be an array`);
    continue;
  }

  evalCaseCount += evalData.cases.length;
  for (const testCase of evalData.cases) {
    if (!testCase.id || ids.has(testCase.id)) errors.push(`${evalPath}: case ids must be present and unique`);
    ids.add(testCase.id);
    if (!testCase.prompt || !skillNames.includes(testCase.expected_owner) || !Array.isArray(testCase.expect) || testCase.expect.length === 0) {
      errors.push(`${evalPath}: ${testCase.id ?? "unnamed case"} lacks a prompt, published owner, or expectations`);
    }
  }
  for (const [type, minimum] of Object.entries(requiredTypes)) {
    const count = evalData.cases.filter((testCase) => testCase.type === type).length;
    if (count < minimum) errors.push(`${evalPath}: expected at least ${minimum} ${type} cases, found ${count}`);
  }
}

if (errors.length > 0) {
  console.error(errors.join("\n"));
  process.exit(1);
}

console.log(`Validated ${skillNames.length} skills and ${evalCaseCount} cases across ${evalFiles.length} eval suite(s).`);
