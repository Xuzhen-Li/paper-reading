# L3 illustrated note — order of work

Start this file only after `SKILL.md` **Ask first** confirms L3 and lists the 板块 and 深度 to keep. Do not invent extra sections.

## Paths

PDF library read-only. Backup the existing note to `TMP_DIR` before overwrite. `pdftotext` and figwork only under `TMP_DIR`. Crops under `FIGURES_DIR/<slug>/`.

## Steps

1. **Extract text** to `TMP_DIR`. Rebuild numbers from this file, not from memory.
2. **Crop figures** (`--method crop`, 3–6). Then `ls` the **png** files and open each one. A `manifest.json` without png is a fail. Caption-anchored crop often hits the title page and in-text “Fig. N” on Nature PDFs. Delete those. Renumber the real figures `fig01.png` onward. The script's `figures_count` is not the note's count.
3. **Write 导读/判断 in English first** (`en-then-zh.md`), polish that draft, translate, then Chinese-polish. The English file stays in `TMP_DIR`.

   YAML (omit empty keys) → one H1 → one DOI line → 速览卡（含作者；GitHub 全套脚本时含**代码**） → optional `## 术语对照` → `## 📖 全文导读` (paper order, lab lineage, figures nested, full Chinese sentences; English terms when the Chinese would be a calque) → 数字速查 → `## 我的判断` (paragraphs) → `## 📜 原文摘抄` (≥8, real locators) → `## ✍️ 写作学习` (**English** 原句) → 关联 (每篇论文带 DOI；本地笔记链是附加，不能代替 DOI)。

4. **Fluency is the Chinese pass** of 导读/判断 (`fluency-zh.md` + `human-writing`). Skip colon/em-dash bans. Do not dump `en_title` / 通讯 under H1. Field terms follow `terminology-zh.md`. After methods, a mermaid flowchart (sample → analysis → conclusions) with one italic line; not a paper-figure crop.
5. **Write only selected 板块.** `论文速读` means the multi-part section (背景与问题, 假说, 方法, 关键结果, 最重要的图表, 关键结论原文, 作者团队), not a telegram table that replaces `全文导读`. `代表性假说与关键论文` is the timeline inside that background, and it is separate from the one-row `研究历史` table. `关键插图` is a Fig-by-Fig read with one line under the image. `每张图的详细推演` is the long walkthrough and is not included in `关键插图`. During 每张图的详细推演, 逐模块, a Q&A 分题, or when `tu-zoom` is ticked, a paragraph about one panel gets its own crop via `scripts/mark_figure_detail.py`. A mark goes on a copy, never on `fig0N.png`, and only where the sentence points at one spot. Put every tight crop under `## 小图精讲`, each as a `###` with the panel id, the png on its own line, and one italic line that contains no other `*`. Caption 笔记裁切，不是原图, or 笔记标注，不是原图改绘. Do not leave the crop only inside the long walkthrough. `逐模块` is written only after the second card, and only for modules named from this paper's result chain. That card is AskQuestion when the tool exists. On Claude Code it is `AskUserQuestion` with `multiSelect: true` and at most 4 module names per call. On Codex it is `request_user_input_async` when listed, otherwise `request_user_input`, with at most 3 options, and every module name that did not fit is printed once per line for the user to copy into Other. Otherwise the reply is only the module list, and the note waits for the next message. An empty Codex answer is not permission to write every module. Do not copy another paper's module titles. `Q&A` stays inside questions this paper can answer; `方法讲透`, `证据链推演`, and `关键流程推演` are separate ticks. `公众号素材` writes its six parts only when the group or those parts are ticked. `后续选题` and `理论问题` are different sections. `读相关文章` only covers papers the user named or that already have a local note or PDF, and it does not download new PDFs or start another L3. Do not put SI folder paths or 「未写入 read_paper」 in the body — YAML `si_dir` / `si_inventory` only.
6. **Gate**: `audit_note_prose.py --strict`. That script also rejects preview-breaking markdown: unclosed `*` / `**`, an image sharing its line with text, an italic line that contains another `*...*`, an open code fence, and a panel crop that is not under `## 小图精讲`. Then `ls` png count = YAML `figures_count` = `![...](_figures/...)` links; `wc -l`. Open the preview: main-figure captions are complete, and each `###` under 小图精讲 shows the panel.

## Extended Data / SI

Default L3 still crops 3–6 **main** figures, **and** downloads the publisher SI into `FIGURES_DIR/<slug>/si/`. **Never** write SI into `PAPER_LIB_DIR`. L2 and sweep batches stay “no separate ESM” unless the user asks.

1. If Extended Data is already in the publisher PDF (Nature often after Methods), crop 2–4 ED figures that change a claim. Name them `edfig0N.png`. Nest them. Do not dump all ED into a gallery.
2. Separate Supplementary Information (Notes, Suppl. Figs, xlsx): save under `FIGURES_DIR/<slug>/si/`. Record `si_dir` and `si_inventory` in YAML. Never write those paths into the note body.
3. Crop 1–2 SI figures (`sfig0N.png`) only if they carry a claim main/ED figures do not (HMM diagram, sample-size SER, discovery vs subset).
4. Tables: means / key rows into 数字速查. Do not paste thousand-row sheets. Recompute counts from Data xlsx when IDs are present; if IDs were stripped, say so.
5. CC BY / CC BY-NC-ND: private note crops OK; do not redistribute adapted figures.

First full SI fold-ins: Wang 1KCP 2026; Hofmeister SHAPEIT5 2023. Prior exceptions cropped ED from the same main PDF (Haak / Fu / Mallick).

## Depth without padding

L3 means the walkthrough can be retold in order, figures exist, SI numbers that change a claim are in 数字速查, excerpts are verbatim, judgment has a confound and an underplayed limit, and the lab/competitors are named. Line-count targets are not a reason to grow or cut.
