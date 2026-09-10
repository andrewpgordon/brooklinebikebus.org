# brooklinebikebus.org

Static site for the Brookline, MA bike buses. Plain HTML and one stylesheet —
no build step, no dependencies, nothing to keep up to date. If you can edit a
text file you can update this site.

```
public/                    ← THE WEBSITE. Only this folder is published.
  index.html               homepage — for now, just sends people to /driscoll/
  driscoll/index.html      the Driscoll ride page
  assets/
    site.css               every colour, every component, shared by all pages
    favicon.svg
    og-default.png         social preview for the town-wide homepage (parked)
    og-driscoll.png        social preview for the Driscoll page
  CNAME                    the domain, for the record (GitHub ignores it — see below)
  .nojekyll                harmless leftover (see below)
  robots.txt
  sitemap.xml

docs/                      project notes — NOT published to the web
  links.local.md           gitignored; URLs that expose sign-up data
  archive/landing-townwide.html   the old town-wide homepage, parked
CLAUDE.md                  project brief for Claude — NOT published
README.md                  this file — NOT published
.gitignore                 keeps links.local.md out of the repo
.github/workflows/deploy.yml   publishes public/ on every push
```

**Why the `public/` split:** GitHub's simple "deploy from a branch" option can
only publish the repo root or `/docs`. Either would put `CLAUDE.md`, the project
notes, and the contacts list on the public web. The workflow in
`.github/workflows/deploy.yml` publishes `./public` and nothing else. There is
still no build step — the files are uploaded exactly as they are.

**If you add a page, it goes in `public/`.**

---

## Deploying it the first time

This was done in September 2026. The steps are here for whoever has to set it
up again. The repo is `andrewpgordon/brooklinebikebus.org`; the domain is
registered at **Namecheap**.

1. **Create the repo.** On GitHub, a new public repository named
   `brooklinebikebus.org`. Public matters — GitHub Pages needs it on the free
   tier.

2. **Turn on Pages before you push.** Repo → Settings → Pages → Source:
   **GitHub Actions** (*not* "Deploy from a branch"). If you push first, the
   first run fails with a "Pages not enabled" error. No harm done: turn Pages
   on, then Actions tab → the failed run → **Re-run all jobs**.

3. **Push these files**, from inside the project folder:
   ```bash
   git init -b main
   git add .
   git status
   ```
   Read the list `git status` prints. **`docs/links.local.md` must not be in
   it.** If it is, stop — the `.gitignore` file is missing. Once it's right:
   ```bash
   git commit -m "Initial site"
   git remote add origin https://github.com/YOURNAME/brooklinebikebus.org.git
   git push -u origin main
   ```
   Watch it under the Actions tab; a deploy takes about a minute.

   Before the domain is connected, the site is also at
   `YOURNAME.github.io/brooklinebikebus.org/` — but it looks unstyled there,
   because the pages load `/assets/…` from the root of the domain. That's
   expected. Judge it on the real domain.

4. **Point the domain at GitHub.** Namecheap → Domain List →
   brooklinebikebus.org → **Manage** → **Advanced DNS**.

   *Delete* only Namecheap's parking records:
   - the `A Record` for host `@` with value `162.255.119.103` — or, if that's
     not there, a `URL Redirect Record` for host `@`
   - the `CNAME Record` for host `www` with value `parkingpage.namecheap.com.`

   *Leave alone* the **Mail Settings** section and the `TXT` record starting
   `v=spf1` — they run the domain's email forwarding.

   *Add*:

   | Type         | Host | Value |
   |--------------|------|-------|
   | A Record     | @    | 185.199.108.153 |
   | A Record     | @    | 185.199.109.153 |
   | A Record     | @    | 185.199.110.153 |
   | A Record     | @    | 185.199.111.153 |
   | CNAME Record | www  | `YOURNAME.github.io.` |

   TTL "Automatic" is fine. Optional, for phones on IPv6-only networks: four
   `AAAA Record`s on `@` — `2606:50c0:8000::153`, `2606:50c0:8001::153`,
   `2606:50c0:8002::153`, `2606:50c0:8003::153`.

5. **Tell GitHub the domain — after step 4, not before.** Settings → Pages →
   Custom domain → `brooklinebikebus.org` → Save. As soon as it's saved, the
   github.io address starts forwarding to the domain, so doing this before the
   DNS works leaves the site unreachable for a while. When the DNS check shows
   green and the certificate is issued (anywhere from minutes to a few hours),
   tick **Enforce HTTPS**.

6. **Optional, worth doing:** verify the domain on your GitHub *account*
   (profile picture → Settings → Pages → Add a domain). It gives you one `TXT`
   record to add at Namecheap, and it stops anyone else's GitHub site from
   claiming the domain if this site's Pages is ever switched off.

After that, every `git push` to `main` republishes the site within a minute.
To republish without a change: Actions → Deploy site → **Run workflow**.

**About `CNAME` and `.nojekyll` in `public/`:** with this kind of deploy
GitHub ignores both — the domain lives in Settings → Pages, and Jekyll never
runs. They're kept as a record. The upload also skips anything whose name
starts with a dot; if you ever need one published (say `public/.well-known/`),
set `include-hidden-files: true` in `.github/workflows/deploy.yml`.

---

## The things you'll actually need to change

### Changing the next ride date

The date is in more places than you'd think, and it's written a few different
ways. The reliable method: in your editor, search the whole `public/` folder
for `Oct` and look at every hit.

- `public/driscoll/index.html` — the crimson band near the top (the date *and*
  the rain date), the `description` and `og:description` tags in the `<head>`
  (written `Wednesday October 7`, no comma), and two answers in the FAQ.
- `public/index.html` — the homepage is only a redirect, but it carries its
  own copy of the `description` and `og:description` tags, because WhatsApp
  reads those from the homepage when someone pastes the bare domain.
- `public/assets/og-driscoll.png` — the picture that shows up when the link is
  pasted into WhatsApp has the date **drawn into the image**. Search won't
  find it. Ask Claude to redraw it with the new date.

While you're there, check the times in `<ul class="stops">` still match.

### The homepage

Right now `brooklinebikebus.org` sends everyone straight to `/driscoll/`.
That's deliberate while Driscoll is the only ride this site runs.

The earlier town-wide homepage — what a bike bus is, cards for Driscoll,
Lincoln and other schools, how to start one — is parked in
`docs/archive/landing-townwide.html`. To bring it back, copy it over
`public/index.html`, check its dates, add its URL back to
`public/sitemap.xml`, and put the "All routes" and "Start one" links back in
the nav on `public/driscoll/index.html`. Before it goes back up, check with
Nathan Freitas: it names him and links Lincoln's ride doc.

### Updating the sign-up form link

`public/driscoll/index.html`, search for `docs.google.com/forms`. One link, in the
gold call-to-action block.

### Marking a volunteer role filled

`public/driscoll/index.html`, in `<div class="vols">`. Swap
`<span class="need open">1 needed</span>` for
`<span class="need filled">Filled &middot; Name</span>`. The class controls the
colour, so change it as well as the words.

### Adding a school

First bring back the town-wide homepage (see "The homepage" above) — with two
schools, the domain can't just redirect to one of them.

1. `cp -r public/driscoll public/lincoln` (or whichever).
2. Edit `public/lincoln/index.html`: the `<title>`, the meta description, the
   `og:` tags, the `<h1>`, the schedule, the map, the contacts.
3. Add a card to `public/index.html` in `<section id="routes">` — copy an existing
   `<div class="route-card">`. Add `class="route-card live"` if it has a
   confirmed next ride.
4. Add the URL to `public/sitemap.xml`.

If a school wants its own colours, add a body class and override the two
variables — everything else follows:

```css
body.school-lincoln{ --crimson:#123456; --gold:#ABCDEF; }
```

### Making a new route map

The maps are inline SVG, drawn from OpenStreetMap street geometry and USGS
elevation data rather than map tiles — so they work offline, print cleanly,
and follow the light/dark theme. They're generated, not hand-drawn. Ask Claude
to build one for a new route; the method is: pull the street network from the
Overpass API for a bounding box, route the path with Dijkstra, project
lat/lon to SVG coordinates, and emit paths.

---

## Conventions worth keeping

**Colours only live in `public/assets/site.css`.** Nothing else should contain a hex
code except the inline SVG maps, which use `var(--…)` and inherit.

**Both themes, always.** Every colour is defined in the bare `:root` block
first, then overridden for dark. If you add a colour only inside the dark
block, it won't exist in light mode and something will go invisible.

**Watch the cascade in `.cta`.** `.cta a { color: inherit }` will override a
plain `.btn` rule because it's more specific. That's why the button rule is
written `.cta a.btn` and placed after it. This bug shipped once already: the
sign-up link rendered dark-on-dark and nobody could see it.

**Every page needs its own `og:image`, `og:title` and `og:description`.**
These are what people see when the link gets pasted into WhatsApp, which is
how most families will actually meet this site.

---

## Legal

The release wording on the Driscoll page and in the sign-up form is a careful
draft, **not legal advice**, and it has not been reviewed by a lawyer. If you
reuse it for another school, get it reviewed. The specific question worth
asking: whether a parent can release claims on behalf of their own minor child
in Massachusetts.

Do not describe any of these rides as school-sponsored, and do not use a
school's logo or branding. They are informal rides organized by parents.

---

## Credits

Map data © [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors
(ODbL). Elevation data from the USGS 3DEP 10-metre model, via
[OpenTopoData](https://www.opentopodata.org/). Typefaces are
Archivo, Source Serif 4 and IBM Plex Mono, all via Google Fonts.

Supported by [Massachusetts Safe Routes to School](https://www.mass.gov/safe-routes-to-school),
a program of MassDOT.
