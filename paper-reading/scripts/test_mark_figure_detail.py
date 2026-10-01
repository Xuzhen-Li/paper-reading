#!/usr/bin/env python3
"""Crop and mark stay off the source figure."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from PIL import Image

import mark_figure_detail as mfd


class MarkFigureDetailTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.src = Path(self.tmp.name) / "fig03.png"
        image = Image.new("RGBA", (200, 100), (255, 255, 255, 255))
        for x in range(10, 40):
            for y in range(10, 40):
                image.putpixel((x, y), (0, 0, 255, 255))
        image.save(self.src)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_crop_is_the_panel_and_source_stays(self) -> None:
        out = Path(self.tmp.name) / "fig03-panel-b.png"
        before = self.src.read_bytes()
        width, height = mfd.crop_and_mark(self.src, out, (0, 0, 80, 80), None, "")
        self.assertEqual((width, height), (80, 80))
        with Image.open(out) as cropped:
            self.assertEqual(cropped.size, (80, 80))
        self.assertEqual(self.src.read_bytes(), before)

    def test_mark_is_on_the_copy(self) -> None:
        out = Path(self.tmp.name) / "fig03-panel-b-note.png"
        mfd.crop_and_mark(self.src, out, (0, 0, 80, 80), (10, 10, 40, 40), "b")
        with Image.open(out) as marked:
            self.assertEqual(marked.getpixel((10, 10))[:3], mfd.MARK_COLOR[:3])
            self.assertNotEqual(marked.getpixel((25, 25))[:3], mfd.MARK_COLOR[:3])

    def test_refuses_to_overwrite_source(self) -> None:
        with self.assertRaises(SystemExit):
            mfd.crop_and_mark(self.src, self.src, (0, 0, 40, 40), None, "")

    def test_crop_outside_image_fails(self) -> None:
        out = Path(self.tmp.name) / "nope.png"
        with self.assertRaises(SystemExit):
            mfd.crop_and_mark(self.src, out, (0, 0, 400, 40), None, "")


if __name__ == "__main__":
    unittest.main()
