"""Give every local <img> its intrinsic width and height.

Without them the browser cannot reserve space before the image loads, so the
page reflows as each one arrives. That is Cumulative Layout Shift, and it is
a Core Web Vitals ranking factor.

Values are read from the real files, never guessed. The CSS carries a
zero-specificity `:where(img[width][height]){height:auto}` so adding the
attributes cannot override a rule that sizes an image deliberately.
"""
import re, os, glob
from PIL import Image

IMG = re.compile(r'<img[^>]*>')
SRC = re.compile(r'src="([^"]+)"')
_size = {}


def size(path):
    if path not in _size:
        try: _size[path] = Image.open(path).size
        except Exception: _size[path] = None
    return _size[path]


def fix(html):
    n = [0]
    def one(m):
        t = m.group(0)
        if re.search(r'\bwidth=', t) and re.search(r'\bheight=', t): return t
        s = SRC.search(t)
        if not s or not s.group(1).startswith("/"): return t
        wh = size(s.group(1).lstrip("/"))
        if not wh: return t
        t = re.sub(r'\s+(width|height)="[^"]*"', '', t)      # drop a lone one
        n[0] += 1
        return t[:-1].rstrip() + f' width="{wh[0]}" height="{wh[1]}">'
    return IMG.sub(one, html), n[0]


def main():
    tot = pages = 0
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith("build/"): continue
        s = open(f).read()
        out, n = fix(s)
        if n: open(f, "w").write(out); tot += n; pages += 1
    print(f"dimensions added to {tot} images across {pages} pages")


if __name__ == "__main__":
    main()
