#!/usr/bin/env python3
"""Annotate PDF pages with a language-switching link at the top right."""
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.annotations import FreeText
from pypdf.generic import (
    ArrayObject, DictionaryObject, FloatObject, NameObject,
    RectangleObject, TextStringObject,
)

PAGE_MARGIN = 72  # 1 inch in points, typical margin


def add_lang_link(pdf_path: str, label: str, target_url: str) -> None:
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    writer.clone_reader_document_root(reader)

    for page in reader.pages:
        mediabox = page.mediabox
        page_w = float(mediabox.width)
        page_h = float(mediabox.height)

        # Small annotation box at top right corner
        box_w, box_h = 80, 18
        x = page_w - PAGE_MARGIN - box_w
        y = page_h - PAGE_MARGIN + 8

        rect = RectangleObject([x, y - box_h, x + box_w, y])

        # URI action pointing to the other language
        action = DictionaryObject({
            NameObject("/Type"): NameObject("/Action"),
            NameObject("/S"): NameObject("/URI"),
            NameObject("/URI"): TextStringObject(target_url),
        })

        # Appearance: transparent fill, no border, small gray text
        appearance = TextStringObject(
            "0 g /Helv 8 Tf " + label + " Tj"
        )

        annot = FreeText(
            rect=rect,
            text=label,
        )
        annot[NameObject("/A")] = action
        annot[NameObject("/DA")] = appearance
        annot[NameObject("/F")] = FloatObject(4)  # Print flag
        annot[NameObject("/Border")] = ArrayObject([
            FloatObject(0), FloatObject(0), FloatObject(0)
        ])
        annot[NameObject("/C")] = ArrayObject([
            FloatObject(0.4), FloatObject(0.4), FloatObject(0.4)
        ])

        writer.add_page(page)
        writer.add_annotation(page_number=len(writer.pages) - 1, annotation=annot)

    writer.write(pdf_path)


def main() -> None:
    output_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("rendercv_output")

    en_pdf = output_root / "Yao_Chius_CV.pdf"
    zh_pdf = output_root / "zh" / "Yao_Chius_CV.pdf"

    if en_pdf.exists():
        add_lang_link(str(en_pdf), "中文", "https://cv.chius.cc/zh/")
        print(f"  annotated {en_pdf}")

    if zh_pdf.exists():
        add_lang_link(str(zh_pdf), "English", "https://cv.chius.cc/")
        print(f"  annotated {zh_pdf}")

    print("done")


if __name__ == "__main__":
    main()
