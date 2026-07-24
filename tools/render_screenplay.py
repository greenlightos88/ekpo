#!/usr/bin/env python3
"""Render the canonical EKPO Fountain screenplay as a producer-facing PDF."""

from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from pathlib import Path

from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


PAGE_WIDTH, PAGE_HEIGHT = LETTER
LEFT_MARGIN = 1.5 * inch
RIGHT_MARGIN = 1.0 * inch
TOP_MARGIN = 0.72 * inch
BOTTOM_MARGIN = 0.68 * inch

FONT_DIR = Path(r"C:\Windows\Fonts")
FONT_FILES = {
    "CourierScreenplay": FONT_DIR / "cour.ttf",
    "CourierScreenplay-Bold": FONT_DIR / "courbd.ttf",
    "CourierScreenplay-Italic": FONT_DIR / "couri.ttf",
    "CourierScreenplay-BoldItalic": FONT_DIR / "courbi.ttf",
}


@dataclass
class Block:
    kind: str
    text: str
    character: str | None = None


def register_fonts() -> None:
    for name, path in FONT_FILES.items():
        if not path.exists():
            raise FileNotFoundError(f"Required screenplay font is missing: {path}")
        pdfmetrics.registerFont(TTFont(name, str(path)))
    pdfmetrics.registerFontFamily(
        "CourierScreenplay",
        normal="CourierScreenplay",
        bold="CourierScreenplay-Bold",
        italic="CourierScreenplay-Italic",
        boldItalic="CourierScreenplay-BoldItalic",
    )


def is_character_cue(line: str) -> bool:
    if len(line) > 42 or line.endswith((".", ":", "!", "?")):
        return False
    letters = [char for char in line if char.isalpha()]
    return bool(letters) and all(char.isupper() for char in letters)


def parse_title_page(lines: list[str]) -> tuple[dict[str, str], int]:
    metadata: dict[str, str] = {}
    index = 0
    for index, raw in enumerate(lines):
        line = raw.strip()
        if line == "===":
            return metadata, index + 1
        if not line:
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip().lower()] = value.strip()
    return metadata, 0


def parse_fountain(text: str) -> tuple[dict[str, str], list[Block]]:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    title, start = parse_title_page(lines)
    blocks: list[Block] = []
    index = start

    while index < len(lines):
        line = lines[index].strip()
        index += 1

        if not line:
            continue
        if line.startswith("#"):
            continue
        if line.startswith("/*"):
            while index < len(lines) and "*/" not in lines[index]:
                index += 1
            index += 1
            continue
        if re.match(r"^(INT\.|EXT\.|INT\./EXT\.|EXT\./INT\.|I/E\.)", line):
            blocks.append(Block("scene", line))
            continue
        if line == "FADE IN:":
            blocks.append(Block("fadein", line))
            continue
        if line in {"CUT TO:", "CUT TO BLACK.", "FADE OUT.", "FADE TO BLACK."}:
            blocks.append(Block("transition", line))
            continue
        if is_character_cue(line):
            dialogue_lines: list[str] = []
            while index < len(lines):
                dialogue = lines[index].strip()
                if not dialogue:
                    index += 1
                    break
                if dialogue.startswith("#") or re.match(
                    r"^(INT\.|EXT\.|INT\./EXT\.|EXT\./INT\.|I/E\.)", dialogue
                ):
                    break
                dialogue_lines.append(dialogue)
                index += 1
            if dialogue_lines:
                blocks.append(
                    Block("dialogue", "\n".join(dialogue_lines), character=line)
                )
            else:
                blocks.append(Block("action", line))
            continue
        blocks.append(Block("action", line))

    return title, blocks


def make_styles() -> dict[str, ParagraphStyle]:
    base = {
        "fontName": "CourierScreenplay",
        "fontSize": 12,
        "leading": 12,
        "textColor": "#000000",
        "allowWidows": 0,
        "allowOrphans": 0,
    }
    return {
        "action": ParagraphStyle(
            "Action",
            **base,
            leftIndent=0,
            rightIndent=0,
            spaceBefore=0,
            spaceAfter=6,
        ),
        "scene": ParagraphStyle(
            "Scene",
            **{
                **base,
                "fontName": "CourierScreenplay-Bold",
                "spaceBefore": 6,
                "spaceAfter": 6,
                "keepWithNext": True,
            },
        ),
        "character": ParagraphStyle(
            "Character",
            **base,
            leftIndent=2.2 * inch,
            rightIndent=0.5 * inch,
            spaceBefore=6,
            spaceAfter=0,
            keepWithNext=True,
        ),
        "dialogue": ParagraphStyle(
            "Dialogue",
            **base,
            leftIndent=1.0 * inch,
            rightIndent=1.5 * inch,
            spaceBefore=0,
            spaceAfter=6,
        ),
        "parenthetical": ParagraphStyle(
            "Parenthetical",
            **base,
            leftIndent=1.6 * inch,
            rightIndent=1.8 * inch,
            spaceBefore=0,
            spaceAfter=0,
        ),
        "transition": ParagraphStyle(
            "Transition",
            **base,
            alignment=TA_RIGHT,
            spaceBefore=6,
            spaceAfter=6,
        ),
        "fadein": ParagraphStyle(
            "FadeIn",
            **base,
            spaceBefore=0,
            spaceAfter=12,
        ),
        "title": ParagraphStyle(
            "Title",
            **{
                **base,
                "fontName": "CourierScreenplay-Bold",
                "fontSize": 14,
                "leading": 14,
                "alignment": TA_CENTER,
                "spaceAfter": 18,
            },
        ),
        "title_sub": ParagraphStyle(
            "TitleSub",
            **base,
            alignment=TA_CENTER,
            spaceAfter=12,
        ),
        "draft": ParagraphStyle(
            "Draft",
            **{
                **base,
                "fontSize": 10,
                "leading": 12,
            },
        ),
    }


def paragraph(text: str, style: ParagraphStyle) -> Paragraph:
    escaped = html.escape(text).replace("\n", "<br/>")
    return Paragraph(escaped, style)


def dialogue_flowables(block: Block, styles: dict[str, ParagraphStyle]):
    flowables = [paragraph(block.character or "", styles["character"])]
    buffer: list[str] = []
    for line in block.text.split("\n"):
        if line.startswith("(") and line.endswith(")"):
            if buffer:
                flowables.append(paragraph(" ".join(buffer), styles["dialogue"]))
                buffer = []
            flowables.append(paragraph(line, styles["parenthetical"]))
        else:
            buffer.append(line)
    if buffer:
        flowables.append(paragraph(" ".join(buffer), styles["dialogue"]))
    return KeepTogether(flowables)


def page_number(canvas, document) -> None:
    physical_page = canvas.getPageNumber()
    screenplay_page = physical_page - 1
    if screenplay_page <= 1:
        return
    canvas.saveState()
    canvas.setFont("CourierScreenplay", 12)
    canvas.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, PAGE_HEIGHT - 0.45 * inch, f"{screenplay_page}.")
    canvas.restoreState()


def build_pdf(source: Path, destination: Path) -> None:
    register_fonts()
    metadata, blocks = parse_fountain(source.read_text(encoding="utf-8"))
    styles = make_styles()
    destination.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(destination),
        pagesize=LETTER,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN,
        title=metadata.get("title", "EKPO"),
        author="",
        subject="Feature Screenplay",
        creator="EKPO screenplay renderer",
    )

    story = [
        Spacer(1, 2.35 * inch),
        paragraph(metadata.get("title", "EKPO").upper(), styles["title"]),
        paragraph(metadata.get("credit", "A Feature Screenplay"), styles["title_sub"]),
        Spacer(1, 3.25 * inch),
        paragraph(
            f"Working Draft\n{metadata.get('draft date', '')}",
            styles["draft"],
        ),
        PageBreak(),
    ]

    for block in blocks:
        if block.kind == "dialogue":
            story.append(dialogue_flowables(block, styles))
        else:
            story.append(paragraph(block.text, styles[block.kind]))

    doc.build(story, onFirstPage=page_number, onLaterPages=page_number)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    build_pdf(args.source.resolve(), args.destination.resolve())


if __name__ == "__main__":
    main()
