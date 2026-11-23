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

import pages as P, schema as S  # noqa: E402  (load after tx.json is updated)
import city_v2 as V  # noqa: E402

e = V.e
BYSLUG = {t["slug"]: t for t in TOWNS}


def ctx_for(t):
    near = sorted((o for o in TOWNS if o["slug"] != t["slug"]), key=lambda o: V.miles(t, o))[:5]
    return dict(
        phone=PHONE, eyebrow="Love Is Blinds \u00b7 North Houston",
        crumbs=[("North Houston", "/north-houston-tx")],
        team_rule="Measured and installed by the same local North Houston team",
        team_call="Call your North Houston team",
        near=[(o["label"], "/" + o["slug"], round(V.miles(t, o))) for o in near],
        near_all=("All of North Houston", "/north-houston-tx", f"{len(TOWNS)} towns"),
        map_src=f"https://www.google.com/maps?q={t['label'].replace(' ', '+')},+TX&output=embed",
        extra=EXTRA[t["slug"]])


def render(t):
    return V.render(t, ctx_for(t))


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
