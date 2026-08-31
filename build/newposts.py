"""Generate the 30 new blog posts.

Topics come from data/new-posts.json, which was picked off Semrush volume and
difficulty against what the existing 97 posts already cover. Cost, measuring,
French doors, kitchens and Roman-shade comparisons had zero coverage.

No prices are invented anywhere. Cost posts explain what actually drives the
number and route to the free measure, and PRICE_NOTE marks where real bands
from the owners would go.
"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import schema as S, territory as T

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BIZ = json.load(open("data/tx.json"))["business"]
CITIES = json.load(open("data/tx.json"))["cities"]
HEAD = open("build/partials/header.html").read()
FOOT = open("build/partials/footer.html").read()
HEAD_INNER = HEAD.split("<body", 1)[1].split(">", 1)[1]
e = lambda s: html.escape(s or "", quote=True)

PRICE_NOTE = ("We quote from the measurements we take in your home, so the number on your "
              "estimate is the number you pay. Nothing here is a placeholder range that moves "
              "once someone has been out.")

def li(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def sec(h, *body):
    return f"<h2>{e(h)}</h2>" + "".join(body)

def sub(h, *body):
    return f"<h3>{e(h)}</h3>" + "".join(body)

def p(*t):
    return "".join(f"<p>{x}</p>" for x in t)

def render(post, body_html, faqs, hero, related):
    url = "/" + post["slug"]
    title = post["title"] if len(post["title"]) <= 60 else post["title"][:60].rsplit(" ", 1)[0]
    if len(title) + 17 <= 60:
        title_tag = title + " | Love Is Blinds"
    else:
        title_tag = title
    desc = post["desc"][:155]
    faqhtml = "".join(
        f"<details><summary>{e(q)}</summary><div class='a'>{e(a)}</div></details>"
        for q, a in faqs)
    rel = "".join(f'<li><a href="{u}">{e(t)}</a></li>' for t, u in related)
    nodes = [S.organization(BIZ), S.website(BIZ), S.business(BIZ),
             S.webpage(url, title_tag, desc, about=S.ORGID, primary=hero),
             S.blogposting(url, post["title"], desc, post["published"], image=hero),
             S.breadcrumbs([("Home", "/"), ("Blog", "/blog"), (post["title"][:60], url)]),
             S.faq(url, faqs)]
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title_tag)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{S.SITE}{url}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#3A4D5C">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{e(BIZ['name'])}">
<meta property="og:title" content="{e(title_tag)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{S.SITE}{url}">
<meta property="og:image" content="{S.SITE}{hero}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title_tag)}">
<meta name="twitter:description" content="{e(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css">
{S.render(nodes)}
</head>
<body>
{HEAD_INNER}
<main>
<article class="section">
  <div class="container">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">&rsaquo;</span>
      <a href="/blog">Blog</a><span class="sep">&rsaquo;</span>{e(post["title"][:70])}</nav>
    <h1 class="title">{e(post["title"])}</h1>
    <div class="post-body">
      <img src="{hero}" alt="{e(post["title"])}" width="1200" height="800" fetchpriority="high">
{body_html}
      <h2>Common questions</h2>
    </div>
    <div class="faq">{faqhtml}</div>
    <div class="post-body">
      <h2>Related reading</h2>
      <ul>{rel}</ul>
    </div>
    <div class="btnrow">
      <a class="btn btn-primary btn-lg" href="/schedule-now">Book a free in-home measure</a>
      <a class="btn btn-secondary btn-lg" href="tel:{BIZ["tel"]}">Call {e(BIZ["phone"])}</a>
    </div>
  </div>
</article>
</main>
{FOOT}'''
