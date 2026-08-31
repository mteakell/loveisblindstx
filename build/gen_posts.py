"""Assemble and write the 30 new posts."""
import json, os, random, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import newposts as N, content_cost as C, content_all as A, content_rest as R, content_rooms as RM
C.N = N
os.chdir(N.ROOT)

BODIES = {}
BODIES.update(A.build(N, C)); BODIES.update(R.build(N)); BODIES.update(RM.build(N))
PLAN = json.load(open("data/new-posts.json"))
EXISTING = json.load(open("data/blog-index.json"))

GENERIC_FAQ = [
 ("Do you charge for the consultation?",
  "No. The in-home consultation, the measuring and the written quote are all free, and there is no "
  "obligation to order afterwards."),
 ("How long does an order take?",
  "Most custom orders arrive within two to four weeks of approval, depending on the product line "
  "and fabric. Motorized treatments can run longer. The timeline is confirmed in writing on your quote."),
 ("What if it does not fit?",
  "We measured it, so we correct it. If an opening does not match the approved measurements we "
  "remake it and reinstall at no cost to you."),
 ("Which parts of Texas do you cover?",
  "Three territories: DFW and the Mid-Cities, North Texas from Denton up to Sherman, and East and "
  "Central Texas covering Tyler, Corsicana, Gun Barrel City, Waco and the Austin metro."),
]
COST_FAQ = [
 ("Can you give me a price over the phone?",
  "Not an honest one. Custom treatments are priced from the size of the opening, the material, the "
  "mount and whether you motorize, so the number depends on measurements we have not taken yet."),
 ("Is installation included in the quote?",
  "Yes. Our quotes cover measurement, the treatment built to those measurements, and professional "
  "installation. There is no separate trip charge."),
 ("Do you offer any financing?",
  "Ask at the consultation. What we can tell you upfront is that the quote you approve is the "
  "amount you pay, with no change after the fact."),
]
MEASURE_FAQ = [
 ("Should I measure the window or the old blind?",
  "Always the window opening. The old treatment may have been measured wrong, mounted differently, "
  "or trimmed, so copying it repeats somebody else's mistake."),
 ("Width or height first?",
  "Width first, always. Reversing the two is the single most common way a custom order goes wrong."),
 ("Do I need to measure if you are coming out anyway?",
  "No. We measure every opening on site as part of the free consultation, which is also why a "
  "measuring error is our problem rather than yours."),
]

def faqs_for(post, city_hint=None):
    base = {"cost": COST_FAQ, "measure": MEASURE_FAQ}.get(post["cluster"], [])
    out = list(base) + list(GENERIC_FAQ)
    return out[:6]

def desc_for(post):
    kw = post["kw"]
    d = {
      "cost": f"What actually drives the price of {kw.replace('how much do ','').replace('cost','').strip() or 'custom window treatments'} in Texas, and how to get a real number for your own windows.",
      "measure": f"A step by step guide to {kw}, including inside versus outside mount, the three point method, and the mistakes that cost a remake.",
      "compare": f"{post['title'].split(':')[0]}: how they differ on cost, light control, lifespan and which rooms each belongs in.",
      "room": f"{post['title']}: the options that actually work, what to decide before you order, and the mistakes we get called out to fix.",
      "patio": f"{post['title']}: how to choose, what it costs to get wrong, and what works on a Texas patio.",
      "smart": "What smart blinds actually do, which features people keep using, and what to ask before you buy.",
      "safety": "Cordless, motorized and shutter options for rooms children use, and why cord cleats are not a solution.",
      "care": "How to clean roller shades and solar screens without marking the fabric or causing mildew.",
    }[post["cluster"]]
    if len(d) > 155:
        d = d[:152].rsplit(" ", 1)[0] + "..."
    return d

def pick_hero(slug):
    pool = sorted(os.listdir("images/blog"))
    idx = sum(ord(c) for c in slug) % len(pool)
    return "/images/blog/" + pool[idx]

def related_for(post, allplan):
    same = [x for x in allplan if x["cluster"] == post["cluster"] and x["slug"] != post["slug"]][:2]
    other = [x for x in allplan if x["cluster"] != post["cluster"]]
    other = [other[sum(ord(c) for c in post["slug"]) % len(other)]] if other else []
    picks = [(x["title"], "/" + x["slug"]) for x in same + other]
    picks.append(("Exterior patio shades in Texas", "/products/exterior-patio-shades"))
    picks.append(("All Texas service areas", "/areas-we-serve"))
    return picks[:5]

if __name__ == "__main__":
    made = []
    for i, post in enumerate(PLAN):
        body = BODIES.get(post["slug"])
        if not body:
            print("MISSING BODY:", post["slug"]); continue
        post = dict(post)
        post["desc"] = desc_for(post)
        # spread publish dates back over recent weeks rather than stamping them all today
        post["published"] = f"2026-0{7 if i < 15 else 8}-{(i % 28) + 1:02d}"
        hero = pick_hero(post["slug"])
        html = N.render(post, body, faqs_for(post), hero, related_for(post, PLAN))
        open(post["slug"] + ".html", "w").write(html)
        made.append(post)
    print(f"wrote {len(made)} posts")
    # fold into the blog index
    idx = json.load(open("data/blog-index.json"))
    have = {p["url"] for p in idx}
    for post in made:
        u = "/" + post["slug"]
        if u not in have:
            idx.append({"url": u, "title": post["title"], "desc": post["desc"],
                        "date": post["published"], "img": pick_hero(post["slug"])})
    json.dump(idx, open("data/blog-index.json", "w"), indent=1)
    print(f"blog index now {len(idx)} posts")
