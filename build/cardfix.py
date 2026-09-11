"""Product-card images: LIB photo library only, verified against the title.

Two separate problems this file fixes.

1. Eight cards still pointed at legacy Duda files (/images/gallery-*.jpg,
   motorization.jpg, shutters.jpg). Those are not from the LIB photo library
   and are the wrong product in several cases. Every card now resolves to
   /images/lib/.

2. The library's FOLDER NAMES ARE NOT RELIABLE. Confirmed by the owners:
   woven-wood-shades-003 is actually a solar/screen roller shade, and several
   roller-* files show other products. So picks here are by what the photo
   SHOWS, verified by eye, not by which folder the file sits in. Where a
   filename disagrees with the product, that is expected: trust the comment.

CONFIDENCE column is honest. "owner" = confirmed by Dustin/Danny.
Anything marked NEEDS-REVIEW is a best guess awaiting owner confirmation;
build/cardproof.py renders them all on one page for a quick pass.
"""
import glob, os, re
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#  href: (library file stem, alt text, confidence)
CARD_IMG = {
 "/products/blinds":
   ("blinds-blinds-007", "White faux wood blinds over a Texas kitchen sink", "high"),
 "/products/faux-wood-blinds":
   ("blinds-blinds-016", "White faux wood blinds on three Texas bedroom windows", "high"),
 "/products/real-wood-blinds":
   ("blinds-blinds-011", "Stained real wood blinds framed by drapery panels", "high"),
 "/products/shades":
   ("roller-shades-roller-shades-137", "Light-filtering shades across a bright Texas living room", "high"),
 # owner-confirmed screen roller, despite the woven-wood filename
 "/products/roller-shades":
   ("roller-shades-roller-shades-901", "Solar screen roller shade over a Texas dining room window", "owner"),
 "/products/honeycomb-shades":
   ("honeycomb-shades-honeycomb-shades-022", "Top-down bottom-up honeycomb cellular shades in a Texas sitting room", "high"),
 "/products/energy-efficient-custom-window-shades":
   ("honeycomb-shades-honeycomb-shades-018", "Insulating cellular shades on an arched Texas window", "high"),
 "/products/roman-shades":
   ("roman-shades-roman-shades-039", "Flat-fold roman shade over a Texas dining room window", "NEEDS-REVIEW"),
 "/products/woven-wood-shades":
   ("woven-wood-shades-woven-wood-shades-home-a", "Bamboo woven wood shades across three Texas living room windows", "NEEDS-REVIEW"),
 "/products/dual-shades":
   ("banded-shades-banded-shades-011", "Dual zebra shades with alternating sheer and solid bands", "high"),
 # Owner-supplied install photos, 2026-09-11 (closed 001, stacked open 002).
 "/products/panel-track-shades":
   ("panel-track-shades-panel-track-shades-001", "Panel track shades closed across a Texas patio slider", "owner"),
 "/products/shutters":
   ("shutters-shutters-151", "Plantation shutters across a bright Texas living room", "high"),
 "/products/plantation-shutters":
   ("shutters-shutters-113", "Plantation shutters on a Texas front room window", "high"),
 "/products/window-treatment-automations":
   ("smart-drapes-smart-drapes-008", "Motorized drapery and shades in a Texas primary bedroom", "high"),
 "/products/motorized-window-treatment-automations":
   ("roller-shades-roller-shades-hardwired-motorized-down", "Hardwired motorized shades on high two-story foyer windows", "NEEDS-REVIEW"),
 "/products/remote-window-treatments":
   ("roller-shades-roller-shades-motorized-remote-good-a", "Handheld remote controlling motorized roller shades in a Texas living room", "NEEDS-REVIEW"),
}

TARGETS = ["products/index.html", "index.html"]


def main():
    total = 0
    for f in TARGETS:
        if not os.path.exists(f):
            continue
        s = open(f).read()
        n = 0
        for href, (img, alt, _conf) in CARD_IMG.items():
            pat = re.compile(
                r'(<a class="prod-card[^"]*" href="' + re.escape(href) + r'">\s*'
                r'<span class="pic">)<picture>.*?</picture>', re.S)
            rep = (r'\1<picture><img src="/images/lib/' + img + '-jpg.webp" '
                   'data-alt-final alt="' + alt + '" loading="lazy" '
                   'width="2000" height="1500"></picture>')
            s, k = pat.subn(rep, s)
            n += k
        open(f, "w").write(s)
        print(f"{f}: {n} cards repointed")
        total += n
    return total


if __name__ == "__main__":
    main()
