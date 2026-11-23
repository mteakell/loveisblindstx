"""Batch 2 of the city-page rewrite: Grand Prairie, Denton, Waco, Lewisville,
Round Rock, Tyler, Georgetown, Flower Mound.

Same rules as build/city_copy_batch1.py and build/houston_towns_copy.py: every
page leads with a different window problem and product focus; geography only
where it changes the recommendation; company and product claims are the ones
the site already makes (products/*.html, services/drapery-installation.html,
solutions/*.html); photos are real Love Is Blinds installs, captioned only
with what they show and never claiming the town they were taken in; no em
dashes, no "honest", no X-not-Y, no rhetorical headings.

Lead angles in this batch:
  grand-prairie-tx  light that changes through the day: dual and banded shades
  denton-tx         heat in summer, cold in winter: cellular shades and shutters
  waco-tx           rentals and guest houses: blackout rollers, faux wood, woven wood
  lewisville-tx     doors: French doors, back sliders, front-door sidelights
  round-rock-tx     home offices and screen glare: solar shades, shutters, woven wood
  tyler-tx          formal front rooms: drapery, roman shades, shutters
  georgetown-tx     easy daily operation: motorized and cordless lifts
  flower-mound-tx   backyard and pool glare: solar shades, exterior shades

Offices: only Waco names its office (7215 Bosque Blvd, Suite 237). Tyler's
physical location closed (build/territory.py), so no Tyler address. The Round
Rock and Georgetown addresses on file look like mailbox suites, so neither is
presented as an office here.

Facts held in data (phone, address, Google profile, owner names, reviews)
come from data/tx.json, build/territory.py and data/reviews.json at render
time, not from this file.
"""

CITIES = [

# ---------------------------------------------------------------------------
dict(
 slug="grand-prairie-tx", label="Grand Prairie",
 desc="Dual and banded shades for Grand Prairie, TX homes: daylight and privacy from one shade, darker at night. Free in-home measure. Call (866) 518-2999.",
 lead="In a Grand Prairie living room, the light you want at breakfast is different from the light you want after dark. We fit dual and banded shades that handle both from one headrail.",
 hero=("banded-shades-banded-shades-003-jpg",
       "Dining room with a light shade lowered partway over a wide window looking out to a field, glass doors to a porch on the right"),
 media=("roller-shades-roller-shades-137-jpg",
        "Living room with a sectional sofa and light shades raised partway on three windows, a patio table visible outside"),
 intro=[
  "Most rooms in a Grand Prairie home need two settings. During the day you want daylight and a look at the yard without the street looking in. At night, with the lamps on, you want the window closed. A shade with a single fabric makes you pick one and put up with it for the other half of the day.",
  "Dual and banded shades carry two kinds of fabric on one headrail, so the same window does both jobs. We bring both styles to the house, hang samples in your own light, and measure every opening before writing the quote."],
 sections=[
  ("Two fabrics on one headrail",
   ["A dual shade pairs a sheer or solar layer for the day with a room-darkening layer for the night. Each layer raises and lowers on its own, and on a motorized shade each one answers to the remote or the app. It does the work of two stacked shades with half the hardware."],
   ("banded-shades-banded-shades-009-jpg",
    "Sitting room with banded shades lowered on a bay window and raised partway on a large side window, two plaid armchairs in front",
    "Banded shades lowered on a bay and raised partway on the window beside it.")),
  ("Banded shades for the front of the house",
   ["Banded shades, also called zebra shades, alternate sheer and solid stripes on one continuous loop. Line up the sheer stripes and you see out. Shift the loop so the solid stripes cover them and the room closes to the street, all in one motion. They suit dining and living rooms at the front of the house."],
   ("banded-shades-banded-shades-012-jpg",
    "Dining area with white banded shades lowered on two windows above a small table with potted plants",
    "Banded shades on a pair of dining room windows.")),
  ("Bedrooms that need the darker layer",
   ["Offset bands give good daytime privacy, but a bedroom usually wants more darkness than stripes can give. A dual shade with a room-darkening layer behind the sheer closes the room for sleep, and the sheer layer keeps the morning light soft. We show you both at the window before you order."],
   ("banded-shades-banded-shades-013-jpg",
    "Bedroom with two banded shades lowered on side-by-side windows above a wood dresser and a table lamp",
    "Banded shades lowered on two bedroom windows.")),
 ],
 faqs=[
  ("What is the difference between dual shades and banded shades?",
   "A dual shade has two separate layers, one sheer and one darkening. A banded shade is a single loop of sheer and solid stripes that you shift for privacy. Both sit on one headrail."),
  ("Are dual shades a good fit for a Grand Prairie room that faces the street?",
   "Yes. The sheer layer keeps daylight and the view while blocking sightlines in, and the darker layer closes the window at night."),
  ("Can each layer of a dual shade be motorized?",
   "Yes. Each layer runs on its own from a remote or an app, so the morning routine can be one button."),
  ("Do dual and banded shades come cordless?",
   "Yes. Cordless and motorized lifts are both available, which keeps cords out of reach of children and pets."),
 ],
 links=[("Dual and banded shades", "/products/dual-shades"),
        ("Motorized window treatments", "/products/motorized-window-treatment-automations"),
        ("Roller and solar shades", "/products/roller-shades")],
 chapter_links=[("Dual shades", "/products/dual-shades"),
                ("Banded shades", "/products/dual-shades"),
                ("Dual shades for bedrooms", "/products/dual-shades")],
 read=("Seeing through zebra blinds at night", "/can-you-see-through-zebra-blinds-at-night"),
 extra=("Grand Prairie, room by room",
  ["<ul><li><strong>Living room facing the street:</strong> dual shades with a sheer day layer and a darker night layer.</li>"
   "<li><strong>Dining room:</strong> banded shades, offset for privacy at dinner.</li>"
   "<li><strong>Bedrooms:</strong> dual shades with a room-darkening back layer.</li>"
   "<li><strong>Kitchen and baths:</strong> faux wood blinds that wipe clean.</li></ul>"],
  ("Do you serve all of Grand Prairie?",
   "Yes. Grand Prairie is covered by our DFW team, and every consultation takes place at your home.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="denton-tx", label="Denton",
 desc="Cellular shades and shutters for Denton, TX homes that run hot in summer and drafty in winter. Free in-home measure. Call (940) 204-0142.",
 lead="Denton homes work their windows hard both ways: summer heat coming in and winter warmth leaking out. We fit cellular shades and shutters that insulate the glass all year.",
 hero=("roman-shades-roman-shades-036-jpg",
       "Bedroom with light roman shades raised partway on a bay of five windows looking out to a lawn and a fence"),
 media=("honeycomb-shades-honeycomb-shades-020-jpg",
        "Vaulted room with dark beams, cellular shades lowered from the top over the lower half of three tall windows below three small upper windows"),
 intro=[
  "A Denton house gets both ends of the year. Afternoon sun heats the living room in July, and in January the same glass pulls warmth out of it. Builder blinds and bare windows do very little about either.",
  "We start with the rooms that feel worst in each season, usually the sunny living areas and the bedrooms, and match each window to the construction it needs. All measurements are taken on site, and installation is written into your quote."],
 sections=[
  ("Double cell shades for sun-facing glass",
   ["Cellular shades fold into cells that hold a pocket of air against the glass. That air slows heat crossing the window in both directions, which is why the same shade helps in July and in January. Double cell construction insulates more than single cell and pays off on big windows and older single-pane glass. Newer double-pane windows often do fine with single cell, and we will tell you which your windows need."],
   ("honeycomb-shades-honeycomb-shades-024-jpg",
    "Dining room with built-in bench seating, one large window covered by a white cellular shade and another open to trees",
    "A cellular shade lowered over a large dining room window.")),
  ("Bedrooms that stay warm and dark",
   ["Blackout cellular fabrics make a bedroom darker and quieter, and the cells insulate the windows you sleep beside. Top-down bottom-up operation lets you drop the shade from the top for daylight while the bottom stays closed for privacy."],
   ("honeycomb-shades-honeycomb-shades-001-jpg",
    "Carpeted room with a bay of four windows, a cellular shade lowered partway on each",
    "Cellular shades lowered partway on the four windows of a bay.")),
  ("Shutters for the front rooms",
   ["Closed, plantation shutters insulate against summer heat and winter drafts better than blinds, and the louvers tilt to let light in without opening the room to the street. A common plan is shutters on the front windows and cellular shades everywhere else."],
   ("shutters-shutters-904-jpg",
    "Vaulted room with a whitewashed brick fireplace wall, white shutters on two angled upper windows and blinds on the two windows below",
    "Shutters on angled upper windows above a brick fireplace wall.")),
 ],
 faqs=[
  ("Do cellular shades help in winter as well as summer?",
   "Yes. The air held in the cells slows heat moving through the glass both ways, so summer heat stays out and winter warmth stays in."),
  ("Single cell or double cell for a Denton home?",
   "Double cell for big windows and older single-pane glass. Newer double-pane windows often do fine with single cell. We decide window by window."),
  ("Can cellular shades darken a bedroom?",
   "Yes. Blackout cellular fabrics darken the room, and top-down bottom-up operation keeps morning privacy."),
  ("Do you serve homes outside Denton city limits?",
   "Yes. Our DFW team works across Denton and the towns around it."),
 ],
 links=[("Honeycomb shades", "/products/honeycomb-shades"),
        ("Energy-efficient shades", "/products/energy-efficient-custom-window-shades"),
        ("Plantation shutters", "/products/plantation-shutters")],
 chapter_links=[("Double cell cellular shades", "/products/honeycomb-shades"),
                ("Blackout cellular shades", "/products/honeycomb-shades"),
                ("Plantation shutters", "/products/plantation-shutters")],
 read=("A Denton cellular shade case study", "/cellular-shades-denton-tx-before-after-energy-efficiency-case-study"),
 extra=("Planning a Denton house for both seasons",
  ["<ul><li><strong>West and south living areas:</strong> double cell light filtering shades.</li>"
   "<li><strong>Bedrooms:</strong> blackout cellular, top-down bottom-up where privacy matters.</li>"
   "<li><strong>Front windows:</strong> plantation shutters.</li>"
   "<li><strong>Kitchen, baths and laundry:</strong> faux wood blinds, which shrug off steam.</li></ul>"],
  ("Will cellular shades lower my energy bill?",
   "They slow heat moving through the glass, which takes load off heating and cooling. How much you notice depends on the windows and the system, so we do not promise a number.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="waco-tx", label="Waco",
 desc="Window treatments for Waco, TX rentals, guest houses and homes: blackout for guest rooms, faux wood and woven shades. Call (254) 232-5744.",
 lead="Plenty of Waco homes are shared with someone else: student rentals near the university, guest houses, short-term rentals. We fit treatments that hold up to turnover and match from one unit to the next.",
 hero=("smart-drapes-smart-drapes-010-jpg",
       "Bedroom with sheer white drapery drawn across a wall of windows and white shutters on two windows beside the bed"),
 media=("woven-wood-shades-woven-wood-shades-040-jpg",
        "Kitchenette in a room with rough stone walls, a woven wood shade lowered partway on the small window above the sink"),
 intro=[
  "A rental window treatment has a harder life than most. Tenants and guests yank cords, bend slats and leave street-facing rooms lit at night. Owners want something that still looks right at the next walkthrough and matches across every unit they own.",
  "We plan rental treatments with the owner: what each room needs, what holds up and what is easy to replace. Our Waco team measures every opening and writes the quote with installation included, and the same team comes back to install."],
 sections=[
  ("Blackout roller shades for guest rooms",
   ["A guest bedroom has to go dark without instructions. Blackout roller shades darken the room, and side channels close the light gaps at the edges where it needs to be fully dark. A plain roller is also simple for someone who has never used it before."],
   ("roller-shades-roller-shades-085-jpg",
    "Bedroom with a tufted headboard and a chandelier, blackout shades lowered on four windows with thin lines of light at the edges",
    "Blackout shades lowered in a bedroom, light showing only at the edges.")),
  ("Faux wood blinds that take a beating",
   ["Faux wood blinds stand up to steam, cleaning chemicals, kids and pets, and they can be washed between tenants. They are the usual choice for rental kitchens, baths and laundry rooms, and one white or one stain can run through every unit so the property looks consistent from outside."],
   ("blinds-blinds-017-jpg",
    "Kitchen with light gray cabinets, a patterned tile backsplash and a white blind on the window above the sink",
    "A white blind over a kitchen sink.")),
  ("Woven wood for guest houses with character",
   ["In a cottage or guest house with stone, wood or plaster walls, woven wood shades in bamboo, jute or grasses suit the room and filter the light into a warm glow. For rentals we fit them with cordless lifts so guests cannot damage the cords, and with a privacy or blackout liner wherever someone sleeps."],
   ("roman-shades-roman-shades-047-jpg",
    "Room with rough stone walls and a beamed ceiling, a woven shade raised partway on a deep-set window",
    "A woven shade on a deep-set window in a stone wall.")),
 ],
 faqs=[
  ("What window treatments hold up best in a Waco rental?",
   "Faux wood blinds in kitchens and baths, roller shades in bedrooms and living rooms, and shutters where the owner wants a lasting finish. Each comes cordless."),
  ("Can every unit get the same look?",
   "Yes. We can repeat the same product, color and mount across units so the property looks consistent from the street."),
  ("Do your warranties transfer if I sell the property?",
   "Yes. The coverage transfers to the new owner if you sell."),
  ("Where is your Waco office?",
   "7215 Bosque Blvd, Suite 237, Waco, TX 76710. Consultations happen at the property."),
 ],
 links=[("Roller shades", "/products/roller-shades"),
        ("Faux wood blinds", "/products/faux-wood-blinds"),
        ("Woven wood shades", "/products/woven-wood-shades")],
 chapter_links=[("Blackout roller shades", "/products/roller-shades"),
                ("Faux wood blinds", "/products/faux-wood-blinds"),
                ("Woven wood shades", "/products/woven-wood-shades")],
 read=("Window treatments for short-term rentals", "/best-window-treatments-for-airbnbs-and-short-term-rentals"),
 extra=("A Waco rental, room by room",
  ["<ul><li><strong>Bedrooms:</strong> blackout roller shades, cordless or motorized.</li>"
   "<li><strong>Kitchen, baths and laundry:</strong> faux wood blinds.</li>"
   "<li><strong>Living room facing the street:</strong> light filtering roller shades.</li>"
   "<li><strong>Guest cottage or casita:</strong> woven wood with a liner.</li></ul>"],
  ("Do you work with homeowners as well as rental owners?",
   "Yes. The consultation, the products and the guarantees are the same for both.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="lewisville-tx", label="Lewisville",
 desc="Panel track shades, door shutters and shades for sliding glass and French doors in Lewisville, TX homes. Free in-home measure. Call (866) 518-2999.",
 lead="In many Lewisville homes the glass that gets used most is a door: French doors to the patio, the back slider, the glass beside the front door. We fit treatments that move with each one.",
 hero=("roller-shades-roller-shades-027-jpg",
       "Long dining room with large roller shades rolled up above walls of sliding glass, water and a pool outside"),
 media=("roman-shades-roman-shades-030-jpg",
        "Dining room with a wood table, a woven shade raised partway on one window and a large uncovered window looking out to water"),
 intro=[
  "Doors are where ordinary blinds fail first. Vertical blinds on a slider swing, clatter and lose vanes. A loose shade on a French door bangs against the glass each time the door opens, and a cord on a moving door snags. The glass beside the front door often gets nothing at all.",
  "At the consultation we check which panel slides, which way each door swings, where the handle sits and how much depth there is for hardware, then recommend the treatment that clears all of it. Each door is measured where it hangs."],
 sections=[
  ("French doors to the patio",
   ["A treatment on a French door has to travel with the door. Shutters can be built with a cut-out for the handle and hung on the door itself. Cellular shades can be fixed at the top and bottom of the glass, and a roller shade can take a hold-down bracket so it stays flat when the door swings. Anything on a door should be cordless or motorized."],
   ("shutters-shutters-love-04-jpg",
    "Two swivel chairs in front of a large window with white shutters, black-framed glass doors to a covered patio beside it",
    "Shutters on a window beside black-framed patio doors.")),
  ("Panel tracks for the back slider",
   ["Panel track shades are the usual replacement for vertical blinds on a slider. A few wide fabric panels glide on a track and stack to one or both sides, sized so the stack clears the side you walk through. Fabrics run from sheer solar weaves to blackout, including woven textures."],
   ("panel-track-shades-panel-track-shades-002-jpg",
    "Dining room beside a sliding glass door, its fabric panels stacked at the right edge and a green yard beyond",
    "A panel track shade stacked beside a sliding door.")),
  ("Glass at the front door",
   ["Sidelights beside a front door let anyone on the porch see in. Narrow shutter panels built to the sidelight's width close that view while the louvers still pass daylight, and they match shutters on the front windows so the entry reads as one design."],
   ("shutters-shutters-040-jpg",
    "Two-story entry with white shutters on the narrow sidelights beside the front door and on an arched window above the stairs",
    "Shutters on the sidelights and on an arched window above the stairs.")),
 ],
 faqs=[
  ("What replaces vertical blinds on a Lewisville patio door?",
   "Panel track shades are the most direct replacement. They use a few wide panels and stack neatly to the side."),
  ("Can plantation shutters go on a sliding door?",
   "Yes. Shutters on a bypass track slide past each other the way the door does, and bi-fold shutters fold back to clear the opening."),
  ("Will a shade on a French door swing when I open it?",
   "Not when it is mounted to the door. Fixed cellular shades and roller shades with a hold-down bracket stay against the glass."),
  ("Do you cover the glass in the front door itself?",
   "Yes, with shades mounted to the door. Sidelights get narrow shutter panels built to their width."),
 ],
 links=[("Sliding glass door solutions", "/solutions/sliding-glass-doors"),
        ("French door solutions", "/solutions/french-doors"),
        ("Panel track shades", "/products/panel-track-shades")],
 chapter_links=[("Shutters for French doors", "/solutions/french-doors"),
                ("Panel track shades", "/products/panel-track-shades"),
                ("Sidelight shutters", "/products/plantation-shutters")],
 read=("Window treatments for homes with large glass doors", "/how-to-choose-window-treatments-for-homes-with-large-glass-doors"),
 extra=("Every door in a Lewisville house",
  ["<ul><li><strong>Back slider used all day:</strong> panel track shades.</li>"
   "<li><strong>Slider that faces west or a pool:</strong> solar roller shades, if it is opened only a few times a day.</li>"
   "<li><strong>French doors:</strong> shutters or cellular shades mounted to the door.</li>"
   "<li><strong>Front door sidelights:</strong> narrow shutter panels.</li></ul>"],
  ("Do door treatments need to be cordless?",
   "Yes. A cord on a moving door snags, so anything mounted to a door should be cordless or motorized.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="round-rock-tx", label="Round Rock",
 desc="Home office window treatments in Round Rock, TX: solar shades for screen glare, shutters and woven wood. Free in-home measure. Call (512) 641-3922.",
 lead="Plenty of Round Rock homes now have a room that works as an office, and its window is rarely where the screen wants it. We fit treatments that cut the glare and keep the room bright.",
 hero=("roman-shades-roman-shades-058-jpg",
       "Open great room under a white plank vaulted ceiling, textured shades lowered on tall windows along one wall"),
 media=("honeycomb-shades-honeycomb-shades-022-jpg",
        "Two striped armchairs under a pair of windows, each cellular shade dropped from the top so trees show through the upper glass"),
 intro=[
  "A home office has two window problems. Sun on the screen makes it hard to read, and a bright window behind you on a video call turns you into a silhouette. A blackout shade fixes both and leaves you working under the lights all day.",
  "Our Austin team, which also covers Round Rock, starts with where the desk sits, which way the window faces and when it takes direct sun. Then we bring fabrics into the room to test against your own screen."],
 sections=[
  ("Solar shades beside the screen",
   ["A solar shade cuts glare and UV at the glass while you still see out, which keeps the room bright and the screen readable. The weave is chosen for the direction: tighter on a west window that takes afternoon sun, more open on a north window. Motorized versions can lower on a schedule before the sun reaches the desk."],
   ("roller-shades-roller-shades-love-21-jpg",
    "Reading corner with a lamp between two gray armchairs, light shades raised near the top of tall windows with trees outside",
    "Light shades raised near the top of tall windows behind two armchairs.")),
  ("Shutters for an office at the front of the house",
   ["When the office is the front room, facing the street, plantation shutters keep it private while the louvers tilt to steer daylight off the screen. There is no cord to tangle with the desk chair, and closed, the panels insulate against summer heat."],
   ("shutters-shutters-004-jpg",
    "Small office with a white desk, a computer and a black chair, white shutters with open louvers on the window",
    "Plantation shutters on a home office window.")),
  ("Woven wood for softer light",
   ["Woven wood shades filter the light, which keeps the room bright and takes the squint away. Bamboo, jute and grass weaves also warm up an office full of screens and white walls. Add a blackout liner if the room doubles as a guest room."],
   ("woven-wood-shades-woven-wood-shades-024-jpg",
    "Woven shade lowered over a deep-set window in a dark stone wall, daylight filtering through the weave",
    "Daylight filtering through a woven shade on a deep-set window.")),
 ],
 faqs=[
  ("What is the best window treatment for a home office in Round Rock?",
   "Usually a solar shade, chosen for the direction the window faces. It cuts screen glare and leaves the room light."),
  ("How do I stop looking like a silhouette on video calls?",
   "Soften the window behind you with a solar or light filtering shade, or turn the desk so the window sits beside you. We look at the desk position during the consultation."),
  ("Can a shade lower itself before the afternoon sun?",
   "Yes. Motorized shades run on a schedule, so a west window closes before the sun reaches the desk."),
  ("Does the Austin team cover Round Rock?",
   "Yes. Our Austin team covers Round Rock, Georgetown and Taylor, and the consultation is at your home."),
 ],
 links=[("Roller and solar shades", "/products/roller-shades"),
        ("Plantation shutters", "/products/plantation-shutters"),
        ("Woven wood shades", "/products/woven-wood-shades")],
 chapter_links=[("Solar shades", "/products/roller-shades"),
                ("Plantation shutters", "/products/plantation-shutters"),
                ("Woven wood shades", "/products/woven-wood-shades")],
 read=("Window treatments for home offices", "/window-treatments-for-home-offices"),
 extra=("Setting up a Round Rock office window",
  ["<ul><li><strong>Window beside the desk:</strong> a solar roller shade, with a tighter weave if it faces west.</li>"
   "<li><strong>Window behind you on calls:</strong> a light filtering shade to soften the backlight.</li>"
   "<li><strong>Office that is also a guest room:</strong> a dual shade, sheer for work and darker for sleep.</li>"
   "<li><strong>Street-facing office:</strong> top-down bottom-up cellular shades or plantation shutters.</li></ul>"],
  ("Will a blackout shade fix screen glare?",
   "It will, but it leaves the room dark enough to need the lights on all day. A solar shade cuts the glare and keeps the daylight.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="tyler-tx", label="Tyler",
 desc="Drapery, roman shades and plantation shutters for formal living and dining rooms in Tyler, TX homes. Free in-home consultation. Call (903) 501-3899.",
 lead="Traditional Tyler homes often keep a formal living room and a dining room at the front of the house. We fit drapery, roman shades and shutters that make those rooms look finished.",
 hero=("roller-shades-roller-shades-091-jpg",
       "Living room with long pale drapery panels framing light shades on four windows, a cream sofa and a patterned rug in front"),
 media=("shutters-shutters-073-jpg",
        "White plantation shutters filling an arched-top window, a divider rail across the middle"),
 intro=[
  "The front rooms of a traditional house are often the first ones guests see, so the windows carry much of the room's style. Builder blinds look thin there, and a bare window leaves a formal room looking unfinished from the street.",
  "We bring fabric, wood and shutter samples to the house and plan the front rooms with the rest, so the front of the house reads as one design. Each window is measured in person before we price it, and installation is part of the price."],
 sections=[
  ("Drapery hung high and wide",
   ["Drapery is placement as much as fabric. Rods go high to add height and wide so the panels stack beside the glass, and the hem is set to just touch or float above the floor. The shade underneath does the daily work of light and privacy. We supply the panels and hardware together and anchor heavy rods properly for your walls."],
   ("smart-drapes-smart-drapes-005-jpg",
    "Bedroom under a pitched wood ceiling with full-length ivory drapery closed on a black rod across one wall",
    "Ivory drapery drawn closed along a bedroom wall.")),
  ("Roman shades for the dining room",
   ["A roman shade puts fabric on a dining room window without the width of drapery. Flat folds look tailored, relaxed folds soften a traditional room, and banded romans add a structured edge. An unlined roman glows in daylight, and a privacy liner stops silhouettes at dinner after dark."],
   ("roman-shades-roman-shades-049-jpg",
    "Wide window under heavy crown trim with a white roman shade lowered most of the way, a farmhouse table in front",
    "A roman shade lowered on a dining room window.")),
  ("Shutters on the front windows",
   ["Plantation shutters are what the street sees. Hardwood suits formal rooms where the finish shows, painted or stained to match your trim at the consultation, and each frame is built to its opening, arches included."],
   ("shutters-shutters-091-jpg",
    "White plantation shutters on a wide window under crown molding in a room with a sloped ceiling",
    "Shutters on a wide window under crown molding.")),
 ],
 faqs=[
  ("Should drapery hang over a shade or on its own?",
   "Over a shade in most rooms. The shade controls light and privacy, and the drapery adds softness and height."),
  ("Can roman shades give privacy at night?",
   "Yes. A privacy liner stops silhouettes, and a blackout liner darkens the room."),
  ("Hardwood or composite shutters for a Tyler home?",
   "Hardwood for living and dining rooms where the finish shows, composite for baths, kitchens and anywhere humid."),
  ("Do you serve homes across Tyler?",
   "Yes. Consultations for Tyler and the nearby East Texas communities happen at your home."),
 ],
 links=[("Drapery installation", "/services/drapery-installation"),
        ("Roman shades", "/products/roman-shades"),
        ("Plantation shutters", "/products/plantation-shutters")],
 chapter_links=[("Drapery", "/services/drapery-installation"),
                ("Roman shades", "/products/roman-shades"),
                ("Plantation shutters", "/products/plantation-shutters")],
 read=("Window treatments for formal and casual rooms", "/how-to-pick-window-treatments-that-work-for-both-formal-and-casual-spaces"),
 extra=("Formal rooms first, then the rest",
  ["<ul><li><strong>Formal living room:</strong> drapery over a light filtering shade.</li>"
   "<li><strong>Dining room:</strong> roman shades with a privacy liner.</li>"
   "<li><strong>Front windows and entry:</strong> hardwood plantation shutters.</li>"
   "<li><strong>Baths and kitchen:</strong> composite shutters or faux wood, which handle East Texas humidity.</li></ul>"],
  ("Can the formal rooms be done first and the rest later?",
   "Yes. The written quote can be phased, starting with the front of the house.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="georgetown-tx", label="Georgetown",
 desc="Motorized and cordless shades and shutters for Georgetown, TX homes, easy to run every day with nothing to climb for. Call (737) 257-6722.",
 lead="Many Georgetown homeowners, including those in its active adult communities, want window treatments that are easy to run every day. We fit motorized and cordless options that take the reaching and pulling out of it.",
 hero=("shutters-shutters-019-jpg",
       "Living room with white shutters across a wide five-panel window below a tall paneled wall, a cream sofa with pillows in front"),
 media=("honeycomb-shades-honeycomb-shades-030-jpg",
        "Breakfast nook in a bay window with cellular shades raised partway on all three windows above a lawn"),
 intro=[
  "Window treatments get used every day, and the daily part is where old ones wear on you: a long cord to pull, a heavy shade to lift, a high window that needs a step stool, a shade over the tub you have to lean across. Over time those are the windows that stop getting opened.",
  "Our Austin team covers Georgetown and plans each room around how it is used and who uses it. We bring motorized and cordless samples to try by hand, and we measure every window ourselves."],
 sections=[
  ("One button for the whole room",
   ["Motorized shades run from a remote, a wall switch, an app, a voice assistant or a schedule. A whole room, or a whole floor, can be grouped to one button, and we set the groups up on install day. Battery motors fit without new wiring, recharge with a USB cable at the headrail and keep working from the remote when the Wi-Fi is down."],
   ("roller-shades-roller-shades-129-jpg",
    "View down from a stair rail into a two-story room with shades lowered on its high windows and on the tall windows below",
    "Shades on high and low windows in a two-story room.")),
  ("Cordless on the everyday windows",
   ["Where a motor is more than a window needs, cordless lift does the job. You raise and lower the shade by hand from the bottom rail, with no cord to find or untangle. It is standard on most of the blinds and shades we install."],
   ("woven-wood-shades-woven-wood-shades-love-02-jpg",
    "Laundry room with green cabinets on either side of a window, a woven wood shade lowered partway above the sink",
    "A woven wood shade above a laundry room sink.")),
  ("Over the tub and the sink",
   ["Windows behind a tub or over a deep counter are the hardest to reach. A motorized roller shade there lowers from a wall switch or a remote, and nobody has to lean over the water to close it. Faux wood blinds and composite shutters are the other bathroom options that handle steam."],
   ("roller-shades-roller-shades-201-jpg",
    "Marble bathroom with a freestanding tub under an arched window, a light shade lowered below the arch behind the shower curtain",
    "A shade lowered behind a freestanding tub, the arch above left open.")),
 ],
 faqs=[
  ("Are motorized shades hard to use?",
   "No. Most people use the remote or a wall switch, and a schedule can open and close them without anyone touching a thing."),
  ("How long do the batteries last?",
   "Typically several months to a year per charge, depending on the window size and use. Recharging is a USB cable at the headrail."),
  ("What happens if the power or Wi-Fi goes out?",
   "Battery motors keep working from the remote. App and voice features come back when the network does."),
  ("Do you come to homes in Georgetown's active adult communities?",
   "Yes. We serve all of Georgetown, and the consultation is at your home."),
 ],
 links=[("Motorized window treatments", "/products/motorized-window-treatment-automations"),
        ("Cordless and motorized options", "/solutions/child-and-pet-safe"),
        ("Plantation shutters", "/products/plantation-shutters")],
 chapter_links=[("Motorized shades", "/products/motorized-window-treatment-automations"),
                ("Cordless shades", "/products/shades"),
                ("Motorized roller shades", "/products/roller-shades")],
 read=("Cordless, corded or motorized lift systems", "/cordless-vs-corded-vs-motorized-lift-systems"),
 extra=("Easy operation, room by room",
  ["<ul><li><strong>Living room and high windows:</strong> motorized shades grouped to one button.</li>"
   "<li><strong>Bedrooms:</strong> motorized or cordless blackout shades, on a schedule for mornings.</li>"
   "<li><strong>Bath:</strong> a motorized shade behind the tub.</li>"
   "<li><strong>Front windows:</strong> plantation shutters, which have no lift at all; the louvers tilt with a rod or a hidden mechanism.</li></ul>"],
  ("Do shutters need to be raised and lowered?",
   "No. Shutters stay in place and the louvers tilt, so there is nothing to lift. The panels swing open when you want the window clear.")),
),

# ---------------------------------------------------------------------------
dict(
 slug="flower-mound-tx", label="Flower Mound",
 desc="Solar shades and exterior patio shades for Flower Mound, TX homes with big windows facing the backyard and pool. Call (866) 518-2999.",
 lead="In a Flower Mound home with a pool out back, the sun reaches the back windows twice: from the sky and off the water. We fit solar and exterior shades that cut the glare and keep the yard in view.",
 hero=("roller-shades-roller-shades-237-jpg",
       "Living room with a large sectional and brown solar shades lowered on a long row of windows, a pool outside"),
 media=("exterior-patio-shades-exterior-patio-shades-023-jpg",
        "Outdoor living room under a covered patio, a screen shade lowered on one side with an open yard and a fenced pool seen through it"),
 intro=[
  "The back of a Flower Mound house is often where it opens up: big windows, a door to the patio, sometimes a pool. That glass faces the yard for the view, and the afternoon sun and the light bouncing off the water come straight into the family room.",
  "We look at which way the back of the house faces, how the room is used in the afternoon and how much of the yard you want to see. Then we bring solar fabrics in more than one weave to compare at your own windows."],
 sections=[
  ("Solar shades on the windows that face the pool",
   ["Solar fabrics cut glare and UV at the glass while the yard stays in view, which also protects floors and furniture that sit in the sun. A tighter weave stops more heat and glare on a west-facing wall. A looser one keeps more of the view on the north side of the house."],
   ("roller-shades-roller-shades-105-jpg",
    "Leather armchair beside three windows and a glass door, each with a light shade lowered most of the way, a pool and patio furniture below",
    "Shades lowered on windows and a door that look out to a pool.")),
  ("Exterior shades for the pool patio",
   ["An exterior shade stops the sun before it reaches the glass or the seating, which no interior treatment can do. On a covered patio by the pool, it keeps the space usable late in the day and takes heat off the room behind it. Retractable versions roll up out of wind and hail, and motorized ones come up quickly when the weather turns."],
   ("exterior-patio-shades-exterior-patio-shades-008-jpg",
    "Covered patio with wicker chairs behind a lowered exterior screen, a fenced pool and umbrellas visible through the weave",
    "An exterior shade lowered between a patio and the pool.")),
  ("Breakfast rooms that look onto the yard",
   ["A breakfast bay facing the yard can take sun from three directions. Shutters handle it one panel at a time: tilt the louvers to block the low sun and keep the light, then open the panels when you want the whole view."],
   ("shutters-shutters-119-jpg",
    "Breakfast nook in a bay with white shutters on every window and a dark wood table under a chandelier",
    "Shutters around a breakfast bay.")),
 ],
 faqs=[
  ("What is the best shade for windows facing a pool?",
   "A solar shade. It cuts glare and UV and keeps the view of the yard. West-facing windows usually get a tighter weave."),
  ("Do exterior shades block the view of the yard?",
   "You still see the yard through the screen. A more open weave keeps more of the view, and a tighter one blocks more sun."),
  ("Can patio shades stay down in the wind?",
   "They should be raised in high wind. Motorization makes that quick, and track-guided systems hold the fabric in gusts."),
  ("Can solar shades lower on a schedule?",
   "Yes. Motorized shades on the back of the house can lower every afternoon before the sun gets there."),
 ],
 links=[("Roller and solar shades", "/products/roller-shades"),
        ("Exterior patio shades", "/products/exterior-patio-shades"),
        ("Heat and glare solutions", "/solutions/heat-and-glare")],
 chapter_links=[("Solar shades", "/products/roller-shades"),
                ("Exterior patio shades", "/products/exterior-patio-shades"),
                ("Plantation shutters", "/products/plantation-shutters")],
 read=("Roller shade openness factors explained", "/roller-shade-openness-factor-explained"),
 extra=("Planning the back of a Flower Mound house",
  ["<ul><li><strong>Family room facing the pool:</strong> solar roller shades, motorized if the windows are tall or many.</li>"
   "<li><strong>Pool patio:</strong> exterior shades, retractable or motorized.</li>"
   "<li><strong>Breakfast bay:</strong> plantation shutters.</li>"
   "<li><strong>Bedrooms on the back:</strong> blackout shades, since solar fabric can be seen through at night.</li></ul>"],
  ("Can people see in through solar shades at night?",
   "Yes, when the lights are on inside. Rooms that need privacy after dark get a dual shade or a darkening layer as well.")),
),
]
