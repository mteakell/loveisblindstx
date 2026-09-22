"""Add Formspree's honeypot field to every form.

Bots fill every field they find; people never see this one. Formspree drops
any submission where _gotcha has a value, so real bot spam is discarded
before it reaches the inbox. Runs as a post-build pass so it covers forms
from every generator. Idempotent.

Also stamps data-venbit-form on the same form tags: Venbit only records a
form-submission event for forms carrying that attribute, so without it the
dashboard shows visits but never conversions.
"""
import glob, os, re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FIELD = ('<input type="text" name="_gotcha" class="hp" tabindex="-1" '
         'autocomplete="off" aria-hidden="true">')
pat = re.compile(r'(<form\b[^>]*formspree\.io[^>]*>)')

def main():
    n = files = 0
    for f in glob.glob("**/*.html", recursive=True) + glob.glob("data/queued-posts/*.html"):
        if f.startswith("build/"):
            continue
        s = open(f).read()
        if "formspree.io" not in s:
            continue
        orig = s
        s = pat.sub(lambda m: m.group(1) if "data-venbit-form" in m.group(1)
                    else m.group(1)[:-1] + ' data-venbit-form>', s)
        out, k = [], 0
        pos = 0
        for m in pat.finditer(s):
            tail = s[m.end():m.end() + 400]
            if "_gotcha" in tail:
                continue
            out.append(s[pos:m.end()] + FIELD); pos = m.end(); k += 1
        if k:
            out.append(s[pos:])
            s = "".join(out)
        if s != orig:
            open(f, "w").write(s)
            n += k; files += 1
    print(f"honeypot added to {n} forms across {files} files")

if __name__ == "__main__":
    main()
