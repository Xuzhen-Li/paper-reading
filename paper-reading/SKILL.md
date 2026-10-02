---
name: paper-reading
description: >-
  One research PDF → a Chinese reading note. Before any extract, crop, or
  writing, open one option card: 分级, 板块, 深度, 扩展. Attach a PDF or path.
  Slash only; do not auto-run.
disable-model-invocation: true
---

# paper-reading

One PDF, one note. Do not open on L3. Before `pdftotext`, crops, SI downloads, or any writing, open the option card, then wait.

`SKILL_DIR` = the directory that contains this file.

## Ask first

Open **one option card** with the AskQuestion tool, then wait. Do not paste this menu as a chat paragraph. Do not load `references/` before the answer. Do not extract, crop, or write before the card comes back.

Skip the card only when the same message says `直接做`, `不用问`, or `按默认`. `按默认` means the L3 set below. If the message already names some cards, pre-select those in how you read the answer, and still show the card unless one of those three phrases is present.

Title: `这次读到哪一步？`

Five questions, Chinese labels, in this order:

1. `level` — 分级。Single choice. First option is the suggestion.
   - `l3`：L3 精读（建议）
   - `l2`：L2 标准
   - `l1`：L1 速览
2. `sections-note` — 板块·笔记与速读。`allow_multiple: true`. Unticked cards are not written. （建议） is a hint, not a silent default. Only `l3-default`, or the words `按默认`, fills the L3 set.
   - `l3-default`：按默认：L3 全套（分类、速览卡、论文速读整组、关键插图、判断整组、关联整组、逐模块、Q&A）
   - `fenlei`：分类（建议）
   - `suolan`：速览卡（建议）
   - `sudu-all`：论文速读整组（建议）：背景与问题、假说、方法、关键结果、最重要的图表、关键结论原文、作者团队
   - `panduan`：判断整组（建议）：亮点、局限性、与我的关系、可引用 / 不要当作
   - `guanlian`：关联整组（建议）：同类论文、关联概念、术语速查
   - `shuyu-duizhao`：术语对照
   - `daodu`：全文导读
   - `shuzi`：数字速查
   - `zhaichao`：摘抄
   - `xiezuo`：写作学习
   - `flowchart`：方法流程图（笔记整理的流程图，不是原文图）
   - `beijing`：背景与问题
   - `jiashuo-timeline`：代表性假说与关键论文（按时间线；只收本文点名的论文，不打开那些 PDF）
   - `jiashe`：假说（本文要检验的说法，以及它推翻的说法）
   - `fangfa`：方法
   - `jieguo`：关键结果
   - `zhongyao-tu`：最重要的图表（点名哪几张，不代替逐张读图）
   - `jielun-yuanwen`：关键结论原文
   - `zuozhe`：作者团队
   - `liangdian`：亮点
   - `juxian`：局限性
   - `guanxi`：与我的关系
   - `keyinyong`：可引用 / 不要当作
   - `tonglei`：同类论文（短表：DOI 加一句关系，五到十二篇）
   - `gainian`：关联概念
   - `shuyu-sucha`：术语速查
   - `yanjiu-lishi`：研究历史（冲突表：一行一条，谁和谁相反）
   - `du-xiangguan`：读相关文章（在补充框写读几篇；不新下 PDF）
3. `sections-deep` — 板块·图、模块、问答与对外。`allow_multiple: true`. Same rule: unticked cards are not written. `l3-default` already includes 关键插图、逐模块、Q&A; it does not include the cards below those three.
   - `chatou`：关键插图（建议）：按 Fig 逐张独立读图，图下一条说明
   - `tu-tuiyan`：每张图的详细推演（Dong 2023 里 Fig.1–6 那种长推演）
   - `tu-si`：关键补充图（只收会改主张的补充图）
   - `tu-zoom`：细讲配图：讲到某一小块时裁到那一块；要指出位置时在副本上加框或短标注。勾了每张图的详细推演、逐模块，或 Q&A 分题时，这条一并生效
   - `zhumokuai`：逐模块（建议）：先读完这篇，再按这篇的结果链列模块。开读前不预设模块名
   - `qa`：Q&A 整组（建议）：只问这篇论文里解得开的问题
   - `qa-method`：方法讲透（正文用了、但没展开的方法）
   - `qa-chain`：证据链推演（从观察到结论，写清被排除的替代解释）
   - `qa-pipeline`：关键流程推演（按这篇实际用的流程，如分群或模型比较）
   - `gongzhonghao`：公众号素材整组：故事钩子、核心比喻、人物线、争议点、与普通人的连接、一句话可截图
   - `gzh-hook`：故事钩子
   - `gzh-metaphor`：核心比喻
   - `gzh-people`：人物线
   - `gzh-dispute`：争议点
   - `gzh-reader`：与普通人的连接
   - `gzh-line`：一句话可截图
   - `houxu`：后续选题（基于本文数据还能做什么）
   - `lilun`：理论问题（这篇没答完的机制问题，不是选题清单）
4. `depth` — 深度。Single choice.
   - `main-figs`：主文+主图（建议）
   - `main-only`：只读主文
   - `si-claims`：再加会改主张的补充材料
5. `extra` — 扩展。Single choice.
   - `none`：不要（建议）
   - `crops-only`：只抽图
   - `polish-words`：润色已有笔记：只改措辞
   - `polish-numbers`：润色已有笔记：对照 PDF 核数字

How the answer limits the work:

- **分级** is the ceiling. L1 and L2 do not grow into L3 because a later section feels useful.
- **板块** is the allow-list from both section questions. Unticked cards are not written, even on L3. `l3-default` writes 分类、速览卡、论文速读整组、关键插图、判断整组、关联整组、逐模块、Q&A, then adds any extra ticks. It does not add 每张图的详细推演、关键补充图、细讲配图、假说时间线、Q&A 分题、公众号小块、后续选题、理论问题, or 流程图. `tu-zoom` also turns on when 每张图的详细推演、逐模块, or a Q&A 分题 is selected. A group option writes that whole group; a single card writes only that card. `论文速读` does not replace `全文导读` when both were ticked. `研究历史` is the one-row conflict table. `代表性假说与关键论文` is the timeline writeup. Both stay inside papers this PDF names. `同类论文` stays a short DOI table. `理论问题` is not `后续选题`. `读相关文章` does not start another L3 and does not download new PDFs. If `读相关文章` is ticked and the note does not say how many, ask once for the number on that same second card, not in a later card. A free-text answer such as `可以下` allows open PDFs of papers this article cites, capped at five, preferring ones that already have a local note. Do not stall the note on a failed download. If no PDF was fetched, say so in that section. Do not start another L3.
- **逐模块** has no fixed list. Dong 2023's modules belong to that paper only. If `zhumokuai` or `l3-default` is selected: extract and read this PDF first, then open **one** second AskQuestion card before writing `## 逐模块`. Title: `这篇的模块，写哪些？` That same call includes `related-n` when 读相关文章 was ticked without a number. Do not ask in a later card. Options for modules come from this paper's result chain, `allow_multiple: true`, plus `all`（这篇的全部模块）. Each label is this paper's own step, one line on what it covers. Do not reuse another note's module titles. Wait. Write only the ticked modules. If none are ticked, write no modules. Other selected 板块 wait for this card too, so the note is written once.
- **深度** chooses how far into the paper those sections go. `只读主文`: no crops, no SI download. `主文+主图`: crop 3–6 main figures. `补充材料`: the SI rules below, and only numbers or figures that change a claim.
- **扩展** is off the main path. `只抽图` crops and stops. If a note for this PDF already exists, either polish option polishes only the ticked 板块 and does not re-extract unless figures are missing. If no note exists, `润色` does not replace the read: write the selected 板块, then run that polish pass on the new draft. Q&A is a 板块, not an extension.

A polish-only request still opens the card. Suggest `none` on 扩展 only when they did not already say 润色. If they said 润色, the suggestion on 扩展 is `polish-words`, and 板块 is which sections to polish.

After they answer, load what that job needs. L1: [references/claim-evidence.md](references/claim-evidence.md) and [references/banned-phrases.md](references/banned-phrases.md). L2: those two, plus [references/terminology-zh.md](references/terminology-zh.md), [references/prose-style-zh.md](references/prose-style-zh.md), [references/layout-hygiene.md](references/layout-hygiene.md), and [templates/note-l2.md](templates/note-l2.md). L3, in order:

1. [references/l3-workflow.md](references/l3-workflow.md)
2. [references/terminology-zh.md](references/terminology-zh.md)
3. [references/lineage-and-related.md](references/lineage-and-related.md)
4. [references/en-then-zh.md](references/en-then-zh.md)
5. [references/fluency-zh.md](references/fluency-zh.md)
6. [references/layout-hygiene.md](references/layout-hygiene.md)
7. [references/banned-phrases.md](references/banned-phrases.md)
8. [references/claim-evidence.md](references/claim-evidence.md)
9. [references/prose-style-zh.md](references/prose-style-zh.md)
10. [references/density-dedup.md](references/density-dedup.md)
11. [references/zh-polish-order.md](references/zh-polish-order.md)

If `human-writing` is installed (`~/.cursor/skills/human-writing/SKILL.md`), load it plus `forum-prose.md` and `reality.md`, then `revision.md` passes 1–4 and 6–7. **Skip pass 5** (colon / em dash). Diagnose paragraph jobs before editing sentences (`zh-polish-order.md`). Do not run `check_prose.py` on the note. English walkthroughs in `TMP_DIR` may use `nature-polishing` stance (terminology ledger, methods-paper questions). Never run `nature-polishing` on the Chinese note.

Public copy / 信息图: [references/downstream.md](references/downstream.md), on a **copy** of the note.

## Paths

Resolve `PAPER_LIB_DIR`, `NOTES_DIR`, `FIGURES_DIR`, `TMP_DIR` from, in order:

1. Environment variables of those names
2. `config.yml` next to this `SKILL.md`, or one directory above the `skills/` folder
3. If these folders exist, use them (local reading pipeline):

| Name | Default |
|------|---------|
| `PAPER_LIB_DIR` | `~/Desktop/read_paper` |
| `NOTES_DIR` | `~/Desktop/script/AI_lib/papers` |
| `FIGURES_DIR` | `~/Desktop/script/AI_lib/papers/_figures` |
| `TMP_DIR` | `~/Desktop/script/AI_lib/projects/read-paper-sweep/tmp` |

`PAPER_LIB_DIR` is **read-only**. Never create, edit, or delete files there. Notes are markdown in `NOTES_DIR`. Figures only under `FIGURES_DIR/<slug>/`. pdftotext, backups, and figwork only in `TMP_DIR`. Do not `rm` an existing note; backup to `TMP_DIR` first. After every write: `ls` the absolute path and `wc -l`.

## Which job

| User says | Job |
|-----------|-----|
| `/paper-reading` or `/精读` plus a PDF / path / DOI | Option card first. L3 only after they pick it |
| `/paper-reading L2` | Still open the card. Suggestion on 分级 is L2, not a silent start |
| `/paper-reading 润色` plus a named note | Polish that note; do not re-extract unless figures are missing |
| `/paper-reading 抽图` | Crops only, then stop |
| `/paper-reading` plus `SI` / `ESM` / 补充材料 | Same as L3; SI is already default (see l3-workflow) |

Skip preprints and off-list venues unless the user names them. If `NOTES_DIR` already has the same DOI, **stop and say so**. Overwrite only when the user names that filename.

## L3 精读 (one shot)

Run this only after Ask first confirms L3, and only for the 板块 and 深度 they kept. Write a 板块 only when they selected it, including 论文速读, 关键插图, 逐模块, Q&A, 研究历史, 读相关文章, 公众号素材, and 后续选题. Do not invent extra blocks. Write 导读/判断 by the English-then-Chinese path in `en-then-zh.md` when 全文导读 or 判断 is selected (English file stays in `TMP_DIR`).

1. **DOI / skip.** Identify the article. Search `NOTES_DIR` for the DOI. Filename: `{year}-{author}-{keywords}-{journal}.md` (no DOI-only names).

2. **Text.** `pdftotext -layout` the PDF into `TMP_DIR`. Rebuild every number from that extract. If the text layer prints a placeholder such as `xx xx xxxx`, leave it as a placeholder. Do not fill it from a screenshot description. If 逐模块 was selected, read this extract and open the second module card before any writing. Module titles come from this paper only. When 读相关文章 is also waiting on a number, that card is the same AskQuestion call.

3. **Figures.** Crop 3–6 **main** figures:

```bash
python3 "$SKILL_DIR/scripts/extract_paper_figures.py" \
  --pdf "$PDF" --slug "$SLUG" --method crop --max-keep 6 \
  --figures-dir "$FIGURES_DIR" --tmp-dir "$TMP_DIR"
```

Then `ls` the **png** files. A `manifest.json` without png is a fail. The script's `figures_count` is not the note's `figures_count`. Nature PDFs often mention “Fig. N” in early body text — those crops are not figures. Open each png. Delete a title page, a prose page, and a caption-only page. Keep true multi-panel figures, in paper order, and rename them `fig01.png` onward. A hand crop replaces the script crop; do not leave the rejected pngs in the figure folder.

**细讲配图.** On for `tu-zoom`, and also for 每张图的详细推演、逐模块, and a Q&A 分题. 关键插图 alone keeps the whole figure. When a paragraph is about one panel or one spot, do not leave the reader on the full figure. Crop that region to a new png. If the sentence points at a place that is easy to miss, mark it on a second copy. Look at the image and set the box from what you see. Never overwrite `fig0N.png`.

Write these crops under their own heading, `## 小图精讲`, not only inside a paragraph of 详细推演. The outline has to show that heading. Each spot is a `###` with the panel id (`### Fig. 2b–c`), the png on its own line, then one italic line. That line starts and ends with a single `*`, contains no other `*`, and says 笔记裁切，不是原图, or 笔记标注，不是原图改绘 when the copy has a box. A mark whose label covers a legend, an axis, or a data point is deleted; keep the unmarked crop. Do not link both copies of the same panel.

```bash
python3 "$SKILL_DIR/scripts/mark_figure_detail.py" \
  --src "$FIGURES_DIR/$SLUG/fig03.png" \
  --out "$FIGURES_DIR/$SLUG/fig03-panel-b.png" \
  --crop 40,80,520,640
python3 "$SKILL_DIR/scripts/mark_figure_detail.py" \
  --src "$FIGURES_DIR/$SLUG/fig03-panel-b.png" \
  --out "$FIGURES_DIR/$SLUG/fig03-panel-b-note.png" \
  --mark 30,20,180,160 --label "b 渐渗"
```

`--crop` and `--mark` are `left,top,right,bottom` in pixels, origin top-left. `--mark` is measured on the output. Open the crop before linking it. If the file is the wrong panel, delete it and crop again. If a label covers a legend, an axis, or a data point, delete that marked copy and keep the unmarked crop. Link the crop from `## 小图精讲` only. The label is a few words naming what the box is. Do not mark every panel, do not redraw the figure, and do not add a number the paper does not show. A linked panel or marked png counts in `figures_count`. Delete a crop the note does not use. An italic caption that also italics a gene name breaks the preview: leave the name in roman, or drop the outer italics.

**L3 downloads SI** (publisher ESM / Suppl. Figs / Data xlsx) into `FIGURES_DIR/<slug>/si/`. Never into `PAPER_LIB_DIR`. If Extended Data is already in the same PDF, crop 2–4 `edfig0N.png` that change a claim. From the separate SI, crop 1–2 `sfig0N.png` only if they carry a claim main/ED figures do not. Tables: key rows into 数字速查. L2 still skips a separate ESM unless the user asks.

4. **Write via English then Chinese** ([references/en-then-zh.md](references/en-then-zh.md); skeleton: [templates/note-l3.md](templates/note-l3.md)):

   YAML (omit empty keys) → one H1 → one DOI line → 速览卡（**必须有作者**；Code availability 有 GitHub/GitLab **全套脚本**时必须有**代码**行） → optional `## 术语对照` → `## 📖 全文导读` → 数字速查 → `## 我的判断` → `## 📜 原文摘抄` (≥8, real locators) → `## ✍️ 写作学习` (English 原句) → 关联（每篇论文带 DOI；本地笔记链不能代替 DOI）。

   导读 is paper order: 全景（这篇做了什么、什么材料数据、主结论一句）→ 实验室与方法家族 → gap → design → Fig.1… → SI if it changes a claim → close. Each kept figure is nested where the result lives, with **one italic line** under the image. Spoken **Chinese sentences**, not English nouns glued together. Unstable terms stay English (`singleton`). Numbers hang on the sentence. Exact table dumps wait in 数字速查. Length follows the extract and SI; do not compress.

   **Code availability.** Read that section (and Data availability if it points to scripts). YAML `code:` gets the URL. If GitHub/GitLab (or a Zenodo tarball) has a **full script set**—tools plus pipelines/scripts that can rerun the paper, not a binary-only dump—**must** put a 速览卡 **代码** row: URL, license, what is in the repo. Repeat once in 数字速查. Do not leave the repo only in YAML. “Upon request” / no repo: say so in 许可; omit the 代码 row. Do not claim 全套脚本 unless the listing or README shows it.

   After the methods paragraphs and before the first result figure, add a **mermaid** flowchart: sample → data → analysis → main conclusions. One italic line under it: 笔记整理，不是原文图. Do not save this as a fake paper figure in `_figures/`.

   **SI stays in YAML.** If SI was downloaded, set `si_dir:` and `si_inventory:` in frontmatter. Do **not** write `_figures/<slug>/si/` paths, MOESM file lists, or 「未写入 read_paper」 in the body. Those are unpublished properties. Nest an SI figure in 导读 only when it changes a claim (`sfig0N.png`), with a caption about the science, not the folder.

5. **Judgment** in paragraphs, not labels. Data highlight, confound, author-underplayed limit, 「可引用 / 不要当作」. Cornwell stays in this prose. Do not stamp `AI 初判`. After the first Chinese draft, walk [references/zh-polish-order.md](references/zh-polish-order.md) (six steps). Then gate.

6. **Gate.** The preview check is part of this script. It fails the note when markdown would hide the rest of a paragraph or the next image: an unclosed `*` or `**`, an image that shares its line with other text, an italic caption that contains another `*...*`, or a code fence left open. A tight crop captioned 笔记裁切 or 笔记标注 without `## 小图精讲` also fails, as does a 小图精讲 section that only links the whole figure.

```bash
python3 "$SKILL_DIR/scripts/audit_note_prose.py" "$NOTE" --strict
```

`ls` png count = YAML `figures_count` = `![...](_figures/...)` links. Report the absolute path and `wc -l`. Open the note preview after the gate: each main figure shows its caption, and each `###` under `## 小图精讲` shows the panel, not a cut-off page.

## Polish only

Backup the named note to `TMP_DIR`. Order: layout → strip process talk → narrative before tables → claim verbs → Chinese prose + fluency → density. Do not invent numbers. If the PDF does not say it, write `原文未说明`. Same gate as above.

## Do not

- Run `nature-polishing` / `nature-writing` / `nature-reviewer` on the whole Chinese note
- Rewrite the note as a Zhihu post or apply baoyu title formulas
- Put generated infographics in `_figures/`
- Fill methods from textbook knowledge
- Pad to a line-count target, or shrink past SI / author-contribution facts that change a claim
- Calque unstable terms (`singleton` → 单例变异, `haplotype scaffold` → 单倍型骨架) or compress 导读 into glued English nouns
- Put Chinese paraphrase in `## ✍️ 写作学习` 原句 (English verbatim only)
- Replace a technical action with a spoken verb (`丢进 hifiasm`, `随机派`, `产数据`, `装不满`) — rewrite the paragraph
- Start every 导读 / 判断 paragraph with 作者
- Write SI folder paths, MOESM inventories, or 「未写入 read_paper」 in the published body — put them in YAML `si_dir` / `si_inventory`
