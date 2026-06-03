#!/usr/bin/env python3
"""Replace the watch__grid inner cards and the lede in index.html (local file edit)."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
idx = os.path.join(ROOT, "index.html")
html = open(idx).read()
cards = open("/tmp/grid.html").read().rstrip("\n")

# 1) Replace inner of <div class="watch__grid"> ... </div>
start_tag = '<div class="watch__grid">'
i = html.index(start_tag)
inner_start = i + len(start_tag)
# find the closing </div> that precedes the watch__hint paragraph
hint_i = html.index('<p class="watch__hint', inner_start)
close_i = html.rindex('</div>', inner_start, hint_i)
new_block = "\n" + cards + "\n    "
html = html[:inner_start] + new_block + html[close_i:]

# 2) Update the lede copy
old_lede = ('<p class="watch__lede reveal">Five near-misses you don\'t want to star in. '
            '<strong>Hover to preview</strong> a clip. Tap any card to watch full-screen with sound.</p>')
new_lede = ('<p class="watch__lede reveal">The whole squad, in their own words. '
            '<strong>Hover to preview</strong>, tap any card to watch full-screen with sound, '
            'or <strong>download the HQ video</strong> to share on social.</p>')
assert old_lede in html, "lede not found"
html = html.replace(old_lede, new_lede)

open(idx, "w").write(html)
print("grid + lede updated; new length", len(html))
