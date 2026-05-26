#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if [ ! -d .venv ]; then
  echo ".venv not found, run: python3 -m venv .venv && .venv/bin/pip install 'rendercv[full]==2.8'"
  exit 1
fi

. .venv/bin/activate

echo "=== Rendering EN ==="
rendercv render cv-en.yaml

echo ""
echo "=== Rendering ZH ==="
rendercv render cv-zh.yaml --output-folder rendercv_output/zh

echo ""
echo "=== Done ==="
echo "  HTML:  http://localhost:8080/Yao_Chius_CV.html"
echo "  PDF:   http://localhost:8080/Yao_Chius_CV.pdf"
echo "  ZH:    http://localhost:8080/zh/Yao_Chius_CV.html"
echo ""
echo "Starting server..."

python3 -m http.server 8080 --directory rendercv_output
