# Love Is Blinds Texas — loveisblindstx.com

Static rebuild of the Duda site. 194 pages, no build step at serve time: plain HTML,
one stylesheet, local images. Everything generated lives under `build/`.

## What changed from the old site

- **Off Duda.** No `cdn-website.com` dependency anywhere. All 642 blog images are local
  (753MB of unresized originals became 71MB at 1400px).
- **Schema, which the old site effectively did not have.** It shipped `WebSite`,
  `VideoObject` and a thin `Organization`. No LocalBusiness, no address, no geo, no
  breadcrumbs, no FAQ, on a 48-city local business. 117 city pages also carried literal
  `"null"` strings inside their JSON-LD.
- **Every meta description was boilerplate** ("the LEADING window treatment Expert of 2026
  in {City}") and all 48 ran past 155 characters, so they truncated in results. All unique
  and in range now.
- **57 tourism pages cut.** `/our-community/*` and `/local-attractions/*` were ~24% of
  organic traffic at ~0% commercial intent, all at $0.00 CPC. 301'd to the matching city page.
- **Duplicate city pages consolidated.** `/fort-worth-tx-2` and `/grapevine-tx-2` were
  service-area duplicates with no Google profile, and they were outranking the real pages.
  Both 301 into the profile-forward page. Corsicana stays split, since that pair is two
  genuine locations.

## Build

    python3 build/pages.py      # 48 city pages
    python3 build/convert.py    # core, product and service pages
    python3 build/extra.py      # areas-we-serve, team, design-checklist, blog index, vodyssey
    python3 build/blog.py       # 97 migrated blog posts
    python3 build/sitemap.py    # sitemap.xml + robots.txt

`build/territory.py` is the single source of truth for which franchise owns which city.
Correcting a city is a one-line edit there followed by a rerun; never hand-edit generated HTML.

## Data

- `data/tx.json` — 48 cities with verified local phones, 13 street addresses, 37 geo points,
  25 Google profile links. A city never claims a street address it does not have.
- `data/redirects.json` + `_redirects` + `vercel.json` + `netlify.toml` — 70 x 301.
- `data/blog-index.json` — the 97 migrated posts.

## Deliberate calls

- **No `aggregateRating` or `Review` nodes on our own business.** Google treats self-serving
  review markup as ineligible for rich results and it can draw a manual action. Reviews still
  render as visible page content.
- **Products use `Service` + `OfferCatalog`, not `Product`/`Offer`.** We publish no prices,
  and a priceless `Offer` is noise.
- **City URLs stay flat** (`/dallas-tx`), unlike the `/service-areas/city-st` pattern on the
  IA/GA/AZ sites. Zero redirects on the 48 highest-value local pages.
- **The Vodyssey funnel is `noindex,follow`** so it never competes with `/products`.

## Still open

- Blog copy de-fluff: posts were migrated as-is at Maddie's direction. Titles, metas and
  em dashes are cleaned; body copy is not rewritten yet.
- Real install-log data to give city pages genuine information gain (see the originality
  plan): city, room, window count, orientation, product, problem solved, photo.
- Dallas currently sits with East & Central Texas and is expected to move.
- Formspree endpoint and GA4 property are not wired.
