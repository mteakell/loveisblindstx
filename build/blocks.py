"""The written sections that carry a city page when reviews cannot.

Dallas has 4 reviews and Arlington 1, so those pages have to earn their depth
from copy rather than customer voice. These blocks add roughly 1,100 words.

Everything rotates on the city index with coprime strides, so two neighbouring
cities do not open with the same paragraph. That matters at 48 pages: identical
blocks repeated 48 times is a duplicate-content problem, not a content win.

Exterior patio shades get their own block rather than a mention. It is the term
Love Is Blinds can actually win: Waco already sits at ARP 2.08 with 93.88 SoLV
on it, and the national competitors are not contesting it.

Claims trace to products_spec.py and the guarantee slides. Where a real number
would help and we do not have one, the copy says what decides the number.
"""

# ---------------------------------------------------------------- rooms
ROOMS = [
 ("Which rooms need which treatment in {city}",
  [("West-facing living rooms",
    "The afternoon sun is the whole problem in a Texas west room. Solar screen cuts glare and heat "
    "while keeping the view out, and the openness of the weave is the dial: tighter stops more heat, "
    "looser keeps more view."),
   ("Bedrooms",
    "This is a blackout decision, and blackout is a fabric job rather than a slat one. Light finds "
    "the gaps between slats and around the edges, so a room that has to go genuinely dark needs "
    "fabric and a mount that covers the opening rather than sitting inside it."),
   ("Kitchens and bathrooms",
    "Moisture rules out real wood. Faux wood and composite hold their shape over a sink or in a room "
    "that steams up, which is why we specify them there even when wood is the nicer material."),
   ("Covered patios and porches",
    "Stop the sun outside the glass. An exterior shade on a patio keeps heat off the opening before "
    "it arrives, which an interior blind on the same window cannot do.")]),
 ("Choosing by room in {city}",
  [("Rooms you use in the evening",
    "Privacy after dark is the requirement, not light control. Anything that closes fully works, so "
    "choose on look and budget rather than on fabric performance."),
   ("Rooms with a view worth keeping",
    "Solar screen and woven wood both filter without blocking. You give up some heat rejection to "
    "keep the view, and that trade is the decision rather than a compromise."),
   ("Rooms that drive the cooling bill",
    "Cellular shades trap air in their cells, which is the reason they insulate where a flat fabric "
    "does not. Worth the money on the glass that is actually costing you."),
   ("Outdoor rooms",
    "A porch or covered patio in {city} is usable through the afternoon with exterior shades and "
    "unusable without them. Motorized versions roll up out of the weather when the wind turns.")]),
 ("Room by room in a {city} home",
  [("Tall and two-storey windows",
    "Weight decides this before style does. Real wood is lighter than faux for the same panel, and a "
    "heavy panel on a tall opening loads the hinges and sags over years."),
   ("Wide sliding doors",
    "A door you use every day has to keep working. Bypass or bi-fold panels move out of the way and "
    "stack somewhere that is not the walkway, which is a mounting decision made at the opening."),
   ("Nurseries and children's rooms",
    "Cordless lift or motorization, with no loop anywhere. A cord cleat is not a solution, it is a "
    "reminder to be careful."),
   ("Patios, pergolas and screened porches",
    "Exterior shades turn an outdoor room into somewhere you sit in July. This is the part of the "
    "job most companies in {city} treat as an afterthought and we do not.")]),
]

# ---------------------------------------------------------------- materials
MATERIALS = [
 ("What each material actually does",
  "Real wood is the lightest of the slat materials and the only one that shows grain, so it belongs "
  "on tall openings and in dry rooms. Faux wood is heavier and does not care about humidity, which "
  "is why it goes over sinks and in bathrooms. Composite splits the difference with a wood core and "
  "a hard outer skin. Aluminium fits shallow openings where none of the others will. On the fabric "
  "side, the weave decides everything: an open weave filters and keeps the view, a tight weave cuts "
  "heat, and a blackout liner is the only thing that genuinely darkens a room."),
 ("Materials, and where each one fails",
  "Every material has a room that ruins it. Real wood moves with moisture, so a bathroom warps it. "
  "Faux wood is heavy, so a tall opening sags it. Aluminium slats bend under rough use. Open-weave "
  "solar fabric will not darken a bedroom no matter how dark the colour looks in the sample. "
  "Choosing well is mostly knowing which failure applies to your room, which is a question we ask at "
  "the consultation rather than something you should have to work out from a catalogue."),
 ("Picking a material without guessing",
  "Three questions settle it. Does the room get moisture, which rules out real wood. Is the opening "
  "tall or wide, which favours the lighter material because panel weight loads the hinges. Does the "
  "room need to go dark, which moves you off slats entirely and onto fabric with a blackout liner. "
  "Answer those and the material is usually decided before anyone talks about colour."),
]

# ---------------------------------------------------------------- patio
PATIO = [
 ("Exterior patio shades in {city}",
  "Shading the outside of the glass is the only approach that stops heat before it enters. An "
  "interior blind absorbs sun that has already come through the window and re-radiates it into the "
  "room. An exterior shade on a patio or a window stops it at the outside face, which is why the same "
  "fabric performs differently depending on which side of the glass it hangs.",
  [("Solar screen patio shades", "Open-weave screen that cuts glare and heat while keeping the view "
    "out to the yard. The usual answer for a covered patio taking hard afternoon sun."),
   ("Motorized patio shades", "Remote, wall switch, app or scheduled. The practical option on wide "
    "openings, and the quickest way to get fabric up when the wind turns."),
   ("Retractable shades", "Roll up out of the weather when the space is not in use, which keeps "
    "fabric out of wind and hail and extends its working life."),
   ("Porch and outdoor room shades", "Enclose a porch so it stays usable through the hottest part "
    "of the day without losing the airflow that makes it worth sitting in.")]),
 ("Why exterior shades matter more in {city} than interior ones",
  "A west-facing patio takes the worst of the afternoon. Once that sun is through the glass the heat "
  "is already in the room and an interior treatment is managing the symptom. Exterior shades are the "
  "only part of the job that changes how much heat arrives in the first place, and on a covered patio "
  "they are the difference between a space you use in July and one you look at.",
  [("Openness factor", "The weave rating is the trade you are making: tighter cuts more heat, looser "
    "keeps more view. It is the single most consequential choice on an exterior shade."),
   ("Wind-rated hardware", "Texas weather is the thing that ends outdoor fabric early. Track guided "
    "and wind-rated systems exist because unguided fabric on a windy opening does not last."),
   ("Sun and wind sensors", "A sensor drops the shade when the sun hits that elevation and raises it "
    "when the wind gets up, which is the part people underestimate until they have lost fabric to a "
    "storm."),
   ("Exterior solar shades for windows", "Not only patios. Mounted outside the glass on a west "
    "elevation, they cut the cooling load on that wall rather than managing it after the fact.")]),
]

# ---------------------------------------------------------------- motorization
MOTOR = [
 ("Motorization, and when it is worth it",
  "Motorization earns its money in three places: windows too high to reach without a ladder, banks of "
  "windows where operating each one is a chore, and exterior shades that need to come down before you "
  "are home. Everywhere else it is a convenience rather than a fix. Battery motors avoid running "
  "wiring and need recharging periodically. Hardwired removes that but has to be planned before the "
  "wall closes. Both can run on a remote, a wall switch, an app or a schedule, and retrofit "
  "motorization exists for treatments already installed."),
 ("What to ask before you motorize",
  "Four questions that decide whether it is worth doing. Is the window one you would otherwise need a "
  "ladder for. Is it a bank of windows where you would be operating six things instead of one. Is it "
  "an exterior shade that should come down on a schedule rather than when someone remembers. And who "
  "services the motor when it needs attention, because that answer is the one people forget to ask "
  "until they need it."),
]

# ---------------------------------------------------------------- process
PROCESS = ("How the job runs", [
 ("Free in-home consultation",
  "We bring samples to your home so you can hold fabrics against your own light rather than a "
  "showroom's. No charge for the visit and no obligation to order."),
 ("We measure every opening",
  "Measured on site by us, not from numbers sent over. That is deliberate: a custom treatment is cut "
  "to a number, so if the number is wrong the treatment is wrong and it is not returnable."),
 ("A written quote you approve",
  "The quote covers the treatment built to those measurements and professional installation. The "
  "amount you approve is the amount you pay."),
 ("The same team installs",
  "The person who measured your windows fits them. If an opening does not match the approved "
  "measurements we remake it and reinstall at no cost."),
])

# ---------------------------------------------------------------- extra FAQ
EXTRA_FAQ = [
 ("Can you match a quote from another company?",
  "Yes. We offer an apples-to-apples price match, so a like-for-like quote from another company is "
  "something to bring to the consultation rather than something to negotiate around."),
 ("What happens if something breaks years from now?",
  "Factory defects are covered for life by the manufacturer's limited lifetime warranty. On top of "
  "that we run a four-year service guarantee: if you have an issue with your treatments we come out "
  "and service them at no cost."),
 ("Does the warranty survive if I sell the house?",
  "Yes. Our warranties transfer to the new owner, so the cover stays with the windows."),
 ("Do I have to buy everything at once?",
  "No, and most people do not. Rooms get done in stages all the time. Worth knowing that for every "
  "ten treatments you buy we replace one free, so a whole-house job earns that faster."),
 ("Are exterior shades really better than interior ones for heat?",
  "For heat, yes, and it is not close. An exterior shade stops sun at the outside face of the glass. "
  "An interior blind is managing sun that is already in the room. For privacy and looks, interior "
  "treatments are the right tool."),
 ("Can you work with an opening that is out of square?",
  "Yes, and older homes often are. A rigid panel cannot hide a gap, so an out-of-true opening gets "
  "handled by the frame style and the mount rather than by the treatment. It is one of the things we "
  "check while measuring."),
]


# ---------------------------------------------------------------- item pools
# Whole-block variants gave 48 pages only 3 possible room sections, so pages
# shared 42% of their sentences. Composing 4 items from a pool of 12, with the
# starting point rotated per city, produces a different section on almost every
# page from the same amount of writing.
ROOM_HEADS = [
 "Which rooms need which treatment in {city}",
 "Choosing by room in {city}",
 "Room by room in a {city} home",
 "What works where in {city}",
 "Matching the treatment to the room in {city}",
]
ROOM_ITEMS = [t for _, items in ROOMS for t in items]

PATIO_HEADS = [
 "Exterior patio shades in {city}",
 "Why exterior shades matter more in {city} than interior ones",
 "Shading the outside of the glass in {city}",
 "Patio and outdoor room shades for {city}",
]
PATIO_INTROS = [p for _, p, _ in PATIO]
PATIO_ITEMS = [t for _, _, items in PATIO for t in items]

MOTOR_HEADS = [
 "Motorization, and when it is worth it",
 "What to ask before you motorize",
 "Motorized treatments in {city}",
 "When a motor earns its money",
]
MOTOR_BODIES = [b for _, b in MOTOR]

MATERIAL_HEADS = [h for h, _ in MATERIALS]
MATERIAL_BODIES = [b for _, b in MATERIALS]

EXTRA_FAQ += [
 ("Do you install treatments I bought elsewhere?",
  "Our quotes cover measurement, the treatment built to those measurements and installation as one "
  "job, which is what lets us stand behind the fit. Ask at the consultation about anything already "
  "on site."),
 ("How do I know the fabric will look right in my room?",
  "You hold it against your own light rather than a showroom's. That is the reason the consultation "
  "happens at your house, because a fabric that reads warm under store lighting can read grey on a "
  "north-facing wall."),
 ("What is the difference between light filtering and blackout?",
  "Light filtering softens the light and keeps the room usable in daylight. Blackout is built to stop "
  "it, and only works if the mount covers the opening rather than sitting inside it, because light "
  "gets in around the edges of an inside mount."),
 ("Can one treatment handle a window used day and night?",
  "Banded and dual shades alternate sheer and solid bands on one roller, so lining up the sheers "
  "gives you filtered light with the view and lining up the solids closes the window. It is one "
  "treatment doing the job people usually solve with two layers."),
 ("How long do custom treatments last?",
  "Longer than the room usually stays the same. Factory defects are covered for life by the "
  "manufacturer's limited lifetime warranty, and our four-year service guarantee covers coming out "
  "and servicing them at no cost in the meantime."),
 ("Do exterior shades hold up to Texas weather?",
  "The ones specified for it do. Track guided and wind-rated systems exist because unguided fabric on "
  "a windy opening does not last, and retractable versions roll up out of hail and high wind rather "
  "than sitting in it."),
]


# ---------------------------------------------------------------- wider pools
# First pass left 48 pages sharing 30% of their sentences with a 71% worst case,
# because the pools were small enough that pages collided on the same variant.
# Doubling every pool is the only honest fix: more writing, not cleverer
# rotation.
ROOM_ITEMS += [
 ("East-facing bedrooms",
  "Morning sun arrives early and lands on the bed. Blackout is the usual answer, but a light "
  "filtering fabric on a top-down bottom-up lift keeps the room bright without putting the sunrise "
  "in someone's face."),
 ("Home offices with a screen",
  "Glare on a monitor is a different problem from heat. It needs the light broken up rather than "
  "blocked, which is what a solar screen or a woven wood does without turning the room into a cave."),
 ("Media rooms",
  "The only room where blackout is genuinely non-negotiable. Outside mount, blackout fabric, and "
  "side channels if the room is used in daylight, because the edges are where light gets in."),
 ("Entryways and sidelights",
  "Narrow openings beside a door where privacy matters and light does not. Shutters suit these "
  "because the frame handles an opening that is rarely square."),
 ("Stairwell and landing windows",
  "High and awkward to reach, which makes this the clearest case for motorization. If you would "
  "need a ladder to adjust it, you will stop adjusting it."),
 ("Dining rooms",
  "Used mostly in the evening, so privacy after dark matters more than daytime performance. That "
  "widens the options and lets you choose on how the room should feel."),
 ("Rooms with pets",
  "Cords and slats both take damage. Cordless lift removes the loop, and a fabric shade gives an "
  "animal less to bend than a stack of slats does."),
 ("Windows over a kitchen sink",
  "Steam plus splashes, and usually a reach across a counter. Faux wood or a wipeable fabric, and a "
  "lift you can work one handed."),
 ("Sunrooms",
  "All glass and all heat. Exterior shading does more here than anything mounted inside, and "
  "cellular shades on the remaining glass cut what gets through the rest."),
 ("Guest rooms used a few nights a year",
  "Not the place to spend the budget. Something that closes fully and looks consistent with the "
  "rest of the house is enough."),
 ("Bay and bow windows",
  "Several openings meeting at angles, so the decision is whether to treat them as one run or as "
  "separate windows. Treating them as one line is usually what makes the room look finished."),
 ("Windows behind furniture",
  "If a sofa or a bed sits against the glass, nobody is reaching the lift. Motorization or a "
  "top-down design solves it; a standard cord does not."),
]

PATIO_ITEMS += [
 ("Track guided patio screens",
  "Side tracks hold the fabric so wind cannot lift it out. On an exposed opening this is the "
  "difference between a shade that lasts and one that frays in a season."),
 ("Outdoor roller shades",
  "Straightforward roll-down shade for porches and outdoor rooms, in a range of openness factors "
  "and fabric colours."),
 ("Pergola shades",
  "A pergola gives structure but very little actual shade. Fabric between the beams is what turns "
  "it into somewhere you sit at four in the afternoon."),
 ("Poolside shades",
  "Glare off water is its own problem, and it comes from below as well as above. Openness factor "
  "matters more here than almost anywhere else."),
 ("Shades for outdoor kitchens",
  "Heat from cooking on top of heat from the sun. Shading the space keeps it usable and keeps "
  "surfaces from getting too hot to work on."),
 ("Wind rated hardware",
  "Texas weather is what ends outdoor fabric early. Wind rated systems cost more and are the reason "
  "a shade is still working in year five."),
 ("Outdoor rated shade fabrics",
  "Built for UV and moisture rather than adapted from an interior fabric. An indoor fabric hung "
  "outside fades and weakens, which is why the two are not interchangeable."),
 ("Motorized and scheduled operation",
  "A shade on a schedule is down through the worst of the afternoon whether or not anyone is home "
  "to lower it, which is most of the benefit of exterior shading in practice."),
]

MATERIAL_BODIES += [
 "The choice usually comes down to how a material behaves rather than how it looks. Wood is light "
 "and shows grain but moves with humidity. Faux wood ignores humidity and is heavier, which matters "
 "on a tall panel. Composite sits between them. On the fabric side the weave is doing the work: an "
 "open weave keeps the view and lets heat through, a tight weave cuts heat and closes the view, and "
 "only a blackout liner genuinely darkens a room.",
 "People tend to choose material by look and then discover the constraint. The constraints are "
 "simple. Moisture ends real wood. Panel weight ends tall faux wood installations. Shallow openings "
 "rule out anything but aluminium. A room that has to go dark rules out slats entirely, because "
 "light comes through the gaps no matter what the slats are made of.",
 "Material is really a durability question. Wood lasts indefinitely in a dry room and warps in a wet "
 "one. Faux wood is unbothered by moisture and sags if the panel is too large for it. Aluminium "
 "bends. Outdoor fabric is built for UV in a way indoor fabric is not, which is why the two cannot "
 "be swapped. Matching the material to what the room does to it is most of the job.",
 "There is no best material, only a best match. What decides it is the room: moisture, opening size, "
 "how dark it needs to go, and how often someone will touch it. Those four answers narrow the "
 "options faster than any showroom comparison, and they are what we work through at the "
 "consultation before anyone opens a colour book.",
 "Fabric and slat are two different tools. A slat gives you a tilt, so you get a middle setting "
 "where light comes in but the view in does not. A fabric gives you one decision, made when you "
 "choose the weave. Rooms that need nuance through the day usually want slats. Rooms with one job, "
 "like a bedroom that has to go dark, usually want fabric.",
]

MOTOR_BODIES += [
 "Motorization is worth it in three places and optional everywhere else: windows you would need a "
 "ladder for, banks of windows where you would otherwise operate six things, and exterior shades "
 "that should come down on a schedule. Battery motors avoid new wiring and need recharging. "
 "Hardwired removes that but has to be planned before the wall closes.",
 "The question worth asking is not whether a motor is nice, it is whether the window is one you "
 "currently ignore. High windows, windows behind furniture and exterior shades all get adjusted less "
 "than they should because adjusting them is a chore. A motor turns an ignored window into one that "
 "actually does its job.",
 "Control matters more than the motor. A remote suits a single room, a wall switch suits a window "
 "you always operate from the same spot, and an app or schedule suits anything that should move "
 "without being asked. Sun triggers are the version that matters most on exterior shades.",
 "Retrofit motorization exists, so a treatment already on the wall is not necessarily stuck being "
 "manual. Whether it is worth doing depends on the lift mechanism and the size of the opening, which "
 "is a look-at-it answer rather than a catalogue one.",
 "Ask who services the motor before you buy it. That is the question people skip and the one that "
 "matters in year four. Our four-year service guarantee covers coming out and servicing your "
 "treatments at no cost, motors included.",
 "Wide openings are where motorization stops being a luxury. A heavy shade across a patio door is "
 "genuinely hard to operate by hand, and the harder it is the less often it moves. On a wide opening "
 "the motor is the thing that makes the shade useful rather than decorative.",
]

PROCESS_VARIANTS = [
 PROCESS,
 ("What to expect", [
  ("We come to you",
   "Samples arrive at your house so you can hold them against your own light. There is no charge for "
   "the visit and nothing to sign at the end of it."),
  ("Every opening measured on site",
   "We take the numbers ourselves rather than working from a list. A custom treatment is cut to a "
   "number, and a wrong number is not returnable."),
  ("A quote with the price on it",
   "Written, itemised, and covering installation. The figure you approve is the figure you pay."),
  ("Installed by the same people",
   "Whoever measured fits it. If something does not match the approved measurements we remake it and "
   "reinstall at no cost."),
 ]),
 ("From first call to installed", [
  ("Book a consultation",
   "One call and we arrange a time that suits you, including evenings and weekends where we can."),
  ("Choose against your own light",
   "Fabric that reads warm in a showroom can read grey on a north wall. Choosing at home is the only "
   "way to know what you are getting."),
  ("Measured, ordered, confirmed",
   "Most custom orders arrive within two to four weeks of approval. Motorized treatments can run "
   "longer, and the timeline goes in writing on the quote."),
  ("Fitted and checked",
   "We hang it, operate every treatment with you, and correct anything that is not right before we "
   "leave."),
 ]),
 ("How we work", [
  ("A visit, not a showroom trip",
   "You do not drive anywhere. The samples, the measuring and the quote all happen at your windows."),
  ("The measuring is ours to get right",
   "We measure every opening, check whether it is square, and decide inside or outside mount there "
   "and then. That is why a mis-measure is our problem and not yours."),
  ("No moving numbers",
   "The written quote is the price. We also price match a like-for-like quote from another company, "
   "so there is nothing to haggle over."),
  ("Backed after we leave",
   "Factory defects are covered for life, and our four-year service guarantee covers us coming back "
   "out at no cost if something needs attention."),
 ]),
]

EXTRA_FAQ += [
 ("Do you do evenings or weekends?",
  "Where we can, yes. The consultation happens at your house, so it has to happen when you are "
  "there. Ask when you book and we will find a time."),
 ("Is there a minimum order?",
  "No. Single windows are a normal job. Plenty of customers start with one room and carry on later, "
  "which is also how the ten-treatment free replacement adds up over time."),
 ("What if I only know roughly what I want?",
  "That is the usual starting point and it is what the consultation is for. Describing the problem, "
  "the room gets too hot in the afternoon, the bedroom is too bright, gets you further than naming a "
  "product."),
 ("Will you tell me if I am overspending?",
  "Yes. A guest room used a few nights a year does not need what a west-facing living room needs, "
  "and saying so is part of the job."),
 ("Do you handle arched or angled windows?",
  "Yes. Shaped openings are a frame and mount problem rather than a fabric one, and they are one of "
  "the reasons we measure on site rather than from a list."),
 ("How disruptive is installation?",
  "Most homes are a few hours. We work room by room, clear up behind us, and operate every treatment "
  "with you before leaving."),
 ("Can I see the treatments working before I decide?",
  "Samples come to the consultation, including motorized ones so you can operate them. It is easier "
  "to decide with something in your hand than from a photograph."),
 ("What makes a quote go up after it is given?",
  "Nothing. The approved quote is the amount you pay. If we got a measurement wrong that is ours to "
  "put right, not something that appears on your invoice."),
]


# ---------------------------------------------------------------- intros
# The most-read sentence on every page was the least varied: one fixed hero
# lead on all 48 city pages, one fixed opening paragraph under it, and five
# generic intros shared by 288 product pages, none of which named the product.
# Every entry here puts the product family and the city in the first sentence,
# which is also where Google reads them.
HERO_LEADS = [
 "Custom blinds, shades and shutters, measured and installed in {c} by the team that quotes them. The in-home consultation is free and there is no obligation to order.",
 "Blinds, shades and shutters built to your windows, not trimmed to fit. We measure every {c} opening ourselves and install what we quoted.",
 "From faux wood blinds to plantation shutters and exterior patio shades, {c} homes get measured on site and quoted in writing.",
 "Shopping for blinds or shutters in {c}? Samples come to your door, every window is measured by us, and the price you approve is the price you pay.",
 "Custom window treatments for {c}: blinds, shades, shutters and patio shades, measured in your home and installed by the same team.",
 "We fit blinds, shades and plantation shutters across {c}, and we measure every opening before anything is ordered. The consultation costs nothing.",
 "Blinds, shades and shutters for {c} homes, backed by a written quote, professional installation and a four-year service guarantee.",
 "Your {c} windows get measured by the owner who quotes them. Blinds, shades, shutters and exterior patio shades, made to those numbers.",
 "Custom blinds and shutters without the guesswork: we bring samples to {c}, measure on site and install what we sold you.",
 "Every blind, shade and shutter we install in {c} is cut to measurements we took ourselves, so the fit is ours to guarantee.",
 "{c} homeowners call us for blinds, shades, shutters and patio shades. We answer with a free consultation and a measured, written quote.",
 "Window treatments for {c}, done in the right order: samples first, measurements second, and an install by the team that quoted it.",
]

BODY_INTROS = [
 "Every blind, shade and shutter here starts with an on-site measure. Nothing is cut to a catalogue size and trimmed to fit, which is what causes the light gaps and crooked bottom rails you see on stock product.",
 "Custom blinds and shutters only work if the numbers are right, so we take them ourselves at every {c} opening. A treatment cut to a wrong measurement is not returnable, which is why we never work from a list sent over.",
 "The blinds, shades and shutters we fit in {c} are made to the opening, not adjusted to it. That is the difference you notice at the edges, where stock product leaks light and custom does not.",
 "A shutter that fits was measured by someone who has to stand behind the fit. We measure every {c} window on site, quote from those numbers and install to them.",
 "Window treatments fail at the measuring stage more than anywhere else. Ours are measured at your {c} home by the team that installs them, so an error is ours to remake, not yours to live with.",
 "Blinds and shades bought off a shelf are cut close and shimmed to fit. Everything we install in {c} is built to the window it was measured against, which is why the reveal is even and the rail sits straight.",
]

PC_INTROS = [
 "{p} for {c} homes, measured at the window and installed by the team that quoted them.",
 "If you are pricing {p} in {c}, start with the measuring, because that is where the result is decided. We do it on site, free.",
 "We build {p} to the opening, not to a catalogue size, and we measure every {c} window ourselves before anything is ordered.",
 "{p} done properly in {c}: samples at your door, measurements taken on site, and a written quote that does not move.",
 "The {p} we install around {c} are cut to numbers we took ourselves, so the fit is guaranteed by the people who measured it.",
 "Every set of {p} we fit in {c} starts with a free in-home consultation, because fabric and finish read differently in your light than in a showroom.",
 "{p} are a measuring job before they are a style decision. In {c} we take those measurements at your windows and stand behind them.",
 "Buying {p} in {c} should not involve guesswork. We measure, we quote in writing, and the same team installs.",
 "For {p} in {c}, the order of operations matters: consultation first, on-site measurements second, then an install by the people who quoted it.",
 "We have been measuring and installing {p} across {c} and the surrounding area, and every job carries the same written quote and four-year service guarantee.",
]
