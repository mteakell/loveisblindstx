"""City-level exterior patio shade pages.

Justified by real demand rather than spun for coverage: local patio terms run
KD 0-21 and the account has no patio ranking at all. Only cities with measured
volume get a page, and each carries its own operator, phone, neighbours, sun
angle framing and FAQ so none of them is a doorway page.
"""
import html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import schema as S, territory as T, pages as P

ROOT = P.ROOT
os.chdir(ROOT)
BIZ = P.BIZ
KW = json.load(open("data/patio-cities.json"))["cities"]
HEAD_INNER = P.HEAD.split("<body", 1)[1].split(">", 1)[1]
e = lambda s: html.escape(s or "", quote=True)

TYPES = [
 ("Solar screen shades",
  "An open weave that cuts glare and heat while you keep the view out to the yard. The default "
  "choice for a covered patio taking hard afternoon sun."),
 ("Motorized patio shades",
  "Remote, wall switch, app or a schedule. On a wide span this is what makes the shades get used, "
  "and it is how you raise them quickly when the wind turns."),
 ("Retractable shades",
  "Roll up out of the weather when the space is not in use, which keeps fabric out of wind and "
  "hail and extends its working life."),
 ("Track guided patio screens",
  "The fabric runs in channels at each side so it does not billow, and the edges seal. Worth it on "
  "an exposed site or where you also want insect control."),
 ("Exterior solar shades for windows",
  "Not every opening is a patio. Solar shades mounted outside the glass stop heat before it enters, "
  "which drops the cooling load on that wall."),
]

def page(slug):
    c = P.BY[slug]
    city = c["label"]
    terr = T.of(slug)
    ph = S.pretty(c["phone"]) or BIZ["phone"]
    tel = S.tel(c["phone"] or BIZ["tel"])
    leads = P._leads(terr)
    url = f"/patio-shades-{slug}"
    title = f"Patio Shades in {city}, TX | Exterior & Motorized"
    if len(title) > 60:
        title = f"Patio Shades in {city}, TX | Love Is Blinds"
    if len(title) > 60:
        title = f"Patio Shades in {city}, TX"
    desc = (f"Exterior patio shades, motorized patio screens and solar shades for {city}, TX "
            f"patios and porches. Free in-home measure. Call {ph}.")[:155]
    near = [o for o in P.nearby(c, 6)]
    nearlinks = "".join(f'<li><a href="{o["url"]}">{e(o["label"])}, TX</a></li>' for o in near)
    types = "".join(f'<div class="prod-card reveal"><div class="pbody"><h3>{e(n)}</h3>'
                    f'<p>{e(b)}</p></div></div>' for n, b in TYPES)
    faqs = [
      (f"Do you install exterior patio shades in {city}?",
       f"Yes. Patio shades, outdoor roller shades and motorized patio screens are a core part of "
       f"what we install in {city}. {leads} runs {terr['brand']}, which covers {city} along with "
       f"{terr['blurb']}. Call {ph} to book a free measure."),
      (f"How much do patio shades cost in {city}?",
       "It depends on the span, the fabric openness, and whether you motorize. Patio openings are "
       "wide, so span drives the number more than anything else. We measure the opening and quote "
       "from those measurements, so the figure you get is the figure you pay."),
      ("What openness factor should I choose?",
       "It depends which way the space faces. A west facing patio taking full afternoon sun wants a "
       "tighter weave. A north facing porch can take a more open one and keep more of the view. We "
       "go through this on site with samples you can hold up in your own light."),
      ("Should I motorize them?",
       "On a wide span, usually yes. A large exterior shade is heavy to crank by hand, and "
       "motorized shades come up far faster when the wind turns, which is what protects the fabric."),
      ("Will they hold up to Texas weather?",
       "Exterior shades should be retracted in high wind. We size the hardware to the opening and "
       "go over the wind guidance at the consultation. Retractable and motorized options make it "
       "practical to actually bring them up when weather turns."),
      (f"How long does a patio shade order take in {city}?",
       "Most custom orders arrive within two to four weeks of approval. Motorized treatments can "
       "run longer. We confirm the timeline in writing on your quote."),
    ]
    faqhtml = "".join(f"<details><summary>{e(q)}</summary><div class='a'>{e(a)}</div></details>"
                      for q, a in faqs)
    hero = "/images/lib/exterior-patio-shades-exterior-patio-shades-001-jpg.webp"
    nodes = [S.organization(BIZ), S.website(BIZ), S.business(BIZ), S.business(BIZ, c),
             S.webpage(url, title, desc, about=f"{S.SITE}{url}#business", primary=hero),
             S.breadcrumbs([("Home", "/"), ("Products", "/products"),
                            ("Exterior Patio Shades", "/products/exterior-patio-shades"),
                            (f"{city}, TX", url)]),
             S.faq(url, faqs),
             S.service(url, f"Exterior Patio Shade Installation in {city}, TX",
                       f"Measurement, custom order and installation of exterior patio shades, "
                       f"outdoor roller shades and motorized patio screens for {city}, Texas.",
                       f"{S.SITE}{url}#business",
                       area={"@type": "City", "name": c["locality"]},
                       catalog=[n for n, _ in TYPES])]
    body = f'''<section class="phero">
  <picture><img src="{hero}" alt="Exterior patio shades installed in {e(city)}, TX by Love Is Blinds" fetchpriority="high"></picture>
  <div class="container"><div class="phero-copy">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">&rsaquo;</span>
      <a href="/products/exterior-patio-shades">Patio Shades</a><span class="sep">&rsaquo;</span>{e(city)}, TX</nav>
    <h1 class="title">Exterior Patio Shades in {e(city)}, Texas</h1>
    <p class="lead">Outdoor shades that stop the sun before it reaches the glass, so a west facing
      patio in {e(city)} is still usable at five in the afternoon. Measured, built to the opening
      and installed by our own team.</p>
    <div class="hero-actions btnrow">
      <a class="btn btn-primary btn-lg" href="tel:{tel}">Call {e(ph)}</a>
      <a class="btn btn-secondary btn-lg" href="/schedule-now">Book a free measure</a>
    </div>
  </div></div>
</section>

<section class="section">
  <div class="container split media-right">
    <div class="body reveal">
      <h2 class="title">Why exterior beats interior on a {e(city)} patio</h2>
      <p>An interior blind stops light after the sun has already come through the glass and heated
         the room. An exterior shade stops it before it gets there. On a west wall in a Texas summer
         that is the entire difference, and it is why a covered patio with exterior shades stays
         usable in the afternoon while an unshaded one does not.</p>
      <p>Shading the patio also shades the wall and the glass behind it, so the rooms on that side
         take less heat load. Most people buy patio shades for the outdoor space and are surprised
         by what it does indoors.</p>
      <ul class="feature-list">
        <li>{P.TICK}Openness factor chosen for the way your patio faces</li>
        <li>{P.TICK}Solar screen, motorized, retractable and track guided options</li>
        <li>{P.TICK}{e(city)} is covered by {e(terr['brand'])}, run by {e(leads)}</li>
        <li>{P.TICK}Measured and installed by the same team that quotes it</li>
      </ul>
      <div class="btnrow">
        <a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a>
      </div>
    </div>
    <div class="media reveal">
      <img src="/images/lib/exterior-patio-shades-exterior-patio-shades-003-jpg.webp"
           width="900" height="600" loading="lazy"
           alt="Motorized exterior patio shades on a covered patio in {e(city)}, TX">
    </div>
  </div>
</section>

<section class="section bg-cream-tint">
  <div class="container center"><h2 class="title">What we install on {e(city)} patios</h2></div>
  <div class="container"><div class="prod-grid">{types}</div></div>
</section>

<section class="section">
  <div class="container split">
    <div class="body reveal">
      <h2 class="title">What drives the price</h2>
      <p>Patio openings are wide, so span moves the number more than anything else. A twenty foot
         opening needs heavier hardware, a larger tube and usually a motor, because nobody cranks a
         shade that size by hand twice a day.</p>
      <ul class="nap-list">
        <li>Span of the opening, which drives hardware and motor sizing</li>
        <li>Fabric openness, since a tighter weave costs more per square foot</li>
        <li>Whether you motorize, and whether it is battery, hardwired or solar charged</li>
        <li>Track guided systems, which add hardware and installation time</li>
      </ul>
      <p>We measure the opening and quote from those measurements. The number on your estimate is
         the number you pay.</p>
      <div class="btnrow"><a class="btn btn-primary btn-lg" href="tel:{tel}">Call {e(ph)}</a></div>
    </div>
    <div class="body reveal">
      <h2 class="title">Nearby areas we serve</h2>
      <ul class="nap-list">{nearlinks}</ul>
      <p><a class="btn-link" href="{c['url']}">All window treatments in {e(city)}
        <span class="arw">&rarr;</span></a></p>
      <p><a class="btn-link" href="/products/exterior-patio-shades">Patio shades across Texas
        <span class="arw">&rarr;</span></a></p>
    </div>
  </div>
</section>

<section class="section bg-cream-tint">
  <div class="container center"><h2 class="title">Patio shade questions from {e(city)}</h2></div>
  <div class="container"><div class="faq">{faqhtml}</div></div>
</section>'''
    return url, title, desc, nodes, body, hero

def build():
    made = []
    for slug in KW:
        url, title, desc, nodes, body, hero = page(slug)
        html_out = P.head_block.__globals__  # not used, we assemble directly
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
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css">
{S.render(nodes)}
</head>
<body>
{HEAD_INNER}
<main>{body}</main>
{P.FOOT}'''
        open(url.lstrip("/") + ".html", "w").write(doc)
        made.append(url)
    return made

if __name__ == "__main__":
    m = build()
    print(f"wrote {len(m)} city patio pages")
    for u in m: print("  ", u)
