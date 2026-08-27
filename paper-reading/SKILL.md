---
name: paper-reading
description: >-
  One research PDF → Chinese L3 illustrated note (导读, cropped figures,
  excerpts, 判断). Attach a PDF or path. Add 润色 and a note filename to
  polish. Slash only; do not auto-run.
disable-model-invocation: true
---

# paper-reading

One call, one note. Default job is **L3 精读** at the quality of the Wang 1KCP / Noraz / Myles tests: a colleague talking through the PDF with figures in place, not a telegram dump and a later “polish”.

`SKILL_DIR` = the directory that contains this file.

Load next, in order:

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
| `/paper-reading` or `/精读` plus a PDF / path / DOI | **L3 精读** (this file’s main path) |
| `/paper-reading L2` | L2: same shape, shorter 导读, no bulk crops |
| `/paper-reading 润色` plus a named note | Polish that note; do not re-extract unless figures are missing |
| `/paper-reading 抽图` | Crops only, then stop |
| `/paper-reading` plus `SI` / `ESM` / 补充材料 | Same as L3; SI is already default (see l3-workflow) |

Skip preprints and off-list venues unless the user names them. If `NOTES_DIR` already has the same DOI, **stop and say so**. Overwrite only when the user names that filename.

## L3 精读 (one shot)

Do not add `论文速读`, 公众号素材, or lettered appendices. Write 导读/判断 by the English-then-Chinese path in `en-then-zh.md` (English file stays in `TMP_DIR`).

1. **DOI / skip.** Identify the article. Search `NOTES_DIR` for the DOI. Filename: `{year}-{author}-{keywords}-{journal}.md` (no DOI-only names).

2. **Text.** `pdftotext -layout` the PDF into `TMP_DIR`. Rebuild every number from that extract.

3. **Figures.** Crop 3–6 **main** figures:

```bash
python3 "$SKILL_DIR/scripts/extract_paper_figures.py" \
  --pdf "$PDF" --slug "$SLUG" --method crop --max-keep 6 \
  --figures-dir "$FIGURES_DIR" --tmp-dir "$TMP_DIR"
```

Then `ls` the **png** files. A `manifest.json` without png is a fail. Nature PDFs often mention “Fig. N” in early body text — those crops are not figures. Open each png; keep true multi-panel evidence; hand-pick pages if needed.

**L3 downloads SI** (publisher ESM / Suppl. Figs / Data xlsx) into `FIGURES_DIR/<slug>/si/`. Never into `PAPER_LIB_DIR`. If Extended Data is already in the same PDF, crop 2–4 `edfig0N.png` that change a claim. From the separate SI, crop 1–2 `sfig0N.png` only if they carry a claim main/ED figures do not. Tables: key rows into 数字速查. L2 still skips a separate ESM unless the user asks.

4. **Write via English then Chinese** ([references/en-then-zh.md](references/en-then-zh.md); skeleton: [templates/note-l3.md](templates/note-l3.md)):

   YAML (omit empty keys) → one H1 → one DOI line → 速览卡（**必须有作者**；Code availability 有 GitHub/GitLab **全套脚本**时必须有**代码**行） → optional `## 术语对照` → `## 📖 全文导读` → 数字速查 → `## 我的判断` → `## 📜 原文摘抄` (≥8, real locators) → `## ✍️ 写作学习` (English 原句) → 关联（每篇论文带 DOI；本地笔记链不能代替 DOI）。

   导读 is paper order: 全景（这篇做了什么、什么材料数据、主结论一句）→ 实验室与方法家族 → gap → design → Fig.1… → SI if it changes a claim → close. Each kept figure is nested where the result lives, with **one italic line** under the image. Spoken **Chinese sentences**, not English nouns glued together. Unstable terms stay English (`singleton`). Numbers hang on the sentence. Exact table dumps wait in 数字速查. Length follows the extract and SI; do not compress.

   **Code availability.** Read that section (and Data availability if it points to scripts). YAML `code:` gets the URL. If GitHub/GitLab (or a Zenodo tarball) has a **full script set**—tools plus pipelines/scripts that can rerun the paper, not a binary-only dump—**must** put a 速览卡 **代码** row: URL, license, what is in the repo. Repeat once in 数字速查. Do not leave the repo only in YAML. “Upon request” / no repo: say so in 许可; omit the 代码 row. Do not claim 全套脚本 unless the listing or README shows it.

   After the methods paragraphs and before the first result figure, add a **mermaid** flowchart: sample → data → analysis → main conclusions. One italic line under it: 笔记整理，不是原文图. Do not save this as a fake paper figure in `_figures/`.

   **SI stays in YAML.** If SI was downloaded, set `si_dir:` and `si_inventory:` in frontmatter. Do **not** write `_figures/<slug>/si/` paths, MOESM file lists, or 「未写入 read_paper」 in the body. Those are unpublished properties. Nest an SI figure in 导读 only when it changes a claim (`sfig0N.png`), with a caption about the science, not the folder.

5. **Judgment** in paragraphs, not labels. Data highlight, confound, author-underplayed limit, 「可引用 / 不要当作」. Cornwell stays in this prose. Do not stamp `AI 初判`. After the first Chinese draft, walk [references/zh-polish-order.md](references/zh-polish-order.md) (six steps). Then gate.

6. **Gate.**

```bash
python3 "$SKILL_DIR/scripts/audit_note_prose.py" "$NOTE" --strict
```

`ls` png count = YAML `figures_count` = `![...](_figures/...)` links. Report the absolute path and `wc -l`.

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
