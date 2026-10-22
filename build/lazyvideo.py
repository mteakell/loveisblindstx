"""Stop background videos from downloading during page load.

The brand videos are 3-5 MB each and every one was marked autoplay. Autoplay
overrides preload="metadata", so the browser starts pulling the whole file
the moment the page opens, even when the video sits far below the fold. On a
phone that bandwidth comes straight out of the hero image and the stylesheet:
the homepage's mobile Largest Contentful Paint measured 10.1s (Oct 2026).

This pass rewrites every autoplay video to load only after the page has
finished loading AND the video is within 200px of the viewport. The poster
image shows until then, so nothing visibly changes except speed. Visitors
with reduced-motion or data-saver turned on keep the poster and never
download the video.

Idempotent: converted videos carry data-lazy-video and their <source> uses
data-src, so a second run finds nothing to change. Runs after media_rich,
which is the pass that adds most of the videos.
"""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SCRIPT = (
    '<script data-lazy-video-loader>(function(){var v=document.querySelectorAll("video[data-lazy-video]");'
    'if(!v.length)return;'
    'if(matchMedia("(prefers-reduced-motion: reduce)").matches||(navigator.connection&&navigator.connection.saveData))return;'
    'function go(x){if(x.dataset.loaded)return;x.dataset.loaded=1;'
    'x.querySelectorAll("source[data-src]").forEach(function(s){s.src=s.dataset.src});'
    'x.load();var p=x.play();if(p&&p.catch)p.catch(function(){})}'
    'function start(){if(!("IntersectionObserver" in window)){v.forEach(go);return}'
    'var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){go(e.target);io.unobserve(e.target)}})},{rootMargin:"200px"});'
    'v.forEach(function(x){io.observe(x)})}'
    'if(document.readyState==="complete")start();else addEventListener("load",start)})();</script>')

VIDEO = re.compile(r"<video\b([^>]*)>(.*?)</video>", re.S)


def convert(m):
    attrs, inner = m.group(1), m.group(2)
    if "data-lazy-video" in attrs or not re.search(r"\bautoplay\b", attrs):
        return m.group(0)
    attrs = re.sub(r"\s*\bautoplay\b", "", attrs)
    attrs = re.sub(r'\s*preload="[^"]*"', "", attrs)
    attrs = " data-lazy-video" + attrs + ' preload="none"'
    inner = re.sub(r'(<source\b[^>]*?)\ssrc="', r'\1 data-src="', inner)
    return f"<video{attrs}>{inner}</video>"


def main():
    pages = [f for f in glob.glob("**/*.html", recursive=True)
             if not f.startswith(("build/", "node_modules/"))]
    changed = 0
    for f in pages:
        t = open(f, encoding="utf-8").read()
        if "<video" not in t:
            continue
        u = VIDEO.sub(convert, t)
        if "data-lazy-video" in u and "data-lazy-video-loader" not in u:
            u = u.replace("</body>", SCRIPT + "\n</body>", 1)
        if u != t:
            open(f, "w", encoding="utf-8").write(u)
            changed += 1
    print("lazyvideo:", changed, "pages updated")


if __name__ == "__main__":
    main()
