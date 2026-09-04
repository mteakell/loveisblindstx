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


def main():
    done = []
    if inject("how-it-works.html", "how", [HOW_DETAIL, gtee_band(), review_strip(REVS[:8])]):
        done.append("how-it-works")
    if inject("areas-we-serve.html", "areas", [AREAS_INTRO, review_strip(REVS[8:16])]):
        done.append("areas-we-serve")
    if inject("design-checklist.html", "check", [CHECK_INTRO, gtee_band()]):
        done.append("design-checklist")
    print("enriched:", ", ".join(done))


if __name__ == "__main__":
    main()
