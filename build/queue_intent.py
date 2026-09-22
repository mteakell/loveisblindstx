"""Seven purchase-intent posts, queued daily after the 30-post run ends.

Where queue30 filled informational gaps, these go after buying-stage
searches: vendor choice, consultation and quote anxiety, and the product
decisions people make in the week before they order. Every claim traces
to copy already published on this site (how-it-works guarantees, product
pages). No prices anywhere, per the standing rule: cost lives in schema
only. APPENDS to data/post-queue.json rather than rewriting it.
"""
import json, os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
import newposts as NP

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
p, sec, sub, li = NP.p, NP.sec, NP.sub, NP.li

POSTS = []
def post(slug, title, desc, hero, body, faqs, related):
    POSTS.append(dict(slug=slug, title=title, desc=desc, hero=hero,
                      body=body, faqs=faqs, related=related))

L = "/images/lib/"

post("custom-blinds-vs-big-box-store-blinds",
 "Custom Blinds vs Big-Box Store Blinds: What You Actually Get",
 "What separates custom blinds from big-box store blinds: fit, measurement, installation, warranty and who stands behind the product after the sale.",
 L + "blinds-blinds-008-jpg.webp",
 p("Every homeowner shopping for blinds hits the same fork: grab boxed blinds off a shelf this afternoon, or order custom and wait a few weeks. The boxed route looks simpler right up until the tape measure comes out. Here is the honest difference, so you can pick the route that fits your project rather than the one that happens to be nearest.")
 + sec("Fit is the whole product",
   p("Boxed blinds come in stock widths, and a store cut-down machine can trim a headrail, but it cannot change the depth of your window, square up an opening that settled, or do anything about a frame that is shallower than the bracket. Custom blinds are built to your opening's real measurements, taken in person. An inside mount that hugs the frame with an even reveal on both sides is what makes a window look finished, and that fit is exactly the part a stock size cannot promise."))
 + sec("Someone measures, and someone answers for it",
   p("With boxed blinds, the measurement is yours, and so is the mistake. A custom treatment is cut to a measurement and a wrong one is not returnable, which is why we measure every opening on site ourselves rather than asking you to. If anything does not match the approved measurements, it is remade and reinstalled at no cost. That guarantee only exists because the person quoting the job is the same person standing in front of your window with the tape."))
 + sec("Installation and what happens after",
   li("Custom orders are installed by the team that measured, and every treatment is operated with you before they leave",
      "Factory defects are covered for life under a limited lifetime warranty",
      "Our Here-4-You guarantee means four years of service visits at no cost if anything acts up",
      "Boxed blinds put all of that on you: the drill, the level, the troubleshooting and the replacement run"))
 + sec("Where boxed blinds genuinely make sense",
   p("A rental you are leaving next year, a garage window, a temporary fix while a room waits for renovation. Boxed blinds exist for a reason, and pretending otherwise would be salesmanship. But for the windows you look at every day in a home you plan to keep, the fit, the warranty and the person who answers the phone afterward are the product. The blind itself is only half of it.")),
 [("Are custom blinds better than store-bought blinds?",
   "For fit, yes: custom blinds are built to your window's exact measurements, taken on site, while boxed blinds rely on stock sizes and your own tape measure. Custom also carries installation and warranty service."),
  ("Who is responsible if custom blinds are measured wrong?",
   "We are. Our team measures every opening in person, and anything that does not match the approved measurements is remade and reinstalled at no cost."),
  ("Do big-box blinds come with installation?",
   "Typically no: you measure, mount and troubleshoot yourself. Custom orders here are installed by the same team that measured, and backed by a four-year service guarantee.")],
 [("What to Know Before Buying Custom Window Treatments Online", "/what-to-know-before-buying-custom-window-treatments-online"),
  ("Cost to Install Blinds: DIY vs Professional", "/cost-to-install-blinds-diy-vs-professional"),
  ("How It Works", "/how-it-works")])

post("what-happens-at-a-free-in-home-consultation",
 "What Happens at a Free In-Home Window Treatment Consultation",
 "What to expect when a window treatment consultant visits: how long it takes, what samples come to your door, how measuring works and what you walk away with.",
 L + "shutters-shutters-091-jpg.webp",
 p("The free in-home consultation is the step most people hesitate over, usually because they picture a hard sell at the kitchen table. Here is what the hour actually looks like, so you know exactly what you are saying yes to when you book.")
 + sec("The samples come to you",
   p("Instead of squinting at a screen or driving to a showroom, the samples arrive at your door: real slats, real fabrics, real louver widths. You hold them against your trim and your paint in your own light, which is the only light that matters. Texas afternoon sun through a west window will tell you more about a fabric in ten seconds than any website ever could."))
 + sec("Every window gets measured properly",
   p("Each opening is measured on site by the person who will stand behind the numbers. Out-of-square openings, shallow frames and tall panels get flagged on the spot, while the fix is still a decision rather than a problem. You do not touch a tape measure, and you are never responsible for a measurement."))
 + sec("You get a written quote that does not move",
   p("Before the visit ends, you know exactly what the project costs. The quote is written, covers installation, and does not move. No estimate ranges, no surprise line items at install. If you want to compare it against another company's number, do: our Apples-to-Apples guarantee is a price-match promise, and a written quote is what makes an honest comparison possible."))
 + sec("What happens if you say yes, and if you don't",
   li("Approved orders typically arrive within two to four weeks",
      "The team that measured comes back to install and operates every treatment with you",
      "Anything that does not match the approved measurements is remade at no cost",
      "And if you are not ready, the quote is yours to keep, no follow-up pressure required"))
 + sec("How to get the most from the visit",
   p("Think about how each room is used before the visit: who sleeps late, which windows glare at the TV, where privacy matters at night. Our ten-minute design checklist walks through exactly these questions and gives you a plan to hand the consultant, which turns the visit from a product tour into a working session.")),
 [("How long does an in-home window treatment consultation take?",
   "Plan for about an hour for a typical home: samples in your rooms, every window measured, and a written quote before the visit ends."),
  ("Does a free consultation obligate me to buy?",
   "No. The visit ends with a written quote that is yours to keep, and the decision is yours on your own schedule."),
  ("Should I measure my windows before the consultation?",
   "No. Every opening is measured on site by our own team, and we stand behind those numbers: mismeasured treatments are remade at no cost.")],
 [("Plan Your Windows in Ten Minutes", "/design-checklist"),
  ("How Long From Order to Install? The Real Window Treatment Timeline", "/how-long-from-order-to-install"),
  ("Book a Free Consultation", "/schedule-now")])

post("questions-to-ask-before-hiring-a-window-treatment-company",
 "10 Questions to Ask Before Hiring a Window Treatment Company",
 "The ten questions that separate a window treatment company you can trust from one you will regret: measuring, quotes, warranties, service and who shows up.",
 L + "shutters-shutters-113-jpg.webp",
 p("Custom window treatments are one of those purchases where the company matters as much as the product. The same shutter can be a twenty-year upgrade or a headache, depending on who measured it, who installed it and who picks up the phone in year three. These are the ten questions worth asking anyone who wants the job, along with the answers you should hear.")
 + sec("The measuring and quoting questions",
   li("Who takes the measurements, me or you? The right answer is the company, in person, at every opening.",
      "What happens if a measurement is wrong? You want remade and reinstalled at no cost, in writing.",
      "Is the quote written, and does it include installation? A number that can move at install time is not a quote.",
      "Will you match a competitor's written quote on the same product? Companies confident in their pricing say yes; ours is called the Apples-to-Apples guarantee."))
 + sec("The people questions",
   li("Who actually shows up to install? The team that measured should be the team that installs, not a subcontractor seeing the job cold.",
      "Is the company locally owned? An owner whose name is on the work answers the phone differently than a call center.",
      "Can I read your reviews by city? Any established company should be able to point you at hundreds of Google reviews from real local addresses."))
 + sec("The after-the-sale questions",
   li("What does the warranty cover, and for how long? Factory defects should be covered for life.",
      "What if something breaks or I just stop liking one? Ask about service guarantees; ours covers service visits for four years at no cost, and our GuaranTEN replaces one treatment free for every ten purchased, no questions asked.",
      "Does the warranty transfer if I sell the house? A transferable warranty is a real line item when a buyer's inspector starts asking about the shutters."))
 + sec("Why the answers matter more than the price",
   p("Any two quotes can be made to look alike on paper. The difference between them lives in these ten answers: who is accountable for the measurement, whether the number moves, and who you will be talking to in year four. Ask all ten. A good company enjoys answering them.")),
 [("What should I ask a blinds company before hiring them?",
   "Ask who measures, who installs, whether the quote is written and includes installation, what the warranty covers, and what service looks like after the sale. Strong companies have quick, specific answers."),
  ("How do I know if a window treatment quote is trustworthy?",
   "It is written, it covers installation, and it does not move. If a company hesitates to put the full number in writing, keep shopping."),
  ("Why does it matter who installs my window treatments?",
   "Custom treatments live or die on fit. The team that measured your windows knows every flagged opening; a stranger seeing the job cold does not.")],
 [("Custom Blinds vs Big-Box Store Blinds: What You Actually Get", "/custom-blinds-vs-big-box-store-blinds"),
  ("Read Our Google Reviews", "/reviews"),
  ("How It Works", "/how-it-works")])

post("faux-wood-vs-real-wood-blinds",
 "Faux Wood vs Real Wood Blinds: How to Choose",
 "Faux wood and real wood blinds side by side: moisture, weight, span, finish and which rooms each one belongs in for a Texas home.",
 L + "blinds-blinds-011-jpg.webp",
 p("Wood blinds come in two families that look nearly identical on the window and behave very differently over the years. Choosing between faux wood and real wood is mostly a matter of matching the material to the room, and a whole-home order usually ends up with some of each.")
 + sec("Where faux wood wins",
   p("Faux wood blinds are composite, and composite does not care about humidity. Kitchens over a steaming sink, bathrooms, laundry rooms and any window that sweats in a Texas August are faux wood territory. The slats will not warp, crack or peel in moisture that would punish real wood, and the finish wipes clean. For white blinds, most homeowners cannot tell faux from painted wood at any distance."))
 + sec("Where real wood earns its keep",
   p("Real wood is significantly lighter than composite, which matters more than people expect. On wide windows, a lighter blind lifts easier and puts less strain on the mechanism, so large living room and bedroom windows favor real wood. It is also the only way to get a true stain finish: a stained real wood blind can match your floors, cabinets or trim in a way paint cannot fake, and the grain is real because it is real."))
 + sec("The quick decision table",
   li("Bathrooms, kitchens, laundry: faux wood, every time",
      "Wide windows where weight strains the lift: real wood",
      "Stained finishes to match woodwork: real wood, the only option",
      "White or painted looks on standard windows: either, so let budget and room moisture decide",
      "Kids' rooms and rentals: faux wood shrugs off abuse"))
 + sec("What a consultation adds to the choice",
   p("Slat width, valance style and mount depth change how either material reads on the window, and those calls are easier with samples in hand at your actual window. Holding a stained slat against your floor beats guessing from a photo, and measuring the frame depth on site settles which mounts are even possible. That is the point where this decision becomes concrete rather than theoretical.")),
 [("Are faux wood blinds better than real wood?",
   "Neither is better everywhere. Faux wood handles moisture and abuse; real wood is lighter on wide windows and offers true stain finishes. Most whole-home orders mix both by room."),
  ("Do faux wood blinds warp in bathrooms?",
   "No, that is their headline advantage. The composite slats stand up to humidity that would warp, crack or peel real wood."),
  ("Can real wood blinds be stained to match my floors?",
   "Yes, and it is the reason to choose them. Stain shows real grain and can be matched to floors, cabinets and trim; faux wood is limited to painted finishes.")],
 [("Real Wood Blinds", "/products/real-wood-blinds"),
  ("Faux Wood Blinds", "/products/faux-wood-blinds"),
  ("Window Coverings You Shouldn't Buy If You Have Kids Around", "/window-covering-you-shouldn-t-buy-if-you-have-kids-around")])

post("vertical-blind-alternatives-for-sliding-glass-doors",
 "Vertical Blind Alternatives for Sliding Glass Doors",
 "Replacing dated vertical blinds on a sliding door: panel track shades, custom drapery and wide roller shades compared, and how to pick between them.",
 L + "panel-track-shades-panel-track-shades-002-jpg.webp",
 p("Vertical blinds had one great idea: slide sideways, like the door. The execution is what dates a room, with clacking vanes that yellow, crack and derail one by one. If you are shopping to replace them, you are really shopping for something that still slides but looks like it belongs in this decade. Three treatments do it well.")
 + sec("Panel track shades: the direct heir",
   p("Panel track takes the sliding motion of vertical blinds and replaces dozens of narrow vanes with a few wide fabric panels that glide on a headrail and stack cleanly to one side. Closed, they read as a calm fabric wall; open, they disappear behind each other. Fabric choices run from light-filtering to blackout, so the same system works on a family room slider or a bedroom patio door. Of everything we install over sliders, this is the treatment people mean when they say they want vertical blinds, but nice."))
 + sec("Custom drapery: the soft answer",
   p("Drapery panels on a proper rod bring height, softness and color that hard treatments cannot, and they clear the door completely when stacked back. Motorized drapery tracks put the whole run on a remote or schedule, which turns a heavy west-facing slider into something you never touch. In rooms where the slider is the biggest visual surface, drapery is often what makes the room feel finished."))
 + sec("Wide roller and solar shades: the minimal answer",
   p("A roller or solar shade mounted above the door keeps the glass and the view while cutting glare and heat, and it vanishes into a slim roll when raised. The tradeoff is vertical operation: the shade must be up to use the door. That suits doors used a few times a day, less so the door the dog goes in and out of forty times an afternoon."))
 + sec("How to choose between the three",
   li("Use the door constantly: panel track, because it slides with you",
      "Want softness, height or a motorized glide: custom drapery",
      "Want the view and the light with minimal hardware: roller or solar shade",
      "Blackout for a bedroom slider: panel track or lined drapery, both do it properly"))
 + sec("Why sliders punish guesswork",
   p("Door openings are wide, heavily used and unforgiving of a treatment that hangs a half-inch too low. Stack direction has to match how the door slides, and clearance over handles and locks has to be measured, not assumed. This is precisely the opening we would rather measure ourselves, which is what the free in-home consultation is for.")),
 [("What can I replace vertical blinds with?",
   "Panel track shades are the most direct upgrade: wide fabric panels that slide like the door. Custom drapery and wide roller or solar shades are the other two strong answers, depending on how the door is used."),
  ("Are panel track shades good for sliding doors?",
   "They are the treatment built for them. Panels glide on a headrail, stack to whichever side the door opens from, and come in light-filtering through blackout fabrics."),
  ("Can sliding door treatments be motorized?",
   "Yes. Motorized drapery tracks and motorized shades both put a heavy west-facing slider on a remote or a schedule.")],
 [("Panel Track Shades", "/products/panel-track-shades"),
  ("How to Choose Window Treatments for Homes with Large Glass Doors", "/how-to-choose-window-treatments-for-homes-with-large-glass-doors"),
  ("Honeycomb vs Panel Track Shades: Which is Right for Your Home", "/honeycomb-vs-panel-track-shades-which-is-best-for-your-home")])

post("whole-house-window-treatments-where-to-start",
 "Buying Window Treatments for the Whole House: Where to Start",
 "How to plan window treatments for an entire home: which rooms to decide first, when to mix products, what should match from the street and how phasing works.",
 L + "roller-shades-roller-shades-230-jpg.webp",
 p("A whole house of bare windows, whether from a new build or a long-postponed upgrade, is a different project than covering one room. Decide window by window and you get a patchwork; decide all at once with no plan and the order overwhelms. The homes that end up looking pulled together follow roughly the same sequence.")
 + sec("Start from the street, not the front door",
   p("The windows on the front of the house read as one composition from the curb, whatever is behind them. Pick one treatment, or at least one color, for every street-facing window before thinking about the rooms inside. White plantation shutters are the classic answer because they look intentional from outside and suit almost any room behind them. Whatever you choose, curb-side consistency is the single decision that makes a whole house look designed rather than accumulated."))
 + sec("Then solve the hard rooms",
   li("Bedrooms: darkness first, so room-darkening or blackout options lead",
      "Bathrooms and kitchens: moisture rules out some materials before style enters into it",
      "Living areas with big glass: heat and glare control, where solar and cellular fabrics earn their keep",
      "Sliders and patio doors: treatments that move the way the door moves"))
 + sec("Mixing products is normal, matching tones is mandatory",
   p("Almost no whole-home order is one product on every window. Shutters on the front, cellular shades in bedrooms, faux wood in the baths and a panel track on the slider is a completely coherent house, provided whites match whites and stains match stains from room to room. Bring the same two or three finishes through the whole house and the mix reads as a plan."))
 + sec("Phasing, and why one measure visit beats four",
   p("Plenty of families do a whole house in stages: front of house and bedrooms first, everything else as it fits. Phasing the budget works fine. What is worth doing all at once is the measuring and the planning, because one consultation that maps every window gives you a written whole-house quote you can execute in any order, with finishes that still match when phase two happens next year. Our GuaranTEN also rewards volume: for every ten treatments purchased, one gets replaced free, no questions asked."))
 + sec("The ten-minute head start",
   p("Before anyone visits, walk the house once with our design checklist: it asks the sleep, glare, privacy and style questions room by room and hands you back a plan. Ten minutes with it turns the consultation into a confirmation rather than a survey.")),
 [("What order should I buy window treatments for a whole house?",
   "Street-facing windows first, for curb-side consistency, then the hard rooms: bedrooms for darkness, baths and kitchens for moisture, big glass for heat. Fill in the rest last."),
  ("Should every room have the same window treatment?",
   "No, mixing products by room is normal. Keep whites and stains consistent through the house and a mixed order still reads as one design."),
  ("Can I buy window treatments for my house in phases?",
   "Yes. One consultation can measure and quote the whole house in writing, and you can execute the plan in stages with finishes that still match.")],
 [("Plan Your Windows in Ten Minutes", "/design-checklist"),
  ("How to Choose Window Treatments That Boost Your Home's Curb Appeal", "/how-to-choose-window-treatments-that-boost-your-homes-curb-appeal"),
  ("Window Treatments for New Construction: What to Order Before Closing", "/window-treatments-new-construction-timing")])

post("what-a-window-treatment-quote-should-include",
 "What a Window Treatment Quote Should Include",
 "How to read and compare window treatment quotes: the line items that belong in writing, the gaps that hide surprises, and how a price-match works.",
 L + "shutters-shutters-060-jpg.webp",
 p("Somewhere between the consultation and the contract, every window treatment project comes down to a piece of paper. Whether you are comparing two companies or sanity-checking one, the quote is where good projects are protected and bad ones are signed. Here is what belongs on it, and what its absence tells you.")
 + sec("The line items that belong in writing",
   li("Every window, identified by room, with the product, material, color and mount for each",
      "Installation, included in the number rather than appearing later",
      "The warranty terms: what is covered, for how long, and whether it transfers",
      "The total, as a figure that does not move between signing and install"))
 + sec("The gaps that hide surprises",
   p("An estimate range instead of a number, installation quoted separately or left for later, and measurements taken by you rather than the company are the three classic gaps. Each one moves risk from the seller to you. A range becomes its own top end, a separate install becomes an upsell, and a self-measured window becomes your mistake to pay for. A company that measures every opening itself and writes one complete number has removed all three."))
 + sec("How to compare two quotes honestly",
   p("Line the quotes up window by window, and check that the products actually match: same material, same mount, same lift, same warranty. A lower number on a different product is not a lower price, it is a different job. When the products genuinely match and the numbers differ, bring it to us: our Apples-to-Apples guarantee is a price-match promise, and it exists precisely because we would rather match an honest comparison than lose one to a padded quote that falls apart at install."))
 + sec("What surrounds the number matters as much",
   p("A quote is also a preview of the company. Ours arrive in writing before the consultation ends, cover installation, and hold until the job is done, because the person who measured is the person accountable for the number. Behind the figure sit a limited lifetime warranty on factory defects, four years of no-cost service visits, and a warranty that transfers if you sell the house. Ask any bidder what sits behind their number. The pause tells you plenty.")),
 [("What should be included in a blinds quote?",
   "Every window by room with product, material, color and mount, installation in the number, warranty terms, and a written total that does not change at install."),
  ("How do I compare window treatment quotes from two companies?",
   "Match them window by window on product, material, mount and warranty first. Numbers only compare when the jobs match; a lower price on a lesser product is a different job."),
  ("What is an apples-to-apples price match?",
   "If a competitor quotes the same product and job for less in writing, we match it. It keeps the comparison about the work rather than the paperwork.")],
 [("10 Questions to Ask Before Hiring a Window Treatment Company", "/questions-to-ask-before-hiring-a-window-treatment-company"),
  ("What Happens at a Free In-Home Window Treatment Consultation", "/what-happens-at-a-free-in-home-consultation"),
  ("Book a Free Consultation", "/schedule-now")])

post("window-treatments-for-west-facing-windows-texas",
 "Window Treatments for West-Facing Windows in Texas",
 "West glass takes the worst of Texas heat. The shades that actually stop afternoon sun, what each does to your view, and when exterior shades win.",
 L + "roller-shades-roller-shades-237-jpg.webp",
 p("West-facing windows get the hardest job in a Texas house: the sun arrives low, hot and glaring exactly when the day is hottest, and it keeps coming until it sets. The best treatments for west glass are solar shades, honeycomb shades and exterior shades, chosen by whether you want to keep the view, kill the heat, or both. Here is how to pick.")
 + sec("Why west windows punish ordinary treatments",
   p("Morning sun through east glass is high and brief. Afternoon sun through west glass is low-angle, which means it comes straight in rather than glancing off, and it lands during peak heat, stacking on top of the hottest part of the day. Fabrics fade, floors bleach in stripes, glare wipes out the TV, and the room the family uses most becomes the room nobody sits in from three to seven."))
 + sec("Solar shades: keep the view, cut the heat",
   p("Solar roller shades are woven screens that reject heat and glare while staying see-through from inside. Openness is the number to know: a tighter weave blocks more sun and shows less view, an open weave keeps the view and lets more light through. On a west wall with a backyard worth looking at, solar shades are usually the first thing we reach for, because the alternative most people fear, a dark room with the shades down all afternoon, never happens."))
 + sec("Honeycomb shades: the insulation play",
   p("When the problem is heat gain more than glare, honeycomb cellular shades trap air in their cells and insulate the glass itself. They give up the view when lowered, which makes them the bedroom and street-facing answer, and the strongest choice where cooling costs matter more than sightlines."))
 + sec("Exterior shades: stop the heat before the glass",
   p("Everything inside the window intercepts sun after it has already passed through the glass. Exterior shades stop it outside, which is why they outperform any interior treatment on brutal west exposures, patios and big slider walls. For a west-facing outdoor living area, they are the difference between a patio you abandon in June and one you use all summer."))
 + sec("The motorization move that does the real work",
   li("A schedule that drops the west bank at 3pm and raises it at sunset, every day, without anyone thinking about it",
      "Remote control for the tall or wide west windows nobody wants to crank by hand",
      "Pairing: solar shades for the day, and drapery or room-darkening shades layered for evenings"))
 + sec("What we look at in your actual room",
   p("West is not one condition. A covered porch changes it, a neighbor's tree changes it, and a lake view changes what you are willing to cover. The free in-home consultation exists for exactly this: we look at the glass at your house, bring the fabric openness samples, and quote the wall in writing on the spot.")),
 [("What is the best window treatment for west-facing windows?",
   "Solar roller shades for view and glare control, honeycomb shades for maximum insulation, and exterior shades where the heat is severe. Many west walls pair solar shades with a schedule that drops them each afternoon."),
  ("Do solar shades block the view?",
   "No, that is their advantage. The woven screen cuts heat and glare while staying see-through from inside; the openness factor you choose sets the balance between sun-blocking and view."),
  ("Are exterior shades worth it on west-facing glass?",
   "On severe west exposures, yes. Stopping sun before it reaches the glass beats any interior treatment, which is why exterior shades rule west patios and big slider walls.")],
 [("Solar Shades vs Blackout Shades: Which Do You Need?", "/solar-shades-vs-blackout-shades"),
  ("Cellular Shades vs Roller Shades for Texas Heat", "/cellular-shades-vs-roller-shades"),
  ("Roller Shades", "/products/roller-shades")])


# ------------------------------------------------------------- render queue
def main():
    start = datetime.date(2026, 10, 6)   # day after queue30's last post
    q = json.load(open("data/post-queue.json"))
    have = {x["slug"] for x in q}
    added = 0
    for i, ps in enumerate(POSTS):
        pub = (start + datetime.timedelta(days=i)).isoformat()
        post = {"slug": ps["slug"], "title": ps["title"], "desc": ps["desc"],
                "published": pub}
        html_out = NP.render(post, ps["body"], ps["faqs"], ps["hero"], ps["related"])
        open(f"data/queued-posts/{ps['slug']}.html", "w").write(html_out)
        if ps["slug"] not in have:
            q.append({"slug": ps["slug"], "title": ps["title"], "desc": ps["desc"],
                      "date": pub, "img": ps["hero"], "published": False})
            added += 1
    json.dump(q, open("data/post-queue.json", "w"), indent=1)
    print(f"{len(POSTS)} intent posts rendered, {added} appended to queue")
    print(f"schedule: {start.isoformat()} through "
          f"{(start + datetime.timedelta(days=len(POSTS)-1)).isoformat()}")

if __name__ == "__main__":
    main()
