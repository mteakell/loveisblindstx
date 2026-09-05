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
    return ('\n<!-- media:video -->\n<section class="section bg-cream-tint"><div class="container center">'
            '<h2 class="title">See it move</h2>'
            f'<p class="lead">{caption}.</p></div>'
            '<div class="container" style="max-width:880px">'
            '<div class="video-frame"><video autoplay muted loop playsinline '
            f'preload="metadata" aria-label="{caption}">'
            f'<source src="/images/video/{src}" type="video/mp4"></video></div>'
            '</div></section>\n<!-- /media:video -->\n')


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
            payload += band_html(fam, f)
            payload += slider_html(fam, f)
        else:
            payload += strip_html(fam, "Recent installs across Texas", page=f)
        strips += 1
        # insert before the closing CTA when there is one, otherwise directly
        # before the footer. rfind("<section") walked past <footer on the
        # converted pages, which parked every strip after the page ended.
        i = s.find('<section class="section closing-cta"')
        jf = s.find("<footer")
        if i < 0 or (0 < jf < i):
            i = jf
        jm = s.find("</main>")
        if 0 < jm < i:
            i = jm
        s = s[:i] + payload + s[i:]
        open(f, "w").write(s)
    print(f"media: {strips} photo strips, {vids} video bands")


if __name__ == "__main__":
    main()
