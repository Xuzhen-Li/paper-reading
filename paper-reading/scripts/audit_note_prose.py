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
