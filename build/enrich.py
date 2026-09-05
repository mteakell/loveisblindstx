"""Enrich the thin converted pages.

how-it-works, design-checklist and areas-we-serve came through the Duda
conversion with 280 to 430 words and no imagery beyond the hero. Each gets
substance that already exists elsewhere in the build: the guarantees, the
process, real reviews, and written copy where a section needs it. Markers
keep it idempotent.
"""
import json, html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
G = json.load(open("data/guarantees.json"))["guarantees"]
REVS = sorted((r for r in json.load(open("data/reviews.json")) if r.get("rating", 5) >= 4),
              key=lambda r: r.get("date", ""), reverse=True)

import sys
sys.path.insert(0, "build")
import icons as IC


def gtee_band():
    cards = "".join(
        f'<div class="type-card">{IC.guarantee_icon(g["id"])}<div class="pbody">'
        f'<h3>{html.escape(g["name"])}</h3><p>{html.escape(g["text"])}</p></div></div>' for g in G)
    return ('<section class="section bg-cream-tint"><div class="container center">'
            '<h2 class="title">Every job is backed five ways</h2></div>'
            f'<div class="container"><div class="prod-grid gtee-grid">{cards}</div></div></section>')


def review_strip(revs, heading="What Texas homeowners say"):
    cards = "".join(
        '<article class="rv-card"><div class="rv-stars" aria-hidden="true">'
        '&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
        f'<p class="rv-quote">{html.escape(r["quote"])}</p>'
        f'<footer class="rv-by"><span class="rv-name">{html.escape(r["name"])}</span>'
        f'<span class="rv-city">{html.escape(r["city"])}, TX</span></footer></article>' for r in revs)
    return ('<section class="section rv-section rv-compact"><div class="container center">'
            f'<h2 class="title">{html.escape(heading)}</h2></div>'
            f'<div class="rv-wrap"><div class="rv-track" tabindex="0" role="region" '
            f'aria-label="Customer reviews">{cards}</div></div></section>')


HOW_DETAIL = ('<section class="section"><div class="container split media-right">'
 '<div class="body"><h2 class="title">What actually happens at each step</h2>'
 '<div class="prose">'
 '<p>The consultation is a working visit, not a sales call. Samples come to your door so fabric '
 'and finish get judged in your light, and we talk through each room by what it has to do: the '
 'west wall that overheats, the bedroom that has to go dark, the slider everyone uses.</p>'
 '<p>Measuring happens the same visit. Every opening is measured on site by the person who will '
 'stand behind the numbers, because a custom treatment is cut to a measurement and a wrong one is '
 'not returnable. Out-of-square openings, shallow frames and tall panels get flagged here, while '
 'the fix is still a decision rather than a problem.</p>'
 '<p>The quote is written, covers installation, and does not move. Most orders arrive within two '
 'to four weeks of approval. The team that measured comes back to install, operates every '
 'treatment with you, and anything that does not match the approved measurements is remade and '
 'reinstalled at no cost.</p></div></div>'
 '<div class="media"><img src="/images/lib/roller-shades-home-hero-shades-1-jpeg.webp" '
 'data-alt-final alt="A bright Texas living room with custom roller shades by Love Is Blinds" '
 'width="2000" height="1500" loading="lazy"></div></div></section>')

AREAS_INTRO = ('<section class="section"><div class="container split media-right">'
 '<div class="body"><h2 class="title">One standard, three local teams</h2>'
 '<div class="prose">'
 '<p>Love Is Blinds Texas is three locally owned franchises: Durrell Glick across DFW and the '
 'Mid-Cities, Jake Wade and Jonathan Arosemena across North Texas, and Danny Rohweder across East '
 'and Central Texas down through Waco to the Austin metro. Whichever city you call from, you '
 'reach the team that will actually measure and install your windows.</p>'
 '<p>Every territory works the same way: a free in-home consultation with samples, measurements '
 'taken on site, a written quote that covers installation, and the same five guarantees behind '
 'the job. The city pages below carry each area&#39;s local number, its reviews and its map.</p>'
 '</div></div>'
 '<div class="media"><img src="/images/lib/shutters-shutters-151-jpg.webp" data-alt-final '
 'alt="Open plantation shutters over a Texas lake view, installed by Love Is Blinds" '
 'width="2000" height="1500" loading="lazy"></div></div></section>')

CHECK_INTRO = ('<section class="section"><div class="container center">'
 '<h2 class="title">Why we ask before we visit</h2>'
 '<p class="lead" style="max-width:66ch">A few answers ahead of the consultation mean we arrive '
 'with the right samples instead of a little of everything. Nothing here commits you to '
 'anything: it just makes the visit sharper, and it is the fastest path to a written quote for '
 'the windows you actually have.</p></div></section>')



# ---------------------------------------------------------------- faqs page
FAQ_GROUPS = [
 ("Cost and quotes", [
  ("How much do custom blinds, shades or plantation shutters cost?",
   "There is no honest flat answer, because custom treatments are priced from the opening: its size, "
   "the material, inside or outside mount, and whether you motorize. What we can promise is the shape "
   "of the number: the quote is written, it includes professional installation, and the amount you "
   "approve is the amount you pay. The free in-home consultation exists to turn your actual windows "
   "into an actual price."),
  ("Is the consultation really free?",
   "Yes. The visit, the measuring and the written quote cost nothing and commit you to nothing. We "
   "bring samples so fabric and finish get judged in your own light rather than a showroom's."),
  ("Can you match a competitor's quote?",
   "Yes. We offer an apples-to-apples price match: a like-for-like quote from another company is "
   "something to bring to the consultation, not something to negotiate around."),
  ("Is there a minimum order?",
   "No. Single windows are a normal job, and plenty of customers do a room at a time. For every ten "
   "window treatments you purchase we replace one free, so staged whole-house projects earn that as "
   "they go."),
 ]),
 ("The process", [
  ("Do you really come to my home for the consultation?",
   "Yes, every time. Samples come to your door, every opening is measured on site by the team that "
   "will install, and the quote is written from those measurements. Most customers never visit a "
   "showroom because there is nothing there your own windows cannot tell us better."),
  ("How long does it take from consultation to install?",
   "Most custom orders arrive within two to four weeks of approving the quote. Motorized treatments "
   "can run longer. The timeline is confirmed in writing on your quote, and the team that measured "
   "returns to install."),
  ("What if a treatment does not fit?",
   "We measured it, so we correct it. Anything that does not match the approved measurements is "
   "remade and reinstalled at no cost to you. That is the point of measuring every opening ourselves."),
  ("Who actually shows up?",
   "The local owner-operator. Love Is Blinds Texas is three locally owned franchises: Durrell Glick "
   "across DFW, Jake Wade and Jonathan Arosemena across North Texas, and Danny Rohweder across East "
   "and Central Texas. The person who quotes your windows is the person who installs them."),
 ]),
 ("Products for Texas conditions", [
  ("Which window treatments handle Texas heat best?",
   "Stop the sun before it enters. Exterior patio shades block heat at the outside face of the glass, "
   "which no interior treatment can do. Inside, honeycomb shades insulate by trapping air in their "
   "cells, and solar screen roller shades cut glare and heat while keeping the view."),
  ("What works in humid rooms like bathrooms and kitchens?",
   "Faux wood and composite. Real wood moves with moisture and will warp over a sink or in steam, so "
   "we specify the materials that hold their shape even when wood is the prettier answer."),
  ("Do you offer motorized or smart shades?",
   "Yes: remote, wall switch, app, voice and scheduled control, in battery and hardwired versions, "
   "plus retrofit motorization for some existing treatments. Motorization earns its keep on high "
   "windows, wide banks of glass and exterior shades that should move on a schedule."),
  ("Are your window treatments child and pet safe?",
   "Cordless lift and motorization remove the loop entirely, and that is what we recommend for any "
   "room children use. A cord cleat is a reminder to be careful; a cordless lift is a solution."),
  ("Do you handle specialty shapes like arches and angled windows?",
   "Yes. Shaped openings are a frame and mount problem rather than a fabric one, which is exactly "
   "why we measure on site instead of working from a list."),
 ]),
 ("Choosing and design", [
  ("Will you help me choose, or just quote what I ask for?",
   "We help you choose, and we will tell you when you are overspending. A guest room used a few "
   "nights a year does not need what a west-facing living room needs, and saying so at the "
   "consultation is part of the job. Samples come to your home so decisions happen in your own "
   "light."),
  ("Can window treatments actually lower my electric bill?",
   "The right ones, on the right glass, yes. Honeycomb shades insulate by trapping air in their "
   "cells, solar screens cut heat at the window, and exterior patio shades stop sun before it "
   "reaches the glass at all. The savings live on the west- and south-facing windows, which is "
   "where we focus them."),
  ("Which treatments suit my style of home?",
   "Plantation shutters carry traditional and farmhouse homes and read well from the street. "
   "Roller and banded shades suit modern builds with big glass. Woven woods bring texture to lake "
   "and ranch houses. The consultation settles it faster than a catalogue, because we are looking "
   "at your rooms, not a showroom's."),
  ("Do you have showrooms I can visit?",
   "No, and that is deliberate. The showroom comes to you: samples at your door, held against "
   "your own walls and your own light, which is the only place fabric and stain decisions are "
   "reliable."),
  ("Do you offer financing?",
   "Ask at the consultation and we will walk through what is available. What we promise up front "
   "is simpler: the written quote you approve is the amount you pay, with no movement after."),
  ("Can you work within my budget?",
   "Yes. Custom has a wider price range than people expect, and there is almost always a "
   "combination of material and lift that lands inside a real number. Tell us the budget at the "
   "consultation and we will design to it rather than around it."),
 ]),
 ("Coverage and after the install", [
  ("What areas of Texas do you serve?",
   "Three territories cover the state: DFW and the Mid-Cities, North Texas from Denton up to "
   "Sherman, and East and Central Texas through Tyler, Corsicana, Gun Barrel City and Waco down to "
   "the Austin metro. If you are anywhere near a town on our service areas page, we come to you, "
   "and each area lists its own local phone number."),
  ("What happens if something breaks after installation?",
   "Two layers. Factory defects are covered for life by the manufacturer's limited lifetime "
   "warranty. On top of that, our four-year service guarantee means we come out and service your "
   "blinds, shades or shutters at no cost."),
  ("Does the warranty survive selling the house?",
   "Yes. Our warranties transfer to the new owner, so the cover stays with the windows rather than "
   "expiring with the move."),
  ("How disruptive is installation day?",
   "A few hours for most homes. We work room by room, clean up behind ourselves, and operate every "
   "treatment with you before we leave."),
 ]),
]

def inject(path, marker, blocks, before="<footer"):
    s = open(path).read()
    s = re.sub(rf'\n?<!-- enrich:{marker} -->.*?<!-- /enrich:{marker} -->\n?', '\n', s, flags=re.S)
    payload = f'\n<!-- enrich:{marker} -->\n' + "".join(blocks) + f'\n<!-- /enrich:{marker} -->\n'
    i = s.find('<section class="section closing-cta"')
    if i < 0:
        i = s.find(before)
    if i < 0:
        return False
    open(path, "w").write(s[:i] + payload + s[i:])
    return True



# ------------------------------------------------ thin pages: brands, about
BRANDS_DEPTH = ('<section class="section"><div class="container" style="max-width:880px">'
 '<h2 class="title">The options that actually shape the quote</h2>'
 '<div class="prose">'
 '<p>Every product line we carry comes in more configurations than any showroom wall can '
 'show. These are the four decisions that matter at your windows, and the consultation '
 'exists to walk you through each one with samples in hand.</p>'
 '<p><b>Light control.</b> The same shade fabric runs from light-filtering to full blackout, '
 'and liners change what a roman or roller shade does after dark. Bedrooms usually want '
 'room-darkening or blackout; living spaces usually want the glow of light-filtering with '
 'privacy at night.</p>'
 '<p><b>Lift and safety.</b> Cordless lift is the standard we quote for homes with kids and '
 'pets. From there the step up is motorization: remote, wall switch, app, or a schedule, '
 'which earns its keep on tall windows and hard-to-reach glass.</p>'
 '<p><b>Material.</b> Faux wood shrugs off steam in kitchens and baths; real wood keeps its '
 'lines on big living-room windows; woven naturals bring texture; honeycomb cells insulate '
 'against Texas heat coming off the glass.</p>'
 '<p><b>Fit and mount.</b> Inside mount sits flush and tailored when the frame is deep and '
 'square; outside mount hides an uneven opening and makes a window read larger. We measure '
 'for both and tell you which your windows want.</p>'
 '</div></div></section>'
 '<section class="section bg-cream-tint"><div class="container" style="max-width:880px">'
 '<h2 class="title">Manufacturer warranties, serviced by the people who installed it</h2>'
 '<div class="prose">'
 '<p>Everything we sell carries its manufacturer warranty, and the difference with Love Is '
 'Blinds is who handles it. A warranty claim goes to the owner-operator who measured and '
 'installed your windows, not a national call queue. On top of the manufacturer cover, our '
 'own guarantees apply to every job: the Limited Lifetime Warranty, Apples-to-Apples '
 'pricing, Our GuaranTEN, Here-4-You service, and a Transferable Warranty if you sell the '
 'home.</p>'
 '<p>That is also why we do not push one brand on every house. The right product line '
 'depends on the window, the room, and the budget, and the free in-home consultation is '
 'where those three meet. <a href="/schedule-now">Book yours</a> and see the options at '
 'your own windows.</p>'
 '</div></div></section>')

ABOUT_DEPTH = ('<section class="section"><div class="container" style="max-width:880px">'
 '<h2 class="title">Three territories, three owners, one standard</h2>'
 '<div class="prose">'
 '<p>Durrell Glick runs the DFW franchise. Jake Wade and Jonathan Arosemena run North '
 'Texas, from the northern suburbs up through Sherman and Gainesville. Danny Rohweder '
 'covers East and Central Texas, from Tyler across to Waco and down to the Austin metro. '
 'Each one quotes, measures, and installs in his own territory, so the person at your '
 'kitchen table on day one is the same person who stands behind the work in year five.</p>'
 '<p>The process is the same in every territory: a free in-home consultation with samples '
 'at your windows, measurements taken by us, a written quote with no games, a custom order '
 'built to those numbers, and an installation by the team that took the measurements. '
 'The details are on our <a href="/how-it-works">how it works</a> page.</p>'
 '<p>Every job is backed five ways: the Limited Lifetime Warranty, Apples-to-Apples '
 'pricing, Our GuaranTEN, Here-4-You service, and a Transferable Warranty that follows '
 'the house if you sell. And the record is public: hundreds of five-star Google reviews '
 'across our Texas locations, many of them quoted throughout this site with the city and '
 'reviewer they came from.</p>'
 '</div></div></section>')


TEAM_DEPTH = ('<section class="section"><div class="container" style="max-width:880px">'
 '<h2 class="title">What owner-operated actually means for your project</h2>'
 '<div class="prose">'
 '<p>Most window treatment companies split the job three ways: a salesperson quotes it, a '
 'subcontractor installs it, and a call center answers for it afterward. Love Is Blinds '
 'does not. The owner you meet at the consultation takes the measurements himself, orders '
 'to those exact numbers, and is on the install. If a shade needs adjusting six months '
 'later, the person who answers has stood in your living room.</p>'
 '<p>It also means the advice is accountable. Nobody here earns a commission for pushing '
 'the most expensive line; the same person who recommends a product has to install it, '
 'service it, and live in the same town as the review you leave afterward. That is why '
 'the reviews across our Texas profiles keep saying the same three things: on time, '
 'clean install, honest recommendation.</p>'
 '<p>Read the bios above, then <a href="/schedule-now">book a free consultation</a> and '
 'meet the owner who covers your city, or find your team on the '
 '<a href="/areas-we-serve">service areas map</a>.</p>'
 '</div></div></section>')


def rebuild_faqs():
    """Rebuild the FAQ page body: grouped, answer-first, with FAQPage schema.

    The page had ten 36-word answers, no FAQPage JSON-LD at all, and promoted
    commercial work, which is off the roster. Answers are written to stand
    alone when quoted, because that is how AI search lifts them.
    """
    s = open("faqs.html").read()
    qs = []
    slug = lambda g: re.sub(r"[^a-z]+", "-", g.lower()).strip("-")
    chips = "".join(
        f'<a class="chip" href="#faq-{slug(g)}">{html.escape(g)} '
        f'<span class="sml">{len(items)}</span></a>' for g, items in FAQ_GROUPS)
    secs = ('<section class="section faq-nav"><div class="container center">'
            f'<div class="faq-chips">{chips}</div></div></section>')
    for gi, (group, items) in enumerate(FAQ_GROUPS):
        faqs_html = "".join(
            f'<details><summary>{html.escape(q)}</summary>'
            f'<div class="a">{html.escape(a)}</div></details>' for q, a in items)
        tint = ' bg-cream-tint' if gi % 2 else ''
        secs += (f'<section class="section{tint}" id="faq-{slug(group)}">'
                 f'<div class="container center"><h2 class="title">{html.escape(group)}</h2></div>'
                 f'<div class="container"><div class="faq faq-grid">{faqs_html}</div></div></section>')
        qs += items
    secs += (
        '<section class="ed-split bg-cream-tint"><div class="ed-inner">'
        '<div class="ed-media"><img src="/images/lib/honeycomb-shades-honeycomb-shades-018-jpg.webp" '
        'data-alt-final alt="Honeycomb shades softening afternoon light in a Texas living room" '
        'loading="lazy" width="2000" height="1500"></div>'
        '<div class="ed-card"><p class="ed-eyebrow">Still have a question?</p>'
        '<h2>Ask the owner, not a call center</h2>'
        '<p>Call and you reach the owner-operator who covers your city. Or book the free '
        'consultation and ask everything at your own windows, with samples in hand.</p>'
        '<div class="btnrow"><a class="btn btn-primary" href="/schedule-now">Book your free '
        'consultation</a><a class="btn btn-secondary" href="tel:+18665182999">Call (866) 518-2999'
        '</a></div></div></div></section>')
    node = {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}}
                           for q, a in qs]}
    payload = ('\n<!-- enrich:faq -->\n' + secs +
               '<script type="application/ld+json">' + json.dumps(node) + '</script>'
               '\n<!-- /enrich:faq -->\n')
    s = re.sub(r'\n?<!-- enrich:faq -->.*?<!-- /enrich:faq -->\n?', '\n', s, flags=re.S)
    # the converted page parked its dark CTA band directly under the hero;
    # the ask-the-owner split is the closer now, so the band goes entirely
    s = re.sub(r'<section class="section bg-deep">\s*<div class="container center">\s*'
               r'<h2 class="title">Ready to love the way your home feels\?'
               r'(?:(?!</section>).)*</section>\s*', '', s, flags=re.S)
    # remove the old flat FAQ block: every details element outside our marker
    s = re.sub(r'<section[^>]*>(?:(?!</section>).)*<details(?:(?!</section>).)*</section>', '', s, flags=re.S)
    i = s.find('<section class="section closing-cta"')
    if i < 0: i = s.find("<footer")
    s = s[:i] + payload + s[i:]
    open("faqs.html", "w").write(s)
    print(f"faqs: {len(qs)} questions in {len(FAQ_GROUPS)} groups, FAQPage schema emitted")


def main():
    done = []
    if inject("how-it-works.html", "how", [HOW_DETAIL, gtee_band(), review_strip(REVS[:8])]):
        done.append("how-it-works")
    if inject("areas-we-serve.html", "areas", [AREAS_INTRO, review_strip(REVS[8:16])]):
        done.append("areas-we-serve")
    if inject("design-checklist.html", "check", [CHECK_INTRO, gtee_band()]):
        done.append("design-checklist")
    if inject("brands.html", "brandsdepth", [BRANDS_DEPTH]):
        done.append("brands")
    if inject("about.html", "aboutdepth", [ABOUT_DEPTH]):
        done.append("about")
    if inject("meet-the-team.html", "teamdepth", [TEAM_DEPTH], before="<footer"):
        done.append("meet-the-team")
    rebuild_faqs()
    print("enriched:", ", ".join(done))


if __name__ == "__main__":
    main()
