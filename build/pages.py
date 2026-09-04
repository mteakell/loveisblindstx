"""City page generator for Love Is Blinds Texas."""
import hashlib, json, math, os, re, sys, html
sys.path.insert(0, os.path.dirname(__file__))
import schema as S, territory as T
import blocks as BK
import icons as IC

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
GUARANTEES = json.load(open(os.path.join(ROOT, "data/guarantees.json")))["guarantees"]
# 4+ stars only, newest first, at the source. product_city.py consumes
# BY_CITY directly, and filtering only in this file's own picker let the
# single 1-star review onto all six Waxahachie product pages.
BY_CITY = {}
for _r in REVIEWS:
    if _r.get("slug") and _r.get("rating", 5) >= 4:
        BY_CITY.setdefault(_r["slug"], []).append(_r)
for _v in BY_CITY.values():
    _v.sort(key=lambda r: r.get("date", ""), reverse=True)

def GAL_LABEL(path):
    """Name the treatment in a photo from its filename, for caption and alt."""
    n = path.split("/")[-1]
    for pre, lab in [("exterior-patio-shades", "Exterior patio shades"),
                     ("shutters-shutters", "Plantation shutters"),
                     ("roller-shades", "Roller shades"),
                     ("honeycomb-shades", "Honeycomb shades"),
                     ("woven-wood-shades", "Woven wood shades"),
                     ("roman-shades", "Roman shades"),
                     ("banded-shades", "Banded shades"),
                     ("smart-drapes", "Drapery and motorization"),
                     ("blinds-blinds", "Custom blinds")]:
        if n.startswith(pre):
            return lab
    return "Custom window treatments"


GALLERY = ["/images/lib/" + f for f in [
 "shutters-shutters-113-jpg.webp", "roller-shades-roller-shades-230-jpg.webp",
 "exterior-patio-shades-exterior-patio-shades-002-jpg.webp", "shutters-shutters-077-jpg.webp",
 "woven-wood-shades-woven-wood-shades-003-jpg.webp", "roller-shades-roller-shades-137-jpg.webp",
 "shutters-shutters-151-jpg.webp", "honeycomb-shades-honeycomb-shades-018-jpg.webp",
 "smart-drapes-smart-drapes-002-jpg.webp", "shutters-shutters-101-jpg.webp",
 "roller-shades-roller-shades-201-jpg.webp", "blinds-blinds-009-jpg.webp",
 "exterior-patio-shades-exterior-patio-shades-001-jpg.webp", "shutters-shutters-060-jpg.webp",
 "roller-shades-roller-shades-245-jpg.webp", "smart-drapes-smart-drapes-010-jpg.webp",
 "shutters-shutters-028-jpg.webp", "honeycomb-shades-honeycomb-shades-026-jpg.webp",
]]

PROD_IMG = {k: ["/images/lib/" + f for f in v] for k, v in {
 "shutters": ["shutters-shutters-113-jpg.webp", "shutters-shutters-077-jpg.webp",
              "shutters-shutters-101-jpg.webp", "shutters-shutters-091-jpg.webp",
              "shutters-shutters-151-jpg.webp"],
 "motor":    ["roller-shades-roller-shades-245-jpg.webp", "smart-drapes-smart-drapes-008-jpg.webp",
              "roller-shades-roller-shades-137-jpg.webp", "smart-drapes-smart-drapes-010-jpg.webp"],
 "patio":    ["exterior-patio-shades-exterior-patio-shades-001-jpg.webp",
              "exterior-patio-shades-exterior-patio-shades-002-jpg.webp",
              "exterior-patio-shades-exterior-patio-shades-005-jpg.webp"],
 "blinds":   ["blinds-blinds-009-jpg.webp", "blinds-blinds-009-jpg.webp",
              "blinds-blinds-007-jpg.webp", "blinds-blinds-011-jpg.webp"],
 "roller":   ["roller-shades-roller-shades-230-jpg.webp", "roller-shades-roller-shades-201-jpg.webp",
              "roller-shades-home-hero-shades-1-jpeg.webp", "roller-shades-roller-shades-137-jpg.webp"],
 "honeycomb":["honeycomb-shades-honeycomb-shades-018-jpg.webp",
              "honeycomb-shades-honeycomb-shades-008-jpg.webp",
              "honeycomb-shades-honeycomb-shades-022-jpg.webp"],
}.items()}
PROD_IMG_KEY = {
 "/products/exterior-patio-shades": "patio",
 "/products/blinds": "blinds",
 "/products/roller-shades": "roller",
 "/products/honeycomb-shades": "honeycomb",
}

IMG_MOTOR = ["/images/lib/" + f for f in [
 "roller-shades-roller-shades-245-jpg.webp",
 "smart-drapes-smart-drapes-008-jpg.webp",
 "roller-shades-roller-shades-230-jpg.webp",
 "exterior-patio-shades-exterior-patio-shades-002-jpg.webp",
 "roller-shades-roller-shades-137-jpg.webp",
 "smart-drapes-smart-drapes-010-jpg.webp",
]]

HEROES = [
 "shutters-shutters-101-jpg.webp",
 "roller-shades-roller-shades-230-jpg.webp",
 "shutters-shutters-113-jpg.webp",
 "roller-shades-roller-shades-201-jpg.webp",
 "woven-wood-shades-woven-wood-shades-003-jpg.webp",
 "shutters-shutters-060-jpg.webp",
 "honeycomb-shades-honeycomb-shades-018-jpg.webp",
 "roller-shades-home-hero-shades-1-jpeg.webp",
 "shutters-shutters-077-jpg.webp",
 "shutters-shutters-151-jpg.webp",
 "roller-shades-roller-shades-245-jpg.webp",
 "shutters-shutters-028-jpg.webp",
 "roller-shades-roller-shades-137-jpg.webp",
]
def hero_for(c):
    return "/images/lib/" + HEROES[sum(ord(x) for x in c["slug"]) % len(HEROES)]

TICK = ('<span class="tick"><svg viewBox="0 0 24 24">'
        '<path d="m20 6-11 11-5-5"/></svg></span>')

# Three blurbs per product, rotated per city. These cards were the same on all
# 48 pages, which put 60 identical words on every one of them for no reason.
PRODUCT_BLURBS = {
 "/products/exterior-patio-shades": [
   "Outdoor shades that stop the sun before it reaches the glass.",
   "Exterior shading for patios, porches and west-facing windows.",
   "Motorized and retractable shades built for Texas afternoons."],
 "/products/blinds": [
   "Real wood, faux wood and composite blinds.",
   "Slat treatments you tilt, in materials matched to the room.",
   "Wood where it stays dry, faux wood where it does not."],
 "/products/roller-shades": [
   "Solar screen and blackout roller shades.",
   "One fabric on a tube, from sheer through to full blackout.",
   "Clean lines, almost no stack, and a fabric for every light level."],
 "/products/honeycomb-shades": [
   "Cellular shades that cut heat transfer at the glass.",
   "Air trapped in cells, which is what makes them insulate.",
   "The option that shows up on the cooling bill."],
}
PRODUCTS = [
 ("Exterior Patio Shades","/products/exterior-patio-shades"),
 ("Custom Blinds","/products/blinds"),
 ("Roller Shades","/products/roller-shades"),
 ("Honeycomb Shades","/products/honeycomb-shades"),
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
        # Two records can share a label (corsicana-tx and
        # w-7th-avenue-corsicana-tx are both "Corsicana"), which rendered the
        # same city name twice in the list. Keep the nearest of each label.
        out, seen = [], {city["label"]}
        for _, o in sorted(scored, key=lambda x: x[0]):
            if o["label"] in seen: continue
            seen.add(o["label"]); out.append(o)
            if len(out) == n: break
        return out
    peers, seen = [], {city["label"]}
    for o in CITIES:
        if o["slug"] == city["slug"]: continue
        if T.of(o["slug"])["key"] != T.of(city["slug"])["key"]: continue
        if o["label"] in seen: continue
        seen.add(o["label"]); peers.append(o)
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
    out += bpick_many(BK.EXTRA_FAQ, c["slug"], 5, 2)
    return out


# ---- block rotation ------------------------------------------------------
_CIX = {c["slug"]: i for i, c in enumerate(sorted(CITIES, key=lambda x: x["slug"]))}
_STRIDE = {0: 1, 1: 5, 2: 7, 3: 11, 4: 13, 5: 17, 6: 19, 7: 23, 12: 29, 13: 31}


def _seed(slug, salt):
    """Stable per-slug, per-block offset.

    A sequential index times a stride made neighbouring slugs land on the same
    variant for several blocks at once, so two review-less pages could share
    half their sentences. Hashing the slug with the salt decorrelates the
    blocks: matching on one no longer means matching on the rest.
    """
    return int(hashlib.sha1(f"{slug}:{salt}".encode()).hexdigest()[:8], 16)


def bpick(pool, slug, salt=0):
    return pool[_seed(slug, salt) % len(pool)]


def bpick_many(pool, slug, n, salt=0):
    """Pick n distinct items, stepping by a stride coprime with the pool."""
    i = _seed(slug, salt) % len(pool)
    step = _STRIDE.get(salt, 1)
    while len(pool) % step == 0 and step > 1:
        step += 2
    return [pool[(i + k * step) % len(pool)] for k in range(min(n, len(pool)))]

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

def body_block(c, n_reviews=8):
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
    # 4+ only. The testimonials block is a curated selection, which is normal
    # for a site's own reviews. The rating in the footer badge is NOT curated:
    # it comes from data/gbp-ratings.json, which carries Google's own figure
    # (Waxahachie 4.9), so the number we publish stays honest.
    revs = sorted((r for r in BY_CITY.get(c["slug"], []) if r.get("rating", 5) >= 4),
                  key=lambda r: r.get("date", ""), reverse=True)[:n_reviews]
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
    _rh = bpick(BK.ROOM_HEADS, c["slug"], 0)
    _rooms = bpick_many(BK.ROOM_ITEMS, c["slug"], 4, 0)
    _used_r, _used_p = set(), set()
    rooms_block = (
      f'<section class="section"><div class="container center">'
      f'<h2 class="title">{e(_rh.format(city=c["label"]))}</h2></div>'
      f'<div class="container"><div class="prod-grid">' +
      "".join(f'<div class="type-card">{IC.icon_for(t, _used_r)}<div class="pbody">'
              f'<h3>{e(t)}</h3><p>{e(b.format(city=c["label"]))}</p></div></div>'
              for t, b in _rooms) + '</div></div></section>')

    _mh = bpick(BK.MATERIAL_HEADS, c["slug"], 1)
    _mb = bpick(BK.MATERIAL_BODIES, c["slug"], 4)
    materials_block = (
      f'<section class="section bg-cream-tint"><div class="container split">'
      f'<div class="body"><h2 class="title">{e(_mh)}</h2><div class="prose"><p>{e(_mb)}</p></div></div>'
      f'<div class="media"><img src="{hero2}" width="900" height="600" loading="lazy" '
      f'alt="Window treatment materials fitted in {e(c["label"])}, TX by Love Is Blinds"></div>'
      f'</div></section>')

    _ph = bpick(BK.PATIO_HEADS, c["slug"], 2)
    _pintro = bpick(BK.PATIO_INTROS, c["slug"], 3)
    _ptypes = bpick_many(BK.PATIO_ITEMS, c["slug"], 4, 2)
    patio_types = "".join(
      f'<div class="type-card">{IC.icon_for(t, _used_p)}<div class="pbody"><h3>{e(t)}</h3>'
      f'<p>{e(b.format(city=c["label"]))}</p></div></div>' for t, b in _ptypes)
    patio_block = (
      f'<section class="section"><div class="container center">'
      f'<h2 class="title">{e(_ph.format(city=c["label"]))}</h2>'
      f'<p class="lead">{e(_pintro.format(city=c["label"]))}</p></div>'
      f'<div class="container"><div class="prod-grid">{patio_types}</div>'
      f'<p class="center" style="margin-top:22px"><a class="btn btn-primary btn-lg" '
      f'href="{patio_url}">Exterior patio shades in {e(c["label"])}</a></p></div></section>')

    _moh = bpick(BK.MOTOR_HEADS, c["slug"], 3)
    _mob = bpick(BK.MOTOR_BODIES, c["slug"], 1)
    # this was a heading and one grey paragraph on a flat background, which was
    # the thinnest-looking thing on the page. Same parallax treatment the
    # product pages use.
    _mimg = bpick(IMG_MOTOR, c["slug"], 7)
    motor_block = (
      f'<section class="parallax-band" style="background-image:url(\'{_mimg}\')">'
      f'<div class="container">'
      f'<p class="pb-eyebrow">Motorization</p>'
      f'<h2 class="pb-title">{e(_moh.format(city=c["label"]))}</h2>'
      f'<p class="pb-body">{e(_mob)}</p>'
      f'<div class="btnrow center" style="justify-content:center">'
      f'<a class="btn btn-primary btn-lg" href="/products/window-treatment-automations">'
      f'See motorized options</a></div>'
      f'</div></section>')

    # a strip of real work, so the run of text sections is broken by something
    # to look at rather than another card grid
    _gimgs = bpick_many(GALLERY, c["slug"], 6, 11)
    gallery_block = (
      f'<section class="section"><div class="container center">'
      f'<h2 class="title">Recent work around {e(c["label"])}</h2>'
      f'<p class="lead">Blinds, shades, shutters and exterior patio shades we have measured and '
      f'installed for Texas homes.</p></div>'
      f'<div class="container"><div class="shots">' +
      "".join(f'<figure class="shot">'
              f'<img src="{g}" data-alt-final alt="{e(GAL_LABEL(g))} installed by Love Is Blinds '
              f'in {e(c["label"])}, TX" loading="lazy" width="2000" height="1500">'
              f'<figcaption><span class="shot-kind">{e(GAL_LABEL(g))}</span>'
              f'<span class="shot-where">{e(c["label"])}, TX</span></figcaption>'
              f'</figure>' for g in _gimgs) +
      f'</div><p class="center" style="margin-top:26px">'
      f'<a class="btn btn-secondary btn-lg" href="/gallery">See the full gallery</a></p>'
      f'</div></section>')

    _prh, _steps = bpick(BK.PROCESS_VARIANTS, c["slug"], 5)
    process_block = (
      f'<section class="section"><div class="container center">'
      f'<h2 class="title">{e(_prh)} in {e(c["label"])}</h2></div>'
      f'<div class="container"><div class="steps">' +
      "".join(f'<div class="step"><span class="step-n">{i}</span>'
              f'<h3>{e(t)}</h3><p>{e(b)}</p></div>'
              for i, (t, b) in enumerate(_steps, 1)) + '</div></div></section>')

    gtee_cards = "".join(
        f'<div class="type-card">{IC.guarantee_icon(g["id"])}<div class="pbody">'
        f'<h3>{e(g["name"])}</h3><p>{e(g["text"])}</p></div></div>'
        for g in GUARANTEES)
    label = e(c["label"])
    # These were text-only cards on every city page while the home page versions
    # carried photos. Six product cards with no imagery was the flattest thing
    # on the page.
    def _pcard(name, url, blurb, img):
        return (f'<a class="prod-card reveal" href="{url}">'
                f'<span class="pic"><img src="{img}" alt="{e(name)} installed in '
                f'{e(c["label"])}, TX by Love Is Blinds" loading="lazy" '
                f'width="2000" height="1500"></span>'
                f'<div class="pbody"><h3>{e(name)}</h3><p>{e(blurb)}</p>'
                f'<span class="btn-link">See {e(name.lower())} '
                f'<span class="arw">&rarr;</span></span></div></a>')

    _pi = lambda k, salt: bpick(PROD_IMG[k], c["slug"], salt)
    prods = (_pcard("Plantation Shutters", shutter_url,
                    "Louvered shutters built to the window opening.", _pi("shutters", 8))
           + _pcard("Motorization", motor_url,
                    "App, remote and voice control.", _pi("motor", 9))
           + "".join(_pcard(n, u, bpick(PRODUCT_BLURBS[u], c["slug"], 6),
                            _pi(PROD_IMG_KEY[u], 10 + i))
                     for i, (n, u) in enumerate(PRODUCTS)))
    nearchips = " ".join(
      f'<a class="chip" href="{o["url"]}">{e(o["label"])}, TX</a>' for o in near)
    gbp_row = ('<li><span class="cc-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
               'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
               '<path d="M12 2a10 10 0 1 0 10 10H12Z"/><path d="M12 2v10h10"/></svg></span>'
               '<span><span class="cc-label">Reviews and photos</span>'
               f'<a class="cc-value" href="{e(c["gbp"][0])}" rel="noopener">Our Google Business Profile</a>'
               '</span></li>') if c.get("gbp") else ""
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
      <p class="lead">{e(bpick(BK.HERO_LEADS, c["slug"], 12).format(c=c["label"]))}</p>
      <div class="hero-actions btnrow">
        <a class="btn btn-primary btn-lg" href="tel:{tel}">Call {e(ph)}</a>
        <a class="btn btn-secondary btn-lg" href="/schedule-now">Book your free consultation</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split media-right">
    <div class="body reveal">
      <h2 class="title">Window treatments fitted to {e(c['label'])} homes</h2>
      <p>{e(bpick(BK.BODY_INTROS, c["slug"], 13).format(c=c["label"]))}</p>
      <ul class="feature-list">
        <li>{TICK}Free in-home consultation with samples you can hold against your own light</li>
        <li>{TICK}Measured, ordered and installed by the same local team</li>
        <li>{TICK}{e(c['label'])} is covered by {e(terr['brand'])}, run by {_leads_linked(terr)}</li>
        <li>{TICK}Remade at no cost if a treatment does not match the approved measurements</li>
      </ul>
      <div class="btnrow"><a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a></div>
    </div>
    <div class="media reveal">
      <img src="{hero2}" width="900" height="600" loading="lazy"
           alt="Custom window treatments installed in {e(c['label'])}, TX by Love Is Blinds">
    </div>
  </div>
</section>

<section class="section bg-cream-tint">
  <div class="container center"><h2 class="title">Blinds, shades and shutters we install in {e(c['label'])}</h2></div>
  <div class="container"><div class="prod-grid prod-grid-6">{prods}</div></div>
</section>

<section class="section contact-band">
  <div class="container contact-cols">
    <div class="contact-card reveal">
      <h2 class="title">Talk to your {e(c['label'])} team</h2>
      <ul class="cc-rows">
        <li><span class="cc-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/></svg></span>
          <span><span class="cc-label">Call your local team</span><a class="cc-value" href="tel:{tel}">{e(ph)}</a></span></li>
        <li><span class="cc-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/></svg></span>
          <span><span class="cc-label">Service area</span><span class="cc-value">{e(c['label'])} and the surrounding area</span></span></li>
        <li><span class="cc-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span>
          <span><span class="cc-label">Prefer to write</span><a class="cc-value" href="/schedule-now">Send us a message</a></span></li>
        {gbp_row}
      </ul>
      <div class="btnrow"><a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a></div>
    </div>
    <div class="contact-side reveal">
      <h2 class="title">We also come to these neighbors</h2>
      <p class="lead">Same team, same written quote, no travel charge.</p>
      <div class="chips">{nearchips}</div>
      <p style="margin-top:18px"><a class="btn-link" href="/areas-we-serve">All Texas service areas
        <span class="arw">&rarr;</span></a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split media-right">
    <div class="body reveal">
      <h2 class="title">Exterior patio shades built for {e(c['label'])} afternoons</h2>
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

{rooms_block}
{materials_block}
{patio_block}
{motor_block}

<section class="section">
  <div class="container center">
    <h2 class="title">Every job in {label} is backed five ways</h2>
  </div>
  <div class="container"><div class="prod-grid gtee-grid">{gtee_cards}</div></div>
</section>

{gallery_block}

{process_block}

{reviews_block}
<section class="section bg-cream-tint">
  <div class="container center"><h2 class="title">{e(c['label'])} questions, answered</h2></div>
  <div class="container"><div class="faq">{faqhtml}</div></div>
</section>

<section class="section closing-cta">
  <div class="container center">
    <h2 class="title">Ready when your windows are</h2>
    <p class="lead">A free in-home consultation in {e(c['label'])}: samples at your door, every
      opening measured, and a written quote before you decide anything.</p>
    <div class="btnrow" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a>
      <a class="btn btn-secondary btn-lg" href="tel:{tel}">Call {e(ph)}</a>
    </div>
  </div>
</section>
</main>
{FOOT}'''

# Reviews are real, unique, per-city copy and we want as many as possible.
# They are also customer voice, not product copy, so past a point they dilute
# what the page is meant to rank for. Waco uncapped printed all 69 and the page
# became 85% reviews. Cap them at a share of the page instead of a flat number,
# so a page with more product copy earns more reviews rather than every page
# getting the same eight.
REVIEW_SHARE = 0.35          # reviews may be at most this much of the page
REVIEW_MIN, REVIEW_MAX = 3, 16


def _words(html, main_only=False):
    if main_only:                       # nav and footer are not page content
        m = re.search(r"<main.*?</main>", html, re.S)
        html = m.group(0) if m else html
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S)
    return len(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)).split())


def review_budget(c):
    """How many reviews fit before they outweigh the rest of the page."""
    revs = [r for r in BY_CITY.get(c["slug"], []) if r.get("rating", 5) >= 4]
    if not revs:
        return 0
    base = _words(body_block(c, 0), main_only=True)       # page without reviews
    avg = sum(len(r["quote"].split()) for r in revs) / len(revs) + 6  # +name/city
    allowed = int((REVIEW_SHARE * base) / ((1 - REVIEW_SHARE) * avg))
    # clamp to the band first, then to what actually exists: a city with one
    # review shows one, not the floor of three
    return min(len(revs), max(REVIEW_MIN, min(REVIEW_MAX, allowed)))


def render_city(c):
    return head_block(c) + "\n" + body_block(c, review_budget(c))

if __name__ == "__main__":
    n = 0
    for c in CITIES:
        open(os.path.join(ROOT, c["slug"] + ".html"), "w").write(render_city(c))
        n += 1
    print(f"wrote {n} city pages")
