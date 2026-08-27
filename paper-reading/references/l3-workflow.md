# L3 illustrated note — order of work

Lessons from Noraz 2026 (figures) and Myles/Noraz (fluency). Follow this order. Do not invent extra sections.

## Paths

PDF library read-only. Backup the existing note to `TMP_DIR` before overwrite. `pdftotext` and figwork only under `TMP_DIR`. Crops under `FIGURES_DIR/<slug>/`.

## Steps

1. **Extract text** to `TMP_DIR`. Rebuild numbers from this file, not from memory.
2. **Crop figures** (`--method crop`, 3–6). Then `ls` the **png** files. A `manifest.json` without png is a fail. Caption-anchored crop often hits in-text “Fig. N” on early pages of Nature PDFs — open the crop, keep only true multi-panel figures, hand-pick pages if needed.
3. **Write 导读/判断 in English first** (`en-then-zh.md`), polish that draft, translate, then Chinese-polish. The English file stays in `TMP_DIR`.

   YAML (omit empty keys) → one H1 → one DOI line → 速览卡（含作者；GitHub 全套脚本时含**代码**） → optional `## 术语对照` → `## 📖 全文导读` (paper order, lab lineage, figures nested, full Chinese sentences; English terms when the Chinese would be a calque) → 数字速查 → `## 我的判断` (paragraphs) → `## 📜 原文摘抄` (≥8, real locators) → `## ✍️ 写作学习` (**English** 原句) → 关联 (每篇论文带 DOI；本地笔记链是附加，不能代替 DOI)。

4. **Fluency is the Chinese pass** of 导读/判断 (`fluency-zh.md` + `human-writing`). Skip colon/em-dash bans. Do not dump `en_title` / 通讯 under H1. Field terms follow `terminology-zh.md`. After methods, a mermaid flowchart (sample → analysis → conclusions) with one italic line; not a paper-figure crop.
5. **Do not add** `论文速读` tables, `公众号素材`, alphabet appendices, or a gallery `## 🖼️` that replaces the walkthrough. Independent figure reads go as one italic line under the image. Do not put SI folder paths or 「未写入 read_paper」 in the body — YAML `si_dir` / `si_inventory` only.
6. **Gate**: `audit_note_prose.py --strict`; `ls` png count = YAML `figures_count` = `![...](_figures/...)` links; `wc -l`.

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
