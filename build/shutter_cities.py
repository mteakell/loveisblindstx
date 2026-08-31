"""City-level plantation shutter pages.

Same justification as the patio set: real measured demand, KD 0-31, and the
highest CPCs on the site (Plano $18.49, McKinney $14.48). Only cities with
volume get a page, and each carries its own operator, phone, neighbours and
FAQ so none of them is a doorway page.
"""
import html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import schema as S, territory as T, pages as P

os.chdir(P.ROOT)
BIZ = P.BIZ
KW = json.load(open("data/shutter-cities.json"))["cities"]
HEAD_INNER = P.HEAD.split("<body", 1)[1].split(">", 1)[1]
e = lambda s: html.escape(s or "", quote=True)

STYLES = [
 ("Full height panels",
  "One uncovered run of louvers from top to bottom. The cleanest look, and the usual choice "
  "where the whole window is the same job."),
 ("Divider rail",
  "A horizontal rail that lets the top and bottom tilt independently, so you can take light in "
  "high and keep privacy low. On a street facing window this is usually the right answer."),
 ("Tier on tier",
  "Top and bottom panels open separately. More flexible than a divider rail and better suited to "
  "tall windows and period openings."),
 ("Cafe style",
  "Covers the lower half only. Keeps daytime privacy at eye level while the top of the window "
  "carries on doing the lighting."),
 ("Bay, angled and arched",
  "Each panel measured and built individually, with the angles between them taken on site. This is "
  "where measuring stops being a DIY job."),
 ("Sliding and bypass panels",
  "For patio doors and wide openings, panels that track sideways rather than swinging into the room."),
]

def page(slug):
    c = P.BY[slug]
    city = c["label"]
    terr = T.of(slug)
    ph = S.pretty(c["phone"]) or BIZ["phone"]
    tel = S.tel(c["phone"] or BIZ["tel"])
    leads = P._leads(terr)
    url = f"/plantation-shutters-{slug}"
    for cand in (f"Plantation Shutters in {city}, TX | Custom Built",
                 f"Plantation Shutters in {city}, TX | Love Is Blinds",
                 f"Plantation Shutters in {city}, TX"):
        title = cand
        if len(title) <= 60:
            break
    desc = (f"Custom plantation shutters built to your openings in {city}, TX. Free in-home "
            f"measure and professional installation. Call {ph}.")[:155]
    near = P.nearby(c, 6)
    nearlinks = "".join(f'<li><a href="{o["url"]}">{e(o["label"])}, TX</a></li>' for o in near)
    styles = "".join(f'<div class="prod-card reveal"><div class="pbody"><h3>{e(n)}</h3>'
                     f'<p>{e(b)}</p></div></div>' for n, b in STYLES)
    faqs = [
      (f"Do you install plantation shutters in {city}?",
       f"Yes. {leads} runs {terr['brand']}, which covers {city} along with {terr['blurb']}. "
       f"Shutters are measured, built to the opening and fitted by the same team. Call {ph}."),
      (f"How much do plantation shutters cost in {city}?",
       "It depends on the size of the opening, the material, the louver size and the frame style. "
       "We measure every opening on site and quote from those measurements, so the number on your "
       "estimate is the number you pay."),
      ("Will shutters fit my windows?",
       "Almost always, but the frame style changes based on what the opening allows. Every shutter "
       "needs a minimum depth for the louvers to rotate. If the opening is shallow, the answer is a "
       "frame that projects rather than abandoning shutters."),
      ("How long do plantation shutters take?",
       "Shutters are built to your measurements, so they take longer than a stock blind. We confirm "
       "the timeline in writing on your quote at the consultation."),
      ("Do shutters add value to a home?",
       "They stay with the house, so unlike most window coverings buyers read them as part of the "
       "property rather than a covering that will be replaced. That is the usual reason people put "
       "shutters in the rooms that show and blinds or shades elsewhere."),
      ("Real wood or composite?",
       "Wood is lighter and takes stain beautifully, so it suits dry living areas. Composite handles "
       "moisture and hard sun without warping, which is why it wins in bathrooms, kitchens and on "
       "west facing walls in Texas."),
    ]
    faqhtml = "".join(f"<details><summary>{e(q)}</summary><div class='a'>{e(a)}</div></details>"
                      for q, a in faqs)
    hero = "/images/lib/shutters-shutters-004-jpg.webp"
    nodes = [S.organization(BIZ), S.website(BIZ), S.business(BIZ), S.business(BIZ, c),
             S.webpage(url, title, desc, about=f"{S.SITE}{url}#business", primary=hero),
             S.breadcrumbs([("Home", "/"), ("Products", "/products"),
                            ("Plantation Shutters", "/products/plantation-shutters"),
                            (f"{city}, TX", url)]),
             S.faq(url, faqs),
             S.service(url, f"Plantation Shutter Installation in {city}, TX",
                       f"Measurement, custom build and professional installation of interior "
                       f"plantation shutters for homes in {city}, Texas.",
                       f"{S.SITE}{url}#business",
                       area={"@type": "City", "name": c["locality"]},
                       catalog=[n for n, _ in STYLES])]
    body = f'''<section class="phero">
  <picture><img src="{hero}" alt="Plantation shutters installed in {e(city)}, TX by Love Is Blinds" fetchpriority="high"></picture>
  <div class="container"><div class="phero-copy">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">&rsaquo;</span>
      <a href="/products/plantation-shutters">Plantation Shutters</a><span class="sep">&rsaquo;</span>{e(city)}, TX</nav>
    <h1 class="title">Plantation Shutters in {e(city)}, Texas</h1>
    <p class="lead">Built to the opening rather than trimmed to fit, hung in their own frame and
      installed by the team that measured them. Free in-home consultation in {e(city)}.</p>
    <div class="hero-actions btnrow">
      <a class="btn btn-primary btn-lg" href="tel:{tel}">Call {e(ph)}</a>
      <a class="btn btn-secondary btn-lg" href="/schedule-now">Book a free measure</a>
    </div>
  </div></div>
</section>

<section class="section">
  <div class="container split media-right">
    <div class="body reveal">
      <h2 class="title">Why shutters get measured differently</h2>
      <p>A shutter is a rigid panel in a frame. It cannot flex to absorb a crooked opening the way a
         fabric shade can, and most {e(city)} homes over a few years old have settled enough that
         the width at the top of a window is not the width at the bottom.</p>
      <p>That is why we measure every opening in three places, check the depth before committing to
         a frame style, and quote from those measurements rather than from a photograph.</p>
      <ul class="feature-list">
        <li>{P.TICK}Every opening measured on site, in three places</li>
        <li>{P.TICK}Frame style chosen from what the opening actually allows</li>
        <li>{P.TICK}{e(city)} is covered by {e(terr['brand'])}, run by {e(leads)}</li>
        <li>{P.TICK}Remade at no cost if a panel does not match the approved measurements</li>
      </ul>
      <div class="btnrow">
        <a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a>
      </div>
    </div>
    <div class="media reveal">
      <img src="/images/lib/shutters-shutters-006-jpg.webp" width="900" height="600" loading="lazy"
           alt="Custom plantation shutters in a {e(city)}, TX home">
    </div>
  </div>
</section>

<section class="section bg-cream-tint">
  <div class="container center"><h2 class="title">Shutter styles we build for {e(city)} homes</h2></div>
  <div class="container"><div class="prod-grid">{styles}</div></div>
</section>

<section class="section">
  <div class="container split">
    <div class="body reveal">
      <h2 class="title">What changes the price</h2>
      <ul class="nap-list">
        <li>Size of the opening, which drives material more than anything else</li>
        <li>Material: hardwood, composite or vinyl</li>
        <li>Louver size, which changes the view out and the material per panel</li>
        <li>Frame style, and whether the opening is square enough for an inside fit</li>
        <li>Panel configuration, since a wide window split four ways costs more than two</li>
        <li>Specialty shapes: bays, arches and angles are built individually</li>
      </ul>
      <div class="btnrow"><a class="btn btn-primary btn-lg" href="tel:{tel}">Call {e(ph)}</a></div>
    </div>
    <div class="body reveal">
      <h2 class="title">Nearby areas we serve</h2>
      <ul class="nap-list">{nearlinks}</ul>
      <p><a class="btn-link" href="{c['url']}">All window treatments in {e(city)}
        <span class="arw">&rarr;</span></a></p>
      <p><a class="btn-link" href="/how-much-do-plantation-shutters-cost-in-texas">What shutters
        cost in Texas <span class="arw">&rarr;</span></a></p>
    </div>
  </div>
</section>

<section class="section bg-cream-tint">
  <div class="container center"><h2 class="title">Shutter questions from {e(city)}</h2></div>
  <div class="container"><div class="faq">{faqhtml}</div></div>
</section>'''
    return url, title, desc, nodes, body, hero

def build():
    made = []
    for slug in KW:
        url, title, desc, nodes, body, hero = page(slug)
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
    print(f"wrote {len(m)} city shutter pages")
