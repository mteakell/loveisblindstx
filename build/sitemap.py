"""Generate sitemap.xml and robots.txt.

The XML is written to match the live Duda sitemap byte-for-byte in structure:
same declaration with standalone="yes", the xhtml namespace on <urlset>,
four-space indentation, and children in loc / priority / changefreq / lastmod
order. Priority follows the live rule: 0.8 for blog posts, 1.0 for everything
else, changefreq monthly throughout.
"""
import datetime, glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import schema as S
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def run():
    posts = {p["url"] for p in json.load(open("data/blog-index.json"))}
    today = datetime.date.today().isoformat()
    urls, skipped = [], []
    for f in sorted(glob.glob("*.html") + glob.glob("*/*.html")):
        u = "/" if f == "index.html" else "/" + f[:-5]
        u = u.replace("/index", "") or "/"
        s = open(f).read()
        if u == "/404" or re.search(r'<meta name="robots"[^>]*noindex', s):
            skipped.append(u); continue
        urls.append((u, "0.8" if u in posts else "1.0"))

    body = "".join(
        "    <url>\n"
        f"        <loc>{S.SITE}{u}</loc>\n"
        f"        <priority>{p}</priority>\n"
        "        <changefreq>monthly</changefreq>\n"
        f"        <lastmod>{today}</lastmod>\n"
        "    </url>\n"
        for u, p in sorted(urls))
    open("sitemap.xml", "w").write(
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + body + "</urlset>\n")

    open("robots.txt", "w").write(
        "User-agent: *\nAllow: /\n\n"
        "# Partner ordering funnel, kept out of search\n"
        "Disallow: /vodyssey\nDisallow: /journey\n\n"
        f"Sitemap: {S.SITE}/sitemap.xml\n")
    return len(urls), skipped, sum(1 for _, p in urls if p == "0.8")

if __name__ == "__main__":
    n, sk, blog = run()
    print(f"sitemap: {n} URLs ({blog} at 0.8, {n-blog} at 1.0)")
    print(f"excluded ({len(sk)}): {sorted(sk)}")
