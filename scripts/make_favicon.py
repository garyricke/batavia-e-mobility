#!/usr/bin/env python3
"""Build favicon.svg (rounded, for tabs) and apple-touch source (full-bleed)
from the City of Batavia windmill mark."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, "assets", "city-of-batavia-logo-mark.svg")).read()

# inner content = everything between the opening <svg ...> and </svg>
inner = re.search(r"<svg[^>]*>(.*)</svg>", src, re.S).group(1).strip()

# favicon.svg — 64x64, white rounded square, windmill centered (~8px padding)
favicon = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">\n'
    '  <rect width="64" height="64" rx="13" fill="#FFFFFF"/>\n'
    '  <g transform="translate(14 8) scale(0.191)">\n    ' + inner + '\n  </g>\n'
    '</svg>\n'
)
open(os.path.join(ROOT, "favicon.svg"), "w").write(favicon)

# apple-touch source — 180x180, full-bleed white (Apple rounds it), ~20px padding
apple = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180">\n'
    '  <rect width="180" height="180" fill="#FFFFFF"/>\n'
    '  <g transform="translate(37 20) scale(0.557)">\n    ' + inner + '\n  </g>\n'
    '</svg>\n'
)
open("/tmp/apple-touch.svg", "w").write(apple)
print("favicon.svg + /tmp/apple-touch.svg written")
