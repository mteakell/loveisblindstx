"""Territory assignment for the franchises sharing loveisblindstx.com.

Three owners, six customer-facing brands (2026-09-05 restructure at Danny's
direction, approved by Maddie):
  North Texas               - Jake Wade and Jonathan Arosemena
  DFW                       - Durrell Glick
  Cedar Creek Lake          - Danny Rohweder
  Waco                      - Danny Rohweder
  Austin                    - Danny Rohweder
  Dallas                    - Danny Rohweder
Danny closed the Tyler location and asked to retire the "East & Central
Texas" umbrella: "having to lump them together with East Texas" did not fit
how customers see the three areas. Update, same day: Maddie kept Tyler AND its pages, detached from Danny:
the physical location closed but Tyler remains a served area, attributed
neutrally to "Love Is Blinds Texas" with no owner named and no card on
the home page.
Dallas, Highland Park, Irving and Las Colinas stay with Danny under a
fourth entity, "Love Is Blinds Dallas" (Maddie, 2026-09-05: "Just Say
Dallas"). Waxahachie rides with Waco (I-35 corridor) - flagged as an
assumption for the owners to confirm.
Danny's per-city naming preference (Option 2) carries over: name only on
waco-tx; other cities in his three territories use franchise attribution.
One file so a correction never means resweeping generated pages.
"""
NORTH = {'mckinney-tx', 'frisco-tx', 'celina-tx', 'sherman-tx', 'plano-tx'}

CEDARCREEK = {'gun-barrel-city-tx', 'kerens-tx', 'corsicana-tx',
              'w-7th-avenue-corsicana-tx'}

TYLER = {'tyler-tx'}

WACO = {'waco-tx', 'waxahachie-tx'}

AUSTIN = {'austin-tx', 'round-rock-tx', 'georgetown-tx', 'taylor-tx'}

DALLAS = {'dallas-tx', 'highland-park-tx', 'irving-tx', 'las-colinas-tx'}

TERRITORIES = {
 "north": {"key":"north","name":"North Texas","brand":"Love Is Blinds North Texas",
   "leads":["Jake Wade","Jonathan Arosemena"],
   "blurb":"Sherman, Celina, Plano, McKinney, Frisco and the surrounding suburbs"},
 "cedarcreek": {"key":"cedarcreek","name":"Cedar Creek Lake",
   "brand":"Love Is Blinds at Cedar Creek Lake","leads":["Danny Rohweder"],
   "name_cities": False,
   "blurb":"Gun Barrel City, Kerens, Corsicana and the Cedar Creek Lake communities"},
 "waco": {"key":"waco","name":"Waco","brand":"Love Is Blinds Waco",
   "leads":["Danny Rohweder"],
   "name_cities": False, "named_slugs": {"waco-tx"},
   "blurb":"Waco, Waxahachie and the I-35 corridor"},
 "austin": {"key":"austin","name":"Austin","brand":"Love Is Blinds Austin",
   "leads":["Danny Rohweder"],
   "name_cities": False,
   "blurb":"Austin, Round Rock, Georgetown and Taylor"},
 "dallas": {"key":"dallas","name":"Dallas","brand":"Love Is Blinds Dallas",
   "leads":["Danny Rohweder"],
   "name_cities": False,
   "blurb":"Dallas, Highland Park, Irving and Las Colinas"},
 "tyler": {"key":"tyler","name":"East Texas","brand":"Love Is Blinds Texas",
   "leads":[],
   "name_cities": False,
   "blurb":"the surrounding East Texas communities"},
 "dfw": {"key":"dfw","name":"DFW","brand":"Love Is Blinds DFW","leads":["Durrell Glick"],
   "blurb":"Fort Worth, Denton, the Mid-Cities, Southlake, Grapevine, Coppell and Granbury"},
}

TEAM = [
 {"slug":"jake-wade","photo":"/images/team/jake-wade.jpg","name":"Jake Wade","territory":"north"},
 {"slug":"jonathan-arosemena","photo":"/images/team/jonathan-arosemena.jpg","name":"Jonathan Arosemena","territory":"north"},
 {"slug":"durrell","photo":"/images/team/durrell.jpg","name":"Durrell Glick","territory":"dfw"},
 {"slug":"danny","photo":"/images/team/danny.jpg","name":"Danny Rohweder","territory":"waco",
  "sub":"Love Is Blinds Waco, Austin, Dallas and Cedar Creek Lake",
  "covers":"the Waco corridor, the Austin metro, Dallas and the Cedar Creek Lake communities"},
]

def of(slug):
    if slug in NORTH: return TERRITORIES["north"]
    if slug in CEDARCREEK: return TERRITORIES["cedarcreek"]
    if slug in WACO: return TERRITORIES["waco"]
    if slug in AUSTIN: return TERRITORIES["austin"]
    if slug in DALLAS: return TERRITORIES["dallas"]
    if slug in TYLER: return TERRITORIES["tyler"]
    return TERRITORIES["dfw"]

def leads_for(slug):
    return of(slug)["leads"]
