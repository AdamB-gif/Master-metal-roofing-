# 15 — Owner Instructions Log

Running log of standing instructions from the site owner, captured verbatim (lightly trimmed)
plus how each is being applied. Append new entries at the top; never delete — if an instruction
is later reversed, note the reversal instead of removing the original line.

---

## 2026-09-05

**Instruction:** "there won't be phone number. no email i guess a fill out form will be the
only thing there."
**Applied as:** The estimate form is now the only inbound contact channel. This **reverses the
core principle in `11-forms-and-lead-capture.md`** ("The phone is the primary channel… never let
[the form] crowd out the phone number") — recorded here rather than edited out of that doc, per
this log's own rule. The concern was put to the owner (most roofing leads call; the doc's position
was deliberate) and the owner confirmed the decision, so it was implemented in full.

Done **structurally in the helpers**, not by find-and-replace, so that if a phone number is ever
added to `data.py` every CTA switches back on by itself:
- `phone_link()`, `phone_text_link()`, `email_text_link()` now return an empty string instead of a
  `[Phone number]` / `[Email address]` placeholder.
- `cta_row()` drops its second button; the header drops the phone link; the mobile drawer's call
  button becomes "Get a Free Estimate".
- The sticky mobile bar is now a single full-width estimate button (its flex children are
  `flex: 1 1 50%`, so a lone child fills the pill — no CSS change needed).
- The footer contact list is built from whatever actually exists, and gained a "Request a free
  estimate" link.
- `business_schema()` already omitted `telephone` when unset — no change needed.

Then the prose, which needed real editing rather than a switch: 15 passages across the home page,
areas hub, four location pages, the 404, the how-it-works steps, and two home FAQ answers were
rewritten from "call us" to "send the form". Kept deliberately: **"we call you back"** on the
thank-you page and in the process steps — the form collects the customer's phone number, so
Metal Master still phones *them*. Outbound calling is unaffected; only inbound is gone. Also
changed the home section heading "Why Neighbors Around Here Call Us First" to "…Come to Us First",
since the idiom now reads as an instruction the visitor can't follow.

Verified across all 19 built pages: zero `[Phone number]`/`[Email address]` placeholders, zero
`tel:`/`mailto:` links, zero "call us", zero empty `<p>`/`<li>` left behind by the removed rows.

**Raised with the owner, unresolved:**
1. **The site currently has no working contact channel at all.** The form still has no
   `FORM_ACCESS_KEY`, so with the phone and email gone it collects nothing. This is now urgent
   rather than a nice-to-have.
2. **A published gallery photo contradicts the decision.** The yard sign in
   `board-and-batten-hunter-green-metal-siding-black-roof-02` is legible and reads
   "Metal Master Roofing LLC · 276-385-5316". If the number is deliberately off the site, that
   photo undoes it. Easy to swap or crop.
3. **Google Business Profile** — see `13-google-business-profile.md` — normally expects a phone
   number, and it is a major local-lead source for a contractor. Worth confirming before launch.
4. Facebook is now the only fallback if the form breaks, and the form's failure message points
   there.

**Instruction:** "how do i put a map up, and connect my email what app should i use?"
(plus the live deploy URL: `metal-master-roofing-…vercel.app`)
**Applied as:** Two things, and one correction to an earlier answer.

**Map.** Owner confirmed Metal Master is a **Service Area Business** — no storefront or office
customers visit. So the map is centred on the service area rather than pinned to a property, and
no street address is published anywhere on the site. Added a `map_embed()` helper in
`templates.py` (Google Maps `output=embed`, no API key, no billing account, `loading="lazy"`),
wired it into the `/service-areas/` hub in place of the old "Map placeholder", and added a new
"Where We Work" section to `/contact/` that says plainly there's no showroom to visit. Centre
point and zoom are `MAP_QUERY` / `MAP_ZOOM` in `data.py`.

**Form delivery.** The owner had answered "Netlify" when asked about hosting, but then sent a
live **Vercel** deploy URL — so Netlify Forms, which `11-forms-and-lead-capture.md` lists first,
is not available. Wired the form for **Web3Forms** instead: a plain HTML POST endpoint that works
on any static host, needs no backend and no account beyond a verified email address. The form was
already fully built (five fields, honeypot, 3-second time trap, inline validation) — only delivery
was missing.

`FORM_ACCESS_KEY` in `data.py` is the switch, handled the same way as `DOMAIN`/`PHONE`/`EMAIL`:
- **Key is `None`** (current state) — form renders exactly as before and says it isn't connected.
- **Key set** — form posts to Web3Forms, adds the `access_key`/`subject`/`from_name` hidden
  fields, shows a sending state, and redirects to `/thank-you/` so the conversion is trackable.
  On failure it keeps everything the customer typed and shows the phone number, per the doc's
  "never silently drop a lead" rule.

Verified both branches render correctly with a throwaway key; no real key is committed.

**Still needed from the owner before the form can go live:** a Web3Forms access key (free, from
web3forms.com — takes an email address and about two minutes) and the destination email address,
which is still the `EMAIL = None` placeholder in `data.py`. SMS notification, which
`11-forms-and-lead-capture.md` argues matters more than email for a contractor on a roof, is not
wired yet — Web3Forms can webhook to Zapier/Make for that once the basics work.

**Instruction:** "also the only standing seam is the big green house. the others are just
legacy textured you can fix that."
**Applied as:** Material factual correction — the photo library had been captioned from
appearance alone, and 18 photos were wrongly described as standing seam. Confirmed with the owner
which house was meant (the large brick ranch with the green roof — the home page hero,
`roof-green-standing-seam`), since "the big green house" could also have read as the hunter green
board & batten cottage from this batch. Only that one photo keeps the standing seam description.

Rewrote 18 alt texts to "textured Legacy" and relabelled the three older before/after pairs
("Worn Shingles to Pewter Legacy", "…to Burgundy Legacy" ×2). Two exceptions: the custom-formed
copper-toned door awnings now say just "custom metal awning" with no profile named — a small
custom-formed awning is plausibly neither profile, and naming one would be guessing again.

Also fixed a real consequence of the error: both the home page and the services hub used
`roof-pewter-detail` — a Legacy roof — as the card image for the **Standing Seam** service page.
Swapped both to `roof-green-standing-seam`, the only genuine standing seam photo in the library.

**Left alone deliberately:** general copy about standing seam as a service (the
`/services/standing-seam-metal-roofing/` page, the standing-seam-vs-exposed-fastener comparison,
and the location pages' profile recommendations). Metal Master does install standing seam — the
green house is the proof — so that copy is accurate. Only claims made *about a specific photo*
were wrong, and only those were changed.

**Instruction:** "add these photo to website and push — This is the black board and batten
Garage we did. Complete vinyl siding job with soffit and facia new gutters. Royal red textured
legacy panel and exposed fastener — John and Isaac did this one. Small Little addition we did
on this Barn. We didn't do the roof on this one, but we built the porch and the roof on the porch."
/ "24x24 carport" / "This is a textured charcoal in the lecacy profile"
**Applied as:** Second owner photo batch — 30 files from `Desktop\New folder`, one exact
duplicate removed (`123.jpeg` == `dddd.jpeg`), leaving **29 new photos**. Ran them through the same
pipeline as the first batch (400/800/1200/1600 ladder for landscape, 400/800/1200 for portrait;
WebP + JPEG at quality 82/80; descriptive lowercase filenames) into `site/static/images/projects/`,
and added them to the `PROJECTS` table in `data.py`. Grouped by the owner's own captions:

- **Black board & batten metal garage** beside a white farmhouse — 5 photos (`bb-black-garage-01..05`)
- **Textured charcoal, Legacy profile** — 6 photos (`roof-charcoal-legacy-01..06`)
- **24×24 carport**, wood posts and metal roof — 3 photos (`carport-24x24-01..03`)
- **Royal red textured Legacy, exposed fastener** (John and Isaac's job) — 2 photos (`roof-royal-red-01..02`)
- **Complete vinyl siding** with new soffit, fascia, and gutters — 1 photo (`vinyl-siding-01`)
- **Small lean-to addition on a metal barn** — 2 photos, finished plus framing (`barn-addition-01`, `barn-addition-framing`)
- **Porch and porch roof built on an existing home** (roof itself was not ours) — 1 photo (`porch-addition-01`)
- **Hunter green board & batten house** — black standing seam roof, timber-frame porch — 5 exterior
  photos plus 3 porch/tongue-and-groove-ceiling detail shots. *The owner did not caption this job;
  captions are descriptive only (material, color, profile) and claim nothing about scope or town.*

Wired the strongest four onto the home page's **Recent Projects** row (black garage, textured
charcoal roof, 24×24 carport, royal red roof), and swapped the hunter green board & batten
house into the home page's "Board & Batten, Done in Metal" split section. Everything else flows
into `/gallery/` automatically through the existing category filters.

**Before/after pairing — asked, then confirmed:** the overhead worn-shingle shot
(`roof-shingle-before-04`) and the overhead finished charcoal roof (`roof-charcoal-legacy-06`)
looked like they *could* be the same house, but the surroundings differ enough between the two
frames that it wasn't certain from the photos alone, so both were published standalone and the
question was put to the owner rather than guessing.

**Owner answer (same day):** "yes they are before and afters." Promoted to the **fourth
before/after pair** (`charcoal`, labelled "Worn Shingles to Textured Charcoal Legacy") and added to
the Before & After section on `/gallery/`. The after photo's alt text now reads "the same home
from above after replacement." Both drop out of the All Projects grid automatically, since
`build_gallery()` excludes photos already shown as a pair.

Town is still not claimed on any photo in either batch — open question #8 in
`14-open-questions.md` still stands.

**Instruction:** "add Abingdon and Wythville, Virginia to location"
**Applied as:** Added `/service-areas/wytheville-va/` and `/service-areas/abingdon-va/` using the
existing `location_page()` template, so they carry the same structure as the four Tazewell County
pages (breadcrumb, quick answer, services-here grid, why-local, nearby links, local FAQ, WebPage +
BreadcrumbList + FAQPage schema). Added both to `AREAS_NAV` (header and mobile nav dropdowns,
footer), to `TOWNS_FOR_FORM` on the estimate form, and to `SERVICE_AREA_SENTENCE`. On the
`/service-areas/` hub they sit under a **new second heading, "Along the I‑81 Corridor"**, kept
separate from the "Tazewell County, Virginia" group because neither town is in Tazewell County
(Wytheville is the Wythe County seat, Abingdon the Washington County seat).

Page copy sticks to publicly verifiable local facts — Wytheville's I‑77/I‑81 crossroads
and ~2,200 ft elevation; Abingdon's historic district, Barter Theatre, and Virginia Creeper Trail
— and deliberately makes **no claim about drive time, response time, or how often we're in
either town**, since none of that is confirmed. Both FAQs answer "do you travel here?" with "yes,
call us and we'll confirm scheduling for your address" rather than inventing a radius. The Abingdon
page notes that exterior changes in a designated historic district can be subject to local review
and tells the homeowner to check with the town — worth confirming with the owner that he's
comfortable with that framing.

---

## 2026-07-28 (continued)

**Instruction:** "Let's continue the work that we started here using Front-end Design. Let's
redesign the website and better color it." / "Use the pictures, put them in the right place,
analyze the pictures, put before and after on the ones that are those."
**Applied as:** Found 27 real project photos (Facebook exports) sitting in the top-level working
folder — these were the launch-blocking photos `09-assets-and-images.md` had been waiting on.
Removed one exact duplicate. Excluded one (`605762052_...jpg`) because a truck's rear license
plate is clearly readable — flagged, not published. Analyzed the remaining 26 by eye (no EXIF/GPS
present — Facebook strips it on upload — so town/description could not be read from the files
themselves) and identified **3 genuine before/after pairs** by matching house, angle, and yard
details:
- White ranch home: worn asphalt shingle → pewter-gray standing seam
- Brick ranch home (white porch columns, rooster/deer yard ornaments): worn shingle → burgundy standing seam
- Brick ranch home (picnic table, propane tank, storage shed): worn shingle → burgundy standing seam

Built an image pipeline (resize to 400–1920px, WebP + JPEG fallback, descriptive lowercase
filenames), added a `PROJECTS` table to `data.py`, and wired real photos into: the home page hero
(with `<link rel=preload fetchpriority=high>`), the home page service cards, the services hub
cards, the About page's related-services cards, and a rebuilt `/gallery/` page with a dedicated
**Before & After** section (side-by-side desktop / stacked mobile, per `08-design-system.md`) plus
a filterable full-photo grid. Screenshotted desktop and mobile, found and fixed a real bug (hero
image was missing a 400w size that the gallery grid also requested, causing several photos to
render blank on mobile — regenerated with a consistent width ladder), and re-verified zero broken
images across home/gallery/services/about at both viewports.

Per-photo town/service/color/notable-detail is **still needed from the owner** before any of these
move onto location pages — see the full id-by-id list and updated status in
`09-assets-and-images.md` and open question #8 in `14-open-questions.md`. Did not touch the brand
navy (it's already built from the owner's real logo per a prior session — see `08-design-system.md`
color rules) since "better color it" is a subjective call now that the photos are doing most of the
visual work; asked the owner directly what specifically feels off, backed by a live localhost
preview, rather than repainting a confirmed brand color speculatively.

**Instruction:** "One of the photos is enlarged. Bring it to size so it's not pixelated." /
"Also look on a mobile phone screen and make sure that everything starts correctly there as well."
**Applied as:** Root cause was the home page hero photo: it's a full-bleed CSS background image
capped at 1920px wide and compressed to quality ~60 to hit the "hero < 200KB" soft budget in
`09-assets-and-images.md` — on any wide or Retina screen the browser has to stretch it past its
real pixel count, and the aggressive compression made that stretch look blocky. Regenerated the
whole photo pipeline at higher quality (82 across the board, up from 58–80) and raised the hero's
resolution ceiling to its true native cap (2048px — that's the actual limit of what Facebook
exported; the original camera photos would be higher-res, see `09-assets-and-images.md`). While
re-verifying, ran a full mobile pass (390px iPhone viewport, 3x DPR) across all 17 built pages and
found a real, separate bug: the `.fact-ph` placeholder style (`[Workmanship warranty length — to
be confirmed]` etc.) forced `white-space: nowrap`, which caused horizontal page overflow on mobile
wherever a long placeholder phrase appeared (e.g. `/services/metal-roofing/`). Fixed by letting
placeholder text wrap normally. Re-ran the full mobile pass afterward: zero broken images, zero
horizontal overflow, zero JS errors across all 17 pages.

**Instruction:** "Set up local host so i can see when your finished."
**Applied as:** Ran the built `site/dist/` output on a local threaded HTTP server so the owner
could preview live in a browser during the session. This is dev-only — not something that ships;
note it here so a future session knows to spin one up again on request rather than assuming one
persists.

**Instruction:** "Everything I tell you, I want you to add to the scale after we're done."
**Applied as:** Every standing instruction/requirement given in conversation gets logged in this
file so it persists across sessions and doesn't get lost or re-asked.

**Instruction:** "Screenshot it and fix all these errors. Do the same thing for desktop view and
mobile view."
**Applied as:** Screenshot the site at a desktop width and a mobile width, list every visual/
functional defect found, fix them, and re-screenshot to confirm. Repeat this pass whenever a
significant round of changes is made, not just once.

**Instruction:** "Revamp it using front-end design. If you don't know what that is, look at
GitHub, find it, download it, make sure it's safe."
**Applied as:** Pull in real front-end design reference/inspiration from reputable, well-vetted
open-source sources on GitHub (checked for license, maintainer legitimacy, and no malicious code
before anything is used) rather than relying solely on a from-scratch guess at "good design."

**Instruction:** "Before you push to GitHub, always check and see if any personal information or
any foothold that somebody could use to get into my network is not exposed."
**Applied as:** **Standing rule, every push, no exceptions:** before `git push`, scan the diff
being pushed for secrets, API keys, tokens, credentials, private keys, internal IPs/hostnames,
personal contact info not meant for publication, `.env` files, and anything else that could give
an attacker a foothold. Report findings before pushing; do not push if anything questionable is
found without flagging it first.
