#!/usr/bin/env python3
"""
Build permission-slip.pdf — a printable, fillable-by-hand permission slip
for the Roll Smart, Ride Safe video shoot.

Re-run any time the markdown source changes:
    python3 build-pdf.py
"""

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUT = "permission-slip.pdf"

# Color palette matching the campaign
INK = HexColor("#14213D")
INK_SOFT = HexColor("#2A3A5F")
MARIGOLD = HexColor("#F5A623")
MARIGOLD_DEEP = HexColor("#D88A0A")
STOP = HexColor("#E63946")
PAPER_2 = HexColor("#F7E7B8")


def underline(c, x1, y, x2, weight=0.8):
    c.setStrokeColor(INK)
    c.setLineWidth(weight)
    c.line(x1, y, x2, y)


def checkbox(c, x, y, size=10):
    c.setStrokeColor(INK)
    c.setLineWidth(1.2)
    c.setFillColor(white)
    c.rect(x, y, size, size, stroke=1, fill=1)


def field_line(c, label, x, y, width, label_size=7.5):
    """Draw a labeled blank line for handwriting."""
    c.setFillColor(INK_SOFT)
    c.setFont("Helvetica-Bold", label_size)
    c.drawString(x, y + 14, label.upper())
    underline(c, x, y, x + width)


def section_heading(c, text, x, y):
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x, y, text.upper())
    # Marigold underline accent
    c.setStrokeColor(MARIGOLD)
    c.setLineWidth(2.5)
    c.line(x, y - 4, x + 60, y - 4)


def build(path=OUT):
    width, height = LETTER
    c = canvas.Canvas(path, pagesize=LETTER)
    c.setTitle("Parental Consent & Media Release — Roll Smart, Ride Safe")
    c.setAuthor("City of Batavia · E-Mobility Campaign")
    c.setSubject("Permission slip for video shoot on May 19, 2026")

    margin_x = 0.6 * inch
    right_x = width - margin_x
    content_w = right_x - margin_x

    y = height - 0.55 * inch

    # ── Header band ─────────────────────────────────────────────
    c.setFillColor(INK)
    c.rect(0, y - 8, width, 6, stroke=0, fill=1)
    c.setFillColor(MARIGOLD)
    c.rect(0, y - 14, width, 6, stroke=0, fill=1)

    y -= 36
    c.setFillColor(STOP)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(margin_x, y, "— PERMISSION SLIP —")

    y -= 28
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(margin_x, y, "Parental Consent & Media Release")

    y -= 18
    c.setFillColor(INK_SOFT)
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(margin_x, y, "for the “Roll Smart, Ride Safe” safety-video shoot")

    # ── Shoot details box ───────────────────────────────────────
    y -= 24
    box_h = 44
    c.setFillColor(PAPER_2)
    c.setStrokeColor(INK)
    c.setLineWidth(1.5)
    c.roundRect(margin_x, y - box_h, content_w, box_h, 8, stroke=1, fill=1)

    col_w = content_w / 3
    labels_vals = [
        ("DATE", "Tue · May 19, 2026"),
        ("TIME", "11:00 AM"),
        ("LOCATION", "Bike Rack Area"),
    ]
    for i, (lbl, val) in enumerate(labels_vals):
        cx = margin_x + i * col_w + 14
        c.setFillColor(INK_SOFT)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(cx, y - 16, lbl)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(cx, y - 32, val)

    y -= box_h + 22

    # ── About the project ───────────────────────────────────────
    section_heading(c, "About the project", margin_x, y)
    y -= 18
    c.setFillColor(INK)
    c.setFont("Helvetica", 10)
    intro = (
        "Our school is participating in the Roll Smart, Ride Safe video campaign — "
        "a fun, fast-paced series of short videos that teach students about bike "
        "and e-bike safety, helmet use, and traffic laws."
    )
    intro_lines = wrap(intro, 95)
    text_obj = c.beginText(margin_x, y)
    text_obj.setLeading(13)
    for line in intro_lines:
        text_obj.textLine(line)
    c.drawText(text_obj)
    y -= 13 * len(intro_lines) + 6

    # Participation list
    items = [
        ("Lead roles:", "delivering short scripted safety lines (“Yikes! Glad I wore my helmet!”)."),
        ("Light acting:", "dusting off after a simulated near-miss, picking up a bike, reacting to a close call."),
        ("Extras:", "reacting in the background to show surprise or relief."),
        ("Wardrobe:", "normal riding clothes — bring your own bike helmet."),
    ]
    for bold, rest in items:
        c.setFillColor(MARIGOLD_DEEP)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(margin_x + 8, y, "•")
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(margin_x + 20, y, bold)
        bold_w = c.stringWidth(bold, "Helvetica-Bold", 9.5)
        c.setFont("Helvetica", 9.5)
        c.drawString(margin_x + 20 + bold_w + 4, y, rest)
        y -= 13

    # Safety note band
    y -= 6
    note_h = 30
    c.setFillColor(INK)
    c.roundRect(margin_x, y - note_h, content_w, note_h, 6, stroke=0, fill=1)
    c.setFillColor(MARIGOLD)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(margin_x + 12, y - 14, "SAFETY:")
    c.setFillColor(white)
    c.setFont("Helvetica", 9)
    c.drawString(
        margin_x + 56, y - 14,
        "All “crashes” and “near-misses” are simulated through acting and"
    )
    c.drawString(
        margin_x + 56, y - 24,
        "creative editing. No students will be placed in actual physical danger during filming."
    )
    y -= note_h + 14

    # ── Student section ─────────────────────────────────────────
    section_heading(c, "Student", margin_x, y)
    y -= 26

    field_line(c, "Student name", margin_x, y, content_w)
    y -= 28

    half_w = (content_w - 16) / 2
    field_line(c, "School", margin_x, y, half_w)
    field_line(c, "Grade / teacher", margin_x + half_w + 16, y, half_w)
    y -= 26

    # ── Role section ────────────────────────────────────────────
    section_heading(c, "Role  (check one)", margin_x, y)
    y -= 20
    checkbox(c, margin_x, y - 1)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_x + 16, y + 1, "Lead Actor")
    c.setFont("Helvetica", 9.5)
    c.setFillColor(INK_SOFT)
    c.drawString(margin_x + 80, y + 1, "(speaking lines + light acting)")

    checkbox(c, margin_x + 280, y - 1)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_x + 296, y + 1, "Extra")
    c.setFont("Helvetica", 9.5)
    c.setFillColor(INK_SOFT)
    c.drawString(margin_x + 332, y + 1, "(background / non-speaking)")
    y -= 22

    # ── Parent / Guardian section ───────────────────────────────
    section_heading(c, "Parent / Guardian", margin_x, y)
    y -= 26
    field_line(c, "Parent or guardian name", margin_x, y, half_w)
    field_line(c, "Emergency contact phone", margin_x + half_w + 16, y, half_w)
    y -= 28
    field_line(c, "Email (optional — for confirmation copy)", margin_x, y, content_w)
    y -= 26

    # ── Consent section ─────────────────────────────────────────
    section_heading(c, "Consent", margin_x, y)
    y -= 16
    c.setFillColor(INK_SOFT)
    c.setFont("Helvetica-Oblique", 9)
    intro2 = (
        "I, the undersigned, being the parent or legal guardian of the student named above, "
        "do hereby grant permission for my child to participate in the “Roll Smart, Ride Safe” "
        "video production. By signing below, I understand and agree to the following:"
    )
    intro2_lines = wrap(intro2, 105)
    text_obj = c.beginText(margin_x, y)
    text_obj.setLeading(12)
    for line in intro2_lines:
        text_obj.textLine(line)
    c.drawText(text_obj)
    y -= 12 * len(intro2_lines) + 6

    consents = [
        ("Media Release.",
         "I authorize the use of my child's image, voice, and performance in the "
         "final videos for educational, promotional, or social-media purposes related "
         "to the Roll Smart, Ride Safe campaign."),
        ("Safety & Supervision.",
         "I understand that filming will take place on school property under the "
         "supervision of school staff and the production team."),
        ("Voluntary Participation.",
         "I understand that participation is voluntary, and that donuts and water "
         "will be provided for those involved."),
    ]
    for bold, rest in consents:
        checkbox(c, margin_x, y - 1)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(margin_x + 16, y + 1, bold)
        bold_w = c.stringWidth(bold, "Helvetica-Bold", 9.5)
        c.setFont("Helvetica", 9.5)
        # Wrap the remaining text after the bold lead-in
        first_line_x = margin_x + 16 + bold_w + 4
        first_line_w = right_x - first_line_x
        remaining = rest
        char_w_first = int(first_line_w / 4.6)
        char_w_rest = int((content_w - 16) / 4.6)
        lines = wrap(remaining, char_w_first, char_w_rest)
        for i, line in enumerate(lines):
            if i == 0:
                c.drawString(first_line_x, y + 1, line)
            else:
                c.drawString(margin_x + 16, y + 1 - 11 * i, line)
        y -= 11 * len(lines) + 6

    # ── Signature ───────────────────────────────────────────────
    y -= 4
    section_heading(c, "Signature", margin_x, y)
    y -= 26
    sig_w = content_w * 0.62
    date_w = content_w - sig_w - 16
    field_line(c, "Parent / guardian signature", margin_x, y, sig_w)
    field_line(c, "Date", margin_x + sig_w + 16, y, date_w)
    # ── Return note + footer (anchored to bottom of page) ───────
    # Use a fixed y so it never overlaps the variable signature block.
    c.setFillColor(INK_SOFT)
    c.setFont("Helvetica-Oblique", 9.5)
    note = "Please return this signed slip to the front office or your child's teacher by Monday, May 18."
    c.drawCentredString(width / 2, 30, note)

    # Footer band
    c.setFillColor(MARIGOLD)
    c.rect(0, 14, width, 4, stroke=0, fill=1)
    c.setFillColor(INK)
    c.rect(0, 10, width, 4, stroke=0, fill=1)
    c.setFillColor(INK_SOFT)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(width / 2, 2, "CITY OF BATAVIA · E-MOBILITY CAMPAIGN · ORDINANCE 2026-010")

    c.showPage()
    c.save()
    print(f"Wrote {path}")


def wrap(text, width_first, width_rest=None):
    """Word-wrap text to roughly `width_*` characters per line."""
    if width_rest is None:
        width_rest = width_first
    words = text.split()
    lines, cur, cur_len, limit = [], [], 0, width_first
    for w in words:
        add = len(w) + (1 if cur else 0)
        if cur_len + add > limit and cur:
            lines.append(" ".join(cur))
            cur, cur_len, limit = [w], len(w), width_rest
        else:
            cur.append(w)
            cur_len += add
    if cur:
        lines.append(" ".join(cur))
    return lines


if __name__ == "__main__":
    build()
