# 01 — Business Facts (Source of Truth)

Every factual claim on the website must trace to this file. Three states:

- **CONFIRMED** — stated by the owner. Safe to publish.
- **INFERRED** — reasonable deduction, flagged. Must be confirmed before publishing.
- **`{{PLACEHOLDER}}`** — unknown. Must be filled before launch.

---

## Identity

| Field | Value | Status |
|---|---|---|
| Legal/trade name | Metal Master Roofing and Construction | CONFIRMED |
| Short brand name (nav, logo, title tags) | Metal Master Roofing | CONFIRMED |
| Facebook | https://www.facebook.com/people/Metal-Master-Roofing-and-Construction/61562911080390/ | CONFIRMED |
| Domain | `{{DOMAIN}}` | placeholder |
| Phone | `{{PHONE}}` | placeholder |
| Email | `{{EMAIL}}` | placeholder |
| Mailing / physical address | `{{ADDRESS}}` — owner elected to supply later | placeholder |
| Business hours | `{{HOURS}}` | placeholder |
| Year established | `{{YEAR_ESTABLISHED}}` | placeholder |
| VA contractor license # | `{{VA_LICENSE_NUMBER}}` | placeholder |
| Insurance carrier / COI available | `{{INSURANCE}}` | placeholder |
| Owner name | `{{OWNER_NAME}}` | placeholder |
| Logo files | `{{LOGO}}` — see `09-assets-and-images.md` | placeholder |

> **Address decision:** the owner is supplying the address later. Until then, build the site as a **service-area business (SAB)**: no address in the footer, no `PostalAddress` in schema, `areaServed` defined by town list instead. This is the correct configuration for a contractor who travels to customers and matches how the Google Business Profile should be set up. See `06-schema-markup.md` for the SAB variant of the JSON-LD, and `13-google-business-profile.md` for why hiding the address on GBP matters.

---

## Services

**CONFIRMED — the owner named these explicitly:**
- Metal roofing
- Board and batten
- Residential work (primary)
- Commercial work (selective, smaller scale)

**INFERRED — standard adjacent offerings for a metal roofing contractor in this market. Confirm each with the owner before building its service page. Delete the page if the answer is no.**
- Standing seam metal roofing (concealed fastener)
- Exposed-fastener / ag-panel / R-panel metal roofing
- Metal roof repair
- Metal roof replacement / re-roof over existing shingles
- Metal siding (board and batten is a siding profile — see terminology note below)
- Pole barns / post-frame buildings
- Carports and metal garages
- Gutters, trim, flashing, and ridge cap
- Storm damage repair
- Shingle roofing (does the owner do asphalt at all, or metal only?)

### Terminology note — important for content accuracy

"Board and batten" in the metal industry most commonly refers to a **vertical siding profile**: wide panel faces separated by raised batten ribs, with concealed fasteners. It is the metal version of the traditional barn/farmhouse wood look, without rot, insect damage, or repainting. It is typically paired with a standing-seam or exposed-fastener metal **roof**.

The owner said "metal, board, and batten," which most likely means: metal roofing **and** board-and-batten metal siding. **Confirm this before writing the service page.** If the owner also installs traditional wood board-and-batten siding, that is a separate page and a separate keyword set. Getting this wrong makes the site read as inexpert to the exact homeowners searching for it.

---

## Project scope and capacity

| Field | Value | Status |
|---|---|---|
| Project ceiling | Under $150,000 | CONFIRMED |
| Residential | Primary business | CONFIRMED |
| Commercial | Yes, smaller-scale | CONFIRMED |
| Likely license class | **Virginia DPOR Class B** | INFERRED |

**On the license class:** Virginia's contractor tiers are Class C ($1,000–$29,999 per contract), Class B ($30,000–$149,999 per contract, $250,000–$999,999 annual gross), and Class A (no cap; required for any project of $150,000 or more). The owner's "nothing over $150,000" maps precisely onto the Class B ceiling, which strongly suggests a Class B license. **Do not publish the class or number until the owner confirms both.** Once confirmed, display it in the footer and in About — a visible license number is one of the highest-trust signals a contractor site can carry, and it's exactly what a cautious homeowner looks for.

**How to write about the ceiling on the site:** frame it as focus, not limitation.
> "We take on residential and light commercial projects up to $150,000 — the size where the owner is still on your roof, not managing it from an office."

Never write "we can't do jobs over $150,000."

---

## Differentiators (owner-selected, CONFIRMED)

1. **Free estimates** — headline this. It is the primary conversion hook and belongs in the hero, in every CTA block, and in the sticky mobile bar.
2. **Local / family owned** — Tazewell County roots. Use specific geography, not the generic phrase "locally owned and operated." Reference the actual towns, the mountains, the weather.
3. **Licensed and insured** — pair with the license number once confirmed. Unnumbered "licensed and insured" is table stakes; a number is proof.

---

## Service area

Primary (Tazewell County, VA): Bluefield, Richlands, Pounding Mill, Tazewell, North Tazewell, Cedar Bluff, Claypool Hill, Raven, Doran, Pocahontas, Bandy, Falls Mills, Jewell Ridge, Tannersville, Burke's Garden, Boissevain.

Tazewell County ZIP codes for reference: 24605 (Bluefield VA), 24609 (Cedar Bluff), 24630 (Doran), 24637 (North Tazewell), 24639 (Raven), 24641 (Richlands), 24651 (Tazewell), 24601, 24602, 24604, 24606, 24608, 24612, 24613 (Pounding Mill), 24619, 24622, 24635, 24640, 24316, 24314, 24377.

Adjacent (confirm the owner will travel there): Bluefield WV, Princeton WV, Bramwell WV, Lebanon VA, Cleveland VA, Honaker VA, Grundy VA, Vansant VA, Marion VA, Wytheville VA, Abingdon VA.

`{{SERVICE_RADIUS}}` — how far will the owner travel? This determines the final location page list. Do not build a page for a town the owner won't drive to; ranking for it produces wasted calls and bad reviews.

---

## Competitive landscape (researched July 2026)

The Bluefield/Tazewell metal roofing SERP is currently dominated by **national lead-generation shells** — programmatically generated city subdomains from directory operators, plus BBB and Yellow Pages category listings. These pages carry no real local content, no real project photos, and no named local owner.

**This is the opening.** A genuine local site with real photos of real Tazewell County roofs, a named owner, a real license number, and town pages written by someone who has actually driven those roads will out-rank thin national templates on relevance and engagement signals. Lean hard into specificity everywhere. That is the entire competitive thesis of this build.

Real local competitors identified include Clinch River Roofing (Tazewell, VA). Do not name or disparage competitors anywhere on the site.

---

## Assets

Facebook photos: the page is login-gated and could not be read programmatically. The owner must manually export project photos. Process in `09-assets-and-images.md`.

`{{PHOTO_COUNT}}` — how many real project photos exist? The gallery and the location pages both depend on this. Minimum viable: 12. Target: 30+.
