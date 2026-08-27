# English draft then Chinese (internal)

导读 / 判断 are written **twice**, only the Chinese lands in `NOTES_DIR`. The English file stays in `TMP_DIR` and is never copied into `papers/`.

## Why

Chinese-first drafts smear technical terms (单点 for singleton) and flatten lab lineage. English-first drafts that skip a Chinese polish read like a translated abstract.

## Order

1. **English walkthrough** in `TMP_DIR` (`*-en-draft.md`). Paper order: gap → design → figures → bound. One claim per paragraph. Numbers from the extract / SI only. Build a terminology ledger (see `terminology-zh.md`) before the first sentence.
2. **Polish the English** with `nature-polishing` **stance only**: methods-paper questions (does it work, is the comparison fair, can it be rerun), terminology ledger, one idea per paragraph. Do **not** turn the draft into a Nature manuscript (no novelty claims, no “here we show” clothes, no phrasebank stuffing). Skip dumping `nature-polishing` fragments into the Chinese note. Em dashes in the English draft may stay if they come from the paper’s own terms (`Li–Stephens`); do not add decorative dashes.
3. **Translate** into spoken Chinese **sentences**. Apply the ledger. If a term has no accurate Chinese, keep English (`singleton`) and gloss once. Do not calque (`haplotype scaffold` → 单倍型骨架). Keep abbreviations in parentheses on first use.
4. **Polish the Chinese** with `fluency-zh.md` + `human-writing` (forum-prose; `revision.md` passes 1–4 and 6–7; **skip pass 5**). Expand telegrams. Do not run `check_prose.py` on the note. The 速览卡 must name authors. If Code availability has GitHub with a full script set, the 速览卡 must have a **代码** row.

YAML, tables, `## 📜 原文摘抄`, and `## ✍️ 写作学习` 原句 stay English / numeric. They are not part of the English draft.

## Length

The extract plus SI decide how long the 导读 is. A 7-page Technical Report with four supplementary figures stays shorter than a 50-page article with 28 SI figures. Do not pad to a line target. Do not shrink past a figure, a table, or an author-contribution fact that changes the claim. Do not compress Chinese into English nouns glued together.
