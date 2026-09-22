"""Dustin's approved Option 2 homepage hero, plus the /hero-options proof page.

From the LIB-TX-Maddie-Handoff package (Sep 2026): the full-bleed dark hero
zoomed so far in on mobile that the room and treatments disappeared, and
mobile is the majority of clicks. Approved replacement: landscape photo with
an overlapping cream card, the existing consultation form beside it in solid
site navy, and the landscape shutter photo in the neighbors section.

The hero rebuilds from constants on every run (the production form is
extracted from whichever hero markup is present and re-seated verbatim), so
changing HERO here is a one-line edit. /hero-options renders every
shortlisted photo in the real hero layout, noindexed, so Dustin can compare
on his phone at a link on the real domain.
"""
import html, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import extra as X, schema as S
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
e = lambda s: html.escape(s or "", quote=True)

# Approved default. Dustin's five shortlisted alternatives are on
# /hero-options; if he picks one, swap the stem and alt here.
HERO = ("roller-shades-home-hero-shades-1-jpeg",
        "Light-filtering roller shades around a furnished bedroom sitting area")

CANDIDATES = [
 ("Approved default", "Rollers, bedroom sitting area", *HERO),
 ("Previous set, first preference", "Rollers, open kitchen",
  "roller-shades-roller-shades-love-31-jpg",
  "Roller shades across an open Texas kitchen"),
 ("Previous set, second preference", "Shutters, fireplace",
  "shutters-shutters-love-02-jpg",
  "Plantation shutters beside a fireplace in a Texas living room"),
 ("Previous set, third preference", "Romans, sitting room",
  "roman-shades-roman-shades-036-jpg",
  "Roman shades in a Texas sitting room"),
 ("Set 2, option 4 (liked)", "Rollers, sunny dining",
  "roller-shades-roller-shades-love-28-jpg",
  "Roller shades in a sunny Texas dining room"),
 ("Set 2, option 5 (liked)", "Shutters, open kitchen",
  "shutters-shutters-160-jpg",
  "Plantation shutters in an open Texas kitchen"),
]

SHUTTER = ("shutters-shutters-love-14-jpg",
           "White plantation shutters above a gray sectional in a bright living room")


def _src(stem):
    return f"/images/lib/{stem}.webp"


def _img(stem, alt):
    v = f"/images/lib/r/{{w}}/{stem}.webp"
    srcset = ", ".join(f"{v.format(w=w)} {w}w" for w in (400, 800, 1600))
    return (f'<img src="{_src(stem)}" data-alt-final alt="{e(alt)}" '
            f'width="2000" height="1500" fetchpriority="high" '
            f'srcset="{srcset}, {_src(stem)} 2000w" '
            f'sizes="(max-width: 880px) 100vw, 55vw">')


def story(stem, alt):
    return (f'<div class="o2-story"><div class="o2-photo">{_img(stem, alt)}'
            '<span class="o2-badge">Beautiful light. Your way.</span></div>'
            '<div class="o2-card">'
            '<div class="o2-eyebrow">Custom window treatments &middot; Texas</div>'
            '<h1>A little change.<br>A whole new feeling.</h1>'
            '<p>Blinds, shades, and shutters chosen in your home, with your light '
            'and your style in mind.</p>'
            '<a class="o2-cta" href="#consultation">Book My Free Consultation '
            '<span aria-hidden="true">&rarr;</span></a>'
            '<div class="o2-fine">Free in-home visit. No pressure, ever.</div></div>'
            '<div class="o2-proof"><span aria-label="5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span> '
            'Loved by Texas homeowners</div></div>')


def hero_section(form_html):
    return ('<section class="option-two-hero" aria-label="Custom window treatments in Texas">'
            f'<div class="container option-two-grid">{story(*HERO)}'
            f'<div id="consultation">{form_html}</div></div></section>')


def apply_home():
    s = open("index.html").read()
    m = (re.search(r'<section class="option-two-hero".*?</section>', s, re.S)
         or re.search(r'<section class="phero has-form">.*?</section>', s, re.S))
    if not m:
        print("home hero: no hero section found"); return
    form = re.search(r'<form class="form-card".*?</form>', m.group(0), re.S)
    if not form:
        print("home hero: production form not found, aborting"); return
    s = s[:m.start()] + hero_section(form.group(0)) + s[m.end():]
    # approved landscape shutter photo in the neighbors section
    s = re.sub(
        r'<img class="owner-photo[^"]*"[^>]*>',
        f'<img class="owner-photo approved-shutter-photo" src="{_src(SHUTTER[0])}" '
        f'data-alt-final alt="{e(SHUTTER[1])}" loading="lazy" width="2000" height="1500">',
        s, count=1)
    open("index.html", "w").write(s)
    print(f"home hero: option-two applied ({HERO[0]}), shutter photo swapped")


def options_page():
    url = "/hero-options"
    title = "Homepage Hero Options"
    desc = "Side-by-side review of the shortlisted homepage hero photos in the approved layout."
    blocks = ""
    for label, room, stem, alt in CANDIDATES:
        blocks += (f'<div class="ho-item"><div class="ho-label"><strong>{e(label)}</strong>'
                   f'<span>{e(room)} &middot; {e(stem)}</span></div>'
                   f'<section class="option-two-hero"><div class="container option-two-grid ho-solo">'
                   f'{story(stem, alt)}</div></section></div>')
    body = ('<section class="section"><div class="container" style="max-width:1000px">'
            '<h1 class="title">Homepage hero options</h1>'
            '<p class="lead">Each photo below is shown in the real approved hero layout, '
            'exactly as it would render on the homepage. Best reviewed on a phone as well '
            'as desktop. The consultation form sits beside the card on the live page.</p>'
            '<p class="sml">This page is for review only. It is not linked from the site '
            'and does not appear in search.</p></div>'
            f'<div class="container" style="max-width:1000px">{blocks}</div></section>')
    nodes = X.BASE() + [S.webpage(url, title, desc)]
    out = X.shell(url, title, desc, nodes, body)
    out = out.replace('<meta charset="UTF-8">',
                      '<meta charset="UTF-8">\n<meta name="robots" content="noindex,nofollow">')
    open("hero-options.html", "w").write(out)
    print(f"hero-options: {len(CANDIDATES)} candidates rendered")


if __name__ == "__main__":
    apply_home()
    options_page()
