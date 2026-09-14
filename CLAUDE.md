# CLAUDE.md — Brookline Bike Bus

Read this first. It is the whole project in one page; `docs/` has the detail.

## What this is

A parent-organized bike bus for the **Michael Driscoll School** in Brookline, MA,
plus the static site that hosts it at **brooklinebikebus.org**. A bike bus is a
group of kids and adults riding to school together on a set route at a set time,
at the pace of the slowest rider.

**The first ride is a pilot: Wednesday, October 7, 2026** (National Walk & Roll to
School Day). Rain date Thursday October 8. If turnout is good it goes monthly.

The domain is meant to be town-wide, not Driscoll-only — Lincoln and Pierce
already run bike buses. **For now, though, the homepage simply redirects to
`/driscoll/`** (Andrew's call, Sep 10 — see D13 in `docs/decisions.md`). The
town-wide homepage is parked in `docs/archive/landing-townwide.html`.

## Who

| Who | Role | Contact |
|---|---|---|
| **Andrew Gordon** | organizer, ride captain, repo owner | andrewpgordon@gmail.com · 781.879.3883 |
| **Nicole McClelland** | co-organizer, sweep | nicole.mcclelland@gmail.com · 336.314.2202 |
| Tina Hein | MA Safe Routes to School (MassDOT), offering route audit + free gear | Tina.Hein@aecom.com · 617.371.4428 |
| Nathan Freitas | runs the Lincoln School bike bus; the model we copied | nathanfreitas@gmail.com · 718-569-7272 |

## Current state

- ✅ Route decided, measured, and mapped
- ✅ Flyer / ride page written
- ✅ Google Form live and collecting sign-ups
- ✅ Site pushed to `andrewpgordon/brooklinebikebus.org`, deploying via Actions
- ✅ Domain bought at **Namecheap** (Sep 2026); live at https://brooklinebikebus.org
  with HTTPS enforced (www and github.io redirect to it)
- ✅ Tina (SRTS) emailed by Andrew; principal + PTO emailed by Nicole (Sep 2026)
- ✅ Tina replied Sep 14: light-touch permissions (basic form, if any); police
  contact is on us; add "ride with traffic, on the right" (done). See
  `docs/outreach/email-tina-srts.md`
- ✅ Nathan messaged about the landing page (Sep 2026) — waiting on his reply
- ⬜ Release language not yet seen by a lawyer ← **blocker**. Andrew has asked
  Tina and other bike buses what they use — useful, but not a legal review.
  Draft for a lawyer: `docs/outreach/email-lawyer-release.md`
- ⬜ Route not yet ridden in person at 7:30 on a school day ← **blocker**
- ⬜ Four volunteer roles unfilled

See `docs/open-questions.md` for the full list, and `docs/timeline.md` for the
week-by-week plan.

## The route (final — don't re-litigate without reading docs/decisions.md)

**Walking group** (optional, for Corey Hill families) — 0.46 mi:
`7:00` Summit Ave & Jordan Rd (218 ft) → `7:05` Summit Ave & Mason Terrace
(137 ft) → down Summit to Beacon → west along the Beacon sidewalk → **cross
Beacon at the Marion Street lights** → Marion St → footpath down to Griggs
Terrace → `7:15` Griggs Park NE corner (36 ft). Bikes are **walked**, not
ridden — Summit is 8–12% and the footpath about 10%. (Crossing is at Marion,
not Summit Ave — Andrew's correction, D15.)

**The ride** — 0.74 mi, max 3%:
`7:15–7:30` gather, Griggs Park NE corner → `7:30` roll out via Griggs Terrace
and Griggs Road → `7:38` Washington Square, **dismount and walk bikes across
Beacon Street** as one group → `7:45` Driscoll bike racks. Bell is 8:00.

Two hard rules, both load-bearing:
1. **The bike bus never rides on Beacon Street.** It crosses it twice, both
   times on foot.
2. **The bike bus never rides on Summit Avenue.** The hill is walked, before
   the ride starts.

## Repo layout

**`public/` is the website. Everything outside it is private to the project.**

```
public/                  ← the only thing published to the web
  index.html             redirect to /driscoll/ (keeps its own og: tags for WhatsApp)
  driscoll/index.html    the Driscoll ride page
  assets/                site.css (all colours + components), favicon, OG images
  CNAME .nojekyll robots.txt sitemap.xml
docs/                    why everything is the way it is — NOT published
  links.local.md         gitignored; holds URLs that expose sign-up data
CLAUDE.md                this file — NOT published
README.md                deploy + edit guide — NOT published
.gitignore               keeps *.local.md out of the public repo
.github/workflows/deploy.yml   uploads ./public to Pages on every push to main
```

That split is load-bearing. GitHub's branch-based Pages deployment can only
publish the repo root or `/docs`, either of which would put `CLAUDE.md` and the
project notes on the public web at `brooklinebikebus.org/CLAUDE.md`. So the
workflow publishes `./public` and nothing else. **If you add a page, it goes in
`public/`.**

Note the repo is **public** (required for free Pages), so `docs/` is readable on
GitHub even though it isn't served on the domain. Names and phone numbers in
there are already on the flyer by choice. The form-editor and responses-sheet
URLs are *not* — they live in `docs/links.local.md`, which is gitignored via
`*.local.md`. Don't paste them into a tracked file.

Plain HTML, one stylesheet, **no build step and no dependencies**. The workflow
uploads the files exactly as they are. This is deliberate: a volunteer successor
must be able to change a date without installing anything. Do not add a
framework, a bundler, or npm without a concrete reason and Andrew's agreement.

## Conventions

- **Colours only in `assets/site.css`.** Driscoll's are crimson `#BB262A` and
  gold `#FFB101`. Nothing else holds a hex code except the inline SVG maps,
  which use `var(--…)`.
- **Both themes always.** Define every colour in bare `:root` first, then
  override in the dark blocks. A colour defined only in a dark block goes
  invisible in light mode.
- **`.cta a.btn` must stay after `.cta a`.** `.cta a{color:inherit}` outranks a
  bare `.btn` rule and once rendered the sign-up button dark-on-dark. A parent
  caught it, not us.
- **Every page needs its own `og:image`, `og:title`, `og:description`.** Most
  families meet this site as a WhatsApp link preview.
- **Never call these rides school-sponsored.** They are not. Do not use school
  logos or branding. (The dragon badge on the Driscoll page is our own
  AI-generated art reading "Driscoll Bike Bus" — see D14. Never "Driscoll School".) The disclaimer wording in `docs/release-language.md` is
  canonical — if you change it in one place, change it everywhere.

## Maps

The route maps are **inline SVG generated from real data**, not map tiles —
so they print, work offline, and follow the theme. Method, if you need another:

1. Pull the street network from the **Overpass API** for a bounding box.
2. Route the path with **Dijkstra**, penalising arterials (Beacon ×6) and
   footpaths for the riding leg so it prefers quiet streets.
3. Elevations from **OpenTopoData** (`ned10m` = USGS 3DEP 10-metre).
4. Project lat/lon equirectangular with a `cos(lat)` correction, simplify, emit
   `<path>` elements.
5. Text labels need a **halo drawn as a duplicate stroked `<text>` underneath** —
   `paint-order` works in browsers but silently inverts in some renderers.

Full measured data in `docs/route-analysis.md`. It took real work to gather;
don't re-measure without reading it first.

## Tone

The flyer and site are written for tired parents at 6am, not for a committee.
Plain, warm, specific, no exclamation marks, no jargon, no "join us for an
exciting morning of…". Where something is unsafe, say so plainly and say what
to do instead. Where a family might feel judged — a wobbly rider, a kid who
needs to walk — say explicitly that it's fine.

**It must not read as AI-written** (Andrew, Sep 10). On the site and in
anything sent under Andrew's name: no em dashes (use a period, comma or
parentheses); no rhythmic threes like "one route, one time, at the pace of the
slowest rider"; no paired slogans like "nobody rides alone, nobody gets
dropped"; no one-word punchlines ("Never.") or neat closing one-liners
("Nobody is keeping score."). Write the way a parent texts other parents:
ordinary sentences, contractions, concrete facts.
