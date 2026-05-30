"""Render the OG social-preview card for github.com/hoainho/iamhumans.

Outputs a 1200x630 PNG suitable for GitHub's repo social preview.
Run from the repo root: ``python3 assets/og/regen.py``.

Requires Pillow (``pip install Pillow``). The PIL composition here is
the production renderer; ``og-image.svg`` in the same directory is a
visual reference, not used at runtime.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630

INK = (26, 26, 26)
DARK_GREY = (74, 74, 74)
DIM = (215, 206, 185)
PAPER = (250, 248, 244)


def load_font(size: int, weight: str = "regular") -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    bold_first = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/System/Library/Fonts/SF-Pro-Display-Bold.otf",
    ]
    candidates = [
        "/System/Library/Fonts/SF-Pro.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    if weight == "bold":
        candidates = bold_first + candidates
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main() -> None:
    img = Image.new("RGB", (W, H), color=PAPER)
    draw = ImageDraw.Draw(img)

    f_bold_huge = load_font(84, "bold")
    f_bold_big = load_font(56, "bold")
    f_reg_med = load_font(32, "regular")
    f_italic = load_font(36, "regular")
    f_eyebrow = load_font(14, "bold")
    f_panel_label = load_font(13, "bold")
    f_panel_caption = load_font(13, "regular")
    f_foot = load_font(13, "regular")

    draw.rectangle([32, 32, 1168, 598], outline=INK, width=1)

    draw.text((72, 84), "AN OPENCODE SKILL · v1.1.1 · MIT", font=f_eyebrow, fill=INK)
    url_text = "github.com/hoainho/iamhumans"
    url_w = draw.textlength(url_text, font=f_eyebrow)
    draw.text((1128 - url_w, 84), url_text, font=f_eyebrow, fill=INK)

    draw.line([(72, 118), (1128, 118)], fill=INK, width=1)

    draw.text((72, 152), "iamhumans", font=f_bold_huge, fill=INK)
    draw.text(
        (72, 252),
        "Teach an LLM to talk like a person — not sound like one.",
        font=f_reg_med,
        fill=DARK_GREY,
    )

    draw.rectangle([72, 296, 1128, 438], fill=INK)
    verdict = '"You are same as 100% real humans."'
    verdict_w = draw.textlength(verdict, font=f_italic)
    draw.text(((W - verdict_w) // 2, 336), verdict, font=f_italic, fill=PAPER)
    attrib = "— INDEPENDENT ORACLE · 10 HELD-OUT CASES · 2026-05-29"
    attrib_w = draw.textlength(attrib, font=f_eyebrow)
    draw.text(((W - attrib_w) // 2, 390), attrib, font=f_eyebrow, fill=DIM)

    panels = [
        (72, "93.27", "/100 PARETO AGGREGATE", "15-case stratified sample, 14 PASS"),
        (446, "86.7%", "VERDICT AGREEMENT", "3 Claude judges, 15 cases · Lane A1"),
        (820, "20 · 100", "BOOKS · EVAL CASES", "Kahneman, Frankl, Buber, Lao Tzu..."),
    ]
    for x, big, label, caption in panels:
        draw.text((x, 460), big, font=f_bold_big, fill=INK)
        draw.text((x, 518), label, font=f_panel_label, fill=DARK_GREY)
        draw.text((x, 538), caption, font=f_panel_caption, fill=DARK_GREY)

    for div_x in (408, 782):
        draw.line([(div_x, 466), (div_x, 552)], fill=INK, width=1)

    foot = "Honestly imperfect. Read the Known Weaknesses."
    foot_w = draw.textlength(foot, font=f_foot)
    draw.text(((W - foot_w) // 2, 575), foot, font=f_foot, fill=DARK_GREY)

    out = Path(__file__).parent / "og-image.png"
    img.save(out, "PNG", optimize=True)
    print(f"saved {out} ({W}x{H}, {out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
