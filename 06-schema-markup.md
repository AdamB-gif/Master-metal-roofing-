# 06 — Structured Data (JSON-LD)

All schema as JSON-LD in `<script type="application/ld+json">`. Validate every template at **validator.schema.org** and **search.google.com/test/rich-results** before launch.

---

## 1. RoofingContractor — sitewide (the important one)

Place in the site-wide `<head>` on **every** page. `RoofingContractor` is a specific subtype of `LocalBusiness` and is more precise than the generic type — use it.

**Service-area-business variant (use this until an address is confirmed):**

```json
{
  "@context": "https://schema.org",
  "@type": "RoofingContractor",
  "@id": "https://{{DOMAIN}}/#business",
  "name": "Metal Master Roofing and Construction",
  "alternateName": "Metal Master Roofing",
  "url": "https://{{DOMAIN}}/",
  "logo": "https://{{DOMAIN}}/images/logo.png",
  "image": "https://{{DOMAIN}}/images/og-default.jpg",
  "telephone": "{{PHONE_E164}}",
  "email": "{{EMAIL}}",
  "description": "Metal roofing, metal siding, and board and batten installation for residential and light commercial properties across Tazewell County, Virginia and southern West Virginia. Family owned, licensed and insured. Free estimates.",
  "priceRange": "$$",
  "sameAs": [
    "https://www.facebook.com/people/Metal-Master-Roofing-and-Construction/61562911080390/",
    "{{GOOGLE_BUSINESS_PROFILE_URL}}"
  ],
  "areaServed": [
    { "@type": "AdministrativeArea", "name": "Tazewell County, Virginia" },
    { "@type": "City", "name": "Bluefield", "addressRegion": "VA" },
    { "@type": "City", "name": "Richlands", "addressRegion": "VA" },
    { "@type": "City", "name": "Pounding Mill", "addressRegion": "VA" },
    { "@type": "City", "name": "Tazewell", "addressRegion": "VA" },
    { "@type": "City", "name": "Cedar Bluff", "addressRegion": "VA" },
    { "@type": "City", "name": "North Tazewell", "addressRegion": "VA" },
    { "@type": "City", "name": "Claypool Hill", "addressRegion": "VA" },
    { "@type": "City", "name": "Raven", "addressRegion": "VA" },
    { "@type": "City", "name": "Bluefield", "addressRegion": "WV" },
    { "@type": "City", "name": "Princeton", "addressRegion": "WV" }
  ],
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "{{OPEN_TIME}}",
    "closes": "{{CLOSE_TIME}}"
  }],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Roofing and Siding Services",
    "itemListElement": [
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Metal Roof Installation" }},
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Standing Seam Metal Roofing" }},
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Exposed Fastener Metal Roofing" }},
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Board and Batten Metal Siding" }},
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Metal Roof Replacement" }},
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Metal Roof Repair" }},
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Commercial Metal Roofing" }}
    ]
  },
  "knowsAbout": ["Metal roofing","Standing seam roofing","Board and batten metal siding","Metal roof repair","Post frame buildings"],
  "slogan": "Free estimates. Licensed and insured. Local.",
  "founder": { "@type": "Person", "name": "{{OWNER_NAME}}" },
  "foundingDate": "{{YEAR_ESTABLISHED}}"
}
```

**If/when an address is confirmed**, add:

```json
"address": {
  "@type": "PostalAddress",
  "streetAddress": "{{STREET}}",
  "addressLocality": "{{CITY}}",
  "addressRegion": "VA",
  "postalCode": "{{ZIP}}",
  "addressCountry": "US"
},
"geo": { "@type": "GeoCoordinates", "latitude": "{{LAT}}", "longitude": "{{LNG}}" }
```

**Rules:**
- `telephone` in E.164 (`+12765550100`) inside schema; formatted for humans in visible copy.
- **Never** add `aggregateRating` that the site generates about itself. Self-serving review markup violates Google's guidelines and risks a manual action. Ratings come from the Google Business Profile, not from schema on your own site.
- Do not invent `foundingDate` or `priceRange`. Omit the property rather than guess.

---

## 2. Organization + logo — for the Google search icon

This works with the favicon (see `07-favicon-and-google-icon.md`) to establish the brand mark. On the **home page only**:

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://{{DOMAIN}}/#organization",
  "name": "Metal Master Roofing and Construction",
  "url": "https://{{DOMAIN}}/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://{{DOMAIN}}/images/logo-512.png",
    "width": 512,
    "height": 512
  },
  "sameAs": ["https://www.facebook.com/people/Metal-Master-Roofing-and-Construction/61562911080390/"]
}
```

---

## 3. WebSite — home page only

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://{{DOMAIN}}/#website",
  "url": "https://{{DOMAIN}}/",
  "name": "Metal Master Roofing and Construction",
  "publisher": { "@id": "https://{{DOMAIN}}/#organization" },
  "inLanguage": "en-US"
}
```

---

## 4. Service — every service page

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Standing Seam Metal Roof Installation",
  "name": "Standing Seam Metal Roofing",
  "description": "Standing seam metal roof installation with concealed fasteners for homes and light commercial buildings in Tazewell County, Virginia.",
  "provider": { "@id": "https://{{DOMAIN}}/#business" },
  "areaServed": [
    { "@type": "AdministrativeArea", "name": "Tazewell County, Virginia" },
    { "@type": "City", "name": "Bluefield", "addressRegion": "VA" },
    { "@type": "City", "name": "Richlands", "addressRegion": "VA" }
  ],
  "url": "https://{{DOMAIN}}/services/standing-seam-metal-roofing/"
}
```

---

## 5. Location pages

Reference the sitewide business `@id` and narrow `areaServed` to that town, plus a `WebPage` node:

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "url": "https://{{DOMAIN}}/service-areas/richlands-va/",
  "name": "Metal Roofing in Richlands, VA",
  "description": "Metal roofing, siding, and board and batten installation in Richlands, Virginia.",
  "about": { "@id": "https://{{DOMAIN}}/#business" },
  "isPartOf": { "@id": "https://{{DOMAIN}}/#website" },
  "primaryImageOfPage": { "@type": "ImageObject", "url": "https://{{DOMAIN}}/images/projects/richlands-standing-seam-01.jpg" }
}
```

⚠️ **Do not create a separate `LocalBusiness` node per town.** Multiple business entities for one business is a spam pattern and confuses entity resolution. One business, many `areaServed` values.

---

## 6. BreadcrumbList — every page except home

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://{{DOMAIN}}/" },
    { "@type": "ListItem", "position": 2, "name": "Service Areas", "item": "https://{{DOMAIN}}/service-areas/" },
    { "@type": "ListItem", "position": 3, "name": "Richlands, VA", "item": "https://{{DOMAIN}}/service-areas/richlands-va/" }
  ]
}
```

Must mirror the visible breadcrumb exactly. Google renders these in results, which lifts click-through.

---

## 7. FAQPage — any page with an FAQ section

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How much does a metal roof cost in Tazewell County?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Most metal roofs we install run between {{PRICE_LOW}} and {{PRICE_HIGH}} per square foot installed, depending on panel type, roof pitch, and complexity. We give an exact written number after measuring."
    }
  }]
}
```

Every Q&A in the markup must be visible on the page. Marking up hidden content is a violation. Google has narrowed FAQ rich-result eligibility, so treat visibility as the point and the rich result as a bonus.

---

## 8. Article — blog posts

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Much Does a Metal Roof Cost in Southwest Virginia?",
  "image": ["https://{{DOMAIN}}/images/blog/metal-roof-cost-hero.jpg"],
  "datePublished": "{{ISO_DATE}}",
  "dateModified": "{{ISO_DATE}}",
  "author": { "@type": "Person", "name": "{{OWNER_NAME}}", "url": "https://{{DOMAIN}}/about/" },
  "publisher": { "@id": "https://{{DOMAIN}}/#organization" },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://{{DOMAIN}}/blog/metal-roof-cost-southwest-virginia/" }
}
```

Real dates. A named human author with a link to a real About page is a meaningful expertise signal — an anonymous "Admin" byline is not.

---

## 9. ImageObject — gallery

```json
{
  "@context": "https://schema.org",
  "@type": "ImageObject",
  "contentUrl": "https://{{DOMAIN}}/images/projects/richlands-standing-seam-01.jpg",
  "name": "Charcoal standing seam metal roof in Richlands, VA",
  "description": "Standing seam metal roof installed on a two-story farmhouse in Richlands, Virginia.",
  "creditText": "Metal Master Roofing and Construction",
  "creator": { "@id": "https://{{DOMAIN}}/#organization" },
  "contentLocation": { "@type": "Place", "name": "Richlands, Virginia" }
}
```

---

## Validation checklist

- [ ] Every template validated at validator.schema.org — zero errors
- [ ] Rich Results Test passes on home, a service page, a location page, a blog post
- [ ] No `aggregateRating` anywhere on self-hosted reviews
- [ ] One business entity, referenced by `@id` — not duplicated per page
- [ ] All FAQ markup corresponds to visible page content
- [ ] No `{{PLACEHOLDER}}` strings remain in production JSON-LD
- [ ] Search Console → Enhancements shows zero structured-data errors 7 days post-launch
