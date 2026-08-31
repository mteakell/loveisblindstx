"""Rotating copy pools so no two city pages read the same way.

Each product gets several genuinely different angles on the same subject rather
than synonym-swapped versions of one paragraph: heat, privacy, longevity, fit
and cost are separate arguments, not rewordings. A deterministic hash of the
city slug picks which combination a page gets, so the assignment is stable
across rebuilds and neighbouring cities do not collide.

This lowers literal duplication. It does not manufacture information gain, which
only real job data from the owners can do.
"""

# ---- opening angles, shared shape but different argument -------------------
INTRO = [
 "Every opening gets measured on site. Nothing here is cut to a catalogue size and trimmed to fit, "
 "which is what causes the light gaps and the crooked bottom rails you see on stock treatments.",
 "The consultation happens in your home, with samples held against your own light, because a fabric "
 "that looks right in a showroom often looks wrong on a west wall at four in the afternoon.",
 "We quote from measurements we take ourselves. That is deliberate: a custom treatment is cut to a "
 "number, and if the number is wrong it is a remake rather than a return.",
 "The person who measures your windows is the person who installs them. There is no handover to a "
 "subcontracted crew who has never seen the job.",
 "Most of what goes wrong with window treatments is decided before anything is ordered: the wrong "
 "material for the room, or a mount the opening was never going to take.",
]

# ---- why this product, several distinct arguments per family ---------------
WHY = {
"blinds": [
 ("Material outlives style",
  "The slat style is a look. The material is what decides whether the blind still works in three "
  "years. Real wood moves with humidity, faux wood and composite do not, and vinyl gives up first "
  "on a wall that takes afternoon sun."),
 ("Slat width changes the room",
  "Wider slats give a cleaner view out and suit larger windows. Narrower slats suit small or period "
  "openings and stack tighter at the top. It is a proportion decision more than a taste one."),
 ("Where blinds beat shades",
  "A blind tilts. That gives you finer control over light than any fabric shade, because you can "
  "take glare off a screen without losing the view or darkening the room."),
 ("The lift matters more than people expect",
  "Cordless is standard now for child and pet safety, and it changes how a blind feels to use every "
  "day. On a heavy or high window it is the difference between a treatment you adjust and one you "
  "leave permanently up."),
 ("Older homes are rarely square",
  "Frames settle. On most homes past a few years old the width at the top of a window is not the "
  "width at the bottom, which is why we measure in three places and often recommend an outside "
  "mount even where an inside mount would look neater."),
],
"shades": [
 ("Openness is a specification, not a preference",
  "On a solar shade the openness factor decides how much sun you stop and how much view you keep. "
  "It should be chosen per window based on which way it faces, not picked once for a whole house."),
 ("Daytime privacy is not night time privacy",
  "A weave that gives complete privacy at midday goes transparent once it is dark outside and the "
  "lights are on inside. Any window that has to work after dark needs blackout or a layered "
  "treatment, not a tighter solar weave."),
 ("Cellular shades work on heat, not light",
  "The honeycomb traps a layer of air right at the glass, which is where heat actually transfers. "
  "That makes them the answer for a room that gets too hot rather than one that gets too bright."),
 ("Blackout always leaks at the edges",
  "An inside mounted shade leaves a gap at each side by design. Real darkness comes from an outside "
  "mount with generous overlap, side channels, or a drape layered over the shade."),
 ("Fabric choice is a durability decision",
  "Sun degrades fabric. A weave rated for a north window will fade on a west one, and that is the "
  "single biggest factor in how long a shade keeps looking new."),
],
"plantation-shutters": [
 ("Shutters cannot absorb a crooked opening",
  "A shutter is a rigid panel in a frame. Unlike a fabric shade it has no give, so an opening that "
  "is out of square has to be handled by the frame style rather than hidden by the treatment."),
 ("Depth decides what is possible",
  "Every shutter needs clearance for the louvers to rotate without hitting the glass. If the frame "
  "is shallow the answer is a frame that projects, not a different product."),
 ("They are read as part of the house",
  "Shutters stay when you move, so buyers treat them as a fixture rather than a covering. That is "
  "why they usually go in the rooms that show while blinds or shades handle the rest."),
 ("Louver size is a view decision",
  "Wider louvers give more view out when open and a cleaner line when closed. Narrower louvers suit "
  "smaller openings and period properties. It changes the character of the window."),
 ("A divider rail solves the street facing problem",
  "One horizontal rail lets the top and bottom tilt separately, so you can take daylight in high "
  "while keeping privacy at eye level. On a front room it is usually the right call."),
],
"shutters": [
 ("Shutter is a category, not a product",
  "Plantation is the most common style, but a bay window, a door sidelight and a bathroom over a tub "
  "each want something different. The opening usually decides, not taste."),
 ("Specialty shapes are templated, not measured",
  "Arches, circles and angles are taken from a physical template on site rather than from numbers, "
  "which is why they are the one job we would never ask a customer to measure."),
 ("Solid panels do what louvers cannot",
  "No louvers means no light gaps at all. It is a period look and the most light blocking shutter "
  "available, which suits a bedroom in a older home better than a plantation panel."),
 ("Doors and sidelights need their own approach",
  "Narrow glass beside or within a front door takes a slim panel with hardware that clears the "
  "handle and lets the door work normally."),
 ("Material follows the room, not the style",
  "Whichever style you choose, hardwood belongs in dry living areas and composite belongs anywhere "
  "with moisture or hard sun. Getting that wrong is the expensive mistake."),
],
"patio-shades": [
 ("Stop the sun before the glass, not after",
  "An interior blind blocks light that has already come through the window and heated the room. An "
  "exterior shade stops it outside. On a west wall in a Texas summer that is the whole argument."),
 ("Span drives everything",
  "Patio openings are wide. A twenty foot span needs heavier hardware, a bigger tube and usually a "
  "motor, because nobody cranks a shade that size by hand twice a day."),
 ("Wind is a design constraint",
  "Exterior shades should come up when weather turns. That is not a caveat, it is the reason "
  "motorization on a large span is practical rather than luxurious."),
 ("Shading the patio cools the house",
  "Covering the outdoor space also shades the wall and glass behind it, so the rooms on that side "
  "take less heat load. Most people buy for the patio and are surprised by what it does indoors."),
 ("Openness decides comfort more than fabric colour",
  "The weave sets how much sun you stop and how much view you keep. Getting it wrong for the "
  "direction the space faces is the most common regret we hear about on outdoor shades."),
],
"motorized-shades": [
 ("Motorize openings, not houses",
  "It earns its cost per window: the ones you cannot reach, the ones too heavy to work by hand, and "
  "the ones you want on a schedule. In most homes that is three to six, not all of them."),
 ("Scheduling is the feature people keep",
  "App and voice control get demonstrated. Scheduling gets used. Shades that close against the "
  "afternoon sun without anyone thinking about it is what customers say they would not give up."),
 ("Power is a planning decision",
  "Battery retrofits anywhere, hardwiring has to happen before the walls close, and solar suits "
  "windows that get real sun. All three are easy to choose before you order and awkward after."),
 ("Motors outlast the fabric they move",
  "The mechanism is rarely what fails. What matters is who services it, which is the practical "
  "difference between buying motorization locally and buying it online."),
 ("Reach is the honest test",
  "If you can comfortably reach a window every day, a motor is convenience. If you cannot, a manual "
  "treatment ends up permanently up or permanently down, and you have paid for something that does "
  "one thing."),
],
}

# ---- closing angle ---------------------------------------------------------
CLOSE = [
 "Booking a consultation costs nothing and commits you to nothing. You get measurements, samples in "
 "your own light, and a written quote from those measurements.",
 "The fastest way to a real number is to have someone measure. Averages do not help, because your "
 "openings are not average.",
 "We would rather talk you out of something that will not work than sell it and come back to fix it.",
 "Bring a budget range rather than a single figure. It lets us show you where spending more changes "
 "the result and where it genuinely does not.",
 "If you already know what you want, the consultation is short. If you do not, that is what it is for.",
]
