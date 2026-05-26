#!/usr/bin/env python3
"""Generate a minimal index.html that embeds the PDF (language switching is in the PDF itself)."""
import sys
from pathlib import Path

PAGE = """\
<!doctype html>
<html lang="{lang}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <meta http-equiv="refresh" content="0;url={pdf_path}">
</head>
</html>
"""


def main() -> None:
    output_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("rendercv_output")

    for lang, pdf_path, title in [
        ("en", "Yao_Chius_CV.pdf", "Yao Chius CV"),
        ("zh", "Yao_Chius_CV.pdf", "Yao Chius CV"),
    ]:
        out_dir = output_root if lang == "en" else output_root / "zh"
        out_dir.mkdir(parents=True, exist_ok=True)
        page = PAGE.format(lang=lang, title=title, pdf_path=pdf_path)
        (out_dir / "index.html").write_text(page, encoding="utf-8")

    print("done")


if __name__ == "__main__":
    main()
