# 00 — Project Brief

## The business in one paragraph

Metal Master Roofing and Construction is a metal roofing and construction contractor based in the Bluefield / Richlands / Pounding Mill area of Tazewell County, Virginia. The company does primarily residential work plus selected light commercial, with project values capped below $150,000. Core offerings are metal roofing, metal siding, and board-and-batten. The business is family owned and locally operated, licensed and insured, and offers free estimates.

## Objectives, in priority order

1. **Rank in the Google local 3-pack** for "metal roofing near me," "metal roof [town]," and "roofing contractor [town]" across the service area.
2. **Rank organically** for long-tail metal roofing questions that a homeowner in southwest Virginia would type before calling anyone.
3. **Convert.** Phone calls first, free-estimate form second. Everything on the site funnels to one of those two.
4. **Look legitimate.** A homeowner comparing three contractors should conclude this one is the real business. The site is the credibility document.
5. **Show the brand icon in Google results** (see `07-favicon-and-google-icon.md`).

## Success metrics (measure at 90 and 180 days post-launch)

| Metric | 90-day target | 180-day target |
|---|---|---|
| Google Business Profile calls/month | Baseline +50% | Baseline +150% |
| Organic sessions/month | 150 | 500 |
| Local pack appearances for "metal roofing" in 4 priority towns | 2 of 4 | 4 of 4 |
| Indexed pages | 100% of submitted | 100% |
| Form submissions/month | 5 | 15 |
| Core Web Vitals | All "Good" | All "Good" |

## Constraints and decisions

**Tech stack: developer's choice**, subject to these hard requirements:
- Static or statically-rendered HTML delivered to the browser. No client-side-only rendering of primary content — the crawler must see full content in the initial HTML response.
- Sub-1.5s Largest Contentful Paint on 4G mobile.
- Content stored as flat files (Markdown/MDX/JSON) so pages are cheap to add and the owner can hand it to any future developer.
- Zero or near-zero monthly hosting cost. Static host with a global CDN and free TLS.
- No database, no CMS admin panel, no login system. This is a brochure site.

**Recommended if the agent has no preference:** Astro + Tailwind, deployed to Cloudflare Pages or Netlify. Astro ships zero JS by default, has first-class content collections for a 45-page content site, and produces the fastest realistic Lighthouse scores for this shape of project. Next.js is acceptable but heavier than the job requires. Hand-written HTML is discouraged at 45 pages — the templating is the point.

**Forms:** no backend. Use the host's native form handling (Netlify Forms / Cloudflare Pages Functions) or a third-party endpoint. See `11-forms-and-lead-capture.md`.

**Domain:** `{{DOMAIN}}` — see open questions. Preference order if unregistered: `metalmasterroofingva.com`, `metalmasterroofingandconstruction.com`, `metalmasterroofingva.net`. Avoid hyphens and avoid keyword-stuffed exact-match domains like `bluefield-metal-roofing.com` — they read as spam to both users and Google.

## Out of scope

Online booking or scheduling, customer portal, e-commerce, financing application, live chat widget, blog comments, multi-language. If the owner wants any of these later, they are Phase 4 conversations.

## Explicit anti-goals

- **No AI-generated stock photography of roofs.** Real work only. Google's helpful-content systems and, more importantly, local homeowners can both tell.
- **No doorway pages.** Location pages that differ only by a find-and-replace on the town name violate Google's spam policies and risk manual action. See `04-page-specs/location-pages.md` for the required uniqueness bar.
- **No fake urgency, countdown timers, or invented limited-time offers.**
- **No claims of certifications, manufacturer partnerships, BBB accreditation, or awards** unless the owner confirms them in writing.
