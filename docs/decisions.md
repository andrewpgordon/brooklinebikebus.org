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
