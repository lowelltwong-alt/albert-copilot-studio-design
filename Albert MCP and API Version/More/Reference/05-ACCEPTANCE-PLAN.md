# Acceptance plan

`acceptance-catalog.json` defines 20 original synthetic protocol examples and 18 tenant, concurrency, human or release cases. The executable reference model illustrates specified predicates. It trusts its input dictionaries and implements no authentication, storage, provider integration, actual workflow, production aggregate validator or semantic evaluator. A reference pass is never an Albert product test or security certification.

## Commands and adapter contract

From this package directory with Python 3.10 or later:

```text
python acceptance-runner.py --mode reference --output reference-test-report.json
python acceptance-runner.py --mode service --adapter PATH_TO_REAL_ADAPTER.py --output service-test-report.json
```

The real adapter is an implementation deliverable (WP23). Without it, service mode exits 2 with blocked status. It must export `run_fixture(state) -> {"findings": [...], "primary": code_or_null}`. It receives synthetic state only, never expected answers. Each call provisions an isolated test namespace, translates the state into service setup plus operation(s), invokes the same production validator/control path, and normalizes actual findings to the catalog codes. It must not implement another copy of reference_rules or return expectations. Case state is a test setup instruction, never an authentication payload supplied to an ordinary production endpoint. Return no extra keys in this small runner contract; place run/service/revision/request and cleanup evidence in a separate sanitized receipt bound to its digest.

For every fixture and both forward/reverse orders, the runner demands a clean baseline from the same adapter, exact ordered findings, exact primary finding and exact delta from clean. A duplicate, secondary-only rejection, unrelated failure, baseline failure or order-dependent behavior fails. The runner sets `production_qualified: false` even in service mode: a separate QA decision must inspect adapter isolation, production validator identity, revision bindings and unexecuted coverage before qualification. Do not edit that field to manufacture qualification.

The 20 executable cases cover representative boundary predicates. They do not prove all schema constraints or job transitions. AT22–AT35 extend the actual service tests to real identity, concurrency, original-page semantics, scoring, both transports and the tenant. Genuine independent evaluator context, actual material defect resolution and real human decisions require their own evidence. Never generate a passing human ballot, study outcome, rubric decision or tenant receipt with a model.

## Execution record and exit rule

Record artifact/config/service/input/policy/fixture/adapter/validator revisions; actor and environment; UTC run time; status for each case (pass, fail, blocked, not run); minimal expected-versus-actual finding codes; cleanup outcome and review owner. Do not put case text, credentials or live tokens in test logs. Keep source evidence in its authorized custody store.

Release requires zero open critical/serious defects, all required cases passed on the candidate revision, resolved packet category mapping for packet convergence claims, actual H05 acceptance, and operations handoff. A diagnostic packet/script pilot may proceed as explicitly diagnostic before formal category mapping is resolved; it cannot be relabeled gold or converged. Optional AT37 does not block a basic pilot but is mandatory for learning-effect claims. AT38 applies to the later public release.

## Manual and integration case instructions
### AT21 — Scope and version pin

Inspect named owners, approved synthetic scope, input/code/policy revisions and decision register. Missing ownership fails commissioning.

Status: not run; attach real evidence before passing.

### AT22 — Movement and custody

Deny expired/revoked approval, unapproved processor/region/telemetry/retention and altered source revision before network I/O. Confirm no source text in logs.

Status: not run; attach real evidence before passing.

### AT23 — Real identity boundary

Use two real test principals through MCP and API. Verify issuer/audience/expiry and witness scope. Maker connection cannot widen an end user. Include expired/revoked grant and guessed artifact IDs.

Status: not run; attach real evidence before passing.

### AT24 — Races and recovery

Inject simultaneous same-key requests, lost response, cancel-before-callback and callback-before-cancel. Crash around outbox commit and provider charge acknowledgement. Verify exactly one job/export/charge and quarantine as applicable.

Status: not run; attach real evidence before passing.

### AT25 — Original-page semantic review

Use synthetic OCR containing omitted negation, continued exhibits, rotated/table pages and multibyte offsets. Human compares original page, crop and spans. Correct digest alone cannot pass an omitted negation.

Status: not run; attach real evidence before passing.

### AT26 — Three familiar families

Premises: witness saw condition after incident, cannot infer prior notice. Medical handoff: hearing a handoff does not prove reading a chart. Cold chain: custody and calibration evidence do not establish medical causation. Review actual source-bound output.

Status: not run; attach real evidence before passing.

### AT27 — Unfamiliar case family

Remove governing rule profile and expertise. Source inventory may complete, domain conclusions must stop with specific missing-rule questions. Preserve conflicting attributed accounts.

Status: not run; attach real evidence before passing.

### AT28 — All schema constraints

Use the production aggregate validator to reject duplicate dimensions/IDs, missing panel cells, broken cross-case references, malformed scopes, and stale dependency bindings; preserve exact primary findings and clean baselines.

Status: not run; attach real evidence before passing.

### AT29 — Real material improvement

Freeze packet and script A0/E0 separately. Complete at least two independently verified material revisions each. Prove actual defect resolution with changed evidence and scores, zero serious findings and no critical regression. A cosmetic rewording fails. Packet formal gate needs resolved category map.

Status: not run; attach real evidence before passing.

### AT30 — Human UI and download

Test H01–H07 required fields, reject/change/approve paths, keyboard navigation, screen-reader labels, double-click and stale-tab handling. H05 creates a distinct export job; download rechecks access and exact current text.

Status: not run; attach real evidence before passing.

### AT31 — MCP tenant compatibility

Standard harness + Teams: direct or Swagger import, TLS/OAuth callback, initialize, tools/list, all eight tools, errors, section paging. Confirm human-decision capability absent from tools. Record actual tenant/protocol/service/config versions.

Status: not run; attach real evidence before passing.

### AT32 — API parity and fallback

Import/configure API connector. Compare same operation under same identity across transports. Transient read fallback preserves scope; 401/403/409/422/budget/quality/cancel/TLS-trust failures never trigger fallback. Lost write response uses lookup without new key.

Status: not run; attach real evidence before passing.

### AT33 — Published-channel behavior

Run published Teams as maker and second pilot user. Measure response limits, cancellation, token renewal, status polling and long-script section retrieval. Test chat alone is insufficient.

Status: not run; attach real evidence before passing.

### AT34 — Harness qualification

Real adapter supplies isolated synthetic namespaces, clean production-validator baselines, forward/reverse runs, exact expected primary codes and no unexpected deltas. Reference mode never counts. Retain fixture/adapter/service/validator digests and setup/cleanup evidence.

Status: not run; attach real evidence before passing.

### AT35 — Capacity and restore

Measure latency, credits, concurrency and queue limits with an approved synthetic budget. Restore artifacts plus ledgers and dependencies; reconcile in-flight jobs and demonstrate revoked grants remain revoked.

Status: not run; attach real evidence before passing.

### AT36 — Pilot handoff

Named pilot/operations owners receive exact artifact/config/test revisions, known defects and recovery runbook; receipt and acknowledgment recorded. No unsatisfied acceptance gate marked passed.

Status: not run; attach real evidence before passing.

### AT37 — Optional human study

Explicit approved protocol, consent, sealed bank, real blinded reviewer assignment and learning outcomes with 24–72-hour follow-up as specified. No model-created ballot or invented study evidence.

Status: not run; attach real evidence before passing.

### AT38 — Later public release

Confirm licenses and release authority. Scan exact allowlisted bundle for secrets, private paths, client content and internal IDs; review rendered files and archive members. No publication implied by a local ZIP.

Status: not run; attach real evidence before passing.
