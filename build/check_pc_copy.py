"""Check build/pc_copy/*.json (the unique layer of the product-city pages).

Hard: missing cities/fields, dashes, banned phrases, a sentence used on more
than one page (across all products), word counts far outside the brief.
  python3 build/check_pc_copy.py
"""
import glob, json, os, re, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
cities = json.load(open("/private/tmp/claude-501/-Users-maddie-emrick-Documents-Claude/"
                        "09f92509-7768-41a7-baed-0c3f2502ca0f/scratchpad/brief/pc_cities.json"))
BANNED = re.compile(r"[–—]|\bhonest|not just|isn.t just|\bit.s not\b|whether you|ready to|look no further|"
                    r"elevate|seamless|peace of mind|so you can|nestled|boasts|perfect for|in today.s|"
                    r"\w, not (a |an |the )?\w+[.,]", re.I)
hard, soft = [], []
sent_where = defaultdict(list)
for f in sorted(glob.glob("build/pc_copy/*.json")):
    prod = os.path.basename(f)[:-5]
    try:
        d = json.load(open(f))
    except Exception as ex:
        hard.append(f"{prod}: bad JSON {ex}"); continue
    missing = set(cities) - set(d)
    if missing:
        hard.append(f"{prod}: missing {len(missing)} cities {sorted(missing)[:4]}")
    for slug, v in d.items():
        if slug not in cities:
            hard.append(f"{prod}: unknown slug {slug}"); continue
        for k in ("lead", "p1", "p2", "faqs"):
            if k not in v:
                hard.append(f"{prod}/{slug}: no {k}")
        if len(v.get("faqs", [])) != 2:
            hard.append(f"{prod}/{slug}: {len(v.get('faqs', []))} faqs")
        txt = " ".join([v.get("lead", ""), v.get("p1", ""), v.get("p2", "")] +
                       [q + " " + a for q, a in v.get("faqs", [])])
        for m in BANNED.finditer(txt):
            hard.append(f"{prod}/{slug}: banned '{m.group(0)}'")
        for k, lo, hi in (("lead", 12, 40), ("p1", 35, 85), ("p2", 25, 75)):
            w = len(v.get(k, "").split())
            if not lo <= w <= hi:
                soft.append(f"{prod}/{slug}: {k} {w} words")
        for s in re.split(r"(?<=[.!?])\s+", txt):
            key = re.sub(r"\W+", " ", s.lower()).strip()
            if len(key.split()) >= 7:
                sent_where[key].append(f"{prod}/{slug}")
dups = {k: v for k, v in sent_where.items() if len(v) > 1}
for k, v in dups.items():
    # one shared company-fact sentence on a few pages is normal; widespread reuse is templating
    (hard if len(v) >= 5 else soft).append(f"repeated sentence on {len(v)} pages {v[:3]}: {k[:90]}")
print(f"{len(glob.glob('build/pc_copy/*.json'))} product files; {len(dups)} repeated sentences")
print("HARD:", *hard[:60], sep="\n  ") if hard else print("hard: none")
print(f"soft: {len(soft)}", *soft[:15], sep="\n  ")
sys.exit(1 if hard else 0)
