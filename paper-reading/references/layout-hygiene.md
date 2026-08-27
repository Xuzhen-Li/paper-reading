# Layout hygiene

1. YAML starts and ends with `---`. Do not wrap frontmatter in a fenced `yaml` block.
2. Omit empty values: `figures_dir: ""`, `dialogue_notes: []`, `figures_count: 0`. If figures exist, set `figures_dir: _figures/<slug>` and `figures_count: N`. If Code availability has a URL, set `code:`; omit the key when there is none. If SI was saved under `FIGURES_DIR/<slug>/si/`, set `si_dir: _figures/<slug>/si/` and `si_inventory:` (what files). Do not mention those paths in the body.
3. `title` may equal the H1. The block right under H1 is **one line**: DOI + journal + year. Do not repeat `en_title`, corresponding author, or first author (they are in YAML).
4. Nothing before YAML: no disclaimer, no polish report, no Ask-mode note.
5. Classification is a compact table or short list, not an ASCII dashboard.
6. Headings name **object + angle**. No metaphor, personification, slogan, or marketing question.

Skeleton:

```markdown
---
title: "……"
en_title: "……"
note_depth: L2
doi: 10.xxxx/xxxx
source_pdf: "relative/path.pdf"
source_pdf_abs: "/resolved/pdf"
---

# 与 title 同文的短标题

> **DOI**: […](https://doi.org/…) · *Journal* year

## 速览卡
```
