# Innovation bounded recheck

**Result: R02 remains HOLD.** This concise recheck supersedes only the timing-method finding in the earlier independent review; it does not revise the demo, source, prior review, or any acceptance state.

## Executed and observed

I ran `python outputs/Albert-Innovation-MVP-1.0/checks/measure_demo.py` against the unchanged script. It exited successfully and printed the same receipt now saved at `checks/DEMO-MEASUREMENTS.json`:

- script SHA-256: `0fc059fd89df1da31b9586cfe09c125390aa706d5639f761d86a9a9bd29d0d97`
- exact method: `str.split()` after an exact bold host/turn label, excluding metadata, labels and cues; hyphenated compounds remain one token
- 43 speech lines, 1,238 spoken whitespace tokens, 10 pauses and 116 pause seconds
- combined estimate: 10.471 minutes at 145 wpm (9.671 at 160; 11.456 at 130)
- PC03 and PC04 both rejected as practice: their feedback is already supplied before the pause, so each is correctly classified as reflection.

The tool's declared scope is timing plus those two order checks, not a semantic-quality or source gate. **FR03 is closed:** the specified count rule makes the 1,238-word and rounded timing values reproducible for this exact script. It does not repair the incorrect T06 descriptions of PC03/PC04.

## RUN-06 adapter recheck

The new `Rubric selection for this runtime adapter` at RUN-06 lines 15–19 is explicit: its five scored dimensions are host contribution, useful depth, examination practice, taught-and-retrieved anchors, and listening coherence; it says the embedded older A02 list is replaced for this starter, retains A02's detailed review rules, and forbids combining practice with anchor retrieval. `ROLE-CONVERSATION.md` uses the same five concepts, and the regenerated RUN-06 part 1 contains the selection unchanged. This resolves the instruction-level rubric ambiguity.

The unchanged script receives this **new adapter assessment**, which must not be compared as a total with the earlier A02-shaped assessment:

| Declared RUN-06 dimension | Score /4 | Evidence |
|---|---:|---|
| Host contribution | 3 | HOST_B materially reframes sensory, causal, timing and document inferences in PC03–PC06. |
| Useful depth | 3 | The four pressure modules use the permitted qualifications rather than invented testimony or legal rules. |
| Examination practice | 2 | PC02 and PC05–PC08 have prompt → pause → feedback order; PC03/PC04 do not. |
| Taught-and-retrieved anchors | 2 | Anchors are taught, but KC09's cited delayed retrieval is partial rather than clause-complete. |
| Listening coherence | 3 | The PC01–PC08 progression is understandable and cumulative, although PC08-A4 remains a dense multi-limit recall turn. |

`craft_gate=REPAIR`: two dimensions are below 3, and the identity/manual-review requirements are still unresolved.

## Remaining holds and exact next repair

1. **Practice-order audit remains false.** T06 rows 13–14 and 25/27 say PC03/PC04 feedback follows their pauses; script PC03-B2 and PC04-B2 give it before the pauses. Either build prompt → pause → source-bounded feedback, or relabel both as reflection and remove their practice credit.
2. **KC09 retrieval remains partial.** T06 row 30 credits complete later retrieval, while PC08-A4/B4 recalls generic entries, Mina-authentication and Lee-explanation limits but not every card clause. Make the closing retrieval clause-addressable or mark the omitted clauses partial.
3. **Assembly metadata is internally inconsistent.** The script, claims, final KC10 and T06 titles/BEGIN markers are R02; yet the script production metadata, claims metadata and KC10 metadata say `source/view/assembly R01` (and the plan carries an R01 assembly reference). SOURCE/graph may properly remain R01, but the reviewed script/claims/card/T06 assembly must consistently name R02. Until that is corrected and the exact complete files are saved/reopened, manual identity is HOLD/NOT_ASSESSED.
4. **No human save/reopen receipt exists.** The tool receipt proves only the local script measurement. It cannot establish that an operator saved/reopened and compared the full required assembly.

One small setup hardening item remains: RUN-06's current-stage override is semantically clear, but the preserved A02 T05 template still prints the older headings (host interaction, spoken clarity, episode arc, source-supported depth, retrieval/ten-anchor integration). Before a live Studio run, add an adapter-owned output-table mapping that names the five RUN-06 dimensions and says not to score the preserved headings. This avoids a mixed-table reviewer report without altering the retained A02 bytes.

No original benchmark, tenant run, audio assessment, or human acceptance was supplied; `reference_comparison_unavailable` and the other declared limits remain in force.
