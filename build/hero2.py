"""Dustin's approved Option 2 homepage hero, plus the /hero-options proof page.

From the LIB-TX-Maddie-Handoff package (Sep 2026): the full-bleed dark hero
zoomed so far in on mobile that the room and treatments disappeared, and
mobile is the majority of clicks. Approved replacement: landscape photo with
an overlapping cream card, the existing consultation form beside it in solid
site navy, and the landscape shutter photo in the neighbors section.

Decision so far: desktop keeps the original full-bleed hero; only the
MOBILE layout changes, to a white overlapping card (tan rejected), applied
by CSS scoped to the phero-mob-card class this pass stamps on the homepage
hero. /hero-options renders every shortlisted photo in the card layout,
noindexed, so Dustin can compare on his phone at a link on the real domain.
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


def tag_home_hero():
    """Mobile-only card layout hook plus the photo carousel. Desktop shows
    only the first (approved) photo exactly as before; at phone widths the
    hero crossfades through every shortlisted candidate."""
    t = open("index.html").read()
    if "phero-mob-card" not in t:
        t = t.replace('<section class="phero has-form">',
                      '<section class="phero has-form phero-mob-card">', 1)
    hero = re.search(r'<section class="phero has-form phero-mob-card">.*?</section>', t, re.S)
    if not hero:
        print("home hero: hero section not found"); return
    h = hero.group(0)
    if 'class="hero-slides"' not in h:
        pic = re.search(r'<picture>(\s*<img[^>]*>)\s*</picture>', h)
        if not pic:
            print("home hero: picture not found"); return
        main_img = re.sub(r'<img ', '<img class="hs-slide on" ', pic.group(1).strip(), count=1)
        extras = ""
        for label, room, stem, alt in CANDIDATES[1:]:
            extras += (f'<img class="hs-slide" src="/images/lib/r/800/{stem}.webp" '
                       f'data-alt-final alt="{e(alt)}" loading="lazy" '
                       f'width="800" height="600">')
        slides = f'<div class="hero-slides">{main_img}{extras}</div>'
        js = ('<script>(function(){if(!matchMedia("(max-width:880px)").matches)return;'
              'var s=document.querySelectorAll(".hero-slides .hs-slide");if(s.length<2)return;'
              'var i=0;setInterval(function(){s[i].classList.remove("on");'
              'i=(i+1)%s.length;s[i].classList.add("on");},4000);})();</script>')
        h2 = h.replace(pic.group(0), slides) + js
        t = t.replace(h, h2, 1)
    open("index.html", "w").write(t)
    print("home hero: mobile carousel in place")


def options_page():
    """/hero-options: every candidate photo inside the REAL homepage mobile
    hero, rendered in true 390px iframes so the mobile media queries fire
    and what Dustin sees is exactly what a phone renders. Each iframe loads
    a minimal /hero-mob/<stem> page holding the live hero markup with the
    photo swapped in."""
    src = open("index.html").read()
    hero = re.search(r'<section class="phero has-form phero-mob-card">.*?</section>', src, re.S)
    if not hero:
        print("hero-options: homepage hero not found"); return
    hero = hero.group(0)

    frames = ""
    for label, room, stem, alt in CANDIDATES:
        page = hero
        page = re.sub(r'<img [^>]*fetchpriority="high"[^>]*>', _img(stem, alt), page, count=1)
        mini = ('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
                '<meta name="robots" content="noindex,nofollow">'
                '<meta name="viewport" content="width=device-width, initial-scale=1">'
                f'<title>Hero preview: {e(stem)}</title>'
                '<link rel="stylesheet" href="/css/styles.css">'
                '</head><body style="margin:0;background:#fff">'
                f'<main>{page}</main></body></html>')
        open(f"hero-mob/{stem}.html", "w").write(mini)
        # phones cannot render fixed-width iframes reliably (iOS expands
        # them), but a phone IS the mobile viewport: render the hero inline
        # there and it lays out natively. Desktop gets the 390px iframe rig.
        # The form stays visible in every preview; ids are stripped so six
        # copies stay valid HTML, and the subject marks any submission as a
        # test from this page rather than a real lead.
        inline = re.sub(r'\s(?:id|for)="[^"]*"', "", page)
        inline = inline.replace('value="New consultation request - home"',
                                'value="Test submission - hero options page"')
        frames += (f'<div class="ho-item"><div class="ho-label"><strong>{e(label)}</strong>'
                   f'<span>{e(room)}</span></div>'
                   f'<div class="ho-phone"><iframe src="/hero-mob/{stem}" title="{e(label)}" '
                   f'loading="lazy" width="390" height="740"></iframe></div>'
                   f'<div class="ho-inline">{inline}</div></div>')

    url = "/hero-options"
    title = "Homepage Hero Options"
    desc = "Each shortlisted photo shown in the real mobile homepage hero."
    body = ('<section class="section"><div class="container" style="max-width:1000px">'
            '<h1 class="title">Homepage hero: photo options on mobile</h1>'
            '<p class="lead">Each frame below is the real homepage mobile hero, rendered at '
            'phone width, with one of the shortlisted photos. Scroll inside a frame to see '
            'the card and the form, exactly as a phone shows them.</p>'
            '<p class="sml">For review only. Not linked from the site, not in search. '
            'Full-frame versions of every photo are on the '
            '<a href="/photo-review">photo review page</a>.</p>'
            '<div class="ho-grid">' + frames + '</div></div></section>')
    nodes = X.BASE() + [S.webpage(url, title, desc)]
    out = X.shell(url, title, desc, nodes, body)
    out = out.replace('<meta charset="UTF-8">',
                      '<meta charset="UTF-8">\n<meta name="robots" content="noindex,nofollow">')
    open("hero-options.html", "w").write(out)
    print(f"hero-options: {len(CANDIDATES)} phone-frame previews rendered")


PHOTOS = [
 ("SMA Home Hero Shades 1.jpeg", "Approved hero photo (current default)",
  "roller-shades-home-hero-shades-1-jpeg",
  "Light-filtering roller shades around a furnished bedroom sitting area"),
 ("SMA shutters-love-14.jpg", "Approved for the neighbors section",
  "shutters-shutters-love-14-jpg",
  "White plantation shutters above a gray sectional in a bright living room"),
 ("SMA roller-shades-love-31.jpg", "Hero alternative, previous set first preference",
  "roller-shades-roller-shades-love-31-jpg",
  "Roller shades across an open Texas kitchen"),
 ("SMA shutters-love-02.jpg", "Hero alternative, previous set second preference",
  "shutters-shutters-love-02-jpg",
  "Plantation shutters beside a fireplace in a Texas living room"),
 ("SMA roman-shades-036.jpg", "Hero alternative, previous set third preference",
  "roman-shades-roman-shades-036-jpg",
  "Roman shades in a Texas sitting room"),
 ("SMA roller-shades-love-28.jpg", "Hero alternative, set 2 option 4 (liked)",
  "roller-shades-roller-shades-love-28-jpg",
  "Roller shades in a sunny Texas dining room"),
 ("SMA shutters-160.jpg", "Hero alternative, set 2 option 5 (liked)",
  "shutters-shutters-160-jpg",
  "Plantation shutters in an open Texas kitchen"),
]


def photo_review():
    """Plain full-size gallery of every photo in the handoff package,
    labeled with original filenames, for client review. Noindexed."""
    url = "/photo-review"
    title = "Photo Review"
    desc = "Full-size review of the homepage photo package."
    blocks = ""
    for orig, role, stem, alt in PHOTOS:
        blocks += (f'<figure class="pr-item"><figcaption class="ho-label">'
                   f'<strong>{e(role)}</strong><span>{e(orig)}</span></figcaption>'
                   f'<img src="{_src(stem)}" data-alt-final alt="{e(alt)}" loading="lazy" '
                   f'width="2000" height="1500" style="width:100%;height:auto;border-radius:12px"></figure>')
    body = ('<section class="section"><div class="container" style="max-width:1000px">'
            '<h1 class="title">Photo review</h1>'
            '<p class="lead">All seven photos from the homepage package at full frame: the two '
            'approved placements and the five hero alternatives. To see any alternative in the '
            'hero layout itself, use the <a href="/hero-options">hero options page</a>.</p>'
            '<p class="sml">This page is for review only. It is not linked from the site '
            'and does not appear in search.</p>'
            f'{blocks}</div></section>')
    nodes = X.BASE() + [S.webpage(url, title, desc)]
    out = X.shell(url, title, desc, nodes, body)
    out = out.replace('<meta charset="UTF-8">',
                      '<meta charset="UTF-8">\n<meta name="robots" content="noindex,nofollow">')
    open("photo-review.html", "w").write(out)
    print(f"photo-review: {len(PHOTOS)} photos rendered")


if __name__ == "__main__":
    tag_home_hero()
    options_page()
    photo_review()
