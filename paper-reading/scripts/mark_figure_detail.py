#!/usr/bin/env python3
"""Crop one panel from a figure png, and optionally mark a box on a copy.

The whole-figure png is never overwritten. Coordinates are pixels, origin
top-left. --mark is measured on the image after --crop.

  python3 mark_figure_detail.py \
    --src fig03.png --out fig03-panel-b.png \
    --crop 40,80,520,640 \
    --mark 30,20,180,160 --label "b"
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

MARK_COLOR = (192, 57, 43, 255)
LABEL_FILL = (255, 255, 255, 230)
FONT_CANDIDATES = (
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
)


def parse_box(text: str) -> tuple[int, int, int, int]:
    parts = [p.strip() for p in text.split(",")]
    if len(parts) != 4:
        raise SystemExit(f"box needs four integers, got {text!r}")
    box = tuple(int(p) for p in parts)
    if box[2] <= box[0] or box[3] <= box[1]:
        raise SystemExit(f"box right/bottom must be greater than left/top: {text}")
    return box  # type: ignore[return-value]


def _font(size: int) -> ImageFont.ImageFont:
    for path in FONT_CANDIDATES:
        if Path(path).is_file():
            try:
                return ImageFont.truetype(path, size=size)
            except OSError:
                continue
    return ImageFont.load_default()


def crop_and_mark(
    src: Path,
    out: Path,
    crop: tuple[int, int, int, int] | None,
    mark: tuple[int, int, int, int] | None,
    label: str,
) -> tuple[int, int]:
    if src.resolve() == out.resolve():
        raise SystemExit("refusing to overwrite the source figure")
    if out.suffix.lower() != ".png":
        raise SystemExit("output must be a .png")
    image = Image.open(src).convert("RGBA")
    if crop is not None:
        if crop[0] < 0 or crop[1] < 0 or crop[2] > image.width or crop[3] > image.height:
            raise SystemExit(
                f"crop {crop} is outside {image.width}x{image.height}"
            )
        image = image.crop(crop)
    if mark is not None:
        if mark[0] < 0 or mark[1] < 0 or mark[2] > image.width or mark[3] > image.height:
            raise SystemExit(
                f"mark {mark} is outside {image.width}x{image.height}"
            )
        draw = ImageDraw.Draw(image)
        draw.rectangle(mark, outline=MARK_COLOR, width=max(2, min(image.size) // 120))
        text = label.strip()
        if text:
            font = _font(max(14, min(image.size) // 28))
            left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
            tw, th = right - left, bottom - top
            x = mark[0]
            y = mark[1] - th - 4
            if y < 0:
                y = mark[1] + 2
            draw.rectangle((x, y, x + tw + 6, y + th + 4), fill=LABEL_FILL)
            draw.text((x + 3, y + 2), text, fill=MARK_COLOR, font=font)
    out.parent.mkdir(parents=True, exist_ok=True)
    image.save(out)
    return image.size


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--src", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--crop", type=parse_box, default=None, help="left,top,right,bottom on the source")
    p.add_argument("--mark", type=parse_box, default=None, help="left,top,right,bottom on the output")
    p.add_argument("--label", default="", help="short note on the mark; omit for a box only")
    args = p.parse_args(argv)
    if not args.src.is_file():
        raise SystemExit(f"missing source: {args.src}")
    if args.crop is None and args.mark is None:
        raise SystemExit("pass --crop, --mark, or both")
    width, height = crop_and_mark(args.src, args.out, args.crop, args.mark, args.label)
    print(f"{args.out} {width}x{height}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
