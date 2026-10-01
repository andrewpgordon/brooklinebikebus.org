# Decision log

Why things are the way they are. If you want to change one of these, read the
reasoning first — most were argued through more than once.

---

### D1 — One pilot ride, not a weekly commitment
Wednesday 7 October 2026, National Walk & Roll to School Day. Free publicity,
SRTS support, weather still good. Monthly is the goal *if* turnout and volunteer
numbers justify it. Starting weekly with one and a half organizers is how bike
buses die in November.

### D2 — Copy Lincoln's schedule wholesale
Lincoln starts at 8:00 and targets a 7:45 arrival, with a 15-minute gathering
window before a 15-minute ride. Same district, same bell. Their Route 2 is
*longer* than ours (0.85 mi vs 0.74) on a gentler grade, and they do it in 15
minutes — so our timings have slack. Don't pad the ride; the gathering window is
what does the real work.

### D3 — The bike bus never rides on Beacon Street
Beacon is a four-lane arterial with a trolley reservation. Every route that used
it was rejected, including two good ones. The group crosses Beacon twice, both
times **on foot**, dismounted, as one group on one light. A police escort would
make riding it possible but can't be sustained monthly, so it isn't designed in.

### D4 — The bike bus never rides on Summit Avenue
8.3% average, 12.1% maximum, and in the morning every foot of it is downhill
finishing at a signalised arterial. A pack of kids gaining speed on that is the
single most dangerous thing we could organize. The hill is walked instead.

### D5 — Start at Griggs Park, not up on the hill
Argued both ways. Starting on the hill (Summit & Mason) is where families
actually live and avoids asking them to travel away from school first — but
every way down from there is 6.4% at best and 13.4% at worst. Accepted the
trade: the hill happens *before* the ride, on foot, with a leader. Andrew's
call, and the right one — "Summit really is a lot for kids learning to cycle."

### D6 — Meet at the park's northeast corner, not "Griggs Park"
A named corner where a footpath actually enters the park. Vague meeting points
cost ten minutes on the morning. Bonus: it shortened the walk from 0.59 to
0.48 mi and lengthened the ride slightly, both improvements.

### D7 — Name Lancaster Terrace explicitly on the flyer
Families who ride down will default to Summit because it's the obvious road,
and it's the worst reasonable option. Lancaster is 6.4–7.0% and steady rather
than pitchy. Naming the least-bad option is more useful than a general warning.

### D8 — A walking group with a named leader, not "come down however"
The descent was the only genuinely hard part of the morning and the only part
with no adult assigned to it. Now it has one, and that person must live up top.
It is the hardest role to fill and the most valuable.

### D9 — Plain HTML, no build step
A volunteer successor must be able to change a ride date without installing
Node. No framework, no bundler, no npm.

### D10 — Town-wide domain, not driscollbikebus.org
Lincoln and Pierce already run bike buses. "Brookline bike bus" is what a parent
types into Google. A shared site is more useful to the town and gives somewhere
to put the next school. **Ask Nathan before promoting it** — a town-wide domain
owned by one parent reads as a land-grab if the others weren't consulted.

### D11 — Google Form over a self-hosted signup
Parents trust it, it exports to CSV for the WhatsApp and email lists, and it
records the release acknowledgement with a timestamp. Not worth building.

### D12 — Fourteen form fields cut to nine
Long forms lose people. Dropped: how kids are getting there, which adult is
riding with them (the rule lives in the release, where it binds), cross streets,
a separate date field (Forms timestamps automatically), and the WhatsApp
question (folded into the mobile field's help text). Kept the typed-name
signature — redundant with the name field, but it's the thing that makes people
actually read the box.

### D13 — For now, the homepage redirects to the Driscoll page
Sep 10, Andrew's call: "landing page should be simpler." Driscoll is the only
ride this site actually runs, and nearly every visitor is a Driscoll family, so
the bare domain goes straight to `/driscoll/`. D10 still stands — the domain
stays town-wide in intent — and the town-wide homepage is parked in
`docs/archive/landing-townwide.html` for when a second school joins.
Side effect: Lincoln and Nathan's name are no longer on the live site.

It's a static-page redirect (meta refresh plus one line of script) because
GitHub Pages can't do server redirects. WhatsApp doesn't follow it, so the
homepage keeps its own copy of the Driscoll page's `og:` tags.

### D14 — A dragon badge, but it says "Driscoll Bike Bus", not "Driscoll School"
Sep 10. Andrew made a badge in Gemini — a red cartoon dragon (Driscoll's mascot
is a dragon) in a helmet, on a bike. The first version's top arc read
"DRISCOLL SCHOOL", which in a round seal looks like an official school emblem
and cuts against the release's "not a school program". Regenerated to read
"DRISCOLL BIKE BUS · BROOKLINE, MA"; that version is on the Driscoll page.

It's our own AI-generated art, not the school's mascot artwork. Keep it that
way: don't swap in the school's real dragon, and don't put "Driscoll School"
back on it. Original in `docs/art/driscoll-badge-original.jpeg`.

### D16 — Pierce gets a page, and the homepage redirect stays until after Oct 7
Sep 29. Pierce sent round a flyer for a bike bus on Friday, October 9, run by
volunteers from the Brookline Safe Routes to School Task Force with help from
Brookline Police. It's listed at `/pierce/`, written in our own words. We
On Sep 29 Andrew asked for their own colours, drawing and map, so the page now
carries all three with credit, and points questions to Marissa Vogt rather
than to us. The wording about who runs it is light: one short paragraph under
the contact box, plus the site footer.

The obvious move was to bring back the town-wide homepage now that a second
school is on the site. Not yet. Every printed QR code (flyer tabs, poster,
handlebar tags, refill tabs) encodes the bare domain, which forwards to
`/driscoll/`. Changing that a week before Oct 7 would land those families on a
list of routes instead of the ride they're looking for. Restore the town-wide
homepage after Oct 7. Until then Pierce is linked from the Driscoll page's nav.

### D15 — The walking group crosses Beacon at Marion Street, not Summit Avenue
Sep 14, Andrew's correction. The map and notes had the walking group crossing
at the Summit Ave signal and going straight to Griggs Park — there's no path
there. The real way: down Summit to Beacon, west along the Beacon sidewalk,
across at the Marion Street lights, along Marion, and down the footpath to
Griggs Terrace. Same meeting corner, 0.46 mi instead of 0.48. Details and
elevations in `route-analysis.md`.

### D17 — The homepage is a two-card chooser, from Sep 29
Andrew asked for it eight days before the first ride: "can we do the homepage,
where you choose between schools and pages? keep it simple." That supersedes
the "keep the redirect until after Oct 7" half of D16.

What's on it: the site name, one sentence saying what a bike bus is, a band
with the next ride, and a card for Driscoll and one for Pierce. Nothing else.
The parked town-wide page also explained how to start a bike bus and listed
the Safe Routes guides; that version is still in
`docs/archive/landing-townwide.html` if any of it is wanted later.

Same day, Andrew asked for two changes: neutral colours and a logo on each
card. The page no longer borrows Driscoll's crimson and gold. `body.townwide`
in site.css swaps them for a plain slate, so the homepage belongs to no school
and each card's own artwork supplies the colour: Driscoll's dragon badge and
the penguin drawing from the Pierce flyer, cropped square as
`assets/pierce-card.jpg`.

The QR problem from D16 still applies. Every printed flyer, poster and
handlebar tag encodes the bare domain, so those families now land here rather
than on the ride page. The answer is layout. Driscoll is the first card, it
carries the dragon badge they have already seen on the flyer, and the whole
card is one big link (`.route-card a::after` covers it), so on a phone you can
tap it as soon as any of it is on screen. It still costs one tap that the
redirect didn't.

**Lincoln is deliberately not on it.** Nathan hasn't answered the message about
the town-wide domain (D10), and both rides already on this site went up before
their organizers were asked. His card is written and takes a minute to add.

### D18 — How the crew is put together, and who can hold a corner
*Oct 1, 2026, six days out.*

Andrew named the people helping on the 7th: Nicole, two more parent volunteers,
two Brookline PD Bicycle Squad units, Tina Hein from MA Safe Routes, and the
organizer of the Pierce ride. The sign-up sheet had 11 entries by Sep 28, seven
of which offered to help with something. Everyone's name and job is in the
gitignored file below, not here.

**The rule that decides the whole assignment: a corner job only goes to an
adult who is riding without a child of their own.** The release families signed,
and the Driscoll page, both say each child's own adult stays with them for the
whole ride. Corking means leaving the group for a few minutes at a time, so a
parent who is the only adult for their kid cannot do it. Four people offered
corker or crossing lead and have their own child riding, and all four were given
jobs that keep them next to that child instead. One parent's own note on the form is the
pattern for doing it the other way round. One of them rides with their three
children and the other takes a job.

**We dismount and walk across Beacon Street whether or not a police officer is
standing there.** This is the one decision the police presence could have
changed and it doesn't. Oct 7 has two officers, a monthly ride won't, and the
rule has to be the same every time or it isn't a rule. Officer positions are a
proposal until they say otherwise, and the morning has to work if they get
called away at 7:35.

What was written: `library/crew-brief.md` (the jobs, the corner list, the
Washington Square choreography, the things that go wrong) and
`library/huddle-script.md` (the 7:20 crew talk and the 7:26 talk to the kids,
built on the seven riding rules already on the website rather than a new set).
The named assignment is in `docs/rides/2026-10-07-crew.local.md`, which is
gitignored, because it holds volunteers' names, their children's names and their
mobile numbers. Andrew and Nicole put their own details on the flyer by choice.
Nobody else did.

The corners in the brief are measured off the drawn route line on the website
map, using the projection in `route-analysis.md`. There were seven to begin
with, and Andrew cut them the same day to four: the first turn, the merge onto
Washington Street, Fairbanks if there's a spare body, and two people at the
Beacon crossing covering one carriageway each. Nothing is held after Beacon,
because the group is three hundred metres from the racks by then. Andrew knows that
street and the map doesn't. The side effect worth keeping is that every position
now sits in the first 860 m, so no corker ever has to ride up the outside of a
line of children to reach a second corner. Three streets that
look like they should be on the route are not: Downing Road, Bartlett Crescent
and Corey Road all sit past the point where the ride line ends at Washington and
Bartlett. Nobody has stood at any of these corners at 7:35 on a school day,
which is still a blocker, and the brief says so on the table.

**The volunteer table on `/driscoll/` was deliberately left alone.** It still
says "2 needed" for corkers and "1 needed" for the hill walker. Nobody has
accepted a specific job yet, and the timeline says to assume one leader drops,
so marking the roles filled six days out would cost recruiting for no gain.
Change it after people say yes.
