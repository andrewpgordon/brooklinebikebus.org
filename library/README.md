# Ride library

The flyer, poster and newsletter text we made for each ride, saved so the
next ride can reuse them. None of this is on the website. Only `public/` is
published.

```
library/
  flyer.html            Letter flyer with a small route map and 8 tear-off tabs
  make-flyer-map.py     makes assets/flyer-map.svg from the map on the website
  poster-kit.html       page 1 is how to build the poster; pages 2 to 8 are the pieces
  handlebar-tag.html    3 tags per sheet to fold around a handlebar at the bike racks
  tab-refill.html       24 more tear-off tabs, for when a flyer's tabs are gone
  bulletin-blurb.md     school bulletin / newsletter text, full and short
  social-posts.md       Facebook, neighborhood group and WhatsApp versions
  listserv-email.md     email for a community list of school families and neighbors
  assets/
    qr-brooklinebikebus.png       QR code for brooklinebikebus.org
    flyer-map.svg                 the flyer's map (don't edit by hand, re-make it)
    driscoll-badge-print.png      dragon badge, full size, no background
    facebook-badge-1080.jpg       the badge as a square photo for Facebook posts
  make-pdfs.sh          turns the three .html files into PDFs for one ride
  rides/
    2026-10-07/         exactly what we printed for the first ride
      flyer.pdf
      poster-kit.pdf
      handlebar-tag.pdf
      tab-refill.pdf
      poster-mockup.png     picture of the finished poster
      bulletin-blurb.md     the blurb as sent
      social-posts.md       the posts as sent
      listserv-email.md     the listserv email as sent
```

## Printing

Open the PDF in `rides/<date>/` and print at **actual size** (not "fit to
page"), on Letter paper.

- **Flyer:** one page. Before you put one up, cut up along the dashed lines
  between the tabs so people can tear one off. Each tab has its own QR code.
- **Poster kit:** page 1 shows where everything goes on a 22 x 28 inch poster
  board held sideways. Print pages 2 to 8, cut on the dashed lines, glue.
- **Tab refill:** when a flyer's tabs have all been taken, leave the flyer up
  and staple a refill strip under it. Three strips per sheet, 8 tabs each.
  Cut the strips apart, cut up between the tabs, then staple the red band
  through the bottom of the old flyer. The band repeats the date, the meeting
  place and the web address, so it still works for anyone who reads it and
  doesn't take a tab.
- **Handlebar tags:** 3 per sheet, cut the long way into 2.6 x 10.4 inch
  strips. Fold one in half around a handlebar with the printing facing out,
  then staple the two halves together just under the bar. It hangs as a
  two-sided tag. The bottom half prints upside down so both sides read the
  right way up once it's folded.
- Color looks best. Black and white is fine for both.

**Paper.** Print the flyers on bright white 28 or 32 lb paper (105 to 120
gsm). Card stock is too stiff for the tabs to tear. Before putting a flyer up,
cut the dashed lines between the tabs and fold each tab back and forth along
the top dashed line so it tears off cleanly. Outside, put clear packing tape
over the top two-thirds and leave the tabs uncovered, or use a sheet protector
with the bottom trimmed off.

The tab QR codes are small, so use matte paper (glossy causes glare), print on
the best quality setting, and scan a torn-off tab from the first sheet before
printing the rest.

Handlebar tags go on the same 28 or 32 lb paper. Card stock won't fold tightly
around a bar. They sit outside all day, so put them on the morning of the ride
week rather than days ahead, and skip it if rain is coming. Don't cover any
brake or shifter cables, and use a stapler rather than tape or zip ties so
people can pull the tag off in one go.

Print the poster pieces on 65 lb cover card stock (about 176 gsm). It holds up
to glue better, and most home printers can feed it. Heavier card usually needs
a copy shop.

## Getting ready for the next ride

1. **Decide the new date, rain date and times.** Check the route and times
   against the ride page on the site.
2. **Edit the text.** In `flyer.html` and `poster-kit.html`, every part that
   changes between rides is marked with a `RIDE DETAILS` comment: the date,
   rain date, times, places, contacts, and the tabs at the bottom of the
   flyer (the tab text is repeated 8 times, so change all 8).
   `handlebar-tag.html` repeats its text 6 times, once per face. In
   `bulletin-blurb.md` and `facebook-post.md`, change the date, times and
   contacts.
3. **Make the PDFs** into a new folder:
   ```bash
   ./library/make-pdfs.sh 2026-11-04
   ```
   This needs WeasyPrint (`brew install weasyprint`). Or just ask Claude to
   do it.
4. **Look at every page before printing.** Longer text can push something
   onto a second page or into the tear-off tabs.
5. **Scan the QR code with your phone** from the printed page.
6. Copy the blurb you actually send into the new `rides/<date>/` folder.

A different school? Change the school name, the badge, the colors (search
for `#BB262A` and `#FFB101`) and the route, and make a new QR code if the
site address for that school is different.

## About the QR code

It encodes `HTTPS://BROOKLINEBIKEBUS.ORG`, in capitals on purpose. Capitals
let the QR code use fewer, bigger squares, so it scans more easily, even the
small ones on the tabs. Web addresses don't care about capitals in the domain.
It works because the homepage currently sends people straight to the Driscoll
page (decision D13).

**If the homepage stops redirecting to the ride page, these QR codes will land
on the homepage instead.** Make a new one that points at the ride page. To
make one (Claude can do this): Python package `segno`,
`segno.make("HTTPS://BROOKLINEBIKEBUS.ORG").save("qr.png", scale=40, border=4)`.
A path like `/driscoll/` must stay lowercase, which makes the code denser.

Checked for the first ride: every QR code on the flyer (including all 8 tabs)
and the poster decoded correctly from a 300 dpi render.

## Rules that apply to everything in here

- Say it's **organized by parents and not a school program**. Never use the
  school's logo. The dragon badge is our own (D14).
- **Every child rides with their own parent or guardian**, and **helmets are
  required**. Someone skimming a flyer could easily think it's a drop-off
  service, so both have to be on it.
- **Write like a parent, not like AI.** See the Tone section of `CLAUDE.md`
  for the specific things to avoid.
- **Check the route against the site** before reusing old text. The walking
  group crosses Beacon at **Marion Street**, not Summit Ave (D15). If the map
  on the website changes, run `python3 library/make-flyer-map.py` and re-make
  the flyer PDF.
- These files use a small tool (WeasyPrint) to make PDFs. That's fine for
  print. The website itself still has no build step (D9).
