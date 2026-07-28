# 09 — Assets & Images

## ⚠️ Facebook photos: what actually has to happen

The Facebook page — `https://www.facebook.com/people/Metal-Master-Roofing-and-Construction/61562911080390/` — is login-gated and JavaScript-rendered. It **could not be read programmatically**, and automated scraping of Facebook violates their terms of service. Don't try to route around it.

**The owner must export the photos manually.** This is a 20-minute task and it is a launch blocker.

### Owner instructions (send this to the client verbatim)

> **On a computer (much easier than the phone):**
> 1. Log in to Facebook and go to your Metal Master Roofing page.
> 2. Click **Photos** in the left menu, then **Albums** or **All Photos**.
> 3. Click a photo to open it, click the **⋯** menu in the corner, choose **Download**.
> 4. Repeat for every project photo worth showing. Save them all to one folder named `metal-master-photos`.
>
> **Faster option — Facebook's bulk export:**
> 1. Facebook **Settings & Privacy → Settings → Your Facebook Information → Download Your Information** (from the *page* if it's a business page, or via Meta Business Suite).
> 2. Select **Posts** and **Photos and Videos**, choose **High** quality, request the download.
> 3. Facebook emails a ZIP link, usually within a few hours.
>
> **Even better:** the original photos on your phone are higher resolution than anything Facebook stores. Facebook compresses uploads heavily. If you still have the originals in your camera roll, send those instead — go to your Photos app, select the roofing job photos, and share them to a Google Drive or Dropbox folder.
>
> **For each photo, tell us three things:**
> - What town it's in (Richlands, Bluefield, Pounding Mill, etc.)
> - What kind of work it is (standing seam, ag panel, board & batten, siding, repair, pole barn)
> - Anything notable ("this one was over old shingles," "12/12 pitch," "matched the brick")
>
> That last part is what makes the website rank. A photo labeled "roof" is worth very little. A photo labeled "charcoal standing seam roof on a farmhouse in Richlands" is worth a lot.

### Photo priorities

**Must have (launch blockers):**
- 1 outstanding hero photo — a finished roof in daylight, ideally with mountains or treeline visible so it reads as *here*
- 12+ finished project photos across different services
- 2+ board & batten siding photos (owner-named specialty, and the one thing competitors won't have)
- 1 photo of the owner or crew working — real, not posed

**Strongly wanted:**
- Before/after pairs — highest-engagement content in any contractor gallery
- Photos tagged by town, ideally 2+ per priority town (Bluefield, Richlands, Pounding Mill, Tazewell)
- Different colors and panel profiles
- One commercial project
- Detail shots: seams, ridge cap, trim, valley work — these signal craftsmanship to people who know what they're looking at

**If photo count is thin (<12):** launch with a smaller gallery rather than padding with stock. Give the owner a standing instruction to photograph every job from now on — three shots minimum: wide before, wide after, one detail. Same angle for before/after.

---

## Logo

`{{LOGO}}` — need the highest-resolution version the owner has: original vector (AI/EPS/SVG), or the file the sign shop or truck-lettering shop used. A screenshot of the Facebook profile picture is not sufficient for print-quality or favicon use.

**If no usable logo exists**, design one. Requirements: works in one color, legible at 16px (for the favicon), reads on a truck door at 40 feet, no thin strokes, no gradients. Deliver SVG master plus PNG exports at 512/256/128/96/48px, on transparent and on white.

---

## File naming

Descriptive, keyword-bearing, hyphenated, lowercase. Filenames are a real (small) ranking factor in image search, and image search sends genuine local traffic for "metal roof colors" type queries.

```
✅ standing-seam-metal-roof-richlands-va-01.jpg
✅ board-and-batten-metal-siding-pounding-mill-va.jpg
✅ metal-roof-before-after-bluefield-va-01.jpg
❌ IMG_4821.jpg
❌ photo1.jpg
❌ metal-roof-metal-roofing-metal-roofer-va-roofing.jpg   (stuffed — counterproductive)
```

## Directory structure

```
/public/images/
  ├── hero/            Full-width hero images, 2400px wide
  ├── projects/        Gallery, 1600px wide
  ├── services/        Service page headers, 1600px
  ├── locations/       Location page headers, 1600px
  ├── blog/            Article images, 1200px
  ├── team/            Owner and crew
  ├── og/              1200×630 social cards
  └── logo/            Logo variants
```

---

## Alt text

Every meaningful image gets alt text that describes what's actually in the picture. Written for a person who can't see it — which is also, conveniently, exactly what search engines want.

```
✅ "Charcoal standing seam metal roof on a two-story farmhouse in Richlands, Virginia"
✅ "Close-up of a concealed-fastener standing seam panel joint with ridge cap"
✅ "Before and after: worn asphalt shingles replaced with dark bronze metal roofing in Bluefield, VA"
❌ "roof"
❌ "metal roofing Bluefield VA metal roofers near me best roofing contractor"
❌ "" on a meaningful photo
```

Decorative images (background textures, dividers) get `alt=""` so screen readers skip them.

---

## Optimization pipeline

Automate at build. No manual step should be required to add a photo.

1. Resize to the max needed dimension (never ship a 4000px photo into an 800px slot)
2. Generate `srcset` variants: 400 / 800 / 1200 / 1600px
3. Encode AVIF (primary), WebP (fallback), JPEG (last resort) via `<picture>`
4. Quality ~80 for photos
5. Strip EXIF from published files — **but capture GPS data first** for town tagging before stripping. Publishing home GPS coordinates of customers' houses is a privacy problem.
6. Explicit `width`/`height` on every `<img>` (kills CLS)
7. `loading="lazy"` below the fold; `fetchpriority="high"` + preload on the hero

**Targets:** hero < 200KB, gallery thumbs < 60KB, full gallery images < 250KB.

---

## Permissions and privacy

- **Only publish photos of the company's own completed work.** Never use a manufacturer's or another contractor's photos, even ones found on a supplier site.
- Get the homeowner's OK before publishing an identifiable house — as a practical matter, avoid house numbers, visible mailboxes with names, and license plates. Crop or blur.
- No people's faces without permission. Crew photos are fine with the crew's consent.
- Don't publish precise addresses of customer homes.

---

## OG images (social cards)

1200×630 per major page. Template: project photo, dark gradient overlay, page title in the display font, logo bottom-left. Auto-generate at build. The owner's existing audience is on Facebook — when a link gets shared there, this image is the entire first impression.

---

## Ongoing photo workflow (give the owner this habit)

Three photos per job, every job:
1. **Wide before** — from the street or driveway
2. **Wide after** — same spot, same angle
3. **One detail** — a seam, a valley, the ridge, the trim

Then text them, with the town name. That's the whole process. Ten minutes a month keeps the gallery growing, keeps the Google Business Profile fed with fresh photos (photo recency is a live local ranking factor), and steadily builds the local-specificity library the location pages depend on.
