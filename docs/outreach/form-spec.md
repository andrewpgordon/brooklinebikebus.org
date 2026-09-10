# Sign-up form — spec and current state

**Live:** https://docs.google.com/forms/d/e/1FAIpQLScIpAX4LoNH75AOq0KV_3eDv0BGpOtlQ7wdjFl4ncqaSGJQaA/viewform
**Edit + responses:** see `docs/links.local.md` (gitignored — those URLs expose
sign-up data)

Built with Gemini in Google Forms. Nine fields — deliberately short, because
long forms lose people.

## Current fields

| # | Question | Type | Req |
|---|---|---|---|
| 1 | Your name | short | ✅ |
| 2 | Email | short | — |
| 3 | Mobile | short | — |
| 4 | Kids coming — names and grades, one per line | paragraph | ✅ |
| 5 | Where will we see you? | multiple choice | ✅ |
| 6 | Could you help? We need four more grown-ups. | checkboxes | — |
| 7 | Please confirm *(the release)* | checkbox | ✅ |
| 8 | Type your name to sign | short | ✅ |
| 9 | Anything we should know? | paragraph | — |

Release text sits in the description above Q7. Verified present and intact.
All five required flags verified present.

## Outstanding fixes

**Add a fourth option to Q5:** `7:38 — Washington Square`. A parent pointed out
you can join the ride there and the form doesn't offer it.

**Add back the help text Gemini dropped** (question → ⋮ → Description):

- **Email** — "Optional, but it's how we send the reminder and the 6:15am
  weather call. Please leave at least one of email or mobile."
- **Mobile** — "Optional. We'll add it to the Bike Bus WhatsApp group unless you
  tell us not to." ← *the only place WhatsApp consent is stated; don't skip it*
- **Kids coming** — "For example: Maya Gordon — 2nd"
- **Anything we should know?** — "Allergies, a bike that needs looking at, a kid
  who'd rather hold someone's hand at the crossing — anything at all."

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
