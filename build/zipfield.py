"""Required ZIP + typed City on the baked lead forms.

The generated forms (city_form, pc_form, design-checklist) get their zip
field at the source; the 32 converted pages carrying the original
form-card lead form are baked, so this pass upgrades them in place:
the City <select> (which offered "Other / not listed" - client rejected)
becomes a required typed field, and a required ZIP code field follows it.
Idempotent: skips any form that already has a zip input.
"""
import glob, os, re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CITY = ('<label for="city">City</label> '
        '<input type="text" id="city" name="city" placeholder="City" '
        'required autocomplete="address-level2">')
ZIP = (' <label for="zip">ZIP code</label> '
       '<input type="text" id="zip" name="zip" placeholder="ZIP code" '
       'required inputmode="numeric" pattern="\\d{5}(-\\d{4})?" '
       'autocomplete="postal-code">')

def main():
    n = 0
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith(("build/", "hero-mob/")) or f == "job-notes.html":
            continue
        s = open(f).read()
        if 'name="city"' not in s or "formspree.io" not in s:
            continue
        def fix(m):
            body = m.group(0)
            if 'name="zip"' in body:
                return body
            out = re.sub(r'<label for="city">City</label>\s*'
                         r'<select id="city" name="city">.*?</select>',
                         lambda _: CITY + ZIP, body, count=1, flags=re.S)
            return out
        out = re.sub(r'<form class="form-card"[^>]*formspree\.io.*?</form>', fix, s, flags=re.S)
        if out != s:
            open(f, "w").write(out)
            n += 1
    print(f"zip + typed city applied on {n} baked form pages")

if __name__ == "__main__":
    main()
