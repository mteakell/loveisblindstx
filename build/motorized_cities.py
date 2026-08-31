"""City-level motorized shade and blind pages.

The lowest difficulty cluster on the site: KD 0-3 with real volume. Only the
six cities with measured demand get a page. 41 of the 47 cities have zero
searches for these terms and deliberately get nothing.
"""
import html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import schema as S, territory as T, pages as P

os.chdir(P.ROOT)
BIZ = P.BIZ
KW = json.load(open("data/motorized-cities.json"))["cities"]
HEAD_INNER = P.HEAD.split("<body", 1)[1].split(">", 1)[1]
e = lambda s: html.escape(s or "", quote=True)

STYLES = [
 ("Battery powered",
  "The simplest retrofit. No electrician, no wiring, and you recharge or swap the pack "
  "periodically depending on how often the shade moves."),
 ("Hardwired",
  "Best during a remodel or new build while the walls are open. Nothing to recharge, and the "
  "cleanest result, but it has to be planned before the drywall goes up."),
 ("Solar charged",
  "A small panel keeps the battery topped up. It suits Texas particularly well, because the "
  "windows that most need motorizing are the ones getting the most sun."),
 ("App and voice control",
  "Control from a phone or a voice assistant. Useful, though in practice the wall switch by the "
  "door is what people reach for day to day."),
 ("Scheduling and sun triggers",
  "The feature people actually keep using. Shades close against the afternoon sun and open in the "
  "morning without anyone thinking about it."),
 ("Wide and high openings",
  "Above a certain width or height a hand-operated treatment simply stops getting used. This is "
  "where motorization pays for itself rather than being a luxury."),
]

def page(slug):
    c = P.BY[slug]
    city = c["label"]
    terr = T.of(slug)
    ph = S.pretty(c["phone"]) or BIZ["phone"]
    tel = S.tel(c["phone"] or BIZ["tel"])
    leads = P._leads(terr)
    url = f"/motorized-shades-{slug}"
    for cand in (f"Motorized Shades & Blinds in {city}, TX | Smart Control",
                 f"Motorized Shades & Blinds in {city}, TX",
                 f"Motorized Shades in {city}, TX"):
        title = cand
        if len(title) <= 60:
            break
    desc = (f"Motorized shades and blinds in {city}, TX with app, remote and voice control. "
            f"Battery, hardwired or solar. Free in-home measure. Call {ph}.")[:155]
    near = P.nearby(c, 6)
    nearlinks = "".join(f'<li><a href="{o["url"]}">{e(o["label"])}, TX</a></li>' for o in near)
    styles = "".join(f'<div class="prod-card reveal"><div class="pbody"><h3>{e(n)}</h3>'
                     f'<p>{e(b)}</p></div></div>' for n, b in STYLES)
    faqs = [
      (f"Do you install motorized shades in {city}?",
       f"Yes. {leads} runs {terr['brand']}, which covers {city} along with {terr['blurb']}. We "
       f"measure, install, pair the motors and set up the schedule before we leave. Call {ph}."),
      (f"How much do motorized blinds cost in {city}?",
       "Motorization adds cost per opening on top of the treatment itself, and the power option "
       "changes it too. We measure every opening and quote from those measurements, so the number "
       "on your estimate is the number you pay."),
      ("Which windows are actually worth motorizing?",
       "The ones you cannot easily reach, the ones too wide or heavy to work by hand, and any you "
       "want on a schedule. In most homes that is three to six openings, not all of them. "
       "Motorizing a whole house evenly is the most common way people overspend."),
      ("Battery, hardwired or solar?",
       "Battery is the simplest retrofit and needs no electrician. Hardwired is best during a "
       "remodel while walls are open. Solar charging suits windows that get real sun, which in "
       "Texas is most of them."),
      ("Will it work with my smart home?",
       "Tell us at the consultation which system you already run and we will confirm compatibility "
       "before you order rather than after. We pair and program everything at installation."),
      ("What happens if a motor needs reprogramming later?",
       "You call the same team that installed it. That is the practical difference between buying "
       "motorization from a local installer and buying it online."),
    ]
    faqhtml = "".join(f"<details><summary>{e(q)}</summary><div class='a'>{e(a)}</div></details>"
                      for q, a in faqs)
    hero = "/images/lib/smart-drapes-smart-drapes-002-jpg.webp"
    nodes = [S.organization(BIZ), S.website(BIZ), S.business(BIZ), S.business(BIZ, c),
             S.webpage(url, title, desc, about=f"{S.SITE}{url}#business", primary=hero),
             S.breadcrumbs([("Home", "/"), ("Products", "/products"),
                            ("Motorization", "/products/motorized-window-treatment-automations"),
                            (f"{city}, TX", url)]),
             S.faq(url, faqs),
             S.service(url, f"Motorized Shade and Blind Installation in {city}, TX",
                       f"Supply, installation, motor pairing and scheduling for motorized shades "
                       f"and blinds in {city}, Texas.",
                       f"{S.SITE}{url}#business",
                       area={"@type": "City", "name": c["locality"]},
                       catalog=[n for n, _ in STYLES])]
    body = f'''<section class="phero">
  <picture><img src="{hero}" alt="Motorized shades installed in {e(city)}, TX by Love Is Blinds" fetchpriority="high"></picture>
  <div class="container"><div class="phero-copy">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">&rsaquo;</span>
      <a href="/products/motorized-window-treatment-automations">Motorization</a><span class="sep">&rsaquo;</span>{e(city)}, TX</nav>
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
      <h2 class="title">Why motorization is decided per window, not per house</h2>
      <p>Motorization earns its cost on specific openings, not across a whole house. The windows
         where it pays for itself are consistent: the ones you cannot reach, the ones too heavy to
         work by hand, and the ones you want moving on a schedule against the afternoon sun.</p>
      <p>In most {e(city)} homes that is three to six openings. We walk the house with you and mark
         which ones genuinely warrant it rather than quoting motors on everything.</p>
      <ul class="feature-list">
        <li>{P.TICK}Battery, hardwired and solar charged options</li>
        <li>{P.TICK}Paired, programmed and tested at installation, not left to you</li>
        <li>{P.TICK}{e(city)} is covered by {e(terr['brand'])}, run by {e(leads)}</li>
        <li>{P.TICK}Scheduling set up before we leave, which is the feature people keep using</li>
      </ul>
      <div class="btnrow">
        <a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a>
      </div>
    </div>
    <div class="media reveal">
      <img src="/images/lib/smart-drapes-smart-drapes-005-jpg.webp" width="900" height="600" loading="lazy"
           alt="Motorized shades in a {e(city)}, TX home">
    </div>
  </div>
</section>

<section class="section bg-cream-tint">
  <div class="container center"><h2 class="title">Motorization options for {e(city)} homes</h2></div>
  <div class="container"><div class="prod-grid">{styles}</div></div>
</section>

<section class="section">
  <div class="container split">
    <div class="body reveal">
      <h2 class="title">What changes the price</h2>
      <ul class="nap-list">
        <li>How many openings you motorize, since it is priced per opening</li>
        <li>Power: battery, hardwired or solar charged</li>
        <li>The treatment itself, since a motor moves whatever you put on the window</li>
        <li>Width and weight, which decide motor sizing on large spans</li>
        <li>Whether you want a hub, wall switches, or app and voice control</li>
      </ul>
      <div class="btnrow"><a class="btn btn-primary btn-lg" href="tel:{tel}">Call {e(ph)}</a></div>
    </div>
    <div class="body reveal">
      <h2 class="title">Nearby areas we serve</h2>
      <ul class="nap-list">{nearlinks}</ul>
      <p><a class="btn-link" href="{c['url']}">All window treatments in {e(city)}
        <span class="arw">&rarr;</span></a></p>
      <p><a class="btn-link" href="/motorized-blinds-cost-is-motorization-worth-it">What motorization
        cost in Texas <span class="arw">&rarr;</span></a></p>
    </div>
  </div>
</section>

<section class="section bg-cream-tint">
  <div class="container center"><h2 class="title">Motorization questions from {e(city)}</h2></div>
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
