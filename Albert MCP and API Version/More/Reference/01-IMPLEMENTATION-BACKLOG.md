# Implementation backlog

28 assignable work packages. Roles are accountable owners to be named by the Innovation. Estimates are person-days for planning; they include local verification but depend on authorized reuse and tenant access. They are not measured duration or a fixed-price commitment. The prompt-only MVP is a separate deliverable and can be tried before this backend work.

Suggested release slices: WP01–WP05 establish contracts/authority/jobs; WP06–WP18 complete source-to-reviewed-artifact behavior; WP19–WP24 prove transport/tenant/operating limits; WP25–WP26 close the pilot and operations handoff. WP27 is optional and separately authorized. WP28 is the later public release. Parallelize integration stubs only after WP02; each listed dependency must pass before its consumer is accepted.

## WP01 — Freeze pilot scope and owners

Owner: Product owner. Estimate: 1–2 person-days. Depends on: none.

- Record one synthetic case, witness, rule profile and expected packet/script outputs.
- Assign platform, backend, review and QA owners; record data/region/budget decisions.
- Pin authorized input/code/policy revisions in an implementation receipt.

Deliverable: Signed scope and decision register; no protected source bundled.
Acceptance: AT21, AT22; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP02 — Implement domain and transport adapters

Owner: Backend lead. Estimate: 2–4 person-days. Depends on: WP01.

- Validate transport DTOs and map them explicitly to domain records.
- Reject unknown fields, malformed bindings, duplicate logical IDs and unresolved references.
- Document sentinel rules and migration/version policy.

Deliverable: Versioned schemas, adapter code and compatibility tests.
Acceptance: AT01, AT06, AT28; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP03 — Implement authenticated case and witness access

Owner: Backend security owner. Estimate: 3–5 person-days. Depends on: WP02.

- Verify token issuer, audience, expiry and delegated identity.
- Persist case roles, movement approvals, witness grants and writer/checker assignments.
- Apply principal/view checks to queries, summaries, counts, previews and downloads.

Deliverable: Authorization middleware and denial tests through both transports.
Acceptance: AT02, AT03, AT04, AT07, AT23; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP04 — Implement source custody and versioned review subjects

Owner: Backend owner. Estimate: 2–4 person-days. Depends on: WP02, WP03.

- Store immutable originals and extraction derivatives separately.
- Issue H01 review subject plus nonce and validate exact approval before any egress.
- Bind source byte digest, processor, region, retention and telemetry classes.

Deliverable: Custody adapter and approved synthetic intake.
Acceptance: AT05, AT06, AT22; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP05 — Implement job ledger and durable recovery

Owner: Backend owner. Estimate: 4–7 person-days. Depends on: WP02, WP03.

- Create transactional idempotency, state-version CAS, worker lease and callback receipt tables.
- Fence cancellation; reconcile unknown provider outcome before retry; account charges once.
- Commit outbox with state and deliver notifications with bounded retries.

Deliverable: Job service, worker adapter and injected-failure evidence.
Acceptance: AT10, AT11, AT12, AT24; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP06 — Implement OCR/layout adapter

Owner: Document processing owner. Estimate: 2–4 person-days. Depends on: WP04, WP05.

- Select an approved OCR adapter and preserve page image dimensions and engine revision.
- Translate declared byte/codepoint/UTF-16 offsets to verified selected text.
- Render source-page review for uncertain negation, tables, quotations and attributions.

Deliverable: One synthetic scanned-document extraction with page/span audit.
Acceptance: AT08, AT25; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP07 — Build page and exhibit boundary review

Owner: Power Platform / UI owner. Estimate: 2–3 person-days. Depends on: WP06.

- Implement H02 crop, span, exhibit alias and continuation fields.
- Require exact reviewed page/exhibit revision; retain rejected values in history.
- Invalidate dependent chunks and descendants when approved boundaries change.

Deliverable: H02 screen and resubmission test.
Acceptance: AT08, AT09, AT25; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP08 — Implement evidence-preserving chunk construction

Owner: Backend owner. Estimate: 2–4 person-days. Depends on: WP07.

- Reuse authorized source splitting through an explicit adapter.
- Prevent cross-exhibit chunks and orphaned Q/A, table-header or qualification spans.
- Generate stable logical IDs plus content revisions and dependency edges.

Deliverable: Chunk adapter with table, Unicode and exhibit fixtures.
Acceptance: AT09, AT25; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP09 — Implement attributed graph and case rule profile

Owner: Knowledge engineer. Estimate: 3–6 person-days. Depends on: WP08.

- Map claims, assertions, conflicts, inferences, gaps and source anchors to existing graph contracts.
- Preserve speaker, time uncertainty and rule-premise provenance.
- Expose bounded typed queries and deny bare inference promotion or cross-case edges.

Deliverable: Graph adapter with source-to-answer trace and unfamiliar-rule stop.
Acceptance: AT04, AT26, AT27; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP10 — Build case profile review

Owner: Rule custodian + UI owner. Estimate: 1–3 person-days. Depends on: WP09.

- Capture case family, applicable rules and unresolved assumptions.
- Keep neutral posture separate from calling side, incentives and expert scope.
- Bind human review to a profile revision and invalidate downstream views on change.

Deliverable: Reviewed synthetic case profile and change test.
Acceptance: AT26, AT27; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP11 — Implement witness view and role controls

Owner: Backend + UI owner. Estimate: 2–4 person-days. Depends on: WP03, WP10.

- Implement H03 form and server validation for human-played roles.
- Compile permitted/prohibited evidence views including intermediate queries.
- Revoke or revise grant on role/source/profile change and deny stale descendants.

Deliverable: Witness view compiler and H03 screenshot/denial evidence.
Acceptance: AT03, AT04, AT07; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP12 — Implement candidate series persistence

Owner: Backend owner. Estimate: 2–3 person-days. Depends on: WP05, WP11.

- Save immutable A0 with server-derived digest and writer assignment.
- Require same series/kind/current bindings for parent and subsequent candidates.
- Store candidate-to-input and candidate-to-evaluation dependencies atomically.

Deliverable: Candidate API with baseline and versioned revision receipts.
Acceptance: AT12, AT14, AT18; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP13 — Wire packet generation prompt

Owner: Agent engineer. Estimate: 1–3 person-days. Depends on: WP12.

- Map P04 inputs to permitted witness excerpts and explicit rule profile.
- Produce packet sections with source notes, knowledge limits and examination practice.
- Persist each draft with SaveCandidate; no self-issued approval or qualification.

Deliverable: Synthetic packet baseline and prompt/config revision.
Acceptance: AT26, AT27, AT29; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP14 — Implement independent evaluation and scoring

Owner: QA/backend owner. Estimate: 3–5 person-days. Depends on: WP12.

- Issue separate checker assignment with clean context and read-only scoring capability.
- Validate exact dimension cells and compute scores without rounded pass comparisons.
- Return span-bound defects and policy status; block packet convergence until category map resolved.

Deliverable: Evaluation service, rubric-owner decision and score tests.
Acceptance: AT13, AT15, AT16, AT17; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP15 — Implement material revision control

Owner: Backend + agent owner. Estimate: 2–4 person-days. Depends on: WP13, WP14.

- Freeze each baseline/evaluation and derive changed input/artifact/outcome.
- Count only independently verified substantive defect resolution; require two accepted revisions.
- Stop at five attempts or critical regression; display remaining work without relabeling failure.

Deliverable: Packet loop receipts and no-op/cap tests.
Acceptance: AT14, AT18, AT29; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP16 — Wire chaptered script generation and revision

Owner: Agent engineer. Estimate: 2–4 person-days. Depends on: WP15.

- Map P05 to exact approved packet/view and chapter plan.
- Separate spoken words from production/citation notes and report word count.
- Run a distinct script series with its own baseline/checker/two counted revisions.

Deliverable: Script baseline and two-cycle synthetic trial evidence.
Acceptance: AT14, AT16, AT29; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP17 — Implement cross-artifact consistency gate

Owner: QA/knowledge owner. Estimate: 2–3 person-days. Depends on: WP16.

- Compare exact packet/script pair for role, dates, exhibit use and source-bound claims.
- Emit findings against affected artifact and route revision to its own series.
- Invalidate pair decision if either member or any dependency changes.

Deliverable: Pair-bound decision and stale-pair denial test.
Acceptance: AT18, AT19, AT29; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP18 — Build final review and controlled export

Owner: UI/backend owner. Estimate: 2–4 person-days. Depends on: WP17.

- Implement H04 scores/diffs and H05 exact artifact decisions.
- Keep generation terminal; record independent artifact approval ledger and enqueue new export job.
- Recheck grant/current digest at preview and download; H07 downloads only approved text/notes.

Deliverable: Screens, audit receipts and approved synthetic download.
Acceptance: AT19, AT20, AT30; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP19 — Implement Copilot-compatible MCP transport

Owner: Integration engineer. Estimate: 2–4 person-days. Depends on: WP03, WP05, WP12, WP14.

- Implement official SDK Streamable HTTP transport and eight declared tools.
- Configure OAuth plus same service/principal mapping; omit human-decision capability.
- Validate tool discovery, bounded outputs, protocol failures and loss recovery.

Deliverable: Deployed candidate MCP endpoint and sanitized protocol report.
Acceptance: AT23, AT24, AT31; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP20 — Implement API alternate transport and failover

Owner: Integration engineer. Estimate: 2–3 person-days. Depends on: WP19.

- Implement all eight agent API operations against the same service ledger.
- Import/configure Swagger 2 connector; route automatic fallback only for permitted reads.
- Reconcile missing mutation responses using operation ID; same-key retry only under explicit alternate-mode policy.

Deliverable: API connector candidate and transport parity/replay tests.
Acceptance: AT12, AT23, AT24, AT32; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP21 — Configure and validate Copilot Studio agent

Owner: Power Platform owner. Estimate: 2–4 person-days. Depends on: WP18, WP19, WP20.

- Create standard-harness parent/children with exact instruction and connection mappings.
- Bind tool inputs/outputs explicitly and use authoritative job polling.
- Run test-chat then published-channel discovery/auth/invoke/denial/timeout probes.

Deliverable: Exported tenant solution/config plus tenant-specific test receipt.
Acceptance: AT31, AT32, AT33; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP22 — Build status and recovery UI

Owner: UI owner. Estimate: 2–3 person-days. Depends on: WP05, WP18.

- Show state, current revision, cost reservation, active blockers and last authoritative poll.
- Provide cancel/rework/new-job actions with state-version checks.
- Handle double-click, stale tab, retry, access denial and safe error correlation IDs.

Deliverable: Accessible status/review screens with failure screenshots.
Acceptance: AT10, AT11, AT24, AT30; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP23 — Implement real-service acceptance adapter

Owner: QA owner. Estimate: 2–4 person-days. Depends on: WP03, WP05, WP14, WP18.

- Map the supplied fixture contract to isolated synthetic service namespaces.
- Verify fixture setup/teardown and capture request/result revision bindings.
- Run both orders with clean baselines, exact primary findings and semantic human tests separately.

Deliverable: Production-validator adapter and release-bound acceptance evidence.
Acceptance: AT01, AT20, AT34; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP24 — Measure capacity, accessibility and tenant limits

Owner: Platform + QA owner. Estimate: 1–3 person-days. Depends on: WP21, WP22, WP23.

- Measure synchronous response time, generation latency, response sizes and credits.
- Test keyboard/screen-reader status and review controls in target channel.
- Agree quotas, rate limits, retention, escalation and backup objectives from observations.

Deliverable: Measured pilot limits and accessibility report.
Acceptance: AT30, AT33, AT35; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP25 — Run staged synthetic pilot and defect closure

Owner: Pilot owner. Estimate: 2–5 person-days. Depends on: WP24.

- Run premises then medical handoff, cold chain and unfamiliar-rule fixtures.
- Log critical/serious findings and repair with exact-revision reruns.
- Obtain human acceptance for the specific packet/script; distinguish tenant readiness from gold.

Deliverable: Pilot report with observed pass/fail and unresolved items.
Acceptance: AT25, AT26, AT27, AT29, AT36; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP26 — Implement operational handoff and restore drill

Owner: Operations owner. Estimate: 2–3 person-days. Depends on: WP25.

- Document on-call ownership, revocation, cancellation, outages and unknown-charge handling.
- Restore ledgers/artifacts/dependency links in an isolated synthetic environment.
- Reconcile in-flight jobs and demonstrate replay cannot issue duplicate exports or charges.

Deliverable: Runbook, recovery drill and downstream acknowledgment.
Acceptance: AT24, AT35, AT36; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP27 — Optional blinded learning study

Owner: Study custodian. Estimate: separately scoped person-days. Depends on: WP25.

- Obtain explicit protocol/consent/data authority and seal transfer bank before use.
- Assign real blinded reviewers and learners; preserve attrition and follow-up timing.
- Apply existing analysis/reliability rules without exposing bank to generators.

Deliverable: Study protocol and separately evaluated learning evidence.
Acceptance: AT37; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.

## WP28 — Prepare later public Git release

Owner: Release owner. Estimate: 1–3 person-days. Depends on: WP26.

- Confirm code/case/prompt licenses and release scope with owner.
- Build allowlisted recipient/public bundle with secret/private-path scan.
- Publish only after authorized release review, exact-hash verification and repository checks.

Deliverable: Reviewed public release candidate; publication not performed here.
Acceptance: AT38; attach exact-revision evidence from `05-ACCEPTANCE-PLAN.md`. Status: specified, not implemented.
