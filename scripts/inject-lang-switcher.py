#!/usr/bin/env python3
"""Generate index.html wrapper pages that embed the PDF with a lang switcher bar."""
import sys
from pathlib import Path

PAGE_TEMPLATE = """\
<!doctype html>
<html lang="{lang}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        html, body {{
            height: 100%;
        }}
        .lang-bar {{
            position: fixed;
            top: 0;
            right: 0;
            z-index: 999;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-size: 13px;
            background: rgba(255,255,255,0.92);
            backdrop-filter: blur(6px);
            border: 1px solid #ddd;
            border-radius: 0 0 0 6px;
            padding: 6px 14px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.06);
        }}
        .lang-bar a {{
            color: #555;
            text-decoration: none;
            padding: 2px 4px;
        }}
        .lang-bar a:hover {{
            color: #000;
            text-decoration: underline;
        }}
        .lang-bar .active {{
            color: #000;
            font-weight: 600;
        }}
        .lang-bar .sep {{
            color: #ccc;
            margin: 0 2px;
        }}
        iframe {{
            border: 0;
            width: 100%;
            height: 100%;
        }}
    </style>
</head>
<body>
    <div class="lang-bar">
        {switcher}
    </div>
    <iframe src="{pdf_path}" title="{title}"></iframe>
</body>
</html>
"""

SWITCHER_EN = '<span class="active">EN</span> <span class="sep">|</span> <a href="/zh/">中文</a>'
SWITCHER_ZH = '<a href="/">EN</a> <span class="sep">|</span> <span class="active">中文</span>'


def write_wrapper(output_dir: Path, lang: str, pdf_path: str, title: str) -> None:
    switcher = SWITCHER_EN if lang == "en" else SWITCHER_ZH
    page = PAGE_TEMPLATE.format(lang=lang, title=title, pdf_path=pdf_path, switcher=switcher)
    (output_dir / "index.html").write_text(page, encoding="utf-8")
    print(f"  wrote {output_dir}/index.html")


def main() -> None:
    output_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("rendercv_output")

    write_wrapper(output_root, "en", "Yao_Chius_CV.pdf", "Yao Chius CV")
    write_wrapper(output_root / "zh", "zh", "Yao_Chius_CV.pdf", "Yao Chius CV")
    print("done")


if __name__ == "__main__":
    main()
