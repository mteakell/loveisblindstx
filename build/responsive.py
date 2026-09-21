"""Responsive image variants + srcset.

Every photo was served at its full 1500-2000px width no matter how small the
slot: the home page pulled 3.1MB across 9 images, and the 88px nav menu
thumbnails downloaded the same file as a full-bleed hero. This generates
400/800/1600px variants and adds srcset/sizes so browsers fetch a size that
matches the slot. Idempotent: variants are only built when missing or stale,
and the sweep skips <img> tags that already carry a srcset.
"""
import glob, os, re, sys
from PIL import Image

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WIDTHS = (400, 800, 1600)
SRC_DIR = "images/lib"
OUT = "images/lib/r"


def build_variants():
    made = skipped = 0
    for src in sorted(glob.glob(SRC_DIR + "/*.webp")):
        name = os.path.basename(src)
        if name.startswith("_unused"):
            continue
        try:
            im = Image.open(src)
        except Exception as e:
            print("skip (unreadable):", name, e); continue
        w0 = im.width
        for w in WIDTHS:
            if w >= w0:
                continue
            dst = f"{OUT}/{w}/{name}"
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
                skipped += 1; continue
            im.copy().resize((w, round(im.height * w / w0)), Image.LANCZOS).save(
                dst, "WEBP", quality=82, method=6)
            made += 1
    print(f"variants: {made} built, {skipped} already current")


def sweep():
    """Add srcset/sizes to every <img> pointing at the library."""
    pat = re.compile(r'<img\b[^>]*?src="/images/lib/([^"/]+\.webp)"[^>]*?>')
    n_tags = n_files = 0
    for f in glob.glob("**/*.html", recursive=True) + glob.glob("data/queued-posts/*.html"):
        if f.startswith("build/"):
            continue
        s = open(f).read()
        orig = s

        def add(m):
            nonlocal n_tags
            tag, name = m.group(0), m.group(1)
            if "srcset=" in tag or name.startswith("_unused"):
                return tag
            cands = [(w, f"{OUT}/{w}/{name}") for w in WIDTHS]
            cands = [(w, p) for w, p in cands if os.path.exists(p)]
            if not cands:
                return tag
            try:
                full_w = Image.open(f"{SRC_DIR}/{name}").width
            except Exception:
                return tag
            parts = [f"/{p} {w}w" for w, p in cands] + [f"/images/lib/{name} {full_w}w"]
            hero = 'fetchpriority="high"' in tag or "phero" in tag
            sizes = "100vw" if hero else "(max-width: 700px) 100vw, 800px"
            n_tags += 1
            return tag[:-1] + f' srcset="{", ".join(parts)}" sizes="{sizes}">'

        s = pat.sub(add, s)
        if s != orig:
            open(f, "w").write(s); n_files += 1
    print(f"srcset added to {n_tags} img tags across {n_files} files")


if __name__ == "__main__":
    build_variants()
    sweep()
