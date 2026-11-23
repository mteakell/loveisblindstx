"""Batch 3 of the city-page rewrite: North Richland Hills, Euless, Celina,
Grapevine, Sherman, Bedford, Waxahachie, Keller.

Same rules as build/city_copy_batch1.py and build/houston_towns_copy.py: every
page leads with a different window problem and product focus; geography only
where it changes the recommendation; company and product claims are the ones
the site already makes; photos are real Love Is Blinds installs, captioned
only with what they show and never claiming the town they were taken in; no
no em or en dashes, none of the banned phrases from the brief, no
rhetorical headings.

Lead angles in this batch:
  North Richland Hills  wet rooms: kitchen sink, baths, laundry
  Euless                daytime privacy that keeps the light
  Celina                east-facing bedrooms and early sun
  Grapevine             sunrooms and rooms with glass on three sides
  Sherman               insulation for hot summers and winter cold snaps
  Bedford               sun fading floors, furniture and art
  Waxahachie            natural materials for older homes and farmhouses
  Keller                drapery layered over working shades

Facts held in data (phone, address, Google profile, owner names, reviews)
come from data/tx.json, build/territory.py and data/reviews.json at render
time and are kept out of this file.
"""

CITIES = [

# ---------------------------------------------------------------------------
dict(
 slug="north-richland-hills-tx", label="North Richland Hills",
 desc="Faux wood blinds, composite shutters and wipeable shades for North Richland Hills, TX kitchens, baths and laundry rooms. Call (817) 587-6007.",
 lead="The window over the kitchen sink takes more steam, splashes and handling than any other in the house. In North Richland Hills we start there, with treatments that wipe clean and hold their shape.",
 hero=("shutters-shutters-160-jpg",
       "Open kitchen and living area with white plantation shutters on the windows above the sink and along the far wall"),
 media=("blinds-blinds-014-jpg",
        "Kitchen with white blinds lowered on the window over the sink and on a tall window beside an espresso machine"),
 intro=[
  "Kitchens, bathrooms and laundry rooms are where window treatments give out first. Real wood slats warp beside a shower, and fabric near the stove picks up grease.",
  "Our team checks each wet room on site: how close the window sits to the faucet, tub or stove, how much steam the room sees, and how often it gets cleaned. Then we recommend a material for each opening and put it all in one written quote with installation included."],
 sections=[
  ("Composite shutters over the sink",
   ["Composite shutters are made for humidity. They take steam and splashes without warping, and the louvers wipe down with a damp cloth. Over a sink they tilt open for daylight while you work and close for privacy after dark, and the panels are sized to swing clear of the faucet."],
   ("shutters-shutters-076-jpg",
    "Kitchen with dark wood cabinets and white shutters with open louvers on a wide window above the sink",
    "Shutters on a wide window above a kitchen sink.")),
  ("Faux wood blinds for baths and laundry rooms",
   ["In a bathroom the problem is daily steam. Faux wood slats are moisture-resistant and stay straight through it, and they can be washed with a mild cleaner. They are also the most budget-friendly wood look, which matters in a house with three or four baths to cover.",
    "Cordless lift keeps strings off wet counters and out of reach of small hands."],
   ("blinds-blinds-017-jpg",
    "Kitchen with gray cabinets and a white blind lowered on the window above the sink",
    "A white blind lowered over a kitchen sink.")),
  ("A fabric shade where the splash cannot reach",
   ["Some kitchens call for fabric to soften all the tile and stone. A roman shade in a wipeable fabric works when it is mounted clear of the splash zone. For a window directly behind the faucet or the cooktop, we steer you to faux wood or a composite shutter instead."],
   ("roman-shades-roman-shades-024-jpg",
    "White kitchen with a striped fabric shade lowered on the window above the sink",
    "A striped fabric shade over a kitchen sink.")),
 ],
 faqs=[
  ("What holds up best in a North Richland Hills bathroom?",
   "Faux wood blinds or composite shutters. Both are moisture-resistant and handle steam without warping."),
  ("Can real wood blinds go in a kitchen?",
   "We keep real wood in the dry rooms. Humidity can warp and crack natural wood over time, so kitchens and baths get faux wood or composite."),
  ("How do I clean faux wood blinds?",
   "Dust them weekly, and wipe them with a damp cloth and mild cleaner when they need more. Moisture does not hurt them."),
  ("How are shutters measured for these windows?",
   "Every opening is measured in three places and the depth is checked before a frame style is chosen, so each shutter is built to the window it goes in."),
 ],
 links=[("Plantation shutters", "/products/plantation-shutters"),
        ("Faux wood blinds", "/products/faux-wood-blinds"),
        ("Roman shades", "/products/roman-shades")],
 chapter_links=[("Plantation shutters", "/products/plantation-shutters"),
                ("Faux wood blinds", "/products/faux-wood-blinds"),
                ("Roman shades", "/products/roman-shades")],
 read=("The best window treatments for kitchens", "/best-window-treatments-for-kitchens"),
 extra=("Every wet room in the house",
  ["<ul><li><strong>Kitchen sink:</strong> composite shutters or faux wood blinds, mounted clear of the faucet.</li>"
   "<li><strong>Primary bath:</strong> composite shutters that close for privacy and tilt for light.</li>"
   "<li><strong>Laundry room:</strong> cordless faux wood blinds.</li>"
   "<li><strong>Breakfast nook:</strong> a roman shade in a wipeable fabric, away from the stove.</li></ul>"],
  ("Will composite shutters match the hardwood shutters in my living room?",
   "They can. Paint or stain is matched to your trim at the consultation, so composite in the wet rooms and hardwood up front share one finish.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="euless-tx", label="Euless",
 desc="Banded, dual and top-down shades for Euless, TX rooms that need daytime privacy and still want the light. Free in-home measure. Call (940) 329-5166.",
 lead="When a living room faces the street or a neighbor's windows, most people keep the blinds shut and the lamps on. For Euless homes we fit shades that block the view in and keep the daylight.",
 hero=("banded-shades-banded-shades-004-jpg",
       "Corner of a room with white banded shades lowered on tall windows and open transom windows above, a round black chandelier in front"),
 media=("honeycomb-shades-honeycomb-shades-tdbu-jpg",
        "Wide window with a light cellular shade covering the lower half and the upper glass left open to the trees"),
 intro=[
  "A closed blind trades the room's light for privacy. Shades built for daytime privacy cover the part of the window people can see into and leave the rest open to the sky.",
  "At the consultation we look at each window from both sides: what a neighbor or a passing car can see, at what height, and when the room needs to be dark. Then we bring the fabrics that answer each one and measure every opening on site."],
 sections=[
  ("Banded and dual shades",
   ["Banded shades alternate sheer and solid stripes on one continuous fabric. Line the stripes up and you see out; offset them and the view in closes, in one motion. Dual shades put a sheer layer and a darkening layer on a single headrail, a good fit for rooms that face the street.",
    "Both come in cordless and motorized versions."],
   ("banded-shades-banded-shades-009-jpg",
    "Sitting room bay with banded shades lowered and another banded shade raised partway on a side window, plaid armchairs in front",
    "Banded shades in a sitting room bay, one raised partway.")),
  ("Top-down bottom-up for front and side windows",
   ["A top-down bottom-up cellular shade lowers from the top and raises from the bottom. Drop the top edge and daylight comes in above eye level while the lower glass stays covered. The cells also insulate, which helps on a window that takes the afternoon sun."],
   ("honeycomb-shades-honeycomb-shades-009-jpg",
    "Bedroom with a light cellular shade lowered on a navy-trimmed window under a patterned fabric top treatment",
    "A cellular shade on a bedroom window under a patterned top treatment.")),
  ("Walls of glass and patio doors",
   ["Big glass toward the backyard has the same problem at a larger size. Panel track shades glide wide fabric panels along a track and stack to the side, in fabrics from sheer solar weaves to blackout. A light filtering weave keeps the room bright and blurs the view in from the yard."],
   ("smart-drapes-smart-drapes-014-jpg",
    "Tall wall of glass under open clerestory windows with light vertical fabric panels drawn across it",
    "Vertical fabric panels drawn across a tall wall of glass.")),
 ],
 faqs=[
  ("Can people see through banded shades at night in Euless?",
   "Partly, when the stripes line up and the room is lit. Slide the solid bands over the sheer ones at night, or pick a dual shade with a darkening layer."),
  ("What is the difference between dual and banded shades?",
   "A dual shade has two separate fabrics on one headrail. A banded shade uses one fabric with sheer and solid stripes that slide past each other."),
  ("Do top-down bottom-up shades come cordless?",
   "Yes. Cordless lift is standard on cellular shades."),
  ("Can privacy shades be motorized?",
   "Yes. On a dual shade each layer runs on its own from the remote or app."),
 ],
 links=[("Dual and zebra shades", "/products/dual-shades"),
        ("Honeycomb shades", "/products/honeycomb-shades"),
        ("Panel track shades", "/products/panel-track-shades")],
 chapter_links=[("Dual and zebra shades", "/products/dual-shades"),
                ("Honeycomb shades", "/products/honeycomb-shades"),
                ("Panel track shades", "/products/panel-track-shades")],
 read=("Balancing natural light and privacy", "/window-treatments-balancing-natural-light-and-privacy"),
 extra=("Privacy, room by room",
  ["<ul><li><strong>Street-facing living room:</strong> banded or dual shades.</li>"
   "<li><strong>Windows that face the next house:</strong> top-down bottom-up cellular shades.</li>"
   "<li><strong>Back slider:</strong> panel track shades in a light filtering weave.</li>"
   "<li><strong>Bedrooms:</strong> a dual shade with a darkening layer for night.</li></ul>"],
  ("Which privacy shade keeps the most daylight?",
   "Top-down bottom-up, because the upper glass stays fully open while the lower part is covered.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="celina-tx", label="Celina",
 desc="Blackout cellular, roman and roller shades for Celina, TX bedrooms that catch the early morning sun. Free in-home measure. Call (972) 846-9683.",
 lead="East-facing bedrooms take the sun at first light, well before most people want to be up. In Celina homes we fit shades that keep those rooms dark until you raise them.",
 hero=("roman-shades-roman-shades-032-jpg",
       "Bedroom with five windows in a curved bay, light roman shades raised to the top and a fenced field outside"),
 media=("roller-shades-roller-shades-042-jpg",
        "Bedroom with a cream roller shade raised partway on a glass door that opens to the backyard"),
 intro=[
  "Morning sun comes in low and flat, straight across the bed. A light filtering fabric that works fine in the afternoon lets the room glow at dawn. Where a Celina bedroom looks out over open land, there is nothing outside to soften it.",
  "Our North Texas team plans bedrooms for two times of day: early morning, when the room has to stay dark, and the rest of the day, when you want the view back. Every window and door is measured on site, and the same team returns to install."],
 sections=[
  ("Blackout cellular shades and the edges",
   ["Blackout fabric stops the light that hits it. What still gets in comes around the sides, where an inside-mounted shade leaves a small gap to the frame. Mounting the shade outside the frame with an overlap closes most of it, and on a roller shade, side channels close the rest.",
    "A blackout cellular shade adds insulation as well, which helps on a window that faces the morning sun all summer."],
   ("honeycomb-shades-honeycomb-shades-017-jpg",
    "Three windows with light cellular shades lowered and a thin line of daylight showing at the edges of each",
    "Daylight showing at the edges of three lowered shades.")),
  ("Roman shades with a blackout liner",
   ["A roman shade brings fabric and softness to a primary bedroom, and the liner decides what it does. A blackout liner darkens the room, and the shade still folds up neatly when you want the yard in view."],
   ("roman-shades-roman-shades-054-jpg",
    "Bedroom with patterned roman shades raised partway on two windows and a lawn outside",
    "Patterned roman shades raised partway on two bedroom windows.")),
  ("Windows on both sides of the bed",
   ["Windows beside the headboard put the first light right at pillow height. Blackout roller shades on those windows, built to each measured opening, lower flat and even. A motorized version can raise on a schedule at the hour you choose."],
   ("roller-shades-roller-shades-099-jpg",
    "Bedroom with roller shades raised partway on windows on both sides of the bed",
    "Roller shades raised partway beside a bed.")),
 ],
 faqs=[
  ("What is the darkest shade for an east-facing bedroom in Celina?",
   "A blackout roller shade with side channels, or a blackout cellular shade mounted to overlap the frame. Drapery over either one closes what is left."),
  ("Why does light still get in around my blackout shade?",
   "The fabric blocks it, but an inside mount leaves a small gap at each side. Side channels or an outside mount close it."),
  ("Can I keep the view during the day?",
   "Yes. Roman and roller shades raise fully, and a dual shade pairs a sheer daytime layer with a darkening one."),
  ("Do you serve all of Celina?",
   "Yes. Our North Texas team covers Celina along with Prosper, McKinney and Frisco."),
 ],
 links=[("Honeycomb shades", "/products/honeycomb-shades"),
        ("Roman shades", "/products/roman-shades"),
        ("Roller and solar shades", "/products/roller-shades")],
 chapter_links=[("Honeycomb shades", "/products/honeycomb-shades"),
                ("Roman shades", "/products/roman-shades"),
                ("Blackout roller shades", "/products/roller-shades")],
 read=("Blackout shades for bedrooms", "/blackout-shades-for-bedrooms"),
 extra=("Bedrooms on the east side",
  ["Plan the east-facing rooms first, since they decide how early the house wakes up. Blackout fabric goes on the windows facing the sunrise, and the west or north windows in the same room can take a light filtering fabric for daytime.",
   "Nurseries and kids' rooms get cordless or motorized lifts, with no cords to reach."],
  ("Can a shade open on its own in the morning?",
   "Yes. A motorized shade can raise on a schedule, so the room stays dark until the time you set.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="grapevine-tx", label="Grapevine",
 desc="Plantation shutters, solar shades and motorized shades for Grapevine, TX sunrooms, breakfast rooms and rooms facing the pool. Call (817) 562-9262.",
 lead="A room with glass on three sides gets sun from morning to evening. In Grapevine sunrooms, breakfast rooms and pool-facing living rooms, we plan each wall of glass separately.",
 hero=("shutters-shutters-love-05-jpg",
       "Sunroom with white plantation shutters on a row of tall windows and a door, louvers open to a pool outside"),
 media=("roller-shades-roller-shades-901-jpg",
        "Dining room with tan textured roller shades lowered on two windows and glass French doors with water visible beyond"),
 intro=[
  "In a room with windows on three walls, the sun is always on one of them. The east glass is bright at breakfast, the west glass is hot by late afternoon, and in winter the same glass can make it the coldest room in the house. Light bouncing off a pool or open water adds glare from below.",
  "At the consultation we note which way every window faces and what you want to see from your chair. Then we measure each opening on site and put the whole room in one written quote, with installation included."],
 sections=[
  ("Shutters for a room made of windows",
   ["Plantation shutters suit a sunroom because the louvers can be set differently on each wall. Tilt them up on the east side in the morning, angle them down on the west side in the afternoon, and close them all on a cold night. Composite holds up where a sunroom gets humid."],
   ("shutters-shutters-021-jpg",
    "Living room with white shutters across a wide bank of windows behind a cream sofa, more shuttered windows in the room beyond",
    "Shutters across a wide bank of living room windows.")),
  ("Solar shades for glare off the water",
   ["Glare from a pool or the lake lands on screens and faces at the worst angle. A solar roller shade cuts that glare and UV at the glass while the water stays in view, and a darker fabric keeps the view clearest. On tall glass, several shades can be grouped to move together from one remote."],
   ("roller-shades-roller-shades-love-07-jpg",
    "Open great room with tall roller shades raised partway over a wall of glass doors, a pool and open water outside",
    "Roller shades raised partway over a wall of glass facing a pool.")),
  ("Shades that move on a schedule",
   ["In a sunroom the sun moves faster than anyone adjusts the shades. Motorized shades can lower on the west glass every afternoon and raise again in the evening, even when the house is empty. In cellular fabric they insulate the glass while they are down."],
   ("honeycomb-shades-honeycomb-shades-026-jpg",
    "Breakfast room with light cellular shades raised near the top of windows on two walls, a dining table in the middle",
    "Cellular shades on windows along two walls of a breakfast room.")),
 ],
 faqs=[
  ("What is the best window treatment for a Grapevine sunroom?",
   "Usually a mix: shutters or cellular shades for insulation, and solar shades on the glass where you want the view."),
  ("Do solar shades work on a window facing a pool?",
   "Yes. They cut the glare off the water and keep the view."),
  ("Can shutters go on the doors into a sunroom?",
   "Yes. Hinged panels fit French doors, and bypass or bi-fold tracks fit sliders."),
  ("Where is your Grapevine office?",
   "1701 W Northwest Highway, Suite 132, Grapevine, TX 76051. We still come to you for the consultation and measure."),
 ],
 links=[("Plantation shutters", "/products/plantation-shutters"),
        ("Roller and solar shades", "/products/roller-shades"),
        ("Motorized window treatments", "/products/motorized-window-treatment-automations")],
 chapter_links=[("Plantation shutters", "/products/plantation-shutters"),
                ("Roller and solar shades", "/products/roller-shades"),
                ("Motorized window treatments", "/products/motorized-window-treatment-automations")],
 read=("The best shades for Texas sunrooms", "/best-shades-for-texas-sunrooms"),
 extra=("A three-sided room, wall by wall",
  ["<ul><li><strong>East wall:</strong> shutters or light filtering shades for bright mornings.</li>"
   "<li><strong>West wall:</strong> solar shades with a tighter weave, motorized on a schedule.</li>"
   "<li><strong>Wall facing the pool or lake:</strong> a darker solar fabric that keeps the water in view.</li>"
   "<li><strong>Doors:</strong> shutters on hinges or a track, or panel track shades.</li></ul>"],
  ("Do all the treatments in a sunroom have to match?",
   "Keeping them in one color family is enough. The products can change wall to wall and still read as one room.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="sherman-tx", label="Sherman",
 desc="Cellular shades, plantation shutters and drapery for Sherman, TX homes that face long summers and winter cold snaps. Call (903) 226-8817.",
 lead="Sherman homes see long, hot summers and winter cold snaps, and the windows lose comfort in both. We fit treatments that insulate the glass all year.",
 hero=("shutters-shutters-099-jpg",
       "Family room with a tile floor, a fireplace and white plantation shutters on several large windows"),
 media=("shutters-shutters-046-jpg",
        "Sitting room with white shutters on two windows, the upper louvers open and the lower louvers closed"),
 intro=[
  "In July the sun heats the glass and the room behind it. In January the same glass pulls warmth out of the room, and older single-pane windows lose the most in both seasons.",
  "Our North Texas team plans Sherman homes for both. We look at which way each window faces, whether the glass is single or double pane, and which rooms feel it most, then recommend a treatment for each opening and measure it on site."],
 sections=[
  ("Cellular shades for both seasons",
   ["Cellular shades hold a layer of air against the glass inside their cells. That air slows heat crossing the window in summer and keeps warmth in on a winter night. Double cell construction insulates more and pays off on big glass and older single-pane windows; newer double-pane windows often do fine with single cell.",
    "Top-down bottom-up versions let daylight in on a sunny winter afternoon while the lower glass stays covered."],
   ("honeycomb-shades-honeycomb-shades-022-jpg",
    "Two windows with light cellular shades lowered from the top, upper glass open to trees, two striped armchairs in front",
    "Cellular shades lowered from the top on two windows.")),
  ("Shutters closed on winter nights",
   ["A closed shutter puts a solid panel between the room and the glass, which keeps out more summer heat and more winter draft than a blind. In summer the louvers tilt to keep direct sun off the floor while light still comes in. Hardwood suits living and dining rooms, and composite goes where there is humidity."],
   ("shutters-shutters-007-jpg",
    "Dining room with a round table and white plantation shutters on the window behind it, a glass-paneled door to the right",
    "Shutters on a dining room window.")),
  ("Drapery over a shade for the coldest rooms",
   ["In a bedroom or living room with a lot of glass, full-length drapery over a shade adds one more layer at night. Hung high and wide, the closed panels cover the glass and the frame around it, where drafts come in."],
   ("smart-drapes-smart-drapes-005-jpg",
    "Bedroom under a wood-beamed ceiling with cream drapery closed across a wide wall of glass",
    "Drapery closed across a bedroom wall.")),
 ],
 faqs=[
  ("What window treatment insulates best for a Sherman winter?",
   "Double cell cellular shades insulate the most. Closed shutters and drapery over a shade also help."),
  ("Do I need double cell shades on newer windows?",
   "Often single cell is enough on double-pane glass. We decide window by window."),
  ("Can cellular shades be motorized?",
   "Yes. A schedule can lower them before the afternoon heat in summer and at sunset in winter."),
  ("Which team serves Sherman?",
   "Our North Texas team, the same one that covers Celina, McKinney and Prosper, measures and installs in Sherman."),
 ],
 links=[("Honeycomb shades", "/products/honeycomb-shades"),
        ("Plantation shutters", "/products/plantation-shutters"),
        ("Energy-efficient shades", "/products/energy-efficient-custom-window-shades")],
 chapter_links=[("Honeycomb shades", "/products/honeycomb-shades"),
                ("Plantation shutters", "/products/plantation-shutters"),
                ("Drapery", "/services/drapery-installation")],
 read=("The best window treatment for insulation", "/what-is-the-best-window-treatment-for-insulation"),
 extra=("Insulating a Sherman house, room by room",
  ["<ul><li><strong>West and south glass:</strong> double cell cellular shades.</li>"
   "<li><strong>Front rooms:</strong> plantation shutters, closed on cold nights.</li>"
   "<li><strong>Primary bedroom:</strong> blackout cellular shades with drapery over them.</li>"
   "<li><strong>North windows:</strong> cellular shades to hold winter warmth in.</li></ul>"],
  ("Which windows should I insulate first?",
   "The west and south glass, which take the most summer heat, and any older single-pane windows.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="bedford-tx", label="Bedford",
 desc="Solar shades, roman shades and woven wood for Bedford, TX homes where the sun is fading floors, furniture and art. Call (817) 859-6699.",
 lead="Strong sun fades wood floors, rugs, upholstery and art slowly, and most people see the damage only when they move a rug. In Bedford homes we fit treatments that cut UV at the glass and keep the rooms bright.",
 hero=("roller-shades-roller-shades-208-jpg",
       "Great room with a dark wood ceiling, stone fireplace and light roller shades raised near the top of tall black-framed windows"),
 media=("honeycomb-shades-honeycomb-shades-024-jpg",
        "Dining nook with a window seat, a light cellular shade lowered on one large window and the other window open to trees"),
 intro=[
  "Fading comes from UV and direct sun landing in the same spot day after day. The usual signs are a pale stripe across a wood floor, a sofa arm lighter than its cushions, or a print that has lost its color on the side facing the window.",
  "At a Bedford consultation we find where the sun lands in each room and at what time of day, then match each window to a fabric that blocks the UV and still lets the room feel bright. Every opening is measured on site, and the written quote includes installation."],
 sections=[
  ("Solar shades on the windows that take the sun",
   ["Solar roller shades cut glare and UV while keeping the view, which makes them the first choice where floors and furniture are fading. A tighter weave blocks more sun; a more open one keeps more of the yard in sight. Motorized on a schedule, they lower before the sun reaches the floor every day without anyone remembering to do it."],
   ("roller-shades-roller-shades-137-jpg",
    "Living room with light roller shades lowered partway on three windows, patio furniture visible outside",
    "Roller shades lowered partway on three living room windows.")),
  ("Roman shades with a liner",
   ["In a dining room with a wood table or a bedroom full of upholstered pieces, a roman shade adds fabric to the room and keeps the sun off the furniture. The liner sets how much light comes through, from a privacy liner that still glows to a blackout liner that stops it."],
   ("roman-shades-roman-shades-051-jpg",
    "Window with a patterned roman shade lowered partway, a lawn and a concrete patio visible below it",
    "A patterned roman shade lowered partway.")),
  ("Rooms with art on the walls",
   ["Art and framed prints need the sun kept off them more than the room needs darkness. Woven wood shades filter daylight into a soft glow, and a privacy or blackout liner can go behind the weave where a piece hangs in line with the window."],
   ("woven-wood-shades-woven-wood-shades-love-03-jpg",
    "Bedroom under a vaulted ceiling with woven wood shades raised partway on two windows and a large abstract painting on the wall",
    "Woven wood shades in a bedroom with a large painting.")),
 ],
 faqs=[
  ("Do solar shades stop fading in a Bedford home?",
   "They cut UV and glare at the glass, which slows fading. No shade that lets daylight in stops it completely."),
  ("Which rooms fade first?",
   "Rooms with west and south windows, since those take the most direct sun."),
  ("Do shutters protect floors?",
   "Yes. Tilted, the louvers keep direct sun off the floor while light still comes in."),
  ("Can my shades lower on their own?",
   "Yes. Motorized shades can follow a schedule that drops them before the sun reaches the floor."),
 ],
 links=[("Roller and solar shades", "/products/roller-shades"),
        ("Roman shades", "/products/roman-shades"),
        ("Woven wood shades", "/products/woven-wood-shades")],
 chapter_links=[("Roller and solar shades", "/products/roller-shades"),
                ("Roman shades", "/products/roman-shades"),
                ("Woven wood shades", "/products/woven-wood-shades")],
 read=("How to stop furniture fading in Texas sun", "/stop-furniture-fading-texas-sun"),
 extra=("Where to start in a Bedford home",
  ["<ul><li><strong>Living room with west glass:</strong> solar roller shades, motorized on a schedule.</li>"
   "<li><strong>Dining room:</strong> a roman shade with a liner over the wood table.</li>"
   "<li><strong>Wall with art across from a window:</strong> woven wood with a liner.</li>"
   "<li><strong>Breakfast nook:</strong> cellular shades, which also insulate.</li></ul>"],
  ("Will a solar shade still let me see out?",
   "Yes. You see out through the weave during the day, and a darker fabric is easier to see through.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="waxahachie-tx", label="Waxahachie",
 desc="Woven wood shades, real wood blinds and roman shades for older Waxahachie, TX homes and farmhouses. Free in-home measure. Call (469) 972-8287.",
 lead="Older Waxahachie houses and farmhouses on acreage have wood trim, wood floors and sometimes stone. We fit woven wood, real wood and fabric shades that suit them, built to each window.",
 hero=("roman-shades-roman-shades-059-jpg",
       "Living area under a white plank vaulted ceiling with textured shades lowered on two wide windows beside French doors, open windows above"),
 media=("woven-wood-shades-woven-wood-shades-026-jpg",
        "Stone-walled room with a woven wood shade lowered on a small window beside a sink"),
 intro=[
  "An older house brings tall windows, deep trim and openings that vary from room to room. A farmhouse adds stone, plank walls and wide windows toward the porch. Natural materials at the window sit well against all of it, and every piece has to be built to the opening it covers.",
  "Our team measures every window on site, including the odd sizes, and brings woven, wood and fabric samples to compare against your trim and floors. The written quote includes installation, and the old blinds come down and leave with us on install day."],
 sections=[
  ("Woven wood shades",
   ["Woven wood shades are made from bamboo, rattan, jute and natural grasses, and each weave casts its own warm, dappled light. They suit stone, shiplap and wood floors. Unlined they are a daytime shade, and a privacy or blackout liner makes the same shade work in a bedroom."],
   ("woven-wood-shades-woven-wood-shades-041-jpg",
    "Room with a rough stone wall and a wood plank ceiling, a woven wood shade raised on a small window",
    "A woven wood shade on a small window set in a stone wall.")),
  ("Real wood blinds for the front rooms",
   ["Real wood blinds have genuine grain and come in stains from pale natural tones to deep espresso, matched to your trim. The slats are lighter than faux wood, so wide windows lift easily and the stack is smaller when raised. We keep them in the dry rooms and use faux wood in kitchens and baths."],
   ("blinds-blinds-011-jpg",
    "Two windows with dark wood-tone blinds lowered and cream drapery panels hung on a black rod",
    "Wood-tone blinds under drapery panels.")),
  ("Roman shades for bedrooms",
   ["A roman shade in a textured fabric softens a bedroom with plank floors or exposed wood. Choose a relaxed fold for an older, more traditional room or a flat fold for a cleaner look, and add a blackout liner where the room needs to be dark."],
   ("roman-shades-roman-shades-062-jpg",
    "Bedroom with light textured roman shades lowered on three tall windows",
    "Roman shades lowered on three bedroom windows.")),
 ],
 faqs=[
  ("Do woven wood shades suit an older Waxahachie home?",
   "Yes. The natural weave sits well against original trim, wood floors and stone, and each shade is built to its measured window."),
  ("Real wood or faux wood blinds?",
   "Real wood for living rooms, dining rooms and bedrooms. Faux wood for kitchens, baths and laundry rooms."),
  ("Can you fit windows that are not a standard size?",
   "Yes. Every treatment is built to the measurements we take on site."),
  ("Where is your Waxahachie office?",
   "300 S Interstate 35 East Service Rd, Suite #102, Waxahachie, TX 75165. The consultation itself happens in your home, at your windows."),
 ],
 links=[("Woven wood shades", "/products/woven-wood-shades"),
        ("Real wood blinds", "/products/real-wood-blinds"),
        ("Roman shades", "/products/roman-shades")],
 chapter_links=[("Woven wood shades", "/products/woven-wood-shades"),
                ("Real wood blinds", "/products/real-wood-blinds"),
                ("Roman shades", "/products/roman-shades")],
 read=("Woven wood shades: pros, cons and where they belong", "/woven-wood-shades-pros-and-cons"),
 extra=("Natural materials, room by room",
  ["<ul><li><strong>Living and dining rooms:</strong> real wood blinds or woven wood shades.</li>"
   "<li><strong>Bedrooms:</strong> roman or woven shades with a blackout liner.</li>"
   "<li><strong>Kitchen and bathrooms:</strong> faux wood blinds or composite shutters, which handle steam.</li>"
   "<li><strong>Windows facing the porch:</strong> unlined woven wood for filtered daylight.</li></ul>"],
  ("Are woven wood shades durable?",
   "Yes. The materials are sturdy and handle daily use for years. Keep them out of direct splash zones.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="keller-tx", label="Keller",
 desc="Custom drapery layered over shades, roman shades and plantation shutters for Keller, TX living rooms and bedrooms. Call (817) 969-3372.",
 lead="A shade handles light and privacy, and on its own it can leave a large living room or primary bedroom looking unfinished. For Keller homes we layer drapery over working shades and plan both together.",
 hero=("roman-shades-roman-shades-039-jpg",
       "Dining room with a beaded chandelier and a light fabric roman shade lowered partway on a wide window"),
 media=("roman-shades-roman-shades-061-jpg",
        "Living room with two recliners facing French doors under a transom, light fabric shades lowered on the tall windows to each side"),
 intro=[
  "A working shade sits inside or just outside the window frame. Drapery adds height, color and a soft edge, and when the rod goes up high and out wide, the panels stack beside the glass and the window reads larger.",
  "We plan the two layers at one consultation: the shade for light and privacy, the drapery for finish. Fabric panels, hardware and installation are quoted together, so the lengths and stack widths are worked out before anything is ordered."],
 sections=[
  ("Drapery over a working shade",
   ["In most finished rooms the shade does the daily work and the drapery frames the window. Pair a sheer shade with blackout drapery in a bedroom, or a solar shade with textured panels in a living room. Across a wide opening or a wall of glass, a motorized track glides the panels open with one command."],
   ("smart-drapes-smart-drapes-love-02-jpg",
    "Bedroom with cream drapery panels open on each side of glass doors that lead to a balcony over water",
    "Drapery panels framing a pair of glass doors.")),
  ("Roman shades for bedrooms and dining rooms",
   ["Where drapery would crowd a room, a roman shade brings the fabric onto the window itself. Banded romans alternate fabric weights for a more structured look, and the liner handles privacy or darkness. Cordless lift is standard, and motorized romans suit tall windows."],
   ("roman-shades-roman-shades-001-jpg",
    "Bedroom with a white roman shade lowered on a window above a nightstand and lamp",
    "A roman shade lowered in a bedroom.")),
  ("Shutters for the rooms that work hardest",
   ["Kitchens, laundry rooms and baths do better with something that wipes clean. Composite shutters are painted to match your trim, so they belong to the same plan as the drapery in the front rooms."],
   ("shutters-shutters-120-jpg",
    "Kitchen with white cabinets, a wood plank ceiling and white shutters on the window above a dark farmhouse sink",
    "Shutters above a farmhouse kitchen sink.")),
 ],
 faqs=[
  ("Do you supply the drapery in Keller or only install it?",
   "Both. Fabric panels, hardware and installation come on one written quote."),
  ("How high should drapery hang?",
   "Usually well above the window frame and wider than the glass, so the panels add height and stack clear of the window."),
  ("Can heavy drapery go on a long span?",
   "Yes. Long spans and ceiling tracks are anchored to suit your wall, and the panels can run on a motorized track."),
  ("Do the shades and drapery have to go in together?",
   "No. The shades can go in first and the drapery later. Planning both at the first visit makes sure the rod or track clears the shade."),
 ],
 links=[("Drapery installation", "/services/drapery-installation"),
        ("Roman shades", "/products/roman-shades"),
        ("Plantation shutters", "/products/plantation-shutters")],
 chapter_links=[("Drapery", "/services/drapery-installation"),
                ("Roman shades", "/products/roman-shades"),
                ("Plantation shutters", "/products/plantation-shutters")],
 read=("Layering trends in Texas window treatments", "/layering-trends-in-texas-window-treatments"),
 extra=("Layers for each room",
  ["<ul><li><strong>Formal living room:</strong> a solar or light filtering shade with drapery panels.</li>"
   "<li><strong>Primary bedroom:</strong> a blackout shade with full-length drapery.</li>"
   "<li><strong>Dining room:</strong> a roman shade, or drapery over a woven shade.</li>"
   "<li><strong>Kitchen and baths:</strong> composite shutters in the trim color.</li></ul>"],
  ("Can drapery go over plantation shutters?",
   "Yes, when there is wall space for the panels to stack beside the frame. We check it at the measure.")),
),
]
