# Page Specs — Trust & Conversion Pages

These pages don't bring much traffic. They close it. A homeowner who has already decided they like the look of the site comes here to check whether the company is real.

---

## `/about/`

**Title:** `About Metal Master Roofing | Family Owned, Tazewell County VA`
**H1:** `About Metal Master Roofing & Construction`
**Words:** 700–1,000

### Sections

**1. The story.** 200–300 words, first person, from the owner. This must be a real interview, not invention. Ask the owner:
- How did you get into metal roofing?
- How long have you been doing it?
- What's the job you're proudest of?
- What do you wish homeowners knew before they call anybody?
- Why metal specifically?

Then write it in the owner's actual voice. A real, specific origin story is worth more than any amount of polished marketing copy, and it's the thing national lead-gen competitors structurally cannot produce.

**2. Photo of the owner** — real, on a jobsite, not a studio headshot. `{{OWNER_PHOTO}}`. This single image measurably raises contact rates on contractor sites. People want to know who's coming to their house.

**3. Licensed & insured.** Virginia contractor license `{{VA_LICENSE_NUMBER}}`, class `{{LICENSE_CLASS}}`, general liability with `{{INSURANCE}}`, workers' comp `{{WORKERS_COMP}}`. Include a line inviting people to verify the license themselves through Virginia DPOR — inviting verification is a stronger trust signal than claiming it.

**4. What we do and don't do.** Honest scoping. Residential and light commercial up to $150,000. Metal roofing, metal siding, board and batten. If there are things the owner doesn't do — flat commercial membrane, multi-story commercial, slate — say so. Contractors who tell you what they don't do read as more trustworthy than contractors who claim everything.

**5. Service area.** Short, with links.

**6. CTA.**

**Schema:** `AboutPage` + `Organization`.

---

## `/gallery/`

**Title:** `Metal Roofing Photo Gallery | Projects in Tazewell County VA`
**H1:** `Our Work`
**Words:** 300–400 of text plus the grid.

### Requirements

- **Filterable grid** — filter by service (metal roofing, standing seam, board & batten, siding, repair, commercial) and by town. Filtering must be CSS/minimal-JS and must not hide content from crawlers. All images render in the initial HTML.
- **Every image gets a real caption:** service + town + a detail. *"Charcoal standing seam roof — Richlands, VA. 12/12 pitch with two dormers."*
- **Every image gets descriptive alt text.** See `09-assets-and-images.md`.
- **Before/after pairs** wherever they exist. These are the highest-engagement items in any contractor gallery — put them first.
- **Lazy-load everything below the fold**, explicit width/height on all images, WebP/AVIF.
- **Each item links** to its service page and its town page. This turns the gallery into an internal-linking engine.
- Lightbox on click is optional; if built, it must be keyboard-accessible (Escape closes, arrows navigate, focus is trapped and restored).

**Minimum 12 images to launch. Target 30+.** A thin gallery is worse than no gallery — it suggests there isn't much work to show.

**Schema:** `ImageGallery` / `CollectionPage`.

---

## `/reviews/`

**Title:** `Reviews | Metal Master Roofing & Construction | Tazewell County VA`
**H1:** `What Our Customers Say`

### Hard rules

⚠️ **Only real, verifiable reviews.** Pulled from Google Business Profile or Facebook, attributed with first name and last initial and the town. Never invent a testimonial. Beyond being a Google policy violation, fake testimonials are an FTC deceptive-practices issue with real penalties, and in a county this size someone will notice.

⚠️ **Do not add `AggregateRating` schema to reviews the site owner collected and displays about itself.** Google's structured data guidelines prohibit self-serving review markup, and it can trigger a manual action. Display reviews as normal HTML and link out to the Google profile.

### If there are fewer than 5 reviews

Don't build this page yet. Instead:
1. Build the page as a stub that links to the Google Business Profile review page.
2. Make review generation the owner's number-one post-launch task. **Review velocity — new reviews arriving steadily — is a stronger local ranking factor than total review count.** Ten reviews over ten months beats forty reviews from three years ago.
3. Give the owner a short SMS script and a QR-coded card to hand out at job completion. Include a direct "leave a review" short link.

### Layout

Review cards with star rating, text, attribution, date, and service performed. A prominent "Leave us a review" CTA linking directly to the Google review form.

---

## `/contact/`

**Title:** `Contact Metal Master Roofing | Bluefield & Richlands VA`
**H1:** `Get in Touch`
**Words:** 300–400

### Layout — two columns

**Left — contact methods.** Phone as a large tap-to-call button (the primary action; most people calling a roofer want to talk to a person). Email. Hours `{{HOURS}}`. Facebook link. Service area summary. Response time expectation `{{RESPONSE_TIME}}` — setting this explicitly reduces the anxiety that stops people from reaching out.

**Right — short form.** Name, phone, email, town, service needed, message. Five fields maximum. See `11-forms-and-lead-capture.md`.

**No embedded Google Map** unless an address is published. If an address is eventually published, use a static map image linking out to Google Maps — not an iframe.

**Schema:** `ContactPage` + `LocalBusiness`.

---

## `/free-estimate/` ★ primary conversion page

**Title:** `Free Metal Roof Estimate | Tazewell County VA | Metal Master Roofing`
**Meta:** `Get a free, no-pressure estimate on a metal roof, siding, or board and batten. Licensed & insured, family owned, serving Tazewell County VA. Call {{PHONE}}.`
**H1:** `Get Your Free Estimate`
**Words:** 400–600

This is where every CTA on the site points. Optimize it ruthlessly.

### Structure

**1. Above the fold: the form itself.** Not a paragraph, then the form. The form. Anyone landing here has already decided.

**2. Beside the form — "What happens next," four steps:**
> 1. You send this form or call us.
> 2. We call you back within `{{RESPONSE_TIME}}` to set a time.
> 3. We come out, get on the roof, and measure it properly.
> 4. You get a written estimate. No pressure, no expiration date, no salesman in your living room for two hours.

That fourth line addresses the specific fear that keeps people from requesting home-services estimates. Keep it.

**3. Below: trust strip.** Licensed & insured · Family owned · Free estimates · Local

**4. Short FAQ (3):**
- Is the estimate really free? (Yes. Always.)
- Do I have to be home? (`{{ANSWER}}` — usually yes for the walkthrough, but confirm.)
- How long does it take to get an estimate? (`{{ANSWER}}`)

**5. Fallback:** "Would rather just talk? Call `{{PHONE}}`." — a large phone button. Many customers in this market will always prefer the phone. Don't force the form.

### Thank-you page
Form submits to `/thank-you/` (`noindex`). Confirms receipt, restates the response time, offers the phone number, links to the gallery to keep them on-site. This URL is the conversion goal in analytics.

---

## `/faq/` (Phase 3)

**Title:** `Metal Roofing FAQ | Common Questions | Tazewell County VA`
**H1:** `Frequently Asked Questions`
**Words:** 1,200–1,800

Aggregate every FAQ on the site into one organized page, grouped: Cost & Estimates · Metal Roofing Basics · Installation · Materials & Colors · Board & Batten Siding · Working With Us · Service Area.

**Value:** long-tail question queries, featured snippets, and — increasingly important — this is the page AI assistants and search summaries pull from when answering "does anyone install metal roofs near Bluefield VA." Direct, plainly-worded answers get cited; marketing copy doesn't.

Use `FAQPage` schema. Note that Google now shows FAQ rich results mainly for authoritative sites, so treat the markup as a bonus rather than the reason for the page.

---

## Legal pages

**`/privacy-policy/`** — required if the site has a form or any analytics. Cover: what's collected, why, how it's stored, third parties (analytics, form processor), cookies, and how to request deletion. `{{LEGAL_REVIEW}}` — a template is fine to start but should be reviewed.

**`/accessibility/`** — a short statement of the WCAG 2.1 AA target and a contact for accessibility issues. Small but genuinely useful, and it reduces drive-by ADA demand-letter risk that has hit contractor sites.
