#!/usr/bin/env python3
"""Inject a language switcher into rendered CV HTML pages."""
import sys
from pathlib import Path

SWITCHER_CSS = """
<style>
.lang-switcher {
    position: fixed;
    top: 12px;
    right: 20px;
    z-index: 999;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 13px;
    background: rgba(255, 255, 255, 0.92);
    backdrop-filter: blur(6px);
    border: 1px solid #ddd;
    border-radius: 6px;
    padding: 5px 12px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
.lang-switcher a {
    color: #555;
    text-decoration: none;
    padding: 2px 4px;
}
.lang-switcher a:hover {
    color: #000;
    text-decoration: underline;
}
.lang-switcher .active {
    color: #000;
    font-weight: 600;
}
.lang-switcher .sep {
    color: #ccc;
    margin: 0 2px;
}
@media print {
    .lang-switcher { display: none; }
}
</style>
"""

SWITCHER_EN = """
<div class="lang-switcher">
    <span class="active">EN</span>
    <span class="sep">|</span>
    <a href="/zh/">中文</a>
</div>
"""

SWITCHER_ZH = """
<div class="lang-switcher">
    <a href="/">EN</a>
    <span class="sep">|</span>
    <span class="active">中文</span>
</div>
"""


def inject_switcher(html_path: Path, lang: str) -> None:
    content = html_path.read_text(encoding="utf-8")

    if "lang-switcher" in content:
        return

    switcher_html = SWITCHER_EN if lang == "en" else SWITCHER_ZH

    # inject CSS before </head>
    content = content.replace("</head>", f"{SWITCHER_CSS}</head>", 1)

    # inject switcher after <body> tag (before any content)
    content = content.replace("<body>", f"<body>\n{switcher_html}", 1)

    html_path.write_text(content, encoding="utf-8")
    print(f"  injected lang switcher into {html_path}")


def main() -> None:
    output_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("rendercv_output")

    en_html = output_root / "Yao_Chius_CV.html"
    en_index = output_root / "index.html"
    zh_html = output_root / "zh" / "Yao_Chius_CV.html"
    zh_index = output_root / "zh" / "index.html"

    if en_html.exists():
        inject_switcher(en_html, "en")
        en_index.write_bytes(en_html.read_bytes())

    if zh_html.exists():
        inject_switcher(zh_html, "zh")
        zh_index.parent.mkdir(parents=True, exist_ok=True)
        zh_index.write_bytes(zh_html.read_bytes())

    print("done")


if __name__ == "__main__":
    main()
