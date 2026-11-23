"""Product-city pages (/{product}-{city}-tx) in the editorial layout (css/city.css).

Each page = the unique layer written for that product in that city
(build/pc_copy/{product}.json: lead, p1, p2, two city FAQs) + the product's
own options, reasons and price drivers (products_spec / variants /
extra_pools) + real Google reviews that mention the product (same city
first, then the same territory) + the local team, phone and Google profile
from data + links to the city page, the city's other products and the same
product in nearby cities.

Pages without a copy entry are not written (the old template stays).
Run from the repo root: python3 build/pc_v2.py
"""
import html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(ROOT)
import pages as P, schema as S, territory as T, products_spec as PS, variants as VR, extra_pools as EP  # noqa: E402
import product_city as PC, city_v2 as CV  # noqa: E402

e = CV.e
BIZ = P.BIZ
ARROW = CV.ARROW
PRODUCT_URL = {"plantation-shutters": "/products/plantation-shutters", "blinds": "/products/blinds",
               "shades": "/products/shades", "shutters": "/products/shutters",
               "patio-shades": "/products/exterior-patio-shades",
               "motorized-shades": "/products/motorized-window-treatment-automations"}
REVIEW_KEYS = {
    "roller-shades": ["roller", "solar shade"], "honeycomb-shades": ["honeycomb", "cellular"],
    "roman-shades": ["roman"], "woven-wood-shades": ["woven", "bamboo"],
    "dual-shades": ["zebra", "dual", "banded"], "panel-track-shades": ["panel track", "slider", "sliding"],
    "faux-wood-blinds": ["faux"], "wood-blinds": ["wood blind", "wooden blind", "real wood"],
    "drapery": ["drape", "drapery", "curtain"], "blinds": ["blind"], "shades": ["shade"],
    "plantation-shutters": ["shutter"], "shutters": ["shutter"],
    "patio-shades": ["patio", "porch", "outdoor", "exterior"],
    "motorized-shades": ["motor", "remote", "automat", "smart"],
}
COPY = {}
for p in PS.SPEC:
    f = f"build/pc_copy/{p}.json"
    if os.path.exists(f):
        COPY[p] = json.load(open(f))


def product_url(prod):
    return PS.SPEC[prod].get("product_url") or PRODUCT_URL[prod]


def stem(fname):
    return fname[:-5] if fname.endswith(".webp") else fname


def reviews_for(prod, slug, n=3):
    keys = REVIEW_KEYS[prod]
    terr = T.of(slug)["key"]
    # a review that praises an owner by name only belongs where that owner works now
    here = {x.split()[0].lower() for x in (T.of(slug).get("leads") or [])}
    names = {"danny", "roeweder", "rohweder", "durrell", "jake", "jonathan", "zeke", "ashlyn"}
    def ok(r):
        q = (r.get("quote") or "").strip()
        low = q.lower()
        named = {nm for nm in names if re.search(r"\b" + nm + r"\b", low)}
        if named - here - ({"roeweder", "rohweder"} if "danny" in here else set()):
            return False
        return (q and "?" not in q and 60 <= len(q) <= 420 and int(r.get("rating", 5)) == 5
                and any(k in low for k in keys))
    own = [r for r in P.BY_CITY.get(slug, []) if ok(r)]
    if len(own) < n:
        seen = {r["quote"] for r in own}
        for s2, rs in P.BY_CITY.items():
            if s2 == slug or T.of(s2)["key"] != terr:
                continue
            own += [r for r in rs if ok(r) and r["quote"] not in seen]
    own.sort(key=lambda r: (r.get("slug") != slug, -len(r["quote"])))
    out, seen_who = [], set()
    for r in own:
        if len(out) == n:
            break
        if r["name"].lower() in seen_who:      # the same reviewer posted twice on some profiles
            continue
        seen_who.add(r["name"].lower())
        where = P.BY.get(r.get("slug"), {}).get("label") or r.get("city") or ""
        out.append((r["quote"], r["name"], where))
    return out


def render(prod, slug):
    spec = PS.SPEC[prod]
    cp = COPY[prod][slug]
    c = P.BY[slug]
    city = c["label"]
    label = f"{city} ({c['variant']})" if c.get("variant") else city
    terr = T.of(slug)
    phone = c["phone"] or re.sub(r"\D", "", BIZ["tel"])[-10:]
    ph, tel = S.pretty(phone), S.tel(phone)
    url = f"/{spec['slug']}-{slug}"
    base = spec["title"].format(city=label)
    title = PC.fit([f"{base} | Love Is Blinds", base, base.replace("Custom ", "")])
    desc = spec["desc"].format(city=label, phone=ph)
    desc = desc if len(desc) <= 155 else desc[:155].rsplit(" ", 1)[0]
    leads = terr.get("leads") or []
    named = (terr.get("name_cities", True) or slug in terr.get("named_slugs", ())) and leads
    who = " and ".join(leads)
    team_rule = (f"Measured and installed by the {terr['brand']} team, run by {who}" if named
                 else f"Measured and installed by the same local {terr['brand']} team")

    _hp = PC.HERO_POOL[prod]
    hero = stem(PC.pick(_hp, slug, 19))
    pool = [stem(x.rsplit("/", 1)[-1]) for x in PC.IMG_POOL[prod]]
    pics = [x for x in PC.pick_many(pool, slug, 4, 3) if x != hero] or pool
    why_pic = pics[0]
    band_pic = pics[1] if len(pics) > 1 else pics[0]

    _items = [x for x in terr["blurb"].replace(" and ", ", ").split(", ") if x != city]
    _bl = ", ".join(_items[:-1]) + " and " + _items[-1] if len(_items) > 1 else _items[0]
    install_q = (f"Do you install {spec['label'].lower()} in {city}?",
                 (f"Yes. {who} run{'s' if len(leads) == 1 else ''} {terr['brand']}, which covers {city} along with {_bl}. "
                  if named else f"Yes. {terr['brand']} covers {city} along with {_bl}. ")
                 + f"The team that measures your windows installs them. Call {ph}.")
    faqs = [tuple(x) for x in cp["faqs"]] + [install_q] + PC.pick_many(spec["faq"] + EP.EXTRA_FAQ[prod], slug, 3, 11) + [
        (f"How much do {spec['label'].lower()} cost in {city}?",
         "It depends on the size of each opening, the material and the options you choose. We measure every "
         "opening on site and give you a written quote with installation included. The consultation is free.")]

    tlist = PC.pick_many(spec["types"] + EP.EXTRA_TYPES[prod], slug, 6, 5)
    why_h, why_body = PC.pick(VR.WHY[prod], slug, 7)
    plist = PC.pick_many(spec["price"], slug, len(spec["price"]), 17)
    revs = reviews_for(prod, slug)
    others = [(o, PS.SPEC[o]) for o in PS.SPEC if o != prod and os.path.exists(f"{PS.SPEC[o]['slug']}-{slug}.html")]
    near = [o for o in P.nearby(c, 8) if not o.get("hub") and os.path.exists(f"{spec['slug']}-{o['slug']}.html")][:5]
    gbp = (c.get("gbp") or [None])[0]

    crumbs = [("Home", "/"), (f"{city}, TX", c["url"]), (spec["label"], url)]
    nodes = [S.organization(BIZ), S.website(BIZ), S.business(BIZ), S.business(BIZ, c),
             S.webpage(url, title, desc, about=f"{S.SITE}{c['url']}#business", primary=CV.img(hero)),
             S.breadcrumbs(crumbs),
             S.faq(url, faqs),
             S.service(url, f"{spec['label']} in {city}, TX",
                       f"Measurement, custom order and professional installation of "
                       f"{spec['label'].lower()} for homes in {city}, Texas.",
                       f"{S.SITE}{c['url']}#business",
                       area={"@type": "City", "name": c["locality"]},
                       catalog=[n for n, _ in spec["types"]])]

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
<meta property="og:image" content="{S.SITE}{CV.img(hero)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="US-TX">
<meta name="geo.placename" content="{e(c.get('locality') or city)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css">
<link rel="stylesheet" href="/css/city.css?v={CV.CITY_V}">
{S.render(nodes)}
</head>'''

    rules = "".join(f'<li><b>0{i+1}</b><span>{x}</span></li>' for i, x in enumerate([
        "Free in-home consultation with samples you can hold against your own light",
        "Every opening measured on site before anything is ordered",
        team_rule,
        "Remade at no cost if it does not match the approved measurements"]))
    options = "".join(f'<li><strong>{e(n)}</strong>{e(b)}</li>' for n, b in tlist)
    prices = "".join(f'<li>{e(x)}</li>' for x in plist)
    rev_html = ""
    if revs:
        cards = "".join(f'<blockquote class="cx-rv"><p>{e(q)}</p><cite>{e(n)}{", " + e(w) if w else ""}</cite></blockquote>'
                        for q, n, w in revs)
        rev_html = (f'<section class="cx-revs"><div class="wrap"><div class="cx-eyebrow">From our Google reviews</div>'
                    f'<h2 style="margin-top:12px">What homeowners say about their {e(spec["label"].lower())}</h2>'
                    f'<div class="cx-revgrid">{cards}</div></div></section>')
    other_li = "".join(f'<a href="/{o["slug"]}-{slug}"><span>{e(o["label"])}</span>{ARROW}</a>' for _, o in others)
    near_li = "".join(f'<li><a href="/{spec["slug"]}-{o["slug"]}">{e(spec["label"])} in {e(o["label"])}, TX '
                      f'<em>{round(CV.miles(c, o))} mi</em></a></li>' for o in near)
    faqhtml = "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faqs)
    crumb_html = (f'<a href="/">Home</a><span>/</span><a href="{c["url"]}">{e(city)}, TX</a>'
                  f'<span>/</span>{e(spec["label"])}')
    gbp_link = (f'<a class="cx-link" href="{e(gbp)}" rel="noopener">Our Google Business Profile {ARROW}</a>' if gbp else "")

    body = f"""<body>
{P.HEAD.split('<body', 1)[1].split('>', 1)[1]}
<main class="cx">
<section class="cx-hero cx-par" data-par="0.18">
  <img src="{CV.img(hero)}" alt="{e(spec['label'])} from {e(terr['brand'])}, the kind we measure and install for {e(city)}, TX homes" width="2000" height="1500" fetchpriority="high" srcset="{CV.srcset(hero)}, {CV.img(hero)} 2000w" sizes="100vw">
  <nav class="cx-crumbs" aria-label="Breadcrumb">{crumb_html}</nav>
  <div class="wrap"><div class="cx-hero-row">
    <div>
      <div class="cx-eyebrow" style="color:#fff;opacity:.85">{e(terr['brand'])}</div>
      <h1>{e(spec['h1'])} in {e(label)}, Texas</h1>
      <p class="cx-lead">{e(cp['lead'])}</p>
      <div class="cx-actions">
        <a class="cx-btn cx-btn-light" href="tel:{tel}">Call {e(ph)}</a>
        <a class="cx-btn cx-btn-line" href="#consult">Book a free consultation</a>
      </div>
    </div>
    <div class="cx-hero-tag"><i></i>Scroll</div>
  </div></div>
</section>

<section class="cx-intro"><div class="wrap">
  <div class="cx-rv"><div class="cx-eyebrow">{e(spec['label'])} for {e(city)} homes</div>
    <p class="cx-statement" style="margin-top:18px">{e(cp['p1'])}</p></div>
  <div class="cx-rv"><p>{e(cp['p2'])}</p><ul class="cx-rules">{rules}</ul>
    <a class="cx-link" href="#consult">Book your free consultation {ARROW}</a></div>
</div></section>

<section class="cx-plan"><div class="wrap">
  <div class="cx-rv"><div class="cx-eyebrow">Options</div><h2 style="margin-top:12px">{e(spec['label'])} we install in {e(city)}</h2>
    <p style="margin-top:18px">{e(spec['lead'])}</p>
    <a class="cx-link" href="{product_url(prod)}">All about {e(spec['label'].lower())} {ARROW}</a></div>
  <div class="cx-rv"><ul>{options}</ul></div>
</div></section>

<section class="cx-ch wide"><div class="wrap">
  <div class="cx-ch-text cx-rv"><div class="cx-num">01</div><div class="cx-eyebrow">{e(spec['label'])}</div>
    <h2>{e(why_h)}</h2><p>{e(why_body)}</p>
    <a class="cx-link" href="{c['url']}">Window treatments in {e(city)} {ARROW}</a></div>
  <figure class="cx-ch-media cx-rv" style="margin-left:0;margin-right:0">
    <div class="cx-par cx-frame" data-par="0.10"><img src="/images/lib/r/1600/{why_pic}.webp" data-alt-final alt="{e(spec['label'])} in a finished Love Is Blinds install, shown for {e(city)}, TX homes" loading="lazy" width="1600" height="1200" srcset="{CV.srcset(why_pic)}" sizes="(max-width: 900px) 100vw, 50vw"></div>
    <figcaption class="cx-cap"><span>{e(spec['label'])} from a Love Is Blinds install.</span><span>{e(city)}, TX homes</span></figcaption>
  </figure>
</div></section>

<section class="cx-band cx-par" data-par="0.16">
  <img src="/images/lib/r/1600/{band_pic}.webp" data-alt-final alt="{e(spec['label'])} measured and installed by Love Is Blinds, the service we bring to {e(city)}" loading="lazy" width="1600" height="1200" srcset="{CV.srcset(band_pic)}" sizes="100vw">
  <div class="wrap"><div class="cx-eyebrow">{e(city)}, Texas</div><h2>What moves the price of {e(spec['label'].lower())}</h2></div>
</section>

<section class="cx-plan"><div class="wrap">
  <div class="cx-rv"><div class="cx-eyebrow">Your quote</div>
    <p style="margin-top:18px">We measure every opening and quote from those measurements, in writing, with installation included.</p>
    <a class="cx-link" href="#consult">Get {e(spec['label'].lower())} priced {ARROW}</a></div>
  <div class="cx-rv"><ul>{prices}</ul></div>
</div></section>

{rev_html}

<section class="cx-prod"><div class="wrap">
  <div class="cx-prod-head cx-rv"><div><div class="cx-eyebrow">More in {e(city)}</div><h2 style="margin-top:12px">Other treatments we install in {e(city)}</h2></div>
    <p><a href="{c['url']}">See the {e(city)} page</a> for how we plan a whole house there.</p></div>
  <div class="cx-plist cx-plist-text cx-rv">{other_li}</div>
</div></section>

<section class="cx-area"><div class="wrap">
  <iframe class="cx-map cx-rv" src="{P.map_embed(c)}" title="Map of {e(city)}, TX" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
  <div class="cx-rv"><div class="cx-eyebrow">Service area</div><h2 style="margin-top:12px">{e(spec['label'])} near {e(city)}</h2>
    {gbp_link}<ul class="cx-near">{near_li}</ul></div>
</div></section>

<section class="cx-faq"><div class="wrap">
  <div class="cx-rv"><div class="cx-eyebrow">Questions</div><h2 style="margin-top:12px">{e(spec['label'])} questions from {e(city)}</h2></div>
  <div class="cx-rv">{faqhtml}</div>
</div></section>

<section class="cx-close" id="consult">
  <div class="cx-close-dark">
    <div><div class="cx-eyebrow" style="color:var(--pop)">Free in-home consultation</div>
      <h2 style="margin-top:14px">Get {e(spec['label'].lower())} priced for your {e(city)} windows</h2>
      <p>Samples at your door, every opening measured, and a written quote with installation included before you decide anything.</p></div>
    <div><small>Call {e(terr['brand'])}</small><a class="cx-phone" href="tel:{tel}">{e(ph)}</a></div>
  </div>
  <div class="cx-close-form">{CV.form_html(city).replace('name="city" value=', 'name="product" value="' + e(spec['label']) + '"><input type="hidden" name="city" value=', 1)}</div>
</section>
</main>
{CV.SCRIPT}
{P.FOOT}"""
    return head + "\n" + body


if __name__ == "__main__":
    n = 0
    only = sys.argv[1:]
    for prod in PS.SPEC:
        if prod not in COPY or (only and prod not in only):
            continue
        for slug in COPY[prod]:
            if slug not in P.BY:
                continue
            open(f"{PS.SPEC[prod]['slug']}-{slug}.html", "w", encoding="utf-8").write(render(prod, slug))
            n += 1
    print(f"pc_v2: wrote {n} product-city pages")
