# paper-reading

## 中文

把一篇研究 PDF，写成一篇**中文带图阅读笔记**。

这是 [Cursor](https://cursor.com) Agent 的斜杠命令技能（`/paper-reading`）。PDF 库留在你自己的机器上。

**L3** 指全文导读，不是短摘要卡片。

**主案例**：[Dong 等 2023，*Science*](examples/2023-dong-grapevine-dual-domestication/README.md)  
*Dual domestications and origin of traits in grapevine evolution*（[10.1126/science.add8655](https://doi.org/10.1126/science.add8655)）。

**次案例**：[Hofmeister 等 2023，*Nature Genetics*](examples/2023-hofmeister-shapeit5/README.md)  
SHAPEIT5 稀有变异定相，含一张自制 scaffold / SER 示意。

装完后新开 Cursor Agent 对话，运行 `/paper-reading`（附上 PDF、路径或 DOI）。不要把本目录软链到 `~/.cursor/skills/`（技能开了 `disable-model-invocation: true`，再加 command 会列两次）。把 `paper-reading/config.example.yml` 复制为 `paper-reading/config.yml`，或设置下方环境变量。命令见「安装 / Install」「用法 / Use」。

规则：

1. `PAPER_LIB_DIR` 只读。
2. 笔记写到 `NOTES_DIR` 的新 markdown。同一 DOI 已有笔记就停，除非你点名了那个文件。
3. 裁图只放 `FIGURES_DIR/<slug>/`。
4. 每次写完后跑下方 lint。不要对原笔记直接跑微信或 HTML 技能；先复制一份。

更多细节：[USAGE.md](USAGE.md)。

## English

Cursor skill that turns **one research PDF** into a **Chinese illustrated reading note**.

This is a [Cursor](https://cursor.com) Agent slash-command skill (`/paper-reading`). Your PDF library stays on your machine.

**L3** means a full guided walkthrough of the paper, not a short abstract card.

**Primary:** [Dong et al. 2023, *Science*](examples/2023-dong-grapevine-dual-domestication/README.md)  
*Dual domestications and origin of traits in grapevine evolution* ([10.1126/science.add8655](https://doi.org/10.1126/science.add8655)).

**Secondary:** [Hofmeister et al. 2023, *Nature Genetics*](examples/2023-hofmeister-shapeit5/README.md)  
SHAPEIT5 rare-variant phasing, with one original scaffold / SER schematic.

After install, open a new Cursor Agent chat and run `/paper-reading` (attach a PDF, path, or DOI). Do **not** symlink this folder into `~/.cursor/skills/` (the skill sets `disable-model-invocation: true`; a symlink plus commands would list it twice). Copy `paper-reading/config.example.yml` to `paper-reading/config.yml`, or set the environment variables below. Commands are in **Install** and **Use**.

Rules:

1. `PAPER_LIB_DIR` is read-only.
2. Notes are new markdown in `NOTES_DIR`. Same DOI already present → stop, unless you named that file.
3. Crops only under `FIGURES_DIR/<slug>/`.
4. After every write, run the lint below. Do not run WeChat or HTML skills on the note in place. Copy it first.

More detail: [USAGE.md](USAGE.md).

## 安装 / Install

```bash
git clone https://github.com/Xuzhen-Li/paper-reading.git
cd paper-reading
PKG="$(pwd)/paper-reading/paper-reading"
mkdir -p ~/.cursor/commands
sed "s|{{SKILL_DIR}}|$PKG|g" "$PKG/commands/paper-reading.md" > ~/.cursor/commands/paper-reading.md
sed "s|{{SKILL_DIR}}|$PKG|g" "$PKG/commands/精读.md" > ~/.cursor/commands/精读.md
```

```bash
export PAPER_LIB_DIR=/path/to/pdf-library   # read-only
export NOTES_DIR=/path/to/notes
export FIGURES_DIR=/path/to/notes/_figures
export TMP_DIR=/path/to/tmp
```

## 用法 / Use

```text
/paper-reading
```

```text
/paper-reading 润色 2026-some-note.md
```

```bash
python3 "$PKG/scripts/audit_note_prose.py" "$NOTE" --strict
```
