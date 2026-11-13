"""Render the North Houston hub page (/north-houston-tx) only.

Adds the city to data/tx.json if missing, then renders it through
pages.render_city with two hub-specific touches kept in schema/visible
parity: a towns-served FAQ, and areaServed widened to Tomball, Magnolia
and Montgomery. Run from repo root: python3 build/houston_hub.py
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "build"))

CITY = {
    "slug": "north-houston-tx",
    "label": "North Houston",
    "url": "/north-houston-tx",
    "phone": "2818643309",   # North Houston GBP (Nov 13 2026)
    "street": "",
    "locality": "North Houston",
    "postal": "",
    "lat": 30.2315,
    "lng": -95.6877,
    "gbp": [],
    "twin": None,
    "geo_source": "area-centroid",
}

d = json.load(open("data/tx.json"))
if not any(c["slug"] == CITY["slug"] for c in d["cities"]):
    d["cities"].append(CITY)
    json.dump(d, open("data/tx.json", "w"), indent=1, ensure_ascii=False)
    print("added north-houston-tx to data/tx.json")

import pages  # noqa: E402  (loads data/tx.json at import, after the append)

c = next(x for x in pages.CITIES if x["slug"] == "north-houston-tx")

TOWNS_FAQ = (
    "Which North Houston communities does Love Is Blinds serve?",
    "This hub covers Tomball, Magnolia and Montgomery, plus the communities "
    "between them along SH 249, FM 1488 and SH 105. If your town is nearby "
    "but not named here, call (281) 864-3309 and ask; the free in-home "
    "consultation works the same way everywhere we serve.",
)

_orig_faqs = pages.faqs_for
def _faqs(city):
    f = _orig_faqs(city)
    if city["slug"] == "north-houston-tx":
        f = [TOWNS_FAQ] + f
    return f
pages.faqs_for = _faqs

html_out = pages.render_city(c)

# Widen areaServed from the single "North Houston" City node to the real towns.
AREA = [
    {"@type": "City", "name": "Tomball", "containedInPlace": {"@type": "State", "name": "Texas"}},
    {"@type": "City", "name": "Magnolia", "containedInPlace": {"@type": "State", "name": "Texas"}},
    {"@type": "City", "name": "Montgomery", "containedInPlace": {"@type": "State", "name": "Texas"}},
    {"@type": "AdministrativeArea", "name": "North Houston, TX"},
]

def widen(node):
    if isinstance(node, dict):
        a = node.get("areaServed")
        if isinstance(a, dict) and a.get("name") in ("North Houston", "North Houston, TX"):
            node["areaServed"] = AREA
        for v in node.values():
            widen(v)
    elif isinstance(node, list):
        for v in node:
            widen(v)

def patch_ld(m):
    data = json.loads(m.group(1))
    widen(data)
    return m.group(0).replace(m.group(1), json.dumps(data, ensure_ascii=False))

html_out = re.sub(
    r'<script type="application/ld\+json">(.*?)</script>',
    patch_ld, html_out, flags=re.S)

# Name the towns in the hero lead so the page says what it is above the fold.
html_out = html_out.replace(
    "</p>\n      <div class=\"hero-actions btnrow\">",
    " Serving Tomball, Magnolia, Montgomery and the communities between them."
    "</p>\n      <div class=\"hero-actions btnrow\">",
    1)

assert "Tomball" in html_out and "Magnolia" in html_out and "Montgomery" in html_out
assert html_out.rstrip().endswith("</html>") or "</html>" in html_out[-40:]
open("north-houston-tx.html", "w").write(html_out)
print("wrote north-houston-tx.html", len(html_out), "bytes")
