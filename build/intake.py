"""Owner intake page. Internal tool, noindexed, lives at /job-notes.

The design constraint is that installers will not fill in a long form. So:
everything except who/where is optional, it works one-handed on a phone in a
driveway, and there is a voice-note escape hatch for anyone who would rather
talk than type.
"""
import html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import schema as S, territory as T
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BIZ = json.load(open("data/tx.json"))["business"]
CITIES = json.load(open("data/tx.json"))["cities"]
D = json.load(open("data/intake-design.json"))
HEAD = open("build/partials/header.html").read()
FOOT = open("build/partials/footer.html").read()
HEAD_INNER = HEAD.split("<body", 1)[1].split(">", 1)[1]
e = lambda s: html.escape(s or "", quote=True)

def build():
    owners = "".join(f'<option>{e(m["name"])}</option>' for m in T.TEAM)
    cities = "".join(f'<option>{e(c["label"])}</option>'
                     for c in sorted(CITIES, key=lambda x: x["label"]))
    prompts = ""
    for cat, qs in D["prompts"].items():
        items = "".join(f"<li>{e(q)}</li>" for q in qs)
        prompts += (f'<details><summary>{e(cat)}</summary>'
                    f'<div class="a"><ul>{items}</ul></div></details>')
    body = f'''<section class="section">
  <div class="container">
    <h1 class="title">Job notes</h1>
    <p class="lead">Two minutes after an install. Only the first two boxes are required,
      everything else is whatever you can be bothered to type. One good sentence is worth
      more than a full form.</p>
    <p class="sml">This page is for the team. It is not linked from the site and it does not
      appear in search.</p>

    <form class="form-card" action="https://formspree.io/f/xbgjdnvg" method="POST">
      <input type="hidden" name="_subject" value="Job notes from the field">
      <div class="field-row">
        <div class="field">
          <label for="who">Who is this <span aria-hidden="true">*</span></label>
          <select id="who" name="who" required><option value="">Choose</option>{owners}</select>
        </div>
        <div class="field">
          <label for="city">City <span aria-hidden="true">*</span></label>
          <select id="city" name="city" required><option value="">Choose</option>{cities}</select>
        </div>
      </div>

      <div class="field">
        <label for="hood">Subdivision or neighbourhood</label>
        <input id="hood" name="subdivision" type="text"
               placeholder="Stonebridge Ranch, the older part of Grapevine, off FM 1187">
        <span class="sml">This one is gold. Nobody else publishes which neighbourhoods have
          which window problems.</span>
      </div>

      <div class="field-row">
        <div class="field">
          <label for="product">What went in</label>
          <input id="product" name="product" type="text"
                 placeholder="Solar shades, 5% openness, motorized">
        </div>
        <div class="field">
          <label for="room">Room</label>
          <input id="room" name="room" type="text" placeholder="Living room, west wall">
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label for="facing">Which way do the windows face</label>
          <select id="facing" name="facing">
            <option value="">Not sure</option><option>West</option><option>South</option>
            <option>East</option><option>North</option><option>Mixed</option></select>
        </div>
        <div class="field">
          <label for="count">How many openings</label>
          <input id="count" name="openings" type="text" placeholder="7">
        </div>
      </div>

      <div class="field">
        <label for="asked">What did they ask for first</label>
        <input id="asked" name="asked_for" type="text"
               placeholder="They wanted blackout blinds in the living room">
      </div>

      <div class="field">
        <label for="rec">What did you actually recommend, and why</label>
        <textarea id="rec" name="recommended" rows="3"
          placeholder="Solar shades instead. West wall, they wanted to keep the view, blackout would have made them turn lights on all day."></textarea>
        <span class="sml">This is the bit that becomes a blog post. The reasoning matters more
          than the product.</span>
      </div>

      <div class="field">
        <label for="solved">Anything you had to solve on site</label>
        <textarea id="solved" name="solved" rows="2"
          placeholder="Frame was 3/8 out of square, went outside mount with overlap."></textarea>
      </div>

      <div class="field">
        <label for="surprise">Did anything surprise the customer</label>
        <textarea id="surprise" name="surprise" rows="2"
          placeholder="They did not know exterior shades cool the room behind the glass too."></textarea>
      </div>

      <div class="field">
        <label for="photos">Photos</label>
        <input id="photos" name="photos" type="text"
               placeholder="Texted to Maddie / in the shared album / none this time">
        <span class="sml">Real job photos beat stock every time. A phone shot is fine.</span>
      </div>

      <div class="field">
        <label for="voice">Would rather talk than type?</label>
        <input id="voice" name="voice_note" type="text"
               placeholder="Voice note sent">
        <span class="sml">Record a voice memo on the drive to the next job and send it. Same
          value, no typing.</span>
      </div>

      <button class="btn btn-primary btn-lg btn-block" type="submit">Send it</button>
      <p class="sml" style="margin-top:10px">No customer names or addresses unless they have
        said yes to being mentioned.</p>
    </form>
  </div>
</section>

<section class="section bg-cream-tint">
  <div class="container">
    <h2 class="title">If you have five minutes instead of two</h2>
    <p class="lead">Pick any one of these and answer it in a couple of sentences. Each one is a
      question customers actually search for and that only somebody doing the work can answer.</p>
    <div class="faq">{prompts}</div>
  </div>
</section>'''
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Job Notes | Love Is Blinds Texas</title>
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="https://www.loveisblindstx.com/job-notes">
<meta name="description" content="Internal job notes form for the Love Is Blinds Texas team.">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#3A4D5C">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css">
</head>
<body>
{HEAD_INNER}
<main>{body}</main>
{FOOT}'''
    open("job-notes.html", "w").write(doc)
    return len(D["prompts"]), sum(len(v) for v in D["prompts"].values())

if __name__ == "__main__":
    c, q = build()
    print(f"/job-notes written: {c} prompt categories, {q} prompts, noindexed")
