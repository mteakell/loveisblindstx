"""Add a "{Product} by city" link block to each product's main page.

Every product-city page (/{product}-{city}-tx) gets a link from its parent
product page, grouped by team, so Google and visitors can reach all of them
from the nav without a 600-item menu. Idempotent: the block sits between
<!-- pc:cities --> markers and is replaced on every run.
Run from the repo root after build/pc_v2.py: python3 build/pc_hub_links.py
"""
import html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(ROOT)
import pages as P, products_spec as PS, territory as T, pc_v2  # noqa: E402

e = lambda s: html.escape(s or "", quote=True)
MARK = re.compile(r"\n?<!-- pc:cities -->.*?<!-- /pc:cities -->\n?", re.S)
ORDER = ["north", "dfw", "austin", "waco", "cedarcreek", "houston", "tyler"]

n = 0
for prod, spec in PS.SPEC.items():
    path = pc_v2.product_url(prod).lstrip("/") + ".html"
    if not os.path.exists(path):
        continue
    groups = {}
    for c in P.CITIES:
        if c.get("hub") or not os.path.exists(f"{spec['slug']}-{c['slug']}.html"):
            continue
        groups.setdefault(T.of(c["slug"])["key"], []).append(c)
    if not groups:
        continue
    cols = ""
    for k in ORDER + [g for g in groups if g not in ORDER]:
        if k not in groups:
            continue
        cs = sorted(groups[k], key=lambda c: c["label"])
        name = T.TERRITORIES[k]["name"]
        cols += (f'<div class="pc-col"><h3>{e(name)}</h3><ul>'
                 + "".join(f'<li><a href="/{spec["slug"]}-{c["slug"]}">{e(c["label"])}'
                           f'{" (" + e(c["variant"]) + ")" if c.get("variant") else ""}</a></li>' for c in cs)
                 + "</ul></div>")
    block = ('\n<!-- pc:cities --><section class="section pc-cities"><div class="container">'
             f'<h2 class="title">{e(spec["label"])} by city</h2>'
             f'<p class="lead">Local pages for {e(spec["label"].lower())} in every Texas city we serve, with the team, '
             'phone and reviews for that area.</p>'
             f'<div class="pc-grid">{cols}</div></div></section><!-- /pc:cities -->\n')
    s = open(path, encoding="utf-8").read()
    s = MARK.sub("\n", s)
    anchor = s.rfind("<footer")
    s = s[:anchor] + block + s[anchor:]
    open(path, "w", encoding="utf-8").write(s)
    n += 1
print(f"pc_hub_links: {n} product pages updated")
