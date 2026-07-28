# Site-wide facts and content. See ../../01-business-facts.md — source of truth.
# Every {{PLACEHOLDER}} here is an unconfirmed fact per 14-open-questions.md.
# Do NOT replace a placeholder with an invented value — replace it with the real one.

BRAND = "Metal Master Roofing"
BRAND_FULL = "Metal Master Roofing and Construction"
DOMAIN = "{{DOMAIN}}"                       # e.g. metalmasterroofingva.com
PHONE_DISPLAY = None                         # "(276) 555-0100" once confirmed
PHONE_E164 = None                            # "+12765550100" once confirmed
EMAIL = None                                 # leads@... once confirmed
HOURS = None                                 # "Mon–Fri, 8am–5pm" once confirmed
FACEBOOK = "https://www.facebook.com/people/Metal-Master-Roofing-and-Construction/61562911080390/"
VA_LICENSE_NUMBER = None
LICENSE_CLASS = None                          # likely Class B — unconfirmed
OWNER_NAME = None
YEAR_ESTABLISHED = None
SERVICE_RADIUS = None
PRICE_LOW = None
PRICE_HIGH = None
WORKMANSHIP_WARRANTY = None
RESPONSE_TIME = None
CURRENT_YEAR = 2026

ONE_LINER = "Metal roofing, metal siding, and board and batten for homes and small commercial buildings across Tazewell County, Virginia."
COMPANY_PARAGRAPH = (
    "Metal Master Roofing and Construction is a family-owned metal roofing and construction "
    "company working out of the Bluefield, Richlands, and Pounding Mill area of Tazewell "
    "County, Virginia. We install metal roofs, metal siding, and board and batten on homes, "
    "barns, shops, and small commercial buildings — residential work mostly, with commercial "
    "projects up to $150,000. Licensed, insured, and free estimates every time."
)
CEILING_LINE = (
    "We take on residential and light commercial projects up to $150,000 — the size where "
    "the owner is still on your roof, not managing it from an office."
)
SERVICE_AREA_SENTENCE = (
    "We work throughout Tazewell County — Bluefield, Richlands, Pounding Mill, Tazewell, "
    "Cedar Bluff, Claypool Hill, and everywhere between — plus parts of Mercer County, West Virginia."
)

TRUST_STRIP = ["Licensed & Insured", "Family Owned & Local", "Free Estimates", "Residential & Commercial"]

# --- Navigation -------------------------------------------------------

SERVICES_NAV = [
    ("Metal Roofing", "/services/metal-roofing/"),
    ("Standing Seam", "/services/standing-seam-metal-roofing/"),
    ("Board & Batten Siding", "/services/board-and-batten-metal-siding/"),
    ("Roof Replacement", "/services/metal-roof-replacement/"),
    ("Roof Repair", "/services/metal-roof-repair/"),
]
AREAS_NAV = [
    ("Bluefield, VA", "/service-areas/bluefield-va/"),
    ("Richlands, VA", "/service-areas/richlands-va/"),
    ("Pounding Mill, VA", "/service-areas/pounding-mill-va/"),
    ("Tazewell, VA", "/service-areas/tazewell-va/"),
]

FOOTER_SERVICES = SERVICES_NAV + [("All Services", "/services/")]
FOOTER_AREAS = AREAS_NAV + [("All Service Areas", "/service-areas/")]
FOOTER_COMPANY = [
    ("About", "/about/"),
    ("Gallery", "/gallery/"),
    ("Contact", "/contact/"),
    ("Free Estimate", "/free-estimate/"),
]

TOWNS_FOR_FORM = ["Bluefield, VA", "Richlands, VA", "Pounding Mill, VA", "Tazewell, VA",
                  "Cedar Bluff, VA", "Claypool Hill, VA", "North Tazewell, VA", "Other"]
SERVICE_NEEDS = ["Metal roof", "Roof repair", "Board & batten siding", "Metal siding",
                  "Pole barn / building", "Commercial", "Not sure yet"]

# --- Reusable FAQ pool (home) ------------------------------------------

# --- Real project photos (owner-exported from Facebook, 2026-07-28) ---
# Each has: id, folder ("hero"|"projects"), base filename (no width/ext —
# the build pipeline generated -{width}.jpg / -{width}.webp variants),
# native pixel size, max generated width, category, and alt text.
# Town is intentionally NOT claimed on any of these — see open question #8
# in 14-open-questions.md. The owner must confirm per-photo town before a
# photo is placed on a specific location page; until then these run on the
# home page and gallery only, captioned by material/color/type, not place.

PROJECTS = [
    dict(id="roof-green-standing-seam", folder="hero",
         base="standing-seam-metal-roof-brick-ranch-green-01",
         w=2048, h=1536, max_w=2048, category="roofing",
         alt="Green standing seam metal roof on a large brick ranch home, freshly completed"),

    dict(id="barn-door-repair", folder="projects",
         base="metal-panel-door-repair-barn-01",
         w=2048, h=1536, max_w=1600, category="repair",
         alt="New sage-green metal panel sliding door built into a weathered wood barn"),

    dict(id="carport-porch-01", folder="projects", base="carport-covered-porch-black-standing-seam-roof-01",
         w=2048, h=1536, max_w=1600, category="carport",
         alt="Black standing seam metal roof over a new covered carport and porch addition"),
    dict(id="carport-porch-02", folder="projects", base="carport-covered-porch-black-standing-seam-roof-02",
         w=2048, h=1536, max_w=1600, category="carport",
         alt="View from beneath a new covered porch framed in wood, black standing seam metal roof overhead"),
    dict(id="carport-porch-03", folder="projects", base="carport-covered-porch-black-standing-seam-roof-03",
         w=2048, h=1536, max_w=1600, category="carport",
         alt="Two-story home with a new black standing seam metal roof over the carport and porch addition"),
    dict(id="carport-porch-04", folder="projects", base="carport-covered-porch-black-standing-seam-roof-04",
         w=2048, h=1536, max_w=1600, category="carport",
         alt="Covered porch steps and black standing seam metal roofline on a home addition"),
    dict(id="carport-porch-05", folder="projects", base="carport-covered-porch-black-standing-seam-roof-05",
         w=2048, h=1536, max_w=1600, category="carport",
         alt="Wide covered deck with a black standing seam metal roof and mountain view"),

    dict(id="pole-barn-01", folder="projects", base="pole-barn-metal-building-cream-siding-01",
         w=2048, h=1536, max_w=1600, category="commercial",
         alt="Cream metal pole barn building with brown trim and open bay doors, mountain backdrop"),
    dict(id="pole-barn-02", folder="projects", base="pole-barn-metal-building-cream-siding-02",
         w=2048, h=1536, max_w=1600, category="commercial",
         alt="Cream metal pole barn with brown standing seam roof and two open garage bays"),

    dict(id="roof-siding-remodel", folder="projects", base="metal-roof-vertical-metal-siding-remodel-dark-green-01",
         w=2048, h=1536, max_w=1600, category="siding",
         alt="Dark green standing seam metal roof and vertical metal siding on a fully re-clad craftsman-style home"),

    dict(id="roof-pewter-before", folder="projects", base="metal-roof-replacement-before-worn-asphalt-shingle-01",
         w=2048, h=1536, max_w=1600, category="roofing",
         alt="Worn brown asphalt shingle roof with a tarp patch, before metal roof replacement",
         pair="pewter", pair_role="before"),
    dict(id="roof-pewter-after-01", folder="projects", base="metal-roof-replacement-after-pewter-standing-seam-02",
         w=2048, h=1536, max_w=1600, category="roofing",
         alt="Same home after replacement, with a new pewter-gray standing seam metal roof",
         pair="pewter", pair_role="after"),
    dict(id="roof-pewter-detail", folder="projects", base="standing-seam-metal-roof-chimney-flashing-detail-01",
         w=1536, h=2048, max_w=1200, category="roofing",
         alt="Close-up of custom-formed step flashing around a brick chimney on a standing seam metal roof"),

    dict(id="carport-bronze-01", folder="projects", base="custom-timber-frame-carport-bronze-standing-seam-01",
         w=2048, h=1536, max_w=1600, category="carport",
         alt="Large custom timber-frame carport with a bronze standing seam metal roof"),
    dict(id="carport-bronze-02", folder="projects", base="custom-timber-frame-carport-bronze-standing-seam-02",
         w=2048, h=1400, max_w=1600, category="carport",
         alt="Timber-frame carport and pavilion roofed in bronze standing seam metal, beside a pool"),
    dict(id="carport-bronze-underside", folder="projects", base="custom-timber-frame-carport-underside-detail-01",
         w=2048, h=1536, max_w=1600, category="carport",
         alt="Exposed tongue-and-groove wood ceiling and steel brackets under a custom carport roof"),
    dict(id="roof-eave-detail", folder="projects", base="standing-seam-metal-roof-eave-fascia-detail-01",
         w=1536, h=2048, max_w=1200, category="roofing",
         alt="Close-up of a standing seam metal roof eave and fascia corner on a brick home"),
    dict(id="awning-copper-01", folder="projects", base="copper-standing-seam-door-awning-detail-01",
         w=2048, h=1536, max_w=1600, category="carport",
         alt="Custom copper-toned standing seam metal awning built over French doors on a brick home"),
    dict(id="awning-copper-02", folder="projects", base="copper-standing-seam-door-awning-detail-02",
         w=1536, h=2048, max_w=1200, category="carport",
         alt="Close-up of a custom standing seam metal door-awning bracket on a brick home"),

    dict(id="roof-burgundy-before-01", folder="projects", base="metal-roof-replacement-before-worn-shingle-brick-ranch-01",
         w=2048, h=1536, max_w=1600, category="roofing",
         alt="Brick ranch home with a worn brown asphalt shingle roof, before metal roof replacement",
         pair="burgundy-a", pair_role="before"),
    dict(id="roof-burgundy-before-02", folder="projects", base="metal-roof-replacement-before-worn-shingle-brick-ranch-02",
         w=2048, h=1536, max_w=1600, category="roofing",
         alt="Same brick ranch home, worn asphalt shingle roof, porch-side view before replacement",
         pair="burgundy-a", pair_role="before"),
    dict(id="roof-burgundy-after-01", folder="projects", base="metal-roof-replacement-after-burgundy-standing-seam-01",
         w=2048, h=1536, max_w=1600, category="roofing",
         alt="Same brick ranch home with a new burgundy standing seam metal roof",
         pair="burgundy-a", pair_role="after"),

    dict(id="roof-burgundy-before-03", folder="projects", base="metal-roof-replacement-before-worn-shingle-brick-ranch-03",
         w=2048, h=1536, max_w=1600, category="roofing",
         alt="Brick home with a worn dark asphalt shingle roof, before metal roof replacement",
         pair="burgundy-b", pair_role="before"),
    dict(id="roof-burgundy-after-02", folder="projects", base="metal-roof-replacement-after-burgundy-standing-seam-02",
         w=2048, h=1536, max_w=1600, category="roofing",
         alt="Same brick home with a new burgundy standing seam metal roof, after replacement",
         pair="burgundy-b", pair_role="after"),

    dict(id="roof-tearoff-progress", folder="projects", base="metal-roof-installation-in-progress-tear-off-01",
         w=1536, h=2048, max_w=1200, category="roofing",
         alt="Crew mid-installation, tearing off old asphalt shingles and setting purlins ahead of a metal roof"),
]

BEFORE_AFTER_PAIRS = [
    dict(key="pewter", label="Worn Shingles to Pewter Standing Seam",
         before="roof-pewter-before", after="roof-pewter-after-01"),
    dict(key="burgundy-a", label="Worn Shingles to Burgundy Standing Seam",
         before="roof-burgundy-before-01", after="roof-burgundy-after-01"),
    dict(key="burgundy-b", label="Worn Shingles to Burgundy Standing Seam",
         before="roof-burgundy-before-03", after="roof-burgundy-after-02"),
]

_PROJECTS_BY_ID = {p["id"]: p for p in PROJECTS}

def project(pid):
    return _PROJECTS_BY_ID[pid]

def projects_by_category(cat):
    return [p for p in PROJECTS if p["category"] == cat]

HOME_FAQ = [
    ("How much does a metal roof cost around here?",
     "It depends on panel type, roof pitch, and how many valleys and penetrations you've got, "
     "but we'll give you a real range on the phone and an exact written number after we measure. "
     "We don't hide behind “it depends” — ask us."),
    ("Can you put a metal roof over my existing shingles?",
     "Often, yes — it depends on your local code, how many layers are already up there, and the "
     "condition of the decking underneath. We'll tell you straight during the estimate whether "
     "your roof is a candidate or whether a tear-off makes more sense."),
    ("How long does a metal roof last?",
     "A properly installed metal roof in this area typically runs 40 to 70 years, depending on "
     "the panel type and finish. That's two to three asphalt roofs in the same time."),
    ("Are metal roofs loud in the rain?",
     "Not on a house. The tin-roof-in-a-thunderstorm sound people remember comes from panels "
     "screwed onto open purlins with nothing underneath, like on an old barn. On a house with "
     "solid decking and underlayment, a metal roof is about as loud as shingles."),
    ("Do you do commercial work?",
     "Yes — smaller-scale commercial, up to $150,000. Churches, shops, storefronts, small "
     "offices, and farm buildings are all in our range."),
    ("How far do you travel?",
     "We're based in the Bluefield–Richlands–Pounding Mill area and work throughout Tazewell "
     "County and into nearby West Virginia. If you're not sure whether you're in range, call us."),
]
