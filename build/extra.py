"""Pages with no Georgia equivalent: the service-area index, the design checklist
and the team profiles."""
import json, os, re, sys, html, collections
sys.path.insert(0, os.path.dirname(__file__))
import schema as S, territory as T

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
D = json.load(open("data/tx.json")); BIZ, CITIES = D["business"], D["cities"]
HEAD = open("build/partials/header.html").read()
FOOT = open("build/partials/footer.html").read()
HEAD_INNER = HEAD.split("<body", 1)[1].split(">", 1)[1]
e = lambda s: html.escape(s or "", quote=True)

def shell(url, title, desc, nodes, body, img="/images/lib/shutters-shutters-004-jpg.webp"):
    return f'''<!DOCTYPE html>
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
<meta property="og:image" content="{S.SITE}{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css">
{S.render(nodes)}
</head>
<body>
{HEAD_INNER}
<main>{body}</main>
{FOOT}'''

HERO = "/images/lib/shutters-shutters-004-jpg.webp"
TICK = ('<span class="tick"><svg viewBox="0 0 24 24">'
        '<path d="m20 6-11 11-5-5"/></svg></span>')

BASE = lambda: [S.organization(BIZ), S.website(BIZ), S.business(BIZ)]

# ------------------------------------------------------------ /areas-we-serve
def areas():
    url = "/areas-we-serve"
    title = "Texas Service Areas | Love Is Blinds"
    desc = ("Every Texas city we serve for custom blinds, shades and shutters, across DFW, "
            "North Texas, East Texas, Waco and the Austin metro.")
    groups = collections.OrderedDict()
    for c in sorted(CITIES, key=lambda x: x["label"]):
        groups.setdefault(T.of(c["slug"])["name"], []).append(c)
    secs, items = "", []
    for name, cs in groups.items():
        links = "".join(
            f'<li><a href="{c["url"]}">{e(c["label"])}, TX</a>'
            + (f' <span class="sml">{e(S.pretty(c["phone"]))}</span>' if c["phone"] else "")
            + "</li>" for c in cs)
        secs += (f'<section class="section"><div class="container">'
                 f'<h2 class="title">{e(name)}</h2>'
                 f'<p class="lead">{e(T.TERRITORIES[[k for k,v in T.TERRITORIES.items() if v["name"]==name][0]]["blurb"])}.</p>'
                 f'<ul class="nap-list city-index">{links}</ul></div></section>')
        items += [c for c in cs]
    lst = {"@type": "ItemList", "@id": S.SITE + url + "#list",
           "name": "Texas service areas", "numberOfItems": len(items),
           "itemListElement": [{"@type": "ListItem", "position": i,
                                "name": f'{c["label"]}, TX', "item": S.SITE + c["url"]}
                               for i, c in enumerate(items, 1)]}
    nodes = BASE() + [S.webpage(url, title, desc),
                      S.breadcrumbs([("Home", "/"), ("Service Areas", url)]), lst]
    body = (f'<section class="phero"><picture><img src="' + HERO + '" alt="Custom window treatments by Love Is Blinds Texas" fetchpriority="high"></picture><div class="container"><div class="phero-copy">'
            f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span>&rsaquo;</span>'
            f'<span aria-current="page">Service Areas</span></nav>'
            f'<h1 class="title">Where Love Is Blinds Works in Texas</h1>'
            f'<p class="lead">Three local teams cover the state. Find your city below for the '
            f'number that reaches the crew who will measure and install your windows.</p>'
            f'</div></div></section>{secs}')
    open("areas-we-serve.html", "w").write(shell(url, title, desc, nodes, body))
    return len(items)

# ------------------------------------------------------------------- /team/*
BIOS = json.load(open("data/team-bios.json"))

def team():
    made = []
    for m in T.TEAM:
        terr = T.TERRITORIES[m["territory"]] if m["territory"] else None
        url = f"/team/{m['slug']}"
        brand = terr["brand"] if terr else BIZ["name"]
        title = f"{m['name']} | {brand}"
        if len(title) > 62: title = f"{m['name']} | Love Is Blinds"
        if terr:
            cs = [c for c in CITIES if T.of(c["slug"])["key"] == terr["key"]]
            desc = (f"{m['name']} runs {brand}, covering {terr['blurb']}. "
                    f"Free in-home window treatment consultations.")
            if len(desc) > 155:
                desc = f"{m['name']} runs {brand}, covering {len(cs)} Texas cities. Free in-home consultations."
            links = "".join(f'<li><a href="{c["url"]}">{e(c["label"])}, TX</a></li>'
                            for c in sorted(cs, key=lambda x: x["label"]))
            area = (f'<section class="section bg-cream-tint"><div class="container">'
                    f'<h2 class="title">Cities {e(m["name"].split()[0])} covers</h2>'
                    f'<ul class="nap-list city-index">{links}</ul></div></section>')
            intro = (f'{e(m["name"])} runs {e(brand)}, one of the three Love Is Blinds '
                     f'franchises working across the state. That territory covers '
                     f'{e(terr["blurb"])}.')
        else:
            desc = f"{m['name']} of Love Is Blinds Texas. Free in-home window treatment consultations across Texas."
            area, intro = "", (f'{e(m["name"])} works with Love Is Blinds across Texas.')
        bio = "".join(f'<p>{e(p)}</p>' for p in BIOS.get(m["slug"], []))
        node = S.person(m["name"], "Owner" if terr else "Love Is Blinds Texas", url,
                        image=m.get("photo"))
        if terr:
            node["worksFor"] = {"@type": "Organization", "name": brand,
                                "parentOrganization": {"@id": S.ORGID}}
        nodes = BASE() + [S.webpage(url, title, desc, about=S.ORGID), node,
            S.breadcrumbs([("Home", "/"), ("Meet the Team", "/meet-the-team"), (m["name"], url)])]
        shot = (f'<div class="media"><img src="{m["photo"]}" width="900" height="1000" '
                f'alt="{e(m["name"])}, {e(brand)}" fetchpriority="high"></div>'
                if m.get("photo") else "")
        body = (f'<section class="section"><div class="container split media-right">'
                f'<div class="body">'
                f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">&rsaquo;</span>'
                f'<a href="/meet-the-team">Meet the Team</a><span class="sep">&rsaquo;</span>'
                f'{e(m["name"])}</nav>'
                f'<h1 class="title">{e(m["name"])}</h1>'
                f'<p class="kicker">{e(brand)}</p><p class="lead">{intro}</p>{bio}'
                f'<div class="btnrow">'
                f'<a class="btn btn-primary btn-lg" href="/schedule-now">Book a consultation</a>'
                f'<a class="btn btn-secondary btn-lg" href="tel:{BIZ["tel"]}">Call {e(BIZ["phone"])}</a>'
                f'</div></div>{shot}</div></section>{area}')
        os.makedirs("team", exist_ok=True)
        open(f"team/{m['slug']}.html", "w").write(shell(url, title, desc, nodes, body))
        made.append(m["slug"])
    return made

# ------------------------------------------------------------ /design-checklist
CHECK = [
 ("Room and window count", "List each room and how many openings it has. Bay and corner windows count as separate openings, and that is usually where a quote surprises people."),
 ("Which way the windows face", "West and south facing glass takes the worst of the Texas afternoon. Those rooms often want a solar screen or a cellular shade rather than a plain blind."),
 ("What the room is for", "Bedrooms and media rooms need blackout. Kitchens and baths need something that tolerates moisture. Living areas usually want filtered light rather than full block."),
 ("Privacy after dark", "A shade that gives daytime privacy can go transparent once the lights come on inside. Decide which windows need to work at night."),
 ("Existing trim and depth", "Shutters and inside-mount blinds need enough depth in the window frame. Measure the depth before you fall in love with a mount type."),
 ("Cord safety", "If children or pets use the room, plan for cordless or motorized. It is a safety requirement in most new installs, not an upgrade."),
 ("Motorization and power", "Decide per window whether you want battery, hardwired or solar charging, and whether you want app, remote or voice control."),
 ("Budget range per room", "Bring a range rather than a single number. It lets us show you where spending more actually changes the result and where it does not."),
]
def checklist():
    url, title = "/design-checklist", "Window Treatment Design Checklist | Love Is Blinds"
    desc = ("Work through this checklist before your in-home consultation: rooms, window "
            "orientation, privacy, trim depth, cord safety, motorization and budget.")
    items = "".join(
        f'<div class="prod-card reveal"><div class="pbody">'
        f'<p class="kicker">Step {i}</p><h3>{e(h)}</h3><p>{e(b)}</p></div></div>'
        for i, (h, b) in enumerate(CHECK, 1))
    lst = {"@type": "ItemList", "@id": S.SITE + url + "#list",
           "name": "Window treatment design checklist", "numberOfItems": len(CHECK),
           "itemListElement": [{"@type": "ListItem", "position": i, "name": h,
                                "description": b} for i, (h, b) in enumerate(CHECK, 1)]}
    nodes = BASE() + [S.webpage(url, title, desc),
                      S.breadcrumbs([("Home", "/"), ("Design Checklist", url)]), lst,
                      S.faq(url, [(h, b) for h, b in CHECK[:4]])]
    body = (f'<section class="phero"><picture><img src="' + HERO + '" alt="Custom window treatments by Love Is Blinds Texas" fetchpriority="high"></picture><div class="container"><div class="phero-copy">'
            f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span>&rsaquo;</span>'
            f'<span aria-current="page">Design Checklist</span></nav>'
            f'<h1 class="title">Window Treatment Design Checklist</h1>'
            f'<p class="lead">Eight things worth deciding before anyone measures your windows. '
            f'Work through them and your consultation turns into a quote in one visit instead '
            f'of two.</p></div></div></section>'
            f'<section class="section"><div class="container"><div class="prod-grid">{items}</div>'
            f'<div class="btnrow"><a class="btn btn-primary btn-lg" href="/contact">Book your free consultation</a>'
            f'<a class="btn btn-secondary btn-lg" href="tel:{BIZ["tel"]}">Call {e(BIZ["phone"])}</a></div>'
            f'</div></section>')
    open("design-checklist.html", "w").write(shell(url, title, desc, nodes, body))


# ------------------------------------------------- meet-the-team owner cards
def team_cards():
    """Owner cards on /meet-the-team. Portrait headshots need their own grid:
    the stock .prod-card image box is 212px landscape, which crops heads off."""
    cards = ""
    for m in T.TEAM:
        terr = T.TERRITORIES[m["territory"]] if m["territory"] else None
        sub = terr["brand"] if terr else "Love Is Blinds Texas"
        blurb = (f"Covers {terr['blurb']}." if terr
                 else "Works with Love Is Blinds across Texas.")
        pic = (f'<div class="pic"><img src="{m["photo"]}" alt="{e(m["name"])}, {e(sub)}" '
               f'loading="lazy" width="600" height="667"></div>' if m.get("photo") else "")
        cards += (f'<a class="prod-card reveal" href="/team/{m["slug"]}">{pic}<div class="pbody">'
                  f'<h3>{e(m["name"])}</h3><p class="kicker">{e(sub)}</p><p>{e(blurb)}</p>'
                  f'<span class="btn-link">Read more <span class="arw">&rarr;</span></span>'
                  f'</div></a>')
    block = (f'<section class="section bg-cream-tint"><div class="container center">'
             f'<h2 class="title">Meet Your Local Owner Operators</h2>'
             f'<p class="lead">Three franchises cover Texas. The person who quotes your windows '
             f'is the person who installs them.</p></div><div class="container">'
             f'<div class="team-grid">{cards}</div></div></section>\n')
    s = open("meet-the-team.html").read()
    s = re.sub(r'<section class="section bg-cream-tint"><div class="container center">'
               r'<h2 class="title">(?:The three Texas teams|Meet Your Local Owner Operators)'
               r'.*?</section>\s*', lambda m: "", s, flags=re.S)
    i = s.find("<footer")
    open("meet-the-team.html", "w").write(s[:i] + block + s[i:])
    return len(T.TEAM)

if __name__ == "__main__":
    print("areas-we-serve:", areas(), "cities")
    print("team pages    :", ", ".join(team()))
    print("owner cards   :", team_cards())
    checklist(); print("design-checklist: written")

# ------------------------------------------------------------------- /blog
def blog_index():
    idx = json.load(open("data/blog-index.json"))
    idx.sort(key=lambda p: (p.get("date") or ""), reverse=True)
    url, title = "/blog", "Window Treatment Blog | Love Is Blinds Texas"
    desc = ("Guides on choosing, measuring, cleaning and motorizing blinds, shades and "
            "shutters for Texas homes.")
    cards = "".join(
        f'<a class="prod-card reveal" href="{p["url"]}">'
        + (f'<div class="pic"><img src="{p["img"]}" alt="{e(p["title"])}" loading="lazy" '
           f'decoding="async" width="600" height="400"></div>' if p.get("img") else "")
        + f'<div class="pbody"><h3>{e(p["title"])}</h3>'
          f'<p>{e((p.get("desc") or "")[:150])}</p>'
          f'<span class="btn-link">Read <span class="arw">&rarr;</span></span></div></a>'
        for p in idx)
    blog = {"@type": "Blog", "@id": S.SITE + url + "#blog", "name": title,
            "description": desc, "publisher": {"@id": S.ORGID}, "inLanguage": "en-US",
            "blogPost": [{"@type": "BlogPosting", "@id": S.SITE + p["url"] + "#post",
                          "headline": p["title"][:110], "url": S.SITE + p["url"],
                          "datePublished": p.get("date") or "2024-01-01"} for p in idx]}
    nodes = BASE() + [S.webpage(url, title, desc, about=S.ORGID),
                      S.breadcrumbs([("Home", "/"), ("Blog", url)]), blog]
    body = (f'<section class="phero"><picture><img src="' + HERO + '" alt="Custom window treatments by Love Is Blinds Texas" fetchpriority="high"></picture><div class="container"><div class="phero-copy">'
            f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span>&rsaquo;</span>'
            f'<span aria-current="page">Blog</span></nav>'
            f'<h1 class="title">Window Treatment Guides</h1>'
            f'<p class="lead">{len(idx)} guides on choosing, measuring, cleaning and '
            f'automating window treatments for Texas homes.</p></div></div></section>'
            f'<section class="section"><div class="container">'
            f'<div class="prod-grid">{cards}</div></div></section>')
    open("blog/index.html", "w").write(shell(url, title, desc, nodes, body))
    return len(idx)

# ---------------------------------------------------------------- /vodyssey
VOD = [
 ("/vodyssey", "vodyssey.html", "Vodyssey Exclusive Access | Love Is Blinds",
  "Vodyssey member access to custom blinds, shades and shutters. Choose your type, choose your colour, measure your windows and order.",
  "Vodyssey Exclusive Access",
  "Vodyssey members order custom window treatments through this four step process. Pick the treatment type, pick the colour, measure your openings and place the order."),
 ("/journey", "journey.html", "Step 1: Choose Your Type | Vodyssey | Love Is Blinds",
  "Step one of the Vodyssey ordering journey. Compare blinds, shades and shutters and choose the treatment type for each room.",
  "Step 1: Choose Your Type",
  "Compare blinds, shades and shutters, then choose a treatment type for each room before moving on to colour."),
 ("/vodyssey/order", "vodyssey/order.html", "Step 4: Placing Your Order | Vodyssey",
  "Step four of the Vodyssey ordering journey. Confirm your measurements, review your selections and place your order.",
  "Step 4: Placing Your Order",
  "Confirm your measurements, review each selection and place the order. We build to the measurements you approve."),
 ("/vodyssey/limited-lifetime-warranty", "vodyssey/limited-lifetime-warranty.html",
  "Limited Lifetime Warranty | Vodyssey | Love Is Blinds",
  "The limited lifetime warranty covering Vodyssey window treatment orders through Love Is Blinds.",
  "Limited Lifetime Warranty",
  "What the limited lifetime warranty covers on Vodyssey orders, and how to make a claim."),
]
def vodyssey():
    os.makedirs("vodyssey", exist_ok=True)
    steps = [(u, t) for u, _, _, _, t, _ in VOD]
    for url, path, title, desc, h1, lead in VOD:
        nav = "".join(f'<li><a href="{u}">{e(t)}</a></li>' for u, t in steps if u != url)
        nodes = BASE() + [S.webpage(url, title, desc, about=S.ORGID),
                          S.breadcrumbs([("Home", "/"), ("Vodyssey", "/vodyssey")]
                                        + ([(h1, url)] if url != "/vodyssey" else []))]
        body = (f'<section class="phero"><picture><img src="' + HERO + '" alt="Custom window treatments by Love Is Blinds Texas" fetchpriority="high"></picture><div class="container"><div class="phero-copy">'
                f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span>&rsaquo;</span>'
                f'<a href="/vodyssey">Vodyssey</a></nav>'
                f'<h1 class="title">{e(h1)}</h1><p class="lead">{e(lead)}</p>'
                f'<div class="btnrow"><a class="btn btn-primary btn-lg" href="/schedule-now">Book a consultation</a>'
                f'<a class="btn btn-secondary btn-lg" href="tel:{BIZ["tel"]}">Call {e(BIZ["phone"])}</a></div>'
                f'</div></div></section>'
                f'<section class="section"><div class="container"><h2 class="title">'
                f'Other steps</h2><ul class="nap-list">{nav}</ul></div></section>')
        s = shell(url, title, desc, nodes, body)
        # partner funnel: keep it out of search so it never competes with /products
        s = s.replace('<meta name="theme-color"',
                      '<meta name="robots" content="noindex,follow">\n<meta name="theme-color"')
        open(path, "w").write(s)
    return len(VOD)

# ------------------------------------------------- /products/exterior-patio-shades
# Biggest single content opportunity on the site: the patio cluster is roughly
# 40k US searches/month at KD 13-42, against ~1.5k for every city term combined.
# Terms targeted here come from data/keywords.json (Semrush, 2026-08-25).
PATIO_FAQ = [
 ("What are exterior patio shades?",
  "Exterior patio shades are fabric or screen shades that mount outside the house, over a porch, "
  "patio or outdoor room. They stop heat and glare before it reaches the glass or the seating area, "
  "which is why they cool a space far more effectively than an interior blind on the same opening."),
 ("What openness factor should I choose?",
  "Openness is how much of the weave is open, and it decides the trade between view and shade. "
  "A more open weave keeps the view and cuts glare. A tighter weave blocks more sun and gives more "
  "daytime privacy but softens the view. West-facing patios that take the afternoon sun usually "
  "want a tighter weave than a north-facing porch."),
 ("Do patio shades work in Texas heat?",
  "That is the case they are built for. Blocking sun on the outside of the glass stops the heat "
  "before it enters, so the patio stays usable in the afternoon and the rooms behind it take less "
  "heat load. It is the same reason exterior shading outperforms interior shading on a west wall."),
 ("Can patio shades be motorized?",
  "Yes. Motorized patio shades run on a remote, a wall switch, an app or a schedule, and can be "
  "battery, hardwired or solar charged. On wide spans motorization is often the practical choice, "
  "because a large exterior shade is heavy to crank by hand every day."),
 ("Are retractable patio shades an option?",
  "Yes. Retractable shades roll up out of the weather when you are not using the space, which "
  "keeps the fabric out of wind and hail and extends its life. Fixed shades suit spots where you "
  "want shade permanently in place."),
 ("Will they hold up to wind and storms?",
  "Exterior shades should be retracted in high wind, and that is the main reason we recommend "
  "motorization on larger openings: it is quick to raise them when weather turns. We size the "
  "hardware to the opening and go over the wind guidance at the consultation."),
 ("How much do patio shades cost?",
  "It depends on the width of the opening, the fabric, and whether you motorize. We measure the "
  "opening and quote from those measurements at the free in-home consultation, so the number you "
  "get is the number, not a range that moves later."),
 ("Do you install patio shades across Texas?",
  "Yes, across all three of our territories: DFW and the Mid-Cities, North Texas, and East and "
  "Central Texas including Waco and the Austin metro. Find your city on our service areas page."),
]
PATIO_TYPES = [
 ("Solar screen patio shades",
  "Open-weave screen that cuts glare and heat while keeping the view out to the yard. The most "
  "common choice for a covered patio that gets hard afternoon sun."),
 ("Motorized patio shades",
  "Remote, wall switch, app or scheduled control. The practical option on wide openings, and the "
  "quickest way to get shades up when the wind turns."),
 ("Retractable patio shades",
  "Roll up out of the weather when the space is not in use, which keeps fabric out of wind and "
  "hail and extends its working life."),
 ("Outdoor roller shades",
  "Straightforward roll-down shade for porches and outdoor rooms, in a range of openness factors "
  "and fabric colours."),
 ("Porch and outdoor room shades",
  "Enclose a porch or screened room so it stays usable through the hottest part of the day without "
  "losing the airflow."),
 ("Exterior solar shades for windows",
  "Mounted outside the glass rather than inside it, so heat is stopped before it enters and the "
  "cooling load on that wall drops."),
]
def patio():
    url = "/products/exterior-patio-shades"
    title = "Patio Shades in Texas | Outdoor & Exterior Shades"
    desc = ("Custom exterior patio shades, outdoor roller shades and motorized patio screens for "
            "Texas porches and patios. Free in-home measure and installation.")
    KW = json.load(open("data/keywords.json"))
    types = "".join(
        f'<div class="prod-card reveal"><div class="pbody">'
        f'<h3>{e(n)}</h3><p>{e(b)}</p></div></div>' for n, b in PATIO_TYPES)
    faqhtml = "".join(
        f'<details><summary>{e(q)}</summary><div class="a">{e(a)}</div></details>'
        for q, a in PATIO_FAQ)
    patio_cities = ["dallas-tx", "austin-tx", "fort-worth-tx", "plano-tx", "frisco-tx",
                    "southlake-tx", "waco-tx", "tyler-tx", "round-rock-tx", "georgetown-tx",
                    "mckinney-tx", "grapevine-tx"]
    BY = {c["slug"]: c for c in CITIES}
    citylinks = "".join(f'<a class="chip" href="{BY[s]["url"]}">Patio shades in {e(BY[s]["label"])}</a>'
                        for s in patio_cities if s in BY)
    svc = S.service(url, "Exterior Patio Shade Installation",
                    "Measurement, custom order and installation of exterior patio shades, outdoor "
                    "roller shades and motorized patio screens across Texas.", S.BIZID,
                    catalog=[n for n, _ in PATIO_TYPES])
    nodes = BASE() + [S.webpage(url, title, desc, primary=HERO),
                      S.breadcrumbs([("Home", "/"), ("Products", "/products"),
                                     ("Exterior Patio Shades", url)]),
                      svc, S.faq(url, PATIO_FAQ)]
    body = (f'<section class="phero"><picture><img src="/images/lib/exterior-patio-shades-exterior-patio-shades-001-jpg.webp" '
            f'alt="Exterior patio shades installed by Love Is Blinds Texas" fetchpriority="high"></picture>'
            f'<div class="container"><div class="phero-copy">'
            f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">&rsaquo;</span>'
            f'<a href="/products">Products</a><span class="sep">&rsaquo;</span>Exterior Patio Shades</nav>'
            f'<h1 class="title">Exterior Patio Shades in Texas</h1>'
            f'<p class="lead">Outdoor shades that stop the sun before it reaches the glass, so a '
            f'west-facing patio is still usable at five in the afternoon. Measured, built to the '
            f'opening and installed by our own team.</p>'
            f'<div class="hero-actions btnrow">'
            f'<a class="btn btn-primary btn-lg" href="tel:{BIZ["tel"]}">Call {e(BIZ["phone"])}</a>'
            f'<a class="btn btn-secondary btn-lg" href="/schedule-now">Book a free measure</a>'
            f'</div></div></div></section>'
            f'<section class="section"><div class="container split media-right">'
            f'<div class="body reveal"><h2 class="title">Shade the outside of the glass, not the inside</h2>'
            f'<p>An interior blind stops light after the sun has already come through the window and '
            f'heated the room. An exterior shade stops it before it gets there. On a west wall in a '
            f'Texas summer that difference is the whole point, and it is why a covered patio with '
            f'exterior shades stays usable in the afternoon while an unshaded one does not.</p>'
            f'<ul class="feature-list">'
            f'<li>{TICK}Openness factor chosen for the direction the patio faces</li>'
            f'<li>{TICK}Manual, motorized, or scheduled on an app</li>'
            f'<li>{TICK}Retractable options that roll up out of wind and hail</li>'
            f'<li>{TICK}Measured and installed by the team that quotes it</li></ul>'
            f'<div class="btnrow"><a class="btn btn-primary btn-lg" href="/schedule-now">'
            f'Book your free consultation</a></div></div>'
            f'<div class="media reveal"><img src="/images/lib/exterior-patio-shades-exterior-patio-shades-003-jpg.webp" '
            f'width="900" height="600" loading="lazy" alt="Motorized exterior patio shades on a covered patio"></div>'
            f'</div></section>'
            f'<section class="section bg-cream-tint"><div class="container center">'
            f'<h2 class="title">Types of outdoor and patio shades we install</h2></div>'
            f'<div class="container"><div class="prod-grid">{types}</div></div></section>'
            f'<section class="section"><div class="container center">'
            f'<h2 class="title">Patio shade questions, answered</h2></div>'
            f'<div class="container"><div class="faq">{faqhtml}</div></div></section>'
            f'<section class="section bg-cream-tint"><div class="container">'
            f'<h2 class="title">Patio shades across Texas</h2>'
            f'<p class="lead">We install exterior patio shades in every city we serve. A few of the '
            f'busiest:</p><div class="chips">{citylinks}</div>'
            f'<p><a class="btn-link" href="/areas-we-serve">All Texas service areas '
            f'<span class="arw">&rarr;</span></a></p></div></section>')
    open("products/exterior-patio-shades.html", "w").write(shell(url, title, desc, nodes, body))
    return len(PATIO_FAQ), len(PATIO_TYPES)
