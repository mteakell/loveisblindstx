"""Photo strips and video bands for the pages that felt bare.

Idempotent by HTML marker, so it runs after every build. Videos are the
compressed MP4s from the brand library (2.5-3.5MB each), muted and looping;
photos come from the vetted images/lib set, matched to the page topic.
"""
import glob, os, re

VIDEOS = {
 "products/roller-shades.html":
   ("videos-bathroom-roller-shade-mov.mp4", "A roller shade lowering in a Texas bathroom"),
 "products/shades.html":
   ("videos-automated-sheer-shades-mov.mp4", "Automated sheer shades operating"),
 "products/window-treatment-automations.html":
   ("videos-jana-motorized-roller-down-a-mov.mp4", "A motorized roller shade lowering on command"),
 "products/motorized-window-treatment-automations.html":
   ("videos-automated-roller-shades-mov.mp4", "Automated roller shades moving together"),
 "products/remote-window-treatments.html":
   ("videos-jana-motorized-roller-down-a-mov.mp4", "A motorized roller shade lowering on command"),
 "products/exterior-patio-shades.html":
   ("videos-automated-exterior-patio-shade-mov.mp4", "An automated exterior patio shade lowering"),
 "services/shades-installation.html":
   ("videos-motorized-cable-guided-patio-shade-mov.mp4", "A cable-guided motorized patio shade"),
 "about.html":
   ("videos-video-001-mov.mp4", "Love Is Blinds installers at work in a Texas home"),
 "how-it-works.html":
   ("videos-automated-roller-shades-mov.mp4", "A finished install: a bank of roller shades moving together"),
}

def _pool(prefixes, exclude=()):
    out = []
    for f in sorted(os.listdir("images/lib")):
        if f.startswith("_unused"): continue
        if any(f.startswith(p) for p in prefixes) and f not in exclude:
            out.append("/images/lib/" + f)
    return out


FAM_PREFIX = {
 "shutter": ("shutters-shutters",),
 "roller":  ("roller-shades",),
 "patio":   ("exterior-patio-shades",),
 "roman":   ("roman-shades", "woven-wood-shades"),
 "blinds":  ("blinds-blinds",),
 "honeycomb": ("honeycomb-shades",),
 "drapes":  ("smart-drapes",),
 "banded":  ("banded-shades",),
 "mixed":   ("shutters-shutters", "roller-shades", "exterior-patio-shades",
             "roman-shades", "honeycomb-shades", "blinds-blinds"),
}
FAM_LABEL = {
 "shutter": "Plantation shutters", "roller": "Roller shades",
 "patio": "Exterior patio shades", "roman": "Roman and woven shades",
 "blinds": "Custom blinds", "honeycomb": "Honeycomb shades",
 "drapes": "Drapery and motorization", "banded": "Banded shades",
 "mixed": "Custom window treatments",
}
ALT_T = [
 "{p} installed by Love Is Blinds in a Texas living space",
 "{p} fitted to the window opening by Love Is Blinds",
 "{p} in a Texas home, measured and installed by Love Is Blinds",
 "Close view of {p} installed by Love Is Blinds",
 "{p} across a wide Texas window, installed by Love Is Blinds",
 "{p} on a bright Texas window wall",
 "{p} in a finished Love Is Blinds installation",
 "{p} shading a Texas room in the afternoon",
]

# topic per page, else mixed
PAGE_FAM = {
 "products/plantation-shutters.html": "shutter", "products/shutters.html": "shutter",
 "products/faux-wood-blinds.html": "mixed", "products/real-wood-blinds.html": "mixed",
 "products/roller-shades.html": "roller", "products/exterior-patio-shades.html": "patio",
 "about.html": "mixed", "how-it-works.html": "mixed", "faqs.html": "mixed",
 "areas-we-serve.html": "mixed", "design-checklist.html": "roman",
}

TARGETS = (["about.html", "how-it-works.html", "faqs.html", "areas-we-serve.html",
            "design-checklist.html"] + sorted(glob.glob("products/*.html"))
           + sorted(glob.glob("services/*.html")))


def fn(name):
    for suffix in ("-jpg.webp", ".webp", "-jpeg.webp"):
        if os.path.exists("images/lib/" + name + suffix):
            return "/images/lib/" + name + suffix
    return None


def strip_html(fam, label, page="", n=8):
    import hashlib
    pool = _pool(FAM_PREFIX[fam])
    if not pool:
        pool = _pool(FAM_PREFIX["mixed"])
    off = int(hashlib.sha1(page.encode()).hexdigest()[:6], 16) % max(1, len(pool))
    shots = (pool[off:] + pool[:off])[:n]
    p = FAM_LABEL[fam]
    figs = "".join(
        f'<figure class="shot"><img src="{src}" data-alt-final '
        f'alt="{ALT_T[k % len(ALT_T)].format(p=p)}" '
        f'loading="lazy" width="2000" height="1500"></figure>'
        for k, src in enumerate(shots))
    return ('\n<!-- media:strip -->\n<section class="section"><div class="container center">'
            f'<h2 class="title">{label}</h2></div>'
            f'<div class="container"><div class="shots">{figs}</div>'
            '<p class="center" style="margin-top:24px"><a class="btn btn-secondary btn-lg" '
            'href="/gallery">See the full gallery</a></p></div></section>\n<!-- /media:strip -->\n')


def video_html(src, caption):
    return ('\n<!-- media:video -->\n'
            '<section class="ed-split vid-split bg-cream-tint"><div class="ed-inner">'
            '<div class="ed-media video-frame"><video autoplay muted loop playsinline '
            f'preload="metadata" aria-label="{caption}">'
            f'<source src="/images/video/{src}" type="video/mp4"></video></div>'
            '<div class="ed-card"><p class="ed-eyebrow">Watch it work</p>'
            f'<h2>See it move</h2><p>{caption}. Motorized, measured to the opening and '
            'installed by the same team that quoted it.</p>'
            '<a class="btn btn-primary" href="/schedule-now">Book your free consultation</a>'
            '</div></div></section>\n<!-- /media:video -->\n')


def slider_html(fam, page, n=12):
    import hashlib
    pool = _pool(FAM_PREFIX[fam])
    if not pool:
        pool = _pool(FAM_PREFIX["mixed"])
    off = int(hashlib.sha1(page.encode()).hexdigest()[:6], 16) % max(1, len(pool))
    shots = (pool[off:] + pool[:off])[:n]
    p = FAM_LABEL[fam]
    cards = "".join(
        f'<figure class="ph-card"><img src="{src}" data-alt-final '
        f'alt="{ALT_T[k % len(ALT_T)].format(p=p)}" '
        f'loading="lazy" width="2000" height="1500"></figure>'
        for k, src in enumerate(shots))
    return ('\n<!-- media:strip -->\n'
            '<section class="section ph-section"><div class="container center">'
            f'<h2 class="title">{p} we have installed across Texas</h2></div>'
            '<div class="rv-wrap">'
            '<button class="rv-nav rv-prev" type="button" aria-label="Previous photos">'
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg></button>'
            f'<div class="ph-track" tabindex="0" role="region" aria-label="Installation photos">{cards}</div>'
            '<button class="rv-nav rv-next" type="button" aria-label="More photos">'
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg></button>'
            '</div>'
            '<script>(function(){var w=document.currentScript.closest(".ph-section");'
            'var t=w.querySelector(".ph-track");'
            'var p=w.querySelector(".rv-prev"),n=w.querySelector(".rv-next");'
            'function step(d){var c=t.querySelector(".ph-card");if(!c)return;'
            'var cw=c.getBoundingClientRect().width+16;'
            'var per=Math.max(1,Math.floor(t.clientWidth/cw));'
            'var from=t.scrollLeft,by=d*cw*per;'
            't.scrollBy({left:by,behavior:"smooth"});'
            'setTimeout(function(){if(Math.abs(t.scrollLeft-from)<2)t.scrollLeft=from+by;},260);}'
            'p.addEventListener("click",function(){step(-1)});'
            'n.addEventListener("click",function(){step(1)});'
            '})();</script>'
            '</section>\n<!-- /media:strip -->\n')


SPLIT_COPY = {
 "shutter": [("Built to the opening, not trimmed to fit",
              "A shutter is a rigid panel in a frame, so an opening that is out of square gets "
              "handled by the frame style rather than hidden by the treatment. That is why every "
              "opening is measured on site before anything is ordered."),
             ("The treatment that shows up in the appraisal",
              "Shutters read from the street and carry the strongest resale story in window "
              "treatments. Painted or stained to your trim at the consultation, in hardwood or "
              "moisture-proof composite by room.")],
 "roller": [("One fabric, every light level",
             "From sheer solar screen to full blackout, the weave decides what a roller shade "
             "does. Tighter stops heat and glare, looser keeps the view. We bring the fabrics to "
             "your window so you choose against your own light."),
            ("Clean lines, almost no stack",
             "A roller shade disappears when you want the window back, which is why they carry "
             "modern builds with big glass. Cordless and motorized lifts keep the look "
             "uncluttered.")],
 "patio": [("Stop the sun before the glass",
            "An exterior shade blocks heat at the outside face of the opening, which no interior "
            "treatment can do. On a covered patio it is the difference between a space you use in "
            "July and one you look at."),
           ("Built for Texas wind",
            "Track-guided systems hold the fabric so gusts cannot work it loose, and retractable "
            "versions roll up out of the weather. Wind-rated hardware is why an exterior shade "
            "is still working in year five.")],
 "roman": [("Structure that reads as tailored",
            "Roman and woven shades bring fabric softness with a disciplined fold, and natural "
            "texture that suits lake and ranch houses. Measured to the opening so the folds land "
            "level."),
           ("Texture without the glare",
            "Woven woods filter light instead of blocking it, keeping a room bright while the "
            "squint goes. Liners add privacy or blackout where the room needs it.")],
 "blinds": [("Wood where it stays dry, faux where it does not",
             "Real wood is the lightest slat material and the only one with grain; faux wood and "
             "composite shrug off steam and splashes. Matching the material to the room is most "
             "of the decision."),
            ("The tilt is the point",
             "A slat gives you a middle setting no fabric can: light in, view out, privacy kept. "
             "Cordless and motorized lifts remove the dangling parts that date a window.")],
 "honeycomb": [("Insulation you can see on the bill",
                "Honeycomb shades trap air in their cells and cut heat transfer at the glass, "
                "which is why they are the treatment that shows up on the cooling bill. Worth the "
                "money on the west and south glass."),
               ("Quiet, soft, and out of the way",
                "Cellular shades stack small and run quietly, in light filtering through "
                "blackout. Top-down bottom-up versions keep light while holding privacy.")],
 "drapes": [("Shades that move themselves",
             "Remote, wall switch, app, voice or a schedule: motorized treatments put high "
             "windows, wide banks of glass and exterior shades on autopilot. Battery versions "
             "retrofit without wiring."),
            ("Drapery with real fullness",
             "Panels with generous fabric read as finished in a way skimpy ones never do. "
             "Motorized tracks glide wall-to-wall glass open with one command.")],
 "banded": [("Two treatments in one roller",
             "Banded shades alternate sheer and solid bands, so lining them up filters light and "
             "offsetting them closes the room. One treatment doing the day and evening job."),
            ("A modern face for big glass",
             "The banding reads architectural on wide windows and sliders, and motorization keeps "
             "wide spans easy to live with.")],
 "mixed": [("Measured by the people who install",
            "Every opening is measured on site, the quote is written from those numbers, and the "
            "team that measured returns to install. A mis-measure is ours to remake, not yours to "
            "live with."),
           ("Backed five ways",
            "Manufacturer limited lifetime warranty on factory defects, a four-year service "
            "guarantee, a price match, a free replacement for every ten treatments, and cover "
            "that transfers if you sell.")],
}


def split_html(fam, page, idx, flip):
    import hashlib
    pool = _pool(FAM_PREFIX[fam])
    if not pool:
        pool = _pool(FAM_PREFIX["mixed"])
    off = (int(hashlib.sha1(page.encode()).hexdigest()[:6], 16) + 5 + idx * 7) % len(pool)
    img = pool[off]
    copy = SPLIT_COPY.get(fam, SPLIT_COPY["mixed"])
    head, body = copy[idx % len(copy)]
    p = FAM_LABEL[fam]
    return (f'\n<!-- media:split{idx} -->\n'
            f'<section class="ed-split{" ed-flip" if flip else ""}"><div class="ed-inner">'
            f'<div class="ed-media"><img src="{img}" data-alt-final '
            f'alt="{ALT_T[(idx + 2) % len(ALT_T)].format(p=p)}" loading="lazy" '
            f'width="2000" height="1500"></div>'
            f'<div class="ed-card"><p class="ed-eyebrow">{p}</p>'
            f'<h2>{head}</h2><p>{body}</p>'
            f'<a class="btn btn-primary" href="/schedule-now">Book your free consultation</a>'
            f'</div></div></section>\n<!-- /media:split{idx} -->\n')


def band_html(fam, page):
    import hashlib
    pool = _pool(FAM_PREFIX[fam])
    if not pool:
        return ""
    img = pool[(int(hashlib.sha1(page.encode()).hexdigest()[:6], 16) + 3) % len(pool)]
    p = FAM_LABEL[fam]
    return ('\n<!-- media:band -->\n'
            f'<section class="parallax-band" style="background-image:url(\'{img}\')">'
            '<div class="container">'
            f'<p class="pb-eyebrow">{p}</p>'
            '<h2 class="pb-title">Measured at your windows, built to those numbers</h2>'
            '<p class="pb-body">The consultation is free, the quote is written, and the team '
            'that measures is the team that installs.</p>'
            '<div class="btnrow"><a class="btn btn-primary btn-lg" href="/schedule-now">'
            'Book your free consultation</a></div>'
            '</div></section>\n<!-- /media:band -->\n')


def main():
    strips = vids = 0
    for f in TARGETS:
        if not os.path.exists(f):
            continue
        s = open(f).read()
        s = re.sub(r'\n?<!-- media:strip -->.*?<!-- /media:strip -->\n?', '\n', s, flags=re.S)
        s = re.sub(r'\n?<!-- media:video -->.*?<!-- /media:video -->\n?', '\n', s, flags=re.S)
        s = re.sub(r'\n?<!-- media:band -->.*?<!-- /media:band -->\n?', '\n', s, flags=re.S)
        s = re.sub(r'\n?<!-- media:split\d -->.*?<!-- /media:split\d -->\n?', '\n', s, flags=re.S)
        payload = ""
        if f in VIDEOS:
            payload += video_html(*VIDEOS[f]); vids += 1
        base = os.path.basename(f)
        if f in PAGE_FAM: fam = PAGE_FAM[f]
        elif "shutter" in base: fam = "shutter"
        elif "patio" in base: fam = "patio"
        elif "roller" in base: fam = "roller"
        elif "honeycomb" in base or "energy" in base: fam = "honeycomb"
        elif "drap" in base or "motor" in base or "remote" in base or "automation" in base: fam = "drapes"
        elif "woven" in base or "roman" in base: fam = "roman"
        elif "blind" in base: fam = "blinds"
        elif "shade" in base: fam = "roller"
        else: fam = "mixed"
        if f.startswith(("products/", "services/")):
            # varied rhythm instead of three centered blocks in a row: an
            # editorial split early, the flipped one later, band + slider at
            # the end. Splits are threaded between existing sections.
            def _ends():
                return [m.end() for m in re.finditer(r'</section>', s[:s.find('<footer class="footer"')])]
            ends = _ends()
            if len(ends) >= 2:
                s = s[:ends[1]] + split_html(fam, f, 0, False) + s[ends[1]:]
            # the full-bleed band sits mid-page, not parked at the end
            ends = _ends()
            if len(ends) >= 4:
                s = s[:ends[3]] + band_html(fam, f) + s[ends[3]:]
            ends = _ends()
            if len(ends) >= 6:
                s = s[:ends[5]] + split_html(fam, f, 1, True) + s[ends[5]:]
            payload += slider_html(fam, f)
        else:
            payload += strip_html(fam, "Recent installs across Texas", page=f)
        strips += 1
        # insert before the closing CTA when there is one, otherwise directly
        # before the footer. rfind("<section") walked past <footer on the
        # converted pages, which parked every strip after the page ended.
        i = s.find('<section class="section closing-cta"')
        # the PAGE footer, not a <footer> element inside a component: review
        # cards attribute their author with <footer class="rv-by">, and finding
        # the bare tag parked the band inside the first review card
        jf = s.find('<footer class="footer"')
        if jf < 0:
            jf = s.rfind("<footer")
        if i < 0 or (0 < jf < i):
            i = jf
        jm = s.find("</main>")
        if 0 < jm < i:
            i = jm
        s = s[:i] + payload + s[i:]
        open(f, "w").write(s)
    print(f"media: {strips} photo strips, {vids} video bands")



# Hero overrides for converted pages, applied idempotently so a convert.py
# re-run cannot quietly restore the old photo.
def _h(name, alt):
    return ("/images/lib/" + name + "-jpg.webp", alt)


# The nicest vetted shot per product family, chosen at the real 5:2 crop.
HERO_OVERRIDE = {
 "products/index.html": _h("roller-shades-roller-shades-208",
   "A Texas great room with a stone fireplace and floor-to-ceiling roller shades by Love Is Blinds"),
 "products/blinds.html": _h("blinds-blinds-008",
   "Faux wood blinds on three windows of a shiplap wall with candle sconces"),
 "products/faux-wood-blinds.html": _h("blinds-blinds-009",
   "Faux wood blinds over a marble counter in a bright white Texas kitchen"),
 "products/real-wood-blinds.html": _h("blinds-blinds-007",
   "Real wood blinds against dark wood cabinetry in a Texas kitchen"),
 "products/plantation-shutters.html": _h("shutters-shutters-113",
   "Plantation shutters on a navy gallery wall of framed art"),
 "products/shutters.html": _h("shutters-shutters-love-05",
   "White plantation shutters opening onto a backyard pool"),
 "products/roller-shades.html": _h("roller-shades-roller-shades-237",
   "Solar roller shades behind a sectional with a pool view"),
 "products/shades.html": _h("roller-shades-roller-shades-230",
   "Roller shades in an octagonal bay beneath a chandelier"),
 "products/dual-shades.html": _h("banded-shades-banded-shades-011",
   "Banded dual shades across three tall windows"),
 "products/energy-efficient-custom-window-shades.html": _h("honeycomb-shades-honeycomb-shades-018",
   "Honeycomb shades on an arched Texas window wall"),
 "products/honeycomb-shades.html": _h("honeycomb-shades-honeycomb-shades-022",
   "Top-down honeycomb shades filtering afternoon light"),
 "products/motorized-window-treatment-automations.html": _h("roller-shades-roller-shades-245",
   "Motorized roller shades in a bright living room overlooking a pool"),
 "products/window-treatment-automations.html": _h("smart-drapes-smart-drapes-002",
   "Motorized drapery and shutters in a chandelier-lit Texas bedroom"),
 "products/remote-window-treatments.html": _h("roller-shades-roller-shades-137",
   "Remote-controlled roller shades in a sunlit Texas family room"),
 "products/panel-track-shades.html": _h("banded-shades-banded-shades-003",
   "Panel and banded shades over a breakfast nook"),
 "products/woven-wood-shades.html": _h("roman-shades-roman-shades-060",
   "Woven wood shades and rattan pendants over a Texas dining table"),
 "products/exterior-patio-shades.html": _h("exterior-patio-shades-exterior-patio-shades-drew-wrap-front",
   "Exterior shades across the wrap porch of a white Texas farmhouse"),
 "brands.html": _h("shutters-shutters-156",
   "Plantation shutters framing a lake view in a Texas living room"),
}


def apply_hero_overrides():
    for f, (src, alt) in HERO_OVERRIDE.items():
        if not os.path.exists(f):
            continue
        s = open(f).read()
        m = re.search(r'(<section class="phero[^"]*">.*?<img[^>]*src=")([^"]+)("[^>]*alt=")([^"]*)(")', s, re.S)
        if not m:
            continue
        if m.group(2) == src:
            continue
        s = s[:m.start(2)] + src + s[m.end(2):m.start(4)] + alt + s[m.end(4):]
        # kill any stale <source> above the img
        s = re.sub(r'(<section class="phero[^"]*">\s*<picture>)<source[^>]*>', r'\1', s, count=1)
        open(f, "w").write(s)
        print(f"hero override applied: {f} -> {src.split('/')[-1]}")


if __name__ == "__main__":
    main()
    apply_hero_overrides()
