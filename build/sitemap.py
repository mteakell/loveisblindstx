"""Generate sitemap.xml and robots.txt from what is actually on disk."""
import glob, json, os, re, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
import schema as S
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

PRIORITY = [(r"^/$", "1.0", "weekly"), (r"^/[a-z0-9\-]+-tx$", "0.9", "monthly"),
            (r"^/products", "0.8", "monthly"), (r"^/services", "0.8", "monthly"),
            (r"^/areas-we-serve$", "0.8", "monthly"), (r"^/blog$", "0.7", "weekly"),
            (r"^/(schedule-now|design-checklist|meet-the-team)$", "0.7", "monthly"),
            (r"^/team/", "0.5", "yearly")]

def meta(f):
    s = open(f).read()
    noindex = bool(re.search(r'<meta name="robots"[^>]*noindex', s))
    return noindex

def run():
    urls, skipped = [], []
    for f in sorted(glob.glob("*.html") + glob.glob("*/*.html")):
        u = "/" if f == "index.html" else "/" + f[:-5]
        u = u.replace("/index", "") or "/"
        if u in ("/404",) or meta(f):
            skipped.append(u); continue
        pri, cf = "0.6", "monthly"
        for pat, p, c in PRIORITY:
            if re.match(pat, u): pri, cf = p, c; break
        urls.append((u, pri, cf))
    today = datetime.date.today().isoformat()
    body = "".join(
        f"  <url>\n    <loc>{S.SITE}{u}</loc>\n    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>{c}</changefreq>\n    <priority>{p}</priority>\n  </url>\n"
        for u, p, c in sorted(urls))
    open("sitemap.xml", "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + "</urlset>\n")
    open("robots.txt", "w").write(
        "User-agent: *\nAllow: /\n\n"
        "# Partner ordering funnel, kept out of search\nDisallow: /vodyssey\nDisallow: /journey\n\n"
        f"Sitemap: {S.SITE}/sitemap.xml\n")
    return len(urls), skipped

if __name__ == "__main__":
    n, sk = run()
    print(f"sitemap: {n} URLs")
    print(f"excluded ({len(sk)}): {sorted(sk)}")
