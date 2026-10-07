# Photos

Written the afternoon of Oct 7, 2026, after the first ride, because two things
came up at once. Some families wanted a shared album. Others didn't want
pictures of their children somewhere strangers could see them. Both are
reasonable, and the album is not the thing that settles it.

## The rule

A gate on an album answers who can look at it. It doesn't answer who is in the
frame, and that second one is what a worried parent is asking about. A locked
album still contains somebody's kid, put there by another parent who meant
well. So the promise is about the photo, not about the album.

1. Any family can say they'd rather their child wasn't photographed. Write it
   down and tell whoever is taking pictures that morning, before anyone starts.
2. Any family can have any picture of their child taken out of the album. No
   reason needed and no discussion.
3. Nothing leaves the album for the website, Facebook, a newsletter or a flyer
   until the families in it have been asked. Asked individually, before it goes
   up.

Point 3 costs something real. `library/crew-brief.md` says photos are how the
second ride gets more families than the first, and that's true, and it still
doesn't outrank a parent who said no.

## The album

One album per ride, in Google Photos, with three settings.

- **Link sharing off.** With it on, the link is the album. Forward it once into
  a bigger group chat and it's gone, and taking a person off the album doesn't
  claw it back: Google's own help page says anyone holding the original link
  still gets in. Off is the setting that matches what the families who objected
  were worried about.
- **Shared with named people**, added by email address. They need a Google
  account on their end. That's the cost of doing it this way, and it's worth it.
- **Collaborate on**, so the families in the album can add their own pictures.

We can't find anything in Google Photos like Drive's "request access" button,
so a parent has no way to ask the album to let them in. They ask Andrew and he adds them, which is
what the ride page tells them to do.

### Two URLs, and only one of them can go anywhere public

The album has an address with no access key on the end, which is what you see in
your own address bar when you're looking at it. Loaded in a signed-out browser on
Oct 7, that one returns a plain Google 404. A stranger holding it gets nothing.
So it's the one Andrew decided to put on the ride page, with a sentence beside it
saying you'll get a Google error unless he has already added you and you're
signed in. A bare 404 with no explanation next to it reads as a broken website.

The URL that "Copy link" hands you in the Share menu is a different thing. It
carries a `?key=` on the end, creating it is what switches link sharing on, and
it works for anyone holding it. That one goes on no page and in no file. If the
link on the ride page ever looks broken, the fix is not to paste that one in.

Still untested: whether an already-added family opening the keyless URL while
signed in actually lands in the album. It should, since it's the same address
they see under Sharing, but one parent tapping it would settle it.

Both the keyless address and the reason it's safe are written down in
`links.local.md`.

To wind it down later, take everyone off and leave link sharing off. That's how
Google makes a shared album private again.

## A Google Group as the list, and whether it can be the gate

Andrew's idea on Oct 7: run a group address like
`driscoll-bike-bus@googlegroups.com`, so that the people who get ride emails and
the people who can see the album are the same list, and nobody has to be added
twice.

As a mailing list that works, and it's better than what we have now. A group
takes any email address, so families without a Google account can be on it. It
gives us one address to send to instead of a growing BCC line pasted out of the
responses sheet, and people can be taken off without Andrew hunting through old
emails.

As the album gate it doesn't work. Andrew tried it on Oct 7 and Google Photos
won't take a group address, which is what the research said would happen: Photos
adds people by Google account, and a group address is a distribution list, not an
account.

So the album gets shared the other way round. Andrew turns on the share link,
which is the URL with the `?key=` on the end, and posts that link in the Google
Group and in the WhatsApp group. Both of those are closed rooms, so the link
reaches exactly the families it should without anybody being added one at a time.
The ride page keeps the keyless URL, which hands a stranger a Google error.

What that costs, and it's worth saying out loud: a share link works for anyone
holding it, and any one of the families can forward it out of WhatsApp to
someone who isn't on the list. Taking that person off the album doesn't take the
link back. So the text card at the top of the album, the one asking people not to
forward it, is now the only thing standing between a closed album and an open
one. It being an ask rather than a control matters more under this setup than it
did under the old one.

One thing to re-test whenever the share link goes on: whether the keyless URL
sitting on the public page starts working for signed-out strangers once link
sharing is switched on. It returned a plain Google 404 while sharing was off. If
turning sharing on wakes it up, the link comes off the ride page.

Google Drive does do it, and Google documents it: share a folder with a group and
people get access as they join and lose it as they leave. So if "membership is
access" is the thing Andrew wants most, the album belongs in a Drive folder
rather than in Photos. What that costs us: in a personal Drive, letting families
add pictures means giving them Editor, and an Editor can delete anybody's files.
A collaborator on a Photos album can only pull out what they put in themselves.
With fifteen families and somebody else's kids in the frame, that matters.

Where this leaves us, pending Andrew's call:

1. Make the group, and use it for ride emails either way.
2. Keep the album in Photos, and add people by hand off the group's member list.
   Fifteen families, once a month.
3. If the hand-adding gets old, move the album to a Drive folder shared with the
   group and accept the Editor problem.

### Group settings that matter

The address is public namespace, so anyone can guess `driscoll-bike-bus` and
turn up at the door. The defaults are too open for a list of Driscoll parents'
email addresses, so set these when you make it:

- Who can join: invited users only. "Anyone can ask to join" turns the group
  into a second request channel and a spam target.
- Who can view conversations: members only.
- Who can view members: managers only. Otherwise any one parent can export every
  family's email address.
- Who can post: worth deciding. Members-can-post makes it a parent conversation,
  owners-only makes it announcements. The WhatsApp group is already the
  conversation, so owners-only is probably right.
- Don't list it in the Groups directory.

Members come out of the form responses sheet, whose URL lives in
`links.local.md` and stays there.

## What goes in the album itself

Google Photos lets you drop a block of text into an album the same way you add a
picture. Put this one at the top, so it's the first thing anybody sees, and send
the short version in the invite email, because people read the email first and
some of them never scroll.

> **Please keep these in the album.**
>
> Everyone in here is somebody's kid. Some families said yes to pictures only
> because this album is small and we know who's in it. So please don't forward
> the link or repost these anywhere, and that includes the bike bus WhatsApp
> group.
>
> Save as many of your own child's pictures as you want. If you want to use one
> somewhere else and another family's child is in it, ask me first and I'll
> check with their parents.
>
> If a picture of your child is in here and you'd rather it wasn't, tell me and
> it comes out. You don't need to give a reason.
>
> Andrew Gordon, andrewpgordon@gmail.com, 781.879.3883

Short version for the invite email:

> The album is just the families who rode. Please don't forward the link or
> repost the pictures, since other people's kids are in them. If one of yours
> shouldn't be in there, tell me and I'll take it out.

None of this stops anyone. A person who can see the album can save what's in it,
and asking is the only lever we have. It works more often than people expect,
and it means nobody can say later that they didn't know.

## What the sign-up form should ask

The form has never asked about photos. `library/bulletin-blurb.md` flagged it in
September ("don't mention photos until the photo wording on the sign-up form is
settled") and it never got settled, so nobody who rode on October 7 was asked in
writing. Draft for a tenth field:

> **Photos** · required, choose one
>
> A few parents take pictures on the morning. The album is shared only with
> families who ride, and nothing goes anywhere public without asking you first.
> You can change your answer any time by emailing andrewpgordon@gmail.com.
>
> - Yes, and the album for riding families is fine.
> - Yes, and you can use them on the website, a flyer or Facebook too.
> - Please don't take pictures of my child.

Required, so that nobody ends up in the unknown column. Everyone who signed up
before the field exists has to be asked some other way. For the October 7 group
that means asking now, before any of this morning's pictures get posted
anywhere.

## Why there are no names in this file

`docs/` is readable on the public repo. The families who asked not to be
photographed are the last people whose names should sit in here. They go in
`docs/rides/2026-10-07-morning.local.md` with the rest of the crew names.
