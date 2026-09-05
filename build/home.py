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
import html, json, os, re

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



# ---------------------------------------------------------------- reviews
REVIEWS = json.load(open("data/reviews.json"))


def _slider():
    """Every 4+ star review in a scroll-snap slider.

    The home page showed three static cards while 364 real reviews sat in the
    data. Scroll-snap plus two buttons rather than a carousel library: no
    dependency, works without JS (it stays a horizontal scroller), and keyboard
    and touch both work for free.
    """
    revs = sorted((r for r in REVIEWS if r.get("rating", 5) >= 4),
                  key=lambda r: r.get("date", ""), reverse=True)
    cards = "".join(
        '<article class="rv-card">'
        '<div class="rv-stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
        f'<p class="rv-quote">{html.escape(r["quote"])}</p>'
        f'<footer class="rv-by"><span class="rv-name">{html.escape(r["name"])}</span>'
        f'<span class="rv-city">{html.escape(r["city"])}, TX</span></footer>'
        '</article>' for r in revs)
    return (
      '\n<!-- lib:slider -->\n'
      '<section class="section bg-cream-tint rv-section">'
      '<div class="container center">'
      '<h2 class="title">What Texas homeowners say</h2>'
      f'<p class="lead">{len(revs)} reviews from customers across {len({r["slug"] for r in revs})} '
      'Texas cities, straight from our Google profiles.</p>'
      '</div>'
      '<div class="rv-wrap">'
      '<button class="rv-nav rv-prev" type="button" aria-label="Previous reviews">'
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
      'stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg></button>'
      f'<div class="rv-track" tabindex="0" role="region" aria-label="Customer reviews">{cards}</div>'
      '<button class="rv-nav rv-next" type="button" aria-label="More reviews">'
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
      'stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg></button>'
      '</div>'
      '<div class="container center" style="margin-top:26px">'
      '<a class="btn btn-secondary btn-lg" href="/areas-we-serve">Find your local team</a></div>'
      '<script>(function(){'
      'var w=document.querySelector(".rv-section");if(!w)return;'
      'var t=w.querySelector(".rv-track");'
      'var p=w.querySelector(".rv-prev"),n=w.querySelector(".rv-next");'
      'if(!t||!p||!n)return;'
      'function step(d){var c=t.querySelector(".rv-card");if(!c)return;'
      'var cw=c.getBoundingClientRect().width+18;'
      'var per=Math.max(1,Math.floor(t.clientWidth/cw));'
      'var from=t.scrollLeft,by=d*cw*per;'
      't.scrollBy({left:by,behavior:"smooth"});'
      'setTimeout(function(){if(Math.abs(t.scrollLeft-from)<2)t.scrollLeft=from+by;},260);}'
      'p.addEventListener("click",function(){step(-1)});'
      'n.addEventListener("click",function(){step(1)});'
      '})();</script>'
      '</section>\n<!-- /lib:slider -->\n')


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


    # .prod-grid is a hard 4 columns; with the patio card added there are 5,
    # so the fifth was orphaned on its own row.
    i = h.find("Explore our custom window treatments")
    if i > 0:
        m = re.search(r'<div class="prod-grid(?! )', h[i:])
        if m:
            at = i + m.start()
            h = h[:at] + '<div class="prod-grid prod-grid-5' + h[at + len('<div class="prod-grid'):]
            added.append("5-up grid")

    # Swap the three static testimonials for the full slider. This has to be
    # idempotent: the first run removes the original section, so on a rebuild
    # there is nothing left to match. Strip the slider, then insert it at the
    # original section if it is still there, otherwise at the marker we left.
    h = strip(h, "slider")
    m = re.search(r'<section[^>]*>(?:(?!</section>).)*Texas homeowners say it best.*?</section>',
                  h, re.S)
    if m:
        h = h[:m.start()] + "<!-- lib:reviews-anchor -->" + _slider() + h[m.end():]
        added.append("review slider")
    elif "<!-- lib:reviews-anchor -->" in h:
        h = h.replace("<!-- lib:reviews-anchor -->",
                      "<!-- lib:reviews-anchor -->" + _slider(), 1)
        added.append("review slider")


    # heading pass: the converted Duda headings were category labels, not
    # sentences anyone would say. Straight string swaps, safe to re-run.
    for a, b in [
        ("Explore our custom window treatments.",
         "Find the right treatment for every window."),
        ("Getting custom window treatments is easy.",
         "From free consultation to finished install."),
        ("Proudly serving Texas communities.",
         "Three local franchises, covering Texas from DFW to Austin."),
    ]:
        h = h.replace(a, b)

    open("index.html", "w").write(h)
    t = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ',
        re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', h, flags=re.S)))
    print(f"home: added {', '.join(added) or 'nothing'} -> {len(t.split())} words, "
          f"{len(re.findall('<h2', h))} H2, patio mentions {h.lower().count('patio shade')}")


if __name__ == "__main__":
    main()
