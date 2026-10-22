"""Rebuild search-index.json, the file the header search box reads.

The index was written once on 2026-09-01 and never refreshed, so every post,
solutions page and city added since then was missing from site search. This
rebuilds it from sitemap.xml so it can run after every build.

Product-city pages (blinds-plano-tx and friends) are left out on purpose:
there are ~300 of them, and a search for "shutters" should land on the
shutters product page, not on 49 near-identical city variants.
"""
import html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BASE = "https://www.loveisblindstx.com"
PCITY = re.compile(r"^/(blinds|shades|shutters|plantation-shutters|motorized-shades|patio-shades)-[a-z0-9-]+-tx$")


def path_for(url):
    p = url[len(BASE):].strip("/")
    if not p:
        return "index.html"
    for c in (p + ".html", p + "/index.html"):
        if os.path.exists(c):
            return c
    return None


def kind(url, page):
    if '"BlogPosting"' in page:
        return "Article"
    if url.startswith("/products"):
        return "Product"
    if url.startswith("/services") or url.startswith("/solutions"):
        return "Service"
    if url.startswith("/meet-the-team"):
        return "Team"
    if re.fullmatch(r"/[a-z0-9-]+-tx", url):
        return "Service Area"
    return "Page"


def text_of(fragment):
    fragment = re.sub(r"<script.*?</script>|<style.*?</style>|<form.*?</form>", " ", fragment, flags=re.S)
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", fragment)).split())


def main():
    locs = re.findall(r"<loc>([^<]+)</loc>", open("sitemap.xml").read())
    out = []
    for loc in locs:
        url = loc[len(BASE):] or "/"
        if PCITY.match(url):
            continue
        f = path_for(loc)
        if not f:
            continue
        page = open(f, encoding="utf-8").read()
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", page, re.S)
        title = text_of(h1.group(1)) if h1 else \
            html.unescape(re.search(r"<title>(.*?)</title>", page, re.S).group(1)).split(" | ")[0]
        d = re.search(r'<meta name="description" content="([^"]*)"', page)
        main = re.search(r"<main[^>]*>(.*?)</main>", page, re.S)
        body = text_of(main.group(1) if main else page)
        out.append({"u": url, "t": html.escape(title, quote=False),
                    "k": kind(url, page),
                    "d": html.unescape(d.group(1)) if d else "",
                    "x": body.lower()[:1400]})
    json.dump(out, open("search-index.json", "w"), ensure_ascii=False, separators=(",", ":"))
    return len(out)


if __name__ == "__main__":
    print("search index:", main(), "pages")
