"""Retire every legacy Duda image in favour of the LIB photo library.

The converted product pages still carried /images/gallery-*.jpg and friends
in their body copy. Those files are not from the Love Is Blinds photo
library and several show the wrong product (gallery-roman is a honeycomb
page card, gallery-woven holds a roller photo). Mapped here to library
photos verified by eye, with per-page overrides where the page's product
decides which library shot is correct.
"""
import glob, os, re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# legacy stem -> (library stem, alt)
DEFAULT = {
 "blinds":               ("blinds-blinds-007", "White faux wood blinds in a Texas kitchen"),
 "gallery-faux-blinds":  ("blinds-blinds-016", "White faux wood blinds on Texas bedroom windows"),
 "gallery-roller":       ("roller-shades-roller-shades-137", "Roller shades in a bright Texas living room"),
 "roller-shades":        ("roller-shades-roller-shades-137", "Roller shades in a bright Texas living room"),
 "gallery-woven":        ("woven-wood-shades-woven-wood-shades-love-01", "Bamboo woven wood shades in a Texas kitchen"),
 "gallery-roman":        ("roman-shades-roman-shades-062", "Fabric shades on three Texas bedroom windows"),
 "gallery-banded":       ("banded-shades-banded-shades-011", "Dual zebra shades with alternating sheer and solid bands"),
 "banded-after":         ("banded-shades-banded-shades-011", "Dual zebra shades with alternating sheer and solid bands"),
 "gallery-smartdrapes":  ("smart-drapes-smart-drapes-008", "Motorized drapery in a Texas primary bedroom"),
 "motorization":         ("smart-drapes-smart-drapes-008", "Motorized window treatments in a Texas bedroom"),
 "gallery-shutters-bath":("shutters-shutters-028", "Plantation shutters beside a Texas bathtub"),
 "shutters":             ("shutters-shutters-113", "Plantation shutters on a Texas front room window"),
}
# page -> {legacy stem: (library stem, alt)}; the page's own product wins
PAGE = {
 "products/real-wood-blinds.html": {
   "blinds": ("blinds-blinds-011", "Stained real wood blinds framed by drapery panels")},
 "products/honeycomb-shades.html": {
   "gallery-roman": ("honeycomb-shades-honeycomb-shades-022", "Top-down bottom-up honeycomb cellular shades")},
 "products/energy-efficient-custom-window-shades.html": {
   "gallery-roman": ("honeycomb-shades-honeycomb-shades-018", "Insulating cellular shades on an arched Texas window")},
 "products/woven-wood-shades.html": {
   "gallery-roller": ("woven-wood-shades-woven-wood-shades-011", "Bamboo woven wood shade over a Texas kitchen window")},
}


# room-local / how-hero were decorative Duda shots whose ALT claimed the
# page's product ("Dual Shades by Love Is Blinds" over a cellular photo).
# Each page now gets a library photo of its own product.
BY_FAMILY = {
 "blinds":            ("blinds-blinds-007", "Faux wood blinds in a Texas kitchen"),
 "faux-wood-blinds":  ("blinds-blinds-016", "White faux wood blinds on Texas bedroom windows"),
 "real-wood-blinds":  ("blinds-blinds-011", "Stained real wood blinds framed by drapery"),
 "shades":            ("roller-shades-roller-shades-137", "Roller shades in a bright Texas living room"),
 "roller-shades":     ("woven-wood-shades-woven-wood-shades-003", "Solar screen roller shade in a Texas dining room"),
 "honeycomb-shades":  ("honeycomb-shades-honeycomb-shades-022", "Honeycomb cellular shades in a Texas sitting room"),
 "energy-efficient-custom-window-shades":
                      ("honeycomb-shades-honeycomb-shades-018", "Insulating cellular shades on an arched window"),
 "roman-shades":      ("roman-shades-roman-shades-062", "Fabric shades on Texas bedroom windows"),
 "woven-wood-shades": ("woven-wood-shades-woven-wood-shades-011", "Bamboo woven wood shade in a Texas kitchen"),
 "dual-shades":       ("banded-shades-banded-shades-011", "Dual zebra shades with alternating sheer and solid bands"),
 "panel-track-shades":("roller-shades-roller-shades-245", "Shades across tall two-story Texas windows"),
 "shutters":          ("shutters-shutters-151", "Plantation shutters in a Texas living room"),
 "plantation-shutters":("shutters-shutters-113", "Plantation shutters on a Texas front room window"),
 "exterior-patio-shades":("exterior-patio-shades-exterior-patio-shades-005", "Exterior patio shades on a Texas porch"),
 "window-treatment-automations":("smart-drapes-smart-drapes-008", "Motorized treatments in a Texas bedroom"),
 "motorized-window-treatment-automations":("smart-drapes-smart-drapes-008", "Motorized drapery in a Texas bedroom"),
 "remote-window-treatments":("roller-shades-roller-shades-230", "Remote-controlled roller shades in a Texas room"),
 "brands":            ("shutters-shutters-151", "Custom window treatments in a Texas living room"),
}
SERVICE_FAMILY = {
 "blinds-installation": "blinds", "blinds-solutions": "blinds",
 "shades-installation": "shades", "shades-solutions": "shades",
 "shutters-installation": "shutters", "shutter-solutions": "plantation-shutters",
 "drapery-installation": "window-treatment-automations",
 "window-treatment-installation": "shades", "window-treatment-solutions": "shutters",
 "index": "shades",
}


def contextual():
    """Swap room-local / how-hero for a library photo of the page's product."""
    n = 0
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith("build/"):
            continue
        s = open(f).read()
        if "/images/room-local." not in s and "/images/how-hero." not in s:
            continue
        stem = os.path.basename(f)[:-5]
        if f.startswith("products/"):
            fam = "shades" if stem == "index" else stem
        elif f.startswith("services/"):
            fam = SERVICE_FAMILY.get(stem, "shades")
        else:
            fam = "shades"
        lib, alt = BY_FAMILY.get(fam, BY_FAMILY["shades"])
        for legacy in ("room-local", "how-hero"):
            s = re.sub(r'<source srcset="/images/' + legacy + r'\.webp"[^>]*>', "", s)
            s, k = re.subn(
                r'<img src="/images/' + legacy + r'\.jpg"([^>]*?)>',
                lambda m: ('<img src="/images/lib/' + lib + '-jpg.webp" data-alt-final alt="'
                           + alt + '"' + re.sub(r'\s*alt="[^"]*"', "", m.group(1)) + '>'),
                s)
            n += k
        open(f, "w").write(s)
    print(f"contextual swaps: {n}")


def main():
    n = files = 0
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith("build/"):
            continue
        s = open(f).read()
        o = s
        table = dict(DEFAULT)
        table.update(PAGE.get(f, {}))
        for legacy, (lib, alt) in table.items():
            # kill the <source> sibling too, so the webp does not survive the swap
            s = re.sub(r'<source srcset="/images/' + re.escape(legacy) + r'\.webp"[^>]*>', "", s)
            s, k = re.subn(
                r'<img src="/images/' + re.escape(legacy) + r'\.jpg"([^>]*?)>',
                lambda m: ('<img src="/images/lib/' + lib + '-jpg.webp" data-alt-final alt="'
                           + alt + '"' + re.sub(r'\s*alt="[^"]*"', "", m.group(1)) + '>'),
                s)
            n += k
        if s != o:
            open(f, "w").write(s)
            files += 1
    print(f"legacy images retired: {n} swaps across {files} files")
    contextual()


if __name__ == "__main__":
    main()
