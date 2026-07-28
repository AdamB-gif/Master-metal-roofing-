# 05 — Technical SEO Specification

## Per-page requirements (every page, no exceptions)

```html
<title>Primary Keyword | Brand</title>                        <!-- ≤60 chars -->
<meta name="description" content="...">                       <!-- 150-160 chars -->
<link rel="canonical" href="https://{{DOMAIN}}/full/path/">   <!-- self-referencing, absolute -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta charset="utf-8">
<html lang="en">
```

Plus: exactly one `<h1>`; heading levels in order with no skips; Open Graph and Twitter Card tags; JSON-LD per `06-schema-markup.md`.

### Title tag patterns

| Page type | Pattern |
|---|---|
| Home | `Metal Roofing Tazewell County VA \| Metal Master Roofing & Construction` |
| Service | `[Service] [Town/Region] \| Metal Master Roofing` |
| Location | `Metal Roofing [Town], [ST] \| Metal Roofs & Siding \| Metal Master` |
| Blog | `[Article Title] \| Metal Master Roofing` |

Front-load the keyword. Brand goes last. Never duplicate a title across pages — duplicate titles are the fastest way to look like a doorway-page site.

### Meta descriptions

150–160 characters, written to earn a click, not to hold keywords. Include the primary keyword naturally, a differentiator, and a call to action with the phone number. Every one unique.

### Open Graph (Facebook matters here — it's the company's existing audience)

```html
<meta property="og:type" content="website">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="https://{{DOMAIN}}/og/[page].jpg">   <!-- 1200×630 -->
<meta property="og:url" content="https://{{DOMAIN}}/path/">
<meta property="og:site_name" content="Metal Master Roofing & Construction">
<meta name="twitter:card" content="summary_large_image">
```

Generate a distinct 1200×630 OG image per major page: project photo, dark overlay, logo, page title. When the owner shares a link on Facebook, this is what appears — treat it as a real deliverable, not an afterthought.

---

## robots.txt

```
User-agent: *
Allow: /
Disallow: /thank-you/

Sitemap: https://{{DOMAIN}}/sitemap.xml
```

Do not block AI crawlers (GPTBot, ClaudeBot, PerplexityBot, etc.). For a local business, being quotable in AI answers is upside, not risk.

## sitemap.xml

Auto-generated at build. All indexable pages, absolute URLs, accurate `lastmod` from real file modification time (never a build timestamp on unchanged files — that's a fake-freshness signal). Omit `priority` and `changefreq`; Google ignores them. Submit in Search Console at launch.

## Redirects

- Force HTTPS. Force one canonical hostname (www or non-www — pick one, redirect the other).
- 301, not 302, for all permanent moves.
- Enforce trailing slashes consistently.
- Custom 404 with search, top service links, and the phone number. Returns a real 404 status — soft 404s that return 200 pollute the index.

---

## Core Web Vitals — targets and how to hit them

| Metric | Target |
|---|---|
| LCP | < 1.5s (Google's "good" is 2.5s; beat it) |
| INP | < 200ms |
| CLS | < 0.05 |
| TTFB | < 400ms |
| Total page weight | < 800KB, home page < 1MB |
| JS shipped | < 50KB gzipped |

**Images** are the whole ballgame on a photo-heavy roofing site:
- AVIF with WebP fallback and JPEG last resort. Generate at build.
- Responsive `srcset` at 400/800/1200/1600px.
- Explicit `width` and `height` on every `<img>` — this alone eliminates most CLS.
- `loading="lazy"` on everything below the fold; **never** on the hero.
- `fetchpriority="high"` + `<link rel="preload">` on the LCP hero image.
- Compress to ~80% quality. A 4MB phone photo must never reach a browser.

**Fonts:** self-host, WOFF2, `font-display: swap`, preload the primary weight, subset to Latin. Two families maximum, three weights total. No Google Fonts CDN link (extra connection, and a GDPR question mark).

**JavaScript:** ship as little as possible. The nav toggle, the gallery filter, and the FAQ accordion are the only interactive elements, and all three can be built with minimal or zero JS. No jQuery. No carousel library. No animation framework.

**Third-party scripts:** each one is a performance tax. Analytics only. **No live chat widget** — they typically cost 300ms+ INP and convert worse than a visible phone number in this market. **No Google Maps iframe** — 500KB+ for zero SEO value; use a static image linking to Maps.

---

## Accessibility (WCAG 2.1 AA)

Not optional — it's a legal exposure area for contractor sites, and it correlates with better SEO.

- Contrast ≥ 4.5:1 for body text, ≥ 3:1 for large text and UI. Check the accent color on white carefully.
- All interactive elements keyboard-reachable with a visible focus ring. Never `outline: none` without a replacement.
- Semantic landmarks: `<header> <nav> <main> <footer>`, one `<main>` per page.
- Alt text on all meaningful images; `alt=""` on decorative ones.
- Form labels are real `<label>` elements, not placeholder text.
- Skip-to-content link as the first focusable element.
- Touch targets ≥ 44×44px.
- Accordions and the gallery lightbox need correct ARIA (`aria-expanded`, `aria-controls`, focus trapping, Escape to close).
- Test with axe DevTools and one keyboard-only pass through the whole site.

---

## Analytics and tracking

- **Google Search Console** — verify at launch, submit sitemap, monitor coverage and queries weekly. Non-negotiable.
- **Google Analytics 4**, or a lighter privacy-first alternative (Plausible, Fathom, Cloudflare Web Analytics). GA4 is free and integrates with Search Console; the alternatives are faster and simpler. Either is defensible.
- **Conversion events:** `phone_click` (any `tel:` click), `form_submit` (on `/thank-you/`), `estimate_page_view`, `email_click`. Without call tracking these are the only lead signals available — instrument them properly.
- Optional: a call-tracking number. Only if the owner wants it, and if used, **the NAP number on the site and Google Business Profile must stay the primary number** — inconsistent NAP across the web actively damages local rankings.

---

## Local SEO on-page essentials

1. **NAP consistency.** The business name, address (if any), and phone must appear byte-identical everywhere: site, Google Business Profile, Facebook, and every directory. "Metal Master Roofing and Construction" vs. "Metal Master Roofing & Construction" as the *business name* is a real inconsistency — pick one canonical form and use it in all structured data and citations. (A shortened brand name in nav display copy is fine; the structured/canonical name is what must match.)
2. **Phone number in the HTML as text**, not baked into an image, and in `tel:` links.
3. **Town names in H1s and title tags** on location pages.
4. **Embedded local relevance** in body copy — real roads, ridges, neighborhoods, weather.
5. **Geo-tagged project photos** where the owner has them. EXIF location data on job photos is a quiet local signal, and it also lets photos be organized by town for the gallery filter.

---

## Post-launch monitoring

**Weekly (first 90 days):** Search Console coverage errors, new query impressions, GBP insights (calls, direction requests, searches), form submissions.

**Monthly:** rank check on the priority keyword set, Core Web Vitals field data, new review count, competitor SERP check for the four priority towns.

**Quarterly:** content refresh on the cost article (prices move), new project photos into the gallery, one new blog article, internal-link audit for orphans.
