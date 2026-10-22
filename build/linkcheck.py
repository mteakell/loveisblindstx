"""Fail loudly on internal links that would 404.

The Oct 2026 audit found 11 links in published posts pointing at slugs that
never existed (the queue posts were written against guessed titles). This
walks every live page and checks each internal href against the files on
disk and the redirects in vercel.json. Links into posts that are queued but
not yet published are reported separately: they 404 until their date.

Exit code 1 when any live page has a dead link, so a build can refuse to ship.
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BASE = "https://www.loveisblindstx.com"


def exists(path):
    p = path.strip("/")
    if not p:
        return True
    return (os.path.exists(p + ".html") or os.path.exists(os.path.join(p, "index.html"))
            or os.path.isfile(p))


def main():
    redirects = {r["source"].rstrip("/") for r in json.load(open("vercel.json"))["redirects"]}
    queued = {"/" + q["slug"] for q in json.load(open("data/post-queue.json")) if not q["published"]}
    pages = [f for f in glob.glob("**/*.html", recursive=True)
             if not f.startswith(("build/", "data/", "node_modules/"))]
    dead, early = {}, {}
    for f in pages:
        for href in re.findall(r'<a\b[^>]*href="([^"#?]+)', open(f, encoding="utf-8").read()):
            if href.startswith(BASE):
                href = href[len(BASE):] or "/"
            if not href.startswith("/") or href.startswith("//"):
                continue
            h = href.rstrip("/") or "/"
            if h.endswith(".html"):
                h = h[:-5]
            if exists(h) or h in redirects:
                continue
            (early if h in queued else dead).setdefault(h, set()).add(f)
    for h, fs in sorted(early.items()):
        print(f"queued, live on its date: {h}  <- {', '.join(sorted(fs))}")
    for h, fs in sorted(dead.items()):
        print(f"DEAD: {h}  <- {', '.join(sorted(fs))}")
    print(f"linkcheck: {len(pages)} pages, {len(dead)} dead targets, {len(early)} queued targets")
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
