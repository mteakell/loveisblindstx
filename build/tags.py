"""Third-party tags that belong in <head>, applied to every page.

There is no shared head partial: pages.py, extra.py, blog.py, newposts.py and
convert.py each build their own <head>. So rather than patching five
generators and hoping a sixth never appears, this runs last and guarantees the
tag is in the head exactly once on every page.

Idempotent, and it also strips the tag from anywhere else on the page, so
moving a tag between head and body is a one-line change here.
"""
import glob, re

TAGS = [
 ('venbit',
  '<script defer src="https://venbit.com/m.js?s=vb_ae6a489f0305" '
  'data-site="vb_ae6a489f0305"></script>'),
 # The Venbit AI site agent (chat / live-visitor view) is a separate product
 # from the analytics tag above. The old Duda site lazy-loaded it on first
 # interaction or 30s so it never hurts LCP; same pattern kept here.
 ('venbit-agent',
  '<script>(function(){var l=false;function f(){if(l)return;l=true;'
  "var s=document.createElement('script');"
  "s.src='https://www.venbit.ai/venbit-site-agent.js?id=site_073933e290';"
  's.async=true;document.head.appendChild(s);}'
  "['mousemove','touchstart','click','scroll'].forEach(function(e){"
  'window.addEventListener(e,f,{once:true,passive:true});});'
  'setTimeout(f,30000);})();</script>'),
 # GA4 + GTM carried over from the old Duda site so measurement history
 # continues in the same properties.
 ('ga4',
  '<script async src="https://www.googletagmanager.com/gtag/js?id=G-G7R0VY8T52"></script>'
  '<script>window.dataLayer=window.dataLayer||[];'
  'function gtag(){dataLayer.push(arguments);}gtag(\'js\',new Date());'
  'gtag(\'config\',\'G-G7R0VY8T52\');</script>'),
 ('gtm',
  "<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':"
  "new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],"
  "j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;"
  "j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;"
  "f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-WCKH3TQ5');</script>"),
 # CallRail dynamic number insertion, same company/script as the old site,
 # so tracked numbers keep swapping in and call attribution survives the move.
 ('callrail',
  '<script defer src="https://cdn.callrail.com/companies/177791272/a1a94f3d60d5a5867e90/12/swap.js"></script>'),
 ('vercel-analytics',
  '<script defer src="/_vercel/insights/script.js"></script>'),
]


def main():
    added = moved = 0
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith("build/"):
            continue
        s = o = open(f).read()
        head_end = s.find("</head>")
        if head_end < 0:
            continue
        for name, tag in TAGS:
            # drop any existing copy, wherever it sits, plus its comment marker
            before = s
            s = re.sub(rf'\n?<!-- {name} -->\n?', '\n', s, flags=re.I)
            s = s.replace(tag, "")
            if s != before:
                moved += 1
            head_end = s.find("</head>")
            s = s[:head_end] + f'<!-- {name} -->\n{tag}\n' + s[head_end:]
            added += 1
        # tidy the blank line the removal can leave behind
        s = re.sub(r'\n{3,}', '\n\n', s)
        if s != o:
            open(f, "w").write(s)
    print(f"tags: {added} inserted into <head>, {moved} relocated from elsewhere")



def wrap_feature_items():
    """Give every .feature-list item exactly two flex children.

    .feature-list li is display:flex so the tick sits beside the text. But a
    bare text node plus inline links means every <a> becomes its own flex item,
    which broke "run by Jake Wade and Jonathan Arosemena" into columns. Wrapping
    the text in a span makes the row tick + text and nothing else.

    Done here rather than in one generator because feature lists are emitted by
    pages.py and by the converted Duda pages alike.
    """
    n = 0
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith("build/"):
            continue
        s = open(f).read()
        if 'class="feature-list"' not in s:
            continue

        def fix(m):
            nonlocal n
            inner = m.group(1)
            if '<span class="ftxt">' in inner:
                return m.group(0)
            mm = re.match(r'(\s*<span class="tick">.*?</span>)(.*)$', inner, re.S)
            if not mm:
                return m.group(0)
            n += 1
            return f'<li>{mm.group(1)}<span class="ftxt">{mm.group(2)}</span></li>'

        out = re.sub(r'<li>((?:(?!</li>).)*)</li>', fix, s, flags=re.S)
        if out != s:
            open(f, "w").write(out)
    print(f"feature lists: wrapped {n} items")




def bust_css():
    """Fingerprint the stylesheet link.

    The design kept looking broken after deploys because browsers held a cached
    styles.css: the page HTML updates but the stylesheet URL never changed, so
    new markup rendered with old rules and giant unstyled icons. Appending a
    content hash means every CSS change is a new URL and a refresh always gets
    the matching stylesheet.
    """
    import hashlib
    digest = hashlib.sha1(open("css/styles.css", "rb").read()).hexdigest()[:10]
    link = re.compile(r'href="/css/styles\.css(?:\?v=[0-9a-f]*)?"')
    n = 0
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith("build/"):
            continue
        s = open(f).read()
        out = link.sub(f'href="/css/styles.css?v={digest}"', s)
        if out != s:
            open(f, "w").write(out); n += 1
    print(f"css cache-bust: v={digest} on {n} pages")




def mark_active_nav():
    """Underline the nav item for the page you are actually on.

    The shared header hardcoded aria-current="page" on Service Areas, so every
    page on the site underlined Service Areas. Cleared here and re-set per page
    from the page's own path.
    """
    import json
    cities = {c["slug"] for c in json.load(open("data/tx.json"))["cities"]}

    def nav_href(path):
        p = path[:-5] if path.endswith(".html") else path      # strip .html
        p = p[:-6] if p.endswith("/index") else p
        if p in ("index", ""): return "/"
        if p.startswith("products/") or p in ("products", "brands"): return "/products"
        if p.startswith("services/") or p == "services": return "/services"
        if p == "gallery": return "/gallery"
        if p in ("areas-we-serve",) or p in cities: return "/areas-we-serve"
        if p in ("about", "meet-the-team", "how-it-works", "faqs", "design-checklist", "reviews") or p.startswith("team/") or p.startswith("meet-the-team/"):
            return "/about"
        if p == "blog": return "/blog"
        # product x city pages sell a product in a place; Service Areas fits best
        if p.endswith("-tx"): return "/areas-we-serve"
        # everything else (blog posts live at the root) reads as Blog
        if "/" not in p: return "/blog"
        return None

    n = 0
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith("build/"):
            continue
        s = open(f).read()
        target = nav_href(f)
        out = re.sub(r'(<ul class="nav-links".*?</ul>)', lambda m:
                     m.group(1).replace(' aria-current="page"', ''), s, count=1, flags=re.S)
        if target:
            out = re.sub(
                r'(<ul class="nav-links"[^>]*>.*?<a href="' + re.escape(target) + r'")(>)',
                r'\1 aria-current="page"\2', out, count=1, flags=re.S)
        if out != s:
            open(f, "w").write(out); n += 1
    print(f"active nav marked on {n} pages")


if __name__ == "__main__":
    main()
    wrap_feature_items()
    mark_active_nav()
    bust_css()
