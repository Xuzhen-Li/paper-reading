# Downstream content pipeline (not this pack)

`paper-reading-kit` stops at a literature note: facts, walkthrough, excerpts, cropped paper figures. Public writing, infographics, and posting live **after** the note exists.

They are stations, not substitutes.

```
PDF (read-only)
  -> paper-deep-read + figure-extract
  -> paper-note-polish
  -> [optional] public article / figure / HTML
```

## What to load when

| Job | Load | Do not |
|-----|------|--------|
| Read a paper into a note | this pack | baoyu title formulas |
| Polish 导读 / 判断 so it reads like a person | `paper-note-polish` + `human-writing` (fluency; skip colon/em-dash bans) | rewrite the note as a Zhihu post; run `check_prose.py` on the whole file |
| WeChat / Zhihu / 口播 from a finished note | `human-writing` on a **copy** | overwrite `NOTES_DIR/*.md` with 论坛腔 or 标题钩子 |
| Infographic, 小红书卡, 公众号 HTML | `baoyu-infographic` / `baoyu-xhs-images` / `baoyu-markdown-to-html` | put generated art into `_figures/` as if it were a paper figure |
| Flow / architecture with exact Chinese labels | `baoyu-diagram` (SVG) | raster infographic for numbers |
| One-file shareable page | `html-express` | replace the markdown note |
| Recurring illustrated column | `ian-xiaohei-illustrations` | data figures or paper crops |

`baoyu-format-markdown` may tidy a **public draft**. It must not re-title a literature note or inject hook formulas.

## Fluency on the note itself

导读 and 判断 load `human-writing` (forum-prose + revision). Skip colon/em-dash bans and `check_prose.py` on the whole file. Do not rewrite as a Zhihu post. Details: `skills/paper-note-polish/references/fluency-zh.md`.

## Figures stay in two piles

| Pile | What | Where |
|------|------|--------|
| Paper evidence | cropped from the PDF | `FIGURES_DIR/<slug>/` |
| Communication art | infographic, 小黑, 封面 | a public-draft folder, never `_figures/` |

Generated images with Chinese labels need a human pass before posting. Wrong characters in a methods diagram are worse than no diagram.
