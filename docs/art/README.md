# Where the pictures came from

Full-size originals live here. Only the versions in `public/assets/` are
published.

**`driscoll-badge-original.jpeg`** — the dragon badge, made in Gemini by Andrew
in Sep 2026. It reads "Driscoll Bike Bus · Brookline, MA" on purpose, never
"Driscoll School" (D14). Published as `public/assets/driscoll-badge.webp`, and
again at 62px as the Driscoll logo on the homepage.

**`pierce-flyer-2026-10-09.webp`** — the flyer Pierce sent round in Sep 2026.
Two pieces of it are on the site, with credit, and Marissa Vogt still needs to
be asked about that (see `../open-questions.md`):

```bash
# the penguin drawing, for the top of /pierce/
magick pierce-flyer-2026-10-09.webp -crop ... -fuzz 3% -trim public/assets/pierce-penguins.jpg
# a square crop of the lead penguin, for the homepage card
magick public/assets/pierce-penguins.jpg -crop 655x655+195+150 +repage \
  -resize 360x360 -quality 82 -strip public/assets/pierce-card.jpg
```

The route map on `/pierce/` is their own Google map, cropped from the same
flyer, credited in the legend.
