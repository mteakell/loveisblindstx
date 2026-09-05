"""Pages with no Georgia equivalent: the service-area index, the design checklist
and the team profiles."""
import json, os, re, sys, html, collections
sys.path.insert(0, os.path.dirname(__file__))
import schema as S, territory as T
import icons as IC

REVIEWS = json.load(open("data/reviews.json"))
GUARANTEES = json.load(open("data/guarantees.json"))["guarantees"]

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
D = json.load(open("data/tx.json")); BIZ, CITIES = D["business"], D["cities"]
HEAD = open("build/partials/header.html").read()
FOOT = open("build/partials/footer.html").read()
HEAD_INNER = HEAD.split("<body", 1)[1].split(">", 1)[1]
e = lambda s: html.escape(s or "", quote=True)

def shell(url, title, desc, nodes, body, img="/images/lib/shutters-shutters-060-jpg.webp"):
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

HERO = "/images/lib/shutters-shutters-060-jpg.webp"
SHUTTER_CITY = json.load(open("data/shutter-cities.json"))["cities"]
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
            f'</div></div></section>{tx_map()}{secs}')
    body += '''<section class="section closing-cta"><div class="container center">
<h2 class="title">Ready when your windows are</h2>
<p class="lead">Free in-home consultation anywhere we serve: samples at your door, measured by us, quoted in writing.</p>
<div class="btnrow" style="justify-content:center">
<a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a>
<a class="btn btn-secondary btn-lg" href="tel:+18665182999">Call (866) 518-2999</a>
</div></div></section>'''
    open("areas-we-serve.html", "w").write(shell(url, title, desc, nodes, body))
    return len(items)

# ------------------------------------------------------------------- /team/*
BIOS = json.load(open("data/team-bios.json"))

def team():
    made = []
    for m in T.TEAM:
        terr = T.TERRITORIES[m["territory"]] if m["territory"] else None
        url = f"/meet-the-team/{m['slug']}"
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
        shot = (f'<div class="media"><img class="owner-photo" src="{m["photo"]}" width="900" height="1125" '
                f'alt="{e(m["name"])}, {e(brand)}" fetchpriority="high"></div>'
                if m.get("photo") else "")
        body = (f'<section class="section"><div class="container split media-right">'
                f'<div class="body">'
                f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">&rsaquo;</span>'
                f'<a href="/meet-the-team">Meet the Team</a><span class="sep">&rsaquo;</span>'
                f'{e(m["name"])}</nav>'
                f'<h1 class="title">{e(m["name"])}</h1>'
                f'<p class="kicker">{e(brand)}</p>'
                f'<div class="prose"><p>{intro}</p>{bio}</div>'
                f'<div class="btnrow">'
                f'<a class="btn btn-primary btn-lg" href="/schedule-now">Book a consultation</a>'
                f'<a class="btn btn-secondary btn-lg" href="tel:{BIZ["tel"]}">Call {e(BIZ["phone"])}</a>'
                f'</div></div>{shot}</div></section>{area}')
        # the pages ran 130 to 215 words: a portrait, a bio and a city list.
        # Territory reviews and the guarantees give a visitor a reason to stay.
        _revs = []
        if terr:
            _slugs = {cc["slug"] for cc in CITIES if T.of(cc["slug"])["key"] == terr["key"]}
            _revs = sorted((r for r in REVIEWS
                            if r.get("slug") in _slugs and r.get("rating", 5) >= 4),
                           key=lambda r: r.get("date", ""), reverse=True)[:8]
        if _revs:
            _cards = "".join(
                '<article class="rv-card"><div class="rv-stars" aria-hidden="true">'
                '&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
                f'<p class="rv-quote">{e(r["quote"])}</p>'
                f'<footer class="rv-by"><span class="rv-name">{e(r["name"])}</span>'
                f'<span class="rv-city">{e(r["city"])}, TX</span></footer></article>' for r in _revs)
            body += (f'<section class="section bg-cream-tint rv-section rv-compact">'
                     f'<div class="container center"><h2 class="title">What {e(m["name"].split()[0])}\'s '
                     f'customers say</h2></div><div class="rv-wrap"><div class="rv-track" tabindex="0" '
                     f'role="region" aria-label="Customer reviews">{_cards}</div></div></section>')
        _g = "".join(
            f'<div class="type-card">{IC.guarantee_icon(g["id"])}<div class="pbody">'
            f'<h3>{e(g["name"])}</h3><p>{e(g["text"])}</p></div></div>' for g in GUARANTEES)
        body += (f'<section class="section"><div class="container center">'
                 f'<h2 class="title">Every job is backed five ways</h2></div>'
                 f'<div class="container"><div class="prod-grid gtee-grid">{_g}</div></div></section>')
        os.makedirs("meet-the-team", exist_ok=True)
        open(f"meet-the-team/{m['slug']}.html", "w").write(shell(url, title, desc, nodes, body))
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
    """/design-checklist: an interactive planner, not a static page.

    Duda's version was a 57-input questionnaire; the first rebuild dropped the
    form entirely. This is the standout version: tap through rooms, priorities,
    products and upgrades (the exact option lists from the Duda form), watch a
    live summary assemble, and send it to the same Formspree inbox as every
    other form. The eight editorial steps stay below for SEO and for people
    who want to read before they tap.
    """
    url, title = "/design-checklist", "Window Treatment Design Checklist | Love Is Blinds"
    desc = ("Build your window plan in ten minutes: rooms, priorities, products and "
            "upgrades, sent straight to your local Love Is Blinds owner so the free "
            "consultation turns into a quote in one visit.")
    ROOMS = ["Living room", "Primary bedroom", "Bedroom", "Kitchen", "Bathroom",
             "Home office", "Media room", "Dining room", "Patio / outdoor"]
    CONSIDER = ["Privacy (bedrooms & bathrooms)", "Adding Design to Your Space",
                "Sound Absorption", "Room Darkening / Blackout",
                "Reduce glare on screens and electronics", "Regulate in-home temperature",
                "Easy to use products", "Easy to clean"]
    PRODUCTS = ["Honeycomb Cellular Shades", "Faux Wood Blinds", "Wood Blinds",
                "Roller Shades", "Woven Wood Shades", "Fabric Roman Shades",
                "Dual Shade / Zebra Shades", "Faux Wood Shutters", "Wood Shutters",
                "Exterior Patio Shades"]
    UPGRADES = ["Cordless Shades / Blinds (Best for Kids & Pets)", "Motorized Operation",
                "Top Down Bottom Up", "No Holes or Cloth Tape (Wood / Faux Wood Blinds)",
                "Cornices / Valances / Top Treatments", "Invisible Tilt (Shutters)"]

    def chips(name, opts):
        return "".join(f'<button type="button" class="pchip" data-group="{name}" '
                       f'data-val="{e(o)}">{e(o)}</button>' for o in opts)

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

    js = (
"(function(){"
"var picked={consider:[],products:[],upgrades:[]};var rooms={};"
"function summarize(){var out=[];var rk=Object.keys(rooms);"
"if(rk.length)out.push('ROOMS: '+rk.map(function(r){return r+' ('+rooms[r]+(rooms[r]===1?' window)':' windows)')}).join(', '));"
"if(picked.consider.length)out.push('PRIORITIES: '+picked.consider.join(', '));"
"if(picked.products.length)out.push('INTERESTED IN: '+picked.products.join(', '));"
"if(picked.upgrades.length)out.push('UPGRADES: '+picked.upgrades.join(', '));"
"var tl=document.getElementById('wp-timeline').value;"
"if(tl)out.push('TIMELINE: '+tl);"
"document.getElementById('wp-plan').value=out.join('\\n');"
"var box=document.getElementById('wp-summary');"
"box.innerHTML=out.length"
"?out.map(function(l){var p=l.split(': ');return '<li><b>'+p[0].toLowerCase()+'</b> '+p.slice(1).join(': ')+'</li>'}).join('')"
":'<li class=empty>Tap options above and your plan builds itself here.</li>';"
"var total=rk.reduce(function(a,r){return a+rooms[r]},0);"
"document.getElementById('wp-count').textContent=total?total+' windows in '+rk.length+' rooms':'';}"
"document.querySelectorAll('.pchip').forEach(function(b){b.addEventListener('click',function(){"
"var g=b.getAttribute('data-group'),v=b.getAttribute('data-val');"
"if(g==='rooms'){if(rooms[v]===undefined){rooms[v]=1;b.classList.add('on');}else{delete rooms[v];b.classList.remove('on');}renderRooms();}"
"else{var i=picked[g].indexOf(v);if(i<0)picked[g].push(v);else picked[g].splice(i,1);b.classList.toggle('on',i<0);}"
"summarize();});});"
"function renderRooms(){var host=document.getElementById('wp-rooms');host.innerHTML='';"
"Object.keys(rooms).forEach(function(r){var row=document.createElement('div');row.className='wp-room';"
"row.innerHTML='<span>'+r+'</span><span class=wp-step>'"
"+'<button type=button aria-label=\"Fewer windows\">&minus;</button>'"
"+'<b>'+rooms[r]+'</b>'"
"+'<button type=button aria-label=\"More windows\">+</button></span>';"
"var btns=row.querySelectorAll('button');"
"btns[0].onclick=function(){if(rooms[r]>1)rooms[r]--;renderRooms();summarize();};"
"btns[1].onclick=function(){rooms[r]++;renderRooms();summarize();};"
"host.appendChild(row);});}"
"document.getElementById('wp-timeline').addEventListener('change',summarize);"
"summarize();})();")

    planner = (
        '<section class="section" id="planner"><div class="container">'
        '<div class="wp-grid">'
        '<form class="wp-form" action="https://formspree.io/f/xbgjdnvg" method="POST">'
        '<input type="hidden" name="_subject" value="New window plan - design checklist">'
        '<input type="hidden" name="window_plan" id="wp-plan">'

        '<div class="wp-block"><p class="kicker">1 &middot; Your rooms</p>'
        '<h2>Which rooms are we covering?</h2>'
        '<p class="wp-help">Tap every room on the list, then set how many windows each one has. '
        'Bay and corner windows count separately; that is where quotes usually surprise people.</p>'
        f'<div class="pchips">{chips("rooms", ROOMS)}</div>'
        '<div id="wp-rooms"></div></div>'

        '<div class="wp-block"><p class="kicker">2 &middot; Priorities</p>'
        '<h2>What matters most?</h2>'
        '<p class="wp-help">West and south rooms fight the Texas afternoon; bedrooms need to go '
        'dark; screens hate glare. Pick everything that applies.</p>'
        f'<div class="pchips">{chips("consider", CONSIDER)}</div></div>'

        '<div class="wp-block"><p class="kicker">3 &middot; Products</p>'
        '<h2>Anything you are already drawn to?</h2>'
        '<p class="wp-help">Skip this if you are not sure. That is what the samples at the '
        'consultation are for.</p>'
        f'<div class="pchips">{chips("products", PRODUCTS)}</div></div>'

        '<div class="wp-block"><p class="kicker">4 &middot; Upgrades</p>'
        '<h2>Worth-it extras</h2>'
        '<p class="wp-help">Cordless is a safety call with kids and pets. Motorization earns its '
        'keep on tall or hard-to-reach glass.</p>'
        f'<div class="pchips">{chips("upgrades", UPGRADES)}</div></div>'

        '<div class="wp-block"><p class="kicker">5 &middot; Timing</p>'
        '<h2>When do you need it done?</h2>'
        '<div class="form-row"><select id="wp-timeline" name="timeline">'
        '<option value="">No deadline yet</option>'
        '<option>As soon as possible</option><option>Within a month</option>'
        '<option>1 to 3 months</option><option>Just planning ahead</option></select></div>'
        '<div class="form-row"><label>Anything else we should know'
        '<textarea name="notes" rows="3" placeholder="Special shapes, arches, sliders, HOA rules..."></textarea></label></div></div>'

        '<div class="wp-block"><p class="kicker">6 &middot; Send it</p>'
        '<h2>Where should your plan go?</h2>'
        '<div class="form-grid">'
        '<label>Name<input type="text" name="name" required autocomplete="name"></label>'
        '<label>Phone<input type="tel" name="phone" required autocomplete="tel"></label>'
        '<label>Email<input type="email" name="email" required autocomplete="email"></label>'
        '<label>City<input type="text" name="city" required autocomplete="address-level2"></label>'
        '<label>How did you hear about us?<input type="text" name="hear_about"></label>'
        '<label>Referral name (if any)<input type="text" name="referral"></label>'
        '</div>'
        '<button class="btn btn-primary btn-lg" type="submit">Send my window plan</button>'
        '<p class="wp-fine">Your local owner reads this before the visit, so the consultation '
        'starts at the quote, not the questionnaire. No pressure, no obligation.</p></div>'
        '</form>'

        '<aside class="wp-side"><div class="wp-card">'
        '<p class="kicker">Your window plan</p>'
        '<p id="wp-count" class="wp-count"></p>'
        '<ul id="wp-summary" class="wp-sum"></ul>'
        '</div>'
        '<div class="wp-card wp-quiet"><p><b>Why this works:</b> owners quote in one visit when '
        'they arrive knowing the rooms, the priorities and the deadline. This plan is read by '
        'the owner who covers your city, not a call center.</p></div></aside>'
        '</div></div></section>'
        f'<script>{js}</script>')

    body = (f'<section class="phero"><picture><img src="' + HERO + '" alt="Custom window treatments by Love Is Blinds Texas" fetchpriority="high"></picture><div class="container"><div class="phero-copy">'
            f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span>&rsaquo;</span>'
            f'<span aria-current="page">Design Checklist</span></nav>'
            f'<h1 class="title">Plan Your Windows in Ten Minutes</h1>'
            f'<p class="lead">Tap through six quick steps and send your local owner a ready-made '
            f'window plan. Your free consultation turns into a quote in one visit instead of two.</p>'
            f'<div class="hero-actions btnrow"><a class="btn btn-primary btn-lg" href="#planner">Start your plan</a>'
            f'<a class="btn btn-secondary btn-lg" href="/schedule-now">Skip to booking</a></div>'
            f'</div></div></section>'
            + planner +
            f'<section class="section bg-cream-tint"><div class="container center">'
            f'<h2 class="title">Prefer to think it through first?</h2>'
            f'<p class="lead">The eight decisions behind the planner, in plain English.</p></div>'
            f'<div class="container"><div class="prod-grid">{items}</div>'
            f'<div class="btnrow"><a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a>'
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
        # No .reveal here. These cards now sit high on the page, and the reveal
        # transition can stall at opacity:0 when the observer fires before the
        # first paint, leaving the whole team section blank.
        cards += (f'<a class="prod-card" href="/meet-the-team/{m["slug"]}">{pic}<div class="pbody">'
                  f'<h3>{e(m["name"])}</h3><p class="kicker">{e(sub)}</p><p>{e(blurb)}</p>'
                  f'<span class="btn-link">Read more <span class="arw">&rarr;</span></span>'
                  f'</div></a>')
    block = (f'<section class="section bg-cream-tint"><div class="container center">'
             f'<h2 class="title">Meet Your Local Owner Operators</h2>'
             f'<p class="lead">Three franchises cover Texas. The person who quotes your window '
             f'treatments is the person who installs them.</p></div><div class="container">'
             f'<div class="team-grid">{cards}</div></div></section>\n')
    s = open("meet-the-team.html").read()
    # Fix the converted hero: the <source> still pointed at a purged portrait
    # (roman-005) and the <img> fallback was the dated woven-wood dining room.
    # One bright landscape shot, no stale source element.
    s = re.sub(
        r'<picture><source[^>]*>\s*<img[^>]*fetchpriority="high"[^>]*>',
        '<picture><img src="/images/lib/roller-shades-home-hero-shades-1-jpeg.webp" '
        'data-alt-final alt="A Texas living room with custom roller shades by Love Is Blinds" '
        'width="2000" height="1500" fetchpriority="high">',
        s, count=1)
    s = re.sub(r'<section class="section bg-cream-tint"><div class="container center">'
               r'<h2 class="title">(?:The three Texas teams|Meet Your Local Owner Operators)'
               r'.*?</section>\s*', lambda m: "", s, flags=re.S)
    # The converted intro carried a bedroom photo alt-texted as the owners.
    # Drop the media pane and let the intro text run full width.
    s = re.sub(r'<div class="media reveal">\s*<img class="owner-photo"[^>]*>\s*</div>\s*', "", s)
    s = s.replace('<div class="container split media-right"> <div class="body reveal"> '
                  '<h2 class="title">Meet the Owner-Operators</h2>',
                  '<div class="container" style="max-width:880px"> <div class="body reveal"> '
                  '<h2 class="title">Meet the Owner-Operators</h2>')
    s = s.replace("/images/lib/shutters-shutters-005-jpg.webp",
                  "/images/lib/roller-shades-home-hero-shades-1-jpeg.webp")
    # old Georgia-site hero lead: this is three owner-operators, not a couple
    s = s.replace("A husband-and-wife team that handles your project personally, "
                  "from first hello to final install.",
                  "Three owner-operators who handle your project personally, "
                  "from first hello to final install.")
    # owner photos are the FIRST thing under the hero
    hero_end = s.find("</section>", s.find('<section class="phero')) + len("</section>")
    open("meet-the-team.html", "w").write(s[:hero_end] + "\n" + block + s[hero_end:])
    return len(T.TEAM)

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
    body += '''<section class="section closing-cta"><div class="container center">
<h2 class="title">Ready when your windows are</h2>
<p class="lead">Free in-home consultation anywhere we serve: samples at your door, measured by us, quoted in writing.</p>
<div class="btnrow" style="justify-content:center">
<a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a>
<a class="btn btn-secondary btn-lg" href="tel:+18665182999">Call (866) 518-2999</a>
</div></div></section>'''
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
    HAS_PAGE = set(json.load(open("data/patio-cities.json"))["cities"])
    citylinks = "".join(
        f'<a class="chip" href="{("/patio-shades-" + s) if s in HAS_PAGE else BY[s]["url"]}">'
        f'Patio shades in {e(BY[s]["label"])}</a>' for s in patio_cities if s in BY)
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
            f'<div class="media reveal"><img src="/images/lib/roller-shades-roller-shades-137-jpg.webp" '
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

# --------------------------------------------------- /areas-we-serve map
# Simplified Texas border, (lng, lat), clockwise from the NW panhandle
# corner. Same projection as the city pins so everything lines up.
TX_OUTLINE = [
 (-101.813,36.502),(-100.000,36.502),(-100.000,34.563),(-99.923,34.574),(-99.699,34.382),
 (-99.578,34.415),(-99.261,34.404),(-99.189,34.212),(-98.987,34.223),(-98.768,34.136),
 (-98.571,34.147),(-98.488,34.065),(-98.362,34.158),(-98.171,34.114),(-98.089,34.004),
 (-97.946,33.988),(-97.870,33.851),(-97.694,33.982),(-97.459,33.906),(-97.371,33.824),
 (-97.256,33.862),(-97.174,33.736),(-96.922,33.961),(-96.851,33.846),(-96.632,33.846),
 (-96.424,33.774),(-96.347,33.687),(-96.150,33.840),(-95.936,33.889),(-95.838,33.835),
 (-95.602,33.933),(-95.547,33.878),(-95.290,33.873),(-95.224,33.961),(-94.967,33.862),
 (-94.868,33.747),(-94.485,33.637),(-94.381,33.544),(-94.184,33.594),(-94.041,33.550),
 (-94.041,33.019),(-94.041,31.994),(-93.822,31.775),(-93.817,31.556),(-93.543,31.151),
 (-93.526,30.937),(-93.630,30.680),(-93.729,30.576),(-93.696,30.439),(-93.767,30.335),
 (-93.691,30.143),(-93.926,29.787),(-93.839,29.689),(-94.003,29.683),(-94.523,29.546),
 (-94.709,29.623),(-94.742,29.787),(-94.874,29.672),(-94.967,29.700),(-95.016,29.557),
 (-94.912,29.497),(-94.896,29.311),(-95.082,29.113),(-95.383,28.867),(-95.985,28.604),
 (-96.046,28.648),(-96.226,28.582),(-96.232,28.642),(-96.478,28.599),(-96.593,28.725),
 (-96.665,28.697),(-96.402,28.440),(-96.593,28.358),(-96.774,28.407),(-96.802,28.226),
 (-97.026,28.040),(-97.256,27.695),(-97.404,27.333),(-97.514,27.361),(-97.541,27.229),
 (-97.426,27.262),(-97.481,26.999),(-97.557,26.988),(-97.563,26.841),(-97.470,26.758),
 (-97.442,26.457),(-97.333,26.353),(-97.305,26.161),(-97.218,25.992),(-97.524,25.888),
 (-97.650,26.019),(-97.886,26.068),(-98.198,26.057),(-98.467,26.222),(-98.669,26.238),
 (-98.823,26.370),(-99.031,26.413),(-99.173,26.539),(-99.266,26.841),(-99.447,27.021),
 (-99.425,27.175),(-99.507,27.339),(-99.480,27.481),(-99.606,27.640),(-99.710,27.657),
 (-99.880,27.799),(-99.934,27.980),(-100.082,28.144),(-100.296,28.281),(-100.400,28.582),
 (-100.498,28.664),(-100.630,28.905),(-100.674,29.103),(-100.800,29.245),(-101.013,29.371),
 (-101.063,29.459),(-101.260,29.535),(-101.413,29.754),(-101.851,29.804),(-102.114,29.793),
 (-102.339,29.869),(-102.388,29.765),(-102.629,29.732),(-102.810,29.524),(-102.919,29.190),
 (-102.980,29.185),(-103.116,28.987),(-103.281,28.982),(-103.527,29.135),(-104.146,29.382),
 (-104.267,29.513),(-104.508,29.639),(-104.677,29.924),(-104.688,30.181),(-104.858,30.390),
 (-104.896,30.570),(-105.006,30.685),(-105.395,30.855),(-105.603,31.085),(-105.773,31.167),
 (-105.954,31.364),(-106.205,31.469),(-106.381,31.731),(-106.529,31.786),(-106.644,31.901),
 (-106.616,32.000),(-103.067,32.000),(-103.067,33.002),(-103.045,34.015),(-103.040,36.502),
 (-103.001,36.502),(-101.813,36.502),
]
_LNG0, _LAT1, _XS, _YS = -106.75, 36.65, 86.0, 100.0

def _mpt(lng, lat):
    return round((lng - _LNG0) * _XS, 1), round((_LAT1 - lat) * _YS, 1)

TKEY_CLASS = {"dfw": "t-dfw", "north": "t-north", "eastwaco": "t-east"}

ANCHOR_PINS = {"dallas-tx", "fort-worth-tx", "austin-tx", "waco-tx", "tyler-tx", "sherman-tx"}
# nudge colliding anchor labels apart in the metroplex
LBL_OFFSET = {"fort-worth-tx": (-16, "end"), "dallas-tx": (16, "start")}

def _county_paths():
    """One faint path per Texas county ring, clipped to the state shape."""
    feats = json.load(open("data/tx-counties.json"))
    d = []
    for f in feats:
        g = f["geometry"]
        polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        for poly in polys:
            for ring in poly:
                seg = [_mpt(lng, lat) for lng, lat in ring]
                d.append("M" + " ".join(f"{round(x)},{round(y)}" for x, y in seg) + "Z")
    return "".join(d)

def tx_map():
    pts = " ".join(f"{x},{y}" for x, y in (_mpt(*p) for p in TX_OUTLINE))
    pins, xs, ys = [], [], []
    for c in sorted(CITIES, key=lambda x: -x["lat"]):   # north pins first, so
        x, y = _mpt(c["lng"], c["lat"])                 # southern labels stack on top
        tk = [k for k in TKEY_CLASS if T.of(c["slug"])["name"] == T.TERRITORIES[k]["name"]][0]
        if tk in ("dfw", "north"): xs.append(x); ys.append(y)
        anchor = " anchor" if c["slug"] in ANCHOR_PINS else ""
        dx, ta = LBL_OFFSET.get(c["slug"], (0, "middle"))
        pins.append(
            f'<a class="mpin {TKEY_CLASS[tk]}{anchor}" href="{c["url"]}" transform="translate({x},{y})">'
            f'<title>{e(c["label"])}, TX</title><circle class="halo" r="14"></circle>'
            f'<circle class="pt" r="9"></circle>'
            f'<text x="{dx}" y="-15" style="text-anchor:{ta}">{e(c["label"])}</text></a>')
    pad = 55
    dfw_vb = (f"{round(min(xs)-pad,1)} {round(min(ys)-pad,1)} "
              f"{round(max(xs)-min(xs)+2*pad,1)} {round(max(ys)-min(ys)+2*pad,1)}")
    full_vb = "0 0 1150 1095"
    js = """
(function(){
  var svg=document.getElementById('txmap');if(!svg)return;
  var btns=document.querySelectorAll('.txmap-toggle button');
  function parse(v){return v.split(' ').map(Number)}
  function setVB(v){svg.setAttribute('viewBox',v.join(' '))}
  function go(target,zoomed){
    var from=parse(svg.getAttribute('viewBox')),to=parse(target),t0=null;
    svg.classList.toggle('zoomed',zoomed);
    function step(ts){
      if(t0===null)t0=ts;var k=Math.min(1,(ts-t0)/350);k=1-Math.pow(1-k,3);
      setVB(from.map(function(f,i){return f+(to[i]-f)*k}));
      if(k<1)requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
    setTimeout(function(){setVB(to)},450);
  }
  btns.forEach(function(b){b.addEventListener('click',function(){
    btns.forEach(function(o){o.classList.remove('on')});b.classList.add('on');
    go(b.getAttribute('data-vb'),b.hasAttribute('data-zoom'));
  })});
})();"""
    return (
        '\n<section class="section txmap-section"><div class="container center">'
        '<h2 class="title">Tap your city on the map</h2>'
        '<p class="lead">Every pin is a city page with the local number, reviews from your '
        'neighbors and directions to the team that covers you. Do not see your town? We still '
        'likely serve you, so call and ask.</p></div>'
        '<div class="container"><div class="txmap-card">'
        '<div class="txmap-head">'
        '<div class="txmap-legend">'
        '<span><i class="dot t-dfw"></i>DFW</span>'
        '<span><i class="dot t-north"></i>North Texas</span>'
        '<span><i class="dot t-east"></i>East &amp; Central Texas</span></div>'
        f'<div class="txmap-toggle" role="group" aria-label="Map zoom">'
        f'<button type="button" class="on" data-vb="{full_vb}">All of Texas</button>'
        f'<button type="button" data-vb="{dfw_vb}" data-zoom>DFW &amp; North Texas</button>'
        '</div></div>'
        f'<svg id="txmap" viewBox="{full_vb}" role="img" '
        'aria-label="Map of Texas showing every Love Is Blinds service city">'
        f'<defs><clipPath id="txclip"><polygon points="{pts}"></polygon></clipPath></defs>'
        f'<polygon class="txshape" points="{pts}"></polygon>'
        f'<path class="txcounties" clip-path="url(#txclip)" d="{_county_paths()}"></path>'
        f'<polygon class="txedge" points="{pts}"></polygon>{"".join(pins)}</svg>'
        f'</div></div><script>{js}</script></section>\n')


if __name__ == "__main__":
    print("areas-we-serve:", areas(), "cities")
    print("team pages    :", ", ".join(team()))
    print("owner cards   :", team_cards())
    checklist(); print("design-checklist: written")
