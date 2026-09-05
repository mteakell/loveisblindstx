"""/products/roman-shades: a page Duda never had.

Romans are all over the catalogue and the blog, and the term has its own
search demand, but neither site ever gave them a page. Content follows the
converted product-page shape; the media passes decorate it like the rest.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import extra as X
import schema as S
import html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

URL = "/products/roman-shades"
TITLE = "Roman Shades in Texas | Custom Built & Installed"
DESC = ("Custom roman shades for Texas homes: flat, relaxed and banded folds, light filtering "
        "to blackout, measured in your home and installed by the team that quoted them.")

FAQS = [
 ("What is the difference between flat and relaxed roman shades?",
  "A flat roman drops in clean horizontal folds and suits tailored, modern rooms. A relaxed roman "
  "curves softly at the bottom and reads warmer and more traditional. Both are built to the "
  "measured opening, so the folds land level."),
 ("Do roman shades work for privacy at night?",
  "With the right liner, yes. A privacy liner stops silhouettes; a blackout liner darkens the room "
  "entirely. Unlined romans filter light beautifully but are a daytime treatment."),
 ("Are roman shades a good fit for kitchens?",
  "In a wipeable fabric and mounted clear of the splash zone, they are one of the best-looking "
  "options over a sink. For steamier rooms we usually steer to faux wood or composite instead."),
 ("Can roman shades be motorized?",
  "Yes. Cordless lift is standard for safety, and motorized romans run from a remote, wall switch, "
  "app or schedule, which suits tall or hard-to-reach windows."),
]


def main():
    faq_html = "".join(
        f'<details><summary>{html.escape(q)}</summary><div class="a">{html.escape(a)}</div></details>'
        for q, a in FAQS)
    nodes = X.BASE() + [
        S.webpage(URL, TITLE, DESC, about=S.ORGID),
        S.breadcrumbs([("Home", "/"), ("Products", "/products"), ("Roman Shades", URL)]),
        S.faq(URL, FAQS),
        S.service(URL, "Custom Roman Shades in Texas",
                  "Measurement, custom order and professional installation of flat, relaxed and "
                  "banded roman shades for Texas homes.", S.BIZID,
                  catalog=["Flat fold romans", "Relaxed fold romans", "Banded romans",
                           "Blackout-lined romans", "Motorized romans"]),
    ]
    body = f'''
<section class="phero"><picture><img src="/images/lib/roman-shades-roman-shades-060-jpg.webp"
  data-alt-final alt="Woven and roman shades over a Texas dining table beneath rattan pendants"
  width="2000" height="1500" fetchpriority="high"></picture>
  <div class="container"><div class="phero-copy">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span class="sep">&rsaquo;</span>
    <a href="/products">Products</a> <span class="sep">&rsaquo;</span>Roman Shades</nav>
    <h1 class="title">Roman Shades, Tailored to Texas Windows</h1>
    <p class="lead">Fabric softness with a disciplined fold. Flat, relaxed and banded romans,
      light filtering through blackout, measured at your windows and installed by the team that
      quoted them.</p>
    <div class="hero-actions btnrow">
      <a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a>
      <a class="btn btn-secondary btn-lg" href="tel:+18665182999">Call (866) 518-2999</a>
    </div>
  </div></div>
</section>

<section class="section"><div class="container split media-right">
  <div class="body">
    <h2 class="title">The fold is the decision</h2>
    <div class="prose"><p>A roman shade is one piece of fabric trained into folds, and the fold
      style sets the character of the room. Flat folds read tailored and modern. Relaxed folds
      curve gently and soften a traditional room. Banded romans alternate fabric weights for a
      structured, designer look. All three are built to measurements we take on site, which is why
      the folds land level and the reveal stays even.</p></div>
  </div>
  <div class="media"><img src="/images/lib/roman-shades-roman-shades-062-jpg.webp" data-alt-final
    alt="Flat-fold roman shades across three windows in a Texas bedroom" loading="lazy"
    width="2000" height="1500"></div>
</div></section>

<section class="section bg-cream-tint"><div class="container split">
  <div class="body">
    <h2 class="title">Liners do the practical work</h2>
    <div class="prose"><p>Unlined romans filter daylight and glow. A privacy liner stops
      silhouettes after dark. A blackout liner turns a bedroom genuinely dark, and an insulating
      liner earns its keep on west glass. The fabric sets the look; the liner sets what the shade
      actually does, and both get chosen at your window with the light in front of you.</p></div>
  </div>
  <div class="media"><img src="/images/lib/roman-shades-roman-shades-061-jpg.webp" data-alt-final
    alt="Relaxed roman shades flanking french doors in a Texas sitting room" loading="lazy"
    width="2000" height="1500"></div>
</div></section>

<section class="section"><div class="container center">
  <h2 class="title">Roman shade questions, answered</h2></div>
  <div class="container"><div class="faq">{faq_html}</div></div>
</section>

<section class="section closing-cta"><div class="container center">
  <h2 class="title">Get roman shades priced for your windows</h2>
  <p class="lead">Free in-home consultation anywhere we serve. Measured by us, quoted in writing,
    installed by the same team.</p>
  <div class="btnrow" style="justify-content:center">
    <a class="btn btn-primary btn-lg" href="/schedule-now">Book your free consultation</a>
    <a class="btn btn-secondary btn-lg" href="tel:+18665182999">Call (866) 518-2999</a>
  </div>
</div></section>'''
    open("products/roman-shades.html", "w").write(
        X.shell(URL, TITLE, DESC, nodes, body, img="/images/lib/roman-shades-roman-shades-060-jpg.webp"))
    print("products/roman-shades.html written")


if __name__ == "__main__":
    main()
