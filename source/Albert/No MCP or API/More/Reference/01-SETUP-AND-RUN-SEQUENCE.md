# Setup and run sequence

Create one unpublished standard-harness agent. Paste `00-ALL-IN-ONE-PROMPT.md` as the parent instruction block. It is a router, not all ten full procedures. At each stage, paste the exact C01–C10 file listed below with its required inputs; these stage files are required for the complete workflow. Paste only approved source spans and the current ledger. Do not paste protected content unless the channel and operator have approved it.

Run exactly: `C01-intake.md` → `C02-source-exhibit-review.md` → `C03-evidence-ledger.md` → `C04-case-witness-profile.md` → `C05-full-witness-packet.md` → `C06-independent-review.md` → `C07-material-revision.md` → `C08-full-chaptered-script.md` → `C09-pair-consistency-final-package.md` → `C10-truthful-rehearsal.md`.

At every stage the operator reviews the complete output and types `CONTINUE — C0X reviewed`. For long artifacts request one chapter per turn and freeze the reviewed text manually as A0, A1 or A2. Keep packet and script series separate. Each requires E0, two substantive human-accepted cycles, and no more than five revision attempts. Stop as `unresolved` if the defect remains, a hard gate fails, or the fifth attempt is exhausted.

Optional child agents may map one-to-one to these roles: `Intake` (C01–C03; inputs approved source spans and H01 decision; outputs intake, source review and ledger), `Profile` (C04; input reviewed ledger; output H03 profile), `Packet Author` (C05; input approved profile/ledger; output packet A0), `Checker` (C06; input one frozen artifact; output scores, diffs, findings and revision plan), `Revision` (C07; input frozen artifact plus approved findings; output A1/A2), `Script Author` (C08; input approved packet/ledger; output chaptered script A0), `Consistency` (C09; input exact packet/script; output pair findings and final package), and `Rehearsal` (C10; input H05-approved text plus prompt; output observed practice). Built-in linking and model separation vary by tenant. If linking fails, paste each stage file manually. Child names do not prove evaluator independence.


After C05, run C06/C07 until packet A0/E0 → A1/E1 → A2/E2 is reviewed before C08. After C08, run C06/C07 separately for the assembled podcast A0/E0 → A1/E1 → A2/E2. Then run C09. Re-run C09 if either artifact changes. See 11-CASE-STORAGE.md for manual checkpoints and optional persistent knowledge upload.
