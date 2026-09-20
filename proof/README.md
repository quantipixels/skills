# Proof without a campaign platform

Start with the question. Package integrity, correct task outcomes and incremental benefit are separate claims. This directory contains reusable evidence assets, not a model runner, scorecard or mandatory campaign.

## Package mechanics

Run the repository's package validator and `tests/`. Native installer tests live beside their shipped script. These checks require no model credentials and do not establish model behavior.

## Existing engineering acceptance

The fixture groups and independent `oracle.py` are retained from the baseline without content changes. Work on disposable copies, never the originals. Give an actor only the selected task, fixture and intended guidance; withhold the oracle, grader controls and reference patches. Use genuine host isolation where available and disclose assignment-only separation.

For a trusted returned candidate:

```bash
python proof/oracle.py /absolute/path/to/disposable/candidate reuse
```

Supported cases are `batching`, `settlement`, `reuse`, `reuse-actions`, `verification`, `migration` and `profile`. Exit zero means all emitted checks passed; nonzero rejects the run. Preserve the emitted difference between assertion failure and runtime/setup error. Original fixtures intentionally contain missing/incorrect behavior; their ordinary local tests alone can pass without satisfying independent acceptance.

Use the retained Java `test_domain_values.py` probe for tolerant external conversion versus a strict internal boundary. Its controls and the Python reuse controls run without models:

```bash
python -m unittest discover -s proof -p 'test_*.py' -v
```

A JDK is required. These tests establish grader discrimination, not a model trial. The standalone oracle executes candidate code and is not a security sandbox or a general bounded-process runner. Use it only for trusted local candidates in disposable environments, or supply actual host isolation.

## Behavioral boundaries and comparisons

Select from [tasks](tasks.md), keeping [acceptance](acceptance.md) separate from actor inputs. Judge what was done and its evidence, not skill-name mentions or prescribed choreography. Include allowed work as well as refusal controls. No rebuilt-skill model runs are claimed.

For an improvement claim use [adanwo](../skills/adanwo/SKILL.md) with matched conditions, finite authorization, independent acceptance and actual artifacts. Record candidate identity, task, host/model/effort when observable, execution/response, failures/interventions, verdict and limits in the task's existing record. Do not create a universal manifest unless the particular experiment needs one.

Historical records and external-trace limits are in the [evidence index](../docs/evidence.md). The removed evaluator's preparation, tamper manifests, fixed study profiles and aggregation are not claimed to survive this smaller interface.
