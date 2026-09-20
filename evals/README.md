# Skill checks and comparisons

Start with the smallest check that can answer the question. Routine instruction edits do not require a model campaign.

| Question | Use |
| --- | --- |
| Does a skill answer a realistic prompt within its authority and stopping point? | A native-host smoke check below |
| Does Alárinà select the right owner and stopping point? | Selected [coordination cases](coordination/README.md) |
| Does returned code preserve the required behavior? | Relevant project tests or [engineering acceptance checks](engineering/README.md) |
| Is one instruction candidate better than another? | `adanwo` with matched candidates and its [agent-evaluation method](../skills/adanwo/references/agent-evaluation.md) |

## Simple prompt checks

Choose one realistic prompt for each changed boundary and the nearest negative control where the skill should stay inactive. Define expected behavior before seeing the response; keep it separate from actor inputs. Use existing cases when they fit. A whole-library sweep is useful when requested, not a gate for every edit.

Give the native worker the exact candidate skill and its required references. Pin the revision or content hash and verify the files actually read: installed skills may be older. Use a fresh session where practical; disclose reused context. The native host owns execution and worker lifecycle.

Judge the response or returned artifact against the expected result, authority, uncertainty and stopping point. Record the prompt, candidate, observed model/effort, response, verdict and material limits in one existing task record. Preserve wrong-source attempts and corrections. Proposed actions establish response behavior only; execute relevant boundaries when claiming tool use, runtime success or side effects.

Stop when the scoped question is answered. A plausible response does not certify the whole skill or demonstrate improvement over another candidate. Use `oro` for instruction corrections; use `adanwo` when a retention decision needs a controlled comparison.

## Retained proof

The engineering kit remains opt-in: it freezes coding tasks and checks actual returned code, regression detection and evidence integrity without running models. Its mechanical tests and project/package checks remain separate from prompt smoke checks. Select relevant cases rather than running every profile by default.

Project-backed [scenario protocols](engineering/scenarios/README.md) retain expectations that small fixtures cannot prove. Historical observations retain their original candidate and evidence limits; they are not current acceptance.

Keep generated runs and private traces in ignored `.qp/` or external storage. Package installation and CI need no model credentials. Directory separation is not a sandbox.

Earlier evaluation structure was informed by [SureForge](vendor/sureforge/UPSTREAM.md); attribution and license remain.
