#!/usr/bin/env python3
"""Lint a literature note for layout, process-meta, L3 structure, and slop."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

EMPTY_YAML_RE = re.compile(
    r"^(figures_dir:\s*\"\"|dialogue_notes:\s*\[\]|figures_count:\s*0)\s*$",
    re.M,
)
PROCESS_META_RE = re.compile(
    r"AI 初判|待人核|## 自检|笔记自检|合格自检|Target 420|"
    r"生成过程|提取行数|作为 AI|我无法访问 PDF|"
    r"未写入\s*`?read_paper|补充材料在\s*`_figures/",
    re.I,
)
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
H1_RE = re.compile(r"^# .+$", re.M)
FRONTMATTER_END = re.compile(r"^---\s*$", re.M)
SCALAR_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")
WALKTHROUGH_RE = re.compile(r"^## .*(全文导读)", re.M)
EXCERPT_RE = re.compile(r"^## .*(原文摘抄)", re.M)
SEQ_WORDS = ("首先", "其次", "再次", "最后")
SIGNIFICANCE_RE = re.compile(r"具有重要意义|填补空白")
OPENING_LABEL_RE = re.compile(r"\*\*EN\*\*|\*\*通讯\*\*|^\s*>\s*\*\*一作\*\*|通讯：|一作：")
FENCE_RE = re.compile(r"^```")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
STRONG_RE = re.compile(r"\*\*[^*]*\*\*")
IMAGE_LINE_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")
ZOOM_HEADING_RE = re.compile(r"^## 小图精讲\s*$", re.M)
PANEL_FILE_RE = re.compile(r"(?:fig|edfig|sfig)\d+-", re.I)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = SCALAR_RE.match(line)
        if match:
            fields[match.group(1)] = match.group(2).strip()
    body = text[end + 4 :]
    if body.startswith("\n"):
        body = body[1:]
    return fields, body


def _error(code: str, message: str) -> dict[str, str]:
    return {"code": code, "message": message}


def _strip_code_and_strong(text: str) -> str:
    without_code = INLINE_CODE_RE.sub("", text)
    return STRONG_RE.sub("", without_code)


def preview_markdown_errors(body: str) -> list[dict[str, str]]:
    """Catch markdown that hides the rest of a paragraph or the next image."""
    errors: list[dict[str, str]] = []
    paragraphs: list[list[tuple[int, str]]] = []
    current: list[tuple[int, str]] = []
    in_fence = False
    for lineno, line in enumerate(body.splitlines(), 1):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            if current:
                paragraphs.append(current)
                current = []
            continue
        if in_fence or not line.strip():
            if current and not in_fence:
                paragraphs.append(current)
                current = []
            continue
        current.append((lineno, line))
    if in_fence:
        errors.append(_error("unclosed_fence", "a code fence is still open at the end of the note"))
    if current:
        paragraphs.append(current)

    for para in paragraphs:
        for lineno, line in para:
            if "![" not in line:
                continue
            rest = IMAGE_LINE_RE.sub("", line).strip()
            if rest:
                errors.append(
                    _error(
                        "image_not_alone",
                        f"line {lineno}: an image shares its line with other text, so a broken span can hide it",
                    )
                )
        plain = _strip_code_and_strong("\n".join(line for _, line in para))
        if plain.count("**") % 2:
            errors.append(
                _error(
                    "unclosed_emphasis",
                    f"line {para[0][0]}: unclosed ** runs through the paragraph and can hide the next image",
                )
            )
        emphasis = plain.replace("**", "")
        if emphasis.count("*") % 2:
            errors.append(
                _error(
                    "unclosed_emphasis",
                    f"line {para[0][0]}: unclosed * runs through the paragraph and can hide the next image",
                )
            )
        for lineno, line in para:
            caption = _strip_code_and_strong(line).strip()
            if caption.startswith("*") and caption.endswith("*") and caption.count("*") >= 4:
                errors.append(
                    _error(
                        "nested_italic",
                        f"line {lineno}: an italic caption contains another *...*; the preview closes the span early",
                    )
                )
    return errors


def zoom_section_errors(body: str) -> list[dict[str, str]]:
    """A tight crop buried in prose is not 小图精讲. The outline needs the heading."""
    errors: list[dict[str, str]] = []
    has_zoom_caption = "笔记裁切" in body or "笔记标注" in body
    heading = ZOOM_HEADING_RE.search(body)
    if has_zoom_caption and heading is None:
        errors.append(
            _error(
                "missing_zoom_heading",
                "笔记裁切 / 笔记标注 need their own ## 小图精讲 so the outline shows the panel",
            )
        )
        return errors
    if heading is None:
        return errors
    after = body[heading.end() :]
    next_heading = re.search(r"^## ", after, re.M)
    section = after[: next_heading.start()] if next_heading else after
    images = IMAGE_RE.findall(section)
    if not images:
        errors.append(_error("zoom_section_empty", "## 小图精讲 has no image"))
        return errors
    if not any(PANEL_FILE_RE.search(Path(dest).name) for dest in images):
        errors.append(
            _error(
                "zoom_not_a_panel",
                "## 小图精讲 only links a whole figure; crop the panel to its own png",
            )
        )
    return errors


def audit_text(text: str, slug: str | None = None) -> dict:
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    fields, body = parse_frontmatter(text)
    depth = fields.get("note_depth") or fields.get("level") or ""
    depth = depth.strip().strip("\"'")

    if EMPTY_YAML_RE.search(text[: text.find("\n---", 4) + 4] if text.startswith("---") else ""):
        errors.append(_error("empty_yaml_field", "omit empty YAML keys such as figures_dir: \"\""))
    else:
        yaml_block = text[4 : text.find("\n---", 4)] if text.startswith("---\n") else ""
        if re.search(r"^(figures_dir:\s*\"\"|dialogue_notes:\s*\[\]|figures_count:\s*0)\s*$", yaml_block, re.M):
            errors.append(_error("empty_yaml_field", "omit empty YAML keys"))

    if PROCESS_META_RE.search(text):
        errors.append(_error("process_meta", "process or self-audit phrasing in the note body"))

    if depth == "L3":
        if not WALKTHROUGH_RE.search(text):
            errors.append(_error("missing_l3_walkthrough", "L3 needs ## 📖 全文导读"))
        if not EXCERPT_RE.search(text):
            errors.append(_error("missing_l3_excerpts", "L3 needs ## 📜 原文摘抄"))

    prefix = f"_figures/{slug}/" if slug else "_figures/"
    for dest in IMAGE_RE.findall(text):
        dest = dest.strip()
        if dest.startswith("http://") or dest.startswith("https://"):
            continue
        if slug and not dest.startswith(prefix):
            errors.append(
                _error(
                    "figure_link_not_under_slug",
                    f"image {dest} is not under {prefix}",
                )
            )
        elif not slug and not dest.startswith("_figures/"):
            errors.append(
                _error("figure_link_not_under_slug", f"image {dest} is not under _figures/")
            )

    h1 = H1_RE.search(body)
    if h1:
        after = body[h1.end() :]
        next_h2 = re.search(r"^## ", after, re.M)
        opening = after[: next_h2.start()] if next_h2 else after[:800]
        en_title = fields.get("en_title", "").strip().strip("\"'")
        repeats = bool(OPENING_LABEL_RE.search(opening))
        if en_title and en_title in opening:
            repeats = True
        if repeats:
            errors.append(
                _error(
                    "opening_repeats_yaml",
                    "H1 block restates en_title / corresponding / first author",
                )
            )

    if SIGNIFICANCE_RE.search(body):
        errors.append(_error("empty_significance", "empty significance phrasing"))
    if all(word in body for word in SEQ_WORDS):
        errors.append(_error("formulaic_sequence", "dense 首先/其次/再次/最后 scaffolding"))

    errors.extend(preview_markdown_errors(body))
    errors.extend(zoom_section_errors(body))

    return {
        "slug": slug,
        "depth": depth,
        "errors": errors,
        "warnings": warnings,
        "ok": not errors,
    }


def audit_path(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    slug = path.stem
    result = audit_text(text, slug=slug)
    result["path"] = str(path)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("note", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--report", type=Path, default=None)
    args = parser.parse_args(argv)

    result = audit_path(args.note)
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(payload + "\n", encoding="utf-8")
    if args.json:
        print(payload)
    else:
        print(f"{result.get('path')} errors={len(result['errors'])} ok={result['ok']}")
        for item in result["errors"]:
            print(f"  error {item['code']}: {item['message']}")
        for item in result["warnings"]:
            print(f"  warn  {item['code']}: {item['message']}")
    if args.strict and result["errors"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
