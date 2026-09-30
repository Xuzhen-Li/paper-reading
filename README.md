# paper-reading

Cursor skill that turns **one research PDF** into a **Chinese illustrated reading note**.

把一篇研究 PDF，写成一篇中文带图阅读笔记。

This is a [Cursor](https://cursor.com) Agent slash-command skill (`/paper-reading`). Your PDF library stays on your machine.

**L3** means a full guided walkthrough of the paper（全文导读）, not a short abstract card.

Journal figures and publisher PDFs are **not** in this repo (Science / AAAS content stays on the publisher site).

## Example

**Primary — [Dong et al. 2023, *Science*](examples/2023-dong-grapevine-dual-domestication/README.md)**

*Dual domestications and origin of traits in grapevine evolution* ([10.1126/science.add8655](https://doi.org/10.1126/science.add8655)). Public crop of a local Chinese L3 note — text only.

**Secondary — [Hofmeister et al. 2023, *Nature Genetics*](examples/2023-hofmeister-shapeit5/README.md)**

SHAPEIT5 rare-variant phasing. One **repo-made** schematic only（自制示意图）, not a journal crop.

## Install

After install, open a new Cursor Agent chat and run `/paper-reading` (attach a PDF, path, or DOI).

Do **not** symlink this folder into `~/.cursor/skills/` (the skill sets `disable-model-invocation: true`; a symlink plus commands would list it twice).

```bash
git clone https://github.com/Xuzhen-Li/paper-reading.git
cd paper-reading
PKG="$(pwd)/paper-reading/paper-reading"
mkdir -p ~/.cursor/commands
sed "s|{{SKILL_DIR}}|$PKG|g" "$PKG/commands/paper-reading.md" > ~/.cursor/commands/paper-reading.md
sed "s|{{SKILL_DIR}}|$PKG|g" "$PKG/commands/精读.md" > ~/.cursor/commands/精读.md
```

Copy `paper-reading/config.example.yml` to `paper-reading/config.yml`, or set:

```bash
export PAPER_LIB_DIR=/path/to/pdf-library   # read-only
export NOTES_DIR=/path/to/notes
export FIGURES_DIR=/path/to/notes/_figures
export TMP_DIR=/path/to/tmp
```

## Use

In Cursor Agent chat:

```text
/paper-reading
```

```text
/paper-reading 润色 2026-some-note.md
```

Rules:

1. `PAPER_LIB_DIR` is read-only.
2. Notes are new markdown in `NOTES_DIR`. Same DOI already present → stop, unless you named that file.
3. Crops only under `FIGURES_DIR/<slug>/`.
4. After every write:

```bash
python3 "$PKG/scripts/audit_note_prose.py" "$NOTE" --strict
```

Do not run WeChat or HTML skills on the note in place. Copy it first.

More detail: [USAGE.md](USAGE.md).
