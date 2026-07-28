# Page Spec — Home (`/`)

**Primary keyword:** metal roofing Tazewell County VA
**Word count:** 900–1,300 visible words
**Goal:** in under 5 seconds, a visitor knows what this company does, where it works, that estimates are free, and how to call.

---

## Meta

```
Title:  Metal Roofing Tazewell County VA | Metal Master Roofing & Construction
Meta:   Metal roofing, siding, and board & batten for homes and small commercial
        buildings across Bluefield, Richlands, Pounding Mill & Tazewell County, VA.
        Family owned, licensed & insured. Free estimates — call {{PHONE}}.
```
Title ≤ 60 chars where possible; meta 150–160.

---

## Section 1 — Hero

**Background:** the single best full-width project photo the owner has. A finished metal roof, shot in daylight, ideally with a mountain or treeline behind it so it reads as *here* and not as a stock image from Texas. Dark gradient overlay (see `08-design-system.md`) so white text stays readable.

**H1:** `Metal Roofing in Tazewell County, Virginia`

**Subhead:**
> Metal roofs, metal siding, and board & batten for homes and small commercial buildings across Bluefield, Richlands, Pounding Mill, and the surrounding area. Family owned. Licensed and insured. Free estimates, always.

**CTAs, side by side:**
- Primary: `Get a Free Estimate` → `/free-estimate/`
- Secondary: `Call {{PHONE}}` → `tel:` link

**Trust strip immediately under the CTAs** — four short items with icons:
`Licensed & Insured` · `Family Owned & Local` · `Free Estimates` · `Residential & Commercial`

> **Performance:** the hero image is the LCP element. Preload it, serve AVIF with WebP fallback, set explicit width/height, and never lazy-load it. This one decision drives most of the Core Web Vitals score.

---

## Section 2 — Services grid

**H2:** `What We Build`

Six cards, each with a real photo, a heading, two sentences, and a "Learn more →" link:

1. **Metal Roofing** → `/services/metal-roofing/` — the roof that outlives the mortgage.
2. **Standing Seam** → `/services/standing-seam-metal-roofing/` — concealed fasteners, no exposed screws.
3. **Board & Batten Siding** → `/services/board-and-batten-metal-siding/` — the farmhouse look, in steel.
4. **Roof Replacement** → `/services/metal-roof-replacement/` — from worn shingles to metal.
5. **Roof Repair** → `/services/metal-roof-repair/` — leaks, screws, flashing, valleys.
6. **Commercial** → `/services/commercial-metal-roofing/` — shops, churches, storefronts.

Below the grid: `View All Services →` linking to `/services/`.

---

## Section 3 — Why Metal Master

**H2:** `Why Neighbors Around Here Call Us First`

Three columns. Write each as 60–90 words of real prose, not bullet fragments:

**Local, and it shows.** We live and work in Tazewell County. We know what a Burke's Garden winter does to a roof, how the wind comes across the ridges, and which color holds up on a house that gets full afternoon sun. When you call, you're talking to somebody who's driven your road.

**Licensed and insured — with a number.** Virginia contractor license `{{VA_LICENSE_NUMBER}}`, and we'll hand you a certificate of insurance before we set a ladder against your house. Ask any contractor for both. If they hesitate, keep calling.

**Free estimates, no pressure.** We come out, get on the roof, measure it right, and give you a written number. If you want to think about it for a month, think about it for a month. The estimate doesn't expire because we said so.

*(Rewrite in the owner's voice once confirmed — see `10-content-copy-guide.md`. Remove the license sentence until the number is confirmed.)*

---

## Section 4 — Service area

**H2:** `Where We Work`

Short paragraph naming the geography, then a two-column link list of all 14 location pages, then a link to `/service-areas/`.

> We're based in the Bluefield–Richlands–Pounding Mill area and work throughout Tazewell County and into Mercer County, West Virginia. If you're within about `{{SERVICE_RADIUS}}`, we'll come look at it.

*Optional:* a simple static map image with the service area shaded. Static image only — an embedded Google Map iframe costs 500KB+ and several hundred milliseconds of blocking, for no SEO benefit whatsoever. This is a common and expensive mistake on contractor sites.

---

## Section 5 — Recent work

**H2:** `Recent Projects`

6–8 photos in a responsive grid, each captioned with the service and the town: *"Standing seam roof — Richlands, VA."* Location-specific captions are quiet, legitimate local relevance signals and they're what a skeptical homeowner actually scrolls for.

`See the Full Gallery →` → `/gallery/`

---

## Section 6 — Board & batten feature

**H2:** `Board & Batten, Done in Metal`

Split layout, photo one side, copy the other. 120–160 words explaining that board and batten gives you the vertical farmhouse-and-barn look that's been on buildings around here for two hundred years — but formed in steel, so it doesn't rot, doesn't need repainting every few years, and doesn't feed carpenter bees. Pairs naturally with a metal roof.

CTA: `About Board & Batten Siding →`

This section exists because board and batten is an owner-named specialty with genuinely low local competition. Give it home-page real estate.

---

## Section 7 — Reviews

**H2:** `What Customers Say`

3 review cards. **Pull only from real Google or Facebook reviews.** If there are fewer than 3 real reviews, cut this section entirely and replace it with an additional project photo band. Do not write placeholder testimonials — invented reviews are both a Google policy violation and an FTC issue.

`Read More Reviews →` → `/reviews/`

---

## Section 8 — Process

**H2:** `How It Works`

Four numbered steps: **1. Call or send the form** → **2. We come measure** → **3. Written estimate** → **4. We build it**. One sentence each. This section quietly answers "what am I signing up for by calling?" — the actual thing stopping people from calling.

---

## Section 9 — FAQ

**H2:** `Common Questions`

6 accordion items. Marked up with `FAQPage` schema (see `06-schema-markup.md`).

1. How much does a metal roof cost around here?
2. Can you put a metal roof over my existing shingles?
3. How long does a metal roof last?
4. Are metal roofs loud in the rain?
5. Do you do commercial work?
6. How far do you travel?

**Answers must be honest and specific.** On cost, give a real range with real caveats rather than "every job is different" — that non-answer is why homeowners bounce. On noise, tell the truth: over solid decking with underlayment, a metal roof is not meaningfully louder than shingles; the tin-roof-in-a-thunderstorm sound people imagine comes from panels over open purlins with no deck.

---

## Section 10 — Final CTA

Full-width accent band.

**H2:** `Free Estimates in Tazewell County and Beyond`
Buttons: `Call {{PHONE}}` and `Request Your Free Estimate`.

---

## Technical

- One `<h1>`. Everything else `<h2>`/`<h3>` in order — no skipped levels.
- `LocalBusiness` (SAB variant) + `FAQPage` + `WebSite` schema. See `06-schema-markup.md`.
- Self-referencing canonical.
- Phone as `tel:` everywhere, formatted `(276) XXX-XXXX` for humans.
- Sticky mobile CTA bar present.
- Target LCP < 1.5s, CLS < 0.05, INP < 200ms.
