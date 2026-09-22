"""/reviews: the destination page for "best company" and "reviews" intent.

361 real Google reviews sat in data with no page for queries like
"love is blinds reviews" or "best blinds company dfw" to land on. Every
number here is computed from data at build time so the page cannot drift
from the badge. No aggregateRating markup: self-serving review schema on
the business is against Google's guidelines, so proof stays visible and
the schema stays WebPage + breadcrumbs.
"""
import collections, html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import schema as S
import territory as T
import extra as X

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
e = lambda s: html.escape(s or "", quote=True)

RATINGS = json.load(open("data/gbp-ratings.json"))["profiles"]
TOTAL = sum(p["reviews"] for p in RATINGS)
LOCS = len(RATINGS)
AVG = round(sum(p["rating"] * p["reviews"] for p in RATINGS if p["rating"]) /
            max(1, sum(p["reviews"] for p in RATINGS if p["rating"])), 1)
REVIEWS = [r for r in json.load(open("data/reviews.json")) if r.get("rating", 5) >= 4]
CITIES = {c["slug"]: c for c in json.load(open("data/tx.json"))["cities"]}

URL = "/reviews"
TITLE = f"Love Is Blinds Reviews | {AVG} Stars Across Texas"
DESC = (f"{TOTAL} Google reviews across {LOCS} Texas locations, {AVG} stars. Read what "
        "homeowners in DFW, North Texas, Dallas, Waco, Austin and Cedar Creek Lake say "
        "about Love Is Blinds.")
ORDER = ["dfw", "north", "dallas", "cedarcreek", "waco", "austin", "tyler"]


def main():
    by_terr = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in REVIEWS:
        slug = r.get("slug")
        if not slug or slug not in CITIES:
            continue
        by_terr[T.of(slug)["key"]][slug].append(r)

    chips, sections = "", ""
    for key in ORDER:
        cities = by_terr.get(key)
        if not cities:
            continue
        terr = T.TERRITORIES[key]
        n = sum(len(v) for v in cities.values())
        chips += (f'<a class="chip" href="#rv-{key}">{e(terr["brand"])} '
                  f'<span class="sml">{n}</span></a>')
        blocks = ""
        for slug in sorted(cities, key=lambda s2: -len(cities[s2])):
            c = CITIES[slug]
            revs = sorted(cities[slug], key=lambda r: r.get("date", ""), reverse=True)
            cards = "".join(
                '<div class="review"><div class="stars">'
                + "&#9733;" * int(r.get("rating", 5)) + "</div>"
                + f'<p>"{e(r["quote"])}"</p><div class="who">{e(r["name"])}</div>'
                + f'<div class="where">{e(r.get("city", c["label"]))}, TX</div></div>'
                for r in revs)
            gbp = (f' <a class="btn-link" href="{e(c["gbp"][0])}" rel="noopener">Read on '
                   f'Google <span class="arw">&rarr;</span></a>' if c.get("gbp") else "")
            blocks += (f'<h3 class="rvh-city">{e(c["label"])}, TX '
                       f'<span class="sml">{len(revs)} reviews</span>{gbp}</h3>'
                       f'<div class="reviews">{cards}</div>')
        sections += (f'<section class="section{" bg-cream-tint" if ORDER.index(key) % 2 else ""}" '
                     f'id="rv-{key}"><div class="container">'
                     f'<h2 class="title">{e(terr["brand"])}</h2>{blocks}</div></section>')

    nodes = X.BASE() + [S.webpage(URL, TITLE, DESC),
                        S.breadcrumbs([("Home", "/"), ("Reviews", URL)])]
    body = f'''<section class="phero"><picture><img src="/images/lib/shutters-shutters-love-15-jpg.webp"
  data-alt-final alt="Plantation shutters on tall dining room windows in a Texas family home, installed by Love Is Blinds"
  width="2000" height="1500" fetchpriority="high"></picture>
  <div class="container"><div class="phero-copy">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span class="sep">&rsaquo;</span>Reviews</nav>
    <h1 class="title">{TOTAL} Google Reviews. {AVG} Stars. Every One Real.</h1>
    <p class="lead">Every review below was left on one of our {LOCS} Google Business Profiles by a
      Texas homeowner we worked for, shown with the city it came from and a link to read it at the
      source. No cherry-picked testimonials page: this is the whole record.</p>
    <div class="hero-actions btnrow">
      <a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a>
      <a class="btn btn-secondary btn-lg" href="tel:+18665182999">Call (866) 518-2999</a>
    </div>
  </div></div>
</section>
<section class="section faq-nav"><div class="container center">
  <div class="faq-chips">{chips}</div></div></section>
{sections}
<section class="section closing-cta"><div class="container center">
  <h2 class="title">Ready to be the next review?</h2>
  <p class="lead">Free in-home consultation anywhere we serve. The person who quotes your
    window treatments is the person who installs them.</p>
  <div class="btnrow" style="justify-content:center">
    <a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a>
    <a class="btn btn-secondary btn-lg" href="tel:+18665182999">Call (866) 518-2999</a>
  </div>
</div></section>'''
    open("reviews.html", "w").write(X.shell(URL, TITLE, DESC, nodes, body,
        img="/images/lib/shutters-shutters-love-15-jpg.webp"))
    print(f"reviews.html: {TOTAL} badge reviews, {sum(len(v) for t in by_terr.values() for v in t.values())} quotes on page, avg {AVG}")


if __name__ == "__main__":
    main()
