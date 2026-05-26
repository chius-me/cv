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
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html, body {{ height: 100%; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
        .top {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 44px;
            background: #f8f9fa;
            border-bottom: 1px solid #e9ecef;
        }}
        .tabs {{
            display: flex;
            gap: 4px;
            background: #e9ecef;
            border-radius: 8px;
            padding: 3px;
        }}
        .tabs a {{
            text-decoration: none;
            font-size: 14px;
            padding: 5px 16px;
            border-radius: 6px;
            color: #6c757d;
            transition: all 0.15s;
        }}
        .tabs a:hover {{ color: #212529; }}
        .tabs .active {{
            background: #fff;
            color: #212529;
            font-weight: 600;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        .main {{
            height: calc(100% - 44px);
        }}
        iframe {{
            border: 0;
            width: 100%;
            height: 100%;
        }}
        @media print {{ .top {{ display: none; }} .main {{ height: 100%; }} }}
    </style>
</head>
<body>
    <div class="top">
        <div class="tabs">
            {switcher}
        </div>
    </div>
    <div class="main">
        <iframe src="{pdf_path}" title="{title}"></iframe>
    </div>
</body>
</html>
"""

SWITCHER_EN = '<span class="active">English</span><a href="/zh/">中文</a>'
SWITCHER_ZH = '<a href="/">English</a><span class="active">中文</span>'


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
