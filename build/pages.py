"""City page generator for Love Is Blinds Texas."""
import json, math, os, re, sys, html
sys.path.insert(0, os.path.dirname(__file__))
import schema as S, territory as T

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D    = json.load(open(os.path.join(ROOT, "data/tx.json")))
BIZ, CITIES = D["business"], D["cities"]
BY = {c["slug"]: c for c in CITIES}
HEAD = open(os.path.join(ROOT, "build/partials/header.html")).read()
FOOT = open(os.path.join(ROOT, "build/partials/footer.html")).read()

PATIO_PAGES = set(json.load(open(os.path.join(ROOT, "data/patio-cities.json")))["cities"])
SHUTTER_PAGES = set(json.load(open(os.path.join(ROOT, "data/shutter-cities.json")))["cities"])
MOTOR_PAGES = set(json.load(open(os.path.join(ROOT, "data/motorized-cities.json")))["cities"])
REVIEWS = json.load(open(os.path.join(ROOT, "data/reviews.json")))
BY_CITY = {}
for _r in REVIEWS:
    if _r.get("slug"):
        BY_CITY.setdefault(_r["slug"], []).append(_r)

HEROES = [
 "shutters-shutters-101-jpg.webp",
 "roller-shades-roller-shades-230-jpg.webp",
 "shutters-shutters-113-jpg.webp",
 "roller-shades-roller-shades-201-jpg.webp",
 "woven-wood-shades-woven-wood-shades-003-jpg.webp",
 "shutters-shutters-091-jpg.webp",
 "honeycomb-shades-honeycomb-shades-018-jpg.webp",
 "roller-shades-home-hero-shades-1-jpeg.webp",
 "shutters-shutters-077-jpg.webp",
 "roman-shades-roman-shades-036-jpg.webp",
 "roller-shades-roller-shades-118-jpg.webp",
 "shutters-shutters-028-jpg.webp",
]
def hero_for(c):
    return "/images/lib/" + HEROES[sum(ord(x) for x in c["slug"]) % len(HEROES)]

TICK = ('<span class="tick"><svg viewBox="0 0 24 24">'
        '<path d="m20 6-11 11-5-5"/></svg></span>')

PRODUCTS = [
 ("Exterior Patio Shades","/products/exterior-patio-shades","Outdoor shades that stop the sun before it reaches the glass."),

 ("Custom Blinds","/products/blinds","Real wood, faux wood and composite blinds."),
 ("Roller Shades","/products/roller-shades","Solar screen and blackout roller shades."),
 ("Honeycomb Shades","/products/honeycomb-shades","Cellular shades that cut heat transfer at the glass."),
]
def e(s): return html.escape(s or "", quote=True)

def _leads(terr):
    L = terr["leads"]
    return L[0] if len(L) == 1 else " and ".join([", ".join(L[:-1]), L[-1]])

_SLUG = {m["name"]: m["slug"] for m in T.TEAM}

def _leads_linked(terr):
    """Same names, each linked to its own team page."""
    parts = [f'<a href="/team/{_SLUG[n]}">{html.escape(n)}</a>' if n in _SLUG
             else html.escape(n) for n in terr["leads"]]
    return parts[0] if len(parts) == 1 else " and ".join([", ".join(parts[:-1]), parts[-1]])

def miles(a, b):
    if not (a.get("lat") and b.get("lat")): return None
    la1, lo1, la2, lo2 = map(math.radians, [a["lat"], a["lng"], b["lat"], b["lng"]])
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 7917.5 * math.asin(math.sqrt(h))

def nearby(city, n=6):
    """Real neighbours by distance; territory peers when we have no coordinates."""
    scored = []
    for o in CITIES:
        if o["slug"] == city["slug"] or o["slug"] == city.get("twin"): continue
        d = miles(city, o)
        if d is not None: scored.append((d, o))
    if scored:
        return [o for _, o in sorted(scored, key=lambda x: x[0])[:n]]
    peers = [o for o in CITIES
             if T.of(o["slug"])["key"] == T.of(city["slug"])["key"] and o["slug"] != city["slug"]]
    return peers[:n]

# ---- demand-driven titles -------------------------------------------------
# Head term per city comes from Semrush volume, not a guess. Dallas wants
# "blinds" (260/mo, $14.76 CPC), McKinney wants "window treatments" (110/mo at
# $22.32), Grapevine and Keller want "plantation shutters". One template for
# 48 cities leaves most of that on the table.
KW = json.load(open(os.path.join(ROOT, "data/keywords.json")))
CITY_KW = KW["city_head"]
PATIO = KW["city_patio"]

TERM_TITLE = {"blinds": "Custom Blinds", "window treatments": "Window Treatments",
              "plantation shutters": "Plantation Shutters", "shutters": "Shutters",
              "custom blinds": "Custom Blinds"}

# A city page must never lead with a term its own dedicated product page owns.
# Doing so is exactly what let /grapevine-tx-2 outrank /grapevine-tx on the live
# site: two pages, one intent, Google picks one at random.
# Every city now has all six product pages, so the city page must not lead with
# any product term or it competes with its own child. "window treatments" is the
# one head term no product page claims, so the city hub keeps that.
_PRODUCT_TERMS = {"blinds", "plantation shutters", "shades", "shutters",
                  "patio shades", "motorized"}

def head_of(c):
    term = CITY_KW.get(c["slug"], {}).get("term")
    return None if term in _PRODUCT_TERMS else term

def title_for(c):
    """Lead with the term the city actually searches; keep brand; stay under 60."""
    city = c["label"]
    h = head_of(c)
    cands = []
    if h:
        lead = TERM_TITLE.get(h, h.title())
        cands += [f"{lead} in {city}, TX | Shutters & Shades | Love Is Blinds",
                  f"{lead} in {city}, TX | Love Is Blinds",
                  f"{lead} {city} TX | Love Is Blinds"]
    cands += [f"Custom Blinds, Shades & Shutters in {city}, TX | Love Is Blinds",
              f"Blinds, Shades & Shutters in {city}, TX | Love Is Blinds",
              f"Blinds & Shutters in {city}, TX | Love Is Blinds",
              f"Window Treatments in {city}, TX | Love Is Blinds",
              f"Blinds & Shutters in {city}, TX"]
    if c.get("variant"):
        cands = [f"Custom Blinds & Shutters in {city}, TX | {c['variant']}"] + cands
    for t in cands:
        if len(t) <= 60:
            return t
    return cands[-1][:60]

def meta_for(c):
    """Under 155, leads with the head term, names patio shades where there is
    real local demand for them, and ends on the number that actually rings."""
    ph = S.pretty(c["phone"]) or BIZ["phone"]
    city, h = c["label"], head_of(c)
    lead = {"window treatments": "Custom window treatments",
            "plantation shutters": "Plantation shutters, blinds and shades",
            "shutters": "Shutters, blinds and shades"}.get(h, "Custom blinds, shades and shutters")
    if c.get("variant"):
        return (f"{lead} from our {c['variant']} location in {city}, TX. "
                f"Free in-home measure and installation. Call {ph}.")[:155]
    tail = ("Patio shades too. " if c["slug"] in PATIO else "")
    for body in [
        f"{lead} for {city}, TX homes. {tail}Free in-home consultation and professional installation. Call {ph}.",
        f"{lead} for {city}, TX homes. {tail}Free in-home consultation and install. Call {ph}.",
        f"{lead} in {city}, TX. {tail}Free in-home consultation and installation. Call {ph}.",
        f"{lead} in {city}, TX. Free in-home consultation and installation. Call {ph}.",
        f"{lead} in {city}, TX. Free in-home measure and install. Call {ph}.",
    ]:
        if len(body) <= 155:
            return body
    return f"{lead} in {city}, TX. Free consultation. Call {ph}."[:155]


def faqs_for(c):
    ph = S.pretty(c["phone"]) or BIZ["phone"]
    terr = T.of(c["slug"])
    out = [
      (f"Do you offer free in-home consultations in {c['label']}?",
       f"Yes. We bring samples to your home in {c['label']}, measure every opening ourselves and "
       f"quote from those measurements. There is no charge for the visit and no obligation to order. "
       f"Call {ph} to book a time."),
      (f"How long does an order take in {c['label']}?",
       "Most custom orders arrive within two to four weeks of approval, depending on the product line "
       "and fabric. Motorized treatments can run longer. We confirm the timeline in writing on your quote."),
      (f"Who measures and installs in {c['label']}?",
       f"{_leads(terr)} run {terr['brand']}, which covers {c['label']} along with "
       f"{terr['blurb']}. The person who measures your windows is the person who fits them."),
      (f"Do you install exterior patio shades in {c['label']}?",
       f"Yes. Exterior patio shades, outdoor roller shades and motorized patio screens are a large "
       f"part of what we do in {c['label']}, because shading the outside of the glass is far more "
       f"effective against Texas afternoon sun than an interior blind on the same opening."),
      ("What if a treatment does not fit correctly?",
       "We measured it, so we correct it. If an opening is wrong against the approved measurements, "
       "we remake it and reinstall at no cost to you."),
    ]
    if c.get("street"):
        out.append((f"Where are you located near {c['label']}?",
          f"Our {c['locality']} location is at {c['street']}, {c['locality']}, TX "
          f"{c.get('postal','')}".strip().rstrip(',') + ". Consultations happen at your home, "
          "so most customers never need to visit us."))
    return out

# ---------------------------------------------------------------- rendering
def head_block(c):
    url, t, m = c["url"], title_for(c), meta_for(c)
    img = hero_for(c)
    nodes = [
        S.organization(BIZ), S.website(BIZ), S.business(BIZ), S.business(BIZ, c),
        S.webpage(url, t, m, about=f"{S.SITE}{url}#business", primary=img),
        S.breadcrumbs([("Home","/"),("Service Areas","/areas-we-serve"),(f"{c['label']}, TX",url)]),
        S.faq(url, faqs_for(c)),
        S.service(url, f"Custom Window Treatments in {c['label']}, TX",
                  f"Measurement, custom order and professional installation of blinds, shades and "
                  f"shutters for homes in {c['label']}, Texas.",
                  f"{S.SITE}{url}#business",
                  area={"@type":"City","name":c["locality"]},
                  catalog=[p[0] for p in PRODUCTS] + ["Outdoor Roller Shades",
                           "Motorized Patio Shades", "Solar Screen Shades"]),
    ]
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t)}</title>
<meta name="description" content="{e(m)}">
<link rel="canonical" href="{S.SITE}{url}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#3A4D5C">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(BIZ['name'])}">
<meta property="og:title" content="{e(t)}">
<meta property="og:description" content="{e(m)}">
<meta property="og:url" content="{S.SITE}{url}">
<meta property="og:image" content="{S.SITE}{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(t)}">
<meta name="twitter:description" content="{e(m)}">
<meta name="twitter:image" content="{S.SITE}{img}">
<meta name="geo.region" content="US-TX">
<meta name="geo.placename" content="{e(c['locality'])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css">
{S.render(nodes)}
</head>'''

def body_block(c):
    hero = hero_for(c)
    hero2 = "/images/lib/" + HEROES[(sum(ord(x) for x in c["slug"]) + 5) % len(HEROES)]
    ph   = S.pretty(c["phone"]) or BIZ["phone"]
    tel  = S.tel(c["phone"] or BIZ["tel"])
    terr = T.of(c["slug"])
    near = nearby(c)
    patio_url = ("/patio-shades-" + c["slug"]) if c["slug"] in PATIO_PAGES \
                else "/products/exterior-patio-shades"
    shutter_url = ("/plantation-shutters-" + c["slug"]) if c["slug"] in SHUTTER_PAGES \
                  else "/products/plantation-shutters"
    motor_url = ("/motorized-shades-" + c["slug"]) if c["slug"] in MOTOR_PAGES \
                else "/products/motorized-window-treatment-automations"
    revs = BY_CITY.get(c["slug"], [])
    if revs:
        cards = "".join(
          '<div class="review reveal"><div class="stars">'
          + "&#9733;" * int(r.get("rating", 5)) + "</div>"
          + f'<p>"{e(r["quote"])}"</p><div class="who">{e(r["name"])}</div>'
          + f'<div class="where">{e(c["label"])}, TX</div></div>' for r in revs)
        gbp_cta = (f'<p><a class="btn-link" href="{e(c["gbp"][0])}" rel="noopener">'
                   f'Read every {e(c["label"])} review on Google '
                   f'<span class="arw">&rarr;</span></a></p>' if c.get("gbp") else "")
        reviews_block = (
          f'<section class="section"><div class="container center">'
          f'<h2 class="title">What {e(c["label"])} homeowners say</h2>'
          f'<p class="lead">Reviews left on our Google profile by customers in and around '
          f'{e(c["label"])}.</p></div><div class="container">'
          f'<div class="reviews">{cards}</div>{gbp_cta}</div></section>')
    else:
        reviews_block = ""
    prods = (f'<a class="prod-card reveal" href="{shutter_url}"><div class="pbody">'
             f'<h3>Plantation Shutters</h3><p>Louvered shutters built to the window opening.</p>'
             f'<span class="btn-link">See plantation shutters <span class="arw">&rarr;</span></span>'
             f'</div></a>'
             f'<a class="prod-card reveal" href="{motor_url}"><div class="pbody">'
             f'<h3>Motorization</h3><p>App, remote and voice control.</p>'
             f'<span class="btn-link">See motorization <span class="arw">&rarr;</span></span>'
             f'</div></a>') + "".join(
      f'<a class="prod-card reveal" href="{u}"><div class="pbody"><h3>{e(n)}</h3>'
      f'<p>{e(d)}</p><span class="btn-link">See {e(n.lower())} <span class="arw">&rarr;</span></span>'
      f'</div></a>' for n,u,d in PRODUCTS)
    nearlinks = " ".join(
      f'<li><a href="{o["url"]}">{e(o["label"])}, TX</a></li>' for o in near)
    faqhtml = "".join(
      f'<details><summary>{e(q)}</summary><div class="a">{e(a)}</div></details>'
      for q, a in faqs_for(c))
    addr = (f'<li class="contact-line">{e(c["street"])}, {e(c["locality"])}, TX {e(c.get("postal",""))}</li>'
            if c.get("street") else
            f'<li class="contact-line">Serving {e(c["label"])} and the surrounding area</li>')
    gbp = (f'<li class="contact-line"><a href="{e(c["gbp"][0])}" rel="noopener">'
           f'View our Google Business Profile</a></li>' if c.get("gbp") else "")
    return f'''<body>
{HEAD.split('<body',1)[1].split('>',1)[1]}
<main>
<section class="phero">
  <picture><img src="{hero}" alt="Custom window treatments in {e(c['label'])}, TX by Love Is Blinds" fetchpriority="high"></picture>
  <div class="container">
    <div class="phero-copy">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">&rsaquo;</span><a href="/areas-we-serve">Service Areas</a><span class="sep">&rsaquo;</span>{e(c['label'])}, TX</nav>
      <h1 class="title">Custom Blinds, Shades and Shutters in {e(c['label'])}, Texas{' (' + e(c['variant']) + ')' if c.get('variant') else ''}</h1>
      <p class="lead">We measure your windows, build the treatments to those measurements and
        install them ourselves. Free in-home consultation in {e(c['label'])}, no charge for the
        visit and no obligation to order.</p>
      <div class="hero-actions btnrow">
        <a class="btn btn-primary btn-lg" href="tel:{tel}">Call {e(ph)}</a>
        <a class="btn btn-secondary btn-lg" href="/schedule-now">Book a consultation</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split media-right">
    <div class="body reveal">
      <h2 class="title">Window treatments fitted to {e(c['label'])} homes</h2>
      <p>Every opening gets measured on site. Nothing here is cut to a catalogue size and trimmed
         to fit, which is what causes the light gaps and the crooked bottom rails you see on
         stock blinds.</p>
      <ul class="feature-list">
        <li>{TICK}Free in-home consultation with samples you can hold against your own light</li>
        <li>{TICK}Measured, ordered and installed by the same local team</li>
        <li>{TICK}{e(c['label'])} is covered by {e(terr['brand'])}, run by {_leads_linked(terr)}</li>
        <li>{TICK}Remade at no cost if a treatment does not match the approved measurements</li>
      </ul>
      <div class="btnrow"><a class="btn btn-primary btn-lg" href="/contact">Book your free consultation</a></div>
    </div>
    <div class="media reveal">
      <img src="{hero2}" width="900" height="600" loading="lazy"
           alt="Custom window treatments installed in {e(c['label'])}, TX by Love Is Blinds">
    </div>
  </div>
</section>

<section class="section bg-cream-tint">
  <div class="container center"><h2 class="title">What we install in {e(c['label'])}</h2></div>
  <div class="container"><div class="prod-grid">{prods}</div></div>
</section>

<section class="section">
  <div class="container split">
    <div class="body reveal">
      <h2 class="title">Reaching us from {e(c['label'])}</h2>
      <ul class="nap-list">
        <li class="contact-line"><a href="tel:{tel}">{e(ph)}</a></li>
        {addr}
        <li class="contact-line"><a href="/contact">Send us a message</a></li>
        {gbp}
      </ul>
      <div class="btnrow"><a class="btn btn-primary btn-lg" href="/contact">Request a quote</a></div>
    </div>
    <div class="body reveal">
      <h2 class="title">Nearby areas we serve</h2>
      <ul class="nap-list">{nearlinks}</ul>
      <p><a class="btn-link" href="/areas-we-serve">All Texas service areas
        <span class="arw">&rarr;</span></a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split media-right">
    <div class="body reveal">
      <h2 class="title">Patio shades for {e(c['label'])} outdoor spaces</h2>
      <p>A west-facing patio in {e(c['label'])} takes the worst of the afternoon. Exterior shades
         stop that sun on the outside of the glass instead of after it has already come through,
         which is what keeps the space usable and takes heat load off the rooms behind it.</p>
      <ul class="feature-list">
        <li>{TICK}Solar screen, motorized and retractable outdoor shades</li>
        <li>{TICK}Openness factor chosen for the way your patio faces</li>
        <li>{TICK}Porches, patios, pergolas and outdoor rooms</li>
      </ul>
      <div class="btnrow">
        <a class="btn btn-primary btn-lg" href="{patio_url}">
          See patio shades in {e(c['label'])}</a>
        <a class="btn btn-secondary btn-lg" href="tel:{tel}">Call {e(ph)}</a>
      </div>
    </div>
    <div class="media reveal">
      <img src="/images/lib/exterior-patio-shades-exterior-patio-shades-002-jpg.webp"
           width="900" height="600" loading="lazy"
           alt="Exterior patio shades installed by Love Is Blinds in {e(c['label'])}, TX">
    </div>
  </div>
</section>

{reviews_block}
<section class="section bg-cream-tint">
  <div class="container center"><h2 class="title">{e(c['label'])} questions, answered</h2></div>
  <div class="container"><div class="faq">{faqhtml}</div></div>
</section>
</main>
{FOOT}'''

def render_city(c):
    return head_block(c) + "\n" + body_block(c)

if __name__ == "__main__":
    n = 0
    for c in CITIES:
        open(os.path.join(ROOT, c["slug"] + ".html"), "w").write(render_city(c))
        n += 1
    print(f"wrote {n} city pages")
