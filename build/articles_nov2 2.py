"""Five long-form articles, second November 2026 batch.

Picked for search demand the site had no page for (Google autocomplete via
Ubersuggest, US, Nov 13 2026; Semrush units were exhausted that day):
  how to clean plantation shutters     188 autocomplete variations; the
                                       plantation shutters product page
                                       already promised this guide
  plantation shutter louver sizes      2.5 vs 3.5 vs 4.5, hidden tilt
  single cell vs double cell shades    "cellular shades vs" family, 94
  zebra shades vs roller shades        "zebra blinds vs" family, 59
  window treatments for black frames   25 variations, no page on the site
Product claims trace to the product pages: hardwood and composite shutters,
louvers 2.5 to 4.5 inches, hidden tilt rods, paint or stain matched to trim;
single- or double-cell honeycombs, double insulates more and costs more,
sheer to blackout, cordless standard, top-down bottom-up; banded/zebra dual
shades with cordless and motorized options. Company claims (free consult,
written quote, same team measures and installs, remake against approved
measurements, four-year service guarantee, manufacturer's limited lifetime
warranty) are the ones every page already states. Every photo is a real
Love Is Blinds install from images/lib, looked at before its alt and
caption were written; captions describe only what the photo shows.

Same rules and lint as build/articles_nov.py. Queued through
data/post-queue.json and published by the daily Action.
Run: python3 build/articles_nov2.py [--preview]
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import articles_nov as A
from articles_nov import p, fig
from newposts import li, sec, sub

POSTS = []


def post(**kw):
    POSTS.append(kw)


CONSULT = ("The consultation is free, and the team that measures is the team that installs. You get a "
           "written quote with installation included, anything that does not fit the approved "
           "measurements is remade at no cost, and every install carries the manufacturer's limited "
           "lifetime warranty plus our four-year service guarantee. Find your local team on the "
           "<a href=\"/areas-we-serve\">service areas page</a>.")


# ---------------------------------------------------------------------------
post(
 slug="how-to-clean-plantation-shutters",
 date="2026-11-16",
 title="How to Clean Plantation Shutters (Wood and Composite)",
 desc="How to clean plantation shutters without damaging the finish: weekly dusting, deep cleaning "
      "wood vs composite, kitchen grease, bathrooms and what to avoid.",
 hero="shutters-shutters-099-jpg",
 hero_alt="Living room with white plantation shutters on every window, louvers tilted open, a "
          "fireplace and a patterned rug",
 body=
 p("<strong>Short answer:</strong> close the louvers flat, dust both sides with a microfiber cloth or "
   "a vacuum brush every week or two, and a few times a year wipe each louver with a cloth that is "
   "barely damp with water and a drop of mild dish soap, then dry it right away. Composite shutters "
   "can take a little more water than wood. Neither should ever be soaked, sprayed directly or "
   "scrubbed with anything abrasive.")
 + sec("What you need",
   li("Two or three microfiber cloths, or a clean cotton sock you can wear over your hand",
      "A vacuum with a soft brush attachment",
      "A small bowl of warm water with a few drops of mild dish soap",
      "A soft, dry towel for drying as you go",
      "A clean paintbrush or makeup brush for the corners where louvers meet the frame"),
   p("Skip ammonia glass cleaners, bleach, scouring pads, magic erasers and anything sold as a "
     "polish. They can dull a painted finish, damage a stained one or leave a film that collects dust "
     "faster. If your shutters came with a care sheet from the manufacturer, it overrides any general "
     "advice, including ours."))
 + sec("Routine dusting, every week or two",
   p("Dust is the main job, and it is quick if you keep up with it. Work from the top of the window "
     "down so dust falls onto areas you have not cleaned yet."),
   li("Close the louvers so they lie flat, pointing down.",
      "Wipe across the faces with a microfiber cloth, or run the vacuum brush over them in long strokes.",
      "Tilt the louvers the other way and repeat on the other side.",
      "Run the cloth along the top of the frame, the divider rail if your shutters have one, and the "
      "tilt rod.",
      "Finish with the window sill, which catches whatever fell."),
   p("A sock over your hand is the fastest tool for this. Pinch each louver between your thumb and "
     "fingers and slide across: one pass cleans the top and bottom at once. On a large living room "
     "with several windows, that turns a long chore into a few minutes per window."),
   fig("shutters-shutters-116-jpg",
       "White plantation shutters across a bay window under a wood plank ceiling, with divider rails "
       "splitting each panel into upper and lower sections",
       "Shutters on a bay window, each panel split by a divider rail. Dust the rail and the frame "
       "along with the louvers."))
 + sec("Deep cleaning, a few times a year",
   p("When dusting no longer brings the finish back, wash the louvers one at a time. Dip a cloth in "
     "the soapy water and wring it until it is only barely damp. Wipe the louver, then follow "
     "immediately with the dry towel. Rinse the cloth often so you are moving dirt off the shutter "
     "instead of spreading it around.",
     "Do one panel completely before starting the next, and check the cloth: when it comes away "
     "clean, you are done. Leave the shutters open afterward so air can move across them while any "
     "last moisture dries."))
 + sec("Wood vs composite: what changes",
   sub("Hardwood shutters",
     p("Wood is the material to be careful with. Water that sits on wood can work into the grain at "
       "edges and joints, where it raises the grain, swells the louver or lifts the finish. Keep the "
       "cloth barely damp and dry each louver as you go. On stained shutters, rub with the grain, and "
       "test any cleaner on the back of a louver first. Never take wood panels down to wash them in a "
       "tub or with a hose.")),
   sub("Composite shutters",
     p("Composite is built for humidity, which is why we recommend it for bathrooms and kitchens, and "
       "it tolerates more water during cleaning. You can use a slightly wetter cloth and a little more "
       "soap on stubborn spots. Still wipe it dry: standing water leaves spots and can collect in the "
       "hardware.")),
   sub("Vinyl and poly shutters",
     p("Many builder-grade shutters are vinyl or a solid poly material. Treat them like composite: "
       "mild soap and water are fine, and wipe them dry. If white vinyl has yellowed, that is usually "
       "the material itself aging in sun, and cleaning will brighten the surface but will not reverse "
       "it.")),
   p("Not sure which you have? Check your paperwork, or call your local team. Our "
     "<a href=\"/real-wood-vs-faux-wood-shutters\">real wood vs faux wood shutters</a> guide covers "
     "how the two materials differ in daily life."),
   fig("shutters-shutters-077-jpg",
       "Three stained plantation shutter panels with divider rails, louvers partly open, set in a "
       "room with dark green paneled walls",
       "Stained shutters in a paneled room. On a stained finish, wipe with the grain and keep "
       "the cloth nearly dry."))
 + sec("Kitchen shutters and grease",
   p("Shutters near a stove pick up a thin film of cooking grease that dust sticks to. Dry dusting "
     "smears it. Use warm water with dish soap, which is made to cut grease, and wipe with a barely "
     "damp cloth, then dry. A second pass with a clean damp cloth removes any soap left behind. A "
     "monthly wipe keeps the film from building up to the point where it needs real effort."),
   fig("shutters-shutters-120-jpg",
       "White plantation shutters on a window above a black farmhouse sink, between white kitchen "
       "cabinets and a gray tile backsplash",
       "Kitchen shutters over the sink. Shutters near the stove and sink get a monthly soapy wipe."))
 + sec("Bathroom shutters",
   p("In a bathroom, moisture is the main problem, along with soap and hairspray residue. "
     "Run the exhaust fan during and after showers, and open the louvers afterward so the shutter "
     "dries along with the room. Wipe the louvers nearest the shower more often than the rest.",
     "Small dark spots that wipe away may be surface mildew. Clean them early: wipe with soapy water, "
     "then with a clean damp cloth, and dry the area well. On composite or vinyl, a diluted white "
     "vinegar solution also works. Spots that come back quickly mean the room needs more "
     "ventilation.",
     "If you are choosing shutters for a bathroom now, our guide to "
     "<a href=\"/shutters-for-bathrooms-moisture-privacy\">shutters for bathrooms</a> covers materials "
     "and placement."))
 + sec("How often to clean plantation shutters",
   li("<strong>Dust:</strong> every week or two in most rooms.",
      "<strong>Kitchens:</strong> a soapy wipe once a month.",
      "<strong>Deep clean:</strong> two to four times a year everywhere else.",
      "<strong>More often</strong> during spring pollen season, during nearby construction, or in a "
      "home on a dirt or gravel road."),
   p("Shutters on west-facing windows show dust sooner in the afternoon, when low sun rakes across "
     "the louvers and lights up every speck."))
 + sec("The back of the panels, the hinges and the glass",
   p("Hinged panels swing open, so a few times a year open them and dust the back of the louvers, "
     "the inside edge of the frame and the window glass behind. Wipe the hinges with a dry cloth while "
     "you are there. If a hinge squeaks or a panel has started to sag or rub, leave the oils on the "
     "shelf and call us; the fix is usually an adjustment."))
 + sec("Mistakes that damage shutters",
   li("Spraying cleaner directly onto the shutter. It runs into joints and hinges. Spray the cloth.",
      "Soaking wood. Water should never stand on or drip from a wood louver.",
      "Pulling louvers one at a time to tilt them. Use the tilt rod, or on hidden-tilt shutters, tilt "
      "one louver gently and let the linkage move the rest.",
      "Using a feather duster as the only tool. It moves dust into the air and back onto the louvers.",
      "Forcing a stiff louver. If louvers will not stay where you put them or are hard to move, the "
      "louver tension probably needs adjusting. On shutters we installed, your local team handles it "
      "under the four-year service guarantee."))
 + sec("When cleaning is not the problem",
   p("Louvers that droop or will not hold their angle, panels that rub the frame or a hinge that has "
     "loosened are not cleaning problems. On shutters we installed, the four-year service guarantee "
     "covers service visits at no cost, so call your local team before forcing anything.",
     "If you are planning shutters for more rooms, " + CONSULT)),
 faqs=[
  ("What is the best way to clean plantation shutters?",
   "Close the louvers and dust both sides with microfiber or a vacuum brush, then a few times a year "
   "wipe each louver with a barely damp, soapy cloth and dry it right away."),
  ("Can I use vinegar on plantation shutters?",
   "A diluted vinegar solution is usually fine on composite, but on wood and stained finishes mild "
   "soap and water is the safer choice. Check the manufacturer's care sheet first."),
  ("How do you keep plantation shutters dust free?",
   "No finish stays dust free, but dusting every week or two with the louvers closed keeps it from "
   "building up. A sock over your hand cleans both sides of a louver in one pass."),
  ("Are plantation shutters hard to clean?",
   "No. They take a few minutes per window to dust, and they hold up to wiping better than fabric "
   "treatments, which need vacuuming or spot cleaning instead."),
 ],
 related=[("Plantation shutters in Texas", "/products/plantation-shutters"),
          ("Real Wood vs Faux Wood Shutters", "/real-wood-vs-faux-wood-shutters"),
          ("Shutters for Bathrooms", "/shutters-for-bathrooms-moisture-privacy"),
          ("White or Stained Shutter Finishes", "/white-or-stained-plantation-shutter-finishes")],
)


# ---------------------------------------------------------------------------
post(
 slug="plantation-shutter-louver-sizes",
 date="2026-11-19",
 title="Plantation Shutter Louver Sizes: 2.5, 3.5 or 4.5 Inch?",
 desc="How to choose plantation shutter louver size: what 2.5, 3.5 and 4.5 inch louvers change in "
      "view, light, style and fit, plus tilt rods and divider rails.",
 hero="shutters-shutters-019-jpg",
 hero_alt="Living room with a wall of white plantation shutters behind a cream sofa, louvers open to "
          "a view of the yard",
 body=
 p("<strong>Short answer:</strong> the three common plantation shutter louver sizes are 2.5, 3.5 and "
   "4.5 inches. Larger louvers mean fewer lines across the window and a wider view when they are "
   "open, and they suit large windows and most modern rooms. Smaller louvers suit small windows, "
   "shallow window frames and traditional rooms. Many homes use one size throughout for a "
   "consistent look, unless window depth forces a smaller louver somewhere.")
 + sec("What louver size measures",
   p("Louver size is the width of each louver across its face, edge to edge. You will also see "
     "in-between sizes such as 3 inch from some shutter makers. A 4.5 inch louver is nearly twice as wide as a 2.5 inch one, so the "
     "same window needs far fewer of them. That changes three things at once: how much you see "
     "through the shutter when it is open, how busy the window looks, and how much depth the shutter "
     "needs to tilt."))
 + sec("The three sizes compared",
   sub("2.5 inch louvers",
     p("The traditional look. More louvers per panel means more horizontal lines, which reads as "
       "classic and detailed. They need the least depth to rotate, so they fit shallow window frames "
       "and windows with cranks or handles close to the glass. On a small window they keep the "
       "proportions right, where a wide louver can look oversized. The tradeoff is more slats to "
       "dust and a narrower view between them when open.")),
   sub("3.5 inch louvers",
     p("The middle option, and the safe choice for a house with a mix of window sizes. It looks "
       "current without reading as oversized on a bedroom or bathroom window, and it fits more "
       "window depths than 4.5 inch louvers.")),
   sub("4.5 inch louvers",
     p("A clean, modern look for living rooms and large windows. "
       "Fewer louvers mean fewer lines across the glass and the widest view when they are open. "
       "Because each louver is wider, it needs more depth to tilt, and it projects further into the "
       "room or toward the glass when open, so it needs the most clearance.")),
   fig("shutters-shutters-162-jpg",
       "Three white shutter panels across a wide dining room window, louvers open to a backyard "
       "fence and sky",
       "Louvers tilted open on a wide dining room window. With the louvers open, the gaps between "
       "them set how much of the yard you see."))
 + sec("Window depth decides more than taste",
   p("Every louver has to rotate inside the opening without hitting the glass, a window crank, a lock "
     "or a handle. On an inside mount, the shutter sits within the window frame, so the frame depth "
     "limits which louver sizes can turn freely. A wide louver in a shallow opening can hit the glass, "
     "a crank or a handle as it tilts open. Each shutter maker publishes the minimum depth for each "
     "louver size, and that chart, measured against your windows, settles the question.",
     "This is why louver size is confirmed at the measure, window by window. If one window cannot "
     "take the size you want, shutter makers handle it with a deeper frame that sets the shutter "
     "forward, or with a smaller louver on that window only. Our guide on "
     "<a href=\"/how-to-measure-for-plantation-shutters\">measuring for plantation shutters</a> shows "
     "what we check."))
 + sec("Light, view and privacy",
   p("Closed, every louver size blocks light about the same way, because the louvers overlap. The "
     "difference shows when they are open. Wider louvers leave wider gaps, so more light and more of "
     "the view come through. Smaller louvers break the view into narrower strips, which some people "
     "prefer in bedrooms and street-facing rooms.",
     "For daytime privacy, tilt the louvers so the room-side edge points up. Someone outside at "
     "ground level sees mostly ceiling, while daylight still bounces in. At night, close them fully.",
     "From the street, larger louvers read as bolder, simpler lines and smaller louvers as a finer "
     "texture, which is one more reason to keep the front of the house consistent."))
 + sec("Hidden tilt or a front tilt rod",
   p("The tilt rod is the vertical bar that moves all the louvers in a panel together. A traditional "
     "front tilt rod sits on the face of the louvers. It is easy to grab and it is part of the "
     "classic shutter look. A hidden tilt system moves the louvers from the back or the side, so the "
     "front of the shutter is uninterrupted. With wide louvers, hidden tilt makes the view through an "
     "open shutter even cleaner.",
     "Both work well. Front rods suit traditional rooms. Hidden tilt suits modern rooms and anyone "
     "who wants the window to read as glass and light. Hidden tilt is available if you want the "
     "cleanest face."))
 + sec("Divider rails",
   p("A divider rail is a horizontal bar across a tall panel. It splits the louvers into an upper "
     "and a lower section that tilt separately: lower louvers closed for privacy, upper ones open for "
     "light. Tall panels often need one for strength as well. Where the window has its own "
     "horizontal rail, the divider rail can be placed to line up with it, so the shutter and the "
     "window read as one design from inside and from the street."),
   fig("shutters-shutters-066-jpg",
       "Two white shutter panels with a divider rail across the middle, louvers tilted open toward "
       "blue sky",
       "Two shutter panels with a divider rail at mid-height, so the upper and lower louvers can be "
       "set separately."))
 + sec("Matching louvers across the house",
   p("From the street, shutters are part of the house's face. Mixed louver sizes on the front windows "
     "show from the curb, so keep one size on every street-facing window even when a back bedroom "
     "could take something different. Inside, keep one size per room for the same reason.",
     "Special shapes follow the same louver as the rest of the room where possible. Arched and "
     "angled tops can be built with a frame that follows the shape of the opening; see <a href=\"/solutions/arched-and-specialty-windows\">arched and specialty windows</a>."),
   fig("shutters-shutters-147-jpg",
       "Great room with arched plantation shutters on two tall windows flanking a white fireplace "
       "and on an arched window above the mantel",
       "Arched shutters on two tall windows and the arched window above the mantel, with one louver "
       "style across the wall."))
 + sec("How to choose in one pass",
   li("Large windows, modern rooms, big views: 4.5 inch, if the depth allows.",
      "A house with mixed window sizes: 3.5 inch throughout.",
      "Small windows, shallow frames, traditional rooms: 2.5 inch.",
      "Any window with a crank, lock or handle near the glass: confirm clearance at the measure.",
      "Want the cleanest view: pair larger louvers with hidden tilt."),
   p("The fastest way to decide is to hold real louver samples up to your own windows, in your own "
     "light. That is what the consultation is for. " + CONSULT)),
 faqs=[
  ("What is the most popular plantation shutter louver size?",
   "For living areas and large windows, 3.5 and 4.5 inch louvers are the usual choice. 2.5 inch "
   "louvers remain common on small windows and in traditional homes."),
  ("Do bigger louvers let in more light?",
   "When open, yes. Wider louvers leave wider gaps, so more light and view come through. Closed, all "
   "sizes block light about the same."),
  ("Can I mix louver sizes in one house?",
   "You can, but keep one size on every street-facing window and one size per room so the house "
   "looks consistent. Mixing is usually done only where window depth requires it."),
  ("Does louver size affect cost?",
   "Material, the number of panels and special shapes usually drive cost more than louver size. Your "
   "written quote shows the price of the options you choose, so you can compare them."),
 ],
 related=[("Plantation shutters in Texas", "/products/plantation-shutters"),
          ("How to Measure for Plantation Shutters", "/how-to-measure-for-plantation-shutters"),
          ("White or Stained Shutter Finishes", "/white-or-stained-plantation-shutter-finishes"),
          ("How Much Do Plantation Shutters Cost in Texas?", "/how-much-do-plantation-shutters-cost-in-texas")],
)


# ---------------------------------------------------------------------------
post(
 slug="single-cell-vs-double-cell-shades",
 date="2026-11-22",
 title="Single Cell vs Double Cell Shades: Is the Extra Cell Worth It?",
 desc="Single cell vs double cell cellular shades: how much more a second cell insulates, when it "
      "earns its cost in Texas homes, and when single cell is enough.",
 hero="honeycomb-shades-honeycomb-shades-025-jpg",
 hero_alt="Dining room with a white cellular shade lowered over a very large picture window and a "
          "second window open to trees",
 body=
 p("<strong>Short answer:</strong> double cell shades insulate better than single cell because they "
   "trap two layers of air instead of one, and they cost more. The second cell earns its cost on "
   "large windows, west and south glass, older single-pane windows and bedrooms where you want the "
   "most darkness and quiet. On double-pane windows in a newer home, or on windows that get little "
   "direct sun, single cell usually does the job.")
 + sec("How cellular shades work",
   p("A cellular shade, also called a honeycomb shade, is folded fabric that forms hollow cells when "
     "you look at it from the side. Each cell holds a pocket of air between the window and the room. "
     "Still air slows heat moving through, so the shade slows summer heat coming in and winter "
     "warmth going out. Our "
     "<a href=\"/are-honeycomb-shades-and-cellular-shades-the-same\">honeycomb vs cellular</a> "
     "explainer covers the naming."))
 + sec("Single cell vs double cell: the difference",
   p("A <strong>single cell</strong> shade has one row of cells. It is lighter, a little slimmer when "
     "raised, and costs less.",
     "A <strong>double cell</strong> shade has two rows of cells, one behind the other, so there are "
     "two air pockets between the glass and the room. It insulates more, blocks a little more sound, "
     "and diffuses light more evenly. It stacks slightly deeper when raised and costs more.",
     "In the same color and pleat size, the two look very similar from the room. The difference is "
     "in how they perform. Some makers also offer triple-cell or cell-in-cell constructions for even "
     "more insulation."),
   fig("honeycomb-shades-honeycomb-shades-014-jpg",
       "Two-story room with cellular shades on three high upper windows above four lower windows "
       "with dark frames",
       "Cellular shades on three high upper windows in a two-story room."))
 + sec("Where the second cell earns its cost",
   li("<strong>West and south windows.</strong> The glass that takes the hardest afternoon sun in a "
      "Texas summer gains the most from the extra layer.",
      "<strong>Large windows and walls of glass.</strong> The bigger the glass, the more heat moves "
      "through it, so better insulation adds up.",
      "<strong>Older single-pane windows.</strong> The window does little insulating on its own, so "
      "the shade does more of the work.",
      "<strong>Bedrooms and nurseries.</strong> With a blackout fabric, a double cell shade makes a "
      "dark room and softens a little more sound than single cell.",
      "<strong>Rooms that are always too hot or too cold.</strong> A bonus room over the garage, or a "
      "room at the end of a long duct run."))
 + sec("Where single cell is enough",
   li("Double-pane or low-E windows in a newer build, especially on north and east walls",
      "Small windows, where the extra cost buys little measurable difference",
      "Rooms where you mostly want soft light and privacy, like a kitchen or a hall",
      "Windows with shallow frames, where the slimmer stack helps an inside mount fit"),
   p("Many homes end up with both: double cell on the big west-facing glass and the bedrooms, single "
     "cell everywhere else. Choosing the same color keeps the windows consistent; ask to see both "
     "constructions side by side."))
 + sec("Cell size",
   p("Cells also come in different widths, measured as the height of each pleat on the face of the "
     "shade. Smaller cells look tailored on small and medium windows and stack tighter when raised. "
     "Larger cells look in scale on tall windows and big glass. Cell size is mainly a look and stack "
     "decision. Larger cells hold slightly more air, but a second cell or an insulating fabric "
     "changes performance more."))
 + sec("Light filtering, room darkening and blackout",
   p("Cell count and opacity are separate choices. Single and double cell shades both come in fabrics "
     "from sheer through light filtering to blackout, and how much light a shade blocks depends far "
     "more on that fabric than on the number of cells. A blackout cellular shade has a lining inside "
     "the cells that stops light through the fabric itself.",
     "Even a blackout fabric can let light in around the edges. On an inside mount, there is a small "
     "gap between the shade and the window frame on each side, and in a dark room that gap shows as "
     "a thin line of light. An outside mount that overlaps the frame closes most of it. Our "
     "<a href=\"/room-darkening-vs-blackout-whats-the-difference\">room darkening vs blackout</a> "
     "guide goes deeper."),
   fig("honeycomb-shades-honeycomb-shades-017-jpg",
       "Three cellular shades lowered on inside-mounted windows, with thin lines of daylight showing "
       "at the edges of each shade",
       "Inside-mounted cellular shades with daylight showing at the edges. An outside mount covers "
       "those gaps in a room that needs full darkness."))
 + sec("Top-down bottom-up and motorization",
   p("Top-down bottom-up operation is available, which lets you lower the shade from the top for "
     "daylight while the bottom stays closed for privacy. Cordless is standard, and honeycomb shades "
     "can be motorized. See "
     "<a href=\"/top-down-bottom-up-shades-explained\">top-down bottom-up shades explained</a>."),
   fig("honeycomb-shades-honeycomb-shades-tdbu-jpg",
       "White cellular shade lowered from the top of a wide bedroom window, covering the lower part "
       "while trees show through the upper glass",
       "A top-down shade lowered from the top: the lower glass stays covered while the trees and sky "
       "stay in view above it."))
 + sec("Noise",
   p("Air pockets soften sound as well as heat, and a double cell shade softens a little more than "
     "single cell. It will not soundproof a room, but in a bedroom on a busy street or under a flight "
     "path the difference is noticeable. Pair it with full drapery for the most effect; see "
     "<a href=\"/whats-the-best-window-treatment-for-noise-reduction\">window treatments for noise "
     "reduction</a>."))
 + sec("Cellular vs other shades",
   p("If you are still deciding whether cellular is the right shade at all, compare it with roller "
     "shades in <a href=\"/cellular-shades-vs-roller-shades\">cellular vs roller shades</a>. Cellular "
     "insulates better. Roller shades have a cleaner profile and offer see-through solar fabrics."))
 + sec("Deciding window by window",
   p("The right answer often differs from one side of the house to the other. At the consultation we "
     "look at which way each window faces, the window type and how you use the room, and spec single "
     "or double cell window by window. " + CONSULT)),
 faqs=[
  ("Are double cell shades worth it?",
   "On west and south glass, large windows, single-pane windows and bedrooms, usually yes. On "
   "double-pane windows facing north or east, single cell is usually enough."),
  ("Do double cell shades block more light?",
   "They diffuse light more evenly and block slightly more, but opacity is mostly set by the fabric. "
   "For darkness, choose a blackout fabric in either construction."),
  ("Are double cell shades noticeably thicker?",
   "Double cell fabric is thicker, so the raised stack is a little taller. On shallow frames, the "
   "measure confirms the inside mount still fits."),
  ("Do cellular shades really lower energy bills?",
   "They slow heat moving through the glass, which helps most on sunny windows in summer. How much "
   "you save depends on your windows, their orientation and your cooling system."),
 ],
 related=[("Honeycomb shades in Texas", "/products/honeycomb-shades"),
          ("Cellular Shades vs Roller Shades", "/cellular-shades-vs-roller-shades"),
          ("Room Darkening vs Blackout", "/room-darkening-vs-blackout-whats-the-difference"),
          ("Window Treatments for West-Facing Windows", "/window-treatments-for-west-facing-windows-texas")],
)


# ---------------------------------------------------------------------------
post(
 slug="zebra-shades-vs-roller-shades",
 date="2026-11-25",
 title="Zebra Shades vs Roller Shades: Which Fits Your Room?",
 desc="Zebra shades vs roller shades compared: how each controls light, privacy and view, how they "
      "look raised and lowered, and which rooms suit each one.",
 hero="banded-shades-banded-shades-004-jpg",
 hero_alt="Corner of a room with white banded zebra shades lowered on six tall windows below a row "
          "of transom windows",
 body=
 p("<strong>Short answer:</strong> choose zebra shades when you want to switch between view and "
   "privacy without raising the shade, in rooms like a street-facing living room or a bedroom that "
   "doubles as an office. Choose roller shades when you want the cleanest look, the widest choice of "
   "fabrics, see-through solar screens or very wide windows. Both are custom-sized, cordless or "
   "motorized, and roll up tight at the top of the window.")
 + sec("What each one is",
   p("A <strong>roller shade</strong> is one continuous piece of fabric that rolls around a tube at "
     "the top of the window. You control light by raising and lowering it. The fabric decides "
     "everything else: a solar screen you can see through, a light-filtering fabric that glows, or a "
     "blackout fabric for sleep.",
     "A <strong>zebra shade</strong>, also called a banded shade (one style of dual shade), is a loop "
     "of fabric with "
     "alternating sheer and solid horizontal stripes, one layer in front of the other. Move the shade "
     "a little and the bands line up so the sheer stripes overlap for a filtered view, or offset so "
     "the solid stripes cover the sheer ones for privacy."),
   fig("banded-shades-banded-shades-013-jpg",
       "Two bedroom windows with white banded shades lowered, daylight showing through the sheer "
       "stripes between the solid ones",
       "Banded shades on two bedroom windows, set with the sheer stripes showing to let daylight "
       "through."))
 + sec("Light and view",
   p("A zebra shade gives you a view through stripes. With the bands aligned, you see outside "
     "through the sheer bands while the solid bands stay in the way. That is enough for daylight and "
     "a sense of the yard, but the view is always interrupted by lines.",
     "A roller shade in a solar screen fabric gives an uninterrupted view through the whole surface, "
     "like a tinted screen. That makes roller shades in a solar fabric a strong pick for a "
     "living room that faces a pool, a lake or a long view. More on fabric choice in "
     "<a href=\"/roller-shade-openness-factor-explained\">roller shade openness explained</a>."),
   fig("roller-shades-roller-shades-237-jpg",
       "Living room with brown see-through roller shades lowered partway on a row of tall windows, "
       "lawn and a pool visible through and below the fabric",
       "Roller shades lowered partway on a wall of windows, with the yard and pool still visible "
       "through the fabric."))
 + sec("Privacy",
   p("Zebra shades are built for switching privacy quickly. Offset the bands and the window closes up "
     "without raising or lowering anything, or you can offset the bands partway so the view in "
     "blurs while some daylight still comes through.",
     "Roller shades are simpler: down is private in a light-filtering or blackout fabric, but a solar "
     "fabric that you can see out of in daylight can also be seen into at night with the lights on. "
     "That is the same reason sheer zebra bands need the solid bands offset after dark; see "
     "<a href=\"/can-you-see-through-zebra-blinds-at-night\">can you see through zebra blinds at "
     "night</a>."))
 + sec("Room darkening",
   p("A roller shade in blackout fabric is the darker option, because it is one solid surface. Even "
     "in a blackout fabric, a zebra shade with its bands closed leaks light at the band seams and "
     "edges, so it darkens a room less completely. For a bedroom that needs real darkness, a blackout "
     "roller shade, or a dual shade with a separate room-darkening layer for night, works better. "
     "Any inside-mounted shade shows thin lines of light at the sides; an outside mount or side "
     "channels close most of that gap."))
 + sec("Cost and energy",
   p("Zebra shades usually cost more than a basic roller shade in the same size, because they carry "
     "two layers of fabric. Specialty roller fabrics and motorization narrow the gap, so compare the "
     "two on your written quote.",
     "Neither is a strong insulator. If cutting heat through the glass is the main goal, a "
     "<a href=\"/products/honeycomb-shades\">cellular shade</a> does that better, and a solar "
     "roller shade on the west windows is the next best way to stop afternoon heat."))
 + sec("How they look",
   p("Raised, both roll up tight at the top of the window. A zebra roll "
     "is a little bulkier because it carries two layers of fabric.",
     "Lowered, a roller shade is a flat, quiet panel that suits minimal and modern rooms and almost "
     "any color scheme. A zebra shade has a visible horizontal pattern that reads as contemporary "
     "and adds texture to plain walls. In a room that already has a lot of pattern, the stripes can "
     "compete."),
   fig("roller-shades-roller-shades-091-jpg",
       "Living room with roller shades raised on one pair of windows and lowered on the other, both "
       "framed by full-length drapery panels",
       "Roller shades under drapery panels, raised on one pair of windows and lowered on the other. "
       "A flat roller shade layers easily under curtains."))
 + sec("Wide windows and sliding doors",
   p("Roller shades handle wide spans well, and two or three shades can sit on aligned brackets and "
     "move together under one control. Zebra shades work on wide doors and windows too, usually split "
     "into two or three shades so each stays a manageable size. See "
     "<a href=\"/how-wide-can-shades-go-coupled-shades\">how wide shades can go</a>."),
   fig("banded-shades-banded-shades-014-jpg",
       "Three white banded shades lowered side by side across a wide glass door",
       "Three banded shades side by side across a wide glass door, with the bands lined up across all "
       "three."))
 + sec("Cleaning and wear",
   p("Roller shades are among the easiest shades to clean: dust or vacuum the flat fabric and spot "
     "clean with a damp cloth. Zebra shades are a loop of two layers, and dust can settle inside. "
     "Vacuum both faces with a soft brush, with the shade fully lowered. Details in our guide to "
     "<a href=\"/how-to-clean-roller-shades-and-solar-screens\">cleaning roller shades</a>."))
 + sec("Which room gets which",
   li("<strong>Street-facing living room or front office:</strong> zebra, for quick privacy changes.",
      "<strong>Room with a view, pool or lake:</strong> roller in a solar screen fabric.",
      "<strong>Bedroom:</strong> roller in blackout, or a dual shade with a room-darkening night layer.",
      "<strong>Kitchen or breakfast nook:</strong> either; roller is easier to wipe down.",
      "<strong>Very wide windows:</strong> roller, or zebra split into sections.",
      "<strong>Modern room that needs texture:</strong> zebra."),
   p("Seeing both fabrics in your own light settles it quickly. " + CONSULT)),
 faqs=[
  ("Are zebra shades better than roller shades?",
   "Neither is better everywhere. Zebra shades switch between view and privacy without raising the "
   "shade. Roller shades give the cleanest look, a full see-through view in solar fabrics, and a "
   "blackout fabric that, with side channels, can make a room fully dark."),
  ("Do zebra shades block light completely?",
   "No. Even blackout zebra fabrics leak some light where the bands meet and at the edges. For the "
   "darkest room, choose a blackout roller shade."),
  ("Are zebra shades out of style?",
   "They remain a common choice in contemporary homes. Their striped look is a style decision, so "
   "they suit some rooms better than others."),
  ("Can zebra and roller shades be motorized?",
   "Yes. Both can be cordless or motorized, controlled by remote, app or schedule."),
 ],
 related=[("Dual and zebra shades in Texas", "/products/dual-shades"),
          ("Roller shades in Texas", "/products/roller-shades"),
          ("Zebra Blinds: Pros and Cons", "/pros-and-cons-of-buying-zebra-blinds-is-it-worth-it"),
          ("Roller Shade Openness Explained", "/roller-shade-openness-factor-explained")],
)


# ---------------------------------------------------------------------------
post(
 slug="window-treatments-for-black-window-frames",
 date="2026-11-28",
 title="Window Treatments for Black Window Frames",
 desc="The best window treatments for black window frames: match the frames or contrast them, how to "
      "mount so the frames stay visible, and which products work.",
 hero="roller-shades-roller-shades-208-jpg",
 hero_alt="Great room with a stone fireplace, wood ceiling and black-framed windows and doors, light "
          "roller shades lowered a short way over the top of the glass",
 body=
 p("<strong>Short answer:</strong> black window frames look best with treatments that either match "
   "them or step out of their way. Matching means charcoal or black shades and hardware that blend "
   "with the frames. Stepping out of the way means light shades, white shutters or drapery mounted so "
   "the black frames show whenever the treatment is open. Most black frames "
   "are a feature you want to show, so cover them only when you need to.")
 + sec("Start with the frames, then the light",
   p("Black windows are a design feature, often the most striking line in the room. Two questions "
     "decide the treatment: should the treatment blend in or contrast, and what does the window "
     "need to do? A west-facing wall of black-framed glass needs sun control in a Texas summer. A "
     "bedroom needs darkness. A front window needs privacy from the street. Pick the product for the "
     "job, then the color and mount for the frames."))
 + sec("Option one: match the frames",
   p("Charcoal and black shades blend with black frames. Raised, a dark roller shade reads as part "
     "of the window header. Lowered, a dark fabric keeps the window reading as one dark shape.",
     "Dark fabrics have a practical advantage too. From inside, a dark solar screen is easier to see "
     "through than a light one, because it bounces less light back toward your eyes. On big windows "
     "with a view, that matters. The tradeoff is heat: a dark fabric absorbs more sun and passes some "
     "of it into the room, so on hot west glass a lighter fabric may be the better choice. We cover "
     "how fabric color affects the view in "
     "<a href=\"/what-color-blinds-should-i-get\">what color blinds should I get</a>.",
     "Check the street side too. Many shades show a white or light back to the street, which "
     "keeps the house uniform from outside whatever color faces the room."),
   fig("roller-shades-roller-shades-027-jpg",
       "Dining room with black-framed glass walls and a tall black-framed door overlooking a lake, "
       "light roller shades lowered partway over the top of the glass",
       "Roller shades stopped partway on black-framed glass, cutting glare at the top while the "
       "lake stays in view below."))
 + sec("Option two: contrast the frames",
   p("White and light treatments against black frames give the crisp, high-contrast look common in "
     "modern farmhouse homes. White plantation shutters are the classic version. Light linen or "
     "cream shades are the softer one.",
     "Closed, shutter panels and lowered shades cover the black frame, so contrast shows most when the "
     "treatment is open: shutter louvers tilted or panels swung back, shades raised. It also works "
     "well when nearby windows or doors stay uncovered, so the black reads clearly in the room."),
   fig("shutters-shutters-love-04-jpg",
       "Sitting area with white plantation shutters on a large window beside black-framed French "
       "doors that open to a covered patio",
       "White shutters on the window next to black-framed French doors. The contrast keeps both "
       "the shutters and the frames visible."))
 + sec("Mounting so the frames stay visible",
   p("Any lowered shade covers the black frame and its grids. Mount position decides what you see "
     "around it and what you see when it is raised.",
     "An <strong>inside mount</strong> fits the treatment within the window opening. Lowered, it "
     "leaves the casing and jambs around the opening in view, which keeps a black outline only if "
     "that trim is painted black. Raised, the roll sits inside the top of the opening and covers a "
     "strip of the frame.",
     "An <strong>outside mount</strong> sits on the wall above and overlaps the opening. Mounted "
     "high and wide enough, a raised shade clears the glass and the frame completely, so in the "
     "daytime the window looks untreated. Lowered, it covers the frame.",
     "To show the frames as much as possible, raise the shade fully, and consider mounting it high "
     "above the opening so the raised roll clears the glass. Frame depth "
     "decides what is possible, which is one reason we measure every window on site. More in "
     "<a href=\"/inside-mount-vs-outside-mount-blinds\">inside mount vs outside mount</a>."))
 + sec("Grids and divided lites",
   p("Many black windows have grids that divide the glass into panes. Horizontal blind slats add "
     "another set of lines across those grids, and the two can look busy together. Roller shades "
     "and flat roman shades let the grid pattern stay the main pattern. Shutters "
     "work well too when their divider rails line up with the window's own horizontal bars."),
   fig("roller-shades-roller-shades-171-jpg",
       "Wide window with dark divided frames and a light roller shade lowered partway, a wood "
       "curio cabinet beside it",
       "A light roller shade lowered partway on a dark divided window. The flat fabric leaves the "
       "grid as the main pattern."))
 + sec("Which treatments work best",
   li("<strong>Roller and solar shades:</strong> the cleanest option, in charcoal to blend or white "
      "to contrast. The best choice for walls of black-framed glass.",
      "<strong>Plantation shutters:</strong> white shutters against black frames are a high-contrast "
      "classic. Closed, the panels cover the frame; swing them open or tilt the louvers to show it. "
      "Ask about hidden tilt for a cleaner face.",
      "<strong>Roman shades:</strong> soft fabric and texture to warm up a room full of hard black "
      "lines.",
      "<strong>Cellular shades:</strong> insulation for sunny or older windows. Ask which colors are "
      "available; the street side is often white.",
      "<strong>Woven wood shades:</strong> natural texture that softens black frames and warms a "
      "modern room; see <a href=\"/woven-wood-shades-pros-and-cons\">woven wood pros and cons</a>.",
      "<strong>Drapery:</strong> mounted wide and high, panels hang beside the black windows and frame "
      "them. Black rods and hardware tie the drapery to the frames."),
   fig("roller-shades-roller-shades-079-jpg",
       "Bedroom with dark-painted walls and ceiling and black-framed windows, a shade raised to the top "
       "of the largest window",
       "A dark bedroom with black frames. The shade raises to the top of the glass, and the frames "
       "blend with the dark walls."))
 + sec("Hardware details",
   p("Small parts show against black frames. Ask which headrail and bottom-bar finishes are "
     "available, match them to the frames or the fabric, and keep that choice consistent across the "
     "room. "
     "Motorized shades remove cords and wands from view, which keeps the window lines clean. See "
     "<a href=\"/are-motorized-blinds-worth-it\">are motorized blinds worth it</a>."))
 + sec("Mixed white and black windows",
   p("Some homes have black frames in the living areas and white frames in bedrooms, or black outside "
     "and white inside. Choose one treatment family for the house and change only color by room: "
     "charcoal shades where frames are black, white where they are white. From the street, keep the "
     "front windows uniform."))
 + sec("See samples against your frames",
   p("Black frames vary from true black to bronze and dark gray, and samples look different against "
     "each. Holding fabric and shutter samples against your actual windows is the quickest way to "
     "choose. " + CONSULT)),
 faqs=[
  ("What color blinds go with black window frames?",
   "Black or charcoal to blend with the frames, or white and light neutrals for contrast. Pick one "
   "approach per room and keep it consistent."),
  ("Should window treatments match black window frames?",
   "They do not have to match. Dark treatments blend in; light treatments contrast with the frames. "
   "Both work when the treatment opens fully and leaves the frames in view."),
  ("Do plantation shutters look good with black windows?",
   "Yes. White shutters against black frames are a classic high-contrast look, especially in modern "
   "farmhouse homes. Open the panels or tilt the louvers to show the frames."),
  ("How do I keep black frames visible with shades?",
   "Raise the shade fully, and mount it high enough above the opening that the raised roll clears "
   "the frame."),
 ],
 related=[("Roller shades in Texas", "/products/roller-shades"),
          ("What Color Blinds Should I Get?", "/what-color-blinds-should-i-get"),
          ("Inside Mount vs Outside Mount", "/inside-mount-vs-outside-mount-blinds"),
          ("Modern Window Treatment Ideas", "/modern-window-treatment-ideas")],
)


def main(preview_only=False):
    bad = A.lint(POSTS)
    if bad:
        print("\n".join(bad))
        sys.exit("articles_nov2: lint failed")
    for ps_ in POSTS:
        print(f"{ps_['date']}  {ps_['slug']}  {A.words(ps_)} words")
    if preview_only:
        return
    q = json.load(open("data/post-queue.json"))
    by = {x["slug"]: x for x in q}
    for ps_ in POSTS:
        entry = by.get(ps_["slug"])
        if entry and entry.get("published"):
            continue
        open(f"data/queued-posts/{ps_['slug']}.html", "w").write(A.render(ps_))
        rec = {"slug": ps_["slug"], "title": ps_["title"], "desc": ps_["desc"], "date": ps_["date"],
               "img": A.L + ps_["hero"] + ".webp", "published": False}
        if entry:
            entry.update(rec)
        else:
            q.append(rec)
    json.dump(q, open("data/post-queue.json", "w"), indent=1)


if __name__ == "__main__":
    main(preview_only="--preview" in sys.argv)
