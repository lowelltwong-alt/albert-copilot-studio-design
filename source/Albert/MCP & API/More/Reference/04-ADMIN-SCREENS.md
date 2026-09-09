# Admin screens

## Shared screen contract

All screens are proposed authenticated external review UIs except simple status routing in the Standard-harness Teams agent. They display a case-scoped, server-produced view and submit a signed decision through `RecordHumanDecision`; they never accept a case, artifact, or role assertion from a hidden card field as authorization. Every submit includes the displayed subject binding, expected revision, purpose, authenticated principal, reason, intended audience where relevant, and a fresh anti-replay token. A revision conflict reloads the current record and requires a new human decision. Teams card, deep-link, accessibility, and authentication behavior remain tenant tests, not established platform behavior here.

The screens show safe status and hashes, not raw service logs. Long source material and artifacts have bounded, authorized viewers. Accessibility includes keyboard operation, visible focus, descriptive controls, semantic headings, labeled errors, and a reviewable text alternative for any visual source comparison.

## H01 rights data movement and budget

**Fields.** Case identifier and title; source binding/digest; requested operations and data classes; processor, tenant, environment, region, retention binding; proposed budget/currency; approver identity; decision; reason; expiration.

**Validation.** The source binding is current; operations/data classes are closed values; region and retention are nonempty; budget is nonnegative; decision is approve, reject, request changes, or revoke; approval expiration is future-dated; the reviewer has H01 authority for the case. Local prompt-only mode displays no approval form because it has no service action.

**Actions.** Approve exact scope creates a data-movement approval binding. Reject or revoke blocks affected queued/running work and starts dependency invalidation. Request changes returns a documented requirement without starting work. Start intake is enabled only after a current approval and budget check.

## H02 source layout and exhibit boundaries

**Fields.** Immutable source/layout bindings; page number; rendered original page; OCR/layout proposal; candidate exhibit label; continuation candidate; page order; table/figure/caption references; uncertainty flags; decision; reason.

**Validation.** Displayed page render and source digest must match the layout binding; no missing page, unresolved duplicate label, or ambiguous continuation can be approved; proposed page ranges are ordered and non-overlapping unless an explicit evidentiary role allows it; reason is required for overrides.

**Actions.** Approve exact boundaries creates the H02 decision consumed by F03. Request changes sends only the proposal reference to P01/S01. Reject blocks dependent chunking. A changed approved boundary invalidates chunks, graph views, grants, artifacts, and exports derived from it.

## H03 case profile and witness settings

**Fields.** Case/graph snapshot binding; applicable rule profile; witness identifier; role use; calling side; knowledge/cannot-know claim lists; expert scope; neutrality, bias, demeanor, challenge level; permitted/prohibited view summary; decision and reason.

**Validation.** Case and witness match the snapshot; role use is explicit; permitted and prohibited claims are disjoint; claims exist in the current graph; a required rule profile is resolved; settings do not rewrite source facts or rulings; reviewer holds the H03 scope.

**Actions.** Approve produces a versioned H03 decision and recipient-specific witness grants. Request changes returns the profile/settings proposal to its producer. Reject prevents F05-F07. Revoke invalidates existing grants and artifacts that depend on them.

## H04 evaluation and rework

**Fields.** Frozen artifact and rubric bindings; evaluator assignment/independence receipt; scores; hard gates; findings with artifact/source anchors; before/after diff; proposed rework plan; reviewer decision/reason.

**Validation.** The evaluator is distinct from the writer by enforced assignment evidence; score dimensions are unique; every hard gate has evidence; finding anchors resolve within the exact artifact; any claimed resolved finding maps to a later immutable revision; the reviewer sees the current quality series only.

**Actions.** Accept rework plan creates a `needs_rework` transition and permits the next assigned writer attempt. Adjudicate records an authenticated decision without altering evaluator history. Reject a required quality path marks the job failed. H04 cannot approve export or modify the rubric mid-series.

## H05 exact artifact approval and export

**Fields.** Exact packet/script bindings and hashes; current quality decisions; cross-artifact consistency result; intended audience; permitted export formats; grant/approval expiry; decision and reason.

**Validation.** Both artifacts are current and review-ready; their grants, quality decisions, and cross-check bind to the displayed hashes; packet category membership is resolved before packet convergence qualification; the reviewer holds H05 export authority; intended audience is allowed by every artifact/grant. A stale or mismatched artifact disables approval.

**Actions.** Approve exact scope writes an artifact-approval ledger entry and starts a separate export job. Request changes marks the affected artifact `needs_rework`. Reject marks the exact artifact rejected. Approval never changes the terminal generation job or releases a public link.

## H06 study custody

**Fields.** Protocol and consent bindings; custodian principal; sealed question-bank binding; participant assignment; initial/retry/delayed response references; delay hours; independent score bindings; adjudication reference.

**Validation.** Study work is disabled until protocol and consent are approved; only the custodian may view the hidden bank; delay is 24 through 72 hours; writers and ordinary reviewers have no hidden-question capability; participants and identifiers are in scope.

**Actions.** Approve creates/updates a study-custody record. Reassign and release occur only under the approved protocol. Revoke locks future study actions while preserving an audit receipt. This screen is not part of routine witness generation.

## H07 manual vendor handoff

**Fields.** H05-approved script/export bindings; exact citations/production-note bindings; selected files and intended vendor/audience; handoff acknowledgment; reason.

**Validation.** Every selected file is current, audience-scoped, and approved; no stale signed URL or unapproved annex is selectable. No vendor credentials, upload destination, or automatic send is stored here.

**Actions.** Produce an approved download manifest and record a manual handoff receipt. The user performs any vendor upload separately. Revocation disables future downloads but does not make an external vendor action reversible.

## Screen acceptance cases

`UX-01` expired H01 approval blocks F01; `UX-02` unresolved continuation blocks H02 approval; `UX-03` overlapping H03 claim sets fail; `UX-04` same writer/checker fails H04; `UX-05` mismatched H05 hash cannot export; `UX-06` H06 hides questions from writers; and `UX-07` H07 rejects a stale file.
