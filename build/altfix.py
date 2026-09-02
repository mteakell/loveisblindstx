"""Post-build alt-text pass.

Two jobs, both of which have to run after every generator because the
converted pages inherit their alt text from the old Duda markup:

  1. no <img> may ship without an alt attribute at all
  2. the same alt string must not describe two different images on one page

Rule 2 matters because repeated alt is keyword repetition with no added
meaning: it tells a crawler and a screen-reader user the same thing twice
about two different photos. Where a duplicate is found, the distinguishing
detail is taken from the image filename, which is usually where the room or
product actually got recorded. If the filename adds nothing, the alt is left
alone rather than padded with noise.

Deliberately NOT touched: alt="" on decorative images. An image inside a
link that already carries its own text should stay silent to assistive tech.
"""
import re, glob, collections

IMG = re.compile(r'<img[^>]*>')
ALT = re.compile(r'alt="([^"]*)"')
SRC = re.compile(r'src="([^"]+)"')


def detail(src):
    """Readable words from an image filename, minus Duda hash and size suffix."""
    n = src.split("/")[-1]
    n = re.sub(r'^[0-9a-f]{8}-', '', n)
    n = re.sub(r'-\d+w\.(jpg|jpeg|png|webp)$|\.(jpg|jpeg|png|webp)$', '', n, flags=re.I)
    n = re.sub(r'[-_]+', ' ', n)
    return re.sub(r'\s+', ' ', n).strip()


def fix(html):
    counts = collections.Counter()
    for t in IMG.findall(html):
        a = ALT.search(t)
        if a and a.group(1).strip(): counts[a.group(1).strip()] += 1
    dupes = {v for v, c in counts.items() if c > 1}
    seen = collections.Counter()
    changed = [0, 0]

    def one(m):
        t = m.group(0)
        src = (SRC.search(t) or ["", ""])[1]
        a = ALT.search(t)
        if not a:                                   # no alt attribute at all
            d = detail(src)
            if not d: return t
            changed[0] += 1
            return t[:-1].rstrip() + f' alt="{d[:1].upper() + d[1:]}">'
        raw = a.group(1)
        v = raw.strip()
        if not v or v not in dupes: return t
        seen[v] += 1
        d = detail(src)
        # An alt repeated across 3+ different images is boilerplate the old
        # site pasted everywhere, and is usually wrong for most of them. Take
        # the filename instead of appending to a description that does not fit.
        if counts[v] >= 3 and d:
            changed[1] += 1
            return t.replace(f'alt="{raw}"', f'alt="{d[:1].upper() + d[1:]}"')
        if seen[v] == 1: return t                   # first use keeps the clean string
        extra = " ".join(w for w in d.split()
                         if w.lower() not in v.lower())[:46].strip(" -")
        if not extra: return t
        changed[1] += 1
        return t.replace(f'alt="{raw}"', f'alt="{v} - {extra}"')

    return IMG.sub(one, html), changed


def main():
    added = diff = pages = 0
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith("build/"): continue
        s = open(f).read()
        out, (a, d) = fix(s)
        if out != s:
            open(f, "w").write(out); pages += 1; added += a; diff += d
    print(f"alt: {added} added, {diff} duplicates differentiated, {pages} pages touched")


if __name__ == "__main__":
    main()
