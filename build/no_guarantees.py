"""Remove the guarantee and warranty claims from built pages (Nov 2026).

The client asked to take the five named guarantees off the site (Limited
Lifetime Warranty, Apples-to-Apples price match, GuaranTEN, Here-4-You
four-year service guarantee, Transferable Warranty) together with the
"remade at no cost" promise. This pass is idempotent and works on the built
HTML, because several of the generators that wrote these blocks (enrich.py,
home.py, media_rich.py, the blog generators) are not rerun.

What it does:
  * five-ways guarantee sections become the four-step process section
    (build/how_strip.py)
  * FAQ items that are about a guarantee are dropped, from the visible
    <details> list and from the FAQPage JSON-LD
  * sentences and list items that state a guarantee are cut; the rest of the
    paragraph stays
Never touched: customer review quotes, legal pages, the Vodyssey brand pages,
and city/product-city pages (built from cleaned sources by city_v2/pc_v2).

  python3 build/no_guarantees.py          # apply
  python3 build/no_guarantees.py --dry    # print every change, write nothing
"""
import glob, html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(ROOT)
import how_strip  # noqa: E402

DRY = "--dry" in sys.argv
SKIP = re.compile(r"^(terms-of-service|privacy-policy|reviews|vodyssey|window-treatment-terms-glossary|brands|blog/index)")

# a claim the company makes about its own cover. Generic advice ("check the
# warranty", "film can void a glass warranty", "a remake you pay for") is left.
CLAIM = re.compile(
    r"remade|remake it|remake and reinstall|remake (?:is |covered|on us)|ours to remake|a remake covered|"
    r"remake on us|lifetime warrant|life time warrant|lifetime guarantee|service guarantee|Here-4-You|GuaranTEN|"
    r"Apples-to-Apples|apples-to-apples|price.match|warranties transfer|warranty transfers|"
    r"transferable warranty|five ways|our guarantees|satisfaction guarantee|free replacement|"
    r"Warrantied|manufacturer warrant|our warrant|warranty claim|warranty service|covered for life|"
    r"cover that transfers|coverage transfers|stand behind those numbers|we correct it", re.I)
HEADBAD = re.compile(CLAIM.pattern + r"|approved (?:measurements|numbers)|what (?:you|we) approved|"
                     r"at no cost|without charge|\bif\b[^,]*$|\b(?:and|plus|or|with)$", re.I)


def fix_sentence(s):
    if not CLAIM.search(s):
        return s
    for m in reversed(list(re.finditer(r",? (?:and|plus) |, |; ", s))):
        head = s[:m.start()].rstrip(" ,;")
        if HEADBAD.search(re.sub(r"<[^>]+>", "", head)) or len(head.split()) < 6:
            continue
        if CLAIM.search(s[m.start():]):
            i = head.rfind(", ")
            if m.group(0) == ", " and i > 15:
                head = head[:i] + " and " + head[i + 2:]
            return head + "."
    return ""


def strip_text(t):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z<])", t)
    return " ".join(p for p in (fix_sentence(x) for x in parts) if p).strip()


def words(t):
    return len(re.sub(r"<[^>]+>", " ", t).split())


changes = []


def note(f, old, new):
    changes.append((f, re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", old)))[:220],
                    re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", new)))[:220] or "(removed)"))


SEC = re.compile(r"<section\b(?:(?!<section\b).)*?five ways(?:(?!</section>).)*?(?:gtee|sol-guarantees).*?</section>", re.S | re.I)
ED_H = re.compile(r"<h2([^>]*)>Backed five ways</h2>\s*<p([^>]*)>[^<]*</p>")
INLINE = r"(?:[^<]|<(?:a|strong|em|b|i|br)\b[^>]*>|</(?:a|strong|em|b|i)>)*?"
DETAILS = re.compile(r"<details>\s*<summary>(.*?)</summary>\s*<div class=['\"]a['\"]>(.*?)</div>\s*</details>", re.S)
LI = re.compile(r"<li\b([^>]*)>(" + INLINE + r")</li>", re.S)
BLOCK = re.compile(r"<(p|span|h3|h2|div class=['\"]a['\"])(\b[^>]*)?>(" + INLINE + r")</(p|span|h3|h2|div)>", re.S)
PROTECT = re.compile(r"<blockquote\b.*?</blockquote>|<article class=\"rv-card.*?</article>|"
                     r"<script\b.*?</script>|<footer\b.*?</footer>|<p class=\"rv-quote\">.*?</p>", re.S)
FAQ_Q_DROP = re.compile(r"warrant|guarant|price.match|does not fit|doesn.t fit|not fit right|"
                        r"measurement is wrong|mismeasure", re.I)

ED_TITLE = "One local team, start to finish"
ED_TEXT = ("The free consultation, the on-site measure and the written quote with installation all come "
           "before anything is ordered, and the team that measured is the team that installs.")


def process(f, s):
    orig = s
    # 1. whole guarantee sections
    def sec(m):
        block = m.group(0)
        if f in ("how-it-works.html", "installation-standards.html"):
            new = ""          # the page itself is the process; no strip needed
        else:
            t = re.search(r"Every job in ([^<]+?) is backed", block)
            new = how_strip.section(f"How a {t.group(1)} project works" if t else "How a project works")
        note(f, "[section] five ways guarantee band", "[section] " + ("removed" if not new else "how it works"))
        return new
    s = SEC.sub(sec, s)
    s = ED_H.sub(lambda m: (note(f, "[ed-split] Backed five ways", ED_TITLE) or
                            f"<h2{m.group(1)}>{ED_TITLE}</h2><p{m.group(2)}>{ED_TEXT}</p>"), s)

    s = s.replace("Measured &middot; Installed &middot; Warrantied", "Measured &middot; Installed &middot; Local")
    s = s.replace("If you are planning shutters for more rooms, The consultation", "If you are planning shutters for more rooms, the consultation")
    # protect reviews, scripts and the footer from text edits
    keep = []
    def hold(m):
        keep.append(m.group(0)); return f"\x00{len(keep) - 1}\x00"
    s = PROTECT.sub(hold, s)

    # 2. FAQ items
    dropped_q = []
    def det(m):
        q, a = m.group(1), m.group(2)
        if not (CLAIM.search(a) or CLAIM.search(q)):
            return m.group(0)
        na = strip_text(a)
        if FAQ_Q_DROP.search(q) or words(na) < 8:
            dropped_q.append(html.unescape(re.sub(r"<[^>]+>", "", q)).strip())
            note(f, "[faq] " + q, "")
            return ""
        note(f, a, na)
        return m.group(0).replace(a, na)
    s = DETAILS.sub(det, s)

    # 3. list items
    def li(m):
        t = m.group(2)
        if not CLAIM.search(t):
            return m.group(0)
        n = strip_text(t)
        if words(n) < 4:
            note(f, t, ""); return ""
        note(f, t, n)
        return f"<li{m.group(1)}>{n}</li>"
    s = LI.sub(li, s)

    # 4. paragraphs and other text blocks
    def blk(m):
        tag, attrs, t, close = m.group(1), m.group(2) or "", m.group(3), m.group(4)
        if not CLAIM.search(t):
            return m.group(0)
        n = strip_text(t)
        note(f, t, n)
        if not n.strip():
            return ""
        return f"<{tag}{attrs}>{n}</{close}>"
    s = BLOCK.sub(blk, s)

    s = re.sub("\x00(\\d+)\x00", lambda m: keep[int(m.group(1))], s)
    s = re.sub(r"<li>\s*</li>|<p>\s*</p>", "", s)

    # 5. FAQPage JSON-LD mirrors the visible list
    def ld(m):
        try:
            data = json.loads(m.group(2))
        except Exception:
            return m.group(0)
        hit = [False]
        def walk(o):
            if isinstance(o, dict):
                if o.get("@type") == "FAQPage" and isinstance(o.get("mainEntity"), list):
                    keep_q = []
                    for q in o["mainEntity"]:
                        name = q.get("name", "")
                        ans = (q.get("acceptedAnswer") or {}).get("text", "")
                        if name in dropped_q or (CLAIM.search(ans) and FAQ_Q_DROP.search(name)):
                            hit[0] = True; continue
                        if CLAIM.search(ans):
                            na = strip_text(ans)
                            if words(na) < 8:
                                hit[0] = True; continue
                            q["acceptedAnswer"]["text"] = na; hit[0] = True
                        keep_q.append(q)
                    o["mainEntity"] = keep_q
                for v in o.values():
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
        walk(data)
        if not hit[0]:
            return m.group(0)
        return m.group(1) + json.dumps(data, indent=1, ensure_ascii=False) + m.group(3)
    s = re.sub(r'(<script type="application/ld\+json">\s*)(.*?)(\s*</script>)', ld, s, flags=re.S)
    return s


files = [f for f in sorted(glob.glob("*.html") + glob.glob("*/*.html") + glob.glob("data/queued-posts/*.html"))
         if not SKIP.match(f) and not os.path.basename(f).startswith("vodyssey")]
n = 0
for f in files:
    s = open(f, encoding="utf-8").read()
    if 'class="cx-' in s:
        continue
    new = process(f, s)
    if new != s:
        n += 1
        if not DRY:
            open(f, "w", encoding="utf-8").write(new)
if DRY:
    for f, o, nw in changes:
        print(f"{f}\n   - {o}\n   + {nw}")
print(f"no_guarantees: {len(changes)} edits on {n} pages{' (dry run)' if DRY else ''}")
