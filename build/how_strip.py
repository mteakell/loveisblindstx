"""The four-step process section that replaced the guarantee band (Nov 2026).

Every claim here is a company claim the site already makes: free in-home
consultation with samples, every opening measured on site, one written quote
with installation included, the same team measures and installs.
Used by extra.team() and by no_guarantees.py for pages built by enrich/home.
"""
import html

STEPS = [
    ("Free in-home consultation",
     "We bring samples to your home so you can hold them against your own windows and light."),
    ("Measured on site",
     "Every opening is measured in person before anything is ordered."),
    ("One written quote",
     "Products and installation are priced together on one written quote."),
    ("Installed by the same team",
     "The people who measured your windows come back to install them."),
]


def section(title="How a project works", link=True):
    e = lambda s: html.escape(s, quote=True)
    cards = "".join(
        f'<div class="type-card how-step"><div class="pbody"><span class="how-n">0{i + 1}</span>'
        f'<h3>{e(h)}</h3><p>{e(p)}</p></div></div>' for i, (h, p) in enumerate(STEPS))
    more = ('<p class="how-more"><a href="/how-it-works">See the full process</a></p>'
            if link else "")
    return (f'<section class="section how-band"><div class="container center">'
            f'<h2 class="title">{e(title)}</h2></div>'
            f'<div class="container"><div class="prod-grid how-grid">{cards}</div>{more}</div></section>')
