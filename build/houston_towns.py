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
import hashlib
CITY_V = hashlib.md5(open("css/city.css","rb").read()).hexdigest()[:10]

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


PRODUCT_LINKS = [("Roller and solar shades", "/products/roller-shades"), ("Roman shades", "/products/roman-shades"),
                 ("Woven wood shades", "/products/woven-wood-shades"), ("Faux wood blinds", "/products/faux-wood-blinds"),
                 ("Dual and zebra shades", "/products/dual-shades"), ("Panel track shades", "/products/panel-track-shades"),
                 ("Drapery", "/services/drapery-installation"), ("Exterior patio shades", "/products/exterior-patio-shades"),
                 ("Plantation shutters", "/products/plantation-shutters"), ("Honeycomb shades", "/products/honeycomb-shades")]

PRODUCTS = [
    ("Plantation Shutters", "/products/plantation-shutters", "shutters-shutters-091-jpg"),
    ("Custom Shades", "/products/shades", "roller-shades-roller-shades-230-jpg"),
    ("Custom Blinds", "/products/blinds", "blinds-blinds-009-jpg"),
    ("Exterior Patio Shades", "/products/exterior-patio-shades", "exterior-patio-shades-exterior-patio-shades-043-jpg"),
    ("Motorized Shades", "/products/motorized-window-treatment-automations", "smart-drapes-smart-drapes-010-jpg"),
    ("Honeycomb Shades", "/products/honeycomb-shades", "honeycomb-shades-honeycomb-shades-018-jpg"),
]


KEYS = {"patio": ["patio", "porch", "outdoor", "exterior"], "roller": ["roller", "solar"], "solar": ["solar", "roller"],
        "woven": ["woven"], "roman": ["roman"], "honeycomb": ["cellular", "honeycomb"], "cellular": ["cellular"],
        "shutter": ["shutter"], "faux": ["faux"], "real wood": ["real wood"], "panel": ["panel track", "slider", "sliding"],
        "dual": ["dual", "zebra"], "motoriz": ["motor"], "drapery": ["drapery"], "blinds": ["blind"],
        "french": ["french door"], "sliding": ["slider", "sliding"], "heat": ["heat", "sun"], "child": ["cordless", "child"],
        "energy": ["insulat", "heat"], "shades": ["shade"]}


OVERRIDE = {("pinehurst-tx", 1): ("Light filtering shades", "/products/shades"),
            ("shenandoah-tx", 0): ("Blackout roller shades", "/products/roller-shades"),
            ("willis-tx", 2): ("Energy-efficient shades", "/products/energy-efficient-custom-window-shades")}


def pick_link(t, sec, i):
    if (t["slug"], i) in OVERRIDE:
        return OVERRIDE[(t["slug"], i)]
    h, paras, f = sec
    text = (h + " " + " ".join(paras)).lower()
    best, score = None, 0
    for name, url in t["links"] + PRODUCT_LINKS:
        ks = [w for k, ws in KEYS.items() if k in name.lower() for w in ws]
        sc = sum(text.count(w) for w in ks) + (2 if h.lower().split()[0] in name.lower() else 0)
        if sc > score:
            best, score = (name, url), sc
    return best or t["links"][i % len(t["links"])]


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
<link rel="stylesheet" href="/css/city.css?v={CITY_V}">
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

    ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6">'
             '<path d="M7 17 17 7M8 7h9v9"/></svg>')
    gloss = {"Limited Lifetime Warranty": "Manufacturer coverage for factory defects.",
             "Apples-to-Apples": "A price-match guarantee.",
             "Our GuaranTEN": "One free replacement for every ten treatments.",
             "Here-4-You": "Four years of service visits at no cost.",
             "Transferable Warranty": "Coverage transfers if you sell."}

    def chapter(i, sec):
        h, paras, (stem, alt, cap) = sec
        kind = ["wide", "flip", "small"][i % 3]
        pname, purl = pick_link(t, sec, i)
        return (
            f'<section class="cx-ch {kind}"><div class="wrap">'
            f'<div class="cx-ch-text cx-rv"><div class="cx-num">0{i+1}</div>'
            f'<div class="cx-eyebrow">{e(pname)}</div><h2>{e(h)}</h2>{body_html(paras)}'
            f'<a class="cx-link" href="{purl}">See {e(pname.lower())} {ARROW}</a></div>'
            f'<figure class="cx-ch-media cx-rv" style="margin-left:0;margin-right:0">'
            f'<div class="cx-par cx-frame" data-par="0.10"><img src="/images/lib/r/1600/{stem}.webp" '
            f'data-alt-final alt="{e(alt)}" loading="lazy" width="1600" height="1200" '
            f'srcset="{srcset(stem)}" sizes="(max-width: 900px) 100vw, 50vw"></div>'
            f'<figcaption class="cx-cap"><span>{e(cap)}</span><span>{e(t["label"])}, TX homes</span></figcaption>'
            f'</figure></div></section>')

    chapters = "".join(chapter(i, sec) for i, sec in enumerate(t["sections"]))
    rules = "".join(f'<li><b>0{i+1}</b><span>{x}</span></li>' for i, x in enumerate([
        "Free in-home consultation with samples you can hold against your own light",
        "Every opening measured on site before anything is ordered",
        "Measured and installed by the same local North Houston team",
        "Remade at no cost if a treatment does not match the approved measurements"]))
    start_urls = {u for _, u in t["links"]}
    plist = "".join(
        f'<a href="{u}"><img src="/images/lib/r/400/{s}.webp" alt="" loading="lazy" width="96" height="72">'
        f'<span>{e(n)}</span>{ARROW}</a>' for n, u, s in PRODUCTS)
    starts = "".join(
        f'<a class="start" href="{u}"><img src="/images/lib/r/400/{st}.webp" alt="" loading="lazy" width="96" height="72">'
        f'<span><small>Start here in {e(t["label"])}</small>{e(n)}</span>{ARROW}</a>'
        for (n, u), st in zip(t["links"], [x[2][0] for x in t["sections"]]))
    plist = starts + "".join(
        f'<a href="{u}"><img src="/images/lib/r/400/{s}.webp" alt="" loading="lazy" width="96" height="72">'
        f'<span>{e(n)}</span>{ARROW}</a>' for n, u, s in PRODUCTS if u not in start_urls)
    near_li = "".join(
        f'<li><a href="/{o["slug"]}">{e(o["label"])}, TX <em>{round(miles(t, o))} mi</em></a></li>'
        for o in near(t, 5)) + '<li><a href="/north-houston-tx">All of North Houston <em>14 towns</em></a></li>'
    trust = "".join(f'<div><b>{e(g["name"])}</b><span>{e(gloss.get(g["name"], ""))}</span></div>'
                    for g in P.GUARANTEES)
    faqhtml = "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faqs)
    rd_t, rd_u = t["read"]
    map_src = f"https://www.google.com/maps?q={t['label'].replace(' ', '+')},+TX&output=embed"
    plan = body_html(xbody)

    body = f"""<body>
{P.HEAD.split('<body', 1)[1].split('>', 1)[1]}
<main class="cx">
<section class="cx-hero cx-par" data-par="0.18">
  <img src="{img(hero_stem)}" alt="{e(hero_alt)}" width="2000" height="1500" fetchpriority="high" srcset="{srcset(hero_stem)}, {img(hero_stem)} 2000w" sizes="100vw">
  <nav class="cx-crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/areas-we-serve">Service Areas</a><span>/</span><a href="/north-houston-tx">North Houston</a><span>/</span>{e(t['label'])}, TX</nav>
  <div class="wrap"><div class="cx-hero-row">
    <div>
      <div class="cx-eyebrow" style="color:#fff;opacity:.85">Love Is Blinds &middot; North Houston</div>
      <h1>Blinds, Shades and Shutters in {e(t['label'])}, Texas</h1>
      <p class="cx-lead">{e(t['lead'])}</p>
      <div class="cx-actions">
        <a class="cx-btn cx-btn-light" href="tel:{tel}">Call {e(ph)}</a>
        <a class="cx-btn cx-btn-line" href="#consult">Book a free consultation</a>
      </div>
    </div>
    <div class="cx-hero-tag"><i></i>Scroll</div>
  </div></div>
</section>

<section class="cx-intro"><div class="wrap">
  <div class="cx-rv"><div class="cx-eyebrow">Window treatments for {e(t['label'])} homes</div>
    <p class="cx-statement" style="margin-top:18px">{t['intro'][0]}</p></div>
  <div class="cx-rv"><p>{t['intro'][1]}</p><ul class="cx-rules">{rules}</ul>
    <a class="cx-link" href="#consult">Book your free consultation {ARROW}</a></div>
</div></section>

{chapters}

<section class="cx-band cx-par" data-par="0.16">
  <img src="/images/lib/r/1600/{m_stem}.webp" data-alt-final alt="{e(m_alt)}" loading="lazy" width="1600" height="1200" srcset="{srcset(m_stem)}" sizes="100vw">
  <div class="wrap"><div class="cx-eyebrow">{e(t['label'])}, Texas</div><h2>{e(xh)}</h2></div>
</section>

<section class="cx-plan"><div class="wrap">
  <div class="cx-rv"><div class="cx-eyebrow">Planning the house</div>
    <p style="margin-top:18px">Every plan starts at your windows, with samples in your own light. For more detail, read <a href="{rd_u}">{e(rd_t)}</a>.</p>
    <a class="cx-link" href="#consult">Plan yours with us {ARROW}</a></div>
  <div class="cx-rv">{plan}</div>
</div></section>

<section class="cx-prod"><div class="wrap">
  <div class="cx-prod-head cx-rv"><div><div class="cx-eyebrow">What we install</div><h2 style="margin-top:12px">Everything we fit in {e(t['label'])}</h2></div>
    <p>Each is measured on site and built to the opening, then installed by the team that measured it.</p></div>
  <div class="cx-plist cx-rv">{plist}</div>
</div></section>

<section class="cx-trust"><div class="wrap">{trust}</div></section>

<section class="cx-area"><div class="wrap">
  <iframe class="cx-map cx-rv" src="{map_src}" title="Map of {e(t['label'])}, TX" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
  <div class="cx-rv"><div class="cx-eyebrow">Service area</div><h2 style="margin-top:12px">{e(t['label'])} and the towns around it</h2>
    <ul class="cx-near">{near_li}</ul></div>
</div></section>

<section class="cx-faq"><div class="wrap">
  <div class="cx-rv"><div class="cx-eyebrow">Questions</div><h2 style="margin-top:12px">{e(t['label'])} window treatment questions</h2></div>
  <div class="cx-rv">{faqhtml}</div>
</div></section>

<section class="cx-close" id="consult">
  <div class="cx-close-dark">
    <div><div class="cx-eyebrow" style="color:var(--pop)">Free in-home consultation</div>
      <h2 style="margin-top:14px">Book a free consultation in {e(t['label'])}</h2>
      <p>Samples at your door, every opening measured, and a written quote with installation included before you decide anything.</p></div>
    <div><small>Call your North Houston team</small><a class="cx-phone" href="tel:{tel}">{e(ph)}</a></div>
  </div>
  <div class="cx-close-form">{form}</div>
</section>
</main>
<script>(function(){{
var els=[].slice.call(document.querySelectorAll('.cx-par'));
var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches||innerWidth<900;
if(!reduce&&els.length){{var tick=false;function run(){{tick=false;var vh=innerHeight;
els.forEach(function(el){{var r=el.getBoundingClientRect();if(r.bottom<0||r.top>vh)return;
var k=parseFloat(el.getAttribute('data-par'))||.12;var c=(r.top+r.height/2-vh/2);
var im=el.querySelector('img');if(im)im.style.transform='translate3d(0,'+(-c*k).toFixed(1)+'px,0)';}});}}
addEventListener('scroll',function(){{if(!tick){{tick=true;requestAnimationFrame(run);}}}},{{passive:true}});addEventListener('resize',run);run();}}
var rv=[].slice.call(document.querySelectorAll('.cx-rv'));
if('IntersectionObserver' in window){{var io=new IntersectionObserver(function(es){{es.forEach(function(x){{if(x.isIntersecting){{x.target.classList.add('in');io.unobserve(x.target);}}}});}},{{rootMargin:'0px 0px -8% 0px'}});rv.forEach(function(x){{io.observe(x);}});}}
else rv.forEach(function(x){{x.classList.add('in');}});
}})();</script>
{P.FOOT}"""
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
