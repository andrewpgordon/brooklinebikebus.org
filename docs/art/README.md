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

**`lincoln-route2-downes-chestnut.webp`**. Nathan Freitas's own annotated map of
the Lincoln Route 2 ride, sent Oct 5 2026 with a request to publish it.
Published whole as `public/assets/lincoln-route-map.webp`, and the homepage card
is a square crop of it:

```bash
magick docs/art/lincoln-route2-downes-chestnut.webp -crop 330x330+200+90 +repage \
  -resize 360x360 -quality 84 -strip public/assets/lincoln-card.webp
```

That crop is a stretch of Chestnut Street with the purple route and no label
boxes, which is the only part that still reads as anything at 62px.

**`private/lincoln-route1-walnut.png`**. His Route 1 map, sent at the same time.
**Not published**, and not publishable as it stands: it's a Google Maps
screenshot with a profile photo on it as a location pin, so putting it up would
publish somebody's whereabouts. Ask Nathan for a clean one (D19).

It sits in `docs/art/private/`, which is gitignored. The rest of `docs/` is
readable on the public GitHub repo even though none of it is served on the
domain, so a file in here that shouldn't be public has to be kept out of git
entirely. Anything else we're sent with a face or a location pin on it goes in
that folder.
