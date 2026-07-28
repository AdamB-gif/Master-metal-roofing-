# 08 — Design System

## Design direction

Rugged, clean, unmistakably local. This should look like a contractor who does careful work — not like a national franchise template and not like a 2011 WordPress theme with a stock photo of a smiling family.

**Reference feel:** heavy dark navy or charcoal, generous white space, big honest photographs of real roofs, a strong warm accent for calls to action, sturdy sans-serif type. Metal, mountains, and daylight.

**The photos carry the design.** Keep the chrome minimal so real project photography does the work. If the photos are good, restraint looks confident. If the design is busy, good photos get buried.

---

## Color

```css
:root {
  /* Brand */
  --navy-900: #14202F;   /* darkest — footer, overlays */
  --navy-800: #1B2A41;   /* primary brand — header, headings, theme-color */
  --navy-600: #2E4363;
  --navy-100: #E8EDF4;   /* tinted section backgrounds */

  /* Accent — CTAs only */
  --accent-600: #B7410E; /* rust / weathered steel */
  --accent-500: #D4551C;
  --accent-100: #FDEDE4;

  /* Neutrals */
  --steel-900: #1A1A1A;  /* body text */
  --steel-600: #4A5462;  /* secondary text */
  --steel-300: #C8CED6;  /* borders */
  --steel-100: #F4F6F8;  /* alt backgrounds */
  --white: #FFFFFF;

  /* Status */
  --success: #1E7B4D;
  --error:   #B3261E;
}
```

**Rules:**
- The accent color is reserved for calls to action. If it's used for decoration, it stops meaning "click here."
- Verify contrast: `--accent-600` on white is roughly 5.5:1 — passes AA for body text. `--accent-500` does **not** — use it only for large text or as a hover state on dark. Check every pairing with a contrast tool; don't assume.
- Dark overlays on hero photos: `linear-gradient(rgba(20,32,47,0.75), rgba(20,32,47,0.45))`. Confirm 4.5:1 against the actual photo, not against the flat color — a bright sky behind white text will fail.
- `{{BRAND_COLORS}}` — if the owner has existing logo colors from signage or truck lettering, use those instead and rebuild the palette around them. Consistency with what's already on the truck beats anything designed from scratch.

---

## Typography

```css
--font-display: 'Barlow Condensed', 'Oswald', system-ui, sans-serif;  /* headings */
--font-body:    'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

Condensed display faces read as industrial and construction-adjacent without being kitschy. Two families, three weights total (400, 600, 700). Self-hosted WOFF2, subset to Latin.

**Scale (fluid, `clamp()`):**

| Element | Size | Weight | Line height |
|---|---|---|---|
| H1 | `clamp(2.25rem, 5vw, 3.75rem)` | 700 | 1.1 |
| H2 | `clamp(1.75rem, 3.5vw, 2.5rem)` | 700 | 1.2 |
| H3 | `clamp(1.25rem, 2.5vw, 1.5rem)` | 600 | 1.3 |
| Body | `1.0625rem` (17px) | 400 | 1.7 |
| Body large | `1.1875rem` | 400 | 1.7 |
| Small | `0.875rem` | 400 | 1.6 |

Body text 17px minimum. A meaningful share of this audience is over 50 and reading on a phone in daylight. Max line length 70ch.

---

## Spacing & layout

8px base scale: `4 8 12 16 24 32 48 64 96 128`.

Container max-width 1200px, content max-width 760px for prose. Section padding: 64px mobile / 96px desktop vertical. Grid: 12 columns desktop, 1 column mobile.

**Breakpoints:** 480 / 768 / 1024 / 1280. Build mobile-first.

---

## Components

### Buttons
```
Primary:   accent-600 bg, white text, 6px radius, 16px/32px padding, 600 weight
           hover: accent-500, 2px lift, subtle shadow
Secondary: transparent bg, 2px navy-800 border, navy-800 text
           hover: navy-800 bg, white text
Phone:     white bg, navy border, phone icon, always visible in header
```
Minimum 48px tall. Visible focus ring: `outline: 3px solid var(--accent-600); outline-offset: 2px`.

### Header
Sticky on scroll, 72px desktop / 60px mobile. White background, subtle bottom shadow once scrolled. Logo left, nav center, phone + Free Estimate button right. Mobile: logo left, hamburger right.

### Sticky mobile CTA bar
Fixed to viewport bottom, all pages, below 768px. Two 50% buttons: `📞 Call Now` (navy) and `Free Estimate` (accent). 56px tall. Not dismissible. Add `padding-bottom` to `<body>` so it never covers footer content.

**This element will generate more leads than anything else on the site.** Build it first, test it on a real phone.

### Cards
White, 8px radius, `1px solid steel-300`, 24px padding. 16:10 image at top, bleeding to card edges. Hover: 4px lift + shadow, 150ms ease. Entire card clickable, with a real `<a>` wrapping the heading for accessibility.

### Section variants
Alternate: white → `steel-100` → white → `navy-800` (inverted text) → white. Prevents the long-scroll monotony that makes contractor sites feel like brochureware.

### Forms
Full-width inputs, 48px tall, 6px radius, `1px solid steel-300`. Focus: 2px accent border + soft ring. Real `<label>` above every field, never placeholder-as-label. Errors below the field in `--error` with an icon, and announced to screen readers via `aria-live`.

### FAQ accordion
`<details>`/`<summary>` — zero JavaScript, keyboard accessible for free, and content stays in the DOM for crawlers. Chevron rotates on open. Answers visible in HTML at all times.

### Image treatments
- Hero: full-bleed, 60vh mobile / 75vh desktop, gradient overlay.
- Gallery: 4:3, `object-fit: cover`, consistent aspect ratio so the grid doesn't jump.
- Before/after: side-by-side on desktop, stacked on mobile, clearly labeled. A drag slider is optional and must not be the only way to see both images.

---

## Motion

Minimal. Buttons and cards get 150ms ease transitions. Optional fade-up on scroll for section entry, 300ms, once only. **Respect `prefers-reduced-motion: reduce`** and disable all of it. No parallax, no auto-playing carousels, no counters that tick up.

---

## Iconography

Simple line icons at 1.5–2px stroke, single color. Lucide or Heroicons, inlined as SVG — no icon-font library. Needed: phone, mail, map pin, check, shield (licensed/insured), home, building, hammer/tools, chevron, star, menu, close.

---

## What to avoid

❌ Stock photos of models in hard hats
❌ Auto-rotating hero carousels — bad for LCP, worse for conversion
❌ Live chat widgets
❌ Full-screen popups or exit-intent modals
❌ Google Maps iframes
❌ Animated counters ("2,847 roofs installed!")
❌ Any claim, badge, or logo the owner hasn't confirmed
❌ Video backgrounds

---

## Print styles

Include a basic print stylesheet. People print estimate pages and contact info more often than you'd expect. Hide nav, footer, and the sticky bar; show URLs after links; keep the phone number prominent.
