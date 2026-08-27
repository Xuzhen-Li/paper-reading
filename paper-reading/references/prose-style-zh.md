# Chinese note prose

Write a literature card a colleague can reread. Not a Nature article, not a model narrating its work.

## Paragraph

- One recognisable claim per paragraph. Claim first; evidence, comparison, bound after.
- Write complete Chinese sentences. Do not calque English compounds (`haplotype scaffold` → 单倍型骨架). If the term has no settled Chinese, keep English and gloss.
- 判断段：两层判断不要焊在一句里。叙述段不设句长上限，改查句子完整性（谁、主动词、代词落处）。不要为了短而拆，也不要为了密而焊。
- 导读第一段是全景段：这篇做了什么、用什么材料和数据、拿到的主结论一句。背景、领域现状放第二段起，不能当开头。
- 亲本方向写「更像父亲还是更像母亲 / 母本传来的」，不写「像父还是像母」。
- Transitions come from real relations (cause, contrast, comparison, condition). Do not buy fluency with 此外 / 另一方面 / 在此基础上 / 进一步地.
- Name the actor: 作者 / Delaneau / SHAPEIT5 / Beagle. Avoid stacked 本文 / 该研究 / 其 / 这表明。不要每段都用「作者」起头。判断段先挡住最容易的误读（读者会当成什么），再写作者实际测到什么。不相容不等于已经知道原因。样张：`AI_lib/articles/古人类演化/evolutionary-rescue.md`。

## Rhythm tells to break

- Mechanical lists of three modifiers
- Repeated 不仅……而且……
- Same sentence length and same SVO shape for a whole section
- Clustered 值得注意 / 综上所述 / 总的来说
- Hedge stacks: 可能潜在表明
- The same point said three times in a closing paragraph

## Empty or fake-emphatic language

| Cut or rewrite | Replace with |
|----------------|--------------|
| 具有重要意义、填补空白、深入揭示 | which tree, accession, or bias changed |
| 首先/其次/再次/最后 as scaffolding | a condition sentence: 不含棉花时…加入后… |
| 值得注意的是、不难发现、可以说、在某种程度上 | a number, or delete |
| 这里我们表明、这一发现凸显了 | who did what and what number came out |
| 仍需进一步研究、可能存在潜在局限 | the actual missing partition, cultivar, or clade |

Keep Latin names, accessions, tree lengths, bootstrap, DOI, and 「可引用 / 不要当作」。

Then run `references/fluency-zh.md` on 导读 and 判断. Subject first, spoken verbs, mixed sentence length. Load `human-writing` if installed.

「显著」 only with a statistical test. 「强 / 大幅 / 全面 / 系统」 need a number, a comparator, or a stated coverage.

## Materials, not atmosphere

A thin PDF does not become a long note by restating the same claim. If a scene, quote, or number is not in the paper or the user, omit it. Fake lab atmosphere (天气、神态、有人说) is worse than a short card. Do not compress a real explanation into a four-word calque.

Do not open a judgment with a straw reader (`不是……而是……` / `你以为……其实……`) unless the note has already walked a real correction in the data. A contrast the figures actually show is fine.

Do not close with 时代意义 or a second abstract.

## 判断怎么起头

先写「不要当成」，再写「可引用」。不要新开 `##` 框、`##` 附录、编辑按。笔记结构仍是速览卡 → 导读 → 数字速查 → 我的判断 → 摘抄。

让步判断（样张 `AI_lib/articles/古人类演化/evolutionary-rescue.md`）：救援是让步，不是证明种群已经被救下来。看到「先下降、再恢复」还不能宣布进化救援；恢复可以有环境变好、迁入等纯生态原因。

零假设判断：不相容 ≠ 已知原因。偏离 HWE 只挡住「样本像随机交配的一个群体」；它不告诉你是 Wahlund、近交、分型错误，还是别的哪一种。

初稿完成后走 [zh-polish-order.md](zh-polish-order.md)。
