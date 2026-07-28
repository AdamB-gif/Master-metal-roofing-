# Metal Master Roofing & Construction — Website Scope of Work

**Client:** Metal Master Roofing and Construction
**Market:** Tazewell County, VA + surrounding SWVA / southern WV
**Goal:** A fast, SEO-first marketing website that ranks in Google's local pack and organic results for metal roofing searches across ~14 towns, and generates phone calls and free-estimate form fills.
**Audience for this document:** an AI coder agent (or human developer) building the site end to end.

---

## READ THIS FIRST

### 1. Placeholders are intentional
Anything wrapped in `{{DOUBLE_BRACES}}` is a fact the developer does **not** have yet. Do **not** invent values. Render them as visible placeholder text in dev, and maintain `14-open-questions.md` as the single list the owner must fill in before launch. Shipping a site with a made-up phone number or a fake license number is worse than shipping with a placeholder.

### 2. Do not fabricate reviews, credentials, awards, or years in business
Every trust claim on this site must trace back to something the owner confirmed. If it isn't in `01-business-facts.md` as CONFIRMED, it does not go on the page.

### 3. Content quality is the SEO strategy
This site has ~45 pages. The failure mode for a large local site is thin, near-duplicate pages — Google filters those out and they can drag down the whole domain. Every location page must contain at least 40% unique, locally specific prose. `04-page-specs/location-pages.md` explains exactly how.

---

## Reading order

| # | File | What it's for |
|---|---|---|
| 00 | `00-project-brief.md` | Objectives, success metrics, constraints, tech decisions |
| 01 | `01-business-facts.md` | Everything known + unknown about the business. Source of truth. |
| 02 | `02-site-architecture.md` | Full sitemap, URL structure, nav, internal linking rules |
| 03 | `03-keyword-map.md` | Every page mapped to its primary + secondary keywords |
| 04 | `04-page-specs/` | Page-by-page build specs (home, services, locations, trust, blog) |
| 05 | `05-seo-technical-spec.md` | Titles, metas, headings, sitemap, robots, Core Web Vitals |
| 06 | `06-schema-markup.md` | Copy-paste JSON-LD for every template |
| 07 | `07-favicon-and-google-icon.md` | Getting the icon to appear next to the site in Google |
| 08 | `08-design-system.md` | Colors, type, components, layout |
| 09 | `09-assets-and-images.md` | Image sourcing from Facebook, naming, alt text, optimization |
| 10 | `10-content-copy-guide.md` | Voice, tone, reusable copy blocks, do-not-say list |
| 11 | `11-forms-and-lead-capture.md` | Estimate form, spam handling, conversion tracking |
| 12 | `12-launch-checklist.md` | Pre-launch QA gate |
| 13 | `13-google-business-profile.md` | Off-site work that drives most of the local ranking |
| 14 | `14-open-questions.md` | The list the owner must answer |

---

## Build phases

**Phase 1 — Foundation (build first, launch-blocking)**
Home, Services hub, 5 core service pages, Service Areas hub, 4 priority location pages (Bluefield VA, Richlands, Pounding Mill, Tazewell), About, Gallery, Contact, Free Estimate. Full technical SEO + schema + favicon. **This is a launchable site.**

**Phase 2 — Coverage expansion**
Remaining service pages, remaining 10 location pages, Reviews page.

**Phase 3 — Authority content**
Blog hub + 10 articles, FAQ page, internal-link pass.

Launch Phase 1 rather than waiting for all three. A live 20-page site beats an unlaunched 45-page site.

---

## Non-negotiables

1. **Phone number is the primary CTA**, visible without scrolling on every page, tap-to-call on mobile, in a sticky mobile bar.
2. **Mobile-first.** Most local roofing searches are on phones, often from a driveway.
3. **Lighthouse ≥ 95** for Performance, Accessibility, Best Practices, SEO on the home page and a representative service and location page.
4. **No page ships without** a unique title tag, meta description, single H1, canonical, and correct schema.
5. **Every image** has descriptive alt text and is served as WebP/AVIF with width/height attributes set.
6. **No stock photos of other people's roofs** presented as the client's work. Real project photos only in the gallery.
