"""Edit pass + reschedule for the queued posts, after the publisher stalled.

The daily task stalled on a permission prompt on Oct 1, leaving 14 posts
overdue. Before restarting, every unpublished post was read against the
site's sources and the writing rules:
  - unsourced claims removed or rewritten to what the site actually says
    (2-4 week arrival, motorized can run longer, single-visit install,
    written no-obligation quote, the five guarantees)
  - decorative closers and "honest"/"X, not Y" constructions cut
  - informational posts that overlap the new /solutions pages now link to them
One post is held until the owners confirm the service it describes.

Fixes apply to the in-memory POSTS from queue30/queue_intent and the posts
are re-rendered from there, so the queued HTML is always rebuilt from source
plus this table. Rerun-safe: only touches unpublished entries.
"""
import datetime, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import newposts as NP
import queue30, queue_intent
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

START = datetime.date(2026, 10, 22)   # restarted again Oct 22: the Mac was off Oct 15-21

# held: premise not confirmed by the owners (do they convert existing shades?)
HOLD = {"can-existing-shades-be-motorized"}

# slug -> [(old, new)] applied to body and FAQ text; every pair must match
FIX = {
 "how-long-from-order-to-install": [
  ("Here is the honest timeline we quote from, stage by stage, and the few things that stretch or shrink it.",
   "Here is the timeline stage by stage, and what can stretch it."),
  ("written quote on the spot or shortly after", "a written quote on the spot"),
  ("we schedule promptly on arrival, usually within days", "your installation is scheduled once the order arrives"),
  ("most whole-home projects finish in a single day", "installation usually happens in a single visit"),
  ("specialty components can add production time", "these can take longer than standard blinds and shades"),
  ("built-to-opening frames are the most fabrication-heavy product we install",
   "frames are built to each opening, so shutters take longer to make than blinds and shades"),
  ("Specialty shapes: arches and custom colors ride slower lines", None),
  ("Peak seasons: spring and pre-holiday windows book install calendars faster", None),
  ("and the same team that measured tracks the order and books your install",
   "and the same team that measured comes back to install"),
  ("say so at the consultation: product lines differ, and we can often steer toward the ones that land in time.",
   "say so at the consultation so the timeline is confirmed in writing before you order."),
  ("the consultation hour spent holding samples in your light is tiny against the years the treatment hangs.",
   "a little time with samples in your own light is worth it for something you will live with for years."),
  ("Most orders arrive in two to four weeks, with installation scheduled within days of arrival.",
   "Most orders arrive in two to four weeks, and installation is scheduled once your order arrives."),
  ("Shutters and specialty shapes: built-to-opening fabrication rides slower lines. Motorized components can also add time.",
   "Shutters and motorized treatments usually take longer than blinds and shades."),
  ("Often, if the deadline is on the table at consultation: product lines differ, and we can steer toward ones that land in your window.",
   "Tell us about the deadline at the consultation, and we confirm the expected timeline in writing on your quote."),
 ],
 "white-or-stained-plantation-shutter-finishes": [
  ("Both are timeless; they are simply different sentences in the same language, and rooms",
   "Both are timeless, and rooms"),
  ("This is the finish that photographs like a listing and never argues with a future paint color.",
   "It also works with any future paint color."),
  ("Real wood shutters carry stain best, since the grain is the point.",
   "Real wood shutters take stain best, because the grain shows through."),
  ("Finish chips lie under showroom light: hold them at your window, beside your trim, at the hour the room gets used. That is precisely what the in-home consultation exists to do.",
   "Finish samples look different under store lighting than at home, so hold them at your window, beside your trim, at the time of day the room gets used. That is why we bring samples to your home."),
 ],
 "best-window-treatments-allergy-homes": [
  ("Window treatments are either dust shelves or dust shields, and for allergy households the difference is felt in sleep and sinuses. The good news: the low-allergen choices are some of the best-looking products in the catalog.",
   "Some window treatments collect dust and some shed it. For a household with allergies, that difference matters most in bedrooms."),
  (", since cleaning skipped is dust kept", ""),
 ],
 "screened-porch-vs-motorized-patio-shades": [
  ("One is construction, the other is an installation, and the differences run deeper than price.",
   "One is construction and the other is an installation."),
  ("Installation is measured in days from order, not weeks of construction, and the system arrives with sun-sensor and schedule automation.",
   "Shades are installed rather than built, so there is no framing or roofing work, and motorized shades can run on a schedule."),
  ("The comparison, honestly", "The comparison"),
  ("HOA friction: retractable shades usually review easier than a structural addition", None),
  ("Plenty of homes land on both", "Some homes use both"),
  ("Generally yes by a wide margin: shades are an installation, a porch is a construction project with framing and roofing.",
   "A shade system is an installation, while a porch is a construction project with framing, roofing and sometimes permits. A free consultation gives you a written quote for the shade side to compare."),
 ],
 "custom-blinds-vs-big-box-store-blinds": [
  ("Here is the honest difference, so you can pick the route that fits your project rather than the one that happens to be nearest.",
   "Here is how the two compare, so you can pick the route that fits your project."),
  (" Boxed blinds exist for a reason, and pretending otherwise would be salesmanship.", ""),
  ("the fit, the warranty and the person who answers the phone afterward are the product. The blind itself is only half of it.",
   "the fit, the warranty and the person who answers the phone afterward matter as much as the blind itself."),
 ],
 "what-happens-at-a-free-in-home-consultation": [
  ("Here is what the hour actually looks like, so you know exactly what you are saying yes to when you book.",
   "Here is what happens during the visit, so you know what you are saying yes to when you book."),
  ("You hold them against your trim and your paint in your own light, which is the only light that matters. Texas afternoon sun through a west window will tell you more about a fabric in ten seconds than any website ever could.",
   "You hold them against your trim and your paint in your own light, which shows how each fabric will actually look in the room."),
  ("a written quote is what makes an honest comparison possible", "a written quote is what makes a fair comparison possible"),
  ("And if you are not ready, the quote is yours to keep, no follow-up pressure required",
   "If you are not ready, there is no obligation to order"),
  ("How long does an in-home window treatment consultation take?", "What happens during an in-home window treatment consultation?"),
  ("Plan for about an hour for a typical home: samples in your rooms, every window measured, and a written quote before the visit ends.",
   "We bring samples to your home, measure every window, and give you a written quote before the visit ends."),
 ],
 "questions-to-ask-before-hiring-a-window-treatment-company": [
  ("The same shutter can be a twenty-year upgrade or a headache", "The same shutter can be a long-term upgrade or a recurring problem"),
  (" A good company enjoys answering them.", ""),
 ],
 "faux-wood-vs-real-wood-blinds": [
  (", and the grain is real because it is real", ""),
  ("That is the point where this decision becomes concrete rather than theoretical.",
   "Seeing both materials at your own windows makes the choice much easier."),
 ],
 "vertical-blind-alternatives-for-sliding-glass-doors": [
  (" Of everything we install over sliders, this is the treatment people mean when they say they want vertical blinds, but nice.", ""),
  ("less so the door the dog goes in and out of forty times an afternoon", "less so a door that is used all day"),
 ],
 "whole-house-window-treatments-where-to-start": [
  ("Ten minutes with it turns the consultation into a confirmation rather than a survey.",
   "It takes about ten minutes and gives you a plan to bring to the consultation."),
 ],
 "what-a-window-treatment-quote-should-include": [
  ("How to compare two quotes honestly", "How to compare two quotes"),
  ("A lower number on a different product is not a lower price, it is a different job.",
   "A lower number on a different product describes a different job."),
  ("bring it to us: our Apples-to-Apples guarantee is a price-match promise, and it exists precisely because we would rather match an honest comparison than lose one to a padded quote that falls apart at install.",
   "bring both quotes to us: our Apples-to-Apples guarantee is a price-match promise."),
  (" The pause tells you plenty.", ""),
 ],
 "window-treatments-for-west-facing-windows-texas": [
  (", and the room the family uses most becomes the room nobody sits in from three to seven", ""),
 ],
}

# related-link additions so overlapping posts feed the commercial pages
RELATED_ADD = {
 "vertical-blind-alternatives-for-sliding-glass-doors":
   ("Sliding Glass Door Solutions", "/solutions/sliding-glass-doors"),
 "window-treatments-for-west-facing-windows-texas":
   ("Window Treatments for Texas Heat and Glare", "/solutions/heat-and-glare"),
 "custom-blinds-vs-big-box-store-blinds":
   ("Our Installation Standards", "/installation-standards"),
}


# related links that point at the wrong slug
RELATED_FIX = {
 "/the-ultimate-guide-to-stylish-plantation-shutters":
   "/transform-your-home-with-stylish-plantation-shutters-the-ultimate-guide",
 "/top-10-dog-proof-window-blinds":
   "/top-10-dog-proof-window-blinds-durable-and-pet-friendly",
 # slugs the queue posts were written against, mapped to the live posts (Oct 22)
 "/how-to-measure-for-blinds-a-room-by-room-guide":
   "/how-to-measure-for-blinds",
 "/custom-window-treatment-solutions-for-every-texas-home":
   "/custom-window-treatment-solutions-for-every-texan-home",
 "/inside-mount-vs-outside-mount-which-should-you-choose":
   "/inside-mount-vs-outside-mount-blinds",
 "/how-to-choose-a-patio-shade-openness-factor":
   "/how-to-choose-patio-shade-openness-factor",
 "/window-treatments-for-home-offices-and-glare-control":
   "/window-treatments-for-home-offices",
 "/cellular-shades-vs-roller-shades-for-texas-heat":
   "/cellular-shades-vs-roller-shades",
 "/worried-about-furniture-fading-how-to-stop-texas-sun-damage":
   "/stop-furniture-fading-texas-sun",
 "/solar-shades-vs-blackout-shades-which-do-you-need":
   "/solar-shades-vs-blackout-shades",
 "/window-treatments-that-fit-modern-homes-in-weatherford-tx":
   "/window-treatments-that-fit-the-way-modern-homes-are-lived-in",
 "/why-cordless-blinds-are-becoming-the-new-standard-in-home-safety":
   "/the-shift-to-cordless-window-treatments",
 "/blackout-curtains-vs-blackout-blinds-which-one-is-right-for-you":
   "/what-is-the-difference-between-blackout-and-blackout-blinds",
 "/why-your-motorized-blinds-are-not-responding-a-simple-checklist":
   "/motorized-blinds-not-responding-checklist",
}


def _apply(text, old, new):
    if new is None:      # a whole list item to drop
        return text.replace(f"<li>{old}</li>", "")
    return text.replace(old, new)


def main():
    posts = {p["slug"]: p for p in queue30.POSTS + queue_intent.POSTS}
    q = json.load(open("data/post-queue.json"))
    day = START
    for entry in q:
        if entry["published"]:
            continue
        slug = entry["slug"]
        ps = posts[slug]
        if slug in HOLD:
            entry["held"] = True
            entry["date"] = "2099-01-01"          # never due until released
            print("held:", slug)
            continue
        body, faqs, rel = ps["body"], list(ps["faqs"]), list(ps["related"])
        for old, new in FIX.get(slug, []):
            hits = body.count(f"<li>{old}</li>" if new is None else old) + sum(
                (q_ + a_).count(old) for q_, a_ in faqs)
            assert hits, f"{slug}: no match for {old[:60]!r}"
            body = _apply(body, old, new)
            faqs = [(_apply(q_, old, new), _apply(a_, old, new)) for q_, a_ in faqs]
        rel = [(t, RELATED_FIX.get(u, u)) for t, u in rel]
        if slug in RELATED_ADD and RELATED_ADD[slug] not in rel:
            rel.append(RELATED_ADD[slug])
        for t, u in rel:
            p = u.lstrip("/")
            assert os.path.exists(p + ".html") or os.path.exists(p + "/index.html") \
                or os.path.exists(f"data/queued-posts/{p}.html"), f"{slug}: dead related {u}"
        assert "—" not in body, f"{slug}: em dash"
        entry["date"] = day.isoformat()
        entry.pop("held", None)
        html_out = NP.render({"slug": slug, "title": ps["title"], "desc": ps["desc"],
                              "published": entry["date"]}, body, faqs, ps["hero"], rel)
        open(f"data/queued-posts/{slug}.html", "w").write(html_out)
        print(f"{entry['date']}  {slug}  ({len(FIX.get(slug, []))} fixes)")
        day += datetime.timedelta(days=1)
    json.dump(q, open("data/post-queue.json", "w"), indent=1)


if __name__ == "__main__":
    main()
