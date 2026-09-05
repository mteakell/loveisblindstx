"""The gallery, rebuilt from the whole vetted library.

The converted Duda gallery repeated images and showed a few dozen. This one
draws every vetted photo in images/lib, deduplicates, groups by product
family with filter chips, lays out as a masonry wall and opens full-size in
a lightbox. No dependencies: CSS columns for the masonry, a <dialog> for the
lightbox.

Runs after convert.py, which would otherwise overwrite gallery.html.
"""
import html, json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
import extra as X
import schema as S

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

FAMS = [
 ("shutters",  ("shutters-shutters",),        "Plantation Shutters"),
 ("roller",    ("roller-shades",),            "Roller Shades"),
 ("patio",     ("exterior-patio-shades",),    "Exterior Patio Shades"),
 ("roman",     ("roman-shades", "woven-wood-shades"), "Roman & Woven"),
 ("honeycomb", ("honeycomb-shades",),         "Honeycomb Shades"),
 ("blinds",    ("blinds-blinds",),            "Custom Blinds"),
 ("drapes",    ("smart-drapes", "banded-shades"), "Drapery & Banded"),
]
ALT_T = [
 "{p} installed by Love Is Blinds in a Texas home",
 "{p} fitted to the window opening by Love Is Blinds",
 "{p} in a finished Love Is Blinds installation",
 "{p} across a bright Texas window wall",
 "Close view of {p} installed by Love Is Blinds",
 "{p} shading a Texas room",
]


def collect():
    out = []
    seen_stems = set()
    for f in sorted(os.listdir("images/lib")):
        if f.startswith("_unused") or not f.endswith(".webp"):
            continue
        if "before" in f:
            continue
        stem = re.sub(r"-(a|b)-jpg\.webp$|-jpg\.webp$|-jpeg\.webp$|\.webp$", "", f)
        if stem in seen_stems:
            continue
        seen_stems.add(stem)
        for key, prefixes, label in FAMS:
            if any(f.startswith(p) for p in prefixes):
                out.append((key, label, "/images/lib/" + f))
                break
    return out


def main():
    shots = collect()
    counts = {}
    for k, _, _ in shots:
        counts[k] = counts.get(k, 0) + 1
    chips = '<button class="gchip is-on" data-f="all">All <span>' + str(len(shots)) + "</span></button>"
    for key, prefixes, label in FAMS:
        if counts.get(key):
            chips += (f'<button class="gchip" data-f="{key}">{html.escape(label)} '
                      f'<span>{counts[key]}</span></button>')
    tiles = ""
    for i, (key, label, src) in enumerate(shots):
        alt = ALT_T[i % len(ALT_T)].format(p=label)
        tiles += (f'<figure class="gtile" data-f="{key}">'
                  f'<img src="{src}" data-alt-final alt="{html.escape(alt)}" loading="lazy" '
                  f'decoding="async" width="2000" height="1500">'
                  f'<figcaption>{html.escape(label)}</figcaption></figure>')

    url, title = "/gallery", "Install Gallery | Love Is Blinds Texas"
    desc = (f"{len(shots)} real installations across Texas: plantation shutters, roller shades, "
            "exterior patio shades, blinds and more, photographed in customers' homes.")
    gallery_node = {"@type": "ImageGallery", "@id": S.SITE + url + "#gallery",
                    "name": "Love Is Blinds Texas installation gallery",
                    "description": desc}
    nodes = X.BASE() + [S.webpage(url, title, desc, about=S.ORGID),
                        S.breadcrumbs([("Home", "/"), ("Gallery", url)]), gallery_node]
    body = (
      '<section class="phero"><picture>'
      '<img src="/images/lib/shutters-shutters-151-jpg.webp" data-alt-final '
      'alt="Open plantation shutters over a lakeside view, installed by Love Is Blinds" '
      'width="2000" height="1500" fetchpriority="high"></picture>'
      '<div class="container"><div class="phero-copy">'
      '<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span>&rsaquo;</span>'
      '<span aria-current="page">Gallery</span></nav>'
      '<h1 class="title">Real Rooms, Real Installs</h1>'
      f'<p class="lead">{len(shots)} installations photographed in Texas homes. '
      'No stock, no staging: this is the work.</p></div></div></section>'
      '<section class="section"><div class="container">'
      f'<div class="gchips">{chips}</div>'
      f'<div class="gwall">{tiles}</div>'
      '</div></section>'
      '<dialog class="glight" id="glight"><button class="gclose" aria-label="Close">&times;</button>'
      '<img alt="" id="glimg"><p id="glcap"></p></dialog>'
      '<script>(function(){'
      'var wall=document.querySelector(".gwall");'
      'document.querySelectorAll(".gchip").forEach(function(ch){'
      'ch.addEventListener("click",function(){'
      'document.querySelectorAll(".gchip").forEach(function(x){x.classList.remove("is-on")});'
      'ch.classList.add("is-on");var f=ch.dataset.f;'
      'wall.querySelectorAll(".gtile").forEach(function(t){'
      't.style.display=(f==="all"||t.dataset.f===f)?"":"none"});});});'
      'var dlg=document.getElementById("glight"),im=document.getElementById("glimg"),'
      'cap=document.getElementById("glcap");'
      'wall.addEventListener("click",function(e){var t=e.target.closest(".gtile");if(!t)return;'
      'im.src=t.querySelector("img").src;im.alt=t.querySelector("img").alt;'
      'cap.textContent=t.querySelector("figcaption").textContent;dlg.showModal();});'
      'dlg.addEventListener("click",function(e){if(e.target===dlg)dlg.close();});'
      'document.querySelector(".gclose").addEventListener("click",function(){dlg.close();});'
      '})();</script>')
    open("gallery.html", "w").write(X.shell(url, title, desc, nodes, body,
                                           img="/images/lib/shutters-shutters-151-jpg.webp"))
    print(f"gallery: {len(shots)} unique photos, {len([k for k in counts if counts[k]])} families")


if __name__ == "__main__":
    main()
