# paper-reading — install

Portable Cursor skill. One PDF → Chinese L3 note (extract → crop → SI → English draft → 中文导读 → excerpts → lint).

## What this package is

`paper-reading/` is a complete skill: `SKILL.md`, `references/`, `scripts/`, `templates/`, `commands/`.

It does **not** include your PDF library. Copy `config.example.yml` to `config.yml` next to `SKILL.md`, or export:

```bash
export PAPER_LIB_DIR=/path/to/pdf-library   # read-only
export NOTES_DIR=/path/to/notes
export FIGURES_DIR=/path/to/notes/_figures
export TMP_DIR=/path/to/tmp
```

## Install (slash commands only)

Do **not** also symlink this folder into `~/.cursor/skills/`. The skill sets `disable-model-invocation: true`. A symlink plus commands lists `paper-reading` twice.

```bash
PKG=/absolute/path/to/skill-export/paper-reading
mkdir -p ~/.cursor/commands
sed "s|{{SKILL_DIR}}|$PKG|g" "$PKG/commands/paper-reading.md" > ~/.cursor/commands/paper-reading.md
sed "s|{{SKILL_DIR}}|$PKG|g" "$PKG/commands/精读.md" > ~/.cursor/commands/精读.md
```

New Agent chat: `/paper-reading` and attach a PDF (or a path / DOI).

```text
/paper-reading
/paper-reading 润色 2026-some-note.md
```

## Path iron rules (agents)

1. `PAPER_LIB_DIR` is **read-only**. Never create, edit, or delete files there.
2. Notes are new markdown in `NOTES_DIR`. Same DOI already present → stop, unless the user named that filename.
3. Crops only under `FIGURES_DIR/<slug>/`. pdftotext, backups, English drafts only in `TMP_DIR`.
4. SI inventory goes in YAML (`si_dir`, `si_inventory`), not in the published body.
5. After every write: `ls` the absolute path and `wc -l`. Then:

```bash
python3 "$PKG/scripts/audit_note_prose.py" "$NOTE" --strict
```

## Not this package

Public WeChat / infographic / HTML: downstream skills on a **copy** of the note. Do not run `nature-polishing` on the Chinese note. Do not run `check_prose.py` on the note (YAML will fail).
