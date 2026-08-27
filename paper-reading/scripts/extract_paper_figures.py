#!/usr/bin/env python3
"""Extract *figures* (not full pages) from a research PDF into papers/_figures/<slug>/.

Default method ``crop``:
  1. Find ``Fig. N`` / ``Figure N`` caption anchors on each page.
  2. Crop the band *above* each caption (figure sits above its legend).
  3. Caption-less pages that are figure-heavy → crop content band
     (strip header/footer only).
  4. Fallbacks: ``pdfimages`` (embedded rasters) or ``pdftoppm`` (full page; last resort).

Usage:
  python3 extract_paper_figures.py \\
    --pdf /path/to/paper.pdf \\
    --slug 2023-dong-grapevine-dual-domestication-science \\
    [--pages 3-8] \\
    [--max-keep 6] \\
    [--method crop|pdfimages|pdftoppm|auto]
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import os
from pathlib import Path

PAPER_FIGURES: Path | None = None
SWEEP_TMP: Path | None = None


def _env_path(name: str) -> Path | None:
    raw = os.environ.get(name, "").strip()
    return Path(raw).expanduser() if raw else None


def configure(figures_dir: Path | str | None = None, tmp_dir: Path | str | None = None) -> None:
    """Resolve output dirs from args, then FIGURES_DIR / TMP_DIR env vars."""
    global PAPER_FIGURES, SWEEP_TMP
    figures = Path(figures_dir) if figures_dir else _env_path("FIGURES_DIR")
    tmp = Path(tmp_dir) if tmp_dir else _env_path("TMP_DIR")
    if figures is None or tmp is None:
        raise SystemExit(
            "Figure extraction needs --figures-dir and --tmp-dir, "
            "or environment variables FIGURES_DIR and TMP_DIR."
        )
    PAPER_FIGURES = figures.expanduser().resolve()
    SWEEP_TMP = tmp.expanduser().resolve()

CAPTION_RE = re.compile(
    r"^(Fig\.?|Figure)\s*(\d+[A-Za-z]?)([.\s]|$)",
    re.IGNORECASE,
)


def ensure_layout() -> None:
    if PAPER_FIGURES is None or SWEEP_TMP is None:
        raise SystemExit("Call configure() or pass --figures-dir/--tmp-dir first.")
    if PAPER_FIGURES.is_symlink():
        raise SystemExit(
            f"{PAPER_FIGURES} is still a symlink; expected a real directory "
            f"papers/_figures/ after migration."
        )
    PAPER_FIGURES.mkdir(parents=True, exist_ok=True)


def parse_pages(spec: str | None) -> list[int] | None:
    if not spec:
        return None
    pages: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            pages.extend(range(int(a), int(b) + 1))
        else:
            pages.append(int(part))
    return sorted(set(pages))


def image_min_side(path: Path) -> int | None:
    try:
        out = subprocess.check_output(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
            text=True,
            stderr=subprocess.DEVNULL,
        )
        w = h = None
        for line in out.splitlines():
            if "pixelWidth:" in line:
                w = int(line.split(":")[-1].strip())
            if "pixelHeight:" in line:
                h = int(line.split(":")[-1].strip())
        if w and h:
            return min(w, h)
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        pass
    return None


def filter_by_size(paths: list[Path], min_side: int) -> list[Path]:
    kept: list[Path] = []
    for p in paths:
        side = image_min_side(p)
        if side is None or side >= min_side:
            kept.append(p)
    return kept


def _is_thin(im: dict, max_thin: float = 25.0) -> bool:
    w, h = float(im["width"]), float(im["height"])
    m = min(w, h)
    if m < max_thin:
        return True
    return (max(w, h) / max(m, 1e-6)) > 15


def _caption_hits(page) -> list[dict]:
    """Return caption anchors sorted by top: {top, bottom, label, x0, x1}."""
    words = page.extract_words() or []
    # Rebuild line-ish groups by rounded top
    lines: dict[float, list] = {}
    for w in words:
        key = round(float(w["top"]), 0)
        lines.setdefault(key, []).append(w)
    hits = []
    for top_key, ws in sorted(lines.items()):
        text = "".join(w["text"] for w in ws)
        # pdfplumber often concatenates without spaces
        spaced = " ".join(w["text"] for w in ws)
        for candidate in (spaced, text):
            m = CAPTION_RE.match(candidate.strip())
            if not m:
                continue
            label = f"Fig.{m.group(2)}"
            hits.append(
                {
                    "top": min(float(w["top"]) for w in ws),
                    "bottom": max(float(w["bottom"]) for w in ws),
                    "label": label,
                    "x0": min(float(w["x0"]) for w in ws),
                    "x1": max(float(w["x1"]) for w in ws),
                    "text": candidate[:120],
                }
            )
            break
    # Dedupe captions very close in Y
    hits.sort(key=lambda h: h["top"])
    deduped = []
    for h in hits:
        if deduped and abs(h["top"] - deduped[-1]["top"]) < 8:
            continue
        deduped.append(h)
    return deduped


def _image_union(page, min_area: float = 2000.0):
    imgs = [
        im
        for im in (page.images or [])
        if not _is_thin(im) and float(im["width"]) * float(im["height"]) >= min_area
    ]
    if not imgs:
        return None
    return (
        min(float(im["x0"]) for im in imgs),
        min(float(im["top"]) for im in imgs),
        max(float(im["x1"]) for im in imgs),
        max(float(im["bottom"]) for im in imgs),
    )


def _content_margins(page, header_frac=0.055, footer_frac=0.055):
    header = page.height * header_frac
    footer = page.height * (1 - footer_frac)
    return header, footer


def plan_crops_for_page(page) -> list[dict]:
    """Plan crop boxes (PDF points, top-left origin as pdfplumber)."""
    header, footer = _content_margins(page)
    captions = _caption_hits(page)
    union = _image_union(page)
    crops = []

    if captions:
        # Figure graphics sit above each caption.
        # Start of band = previous caption bottom (if any) else header,
        # but prefer image-union top when it is below header.
        prev_bottom = header
        for i, cap in enumerate(captions):
            # Skip caption-only bands that are essentially text under a prior figure
            # (caption near top with almost no room above for graphics).
            top = prev_bottom
            if union and i == 0 and union[1] < cap["top"]:
                # First caption: if images exist above it, start at union top
                # (but not above header).
                top = max(header, min(union[1], cap["top"] - 10))
            bottom = min(footer, cap["bottom"] + 6)
            # If this caption is near the top (<15% page) it is often a
            # carry-over legend from previous page — keep a short band only
            # when there is meaningful image area above it.
            height = bottom - top
            if height < 40:
                prev_bottom = cap["bottom"]
                continue
            if cap["top"] < page.height * 0.12 and height < page.height * 0.18:
                # Tiny top caption strip → skip (text continuation)
                prev_bottom = cap["bottom"]
                continue
            # Horizontal: prefer image union width, else near-full content
            if union:
                x0 = max(0, min(union[0], 36) - 4)
                x1 = min(page.width, max(union[2], page.width - 36) + 4)
            else:
                x0, x1 = 28, page.width - 28
            # Expand top upward to include images that belong to this figure
            if union and union[1] < cap["top"] and union[1] >= prev_bottom - 5:
                top = max(header, min(top, union[1] - 4))
            # For mid-page captions, top should be after previous caption
            if i > 0:
                top = max(top, prev_bottom + 4)
                if union and union[3] > prev_bottom and union[1] < cap["top"]:
                    # Clip union to this band
                    top = max(top, min(union[1], prev_bottom + 4))
            if bottom - top >= 60:
                crops.append(
                    {
                        "x0": x0,
                        "top": top,
                        "x1": x1,
                        "bottom": bottom,
                        "label": cap["label"],
                        "page": None,  # filled by caller
                    }
                )
            prev_bottom = cap["bottom"]

        # After last caption: if large images remain below, rare — ignore.

    # Caption-less page: figure-only sheet (common when legend is on next page)
    if not crops:
        if union:
            x0 = max(0, union[0] - 6)
            top = max(header, union[1] - 6)
            x1 = min(page.width, union[2] + 6)
            bottom = min(footer, union[3] + 6)
            # If union only covers a thin top strip but page is figure-heavy,
            # expand to content band (vector panels below rasters).
            if (bottom - top) < page.height * 0.35:
                top = header
                bottom = footer
                x0, x1 = 24, page.width - 24
        else:
            # No rasters — still may be vector-only figure page
            top, bottom = header, footer
            x0, x1 = 24, page.width - 24
        if bottom - top >= 80:
            crops.append(
                {
                    "x0": x0,
                    "top": top,
                    "x1": x1,
                    "bottom": bottom,
                    "label": "Fig",
                    "page": None,
                }
            )
    return crops


def render_crop(pdf_path: Path, page_index: int, box: dict, scale: float, dest: Path) -> None:
    import pypdfium2 as pdfium

    pdf = pdfium.PdfDocument(str(pdf_path))
    page = pdf[page_index]
    pil = page.render(scale=scale).to_pil()
    L = int(box["x0"] * scale)
    T = int(box["top"] * scale)
    R = int(box["x1"] * scale)
    B = int(box["bottom"] * scale)
    L, T = max(0, L), max(0, T)
    R, B = min(pil.width, R), min(pil.height, B)
    crop = pil.crop((L, T, R, B))
    dest.parent.mkdir(parents=True, exist_ok=True)
    crop.save(dest)
    pdf.close()


def run_crop(pdf: Path, work: Path, pages: list[int] | None, scale: float = 2.5) -> list[Path]:
    import pdfplumber

    work.mkdir(parents=True, exist_ok=True)
    out_paths: list[Path] = []
    with pdfplumber.open(str(pdf)) as pl:
        indices = range(len(pl.pages))
        if pages:
            indices = [p - 1 for p in pages if 1 <= p <= len(pl.pages)]
        fig_i = 0
        for idx in indices:
            page = pl.pages[idx]
            plans = plan_crops_for_page(page)
            for plan in plans:
                fig_i += 1
                label = plan["label"].replace(".", "").replace(" ", "")
                dest = work / f"crop_p{idx+1}_{label}_{fig_i:02d}.png"
                render_crop(pdf, idx, plan, scale, dest)
                out_paths.append(dest)
    return out_paths


def run_pdfimages(pdf: Path, work: Path, pages: list[int] | None) -> str:
    work.mkdir(parents=True, exist_ok=True)
    prefix = work / "img"
    cmd = ["pdfimages", "-png"]
    if pages:
        cmd += ["-f", str(min(pages)), "-l", str(max(pages))]
    cmd += [str(pdf), str(prefix)]
    subprocess.check_call(cmd)
    return "pdfimages"


def run_pdftoppm(pdf: Path, work: Path, pages: list[int] | None, dpi: int = 200) -> str:
    work.mkdir(parents=True, exist_ok=True)
    prefix = work / "page"
    cmd = ["pdftoppm", "-png", "-r", str(dpi)]
    if pages:
        cmd += ["-f", str(min(pages)), "-l", str(max(pages))]
    cmd += [str(pdf), str(prefix)]
    subprocess.check_call(cmd)
    return "pdftoppm"


def collect_images(work: Path) -> list[Path]:
    exts = {".png", ".jpg", ".jpeg", ".tif", ".tiff"}
    return sorted(p for p in work.iterdir() if p.suffix.lower() in exts)


def finalize(
    images: list[Path],
    out_dir: Path,
    method: str,
    pdf: Path,
    pages: list[int] | None,
    max_keep: int,
) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    # Clear previous png/jpg in out_dir (keep nothing stale)
    for old in out_dir.glob("fig*"):
        old.unlink()
    selected = images[:max_keep]
    files: list[dict] = []
    for i, src in enumerate(selected, start=1):
        dst_name = f"fig{i:02d}{src.suffix.lower()}"
        dst = out_dir / dst_name
        shutil.copy2(src, dst)
        files.append(
            {
                "file": dst_name,
                "source": src.name,
                "min_side": image_min_side(dst),
            }
        )
    manifest = {
        "slug": out_dir.name,
        "source_pdf": str(pdf),
        "method": method,
        "pages_requested": pages,
        "figures_count": len(files),
        "files": files,
        "md_link_prefix": f"_figures/{out_dir.name}/",
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return manifest


def extract(
    pdf: Path,
    slug: str,
    pages: list[int] | None = None,
    min_side: int = 200,
    max_keep: int = 6,
    method: str = "crop",
    figures_dir: Path | str | None = None,
    tmp_dir: Path | str | None = None,
) -> dict:
    if not pdf.is_file():
        raise FileNotFoundError(pdf)
    if figures_dir or tmp_dir or PAPER_FIGURES is None:
        configure(figures_dir=figures_dir, tmp_dir=tmp_dir)
    ensure_layout()
    work = SWEEP_TMP / f"figwork_{slug}"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)

    used = method
    if method in ("auto", "crop"):
        try:
            paths = run_crop(pdf, work, pages)
            imgs = filter_by_size(paths, min_side)
            used = "crop"
            if len(imgs) < 1:
                raise RuntimeError("crop produced no images")
        except Exception as exc:
            if method == "crop":
                raise
            print(f"[warn] crop failed ({exc}); falling back", file=sys.stderr)
            used = run_pdfimages(pdf, work, pages)
            imgs = filter_by_size(collect_images(work), min_side)
            if len(imgs) < 1:
                used = run_pdftoppm(pdf, work, pages)
                imgs = filter_by_size(collect_images(work), min_side)
    elif method == "pdfimages":
        used = run_pdfimages(pdf, work, pages)
        imgs = filter_by_size(collect_images(work), min_side)
    else:
        used = run_pdftoppm(pdf, work, pages)
        imgs = filter_by_size(collect_images(work), min_side)

    # Keep crop order (page order); for pdfimages sort by size
    if used != "crop":
        imgs = sorted(imgs, key=lambda p: (image_min_side(p) or 0), reverse=True)

    out_dir = PAPER_FIGURES / slug
    return finalize(imgs, out_dir, used, pdf, pages, max_keep)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--pdf", type=Path, required=True)
    p.add_argument("--slug", required=True)
    p.add_argument("--pages", default=None, help="e.g. 3,5,8-10")
    p.add_argument("--min-side", type=int, default=200)
    p.add_argument("--max-keep", type=int, default=6)
    p.add_argument(
        "--method",
        choices=("crop", "auto", "pdfimages", "pdftoppm"),
        default="crop",
        help="crop=figure bands (default); pdftoppm=full page (discouraged)",
    )
    p.add_argument("--figures-dir", type=Path, default=None, help="or set FIGURES_DIR")
    p.add_argument("--tmp-dir", type=Path, default=None, help="or set TMP_DIR")
    args = p.parse_args(argv)
    configure(figures_dir=args.figures_dir, tmp_dir=args.tmp_dir)
    pages = parse_pages(args.pages)
    manifest = extract(
        args.pdf.resolve(),
        args.slug,
        pages=pages,
        min_side=args.min_side,
        max_keep=args.max_keep,
        method=args.method,
        figures_dir=args.figures_dir,
        tmp_dir=args.tmp_dir,
    )
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    print(
        f"Wrote {PAPER_FIGURES / args.slug} ({manifest['figures_count']} files, method={manifest['method']})",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
