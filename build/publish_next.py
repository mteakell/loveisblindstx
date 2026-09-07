"""Publish queued blog posts whose date has arrived. Run daily.

Moves due posts from data/queued-posts/ into the site root, registers them
in the blog index, reruns the passes that wire a post into the site, and
commits + pushes. Safe to run any number of times a day: already-published
posts are skipped, and a day with nothing due exits quietly.
"""
import datetime, json, os, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def run(*cmd, quiet=True):
    r = subprocess.run(cmd, capture_output=quiet, text=True)
    if r.returncode != 0:
        print(f"FAILED: {' '.join(cmd)}\n{(r.stderr or '')[-800:]}")
        sys.exit(1)
    return r

def main():
    q = json.load(open("data/post-queue.json"))
    today = datetime.date.today().isoformat()
    due = [p for p in q if not p["published"] and p["date"] <= today]
    if not due:
        remaining = sum(1 for p in q if not p["published"])
        print(f"nothing due today ({remaining} still queued)")
        return

    idx = json.load(open("data/blog-index.json"))
    for p2 in due:
        src = f"data/queued-posts/{p2['slug']}.html"
        shutil.move(src, f"{p2['slug']}.html")
        if not any(x["url"] == "/" + p2["slug"] for x in idx):
            idx.append({"url": "/" + p2["slug"], "title": p2["title"],
                        "desc": p2["desc"], "date": p2["date"], "img": p2["img"]})
        p2["published"] = True
        print("published:", p2["slug"])
    json.dump(idx, open("data/blog-index.json", "w"), indent=1)
    json.dump(q, open("data/post-queue.json", "w"), indent=1)

    sys.path.insert(0, "build")
    import extra
    extra.blog_index()
    for mod in ("crosslinks", "altfix", "dims", "tags", "sitemap"):
        run(sys.executable, f"build/{mod}.py")
    run("git", "add", "-A")
    titles = ", ".join(p2["slug"] for p2 in due)
    run("git", "commit", "-m",
        f"Publish scheduled post: {titles}\n\nCo-Authored-By: Claude Fable 5 <noreply@anthropic.com>")
    run("git", "push", "origin", "main")
    print(f"live and pushed ({sum(1 for p in q if not p['published'])} still queued)")

if __name__ == "__main__":
    main()
