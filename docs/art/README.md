# Where the pictures came from

Full-size originals live here. Only the versions in `public/assets/` are
published.

**`driscoll-badge-original.jpeg`**. The dragon badge, made in Gemini by Andrew
in Sep 2026. It reads "Driscoll Bike Bus · Brookline, MA" on purpose, never
"Driscoll School" (D14). Published as `public/assets/driscoll-badge.webp`, on
the flyer, poster and handlebar tags as
`library/assets/driscoll-badge-print.png`, and at 62px as the Driscoll logo on
the homepage.

**`pierce-flyer-2026-10-09.webp`**. The flyer Pierce sent round in Sep 2026.
Two pieces of it are on the site, with credit, and Marissa Vogt still needs to
be asked about that (see `../open-questions.md`). The drawing and the map were
each cut out of the flyer by hand, trimmed of their white edges, and resized:
the drawing to 900px as `public/assets/pierce-penguins.jpg`, the map to 928px
wide as `public/assets/pierce-route-map.png`.

The square version on the homepage card came from the drawing:

```bash
magick public/assets/pierce-penguins.jpg -crop 655x655+195+150 +repage \
  -resize 360x360 -quality 82 -strip public/assets/pierce-card.jpg
```

That crop centres the lead penguin and cuts off the white strip down the right
side of the original, which would otherwise show as a pale sliver in dark mode.

The route map on `/pierce/` is their own Google map, credited in the legend.
