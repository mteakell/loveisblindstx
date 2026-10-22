"""Two Duda-migration leftovers, cleaned on every page.

1. Meta descriptions cut mid-word. The migration sliced descriptions at a
   fixed length, so ~45 pages showed Google text like "...window treatm".
   A description that is 140+ characters and does not end in punctuation or
   a digit is treated as cut: it is trimmed back to its last full sentence
   when that leaves 70+ characters, otherwise to its last whole word (minus
   any dangling "and", "with", "of"...) and closed with a period. The same
   string is replaced in og:description, twitter:description and JSON-LD.
2. Empty <h3></h3> / <h3><br></h3> tags (600+ across ~50 old posts). They
   add nothing for readers and break the heading outline.

Idempotent: a fixed description ends in punctuation, and removed tags are gone.
Found by the Oct 2026 Solar Shield blog comparison.
"""
import glob, html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

EMPTY_H3 = re.compile(r"<h3[^>]*>\s*(?:<br\s*/?>|&nbsp;|\s)*</h3>")
DANGLING = {"and", "or", "with", "of", "to", "the", "a", "an", "for", "in", "your", "our", "at",
            "by", "on", "from", "that", "while", "into", "&"}


def trim(d):
    if len(d) < 140 or re.search(r"[.!?)\"”\d]$", d):
        return d
    ends = [m.end() for m in re.finditer(r"[.!?](?=\s|$)", d)]
    if ends and ends[-1] >= 70:
        return d[:ends[-1]].strip()
    words = d.split()[:-1]                      # drop the cut fragment
    while words and words[-1].lower().strip(",;:") in DANGLING:
        words.pop()
    return " ".join(words).rstrip(",;:-") + "."


# Post titles the old generators chopped at 60 characters mid-phrase
# ("...The Real Window Treatment"). Written by hand to fit, keyed by slug.
TITLES = {
 "affordable-alternatives-to-blinds": "Affordable Alternatives to Blinds | Love Is Blinds",
 "honeycomb-vs-panel-track-shades-which-is-best-for-your-home": "Honeycomb vs Panel Track Shades: Which Is Best?",
 "how-do-cordless-window-blinds-work": "How Do Cordless Window Blinds Work? | Love Is Blinds",
 "how-to-choose-window-treatments-that-boost-your-homes-curb-appeal": "Window Treatments That Boost Curb Appeal | Love Is Blinds",
 "how-to-fix-window-shades-that-won-t-roll-up-or-down-properly": "How to Fix Shades That Won't Roll Up or Down",
 "how-to-match-your-window-treatments-to-different-home-decor-styles": "Matching Window Treatments to Your Decor Style",
 "in-home-window-treatment-consultations-in-texas": "Free In-Home Window Treatment Consultations in Texas",
 "plantation-shutters-vs-blinds-which-is-the-better-investment-for-your-dfw-home": "Plantation Shutters vs Blinds: Better Investment in DFW?",
 "the-shift-to-cordless-window-treatments": "Why Cordless Blinds Are the New Safety Standard",
 "top-10-dog-proof-window-blinds-durable-and-pet-friendly": "Top 10 Dog-Proof Window Blinds | Love Is Blinds",
 "what-are-the-best-window-treatments-for-arched-windows-and-how-do-you-install-them": "Best Window Treatments for Arched Windows | Love Is Blinds",
 "why-motorized-window-treatments-are-perfect-for-dallas-luxury-homes": "Motorized Window Treatments for Dallas Luxury Homes",
 "why-pvc-blinds-are-a-top-choice-for-outdoor-patios-windows": "Why PVC Blinds Work for Outdoor Patios | Love Is Blinds",
 "what-are-the-best-window-treatments-for-homes-in-sherman-tx": "Best Window Treatments for Sherman, TX Homes",
 "motorized-blinds-not-responding-checklist": "Motorized Blinds Not Responding? A Simple Checklist",
 "top-down-bottom-up-shades-explained": "Top-Down Bottom-Up Shades: How They Work",
 "battery-vs-hardwired-vs-solar-motorized-shades": "Battery vs Solar vs Hardwired Motorized Shades",
 "standard-window-sizes-texas-why-custom-wins": "Standard Window Sizes in Texas, and Why Custom Wins",
 "shutters-for-bathrooms-moisture-privacy": "Shutters for Bathrooms: Moisture, Privacy, Faux Wood",
 "window-treatments-new-construction-timing": "New Construction Window Treatments: What to Order",
 "solar-screens-vs-window-film-vs-exterior-shades": "Solar Screens vs Window Film vs Exterior Shades",
 "how-long-from-order-to-install": "How Long From Order to Install? The Real Timeline",
 "screened-porch-vs-motorized-patio-shades": "Screened Porch vs Motorized Patio Shades",
}


def fix_title(path, u):
    slug = os.path.basename(path)[:-5]
    new = TITLES.get(slug)
    if not new:
        return u
    m = re.search(r"<title>(.*?)</title>", u, re.S)
    if not m:
        return u
    old_raw = m.group(1)
    new_raw = html.escape(new, quote=False)
    if old_raw == new_raw:
        return u
    u = u.replace(f"<title>{old_raw}</title>", f"<title>{new_raw}</title>", 1)
    for prop in ("og:title", "twitter:title"):
        u = re.sub(r'(<meta (?:property|name)="' + prop + r'" content=")' + re.escape(old_raw) + '"',
                   lambda mm: mm.group(1) + html.escape(new, quote=True) + '"', u)
    return u


def main():
    pages = [f for f in glob.glob("**/*.html", recursive=True)
             if not f.startswith(("build/", "node_modules/"))]
    fixed_desc = fixed_h3 = 0
    for f in pages:
        t = open(f, encoding="utf-8").read()
        u, n = EMPTY_H3.subn("", t)
        fixed_h3 += n
        u = fix_title(f, u)
        m = re.search(r'<meta name="description" content="([^"]*)"', u)
        if m:
            raw = m.group(1)
            old = html.unescape(raw)
            new = trim(old)
            if new != old:
                fixed_desc += 1
                for o, nn in ((raw, html.escape(new, quote=True)),
                              (old, new),
                              (json_escape(old), json_escape(new))):
                    u = u.replace(o, nn)
        if u != t:
            open(f, "w", encoding="utf-8").write(u)
    print(f"metafix: {fixed_desc} descriptions trimmed, {fixed_h3} empty h3 removed")


def json_escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


if __name__ == "__main__":
    main()
