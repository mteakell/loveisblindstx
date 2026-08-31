"""Content for the cost cluster. No dollar figures: every one of these routes
to a real measured quote instead of inventing a range."""

DRIVERS = [
 ("Size of the opening",
  "Price tracks square footage more than anything else. A bank of tall windows in a two storey "
  "entry costs more than the same treatment across three bedroom windows, because there is more "
  "material and the install takes longer and often takes two people."),
 ("Material",
  "Basswood and hardwood sit at the top, composite and faux wood in the middle, vinyl and "
  "aluminium at the bottom. The gap between them is real, but so is the difference in how they "
  "behave in a bathroom or on a west wall."),
 ("Mount type",
  "Inside mount looks cleaner but needs enough depth in the frame and unforgiving measurements. "
  "Outside mount forgives an out of square opening and covers more glass, which matters in older "
  "houses where nothing is plumb."),
 ("Motorization",
  "Motors, hubs and the choice between battery, hardwired and solar charging add cost per opening. "
  "On wide or high windows it is often the difference between a treatment you use daily and one "
  "you stop bothering with."),
 ("Specialty shapes",
  "Arches, angles, bays and anything that is not a rectangle takes custom fabrication and more "
  "time on site. Sliding doors and French doors have their own hardware requirements."),
 ("Fabric and finish",
  "Within any product line there is a spread between the standard book and the designer fabrics. "
  "Openness factor on a solar shade, blackout lining on a Roman, a stain matched to your trim: all "
  "of it moves the number."),
]

def cost_body(N, product="window treatments", extra_sections=()):
    """Shared skeleton for the cost posts. `extra_sections` are per-post."""
    b = []
    b.append(N.p(f"<strong>Short answer:</strong> the price of {product} comes down to the size of "
                 f"the opening, the material, the mount, and whether you motorize. Anyone quoting "
                 f"you a firm number before measuring is guessing."))
    b.append(N.sec("Why a single price never fits",
        N.p("Custom treatments are made to your openings, so there is no shelf price. Two houses "
            "on the same street can differ by a wide margin because one has standard bedroom "
            "windows and the other has an arched entry and a sixteen foot slider.",
            "That is why we measure first and quote from those measurements. " + N.PRICE_NOTE)))
    b.append(N.sec("What actually moves the number",
        "".join(N.sub(h, N.p(t)) for h, t in DRIVERS)))
    for s in extra_sections:
        b.append(s)
    b.append(N.sec("Where people over and under spend",
        N.p("The most common mistake is buying the cheapest option for a window that takes hard "
            "afternoon sun. Vinyl on a west facing wall in a Texas summer will warp, and you pay "
            "twice. The second most common is motorizing everything when only two or three "
            "openings are genuinely awkward to reach."),
        N.li("Spend where the sun is hardest and the window is hardest to reach",
             "Save on small openings in rooms you barely use",
             "Match material to moisture: a bathroom is not a bedroom",
             "Buy the mount that suits the frame, not the one that sounds cheaper")))
    b.append(N.sec("What a quote from us includes",
        N.p("Every quote covers measurement, the treatment built to those measurements, and "
            "professional installation. There is no separate trip charge and no charge for the "
            "consultation itself."),
        N.li("Free in-home consultation with samples you can hold against your own light",
             "Every opening measured on site, not estimated from your photos",
             "A written quote based on those measurements",
             "Installation by the same team that measured",
             "Remade at no cost if a treatment does not match the approved measurements")))
    b.append(N.sec("Getting a real number for your house",
        N.p("The fastest way to a number is to have someone measure. The consultation is free, "
            "there is no obligation, and you will know what your specific openings cost rather "
            "than what an average house costs.")))
    return "".join(b)
