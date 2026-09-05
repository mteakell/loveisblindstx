"""Blog posts link back to money pages, and link equity spreads to the
least-linked sibling posts instead of piling onto the same few.

Idempotent via the lib:crosslinks marker. Runs after gen_posts/blog_images.
"""
import collections, glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import blog_images as BI

IDX = json.load(open("data/blog-index.json"))
PRODUCT = {
 "patio": ("/products/exterior-patio-shades", "Exterior patio shades"),
 "shutters": ("/products/plantation-shutters", "Plantation shutters"),
 "roman": ("/products/roman-shades", "Roman shades"),
 "woven": ("/products/woven-wood-shades", "Woven wood shades"),
 "banded": ("/products/dual-shades", "Dual shades"),
 "honeycomb": ("/products/honeycomb-shades", "Honeycomb shades"),
 "drapes": ("/products/window-treatment-automations", "Motorization"),
 "roller": ("/products/roller-shades", "Roller shades"),
 "blinds": ("/products/blinds", "Custom blinds"),
}
SERVICE = {
 "shutters": [("/services/shutters-installation", "Shutter installation"),
              ("/services/shutter-solutions", "Shutter solutions")],
 "blinds": [("/services/blinds-installation", "Blinds installation"),
            ("/services/blinds-solutions", "Blinds solutions")],
 "drapes": [("/services/drapery-installation", "Drapery installation")],
}
SHADE_SVC = [("/services/shades-installation", "Shade installation"),
             ("/services/shades-solutions", "Shade solutions")]
for _f in ("roller", "honeycomb", "roman", "woven", "banded", "patio"):
    SERVICE[_f] = SHADE_SVC
DEF_PROD = ("/products", "All products")
DEF_SVC = [("/services/window-treatment-installation", "Installation service")]


def fam_of(post):
    t = (post["title"] + " " + (post.get("desc") or "")).lower()
    best = None
    for name, prefixes, words in BI.FAMILY:
        hits = sum(t.count(w) for w in words)
        if hits and (best is None or hits > best[0]):
            best = (hits, name)
    return best[1] if best else "roller"


def main():
    posts = {p["url"]: p for p in IDX}
    files = {u: u.lstrip("/") + ".html" for u in posts}
    files = {u: f for u, f in files.items() if os.path.exists(f)}
    fams = {u: fam_of(posts[u]) for u in files}

    # count inlinks between posts only, to find the starved ones
    inlinks = collections.Counter({u: 0 for u in files})
    for u, f in files.items():
        s = open(f).read()
        for v in files:
            if v != u and f'href="{v}"' in s:
                inlinks[v] += 1

    n = 0
    for u, f in sorted(files.items()):
        s = open(f).read()
        s = re.sub(r'\n?<!-- lib:crosslinks -->.*?<!-- /lib:crosslinks -->\n?', "\n", s, flags=re.S)
        fam = fams[u]
        prod = PRODUCT.get(fam, DEF_PROD)
        svcs = SERVICE.get(fam, DEF_SVC)
        sibs = sorted((v for v in files if v != u and fams[v] == fam),
                      key=lambda v: (inlinks[v], v))[:2]
        sib_html = "".join(
            f'<li><a href="{v}">{posts[v]["title"]}</a></li>' for v in sibs)
        box = (
            '\n<!-- lib:crosslinks -->\n'
            '<section class="section bg-cream-tint"><div class="container" style="max-width:880px">'
            '<h2 class="title">Where to go from here</h2>'
            '<div class="btnrow" style="margin:16px 0 10px">'
            f'<a class="btn btn-primary" href="{prod[0]}">{prod[1]}</a>'
            + "".join(f'<a class="btn btn-secondary" href="{u}">{t}</a>' for u, t in svcs)
            + '<a class="btn btn-secondary" href="/schedule-now">Free consultation</a></div>'
            + (f'<ul class="nap-list">{sib_html}</ul>' if sib_html else "")
            + '</div></section>\n<!-- /lib:crosslinks -->\n')
        i = s.find('<section class="section closing-cta"')
        if i < 0:
            i = s.find('<footer class="footer"')
        if i < 0:
            continue
        for v in sibs:
            inlinks[v] += 1
        open(f, "w").write(s[:i] + box + s[i:])
        n += 1
    print(f"crosslinks: {n} posts boxed; min post inlinks now {min(inlinks.values())}")


if __name__ == "__main__":
    main()
