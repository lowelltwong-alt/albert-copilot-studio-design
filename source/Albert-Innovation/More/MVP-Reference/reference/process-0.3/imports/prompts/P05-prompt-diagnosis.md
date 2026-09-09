# P05 · Improve the right layer

Portable core v0.1.0. Inputs: locked task/rubric, exact prompt revision, artifacts, independently checked findings, runtime bindings and prior attempts.

Separate outcome from cause. Test whether a bad score reflects a source error, missing input, context loss, tool defect, role ordering, overly broad instruction, poor model fit, contamination or an evaluator error. Give a concrete check for each plausible explanation; mark untested hypotheses. Repeated self-critique is not independent evidence.

Choose one: no change, repair evaluator, improve input contract, change workflow/handoff, add a bounded specialist, change runtime route, revise a prompt, or collect more evidence. If revising, propose the smallest conditional change and remove overlapping guidance. Preserve old and new prompt versions.

Use matched cases for diagnosis, then an untouched case for promotion evidence. Freeze success and non-regression criteria before the test; record cost, elapsed time, context visibility and actual model binding. Do not call reused examples holdouts. A new model or prompt needs new evidence. Return a candidate decision packet with the owner and rollback; do not auto-adopt.
