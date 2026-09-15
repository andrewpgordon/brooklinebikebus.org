"""Makes assets/flyer-map.svg, the small route map on the flyer.

It copies the route map from public/driscoll/index.html, so the flyer always
matches the website. Run it again whenever the map on the website changes:

    python3 library/make-flyer-map.py

What it changes for print: fixed light colours instead of the website's
light/dark theme, a tighter crop around the route, bigger labels, and fewer
street names so the small map stays readable.
"""
import re
from pathlib import Path

here = Path(__file__).resolve().parent
page = (here.parent / "public/driscoll/index.html").read_text(encoding="utf-8")
svg = re.search(r'<svg viewBox="0 0 940 473".*?</svg>', page, re.S).group(0)

# Print colours. Slightly stronger than the website so they survive a home printer.
colours = {
    "--mapbg": "#EFEBE5", "--parkfill": "#DCE5CE", "--schoolfill": "#FFE3A8",
    "--roadline": "#FFFFFF", "--artline": "#CDBFAC", "--walkline": "#3D302E",
    "--rideline": "#BB262A", "--maplabel": "#5A4A47", "--mapart": "#6B5B58",
    "--text": "#1E1516", "--gold": "#FFB101",
}
for name, hexcode in colours.items():
    svg = svg.replace(f"var({name})", hexcode)
leftover = re.findall(r"var\(--[a-z-]+\)", svg)
if leftover:
    raise SystemExit(f"Unknown colours in the website map: {sorted(set(leftover))}")

# Crop to the route.
svg = svg.replace('viewBox="0 0 940 473"', 'viewBox="60 20 880 400"', 1)
svg = re.sub(r'<rect x="0" y="0" width="940" height="473"', '<rect x="60" y="20" width="880" height="400"', svg, count=1)
svg = re.sub(r'\s(role|aria-label)="[^"]*"', "", svg)

# Street names: drop the small ones, enlarge the rest.
for drop in ("MARION ST", "COREY HILL PARK", "7:05 Mason Terr"):
    svg = re.sub(rf'\s*<text[^>]*>{drop}</text>', "", svg)
svg = svg.replace('font-size="12" letter-spacing="0.12em"', 'font-size="17" letter-spacing="0.1em"')
svg = svg.replace('font-size="11" letter-spacing="0.1em"', 'font-size="15" letter-spacing="0.08em"')
svg = svg.replace('stroke-width="5" stroke-linejoin="round">', 'stroke-width="6" stroke-linejoin="round">', 1)

# Stop labels: bigger and shorter.
svg = svg.replace('font-size="14.5" font-weight="800"', 'font-size="22" font-weight="800"')
svg = svg.replace('stroke-width="5.5"', 'stroke-width="7"')
for old, new in {
    "7:15 Griggs Park, NE corner": "7:15 Griggs Park",
    "7:38 Washington Sq (join here too)": "7:38 Washington Sq",
    "7:45 DRISCOLL": "7:45 Driscoll",
}.items():
    svg = svg.replace(f">{old}<", f">{new}<")

svg = svg.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" ', 1)
out = here / "assets/flyer-map.svg"
out.write_text(svg + "\n", encoding="utf-8")
print(f"Wrote {out}")
