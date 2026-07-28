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
