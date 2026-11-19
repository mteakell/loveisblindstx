"""Batch 4 of the city-page rewrite: Haltom City, Prosper, Coppell, Hurst,
Weatherford, Southlake, Colleyville and Corsicana.

Same rules as build/city_copy_batch1.py and build/houston_towns_copy.py: every
page leads with a different window problem and product focus; geography only
where it changes the recommendation; company and product claims are the ones
the site already makes (products/*.html, services/drapery-installation.html,
solutions/*.html and the linked guides); photos are real Love Is Blinds
installs, captioned only with what they show and never claiming the town they
were taken in; no em dashes, no X-not-Y, no rhetorical headings.

Lead angles in this batch:
  haltom-city-tx  whole-house plan on a budget (faux wood first, shutters where seen)
  prosper-tx      new builds: wire motorized shades before the drywall
  coppell-tx      open floor plans: one sightline, several jobs
  hurst-tx        wet rooms first: kitchens, baths and laundry
  weatherford-tx  ranch and farmhouse materials: woven wood and texture
  southlake-tx    layering drapery over shades and shutters
  colleyville-tx  painted or stained: shutter and wood blind finishes
  corsicana-tx    inside or outside mount, chosen per frame

Corsicana has a second location page (w-7th-avenue-corsicana-tx) written
separately; this entry does not mention it.

Facts held in data (phone, address, Google profile, owner names, reviews)
come from data/tx.json, build/territory.py and data/reviews.json at render
time. This file holds only the copy and photo choices.
"""

CITIES = [

# ---------------------------------------------------------------------------
dict(
 slug="haltom-city-tx", label="Haltom City",
 desc="Faux wood blinds, plantation shutters and roman shades for Haltom City, TX homes, planned room by room to fit your budget. Call (866) 518-2999.",
 lead="Covering every window in a house at once is a big purchase. In Haltom City we plan it room by room, spending where it shows and keeping the other windows simple and durable.",
 hero=("roman-shades-roman-shades-053-jpg",
       "Dining room with two windows over a green lawn, textured roman shades raised to the top of each"),
 media=("blinds-blinds-008-jpg",
        "Living room with a gray paneled wall and white blinds on three windows above a tufted sofa"),
 intro=[
  "Every house has a few windows that everyone sees and many more that only the family sees. The front room, the dining room and anything facing the street set the look. Bedrooms, baths and the back of the house mostly need privacy and light control that lasts.",
  "We walk the house with you, measure every opening on site and write one quote with installation included. The quote can be split into phases, and our price match applies to it."],
 sections=[
  ("Faux wood blinds for most of the house",
   ["Faux wood blinds give the look of wood for less than real wood, and that difference adds up across a whole house. The composite and PVC slats stand up to humidity, kids and pets, and they can be washed with a damp cloth and mild cleaner. Tilt the slats and daylight comes in while the view from outside stays blocked."],
   ("blinds-blinds-016-jpg",
    "Room with a wood plank tray ceiling and white blinds on three tall windows, slats tilted open to a fenced yard",
    "White blinds on three tall windows, slats tilted open.")),
  ("Shutters where the house is seen",
   ["Plantation shutters cost more per window, so we put them where they count: the front windows and the main living space. Painted to match your trim, they look built in, and closed they insulate better than blinds. Plenty of homeowners start with the front of the house and add rooms later."],
   ("shutters-shutters-008-jpg",
    "Empty room with a lantern pendant and white plantation shutters on a wide window, louvers open",
    "White shutters on a wide front window.")),
  ("Fabric for the primary bedroom",
   ["One or two fabric shades in the private rooms change how a house feels. A roman shade with a blackout liner darkens the primary bedroom and brings in softness that blinds lack. Cordless lift is standard, so nothing hangs from the window."],
   ("roman-shades-roman-shades-004-jpg",
    "Bedroom window with a white roman shade raised partway above a bedside lamp",
    "A roman shade raised partway in a bedroom.")),
 ],
 faqs=[
  ("What is the most budget-friendly wood look for a whole house?",
   "Faux wood blinds. They cost less than real wood, handle humidity, and come in stained or painted finishes."),
  ("Can I start with a few rooms and add the rest later?",
   "Yes. The written quote can be split into phases, and many people start with the front of the house and the bedrooms."),
  ("Do you price match?",
   "Yes. Price matching is one of our guarantees, along with one free replacement for every ten treatments you order."),
  ("Do you remove the blinds you are replacing?",
   "Yes. The old blinds come down on installation day and leave with us if you want them gone."),
 ],
 links=[("Faux wood blinds", "/products/faux-wood-blinds"),
        ("Plantation shutters", "/products/plantation-shutters"),
        ("Roman shades", "/products/roman-shades")],
 chapter_links=[("Faux wood blinds", "/products/faux-wood-blinds"),
                ("Plantation shutters", "/products/plantation-shutters"),
                ("Roman shades", "/products/roman-shades")],
 read=("How much do blinds cost?", "/how-much-do-blinds-cost"),
 extra=("Where the budget goes in a Haltom City house",
  ["<ul><li><strong>Front windows and living room:</strong> plantation shutters painted to the trim.</li>"
   "<li><strong>Bedrooms:</strong> faux wood blinds, with a blackout roman shade in the primary.</li>"
   "<li><strong>Kitchen, baths and laundry:</strong> faux wood blinds, which take steam and splashes.</li>"
   "<li><strong>Back slider:</strong> a panel track shade where the vertical blinds used to hang.</li></ul>"],
  ("Are shutters worth it if I am watching the budget?",
   "On the front windows, often yes, because they set the look from the street. Elsewhere, faux wood blinds cover the window well for less.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="prosper-tx", label="Prosper",
 desc="Hardwired and battery motorized shades for new Prosper, TX homes, planned while the walls are still open. Free in-home measure. Call (972) 846-9683.",
 lead="Prosper is still building, and a house with open walls is the easiest place to plan motorized shades. We help you decide which windows to wire before the drywall goes up.",
 hero=("roller-shades-roller-shades-118-jpg",
       "Open living and dining room with a ceiling fan, light shades lowered on wide windows and a sliding door"),
 media=("roller-shades-roller-shades-137-jpg",
        "Living room with a light sectional, roller shades raised partway on three windows and a dining area through an arch"),
 intro=[
  "Hardwired motors run on low-voltage power brought to the window during construction. They never need charging and suit banks of shades that move together. Once drywall and paint are done, adding that wire means opening walls, so the decision is worth making early.",
  "If your home is already finished, battery motors do the same job with no wiring at all. Our North Texas team measures the finished openings on site, after trim and paint, and the same team comes back to install."],
 sections=[
  ("Choosing which windows to wire",
   ["Wire the windows you know you will automate: high glass in the entry and family room, a wide bank in the great room, and the media room. Rooms you might motorize later can run on battery motors, which use the same remotes, apps and schedules as the wired ones."],
   ("roller-shades-roller-shades-hardwired-motorized-down-jpg",
    "Two-story entry with a staircase and a crystal chandelier, light shades lowered on the high windows",
    "Shades lowered on the high windows of a two-story entry.")),
  ("Two rows of glass on one control",
   ["Kitchens and great rooms with an upper row of windows need both rows to move together. Banded shades alternate sheer and solid stripes: line the bands up for the view, offset them for privacy. Motorized, the upper and lower shades can be grouped to one button."],
   ("banded-shades-banded-shades-007-jpg",
    "Kitchen with a two-story wall of windows, white banded shades lowered on the upper and lower rows",
    "Banded shades on both rows of a two-story kitchen wall.")),
  ("Battery motors for the other rooms",
   ["Bedrooms and smaller rooms rarely justify the wire. A rechargeable battery motor charges with a USB cable, usually a couple of times a year, and keeps working from its remote during a power outage. A hardwired motor stops where it is until the power returns."],
   ("roller-shades-roller-shades-099-jpg",
    "Bedroom with light roller shades raised partway on two windows on either side of the bed",
    "Roller shades on two bedroom windows.")),
 ],
 faqs=[
  ("When should I talk to you about motorized shades for a Prosper new build?",
   "Before drywall if you want any of them hardwired. Ask your builder whether low-voltage wire can be run to the windows you plan to automate."),
  ("Is hardwiring worth it?",
   "For the banks of shades you know you will automate, yes. The wire costs little while the walls are open and removes charging for good."),
  ("When do you measure a new home?",
   "After drywall, trim and paint. The casing changes the opening, so a window measured before trim can come out wrong."),
  ("Can battery and hardwired shades run together?",
   "Yes. They work from the same remotes, apps and schedules, so the house runs as one system."),
 ],
 links=[("Motorized window treatments", "/products/motorized-window-treatment-automations"),
        ("Dual and banded shades", "/products/dual-shades"),
        ("Roller shades", "/products/roller-shades")],
 chapter_links=[("Motorized window treatments", "/products/motorized-window-treatment-automations"),
                ("Dual and banded shades", "/products/dual-shades"),
                ("Roller shades", "/products/roller-shades")],
 read=("Battery vs solar vs hardwired motorized shades", "/battery-vs-hardwired-vs-solar-motorized-shades"),
 extra=("A Prosper build, window by window",
  ["<ul><li><strong>Entry and two-story family room:</strong> hardwired motorized shades.</li>"
   "<li><strong>Kitchen with an upper row:</strong> banded shades grouped to one control.</li>"
   "<li><strong>Media room:</strong> blackout roller shades with side channels, wired if the walls are open.</li>"
   "<li><strong>Bedrooms:</strong> battery motors or cordless cellular shades.</li></ul>"],
  ("What should I ask my builder before closing?",
   "Whether any blinds are included and on which windows, whether low-voltage wire can reach the windows you plan to motorize, and when you can get in to have the windows measured.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="coppell-tx", label="Coppell",
 desc="Coordinated shades, shutters and panel track shades for open floor plans in Coppell, TX homes, planned as one room. Call (866) 518-2999.",
 lead="In an open Coppell floor plan, the kitchen, dining and living windows all sit in one view. We plan them together so they match, and each window still does its own job.",
 hero=("roman-shades-roman-shades-060-jpg",
       "Open dining and living area under a white plank ceiling, gray textured shades lowered on large windows and the angled upper windows left open"),
 media=("banded-shades-banded-shades-009-jpg",
        "Sitting room with two plaid armchairs, banded shades on a bay of windows and on a wide window beside it"),
 intro=[
  "One open room can face two or three directions. The dining end might take morning sun, the living area gets afternoon glare on the TV, and a slider in the middle is opened all day. Choosing each window on its own usually ends with three styles in one sightline.",
  "We start from where you stand most, often the kitchen, and plan outward from there. Every opening is measured on site, and the samples go up against your own windows to compare the colors side by side."],
 sections=[
  ("One finish across the sightline",
   ["Rooms that can see each other should agree. That can mean one product everywhere, or different products in one color family: shutters in the living area and shades at the dining table, all in the same white. Repeating the hardware finish ties it together."],
   ("shutters-shutters-161-jpg",
    "Living room with white plantation shutters on a wide window, louvers open, and a dining area with shutters beyond",
    "Shutters in the living area and the dining area beyond, in one white.")),
  ("Glare at the table",
   ["A big dining window looks great until the sun lands on the table. Cellular shades soften that light and insulate the glass. A top-down bottom-up version lowers from the top for daylight while the lower glass stays covered."],
   ("honeycomb-shades-honeycomb-shades-025-jpg",
    "Dining room with a long table and window seat, a light cellular shade lowered on one large window and the other open to the trees",
    "A cellular shade on one dining window, the other open to the yard.")),
  ("The slider in the middle",
   ["A sliding door in an open plan gets used constantly. Panel track shades replace vertical blinds with wide fabric panels that stack to one side, clear of the walkway, and the fabric can match the shades on the windows around it."],
   ("panel-track-shades-panel-track-shades-002-jpg",
    "Dining area with fabric panels stacked to one side of a sliding glass door that stands open to the yard",
    "Panel track shades stacked beside an open sliding door.")),
 ],
 faqs=[
  ("Do all the treatments in an open Coppell kitchen and living room have to match?",
   "They should look related. The product can change from window to window as long as the color and finish carry through."),
  ("What works on a sliding door next to the kitchen?",
   "Panel track shades. The panels stack beside the door, out of the walkway, and move with one pull."),
  ("How do I stop glare on the TV without darkening the room?",
   "A light filtering or solar roller shade on the windows facing the screen cuts the glare and keeps the room bright."),
  ("Which team serves Coppell?",
   "Our DFW team, which also covers Grapevine, Flower Mound, Lewisville and Southlake. The consultation is at your home."),
 ],
 links=[("Plantation shutters", "/products/plantation-shutters"),
        ("Honeycomb shades", "/products/honeycomb-shades"),
        ("Panel track shades", "/products/panel-track-shades")],
 chapter_links=[("Plantation shutters", "/products/plantation-shutters"),
                ("Honeycomb shades", "/products/honeycomb-shades"),
                ("Panel track shades", "/products/panel-track-shades")],
 read=("Window treatments for open floor plans", "/the-best-window-treatments-for-homes-with-open-floor-plans"),
 extra=("Planning an open Coppell floor plan",
  ["<ul><li><strong>Kitchen:</strong> faux wood blinds, or a wipeable roman shade mounted clear of the sink.</li>"
   "<li><strong>Dining area:</strong> top-down bottom-up cellular shades.</li>"
   "<li><strong>Living area:</strong> solar or light filtering roller shades where the TV faces the glass.</li>"
   "<li><strong>Slider:</strong> panel track shades in a fabric that matches the windows.</li></ul>"],
  ("Can motorized shades in one open room move together?",
   "Yes. A whole room can be grouped to one button or schedule, and we set up the groups on install day.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="hurst-tx", label="Hurst",
 desc="Composite shutters, faux wood blinds and wipeable shades for kitchens, bathrooms and laundry rooms in Hurst, TX. Call (817) 813-8846.",
 lead="The windows that wear out first in a Hurst home are the ones near water: over the kitchen sink, beside the tub, in the laundry room. We choose those treatments for steam and splashes first.",
 hero=("shutters-shutters-101-jpg",
       "Open kitchen with a marble island and white plantation shutters on the windows over the sink and across the living area"),
 media=("blinds-blinds-017-jpg",
        "Kitchen with gray shaker cabinets and white blinds on the window above the sink"),
 intro=[
  "Humidity is hard on real wood. Steam swells it, splashes stain it, and over time slats warp and finishes crack. Wet rooms also need more privacy than most, because a bathroom window often sits low or faces the house next door.",
  "When we measure, we look at what sits around each window: a tub deck, a faucet, a tall backsplash or a tile return that eats into the frame depth. The treatment is chosen to clear all of it before anything is ordered."],
 sections=[
  ("Shutters beside the tub",
   ["Composite shutters take steam without swelling and wipe clean. Tilt the louvers up and daylight bounces off the ceiling while the view in from outside stays closed. Over a tub, a cafe-height panel can cover the lower glass and leave the top open."],
   ("shutters-shutters-140-png",
    "Bathroom with a soaking tub, a glass shower and marble walls, white shutters on the window above the tub",
    "White shutters over a soaking tub.")),
  ("Fabric over the kitchen sink",
   ["A roman shade can work over a sink in a wipeable fabric, mounted clear of the splash zone. Raised partway while you cook, it adds texture to a kitchen full of hard surfaces. For the steamiest kitchens, faux wood or composite is the safer choice."],
   ("roman-shades-roman-shades-025-jpg",
    "Kitchen with white cabinets and a tiled backsplash, a gray textured shade raised partway over the window above the sink",
    "A textured shade raised over a kitchen sink.")),
  ("Faux wood for kitchens and laundry rooms",
   ["Faux wood blinds use composite and PVC slats that stay straight through steam and temperature swings, and a damp cloth with mild cleaner takes care of grease. Most houses use them in every wet room and keep real wood for the dry rooms where the grain shows."],
   ("blinds-blinds-014-jpg",
    "Kitchen with white cabinets and an espresso machine, white blinds on a window by the sink and on a taller window beside it",
    "White blinds on two kitchen windows.")),
 ],
 faqs=[
  ("What window treatment holds up best in a Hurst bathroom?",
   "Composite shutters or faux wood blinds. Both handle steam and wipe clean."),
  ("Can real wood go in a powder room?",
   "Yes, if there is no shower. Without steam, a powder room is a dry room as far as the wood is concerned."),
  ("Will a shutter panel hit my faucet or tub spout?",
   "Not if the panel layout is planned around it. We check that clearance when we measure."),
  ("Can bathroom shutters match the rest of the house?",
   "Yes. Composite and painted wood in the same white look identical from the street."),
 ],
 links=[("Plantation shutters", "/products/plantation-shutters"),
        ("Roman shades", "/products/roman-shades"),
        ("Faux wood blinds", "/products/faux-wood-blinds")],
 chapter_links=[("Plantation shutters", "/products/plantation-shutters"),
                ("Roman shades", "/products/roman-shades"),
                ("Faux wood blinds", "/products/faux-wood-blinds")],
 read=("Shutters for bathrooms: moisture and privacy", "/shutters-for-bathrooms-moisture-privacy"),
 extra=("Wet rooms first in a Hurst house",
  ["<ul><li><strong>Full baths:</strong> composite shutters or faux wood blinds.</li>"
   "<li><strong>Powder room:</strong> real wood or fabric, since there is no shower steam.</li>"
   "<li><strong>Kitchen sink:</strong> faux wood or composite, or a wipeable roman shade mounted clear of splashes.</li>"
   "<li><strong>Laundry room:</strong> faux wood blinds.</li></ul>"],
  ("Do I still need to run the bathroom fan with composite shutters?",
   "Yes. Run the exhaust fan during and after showers and wipe the sill now and then, so condensation does not collect on the frame.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="weatherford-tx", label="Weatherford",
 desc="Woven wood shades, textured roman shades and exterior patio shades for ranch and farmhouse homes in Weatherford, TX. Call (817) 774-9493.",
 lead="Wood ceilings, stone and windows that look out over open land. If your Weatherford home leans ranch or farmhouse, its window treatments should suit those materials.",
 hero=("roller-shades-roller-shades-209-jpg",
       "Great room with a beamed wood ceiling and stone fireplace, light shades lowered partway on tall black-framed windows"),
 media=("woven-wood-shades-woven-wood-shades-004-jpg",
        "Dining nook with wood-paneled walls, woven wood shades lowered on two windows over a round table"),
 intro=[
  "Plain white blinds can look out of place against beams, plank ceilings and a stone fireplace. Natural weaves and textured fabrics sit better beside those materials, and they filter the light into a warm glow.",
  "We bring bamboo, jute, grass and textured fabric samples to your home and hold them up in your own light, since every natural weave varies a little. Every opening is measured on site, including windows set deep in stone or brick."],
 sections=[
  ("Woven wood in the bedroom",
   ["Woven wood shades are made from bamboo, rattan, jute and grasses. Unlined, light comes through the natural gaps in the weave. Add a privacy or blackout liner and the same shade covers a bedroom window at night."],
   ("woven-wood-shades-woven-wood-shades-031-jpg",
    "Bedroom with a cane headboard and woven wood shades raised partway on two windows beside the bed",
    "Woven wood shades raised on two bedroom windows.")),
  ("Small windows in stone and plank rooms",
   ["A small window in a rustic room usually looks best with a fabric shade set inside the frame, so the stone or trim around it stays in view. A roman shade with a privacy liner covers a bathroom window after dark and folds up out of the way during the day."],
   ("roman-shades-roman-shades-042-jpg",
    "Bathroom with stone walls and a wood plank ceiling, a roman shade raised on a small window",
    "A roman shade on a small window in a stone-walled bathroom.")),
  ("A patio that faces the land",
   ["On a covered patio, the late sun comes in under the roof. An exterior shade stops it at the outside of the opening, and a solar screen weave cuts glare and heat while keeping the view across the property. Retractable versions roll up out of wind and hail when the patio is empty."],
   ("exterior-patio-shades-exterior-patio-shades-023-jpg",
    "Covered patio with a stone wall and outdoor kitchen, an exterior screen shade lowered on one opening and a pool and open field beyond",
    "An exterior screen shade lowered on one side of a covered patio.")),
 ],
 faqs=[
  ("Are woven wood shades a good choice for a farmhouse kitchen?",
   "Yes, kept out of the direct splash zone. Right over a busy sink, faux wood or composite holds up better."),
  ("Can woven wood shades be motorized?",
   "Yes. The motor sits inside the headrail, and the shade looks the same as a manual one."),
  ("Do patio shades come motorized?",
   "Yes. They run from a remote, wall switch, app or schedule, which helps on wide openings and when the wind picks up."),
  ("Do you have a Weatherford address?",
   "Yes: 220 Adams Dr, STE 280 - 1052, Weatherford, TX 76086. We come to you for the consultation and the measure."),
 ],
 links=[("Woven wood shades", "/products/woven-wood-shades"),
        ("Roman shades", "/products/roman-shades"),
        ("Exterior patio shades", "/products/exterior-patio-shades")],
 chapter_links=[("Woven wood shades", "/products/woven-wood-shades"),
                ("Roman shades", "/products/roman-shades"),
                ("Exterior patio shades", "/products/exterior-patio-shades")],
 read=("Woven wood shades: pros, cons and where they belong", "/woven-wood-shades-pros-and-cons"),
 extra=("A Weatherford ranch house, room by room",
  ["<ul><li><strong>Great room with beams and stone:</strong> light filtering roller shades or woven wood in a natural tone.</li>"
   "<li><strong>Bedrooms:</strong> woven wood with a blackout liner.</li>"
   "<li><strong>Dining room and study:</strong> woven wood or a textured roman shade.</li>"
   "<li><strong>West patio or porch:</strong> exterior solar screen shades, motorized on wide openings.</li></ul>"],
  ("How do I choose a weave color for a room with wood ceilings?",
   "Hold the samples against the wood in your own daylight. Natural materials shift with the light, which is why we bring them to the house.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="southlake-tx", label="Southlake",
 desc="Drapery layered over shutters and shades, plus sheers for sliding doors, in Southlake, TX homes. Free design consultation at home. Call (817) 961-9004.",
 lead="In a Southlake living room or primary suite, the windows are often the last part of the room left to finish. We layer drapery over a working shade or shutter so the room looks complete and still controls light.",
 hero=("smart-drapes-smart-drapes-002-jpg",
       "Vaulted bedroom with a crystal chandelier, white plantation shutters on the windows and long drapery panels on either side of one"),
 media=("smart-drapes-smart-drapes-long-jpg",
        "Sheer white drapery drawn the length of a window wall beside a round dining table under a plank ceiling"),
 intro=[
  "A shade or shutter handles light and privacy. Drapery adds height, softness and a finished edge, and it closes the light gaps a shade leaves at the sides. Layered, the two do more than either one on its own.",
  "We supply the drapery and the hardware and quote them together with installation, so panel lengths and stack widths are worked out at your windows before anything is made. Rods and ceiling tracks are anchored for the weight they carry."],
 sections=[
  ("Drapery over a cellular shade",
   ["Panels on either side of a window frame it, and a rod mounted high adds height to the room. The cellular shade underneath does the daily work: it lowers for privacy, insulates the glass, and on an arched window it can cover the rectangle while the arch stays open."],
   ("honeycomb-shades-honeycomb-shades-013-jpg",
    "Arched-top window with patterned drapery panels on an iron rod and a light cellular shade lowered below the arch",
    "Drapery panels framing a cellular shade under an arched top.")),
  ("Sheers across a sliding door",
   ["A standard shade has to be raised every time someone uses the door. Sheer vertical panels on a track draw to one side instead, filter daylight when closed and leave the door free. Drapery on a track works the same way and stacks beside the frame."],
   ("smart-drapes-smart-drapes-navy-jpg",
    "Dining area with sheer vertical panels on a navy-topped track across a sliding door, white blinds on the windows on each side",
    "Sheer vertical panels drawn across a sliding door.")),
  ("Full-width drapery in the primary suite",
   ["Across a wall of glass, drapery on a ceiling-mounted rod or track turns the windows into one soft surface. Blackout drapery darkens the room for sleep, and a motorized track can open the panels on a schedule each morning."],
   ("smart-drapes-smart-drapes-005-jpg",
    "Bedroom under a beamed wood ceiling with cream drapery closed across a full wall on a black rod",
    "Cream drapery closed across a bedroom wall.")),
 ],
 faqs=[
  ("Do you supply the drapery or only install it?",
   "Both. The fabric panels, the rods or tracks and the installation are quoted together."),
  ("How high should drapery hang in a Southlake great room?",
   "High and wide: mounted well above the window and extended past it, so the panels add height and stack off the glass when open."),
  ("Can drapery go over plantation shutters?",
   "Yes. The rod is set far enough out for the shutter panels to swing open, and the drapery adds softness while the shutters handle the light."),
  ("Will a motorized drapery track work with my smart home?",
   "Yes. Motorized tracks run from a remote, an app, a voice assistant or a schedule."),
 ],
 links=[("Drapery installation", "/services/drapery-installation"),
        ("Honeycomb shades", "/products/honeycomb-shades"),
        ("Sliding glass door solutions", "/solutions/sliding-glass-doors")],
 chapter_links=[("Honeycomb shades", "/products/honeycomb-shades"),
                ("Sliding glass door solutions", "/solutions/sliding-glass-doors"),
                ("Drapery installation", "/services/drapery-installation")],
 read=("Layering trends in Texas window treatments", "/layering-trends-in-texas-window-treatments"),
 extra=("Layering a Southlake home",
  ["<ul><li><strong>Primary suite:</strong> a blackout shade with full drapery over it.</li>"
   "<li><strong>Living room:</strong> plantation shutters with side panels for softness.</li>"
   "<li><strong>Sliding door:</strong> sheer verticals or drapery on a track.</li>"
   "<li><strong>Dining room:</strong> a roman shade under stationary panels.</li></ul>"],
  ("Should the drapery and the shade be the same color?",
   "They should share a palette. A quiet shade under a patterned or textured drapery lets the fabric lead and keeps the window calm.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="colleyville-tx", label="Colleyville",
 desc="Painted or stained plantation shutters and real wood blinds for Colleyville, TX homes, matched to your trim and wood floors. Call (817) 859-7116.",
 lead="The first shutter decision in many Colleyville homes is the finish. Painted shutters join the trim, and stained ones pick up wood floors, doors and cabinets. We help you choose room by room.",
 hero=("shutters-shutters-028-jpg",
       "Living room with white plantation shutters on three tall windows below a row of transom windows, armchairs around a coffee table"),
 media=("shutters-shutters-love-15-jpg",
        "Dining room with a long farmhouse table and white plantation shutters on the windows along the wall"),
 intro=[
  "White and off-white shutters read as part of the architecture and bounce light deeper into the room. Stain shows the grain and turns the window into a warm feature, which suits studies, dens and rooms with stained doors or floors.",
  "Finishes look different at home than under store lights, so we bring samples to your windows and hold them against your trim at the hour the room gets used. Paint and stain are matched during the consultation."],
 sections=[
  ("Stained shutters for studies and dens",
   ["Real wood takes stain best, because the grain shows through. In a darker room or one with paneling, stained shutters read like furniture. Hidden tilt rods keep the louvers clean if you want the simplest look."],
   ("shutters-shutters-077-jpg",
    "Stained wood shutters with louvers tilted open on three windows set into dark green paneled walls",
    "Stained shutters on three windows in a green paneled room.")),
  ("Painted shutters matched to the trim",
   ["Most homes already have several whites: ceilings, trim, cabinets and doors. Shutters look best matched to the trim they sit inside, and a near miss shows along the line where the shutter frame meets the casing."],
   ("shutters-shutters-049-jpg",
    "Sitting area with two floral wingback chairs and white plantation shutters on the windows on either side",
    "White shutters on the windows of a sitting area.")),
  ("Real wood blinds for the dry rooms",
   ["Real wood blinds bring grain and warmth to bedrooms and studies. The slats are lighter than faux wood, so a wide window lifts more easily and the stack is smaller when raised. Stains run from pale natural tones to deep espresso."],
   ("blinds-blinds-011-jpg",
    "Two windows with wood-tone blinds lowered and cream drapery panels hanging from an iron rod",
    "Wood-tone blinds under drapery panels.")),
 ],
 faqs=[
  ("Can I have white shutters in some Colleyville rooms and stained in others?",
   "Yes. Keep one finish in rooms that see each other, and one finish across the front windows so the house looks consistent from the street."),
  ("Should shutters match the trim or the walls?",
   "The trim. Hold the sample flat against the window casing to check."),
  ("How do I clean stained shutters?",
   "A soft cloth or duster across the louvers, and a barely damp cloth for marks. Skip ammonia and abrasive cleaners, which dull the finish."),
  ("What louver sizes are available?",
   "Louvers run from 2.5 to 4.5 inches, and we bring samples of each size to hold against your own window."),
 ],
 links=[("Plantation shutters", "/products/plantation-shutters"),
        ("Real wood blinds", "/products/real-wood-blinds"),
        ("Custom shutters", "/products/shutters")],
 chapter_links=[("Plantation shutters", "/products/plantation-shutters"),
                ("Custom shutters", "/products/shutters"),
                ("Real wood blinds", "/products/real-wood-blinds")],
 read=("White or stained? Choosing plantation shutter finishes", "/white-or-stained-plantation-shutter-finishes"),
 extra=("Finishes across a Colleyville house",
  ["<ul><li><strong>Front rooms and living areas:</strong> painted shutters matched to the trim.</li>"
   "<li><strong>Study or den:</strong> stained hardwood shutters.</li>"
   "<li><strong>Bedrooms:</strong> real wood blinds in a stain that suits the furniture or floors.</li>"
   "<li><strong>Kitchen and baths:</strong> painted composite shutters, which handle moisture.</li></ul>"],
  ("Does afternoon sun change how a finish looks?",
   "Yes. Warm west light can push a white toward cream and make a mid-tone stain look redder, so judge samples at the window where they will hang.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="corsicana-tx", label="Corsicana",
 desc="Custom shades, blinds and shutters for Corsicana, TX homes, with an inside or outside mount chosen for each window frame. Call (903) 420-9161.",
 lead="Before fabric or color, every Corsicana window needs one practical decision: whether the treatment sits inside the frame or covers it. We check each opening and recommend the mount it supports.",
 hero=("roman-shades-roman-shades-033-jpg",
       "Bedroom with five tall windows along a curved wall, white roman shades lowered partway inside each frame"),
 media=("honeycomb-shades-honeycomb-shades-030-jpg",
        "Breakfast bay with light cellular shades raised partway inside three windows and a round table in front"),
 intro=[
  "An inside mount looks built in and leaves the trim and sill on show, but it needs a frame that is deep enough and close to square. An outside mount covers the whole opening, blocks more light and makes a small window look bigger.",
  "Window cranks, alarm sensors and deep sills all take up depth, and any one of them can change the answer. Our Cedar Creek Lake team measures every Corsicana window on site, so problems like these are found at the consultation."],
 sections=[
  ("Inside mount for windows with good trim",
   ["When the casing is worth seeing, the shade goes inside it. Woven wood and roman shades look tailored set into the frame, and the sill stays clear for plants or books. Expect a small light gap at each side, which comes with any inside mount."],
   ("woven-wood-shades-woven-wood-shades-home-b-jpg",
    "Den with a leather armchair and patterned rug, woven wood shades mounted inside three windows and lowered partway",
    "Woven wood shades set inside three window frames.")),
  ("Outside mount for full coverage",
   ["Mounted on the wall above the frame, a shade overlaps the opening on every side. That blocks more light at the edges, covers more of the glass, and forgives a frame that is out of square or too shallow."],
   ("roller-shades-roller-shades-049-jpg",
    "Light roller shade mounted above a window and lowered over it, two stained glass panels showing through the fabric",
    "A roller shade mounted above the frame, covering the whole window.")),
  ("How deep the frame needs to be",
   ["Each product needs a different depth for an inside mount. Roller shades need the least, cellular shades need room for the headrail and stack, blinds need room for the slats to tilt, and shutters need the most so the louvers clear the glass."],
   ("roman-shades-roman-shades-049-jpg",
    "Dining room with a white roman shade lowered most of the way inside a trimmed window above a table set with blue placemats",
    "A roman shade mounted inside a trimmed dining room window.")),
 ],
 faqs=[
  ("Which mount is better for a Corsicana bedroom?",
   "Usually an outside mount. It overlaps the frame and blocks more light at the edges."),
  ("What if my window frame is not square?",
   "An outside mount covers the difference. Shutters can also handle it through the frame style, which we choose after measuring."),
  ("Can you mount inside a shallow frame?",
   "Often with a roller shade, which needs the least depth. If the frame is too shallow for the product you want, we recommend an outside mount."),
  ("Who serves Corsicana?",
   "Our Cedar Creek Lake team, which also covers Kerens and Gun Barrel City. The consultation takes place in your home."),
 ],
 links=[("Woven wood shades", "/products/woven-wood-shades"),
        ("Roller shades", "/products/roller-shades"),
        ("Roman shades", "/products/roman-shades")],
 chapter_links=[("Woven wood shades", "/products/woven-wood-shades"),
                ("Roller shades", "/products/roller-shades"),
                ("Roman shades", "/products/roman-shades")],
 read=("Inside mount vs outside mount", "/inside-mount-vs-outside-mount-blinds"),
 extra=("Mount by mount in a Corsicana home",
  ["<ul><li><strong>Living and dining rooms with good trim:</strong> inside-mount woven wood or roman shades.</li>"
   "<li><strong>Bedrooms:</strong> outside-mount blackout shades.</li>"
   "<li><strong>Kitchen window with a crank:</strong> an outside mount, or a roller shade if the depth allows.</li>"
   "<li><strong>Bay windows:</strong> an inside mount on each window so the shades line up.</li></ul>"],
  ("Will an inside mount leave light gaps?",
   "A small one at each side. In rooms that need darkness, an outside mount or drapery closes it.")),
),
]
