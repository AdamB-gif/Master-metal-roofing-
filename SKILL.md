---
name: local-business-website
description: Produce a complete, SEO-oriented scope of work for a local service business website — sitemap, keyword map, page-by-page specs, schema markup, favicon/Google icon setup, and a launch checklist — ready to hand to a coder agent. Use when the user wants a website, site plan, or web presence for a contractor, trade, or local service business (roofing, HVAC, plumbing, electrical, landscaping, construction, remodeling, auto, dental, legal, salon, restaurant, or similar), or asks to "build a website for", "make a site for", "scope a website", "plan a website", "get [business] found on Google", or "rank locally". Also use for rebuilding or expanding an existing local business site.
---

# Local Business Website Scope

Produce a scope of work a coder agent can build from without asking follow-up questions. The deliverable is a folder of markdown files, not a built website — unless the user explicitly asks you to build it too.

## Core premise

Local service businesses win on **local specificity and trust signals**, not on volume of content. The competitors ranking for most local trade searches are national lead-generation shells with programmatically generated city pages, no real photos, and no named owner. A genuine local site with real project photography, a named person, a verifiable license, and town pages written by someone who knows the area beats them.

Everything in this skill follows from that.

## Process

### 1. Gather before you write

Never invent business facts. Ask the user for what you don't have, and mark the rest as placeholders.

Run `AskUserQuestion` early to settle: contact details (or confirm placeholders), tech stack preference, site size, and differentiators to emphasize. See `references/discovery-interview.md` for the full question set and the 45-minute owner interview that produces the local specificity everything else depends on.

### 2. Research the actual market

Do not skip this. Search for:
- Competitors in the target towns — who ranks now, and are they real local businesses or lead-gen shells?
- The trade's technical vocabulary (panel profiles, gauges, system types). Getting terminology wrong makes the site read as inexpert to exactly the customers searching for it.
- Licensing tiers and monetary limits in the state, and whether the user's stated project ceiling maps to a license class.
- Geography: towns, ZIP codes, counties, populations, adjacent markets, and any same-name-different-state ambiguity.
- Current local SEO and Google Business Profile guidance — this changes.

### 3. Classify every fact

Three states, applied to every claim that reaches a page:

- **CONFIRMED** — the user said it. Safe to publish.
- **INFERRED** — a reasonable deduction. Flag it; must be confirmed before publishing.
- **`{{PLACEHOLDER}}`** — unknown. Render visibly in dev; track in the open-questions file.

Shipping a placeholder is always better than shipping an invented phone number, license number, review, or founding year.

### 4. Build the folder

Standard structure (adapt file count to project size):

```
README.md                  Reading order, build phases, non-negotiables
00-project-brief.md        Objectives, metrics, constraints, tech decisions, anti-goals
01-business-facts.md       Source of truth. CONFIRMED / INFERRED / placeholder.
02-site-architecture.md    Sitemap, URLs, nav, internal linking rules, breadcrumbs
03-keyword-map.md          Every page → one primary keyword + secondaries
04-page-specs/             home.md, service-pages.md, location-pages.md,
                           trust-pages.md, blog-pages.md
05-seo-technical-spec.md   Meta patterns, robots, sitemap, Core Web Vitals, a11y
06-schema-markup.md        Copy-paste JSON-LD per template
07-favicon-and-google-icon.md
08-design-system.md        Colors, type, components, what to avoid
09-assets-and-images.md    Photo sourcing, naming, alt text, optimization
10-content-copy-guide.md   Voice, reusable blocks, banned phrases
11-forms-and-lead-capture.md
12-launch-checklist.md     With hard blockers marked
13-google-business-profile.md
14-open-questions.md       Grouped by urgency; blockers first
```

### 5. Verify before delivering

- Cross-check that every URL in the sitemap appears in the keyword map and has a page spec
- Validate every JSON-LD block parses
- Confirm page counts are consistent across files
- Grep for placeholder syntax and confirm the inventory matches the open-questions file
- Confirm no fact was published that wasn't CONFIRMED

## The five rules that matter most

**1. One page, one primary keyword.** Two pages targeting the same keyword cannibalize each other and both underperform.

**2. Location pages must be genuinely different.** At least 40% unique prose per page. A page that differs only by the town name is a doorway page — a named Google spam policy violation that risks filtering or manual action. This is the single most common way local sites fail. See `references/location-pages.md`.

**3. Never build service × location combination pages.** Twelve services × fourteen towns is 168 doorway pages. Use the cross-link mesh in `references/site-architecture.md` instead — it captures the same long-tail traffic safely.

**4. No self-serving review markup.** `aggregateRating` schema on reviews the site owner collected and displays about itself violates Google's structured data guidelines. Reviews live on the Google Business Profile.

**5. The Google Business Profile matters more than the website.** GBP signals are roughly a third of local pack ranking; reviews about a fifth; on-page SEO around 15%. Say this plainly in the deliverable. The website converts traffic and establishes credibility — the profile is what gets found. See `references/google-business-profile.md`.

## Content standards

Write the way a good tradesperson talks to a customer in the driveway: direct, concrete, willing to say the unwelcome thing.

- **Publish real price ranges.** Refusing to discuss cost is why homeowners bounce. Get the owner's actual numbers; include a worked example.
- **Say the true thing even when it costs a sale.** "Don't do this if you're selling in two years" builds more trust than a page of superlatives and makes everything else believable.
- **Real photos only.** Never stock photography presented as the business's work.
- **Never fabricate** reviews, credentials, awards, certifications, or years in business.
- Banned: *premier, industry-leading, unparalleled, we pride ourselves on, look no further, nestled in the heart of, top-notch, hassle-free, one-stop shop.*

## Regulated-trade cautions

Flag these in the deliverable where relevant:

- **Insurance claims** — contractors must not promise to handle claims, negotiate with adjusters, or waive deductibles. Deductible waiving is fraud. Safe framing: document the damage, provide a written estimate for the adjuster.
- **Licensing** — verify class and monetary limits per state; don't publish a number until confirmed; check separate licensure for adjacent states before building pages targeting them.
- **Medical, legal, financial trades** — additional advertising restrictions apply. Research before writing claims.

## Reference files

- `references/site-architecture.md` — sitemap patterns, URL rules, the cross-link mesh, nav, breadcrumbs
- `references/location-pages.md` — the uniqueness bar, specificity sources, what not to do
- `references/seo-technical.md` — meta patterns, Core Web Vitals, accessibility, analytics
- `references/schema-templates.md` — JSON-LD for every template, with pitfalls
- `references/favicon-google-icon.md` — getting the brand icon into search results
- `references/google-business-profile.md` — the off-site work, and realistic timelines
- `references/discovery-interview.md` — what to ask the user and the owner
