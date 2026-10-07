# CLAUDE.md — Brookline Bike Bus

Read this first. It is the whole project in one page; `docs/` has the detail.

## What this is

A parent-organized bike bus for the **Michael Driscoll School** in Brookline, MA,
plus the static site that hosts it at **brooklinebikebus.org**. A bike bus is a
group of kids and adults riding to school together on a set route at a set time,
at the pace of the slowest rider.

**The first ride happened Wednesday, October 7, 2026** (National Walk & Roll to
School Day). Fifteen kids, and it worked. **The second is Wednesday, November 18,
2026**, with a few more pencilled in for the spring.

The domain is town-wide. Pierce's ride is listed at `/pierce/` (added Sep 29
from their flyer; they run it, we don't). Lincoln's is at `/lincoln/` (added
Oct 5, at Nathan Freitas's own request and from what he sent; he runs it, we
don't).

**The homepage is a chooser** (D17, Sep 29): a card for Driscoll and a card
for Pierce, each with that ride's own artwork, and the next ride in a band
above them. It replaced the redirect to `/driscoll/`. It uses neutral slate
rather than any school's colours. Every printed QR code points at the bare
domain, so Driscoll is first, wears the dragon badge from the flyer, and the
whole card is one tap. All three cards are on it. The older, longer town-wide page (what a bike bus is, how
to start one, resources) is still parked in `docs/archive/landing-townwide.html`.

## Who

| Who | Role | Contact |
|---|---|---|
| **Andrew Gordon** | organizer, ride captain, repo owner | andrewpgordon@gmail.com · 781.879.3883 |
| **Nicole McClelland** | co-organizer. Was down as sweep until Oct 1, when it turned out there's no bike | nicole.mcclelland@gmail.com · 336.314.2202 |
| Tina Hein | MA Safe Routes to School (MassDOT), offering route audit + free gear | Tina.Hein@aecom.com · 617.371.4428 |
| Nathan Freitas | runs the Lincoln School bike bus, the model we copied. Asked us on Oct 5 to list it, and to publish these details | nathanfreitas@gmail.com · 718-569-7272 |

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
- ✅ Nathan replied Oct 5 and asked for a Lincoln page like the Pierce one, with
  his name, email and phone on it. Done the same day (D19). Lincoln rides every
  Wednesday at 7:30 and alternates two routes, so the page sends people to his
  own doc for which one is running
- ✅ Pierce ride listed at `/pierce/` (Sep 29). Their organizers haven't been
  told yet, same mistake we made with Nathan
- ⬜ Release language not yet seen by a lawyer ← **blocker**. Andrew has asked
  Tina and other bike buses what they use — useful, but not a legal review.
  Draft for a lawyer: `docs/outreach/email-lawyer-release.md`
- ⬜ Route not yet ridden in person at 7:30 on a school day ← **blocker**
- ✅ 11 families signed up by Sep 28: 15 kids (BEEP to 6th grade, five of them
  kindergarten or younger) and about 16 adults
- ✅ Crew jobs worked out (Oct 1, D18). `library/crew-brief.md` is what each job
  involves and where the seven corners are; `library/huddle-script.md` is what
  to say at 7:20 and 7:26. The named assignment is in
  `docs/rides/2026-10-07-crew.local.md`, gitignored because it holds volunteers'
  and children's names. **A corner only goes to an adult riding without a child
  of their own**, since the release says each child's adult stays with them
- ⬜ Nobody has accepted a specific job yet, so `/driscoll/` still says "2
  needed". Change it after people say yes, not before
- ⬜ **The sweep is open.** Nicole has no bike (Oct 1). `/driscoll/` still says
  "Sweep: Filled, Nicole", which is now wrong, and it's left that way until
  Andrew decides whether to find a bike or move the job
- ⬜ Two Brookline PD Bicycle Squad units expected (Andrew, Oct 1). No record of
  who agreed it; the draft at `docs/outreach/email-brookline-pd.md` was never
  marked sent. **The group dismounts and walks across Beacon whether or not an
  officer is there** (D18)

See `docs/open-questions.md` for the full list, and `docs/timeline.md` for the
week-by-week plan.

## The route (final — don't re-litigate without reading docs/decisions.md)

**The walking group is gone** (D21, Oct 7 evening). Corey Hill families make
their own way to Griggs Park. Everything about Summit Ave, Jordan Rd, Mason
Terrace, the Marion Street crossing and the footpath is history now, kept in
`docs/route-analysis.md` and D15 in case it ever comes back.

**The ride** — 0.74 mi, max 3%:
`7:15–7:30` gather, Griggs Park NE corner (36 ft) → `7:30` roll out via Griggs
Terrace and Griggs Road → stop at Washington Street and wait for the group →
`7:38` Washington Square, wait again, then **ride across Beacon Street** as one
group on one light → `7:45` Driscoll bike racks. Bell is 8:00.

Two hard rules, both load-bearing:
1. **The bike bus never rides along Beacon Street.** It crosses it once, at
   Washington Square, together on one light with adults holding the
   intersection. The first ride walked that crossing. It rode it instead and
   that worked better, so riding it is the plan from now on (D21, Andrew's call
   from the day). Open: whether it worked because Brookline PD were there.
2. **The bike bus never rides on Summit Avenue.** Nothing goes up or down that
   hill as a group, which is also why the walking group is gone.

## Repo layout

**`public/` is the website. Everything outside it is private to the project.**

```
public/                  ← the only thing published to the web
  index.html             homepage: pick a school (Driscoll, Pierce, Lincoln)
  driscoll/index.html    the Driscoll ride page
  pierce/index.html      the Pierce ride, run by the SRTS Task Force, not by us
  lincoln/index.html     the Lincoln ride, run by Nathan Freitas, not by us
  assets/                site.css (all colours + components), favicon, OG images
  CNAME .nojekyll robots.txt sitemap.xml
library/                 flyer, poster kit, bulletin blurb, reusable per ride — NOT published
  rides/2026-10-07/      the PDFs actually printed for that ride
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
  gold `#FFB101`, and they're the defaults. Pierce overrides them with their
  greens (`body.school-pierce`), Lincoln with the purple of Nathan's own route
  maps (`body.school-lincoln`), and the homepage with a plain slate
  (`body.townwide`), because it isn't any one school's page. Nothing else holds
  a hex code except the inline SVG maps, which use `var(--…)`.
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

**Nothing may read as AI-written** (Andrew, Sep 10, widened Sep 15). That
covers everything: the site, print pieces, emails and blurbs sent under
Andrew's name, the notes in this repo, and replies in chat. Things to avoid:

- em dashes (use a period, comma or parentheses)
- rhythmic threes ("one route, one time, at the pace of the slowest rider")
  and paired slogans ("nobody rides alone, nobody gets dropped")
- one-word punchlines ("Never.") and tidy closers or stock reassurance ("Nobody
  is keeping score.", "That's completely fine.")
- "not X, just Y" and "X, not Y" contrasts used for effect
- a bold lead-in on every bullet, and colon-then-list sentences in prose
- filler words like "seamless", "ensure", "crucial", "robust"

Write the way a parent texts other parents: ordinary sentences, contractions,
concrete facts. Before publishing anything, reread it asking "would a tired
parent have written this?"

Older notes in `docs/` and this file were written before the rule and still
have em dashes. Fix them in any passage you're already editing.
