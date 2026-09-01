"""Footer trust badge, computed from real Google profile data.

The rating is a review-weighted mean across every Love Is Blinds Texas
profile in data/gbp-ratings.json, not a hardcoded number. Profiles with no
reviews count as locations but contribute nothing to the average.

Deliberately NOT emitted as aggregateRating JSON-LD: markup describing your
own business's reviews is self-serving, is ineligible for rich results, and
risks a structured data manual action. Visible on the page is fine and true.
"""
import json, re, glob

BADGE_RE = re.compile(r'<div class="ftrust">.*?</div>\s*', re.S)


def numbers():
    d = json.load(open("data/gbp-ratings.json"))["profiles"]
    rated = [p for p in d if p["reviews"] > 0]
    total = sum(p["reviews"] for p in rated)
    avg = sum(p["rating"] * p["reviews"] for p in rated) / total
    return round(avg, 1), total, len(d)


def badge(avg, total, locations):
    full = int(avg)                       # only draw stars we actually earned
    half = (avg - full) >= 0.5
    stars = "★" * full + ("½" if half else "")
    return (
        f'<div class="ftrust">'
        f'<span class="fstars" aria-hidden="true">{stars}</span>'
        f'<span class="ftrust-text"><strong>{avg} average</strong> from {total} Google '
        f'reviews across {locations} Texas locations</span>'
        f'</div>\n      '
    )


def main():
    avg, total, locations = numbers()
    block = badge(avg, total, locations)

    f = "build/partials/footer.html"
    s = open(f).read()
    s = BADGE_RE.sub("", s)
    anchor = '</p>\n    </div>'                       # end of the .fabout blurb
    assert anchor in s, "footer brand column not found"
    s = s.replace(anchor, '</p>\n      ' + block + '</div>', 1)
    open(f, "w").write(s)

    # push into every already-built page
    new = BADGE_RE.search(s).group(0).rstrip()
    n = 0
    for p in glob.glob("**/*.html", recursive=True):
        if p.startswith("build/"):
            continue
        t = o = open(p).read()
        t = BADGE_RE.sub("", t)
        i = t.find('</p>', t.find('class="fabout"'))
        if i < 0:
            continue
        t = t[:i + 4] + new + t[i + 4:]
        if t != o:
            open(p, "w").write(t); n += 1
    print(f"badge: {avg} from {total} reviews across {locations} locations -> {n} pages")


if __name__ == "__main__":
    main()
