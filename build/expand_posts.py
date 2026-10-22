"""Deepen the short blog posts. Oct 2026, at Maddie's direction: expand, never merge.

The October audit found 32 posts under 500 words. Each one here gets two or
three new sections inserted before its "Common questions" block. Rules the
copy was written to:
  * every claim about Love Is Blinds traces to the site: the five guarantees
    as worded in data/guarantees.json, the two-to-four-week timeline, the same
    team measuring and installing, the written quote, remakes against the
    approved measurements
  * no product options the owners have not confirmed (louver sizes, openness
    choices offered, motor brands, voice assistants, skylights, wind sensors);
    general how-it-works knowledge is fine, a promise about our catalog is not
  * no prices, no em dashes, no "honest", no "X, not Y" constructions
can-existing-shades-be-motorized is held in the queue and is left alone until
the owners answer.

Idempotent: the inserted block sits between lib:expand markers and is
replaced in place on every run, so editing the copy and rerunning updates the
posts. Runs on live posts and on queued posts in data/queued-posts, and the
publisher reruns it, so a queued post that gets re-rendered picks it up again.
"""
import datetime, glob, html, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(ROOT)
import expand_a, expand_b, expand_c, expand_d

E = {}
for mod in (expand_a, expand_b, expand_c, expand_d):
    dup = set(E) & set(mod.E)
    assert not dup, f"slug in two batches: {dup}"
    E.update(mod.E)

EXPANDED_ON = "2026-10-22"
START, END = "<!-- lib:expand -->", "<!-- /lib:expand -->"
ANCHOR = re.compile(r"(\n\s*)<h2>Common questions</h2>")

BANNED = [(re.compile("—"), "em dash"),
          (re.compile(r"\bhonest(ly)?\b", re.I), "'honest'"),
          (re.compile(r"\bnot just\b", re.I), "'not just'"),
          (re.compile(r"\w, not (a |an |the )?\w+[.,]"), "X, not Y")]


def lint():
    bad = []
    for slug, spec in E.items():
        for h2, blocks in spec["sections"]:
            texts = [h2] + [x for b in blocks for x in (b if isinstance(b, list) else [b])]
            for t in texts:
                plain = re.sub(r"<[^>]+>", "", t)
                for rx, why in BANNED:
                    if rx.search(plain):
                        bad.append(f"{slug}: {why}: {plain[:90]}")
    return bad


def render(spec):
    out = []
    for h2, blocks in spec["sections"]:
        out.append(f"<h2>{html.escape(h2, quote=False)}</h2>")
        for b in blocks:
            if isinstance(b, list):
                out.append("<ul>" + "".join(f"<li>{x}</li>" for x in b) + "</ul>")
            else:
                out.append(f"<p>{b}</p>")
    return START + "".join(out) + END


def bump_modified(t):
    pub = re.search(r'"datePublished":\s*"([0-9-]+)"', t)
    when = max(EXPANDED_ON, pub.group(1)) if pub else EXPANDED_ON
    return re.sub(r'("dateModified":\s*")[0-9-]+(")', rf"\g<1>{when}\2", t, count=1)


def apply(path, spec):
    t = open(path, encoding="utf-8").read()
    u = t
    for old, new in spec.get("replace", []):
        u = u.replace(old, new)
    block = render(spec)
    if START in u:
        u = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda m: block, u, count=1, flags=re.S)
    else:
        m = ANCHOR.search(u)
        if not m:
            return "no anchor"
        u = u[:m.start()] + m.group(1) + block + u[m.start():]
    if u != t:
        u = bump_modified(u)
        open(path, "w", encoding="utf-8").write(u)
        return "updated"
    return "unchanged"


def main():
    bad = lint()
    if bad:
        print("\n".join(bad))
        sys.exit("expand_posts: copy failed lint, nothing written")
    tally = {}
    for slug, spec in E.items():
        for path in (f"{slug}.html", f"data/queued-posts/{slug}.html"):
            if os.path.exists(path):
                r = apply(path, spec)
                tally[r] = tally.get(r, 0) + 1
                if r == "no anchor":
                    print("no Common questions anchor:", path)
    print("expand_posts:", len(E), "posts,", tally)


if __name__ == "__main__":
    main()
