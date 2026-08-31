# Product x City pages

**6 products x 48 cities = 288 pages.**

Built for every city at Maddie's direction, including cities with no measured search
volume, so anyone in the service area lands on something specific to their city and
product rather than a generic page.

## What keeps these from being thin permutations

| Element | How it differs per page |
|---|---|
| Operator | Named, and linked to their own profile |
| Phone | That city's local tracking number, not the 866 |
| Nearby cities | Computed by real distance from that city's coordinates |
| Reviews | That city's own Google reviews where we have them |
| Address | Shown where that location has a real one |
| Product scope | The six families do not overlap in what they cover |
| FAQs | City name and operator in the answers, plus product specific questions |

## Products

| Product | URL pattern | Scope |
|---|---|---|
| Custom Blinds | `/blinds-{city}-tx` | Real wood, faux wood, composite, vertical, mini, cordless and motorized lift |
| Custom Shades | `/shades-{city}-tx` | Roller, solar screen, cellular, Roman, woven wood, dual and day-night |
| Plantation Shutters | `/plantation-shutters-{city}-tx` | Louvered interior shutters: full height, divider rail, tier on tier, cafe, specialty shapes |
| Window Shutters | `/shutters-{city}-tx` | The whole shutter category: plantation, cafe, solid panel, sidelight, specialty, sliding |
| Exterior Patio Shades | `/patio-shades-{city}-tx` | Exterior: solar screen, motorized, retractable, track guided, porch, exterior solar |
| Motorized Shades | `/motorized-shades-{city}-tx` | Battery, hardwired, solar charged, app and voice, scheduling, wide and high openings |

## Where search volume is measured

27 of the 288 have confirmed demand. The rest are built for coverage.

| Product | Cities with volume | Total vol |
|---|---|---|
| Plantation shutters | 13 | 980/mo |
| Patio shades | 8 | 990/mo |
| Motorized shades | 6 | 800/mo |
| Blinds | 20 | 1,290/mo (city pages also target this) |
| Shades | 8 | 280/mo |
| Shutters | 9 | 230/mo |

## Cannibalisation rule

Because every city now has all six product pages, no city page leads with a product
term. `head_of()` in `build/pages.py` returns None for blinds, shades, shutters,
plantation shutters, patio shades and motorized, so `/dallas-tx` is the broad hub
("Blinds, Shades & Shutters in Dallas, TX") and `/blinds-dallas-tx` owns the specific
term. Without this the two compete and Google picks one at random, which is exactly
what let `/grapevine-tx-2` outrank the real `/grapevine-tx` on the Duda site.

## Regenerate

    python3 build/product_city.py

Product scope, copy and FAQs live in `build/products_spec.py`. Edit there, never the HTML.
