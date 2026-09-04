"""Generate [product]-[city]-[state] pages for every product across every city.

Built at Maddie's direction for all cities, including those with no measured
search volume. To keep these from reading as thin permutations, each page
carries: the local operator by name and their phone, the real nearest cities
by distance, that city's own reviews where we have them, the street address
where one exists, product scope that does not overlap the other five families,
its own price drivers, and city-specific FAQs.
"""
import html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import schema as S, territory as T, pages as P, products_spec as PS, variants as V
import extra_pools as EP
import icons as IC
import blocks as BK

# Assign variants by the city's INDEX rather than a hash of its name. A hash
# collides: two cities land on the same combination and their pages read
# identically. An index guarantees the 48 cities spread across the pools.
CITY_IX = {c["slug"]: i for i, c in enumerate(sorted(P.CITIES, key=lambda x: x["slug"]))}

HERO_POOL = {
 "blinds": ["blinds-blinds-007-jpg.webp","blinds-blinds-008-jpg.webp","blinds-blinds-009-jpg.webp",
            "blinds-blinds-011-jpg.webp","blinds-blinds-004-jpg.webp","blinds-blinds-006-jpg.webp"],
 "shades": ["roller-shades-roller-shades-230-jpg.webp","roller-shades-home-hero-shades-1-jpeg.webp",
            "roller-shades-roller-shades-137-jpg.webp","roller-shades-roller-shades-245-jpg.webp",
            "honeycomb-shades-honeycomb-shades-018-jpg.webp","honeycomb-shades-honeycomb-shades-022-jpg.webp",
            "roller-shades-roller-shades-201-jpg.webp","woven-wood-shades-woven-wood-shades-003-jpg.webp",
            "banded-shades-banded-shades-011-jpg.webp","roman-shades-roman-shades-050-jpg.webp"],
 "plantation-shutters": ["shutters-shutters-101-jpg.webp","shutters-shutters-113-jpg.webp",
            "shutters-shutters-091-jpg.webp","shutters-shutters-151-jpg.webp","shutters-shutters-060-jpg.webp",
            "shutters-shutters-028-jpg.webp","shutters-shutters-077-jpg.webp","shutters-shutters-123-jpg.webp"],
 "shutters": ["shutters-shutters-147-jpg.webp","shutters-shutters-162-jpg.webp","shutters-shutters-068-jpg.webp",
            "shutters-shutters-084-jpg.webp","shutters-shutters-112-jpg.webp","shutters-shutters-030-jpg.webp",
            "shutters-shutters-101-jpg.webp","shutters-shutters-077-jpg.webp"],
 "patio-shades": ["exterior-patio-shades-exterior-patio-shades-001-jpg.webp",
            "exterior-patio-shades-exterior-patio-shades-002-jpg.webp",
            "exterior-patio-shades-exterior-patio-shades-005-jpg.webp",
            "exterior-patio-shades-exterior-patio-shades-014-jpg.webp",
            "exterior-patio-shades-exterior-patio-shades-017-jpg.webp",
            "exterior-patio-shades-exterior-patio-shades-022-jpg.webp"],
 "motorized-shades": ["roller-shades-roller-shades-245-jpg.webp","smart-drapes-smart-drapes-002-jpg.webp",
            "roller-shades-roller-shades-137-jpg.webp","smart-drapes-smart-drapes-010-jpg.webp",
            "roller-shades-roller-shades-230-jpg.webp","smart-drapes-smart-drapes-008-jpg.webp"],
}

IMG_POOL = json.load(open(os.path.join(P.ROOT, "data/image-pools.json")))

# Mixed radix decomposition of the city index. Each successive call peels off a
# different digit, so two cities cannot share every selection: with pools of 5,
# 5, 5 and 10 the combination space is far larger than 48 cities.
# Each selector gets its own coprime stride over the city index, so two cities
# would have to agree on every one of six independent selections to read alike.
# With strides 1, 3, 7, 9, 11, 13 across pools of 5-18 that cannot happen for 48
# cities.
_STRIDE = {0: 1, 5: 3, 7: 7, 11: 9, 13: 11, 17: 13, 21: 17, 3: 19}

def pick(pool, slug, salt=0):
    i = CITY_IX.get(slug, 0)
    return pool[(i * _STRIDE.get(salt, 1) + salt) % len(pool)]

def pick_many(pool, slug, n, salt=0):
    i = CITY_IX.get(slug, 0)
    start = (i * _STRIDE.get(salt, 1) + salt) % len(pool)
    return [pool[(start + i2) % len(pool)] for i2 in range(min(n, len(pool)))]

os.chdir(P.ROOT)
BIZ = P.BIZ
HEAD_INNER = P.HEAD.split("<body", 1)[1].split(">", 1)[1]
e = lambda s: html.escape(s or "", quote=True)
VOL = {}
for _p, _f in [("plantation-shutters","data/shutter-cities.json"),
               ("patio-shades","data/patio-cities.json"),
               ("motorized-shades","data/motorized-cities.json")]:
    for _s, _v in json.load(open(_f))["cities"].items():
        VOL[(_p, _s)] = sum(x[1] for x in _v["terms"])

def fit(cands, limit=60):
    for c in cands:
        if len(c) <= limit:
            return c
    return cands[-1][:limit].rsplit(" ", 1)[0]

def page(prod, slug):
    spec = PS.SPEC[prod]
    c = P.BY[slug]
    city = c["label"]
    # two Corsicana locations share a label, so the second carries its variant
    label = f"{city} ({c['variant']})" if c.get("variant") else city
    terr = T.of(slug)
    ph = S.pretty(c["phone"]) or BIZ["phone"]
    tel = S.tel(c["phone"] or BIZ["tel"])
    leads = P._leads(terr)
    url = f"/{spec['slug']}-{slug}"
    base = spec["title"].format(city=label)
    title = fit([f"{base} | Love Is Blinds", base, base.replace("Custom ", "")])
    desc = spec["desc"].format(city=label, phone=ph)[:155]
    near = P.nearby(c, 6)
    nearlinks = "".join(f'<li><a href="{o["url"]}">{e(o["label"])}, TX</a></li>' for o in near)
    # rotate which types lead, so no two city pages open with the same card
    tlist = pick_many(spec["types"] + EP.EXTRA_TYPES[prod], slug, 6, 5)
    types = "".join(f'<div class="type-card reveal">{IC.icon_for(n)}'
                    f'<div class="pbody"><h3>{e(n)}</h3><p>{e(b)}</p></div></div>'
                    for n, b in tlist)
    intro = pick(BK.PC_INTROS, slug, 23).format(
        p=spec["label"] if spec["label"].endswith("s") else spec["label"] + "s",
        c=label)
    why_h, why_body = pick(V.WHY[prod], slug, 7)
    close = pick(V.CLOSE, slug, 13)
    shots = pick_many(IMG_POOL[prod], slug, 6, 3)
    # each shot gets its own alt; three identical strings on one page is
    # keyword repetition with no added meaning
    # six shots per page, so six templates: three cycled twice still left
    # every page with three duplicated alt strings
    _SHOT = ["{p} installed in a {c}, TX home by Love Is Blinds",
             "{p} fitted to the window opening in {c}, TX",
             "Close-up of {p} installed by Love Is Blinds in {c}, TX",
             "{p} measured and installed in {c}, TX",
             "{p} in a {c}, TX living space",
             "{p} on a wide window in {c}, TX"]
    gallery = "".join(
        f'<img src="{sh}" data-alt-final alt="{e(_SHOT[i % len(_SHOT)].format(p=spec["label"], c=label))}" '
        f'loading="lazy" width="600" height="450">' for i, sh in enumerate(shots))
    band = pick(IMG_POOL[prod], slug, 21)
    plist = pick_many(spec["price"], slug, len(spec["price"]), 17)
    prices = "".join(f"<li>{e(x)}</li>" for x in plist)

    faqs = [(f"Do you install {spec['label'].lower()} in {city}?",
             f"Yes. {leads} runs {terr['brand']}, which covers {city} along with {terr['blurb']}. "
             f"The person who measures your windows is the person who fits them. Call {ph}.")]
    faqs += pick_many(spec["faq"] + EP.EXTRA_FAQ[prod], slug, 5, 11)
    faqs.append((f"How much do {spec['label'].lower()} cost in {city}?",
                 "It depends on the size of the openings, the material and the options you choose. "
                 "We measure every opening on site and quote from those measurements, so the number "
                 "on your estimate is the number you pay. The consultation is free."))
    if c.get("street"):
        faqs.append((f"Where are you based near {city}?",
                     f"Our {c['locality']} location is at {c['street']}, {c['locality']}, TX "
                     f"{c.get('postal','')}".strip().rstrip(',') + ". Consultations happen at your "
                     "home, so most customers never need to visit us."))
    faqhtml = "".join(f"<details><summary>{e(q)}</summary><div class='a'>{e(a)}</div></details>"
                      for q, a in faqs)

    revs = P.BY_CITY.get(slug, [])[:3]
    reviews = ""
    if revs:
        cards = "".join('<div class="review reveal"><div class="stars">'
                        + "&#9733;" * int(r.get("rating", 5)) + "</div>"
                        + f'<p>"{e(r["quote"])}"</p><div class="who">{e(r["name"])}</div>'
                        + f'<div class="where">{e(city)}, TX</div></div>' for r in revs)
        reviews = (f'<section class="section"><div class="container center">'
                   f'<h2 class="title">What {e(city)} homeowners say</h2></div>'
                   f'<div class="container"><div class="reviews">{cards}</div></div></section>')

    others = "".join(
        f'<li><a href="/{PS.SPEC[o]["slug"]}-{slug}">{e(PS.SPEC[o]["label"])} in {e(city)}</a></li>'
        for o in PS.SPEC if o != prod)

    # every page of a product family shared one fixed hero, so all 48 blinds
    # pages looked identical. Rotate within a curated per-family pool instead.
    _hp = HERO_POOL[prod]
    hero = "/images/lib/" + pick(_hp, slug, 19)
    hero2 = "/images/lib/" + pick(_hp, slug, 29)
    if hero2 == hero:
        hero2 = "/images/lib/" + _hp[(_hp.index(pick(_hp, slug, 29)) + 1) % len(_hp)]
    nodes = [S.organization(BIZ), S.website(BIZ), S.business(BIZ), S.business(BIZ, c),
             S.webpage(url, title, desc, about=f"{S.SITE}{url}#business", primary=hero),
             S.breadcrumbs([("Home","/"),("Products","/products"),
                            (spec["label"], f"/products/{'plantation-shutters' if prod=='plantation-shutters' else 'blinds' if prod=='blinds' else 'shades' if prod=='shades' else 'shutters' if prod=='shutters' else 'exterior-patio-shades' if prod=='patio-shades' else 'motorized-window-treatment-automations'}"),
                            (f"{city}, TX", url)]),
             S.faq(url, faqs),
             S.service(url, f"{spec['label']} in {city}, TX",
                       f"Measurement, custom order and professional installation of "
                       f"{spec['label'].lower()} for homes in {city}, Texas.",
                       f"{S.SITE}{url}#business",
                       area={"@type":"City","name":c["locality"]},
                       catalog=[n for n,_ in spec["types"]])]
    body = f'''<section class="phero">
  <picture><img src="{hero}" alt="{e(spec['label'])} installed in {e(city)}, TX by Love Is Blinds" fetchpriority="high"></picture>
  <div class="container"><div class="phero-copy">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">&rsaquo;</span>
      <a href="{c['url']}">{e(city)}, TX</a><span class="sep">&rsaquo;</span>{e(spec['label'])}</nav>
    <h1 class="title">{e(spec['h1'])} in {e(label)}, Texas</h1>
    <p class="lead">{e(spec['lead'])} Free in-home consultation in {e(city)}.</p>
    <div class="hero-actions btnrow">
      <a class="btn btn-primary btn-lg" href="tel:{tel}">Call {e(ph)}</a>
      <a class="btn btn-secondary btn-lg" href="/schedule-now">Book your free consultation</a>
    </div>
  </div></div>
</section>

<section class="section">
  <div class="container split media-right">
    <div class="body reveal">
      <h2 class="title">{e(why_h)}</h2>
      <p>{e(intro)}</p>
      <p>{e(why_body)}</p>
      <ul class="feature-list">
        <li>{P.TICK}Free in-home consultation with samples you can hold against your own light</li>
        <li>{P.TICK}Every opening measured on site, not estimated</li>
        <li>{P.TICK}{e(city)} is covered by {e(terr['brand'])}, run by {P._leads_linked(terr)}</li>
        <li>{P.TICK}Remade at no cost if it does not match the approved measurements</li>
      </ul>
      <div class="btnrow"><a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a></div>
    </div>
    <div class="media reveal">
      <img src="{hero2}" width="900" height="600" loading="lazy"
           alt="{e(spec['label'])} in a {e(city)}, TX home">
    </div>
  </div>
</section>

<section class="section bg-cream-tint">
  <div class="container center"><h2 class="title">{e(spec['label'])} we install in {e(label)}</h2></div>
  <div class="container"><div class="prod-grid">{types}</div></div>
</section>

<section class="parallax-band" style="background-image:url('{band}')">
  <div class="container center">
    <span class="pb-eyebrow">Love Is Blinds &middot; {e(label)}</span>
    <h2 class="pb-title">{e(spec['label'])}, measured and installed in {e(label)} by {e(leads)}.</h2>
  </div>
</section>

<section class="section">
  <div class="container center">
    <h2 class="title">{e(spec["label"])} we have installed for Texas homes</h2>
    <p class="lead">{e(close)}</p>
  </div>
  <div class="container"><div class="city-gallery">{gallery}</div></div>
</section>

<section class="section">
  <div class="container split">
    <div class="body reveal">
      <h2 class="title">What moves the price of {e(spec["label"].lower())}</h2>
      <ul class="nap-list">{prices}</ul>
      <p>We measure the openings and quote from those measurements. The number on your estimate is
         the number you pay.</p>
      <div class="btnrow"><a class="btn btn-primary btn-lg" href="tel:{tel}">Call {e(ph)}</a></div>
    </div>
    <div class="body reveal">
      <h2 class="title">Other treatments we install in {e(city)}</h2>
      <ul class="nap-list">{others}</ul>
      <h2 class="title">{e(spec["label"])} near {e(city)}</h2>
      <ul class="nap-list">{nearlinks}</ul>
      <p><a class="btn-link" href="{c['url']}">All window treatments in {e(city)}
        <span class="arw">&rarr;</span></a></p>
    </div>
  </div>
</section>
{reviews}
<section class="section bg-cream-tint">
  <div class="container center"><h2 class="title">{e(spec['label'])} questions from {e(city)}</h2></div>
  <div class="container"><div class="faq">{faqhtml}</div></div>
</section>'''
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{S.SITE}{url}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#3A4D5C">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(BIZ['name'])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{S.SITE}{url}">
<meta property="og:image" content="{S.SITE}{hero}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="geo.region" content="US-TX">
<meta name="geo.placename" content="{e(c['locality'])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css">
{S.render(nodes)}
</head>
<body>
{HEAD_INNER}
<main>{body}
<section class="section closing-cta">
  <div class="container center">
    <h2 class="title">Get {e(spec["label"].lower())} priced for your windows</h2>
    <p class="lead">Free in-home consultation in {e(city)}. Measured by us, quoted in writing,
      installed by the same team.</p>
    <div class="btnrow" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a>
      <a class="btn btn-secondary btn-lg" href="tel:{tel}">Call {e(ph)}</a>
    </div>
  </div>
</section>
</main>
{P.FOOT}'''
    return url, doc

if __name__ == "__main__":
    n = 0
    for prod in PS.SPEC:
        for c in P.CITIES:
            url, doc = page(prod, c["slug"])
            open(url.lstrip("/") + ".html", "w").write(doc)
            n += 1
    print(f"wrote {n} product x city pages ({len(PS.SPEC)} products x {len(P.CITIES)} cities)")
