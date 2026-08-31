"""Room, patio, smart, safety and care posts."""

def build(N):
    p, sec, sub, li = N.p, N.sec, N.sub, N.li
    CONSULT = sec("Let us measure it",
        p("The consultation is free, we bring samples you can hold against your own light, and we "
          "measure every opening on site. You get a written quote from those measurements."))
    TEXAS = sec("The Texas factor",
        p("West and south facing glass takes the worst of the afternoon here, and it is the single "
          "thing that should drive the specification. A treatment that is perfect on a north window "
          "can fade, warp or simply fail to do its job on a west wall."),
        li("Check which way each window faces before choosing material",
           "Moisture rules bathrooms and kitchens: faux wood or composite, not real wood",
           "Anything on the hot side should be specified for sun, not chosen on looks",
           "Shading the outside of the glass beats shading the inside, every time"))
    X = {}

    def room(intro, options, considerations, mistakes, extra=()):
        """Room and application posts. Each gets options, decisions, mistakes,
        a materials section, a light-control section and the Texas context."""
        out = [p(f"<strong>Short answer:</strong> {intro}"),
               p("The rest of this covers the options that actually work in that situation, what "
                 "to decide before you order, the mistakes we get called out to fix, and how the "
                 "Texas sun should change your choice.")]
        out.append(sec("What works, and why", "".join(sub(h, p(t)) for h, t in options)))
        out.append(sec("What to decide before you order", li(*considerations)))
        out.append(sec("Material, and why it matters more than style",
            p("The format of a treatment is a look. The material is what decides whether it still "
              "works in three years. Getting this wrong is the most expensive mistake available, "
              "because a custom treatment is not returnable and a warped one gets replaced."),
            sub("Real wood",
                p("Lightest, takes stain beautifully, and belongs in dry living areas. It moves "
                  "with humidity, so it is the wrong answer near a shower or a sink.")),
            sub("Faux wood and composite",
                p("Handle moisture and hard sun without warping. Heavier, which matters on a wide "
                  "span, but they are why most Texas kitchens and bathrooms end up with them.")),
            sub("Fabric shades",
                p("Softer and warmer in a room, and the only option where openness factor lets you "
                  "tune view against shade. Choose a weave rated for sun on a hot wall.")),
            sub("Vinyl and aluminium",
                p("Cheapest, and they behave like it on a west facing window. Fine on a shaded "
                  "north opening in a room nobody uses."))))
        out.append(sec("Light control, privacy and the night time problem",
            p("Daytime privacy and night time privacy are different problems, and a lot of "
              "disappointment comes from assuming one treatment solves both. A weave that gives "
              "perfect privacy at noon can go transparent once the lights are on inside."),
            li("Decide per window whether you need light filtering, room darkening or blackout",
               "Check whether the window needs to work after dark, not just during the day",
               "Remember that any inside mount leaks light at the edges, by design",
               "Layering a shade under a drape solves most cases that one product cannot")))
        for s2 in extra:
            out.append(s2)
        out.append(sec("Mistakes we get called out to fix", li(*mistakes)))
        out.append(TEXAS)
        out.append(sec("How we would approach it",
            p("At the consultation we look at which way the window faces, what the room is used "
              "for, how the opening is built and whether it is square and deep enough for the "
              "mount you want. Then we measure every opening ourselves and quote from those "
              "measurements."),
            li("Samples brought to your home so you see them in your own light",
               "Every opening measured on site rather than estimated",
               "A written quote based on those measurements",
               "Installation by the same team that measured",
               "Remade at no cost if it does not match the approved measurements")))
        out.append(CONSULT)
        return "".join(out)

    X["window-treatments-for-french-doors"] = room(
      "French doors need a treatment that clears the handle, does not swing with the door, and "
      "still lets the doors work. That usually means a shallow, door mounted treatment rather than "
      "anything that hangs free.",
      [("Shutters on the door",
        "Custom shutters can be built with a cut-out for the handle and mounted directly to the "
        "door, so they move with it. The most finished looking answer and the most expensive."),
       ("Cellular or pleated shades, door mounted",
        "Slim, mounted top and bottom so they cannot swing. They work with the door rather than "
        "against it, and they add insulation on a lot of glass."),
       ("Roller shades with a bottom bracket",
        "A flat panel with a hold-down bracket at the sill stops the shade swinging every time the "
        "door opens."),
       ("Drapery on a wide rod",
        "Hung wide enough to clear the doors entirely when open. Softens the room, but you lose "
        "wall space and it does nothing when the doors are in use.")],
      ["Whether the doors swing in or out, which decides how much clearance you have",
       "Where the handle sits, and how far it projects",
       "Whether you need both doors to open fully, or only one in daily use",
       "How much light you actually want to keep, since French doors are usually the light source",
       "Whether the doors are used daily or are effectively a window"],
      ["A treatment mounted above the door that swings and bangs every time it opens",
       "A blind that fouls the handle, so the door will not close",
       "An inside mount on a door with no depth for the headrail",
       "Blocking the light source completely in a room that has no other window"])

    X["best-window-treatments-for-kitchens"] = room(
      "kitchens need something that tolerates heat, steam and grease, wipes clean, and clears "
      "window cranks and sills you actually use. Faux wood, composite and easy-clean roller shades "
      "do the job. Real wood and heavy fabric do not.",
      [("Faux wood blinds",
        "The default for good reason. They handle steam without warping and wipe down with a cloth, "
        "which matters over a sink or near a hob."),
       ("Composite shutters",
        "The most finished look that still survives a kitchen. More expensive, but they do not mind "
        "moisture and they clean easily."),
       ("Roller and solar shades",
        "Flat, minimal, and they roll out of the way over a sink. Choose a fabric rated for easy "
        "cleaning rather than a textured weave that traps grease."),
       ("What to avoid",
        "Real wood warps over a sink. Woven wood and heavy fabric absorb cooking smells and are "
        "difficult to clean. Neither belongs over a hob.")],
      ["Whether there is a window crank, which usually forces an outside mount",
       "Whether you use the sill as a shelf",
       "How close the window is to the hob, which decides how much grease it will take",
       "Whether the window is over a sink, and how far you have to reach"],
      ["Real wood over a sink, which warps within a couple of seasons",
       "An inside mount that fouls a window crank",
       "Textured fabric near a hob that cannot be cleaned",
       "A treatment you cannot reach across a deep counter"])

    X["best-blinds-for-large-windows"] = room(
      "large windows need the weight considered before the look. Wide treatments are heavy, sag if "
      "the headrail is not specified for the span, and are awkward to operate by hand, which is why "
      "motorization and splitting into panels come up so often.",
      [("Split the span into panels",
        "Two or three treatments across one wide opening are easier to operate, cheaper to replace "
        "if one is damaged, and less likely to sag than a single very wide unit."),
       ("Motorize it",
        "Above a certain width and height, a hand-operated treatment stops getting used. "
        "Motorization is what keeps a large window's shades actually working day to day."),
       ("Panel track for very wide openings",
        "Sliding panels handle wide spans and patio doors without the weight problem a single "
        "roller has."),
       ("Cellular for the heat load",
        "A large window is a large heat load. If the span faces west, insulation at the glass "
        "matters more than the style of the treatment.")],
      ["The exact span, since headrail specification changes with width",
       "Whether you can physically reach the top of the window",
       "How the treatment will stack when open, and how much glass that covers",
       "Whether the opening faces the afternoon sun"],
      ["A single treatment across a span it was never rated for, which sags",
       "Hand operation on a window nobody can comfortably reach",
       "Ignoring stack height, so a third of the view is covered when the shade is up",
       "Choosing on looks alone for a west facing wall of glass"])

    X["blackout-shades-for-bedrooms"] = room(
      "no inside mounted shade is truly blackout on its own, because light always leaks at the "
      "edges. Real darkness comes from an outside mount with generous overlap, side channels, or "
      "layering a shade under a drape.",
      [("Outside mount with overlap",
        "The simplest fix. Mount above the opening and extend past it on both sides so there is no "
        "edge for light to come around."),
       ("Side channels",
        "Tracks at each side that the shade runs in. The closest to genuine blackout you can get "
        "from a shade alone, and the right answer for a media room."),
       ("Cellular blackout shades",
        "Blackout fabric plus the insulating cell. Good for a west facing bedroom where heat and "
        "light are both problems."),
       ("Layering",
        "A roller or cellular shade with a drape over it. Handles light and softens the room, and "
        "it is what most bedrooms end up with.")],
      ["Whether you need true darkness or just much less light",
       "Whether the room takes morning or afternoon sun",
       "How much wall space there is above and beside the opening for an outside mount",
       "Whether anyone in the room sleeps during the day"],
      ["An inside mount sold as blackout, which always leaks at the edges",
       "Blackout fabric with no plan for the gaps, which is the same brightness at 6am",
       "Ignoring heat, so the room is dark and still too warm to sleep in",
       "Cords in a child's bedroom, which should be cordless or motorized as standard"])

    X["window-treatments-for-home-offices"] = room(
      "home offices are a glare problem before they are a privacy problem. Solar shades with the "
      "right openness factor cut screen glare while keeping the view, which is what most people "
      "actually want at a desk.",
      [("Solar shades",
        "Cut glare without darkening the room. Openness factor is chosen for which way the window "
        "faces, tighter for west, more open for north."),
       ("Dual or day-night shades",
        "A solar layer for working hours and a blackout layer for video calls or afternoon sun. "
        "One treatment, two jobs."),
       ("Motorized with a schedule",
        "The shades handle the afternoon sun without you getting up mid-call. This is the feature "
        "home office clients say they would not give up."),
       ("What to avoid",
        "Anything that makes the room dark enough to need lights on all day, which usually makes "
        "screen glare worse rather than better.")],
      ["Where the screen sits relative to the window",
       "Whether the window is behind you on video calls",
       "Which way the room faces and when it takes direct sun",
       "Whether the room doubles as a guest room and needs blackout too"],
      ["Blackout on a north facing office, which just means lights on all day",
       "A shade that is see-through at night when the desk lamp is on",
       "Glare handled by tilting a blind, which cuts the view as well as the glare",
       "Manual shades on a window behind the desk you have to climb over to reach"])

    X["window-treatments-for-nurseries"] = room(
      "nurseries need two things without compromise: no accessible cords, and enough darkness for "
      "daytime naps. Cordless or motorized blackout, mounted outside the opening, is the answer.",
      [("Cordless is not optional",
        "Corded window coverings are a recognised strangulation hazard for young children. Cordless "
        "lift or motorization should be treated as a requirement in any room a child sleeps in."),
       ("Blackout, mounted outside",
        "Daytime naps need real darkness, and an inside mount always leaks at the edges. Outside "
        "mount with overlap, or side channels."),
       ("Cellular blackout",
        "Blocks light and insulates, which helps keep the room at a steady temperature through a "
        "Texas afternoon."),
       ("Motorized on a schedule",
        "Shades that close for nap time without anyone opening the door is a small thing that "
        "parents consistently say was worth it.")],
      ["Where the cot sits relative to the window",
       "Whether the room takes morning or afternoon sun",
       "Whether you need darkness for daytime naps as well as at night",
       "How the room will be used in three years, when it is no longer a nursery"],
      ["Any accessible cord within reach of a cot",
       "Inside mounted blackout that still lets a bright line in at 3pm",
       "Furniture placed so a child can climb to reach a window covering",
       "Choosing on looks in a room where safety is the specification"])

    # ------------------------------------------------------------- patio
    X["motorized-patio-shades-for-texas-patios"] = room(
      "on a patio span, motorization is a practical requirement rather than a luxury. Exterior "
      "shades should be retracted in high wind, and a large shade you have to crank by hand is one "
      "you will leave down when you should not.",
      [("Why span forces the decision",
        "Patio openings are wide. A shade across sixteen or twenty feet is heavy, and hand "
        "operation stops happening within a season."),
       ("Wind is the real argument",
        "Exterior shades come up when weather turns. Motorization is what makes that quick enough "
        "that it actually gets done, which is what protects the fabric and the hardware."),
       ("Power options outdoors",
        "Solar charging suits patios particularly well, because the shade is in the sun by "
        "definition. Hardwired is cleanest if the structure is being built or rewired."),
       ("Control that gets used",
        "A wall switch by the patio door, a remote, and a schedule for the afternoon. App control "
        "is useful, but the switch by the door is what people reach for.")],
      ["The exact span, which drives hardware and motor sizing",
       "Which way the patio faces, which drives fabric openness",
       "Whether there is power at the structure or you need battery and solar",
       "How exposed the site is to wind"],
      ["A hand-cranked shade on a wide span that ends up permanently down",
       "Fabric left out in high wind because retracting it was too much effort",
       "Openness chosen on looks rather than on which way the patio faces",
       "Hardware sized for the fabric but not for the span"],
      [sec("What this does for the house, not just the patio",
        p("Shading a patio also shades the wall and glass behind it. The rooms on that side take "
          "less heat load in the afternoon, which is the part people do not expect when they buy "
          "shades for the outdoor space."))])

    X["outdoor-roller-shades-vs-patio-screens"] = room(
      "the terms get used interchangeably, but the practical difference is how they are held at the "
      "edges. A roller shade hangs free and moves in wind. A screen system runs in side tracks and "
      "stays put, which matters on an exposed patio.",
      [("Outdoor roller shades",
        "A fabric panel on a tube, usually with a weighted bottom bar. Simple, less expensive, and "
        "the right answer on a sheltered porch."),
       ("Track guided patio screens",
        "The fabric runs in channels at each side, so it does not billow and it seals the edges. "
        "Better on an exposed site and better at keeping insects out."),
       ("Openness factor applies to both",
        "Whichever system you choose, the weave decides how much sun and view you keep. That "
        "choice matters more than the system for comfort."),
       ("Cost and complexity",
        "Tracks add hardware and installation time. On a sheltered patio that money is often better "
        "spent on a better fabric or on motorization.")],
      ["How exposed the patio is to wind",
       "Whether you want insect control as well as shade",
       "Whether the opening is a simple rectangle or has posts and beams in the way",
       "Which way the space faces and at what time of day you use it"],
      ["A free hanging shade on an exposed site that billows and wears at the edges",
       "Track systems specified where a simple roller would have done",
       "Openness chosen without considering the orientation",
       "Hardware not rated for the span"])

    X["how-to-choose-patio-shade-openness-factor"] = room(
      "openness is the percentage of the weave that is open. Lower numbers block more sun and give "
      "more daytime privacy but soften the view. Higher numbers keep the view and still cut glare. "
      "Which way the space faces should decide it.",
      [("Tighter weaves",
        "Block the most sun and give the most daytime privacy. The right choice for a west facing "
        "patio that takes hard afternoon sun, at the cost of some view."),
       ("Mid range weaves",
        "The usual compromise. Meaningful heat and glare reduction while keeping a usable view out "
        "to the yard. Where most patios land."),
       ("More open weaves",
        "Keep the view almost intact and still cut glare. Suit north facing porches and spaces you "
        "use in the morning rather than the afternoon."),
       ("Fabric colour matters too",
        "Darker fabrics cut glare and preserve the view better. Lighter fabrics reflect more heat "
        "but scatter light, which can actually increase glare.")],
      ["Which way the space faces and when you use it",
       "Whether you want to keep a specific view",
       "How close the neighbours are, since daytime privacy comes with a tighter weave",
       "Whether the space is used mainly morning or afternoon"],
      ["An open weave on a west facing patio, which does not cut enough afternoon sun",
       "A tight weave on a north porch, which makes it gloomy for no benefit",
       "Choosing colour on looks without considering glare",
       "Expecting any openness factor to give privacy after dark, which none of them do"])

    # ------------------------------------------------------------- other
    X["smart-blinds-what-they-do"] = room(
      "smart blinds are motorized blinds that talk to something else: an app, a voice assistant, a "
      "hub or a schedule. The motor is the hardware, smart is what you connect it to.",
      [("Scheduling",
        "The feature people actually keep using. Shades close against the afternoon sun and open in "
        "the morning without anyone thinking about it."),
       ("Voice and app control",
        "Useful, and the thing everyone asks about first. In practice a wall switch by the door "
        "gets used more often than a phone."),
       ("Scenes and integration",
        "Shades that move with the rest of a smart home setup, so a single action handles lights "
        "and shades together."),
       ("Sun and temperature triggers",
        "Shades that respond to conditions rather than the clock. The most genuinely useful version "
        "in a Texas summer, and the least commonly set up.")],
      ["Which ecosystem you already use, since that decides compatibility",
       "Whether you want battery, hardwired or solar charging",
       "Who sets it up and programs it at install",
       "Whether the motor is serviceable, and what the warranty covers"],
      ["Motorizing every window instead of the ones that need it",
       "Buying into an ecosystem that does not match what the house already runs",
       "Nobody configuring the schedule, so it stays a very expensive remote control",
       "Battery packs on high windows that are awkward to recharge"])

    X["child-safe-window-coverings"] = room(
      "the only reliably safe option is no accessible cord. Cordless lift, motorization, or a "
      "shutter with no cord at all. Cord cleats and tie-downs are a mitigation, not a solution.",
      [("Cordless lift",
        "You raise and lower the treatment by hand with no cord. Standard on most new blinds and "
        "shades, and the baseline for any room a child uses."),
       ("Motorization",
        "No cord and no reaching. Particularly worth it on high windows where a cordless lift is "
        "still awkward."),
       ("Shutters",
        "No cords by design. Louvers tilt with a rod or a hidden mechanism, which is part of why "
        "they suit children's rooms."),
       ("What is not enough",
        "Cord cleats, tension devices and tie-downs depend on an adult using them correctly every "
        "single time. They reduce risk, they do not remove it.")],
      ["Every room a child sleeps in, plays in, or can reach unsupervised",
       "Where furniture sits, since a cot or chair turns a high window into a reachable one",
       "Older treatments elsewhere in the house that still have cords",
       "Whether the treatment will still be cordless after a repair"],
      ["A cord tucked behind furniture, which moves",
       "Assuming a high window is out of reach when there is furniture beneath it",
       "Replacing one room and leaving corded treatments in the rest of the house",
       "Relying on a cleat that only works if someone uses it every day"])

    X["how-to-clean-roller-shades-and-solar-screens"] = room(
      "most roller and solar shades clean with a vacuum brush and a damp cloth. What ruins them is "
      "soaking the fabric, harsh cleaners, or rolling them up wet.",
      [("Regular dusting",
        "A vacuum brush attachment on a low setting, top to bottom, with the shade fully lowered. "
        "Doing this every few weeks prevents most of the work later."),
       ("Spot cleaning",
        "A cloth barely damp with water and mild soap, blotted rather than scrubbed. Test in a "
        "corner first, especially on a coated solar fabric."),
       ("Solar screen fabrics",
        "The open weave releases dust easily but collects it in the mesh. A soft brush works "
        "better than a cloth, which can push dirt into the weave."),
       ("Drying matters most",
        "Leave the shade fully down until it is completely dry. Rolling a damp shade is how you get "
        "marks and, on some fabrics, mildew.")],
      ["Whether the fabric is coated, which changes what you can use on it",
       "Whether the shade is exterior, since those take real dirt rather than dust",
       "How accessible the shade is, which decides how often it realistically gets done",
       "What the manufacturer's care guidance says, since it varies by fabric"],
      ["Soaking the fabric, which leaves water marks",
       "Rolling a damp shade up, which causes mildew",
       "Harsh or solvent cleaners that strip a fabric coating",
       "Scrubbing a solar weave, which pushes dirt deeper into the mesh"])
    return X
