# Reference evidence and design decisions

Inspected 2026-09-08. The user confirms creating the original podcasts with NotebookLM. Repository commentary had inferred that origin; the user's confirmation is additional provenance, not evidence of the private generation prompt.

## Actual local references

`How_a_Flying_Bat_Fractured_the_Truth.transcript.md`: 22:10.039, SHA-256 `8ac976e5094fcdf9df12bc1655215e9505fdc017e5ca7da592f1f3238c126eed`. Its source package is `source/processed/witness_prep/podcast_gold_standard` in the user's Mock Trial repository. Original audio is named in the transcript. Local ASR, not certified verbatim. Speaker labels infer acoustic male/female presentation; segment boundaries are not reliable conversational turns.

`Trial_prep_for_beer_vendor_Ben_Stone_1.transcript.md`: 39:56.810, SHA-256 `da0c592bf8b7d8d3dd829b32f6348eb5daa57f876308f2cf831fac9b54d9e8b2`. This is the closer duration/task reference for a rich witness-preparation episode. Both originals are style evidence, not Msimoto facts or proof that their coaching is correct.

Observed functions: a concrete opening; two hosts building and challenging an explanation; links among source details; a shift from overall case to the selected witness; personal observation versus later learning; document acknowledgment; direct/cross contrasts; source-bound pressure and credibility coaching; retrieval and a compact close. The flying-bat spans 00:00–02:22 and 19:50–20:22 show orientation/synthesis; Ben spans 13:30–21:46, 22:01–25:29 and 29:23–38:24 show witness focus, document handling and examination/recall. The combined working draft has know-cold passages at lines 1522–1534 and 2555–2569, but no verified exact ten-item list was located. Ten anchors are the user's current design requirement.

Do not copy the originals' asserted motives, desired witness answers, disputed facts or metaphors. Transfer conversational functions with a fresh case and traceable evidence. A02 checks those functions; exact acoustic fidelity is untested without listening to produced audio. Original case/audio/ASR content is not bundled with the generic package.

## Public product evidence

Google describes Deep Dive as a two-host conversation connecting source topics. Its help lists Shorter/Default/Longer and topic/expertise customization; those controls do not establish a guaranteed 30-minute runtime. The page also documents “View custom prompt” in the artifact's menu, which can recover an owner's customization if available. We have not accessed that notebook. The help currently redirects under Gemini Notebook branding. [Google help](https://support.google.com/gemininotebook/answer/16212820?hl=en)

Meta's NotebookLlama is an open-source tutorial pipeline: preprocess text, write a transcript, rewrite for conversation/drama, then synthesize speech. We reuse the separation of writing and conversational revision, with independent source checks; its model names and dramatic prompting are not mandatory for our core. This is not evidence of NotebookLM's hidden internals. No Meta code/runtime was copied or installed. [Meta's official repository](https://github.com/meta-llama/llama-cookbook/blob/main/end-to-end-use-cases/NotebookLlama/README.md)

## Our testable reconstruction

Full authorized case context → source-linked permitted witness view → episode and KC10 plan → substantial two-host dialogue → independent conversation and evidence reviews → bounded revision → timing/export. This is prompt-only with operator-saved files. The intended 30–40 minutes is measured from actual speech words plus pauses; we never add unsupported facts or empty repetition to reach it. Broader case research stays author-only where the witness cannot know it. We do not know NotebookLM's private system prompt or guarantee identical audio behavior.
