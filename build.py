"""Build the static quiz and set its deployed backend URL."""

import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "index.html"
OUTPUT = ROOT / "dist"
API_URL = os.environ.get("API_BASE_URL", "").strip().rstrip("/")

if not re.fullmatch(r"https://[A-Za-z0-9.-]+(?::\d+)?", API_URL):
    raise SystemExit("Set API_BASE_URL to the backend's HTTPS base URL in Render.")

html = SOURCE.read_text(encoding="utf-8")
html, count = re.subn(
    r'(<meta\s+name="quiz-api-base"\s+content=")[^"]*("\s*/?>)',
    lambda match: f"{match.group(1)}{API_URL}{match.group(2)}",
    html,
    count=1,
    flags=re.IGNORECASE,
)
if count != 1:
    raise SystemExit('Could not find the quiz-api-base meta tag in index.html.')

OUTPUT.mkdir(parents=True, exist_ok=True)
(OUTPUT / "index.html").write_text(html, encoding="utf-8")
print(f"Built quiz frontend for backend: {API_URL}")
