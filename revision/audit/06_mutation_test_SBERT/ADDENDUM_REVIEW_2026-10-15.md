# Addendum on interpretation after the review of 15 Oct 2026

English translation (19 Oct 2026, prepared with an AI assistant, Claude) of the Vietnamese original `ADDENDUM_REVIEW_2026-10-15.md` (SHA-256 6b2240dd713fe252…), which the authors keep unchanged.

PROTOCOL_Codex.md is the protocol written before measuring, on 12 Oct, and it is kept unchanged. The sample, seed, threshold, operators and results were not changed after the review.

- The transformation experiment runs on **one extracted scenario**, whereas the paper's main metric encodes **the whole feature file**. The result is only an auxiliary sensitivity check; it does not yet measure the sensitivity of the whole-file pipeline to defects.
- For M_NUM and M_PARAM, the skeleton masking step erases the change to the numbers/double-quoted strings. Identical skeletons are an invariance by definition, not an independent empirical finding about business-logic defects.
- In total there are 120 scenarios and 683 applicable mutants. 74 scenarios had their Background dropped, 5 originals have a hard error according to the checker, and 29 mutants cannot be parsed. These groups can overlap, so they cannot simply be added or subtracted.
- The subset of 623 pairs requires that the original and the mutant both parse and that the original has no hard error. This filtering does not restore the lost Background and does not prove that the mutants are wrong in business terms. Both the 683 and the 623 have cosine ≥0.85; always state the correct denominator and the limitations.
- Do not call this GPT's actual false-negative rate, or evidence that all 683 mutants are wrong. The M_NUM/M_PARAM tables are kept for reproduction and are presented clearly as invariance checks.

The corrected write-ups are in B2_ket_qua.md, H3_ket_qua.md and DOAN_THAY_THE_B2_H3_E13_E15.md (file names in Vietnamese: "ket_qua" = results, "DOAN_THAY_THE" = replacement passages).
