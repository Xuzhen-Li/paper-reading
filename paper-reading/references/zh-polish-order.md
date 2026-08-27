# Chinese polish order (notes)

Borrowed from `famous-bio` `write-body.md` / `reader-voice.md`: diagnosis before sentence work, whole-paragraph rewrite, fail-even-if-green shapes. Do **not** take WeChat length bands, title formulas, `check_prose.py`, or a live-literature ending hook.

Apply to Chinese **narrative** only: 速览卡「一句话」、`## 📖 全文导读`、`## 我的判断`. Leave YAML, tables, English excerpts, locators, DOI, and figure paths alone.

## 顺序

After the first Chinese draft, walk these in order. If any pass still finds translated syntax, a half-sentence, or editorial leakage, return to the **whole paragraph**, not the offending word.

1. **Paragraph diagnosis.** Privately label each paragraph as action, evidence, explanation, background, or judgment. Move or delete paragraphs doing the wrong job before editing sentences.
2. **Whole-paragraph rewrite.** If a paragraph follows English clause order, reads like an abstract, or was assembled by patching warnings, put its wording aside. Rewrite from the PDF extract. Do not replace isolated words and call it polished.
3. **Sentence integrity.** For every prose sentence, identify the actor and main verb. Rewrite fragments, compressed predicates, and pronouns whose subject exists only in the writer's notes. Narrative paragraphs have **no English sentence-length cap**. 「一句一层」applies only to **judgment**: two layers of inference must not be welded into one sentence.
4. **Reader-only pass.** Remove process talk, verification theater, and explanations written for an editor. Do not start every paragraph with 作者. A methods note may name the lab once; it must not become a Crossref log.
5. **Read aloud.** Inspect eight consecutive paragraphs for repeated cadence, forced short closers, formulaic openings, and compulsory hand-offs. A paragraph may finish normally.
6. **Mechanical gates last.** Run `audit_note_prose.py --strict`. Pass is necessary. It does not prove the Chinese is natural.

Keep a terminology ledger only for scientific terms, names, symbols, and units (`terminology-zh.md`). Do not turn common Chinese words into a substitution table. Spoken verbs in methods (`丢进`、`随机派`、`装不满`) are fixed by rewriting the paragraph, not by a ban list.

## 判不合格的形状

Fail the note on these even if `audit_note_prose.py` is green. Examples are from real notes (Otava 2022; SHAPEIT5 2023).

| 形状 | 长什么样 | 怎么改 |
|------|----------|--------|
| 电报腔 | 「塌掉的那一段，后面几乎正好对上 IBD。」 | 写成完整句子：近乎相同的区段在初始组装里塌缩成一条 contig；这些塌缩区域后来和 IBD 块对上。 |
| 英文分句逐项转写 | 连续抽象名词、没有主动词的半句；「芯片时代的单倍型定相已经能扛几十万人。」 | 放下英文词序，从已核事实重写整段：谁、对什么材料、做了什么、数字是多少。 |
| 每段主语都是「作者」 | 「作者写成…／作者认为…／作者报…」连排 | 数字、图表、材料当主语。作者只在判断、推测、讨论立场处出场。 |
| 导读用背景开头，全景段缺失 | 第一段就是「商业马铃薯多半是无性繁殖的杂合同源四倍体。」读者还不知道这篇装成了什么 | 第一段写这篇做了什么、用什么材料和数据、主结论一句。背景放到全景和实验室段之后。 |
| 作者段夹在方法中间 | 先讲 trio binning 失效，再插通讯作者单位，再回头讲材料 | 作者段紧跟全景段。圈内熟面孔先一两句因什么出名，本文分工不超过两句。 |
| 口语替专业动作词 | 「先把 Otava 的 HiFi 直接丢进 hifiasm。」「读段随机派。」「产数据。」「初始 2.2 Gb 装不满。」 | 整段重写动作：交给 hifiasm 做初始组装；比对后归到各条 haplotype；产生测序数据；初始组装总长只有 2.2 Gb，约占四倍体大小的 65%。 |
| 术语硬拼或口语化 | 「单倍型骨架」「加倍单倍体」「塌掉」「分箱」「像父还是像母」 | 无公认中文则留英文并解释（`haplotype scaffold`、`doubled monoploid`）。有公认中文则用中文（塌缩区域、定相）。亲本方向写「更像父亲还是更像母亲」。方法名 `trio binning` / `gamete binning` 留英文。 |
| 判断段先给结论、没有先挡误读 | 一上来就报 99.6%、3.1 Gb，读者会把「haplotype 解析」读成四套处处不同 | 先写不要当成什么，再写作者实际测到什么。不相容不等于已经知道原因。 |
| 串篇 | 「Beagle 式的对照在这里不存在。」Beagle 是上一篇 SHAPEIT5 笔记的对照工具，与 Otava 组装无关 | 只写本篇真正的前身与后续。删掉上一篇论文留在缓存里的工具名。 |

`audit_note_prose.py --strict` 通过是必要条件，不证明中文自然。
