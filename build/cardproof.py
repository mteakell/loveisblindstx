"""/card-proof: one noindexed page showing every product card image beside
its title, so the owners can confirm or correct product identification in a
single pass instead of trading screenshots.

Grew out of the owners catching several photos filed under the wrong product
family in the LIB library (a solar roller filed as woven wood, dual shades
shown as panel track). They can identify these instantly; we cannot.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cardfix

BADGE = {
 "high":         ("#2E6B4F", "#E8F1EC", "believed correct"),
 "owner":        ("#2E6B4F", "#E8F1EC", "confirmed by owners"),
 "NEEDS-REVIEW": ("#9C7A3C", "#F3ECDD", "please confirm"),
 "NEEDS-PHOTO":  ("#B4552E", "#F7E7DE", "no real photo exists"),
}
LABEL = {
 "/products/blinds": "Custom Blinds", "/products/faux-wood-blinds": "Faux Wood Blinds",
 "/products/real-wood-blinds": "Real Wood Blinds", "/products/shades": "Custom Window Shades",
 "/products/roller-shades": "Roller Shades", "/products/honeycomb-shades": "Honeycomb Shades",
 "/products/energy-efficient-custom-window-shades": "Energy-Efficient Shades",
 "/products/roman-shades": "Roman Shades", "/products/woven-wood-shades": "Woven Wood Shades",
 "/products/dual-shades": "Dual Shades", "/products/panel-track-shades": "Panel Track Shades",
 "/products/shutters": "Custom Shutters", "/products/plantation-shutters": "Plantation Shutters",
 "/products/window-treatment-automations": "Window Treatment Automation",
 "/products/motorized-window-treatment-automations": "Motorized Window Treatments",
 "/products/remote-window-treatments": "Remote-Controlled Treatments",
}
ORDER = ["NEEDS-PHOTO", "NEEDS-REVIEW", "high", "owner"]


def main():
    rows = sorted(cardfix.CARD_IMG.items(),
                  key=lambda kv: (ORDER.index(kv[1][2]), LABEL.get(kv[0], kv[0])))
    cards = ""
    for href, (img, alt, conf) in rows:
        fg, bg, text = BADGE[conf]
        cards += f'''
<figure class="cp">
  <img src="/images/lib/{img}-jpg.webp" alt="{alt}" loading="lazy" width="2000" height="1500">
  <figcaption>
    <b>{LABEL.get(href, href)}</b>
    <span class="badge" style="color:{fg};background:{bg}">{text}</span>
    <code>{img}</code>
  </figcaption>
</figure>'''
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Product card photo check | Love Is Blinds</title>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
 body{{font-family:'Mulish',system-ui,sans-serif;margin:0;background:#FAF7F0;color:#46535E;line-height:1.6}}
 .wrap{{max-width:900px;margin:0 auto;padding:32px 20px 70px}}
 h1{{color:#222E37;font-size:26px;margin:0 0 6px}}
 p.lede{{margin:0 0 26px;max-width:60ch}}
 .cp{{margin:0 0 24px;background:#fff;border:1px solid #E7E3DA;border-radius:14px;overflow:hidden}}
 .cp img{{display:block;width:100%;height:auto}}
 figcaption{{padding:14px 18px;display:flex;align-items:center;gap:12px;flex-wrap:wrap}}
 figcaption b{{color:#222E37;font-size:17px}}
 .badge{{font-size:11.5px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;
   padding:4px 11px;border-radius:999px}}
 code{{font-size:11.5px;color:#67737C;width:100%}}
 .note{{background:#fff;border:1px solid #E7E3DA;border-left:4px solid #E07A00;
   border-radius:10px;padding:16px 18px;margin-bottom:26px;font-size:14.5px}}
</style>
</head>
<body>
<div class="wrap">
  <h1>Product card photo check</h1>
  <p class="lede">Every product card image on the site, beside the product it is labeled as.
  If a photo is the wrong product, reply with the product name and we will swap it.
  All photos come from the Love Is Blinds photo library.</p>
  <div class="note"><b>Two we already know about:</b> Panel Track Shades has no real
  panel-track photo in the library, so it is showing wide-window shades as a placeholder.
  A real panel track install photo would replace it. Roman Shades and a couple of the
  motorization shots are best guesses, flagged below.</div>
  {cards}
</div>
</body>
</html>'''
    open("card-proof.html", "w").write(page)
    print(f"card-proof.html written ({len(rows)} cards)")


if __name__ == "__main__":
    main()
