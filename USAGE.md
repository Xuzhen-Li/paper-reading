# paper-reading — 安装与用法 / install and usage

## 中文

可移植的 Cursor 技能。一篇 PDF → 中文 L3 笔记（抽取 → 裁图 → SI 清单 → 英文草稿 → 中文导读 → 摘句 → 检查）。

### 本包是什么

`paper-reading/` 是完整技能：`SKILL.md`、`references/`、`scripts/`、`templates/`、`commands/`。

不含你的 PDF 库。把 `config.example.yml` 复制为与 `SKILL.md` 同目录的 `config.yml`，或导出环境变量（见下方「安装 / Install」中的 `export` 块）。

### 安装说明

从仓库根目录安装斜杠命令即可。不要同时软链到 `~/.cursor/skills/`：技能开了 `disable-model-invocation: true`，软链再加 command 会让 `paper-reading` 出现两次。

命令见下方「安装 / Install」。新开 Agent 对话后用 `/paper-reading`，并附上 PDF（或路径 / DOI）。润色：`/paper-reading 润色 某笔记.md`。

### 路径硬规则（给 Agent）

1. `PAPER_LIB_DIR` **只读**。禁止在其中新建、修改、删除文件。
2. 笔记写到 `NOTES_DIR` 的新 markdown。同一 DOI 已有笔记就停，除非用户点名了那个文件名。
3. 裁图只放 `FIGURES_DIR/<slug>/`。pdftotext、备份、英文草稿只放 `TMP_DIR`。
4. SI 清单进 YAML（`si_dir`、`si_inventory`），不进成稿正文。
5. 每次写完：对绝对路径 `ls` 并 `wc -l`，再跑下方检查命令。

### 本包不做的事

公众号 / 信息图 / HTML：下游技能请对笔记的**副本**操作。不要对中文笔记跑 `nature-polishing`。不要对笔记跑 `check_prose.py`，YAML 会让它失败。

## English

Portable Cursor skill. One PDF → Chinese L3 note (extract → crop → SI → English draft → Chinese guide → excerpts → check).

### What this package is

`paper-reading/` is a complete skill: `SKILL.md`, `references/`, `scripts/`, `templates/`, `commands/`.

It does **not** include your PDF library. Copy `config.example.yml` to `config.yml` next to `SKILL.md`, or export the variables in the **Install** block below.

### Install notes

Install slash commands from the clone root only. Do **not** also symlink this folder into `~/.cursor/skills/`. The skill sets `disable-model-invocation: true`. A symlink plus commands lists `paper-reading` twice.

Commands are in **Install** below. New Agent chat: `/paper-reading` and attach a PDF (or a path / DOI). Polish: `/paper-reading 润色 some-note.md`.

### Path iron rules (agents)

1. `PAPER_LIB_DIR` is **read-only**. Never create, edit, or delete files there.
2. Notes are new markdown in `NOTES_DIR`. Same DOI already present → stop, unless the user named that filename.
3. Crops only under `FIGURES_DIR/<slug>/`. pdftotext, backups, English drafts only in `TMP_DIR`.
4. SI inventory goes in YAML (`si_dir`, `si_inventory`), not in the published body.
5. After every write: `ls` the absolute path and `wc -l`. Then run the check command below.

### Not this package

Public WeChat / infographic / HTML: downstream skills on a **copy** of the note. Do not run `nature-polishing` on the Chinese note. Do not run `check_prose.py` on the note; YAML will make it fail.

## 安装 / Install

```bash
git clone https://github.com/Xuzhen-Li/paper-reading.git
cd paper-reading
PKG="$(pwd)/paper-reading"
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

```text
/paper-reading
/paper-reading 润色 2026-some-note.md
```

## 检查 / Check

```bash
python3 "$PKG/scripts/audit_note_prose.py" "$NOTE" --strict
```
