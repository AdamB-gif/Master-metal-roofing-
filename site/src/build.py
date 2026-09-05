import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(__file__))
import data as d
import templates as t

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "dist")
PAGES = []  # (url, priority) for sitemap.xml


def write_page(url, html, priority="0.6"):
    if url == "/":
        target = os.path.join(OUT, "index.html")
    else:
        target = os.path.join(OUT, url.strip("/"), "index.html")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w") as f:
        f.write(html)
    if not url.startswith("/thank-you"):
        PAGES.append((url, priority))


def write_raw(rel_path, content):
    target = os.path.join(OUT, rel_path.lstrip("/"))
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w") as f:
        f.write(content)


# ======================================================================
# HOME
# ======================================================================

def build_home():
    url = "/"
    title = "Metal Roofing Tazewell County VA | Metal Master Roofing & Construction"
    desc = (f"Metal roofing, siding, and board & batten for homes and small commercial buildings "
            f"across Bluefield, Richlands, Pounding Mill & Tazewell County, VA. Family owned, "
            f"licensed & insured. Free estimates. {t.meta_call_cta()}")

    _hero_p = d.project("roof-green-standing-seam")
    _hero_url = f'/images/{_hero_p["folder"]}/{_hero_p["base"]}-{_hero_p["max_w"]}.jpg'
    hero_preload = (
        f'<link rel="preload" as="image" href="{_hero_url}" fetchpriority="high">'
    )
    hero = f'''<section class="hero has-photo" id="hero" style="--hero-photo-url:url('{_hero_url}');">
    <div class="container hero-inner">
      <h1>Metal Roofing in Tazewell County, Virginia</h1>
      <p class="lede">Metal roofs, metal siding, and board &amp; batten for homes and small
      commercial buildings across Bluefield, Richlands, Pounding Mill, and the surrounding area.
      Family owned. Licensed and insured. Free estimates, always.</p>
      {t.cta_row(on_dark=True)}
      {t.trust_strip_html()}
    </div>
  </section>'''

    services = f'''<section class="section-white" id="services-grid">
    <div class="container">
      <div class="section-head"><h2>What We Build</h2></div>
      <div class="grid grid-3">
        {t.real_card("roof-eave-detail", "Metal Roofing", "/services/metal-roofing/", "The roof that outlives the mortgage — standing seam or exposed fastener, built for these mountains.")}
        {t.real_card("roof-green-standing-seam", "Standing Seam", "/services/standing-seam-metal-roofing/", "Concealed fasteners, no exposed screws, and nothing on the surface to fail in twenty years.")}
        {t.real_card("roof-siding-remodel", "Board & Batten Siding", "/services/board-and-batten-metal-siding/", "The farmhouse look that's been on barns around here for two hundred years — now in steel.")}
        {t.real_card("roof-tearoff-progress", "Roof Replacement", "/services/metal-roof-replacement/", "From worn-out shingles to a metal roof, often without a full tear-off.")}
        {t.real_card("barn-door-repair", "Roof Repair", "/services/metal-roof-repair/", "Leaks, backed-out screws, flashing, and valley problems — diagnosed straight.")}
        {t.real_card("pole-barn-02", "Commercial", "/services/commercial-metal-roofing/", "Churches, shops, storefronts, and small offices — projects up to $150,000.")}
      </div>
      <p class="text-center" style="margin-top:var(--space-7);"><a class="btn btn-secondary" href="/services/">View All Services &rarr;</a></p>
    </div>
  </section>'''

    why = f'''<section class="section-tint" id="why">
    <div class="container">
      <div class="section-head"><h2>Why Neighbors Around Here Come to Us First</h2></div>
      <div class="grid grid-3">
        <div>
          <h3>Local, and it shows.</h3>
          <p>We live and work in Tazewell County. We know what a mountain winter does to a roof,
          how the wind comes across the ridges, and which colors hold up on a house that gets
          full afternoon sun. When we call you back, you're talking to somebody who's driven your road.</p>
        </div>
        <div>
          <h3>Licensed and insured.</h3>
          <p>{t.license_line()}. We'll hand you a certificate of insurance before we set a ladder
          against your house. Ask any contractor for both — if they hesitate, keep calling.</p>
        </div>
        <div>
          <h3>Free estimates, no pressure.</h3>
          <p>We come out, get on the roof, measure it right, and give you a written number.
          If you want to think about it for a month, think about it for a month. The estimate
          doesn't expire because we said so.</p>
        </div>
      </div>
    </div>
  </section>'''

    area = f'''<section class="section-white" id="area">
    <div class="container">
      <div class="split">
        <div>
          <h2>Where We Work</h2>
          <p>We're based in the Bluefield&ndash;Richlands&ndash;Pounding Mill area and work
          throughout Tazewell County and into nearby West Virginia. {("If you're within about " + d.SERVICE_RADIUS + ", we'll come look at it.") if d.SERVICE_RADIUS else "Not sure whether you're in range? Send the form and ask — it costs nothing."}</p>
          {t.link_list(d.AREAS_NAV + [("View All Service Areas", "/service-areas/")])}
        </div>
        {t.photo_placeholder("Service area map", "Map placeholder")}
      </div>
    </div>
  </section>'''

    recent = f'''<section class="section-tint" id="recent">
    <div class="container">
      <div class="section-head"><h2>Recent Projects</h2></div>
      <div class="grid grid-4">
        {t.real_gallery_item("bb-black-garage-01", "Board &amp; batten garage &middot; black", "siding")}
        {t.real_gallery_item("roof-charcoal-legacy-01", "Metal roof &middot; textured charcoal", "roofing")}
        {t.real_gallery_item("carport-24x24-01", "24&times;24 carport", "carport")}
        {t.real_gallery_item("roof-royal-red-01", "Metal roof &middot; royal red", "roofing")}
      </div>
      <p class="text-center" style="margin-top:var(--space-7);"><a class="btn btn-secondary" href="/gallery/">See the Full Gallery &rarr;</a></p>
    </div>
  </section>'''

    batten = f'''<section class="section-white" id="batten">
    <div class="container">
      <div class="split reverse">
        {t.project_picture("bb-green-house-01", sizes="(min-width: 1024px) 50vw, 100vw")}
        <div>
          <h2>Board &amp; Batten, Done in Metal</h2>
          <p>Board and batten gives you the vertical farmhouse-and-barn look that's been on
          buildings around here for two hundred years — but formed in steel, so it doesn't rot,
          doesn't need repainting every few years, and doesn't feed carpenter bees. It pairs
          naturally with a standing seam or exposed-fastener metal roof for a coherent,
          whole-building look. It's one of the things we do that most contractors in this
          area don't.</p>
          <a class="btn btn-secondary" href="/services/board-and-batten-metal-siding/">About Board &amp; Batten Siding &rarr;</a>
        </div>
      </div>
    </div>
  </section>'''

    process = f'''<section class="section-tint" id="process">
    <div class="container">
      <div class="section-head"><h2>How It Works</h2></div>
      {t.steps_html([
          ("Send the form", "Tell us where you are and what's going on with your roof."),
          ("We come measure", "We get on the roof, measure it properly, and look for anything you can't see from the ground."),
          ("Written estimate", "A real number, in writing. No expiration date, no pressure."),
          ("We build it", "Scheduled around your timeline, cleaned up when we're done."),
      ])}
    </div>
  </section>'''

    faq = f'''<section class="section-white" id="faq">
    <div class="container">
      <div class="section-head"><h2>Common Questions</h2></div>
      {t.faq_block(d.HOME_FAQ)}
    </div>
  </section>'''

    final_cta = f'''<section class="section-accent" id="final-cta">
    <div class="container text-center">
      <h2>Free Estimates in Tazewell County and Beyond</h2>
      <p style="max-width:60ch;margin:0 auto var(--space-6);">Send the form and we'll get back to you — the estimate
      is free and there's no pressure attached to it.</p>
      <div class="cta-row" style="justify-content:center;">
        {t.phone_link(cls="btn btn-on-dark")}
        <a class="btn" style="background:var(--navy-900);color:var(--white);" href="/free-estimate/">Request Your Free Estimate</a>
      </div>
    </div>
  </section>'''

    body = hero + services + why + area + recent + batten + process + faq + final_cta
    schemas = [t.business_schema(), t.website_schema(), t.faq_schema(d.HOME_FAQ)]
    write_page(url, t.page(url, title, desc, body, schemas, extra_head=hero_preload), priority="1.0")


# ======================================================================
# SERVICES HUB
# ======================================================================

def build_services_hub():
    url = "/services/"
    title = "Metal Roofing & Construction Services | Tazewell County, VA"
    desc = f"Metal roofing, siding, board & batten, and small commercial construction across Tazewell County, VA. {t.meta_call_cta()}"

    crumb = t.breadcrumb_html([("Home", "/"), ("Services", None)])
    hero = f'''<section class="hero hero-page">
    <div class="container hero-inner">
      <h1>Our Services</h1>
      <p class="lede">Metal roofing, metal siding, and board &amp; batten — residential mostly,
      with light commercial work up to $150,000. Every job starts with a free, honest estimate.</p>
    </div>
  </section>'''

    intro = f'''<section class="section-white">
    <div class="container prose">
      <p>We install metal roofs and metal siding on homes, barns, shops, and small commercial
      buildings across Tazewell County and the surrounding area. Most of what we do is
      residential — full roof replacements, repairs, and board &amp; batten siding — plus
      selected commercial jobs sized for an owner-operated crew rather than a big regional
      contractor. {d.CEILING_LINE} Whatever you're looking at, we'll tell you plainly whether
      it's a repair or a replacement, and what it's going to cost.</p>
    </div>
  </section>'''

    def group(title, items):
        cards = "".join(
            t.real_card(pid, n, u, s) if pid else t.card(n, u, s)
            for n, u, s, pid in items
        )
        return f'<h3>{title}</h3><div class="grid grid-3" style="margin-bottom:var(--space-8);">{cards}</div>'

    roofing = group("Roofing", [
        ("Metal Roofing", "/services/metal-roofing/", "Standing seam and exposed fastener installation across the county.", "roof-green-standing-seam"),
        ("Standing Seam", "/services/standing-seam-metal-roofing/", "Concealed fasteners, premium look, longest service life.", "roof-green-standing-seam"),
        ("Roof Replacement", "/services/metal-roof-replacement/", "Shingle tear-off or go-over, done right.", "roof-burgundy-after-01"),
        ("Roof Repair", "/services/metal-roof-repair/", "Leaks, screws, flashing, and valley problems.", "barn-door-repair"),
    ])
    siding = group("Siding", [
        ("Board & Batten Metal Siding", "/services/board-and-batten-metal-siding/", "Our specialty — the farmhouse look, in steel.", "roof-siding-remodel"),
    ])
    commercial = group("By Customer", [
        ("Commercial Metal Roofing", "/services/commercial-metal-roofing/", "Small commercial projects up to $150,000.", "pole-barn-01"),
    ])

    grid_section = f'''<section class="section-tint">
    <div class="container">
      {roofing}{siding}{commercial}
    </div>
  </section>'''

    cta = f'''<section class="section-accent text-center">
    <div class="container">
      <h2>Not sure what you need?</h2>
      <p>Tell us what's going on and we'll point you at the right service — or just come look at it.</p>
      <div class="cta-row" style="justify-content:center;">{t.phone_link(cls="btn btn-on-dark")}<a class="btn" style="background:var(--navy-900);color:var(--white);" href="/free-estimate/">Request a Free Estimate</a></div>
    </div>
  </section>'''

    body = crumb + hero + intro + grid_section + cta
    schemas = [t.webpage_schema(title, url, desc), t.breadcrumb_schema([("Home", "/"), ("Services", url)])]
    write_page(url, t.page(url, title, desc, body, schemas), priority="0.9")


# ======================================================================
# SERVICE PAGE TEMPLATE
# ======================================================================

def service_page(slug, title, meta, h1, service_type, quick_answer, sections, faq, words_note=""):
    url = f"/services/{slug}/"
    crumb = t.breadcrumb_html([("Home", "/"), ("Services", "/services/"), (h1, None)])
    hero = f'''<section class="hero hero-page">
    <div class="container hero-inner"><h1>{h1}</h1></div>
  </section>'''

    qa = f'''<section class="section-tint">
    <div class="container prose">
      <p class="text-large" style="border-left:4px solid var(--accent-600);padding-left:var(--space-5);"><strong>Quick answer:</strong> {quick_answer}</p>
    </div>
  </section>'''

    body_sections = ""
    for sec_title, sec_html in sections:
        body_sections += f'<section class="section-white"><div class="container prose">{f"<h2>{sec_title}</h2>" if sec_title else ""}{sec_html}</div></section>'

    towns_section = f'''<section class="section-tint">
    <div class="container">
      <h2>Where We Do This Work</h2>
      <p>{d.SERVICE_AREA_SENTENCE}</p>
      {t.link_list(d.AREAS_NAV, two_col=True)}
    </div>
  </section>'''

    related = f'''<section class="section-white">
    <div class="container">
      <h2>Related Services</h2>
      <div class="grid grid-3">
        {t.real_card("roof-green-standing-seam", "Metal Roofing", "/services/metal-roofing/", "The full picture on materials, cost, and process.")}
        {t.real_card("roof-siding-remodel", "Board & Batten Siding", "/services/board-and-batten-metal-siding/", "Pairs naturally with a new metal roof.")}
        {t.real_card("barn-door-repair", "Roof Repair", "/services/metal-roof-repair/", "Not sure if you need a repair or a replacement? Start here.")}
      </div>
    </div>
  </section>'''

    faq_section = f'''<section class="section-tint">
    <div class="container"><h2>FAQ</h2>{t.faq_block(faq)}</div>
  </section>'''

    cta = f'''<section class="section-accent text-center">
    <div class="container">
      <h2>Free Estimates, No Pressure</h2>
      <div class="cta-row" style="justify-content:center;">{t.phone_link(cls="btn btn-on-dark")}<a class="btn" style="background:var(--navy-900);color:var(--white);" href="/free-estimate/">Request a Free Estimate</a></div>
    </div>
  </section>'''

    body = crumb + hero + qa + body_sections + towns_section + related + faq_section + cta
    schemas = [
        t.service_schema(h1, service_type, url, meta),
        t.webpage_schema(title, url, meta),
        t.breadcrumb_schema([("Home", "/"), ("Services", "/services/"), (h1, url)]),
        t.faq_schema(faq),
    ]
    write_page(url, t.page(url, title, meta, body, schemas), priority="0.9")


def build_service_pages():
    # --- Metal Roofing (flagship) ---
    service_page(
        slug="metal-roofing",
        title="Metal Roofing Bluefield VA | Metal Roof Installation | Metal Master",
        meta=f"Metal roof installation across Bluefield, Richlands, Pounding Mill & Tazewell County VA. Standing seam & exposed fastener. Licensed, insured, free estimates. {t.meta_call_cta()}",
        h1="Metal Roofing in Bluefield, VA and Across Tazewell County",
        service_type="Metal Roof Installation",
        quick_answer=("A metal roof installed on a home in Tazewell County typically lasts 40 to "
                       "70 years, handles the snow and wind we get on these ridges better than "
                       "asphalt, and can often go on over your existing shingles. Most homes here "
                       "use either a standing seam panel or an exposed-fastener ag panel, "
                       "depending on budget and how the house is going to look."),
        sections=[
            ("Standing Seam vs. Exposed Fastener", '''<p>These are the two panel systems we install, and the honest difference between
                them is fasteners and price. <strong>Standing seam</strong> panels lock together with
                concealed clips under the seam — no screw holes through the surface, roughly double
                the upfront cost of exposed fastener, and the premium choice if you're staying in
                the house. <strong>Exposed fastener</strong> (ag panel / R-panel) is screwed directly
                through the panel face — about half the cost, a proven system on barns and budget
                rooflines, but the screws and washers need checking every several years and
                eventually re-driving. Read the full breakdown on our
                <a href="/services/standing-seam-metal-roofing/">standing seam</a> page. We'll walk
                you through both during your estimate and tell you which one makes sense for your
                roof and your budget — not just sell you the more expensive one.</p>'''),
            ("Gauges and Materials", '''<p>Panel thickness is measured in gauge — 29 gauge is the common
                residential standard, 26 gauge is heavier and holds up better to hail and foot
                traffic. Most panels are galvalume steel (an aluminum-zinc coating that resists rust
                better than plain galvanized) with a painted finish on top. Ask about the paint
                warranty specifically — it's usually separate from, and longer than, a general
                material warranty.</p>'''),
            ("Metal Over Existing Shingles", '''<p>Often, yes — code and manufacturer requirements
                permitting, and depending on how many layers of shingles are already up there and
                whether the decking underneath is sound. It saves the cost and mess of a tear-off.
                We'll check the decking and the layer count during your estimate and tell you
                straight whether your roof is a candidate. See our
                <a href="/services/metal-roof-replacement/">roof replacement</a> page for the
                tear-off-vs-go-over decision in detail.</p>'''),
            ("Snow and Ice in the Mountains", '''<p>This is where a lot of national roofing content
                falls flat — it's written for somewhere that doesn't get real winter. Metal panels
                shed snow off a steep pitch faster than shingles do, which is good for the roof and
                occasionally alarming for whoever's walking underneath — snow guards over doors and
                walkways are worth discussing on a steep metal roof. Standing seam's smooth surface
                and lack of surface fasteners also means less for ice to grab onto compared to a
                shingle roof or an exposed-fastener panel.</p>'''),
            ("Colors", f'''<p>We'll go over the color options actually available from our suppliers
                during your estimate — dark, weathered tones tend to suit the older housing stock
                around here, but it comes down to what you want on your house. See real installs in
                the <a href="/gallery/">gallery</a>.</p>'''),
            ("Warranty", f'''<p>{("Workmanship warranty: " + d.WORKMANSHIP_WARRANTY + ".") if d.WORKMANSHIP_WARRANTY else t.ph("Workmanship warranty length — to be confirmed")}
                Manufacturer paint and substrate warranties are separate and vary by product — we'll
                give you the actual paperwork, not just a verbal number.</p>'''),
        ],
        faq=[
            ("How much does a metal roof cost per square foot?",
             "It depends heavily on panel type, pitch, and complexity — standing seam runs roughly "
             "double exposed fastener installed. We'll give you a real range on the phone and an "
             "exact written number after measuring your roof."),
            ("How long does a metal roof last?",
             "Typically 40 to 70 years depending on panel type and finish — two to three asphalt "
             "roofs in the same span."),
            ("Can it go over my existing shingles?",
             "Often, yes, if the decking is sound and code allows it for your layer count. We check "
             "this at the estimate."),
            ("Are metal roofs loud in the rain?",
             "Not on a house with solid decking and underlayment. The loud-tin-roof sound comes from "
             "panels over open purlins, like on a barn."),
            ("Does metal attract lightning?",
             "No — that's a myth. Metal is also non-combustible, which is a genuine safety advantage "
             "over some other roofing materials."),
            ("Does a metal roof help resale value?",
             "Buyers in this area increasingly recognize metal as a durability upgrade, though exact "
             "resale impact varies by house and market."),
            ("How long does installation take?",
             "Depends on the size and complexity of the roof and the weather — we'll give you a "
             "realistic timeline before we start, not an optimistic one."),
        ],
    )

    # --- Standing Seam ---
    service_page(
        slug="standing-seam-metal-roofing",
        title="Standing Seam Metal Roof Installation | Southwest Virginia",
        meta=f"Standing seam metal roofing installation in Tazewell County VA. Concealed fasteners, premium durability. {t.meta_call_cta()}",
        h1="Standing Seam Metal Roofing",
        service_type="Standing Seam Metal Roof Installation",
        quick_answer=("Standing seam panels lock together with concealed clips hidden under the "
                       "raised seam, so there are no screw holes through the roof surface for water "
                       "to find in twenty years. It costs roughly double an exposed-fastener roof "
                       "up front, but over a 50-year horizon it's often the cheaper option because "
                       "there's no re-screwing to do."),
        sections=[
            ("Why Concealed Fasteners Matter", '''<p>Every screw through a roof surface is a
                potential leak point the moment its washer degrades. Standing seam avoids that
                entirely — panels interlock along a raised seam, and the clips holding them down are
                hidden underneath, never exposed to weather. That's the entire case for the extra
                cost: fewer places for water to get in, for longer.</p>'''),
            ("Snap-Lock vs. Mechanically Seamed", '''<p>Snap-lock panels click together by hand and
                are the more common, more affordable option for most homes. Mechanically seamed
                panels are crimped together with a seaming tool for an even tighter, lower-slope-
                capable seam — usually reserved for low-pitch roofs or higher-end installs. We'll
                recommend the right one for your roof's pitch.</p>'''),
            ("Panel Widths, Seam Heights, and Thermal Movement", '''<p>Panels are cut to the length
                of your roof plane and expand and contract with temperature swings — the clip system
                is designed to let that happen without stressing the panel or the seam. This is
                standard, engineered behavior, not a defect.</p>'''),
            ("Cost, Honestly", '''<p>Standing seam typically runs roughly double the installed cost of
                exposed-fastener panel. Over a 50-year horizon it often costs less overall, because
                you're not periodically chasing failed washers and re-screwing an entire roof. If
                budget is the deciding factor, see our
                <a href="/services/exposed-fastener-metal-roofing/">exposed fastener</a> page for the
                honest tradeoffs on that system instead.</p>'''),
        ],
        faq=[
            ("What does standing seam cost?", "Roughly double exposed-fastener panel installed — we'll give you an exact number after measuring."),
            ("Why is it more than screw-down panel?", "No exposed fasteners means no washers to fail and no screw holes to leak, which is worth paying for on a house you're keeping."),
            ("How long does it last?", "Commonly 50 years or more with proper installation and maintenance."),
            ("Is it for residential or commercial?", "Both — it's common on homes and works well on small commercial buildings too."),
            ("Can it go on a low-slope roof?", "Mechanically seamed panel systems can handle lower slopes than snap-lock — we'll assess your roof's pitch before recommending a system."),
        ],
    )

    # --- Board & Batten ---
    service_page(
        slug="board-and-batten-metal-siding",
        title="Board & Batten Metal Siding | Tazewell County VA | Metal Master",
        meta=f"Board and batten metal siding installation across southwest Virginia. The farmhouse look in steel — no rot, no repainting. {t.meta_call_cta()}",
        h1="Board & Batten Metal Siding",
        service_type="Board and Batten Metal Siding Installation",
        quick_answer=("Board and batten metal siding gives you the vertical farmhouse look — wide "
                       "panel faces with raised batten ribs — formed in steel instead of wood. Same "
                       "look that's been on barns and farmhouses around here for two hundred years, "
                       "without the rot, the insects, or the repainting every few years."),
        sections=[
            ("The Look, and Where It Came From", '''<p>Board and batten started as a practical barn
                and farmhouse siding — wide boards covering the wall, narrow battens covering the
                gaps between them. In Tazewell County that's not a design trend, it's what a lot of
                the buildings already look like. The metal version keeps the same visual rhythm —
                wide panel faces, raised batten ribs — with concealed fasteners and a steel
                substrate underneath.</p>'''),
            ("Metal vs. Wood vs. Vinyl", '''<p>Wood board and batten needs regular repainting or
                staining and is vulnerable to rot, insects, and woodpeckers. Vinyl is cheap and low-
                maintenance but can crack in real cold and fades over time. Metal costs more upfront
                than either, doesn't rot, doesn't feed carpenter bees, and holds its finish for
                decades under a quality paint system — the tradeoff is the initial price.</p>'''),
            ("Panel Details", '''<p>Panels are installed with concealed fasteners, in a range of face
                widths and batten profiles, over a standard housewrap and furring system. Gauge and
                finish options are the same family of products used on our roofing jobs, which is
                part of why the two pair so well visually and practically.</p>'''),
            ("Pairing With a Metal Roof", '''<p>Board and batten siding with a standing seam or
                exposed-fastener metal roof reads as one coherent, built-to-last exterior rather than
                two separate projects. It's the natural upsell when we're already doing your roof,
                and vice versa. See <a href="/services/metal-roofing/">metal roofing</a> for the roof
                side of that pairing.</p>'''),
            ("Where It Goes", '''<p>Houses, barns, shops, garages, gable accents, and small commercial
                storefronts. It reads equally well as a full-building treatment or as an accent on
                gables and dormers over a different primary siding.</p>'''),
        ],
        faq=[
            ("What is board and batten siding?", "A vertical siding profile with wide panel faces and raised battens covering the seams — traditionally wood, now available in steel."),
            ("How does metal compare to wood board and batten?", "Higher upfront cost, but no rot, no insect damage, and no repainting cycle — it holds its finish for decades."),
            ("What does it cost?", "We'll give you a real number after seeing the project — it depends on square footage, panel profile, and prep work needed."),
            ("Can it go over existing siding?", "Sometimes, depending on the condition of what's underneath — we'll assess this during your estimate."),
            ("How long does it last?", "Decades, with a quality paint finish and proper installation — it doesn't rot or degrade the way wood does."),
            ("Does it dent?", "Like any metal product it can dent under significant impact, but it holds up well to normal weather and everyday wear."),
        ],
    )

    # --- Replacement ---
    service_page(
        slug="metal-roof-replacement",
        title="Metal Roof Replacement | Shingle to Metal | Tazewell County VA",
        meta=f"Replacing an old shingle roof with metal in Tazewell County VA. Tear-off or go-over, done right, cleaned up. {t.meta_call_cta()}",
        h1="Roof Replacement — Shingles to Metal",
        service_type="Metal Roof Replacement",
        quick_answer=("Replacing an old shingle roof with metal usually means one of two paths: "
                       "tearing the old roof off down to the decking, or — if the decking is sound "
                       "and code allows it — installing metal panels directly over the existing "
                       "shingles. We'll tell you honestly which one your roof needs after we get up "
                       "there and look."),
        sections=[
            ("When to Replace vs. Repair", '''<p>If the damage is isolated — a few bad shingles, a
                flashing leak, storm damage to one section — repair is usually the right call. If the
                roof is old across the board, has widespread wear, or you're planning to be in the
                house a long time, replacement is where the money's better spent. We'll give you a
                straight answer either way, not just the bigger job.</p>'''),
            ("Tear-Off vs. Going Over", '''<p>A full tear-off gets you down to bare decking, lets us
                catch and fix any rot or damage underneath, and gives the cleanest install. Going
                over existing shingles (where the decking is sound and code allows it) saves time,
                mess, and cost. We'll check your roof and tell you which applies.</p>'''),
            ("What We Find Under Old Roofs", '''<p>Rotted decking, layered shingles from a previous
                go-over, and bad flashing around chimneys and valleys are the most common finds.
                We'll show you what we find and give you a clear number to fix it before we
                proceed — no surprise change orders after the fact.</p>'''),
            ("Timeline, Permits, and Cleanup", '''<p>We'll give you a realistic timeline up front,
                pull permits where required, and run a magnet sweep for stray nails and screws when
                we're done. Cleanup is part of the job, not an afterthought — a roof site should look
                like nobody worked there when we leave.</p>'''),
        ],
        faq=[
            ("How long does a roof replacement take?", "Depends on size and complexity — we'll give you a real timeline before we start."),
            ("Do I have to move out during the work?", "No — you can stay in the house during a typical residential re-roof."),
            ("What if the decking is bad underneath?", "We'll show you and give you a clear price to fix it before continuing — no surprises."),
            ("Can you go over my existing shingles?", "Sometimes — it depends on layer count, decking condition, and local code. We'll check."),
            ("Do you pull permits?", "Yes, where required for the scope of work."),
            ("How do you handle disposal?", "Old roofing material is hauled off, and we run a magnet sweep for nails before we leave."),
        ],
    )

    # --- Repair ---
    service_page(
        slug="metal-roof-repair",
        title="Metal Roof Repair & Leak Repair | Tazewell County VA",
        meta=f"Metal roof repair and leak diagnosis in Tazewell County VA. Honest repair-vs-replace advice. {t.meta_call_cta()}",
        h1="Metal Roof Repair",
        service_type="Metal Roof Repair",
        quick_answer=("Most metal roof leaks trace back to backed-out screws, degraded washers, "
                       "failed sealant at penetrations, or flashing and valley problems — not the "
                       "panels themselves. We diagnose it properly before we quote it, and we'll "
                       "tell you if repair is throwing money at a roof that needs replacing instead."),
        sections=[
            ("Common Failures", '''<p>Backed-out screws and degraded neoprene washers are the most
                common issue on exposed-fastener roofs. Failed sealant at pipe boots, vents, and
                other penetrations is another frequent leak source, along with flashing and valley
                problems and, occasionally, storm damage or dented panels.</p>'''),
            ("Repair or Replace", '''<p>If the roof is otherwise sound and the problem is isolated —
                a handful of fasteners, one bad flashing detail — repair is the right, cheaper answer.
                If a roof is old and failing broadly, repeated repairs start costing more than a
                replacement would have. We'll tell you honestly which situation you're in.</p>'''),
            ("Response Time", f'''<p>{("We aim to get back to you within " + d.RESPONSE_TIME + ".") if d.RESPONSE_TIME else t.ph("Typical response time — to be confirmed")}
                A leak doesn't wait for a convenient week, and neither should the callback.</p>'''),
        ],
        faq=[
            ("What does it cost to repair a leak?", "Depends on the cause and how many spots need attention — we'll quote it after diagnosing the actual problem."),
            ("Should I repair or replace?", "If the rest of the roof is sound, repair. If it's old and failing broadly, we'll tell you when replacement makes more financial sense."),
            ("Do exposed-fastener roofs need re-screwing eventually?", "Yes — washers degrade over years of sun and weather, and a fastener check-and-replace extends the roof's life."),
            ("Do you handle emergency repairs?", "Reach out and we'll do what we can to get to you promptly, especially for active leaks."),
            ("Will you repair another contractor's work?", "Yes — we diagnose and fix regardless of who originally installed the roof."),
        ],
    )


# ======================================================================
# SERVICE AREAS HUB
# ======================================================================

def build_areas_hub():
    url = "/service-areas/"
    title = "Service Areas | Metal Roofing Tazewell County VA & Beyond"
    desc = f"Where Metal Master Roofing works — Bluefield, Richlands, Pounding Mill, Tazewell, plus Wytheville and Abingdon. {t.meta_call_cta()}"

    crumb = t.breadcrumb_html([("Home", "/"), ("Service Areas", None)])
    hero = f'''<section class="hero hero-page">
    <div class="container hero-inner">
      <h1>Where We Work</h1>
      <p class="lede">We're based in the Bluefield&ndash;Richlands&ndash;Pounding Mill area and
      work throughout Tazewell County, Virginia{" and into nearby West Virginia" if False else ""}.</p>
    </div>
  </section>'''

    intro = f'''<section class="section-white">
    <div class="container prose">
      <p>{d.SERVICE_AREA_SENTENCE} {("Generally, if you're within " + d.SERVICE_RADIUS + " of Pounding Mill, we'll come take a look.") if d.SERVICE_RADIUS else "Not sure if you're in range? Send the form and ask — it costs nothing."}</p>
      {t.map_embed()}
    </div>
  </section>'''

    towns = f'''<section class="section-tint">
    <div class="container">
      <h2>Tazewell County, Virginia</h2>
      <div class="grid grid-4">
        {t.card("Bluefield, VA", "/service-areas/bluefield-va/", "Elevation, older neighborhoods, and the state line with WV.", "Location photo")}
        {t.card("Richlands, VA", "/service-areas/richlands-va/", "Clinch River valley, coal-era housing, a light-commercial corridor.", "Location photo")}
        {t.card("Pounding Mill, VA", "/service-areas/pounding-mill-va/", "Our home base — rural, agricultural, a lot of outbuildings.", "Location photo")}
        {t.card("Tazewell, VA", "/service-areas/tazewell-va/", "The county seat — historic homes and higher elevation.", "Location photo")}
      </div>
      <h2 style="margin-top:var(--space-8);">Along the I&#8209;81 Corridor</h2>
      <div class="grid grid-4">
        {t.card("Wytheville, VA", "/service-areas/wytheville-va/", "Wythe County seat, at the I&#8209;77 and I&#8209;81 crossroads.", "Location photo")}
        {t.card("Abingdon, VA", "/service-areas/abingdon-va/", "Washington County seat &mdash; historic district, higher elevation.", "Location photo")}
      </div>
    </div>
  </section>'''

    cta = f'''<section class="section-accent text-center">
    <div class="container"><h2>Not Sure If We Cover Your Area?</h2>
      <div class="cta-row" style="justify-content:center;">{t.phone_link(cls="btn btn-on-dark")}<a class="btn" style="background:var(--navy-900);color:var(--white);" href="/free-estimate/">Request a Free Estimate</a></div>
    </div>
  </section>'''

    body = crumb + hero + intro + towns + cta
    schemas = [t.webpage_schema(title, url, desc), t.breadcrumb_schema([("Home", "/"), ("Service Areas", url)])]
    write_page(url, t.page(url, title, desc, body, schemas), priority="0.9")


# ======================================================================
# LOCATION PAGE TEMPLATE
# ======================================================================

def location_page(slug, town, state, intro_html, quick_answer, why_local, faq, nearby):
    url = f"/service-areas/{slug}/"
    h1 = f"Metal Roofing in {town}, {state}"
    title = f"Metal Roofing {town}, {state} | Metal Roofs & Siding | Metal Master Roofing"
    meta = f"Metal roofing, siding & board and batten in {town}, {state}. Local, family owned, licensed & insured. Free estimates. {t.meta_call_cta()}"

    crumb = t.breadcrumb_html([("Home", "/"), ("Service Areas", "/service-areas/"), (f"{town}, {state}", None)])
    hero = f'''<section class="hero hero-page">
    <div class="container hero-inner"><h1>{h1}</h1></div>
  </section>'''

    intro = f'''<section class="section-white">
    <div class="container prose">{intro_html}</div>
  </section>'''

    qa = f'''<section class="section-tint">
    <div class="container prose">
      <p class="text-large" style="border-left:4px solid var(--accent-600);padding-left:var(--space-5);"><strong>Quick answer:</strong> {quick_answer}</p>
    </div>
  </section>'''

    services_here = f'''<section class="section-white">
    <div class="container">
      <h2>Services in {town}</h2>
      <div class="grid grid-3">
        {t.card("Metal Roofing", "/services/metal-roofing/", f"Standing seam and exposed fastener installation for homes in {town}.")}
        {t.card("Board & Batten Siding", "/services/board-and-batten-metal-siding/", "The farmhouse look, in steel, for houses and outbuildings.")}
        {t.card("Roof Repair", "/services/metal-roof-repair/", "Leak diagnosis and honest repair-vs-replace advice.")}
      </div>
    </div>
  </section>'''

    local_projects = f'''<section class="section-tint">
    <div class="container">
      <h2>Local Projects</h2>
      <div class="grid grid-2">
        {t.gallery_item(f"Metal roof project", f"{town}, {state}", "/services/metal-roofing/", url, "roofing", slug)}
        {t.gallery_item(f"Siding or repair project", f"{town}, {state}", "/services/board-and-batten-metal-siding/", url, "siding", slug)}
      </div>
      <p class="text-small" style="margin-top:var(--space-4);color:var(--steel-600);">Photo gallery for this town is growing as jobs are tagged — see the <a href="/gallery/">full gallery</a> for current work.</p>
    </div>
  </section>'''

    why_section = f'''<section class="section-white">
    <div class="container prose">
      <h2>Why Local Matters Here</h2>
      {why_local}
    </div>
  </section>'''

    nearby_section = f'''<section class="section-tint">
    <div class="container">
      <h2>Nearby Areas</h2>
      {t.link_list(nearby, two_col=True)}
      <p style="margin-top:var(--space-5);"><a href="/service-areas/">All Service Areas &rarr;</a></p>
    </div>
  </section>'''

    faq_section = f'''<section class="section-white">
    <div class="container"><h2>Local FAQ</h2>{t.faq_block(faq)}</div>
  </section>'''

    cta = f'''<section class="section-accent text-center">
    <div class="container">
      <h2>Free Estimates in {town}, {state}</h2>
      <div class="cta-row" style="justify-content:center;">{t.phone_link(cls="btn btn-on-dark")}<a class="btn" style="background:var(--navy-900);color:var(--white);" href="/free-estimate/">Request a Free Estimate</a></div>
    </div>
  </section>'''

    body = crumb + hero + intro + qa + services_here + local_projects + why_section + nearby_section + faq_section + cta
    schemas = [
        t.webpage_schema(title, url, meta),
        t.breadcrumb_schema([("Home", "/"), ("Service Areas", "/service-areas/"), (f"{town}, {state}", url)]),
        t.faq_schema(faq),
    ]
    write_page(url, t.page(url, title, meta, body, schemas), priority="0.85")


def build_location_pages():
    location_page(
        slug="bluefield-va", town="Bluefield", state="VA",
        intro_html='''<p>Bluefield sits up at elevation on the Virginia side of the state line — the
            higher ground here means it runs noticeably cooler and gets more snow than lower parts
            of the county, part of why it's known locally as the "Nature's Air Conditioned City."
            That elevation and snow load matter when you're picking a roofing system: it's exactly
            the kind of roof our steep-slope metal panels and snow-shedding standing seam are built
            for. We work on a mix of older established neighborhoods and newer construction
            throughout Bluefield, and because plenty of residents work and shop across the state
            line, we serve <a href="/service-areas/bluefield-wv/">Bluefield, WV</a> as well — two
            different towns, same name, and we're clear about which is which.</p>
            <p>We install metal roofing, metal siding, and board &amp; batten on homes throughout
            Bluefield, from established in-town streets to newer construction on the outskirts.
            Send the form for a free, no-pressure estimate.</p>''',
        quick_answer=("Bluefield's elevation means colder winters and more snow than lower parts of "
                       "the county — a real argument for a metal roof's snow-shedding surface and "
                       "long service life over asphalt that wears faster under freeze-thaw cycles."),
        why_local='''<p>Higher elevation changes the math on a roof here: more snow load, more
            freeze-thaw cycling on aging shingles, and colder average temperatures than towns just a
            few hundred feet lower in the valley. Standing seam's smooth, fastener-free surface sheds
            snow cleanly instead of holding it against the panel the way shingles or an
            open-fastener roof can. Bluefield's mix of older in-town housing and newer builds also
            means we see a real range of roof conditions — from decades-old decking that needs a real
            look before anything goes back on, to newer homes where a straightforward install is all
            that's needed.</p>''',
        faq=[
            ("Do you serve both Bluefield, VA and Bluefield, WV?", "Yes — we work both sides of the state line. See our Bluefield, WV page for that side specifically."),
            ("Does Bluefield's elevation affect roofing choices?", "Yes — colder temperatures and more snow make a metal roof's durability and snow-shedding surface a stronger fit than in lower, milder parts of the county."),
            ("How far is Bluefield from your other service areas?", "Close — we're regularly in Bluefield, Richlands, Pounding Mill, and Tazewell, all within the same general drive."),
            ("Do you work on older Bluefield homes?", "Yes — we regularly assess older decking and roof structures before recommending a repair or full replacement."),
        ],
        nearby=[("Bluefield, WV", "/service-areas/bluefield-wv/"), ("Pocahontas, VA", "/service-areas/tazewell-county-va/"),
                ("Tazewell, VA", "/service-areas/tazewell-va/"), ("Richlands, VA", "/service-areas/richlands-va/")],
    )

    location_page(
        slug="richlands-va", town="Richlands", state="VA",
        intro_html='''<p>Richlands sits down in the Clinch River valley, and that changes what a roof
            goes through. Fog settles in the low ground most mornings, the river keeps humidity up,
            and a lot of the older housing around town — built during the coal years — was never put
            up with a fifty-year roof in mind. We install metal roofing and board and batten siding
            on homes throughout Richlands, from brick ranches in town to farmhouses out past the
            edge of it. Richlands' hospital and commercial corridor also make it one of our better
            spots for small commercial work.</p>
            <p>We're about twenty minutes up the road in Pounding Mill, so we're in Richlands
            constantly. If you want somebody to look at your roof and tell you straight whether it
            needs replacing or just needs work, send us the form. The estimate's free either way.</p>''',
        quick_answer=("Richlands' river-valley humidity and fog put extra wear on older, coal-era "
                       "roofs faster than drier parts of the county — a metal roof and rust-resistant "
                       "galvalume coating hold up better against that moisture over the long run."),
        why_local='''<p>The Clinch River corridor keeps humidity and morning fog higher in Richlands
            than in the ridge towns nearby, and that moisture is hard on aging fasteners, flashing,
            and shingle roofs left past their service life. A lot of the town's housing stock dates
            to the coal era, alongside newer mid-century ranches, which means we regularly find
            decking and flashing details that need real attention before a new roof goes back on —
            we'll tell you what we find. Richlands' commercial corridor near the hospital also gives
            us a steady run of small commercial and storefront roofing work.</p>''',
        faq=[
            ("Does the river valley affect roofing in Richlands?", "Yes — higher humidity and morning fog are harder on aging roofs than in higher, drier parts of the county, which is part of why we check decking condition closely here."),
            ("Do you work on older coal-era homes in Richlands?", "Regularly — a lot of Richlands housing dates to that era, and we know what to look for underneath."),
            ("Do you do commercial work near the hospital corridor?", "Yes — small commercial and storefront roofing up to $150,000."),
            ("How far is Richlands from your home base?", "About twenty minutes from Pounding Mill — we're in Richlands constantly."),
        ],
        nearby=[("Cedar Bluff, VA", "/service-areas/cedar-bluff-va/" if False else "/service-areas/"), ("Pounding Mill, VA", "/service-areas/pounding-mill-va/"),
                ("Tazewell, VA", "/service-areas/tazewell-va/"), ("Bluefield, VA", "/service-areas/bluefield-va/")],
    )

    location_page(
        slug="pounding-mill-va", town="Pounding Mill", state="VA",
        intro_html='''<p>Pounding Mill is our home base — this is where we live and work, not just a
            town we drive to. It's a small, unincorporated community along the Route 460 corridor,
            more rural and agricultural than Richlands or Tazewell, with a lot of barns, shops,
            outbuildings, and farmhouses spread across the surrounding land. That's the natural
            territory for ag-panel and exposed-fastener metal roofing, pole-barn and outbuilding
            roofs, and board &amp; batten siding on both houses and barns.</p>
            <p>Because we're based right here, Pounding Mill gets the fastest response time and the
            most day-to-day attention of anywhere we work. Send the form — there's a good chance we're
            already close by.</p>''',
        quick_answer=("Pounding Mill's rural, agricultural land is the territory ag-panel metal "
                       "roofing and pole-barn buildings were built for — durable, affordable, and "
                       "proven on outbuildings and farmhouses alike."),
        why_local='''<p>This is farm and outbuilding country — barns, shops, equipment sheds, and
            farmhouses spread out along Route 460 and the surrounding rural roads, rather than the
            tighter in-town lots you get in Richlands or Tazewell. That means more exposed-fastener
            and ag-panel roofing, more pole-barn and post-frame work, and board &amp; batten siding
            that suits both the house and the outbuildings on the same property. Being based here
            means we're not driving in from somewhere else — we know the roads, the properties, and
            often the people.</p>''',
        faq=[
            ("Is Pounding Mill really where you're based?", "Yes — this is our home base, not just a service area."),
            ("Do you do pole barns and outbuildings here?", "Yes — it's a natural fit for the rural, agricultural properties around Pounding Mill."),
            ("What roofing works best for barns and outbuildings?", "Exposed-fastener ag panel is the common, cost-effective choice — we'll walk you through the tradeoffs against standing seam."),
            ("How fast can you respond in Pounding Mill?", "Faster than almost anywhere else we work, since we're right here."),
        ],
        nearby=[("Claypool Hill, VA", "/service-areas/"), ("Cedar Bluff, VA", "/service-areas/"),
                ("Tazewell, VA", "/service-areas/tazewell-va/"), ("Richlands, VA", "/service-areas/richlands-va/")],
    )

    location_page(
        slug="tazewell-va", town="Tazewell", state="VA",
        intro_html='''<p>Tazewell is the county seat, with a historic downtown and courthouse area
            where a lot of the housing stock is older and roof appearance genuinely matters —
            homeowners here often want a roof that looks right on a historic-style house, which is a
            real argument for standing seam's clean, traditional profile over an ag-panel look.
            Tazewell also sits at higher elevation, with real snow load most winters, and Burke's
            Garden — a distinctive high-elevation bowl known for severe weather — is nearby.</p>
            <p>We install metal roofing, siding, and board &amp; batten throughout Tazewell, from the
            homes near the courthouse to newer construction on the edges of town. Free estimates,
            no pressure.</p>''',
        quick_answer=("Tazewell's higher elevation brings real snow load most winters, and its "
                       "historic downtown housing stock often calls for standing seam's traditional, "
                       "clean profile over a more agricultural exposed-fastener look."),
        why_local='''<p>The historic homes near the courthouse mean roof appearance is often as much
            a factor as durability — standing seam's traditional, low-profile look tends to suit
            older architecture better than an ag-panel roof does. Tazewell's elevation also brings
            heavier snow most winters than lower parts of the county, and nearby Burke's Garden — a
            high-elevation bowl known locally for severe weather — is a reminder of how quickly
            conditions change with elevation here. We factor pitch, snow load, and the look of the
            house into every recommendation in Tazewell.</p>''',
        faq=[
            ("Do you work on historic homes near the courthouse?", "Yes — and we'll talk through which roofing profile looks right on an older house, not just what's cheapest."),
            ("Does Tazewell get more snow than other towns you serve?", "Generally yes, given the elevation — it's a factor in what we recommend."),
            ("Do you serve Burke's Garden?", "It's within our general area — send the form to confirm for your specific location."),
            ("What roofing profile suits a historic-style home?", "Standing seam's clean, traditional look is usually the better fit over an ag-panel profile."),
        ],
        nearby=[("North Tazewell, VA", "/service-areas/"), ("Claypool Hill, VA", "/service-areas/"),
                ("Bluefield, VA", "/service-areas/bluefield-va/"), ("Richlands, VA", "/service-areas/richlands-va/")],
    )

    location_page(
        slug="wytheville-va", town="Wytheville", state="VA",
        intro_html='''<p>Wytheville sits where I&#8209;77 and I&#8209;81 cross, up around 2,200 feet in
            Wythe County. That elevation means real snow most winters and a lot of freeze&ndash;thaw
            cycling &mdash; the kind of repeated expansion and contraction that finds every weak
            fastener and every tired shingle on a roof. It's exactly the argument for metal: a
            standing seam roof sheds snow off a smooth, fastener-free surface, and its concealed
            clips let the panel move with temperature instead of working screws loose.</p>
            <p>We install metal roofing, metal siding, and board &amp; batten on homes, barns, and
            small commercial buildings in and around Wytheville. The interstate crossroads brings a
            fair amount of storefront and small commercial property with it, and that's work we take
            on too &mdash; projects up to $150,000. Send the form for a free estimate and we'll confirm
            scheduling for your address.</p>''',
        quick_answer=("Wytheville's elevation brings real snow and heavy freeze\u2013thaw cycling most "
                       "winters \u2014 conditions that wear out asphalt shingles and back out exposed "
                       "screws faster than they do in milder, lower country."),
        why_local='''<p>Two things shape roofing here. First, elevation: at roughly 2,200 feet,
            Wytheville gets more snow and more freeze&ndash;thaw cycling than lower ground, and that
            cycling is what loosens fasteners and lifts shingle tabs over time. Standing seam's
            concealed clips let panels expand and contract without fighting the fastener, which is
            why we lean toward it on exposed, higher-elevation roofs. Second, the land: Wythe County
            has a lot of open farm ground, and open ground means wind. Panel gauge, fastening
            pattern, and edge-metal detail matter more on a roof with nothing upwind of it than they
            do on a sheltered in-town lot &mdash; and edge detail is where a cheap roof fails
            first.</p>''',
        faq=[
            ("Do you travel to Wytheville?", "Yes \u2014 Wytheville is within the area we serve. Send the form and we'll confirm scheduling for your address."),
            ("Does Wytheville's elevation change what roof you'd recommend?", "It pushes us toward standing seam on most homes \u2014 concealed fasteners and a smooth, snow-shedding surface hold up better through repeated freeze\u2013thaw cycles."),
            ("Do you do commercial work in Wytheville?", "Yes \u2014 storefronts, shops, and small offices, on projects up to $150,000."),
            ("Do you do barns and outbuildings out in Wythe County?", "Yes \u2014 pole barns, equipment sheds, and ag-panel roofing are regular work for us."),
        ],
        nearby=[("Abingdon, VA", "/service-areas/abingdon-va/"), ("Tazewell, VA", "/service-areas/tazewell-va/"),
                ("Bluefield, VA", "/service-areas/bluefield-va/"), ("Richlands, VA", "/service-areas/richlands-va/")],
    )

    location_page(
        slug="abingdon-va", town="Abingdon", state="VA",
        intro_html='''<p>Abingdon is the Washington County seat, and its historic district &mdash; the
            Main Street blocks around the Barter Theatre and the head of the Virginia Creeper Trail
            &mdash; is one of the better-preserved in southwest Virginia. That matters for roofing:
            on a house where the architecture is the point, the profile and color of the roof are
            part of the decision, not an afterthought. Standing seam's clean, traditional lines
            usually sit better on an older home than an agricultural exposed-fastener panel does.
            Exterior changes within a designated historic district can also be subject to local
            review, so it's worth checking with the town before you settle on a color.</p>
            <p>We install metal roofing, metal siding, and board &amp; batten throughout Abingdon
            &mdash; historic homes near downtown, newer construction on the edges, and the barns and
            outbuildings on the farms around it. Free estimates, and we'll tell you straight what
            your roof actually needs.</p>''',
        quick_answer=("On Abingdon's older and historic-district homes, roof appearance carries real "
                       "weight \u2014 standing seam's clean, traditional profile suits that architecture "
                       "better than an agricultural exposed-fastener look, and exterior changes in the "
                       "district may need local review first."),
        why_local='''<p>Abingdon's housing stock runs older than most of what we see, and an older
            house is rarely a straight tear-off-and-replace. Decking condition, existing flashing,
            chimney and dormer details, and how the eave and rake were originally built all change
            what a proper metal roof install looks like &mdash; and we'd rather find that during the
            estimate than halfway through the job. Appearance carries more weight here too: on a
            house in or near the historic district, panel profile, seam spacing, and color are part
            of the decision, not just durability. Outside town, Washington County is farm country,
            which means barns, equipment sheds, and pole buildings where an exposed-fastener ag
            panel is the sensible, cost-effective choice. We do both, and we'll tell you which one
            your building calls for.</p>''',
        faq=[
            ("Do you travel to Abingdon?", "Yes \u2014 Abingdon is within the area we serve. Send the form and we'll confirm scheduling for your address."),
            ("Can I put a metal roof on a home in the historic district?", "Often yes, but exterior changes in a designated historic district can require local review \u2014 check with the town first, and we'll work with whatever profile and color get approved."),
            ("What roof profile suits an older Abingdon home?", "Standing seam, usually \u2014 its clean, traditional lines suit older architecture better than an agricultural exposed-fastener panel."),
            ("Do you do barns and farm buildings around Washington County?", "Yes \u2014 pole barns, equipment sheds, and ag-panel roofing, alongside our residential work."),
        ],
        nearby=[("Wytheville, VA", "/service-areas/wytheville-va/"), ("Tazewell, VA", "/service-areas/tazewell-va/"),
                ("Bluefield, VA", "/service-areas/bluefield-va/"), ("Richlands, VA", "/service-areas/richlands-va/")],
    )


# ======================================================================
# ABOUT
# ======================================================================

def build_about():
    url = "/about/"
    title = "About Metal Master Roofing | Family Owned, Tazewell County VA"
    desc = f"Family-owned metal roofing contractor based in Tazewell County, VA. Licensed, insured, and honest about what we do and don't do. {t.meta_call_cta()}"

    crumb = t.breadcrumb_html([("Home", "/"), ("About", None)])
    hero = f'''<section class="hero hero-page"><div class="container hero-inner"><h1>About Metal Master Roofing &amp; Construction</h1></div></section>'''

    story = f'''<section class="section-white">
    <div class="container">
      <div class="split">
        <div class="prose">
          <h2>Our Story</h2>
          <p><em>{t.ph("Owner's real story goes here")} — this section is written from a real
          interview with the owner, not invented. See <code>14-open-questions.md</code> question
          set: how they got into metal roofing, how long they've been at it, the job they're
          proudest of, and what they wish homeowners knew before calling anybody. A real, specific
          origin story in the owner's own words is worth more than any polished marketing copy —
          and it's the one thing a national lead-generation competitor structurally cannot
          produce.</em></p>
        </div>
        {t.photo_placeholder("Owner on a jobsite", "Owner photo")}
      </div>
    </div>
  </section>'''

    licensed = f'''<section class="section-tint">
    <div class="container prose">
      <h2>Licensed &amp; Insured</h2>
      <p>Virginia contractor license {d.VA_LICENSE_NUMBER or t.ph("license number")}, class
      {d.LICENSE_CLASS or t.ph("license class")}. We carry general liability
      {"and workers' compensation" if True else ""} and can provide a certificate of insurance
      before we set a ladder against your house. You're welcome to verify our license directly
      through Virginia DPOR — we'd rather you check than just take our word for it.</p>
    </div>
  </section>'''

    scope = f'''<section class="section-white">
    <div class="container prose">
      <h2>What We Do — and Don't</h2>
      <p>{d.CEILING_LINE} We install metal roofing, metal siding, and board &amp; batten on homes,
      barns, shops, and small commercial buildings. We don't take on large-scale commercial roofing
      or projects outside that range — if that's what you need, we'll tell you plainly rather than
      take the job anyway.</p>
    </div>
  </section>'''

    area = f'''<section class="section-tint">
    <div class="container">
      <h2>Service Area</h2>
      <p>{d.SERVICE_AREA_SENTENCE}</p>
      {t.link_list(d.AREAS_NAV + [("All Service Areas", "/service-areas/")])}
    </div>
  </section>'''

    cta = f'''<section class="section-accent text-center">
    <div class="container"><h2>Talk to Us</h2>
    <div class="cta-row" style="justify-content:center;">{t.phone_link(cls="btn btn-on-dark")}<a class="btn" style="background:var(--navy-900);color:var(--white);" href="/free-estimate/">Request a Free Estimate</a></div>
    </div>
  </section>'''

    body = crumb + hero + story + licensed + scope + area + cta
    schemas = [t.webpage_schema(title, url, desc), t.breadcrumb_schema([("Home", "/"), ("About", url)])]
    write_page(url, t.page(url, title, desc, body, schemas), priority="0.8")


# ======================================================================
# GALLERY
# ======================================================================

def build_gallery():
    url = "/gallery/"
    title = "Metal Roofing Photo Gallery | Projects in Tazewell County VA"
    desc = f"Real metal roofing, siding, and carport projects across Tazewell County, VA — including before-and-after roof replacements. {t.meta_call_cta()}"

    crumb = t.breadcrumb_html([("Home", "/"), ("Gallery", None)])
    hero = f'''<section class="hero hero-page"><div class="container hero-inner">
      <h1>Our Work</h1>
      <p class="lede">Real jobs, real photos — no stock. Towns aren't tagged on these yet; we're
      confirming that with the owner job by job, so for now everything is captioned by material
      and color instead of place.</p>
    </div></section>'''

    before_after = f'''<section class="section-white">
    <div class="container">
      <div class="section-head"><h2>Before &amp; After</h2><p>The most convincing photo in any roofing gallery — same house, same angle, before the tear-off and after the last panel goes on.</p></div>
      <div class="before-after-grid">
        {t.before_after_block("pewter")}
        {t.before_after_block("burgundy-a")}
        {t.before_after_block("burgundy-b")}
        {t.before_after_block("charcoal")}
      </div>
    </div>
  </section>'''

    # Individual gallery items, excluding the ones already shown above in the before/after section.
    _shown = {p["id"] for pair in d.BEFORE_AFTER_PAIRS for p in
              (d.project(pair["before"]), d.project(pair["after"]))}
    _shown |= {p["id"] for p in d.PROJECTS if p["folder"] == "hero"}
    _caption_by_category = {
        "roofing": "Metal roof",
        "siding": "Metal roof &amp; siding",
        "carport": "Carport / covered porch",
        "commercial": "Pole barn / commercial",
        "repair": "Repair",
    }
    grid_items = "".join(
        t.real_gallery_item(p["id"], _caption_by_category.get(p["category"], "Project"), p["category"])
        for p in d.PROJECTS if p["id"] not in _shown
    )

    filters = ["all", "roofing", "siding", "carport", "commercial", "repair"]
    filter_bar = '<div class="filter-bar" role="group" aria-label="Filter gallery by type">' + "".join(
        f'<button class="filter-btn{" is-active" if f == "all" else ""}" data-filter="{f}">{f.title()}</button>' for f in filters
    ) + "</div>"

    gallery = f'''<section class="section-tint">
    <div class="container">
      <div class="section-head"><h2>All Projects</h2></div>
      {filter_bar}
      <div class="grid grid-4" id="gallery-grid">{grid_items}</div>
    </div>
  </section>'''

    cta = f'''<section class="section-accent text-center">
    <div class="container"><h2>Like What You See?</h2>
    <div class="cta-row" style="justify-content:center;">{t.phone_link(cls="btn btn-on-dark")}<a class="btn" style="background:var(--navy-900);color:var(--white);" href="/free-estimate/">Request a Free Estimate</a></div>
    </div>
  </section>'''

    body = crumb + hero + before_after + gallery + cta
    schemas = [t.webpage_schema(title, url, desc), t.breadcrumb_schema([("Home", "/"), ("Gallery", url)])]
    write_page(url, t.page(url, title, desc, body, schemas), priority="0.8")


# ======================================================================
# CONTACT
# ======================================================================

def build_contact():
    url = "/contact/"
    title = "Contact Metal Master Roofing | Bluefield & Richlands VA"
    desc = f"Get in touch with Metal Master Roofing and Construction — Tazewell County, VA. {t.meta_call_cta()}"

    crumb = t.breadcrumb_html([("Home", "/"), ("Contact", None)])
    hero = f'''<section class="hero hero-page"><div class="container hero-inner"><h1>Get in Touch</h1></div></section>'''

    left = f'''<div>
      <h2>Contact Us</h2>
      <p>The form is the way to reach us. It comes straight through, and we'll get back to
      you with a real answer rather than a runaround. Tell us what's going on with your roof
      and where you are, and we'll take it from there.</p>
      <p><strong>Hours:</strong> {t.hours_text()}</p>
      <p><strong>Response time:</strong> {("We typically call back within " + d.RESPONSE_TIME + ".") if d.RESPONSE_TIME else t.ph("Response time — to be confirmed")}</p>
      <p><a href="{d.FACEBOOK}">Find us on Facebook &rarr;</a></p>
      <p>{d.SERVICE_AREA_SENTENCE}</p>
    </div>'''

    right = form_html(compact=True)

    layout = f'''<section class="section-white">
    <div class="container">
      <div class="split">{left}<div class="card-form">{right}</div></div>
    </div>
  </section>'''

    map_section = f'''<section class="section-tint">
    <div class="container">
      <div class="section-head"><h2>Where We Work</h2>
      <p>We come to you — there's no storefront or showroom to visit. Here's the area we cover.</p></div>
      {t.map_embed()}
      <p class="text-center" style="margin-top:var(--space-5);"><a href="/service-areas/">See every town we serve &rarr;</a></p>
    </div>
  </section>'''

    body = crumb + hero + layout + map_section
    schemas = [t.webpage_schema(title, url, desc), t.breadcrumb_schema([("Home", "/"), ("Contact", url)])]
    write_page(url, t.page(url, title, desc, body, schemas), priority="0.7")


# ======================================================================
# FORM (shared between /contact/ and /free-estimate/)
# ======================================================================

def form_html(compact=False):
    town_opts = "".join(f'<option>{tn}</option>' for tn in d.TOWNS_FOR_FORM)
    need_opts = "".join(f'<option>{s}</option>' for s in d.SERVICE_NEEDS)
    heading = "" if compact else "<h2>Request Your Free Estimate</h2>"
    action = d.FORM_ENDPOINT if d.FORM_ACCESS_KEY else "#"
    hidden = ""
    if d.FORM_ACCESS_KEY:
        hidden = (f'<input type="hidden" name="access_key" value="{d.FORM_ACCESS_KEY}">'
                  f'<input type="hidden" name="subject" value="New estimate request — {d.BRAND} website">'
                  f'<input type="hidden" name="from_name" value="{d.BRAND} website">')
    return f'''<form id="estimate-form" novalidate action="{action}" method="post" data-live="{"1" if d.FORM_ACCESS_KEY else "0"}">
    {heading}
    {hidden}
    <div class="honeypot-field" aria-hidden="true">
      <label for="company_website">Company Website</label>
      <input type="text" id="company_website" name="company_website" tabindex="-1" autocomplete="off">
    </div>
    <input type="hidden" name="form_rendered_at" id="form_rendered_at" value="">
    <div class="field">
      <label for="f-name">Name <span class="req">*</span></label>
      <input type="text" id="f-name" name="name" required autocomplete="name">
      <p class="field-error">{t.icon("check")} Please enter your name.</p>
    </div>
    <div class="field">
      <label for="f-phone">Phone <span class="req">*</span></label>
      <input type="tel" id="f-phone" name="phone" inputmode="tel" required autocomplete="tel">
      <p class="field-error">{t.icon("check")} Please enter a phone number.</p>
    </div>
    <div class="field">
      <label for="f-email">Email</label>
      <input type="email" id="f-email" name="email" autocomplete="email">
    </div>
    <div class="field">
      <label for="f-town">Town <span class="req">*</span></label>
      <select id="f-town" name="town" required>
        <option value="" disabled selected>Select your town</option>
        {town_opts}
      </select>
      <p class="field-error">{t.icon("check")} Please select your town.</p>
    </div>
    <div class="field">
      <label for="f-need">What do you need? <span class="req">*</span></label>
      <select id="f-need" name="service_needed" required>
        <option value="" disabled selected>Select one</option>
        {need_opts}
      </select>
      <p class="field-error">{t.icon("check")} Please select what you need.</p>
    </div>
    <div class="field">
      <label for="f-message">Tell us about it</label>
      <textarea id="f-message" name="message"></textarea>
    </div>
    <button type="submit" class="btn btn-primary btn-block">Get My Free Estimate</button>
    <div class="form-status" id="form-status" role="alert" aria-live="polite"></div>
    {f'<p class="form-note">Would rather just talk? {t.phone_text_link()}.</p>' if d.PHONE_E164 else ''}
  </form>'''


# ======================================================================
# FREE ESTIMATE
# ======================================================================

def build_free_estimate():
    url = "/free-estimate/"
    title = "Free Metal Roof Estimate | Tazewell County VA | Metal Master Roofing"
    desc = f"Get a free, no-pressure estimate on a metal roof, siding, or board and batten. Licensed & insured, family owned, serving Tazewell County VA. {t.meta_call_cta()}"

    crumb = t.breadcrumb_html([("Home", "/"), ("Free Estimate", None)])
    hero = f'''<section class="hero hero-page"><div class="container hero-inner"><h1>Get Your Free Estimate</h1></div></section>'''

    whats_next = f'''<div>
      <h2>What Happens Next</h2>
      {t.steps_html([
          ("You send the form.", "Takes about a minute, and it comes straight to us."),
          (f"We call you back{(' within ' + d.RESPONSE_TIME) if d.RESPONSE_TIME else ''}.", "To set a time that works for you."),
          ("We come out and measure.", "Properly, on the roof — not guessed from the driveway."),
          ("You get a written estimate.", "No pressure, no expiration date, no salesman camped out in your living room."),
      ])}
      {t.trust_strip_html()}
    </div>'''

    layout = f'''<section class="section-white">
    <div class="container">
      <div class="split">
        <div class="card-form">{form_html()}</div>
        {whats_next}
      </div>
    </div>
  </section>'''

    faq = [
        ("Is the estimate really free?", "Yes. Always. No strings attached."),
        ("Do I have to be home?", (d.RESPONSE_TIME and "Usually yes for the walkthrough — we'll confirm when we schedule.") or "Usually yes for the walkthrough, so we can talk through what we find — we'll confirm details when we schedule."),
        ("How long does it take to get an estimate?", "We'll give you a specific window when we schedule the visit — it depends on our current schedule and your location."),
    ]

    faq_section = f'''<section class="section-tint">
    <div class="container"><h2>Estimate FAQ</h2>{t.faq_block(faq)}</div>
  </section>'''

    fallback = f'''<section class="section-accent text-center">
    <div class="container"><h2>Would Rather Just Talk?</h2>
      {t.phone_link(cls="btn btn-on-dark")}
    </div>
  </section>'''

    body = crumb + hero + layout + faq_section + fallback
    schemas = [t.webpage_schema(title, url, desc), t.breadcrumb_schema([("Home", "/"), ("Free Estimate", url)]), t.faq_schema(faq)]
    write_page(url, t.page(url, title, desc, body, schemas), priority="1.0")


# ======================================================================
# THANK YOU / 404
# ======================================================================

def build_thank_you():
    url = "/thank-you/"
    title = "Thank You | Metal Master Roofing"
    desc = "Your estimate request was received."
    crumb = ""
    body_html = f'''<section class="hero hero-page"><div class="container hero-inner text-center" style="width:100%;">
      <h1>Thanks — We Got It</h1>
      <p class="lede" style="margin:0 auto;">{("We'll call you back within " + d.RESPONSE_TIME + ".") if d.RESPONSE_TIME else "We'll call you back soon."}
      Need us sooner? {t.phone_link(cls="btn btn-on-dark")}</p>
      <p style="margin-top:var(--space-6);"><a class="btn btn-secondary" style="background:transparent;border-color:white;color:white;" href="/gallery/">See Our Work While You Wait &rarr;</a></p>
    </div></section>'''
    write_page(url, t.page(url, title, desc, body_html, [], noindex=True))


def build_404():
    body_html = f'''<section class="hero hero-page"><div class="container hero-inner text-center" style="width:100%;">
      <h1>Page Not Found</h1>
      <p class="lede" style="margin:0 auto;">That page doesn't exist. Try the homepage, or request a free estimate.</p>
      <div class="cta-row" style="justify-content:center;margin-top:var(--space-6);">
        <a class="btn btn-on-dark" href="/">Back to Homepage</a>
        {t.phone_link(cls="btn btn-on-dark")}
      </div>
    </div></section>'''
    html = t.page("/404/", "Page Not Found | Metal Master Roofing", "Page not found.", body_html, [], noindex=True)
    write_raw("404.html", html)


# ======================================================================
# TECHNICAL FILES
# ======================================================================


def build_robots():
    write_raw("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /thank-you/\n\nSitemap: https://{d.DOMAIN}/sitemap.xml\n")


def build_sitemap():
    urls = []
    for url, priority in PAGES:
        loc = f"https://{d.DOMAIN}{url}"
        urls.append(f"  <url><loc>{loc}</loc><priority>{priority}</priority></url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(urls) + "\n</urlset>\n")
    write_raw("sitemap.xml", xml)


def build_js():
    js = r'''(function () {
  "use strict";

  // Header shadow on scroll
  var header = document.getElementById("site-header");
  function onScroll() {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 4);
  }
  document.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Mobile drawer
  var hamburger = document.getElementById("hamburger-btn");
  var drawer = document.getElementById("mobile-drawer");
  var closeBtn = document.getElementById("drawer-close-btn");
  function openDrawer() {
    drawer.classList.add("is-open");
    hamburger.setAttribute("aria-expanded", "true");
    document.body.style.overflow = "hidden";
  }
  function closeDrawer() {
    drawer.classList.remove("is-open");
    hamburger.setAttribute("aria-expanded", "false");
    document.body.style.overflow = "";
  }
  if (hamburger && drawer) {
    hamburger.addEventListener("click", openDrawer);
    closeBtn && closeBtn.addEventListener("click", closeDrawer);
    drawer.addEventListener("click", function (e) {
      if (e.target.tagName === "A") closeDrawer();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeDrawer();
    });
  }

  // Gallery filter (does not remove items from the DOM/crawlers — just hides visually)
  var filterBtns = document.querySelectorAll(".filter-btn");
  var galleryGrid = document.getElementById("gallery-grid");
  if (filterBtns.length && galleryGrid) {
    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterBtns.forEach(function (b) { b.classList.remove("is-active"); });
        btn.classList.add("is-active");
        var filter = btn.getAttribute("data-filter");
        galleryGrid.querySelectorAll("[data-service]").forEach(function (item) {
          var match = filter === "all" || item.getAttribute("data-service") === filter;
          item.style.display = match ? "" : "none";
        });
      });
    });
  }

  // Phone / email click tracking (fires a dataLayer event if analytics is present later)
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href^='tel:'], a[href^='mailto:']");
    if (!a) return;
    var eventName = a.href.indexOf("tel:") === 0 ? "phone_click" : "email_click";
    if (window.dataLayer) window.dataLayer.push({ event: eventName });
  });

  // Estimate / contact form: honeypot + time-trap + inline validation
  document.querySelectorAll("#estimate-form").forEach(function (form) {
    var renderedAt = Date.now ? Date.now() : new Date().getTime();
    var renderedField = form.querySelector("#form_rendered_at");
    if (renderedField) renderedField.value = String(renderedAt);

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector("#form-status");
      var honeypot = form.querySelector("#company_website");

      // Spam checks
      if (honeypot && honeypot.value) {
        return; // silently discard
      }
      var elapsed = (Date.now ? Date.now() : new Date().getTime()) - renderedAt;
      if (elapsed < 3000) {
        return; // silently discard — submitted too fast to be human
      }

      // Inline validation
      var valid = true;
      form.querySelectorAll("[required]").forEach(function (field) {
        var wrapper = field.closest(".field");
        var ok = field.value && field.value.trim().length > 0;
        if (wrapper) wrapper.classList.toggle("has-error", !ok);
        if (!ok) valid = false;
      });
      if (!valid) {
        if (status) {
          status.textContent = "Please fill in the required fields above.";
          status.className = "form-status error is-visible";
        }
        return;
      }

      // Delivery goes live only once FORM_ACCESS_KEY is set in data.py.
      if (form.getAttribute("data-live") !== "1") {
        if (status) {
          status.textContent = "This preview form isn't connected to a live inbox yet.";
          status.className = "form-status success is-visible";
        }
        return;
      }

      var btn = form.querySelector("button[type=submit]");
      if (btn) { btn.disabled = true; btn.textContent = "Sending..."; }
      if (status) {
        status.textContent = "Sending...";
        status.className = "form-status is-visible";
      }
      fetch(form.action, {
        method: "POST",
        headers: { "Accept": "application/json" },
        body: new FormData(form)
      }).then(function (res) {
        if (!res.ok) throw new Error("Request failed");
        window.location.href = "/thank-you/";
      }).catch(function () {
        // Never silently drop a lead: keep what they typed, point them at the phone.
        if (btn) { btn.disabled = false; btn.textContent = "Get My Free Estimate"; }
        var hp = document.querySelector(".header-phone");
        if (status) {
          status.textContent = hp
            ? "Something went wrong sending that. Please call us instead on " + hp.textContent.trim() + "."
            : "Something went wrong sending that. Please try again in a moment, or message us on Facebook.";
          status.className = "form-status error is-visible";
        }
      });
    });

    form.querySelectorAll("[required]").forEach(function (field) {
      field.addEventListener("blur", function () {
        var wrapper = field.closest(".field");
        var ok = field.value && field.value.trim().length > 0;
        if (wrapper) wrapper.classList.toggle("has-error", !ok);
      });
    });
  });
})();
'''
    write_raw("js/main.js", js)


# ======================================================================

def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    # Copy hand-written static assets (css, images) into the build output
    static_dir = os.path.join(ROOT, "static")
    for name in os.listdir(static_dir):
        src = os.path.join(static_dir, name)
        dst = os.path.join(OUT, name)
        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)

    build_home()
    build_services_hub()
    build_service_pages()
    build_areas_hub()
    build_location_pages()
    build_about()
    build_gallery()
    build_contact()
    build_free_estimate()
    build_thank_you()
    build_404()
    build_robots()
    build_sitemap()
    build_js()

    print(f"Built {len(PAGES)} indexable pages to {OUT}")


if __name__ == "__main__":
    main()
