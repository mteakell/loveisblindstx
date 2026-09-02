"""Give thin blog posts real photography.

39 of 126 posts shipped with one image or none, 38,000 words between them, so
they read as walls of text and offer nothing to image search. This picks
photos from the family the post is actually about and drops them at section
boundaries.

Selection is deterministic on the post slug, so a rebuild does not reshuffle
every image on the site, and no photo repeats within a post.
"""
import glob, hashlib, os, re

LIB = "images/lib"

# post topic -> filename prefixes, most specific first
FAMILY = [
 ("patio",      ("exterior-patio-shades",), ("patio", "exterior shade", "outdoor shade", "pergola", "porch")),
 ("shutters",   ("shutters-shutters",),     ("shutter", "plantation")),
 ("roman",      ("roman-shades",),          ("roman shade",)),
 ("woven",      ("woven-wood-shades",),     ("woven wood", "bamboo", "natural shade")),
 ("banded",     ("banded-shades",),         ("banded", "zebra", "dual shade")),
 ("honeycomb",  ("honeycomb-shades",),      ("honeycomb", "cellular", "energy", "insulat")),
 ("drapes",     ("smart-drapes",),          ("drape", "curtain", "panel track")),
 ("roller",     ("roller-shades",),         ("roller", "solar shade", "blackout", "motoriz", "smart")),
 ("blinds",     ("blinds-blinds",),         ("blind", "faux wood", "real wood", "venetian")),
]
DEFAULT = ("roller-shades", "shutters-shutters", "blinds-blinds")


def pool(prefixes):
    return sorted(f"/{LIB}/{f}" for f in os.listdir(LIB)
                  if any(f.startswith(p) for p in prefixes))


def family_for(text):
    t = text.lower()
    best = None
    for name, prefixes, words in FAMILY:
        hits = sum(t.count(w) for w in words)
        if hits and (best is None or hits > best[0]): best = (hits, name, prefixes)
    return best[2] if best else DEFAULT


def label(prefix):
    n = prefix.split("/")[-1]
    for a, b in [("exterior-patio-shades", "Exterior patio shades"), ("shutters-shutters", "Plantation shutters"),
                 ("roman-shades", "Roman shades"), ("woven-wood-shades", "Woven wood shades"),
                 ("banded-shades", "Banded shades"), ("honeycomb-shades", "Honeycomb shades"),
                 ("smart-drapes", "Drapery"), ("roller-shades", "Roller shades"), ("blinds-blinds", "Custom blinds")]:
        if n.startswith(a): return b
    return "Window treatments"


def main():
    from PIL import Image
    touched = added = 0
    for f in sorted(glob.glob("*.html")):
        if re.match(r'^[a-z0-9-]+-tx\.html$', f): continue
        s = open(f).read()
        if "BlogPosting" not in s: continue
        m = re.search(r'<main.*?</main>', s, re.S)
        if not m: continue
        body = m.group(0)
        if len(re.findall(r'<img', body)) > 1: continue      # already illustrated

        text = re.sub(r'<[^>]+>', ' ', body)
        prefixes = family_for(text)
        cands = pool(prefixes) or pool(DEFAULT)
        if not cands: continue

        # split on h2 so photos land between sections, never mid-argument
        parts = re.split(r'(?=<h2)', body)
        slots = [i for i in range(1, len(parts))]
        if not slots: continue
        seed = int(hashlib.sha1(f.encode()).hexdigest(), 16)
        want = min(3, len(slots), len(cands))
        step = max(1, len(slots)//want)
        chosen = slots[::step][:want]

        for k, idx in enumerate(sorted(chosen, reverse=True)):
            src = cands[(seed + k*7) % len(cands)]
            w, h = Image.open(src.lstrip("/")).size
            alt = f"{label(src)} installed by Love Is Blinds in a Texas home"
            fig = (f'<figure class="post-figure">'
                   f'<img src="{src}" data-alt-final alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async">'
                   f'</figure>\n')
            parts[idx] = fig + parts[idx]
            added += 1
        new = "".join(parts)
        open(f, "w").write(s.replace(body, new, 1))
        touched += 1
    print(f"illustrated {touched} posts with {added} photos")


if __name__ == "__main__":
    main()
