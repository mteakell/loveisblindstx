"""Three long-form articles, November 2026.

Picked for demand the site had no page for (Ubersuggest, US, Nov 2 2026):
  outdoor shades for porch           8,100/mo (14,800 in June), SD 18
  plantation shutters with curtains  1,300/mo, SD 13
  what color blinds should I get     volume to confirm before it publishes (Nov 8)
The ranking pages for all three were thin franchise blogs and UK/AU sites
with stock photos and nothing Texas-specific, so each article leads with a
direct answer, covers the sub-questions those pages skip, and uses only
real Love Is Blinds installs from images/lib, each looked at before its alt
and caption were written.

Drafts went through an adversarial review (a separate critic pass per
article: search intent coverage against the live SERP, sourcing, voice)
before this version.

Rules: claims about Love Is Blinds trace to the site (guarantees, written
quote, same team measures and installs, remake against approved
measurements, exterior shade options the product page already lists). No
prices, no em dashes, no "honest", no X-not-Y.

Queued through data/post-queue.json and published by the daily Action.
Run: python3 build/articles_nov.py   (rerun-safe; only rewrites unpublished)
"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import newposts as NP
from newposts import li, sec
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

e = lambda s: html.escape(s or "", quote=True)
L = "/images/lib/"


def p(*t):
    return "".join(f"<p>{x}</p>" for x in t)


def fig(stem, alt, caption):
    v = f"/images/lib/r/{{w}}/{stem}.webp"
    srcset = ", ".join(f"{v.format(w=w)} {w}w" for w in (400, 800, 1600))
    return (f'<figure class="post-figure"><img src="{v.format(w=800)}" data-alt-final '
            f'alt="{e(alt)}" loading="lazy" width="800" height="600" srcset="{srcset}" '
            f'sizes="(max-width: 760px) 100vw, 740px"><figcaption>{caption}</figcaption></figure>')


POSTS = []


def post(**kw):
    POSTS.append(kw)


# ---------------------------------------------------------------------------
post(
 slug="outdoor-shades-for-porches-texas",
 date="2026-11-04",
 title="Outdoor Shades for Porches in Texas: Types, Fabric and Wind",
 desc="Which porch shades block Texas afternoon sun, hold up to wind and keep the view: types, fabrics "
      "and options compared, plus what to ask at a consultation.",
 hero="exterior-patio-shades-exterior-patio-shades-002-jpg",
 hero_alt="Covered lakeside porch with a wood ceiling and a dark exterior shade lowered over one "
          "opening at sunset",
 body=
 p("<strong>Short answer:</strong> for most Texas porches, the best outdoor shades are exterior solar "
   "screen shades on the west and south openings, track-guided if the porch catches wind and "
   "motorized if the openings are wide. They stop the low afternoon sun that slides in under the "
   "porch roof, keep the view, and roll up out of the weather when you are not using them.")
 + sec("Why a covered porch still gets hot",
   p("A porch roof blocks the high midday sun. By mid-afternoon the sun is low enough to shine "
     "sideways under the edge of the roof, straight onto the chairs, the table and the people in them. "
     "In a DFW, Waco or Austin summer, that is also the hottest part of the day, so the porch is least "
     "usable exactly when you get home.",
     "A porch shade is a vertical panel of outdoor fabric hanging from the top of the opening. It "
     "catches that sideways sun before it reaches the seating area, the same way shading a window from "
     "outside stops heat before it gets into the room."),
   fig("exterior-patio-shades-exterior-patio-shades-023-jpg",
       "Exterior shade lowered across a wide opening on a covered patio with limestone walls, the "
       "pool and yard visible through the weave",
       "An exterior shade lowered on a covered patio with limestone walls. The weave cuts the sun "
       "while the pool and yard stay in view."))
 + sec("Types of outdoor porch shades",
   li("<strong>Store-bought roll-up shades:</strong> bamboo, reed or PVC panels in standard sizes, "
      "raised with a cord or by hand. Inexpensive and easy to hang, but sized to a label rather than "
      "your opening, and they swing freely in wind.",
      "<strong>Outdoor curtains:</strong> fabric panels on a rod or cable. Soft and decorative, with "
      "gaps at the edges and plenty of movement in a breeze.",
      "<strong>Awnings:</strong> a sloped cover that projects out from the house. Good overhead shade, "
      "but little help against the low, sideways afternoon sun a porch actually struggles with.",
      "<strong>Custom exterior solar screen shades:</strong> a vertical screen fabric built to each "
      "opening, on a roller with a housing at the top. This is what we install, manual or motorized, "
      "with track-guided options for windy sites."),
   p("Exterior solar screen shades suit most Texas porches because they work on the vertical, low-sun "
     "problem, keep the view through the weave, and retract into their housing when the porch is open."))
 + sec("Which sides to shade first",
   li("<strong>West:</strong> almost always first. It takes the late-day sun that makes a porch hard to "
      "use from about four o'clock on in summer.",
      "<strong>South:</strong> usually second. The roof blocks much of the high summer sun here, but "
      "spring and fall sun comes in lower and reaches further under the roof.",
      "<strong>East:</strong> morning sun. Comfortable on most porches, worth shading if you eat "
      "breakfast out there or it faces a close neighbor.",
      "<strong>North:</strong> rarely needs sun control. Shade it for privacy or wind, if at all."),
   p("Many porches only need two of their open sides shaded. Shading every opening costs more and "
     "closes the porch in more than most people want, so start with the sides that drive the heat."))
 + sec("Front porch vs back porch shades",
   p("A <strong>back porch</strong> is usually about afternoon heat, the view of the yard or pool, and "
     "evenings outside. Weave openness and the west side matter most, and bugs come up more often.",
     "A <strong>front porch</strong> is about privacy from the street, glare at the front door, and how "
     "the house looks from the curb. Here the fabric and housing colors matter as much as the weave, "
     "and in many Texas neighborhoods the HOA will review the change. Retractable shades tend to be "
     "easier to approve, because the house looks unchanged whenever they are rolled up. A request with "
     "the product photo, colors, mounting location and dimensions moves fastest; see "
     "<a href=\"/exterior-shades-hoa-rules-texas\">exterior shades and HOA rules</a>."),
   fig("exterior-patio-shades-exterior-patio-shades-046-jpg",
       "Stone house seen from the yard with tan exterior shades lowered across its porch openings",
       "Seen from the yard: tan shades lowered across the porch openings of a stone house, colored to "
       "blend with the stone and trim."))
 + sec("How open should the weave be?",
   p("Outdoor shade fabric is rated by openness: the share of the weave that is open space. A tighter "
     "weave blocks more sun and heat and gives more daytime privacy, with a softer view. A more open "
     "weave keeps more of the view and the breeze and still cuts glare. West-facing porches usually "
     "want a tighter weave than north-facing ones.",
     "Color changes the view too. From the shaded side, darker fabrics are easier to see through "
     "because they bounce less light back toward your eyes, while lighter fabrics glow in direct sun.",
     "After dark the situation reverses: with the porch lights on, people outside can see in through "
     "any screen weave. If the porch faces a street or a close neighbor, plan for that. Our guide to "
     "<a href=\"/how-to-choose-patio-shade-openness-factor\">patio shade openness</a> goes deeper on "
     "picking the number."),
   fig("exterior-patio-shades-exterior-patio-shades-037-jpg",
       "Cedar-framed porch with exterior shades lowered partway over two openings, looking out over a "
       "deck to the horizon",
       "Shades lowered partway on a cedar-framed porch, with the horizon still in view."))
 + sec("Retractable, track-guided and motorized: what the terms mean",
   li("<strong>Retractable:</strong> the shade rolls up into a housing at the top of the opening when "
      "you are not using it, so the fabric spends storms rolled up and protected.",
      "<strong>Track-guided:</strong> the fabric's edges run inside side channels. Wind pushes against "
      "a panel held at both sides, and the channels close the edge gaps where light and insects get "
      "past a free-hanging shade.",
      "<strong>Motorized:</strong> remote, wall switch, app or schedule control. Shades on wide porch "
      "openings are heavy, and a motor makes raising them a one-second job when the weather turns.",
      "<strong>Manual:</strong> a sensible choice for smaller openings that are easy to reach."),
   p("Raise exterior shades in high wind, whatever the system. Motorized versions can use a wind sensor "
     "that raises the shade when gusts pick up, whether or not anyone is home. More in "
     "<a href=\"/wind-rated-patio-shades-texas\">patio shades and Texas wind</a>."),
   fig("exterior-patio-shades-exterior-patio-shades-025-jpg",
       "Exterior shades rolled up into slim housings along the header of a covered porch with brick "
       "columns and a wood ceiling",
       "Shades rolled up into slim housings along the porch header. Retracted, the porch is fully open "
       "to the yard."))
 + sec("Bugs, rain, cleaning and lifespan",
   p("<strong>Bugs:</strong> deployed shades cut down on insects, and track-guided systems keep out "
     "more because the edges are closed. A screened room is still the stronger answer for heavy "
     "mosquitoes at dusk, and some homes use both. We compare them in "
     "<a href=\"/screened-porch-vs-motorized-patio-shades\">screened porch vs motorized patio shades</a>.",
     "<strong>Rain:</strong> screen weave is open, so wind-driven rain blows through it. Shades cut "
     "the sun and wind on a porch; a roof keeps it dry. If a shade gets wet, let it dry in the down "
     "position before rolling it up.",
     "<strong>Cleaning:</strong> rinse the fabric with a hose now and then and use mild soap and water "
     "for spots. Skip pressure washers and harsh cleaners.",
     "<strong>Lifespan:</strong> how long a porch shade lasts depends mostly on how it is used in "
     "weather. Shades rolled up in storms and high wind last far longer than shades left down to flap."))
 + sec("How porch shades mount",
   p("Shades mount to the porch structure: the beam or header across the top of each opening, plus "
     "the posts or columns at the sides for track-guided systems. Real porch openings are rarely "
     "square. Posts lean, headers settle, and two openings on the same porch can measure differently. "
     "That is why every exterior shade we install is measured on site, opening by opening, with "
     "hardware chosen for the span."),
   fig("exterior-patio-shades-exterior-patio-shades-043-jpg",
       "Corner of a stone and cedar porch with exterior shades lowered on three sides",
       "Shades on three sides of a stone-and-cedar porch corner, each built to its own opening."))
 + sec("What to have ready for the consultation",
   li("Which sides get the afternoon sun, and the hours you actually use the porch",
      "Whether there is power near the porch, which decides between battery, solar and hardwired "
      "motors",
      "Your HOA's architectural guidelines, if you have them",
      "How open you want the porch to feel with the shades down"),
   p("The consultation is free, and the team that measures is the team that installs. You get a "
     "written quote with installation included. If a shade does not fit the approved measurements, we "
     "remake it at no cost, and the four-year service guarantee and the manufacturer's limited lifetime "
     "warranty apply outdoors the same as inside. Our teams cover DFW, North Texas, Dallas, Waco, Austin "
     "and Cedar Creek Lake; find yours on the <a href=\"/areas-we-serve\">service areas page</a>.")),
 faqs=[
  ("What kind of outdoor shades are best for a porch?",
   "For most Texas porches, exterior solar screen shades: they stop the low afternoon sun and keep the "
   "view. Track-guided or motorized systems suit wide or windy openings."),
  ("Do porch shades block heat?",
   "Yes. They stop the sun before it reaches the seating area. The biggest gain is on the west side "
   "late in the day, when the sun comes in under the roof."),
  ("Can porch shades stay down in the wind?",
   "Raise exterior shades in high wind. Track-guided systems hold up better, and motorized shades with "
   "a wind sensor can raise themselves."),
  ("Do outdoor porch shades keep rain out?",
   "Not fully. Screen fabric is open, so wind-driven rain blows through. Shades handle sun, glare and "
   "wind; the porch roof handles rain."),
 ],
 related=[("Exterior patio shades in Texas", "/products/exterior-patio-shades"),
          ("How to Choose a Patio Shade Openness Factor", "/how-to-choose-patio-shade-openness-factor"),
          ("Wind-Rated Patio Shades for Texas Weather", "/wind-rated-patio-shades-texas"),
          ("Screened Porch vs Motorized Patio Shades", "/screened-porch-vs-motorized-patio-shades")],
)

# ---------------------------------------------------------------------------
post(
 slug="plantation-shutters-with-curtains",
 date="2026-11-06",
 title="Plantation Shutters With Curtains: How to Pair and Hang Them",
 desc="Can you put curtains over plantation shutters? When it works, how to hang drapery so "
      "the panels open, valances, and colors for white or stained shutters.",
 hero="smart-drapes-smart-drapes-002-jpg",
 hero_alt="Bedroom with white plantation shutters on three windows and floor-length linen drapery "
          "hung high and wide on the largest one",
 body=
 p("<strong>Short answer:</strong> yes, curtains over plantation shutters are one of the most common "
   "ways to finish a room. The one rule is mechanical: the drapery has to leave room for the shutter "
   "panels to swing open and the louvers to tilt. Hang the rod high and wide, and the curtains add "
   "softness, color and height that shutters alone do not.")
 + sec("Why pair them",
   p("Plantation shutters behave like architecture. They join the trim, give the window crisp "
     "horizontal lines, and handle light and privacy every day. In a living room that is often all a "
     "window needs. In a bedroom or a formal room, all those hard lines can feel cool, and drapery "
     "warms them up."),
   li("<strong>Softness:</strong> fabric breaks up the lines of the louvers and the frame.",
      "<strong>Color and pattern:</strong> shutters are usually white or stained, so drapery is where "
      "the room's color comes in.",
      "<strong>Height:</strong> a rod mounted near the ceiling makes the window, and the room, look "
      "taller.",
      "<strong>Darkness:</strong> closed shutters still pass some light at the louver edges. Drapery "
      "drawn over them covers it, which helps in bedrooms.",
      "<strong>Heat:</strong> lined drapery drawn over shutters adds one more layer between a "
      "west-facing window and the room on summer afternoons.",
      "<strong>Sound:</strong> fabric softens echo in rooms with hard floors and high ceilings."))
 + sec("How to hang curtains with plantation shutters",
   p("Shutter panels are hinged and swing into the room. When they are open, they fold flat beside "
     "the window frame. Curtains hung tight to the frame land right where the panels need to go, so "
     "the shutters end up staying closed. Work through it in this order:"),
   "<ol>"
   "<li><strong>Shutters first.</strong> Know where the panels swing and how wide they are when "
   "folded open before choosing the rod.</li>"
   "<li><strong>Rod height.</strong> Mount the rod well above the window frame, often closer to the "
   "ceiling than to the top of the trim.</li>"
   "<li><strong>Rod width.</strong> Extend the rod past the trim far enough that the stacked "
   "curtains rest on the wall beyond the opened shutter panels. A common rule of thumb is 8 to 12 "
   "inches past the trim on each side, more where the shutter panels are wide.</li>"
   "<li><strong>Bracket projection.</strong> Choose brackets that hold the rod far enough off the "
   "wall for the fabric to hang in front of the shutter frame and any tilt rod.</li>"
   "<li><strong>Length.</strong> Decide how the curtains meet the floor (below).</li>"
   "</ol>",
   fig("smart-drapes-smart-drapes-010-jpg",
       "Bedroom with sheer drapery across a large window and white plantation shutters on two smaller "
       "side windows",
       "Sheer drapery on the large window, shutters on the side windows. Each opening gets the "
       "treatment that suits it, and the white ties the room together."))
 + sec("Curtain length",
   li("<strong>Skimming the floor:</strong> the cleanest look and the easiest to live with. A good "
      "default for Texas homes with tile, wood or concrete floors.",
      "<strong>A slight break:</strong> an inch or so of fabric resting on the floor. Softer, and "
      "forgiving if the floor is not perfectly level.",
      "<strong>Puddled:</strong> several inches pooled on the floor. Formal and dramatic, best in rooms "
      "with little foot traffic and no pets."))
 + sec("Stationary panels or working drapery",
   p("<strong>Stationary side panels</strong> frame the window and never close. They are the simplest "
     "pairing, since the shutters handle light and privacy and the panels only need to look good. They "
     "also take less fabric. If a panel crowds the shutter hinge, a tieback or a holdback mounted on "
     "the wall pulls it clear.",
     "<strong>Working drapery</strong> draws across the whole window, over the closed shutters. It "
     "suits bedrooms that need more darkness and rooms where you want a softer look at night. It needs "
     "a full-width rod and enough stacking room on each side to clear the shutter panels. On wide "
     "windows, drapery can also be motorized on a track and drawn by remote or schedule. More in "
     "<a href=\"/what-is-custom-drapery\">what custom drapery is</a>."))
 + sec("Valances and cornices over plantation shutters",
   p("A valance is a short fabric treatment across the top of the window; a cornice is a firmer, "
     "box-like version, usually upholstered. Either can finish the top of a shuttered window and hide "
     "the rod.",
     "Mount it high enough that it clears the top of the shutter panels and the louvers can tilt fully "
     "open without hitting it. Coordinate the valance with the drapery, if there is any, rather than "
     "the shutters. Keep it simple: a tailored valance or a clean cornice looks current, while heavy "
     "swags and stacked layers are what date a shuttered room."))
 + sec("Choosing curtain colors for your shutters",
   li("<strong>White shutters:</strong> ivory, linen and soft neutrals look calm. Match the white "
      "family: warm white shutters sit best with warm, creamy fabrics, and bright cool white with "
      "crisper ones.",
      "<strong>Stained shutters:</strong> warm colors and richer textures echo the wood. Deep greens, "
      "rust and camel all work against a mid-tone stain.",
      "<strong>Patterns:</strong> shutters are a quiet backdrop, so a patterned fabric can be the "
      "feature without the window looking busy.",
      "<strong>Sheers:</strong> keep the daylight and add movement. A good fit for living rooms where "
      "the shutters already handle privacy."),
   p("Strong Texas afternoon light pushes colors warm, so judge fabric next to the shutters at the "
     "time of day the room gets used. Our guide to <a href=\"/white-or-stained-plantation-shutter-finishes\">"
     "white or stained shutter finishes</a> covers the shutter side of the pairing, and "
     "<a href=\"/real-wood-vs-faux-wood-shutters\">real wood vs faux wood shutters</a> covers which "
     "materials take stain."))
 + sec("When curtains are optional",
   li("Kitchens and full bathrooms, where moisture and cooking are hard on fabric and faux wood "
      "shutters do the job alone. See <a href=\"/shutters-for-bathrooms-moisture-privacy\">shutters "
      "for bathrooms</a>.",
      "Windows beside a door or a tall piece of furniture, where the drapery has nowhere to stack",
      "<a href=\"/cafe-shutters-half-height-charm\">Cafe shutters</a>, which usually look best with a "
      "simple valance or side panels and nothing over the open top",
      "Shutters on <a href=\"/solutions/french-doors\">French doors</a> or "
      "<a href=\"/plantation-shutters-for-sliding-glass-doors\">sliding doors</a>: possible, but only "
      "with a rod wide enough that the drapery stacks clear of the doors",
      "Rooms where the trim and the view are the feature"),
   fig("shutters-shutters-099-jpg",
       "Living room with white plantation shutters on every window and no drapery",
       "Shutters alone on every window of this living room. The trim and louvers carry the look on "
       "their own."))
 + sec("Planning both together",
   p("We install plantation shutters and custom drapery, so the rod position can be planned around the "
     "shutter swing from the start instead of discovered after. The in-home consultation is free, we "
     "bring samples to your home, and the quote is written with installation included. See "
     "<a href=\"/what-happens-at-a-free-in-home-consultation\">what happens at a consultation</a>.")),
 faqs=[
  ("Can you put curtains over plantation shutters?",
   "Yes. Hang the rod above and wider than the window so the drapery stacks beside the opened shutter "
   "panels, leaving them free to swing."),
  ("How far past the window should the curtain rod go with shutters?",
   "Far enough that the stacked curtains clear the opened shutter panels. A common rule of thumb is 8 "
   "to 12 inches past the trim on each side, more for wide panels."),
  ("Can you put a valance over plantation shutters?",
   "Yes. Mount it high enough that the louvers can tilt fully open, and coordinate it with any drapery "
   "in the room."),
  ("What color curtains go with white shutters?",
   "Ivory, linen and soft neutrals in the same warm or cool white family look calm. Patterns work too, "
   "because the shutters give a quiet backdrop."),
  ("Do curtains with shutters help a bedroom get darker?",
   "Yes. Closed shutters pass some light at the louver edges, and drapery drawn over them covers it."),
 ],
 related=[("What Is Custom Drapery?", "/what-is-custom-drapery"),
          ("White or Stained? Choosing Plantation Shutter Finishes", "/white-or-stained-plantation-shutter-finishes"),
          ("Plantation shutters", "/products/plantation-shutters"),
          ("Real Wood vs Faux Wood Shutters", "/real-wood-vs-faux-wood-shutters")],
)

# ---------------------------------------------------------------------------
post(
 slug="what-color-blinds-should-i-get",
 date="2026-11-08",
 title="What Color Blinds Should I Get? Trim, Walls, Light or Dark",
 desc="What color blinds should you get? Match the trim, mind the undertones, and see what light "
      "and dark colors do to heat, glare and the view in Texas sun.",
 hero="roller-shades-roller-shades-237-jpg",
 hero_alt="Bronze solar roller shades lowered across a long wall of living room windows, with the lawn "
          "and pool visible through the weave",
 body=
 p("<strong>Short answer:</strong> if you are unsure, choose white or off-white matched to your "
   "window trim. It is the safest choice for blinds and shutters, it suits almost any wall color, and "
   "it is what a future buyer expects. Move away from white for a reason: a darker solar shade gives a "
   "clearer view out and calms glare, a stained wood brings warmth, and a contrasting color makes the "
   "window a feature. Then check the sample in the room's own light before you order.")
 + sec("Should blinds match the trim or the walls?",
   p("There are three ways to do it, and all three work in the right room."),
   li("<strong>Match the trim.</strong> The most common choice. Blinds and shutters mounted inside the "
      "frame read as part of the window, so the walls, floors and furniture carry the room.",
      "<strong>Go tone-on-tone with the wall.</strong> A color a shade or two lighter or darker than the "
      "wall. This suits fabric shades and rooms with colored walls, where white would stand out.",
      "<strong>Contrast on purpose.</strong> Dark against white walls, or light against dark walls. "
      "The window becomes a feature, which works when the window is worth looking at."),
   p("Whichever you choose, mind the undertone. Whites differ: some lean warm and creamy, others cool "
     "and blue. A cool white blind next to a creamy trim looks dingy, and the reverse looks yellow. "
     "Match warm to warm and cool to cool, and hold the sample against the actual trim paint, since "
     "two whites can look identical on their own and different side by side."),
   fig("roller-shades-roller-shades-154-jpg",
       "Cream roller shade on a bedroom window with charcoal walls and black window frames",
       "Contrast on purpose: a cream roller shade against charcoal bedroom walls."))
 + sec("Popular blind colors and when each one works",
   li("<strong>White:</strong> the default. Matches most painted trim, brightens the room, easy to "
      "live with.",
      "<strong>Off-white, cream and ivory:</strong> softer than white and better with warm, creamy trim "
      "and beige or greige walls.",
      "<strong>Gray:</strong> suits cool-toned rooms and gray walls. Pick a gray that leans the same way "
      "as the wall.",
      "<strong>Beige and greige:</strong> blends with warm neutral walls and wood floors without "
      "drawing attention.",
      "<strong>Black and charcoal:</strong> a modern look that lines up with black window frames.",
      "<strong>Bronze and brown:</strong> warm, calm, and often the best color for seeing out through a "
      "solar shade.",
      "<strong>Wood tones and natural weaves:</strong> warmth and texture from real wood, stain or "
      "woven materials."),
   fig("roller-shades-roller-shades-003-jpg",
       "Charcoal roller shade mounted above a row of black-framed windows in a white room",
       "A charcoal roller shade above black-framed windows. Matched to the frames, it all but "
       "disappears when raised."))
 + sec("What light and dark colors actually do",
   "<table><thead><tr><th>Effect</th><th>Lighter colors</th><th>Darker colors</th></tr></thead><tbody>"
   "<tr><td>Heat</td><td>Reflect more of the sun's energy back out through the glass</td>"
   "<td>Absorb more of it at the window and give some of that heat to the room</td></tr>"
   "<tr><td>View through solar fabric</td><td>Hazier, because the weave lights up in sun</td>"
   "<td>Clearer, because the weave reflects less light toward your eyes</td></tr>"
   "<tr><td>Glare</td><td>The fabric glows on bright days</td>"
   "<td>Calmer, which helps rooms with screens</td></tr>"
   "<tr><td>Room feel</td><td>Small rooms feel larger and brighter</td>"
   "<td>Large rooms feel cozier</td></tr>"
   "<tr><td>Dust and marks</td><td>Hide dust, show smudges</td><td>Show dust, hide smudges</td></tr>"
   "</tbody></table>",
   p("For solar shades, the view difference is often big enough to decide the color by itself. In the "
     "living room at the top of this page, bronze solar shades keep the lawn and pool in sight with the "
     "shades down. A white fabric at the same <a href=\"/roller-shade-openness-factor-explained\">"
     "openness</a> would look like a bright wall in the afternoon sun. If heat matters more than the "
     "view, a lighter fabric is the better trade.",
     "For blackout, color plays a small part in how dark the room gets. The fabric's opacity does most "
     "of the work, and the gaps around the edges let in more light than any face color. More on that in "
     "<a href=\"/room-darkening-vs-blackout-whats-the-difference\">room-darkening vs blackout</a>."))
 + sec("Floors, wood tones and stains",
   p("Real wood blinds and shutters take a true stain, so they can match floors, cabinets or doors, or "
     "contrast with them deliberately. Faux wood cannot take a real stain, which is one reason painted "
     "white faux wood is the usual pick for kitchens and bathrooms. Our guide to "
     "<a href=\"/faux-wood-vs-real-wood-blinds\">faux wood vs real wood blinds</a> covers where each "
     "belongs. A stained window becomes a warm feature, and in strong afternoon light a mid-tone stain "
     "can look redder than it did in the sample, so look at it at the window."),
   fig("shutters-shutters-077-jpg",
       "Stained wood plantation shutters set into deep green paneled walls",
       "Stained wood shutters in deep green paneling. The stain makes the windows a warm feature."),
   p("Natural woven woods sit between painted and stained. They bring a mid-tone and texture without a "
     "strong color, and they get along with nearly any wall and floor."),
   fig("woven-wood-shades-woven-wood-shades-031-jpg",
       "Natural woven wood shades on two windows of a bedroom with white walls",
       "Natural woven wood shades in a white bedroom: texture and a mid-tone without a strong color."))
 + sec("How your house looks from the street",
   p("Blinds and shutters are the same color on both sides, so the color you pick for the room is the "
     "color the street sees. Fabric shades show their back to the street, and that side can look "
     "different from the room side. If a front room calls for a bold or dark color, look at a sample "
     "from outside before deciding, and keep the street-facing windows consistent so the front of the "
     "house reads as one design. Some neighborhood covenants also address how window coverings look "
     "from the street, so check yours."))
 + sec("Color by room",
   li("<strong>West-facing living rooms:</strong> a mid to dark solar fabric for the view and the glare, "
      "or a lighter one if heat is the bigger problem.",
      "<strong>Bedrooms:</strong> any color you like on a blackout or room-darkening fabric.",
      "<strong>Media rooms:</strong> a darker color facing the room keeps reflected light off the screen. "
      "See <a href=\"/best-window-treatments-for-media-rooms\">window treatments for media rooms</a>.",
      "<strong>Kitchens and bathrooms:</strong> white or light colors in moisture-tolerant materials, "
      "which wipe clean and suit painted cabinets.",
      "<strong>Rooms with drapery:</strong> keep the blinds or shades quiet and let the "
      "<a href=\"/what-is-custom-drapery\">drapery</a> bring the color."),
   fig("blinds-blinds-011-jpg",
       "Dark wood blinds on two windows framed by ivory drapery panels on a black rod",
       "Dark wood blinds framed by ivory drapery panels on a black rod."))
 + sec("How to test colors before you order",
   li("Hold each sample at the window, at the time of day the room gets used.",
      "Look at it against both the trim and the wall.",
      "Compare a light and a dark version of the same fabric side by side.",
      "Look at front-room samples from the street at dusk.",
      "Make final calls in person; screens shift colors."),
   p("We bring samples to your home at the free <a href=\"/what-happens-at-a-free-in-home-consultation\">"
     "in-home consultation</a> for this reason. A color under store lighting or on a phone is a "
     "different color in your west-facing room at five o'clock."))
 + sec("Colors that age well",
   p("White and soft neutrals stay in style longest and suit a future buyer, which is why they are the "
     "default for blinds and shutters. If you want a bold color, put it in drapery, which is easier to "
     "change than a house full of shades. Most fabrics fade over years of direct sun and saturated "
     "colors show it first, so keep the strongest colors off the hottest west windows.")),
 faqs=[
  ("What color blinds should I get if I'm not sure?",
   "White or off-white matched to your window trim. It suits almost any wall color and is the safest "
   "choice for resale."),
  ("Should blinds be lighter or darker than the walls?",
   "Either works. Matching the trim is most common; a color a shade lighter or darker than the wall "
   "blends in; strong contrast makes the window a feature."),
  ("What color blinds go with gray or beige walls?",
   "With gray walls, white or a gray with the same cool undertone. With beige or greige walls, "
   "off-white, cream or a warm beige."),
  ("Do dark shades make a room hotter?",
   "A dark fabric absorbs more sun at the window and passes some of that heat into the room. A lighter "
   "fabric reflects more of it back out."),
  ("Do dark solar shades give a better view?",
   "Yes. Dark weaves reflect less light toward your eyes, so the view through them is clearer than "
   "through a light fabric at the same openness."),
 ],
 related=[("Roller Shade Openness Factors Explained", "/roller-shade-openness-factor-explained"),
          ("White or Stained? Choosing Plantation Shutter Finishes", "/white-or-stained-plantation-shutter-finishes"),
          ("Faux Wood vs Real Wood Blinds", "/faux-wood-vs-real-wood-blinds"),
          ("Solar Shades vs Blackout Shades", "/solar-shades-vs-blackout-shades")],
)


BANNED = [(re.compile("—"), "em dash"), (re.compile(r"\bhonest", re.I), "honest"),
          (re.compile(r"\bnot just\b", re.I), "not just"),
          (re.compile(r"\w, not (a |an |the )?\w+[.,]"), "X, not Y")]


def lint(ps):
    bad = []
    for ps_ in ps:
        txt = re.sub(r"<[^>]+>", " ", ps_["body"] + " ".join(q + a for q, a in ps_["faqs"])
                     + ps_["title"] + ps_["desc"])
        for rx, why in BANNED:
            for m in rx.finditer(txt):
                bad.append(f"{ps_['slug']}: {why}: ...{txt[max(0, m.start()-40):m.end()+20]}")
        if len(ps_["desc"]) > 155:
            bad.append(f"{ps_['slug']}: desc {len(ps_['desc'])} chars")
    return bad


def words(ps_):
    return len(re.sub(r"<[^>]+>", " ", ps_["body"]).split())


def render(ps_):
    hero = L + ps_["hero"] + ".webp"
    out = NP.render({"slug": ps_["slug"], "title": ps_["title"], "desc": ps_["desc"],
                     "published": ps_["date"]}, ps_["body"], ps_["faqs"], hero, ps_["related"])
    v = f"/images/lib/r/{{w}}/{ps_['hero']}.webp"
    srcset = ", ".join(f"{v.format(w=w)} {w}w" for w in (400, 800, 1600))
    out = out.replace(
        f'<img src="{hero}" alt="{e(ps_["title"])}" width="1200" height="800" fetchpriority="high">',
        f'<img src="{hero}" data-alt-final alt="{e(ps_["hero_alt"])}" width="1200" height="800" '
        f'fetchpriority="high" srcset="{srcset}, {hero} 2000w" sizes="(max-width: 760px) 100vw, 740px">', 1)
    assert ps_["hero_alt"] in html.unescape(out), "hero alt not applied"
    return out


def main(preview_only=False):
    bad = lint(POSTS)
    if bad:
        print("\n".join(bad))
        sys.exit("articles_nov: lint failed")
    for ps_ in POSTS:
        print(f"{ps_['date']}  {ps_['slug']}  {words(ps_)} words")
    if preview_only:
        return
    q = json.load(open("data/post-queue.json"))
    by = {x["slug"]: x for x in q}
    for ps_ in POSTS:
        entry = by.get(ps_["slug"])
        if entry and entry.get("published"):
            continue                      # live: never rewrite a published post from here
        open(f"data/queued-posts/{ps_['slug']}.html", "w").write(render(ps_))
        rec = {"slug": ps_["slug"], "title": ps_["title"], "desc": ps_["desc"], "date": ps_["date"],
               "img": L + ps_["hero"] + ".webp", "published": False}
        if entry:
            entry.update(rec)
        else:
            q.append(rec)
    json.dump(q, open("data/post-queue.json", "w"), indent=1)


if __name__ == "__main__":
    main(preview_only="--preview" in sys.argv)
