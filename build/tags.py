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


if __name__ == "__main__":
    main()
