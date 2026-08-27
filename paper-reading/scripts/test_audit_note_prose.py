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

    def test_audit_path(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "good-note.md"
            path.write_text(GOOD_L3)
            result = anp.audit_path(path)
        self.assertEqual(result["errors"], [])


if __name__ == "__main__":
    unittest.main()
