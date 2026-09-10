# T04 · Bounded subagent instruction-and-output review

**Review packet ID:**  
**Workflow / capability IDs:** `ATTK.WF04.SUBAGENT_IMPROVEMENT` / `ATTK.A01.SUBAGENT_IMPROVER`  
**Task contract revision and digest:**  
**Worker instruction revision and digest:**  
**Actual worker outputs / evidence revisions and digests:**  
**Grader rubric/result revision and digest (if present):**  
**Runtime adapter, actual model/effort, tools/effects, source visibility:**  
**Named human adopter and intended reverse consumers:**  
**Budget / stop condition:** one repair and one recheck by default

## 1. Instruction trace

| # | Class: mandatory / prohibited / preference | Exact instruction or location-addressable excerpt | Observed exact output/evidence location | Status: met / violated / missing / not_assessable | Evidence limitation |
| --- | --- | --- | --- | --- | --- |
| 1 |  |  |  |  |  |

## 2. Separate verdicts

| Dimension | Locked criterion | Exact evidence | Verdict | Limitation |
| --- | --- | --- | --- | --- |
| Task quality |  |  | met / violated / missing / not_assessable |  |
| Instruction compliance |  |  | met / violated / missing / not_assessable |  |

## 3. Independent checker and grader audit

Use [P03](../prompts/P03-independent-verification.md). The checker must state
what it actually replayed, shared context/lineage, outcome-score visibility,
and whether each finding is `fixed`, `not_fixed`, `not_evaluable`, or
`checker_error`.

| Finding / grader criterion | Independent evidence | Result | Grader integrity concern or limitation | Necessary next action |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 4. Competing causal layers

Use [P05](../prompts/P05-prompt-diagnosis.md). A grade alone does not identify
an instruction defect.

| Plausible layer | Discriminating check | Observation | Status: supported / weakened / untested | Consequence |
| --- | --- | --- | --- | --- |
| Input/source contract |  |  |  |  |
| Context/data visibility |  |  |  |  |
| Worker instruction |  |  |  |  |
| Tool or runtime route |  |  |  |  |
| Workflow/handoff |  |  |  |  |
| Grader/evaluation harness |  |  |  |  |
| Reviewer or downstream specialist |  |  |  |  |

## 5. One bounded proposal

**Disposition:** `no_change` / `collect_more_evidence` / `repair_evaluator` /
`improve_input_contract` / `change_workflow_or_handoff` /
`compose_specialist` / `change_runtime_route` / `revise_instruction`  
**Smallest conditional change (or why none):**  
**Owner and allowed effect:**  
**Candidate revision and retained prior revision:**  
**Success and non-regression criteria frozen before test:**  
**Regression case / untouched holdout case / cost and latency measurement:**  
**Migration:**  
**Rollback:** human adopter selects retained prior revision and withdraws candidate  
**Privacy-safe lesson candidate (optional):**  

## 6. Independent evaluator audit and worker rebuttal

The evaluator inspects the worker, checker, grader, proposal, and evidence;
it does not accept their summaries as proof. The worker may rebut with exact
evidence. Record unresolved disagreement without recursive review.

| Evaluator audit question | Evidence | Verdict | Worker rebuttal | Final limitation / human question |
| --- | --- | --- | --- | --- |
| Is the trace complete and correctly classified? |  |  |  |  |
| Is the task-quality verdict separate from compliance? |  |  |  |  |
| Is the grader replayable, calibrated, and appropriate? |  |  |  |  |
| Does the proposal address the supported cause? |  |  |  |  |
| Does the test plan protect against regression? |  |  |  |  |

## 7. Recheck and human adoption

**Repair count / recheck count:**  
**Regression result:**  
**Untouched holdout result:**  
**Human decision:** `candidate_only` / `deferred` / `blocked` / `adopt` / `rollback`  
**Decision receipt / date / authority:**  
**Delivery state to reverse consumers:** prepared / delivered / acknowledged / incorporated / blocked  

Do not include raw conversations, secrets, private source rows, long logs, or
hidden reasoning. Missing evidence stays `not_assessable`; this packet cannot
self-certify adoption, independence, or qualification.
