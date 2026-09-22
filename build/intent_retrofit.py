"""Purchase-intent retrofit for the blog's proven traffic winners.

GSC (90 days, mostly pre-migration) showed the posts that pull near-buyers
are problem-to-product posts, but none of them had a consultation CTA above
the fold or an explicit product panel high in the post, so the authority
they earn never reached the /products/ pages ranking in the 50s. This pass:

 1. inserts one compact "What we install for this" band with exact
    product-name anchors + a consultation CTA right after the opening
    answer of each winner (idempotent via the ir-band class);
 2. rewrites the fabric-blinds title/meta to promise a specific answer
    (7.6K impressions, zero clicks was a snippet problem);
 3. retires the two cannibal posts with in-place link rewrites here and
    301s in vercel.json (done once; guarded by file existence).

Runs after convert/crosslinks so a rebuild cannot resurrect anything.
"""
import glob, json, os, re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# slug -> list of (product anchor text, product url); anchor is the exact
# product name so the target page gets its money term as anchor text.
PANEL = {
 "top-10-dog-proof-window-blinds-durable-and-pet-friendly":
   [("Faux Wood Blinds", "/products/faux-wood-blinds"),
    ("Plantation Shutters", "/products/plantation-shutters")],
 "can-you-use-roller-shades-on-a-sliding-glass-door":
   [("Panel Track Shades", "/products/panel-track-shades"),
    ("Roller Shades", "/products/roller-shades")],
 "what-is-the-best-fabric-blinds-for-windows":
   [("Roller Shades", "/products/roller-shades"),
    ("Roman Shades", "/products/roman-shades")],
 "what-are-the-best-window-treatments-for-arched-windows-and-how-do-you-install-them":
   [("Plantation Shutters", "/products/plantation-shutters"),
    ("Honeycomb Shades", "/products/honeycomb-shades")],
 "the-best-curtains-for-angled-windows":
   [("Plantation Shutters", "/products/plantation-shutters"),
    ("Window Treatment Automation", "/products/window-treatment-automations")],
 "what-is-the-best-window-treatment-for-awning-windows":
   [("Roller Shades", "/products/roller-shades"),
    ("Honeycomb Shades", "/products/honeycomb-shades")],
 "affordable-alternatives-to-blinds":
   [("Faux Wood Blinds", "/products/faux-wood-blinds"),
    ("Roller Shades", "/products/roller-shades")],
 "shutters-vs-blinds-which-is-right-for-your-home":
   [("Plantation Shutters", "/products/plantation-shutters"),
    ("Custom Blinds", "/products/blinds")],
 "plantation-shutters-vs-blinds-which-is-the-better-investment-for-your-dfw-home":
   [("Plantation Shutters", "/products/plantation-shutters"),
    ("Custom Blinds", "/products/blinds")],
 "window-blinds-vs-shades-which-one-is-better":
   [("Custom Blinds", "/products/blinds"),
    ("Custom Shades", "/products/shades")],
 "how-to-fix-window-shades-that-won-t-roll-up-or-down-properly":
   [("Motorized Window Treatments", "/products/motorized-window-treatment-automations"),
    ("Roller Shades", "/products/roller-shades")],
 "best-window-treatments-for-media-rooms":
   [("Roller Shades", "/products/roller-shades"),
    ("Motorized Window Treatments", "/products/motorized-window-treatment-automations")],
 "top-10-best-blinds-for-large-windows-functional-window-treatments":
   [("Motorized Window Treatments", "/products/motorized-window-treatment-automations"),
    ("Panel Track Shades", "/products/panel-track-shades")],
}

# retired cannibal -> surviving winner (files deleted, links rewritten,
# 301s live in vercel.json)
RETIRED = {
 "/window-shutters-vs-blinds-which-one-is-better-for-your-home":
   "/shutters-vs-blinds-which-is-right-for-your-home",
 # GSC: can-you-use had 21 clicks at position 13; what-types had 1 at 47.
 # The weaker page folds into the proven winner, not the other way round.
 "/what-types-of-roller-shades-are-best-in-sliding-doors":
   "/can-you-use-roller-shades-on-a-sliding-glass-door",
}

TITLE_FIX = {
 "what-is-the-best-fabric-blinds-for-windows": (
   "Best Fabric for Blinds and Shades on Texas Windows",
   "Which blind and shade fabrics survive Texas sun: the light-filtering, "
   "blackout and solar fabrics we install, where each belongs, and the one "
   "mistake that fades furniture."),
}


def band(slug):
    links = "".join(
        f'<a class="btn btn-secondary btn-sm" href="{u}">{t}</a>'
        for t, u in PANEL[slug])
    return ('<div class="ir-band"><p class="ir-kicker">What we install for this</p>'
            f'<div class="btnrow">{links}'
            '<a class="btn btn-primary btn-sm" href="/schedule-now">'
            'Free in-home consultation</a></div></div>')


def insert_bands():
    n = 0
    for slug in PANEL:
        f = slug + ".html"
        if not os.path.exists(f):
            continue
        s = open(f).read()
        if 'class="ir-band"' in s:
            continue
        i = s.find('class="post-body"')
        if i < 0:
            continue
        # after the opening answer: first </p> that is not the TLDR label
        j = s.find("</p>", i)
        if "TLDR" in s[i:j] or "TL;DR" in s[i:j]:
            j = s.find("</p>", j + 4)
        if j < 0:
            continue
        j += len("</p>")
        s = s[:j] + band(slug) + s[j:]
        open(f, "w").write(s)
        n += 1
    print(f"intent bands inserted on {n} posts")


def fix_titles():
    for slug, (title, desc) in TITLE_FIX.items():
        f = slug + ".html"
        if not os.path.exists(f):
            continue
        s = o = open(f).read()
        s = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", s, count=1)
        s = re.sub(r'(<meta name="description" content=")[^"]*(")',
                   lambda m: m.group(1) + desc + m.group(2), s, count=1)
        s = re.sub(r'(<meta property="og:title" content=")[^"]*(")',
                   lambda m: m.group(1) + title + m.group(2), s, count=1)
        s = re.sub(r'(<meta (?:property="og:description"|name="twitter:description") content=")[^"]*(")',
                   lambda m: m.group(1) + desc + m.group(2), s)
        s = re.sub(r'(<meta name="twitter:title" content=")[^"]*(")',
                   lambda m: m.group(1) + title + m.group(2), s, count=1)
        if s != o:
            open(f, "w").write(s)
            print(f"title/meta rewritten: {slug}")


def retire():
    # rewrite links everywhere, then remove the files
    n = 0
    for f in glob.glob("**/*.html", recursive=True) + glob.glob("data/queued-posts/*.html"):
        if f.startswith("build/"):
            continue
        s = o = open(f).read()
        for old, new in RETIRED.items():
            s = s.replace(f'href="{old}"', f'href="{new}"')
        if s != o:
            open(f, "w").write(s); n += 1
    for old in RETIRED:
        p = old.lstrip("/") + ".html"
        if os.path.exists(p):
            os.remove(p)
            print(f"retired: {p}")
    idx = json.load(open("data/blog-index.json"))
    idx = [x for x in idx if x["url"] not in RETIRED]
    json.dump(idx, open("data/blog-index.json", "w"), indent=1)
    print(f"links rewritten on {n} pages; blog index now {len(idx)} posts")


if __name__ == "__main__":
    insert_bands()
    fix_titles()
    retire()
