"""Territory assignment for the three franchises sharing loveisblindstx.com.

Confirmed 2026-08-25 from the live /team/* page titles, which name each operator's
territory outright, and from Maddie's corrections:
  North Texas          - Jake Wade and Jonathan Arosemena
  DFW                  - Durrell Glick
  East & Central Texas - Danny Rohweder
Dustin Herron appears without a territory and is treated as company-wide.
Boyd, Paradise, Lewisville and Flower Mound sit with DFW, not North TX.
Dallas rides with East & Central for now and Maddie expects that to move.
One file so a correction never means resweeping 48 generated pages.
"""
NORTH = {'mckinney-tx', 'frisco-tx', 'celina-tx', 'roanoke-tx', 'argyle-tx', 'sherman-tx', 'westlake-tx', 'plano-tx', 'denton-tx', 'trophy-club-tx', 'justin-tx', 'northlake-tx', 'gainesville-tx'}

EASTWACO = {'gun-barrel-city-tx', 'taylor-tx', 'highland-park-tx', 'las-colinas-tx', 'w-7th-avenue-corsicana-tx', 'tyler-tx', 'kerens-tx', 'waco-tx', 'dallas-tx', 'georgetown-tx', 'austin-tx', 'waxahachie-tx', 'irving-tx', 'corsicana-tx', 'round-rock-tx'}

TERRITORIES = {
 "north": {"key":"north","name":"North Texas","brand":"Love Is Blinds North Texas",
   "leads":["Jake Wade","Jonathan Arosemena"],
   "blurb":"Sherman, Celina, Plano, McKinney, Denton and the northern suburbs"},
 "eastwaco": {"key":"eastwaco","name":"East & Central Texas",
   "brand":"Love Is Blinds East & Central Texas","leads":["Danny Rohweder"],
   "blurb":"Tyler, Corsicana, Gun Barrel City, Waco, the Austin metro, Highland Park and Las Colinas"},
 "dfw": {"key":"dfw","name":"DFW","brand":"Love Is Blinds DFW","leads":["Durrell Glick"],
   "blurb":"Fort Worth, the Mid-Cities, Southlake, Grapevine, Coppell and Granbury"},
}

TEAM = [
 {"slug":"jake-wade","photo":"/images/team/jake-wade.jpg","name":"Jake Wade","territory":"north"},
 {"slug":"jonathan-arosemena","photo":"/images/team/jonathan-arosemena.jpg","name":"Jonathan Arosemena","territory":"north"},
 {"slug":"durrell","photo":"/images/team/durrell.jpg","name":"Durrell Glick","territory":"dfw"},
 {"slug":"danny","photo":"/images/team/danny.jpg","name":"Danny Rohweder","territory":"eastwaco"},
 {"slug":"dustin","photo":"/images/team/dustin.jpg","name":"Dustin Herron","territory":None},
]

def of(slug):
    if slug in NORTH: return TERRITORIES["north"]
    if slug in EASTWACO: return TERRITORIES["eastwaco"]
    return TERRITORIES["dfw"]

def leads_for(slug):
    return of(slug)["leads"]
