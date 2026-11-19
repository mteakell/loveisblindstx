"""Render the rewritten original city pages, batch by batch (biggest first).

Copy lives in build/city_copy_batch*.py. Facts come from data at render time:
phone, street address and Google profile from data/tx.json, the operator from
build/territory.py, reviews from data/reviews.json (via pages.BY_CITY), the
<title> from pages.title_for() so each page keeps the keyword it already
ranks for. Rewritten cities are marked "custom" in data/tx.json so pages.py
and product_city.py skip them on a full rebuild.

Run from the repo root: python3 build/city_batches.py
"""
import importlib, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(ROOT)

BATCHES = ["city_copy_batch1"]
CITIES = []
for b in BATCHES:
    CITIES += importlib.import_module(b).CITIES

d = json.load(open("data/tx.json"))
by = {c["slug"]: c for c in d["cities"]}
for t in CITIES:
    by[t["slug"]]["custom"] = True
json.dump(d, open("data/tx.json", "w"), indent=1, ensure_ascii=False)

import pages as P, territory as T, city_v2 as V  # noqa: E402


def reviews_for(slug, n=3):
    out = []
    for r in P.BY_CITY.get(slug, []):
        q = (r.get("quote") or "").strip()
        if not q or "?" in q or len(q) < 60 or len(q) > 420 or int(r.get("rating", 5)) < 5:
            continue          # questions, one-liners and essays read badly as pull quotes
        out.append((q, r["name"]))
    out.sort(key=lambda x: -len(x[0]))
    return out[:n]


def ctx_for(t):
    c = P.BY[t["slug"]]
    terr = T.of(t["slug"])
    leads = terr.get("leads") or []
    named = terr.get("name_cities", True) and leads
    who = " and ".join(leads)
    team_rule = (f"Measured and installed by the {terr['brand']} team, run by {who}" if named
                 else f"Measured and installed by the same local {terr['brand']} team")
    near = [o for o in P.nearby(c, 8) if not o.get("hub")][:5]
    addr = (f"{c['street']}, {c['locality']}, TX {c.get('postal', '')}".strip() if c.get("street") else None)
    return dict(
        phone=c["phone"] or P.BIZ["tel"], eyebrow=terr["brand"], crumbs=[],
        team_rule=team_rule, team_call=f"Call {terr['brand']}",
        near=[(o["label"], o["url"], round(V.miles(c, o))) for o in near],
        near_all=("All Texas service areas", "/areas-we-serve", ""),
        map_src=P.map_embed(c), title=P.title_for(c), extra=t["extra"],
        reviews=reviews_for(t["slug"]), address=addr,
        gbp=(c.get("gbp") or [None])[0])


for t in CITIES:
    open(t["slug"] + ".html", "w", encoding="utf-8").write(V.render(t, ctx_for(t)))
print(f"city_batches: wrote {len(CITIES)} city pages")
