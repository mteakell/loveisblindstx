"""Migrate the Duda blog into the Texas shell.

Content is lifted from the Duda markup, stripped of platform classes and inline
styles, repointed at locally hosted images, and rewrapped with BlogPosting +
BreadcrumbList schema. Copy is preserved as-is: Maddie deferred the de-fluff to
a second pass. Em dashes are the one exception, since those are a standing rule.
"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import schema as S

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRATCH = ("/private/tmp/claude-501/-Users-maddie-emrick-Documents-Claude/"
           "8f42eabe-f124-4b4c-b313-1caf93cbd159/scratchpad")
os.chdir(ROOT)
BIZ = json.load(open("data/tx.json"))["business"]
HEAD = open("build/partials/header.html").read()
FOOT = open("build/partials/footer.html").read()
HEAD_INNER = HEAD.split("<body", 1)[1].split(">", 1)[1]
IMG = json.load(open(f"{SCRATCH}/img-map.json"))
REN = json.load(open(f"{SCRATCH}/renames.json"))
CITY_SLUGS = {c["slug"] for c in json.load(open("data/tx.json"))["cities"]}
POST_SLUGS = {u.strip().lstrip("/") for u in open("data/blog-urls.txt") if u.strip()}
IMG = {k: ("/images/blog/" + REN.get(v.split("/")[-1], v.split("/")[-1])) for k, v in IMG.items()}
e = lambda s: html.escape(s or "", quote=True)

def _nodash(s):
    """Standing rule across every client site: no em dashes in generated copy."""
    return s.replace("\u2014", ",").replace("&mdash;", ",").replace(" , ", ", ")

DROP_ATTR = re.compile(r'\s+(?:class|id|style|data-[\w-]+|on[a-z]+|srcset|sizes)="[^"]*"')
KEEP = re.compile(r"^(p|h2|h3|h4|ul|ol|li|strong|em|b|i|br|a|img|blockquote|table|thead|tbody|tr|td|th)$")

LEGACY = {"/products/roman-shades": "/products/shades",
          "/services/custom-blinds-installation": "/services/blinds-installation",
          "/contact": "/schedule-now", "/team": "/meet-the-team",
          "/service-areas": "/areas-we-serve"}

def relink(href):
    """Old Duda internal links: legacy city pattern, legacy blog path, dead pages."""
    b = href.rstrip("/") or "/"
    if b in LEGACY: return LEGACY[b]
    m = re.match(r"^/window-treatments/(.+)$", b)
    if m:
        slug = m.group(1)
        if slug in CITY_SLUGS: return "/" + slug
        trimmed = re.sub(r"-\d+$", "", slug)
        return "/" + trimmed if trimmed in CITY_SLUGS else "/areas-we-serve"
    if b == "/window-treatments": return "/areas-we-serve"
    m = re.match(r"^/blog/(.+)$", b)
    if m: return "/" + m.group(1) if m.group(1) in POST_SLUGS else "/blog"
    return href

def clean(seg):
    seg = re.sub(r"<(script|style|noscript|iframe|form|svg)[^>]*>.*?</\1>", "", seg, flags=re.S)
    seg = re.sub(r"<h1[^>]*>.*?</h1>", "", seg, flags=re.S)          # h1 is re-emitted by the shell
    for u, local in IMG.items():                                      # local images
        seg = seg.replace(u, local)
    seg = re.sub(r'src="https?://(?:i|l)rp\.cdn-website\.com[^"]*"', 'src=""', seg)
    def keeptag(m):
        close, tag, attrs = m.group(1), m.group(2).lower(), m.group(3)
        if not KEEP.match(tag): return ""
        if close: return f"</{tag}>"
        attrs = DROP_ATTR.sub("", attrs)
        if tag == "a":
            attrs = re.sub(r'href="https?://(?:www\.)?loveisblindstx\.com', 'href="', attrs)
            attrs = re.sub(r'href="(/[^"#?]*)"',
                           lambda h: f'href="{relink(h.group(1))}"', attrs)
        if tag == "img":
            attrs = attrs.rstrip().rstrip("/")
            attrs += ' loading="lazy" decoding="async"'
            if "alt=" not in attrs:
                src = re.search(r'src="([^"]*)"', attrs)
                base = os.path.basename(src.group(1)) if src else ""
                base = re.sub(r"^[0-9a-f]{8}-", "", os.path.splitext(base)[0])
                base = re.sub(r"-\d+w$", "", base).replace("-", " ").replace("+", " ").strip()
                attrs += f' alt="{base[:110] or "Window treatment by Love Is Blinds"}"'
        return f"<{tag}{attrs}>"
    seg = re.sub(r"<(/?)([A-Za-z0-9]+)((?:\s[^>]*)?)/?>", keeptag, seg)
    seg = seg.replace("—", ",").replace("&mdash;", ",")
    seg = re.sub(r'<img[^>]*src=""[^>]*>', "", seg)
    # dead Duda share buttons: empty anchors wrapping a mailto share href
    seg = re.sub(r'<a [^>]*href="mailto:\?subject=[^"]*"[^>]*>\s*</a>', "", seg)
    # Duda leaves paragraphs holding only invisible characters (BOM, zero-width,
    # non-breaking space). They render as large blank gaps between real paragraphs.
    seg = re.sub(r"(?:&nbsp;|&#160;|&#65279;|[\u00a0\u200b\u200c\ufeff])", " ",
                 seg) if False else seg
    seg = re.sub(r"<p>(?:\s|&nbsp;|&#160;|&#65279;|<br\s*/?>|[\u00a0\u200b\ufeff])*</p>",
                 "", seg)
    seg = re.sub(r"(?:<br\s*/?>\s*){3,}", "<br><br>", seg)
    seg = re.sub(r"\n{3,}", "\n\n", seg)
    return re.sub(r"[ \t]{2,}", " ", seg).strip()

def extract(path):
    h = open(path, encoding="utf-8", errors="ignore").read()
    t = re.search(r"<title>(.*?)</title>", h, re.S)
    title = _nodash(" ".join(html.unescape(t.group(1)).split())) if t else ""
    d = re.search(r'<meta name="description" content="(.*?)"', h, re.S)
    desc = _nodash(" ".join(html.unescape(d.group(1)).split())) if d else ""
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
    head = _nodash(" ".join(html.unescape(re.sub(r"<[^>]*>", "", h1.group(1))).split())) if h1 else title
    pub = re.search(r'"datePublished"\s*:\s*"([^"]+)"', h)
    # slice on tag boundaries: h.find lands inside a class attribute, and slicing
    # there leaks the rest of the opening tag onto the page as visible text.
    i = h.find("blog-post-row")
    if i > 0:
        i = h.find(">", i) + 1                       # past the end of that opening tag
    j = h.find("postArticle", i if i > 0 else 0)
    if j > 0:
        j = h.rfind("<", 0, j)                       # back to the start of its opening tag
    body = clean(h[i:j]) if i > 0 and j > i else ""
    hero = re.search(r'<img[^>]+src="(/images/blog/[^"]+)"', body)
    return dict(title=title, desc=desc, h1=head, body=body,
                published=(pub.group(1) if pub else None),
                hero=hero.group(1) if hero else None)

BRAND = " | Love Is Blinds"

def _fit_title(raw, h1):
    """Under 60, never cut mid-word, and prefer a complete phrase over a stub.

    Duda's own titles sometimes drop the leading number the H1 carries
    ("Reasons to Avoid..." vs "3 Reasons You Should Never..."), and several run
    long. So try the whole candidates first and only trim as a last resort.
    """
    def clean(t):
        return " ".join((t or "").replace("\u00a0", " ").split())

    def trim(t, n):
        if len(t) <= n:
            return t
        cut = t[:n].rsplit(" ", 1)[0].rstrip(" ,:;-|&")
        return cut or t[:n]

    def debrand(t):
        for sep in ["|", "\u2013", "\u2014"]:
            if sep in t:
                head, tail = t.split(sep, 1)
                if len(head.strip()) >= 20 and "love is blinds" in tail.lower():
                    return head.strip()
        return t

    title, head = debrand(clean(raw)), debrand(clean(h1))
    # whole candidates, shortest complete one that still carries the brand wins
    for c in (title, head):
        if c and len(c) + len(BRAND) <= 60:
            return c + BRAND
    fits = [x for x in (title, head) if x and len(x) <= 60]
    if fits:
        return max(fits, key=len)
    longest_complete = max([title, head], key=len) if (title or head) else ""
    return trim(longest_complete, 60)

def build(url, p):
    title = _fit_title(p["title"], p["h1"])
    desc = p["desc"][:155]
    nodes = [S.organization(BIZ), S.website(BIZ), S.business(BIZ),
             S.webpage(url, title, desc, kind="WebPage", about=S.ORGID, primary=p["hero"]),
             S.blogposting(url, p["h1"] or title, desc, p["published"] or "2024-01-01",
                           image=p["hero"]),
             S.breadcrumbs([("Home", "/"), ("Blog", "/blog"), (p["h1"][:60], url)])]
    img = p["hero"] or "/images/hero-shutters-desktop.jpg"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{S.SITE}{url}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#3A4D5C">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{e(BIZ['name'])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{S.SITE}{url}">
<meta property="og:image" content="{S.SITE}{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css">
{S.render(nodes)}
</head>
<body>
{HEAD_INNER}
<main>
<article class="section">
  <div class="container">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span>&rsaquo;</span>
      <a href="/blog">Blog</a> <span>&rsaquo;</span>
      <span aria-current="page">{e(p["h1"][:70])}</span></nav>
    <h1 class="title">{e(p["h1"])}</h1>
    <div class="post-body">
{p["body"]}
    </div>
    <div class="btnrow">
      <a class="btn btn-primary btn-lg" href="/schedule-now">Book a free consultation</a>
      <a class="btn btn-secondary btn-lg" href="tel:{BIZ["tel"]}">Call {e(BIZ["phone"])}</a>
    </div>
  </div>
</article>
</main>
{FOOT}'''

if __name__ == "__main__":
    urls = [u.strip() for u in open("data/blog-urls.txt") if u.strip()]
    made, empty = [], []
    index = []
    for u in urls:
        src = f"{SCRATCH}/posts/{u.lstrip('/')}.html"
        if not os.path.exists(src): empty.append(u); continue
        p = extract(src)
        if len(re.sub(r"<[^>]*>", "", p["body"]).split()) < 80:
            empty.append(u); continue
        open(u.lstrip("/") + ".html", "w").write(build(u, p))
        made.append(u)
        index.append({"url": u, "title": p["h1"], "desc": p["desc"],
                      "date": p["published"], "img": p["hero"]})
    json.dump(index, open("data/blog-index.json", "w"), indent=1)
    print(f"migrated {len(made)} posts")
    if empty: print(f"skipped {len(empty)} with no extractable body: {empty}")
