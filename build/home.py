"""Home page treatment.

index.html comes through convert.py from the old Duda markup and was never
touched by the rebuild, so it ended up the thinnest important page on the
site: 1,192 words against a 1,625-word median on the city pages, no
guarantees, no parallax, and no exterior patio shades anywhere in the product
grid. Patio shades is the one term Love Is Blinds can actually win, so leaving
it off the home page was the worst single omission on the site.

Runs after convert.py. Idempotent: every block is removed by marker before it
is re-inserted, so a rebuild does not stack them.
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
G = json.load(open("data/guarantees.json"))["guarantees"]

PATIO_CARD = (
 '<a class="prod-card reveal" href="/products/exterior-patio-shades"> '
 '<span class="pic"><picture>'
 '<img src="/images/lib/exterior-patio-shades-exterior-patio-shades-001-jpg.webp" '
 'alt="Exterior patio shades on a covered Texas porch" loading="lazy" width="2000" height="1500">'
 '</picture></span> <span class="pbody"> '
 '<span class="kicker">Outdoor &amp; Motorized</span> '
 '<h3>Exterior Patio Shades</h3> '
 '<p>Shade that stops the sun on the outside of the glass, so a covered patio '
 'stays usable through a Texas afternoon.</p> '
 '<span class="btn-link">Explore <span class="arw">&#8594;</span></span> '
 '</span> </a>')

GUARANTEES = (
 '\n<!-- lib:guarantees -->\n'
 '<section class="section bg-cream-tint">'
 '<div class="container center"><h2 class="title">Every job is backed five ways</h2>'
 '<p class="lead">The same cover on a single window as on a whole house.</p></div>'
 '<div class="container"><div class="guarantees">' +
 "".join(f'<div class="gtee"><h3>{g["name"]}</h3><p>{g["text"]}</p></div>' for g in G) +
 '</div></div></section>\n<!-- /lib:guarantees -->\n')

BAND = (
 '\n<!-- lib:band -->\n'
 '<section class="parallax-band" '
 'style="background-image:url(\'/images/lib/exterior-patio-shades-exterior-patio-shades-002-jpg.webp\')">'
 '<div class="container">'
 '<p class="pb-eyebrow">Exterior patio shades</p>'
 '<h2 class="pb-title">Stop the sun before it reaches the glass</h2>'
 '<p class="pb-body">An interior blind manages sun that is already in the room. An exterior shade '
 'stops it at the outside face of the glass, which is why the same fabric performs differently '
 'depending on which side it hangs. On a covered patio it is the difference between a space you use '
 'in July and one you look at.</p>'
 '<div class="btnrow"><a class="btn btn-primary btn-lg" href="/products/exterior-patio-shades">'
 'See exterior patio shades</a></div>'
 '</div></section>\n<!-- /lib:band -->\n')


def strip(html, marker):
    return re.sub(rf'\n?<!-- lib:{marker} -->.*?<!-- /lib:{marker} -->\n?', '', html, flags=re.S)


def main():
    h = open("index.html").read()
    h = strip(strip(h, "guarantees"), "band")
    added = []

    # 1. patio shades into the product grid, first, ahead of the interior lines
    if "/products/exterior-patio-shades" not in h.split("Explore our custom")[1][:3000]:
        i = h.find("Explore our custom window treatments")
        m = re.search(r'<div class="prod-grid[^"]*">', h[i:])
        if m:
            at = i + m.end()
            h = h[:at] + PATIO_CARD + h[at:]
            added.append("patio card")

    # 2. guarantees, before the closing call to action
    m = re.search(r'<section[^>]*>(?=(?:(?!</section>).)*Ready for blinds)', h, re.S)
    if m:
        h = h[:m.start()] + GUARANTEES + h[m.start():]
        added.append("guarantees")

    # 3. parallax band, after the process section
    i = h.find("Getting custom window treatments is easy")
    if i > 0:
        j = h.find("</section>", i)
        if j > 0:
            j += len("</section>")
            h = h[:j] + BAND + h[j:]
            added.append("patio band")

    open("index.html", "w").write(h)
    t = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ',
        re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', h, flags=re.S)))
    print(f"home: added {', '.join(added) or 'nothing'} -> {len(t.split())} words, "
          f"{len(re.findall('<h2', h))} H2, patio mentions {h.lower().count('patio shade')}")


if __name__ == "__main__":
    main()
