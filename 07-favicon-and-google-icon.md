# 07 — Favicon & the Google Search Icon

## The goal, stated precisely

When someone searches **"Metal Master Roofing,"** the owner wants the company's icon displayed next to the site in Google's results.

That icon is the **favicon**. Google shows it beside the result on mobile search and, for many queries, on desktop as well. Getting it to appear is straightforward but has specific requirements — and one honest caveat.

> **Caveat, stated up front:** Google does not guarantee favicon display even when every guideline is met. Following the spec below makes it very likely, not certain. Set that expectation with the owner rather than promising it.

Two related but separate things are worth distinguishing:
1. **Favicon in search results** — the small icon beside the URL. Fully controllable. Do all of the below.
2. **Knowledge panel / brand logo** — the larger card that can appear on the right for a recognized business entity. Not directly controllable; it emerges from a verified Google Business Profile plus consistent entity signals. Covered at the end.

---

## Google's requirements

| Requirement | Spec |
|---|---|
| Shape | Square |
| Minimum size | 8×8px (technically) |
| **Recommended size** | **≥ 48×48px; use 96×96 or larger for sharpness** |
| Formats accepted | ICO, PNG, SVG, JPEG, GIF |
| Location | Crawlable URL, not blocked by robots.txt |
| Declaration | `<link rel="icon">` in the `<head>` of the **home page** |
| Stability | Same URL over time — Google caches it; frequent changes delay updates |
| Content | Must represent the brand. No adult, hateful, or violent imagery. |

**Google recrawls the home page to pick up favicon changes.** After launch, expect days to a few weeks before the icon appears. It is not instant, and no amount of resubmitting speeds it up.

---

## Designing the icon

The favicon renders at roughly **16×16 CSS pixels** in search results. Nearly everything is illegible at that size. Design for the constraint:

**Do:**
- Extract a **monogram or mark**, not the full logo. `MM`, a single stylized `M`, or a simple roofline silhouette.
- Solid, high-contrast colors. Ideally the brand's dark navy/charcoal with the accent color.
- Bold geometric shapes. Minimum 2–3px stroke weight at the target size.
- A **filled background** — the icon sits on white in Google's results, and a transparent icon with light elements disappears entirely. Fill the square with the dark brand color and put the mark in light.
- Test it by shrinking to 16×16 and looking at it on a phone at arm's length. If you can't tell what it is, simplify further.

**Don't:**
- Don't use the full logo with the company name. "Metal Master Roofing and Construction" at 16px is a gray smudge.
- Don't use thin lines, fine detail, gradients, or drop shadows.
- Don't use a photo.
- Don't use a transparent background with dark-only elements.

**Recommended concept:** a rounded square filled with the dark brand navy, containing a simple light-colored roofline chevron (an inverted V, like the profile of a gable) with a subtle standing-seam line — or, simpler and safer, a bold `MM` monogram. The chevron reads as "roof" instantly at small size and is more distinctive than letters. Produce both and compare at 16px before choosing.

---

## Files to generate

Generate all from one 1024×1024 master (SVG source preferred).

```
/favicon.ico                    16, 32, 48 multi-resolution ICO — root, legacy support
/favicon.svg                    Vector, modern browsers, supports dark-mode variants
/favicon-96x96.png              Google's recommended size
/favicon-192x192.png            Android
/apple-touch-icon.png           180×180, opaque background (iOS ignores transparency)
/icon-512x512.png               PWA / Organization schema logo
/site.webmanifest
```

## `<head>` declaration — home page and, for consistency, every page

```html
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#1B2A41">
```

`site.webmanifest`:

```json
{
  "name": "Metal Master Roofing and Construction",
  "short_name": "Metal Master",
  "icons": [
    { "src": "/favicon-192x192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icon-512x512.png", "sizes": "512x512", "type": "image/png" }
  ],
  "theme_color": "#1B2A41",
  "background_color": "#ffffff",
  "display": "standalone"
}
```

---

## Verification checklist

- [ ] Favicon files return HTTP 200 at their absolute URLs
- [ ] `robots.txt` does not block `/favicon*` or `/images/`
- [ ] The `<link rel="icon">` tags are in the **home page** `<head>` (Google reads the home page specifically)
- [ ] Icon is square and ≥ 96×96 in the PNG version
- [ ] Icon is legible at 16×16 — verify visually, on a phone
- [ ] Icon has an opaque background
- [ ] `Organization` schema `logo` points to `/icon-512x512.png` (see `06-schema-markup.md`)
- [ ] Same icon uploaded as the Google Business Profile logo
- [ ] Same icon set as the Facebook page profile picture
- [ ] Home page submitted for indexing in Search Console at launch
- [ ] Check `site:{{DOMAIN}}` on mobile Google 1–3 weeks post-launch to confirm

---

## Beyond the favicon: getting the full brand presence

The favicon is step one. To make a search for "Metal Master Roofing" return a rich, branded result — icon, business card panel, map, reviews, call button — three things must line up:

1. **Verified Google Business Profile.** This is what produces the panel on the right-hand side with photos, hours, reviews, and a call button. It matters more than anything on the website for branded searches. See `13-google-business-profile.md`. **This is the single highest-value action on the entire project.**

2. **Consistent entity signals.** The exact same business name, phone number, and logo across the website, the Google Business Profile, the Facebook page, and any directory listing. Google resolves these into one entity; inconsistency splits it into several weak ones.

3. **`Organization` + `RoofingContractor` schema** connecting the website to the brand, with `sameAs` linking to the Facebook page and Google profile. This is how the site tells Google "this website and that business profile are the same company."

**Realistic timeline:** favicon in results within 1–4 weeks of launch. Branded search returning site + Google Business Profile panel within 2–8 weeks of GBP verification, assuming the name is reasonably distinctive — and "Metal Master Roofing" is distinctive enough that ranking #1 for it should be straightforward.
