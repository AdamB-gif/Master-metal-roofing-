# 15 — Owner Instructions Log

Running log of standing instructions from the site owner, captured verbatim (lightly trimmed)
plus how each is being applied. Append new entries at the top; never delete — if an instruction
is later reversed, note the reversal instead of removing the original line.

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
