# OG image — social preview

`og-image.png` (1200×630, PIL-rendered) is the canonical social preview card for the repo. It's what appears when the repo link is shared on Twitter/X, Slack, LinkedIn, or any other platform that reads OpenGraph metadata.

## Files

| File | Role |
|---|---|
| `og-image.svg` | Hand-edited source. Calibre/Swiss editorial style. The truth. |
| `og-image.png` | 1200×630 rasterized rendering, used by GitHub's social preview. |
| `regen.py` | Re-render the PNG from PIL primitives. Run when you bump version numbers or the verdict line. |

## Upload to GitHub social preview

The PNG is **not** auto-served. GitHub stores the social preview separately from the repo. Manual upload:

1. Go to `https://github.com/hoainho/iamhumans/settings`
2. Scroll to "Social preview"
3. Click "Edit" → "Upload an image"
4. Pick `assets/og/og-image.png`
5. Save

After upload, sharing the repo link on any OpenGraph-aware platform will render with this card.

## Regenerating

```sh
cd <repo-root>
python3 assets/og/regen.py
```

Requires Pillow (`pip install Pillow`). The script outputs the PNG in this same directory. If you change the SVG, you'll need to update the corresponding PIL code in `regen.py` — they are intentionally separate (SVG = visual reference, PIL = production renderer).

## Design rationale

- **Calibre/Swiss editorial palette**: warm off-white (#FAF8F4) background, ink (#1A1A1A) primary, single accent through the dark verdict block.
- **Hairline frame** at 32px inset — gives the card a printed-page feel.
- **Verdict centerpiece**: the held-out oracle line is the headline because it's the evidence other repos can't replicate. The dark block makes it the visual anchor.
- **Three data panels**: 93.27 (Pareto aggregate) · 86.7% (cross-judge agreement) · 20·100 (corpus depth). Each number is concrete, each label is specific.
- **Foot tagline**: *"Honestly imperfect. Read the Known Weaknesses."* — the line that distinguishes iamhumans from sloppy marketing repos. Same line as the GitHub description.

The image is light-locked on purpose. A dark variant could be added at `og-image-dark.png` but most OG-aware platforms render in light-mode bias, so light is the safe default.
