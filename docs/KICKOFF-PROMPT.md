# Kickoff prompt for the Claude Code session

Copy everything in the block below into a fresh Claude Code session opened in
this repo.

---

```
This repo is the Brookline Bike Bus project — a parent-organized bike bus for
the Driscoll School in Brookline MA, plus the static site at
brooklinebikebus.org that hosts it. I've just moved it over from another
session, so nothing has been committed yet.

The website lives in public/ and only that folder is deployed; everything else
(CLAUDE.md, docs/) is project knowledge that must never be published.

Please start by reading CLAUDE.md, then README.md, then everything in docs/.
docs/route-analysis.md has measured elevation and grade data that was expensive
to gather — don't re-measure any of it without reading that file first.
docs/decisions.md explains why the route is what it is; several options that
look obviously better were considered and rejected for reasons.

Then give me a short summary of where the project stands and what you think the
next three things are, and wait — don't start working yet.

Once we agree on the plan, the first jobs are:

1. git init, first commit, and push to a new public GitHub repo named
   brooklinebikebus.org
2. Walk me through enabling GitHub Pages — Source must be "GitHub Actions",
   not "deploy from a branch" — and the DNS records for the custom domain
   (README.md has both)
3. Confirm nothing outside public/ is reachable on the domain once it's live
4. Verify both pages render correctly in a browser — especially the inline SVG
   route map on the Driscoll page in both light and dark mode

Context you should have:
- The first ride is Wednesday October 7 2026. It's a pilot; monthly if turnout
  justifies it.
- I'm Andrew Gordon; Nicole McClelland is co-organizing.
- The sign-up form is already live and collecting responses.
- Two things are genuinely blocking and I'd like you to keep reminding me:
  the release language hasn't been seen by a lawyer, and I haven't ridden the
  route in person at 7:30 on a school day yet.
- I'm not a professional developer. Keep the site plain HTML with no build
  step — another parent has to be able to change a ride date in two years.
```
