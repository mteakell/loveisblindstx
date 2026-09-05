"""Product-card images verified by eye, mapped by href.

The legacy Duda gallery-*.jpg files are mislabeled at source (gallery-roman
shows a honeycomb page card, gallery-woven holds a roller photo, blinds.jpg
is sheer shadings), so cards here point at lib photos that were visually
confirmed to show the product they sell. Idempotent: keyed on href, rewrites
the whole <picture> for mapped cards wherever they appear.
"""
import glob, os, re, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CARD_IMG = {
 "/products/blinds": ("blinds-blinds-007", "White faux wood blinds in a Texas kitchen"),
 "/products/real-wood-blinds": ("blinds-blinds-011", "Stained wood blinds with drapery panels in a Texas bedroom"),
 "/products/roller-shades": ("roller-shades-roller-shades-137", "Light-filtering roller shades in a bright Texas living room"),
 "/products/honeycomb-shades": ("honeycomb-shades-honeycomb-shades-022", "Top-down bottom-up honeycomb shades beside striped armchairs"),
 "/products/energy-efficient-custom-window-shades": ("honeycomb-shades-honeycomb-shades-018", "Insulating cellular shades on an arched Texas window"),
 "/products/woven-wood-shades": ("woven-wood-shades-woven-wood-shades-003", "Textured woven shades around a Texas dining room"),
 "/products/panel-track-shades": ("roller-shades-roller-shades-245", "Wide flat fabric panels across tall two-story Texas windows"),
}

def main():
    total = 0
    for f in ["products/index.html", "index.html"]:
        s = open(f).read()
        n = 0
        for href, (img, alt) in CARD_IMG.items():
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
