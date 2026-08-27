# Fluency pass (human-writing, notes)

Apply this to Chinese **narrative** only: `## 导读` / `## 📖 全文导读` / `## 我的判断` (and 速览卡「一句话」). Leave YAML, tables, `## 📜 原文摘抄`, `出处：`, DOI, filenames, and Latin names alone.

If the `human-writing` skill is installed, load its `SKILL.md`, then `references/forum-prose.md` and `references/reality.md`. After the rewrite, load `references/revision.md` and walk passes 1–4 and 6–7. **Skip pass 5 punctuation** (colon / em dash). Notes need `出处：`, YAML, `Mann–Whitney`, and ranges like `560–610 km`.

Write as a colleague who has the PDF open. Not a Zhihu post, not a Nature manuscript. Field terms follow `terminology-zh.md`. If the Chinese would be a glued calque (`singleton` → 单例变异, `scaffold` → 单倍型骨架), **keep the English** and explain in a full sentence. Lab and competitor names stay in 导读.

**Do this on the first draft.** Do not write a telegram 导读. Spoken Chinese with numbers in the sentence. Do **not** compress: a short English clause must become a complete Chinese sentence, not four technical nouns in a row. Do not cut the 导读 opening to look tight.

Bad (English words glued, then shortened): 「芯片时代的单倍型定相已经能扛几十万人。UKB 150,119 人的 WGS 位点数比 Axiom 芯片高三个数量级。」

Good: 「以前做全基因组关联，主要靠 SNP 芯片。芯片上大多是常见位点；当时的统计定相方法，也是为这些常见位点写的，已经可以处理几十万人的数据。UK Biobank 后来放出 150,119 人的全基因组测序。和他们自己用的 Axiom 芯片比，位点数量高了大约三个数量级。」

Bad (spoken verbs + calque, Otava note): 「先把 Otava 的 HiFi 直接丢进 hifiasm……塌掉的那一段，后面几乎正好对上 IBD。要把塌掉的 contig 解开，作者改走读段分箱。」

Good: 「作者先把 Otava 的 HiFi 读段交给 hifiasm 做初始组装。四套 haplotype 里几乎相同的区段在初始组装里塌缩成一条 contig；这些塌缩区域后来和 IBD 块对上。于是改用 717 个花粉核，把 HiFi 读段按 haplotype 分开，再各自组装。」

Good (parental direction): 「trio binning 在二倍体里能用，因为一条读段可以按它更像父亲还是更像母亲来归组。」

## What to take from human-writing

- One job per paragraph. The next paragraph answers the question the last one just raised.
- Subject and verb first. Long 的-strings go. Complete clauses, not English-word piles.
- Spoken verbs: 做成、留下、盖不住、判成、建不起来. Cut 进行了 / 实现了 / 具有……意义.
- 长短可以混，但后一句接住前一句问出来的事，不要把三层焊成一句对账。短英文从句必须扩成完整中文句子，不要压成一串英文名词。不要为了短把一段拆成半截。
- Repeat the real noun (vinifera、PIGA、singleton、SHAPEIT5). Do not rotate 该研究 / 该物种 / 这一发现.
- Judgment from the front. A data contrast is allowed (不含棉花时并系，加入后单系). A straw reader is not (你以为……其实……).
- If the PDF does not support the sentence, write `原文未说明`. No weather, facial expression, or invented lab talk.

## What not to take

- Forum clothes (老铁、谢邀)
- 1500-word public-account length
- Title hooks
- Colon / em-dash bans on the whole file
- `scripts/check_prose.py` as a note gate (it will fail YAML)

## After

Run `audit_note_prose.py --strict`. Scientific claims and numbers must match the PDF extract.
