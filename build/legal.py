"""Privacy Policy and Terms of Service. Nov 2026.

The privacy policy written in September described a site with one analytics
script and no advertising cookies. By November the site ran GA4, Google Tag
Manager (which carries a Google Ads conversion tag and the conversion
linker), CallRail call tracking, Vercel Web Analytics and the Venbit site
agent, and the forms collected ZIP codes. A policy that understates what a
site collects is worse than none, so it was rewritten against build/tags.py
and the live GTM container (GTM-WCKH3TQ5, checked Nov 4 2026).

There was no Terms of Service page at all. This adds /terms-of-service,
built from the privacy page's shell so chrome, schema and tags match, plus a
footer link on every page. Both pages carry standard text-message language
(STOP/HELP, no sharing of mobile opt-in data) so they can back an SMS
registration. Facts about Love Is Blinds come from the site: the five
guarantees as worded in data/guarantees.json, the written quote, the same
team measuring and installing, remakes against approved measurements.

Rerun-safe: rewrites both pages' content blocks and the footer link in place.
If CONTACT details or tags change, edit here and rerun, then tags/sitemap.
"""
import glob, html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

UPDATED = "November 4, 2026"
EMAIL = "access@loveisblindstx.com"
PHONE, TEL = "(866) 518-2999", "+18665182999"
ADDRESS = "9500 Ray White Rd, Suite 276, Fort Worth, TX 76244"
SITE = "https://www.loveisblindstx.com"

CONTACT = (f'<p>Love Is Blinds Texas<br>{ADDRESS}<br>'
           f'<a href="mailto:{EMAIL}">{EMAIL}</a><br>'
           f'<a href="tel:{TEL}">{PHONE}</a></p>')

PRIVACY = f"""<p class="lead">This policy explains what information loveisblindstx.com collects, what it
is used for, and which services handle it. It is written to match what the site actually runs.</p>

<h2>Who we are</h2>
<p>Love Is Blinds Texas is a group of locally owned Love Is Blinds locations serving DFW, North Texas,
Dallas, Waco, Austin and the Cedar Creek Lake area, sharing this website. When you contact us, your
request goes to the location that serves your city.</p>

<h2>Information you give us</h2>
<ul>
<li><strong>Consultation forms:</strong> your first and last name, phone number, email address, city,
ZIP code, the products you are interested in, and anything you choose to write in the message.</li>
<li><strong>Phone calls:</strong> when you call a number shown on this site, our call tracking service
records your phone number, the time and length of the call, and which page or ad led to the call.
Calls may be recorded for quality and training.</li>
<li><strong>Website chat:</strong> if you use the chat assistant on the site, the messages you type are
collected so we can answer you.</li>
</ul>

<h2>Information collected automatically</h2>
<p>Like most websites, this site collects standard usage information: the pages you visit, how you
arrived (for example a search or an ad), your device and browser type, and your approximate location
based on your IP address. This is collected through the analytics and advertising tools listed below,
some of which use cookies.</p>

<h2>How we use it</h2>
<ul>
<li>To respond to your request, schedule your in-home consultation, prepare your quote, and install and
service your window treatments</li>
<li>To understand how the site is used and improve it</li>
<li>To measure whether our advertising leads to consultation requests</li>
</ul>
<p>We do not sell your personal information, and we do not rent or share it with anyone outside the
business for their own marketing.</p>

<h2>Services that process your information</h2>
<ul>
<li><strong>Formspree</strong> delivers consultation form submissions to us.</li>
<li><strong>CallRail</strong> provides call tracking for the phone numbers shown on the site.</li>
<li><strong>Venbit</strong> provides site analytics and the website chat assistant.</li>
<li><strong>Google</strong> provides Google Analytics, Google Tag Manager, Google Ads conversion
measurement, Google Fonts and the Google Maps embeds on our location pages.</li>
<li><strong>Vercel</strong> hosts the site, keeps standard server logs such as IP addresses, and provides
Vercel Web Analytics, which measures page views without cookies.</li>
</ul>
<p>Each of these services handles data under its own privacy policy.</p>

<h2>Cookies and advertising</h2>
<p>Google Analytics uses cookies to count visits and understand how the site is used. When you arrive
from one of our Google ads, Google Ads stores an ad click identifier in a cookie so we can tell whether
the ad led to a consultation request. Google Maps and other embeds may set their own cookies.</p>
<p>You can block or delete cookies in your browser settings, opt out of Google Analytics with
<a href="https://tools.google.com/dlpage/gaoptout" rel="noopener">Google's opt-out add-on</a>, and
manage ad personalization in <a href="https://myadcenter.google.com/" rel="noopener">Google's My Ad
Center</a>.</p>

<h2>Text messages</h2>
<p>If you give us your mobile number and agree to receive text messages, we use it only to contact you
about your request, consultation, order or installation. You can reply STOP to any message to stop
receiving texts, or HELP for help.</p>
<p>No mobile information will be shared with third parties or affiliates for marketing or promotional
purposes. Text messaging originator opt-in data and consent are excluded from every category of sharing
described in this policy and will not be shared with any third parties.</p>

<h2>How long we keep it</h2>
<p>We keep consultation requests and customer records for as long as they are useful for serving you,
including warranty and service needs, and you can ask us to delete yours at any time.</p>

<h2>Your choices</h2>
<p>You can ask what information we hold about you, ask us to correct it, or ask us to delete it. Email
<a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{TEL}">{PHONE}</a>. If you prefer not to use
the forms, every page lists a phone number.</p>

<h2>Security</h2>
<p>We use reasonable measures to protect the information you send us, and the site is served only over
encrypted HTTPS. No method of transmission or storage is perfectly secure.</p>

<h2>Children</h2>
<p>This site is not directed at children, and we do not knowingly collect information from anyone
under 13.</p>

<h2>Changes</h2>
<p>When what the site collects changes, this page changes with it. This policy was last updated on
{UPDATED}. See also our <a href="/terms-of-service">Terms of Service</a>.</p>

<h2>Contact</h2>
{CONTACT}"""

G = {g_id: (name, text) for g_id, name, text in [
    ("lifetime", "Limited Lifetime Warranty",
     "Your window treatments come with a manufacturer's limited lifetime warranty. Factory defects are "
     "covered for life."),
    ("price-match", "Apples-to-Apples",
     "An apples-to-apples price-match guarantee."),
    ("guaranten", "GuaranTEN",
     "For every ten window treatments you purchase, we will replace one for free."),
    ("service", "Here-4-You",
     "A 4-year service guarantee: if you have an issue with your window treatments, we will come out and "
     "service your blinds, shades or shutters at no cost."),
    ("transferable", "Transferable Warranty",
     "Our warranties transfer if you sell your home."),
]}

TERMS = f"""<p class="lead">These terms cover your use of loveisblindstx.com and how consultations, quotes
and orders work with Love Is Blinds Texas. By using this site, you agree to them.</p>

<h2>Who we are</h2>
<p>Love Is Blinds Texas is a group of locally owned Love Is Blinds locations serving DFW, North Texas,
Dallas, Waco, Austin and the Cedar Creek Lake area, sharing this website. Your quote and any order are
with the location that serves your city.</p>

<h2>Using this website</h2>
<p>This site is provided for general information about our products and services. Product details,
photos and articles describe what we typically install and may change without notice. Photos show past
installations and examples; your products are built to your own windows and selections. Nothing on this
site is an offer to sell at a particular price.</p>

<h2>Consultations and quotes</h2>
<p>In-home consultations are free, and there is no obligation to order. Prices are set only by the
written quote you receive for your project, which includes installation. Your written quote and any
agreement you sign when you order govern your project and take priority over anything on this website.</p>

<h2>Orders, measuring and installation</h2>
<ul>
<li>We measure your windows ourselves, and your products are custom made to those measurements and to
the selections you approve.</li>
<li>Timelines on this site are typical estimates. Your expected timeline is confirmed in writing on your
quote, and manufacturing or shipping delays can affect it.</li>
<li>For installation day, please provide access to the windows on your order and a safe place to
work.</li>
<li>If a product does not match the approved measurements, we remake it at no cost.</li>
<li>Because products are made to order, cancellation and return terms are set out in your written
agreement.</li>
</ul>

<h2>Guarantees and warranties</h2>
<p>Love Is Blinds Texas offers the following guarantees, subject to the terms in your written agreement
and the manufacturer's warranty for your products:</p>
<ul>
{''.join(f'<li><strong>{n}:</strong> {t}</li>' for n, t in G.values())}
</ul>

<h2>Calls, texts and email</h2>
<p>When you submit a form or contact us, you agree that we may contact you by phone, email or text about
your request, consultation, order or installation. Calls to numbers on this site are handled by a call
tracking service and may be recorded for quality and training.</p>
<p>If you opt in to text messages, message frequency varies, and message and data rates may apply. Reply
STOP to cancel at any time or HELP for help. Agreeing to texts is not a condition of any purchase.
Carriers are not liable for delayed or undelivered messages. See our
<a href="/privacy-policy">Privacy Policy</a> for how we handle your information.</p>

<h2>Reviews</h2>
<p>Customer reviews shown on this site come from our Google Business Profiles and reflect the opinions
of the customers who wrote them.</p>

<h2>Intellectual property</h2>
<p>The text, photos, logos and design of this site belong to Love Is Blinds or its licensors. You may
view and share pages for personal use, but you may not copy, sell or reuse site content for commercial
purposes without written permission. Love Is Blinds is a trademark of its owner.</p>

<h2>Links to other sites</h2>
<p>This site links to outside services such as Google Maps and review pages. We do not control those
sites and are not responsible for their content or practices.</p>

<h2>Disclaimers and limitation of liability</h2>
<p>This website is provided "as is." To the fullest extent permitted by law, Love Is Blinds Texas is not
liable for indirect or consequential damages arising from use of this website. Nothing in these terms
limits the warranties that come with your products or your rights under your written agreement or
Texas law.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of the State of Texas.</p>

<h2>Changes</h2>
<p>We may update these terms from time to time, and changes apply from the date they are posted. These
terms were last updated on {UPDATED}.</p>

<h2>Contact</h2>
{CONTACT}"""

PRIV_DESC = ("What loveisblindstx.com collects, how it is used, the services that process it, "
             "cookies, text messages, and how to ask us to delete your information.")
TERMS_DESC = ("Terms for using loveisblindstx.com and how consultations, written quotes, orders, "
              "guarantees, calls and text messages work with Love Is Blinds Texas.")

PROSE = re.compile(r'(<div class="prose">\n).*?(\n</div>\n</div></section>)', re.S)


def set_prose(t, body):
    assert PROSE.search(t), "prose block not found"
    return PROSE.sub(lambda m: m.group(1) + body + m.group(2), t, count=1)


def set_desc(t, desc):
    for attr in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        t = re.sub(r'(<meta ' + attr + r' content=")[^"]*(")',
                   lambda m: m.group(1) + html.escape(desc, quote=True) + m.group(2), t)
    return t


def main():
    src = open("privacy-policy.html", encoding="utf-8").read()
    old_desc = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', src).group(1))

    priv = set_desc(set_prose(src, PRIVACY), PRIV_DESC)
    priv = priv.replace(json_str(old_desc), json_str(PRIV_DESC))
    open("privacy-policy.html", "w", encoding="utf-8").write(priv)

    terms = set_prose(src, TERMS)
    terms = set_desc(terms, TERMS_DESC).replace(json_str(old_desc), json_str(TERMS_DESC))
    terms = terms.replace(json_str(PRIV_DESC), json_str(TERMS_DESC))
    for a, b in [("Privacy Policy | Love Is Blinds Texas", "Terms of Service | Love Is Blinds Texas"),
                 (f"{SITE}/privacy-policy", f"{SITE}/terms-of-service"),
                 ('<h1 class="title">Privacy Policy</h1>', '<h1 class="title">Terms of Service</h1>'),
                 ('&rsaquo;</span>Privacy Policy</nav>', '&rsaquo;</span>Terms of Service</nav>'),
                 ('"name": "Privacy Policy"', '"name": "Terms of Service"'),
                 ("Love Is Blinds Texas privacy policy", "Love Is Blinds Texas terms of service")]:
        terms = terms.replace(a, b)
    assert "privacy-policy" not in re.sub(r'href="/privacy-policy"', "", terms).split("<body", 1)[0], \
        "privacy URL left in terms head"
    open("terms-of-service.html", "w", encoding="utf-8").write(terms)

    # footer: Privacy Policy · Terms of Service · Sitemap, on every page and the partial
    old = '<a href="/privacy-policy">Privacy Policy</a> &nbsp;&middot;&nbsp; <a href="/sitemap.xml">'
    new = ('<a href="/privacy-policy">Privacy Policy</a> &nbsp;&middot;&nbsp; '
           '<a href="/terms-of-service">Terms of Service</a> &nbsp;&middot;&nbsp; <a href="/sitemap.xml">')
    n = 0
    for f in ["build/partials/footer.html"] + [p for p in glob.glob("**/*.html", recursive=True)
                                                if not p.startswith(("build/", "node_modules/"))]:
        t = open(f, encoding="utf-8").read()
        if old in t and new not in t:
            open(f, "w", encoding="utf-8").write(t.replace(old, new))
            n += 1
    print(f"legal: privacy policy rewritten, terms of service written, footer link added to {n} files")


def json_str(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


if __name__ == "__main__":
    main()
