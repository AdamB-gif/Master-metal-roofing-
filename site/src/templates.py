import json
import re
import time
import data as d

BUILD_VERSION = str(int(time.time()))

# ---------------------------------------------------------------- icons ---

ICONS = {
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16v16H4z"/><path d="m22 6-10 7L2 6"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/></svg>',
    "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/><path d="M9 22V12h6v10"/></svg>',
    "building": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20"/><path d="M9 22v-4h6v4M9 6h.01M9 10h.01M9 14h.01M15 6h.01M15 10h.01M15 14h.01"/></svg>',
    "tools": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
    "chevron": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h18M3 6h18M3 18h18"/></svg>',
    "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18M6 6l12 12"/></svg>',
    "roof": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12 12 4l9 8"/><path d="M5 11v9h14v-9"/><path d="M9 20v-6h6v6"/></svg>',
    "image": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg>',
}

def icon(name, cls=""):
    svg = ICONS[name]
    if cls:
        svg = svg.replace("<svg ", f'<svg class="{cls}" ', 1)
    return svg

# ------------------------------------------------------------ helpers -----

def ph(label):
    """Visible placeholder for an unconfirmed business fact."""
    return f'<span class="fact-ph">[{label}]</span>'

def phone_display():
    return d.PHONE_DISPLAY or ph("Phone number")

def phone_link(label=None, cls="btn btn-phone"):
    # No phone on the site by owner's decision — the form is the only inbound
    # channel. Render nothing at all rather than a dead placeholder button.
    if not d.PHONE_E164:
        return ""
    label = label or f"Call {d.PHONE_DISPLAY}"
    return f'<a class="{cls}" href="tel:{d.PHONE_E164}">{icon("phone")}{label}</a>'

def phone_text_link():
    if d.PHONE_E164:
        return f'<a href="tel:{d.PHONE_E164}">{d.PHONE_DISPLAY}</a>'
    return ""

def email_text_link():
    # Same as the phone: no public address, so nothing renders.
    if d.EMAIL:
        return f'<a href="mailto:{d.EMAIL}">{d.EMAIL}</a>'
    return ""

def hours_text():
    return d.HOURS or ph("Business hours")

def meta_call_cta():
    return f"Call {d.PHONE_DISPLAY}." if d.PHONE_DISPLAY else "Free estimates — contact us today."

def license_line():
    if d.VA_LICENSE_NUMBER:
        return f"Licensed & Insured · VA Lic. {d.VA_LICENSE_NUMBER}"
    return "Licensed & Insured · certificate available on request"

def esc(s):
    return s

def faq_block(items, heading="Common Questions"):
    rows = []
    for q, a in items:
        rows.append(f'''<details>
      <summary>{q} {icon("chevron", "chevron")}</summary>
      <p>{a}</p>
    </details>''')
    return f'''<div class="faq">
    {''.join(rows)}
  </div>'''

def faq_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^<]+?>', '', a)}}
            for q, a in items
        ]
    }

def breadcrumb_html(trail):
    """trail: list of (name, url) tuples, last item is current page (url can be None)."""
    parts = []
    for i, (name, url) in enumerate(trail):
        if i:
            parts.append('<span class="sep">/</span>')
        if url:
            parts.append(f'<a href="{url}">{name}</a>')
        else:
            parts.append(f'<span class="current">{name}</span>')
    return f'<nav class="breadcrumb container" aria-label="Breadcrumb">{"".join(parts)}</nav>'

def breadcrumb_schema(trail):
    items = []
    for i, (name, url) in enumerate(trail, start=1):
        item = {"@type": "ListItem", "position": i, "name": name}
        if url:
            item["item"] = f"https://{d.DOMAIN}{url}"
        items.append(item)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

def trust_strip_html(dark=False):
    icons = ["shield", "home", "check", "building"]
    items = "".join(
        f'<li>{icon(icons[i % 4])}{t}</li>' for i, t in enumerate(d.TRUST_STRIP)
    )
    return f'<ul class="trust-strip">{items}</ul>'

def cta_row(primary=("Get a Free Estimate", "/free-estimate/"), show_phone=True, on_dark=False):
    sec_cls = "btn-on-dark" if on_dark else "btn-phone"
    html = f'<div class="cta-row"><a class="btn btn-primary" href="{primary[1]}">{primary[0]}</a>'
    if show_phone and d.PHONE_E164:
        html += phone_link(cls=f"btn {sec_cls}")
    html += "</div>"
    return html

def photo_placeholder(label, tag="Photo placeholder", ratio=""):
    cls = f"photo-ph {ratio}".strip()
    return f'''<div class="{cls}">
      {icon("image")}
      <span class="ph-tag">{tag}</span>
      <span class="ph-label">{label}</span>
    </div>'''

def gallery_item(label, tag, service_url, area_url, categories, town):
    return f'''<figure class="gallery-figure card" data-service="{categories}" data-town="{town}">
    {photo_placeholder(label, tag, "ratio-4-3")}
    <figcaption>{label} &middot; <a href="{service_url}">{tag}</a> &middot; <a href="{area_url}">{town.replace('-', ' ').title()}</a></figcaption>
  </figure>'''

# ------------------------------------------------------- real photos ---

IMG_STEP_WIDTHS = [400, 800, 1200, 1600, 1920]

def project_picture(pid, sizes="(min-width: 1024px) 25vw, (min-width: 640px) 50vw, 100vw",
                     cls="", loading="lazy", fetchpriority=None):
    """<picture> with WebP + JPEG srcset for a real project photo. See data.PROJECTS."""
    p = d.project(pid)
    widths = sorted({w for w in IMG_STEP_WIDTHS if w <= p["max_w"]} | {p["max_w"]})
    base_url = f'/images/{p["folder"]}/{p["base"]}'
    webp_srcset = ", ".join(f'{base_url}-{w}.webp {w}w' for w in widths)
    jpg_srcset = ", ".join(f'{base_url}-{w}.jpg {w}w' for w in widths)
    default_w = widths[-1]
    fp_attr = f' fetchpriority="{fetchpriority}"' if fetchpriority else ""
    load_attr = "" if fetchpriority == "high" else f' loading="{loading}"'
    return f'''<picture>
      <source type="image/webp" srcset="{webp_srcset}" sizes="{sizes}">
      <img class="{cls}" src="{base_url}-{default_w}.jpg" srcset="{jpg_srcset}" sizes="{sizes}" width="{p['w']}" height="{p['h']}" alt="{p['alt']}"{load_attr}{fp_attr}>
    </picture>'''

def real_gallery_item(pid, caption_html, categories):
    p = d.project(pid)
    return f'''<figure class="gallery-figure card" data-service="{categories}">
    {project_picture(pid, cls="gallery-photo")}
    <figcaption>{caption_html}</figcaption>
  </figure>'''

def real_card(pid, title, url, desc):
    return f'''<article class="card">
    {project_picture(pid, cls="card-photo")}
    <div class="card-body">
      <h3><a href="{url}" class="card-link" style="color:inherit;text-decoration:none;">{title}</a></h3>
      <p>{desc}</p>
      <a class="card-link" href="{url}" aria-hidden="true">Learn more &rarr;</a>
    </div>
  </article>'''

def before_after_block(pair_key):
    pair = next(x for x in d.BEFORE_AFTER_PAIRS if x["key"] == pair_key)
    return f'''<figure class="before-after">
    <div class="ba-item"><span class="ba-label">Before</span>{project_picture(pair["before"], cls="ba-photo", sizes="(min-width: 768px) 50vw, 100vw")}</div>
    <div class="ba-item"><span class="ba-label">After</span>{project_picture(pair["after"], cls="ba-photo", sizes="(min-width: 768px) 50vw, 100vw")}</div>
    <figcaption>{pair["label"]}</figcaption>
  </figure>'''

def card(title, url, desc, tag="Project photo"):
    return f'''<article class="card">
    {photo_placeholder(title, tag)}
    <div class="card-body">
      <h3><a href="{url}" class="card-link" style="color:inherit;text-decoration:none;">{title}</a></h3>
      <p>{desc}</p>
      <a class="card-link" href="{url}" aria-hidden="true">Learn more &rarr;</a>
    </div>
  </article>'''

def map_embed(query=None, zoom=None, title="Map of our service area"):
    """Service-area map. No API key needed, and no street address is exposed —
    the map is centred on the service area, not on a property."""
    from urllib.parse import quote_plus
    q = quote_plus(query or d.MAP_QUERY)
    z = zoom or d.MAP_ZOOM
    return f'''<div class="map-embed">
      <iframe src="https://maps.google.com/maps?q={q}&z={z}&output=embed"
              title="{title}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
              allowfullscreen></iframe>
    </div>'''


def area_card(title, url, desc):
    """Town card with no photo. Deliberate: we have no photo confirmed to be in
    any given town, and a project photo on a town card reads as a claim that the
    job was there. A map-pin card looks finished and claims nothing."""
    town = title.split(",")[0]
    return f'''<article class="card area-card">
    <div class="card-body">
      <h3><a href="{url}" class="card-link">{icon("pin")}<span>{title}</span></a></h3>
      <p>{desc}</p>
      <a class="card-link" href="{url}" aria-hidden="true">Metal roofing in {town} &rarr;</a>
    </div>
  </article>'''


def steps_html(steps):
    items = []
    for i, (title, body) in enumerate(steps, start=1):
        items.append(f'<li><div class="step-num">{i}</div><h3>{title}</h3><p>{body}</p></li>')
    return f'<ol class="steps">{"".join(items)}</ol>'

def link_list(items, two_col=False):
    cls = "link-list two-col-links" if two_col else "link-list"
    lis = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in items)
    return f'<ul class="{cls}">{lis}</ul>'

# --------------------------------------------------------------- header ---

def _services_dropdown():
    links = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in d.SERVICES_NAV)
    return f'<ul class="dropdown">{links}<li><a class="view-all" href="/services/">View All Services &rarr;</a></li></ul>'

def _areas_dropdown():
    links = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in d.AREAS_NAV)
    return f'<ul class="dropdown">{links}<li><a class="view-all" href="/service-areas/">All Service Areas &rarr;</a></li></ul>'

def header_html():
    return f'''<header class="site-header" id="site-header">
    <div class="container header-inner">
      <a class="brand" href="/">
        <img class="brand-mark" src="/images/logo/metal-master-roof-mark-transparent.png" alt="" width="36" height="36">
        {d.BRAND}
      </a>
      <nav class="main-nav" aria-label="Primary">
        <ul>
          <li class="has-dropdown"><a class="nav-link" href="/services/">Services {icon("chevron")}</a>{_services_dropdown()}</li>
          <li class="has-dropdown"><a class="nav-link" href="/service-areas/">Service Areas {icon("chevron")}</a>{_areas_dropdown()}</li>
          <li><a class="nav-link" href="/gallery/">Gallery</a></li>
          <li><a class="nav-link" href="/about/">About</a></li>
          <li><a class="nav-link" href="/contact/">Contact</a></li>
        </ul>
      </nav>
      <div class="header-actions">
        {f'<a class="header-phone" href="tel:{d.PHONE_E164}">{icon("phone")}{phone_display()}</a>' if d.PHONE_E164 else ''}
        <a class="btn btn-primary" href="/free-estimate/">Free Estimate</a>
        <button class="hamburger" id="hamburger-btn" aria-expanded="false" aria-controls="mobile-drawer" aria-label="Open menu">
          {icon("menu")}
        </button>
      </div>
    </div>
  </header>
  <div class="mobile-drawer" id="mobile-drawer">
    <div class="mobile-drawer-head">
      <a class="brand" href="/">
        <img class="brand-mark" src="/images/logo/metal-master-roof-mark-transparent.png" alt="" width="36" height="36">{d.BRAND}
      </a>
      <button class="close-btn" id="drawer-close-btn" aria-label="Close menu">{icon("close")}</button>
    </div>
    <ul>
      <li><details><summary>Services {icon("chevron", "chevron")}</summary>
        <ul>{"".join(f'<li><a href="{u}">{n}</a></li>' for n, u in d.SERVICES_NAV + [("View All Services", "/services/")])}</ul>
      </details></li>
      <li><details><summary>Service Areas {icon("chevron", "chevron")}</summary>
        <ul>{"".join(f'<li><a href="{u}">{n}</a></li>' for n, u in d.AREAS_NAV + [("All Service Areas", "/service-areas/")])}</ul>
      </details></li>
      <li><a href="/gallery/">Gallery</a></li>
      <li><a href="/about/">About</a></li>
      <li><a href="/contact/">Contact</a></li>
      <li><a href="/free-estimate/">Free Estimate</a></li>
    </ul>
    {phone_link(cls="btn btn-secondary btn-block") or '<a class="btn btn-secondary btn-block" href="/free-estimate/">Get a Free Estimate</a>'}
  </div>'''

def mobile_cta_bar():
    # With no phone, this is a single full-width estimate button. The flex
    # children are `flex: 1 1 50%`, so a lone child grows to fill the pill.
    call = phone_link("Call Now", "call") if d.PHONE_E164 else ""
    return f'''<div class="mobile-cta-bar">
    {call}
    <a class="estimate" href="/free-estimate/">Get a Free Estimate</a>
  </div>'''

def footer_html():
    return f'''<footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <a class="brand" href="/" style="color:var(--white);margin-bottom:var(--space-3);">
          <img class="brand-mark" src="/images/logo/metal-master-roof-mark-transparent.png" alt="" width="36" height="36">{d.BRAND}
        </a>
        <p>{d.ONE_LINER}</p>
        <ul class="footer-contact">
          {"".join(f"<li>{item}</li>" for item in [
              phone_text_link(),
              email_text_link(),
              hours_text(),
              f'<a href="{d.FACEBOOK}">Facebook &rarr;</a>',
              '<a href="/free-estimate/">Request a free estimate &rarr;</a>',
          ] if item)}
        </ul>
        <p class="footer-license">{license_line()}</p>
      </div>
      <div>
        <h4>Services</h4>
        {link_list(d.FOOTER_SERVICES)}
      </div>
      <div>
        <h4>Service Areas</h4>
        {link_list(d.FOOTER_AREAS)}
      </div>
      <div>
        <h4>Company</h4>
        {link_list(d.FOOTER_COMPANY)}
      </div>
    </div>
    <div class="footer-bottom">
      &copy; {d.CURRENT_YEAR} {d.BRAND_FULL} &middot; Serving Tazewell County, Virginia and surrounding areas
    </div>
  </footer>'''

def dev_banner():
    return ('<div class="dev-banner">'
            '<strong>Development preview.</strong> Bracketed items like '
            '<span class="fact-ph" style="color:#F2C6AC;border-color:#F2C6AC;">[Business hours]</span> '
            'are placeholders — see <code>14-open-questions.md</code> for what the owner still needs to confirm.'
            '</div>')

# --------------------------------------------------------------- schema ---

def business_schema():
    towns = ["Bluefield|VA", "Richlands|VA", "Pounding Mill|VA", "Tazewell|VA",
             "Cedar Bluff|VA", "North Tazewell|VA", "Claypool Hill|VA", "Raven|VA"]
    area_served = [{"@type": "AdministrativeArea", "name": "Tazewell County, Virginia"}]
    for t in towns:
        name, region = t.split("|")
        area_served.append({"@type": "City", "name": name, "addressRegion": region})
    obj = {
        "@context": "https://schema.org",
        "@type": "RoofingContractor",
        "@id": f"https://{d.DOMAIN}/#business",
        "name": d.BRAND_FULL,
        "alternateName": d.BRAND,
        "url": f"https://{d.DOMAIN}/",
        "image": f"https://{d.DOMAIN}/images/og/og-default.jpg",
        "description": ("Metal roofing, metal siding, and board and batten installation for "
                         "residential and light commercial properties across Tazewell County, "
                         "Virginia. Family owned, licensed and insured. Free estimates."),
        "sameAs": [d.FACEBOOK],
        "areaServed": area_served,
        "slogan": "Free estimates. Licensed and insured. Local.",
    }
    if d.PHONE_E164:
        obj["telephone"] = d.PHONE_E164
    if d.EMAIL:
        obj["email"] = d.EMAIL
    return obj

def website_schema():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"https://{d.DOMAIN}/#website",
        "url": f"https://{d.DOMAIN}/",
        "name": d.BRAND_FULL,
        "inLanguage": "en-US",
    }

def service_schema(name, service_type, url, desc):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": service_type,
        "name": name,
        "description": desc,
        "provider": {"@id": f"https://{d.DOMAIN}/#business"},
        "url": f"https://{d.DOMAIN}{url}",
    }

def webpage_schema(name, url, desc):
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "url": f"https://{d.DOMAIN}{url}",
        "name": name,
        "description": desc,
        "about": {"@id": f"https://{d.DOMAIN}/#business"},
        "isPartOf": {"@id": f"https://{d.DOMAIN}/#website"},
    }

def schema_scripts(*schemas):
    out = []
    for s in schemas:
        if s:
            out.append(f'<script type="application/ld+json">{json.dumps(s)}</script>')
    return "\n  ".join(out)

# ---------------------------------------------------------------- layout --

def page(path, title, meta_desc, body, schemas=(), noindex=False, extra_head=""):
    canonical = f"https://{d.DOMAIN}{path}"
    robots = '<meta name="robots" content="noindex,follow">' if noindex else ""
    return f'''<!doctype html>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="{canonical}">
{robots}
<meta name="theme-color" content="#173B59">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{d.BRAND_FULL}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css?v={BUILD_VERSION}">
{schema_scripts(*schemas)}
{extra_head}
</head>
<body>
{dev_banner()}
{header_html()}
<main id="main">
{body}
</main>
{footer_html()}
{mobile_cta_bar()}
<script src="/js/main.js?v={BUILD_VERSION}" defer></script>
</body>
</html>'''
