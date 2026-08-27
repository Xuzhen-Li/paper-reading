# paper-reading

Homemade Cursor skill. One research PDF to one Chinese L3 illustrated note.

Pipeline: extract → crop → SI inventory → English draft → Chinese guide → excerpts → lint.

This repository is the shareable skill. Your PDF library stays on your machine.

## Install

Do **not** symlink the folder into `~/.cursor/skills/` (the skill sets `disable-model-invocation: true`; a symlink plus commands would list it twice).

```bash
git clone https://github.com/Xuzhen-Li/paper-reading.git
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

New agent chat, attach a PDF (or a path / DOI):

```text
/paper-reading
```

```text
/paper-reading polish 2026-some-note.md
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

Full steps: [USAGE.md](USAGE.md). Agent entry: [paper-reading/SKILL.md](paper-reading/SKILL.md).

## License

MIT.
