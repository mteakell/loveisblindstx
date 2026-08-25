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

HEROES = [
 "blinds-blinds-001-jpg.webp","shutters-shutters-004-jpg.webp","roller-shades-roller-shades-001-jpg.webp",
 "honeycomb-shades-honeycomb-shades-001-jpg.webp","roman-shades-roman-shades-001-jpg.webp",
 "blinds-blinds-005-jpg.webp","shutters-shutters-006-jpg.webp","roller-shades-roller-shades-004-jpg.webp",
 "smart-drapes-smart-drapes-002-jpg.webp","shutters-shutters-008-jpg.webp",
 "honeycomb-shades-honeycomb-shades-008-jpg.webp","roman-shades-roman-shades-005-jpg.webp",
]
def hero_for(c):
    return "/images/lib/" + HEROES[sum(ord(x) for x in c["slug"]) % len(HEROES)]

TICK = ('<span class="tick"><svg viewBox="0 0 24 24">'
        '<path d="m20 6-11 11-5-5"/></svg></span>')

PRODUCTS = [
 ("Plantation Shutters","/products/plantation-shutters","Louvered shutters built to the window opening."),
 ("Custom Blinds","/products/blinds","Real wood, faux wood and composite blinds."),
 ("Roller Shades","/products/roller-shades","Solar screen and blackout roller shades."),
 ("Honeycomb Shades","/products/honeycomb-shades","Cellular shades that cut heat transfer at the glass."),
 ("Motorization","/products/motorized-window-treatment-automations","App, remote and voice control."),
 ("Exterior Patio Shades","/products/exterior-patio-shades","Shade for porches, patios and outdoor rooms."),
]
def e(s): return html.escape(s or "", quote=True)

def _leads(terr):
    L = terr["leads"]
    return L[0] if len(L) == 1 else " and ".join([", ".join(L[:-1]), L[-1]])

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

def title_for(c):
    if c.get("variant"):
        return f"Custom Blinds & Shutters in {c['label']}, TX | {c['variant']}"
    t = f"Custom Blinds, Shades & Shutters in {c['label']}, TX | Love Is Blinds"
    if len(t) > 62:
        t = f"Blinds, Shades & Shutters in {c['label']}, TX | Love Is Blinds"
    if len(t) > 62:
        t = f"Window Treatments in {c['label']}, TX | Love Is Blinds"
    if len(t) > 62:
        t = f"Blinds & Shutters in {c['label']}, TX | Love Is Blinds"
    return t

def meta_for(c):
    """Unique, under 155 chars, and it leads with the number that actually rings."""
    ph = S.pretty(c["phone"]) or BIZ["phone"]
    loc = c["label"]
    if c.get("variant"):
        return (f"Custom blinds, shades and shutters from our {c['variant']} location in {loc}, "
                f"TX. Free in-home measure and installation. Call {ph}.")
    if c.get("street"):
        base = (f"Custom blinds, shades and plantation shutters in {loc}, TX. "
                f"Free in-home consultation and professional installation. Call {ph}.")
    else:
        terr = T.of(c["slug"])["name"]
        base = (f"Custom blinds, shades and plantation shutters for {loc}, TX homes. "
                f"Free in-home measure across {terr}. Call {ph}.")
    if len(base) > 155:
        base = (f"Custom blinds, shades and shutters in {loc}, TX. "
                f"Free in-home consultation and installation. Call {ph}.")
    return base

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
                  catalog=[p[0] for p in PRODUCTS]),
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
    prods = "".join(
      f'<a class="prod-card reveal" href="{u}"><div class="pbody"><h3>{e(n)}</h3>'
      f'<p>{e(d)}</p><span class="btn-link">See {e(n.lower())} <span class="arw">&rarr;</span></span>'
      f'</div></a>' for n,u,d in PRODUCTS)
    nearlinks = " ".join(
      f'<li><a href="{o["url"]}">{e(o["label"])}, TX</a></li>' for o in near)
    faqhtml = "".join(
      f'<div class="a"><h3>{e(q)}</h3><p>{e(a)}</p></div>' for q,a in faqs_for(c))
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
        <li>{TICK}{e(c['label'])} is covered by {e(terr['brand'])}, run by {e(_leads(terr))}</li>
        <li>{TICK}Remade at no cost if a treatment does not match the approved measurements</li>
      </ul>
      <div class="btnrow"><a class="btn btn-primary btn-lg" href="/contact">Book your free consultation</a></div>
    </div>
    <div class="media reveal">
      <img src="{hero2}" width="900" height="600" loading="lazy"
           alt="Custom window treatments installed by Love Is Blinds">
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
        <li class="contact-line"><a href="mailto:{BIZ['email']}">{BIZ['email']}</a></li>
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
