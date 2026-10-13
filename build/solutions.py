"""Solutions by window type, plus the installation standards page.

Gap found comparing the site with solarshieldblinds.com (Oct 2026): they run
commercial landing pages per opening type (sliding doors, French doors,
specialty shapes...) while LIB answered those needs only in blog posts,
which Google reads as informational. These pages are commercial: Service
schema, every product option compared, the lead form in the hero.

No new facts. Every product statement restates a product page, an
opening-type post or the how-it-works guarantees already on the site; the
source is noted beside each block. Owner confirmations still pending
(bypass and bi-fold shutters) are listed in the owner checklist.

Also: links into the new pages from the product pages and the problem-based
solutions page, and two Services menu entries swept into every page.
"""
import glob, html, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import extra as X, schema as S
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import resource_posts as RP          # DFW west/south sun ratio, computed
e = lambda s: html.escape(s or "", quote=True)
L = "/images/lib/"
FIVE = RP.times("Dallas-Fort Worth")

# The product-page hero form, re-labelled per page so leads say where they came from.
_FORM = re.search(r'<form class="form-card".*?</form>',
                  open("products/panel-track-shades.html").read(), re.S).group(0)

def form(slug, label):
    f = re.sub(r'(name="_subject" value=")[^"]*', lambda m: m.group(1) + f"New consultation request - {label}", _FORM)
    return re.sub(r'(name="source_page" value=")[^"]*', lambda m: m.group(1) + slug, f)

def img(stem, alt, cls="", eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img src="{L}{stem}-jpg.webp" data-alt-final alt="{e(alt)}" {load} '
            f'width="2000" height="1500"{" class=" + chr(34) + cls + chr(34) if cls else ""}>')

def hero(trail, eyebrow, h1, sub, stem, alt, slug, label):
    crumbs = '<a href="/">Home</a>' + "".join(
        f'<span class="sep">&rsaquo;</span>' + (f'<a href="{u}">{e(t)}</a>' if u else e(t)) for t, u in trail)
    return (f'<section class="phero has-form"><picture>{img(stem, alt, eager=True)}</picture>'
            f'<div class="container"><div class="phero-copy">'
            f'<nav class="crumbs" aria-label="Breadcrumb">{crumbs}</nav>'
            f'<h2 class="eyebrow">{e(eyebrow)}</h2><h1 class="title">{e(h1)}</h1>'
            f'<p class="sub">{sub}</p>'
            f'<div class="hero-trust"><span class="tp"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
            f'Rated 5 stars by Texas homeowners</span><span class="tp">Free in-home consultations</span></div>'
            f'</div>{form(slug, label)}</div></section>')

def faq_block(pairs):
    items = "".join(f"<details><summary>{e(q)}</summary><div class='a'>{e(a)}</div></details>" for q, a in pairs)
    return (f'<section class="section"><div class="container center"><h2 class="title">Common questions</h2></div>'
            f'<div class="container"><div class="faq">{items}</div></div></section>')

def related(links):
    for t, u in links:
        assert os.path.exists(u.lstrip("/") + ".html") or os.path.exists(u.lstrip("/") + "/index.html"), u
    lis = "".join(f'<li><a href="{u}">{e(t)}</a></li>' for t, u in links)
    return (f'<section class="section bg-cream-tint"><div class="container" style="max-width:880px">'
            f'<h2 class="title">Guides on this topic</h2><ul class="sol-guides">{lis}</ul></div></section>')

CLOSE = ('<section class="section closing-cta"><div class="container center">'
         '<h2 class="title">See the options at your own windows</h2>'
         '<p class="lead">Free in-home consultation: samples brought to your door, every opening measured '
         'by us, and a written quote that includes installation.</p>'
         '<div class="btnrow" style="justify-content:center">'
         '<a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a>'
         '<a class="btn btn-secondary btn-lg" href="tel:+18665182999">Call (866) 518-2999</a>'
         '</div></div></section>')


# --------------------------------------------------------------- the pages
# option = (name, product url, image stem, image alt, paragraph)
PAGES = [
dict(
  slug="sliding-glass-doors", nav="Sliding Glass Doors",
  title="Sliding Glass Door Blinds, Shades & Shutters | Love Is Blinds",
  h1="Window Treatments for Sliding Glass Doors", eyebrow="Solutions · Sliding doors",
  desc=("What works on a sliding glass door: panel track shades, solar roller shades, plantation "
        "shutters on a bypass track, and drapery. How to choose, measured and installed across Texas."),
  hero=("panel-track-shades-panel-track-shades-002", "Panel track shades stacked open beside a Texas patio slider"),
  # sources: plantation-shutters-for-sliding-glass-doors, products/panel-track-shades, products/roller-shades
  intro=("A sliding door is wide, full height and used every day, so its treatment has to move the "
         "way the door moves and stack somewhere other than the walkway. Four options do that well. "
         "Which one fits depends on how often the door is used, which panel slides, and how much sun "
         "the glass takes."),
  options=[
    ("Panel track shades", "/products/panel-track-shades", "panel-track-shades-panel-track-shades-001",
     "Panel track shades closed across a Texas patio slider",
     "Wide fabric panels glide along a track and stack neatly to one or both sides, so they move "
     "the same way the door does. Fabrics range from sheer solar weaves to full blackout, including "
     "woven textures. Panel tracks are the usual replacement for vertical blinds that swing and "
     "clatter when the air conditioning kicks on."),
    ("Roller and solar shades", "/products/roller-shades", "roller-shades-roller-shades-237",
     "Solar roller shades behind a sectional with a pool view",
     "A single panel of fabric that rolls up out of sight. Solar fabrics cut glare and UV while "
     "keeping the view, which suits doors that face west or look out on a pool. The shade has to be "
     "raised to use the door, so rollers fit doors that are opened a few times a day."),
    ("Plantation shutters on a track", "/products/plantation-shutters", "shutters-shutters-113",
     "Plantation shutters on a navy gallery wall of framed art",
     "Bypass shutters hang from a head track and slide past each other, so the stack sits in front "
     "of the fixed pane. Bi-fold shutters fold back on themselves and clear the whole doorway. When "
     "only one side of the door slides, the fixed side can take ordinary hinged panels."),
    ("Drapery", "/services/drapery-installation", "smart-drapes-smart-drapes-002",
     "Motorized drapery and shutters in a chandelier-lit Texas bedroom",
     "Panels on a rod or track that draw across the door and stack beside it when open. Drapery "
     "softens a room with a lot of hard glass, and a motorized track can open and close it on a "
     "schedule."),
  ],
  table=(["Option", "Best when", "Keep in mind"], [
    ("Panel track shades", "The door is used many times a day", "The open panels stack at one or both sides"),
    ("Roller and solar shades", "You want the view and a minimal look", "The shade has to be up to use the door"),
    ("Shutters on a track", "Shutters run through the rest of the room", "The track needs depth in front of the glass"),
    ("Drapery", "The room needs softness or height", "Needs wall space beside the door for the stack"),
  ]),
  checks=["Which panel slides, and in which direction",
          "How much depth there is in front of the glass for a track or bracket",
          "Clearance over the handle and lock",
          'How much afternoon sun the glass takes. West-facing doors take the most, as our '
          '<a href="/how-much-sun-hits-each-side-of-a-texas-house">sun data by direction</a> shows'],
  faqs=[
    ("What is the best window treatment for a sliding glass door?",
     "For a door used many times a day, panel track shades, because they slide the same way the door "
     "does and stack to the side. Solar roller shades suit doors where the view matters most, shutters "
     "on a bypass track suit rooms with shutters elsewhere, and drapery adds softness."),
    ("Can you put plantation shutters on a sliding glass door?",
     "Yes. Shutters on a bypass track slide past each other the way the door does, and bi-fold shutters "
     "fold back to clear the whole opening."),
    ("What can replace vertical blinds on a sliding door?",
     "Panel track shades are the most direct replacement. They use a few wide fabric panels instead of "
     "many narrow vanes and stack neatly to one or both sides."),
  ],
  related=[("Can You Use Roller Shades on a Sliding Glass Door?", "/can-you-use-roller-shades-on-a-sliding-glass-door"),
           ("Plantation Shutters for Sliding Glass Doors", "/plantation-shutters-for-sliding-glass-doors"),
           ("Honeycomb vs Panel Track Shades", "/honeycomb-vs-panel-track-shades-which-is-best-for-your-home")],
),
dict(
  slug="french-doors", nav="French Doors & Door Glass",
  title="French Door Blinds, Shades & Shutters | Love Is Blinds",
  h1="Window Treatments for French Doors and Door Glass", eyebrow="Solutions · French doors & sidelights",
  desc=("What works on French doors, door glass and sidelights: door-mounted shutters, cellular and "
        "roller shades, and drapery that clears the doors. Measured and installed across Texas."),
  hero=("shutters-shutters-love-04", "Plantation shutters beside black French doors in a Texas living room"),
  # sources: window-treatments-for-french-doors, window-treatments-for-sidelights-and-door-glass
  intro=("French doors and the glass beside a front door have one thing in common: the treatment is "
         "mounted to something that moves. It has to clear the handle, stay put when the door swings, "
         "and leave the door easy to use. That rules out anything that hangs loose and points to "
         "shutters or shades mounted to the door itself."),
  options=[
    ("Shutters on the door", "/products/plantation-shutters", "shutters-shutters-love-05",
     "White plantation shutters opening onto a backyard pool",
     "Custom shutters can be built with a cut-out for the handle and mounted to the door, so they "
     "swing with it. For sidelights, narrow panels built to the exact width close sightlines while "
     "the louvers still let daylight in. Shutters at the entry also match shutters on the front "
     "windows, so the house reads as one design from the street."),
    ("Door-mounted cellular shades", "/products/honeycomb-shades", "honeycomb-shades-honeycomb-shades-022",
     "Top-down honeycomb shades filtering afternoon light",
     "Slim cellular shades fixed at the top and bottom of the glass cannot swing when the door moves, "
     "and their cells add insulation to a lot of glass."),
    ("Roller shades with a hold-down bracket", "/products/roller-shades", "roller-shades-roller-shades-230",
     "Roller shades in an octagonal bay beneath a chandelier",
     "A flat roller panel with a bracket at the bottom stays against the glass every time the door "
     "opens."),
    ("Drapery on a wide rod", "/services/drapery-installation", "smart-drapes-smart-drapes-love-02",
     "Custom drapes framing a lake view in a Texas bedroom",
     "Hung wide enough to clear the doors completely when they are open. Drapery softens the room, "
     "though it takes wall space and does nothing while the doors are in use."),
  ],
  table=(["Option", "Best when", "Keep in mind"], [
    ("Shutters on the door", "You want the most finished look", "Needs a cut-out built around the handle"),
    ("Door-mounted cellular", "The doors are mostly glass and you want insulation", "Fixed at top and bottom on the door"),
    ("Roller with hold-down", "You want a clean, simple look", "Needs the bottom bracket to stop it swinging"),
    ("Drapery", "You want softness and height", "Needs wall space beside the doors"),
  ]),
  checks=["Whether the doors swing in or out, which decides how much clearance there is",
          "Where the handle sits and how far it projects",
          "Cordless operation on anything mounted to a door, since a cord on a moving door snags",
          "Whether frosted film is the better fit. Film keeps the glass obscured day and night; a "
          "shutter or shade gives the same privacy with the option to open it"],
  faqs=[
    ("What window treatment works best on French doors?",
     "One mounted to the door itself: shutters with a handle cut-out, cellular shades fixed at the top "
     "and bottom, or roller shades with a hold-down bracket. Drapery works if it hangs wide enough to "
     "clear the doors."),
    ("How do you cover the glass beside a front door?",
     "Narrow shutter panels built to the sidelight's width, or door-mounted shades for glass in the "
     "door itself. Both keep daylight while blocking the view in."),
    ("Should shades on a door be cordless?",
     "Yes. A cord on a moving door snags, so door treatments should be cordless or motorized."),
  ],
  related=[("Window Treatments for French Doors", "/window-treatments-for-french-doors"),
           ("Sidelights and Door Glass", "/window-treatments-for-sidelights-and-door-glass"),
           ("Child-Safe Window Coverings", "/child-safe-window-coverings")],
),
dict(
  slug="arched-and-specialty-windows", nav="Arched & Specialty Shapes",
  title="Arched & Specialty Window Treatments | Love Is Blinds",
  h1="Window Treatments for Arched and Specialty-Shape Windows", eyebrow="Solutions · Specialty shapes",
  desc=("Arches, angled tops and bay windows need treatments built to the shape. Custom shutters, "
        "cellular shades and roller shades for specialty windows across Texas."),
  hero=("honeycomb-shades-honeycomb-shades-018", "Honeycomb shades on an arched Texas window wall"),
  # sources: arched-windows post, products/plantation-shutters ("out of square ... frame style")
  intro=("Arches, half-rounds, angled tops and bay windows give a room its character, and none of "
         "them fit a standard size. The treatments that work are built to the shape of the opening: "
         "custom shutters, cellular shades, and roller shades made for the window."),
  options=[
    ("Custom shutters", "/products/plantation-shutters", "shutters-shutters-151",
     "Plantation shutters in a bright Texas living room",
     "Shutters can be built with a frame that follows the shape of the opening. Because a shutter is "
     "a rigid panel in its own frame, an opening that is out of square is handled by the frame style "
     "instead of being hidden by the treatment."),
    ("Cellular shades", "/products/honeycomb-shades", "honeycomb-shades-honeycomb-shades-022",
     "Top-down honeycomb shades filtering afternoon light",
     "Cellular shades can be made for arched and angled openings, and their air-filled cells "
     "insulate the glass."),
    ("Roller shades", "/products/roller-shades", "roller-shades-roller-shades-230",
     "Roller shades in an octagonal bay beneath a chandelier",
     "In a bay or a run of angled windows, individual roller shades fitted to each pane keep the "
     "lines clean and let each window be set on its own."),
  ],
  table=None,
  checks=["The exact shape and size of every opening, measured at the window",
          "Whether the frame is out of square, which decides the shutter frame style",
          "Whether each pane in a bay should move on its own or together"],
  faqs=[
    ("What window treatments work on arched windows?",
     "Custom shutters built to the arch, cellular shades made for the shape, and arched roller shades. "
     "Each one is measured and built for the specific opening."),
    ("Can plantation shutters be made for an arched window?",
     "Yes. Shutters can be built with a frame that follows the shape of the arch."),
    ("How are specialty-shape windows measured?",
     "At the window, like every opening we cover, and the treatment is built to those exact "
     "measurements, since a standard size will not fit an arch or an angle."),
  ],
  related=[("Window Treatments for Arched Windows",
            "/what-are-the-best-window-treatments-for-arched-windows-and-how-do-you-install-them"),
           ("Curtains for Angled Windows", "/the-best-curtains-for-angled-windows"),
           ("Window Treatment Terms, Defined", "/window-treatment-terms-glossary")],
),
dict(
  slug="tall-and-two-story-windows", nav="Tall & Two-Story Windows",
  title="Two-Story & Tall Window Treatments | Love Is Blinds",
  h1="Window Treatments for Tall and Two-Story Windows", eyebrow="Solutions · Tall windows",
  desc=("Motorized shades for two-story and tall windows, with shutters or cellular shades on the "
        "lower tier. Measured and installed across Texas, on ladders where it takes ladders."),
  hero=("roller-shades-roller-shades-love-31", "Roller shades on tall windows in an open Texas kitchen"),
  # sources: window-treatments-for-tall-two-story-windows, products/window-treatment-automations
  intro=("Two-story great rooms and tall glass bring in the most light in a house, and the most heat. "
         "Covering them comes down to reach, scale, and how the wall looks from both floors. Motorized "
         "shades handle the height, and matching fabrics keep the whole wall reading as one design."),
  options=[
    ("Motorized roller and solar shades", "/products/window-treatment-automations", "roller-shades-roller-shades-245",
     "Motorized roller shades in a bright living room overlooking a pool",
     "Upper shades run from a remote, app, schedule or voice assistant. A schedule that lowers the "
     "west-facing bank every afternoon does the job nobody remembers to do by hand. Battery-powered "
     "motors retrofit without wiring, and every motor is paired to your remotes, app and voice "
     "assistant on install day."),
    ("Cellular shades in tall runs", "/products/honeycomb-shades", "honeycomb-shades-honeycomb-shades-022",
     "Top-down honeycomb shades filtering afternoon light",
     "For insulation where afternoon sun loads a tall room."),
    ("Shutters below, shades above", "/products/plantation-shutters", "shutters-shutters-156",
     "Plantation shutters framing a lake view in a Texas living room",
     "Shutters on the lower tier you can reach, with shades on the glass above, keeps the reachable "
     "windows adjustable by hand."),
  ],
  table=None,
  checks=["Which windows nobody can reach. Anything out of reach should be motorized",
          "Matching fabrics across upper and lower tiers so the wall reads as one composition",
          "Inside mounts where the trim is worth showing",
          "Every opening measured on site, on ladders where it takes ladders"],
  faqs=[
    ("How do you open shades on two-story windows?",
     "With motorization. Upper shades run from a remote, app, schedule or voice assistant, so they move "
     "with the sun instead of staying in one position."),
    ("What is the best window treatment for a two-story great room in Texas?",
     "Motorized roller or solar shades on the upper glass, often with shutters or cellular shades on the "
     "lower tier you can reach."),
    ("Can motorized shades be added without new wiring?",
     "Yes. Battery-powered motors retrofit without wiring."),
  ],
  related=[("Window Treatments for Tall and Two-Story Windows", "/window-treatments-for-tall-two-story-windows"),
           ("The Best Blinds for Large Windows", "/best-blinds-for-large-windows"),
           ("How Much Sun Hits Each Side of a Texas House", "/how-much-sun-hits-each-side-of-a-texas-house")],
),
dict(
  slug="child-and-pet-safe", nav="Child & Pet Safe",
  title="Child & Pet Safe Window Treatments | Love Is Blinds",
  h1="Window Treatments That Are Safe for Children and Pets", eyebrow="Solutions · Kids & pets",
  desc=("Cordless, motorized and shutter options with no reachable cords, plus treatments that hold "
        "up to dogs. Measured and installed across Texas."),
  hero=("shutters-shutters-love-15", "Plantation shutters in a family dining room with a dog resting on the rug"),
  # sources: child-safe-window-coverings, top-10-dog-proof post
  intro=("In a house with small children, the safe choice is a window treatment with no cord a child "
         "can reach. With pets the problem is wear: slats that bend when a dog checks the window, and "
         "materials that do not stand up to scratching. The options below handle both."),
  options=[
    ("Cordless blinds and shades", "/products/faux-wood-blinds", "blinds-blinds-009",
     "Faux wood blinds over a marble counter in a bright white Texas kitchen",
     "You raise and lower the treatment by hand from the bottom rail, with no cord. Cordless is "
     "standard on most new blinds and shades and is the baseline for any room a child uses. Faux "
     "wood stands up to scratching and moisture better than real wood, which makes it a good fit in "
     "homes with dogs."),
    ("Motorized treatments", "/products/window-treatment-automations", "smart-drapes-smart-drapes-002",
     "Motorized drapery and shutters in a chandelier-lit Texas bedroom",
     "No cord and no reaching. Motorization is most useful on high windows, where cordless lift is "
     "still awkward."),
    ("Plantation shutters", "/products/plantation-shutters", "shutters-shutters-060",
     "Plantation shutters on tall windows in a Texas family room",
     "No cords by design. The louvers tilt with a rod or a hidden mechanism, and the solid panels "
     "hold up in homes with pets."),
  ],
  table=None,
  checks=["Every room a child sleeps in, plays in, or can reach unsupervised",
          "Where furniture sits, since a crib or chair can put a high window within reach",
          "Older treatments elsewhere in the house that still have cords",
          "Cord cleats and tie-downs reduce risk but depend on an adult using them every time. "
          "Cordless and motorized treatments remove it"],
  faqs=[
    ("What window treatments are safest for children?",
     "Treatments with no accessible cord: cordless blinds and shades, motorized treatments, and "
     "plantation shutters. Cord cleats and tie-downs reduce risk but depend on an adult using them "
     "every time."),
    ("What blinds hold up to dogs?",
     "Faux wood blinds and plantation shutters stand up to scratching and moisture better than real "
     "wood."),
    ("Can existing corded blinds be made safe?",
     "Tie-downs and cleats reduce the risk. Replacing corded blinds with cordless or motorized "
     "treatments removes it."),
  ],
  related=[("Child-Safe Window Coverings", "/child-safe-window-coverings"),
           ("Dog-Proof Window Blinds", "/top-10-dog-proof-window-blinds-durable-and-pet-friendly"),
           ("Window Coverings to Avoid With Kids", "/window-covering-you-shouldn-t-buy-if-you-have-kids-around")],
),
dict(
  slug="heat-and-glare", nav="Heat, Glare & West Windows",
  title="Window Treatments for Texas Heat & Glare | Love Is Blinds",
  h1="Window Treatments for Texas Heat and Glare", eyebrow="Solutions · Heat & glare",
  desc=(f"West windows in DFW take about {FIVE} times the direct June sun of south windows. Solar, "
        "cellular and exterior shades that handle Texas heat and glare."),
  hero=("exterior-patio-shades-exterior-patio-shades-drew-wrap-front",
        "Exterior shades across the wrap porch of a white Texas farmhouse"),
  # sources: products/roller-shades, products/honeycomb-shades, how-much-sun-hits... (computed)
  intro=(f'In Dallas-Fort Worth, a west-facing window takes about {FIVE} times the direct June sun of '
         f'a south-facing one, by our <a href="/how-much-sun-hits-each-side-of-a-texas-house">clear-sky '
         f'calculations</a>. That afternoon sun is where most Texas heat and glare problems start. The '
         f'right treatment depends on whether you want to keep the view, insulate the glass, or stop '
         f'the sun before it reaches the window.'),
  options=[
    ("Solar shades", "/products/roller-shades", "roller-shades-roller-shades-237",
     "Solar roller shades behind a sectional with a pool view",
     "Solar fabrics cut glare and UV while keeping the view. They are the answer for west-facing "
     "glass and for rooms where floors and furniture are fading. A tighter weave stops more heat and "
     "glare; a looser one keeps more of the view."),
    ("Cellular shades", "/products/honeycomb-shades", "honeycomb-shades-honeycomb-shades-018",
     "Honeycomb shades on an arched Texas window wall",
     "The cells trap a pocket of air against the glass, which slows heat moving through it in both "
     "directions: summer heat stays out and winter warmth stays in. They are worth the money on west "
     "and south glass."),
    ("Exterior patio shades", "/products/exterior-patio-shades", "exterior-patio-shades-exterior-patio-shades-002",
     "Exterior patio shades on a Texas home",
     "Mounted outside, they stop the sun before it reaches the glass, which no interior treatment can "
     "do. They suit west-facing patios and large walls of glass."),
    ("Motorized schedules", "/products/window-treatment-automations", "roller-shades-roller-shades-245",
     "Motorized roller shades in a bright living room overlooking a pool",
     "A schedule that lowers the west-facing shades every afternoon, without anyone remembering to."),
  ],
  table=(["Goal", "Best fit"], [
    ("Keep the view, cut glare", "Solar shades"),
    ("Insulate the glass", "Cellular shades"),
    ("Stop heat before the glass", "Exterior patio shades"),
    ("Never forget to close them", "Motorization on a schedule"),
  ]),
  checks=["Which way each window faces, and which ones take afternoon sun",
          "Whether the view matters enough to keep, which points to solar fabric",
          "Whether a patio or outdoor room needs shade too",
          "How the treatment is operated, if it has to move every afternoon"],
  faqs=[
    ("What is the best window treatment for Texas heat?",
     "Exterior shades stop heat before it reaches the glass. Inside, cellular shades insulate the most, "
     "and solar shades cut heat and glare while keeping the view."),
    ("Do solar shades block heat?",
     "They cut heat, glare and UV while staying see-through from inside. A tighter weave blocks more "
     "sun; a more open weave keeps more of the view."),
    ("Which windows need heat control most in Texas?",
     f"West-facing windows. In Dallas-Fort Worth they take about {FIVE} times the direct June sun of "
     f"south-facing windows, and that sun arrives during the hottest part of the day."),
  ],
  related=[("How Much Sun Hits Each Side of a Texas House", "/how-much-sun-hits-each-side-of-a-texas-house"),
           ("Interior vs Exterior Shades for Texas Sun", "/interior-vs-exterior-shades-for-texas-sun"),
           ("Cellular Shades vs Roller Shades for Texas Heat", "/cellular-shades-vs-roller-shades")],
),
]



# ----------------------------------------------------- depth: real content
# Reviews: verbatim Google reviews whose text is about the page's topic.
# French doors has none that genuinely are, so it gets no review block
# rather than a forced one. Tall windows uses motorized-shade reviews,
# labelled as such, since no review mentions tall windows directly.
import json as _json
_ALL = _json.load(open("data/reviews.json"))
# Only quote people who reviewed a single profile. 102 of 373 reviews come
# from names that appear on 2+ profiles, including an owner's name; until
# the owners identify family/staff, multi-profile reviewers are left out.
_CITIES_BY = {}
for _r in _ALL:
    _CITIES_BY.setdefault((_r.get("name") or "").strip().lower(), set()).add(_r.get("city"))
_REVS = [r for r in _ALL if float(r.get("rating", 5)) >= 4
         and len(_CITIES_BY[(r.get("name") or "").strip().lower()]) == 1]
REVIEW_TOPICS = {
 "sliding-glass-doors": (r"sliding (glass )?doors?|slider|back door|patio door",
                         "What homeowners say about their sliding door shades"),
 "arched-and-specialty-windows": (r"\barch(ed|es)?\b|bay windows?|angled|specialty window|odd[- ]shaped|transom",
                                  "What homeowners say about their specialty windows"),
 "tall-and-two-story-windows": (r"motoriz", "What homeowners say about their motorized shades"),
 "child-and-pet-safe": (r"\bdogs?\b|\bpets?\b|\bkids?\b|\bchild(ren)?\b|grandkids|cordless",
                        "What homeowners with kids and pets say"),
 "heat-and-glare": (r"\bglare\b|\bsolar\b|\bheat\b|\bsun ?block|\bsunlight\b|afternoon sun|\bcooler\b",
                    "What homeowners say about sun and glare"),
}

def _pick_reviews(slug, n=4):
    if slug not in REVIEW_TOPICS:
        return []
    pat = REVIEW_TOPICS[slug][0]
    out = []
    for r in _REVS:
        q = r.get("quote") or ""
        w = len(q.split())
        if not (12 <= w <= 100) or "  " in q:
            continue
        m = re.findall(pat, q.lower())
        if m:
            out.append((len(set(map(str, m))), -abs(w - 45), r))
    out.sort(key=lambda x: (x[0], x[1]), reverse=True)
    picked, names = [], set()
    for _, _, r in out:            # one review per person: some posted on two profiles
        who = (r.get("name") or "").strip().lower()
        if who in names:
            continue
        names.add(who)
        picked.append(r)
        if len(picked) == n:
            break
    return picked

def _who(r):
    parts = (r.get("name") or "").split()
    name = parts[0] + (f" {parts[-1][0]}." if len(parts) > 1 else "") if parts else "Google reviewer"
    return f"{name}, {r.get('city', 'Texas')}"

def reviews_html(slug):
    picks = _pick_reviews(slug)
    if not picks:
        return ""
    cards = "".join(
        f'<figure class="sol-review"><div class="stars" aria-label="5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
        f'<blockquote>{e(r["quote"])}</blockquote><figcaption>{e(_who(r))}, TX</figcaption></figure>'
        for r in picks)
    return (f'<section class="section bg-cream-tint"><div class="container">'
            f'<h2 class="title center">{e(REVIEW_TOPICS[slug][1])}</h2>'
            f'<div class="sol-reviews">{cards}</div>'
            f'<p class="lead center" style="margin:26px auto 0">Verbatim Google reviews. '
            f'<a href="/reviews">Read all of our reviews</a>.</p></div></section>')

# Installed photos, hand-picked and viewed; alt text describes the photo.
G = {
 "roller-love-01-after": ("roller-shades-roller-shades-love-01-after", "Roller shades lowered across tall windows in a modern Texas dining room"),
 "roller-love-10": ("roller-shades-roller-shades-love-10", "Light-filtering shades on tall windows beside a modern fireplace"),
 "roller-love-21": ("roller-shades-roller-shades-love-21", "Roller shades on a wall of windows in a Texas sitting room"),
 "roller-love-45": ("roller-shades-roller-shades-love-45", "Roller shade over a kitchen sink window in a Texas home"),
 "drapes-love-01": ("smart-drapes-smart-drapes-love-01", "Floor-to-ceiling drapery across a Texas bedroom wall"),
 "drapes-love-02": ("smart-drapes-smart-drapes-love-02", "Custom drapes framing a lake view in a Texas bedroom"),
 "shut-love-01": ("shutters-shutters-love-01", "Plantation shutters beneath angled transom windows in a vaulted Texas living room"),
 "shut-love-08": ("shutters-shutters-love-08", "Plantation shutters around a bay breakfast nook with transom windows above"),
 "shut-love-14": ("shutters-shutters-love-14", "White plantation shutters above a gray sectional in a bright living room"),
 "shut-160": ("shutters-shutters-160", "Plantation shutters in an open Texas kitchen"),
 "blinds-008": ("blinds-blinds-008", "Faux wood blinds on three windows of a shiplap wall with candle sconces"),
}
GALLERY = {
 "sliding-glass-doors": ["roller-love-01-after", "roller-love-21", "drapes-love-01"],
 "french-doors": ["shut-love-14", "shut-160", "shut-love-08"],
 "arched-and-specialty-windows": ["shut-love-01", "shut-love-08"],
 "tall-and-two-story-windows": ["roller-love-01-after", "roller-love-10", "drapes-love-02"],
 "child-and-pet-safe": ["blinds-008", "shut-love-14", "shut-love-08"],
 "heat-and-glare": ["roller-love-21", "roller-love-45", "roller-love-10"],
}

def gallery_html(slug):
    items = "".join(f'<figure class="sol-shot"><picture>{img(*G[k])}</picture>'
                    f'<figcaption>{e(G[k][1])}</figcaption></figure>' for k in GALLERY.get(slug, []))
    if not items:
        return ""
    return (f'<section class="section"><div class="container">'
            f'<h2 class="title center">Installed in Texas homes</h2>'
            f'<p class="lead center" style="margin:0 auto 26px">Photos from projects measured and installed by our teams.</p>'
            f'<div class="sol-gallery">{items}</div></div></section>')

_CITIES = [c for c in _json.load(open("data/tx.json"))["cities"] if not c.get("unlisted")]

def cities_html(p):
    chips = "".join(f'<a class="sol-city" href="/{c["slug"]}">{e(c["label"])}</a>'
                    for c in sorted(_CITIES, key=lambda c: c["label"]))
    return (f'<section class="section"><div class="container" style="max-width:980px">'
            f'<h2 class="title center">Find your local team</h2>'
            f'<p class="lead center" style="margin:0 auto 22px">Every Love Is Blinds team measures and '
            f'installs in person. Find your city for local reviews and the team that covers you.</p>'
            f'<div class="sol-cities">{chips}</div></div></section>')


def options_html(opts):
    out = ""
    for i, (name, url, stem, alt, para) in enumerate(opts):
        text = (f'<div class="body"><p class="sol-kicker">Option {i + 1} of {len(opts)}</p>'
                f'<h2 class="title">{e(name)}</h2><p class="lead">{para}</p>'
                f'<a class="btn-link" href="{url}">See {e(name.lower())} <span class="arw">&rarr;</span></a></div>')
        media = f'<div class="media"><picture>{img(stem, alt)}</picture></div>'
        # even options: text left, image right; odd: image first in the markup, so it sits left
        inner = (f'<div class="container split media-right">{text}{media}</div>' if i % 2 == 0
                 else f'<div class="container split">{media}{text}</div>')
        out += f'<section class="section{" bg-cream-tint" if i % 2 else ""}">{inner}</section>'
    return out

def table_html(t):
    if not t:
        return ""
    head, rows = t
    th = "".join(f"<th>{e(h)}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in rows)
    return (f'<section class="section"><div class="container" style="max-width:880px">'
            f'<h2 class="title">Side by side</h2><div class="sol-table-wrap"><table class="sol-table">'
            f'<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div></div></section>')

def build_page(p):
    url = f"/solutions/{p['slug']}"
    body = (hero([("Solutions", "/solutions"), (p["nav"], None)], p["eyebrow"], p["h1"], p["intro"],
                 *p["hero"], f"solutions/{p['slug']}", p["nav"])
            + options_html(p["options"]) + table_html(p["table"])
            + '<section class="section"><div class="container" style="max-width:880px">'
              '<h2 class="title">What we check before recommending one</h2><ul class="sol-checks">'
            + "".join(f"<li>{c}</li>" for c in p["checks"]) + "</ul></div></section>"
            + gallery_html(p["slug"]) + reviews_html(p["slug"])
            + faq_block(p["faqs"]) + related(p["related"]) + cities_html(p) + CLOSE)
    nodes = X.BASE() + [
        S.webpage(url, p["title"], p["desc"], primary=L + p["hero"][0] + "-jpg.webp"),
        S.breadcrumbs([("Home", "/"), ("Solutions", "/solutions"), (p["nav"], url)]),
        S.service(url, p["h1"], p["desc"], S.ORGID, catalog=[o[0] for o in p["options"]]),
        S.faq(url, p["faqs"])]
    os.makedirs("solutions", exist_ok=True)
    open(f"solutions/{p['slug']}.html", "w").write(
        X.shell(url, p["title"], p["desc"], [n for n in nodes if n], body,
                img=L + p["hero"][0] + "-jpg.webp"))


def build_hub():
    url = "/solutions"
    title = "Window Treatment Solutions by Window Type | Love Is Blinds"
    desc = ("What works on sliding doors, French doors, arches, tall windows and more. Every option "
            "for each opening type, measured and installed across Texas.")
    cards = "".join(
        f'<a class="sol-card" href="/solutions/{p["slug"]}"><span class="sol-pic">{img(*p["hero"])}</span>'
        f'<span class="sol-body"><b>{e(p["nav"])}</b><span>{e(", ".join(o[0] for o in p["options"]).capitalize())}</span>'
        f'<span class="btn-link">See the options <span class="arw">&rarr;</span></span></span></a>'
        for p in PAGES)
    body = (hero([("Solutions", None)], "Solutions by window type", "Window Treatment Solutions by Window Type",
                 "Some openings rule out most treatments before style even comes up: a sliding door you "
                 "walk through every day, a French door with a handle in the way, an arch, a window twenty "
                 "feet up. Each page below lays out what works on that opening, what to decide before you "
                 "order, and which of our products fit.",
                 "shutters-shutters-160", "Plantation shutters in an open Texas kitchen", "solutions", "Solutions")
            + f'<section class="section"><div class="container"><div class="sol-grid">{cards}</div>'
              f'<p class="lead center" style="margin:36px auto 0">Looking by problem instead, such as blackout '
              f'or energy savings? See <a href="/services/window-treatment-solutions">window treatment '
              f'solutions by problem</a>.</p></div></section>' + CLOSE)
    item_list = {"@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": S.SITE + f"/solutions/{p['slug']}", "name": p["h1"]}
        for i, p in enumerate(PAGES)]}
    nodes = X.BASE() + [S.webpage(url, title, desc), S.breadcrumbs([("Home", "/"), ("Solutions", url)]), item_list]
    os.makedirs("solutions", exist_ok=True)
    open("solutions/index.html", "w").write(
        X.shell(url, title, desc, nodes, body, img=L + "shutters-shutters-160-jpg.webp"))


def build_standards():
    url = "/installation-standards"
    title = "Installation Standards | Love Is Blinds Texas"
    desc = ("How every Love Is Blinds team in Texas measures and installs: on-site measuring, a written "
            "quote that includes installation, and a remake at no cost if anything does not fit.")
    # sources: how-it-works (process + five guarantees, wording followed closely),
    # products/window-treatment-automations (motor pairing on install day)
    steps = [
        ("Measured on site by the people who install",
         "Every opening is measured in your home by the person who will stand behind the numbers. You "
         "never measure anything yourself. Out-of-square openings, shallow frames and tall panels are "
         "flagged at this visit, while the fix is still a choice."),
        ("A written quote that includes installation",
         "The quote is written from those measurements, covers installation, and does not move."),
        ("Built to your measurements",
         "Most orders arrive within two to four weeks of approval. Motorized treatments can take longer, "
         "and we confirm the timeline in writing on your quote."),
        ("Installed by the team that measured",
         "The same team returns to install and operates every treatment with you before leaving. "
         "Motorized treatments are paired to your remotes, app and voice assistant on install day, with "
         "scenes, schedules and groups set up."),
        ("Remade if it does not fit",
         "Anything that does not match the approved measurements is remade and reinstalled at no cost "
         "to you."),
    ]
    guarantees = [
        ("Limited Lifetime Warranty", "A manufacturer's limited lifetime warranty: factory defects are covered for life."),
        ("Apples-to-Apples", "A price-match guarantee on comparable written quotes."),
        ("GuaranTEN", "For every ten window treatments you purchase, we replace one for free. Break it, "
                      "don't like it, get tired of it, we replace it, no questions asked."),
        ("Here-4-You", "A four-year service guarantee. If you have any issues, we come out and service your "
                       "blinds, shades or shutters at no cost."),
        ("Transferable Warranty", "Our warranties transfer if you sell your home."),
    ]
    faqs = [
        ("Who installs Love Is Blinds window treatments?",
         "The same local team that measured your windows. Each part of Texas is served by an "
         "owner-operated franchise."),
        ("What happens if a window treatment does not fit?",
         "If it does not match the approved measurements, we remake it and reinstall it at no cost to you."),
        ("How long does it take to get window treatments installed?",
         "Most orders arrive within two to four weeks of approval, and motorized treatments can take "
         "longer. Installation is scheduled once your order arrives."),
    ]
    step_html = "".join(f'<li><h3>{e(h)}</h3><p>{e(t)}</p></li>' for h, t in steps)
    g_html = "".join(f'<li><b>{e(h)}</b><span>{e(t)}</span></li>' for h, t in guarantees)
    body = (hero([("Installation Standards", None)], "Installation standards", "How We Measure and Install",
                 "Custom window treatments are built to a measurement, so the measuring and the "
                 "installation decide whether they work. These are the standards every Love Is Blinds "
                 "team in Texas works to, from the first visit through install day.",
                 "shutters-shutters-love-02", "Plantation shutters beside a fireplace in a Texas living room",
                 "installation-standards", "Installation standards")
            + f'<section class="section"><div class="container" style="max-width:880px">'
              f'<h2 class="title">From first visit to install day</h2><ol class="sol-steps">{step_html}</ol>'
              f'<p class="lead" style="margin-top:28px">Installation comes up in 31% of our Google reviews. '
              f'<a href="/what-our-google-reviews-say-about-hiring-a-blinds-company">See what homeowners '
              f'mention most</a>.</p></div></section>'
            + f'<section class="section bg-cream-tint"><div class="container" style="max-width:880px">'
              f'<h2 class="title">Backed five ways</h2><ul class="sol-guarantees">{g_html}</ul>'
              f'<p class="lead" style="margin-top:22px"><a href="/how-it-works">How the whole process works</a></p>'
              f'</div></section>'
            + faq_block(faqs) + CLOSE)
    nodes = X.BASE() + [S.webpage(url, title, desc, primary=L + "shutters-shutters-love-02-jpg.webp"),
                        S.breadcrumbs([("Home", "/"), ("Installation Standards", url)]),
                        S.service(url, "Window treatment installation", desc, S.ORGID,
                                  catalog=[h for h, _ in steps]),
                        S.faq(url, faqs)]
    open("installation-standards.html", "w").write(
        X.shell(url, title, desc, nodes, body, img=L + "shutters-shutters-love-02-jpg.webp"))


# product page -> solution pages it belongs on (links back into the new pages)
FITS = {
 "products/panel-track-shades.html": ["sliding-glass-doors"],
 "products/plantation-shutters.html": ["sliding-glass-doors", "french-doors", "arched-and-specialty-windows", "child-and-pet-safe"],
 "products/shutters.html": ["sliding-glass-doors", "french-doors", "arched-and-specialty-windows", "child-and-pet-safe"],
 "products/honeycomb-shades.html": ["french-doors", "arched-and-specialty-windows", "heat-and-glare"],
 "products/energy-efficient-custom-window-shades.html": ["heat-and-glare", "tall-and-two-story-windows"],
 "products/roller-shades.html": ["sliding-glass-doors", "heat-and-glare", "tall-and-two-story-windows"],
 "products/shades.html": ["sliding-glass-doors", "heat-and-glare", "tall-and-two-story-windows"],
 "products/window-treatment-automations.html": ["tall-and-two-story-windows", "child-and-pet-safe", "heat-and-glare"],
 "products/motorized-window-treatment-automations.html": ["tall-and-two-story-windows", "child-and-pet-safe", "heat-and-glare"],
 "products/exterior-patio-shades.html": ["heat-and-glare"],
 "products/faux-wood-blinds.html": ["child-and-pet-safe"],
 "products/blinds.html": ["child-and-pet-safe"],
 "services/window-treatment-solutions.html": [p["slug"] for p in PAGES],
}

def link_in():
    names = {p["slug"]: p["nav"] for p in PAGES}
    n = 0
    for f, slugs in FITS.items():
        if not os.path.exists(f):
            continue
        s = open(f).read()
        s = re.sub(r'<!-- sol-band -->.*?<!-- /sol-band -->', "", s, flags=re.S)
        links = "".join(f'<a class="btn btn-secondary" href="/solutions/{x}">{e(names[x])}</a>' for x in slugs)
        band = ('<!-- sol-band --><section class="section sol-band"><div class="container center">'
                '<h2 class="title">Where this works best</h2>'
                f'<div class="btnrow" style="justify-content:center">{links}</div>'
                '<p class="lead" style="margin-top:14px"><a href="/solutions">All solutions by window type</a></p>'
                '</div></section><!-- /sol-band -->')
        i = s.find('class="faq"')
        j = s.find("</section>", i) + len("</section>") if i >= 0 else s.find('<footer')
        s = s[:j] + band + s[j:]
        open(f, "w").write(s)
        n += 1
    print(f"solution links added to {n} pages")

NAV_ADD = [('<a href="/services/window-treatment-installation">Window Treatment Installation</a>',
            '<a href="/installation-standards">Installation Standards</a>'),
           ('<a href="/services/window-treatment-solutions">Window Treatment Solutions</a>',
            '<a href="/solutions">Solutions by Window Type</a>')]

def nav():
    files = ["build/partials/header.html"] + [f for f in glob.glob("**/*.html", recursive=True)
                                             if not f.startswith(("build/", "hero-mob/"))]
    n = 0
    for f in files:
        s = o = open(f).read()
        for anchor, add in NAV_ADD:
            if add not in s and anchor in s:
                s = s.replace(anchor, anchor + "\n            " + add, 1)
        if s != o:
            open(f, "w").write(s)
            n += 1
    print(f"services menu updated on {n} files")


if __name__ == "__main__":
    for p in PAGES:
        build_page(p)
    build_hub()
    build_standards()
    print(f"solutions: hub + {len(PAGES)} pages, installation standards written")
    link_in()
    nav()
