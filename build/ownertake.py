"""Owner's Take: first-person opinion posts under a real owner's byline.

A distinct blog type built to be cited by AI search: question-form title,
a direct quotable answer up top, the owner's verbatim words as a pull
quote, Person author schema pointing at the bio page, and Q&A subheads.
The owner's opinion is ONLY what the owner actually said; everything else
is product fact already published on this site, framed as guidance.

First post: Durrell Glick (DFW) on plantation shutters, 2026-09-05.
"""
import html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import schema as S

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BIZ = json.load(open("data/tx.json"))["business"]
HEAD_INNER = open("build/partials/header.html").read().split("<body", 1)[1].split(">", 1)[1]
FOOT = open("build/partials/footer.html").read()
e = lambda s: html.escape(s or "", quote=True)

SLUG = "are-plantation-shutters-worth-it"
TITLE = "Are Plantation Shutters Worth It? A DFW Owner's Honest Take"
DESC = ("Durrell Glick, owner of Love Is Blinds DFW, on why plantation shutters are his "
        "favorite window treatment: timeless style, real curb appeal, and when he would "
        "point you to something else.")
PUBLISHED = "2026-09-05"
HERO = "/images/lib/shutters-shutters-151-jpg.webp"

QUOTE = ("I think plantation shutters are my favorite. They are timeless, classy and "
         "never go out of style. I love when people do them on the front of the house "
         "because of the curb appeal shutters provide.")


def img(name, alt):
    return (f'<img src="/images/lib/{name}-jpg.webp" data-alt-final alt="{e(alt)}" '
            f'loading="lazy" width="2000" height="1500">')


def main():
    url = "/" + SLUG
    faqs = [
        ("Are plantation shutters worth the money?",
         "For the rooms people see, yes. Shutters are custom-built to the window frame and "
         "finished like furniture, so they read as an upgrade to the house itself rather "
         "than a covering on it. They add curb appeal from the street, and our warranty "
         "transfers if you sell the home."),
        ("Do plantation shutters go out of style?",
         "No. Wide-louver shutters in a neutral finish have looked right in Texas homes for "
         "decades and are not tied to a trend cycle the way fabrics and colors can be. That "
         "is a large part of why homeowners choose them for the front of the house."),
        ("Should I put plantation shutters on the front of the house?",
         "It is one of the most popular ways to use them. From the street, every front "
         "window shows the same clean lines and consistent louvers, which is the curb "
         "appeal shutters are known for."),
        ("Real wood or faux wood shutters?",
         "Both are custom-built to your openings. Faux wood shrugs off the moisture in "
         "kitchens and baths; real wood keeps its lines on big living-area windows. The "
         "free in-home consultation is where you compare them at your own windows."),
    ]
    faqhtml = "".join(
        f"<details><summary>{e(q)}</summary><div class='a'>{e(a)}</div></details>"
        for q, a in faqs)

    _idx = {p["url"]: p.get("img") for p in json.load(open("data/blog-index.json"))}
    related = [
        ("Plantation Shutters vs Blinds: Which Is the Better Investment?",
         "/plantation-shutters-vs-blinds-which-is-the-better-investment-for-your-dfw-home"),
        ("How Much Do Plantation Shutters Cost in Texas?",
         "/how-much-do-plantation-shutters-cost-in-texas"),
        ("Real Wood vs Faux Wood Shutters", "/real-wood-vs-faux-wood-shutters"),
    ]
    rel = "".join(
        (lambda t, u: f'<a class="prod-card rel-card" href="{u}">'
         + (f'<span class="pic"><img src="{_idx[u]}" alt="" loading="lazy" width="600" height="400"></span>' if _idx.get(u) else "")
         + f'<div class="pbody"><h3>{e(t)}</h3>'
           f'<span class="btn-link">Read <span class="arw">&rarr;</span></span></div></a>')(t, u)
        for t, u in related)

    post_node = S.blogposting(url, TITLE, DESC, PUBLISHED, image=HERO)
    post_node["author"] = S.person("Durrell Glick", "Owner, Love Is Blinds DFW",
                                   "/meet-the-team/durrell", "/images/team/durrell.jpg")
    nodes = [S.organization(BIZ), S.website(BIZ), S.business(BIZ),
             S.webpage(url, TITLE, DESC, about=S.ORGID, primary=HERO),
             post_node,
             S.breadcrumbs([("Home", "/"), ("Blog", "/blog"), (TITLE[:60], url)]),
             S.faq(url, faqs)]

    byline = (
        '<div class="ot-byline">'
        '<img src="/images/team/durrell.jpg" alt="Durrell Glick, owner of Love Is Blinds DFW" '
        'width="600" height="667" loading="lazy">'
        '<div><b><a href="/meet-the-team/durrell">Durrell Glick</a></b>'
        '<span>Owner, Love Is Blinds DFW &middot; quotes, measures and installs across '
        'Fort Worth, Denton and the Mid-Cities</span></div></div>')

    body = f'''
<p class="ot-answer"><b>The short answer:</b> if you want a window treatment for the rooms
people see, and for the front of the house, plantation shutters are the one I recommend
first. They are built to the window, finished like furniture, and they do not chase a
trend. Here is my honest take, and where I would steer you to something else.</p>

{img("shutters-shutters-151", "Plantation shutters across a bright Texas living room, installed by Love Is Blinds")}

<blockquote class="ot-quote"><p>&ldquo;{e(QUOTE)}&rdquo;</p>
<footer>&mdash; Durrell Glick, Owner, Love Is Blinds DFW</footer></blockquote>

<h2>Why plantation shutters are my favorite</h2>
<p>Most window treatments are something you put on a window. Plantation shutters become
part of the window. They are custom-built to your exact frames, set in their own frame,
and finished like furniture, which is why a room with shutters reads as a nicer room
before you can even say what changed. Timeless and classy is exactly the right way to
put it: a wide-louver shutter in a clean finish looked right thirty years ago and it
will look right thirty years from now.</p>

{img("shutters-shutters-101", "Wide-louver plantation shutters framing a Texas dining space")}

<h2>The curb appeal case for the front of the house</h2>
<p>This is the part I love. Fabrics and blinds look different from the street on every
window: one raised, one lowered, one a slightly different color. Shutters give the front
of the house the same clean, consistent lines on every window, every day. From the curb
the whole facade looks composed, which is why shutters are the treatment realtors point
at when they talk about window coverings adding home value.</p>

{img("shutters-shutters-113", "Front-room plantation shutters showing clean consistent louvers")}
{img("shutters-shutters-060", "Plantation shutters on tall windows in a Texas family room")}

<h2>Do they go out of style?</h2>
<p>No, and that is the whole argument. Colors cycle, fabric trends cycle, hardware
finishes cycle. Wide-louver shutters in white or a neutral stain sit outside that cycle.
When you are spending real money on the front rooms of your home, buying something that
will not date itself is the safest design decision you can make.</p>

{img("shutters-shutters-077", "Classic white plantation shutters in a Texas bedroom")}

<h2>Where I would point you to something else</h2>
<p>An honest answer includes this part. A bedroom that needs to be truly dark wants a
room-darkening or blackout shade, either instead of shutters or layered behind them,
because louvers alone let a line of light through. And in a room where the budget has to
work harder, faux wood blinds are the workhorse: durable, easy to clean, and a fraction
of the spend. For steamy bathrooms we build faux wood shutters rather than real wood, so
you do not have to give up the look to get the durability.</p>

{img("shutters-shutters-028", "Plantation shutters beside a freestanding tub in a Texas bathroom")}

<h2>What we actually build</h2>
<p>Real wood and faux wood plantation shutters, custom-measured to your openings by the
person who quotes them, including the shapes most companies pass on: arches, bays,
sliders and tall windows. Options like invisible tilt keep the face of the shutter
completely clean. Every job carries our guarantees, including a warranty that transfers
with the house.</p>

{img("shutters-shutters-123", "Plantation shutters fitted to a wide Texas window wall")}
{img("shutters-shutters-091", "Detail of custom plantation shutter louvers and frame")}

<p>If you are weighing shutters for your own front rooms, the free in-home consultation
is the honest way to decide: we bring samples, measure your actual windows, and you see
the louver sizes in your own light. If shutters are not the right call for a room, I
will tell you that too.</p>'''

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(TITLE[:57])} | Love Is Blinds</title>
<meta name="description" content="{e(DESC[:155])}">
<link rel="canonical" href="{S.SITE}{url}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#3A4D5C">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{e(BIZ['name'])}">
<meta property="og:title" content="{e(TITLE)}">
<meta property="og:description" content="{e(DESC[:155])}">
<meta property="og:url" content="{S.SITE}{url}">
<meta property="og:image" content="{S.SITE}{HERO}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(TITLE)}">
<meta name="twitter:description" content="{e(DESC[:155])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css">
{S.render(nodes)}
</head>
<body>
{HEAD_INNER}
<main>
<article class="section">
  <div class="container">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">&rsaquo;</span>
      <a href="/blog">Blog</a><span class="sep">&rsaquo;</span>{e(TITLE[:70])}</nav>
    <p class="ot-eyebrow">An Owner&rsquo;s Take</p>
    <h1 class="title">{e(TITLE)}</h1>
    {byline}
    <div class="post-body">
{body}
      <h2>Common questions</h2>
    </div>
    <div class="faq">{faqhtml}</div>
    <div class="rel-block">
      <h2>Related reading</h2>
      <div class="prod-grid rel-grid">{rel}</div>
    </div>
    <div class="btnrow post-cta">
      <a class="btn btn-primary btn-lg" href="/schedule-now">Book a free in-home measure</a>
      <a class="btn btn-secondary btn-lg" href="tel:{BIZ["tel"]}">Call {e(BIZ["phone"])}</a>
    </div>
  </div>
</article>
</main>
{FOOT}'''
    open(SLUG + ".html", "w").write(page)

    idx = json.load(open("data/blog-index.json"))
    if not any(p["url"] == url for p in idx):
        idx.append({"url": url, "title": TITLE, "desc": DESC, "date": PUBLISHED, "img": HERO})
        json.dump(idx, open("data/blog-index.json", "w"), indent=1)
    print(f"{SLUG}.html written; index has {len(idx)} posts")


if __name__ == "__main__":
    main()
