# P02 · Diagnose and propose the smallest repair

Portable core v0.1.0. Inputs: reproducible failure, frozen inputs/output, checker finding, current contract and budget. Source data stays in the authorized workspace.

First verify the finding. List competing causal layers: input, context, tool, instruction, model route, workflow order, handoff and evaluator. For the plausible layers, name a discriminating check and the evidence available. Do not invent an experiment result. If uncertainty remains, use `collect_more_evidence` rather than asserting root cause.

Propose one bounded repair to the demonstrated layer. State exact changed artifact, expected observable difference, source/authority boundaries, regression risk, acceptance check, unaffected invariants and rollback. Preserve the preimage. Do not change thresholds to make the repair pass. The operator applies only authorized edits.

Output a concise diagnosis, minimal change, test plan and stopping rule. If the issue is merely stylistic preference or a grader defect, do not inflate it into a universal instruction.
