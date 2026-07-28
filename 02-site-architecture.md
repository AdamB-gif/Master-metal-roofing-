# 02 — Site Architecture

## URL rules

- Lowercase, hyphenated, trailing slash, no file extensions, no dates in blog URLs.
- Max depth 3: `/services/metal-roofing/` not `/services/roofing/metal/standing-seam/`.
- Location pages carry the state suffix to disambiguate — critical here because **Bluefield exists in both Virginia and West Virginia**, straddling the state line. `/service-areas/bluefield-va/` and `/service-areas/bluefield-wv/` are different pages targeting different searchers.
- Never change a URL after launch without a 301.

---

## Full sitemap — 45 indexable pages

### Tier 0 — Core (6)

| # | URL | Priority |
|---|---|---|
| 1 | `/` | P1 |
| 2 | `/about/` | P1 |
| 3 | `/gallery/` | P1 |
| 4 | `/contact/` | P1 |
| 5 | `/free-estimate/` | P1 |
| 6 | `/reviews/` | P2 |

### Tier 1 — Services (13)

| # | URL | Priority | Notes |
|---|---|---|---|
| 7 | `/services/` | P1 | Hub |
| 8 | `/services/metal-roofing/` | P1 | Flagship page |
| 9 | `/services/standing-seam-metal-roofing/` | P1 | Confirm offered |
| 10 | `/services/exposed-fastener-metal-roofing/` | P1 | Confirm offered |
| 11 | `/services/board-and-batten-metal-siding/` | P1 | Owner-named service |
| 12 | `/services/metal-roof-replacement/` | P1 | |
| 13 | `/services/metal-roof-repair/` | P2 | |
| 14 | `/services/metal-siding/` | P2 | |
| 15 | `/services/residential-metal-roofing/` | P2 | |
| 16 | `/services/commercial-metal-roofing/` | P2 | Emphasize sub-$150k light commercial |
| 17 | `/services/pole-barns-metal-buildings/` | P2 | Confirm offered |
| 18 | `/services/carports-metal-garages/` | P3 | Confirm offered |
| 19 | `/services/storm-damage-roof-repair/` | P3 | Confirm offered |

### Tier 2 — Service areas (15)

| # | URL | Priority |
|---|---|---|
| 20 | `/service-areas/` | P1 (hub) |
| 21 | `/service-areas/tazewell-county-va/` | P1 (county hub) |
| 22 | `/service-areas/bluefield-va/` | P1 |
| 23 | `/service-areas/richlands-va/` | P1 |
| 24 | `/service-areas/pounding-mill-va/` | P1 |
| 25 | `/service-areas/tazewell-va/` | P1 |
| 26 | `/service-areas/cedar-bluff-va/` | P2 |
| 27 | `/service-areas/north-tazewell-va/` | P2 |
| 28 | `/service-areas/claypool-hill-va/` | P2 |
| 29 | `/service-areas/raven-va/` | P3 |
| 30 | `/service-areas/bluefield-wv/` | P2 |
| 31 | `/service-areas/princeton-wv/` | P2 |
| 32 | `/service-areas/bramwell-wv/` | P3 |
| 33 | `/service-areas/lebanon-va/` | P3 |
| 34 | `/service-areas/grundy-va/` | P3 |

*Add or remove based on `{{SERVICE_RADIUS}}`. Candidates if the radius is wide: Honaker, Cleveland, Vansant, Wytheville, Marion, Abingdon, Bland, Rocky Gap.*

### Tier 3 — Content / blog (11)

| # | URL | Target intent |
|---|---|---|
| 35 | `/blog/` | Hub |
| 36 | `/blog/metal-roof-cost-southwest-virginia/` | Cost research |
| 37 | `/blog/metal-roof-vs-shingles/` | Comparison |
| 38 | `/blog/standing-seam-vs-exposed-fastener/` | Comparison |
| 39 | `/blog/board-and-batten-metal-siding-guide/` | Product education |
| 40 | `/blog/how-long-does-a-metal-roof-last/` | Question |
| 41 | `/blog/metal-roof-colors-guide/` | Selection |
| 42 | `/blog/can-you-put-a-metal-roof-over-shingles/` | Question |
| 43 | `/blog/signs-you-need-a-new-roof/` | Problem-aware |
| 44 | `/blog/metal-roofs-snow-ice-appalachian-winters/` | Regional |
| 45 | `/blog/how-to-choose-a-roofing-contractor-in-tazewell-county/` | Trust / bottom-funnel |

### Utility (not in main nav, mostly noindex)

`/thank-you/` (noindex), `/privacy-policy/`, `/accessibility/`, `/404`, `/sitemap.xml`, `/robots.txt`, `/faq/` (indexable, build in Phase 3).

---

## Navigation

**Header (desktop)**
`[Logo] Services ▾ | Service Areas ▾ | Gallery | About | Blog | Contact` + right-aligned button group: `{{PHONE}}` (tap-to-call) and **Free Estimate** (accent button).

**Services dropdown** — 6 links max, not all 12. Overloaded dropdowns tank mobile usability:
Metal Roofing · Standing Seam · Board & Batten Siding · Roof Replacement · Roof Repair · **View All Services →**

**Service Areas dropdown** — 6 links max:
Bluefield VA · Richlands · Pounding Mill · Tazewell · Cedar Bluff · **All Service Areas →**

**Mobile:** hamburger drawer with accordion sections. Plus a **sticky bottom bar, always visible**, split 50/50: `📞 Call Now` | `Free Estimate`. This bar is the single highest-value conversion element on the site — do not let it be dismissible.

**Footer — 4 columns**
1. Logo, one-line description, `{{PHONE}}`, `{{EMAIL}}`, `{{HOURS}}`, Facebook link, "Licensed & Insured · VA Lic. `{{VA_LICENSE_NUMBER}}`"
2. Services (all 12 links — footers are legitimate for full link lists)
3. Service Areas (all 14 links)
4. Company: About, Gallery, Reviews, Blog, FAQ, Contact, Free Estimate, Privacy

Bottom bar: `© {{CURRENT_YEAR}} Metal Master Roofing and Construction · Serving Tazewell County, Virginia and surrounding areas`

---

## Internal linking rules

This is what makes 45 pages behave like an authority site instead of 45 orphans.

1. **Hub-and-spoke.** `/services/` links to all 12 service pages; every service page links back to the hub. Same for `/service-areas/`.
2. **The service × location cross-link mesh.** Every location page links to the 5 most relevant service pages using natural in-sentence anchors ("we install [standing seam metal roofing] on homes throughout Richlands"). Every service page links to the 4 nearest/largest towns. This mesh is what lets the site rank for "standing seam metal roof Richlands VA" without building a separate page for every service-town combination — which would be 168 doorway pages and a spam penalty.
3. **Blog → money pages.** Every article links to at least 2 service pages and 1 location page, in body copy, with descriptive anchors.
4. **Gallery → both.** Each gallery item is tagged with its service and its town and links to both.
5. **Never use "click here" or bare URLs as anchor text.** Anchors describe the destination.
6. **Every page is reachable from the home page in ≤ 3 clicks.**
7. **No page is orphaned.** Run a crawl before launch and confirm every URL in `sitemap.xml` has ≥ 1 internal inbound link.

## Breadcrumbs

Visible on every page below the header, and marked up with `BreadcrumbList` schema (Google renders these in results, which raises click-through):

`Home › Services › Metal Roofing`
`Home › Service Areas › Tazewell County › Richlands, VA`
`Home › Blog › Metal Roof vs. Shingles`
