"""Keep every Formspree form on the page after it is sent (Nov 2026).

The shared footer script only caught forms with class "form-card", so the
city-form on every city and product-city page (and the wp-form on
design-checklist) did a plain POST and landed visitors on Formspree's own
thank-you page, and never fired the generate_lead event. This pass widens
the selector to any form that posts to Formspree. The partial
build/partials/footer.html carries the same change, so rebuilt pages get it too.
Idempotent. Run from the repo root: python3 build/form_inline.py
"""
import glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
OLD = "document.querySelectorAll('form.form-card')"
NEW = "document.querySelectorAll('form[action*=\"formspree.io\"]')"
n = 0
for f in glob.glob("*.html") + glob.glob("*/*.html") + glob.glob("data/queued-posts/*.html") + ["build/partials/footer.html"]:
    if f.startswith("build/") and f != "build/partials/footer.html":
        continue
    s = open(f, encoding="utf-8").read()
    if OLD in s:
        open(f, "w", encoding="utf-8").write(s.replace(OLD, NEW))
        n += 1
print(f"form_inline: {n} files updated")
