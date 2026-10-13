"""Three resource articles built on data rather than generic advice.

1. A count of what homeowners mention across our Google reviews, computed
   from data/reviews.json at build time (brand name stripped before
   counting, so "Love Is Blinds" never counts as a mention of blinds).
2. Clear-sky solar geometry by window direction for DFW, Austin and
   Sherman, computed here with the Meinel air-mass model.
3. A plain-English glossary; every definition traces to a product page
   or guarantee already on the site.

Numbers are generated, never hand-copied, so a rebuild after new reviews
keeps the article accurate. Publishes immediately (not queued).
"""
import datetime, json, math, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import newposts as NP
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
p, sec, sub, li = NP.p, NP.sec, NP.sub, NP.li
L = "/images/lib/"
TODAY = "2026-10-13"


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>"


# ------------------------------------------------------------ reviews data
revs = json.load(open("data/reviews.json"))
N = len(revs)
BRAND = re.compile(r"love\s*is\s*blinds?|loveisblinds?|live is blinds", re.I)
TXT = [BRAND.sub(" ", r.get("quote") or "").lower() for r in revs]

def pct(pat):
    n = sum(1 for t in TXT if re.search(pat, t))
    return n, round(n * 100 / N)

OWNER = pct(r"\b(jake|jonathan|durrell|danny|dustin)\b")
TOPICS = [
    ("Recommends the company", pct(r"\brecommend")),
    ("The installation", pct(r"\binstall")),
    ("Professionalism", pct(r"\bprofessional")),
    ("Product quality", pct(r"\bquality\b")),
    ("Price or pricing", pct(r"\bpric(e|es|ed|ing)\b")),
    ("Knowledge or explaining options", pct(r"\bknowledg|\bexplain")),
    ("Communication", pct(r"\bcommunicat")),
    ("Arriving on time", pct(r"\bon time\b|\bpunctual")),
    ("Patience or no pressure", pct(r"\bpatien|\bno pressure|\bpushy")),
    ("The measuring", pct(r"\bmeasur")),
    ("Samples", pct(r"\bsamples?\b")),
]
T = dict(TOPICS)
PRODUCTS = [
    ("Blinds", pct(r"\bblinds?\b")),
    ("Shades", pct(r"\bshades?\b")),
    ("Shutters", pct(r"\bshutters?\b")),
    ("Motorized treatments", pct(r"\bmotoriz")),
]
_SVC = (r"\brecommend|\binstall|\bprofessional|\bquality\b|\bknowledg|\bexplain|\bcommunicat"
        r"|\bon time\b|\bpatien|\bresponsive|\bfriendly|\bhelpful|\bgreat (job|service|experience)")
_PR = [t for t in TXT if re.search(r"\bpric(e|es|ed|ing)\b", t)]
PRICE_SVC = sum(1 for t in _PR if re.search(_SVC, t))
FIVE = sum(1 for r in revs if float(r.get("rating", 5)) == 5)
CITIES = len({r.get("city") for r in revs if r.get("city")})
WORDS = sorted(len(t.split()) for t in TXT)
MEDIAN = WORDS[N // 2]
LONG = sum(1 for w in WORDS if w > 50)
MONTH = datetime.date.fromisoformat(TODAY).strftime("%B %Y")

post1 = dict(
    slug="what-our-google-reviews-say-about-hiring-a-blinds-company",
    title=f"What {N} Reviews Say About Hiring a Blinds Company",
    desc=(f"We counted what Texas homeowners mention across {N} Google reviews. "
          "Installers come up far more often than price. Use the patterns to vet any company."),
    hero=L + "shutters-shutters-love-15-jpg.webp",
    body=(
        p(f"Most people shopping for custom blinds or shutters read reviews before they call "
          f"anyone. We wanted to know what those reviews actually contain, so we counted. We "
          f"took every Google review on our Texas Business Profiles, {N} of them from homeowners "
          f"in {CITIES} cities, and tallied the topics people chose to bring up. The results are "
          f"below, along with a way to use them when you read reviews for any window treatment "
          f"company.")
        + sec("Most reviews name the person who did the work",
            p(f"{OWNER[1]}% of the reviews mention the owner who handled the job by first name. "
              f"Google's review form asks only for a star rating and a few words, so every one of "
              f"those names was volunteered."),
            p("That shows where homeowners see the risk in a custom window treatment project. The "
              "blind or shutter is built in a factory to a measurement. Whether it fits the "
              "opening, hangs level and works on day one depends on the person who measured and "
              "installed it, and that is what reviewers write about."))
        + sec("What homeowners mention, counted",
            table(["Topic mentioned", f"Share of {N} reviews"],
                  [(k, f"{v[1]}%") for k, v in TOPICS]),
            p(f"Price appears in {T['Price or pricing'][1]}% of reviews, and {PRICE_SVC} of those "
              f"{len(_PR)} also talk about the service: the installation, the owner's knowledge, "
              f"the communication. Professionalism and the installation each come up about twice "
              f"as often as price."))
        + sec("What they bought",
            table(["Product mentioned", f"Share of {N} reviews"],
                  [(k, f"{v[1]}%") for k, v in PRODUCTS]),
            p(f"Blinds come up most often, followed by shades and shutters. Motorized treatments "
              f"come up in {PRODUCTS[3][1][0]} reviews."))
        + sec("How to use this when you read reviews for any company",
            li("<strong>Look for names.</strong> A review that names the person who measured and "
               "installed tells you one person was responsible for the whole job. A review that "
               "mentions only the brand cannot tell you who will come to your house.",
               "<strong>Read about install day.</strong> The installation is where custom "
               "treatments go right or wrong. Reviews that describe it show you what to expect.",
               "<strong>Read recent and older reviews.</strong> A company that has held the same "
               "standard for years will show it in both.",
               f"<strong>Check the cities.</strong> A company that works across a region will have "
               f"reviews from across that region. Ours come from {CITIES} Texas cities, and our "
               f"<a href=\"/reviews\">reviews page</a> groups them by city."))
        + sec("How we counted",
            p(f"We matched words and phrases across the text of all {N} reviews on our Google "
              f"Business Profiles as of {MONTH}. {FIVE} of the {N} are five stars. Each review "
              f"counts once per topic, however many times the topic appears in it. We removed our "
              f"own company name before counting, so the word \"Blinds\" in \"Love Is Blinds\" "
              f"does not count as a mention of blinds. The median review is {MEDIAN} words long, "
              f"and {LONG} reviews run past 50 words. Every review is public on Google.")),
    ),
    faqs=[
        ("What do customers mention most in reviews of window treatment companies?",
         f"Across our {N} Google reviews, the most common topics are recommending the company "
         f"({T['Recommends the company'][1]}%), the owner who did the work by name ({OWNER[1]}%), "
         f"the installation ({T['The installation'][1]}%) and professionalism "
         f"({T['Professionalism'][1]}%). Price comes up in {T['Price or pricing'][1]}%."),
        ("How should I read reviews when choosing a blinds company?",
         "Look for reviews that name the person who measured and installed, read descriptions of "
         "install day, compare recent reviews with older ones, and check that reviews come from "
         "the cities the company says it serves."),
        ("Where can I read these reviews?",
         "They are public reviews on our Google Business Profiles. Our reviews page collects them "
         "by city with links to each profile."),
    ],
    related=[("Read Our Google Reviews", "/reviews"),
             ("How It Works", "/how-it-works"),
             ("Shutters vs Blinds: Which Is Right for Your Home?",
              "/shutters-vs-blinds-which-is-right-for-your-home")],
)


# ------------------------------------------------------------- solar data
def _pos(lat, dec, ha):
    la, de, h = map(math.radians, (lat, dec, ha))
    sa = math.sin(la) * math.sin(de) + math.cos(la) * math.cos(de) * math.cos(h)
    alt = math.asin(sa)
    ca = (math.sin(de) - math.sin(alt) * math.sin(la)) / (math.cos(alt) * math.cos(la))
    az = math.degrees(math.acos(max(-1, min(1, ca))))
    return alt, (360 - az if ha > 0 else az)

def daily(lat, dec):
    """kWh/m2/day of clear-sky direct beam on a vertical window per facade."""
    fac = {"North": 0, "East": 90, "South": 180, "West": 270}
    e = {f: 0.0 for f in fac}
    for m in range(-720, 720):
        alt, az = _pos(lat, dec, m / 4)
        if alt <= math.radians(2):
            continue
        b = 1.353 * 0.7 ** ((1 / math.sin(alt)) ** 0.678)   # Meinel model
        for f, n in fac.items():
            c = math.cos(alt) * math.cos(math.radians(az - n))
            if c > 0:
                e[f] += b * c / 60
    return e

LAT = {"Dallas-Fort Worth": 32.78, "Austin": 30.27, "Sherman": 33.64}
SEASON = {"June 21": 23.44, "Sept. 21": 0.0, "Dec. 21": -23.44}
SUN = {c: {s: daily(la, d) for s, d in SEASON.items()} for c, la in LAT.items()}
D = SUN["Dallas-Fort Worth"]
ratio = lambda c: SUN[c]["June 21"]["West"] / SUN[c]["June 21"]["South"]
WORD = {2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
times = lambda c: WORD.get(round(ratio(c)), str(round(ratio(c))))
NOON_JUNE_DFW = round(90 - LAT["Dallas-Fort Worth"] + 23.44)
f2 = lambda x: f"{x:.2f}"

post2 = dict(
    slug="how-much-sun-hits-each-side-of-a-texas-house",
    title="How Much Sun Hits Each Side of a Texas House",
    desc=(f"West windows in DFW take about {times('Dallas-Fort Worth')} times the direct "
          f"summer sun of south windows. Numbers by direction and season, and what to install."),
    hero=L + "roller-shades-roller-shades-237-jpg.webp",
    body=(
        p("The direction a window faces says more about its sun problem than the room it is in. "
          "To put numbers on that, we calculated how much direct sunlight reaches a vertical "
          "window facing each direction in Dallas-Fort Worth, Austin and Sherman, on a clear day "
          "at the summer solstice, the fall equinox and the winter solstice.")
        + sec("Direct sun on a window in Dallas-Fort Worth",
            table(["Window faces"] + list(SEASON),
                  [(f, *(f2(D[s][f]) for s in SEASON)) for f in ("North", "East", "South", "West")]),
            p("Figures are kilowatt-hours of direct sunlight per square meter of glass per day, "
              "on a clear day."))
        + sec("What the numbers show",
            p(f"<strong>West windows take about {times('Dallas-Fort Worth')} times the "
              f"direct summer sun of south windows.</strong> In June the midday sun over DFW climbs "
              f"to about {NOON_JUNE_DFW} degrees above the horizon, nearly overhead, so it barely "
              f"reaches into south-facing glass. Afternoon sun comes in low from the west and "
              f"strikes west glass almost head-on."),
            p(f"<strong>North windows get more direct sun than south windows in midsummer.</strong> "
              f"From late spring through summer, the sun rises and sets north of due east and due "
              f"west. North glass catches low sun early in the morning and late in the evening. On "
              f"June 21 it takes {f2(D['June 21']['North'])} kWh per square meter, against "
              f"{f2(D['June 21']['South'])} for south glass."),
            p(f"<strong>South windows get their most sun in winter.</strong> In December the sun "
              f"stays low in the southern sky all day, and south glass takes "
              f"{f2(D['Dec. 21']['South'])} kWh per square meter, more than any wall at any other "
              f"point in the year."),
            p("East and west windows take the same amount of direct sun in this model, because the "
              "sun's path is symmetrical around noon. The difference is timing. East sun arrives "
              "in the cool of the morning. West sun lands in the afternoon, when the air outside "
              "is already at its hottest."))
        + sec("Austin and Sherman",
            table(["City", "West window, June 21", "South window, June 21", "South window, Dec. 21"],
                  [(c, f2(SUN[c]["June 21"]["West"]), f2(SUN[c]["June 21"]["South"]),
                    f2(SUN[c]["Dec. 21"]["South"])) for c in LAT]),
            p(f"The pattern holds across the state, and the summer gap grows the farther south "
              f"you go. In Austin, a west window takes about {times('Austin')} times the "
              f"direct June sun of a south window. In Sherman, near the Oklahoma line, it is "
              f"about {times('Sherman')} times."))
        + sec("What we install on each side",
            p("<strong>North.</strong> Little direct sun for most of the year, so the choice comes "
              "down to privacy and style. Shutters, roman shades and woven wood shades all work. "
              "North-facing bedrooms still need a lining or room-darkening fabric for privacy once "
              "the lights are on."),
            p("<strong>South.</strong> Strong sun in winter, little in summer. Plantation shutters "
              "let you tilt the louvers to send light toward the ceiling, and cellular shades "
              "insulate the glass in both seasons."),
            p("<strong>East.</strong> Direct morning sun that ends by midday. In bedrooms, "
              "room-darkening or blackout shades keep sunrise out. In kitchens and breakfast rooms, "
              "light-filtering shades cut glare and keep the room bright."),
            p("<strong>West.</strong> The hardest exposure in Texas. Solar shades block heat and "
              "glare while keeping the view. Cellular shades insulate when the view matters less. "
              "On large west-facing glass and patios, exterior shades stop the sun before it "
              "reaches the window. Motorized shades on a schedule can lower themselves every "
              "afternoon."))
        + sec("How we calculated this",
            p("We computed the sun's position every minute from sunrise to sunset for each city's "
              "latitude, estimated clear-sky direct sunlight with the standard Meinel air-mass "
              "model, and multiplied it by the angle at which the sun strikes a vertical window. "
              "The figures cover direct sunlight only and leave out diffuse light from the sky and "
              "light reflected off the ground. They are useful for comparing directions. Real days "
              "have clouds, and trees, overhangs and neighboring houses shade many windows.")),
    ),
    faqs=[
        ("Which side of a house gets the most sun in Texas?",
         f"In summer, east and west walls take the most direct sun, and west sun arrives during "
         f"the hottest part of the day. In winter, south walls take the most. In Dallas-Fort "
         f"Worth, a west window gets about {times('Dallas-Fort Worth')} times the direct "
         f"June sun of a south window."),
        ("Do north-facing windows get direct sun in Texas?",
         "Yes, from late spring through summer. The sun rises and sets north of due east and west "
         "then, so north windows catch low sun early and late in the day. At the June solstice "
         "they take slightly more direct sun than south windows."),
        ("What is the best window treatment for a west-facing window in Texas?",
         "Solar shades keep the view while cutting heat and glare, cellular shades add insulation, "
         "and exterior shades stop the sun before it reaches the glass. On large west windows, "
         "motorized shades on an afternoon schedule help."),
    ],
    related=[("Interior vs Exterior Shades for Texas Sun", "/interior-vs-exterior-shades-for-texas-sun"),
             ("Solar Shades vs Blackout Shades", "/solar-shades-vs-blackout-shades"),
             ("Cellular Shades vs Roller Shades for Texas Heat", "/cellular-shades-vs-roller-shades")],
)


# --------------------------------------------------------------- glossary
def terms(*pairs):
    return "".join(f"<p><strong>{t}.</strong> {d}</p>" for t, d in pairs)

post3 = dict(
    slug="window-treatment-terms-glossary",
    title="Window Treatment Terms, Defined in Plain English",
    desc=("Plain-English definitions for the terms on a window treatment quote: mounts, reveal, "
          "openness factor, top-down bottom-up, cellular, panel track and more."),
    hero=L + "shutters-shutters-060-jpg.webp",
    body=(
        p("Window treatment quotes and sample books use a lot of trade terms. This glossary "
          "defines the ones you are most likely to see, grouped by topic.")
        + sec("Types of window treatments", terms(
            ("Blinds", "Treatments made of hard slats that tilt, such as faux wood, real wood and "
             "aluminum. Tilting the slats changes the light without raising the blind."),
            ("Shades", "Treatments made of continuous fabric that raise and lower by rolling, "
             "folding or stacking. Roller, roman, cellular and solar shades are all shades."),
            ("Shutters", "Hinged panels with tilting louvers, mounted to the window frame and "
             "built to the size of the opening."),
            ("Drapery", "Fabric panels hung from a rod or track. Stationary panels frame a window; "
             "traversing panels open and close across it."),
            ("Window treatment store, blinds shop", "Google's business categories for companies "
             "that sell and install window treatments. Some have showrooms. Others, including Love "
             "Is Blinds, bring samples to your home and do the measuring and installation there.")))
        + sec("Mounting and measuring", terms(
            ("Inside mount", "The treatment sits inside the window opening, flush with the wall. "
             "It needs enough depth in the frame to fit the hardware."),
            ("Outside mount", "The treatment attaches to the wall or trim above the opening and "
             "overlaps it. It suits shallow frames and blocks more light at the edges."),
            ("Reveal", "The strip of window frame left visible around an inside-mounted treatment. "
             "An even reveal on every side means the measurement was right."),
            ("Headrail", "The housing across the top of a blind or shade that holds the lift "
             "mechanism and attaches to the mounting brackets."),
            ("Light gap", "The small gap between a treatment's edge and the window frame. Inside "
             "mounts always have one; outside mounts reduce it."),
            ("Out of square", "An opening whose corners are not true right angles, common in homes "
             "whose foundations have shifted. Careful measuring checks the width at the top, "
             "middle and bottom of the opening for this reason.")))
        + sec("Light and privacy", terms(
            ("Light-filtering", "Fabric that lets soft, diffused light through while blocking the "
             "view into the room during the day."),
            ("Room-darkening", "Fabric that blocks most light. The room gets dim but not fully dark."),
            ("Blackout", "Fabric that blocks light completely. How dark the room gets also depends "
             "on the mount, because light can enter around the edges."),
            ("Openness factor", "On solar shades, the percentage of the weave that is open. A lower "
             "percentage blocks more sun and glare and shows less of the view. A higher percentage "
             "keeps more of the view and lets in more light."),
            ("Top-down bottom-up", "A shade with two moving rails, so it opens from the top, the "
             "bottom or both. It lets light in above eye level while covering the lower glass."),
            ("Louver", "One slat of a shutter. Wider louvers give a more open view when tilted.")))
        + sec("Products", terms(
            ("Cellular shades", "Also called honeycomb shades. The fabric forms air-filled cells, "
             "visible as honeycombs from the side, which insulate the window."),
            ("Solar shades", "Roller shades made of a woven screen that cuts heat and glare while "
             "staying see-through from inside."),
            ("Roman shades", "Fabric shades that fold into horizontal pleats as they rise."),
            ("Woven wood shades", "Shades woven from bamboo, rattan, jute and natural grasses. They "
             "filter light, and a liner adds privacy at night."),
            ("Dual shades", "Also called zebra shades. Alternating sheer and solid bands line up "
             "or offset as the shade moves, switching between view and privacy."),
            ("Panel track shades", "Wide fabric panels that slide along a track and stack to one "
             "side. Common on sliding glass doors and wide windows."),
            ("Plantation shutters", "Interior shutters with wide, tilting louvers, mounted to the "
             "window frame."),
            ("Exterior patio shades", "Shades mounted outside, over patios and large glass, that "
             "stop sun before it reaches the window.")))
        + sec("Motorization and lift", terms(
            ("Motorized", "The treatment moves by remote, app, schedule or voice instead of a cord "
             "or wand."),
            ("Rechargeable and hardwired motors", "A rechargeable motor runs on a built-in battery "
             "that is charged periodically. A hardwired motor runs on low-voltage wiring, which is "
             "easiest to plan during construction."),
            ("Cordless", "No pull cords. You raise and lower the treatment by hand from the bottom "
             "rail, so there are no cords within a child's reach.")))
        + sec("On a quote", terms(
            ("Written quote", "The full project price in writing, window by window, including "
             "installation."),
            ("Limited lifetime warranty", "The manufacturer covers factory defects for the life of "
             "the product."),
            ("Transferable warranty", "A warranty that passes to the next owner if you sell the "
             "house."),
            ("Price match", "A promise to match a competitor's written quote for the same product "
             "and job. Ours is called the Apples-to-Apples guarantee.")))
        + p("For terms not listed here, ask the company that wrote your quote to explain them."),
    ),
    faqs=[
        ("What is openness factor on solar shades?",
         "The percentage of the shade's weave that is open. A lower percentage blocks more sun and "
         "glare and shows less of the view; a higher percentage keeps more of the view and lets "
         "in more light."),
        ("What is the difference between inside mount and outside mount?",
         "An inside mount sits within the window opening for a built-in look. An outside mount "
         "attaches to the wall or trim above the opening and overlaps it, which suits shallow "
         "frames and blocks more light at the edges."),
        ("What is the difference between room-darkening and blackout?",
         "Room-darkening fabric blocks most light. Blackout fabric blocks light completely, "
         "although light can still enter around the edges depending on how the shade is mounted."),
    ],
    related=[("Room-Darkening vs Blackout", "/room-darkening-vs-blackout-whats-the-difference"),
             ("Inside Mount vs Outside Mount", "/inside-mount-vs-outside-mount-blinds"),
             ("How to Choose a Patio Shade Openness Factor",
              "/how-to-choose-patio-shade-openness-factor")],
)


def main():
    idx = json.load(open("data/blog-index.json"))
    for ps in (post1, post2, post3):
        body = ps["body"]
        if isinstance(body, tuple):      # trailing comma in the dict literal
            body = "".join(body)
        html_out = NP.render({"slug": ps["slug"], "title": ps["title"], "desc": ps["desc"],
                              "published": TODAY},
                             body, ps["faqs"], ps["hero"], ps["related"])
        assert not body.startswith("("), f"body not joined in {ps['slug']}"
        assert "—" not in html_out, f"em dash in {ps['slug']}"
        open(f"{ps['slug']}.html", "w").write(html_out)
        idx = [x for x in idx if x["url"] != "/" + ps["slug"]]
        idx.append({"url": "/" + ps["slug"], "title": ps["title"], "desc": ps["desc"],
                    "date": TODAY, "img": ps["hero"]})
        print("published:", ps["slug"])
    json.dump(idx, open("data/blog-index.json", "w"), indent=1)


if __name__ == "__main__":
    main()
