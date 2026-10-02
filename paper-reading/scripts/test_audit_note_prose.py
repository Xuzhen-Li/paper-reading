#!/usr/bin/env python3
"""Unit tests for audit_note_prose (no PDF, no library walk)."""

from __future__ import annotations

import unittest
from pathlib import Path

import audit_note_prose as anp

GOOD_L3 = """---
title: "Good note"
en_title: "A real title"
note_depth: L3
doi: 10.1038/example
source_pdf: "folder/paper.pdf"
figures_dir: "_figures/good-note"
figures_count: 2
---

# Good note

> **DOI**: [10.1038/example](https://doi.org/10.1038/example) · *Nature* 2024

## 速览卡

一句话。

## 📖 全文导读

作者给出一个结果。

![Fig.1](_figures/good-note/fig01.png)

## 📜 原文摘抄

> **EN**: "We report X."
"""

EMPTY_YAML = """---
title: "Empty yaml"
note_depth: L2
figures_dir: ""
dialogue_notes: []
figures_count: 0
---

# Empty yaml

> **DOI**: 10.1/x
"""

META_NOTE = """---
title: "Meta"
note_depth: L2
---

# Meta

> [AI 初判·待人核]

## 自检

Target 420 lines
"""

L3_NO_NARRATIVE = """---
title: "No walk"
note_depth: L3
---

# No walk

## 📜 原文摘抄

quote
"""

BAD_FIG_LINK = """---
title: "Bad fig"
note_depth: L3
---

# Bad fig

## 📖 全文导读

![Fig.1](assets/fig01.png)

## 📜 原文摘抄

quote
"""

OPENING_DUMP = """---
title: "Dump"
en_title: "English Title Here"
corresponding: "Ada Lovelace"
first_author: "Ada Lovelace"
note_depth: L2
---

# Dump

> **EN**: *English Title Here*
> **通讯**: Ada Lovelace
> **一作**: Ada Lovelace
"""

SLOP_DENSE = """---
title: "Slop"
note_depth: L2
---

# Slop

这篇工作具有重要意义，填补空白。值得注意的是，首先，其次，再次，最后。
"""


NESTED_ITALIC = """---
title: "Nested"
note_depth: L2
---

# Nested

*HPG1 的采样点，以及 *rtel1-1* 两条缺失。*
"""

SEPARATE_ITALICS = """---
title: "Separate"
note_depth: L2
---

# Separate

插入 *U* = 20，*P* = 1.000。
"""

UNCLOSED = """---
title: "Unclosed"
note_depth: L2
---

# Unclosed

这句话的斜体没有收口 *

![Fig.1](_figures/unclosed/fig01.png)
"""

IMAGE_WITH_TEXT = """---
title: "Image text"
note_depth: L2
---

# Image text

见图 ![Fig.1](_figures/image-text/fig01.png) 的 a 面板。
"""

ZOOM_BURIED = """---
title: "Buried"
note_depth: L2
---

# Buried

![panel](_figures/buried/fig02-indel.png)

*笔记裁切，不是原图。*
"""

ZOOM_WHOLE = """---
title: "Whole"
note_depth: L2
---

# Whole

## 小图精讲

![Fig.1](_figures/whole/fig01.png)

*笔记裁切，不是原图。*
"""

ZOOM_OK = """---
title: "Zoom ok"
note_depth: L2
---

# Zoom ok

## 小图精讲

### Fig. 3c

![Fig. 3c](_figures/zoom-ok/fig03-panel-bc-note.png)

*笔记标注，不是原图改绘。红框圈住引进的那段。*
"""


class AuditNoteProseTest(unittest.TestCase):
    def test_good_l3_clean(self) -> None:
        result = anp.audit_text(GOOD_L3, slug="good-note")
        self.assertEqual(result["errors"], [], result)

    def test_empty_yaml_keys(self) -> None:
        result = anp.audit_text(EMPTY_YAML, slug="empty-yaml")
        codes = {e["code"] for e in result["errors"]}
        self.assertIn("empty_yaml_field", codes)

    def test_ai_meta_phrases(self) -> None:
        result = anp.audit_text(META_NOTE, slug="meta")
        codes = {e["code"] for e in result["errors"]}
        self.assertIn("process_meta", codes)

    def test_l3_missing_walkthrough(self) -> None:
        result = anp.audit_text(L3_NO_NARRATIVE, slug="no-walk")
        codes = {e["code"] for e in result["errors"]}
        self.assertIn("missing_l3_walkthrough", codes)

    def test_figure_link_not_under_slug(self) -> None:
        result = anp.audit_text(BAD_FIG_LINK, slug="bad-fig")
        codes = {e["code"] for e in result["errors"]}
        self.assertIn("figure_link_not_under_slug", codes)

    def test_opening_repeats_yaml(self) -> None:
        result = anp.audit_text(OPENING_DUMP, slug="dump")
        codes = {e["code"] for e in result["errors"]}
        self.assertIn("opening_repeats_yaml", codes)

    def test_chinese_slop(self) -> None:
        result = anp.audit_text(SLOP_DENSE, slug="slop")
        codes = {e["code"] for e in result["errors"]}
        self.assertTrue(
            {"empty_significance", "formulaic_sequence"} & codes,
            result,
        )

    def test_nested_italic_breaks_preview(self) -> None:
        result = anp.audit_text(NESTED_ITALIC, slug="nested")
        codes = {e["code"] for e in result["errors"]}
        self.assertIn("nested_italic", codes)

    def test_separate_italics_are_ok(self) -> None:
        result = anp.audit_text(SEPARATE_ITALICS, slug="separate")
        codes = {e["code"] for e in result["errors"]}
        self.assertNotIn("nested_italic", codes)
        self.assertNotIn("unclosed_emphasis", codes)

    def test_unclosed_emphasis(self) -> None:
        result = anp.audit_text(UNCLOSED, slug="unclosed")
        codes = {e["code"] for e in result["errors"]}
        self.assertIn("unclosed_emphasis", codes)

    def test_image_must_be_alone(self) -> None:
        result = anp.audit_text(IMAGE_WITH_TEXT, slug="image-text")
        codes = {e["code"] for e in result["errors"]}
        self.assertIn("image_not_alone", codes)

    def test_zoom_caption_needs_heading(self) -> None:
        result = anp.audit_text(ZOOM_BURIED, slug="buried")
        codes = {e["code"] for e in result["errors"]}
        self.assertIn("missing_zoom_heading", codes)

    def test_zoom_section_rejects_whole_figure(self) -> None:
        result = anp.audit_text(ZOOM_WHOLE, slug="whole")
        codes = {e["code"] for e in result["errors"]}
        self.assertIn("zoom_not_a_panel", codes)

    def test_zoom_section_accepts_panel(self) -> None:
        result = anp.audit_text(ZOOM_OK, slug="zoom-ok")
        self.assertEqual(result["errors"], [], result)

    def test_audit_path(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "good-note.md"
            path.write_text(GOOD_L3)
            result = anp.audit_path(path)
        self.assertEqual(result["errors"], [])


if __name__ == "__main__":
    unittest.main()
