# Bounded improvement experiment

experiment_id: TO_FILL
owner: TO_FILL
baseline_prompt_package: TO_FILL
candidate_prompt_package: TO_FILL
input_case_witness_source_view_revisions: TO_FILL
model_settings_context_exposure: TO_FILL
one_failure_to_address: TO_FILL
proposed_cause_and_alternatives: TO_FILL
minimal_instruction_change: TO_FILL
targeted_acceptance_probe: TO_FILL
counterexample_or_regression_probe: TO_FILL
maximum_loops: 2
second_loop_condition: meaningful benefit, no material veto/regression, named remaining deficit

| Attempt | Input identity | Output identity | Evidence hold? | Craft five dimensions /20 | Concrete benefit/loss | Reviewer/context | Keep/reject/hold |
|---|---|---|---|---|---|---|---|

## Independent reviewer challenge

Instruction → actual output span → finding → raw verification → cause → minimal change. Preserve disagreement and distinguish checker_error from author_error. No recursive critic chain.

## Fresh and transfer tests

Freeze candidate first. New author sees source, permission, prompts and task only. Save first-pass and repaired results separately; disclose prior exposure. Another case/witness must test the generalized change.

## Adoption decision

Owner/date, exact accepted revision, rejected alternatives, unresolved limits, rollback revision, next review trigger. Candidate lessons contain generic rules and authorized pointers, never private case content.
