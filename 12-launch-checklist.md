# 12 — Launch Checklist

Nothing goes live until every launch-blocking item is checked. Items marked 🚫 are hard blockers.

---

## Content

- [ ] 🚫 **Zero `{{PLACEHOLDER}}` strings anywhere in production HTML.** Grep the build output for `{{` before deploying.
- [ ] 🚫 Phone number correct, consistent, and tested by actually calling it
- [ ] 🚫 No invented reviews, credentials, awards, certifications, or years in business
- [ ] 🚫 License number and class confirmed by the owner before publishing
- [ ] 🚫 West Virginia pages removed unless WV licensing is confirmed
- [ ] Board & batten terminology confirmed with the owner (metal siding vs. wood vs. both)
- [ ] Every service page corresponds to a service the owner actually performs
- [ ] Every location page is a town the owner will actually drive to
- [ ] Every page proofread — spelling, grammar, town names spelled correctly
- [ ] Location pages pass the 40% uniqueness bar. Spot-check by diffing two pages.
- [ ] No banned phrases from `10-content-copy-guide.md`
- [ ] Cost information reflects the owner's real pricing, not national averages

## Technical SEO

- [ ] 🚫 Every page has a unique title tag ≤ 60 chars
- [ ] 🚫 Every page has a unique meta description, 150–160 chars
- [ ] 🚫 Every page has a self-referencing absolute canonical
- [ ] 🚫 Exactly one `<h1>` per page; no skipped heading levels
- [ ] 🚫 `sitemap.xml` generated, accurate, and contains only indexable pages
- [ ] 🚫 `robots.txt` correct, not blocking anything important, sitemap referenced
- [ ] `/thank-you/` is `noindex`
- [ ] HTTPS forced; single canonical hostname; www/non-www redirect working
- [ ] Trailing slashes consistent
- [ ] Custom 404 returns a real 404 status
- [ ] No broken internal links (run a full crawl)
- [ ] No orphan pages — every URL in the sitemap has ≥1 internal inbound link
- [ ] Open Graph + Twitter Card tags on every page; OG images render correctly (test with Facebook's Sharing Debugger)
- [ ] `lang="en"` on `<html>`

## Structured data

- [ ] 🚫 `RoofingContractor` schema sitewide, validates with zero errors
- [ ] 🚫 No `aggregateRating` on self-hosted reviews
- [ ] `Organization` + `WebSite` on home page
- [ ] `Service` schema on every service page
- [ ] `BreadcrumbList` on every non-home page, mirroring the visible breadcrumb
- [ ] `FAQPage` where FAQs exist, and all marked-up content is visible
- [ ] `Article` on blog posts with real dates and a named author
- [ ] Rich Results Test passes on home, a service page, a location page, a blog post
- [ ] No placeholder strings in production JSON-LD

## Favicon & branding

- [ ] 🚫 Favicon set generated at all required sizes
- [ ] 🚫 `<link rel="icon">` tags present in the **home page** `<head>`
- [ ] Favicon files return 200 and are not blocked by robots.txt
- [ ] Icon is square, ≥96×96 PNG, opaque background, legible at 16×16 (check on a phone)
- [ ] `site.webmanifest` valid
- [ ] `theme-color` set
- [ ] Same logo used on the website, Google Business Profile, and Facebook

## Performance

- [ ] 🚫 Lighthouse ≥ 95 on Performance, Accessibility, Best Practices, SEO — home, one service, one location page
- [ ] LCP < 1.5s on throttled 4G mobile
- [ ] CLS < 0.05
- [ ] INP < 200ms
- [ ] Hero image preloaded, `fetchpriority="high"`, not lazy-loaded
- [ ] All images AVIF/WebP with responsive `srcset`
- [ ] Every `<img>` has explicit width and height
- [ ] Below-fold images lazy-loaded
- [ ] Fonts self-hosted, WOFF2, subset, `font-display: swap`
- [ ] JS bundle < 50KB gzipped
- [ ] No Google Maps iframe, no chat widget, no carousel library

## Accessibility

- [ ] 🚫 axe DevTools: zero critical violations
- [ ] 🚫 Full keyboard-only pass through the site — everything reachable, visible focus ring
- [ ] Contrast ≥ 4.5:1 body text, ≥ 3:1 large text and UI — including text over hero photos
- [ ] All meaningful images have descriptive alt text; decorative images have `alt=""`
- [ ] Form fields use real `<label>` elements
- [ ] Skip-to-content link present and first in tab order
- [ ] Touch targets ≥ 44×44px
- [ ] Accordion and lightbox ARIA correct; Escape closes; focus restored
- [ ] `prefers-reduced-motion` respected
- [ ] Screen reader spot-check on home and the estimate form

## Forms & conversion

- [ ] 🚫 Estimate form submits successfully, end to end, on a real phone
- [ ] 🚫 Lead notification arrives at the owner's email **and** phone — verified by the owner, not assumed
- [ ] Contact form works
- [ ] Honeypot and time-trap spam protection active
- [ ] Auto-reply sends (if configured)
- [ ] Redirects to `/thank-you/` on success
- [ ] Failure state preserves data and shows the phone number
- [ ] Every `tel:` link tested on iOS and Android
- [ ] Sticky mobile CTA bar present on all pages, doesn't obscure footer content

## Analytics

- [ ] 🚫 Google Search Console verified, sitemap submitted
- [ ] Analytics installed and firing
- [ ] `phone_click` and `form_submit` configured as key events/conversions
- [ ] `/thank-you/` tracking as a conversion
- [ ] Test conversion fired and confirmed in the analytics dashboard

## Cross-browser & device

- [ ] Chrome, Safari, Firefox, Edge — desktop
- [ ] iOS Safari and Android Chrome — **on real hardware, not just emulation**
- [ ] 320px width (small phones) — no horizontal scroll anywhere
- [ ] 768px, 1024px, 1440px, 1920px
- [ ] Landscape orientation on phone
- [ ] Print stylesheet works on the contact and estimate pages

## Legal & privacy

- [ ] Privacy policy published and linked in the footer
- [ ] Accessibility statement published
- [ ] Copyright year is dynamic
- [ ] No customer addresses, faces, license plates, or house numbers published without permission
- [ ] EXIF GPS stripped from published photos
- [ ] No manufacturer logos or certification badges the owner hasn't confirmed rights to use

## Day-of-launch

1. Deploy to production
2. Verify HTTPS and the redirect chain
3. Verify Search Console; submit the sitemap
4. Request indexing for the home page (this is what triggers favicon pickup)
5. Test the form live in production — not just staging
6. Call the phone number from an outside line
7. Share the URL to Facebook and check that the OG card renders
8. Update the Google Business Profile website field
9. Update the Facebook page's website field
10. Screenshot Lighthouse scores for the record

---

## Week 1 after launch

- [ ] Search Console: confirm pages are being indexed, zero coverage errors
- [ ] Confirm no `noindex` accidentally shipped to production (the classic staging-to-prod mistake — check this specifically)
- [ ] Check that at least one real lead has come through
- [ ] Google Business Profile fully completed and, if new, verification in progress
- [ ] Ask the owner to review every page for factual accuracy

## Week 2–4 after launch

- [ ] Check `site:{{DOMAIN}}` on mobile Google — is the favicon showing?
- [ ] Search "Metal Master Roofing" — does the site rank #1? Does the GBP panel appear?
- [ ] Search Console: first impression data, first query list
- [ ] Core Web Vitals field data starting to populate
- [ ] Review generation underway — at least 2 new reviews requested

---

## Handoff to the owner

Deliver a short plain-language document covering:

1. How to reach the site's files and hosting; who has access to what
2. How to check leads and where notifications go
3. The Google Business Profile weekly routine — photos, a post, review requests, review responses
4. How to send new project photos for the gallery, and the three-photos-per-job habit
5. What to expect and when — the timeline in `13-google-business-profile.md`, so month two doesn't feel like failure
6. Who to call when something breaks
