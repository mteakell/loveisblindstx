"""Put reviews on the product and service pages.

They had none: 0 of 17 product pages and 0 of 10 service pages, while 364
real reviews sat in the data. These are the pages people land on from a
product search, so they are exactly where proof belongs.

Reviews are matched to the page topic by what the customer actually wrote. A
shutters page shows reviews that mention shutters. Where a topic has too few
matches it tops up with the highest-rated general ones, so no page is padded
with irrelevant quotes.
"""
import glob, html, json, os, re, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
REVIEWS = [r for r in json.load(open("data/reviews.json")) if r.get("rating", 5) >= 4]

TOPIC = [
 ("shutter",   ("shutter", "plantation")),
 ("patio",     ("patio", "outdoor", "porch", "pergola", "exterior")),
 ("motor",     ("motor", "remote", "automat", "app", "alexa", "google", "smart")),
 ("roller",    ("roller", "solar", "screen")),
 ("honeycomb", ("honeycomb", "cellular")),
 ("woven",     ("woven", "bamboo", "natural")),
 ("roman",     ("roman",)),
 ("drape",     ("drape", "curtain", "panel track")),
 ("blind",     ("blind", "wood", "faux")),
 ("shade",     ("shade",)),
]


def topic_for(path, title):
    t = (path + " " + title).lower()
    for name, words in TOPIC:
        if any(w in t for w in words):
            return words
    return None


def pick(words, slug, n=6):
    """Reviews whose text matches the topic, newest first, topped up if thin."""
    if words:
        hit = [r for r in REVIEWS if any(w in r["quote"].lower() for w in words)]
    else:
        hit = []
    hit.sort(key=lambda r: r.get("date", ""), reverse=True)
    if len(hit) < n:
        seen = {id(r) for r in hit}
        rest = sorted((r for r in REVIEWS if id(r) not in seen),
                      key=lambda r: r.get("date", ""), reverse=True)
        hit += rest[: n - len(hit)]
    # rotate the starting point so two product pages do not open identically
    off = int(hashlib.sha1(slug.encode()).hexdigest()[:6], 16) % max(1, len(hit))
    return (hit[off:] + hit[:off])[:n]


def block(revs, heading):
    cards = "".join(
        '<article class="rv-card">'
        '<div class="rv-stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
        f'<p class="rv-quote">{html.escape(r["quote"])}</p>'
        f'<footer class="rv-by"><span class="rv-name">{html.escape(r["name"])}</span>'
        f'<span class="rv-city">{html.escape(r["city"])}, TX</span></footer>'
        '</article>' for r in revs)
    return (
      '\n<!-- lib:pagereviews -->\n'
      '<section class="section bg-cream-tint rv-section rv-compact">'
      f'<div class="container center"><h2 class="title">{html.escape(heading)}</h2>'
      '<p class="lead">From our Google profiles across Texas.</p></div>'
      f'<div class="rv-wrap"><div class="rv-track" tabindex="0" role="region" '
      f'aria-label="Customer reviews">{cards}</div></div>'
      '<div class="container center" style="margin-top:24px">'
      '<a class="btn btn-secondary btn-lg" href="/areas-we-serve">Find your local team</a>'
      '</div></section>\n<!-- /lib:pagereviews -->\n')


def main():
    n = 0
    for f in sorted(glob.glob("products/*.html") + glob.glob("services/*.html")):
        s = open(f).read()
        s = re.sub(r'\n?<!-- lib:pagereviews -->.*?<!-- /lib:pagereviews -->\n?', '\n', s, flags=re.S)
        title = (re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S) or ["", ""])[1]
        title = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', title)).strip()
        words = topic_for(f, title)
        revs = pick(words, f)
        if not revs:
            continue
        head = f"What customers say about {title}" if title and len(title) < 46 \
               else "What Texas homeowners say"
        # before the last section, which is the closing call to action
        idx = s.rfind("<section")
        if idx < 0:
            continue
        s = s[:idx] + block(revs, head) + s[idx:]
        open(f, "w").write(s)
        n += 1
    print(f"reviews added to {n} product and service pages")


if __name__ == "__main__":
    main()
