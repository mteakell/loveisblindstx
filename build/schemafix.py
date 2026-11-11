"""Repair and check the JSON-LD on every built page.

Found by an independent audit (Nov 10 2026), confirmed here:
  * 294 product-city pages pointed WebPage.about and Service.provider at
    /{product}-{city}#business, an @id defined nowhere; the business the
    page declares is /{city}#business.
  * 376 Service nodes carried a $0-$10,000 AggregateOffer that no page
    shows. Replaced with the free-consultation Offer every page states.
  * Fort Worth's city node placed the Ray White Rd business downtown, 11 mi
    from its Google profile pin; Austin, McKinney, Colleyville and Las Colinas
    used city-center or legacy pins. Coordinates now come from data/tx.json,
    which carries the Google profile pins.
The generators (schema.py, product_city.py) are fixed at the source; this
pass brings already-built pages in line without a full rebuild.

  python3 build/schemafix.py           repair in place
  python3 build/schemafix.py --check   report only; exit 1 on any defect
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(ROOT)
import schema as S

BLOCK = re.compile(r'(<script type="application/ld\+json">\n?)(.*?)(\n?</script>)', re.S)
TX = json.load(open("data/tx.json"))
GEO = {S.SITE + c["url"] + "#business": (c["lat"], c["lng"]) for c in TX["cities"]
       if c.get("lat") is not None}
GEO[S.BIZID] = (TX["business"]["lat"], TX["business"]["lng"])


def nodes_of(doc):
    return doc.get("@graph", [doc]) if isinstance(doc, dict) else doc


def defined_ids(docs):
    out = set()
    def walk(o):
        if isinstance(o, dict):
            if "@id" in o and len(o) > 1:
                out.add(o["@id"])
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    for d in docs:
        walk(d)
    return out


def is_ref(o):
    return isinstance(o, dict) and set(o) == {"@id"}


def bad_offer(o):
    return isinstance(o, dict) and o.get("@type") == "AggregateOffer" \
        and o.get("lowPrice") == 0 and o.get("highPrice") == 10000


def repair(docs, ids):
    city_biz = [i for i in ids if i.endswith("#business") and i != S.BIZID]
    target = city_biz[0] if len(city_biz) == 1 else S.BIZID
    changes = 0

    def walk(o):
        nonlocal changes
        if isinstance(o, dict):
            for k, v in list(o.items()):
                if is_ref(v) and v["@id"] not in ids and v["@id"].endswith("#business"):
                    o[k] = {"@id": target}; changes += 1
                elif k == "offers" and bad_offer(v):
                    o[k] = S.CONSULT_OFFER; changes += 1
                else:
                    walk(v)
            if o.get("@id") in GEO and isinstance(o.get("geo"), dict):
                lat, lng = GEO[o["@id"]]
                if (o["geo"].get("latitude"), o["geo"].get("longitude")) != (lat, lng):
                    o["geo"]["latitude"], o["geo"]["longitude"] = lat, lng; changes += 1
        elif isinstance(o, list):
            for v in o:
                walk(v)
    for d in docs:
        walk(d)
    return changes


def problems(docs, ids):
    out = []
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if is_ref(v) and v["@id"] not in ids:
                    out.append(f"unresolved {k} -> {v['@id']}")
                if k == "offers" and bad_offer(v):
                    out.append("generic $0-$10,000 AggregateOffer")
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    for d in docs:
        walk(d)
    return out


def main(check=False):
    pages = [f for f in glob.glob("**/*.html", recursive=True)
             if not f.startswith(("build/", "node_modules/"))]
    fixed = changed = 0
    report = {}
    for f in pages:
        t = open(f, encoding="utf-8").read()
        blocks = BLOCK.findall(t)
        if not blocks:
            continue
        docs = [json.loads(b[1]) for b in blocks]
        ids = defined_ids(docs)
        if check:
            p = problems(docs, ids)
            if p:
                report[f] = p
            continue
        n = repair(docs, ids)
        if n:
            it = iter(docs)
            u = BLOCK.sub(lambda m: m.group(1) + json.dumps(next(it), indent=1, ensure_ascii=False)
                          + m.group(3), t)
            open(f, "w", encoding="utf-8").write(u)
            fixed += 1; changed += n
    if check:
        kinds = {}
        for f, ps in report.items():
            for p in ps:
                kinds[p.split(" ->")[0]] = kinds.get(p.split(" ->")[0], 0) + 1
        print(f"schemacheck: {len(pages)} pages, {len(report)} with defects", kinds or "")
        for f, ps in list(report.items())[:10]:
            print("  ", f, ps[:3])
        return 1 if report else 0
    print(f"schemafix: {fixed} pages repaired, {changed} changes")
    return 0


if __name__ == "__main__":
    sys.exit(main(check="--check" in sys.argv))
