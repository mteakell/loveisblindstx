"""Per-post unique content. Each entry supplies the sections that make the post
worth reading on its own, on top of any shared skeleton."""

def build(N, C):
    p, sec, sub, li = N.p, N.sec, N.sub, N.li
    X = {}

    # ---------------------------------------------------------------- cost
    X["how-much-do-plantation-shutters-cost-in-texas"] = C.cost_body(N, "plantation shutters", [
      sec("Why shutters cost more than blinds, and why people still buy them",
        p("Shutters are furniture. They are built to the opening, hung on a frame, and they stay "
          "with the house. That is why the number is higher than a blind and why buyers read them "
          "as a permanent upgrade rather than a covering that will be replaced."),
        p("In practice most people who ask about shutter pricing are comparing a whole-house blind "
          "job against shutters in the front rooms and blinds elsewhere. That split is usually the "
          "better use of the budget.")),
      sec("What changes the price on a shutter specifically",
        sub("Louver size", p("Wider louvers give a cleaner view out and suit larger windows. "
          "Narrower louvers suit smaller or period openings. The size you choose changes the "
          "material used per panel.")),
        sub("Frame style", p("A shutter can be hung in a frame that fits inside the opening or on "
          "a frame that sits over it. Deep sills, tile returns and out of square openings all push "
          "toward one or the other.")),
        sub("Panel configuration", p("How many panels, which way they swing, whether there is a "
          "divider rail so the top and bottom tilt separately. A wide window split into four "
          "panels costs more than the same width in two."))),
    ])
    X["how-much-do-blinds-cost"] = C.cost_body(N, "blinds", [
      sec("Real wood, faux wood, composite and vinyl",
        p("The material decision drives more of the number than most people expect, and the right "
          "answer changes room to room."),
        li("<strong>Real wood</strong> is the lightest and takes stain beautifully, but it moves "
           "in humidity, so it belongs in living areas rather than bathrooms",
           "<strong>Faux wood</strong> handles moisture and hard sun without warping, which is why "
           "it ends up in most Texas bathrooms and kitchens",
           "<strong>Composite</strong> splits the difference on cost and durability",
           "<strong>Vinyl and aluminium</strong> are the cheapest and behave like it on a west wall")),
      sec("Cordless is not an upgrade any more",
        p("Cordless operation is standard on most new blinds for child and pet safety, and it is "
          "worth confirming what any quote includes. A price that looks unusually low sometimes "
          "still assumes a corded lift.")),
    ])
    X["how-much-do-window-shutters-cost"] = C.cost_body(N, "window shutters", [
      sec("Interior shutters versus exterior shutters",
        p("Most people searching shutter pricing mean interior plantation shutters. Exterior "
          "shutters are a different product with different pricing and, in most Texas "
          "neighbourhoods, a decorative role rather than a functional one."),
        p("If what you actually want is heat control on the outside of the glass, exterior patio "
          "shades or solar screens do that job far better than a decorative shutter.")),
      sec("Shutters as a resale argument",
        p("Shutters stay with the house, so unlike most window coverings they read to a buyer as "
          "part of the property. That is the usual reason people stretch for them in the rooms "
          "that show, then use blinds or shades elsewhere.")),
    ])
    X["blinds-installation-cost-what-to-expect"] = C.cost_body(N, "blinds installation", [
      sec("What installation actually involves",
        p("Installation is not just hanging a bracket. It is confirming the treatment matches the "
          "approved measurements, mounting square in an opening that often is not, setting the "
          "tilt and lift, and cleaning up."),
        li("Brackets set into the frame or the wall depending on mount type",
           "Levelling in an opening that has usually settled out of square",
           "Motor pairing and programming where the treatment is motorized",
           "Testing every opening before we leave",
           "Old treatments taken down and removed if you want them gone")),
      sec("Why we do not price installation separately",
        p("Our quotes include installation because separating it invites the sort of surprise "
          "that makes people distrust the trade. You approve one number that covers measurement, "
          "the treatment, and fitting it.")),
    ])
    X["motorized-blinds-cost-is-motorization-worth-it"] = C.cost_body(N, "motorized blinds", [
      sec("Where motorization earns its cost",
        p("Motorization is worth it per opening, not per house. The openings where it pays for "
          "itself are consistent."),
        li("Windows above a stairwell, a tub or built-in furniture you cannot reach",
           "Very wide or very tall treatments that are heavy to operate by hand",
           "Rooms where you want the shades to move on a schedule for heat or privacy",
           "Patio shades that need to come up quickly when the wind turns")),
      sec("Battery, hardwired or solar",
        sub("Battery", p("Simplest to retrofit, no electrician. You recharge or replace packs "
          "periodically, and how often depends on how much the shade moves.")),
        sub("Hardwired", p("Best for new build or a remodel where the walls are open. Nothing to "
          "recharge, but it needs planning before the drywall goes up.")),
        sub("Solar charged", p("A small panel keeps the battery topped up. Works well on windows "
          "that get real sun, which in Texas is most of them."))),
    ])
    X["cost-to-install-blinds-diy-vs-professional"] = C.cost_body(N, "blinds installation", [
      sec("What DIY actually saves, and what it risks",
        p("The saving on a straightforward rectangular window in a newer house is real. The risk "
          "is that custom treatments are cut to your measurements, so a measuring error is not "
          "returnable, it is a remake you pay for."),
        li("Measure twice per opening, width at top, middle and bottom",
           "Check frame depth before committing to an inside mount",
           "Confirm the opening is square before ordering, most are not",
           "Factor in that you own any mistake on a custom order")),
      sec("When to stop and call someone",
        p("Arches, angles, bays, sliding doors, anything above a stairwell, and any motorized "
          "treatment. Those are the jobs where a small error is expensive and where two people and "
          "the right ladder matter more than the tool.")),
    ])
    X["affordable-plantation-shutters-without-cutting-corners"] = C.cost_body(N, "shutters", [
      sec("Where it is safe to save",
        li("Composite instead of hardwood in rooms that do not show",
           "Standard louver sizes rather than specialty",
           "Shutters in the front rooms, quality blinds or shades elsewhere",
           "Simpler panel configurations on wide windows")),
      sec("Where saving costs you later",
        p("The false economy is buying a shutter too thin or too light for a west facing opening, "
          "or skipping the divider rail on a tall window and then never being able to tilt the top "
          "independently. Both are cheap on day one and annoying for a decade.")),
    ])
    X["patio-shade-cost-what-drives-the-price"] = C.cost_body(N, "exterior patio shades", [
      sec("Span is the biggest single factor",
        p("Patio openings are wide. A twenty foot span needs heavier hardware, a bigger tube and "
          "usually a motor, because nobody cranks a shade that size by hand twice a day. That is "
          "why patio pricing behaves differently from interior pricing.")),
      sec("Fabric openness changes both price and performance",
        p("A tighter weave blocks more sun and costs more per square foot than an open one. The "
          "right choice depends on which way the patio faces, and getting it wrong is the most "
          "common regret we hear about on outdoor shades.")),
      sec("Wind is a cost factor people forget",
        p("Exterior shades should come up in high wind. Motorization is not a luxury on a large "
          "span, it is what makes retracting them quick enough that you actually do it.")),
    ])
    return X
