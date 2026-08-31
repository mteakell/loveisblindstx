"""Convert the cloned Georgia pages into Texas pages.

Swaps the chrome for the TX partials, regenerates JSON-LD from schema.py so no
Georgia entity survives, and maps the remaining Georgia body copy to Texas.
"""
import glob, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import schema as S

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BIZ = json.load(open("data/tx.json"))["business"]
HEAD = open("build/partials/header.html").read()
FOOT = open("build/partials/footer.html").read()
HEAD_INNER = HEAD.split("<body", 1)[1].split(">", 1)[1]

TEXT = [
 ("info@loveisblindsga.com", "access@loveisblindstx.com"),
 ("info@loveisblindstx.com", "access@loveisblindstx.com"),
 ("Love Is Blinds Georgia", "Love Is Blinds Texas"),
 ("loveisblindsga.com", "loveisblindstx.com"),
 ("North Georgia", "Texas"),
 ("Georgia", "Texas"),
 ("owned and operated in Texas", "owned and operated in Texas"),
 ("Ben and Ashley Honeycutt", "our local team"),
 ("Ben &amp; Ashley Honeycutt", "our local team"),
 ("Ben &amp; Ashley", "our local team"),
 ("Ben and Ashley", "our local team"),
 ("the Honeycutts", "our owners"),
 ("Honeycutt", ""),
 ("within a two-hour radius of Dalton", "across DFW, North Texas, East Texas, Waco and the Austin metro"),
 ("Free in-home consultations within 2 hours of Dalton",
  "Free in-home consultations across North, East and Central Texas"),
 ("Serving Texas from Dalton, GA", "Serving Texas from Fort Worth, TX"),
 ("Dalton, GA", "Fort Worth, TX"),
 ("Chattanooga, TN", "Dallas, TX"),
 ("Chattanooga", "Dallas"),
 ("Dalton", "Fort Worth"),
 ("(706) 406-6653", BIZ["phone"]), ("7064066653", "8665182999"),
 ("+17064066653", BIZ["tel"]), ("866-515-1562", "866-518-2999"),
 ("(866) 515-1562", BIZ["phone"]), ("8665151562", "8665182999"),
 ("info@loveisblindsga.com", BIZ["email"]),
 ("/service-areas/", "/"), ("/service-areas", "/areas-we-serve"),
 ("&mdash;", ","), ("—", ","),
]

def strip_ld(s):
    return re.sub(r'<script type="application/ld\+json">.*?</script>\s*', "", s, flags=re.S)

def swap_chrome(s):
    """Replace the Georgia header and footer with the Texas partials."""
    s = re.sub(r"<body[^>]*>.*?</header>", lambda m: "<body>" + HEAD_INNER, s, flags=re.S)
    s = re.sub(r"<footer.*?</html>", lambda m: FOOT, s, flags=re.S)
    return s

def detext(s):
    for a, b in TEXT:
        s = s.replace(a, b)
    s = re.sub(r"<li class=\"contact-line\"><a href=\"https://business\.daltonchamber\.org.*?</li>",
               "", s, flags=re.S)
    s = re.sub(r"\s{2,}", " ", s)
    return s

def meta_of(s, name):
    m = re.search(rf'<meta name="{name}" content="(.*?)">', s, re.S)
    return html.unescape(m.group(1)) if m else ""

def title_of(s):
    m = re.search(r"<title>(.*?)</title>", s, re.S)
    return html.unescape(m.group(1)) if m else ""

def rewrite_head(s, url, title, desc, nodes):
    """Rebuild every head tag that carries a URL, title or description."""
    e = lambda x: html.escape(x, quote=True)
    s = re.sub(r"<title>.*?</title>", lambda m: f"<title>{e(title)}</title>", s, flags=re.S)
    s = re.sub(r'<meta name="description" content=".*?">',
               lambda m: f'<meta name="description" content="{e(desc)}">', s, flags=re.S)
    s = re.sub(r'<link rel="canonical" href=".*?">',
               lambda m: f'<link rel="canonical" href="{S.SITE}{url}">', s, flags=re.S)
    for p, v in [("og:title", title), ("og:description", desc), ("og:url", S.SITE + url),
                 ("og:site_name", BIZ["name"])]:
        s = re.sub(rf'<meta property="{p}" content=".*?">',
                   lambda m, p=p, v=v: f'<meta property="{p}" content="{e(v)}">', s, flags=re.S)
    for p, v in [("twitter:title", title), ("twitter:description", desc)]:
        s = re.sub(rf'<meta name="{p}" content=".*?">',
                   lambda m, p=p, v=v: f'<meta name="{p}" content="{e(v)}">', s, flags=re.S)
    s = s.replace("</head>", S.render(nodes) + "\n</head>")
    return s

# ------------------------------------------------------------------ manifest
PRODUCT_COPY = {
 "blinds": ("Custom Blinds in Texas | Wood & Faux Wood Blinds", "Real wood, faux wood and composite blinds, custom measured to your openings and installed by our own team across Texas.", ["Real Wood Blinds","Faux Wood Blinds","Composite Blinds","Vertical Blinds"]),
 "shades": ("Custom Window Shades in Texas | Roller & Cellular", "Roller, solar, cellular, Roman and woven wood shades chosen for Texas light and heat. Free in-home measure and installation.", ["Roller Shades","Solar Shades","Cellular Shades","Roman Shades","Woven Wood Shades"]),
 "shutters": ("Custom Shutters in Texas | Interior Window Shutters", "Interior shutters built to the window opening rather than trimmed to fit. Free in-home consultation and professional installation.", ["Plantation Shutters","Composite Shutters","Wood Shutters"]),
 "plantation-shutters": ("Plantation Shutters in Texas | Custom Built & Installed", "Louvered plantation shutters custom built to each opening and professionally installed across DFW, North, East and Central Texas.", ["Wood Plantation Shutters","Composite Plantation Shutters"]),
 "real-wood-blinds": ("Real Wood Blinds in Texas | Custom Hardwood Blinds", "Hardwood blinds in stains and paints matched to your trim, custom measured and installed. Free in-home consultation.", None),
 "faux-wood-blinds": ("Faux Wood Blinds in Texas | Moisture Resistant", "Moisture-resistant faux wood blinds for baths, kitchens and sun-heavy rooms. Custom measured and professionally installed.", None),
 "roller-shades": ("Roller Shades in Texas | Solar & Blackout Roller Shades", "Solar screen and blackout roller shades in a range of openness factors, measured to your openings and installed by our team.", None),
 "honeycomb-shades": ("Honeycomb Shades in Texas | Cellular Shades", "Cellular honeycomb shades that slow heat transfer at the glass, which matters most on west-facing Texas windows.", None),
 "dual-shades": ("Dual Shades in Texas | Day and Night Zebra Shades", "Day and night dual shades that switch between filtered light and privacy in one treatment. Free in-home measure.", None),
 "panel-track-shades": ("Panel Track Shades in Texas | Sliding Door Shades", "Sliding panel track shades for wide openings and patio doors, custom measured and professionally installed.", None),
 "woven-wood-shades": ("Woven Wood Shades in Texas | Bamboo & Natural Shades", "Bamboo, reed and grass weave shades with optional privacy liners, custom measured and installed across Texas.", None),
 "energy-efficient-custom-window-shades": ("Energy Efficient Window Shades in Texas", "Shades chosen for heat gain, glare and west-facing exposure, so the rooms that cook in August stop cooking. Free measure.", None),
 "motorized-window-treatment-automations": ("Motorized Shades & Blinds in Texas | Smart Control", "Motorized shades and blinds with app, remote and voice control. Battery, hardwired and solar charged options, professionally installed.", ["App Control","Voice Control","Scheduled Scenes","Hardwired Motors"]),
 "window-treatment-automations": ("Window Treatment Automation in Texas | Smart Shades", "Scheduling, scenes and smart home integration for your blinds and shades, set up by the team that installs them.", None),
 "remote-window-treatments": ("Remote Control Blinds & Shades in Texas", "Handheld and wall-mounted remote control for shades and blinds, fitted and programmed at installation.", None),
}
SERVICE_COPY = {
 "blinds-installation": ("Blinds Installation in Texas", "Professional blinds installation across Texas, measured and fitted by our own team."),
 "blinds-solutions": ("Blinds Solutions in Texas", "Help choosing the right blinds for light, privacy and heat in each room."),
 "shades-installation": ("Shades Installation in Texas", "Professional shade installation, measured and fitted by our own team."),
 "shades-solutions": ("Shades Solutions in Texas", "Shade recommendations matched to window orientation and room use."),
 "shutters-installation": ("Shutter Installation in Texas", "Plantation shutter installation, built to the opening and fitted on site."),
 "shutter-solutions": ("Shutter Solutions in Texas", "Shutter configurations for bays, arches, sliders and tall windows."),
 "drapery-installation": ("Drapery Installation in Texas", "Drapery, hardware and layered treatments measured and hung by our team."),
 "window-treatment-installation": ("Window Treatment Installation in Texas", "Full installation service for blinds, shades, shutters and drapery."),
 "window-treatment-solutions": ("Window Treatment Solutions in Texas", "A free in-home consultation that ends in a written, measured quote."),
}
CORE = {
 "index.html": ("/", "Custom Blinds, Shades & Shutters in Texas | Love Is Blinds",
   "Custom blinds, shades and plantation shutters across DFW, North Texas, East Texas, Waco and Austin. Free in-home consultation. Call (866) 518-2999."),
 "about.html": ("/about", "About Love Is Blinds Texas | Custom Window Treatments",
   "Three local franchises covering DFW, North Texas, East Texas, Waco and the Austin metro. We measure, order and install every job ourselves."),
 "contact.html": ("/contact", "Contact Love Is Blinds Texas | Free In-Home Consultation",
   "Book a free in-home window treatment consultation anywhere in our Texas service area. Call (866) 518-2999 or send us a message."),
 "gallery.html": ("/gallery", "Window Treatment Gallery | Love Is Blinds Texas",
   "Blinds, shades and plantation shutters installed in Texas homes. Browse real installations by room and product type."),
 "faqs.html": ("/faqs", "Window Treatment FAQs | Love Is Blinds Texas",
   "Answers on measuring, lead times, motorization, warranties and what a free in-home consultation actually involves."),
 "how-it-works.html": ("/how-it-works", "How It Works | Love Is Blinds Texas",
   "Consultation, measure, order, install. What each step involves and how long it takes."),
 "brands.html": ("/brands", "Window Treatment Brands We Carry | Love Is Blinds Texas",
   "The manufacturers and product lines we install across Texas, and how to choose between them."),
 "team.html": ("/meet-the-team", "Meet the Team | Love Is Blinds Texas",
   "The people who measure and install your window treatments across DFW, North Texas, East Texas and Central Texas."),
 "privacy-policy.html": ("/privacy-policy", "Privacy Policy | Love Is Blinds Texas",
   "How Love Is Blinds Texas collects, uses and protects the information you submit through this site."),
 "404.html": ("/404", "Page Not Found | Love Is Blinds Texas",
   "That page is not here. Browse our window treatment products or find your Texas service area."),
}

def crumbs(url, name, parent=None):
    t = [("Home", "/")]
    if parent: t.append(parent)
    if url != "/": t.append((name, url))
    return S.breadcrumbs(t)

def run():
    base = [S.organization(BIZ), S.website(BIZ), S.business(BIZ)]
    done = []

    for f, (url, title, desc) in CORE.items():
        if not os.path.exists(f): continue
        s = detext(swap_chrome(strip_ld(open(f).read())))
        short = title.split("|")[0].strip()
        nodes = base + [S.webpage(url, title, desc), crumbs(url, short)]
        s = rewrite_head(s, url, title, desc, nodes)
        open(f, "w").write(s); done.append((f, url))

    for path, (label, blurb, cat) in PRODUCT_COPY.items():
        f = f"products/{path}.html"
        if not os.path.exists(f):                       # exterior-patio-shades is new to TX
            f = "products/roller-shades.html"
            if not os.path.exists(f): continue
            s = open(f).read(); f = f"products/{path}.html"
        else:
            s = open(f).read()
        url = f"/products/{path}"
        title = f"{label} | Love Is Blinds"
        if len(title) > 62: title = label
        s = detext(swap_chrome(strip_ld(s)))
        nodes = base + [S.webpage(url, title, blurb),
                        crumbs(url, label, ("Products", "/products")),
                        S.service(url, label, blurb, S.BIZID, catalog=cat)]
        s = rewrite_head(s, url, title, blurb, nodes)
        open(f, "w").write(s); done.append((f, url))

    for path, (label, blurb) in SERVICE_COPY.items():
        f = f"services/{path}.html"
        if not os.path.exists(f): continue
        url = f"/services/{path}"
        title = f"{label} | Love Is Blinds"
        if len(title) > 62: title = label
        s = detext(swap_chrome(strip_ld(open(f).read())))
        nodes = base + [S.webpage(url, title, blurb),
                        crumbs(url, label, ("Services", "/services")),
                        S.service(url, label, blurb, S.BIZID)]
        s = rewrite_head(s, url, title, blurb, nodes)
        open(f, "w").write(s); done.append((f, url))

    for f, url, title, desc in [
        ("products/index.html", "/products", "Window Treatment Products in Texas | Love Is Blinds",
         "Blinds, shades, plantation shutters, motorization and exterior patio shades, all custom measured and installed for Texas homes."),
        ("services/index.html", "/services", "Window Treatment Services | Love Is Blinds Texas",
         "Consultation, measuring, custom ordering and professional installation across Texas.")]:
        if not os.path.exists(f): continue
        s = detext(swap_chrome(strip_ld(open(f).read())))
        nodes = base + [S.webpage(url, title, desc), crumbs(url, title.split("|")[0].strip())]
        s = rewrite_head(s, url, title, desc, nodes)
        open(f, "w").write(s); done.append((f, url))

    # GA-only page with no Texas equivalent
    for gone in ["services/custom-blinds-installation.html"]:
        if os.path.exists(gone): os.remove(gone)
    return done

if __name__ == "__main__":
    d = run()
    print(f"converted {len(d)} pages")
