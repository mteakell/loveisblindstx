"""Done-gate checks for the hand-written city pages (copy files, before render).

  python3 build/check_city_copy.py            all copy files
Checks: dashes and banned phrases, desc length with phone, 6-gram overlap
between every pair of rewritten pages, photos (exist, sizes, reuse), links
that point at real files, required keys.
Exit 1 on any hard failure.
"""
import glob, importlib, itertools, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(ROOT)

from houston_towns_copy import TOWNS, EXTRA
entries = [(t, EXTRA[t["slug"]], "houston") for t in TOWNS]
for f in sorted(glob.glob("build/city_copy_batch*.py")):
    m = importlib.import_module(os.path.basename(f)[:-3])
    entries += [(t, t["extra"], os.path.basename(f)[:-3]) for t in m.CITIES]

BANNED = re.compile(r"[\u2013\u2014]|\bhonest|not just|isn.t just|\bit.s not\b|whether you|ready to|look no further|"
                    r"elevate|seamless|peace of mind|so you can|\w, not (a |an |the )?\w+[.,]", re.I)
hard, soft = [], []


def text_of(t, x):
    parts = [t["lead"], t["desc"]] + t["intro"] + [p for h, ps, f in t["sections"] for p in ps] + \
            [h for h, ps, f in t["sections"]] + [q + " " + a for q, a in t["faqs"]] + [x[0]] + x[1] + [x[2][0], x[2][1]] + \
            [f[1] + " " + f[2] for h, ps, f in t["sections"]] + [t["hero"][1], t["media"][1]]
    return re.sub(r"<[^>]+>", " ", " ".join(parts))


def words(t, x):
    s = text_of(t, x).replace(t["label"], "TOWN")
    return s.lower().split()


uses, heroes = {}, {}
for t, x, src in entries:
    s = text_of(t, x)
    for m in BANNED.finditer(s):
        hard.append(f"{t['slug']}: banned '{m.group(0)}' ...{s[max(0, m.start()-40):m.end()+20]}")
    if len(t["desc"]) > 155:
        hard.append(f"{t['slug']}: desc {len(t['desc'])} chars")
    if not re.search(r"\(\d{3}\) \d{3}-\d{4}", t["desc"]):
        soft.append(f"{t['slug']}: desc has no phone")
    n = len(words(t, x))
    if n < 300:
        soft.append(f"{t['slug']}: only {n} words of copy")
    stems = [t["hero"][0], t["media"][0]] + [f[0] for h, ps, f in t["sections"]]
    if len(set(stems)) < len(stems):
        hard.append(f"{t['slug']}: photo repeated on the page")
    for i, st in enumerate(stems):
        for w in (400, 800, 1600):
            if not os.path.exists(f"images/lib/r/{w}/{st}.webp"):
                soft.append(f"{t['slug']}: missing r/{w}/{st}")
        if not os.path.exists(f"images/lib/{st}.webp"):
            hard.append(f"{t['slug']}: no image {st}")
        uses.setdefault(st, []).append(t["slug"])
        if i == 0:
            heroes.setdefault(st, []).append(t["slug"])
    links = [u for n_, u in t["links"]] + [t["read"][1]] + [u for n_, u in t.get("chapter_links", [])]
    for blob in t["intro"] + [p for h, ps, f in t["sections"] for p in ps] + x[1]:
        links += re.findall(r'href=\\?"(/[^"\\#]*)', blob)
    for u in links:
        p = u.strip("/")
        if not (os.path.exists(p + ".html") or os.path.exists(p + "/index.html")):
            hard.append(f"{t['slug']}: dead link {u}")

for st, ss in heroes.items():
    if len(ss) > 1:
        hard.append(f"hero used on several pages: {st} {ss}")
for st, ss in uses.items():
    if len(ss) > 2:
        soft.append(f"photo on {len(ss)} pages: {st} {ss}")

sh = {t["slug"]: (lambda w: {" ".join(w[i:i+6]) for i in range(len(w) - 6)})(words(t, x)) for t, x, s in entries}
pairs = sorted(((len(sh[a] & sh[b]) / max(1, min(len(sh[a]), len(sh[b]))), a, b)
                for a, b in itertools.combinations(sh, 2)), reverse=True)
for v, a, b in pairs:
    if v > 0.08:
        hard.append(f"overlap {v:.1%} {a} / {b}")
print(f"{len(entries)} pages checked; top overlaps:", [(f'{v:.1%}', a, b) for v, a, b in pairs[:4]])
print("HARD:", *hard, sep="\n  ") if hard else print("hard: none")
print("soft:", *soft[:40], sep="\n  ") if soft else print("soft: none")
sys.exit(1 if hard else 0)
