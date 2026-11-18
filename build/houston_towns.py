"""Render the North Houston town pages from hand-written copy.

Copy and photos live in build/houston_towns_copy.py, one entry per town.
This file only lays them out in the site's existing city-page design, so
every page shares the header, footer, form and guarantees but none of the
body copy, headings, FAQs or photos.

Also:
  * adds each town to data/tx.json ("custom": true, so pages.py and
    product_city.py leave these pages alone on a full rebuild)
  * writes the "Communities we serve" card section into the North Houston hub

Run from the repo root: python3 build/houston_towns.py
Then the usual passes (honeypot, dims, tags, sitemap, search_index,
schemafix, responsive) and extra.areas() for the areas page and map.
"""
import html, json, math, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(ROOT)
from houston_towns_copy import TOWNS, EXTRA

PHONE = "2818643309"

# --- 1. data/tx.json -------------------------------------------------------
d = json.load(open("data/tx.json"))
have = {c["slug"]: c for c in d["cities"]}
for t in TOWNS:
    rec = {"slug": t["slug"], "label": t["label"], "url": "/" + t["slug"], "phone": PHONE,
           "street": "", "locality": t["label"], "postal": "", "lat": t["lat"], "lng": t["lng"],
           "gbp": [], "twin": None, "geo_source": "town-center", "added": "2026-11", "custom": True}
    if t["slug"] in have:
        have[t["slug"]].update(rec)
    else:
        d["cities"].append(rec)
json.dump(d, open("data/tx.json", "w"), indent=1, ensure_ascii=False)

import pages as P, schema as S, icons as IC  # noqa: E402  (load after tx.json is updated)

e = lambda s: html.escape(s or "", quote=True)
BIZ = P.BIZ
TICK = P.TICK
ph, tel = S.pretty(PHONE), S.tel(PHONE)
HUB = P.BY["north-houston-tx"]
BYSLUG = {t["slug"]: t for t in TOWNS}


def miles(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a["lat"], a["lng"], b["lat"], b["lng"]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 3959 * 2 * math.asin(math.sqrt(h))


def near(t, n=6):
    return sorted((o for o in TOWNS if o["slug"] != t["slug"]), key=lambda o: miles(t, o))[:n]


def img(stem):
    return f"/images/lib/{stem}.webp"


def srcset(stem):
    return ", ".join(f"/images/lib/r/{w}/{stem}.webp {w}w" for w in (400, 800, 1600))


def fig(f):
    stem, alt, cap = f
    return (f'<figure class="post-figure town-figure"><img src="/images/lib/r/800/{stem}.webp" '
            f'data-alt-final alt="{e(alt)}" loading="lazy" width="800" height="600" '
            f'srcset="{srcset(stem)}" sizes="(max-width: 760px) 100vw, 560px">'
            f'<figcaption>{e(cap)}</figcaption></figure>')


def body_html(parts):
    out = []
    for x in parts:
        out.append(x if x.lstrip().startswith("<") else f"<p>{x}</p>")
    return "".join(out)


PRODUCTS = [
    ("Plantation Shutters", "/products/plantation-shutters", "shutters-shutters-091-jpg"),
    ("Custom Shades", "/products/shades", "roller-shades-roller-shades-230-jpg"),
    ("Custom Blinds", "/products/blinds", "blinds-blinds-009-jpg"),
    ("Exterior Patio Shades", "/products/exterior-patio-shades", "exterior-patio-shades-exterior-patio-shades-043-jpg"),
    ("Motorized Shades", "/products/motorized-window-treatment-automations", "smart-drapes-smart-drapes-010-jpg"),
    ("Honeycomb Shades", "/products/honeycomb-shades", "honeycomb-shades-honeycomb-shades-018-jpg"),
]


def render(t):
    c = P.BY[t["slug"]]
    url = c["url"]
    title = t["title"] if len(t["title"]) + 17 > 60 or "Love Is Blinds" in t["title"] else t["title"] + " | Love Is Blinds"
    desc = t["desc"]
    xh, xbody, xfaq = EXTRA[t["slug"]]
    faqs = t["faqs"] + [xfaq] + [(f"How much do window treatments cost in {t['label']}?",
                         "It depends on the size of each opening, the material and the options you choose. "
                         "We measure every opening on site and give you a written quote with installation "
                         "included. The consultation is free.")]
    hero_stem, hero_alt = t["hero"]
    m_stem, m_alt = t["media"]
    nodes = [
        S.organization(BIZ), S.website(BIZ), S.business(BIZ), S.business(BIZ, c),
        S.webpage(url, title, desc, about=f"{S.SITE}{url}#business", primary=img(hero_stem)),
        S.breadcrumbs([("Home", "/"), ("Service Areas", "/areas-we-serve"),
                       ("North Houston", "/north-houston-tx"), (f"{t['label']}, TX", url)]),
        S.faq(url, faqs),
        S.service(url, f"Custom Window Treatments in {t['label']}, TX",
                  f"Measurement, custom order and professional installation of blinds, shades, "
                  f"shutters and exterior patio shades for homes in {t['label']}, Texas.",
                  f"{S.SITE}{url}#business",
                  area={"@type": "City", "name": t["label"]},
                  catalog=[p[0] for p in PRODUCTS]),
    ]
    head = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{S.SITE}{url}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#3A4D5C">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(BIZ['name'])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{S.SITE}{url}">
<meta property="og:image" content="{S.SITE}{img(hero_stem)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{S.SITE}{img(hero_stem)}">
<meta name="geo.region" content="US-TX">
<meta name="geo.placename" content="{e(t['label'])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css">
<style>.town-copy h2+p,.town-copy h2+ul{{margin-top:14px}}.town-copy p+p,.town-copy p+ul,.town-copy ul+p{{margin-top:14px}}.town-copy ul:not(.feature-list){{padding-left:1.2em;list-style:disc}}.town-copy ul:not(.feature-list) li{{margin:8px 0}}</style>
{S.render(nodes)}
</head>'''

    form = (
        '<form class="city-form" action="https://formspree.io/f/xyezwzlb" method="POST">'
        f'<input type="hidden" name="_subject" value="New consultation request - {e(t["label"])}, TX">'
        f'<input type="hidden" name="city" value="{e(t["label"])}, TX">'
        '<p class="cf-lede">Prefer to write? Send this and your local team replies within one business day.</p>'
        '<div class="cf-grid">'
        '<label>Name<input type="text" name="name" required autocomplete="name"></label>'
        '<label>Phone<input type="tel" name="phone" required autocomplete="tel"></label>'
        '<label>Email<input type="email" name="email" required autocomplete="email"></label>'
        '<label>ZIP code<input type="text" name="zip" required inputmode="numeric" pattern="\\d{5}(-\\d{4})?" autocomplete="postal-code"></label>'
        '<label>What are you considering?<select name="considering">'
        '<option>Not sure yet</option><option>Blinds</option><option>Shades</option>'
        '<option>Plantation shutters</option><option>Exterior patio shades</option>'
        '<option>Motorization</option></select></label>'
        '</div>'
        '<button class="btn btn-primary btn-block" type="submit">Request my free consultation</button>'
        '<p class="cf-fine">No pressure, no obligation. We never share your information.</p>'
        '</form>')

    secs = []
    for i, (h, paras, f) in enumerate(t["sections"]):
        side = "media-right" if i % 2 == 0 else "media-left"
        bg = " bg-cream-tint" if i % 2 == 1 else ""
        secs.append(
            f'<section class="section{bg}"><div class="container split {side}">'
            f'<div class="body reveal town-copy"><h2 class="title">{e(h)}</h2>{body_html(paras)}</div>'
            f'<div class="media reveal">{fig(f)}</div></div></section>')

    links = " ".join(f'<a class="btn btn-secondary" href="{u}">{e(n)}</a>' for n, u in t["links"])
    prods = "".join(
        f'<a class="prod-card reveal" href="{u}"><span class="pic"><img src="{img(s)}" '
        f'alt="{e(n)} from Love Is Blinds, available in {e(t["label"])}, TX" loading="lazy" '
        f'width="2000" height="1500"></span><span class="pbody"><h3>{e(n)}</h3>'
        f'<span class="btn-link">See {e(n.lower())} <span class="arw">&rarr;</span></span></span></a>'
        for n, u, s in PRODUCTS)
    chips = " ".join(f'<a class="chip" href="/{o["slug"]}">{e(o["label"])}, TX</a>' for o in near(t)) \
        + ' <a class="chip" href="/north-houston-tx">All of North Houston</a>'
    gloss = {"Limited Lifetime Warranty": "manufacturer coverage for factory defects",
             "Apples-to-Apples": "a price-match guarantee",
             "Our GuaranTEN": "one free replacement for every ten treatments",
             "Here-4-You": "four years of service visits at no cost",
             "Transferable Warranty": "coverage that transfers if you sell"}
    gtee = "".join(f'<li>{TICK}<span><strong>{e(g["name"])}:</strong> {e(gloss.get(g["name"], ""))}</span></li>'
                   for g in P.GUARANTEES)
    faqhtml = "".join(f'<details><summary>{e(q)}</summary><div class="a">{e(a)}</div></details>'
                      for q, a in faqs)
    rd_t, rd_u = t["read"]
    map_src = f"https://www.google.com/maps?q={t['label'].replace(' ', '+')},+TX&output=embed"

    body = f'''<body>
{P.HEAD.split('<body', 1)[1].split('>', 1)[1]}
<main>
<section class="phero">
  <picture><img src="{img(hero_stem)}" alt="{e(hero_alt)}" width="2000" height="1500" fetchpriority="high"></picture>
  <div class="container">
    <div class="phero-copy">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">&rsaquo;</span><a href="/areas-we-serve">Service Areas</a><span class="sep">&rsaquo;</span><a href="/north-houston-tx">North Houston</a><span class="sep">&rsaquo;</span>{e(t['label'])}, TX</nav>
      <h1 class="title">Blinds, Shades and Shutters in {e(t['label'])}, Texas</h1>
      <p class="lead">{e(t['lead'])}</p>
      <div class="hero-actions btnrow">
        <a class="btn btn-primary btn-lg" href="tel:{tel}">Call {e(ph)}</a>
        <a class="btn btn-secondary btn-lg" href="/schedule-now">Book your free consultation</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split media-right">
    <div class="body reveal town-copy">
      <h2 class="title">Window treatments for {e(t['label'])} homes</h2>
      {body_html(t['intro'])}
      <ul class="feature-list">
        <li>{TICK}Free in-home consultation with samples you can hold against your own light</li>
        <li>{TICK}Every opening measured on site before anything is ordered</li>
        <li>{TICK}Measured and installed by the same local North Houston team</li>
        <li>{TICK}Remade at no cost if a treatment does not match the approved measurements</li>
      </ul>
      {form}
    </div>
    <div class="media reveal">
      <img src="/images/lib/r/800/{m_stem}.webp" data-alt-final alt="{e(m_alt)}" width="900" height="600" loading="lazy" srcset="{srcset(m_stem)}" sizes="(max-width: 760px) 100vw, 560px">
    </div>
  </div>
</section>

{"".join(secs)}

<section class="section"><div class="container town-copy" style="max-width:820px">
  <h2 class="title">{e(xh)}</h2>{body_html(xbody)}
</div></section>

<section class="section">
  <div class="container center">
    <h2 class="title">Where to start in {e(t['label'])}</h2>
    <p class="lead">Most {e(t['label'])} consultations start with these. For more detail, read <a href="{rd_u}">{e(rd_t)}</a>.</p>
    <div class="btnrow" style="justify-content:center;margin-top:18px">{links}</div>
  </div>
</section>

<section class="section bg-cream-tint">
  <div class="container center"><h2 class="title">Everything we install in {e(t['label'])}</h2></div>
  <div class="container"><div class="prod-grid prod-grid-6">{prods}</div></div>
</section>

<section class="section contact-band">
  <div class="container contact-cols">
    <div class="contact-card reveal">
      <h2 class="title">Talk to your North Houston team</h2>
      <ul class="cc-rows">
        <li><span class="cc-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/></svg></span>
          <span><span class="cc-label">Call your local team</span><a class="cc-value" href="tel:{tel}">{e(ph)}</a></span></li>
        <li><span class="cc-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/></svg></span>
          <span><span class="cc-label">Service area</span><span class="cc-value">{e(t['label'])} and North Houston</span></span></li>
        <li><span class="cc-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span>
          <span><span class="cc-label">Prefer to write</span><a class="cc-value" href="/schedule-now">Send us a message</a></span></li>
      </ul>
      <div class="btnrow"><a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a></div>
    </div>
    <div class="contact-side reveal">
      <div class="map-card">
        <iframe src="{map_src}" title="Map of {e(t['label'])}, TX" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
        <span class="map-gbp">Serving {e(t['label'])} and the North Houston area</span>
      </div>
      <h2 class="title" style="margin-top:26px">Nearby towns we serve</h2>
      <div class="chips" style="margin-top:14px">{chips}</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container town-copy" style="max-width:820px"><h2 class="title">Backed five ways</h2>
    <ul class="feature-list">{gtee}</ul>
    <p><a class="btn-link" href="/installation-standards">How we install and what is covered <span class="arw">&rarr;</span></a></p></div>
</section>

<section class="section bg-cream-tint">
  <div class="container center"><h2 class="title">{e(t['label'])} window treatment questions</h2></div>
  <div class="container"><div class="faq">{faqhtml}</div></div>
</section>

<section class="section closing-cta">
  <div class="container center">
    <h2 class="title">Book a free consultation in {e(t['label'])}</h2>
    <p class="lead">Samples at your door, every opening measured, and a written quote before you decide anything.</p>
    <div class="btnrow" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a>
      <a class="btn btn-secondary btn-lg" href="tel:{tel}">Call {e(ph)}</a>
    </div>
  </div>
</section>
</main>
{P.FOOT}'''
    return head + "\n" + body


for t in TOWNS:
    open(t["slug"] + ".html", "w", encoding="utf-8").write(render(t))

# --- hub: communities section --------------------------------------------
hub_path = "north-houston-tx.html"
h = open(hub_path, encoding="utf-8").read()
h = re.sub(r"\n?<!-- nhou:towns -->.*?<!-- /nhou:towns -->\n?", "\n", h, flags=re.S)
cards = "".join(
    f'<a class="prod-card reveal" href="/{t["slug"]}"><span class="pic"><img src="/images/lib/r/800/{t["hero"][0]}.webp" '
    f'alt="{e(t["hero"][1])}" loading="lazy" width="800" height="600"></span>'
    f'<span class="pbody"><h3>{e(t["label"])}, TX</h3><p>{e(t["lead"])}</p>'
    f'<span class="btn-link">{e(t["label"])} window treatments <span class="arw">&rarr;</span></span></span></a>'
    for t in sorted(TOWNS, key=lambda x: x["label"]))
block = ('\n<!-- nhou:towns --><section class="section"><div class="container center">'
         '<h2 class="title">Communities we serve around North Houston</h2>'
         '<p class="lead">Each town page covers the window problems we see most there, with the '
         'products that solve them.</p></div>'
         f'<div class="container"><div class="prod-grid">{cards}</div></div></section><!-- /nhou:towns -->\n')
anchor = '<section class="section bg-cream-tint">\n  <div class="container center"><h2 class="title">North Houston questions, answered</h2>'
assert anchor in h, "hub FAQ anchor not found"
h = h.replace(anchor, block + anchor, 1)
open(hub_path, "w", encoding="utf-8").write(h)
print(f"houston_towns: wrote {len(TOWNS)} town pages and the hub communities section")

# --- hub: no photo claims a North Houston location ------------------------
# The franchise is new; every photo is a real install by another Texas team.
h = open(hub_path, encoding="utf-8").read()
h = h.replace("Recent work around North Houston", "Recent work from Love Is Blinds teams")
h = h.replace('shot-where">North Houston, TX<', 'shot-where">Love Is Blinds Texas<')
h = re.sub(r'alt="([^"]*?) (?:installed|fitted) (?:by Love Is Blinds )?in North Houston, TX(?: by Love Is Blinds)?"',
           lambda m: f'alt="{m.group(1)} from Love Is Blinds for North Houston homes"', h)
h = h.replace('alt="Custom window treatments in North Houston, TX by Love Is Blinds"',
              'alt="Custom window treatments from Love Is Blinds for North Houston homes"')
open(hub_path, "w", encoding="utf-8").write(h)
