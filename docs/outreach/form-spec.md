# Sign-up form — spec and current state

**Live:** https://docs.google.com/forms/d/e/1FAIpQLScIpAX4LoNH75AOq0KV_3eDv0BGpOtlQ7wdjFl4ncqaSGJQaA/viewform
**Edit + responses:** see `docs/links.local.md` (gitignored — those URLs expose
sign-up data)

Built with Gemini in Google Forms. Nine fields, deliberately short, because
long forms lose people.

**Updated Oct 21, 2026 for the Nov 18 ride**, and the sections below were wrong
in three places before that. They are corrected inline and marked.

## Current fields

| # | Question | Type | Req |
|---|---|---|---|
| 1 | Your name | short | ✅ |
| 2 | Email | short | — |
| 3 | Mobile | short | — |
| 4 | Kids coming — names and grades, one per line | paragraph | ✅ |
| 5 | Will you be at Griggs Park between 7:15 and 7:30? | multiple choice | ✅ |
| 6 | Could you help on the day? | checkboxes | — |
| 7 | Please confirm *(the release)* | checkbox | ✅ |
| 8 | Type your name to sign | short | ✅ |
| 9 | Anything we should know? | paragraph | — |

Release text sits in the description above Q7. Verified present and intact.
All five required flags verified present.

## Fixes — status as of Sep 10, 2026

**Help text put back** (question → ⋮ → Description), checked on the live form:

- ✅ **Email** — "Optional, but it's how we send the reminder and the 6:15am
  weather call. Please leave at least one of email or mobile."
- ✅ **Mobile** — "Optional. We'll add it to the Bike Bus WhatsApp group unless
  you tell us not to." ← *the only place WhatsApp consent is stated*
- ✅ **Kids coming** — "For example: Maya Gordon — 2nd"
- ✅ **Anything we should know?** "Allergies, a bike that needs looking at, or a
  kid who'd rather hold someone's hand at the crossing. Anything at all."
  (This was marked open here for a month. It has been on the live form the whole
  time. Checked Oct 21.)

✅ **Q5 had a fourth option, `7:38 — Washington Square`.** Removed Oct 21 along
with the two Summit Avenue options, because Griggs Park is the only meeting
place now (D22) and the walking group is gone (D21). Q5 is now a yes / not-sure
question and is arguably not worth keeping at all. It was left in rather than
deleted, because deleting a question on a form with responses is the one step
that isn't cleanly reversible.

**Q6 options as of Oct 21:** Sweep, Corker (with the note that it has to be an
adult riding without a child of their own), Photos, Donuts, "Not this time, but
ask me again". Hill walker and Crossing lead were removed. The old response
columns keep their old headers in the sheet, which is Google's behaviour and not
a mistake.

Families who signed up before Sep 10 never saw the WhatsApp sentence. Before
adding their numbers to the group, ask them first.

## Photos: settled Oct 21, 2026 (D23)

This section used to say the form had never asked about photos. It has been
asking all along, inside the release above Q7, and twenty families agreed to it
when they ticked the box. The wording is now in `docs/release-language.md`,
which is the canonical copy.

**Opt-out is the rule.** Andrew confirmed it on Oct 21. Photos may go in the
WhatsApp group, on brooklinebikebus.org, in the school newsletter and to local
news, never with a child's name. A family opts out by email or at the start of
the ride, and can change their mind later and have anything taken down. The ride
page was rewritten the same day to say the same thing, so the form, the page and
`release-language.md` finally agree.

✅ **The gross-negligence bullet is fixed.** It used to end "...or willful
misconduct.it's completely fine to stay home or walk instead.it's completely
fine to stay home or walk instead." The two stray copies were deleted on Oct 21
and the live form now ends that line at "misconduct."

⬜ Still nothing on the form records a photo preference per family, so an
opt-out lives wherever Andrew writes it down rather than in the responses sheet.
A draft tenth field is kept in `docs/photos.md` if that ever becomes worth
doing.

## Settings to verify

- **Collect email addresses: OFF.** Otherwise people must sign into a Google
  account to sign up, and Q2 already asks.
- **Allow response editing: ON.** So a family can add a second child later
  without filing twice.
- **Responses → Link to Sheets.** That sheet is the email list and the WhatsApp
  invite list.

## Fields deliberately cut

Cut from an earlier fourteen-field version: how the kids are getting there
(you'd find out at 7:15 anyway); which adult is riding with them (the rule lives
in the release, where it binds); cross streets (Q5 already sorts hill vs not);
a date field (Forms timestamps automatically); and a WhatsApp opt-in question
(folded into the mobile help text).

Kept despite redundancy: the typed-name signature. It duplicates Q1, but a
signature sitting directly under the release is doing different work than a name
typed for a mailing list — it's what makes people actually read the box.

## Watch out

Gemini reliably drops **required** flags, **Other** options, and **all help
text**. After any regeneration, check every field.
