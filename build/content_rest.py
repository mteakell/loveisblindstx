"""Measuring, comparison, room, patio, smart, safety and care posts."""

def build(N):
    p, sec, sub, li = N.p, N.sec, N.sub, N.li
    X = {}
    DEPTH = "".join([
      sec("Why custom orders punish small errors",
        p("A custom treatment is cut to the number you give. There is no returning it, no trimming "
          "it down and no swapping it for the next size. That is the whole reason we measure every "
          "opening ourselves rather than working from a list."),
        li("An eighth of an inch too wide on an inside mount will not fit at all",
           "An eighth too narrow leaves a light gap you will notice every morning",
           "A height error shows as a treatment that stops short of the sill",
           "Reversing width and height produces something unusable")),
      sec("Openings are rarely square",
        p("Houses settle. Frames move. In most homes over a few years old, the width at the top of "
          "a window is not the width at the bottom, and the difference is often enough to matter on "
          "an inside mount."),
        p("This is why we measure in three places and why an outside mount is frequently the right "
          "answer in an older house, even when an inside mount would look neater.")),
      sec("Tools worth having",
        li("A steel tape, not a cloth or fabric one, which stretches",
           "A step ladder, so you are measuring level rather than reaching",
           "A notepad with a column for width and a column for height, kept in that order",
           "A second person for anything wide or high")),
    ])

    CONSULT = sec("Or let us measure it",
        p("Every consultation includes measuring each opening on site. It is free, there is no "
          "obligation, and it removes the one risk that matters on a custom order: a treatment "
          "cut to the wrong number."))

    # ------------------------------------------------------------- measure
    STEPS = sec("Measuring step by step",
        sub("1. Decide inside or outside mount first",
            p("Everything downstream changes based on this. Inside mount sits within the frame and "
              "looks built in. Outside mount covers the opening and hides an out of square frame.")),
        sub("2. Measure the width in three places",
            p("Top, middle and bottom. Openings settle, especially in older houses. For an inside "
              "mount use the narrowest of the three. For an outside mount measure the area you want "
              "covered and add overlap on each side.")),
        sub("3. Measure the height in three places",
            p("Left, centre and right. For an inside mount use the longest. For an outside mount "
              "measure from where the treatment will mount to where you want it to end.")),
        sub("4. Check the depth",
            p("Inside mount needs enough clear depth for the headrail. Shutters need more than "
              "blinds. If the frame is shallow, or there is a crank, alarm sensor or tile return "
              "in the way, outside mount is the answer.")),
        sub("5. Write it width by height, always",
            p("Width first, height second, every time. Reversing them is the single most common "
              "way a custom order goes wrong.")))
    MISTAKES = sec("The mistakes that cost a remake",
        li("Measuring the old blind instead of the opening",
           "Rounding up on an inside mount, which leaves a treatment that will not fit",
           "Using one width measurement on an opening that is not square",
           "Forgetting the depth check before committing to inside mount",
           "Writing height before width"))
    X["how-to-measure-for-blinds"] = "".join([
      p("<strong>Short answer:</strong> decide inside or outside mount, measure width and height in "
        "three places each, use the narrowest width and longest height for inside mount, and always "
        "write width before height."),
      sec("Why measuring is where custom orders go wrong",
        p("A custom blind is cut to your number. If the number is wrong, the blind is wrong, and it "
          "is not returnable. That is the whole reason we measure every opening ourselves rather "
          "than working from a list a customer sends over.")),
      STEPS, MISTAKES,
      sec("Room by room quirks",
        sub("Bathrooms", p("Check for tile returns and the swing of the shower door. Moisture also "
          "pushes you toward faux wood or composite rather than real wood.")),
        sub("Kitchens", p("Watch for window cranks and for a sill you use as a shelf. Outside "
          "mount often wins here.")),
        sub("Bedrooms", p("If you want real darkness, an outside mount with generous overlap beats "
          "an inside mount, because inside mount always leaves light gaps at the edges.")),
        sub("Sliding doors", p("Measure the full opening including the frame, and decide early "
          "whether the treatment stacks left, right or splits."))),
      DEPTH, CONSULT])
    X["how-to-measure-windows-for-blinds-and-shades"] = "".join([
      p("<strong>Short answer:</strong> the method is the same for blinds and shades, but shades "
        "are less forgiving on width and blackout shades need extra overlap to control light gaps."),
      sec("What differs between blinds and shades", 
        p("A blind has slats and a headrail. A shade is a continuous panel. That makes shades "
          "cleaner looking and slightly less tolerant of a crooked opening, because there are no "
          "slats to disguise a gap."),
        li("Blinds hide small width errors better than shades do",
           "Roller and solar shades need the roll direction decided before ordering",
           "Cellular shades need clear depth for the headrail stack",
           "Blackout shades need overlap or a side channel, or light leaks at the edges")),
      STEPS, MISTAKES,
      sec("Light gaps, and what actually closes them",
        p("Every inside mount leaves a gap at the edges. It is physics, not a defect. If the room "
          "has to be genuinely dark, the options are an outside mount with overlap, side channels, "
          "or layering a drape over the shade.")),
      DEPTH, CONSULT])
    X["inside-mount-vs-outside-mount-blinds"] = "".join([
      p("<strong>Short answer:</strong> inside mount looks built in and needs a square, deep enough "
        "frame. Outside mount forgives a bad opening, covers more glass and blocks more light."),
      sec("Inside mount",
        p("The treatment sits inside the window frame. It shows off trim, keeps the sill usable and "
          "looks purpose built."),
        li("Needs enough clear depth for the headrail",
           "Needs an opening close to square",
           "Always leaves small light gaps at the sides",
           "Leaves the sill and trim visible")),
      sec("Outside mount",
        p("The treatment mounts on the wall or the trim above the opening and covers it."),
        li("Forgives an out of square or shallow opening",
           "Blocks far more light, which is why bedrooms often use it",
           "Makes a small window look larger",
           "Covers trim you may want to see")),
      sec("How to choose in ten seconds",
        li("Beautiful trim and a square frame: inside mount",
           "Bedroom or media room where darkness matters: outside mount",
           "Shallow frame, crank handle, alarm sensor or tile return: outside mount",
           "Small window you want to feel bigger: outside mount")),
      sec("What we do on site",
        p("We check depth and square at the consultation and tell you which mount the opening "
          "actually supports, rather than which one sounded better in the abstract.")),
      sec("Depth requirements differ by product",
        p("Every treatment has a minimum depth for an inside mount, and they are not the same. A "
          "roller shade needs the least, a shutter needs the most, and cellular sits in between "
          "because the headrail has to house the stack."),
        li("Roller and solar shades need the least clear depth",
           "Cellular needs enough for the headrail and the stack",
           "Wood and faux wood blinds need room for the slats to tilt",
           "Shutters need the most, because louvers have to rotate without hitting the glass")),
      sec("What sits in the opening besides the window",
        p("Cranks, alarm sensors, tile returns, deep sills and trim all eat into usable depth. Any "
          "one of them can turn an inside mount into an outside mount, and it is better to find "
          "that out at the measure than after the order."),
        li("Window cranks in kitchens and older casement windows",
           "Alarm contacts at the top of the frame",
           "Tile returns in bathrooms that project into the opening",
           "Sills you actually use as a shelf")),
      DEPTH, CONSULT])
    X["how-to-measure-for-plantation-shutters"] = "".join([
      p("<strong>Short answer:</strong> shutters need more depth than blinds, the opening has to be "
        "assessed for square, and the frame style is chosen from what the measurement reveals."),
      sec("Shutters are less forgiving than any other treatment",
        p("A shutter is a rigid panel in a frame. It cannot flex to absorb a crooked opening the "
          "way a fabric shade can, which is why shutter measuring is the one we would least "
          "recommend doing yourself.")),
      STEPS,
      sec("Depth is the first question",
        p("Every shutter has a minimum depth for the louvers to rotate without hitting the glass or "
          "the frame. If the opening is too shallow, the answer is a frame that projects rather "
          "than abandoning shutters.")),
      sec("Frame styles and when each is used",
        sub("Inside the opening", p("Cleanest look, needs depth and a reasonably square frame.")),
        sub("Over the opening", p("Sits on the trim or wall, hides an irregular opening.")),
        sub("Bay and angled", p("Each panel is measured and built individually, and the angles "
          "between them measured on site."))),
      MISTAKES, DEPTH, CONSULT])

    # ----------------------------------------------------------- compare
    def compare(a, b, intro, rows, verdict, extra=()):
        """Comparison posts need real depth, not two bullet lists. Every one gets
        an at-a-glance pair, cost, lifespan, a Texas section and a verdict."""
        out = [p(f"<strong>Short answer:</strong> {intro}"),
               p(f"Below is how {a.lower()} and {b.lower()} actually differ on cost, light "
                 f"control, lifespan and the rooms each belongs in, so you can decide per window "
                 f"rather than picking one for the whole house.")]
        out.append(sec(f"{a} at a glance", li(*rows[0])))
        out.append(sec(f"{b} at a glance", li(*rows[1])))
        out.append(sec("The cost difference, honestly",
            p("Neither is a single price. Both are made to your openings, so the number depends on "
              "size, material, mount and whether you motorize. What is reliable is the ordering: "
              "within the same window, the option with more material and more hardware costs more."),
            p("The useful question is not which is cheaper overall, it is which one you want in "
              "the three or four rooms that matter most, and what goes in the rest of the house.")))
        out.append(sec("Lifespan and how they age",
            p("Anything on a west facing window in Texas ages faster than the same product on a "
              "north wall. Sun degrades fabric and warps light materials, and that is the single "
              "biggest factor in how long a treatment looks good."),
            li("Rigid products hold their shape but show dust and fingerprints",
               "Fabric products are softer and warmer but fade if the weave is not rated for sun",
               "Anything on a hot wall should be specified for that wall, not chosen on looks",
               "Motors and hardware usually outlast the fabric they move")))
        if len(rows) > 2:
            out.append(sec("How to choose, room by room",
                sub("Living areas", p(rows[2][0])),
                sub("Bedrooms", p(rows[2][1])),
                sub("Kitchens and bathrooms", p(rows[2][2])),
                sub("Windows that take hard afternoon sun", p(rows[2][3]))))
        for s2 in extra:
            out.append(s2)
        out.append(sec("Material decides more than format",
            p("Whichever of the two you choose, the material is what decides whether it still "
              "works in three years. On a west facing Texas window that is not a style question, "
              "it is the whole question."),
            sub("Real wood", p("Lightest and takes stain beautifully, but it moves with humidity, "
                "so it belongs in dry living areas rather than bathrooms or over a sink.")),
            sub("Faux wood and composite", p("Handle moisture and hard sun without warping. "
                "Heavier, which matters across a wide span, but far more forgiving.")),
            sub("Fabric", p("Softer in a room, and the only option where openness factor lets you "
                "trade view against shade. Specify a weave rated for sun on a hot wall."))))
        out.append(sec("Daytime privacy is not night time privacy",
            p("This catches people out more than any other detail. A weave that gives complete "
              "privacy at midday can become see-through once it is dark outside and the lights are "
              "on inside."),
            li("Decide per window whether it needs to work after dark",
               "Any inside mount leaks light at the edges, by design rather than by fault",
               "Layering a shade under a drape solves most cases one product cannot",
               "Blackout means overlap or side channels, not just opaque fabric")))
        out.append(sec("What we would ask at your consultation",
            li("Which way does the window face, and when does it take direct sun",
               "Is this a room where you need real darkness, or just less glare",
               "Do you want to keep the view, or is privacy the priority",
               "Is the opening square and deep enough for an inside mount",
               "Is it a window you can comfortably reach every day")))
        out.append(sec("The verdict", p(verdict)))
        out.append(CONSULT)
        return "".join(out)

    X["shutters-vs-blinds-which-is-right-for-your-home"] = compare("Shutters","Blinds",
      "shutters cost more, last longer and stay with the house. Blinds cost less and give you far "
      "more choice of material and light control per room.",
      [["Built to the opening and hung in a frame, so they fit the window rather than covering it","Buyers read them as part of the house, which is why they hold value at resale",
        "Easy to wipe down, with no fabric to hold dust or absorb kitchen smells","The highest cost per opening of anything we install, and the longest lived"],
       ["The widest range of materials and price points, from vinyl up to hardwood","Quick and inexpensive to swap when a room gets redecorated",
        "Slat tilt gives finer control over light than any fabric shade can","Lower cost up front, shorter working life, especially on a sun-heavy wall"],
       ["Shutters show best in front rooms and anywhere with good trim.",
        "Blinds or shades usually win, because darkness matters more than looks.",
        "Faux wood blinds or composite shutters, never real wood.",
        "Either works if the material is right, but the material matters more than the format."]],
      "Most people who ask this end up doing both: shutters in the rooms that show, blinds or shades "
      "everywhere else. That is usually the best use of the budget rather than a compromise.")
    X["roman-shades-vs-roller-shades"] = compare("Roman shades","Roller shades",
      "Roman shades are a soft, folded fabric treatment that reads as decor. Roller shades are a "
      "flat panel that rolls away almost invisibly and does the functional work better.",
      [["Fold into soft horizontal pleats as they raise, which reads as decor rather than hardware","Sit visually closer to a drape than to a blind, so they warm up a hard room",
        "Stack at the top and cover some glass even fully raised, which matters on a short window","Take a blackout lining well, so they can work in a bedroom as well as a lounge"],
       ["Roll into a slim tube and effectively disappear when raised","Available in solar screen weaves where openness is a specification you choose",
        "The best value option for glare and heat control per dollar spent","The cleanest look on a modern window, with almost no visual weight"]],
      "If the window is a design feature, Roman. If the window is a heat and glare problem, roller. "
      "In practice a lot of Texas homes use roller or solar shades on the hot side of the house and "
      "Romans in the rooms they entertain in.",
      [sec("What each does about heat",
        p("A solar roller shade is the better tool for heat and glare, because openness factor is a "
          "specification you choose. A Roman shade controls light well but is chosen for how it "
          "looks first."))])
    X["cellular-shades-vs-roller-shades"] = compare("Cellular shades","Roller shades",
      "cellular shades insulate because of the air pockets in the cell. Roller and solar shades "
      "control glare and keep the view. In Texas the honest answer is that they solve different "
      "halves of the same problem.",
      [["Honeycomb cells trap a layer of air right at the glass, which is where heat transfers","The best insulation value of any fabric shade, single or double cell",
        "Available in blackout or light filtering, so they suit bedrooms and living rooms","Stack compactly at the top, so they clear most of the glass when raised"],
       ["A single flat panel that rolls out of the way entirely","Solar screen weaves cut glare while keeping the view out to the yard",
        "Openness factor is a real specification, so you can tune view against shade","The most glare control per dollar of any interior treatment"]],
      "Cellular for rooms where the heat load through the glass is the problem, especially west "
      "facing bedrooms. Solar roller for rooms where glare and keeping the view are the problem.",
      [sec("The Texas answer",
        p("Shading the outside of the glass beats both. An exterior patio shade or solar screen "
          "stops the sun before it enters, which is why a covered patio with exterior shades stays "
          "usable in the afternoon and an unshaded one does not. Interior shades manage what is "
          "already in the room."))])
    X["are-motorized-blinds-worth-it"] = "".join([
      p("<strong>Short answer:</strong> yes on specific openings, no as a blanket upgrade. Motorize "
        "the windows you cannot reach, the ones too heavy to work by hand, and the ones you want on "
        "a schedule."),
      sec("The openings where it pays for itself",
        li("Above a stairwell, a tub, or built-in furniture",
           "Very wide or very tall treatments that are heavy to lift",
           "Patio shades that need to come up fast when the wind turns",
           "Whole banks of windows you would otherwise adjust one at a time",
           "Rooms you want on a heat or privacy schedule")),
      sec("Where it is money you did not need to spend",
        p("A standard bedroom window you walk past every day does not need a motor. Motorizing a "
          "whole house evenly is the most common way people spend more than they meant to."),
        p("A better approach is to walk the house and mark only the openings that are genuinely "
          "awkward, heavy, or that you would want on a schedule. In most houses that is three to "
          "six windows, not all of them.")),
      sec("What motorization actually changes day to day",
        p("The honest answer is that it changes whether the treatment gets used. A shade that is "
          "difficult to reach ends up permanently up or permanently down, and at that point you "
          "have paid for a treatment that does one thing."),
        li("Windows you can reach get adjusted with or without a motor",
           "Windows you cannot reach only get adjusted if there is a motor",
           "Scheduling handles the afternoon sun without anyone remembering",
           "Patio shades come up faster when the wind turns, which protects the fabric")),
      sec("Power options",
        sub("Battery", p("Simplest retrofit, no electrician, periodic recharging.")),
        sub("Hardwired", p("Best during a remodel while walls are open, nothing to recharge.")),
        sub("Solar charged", p("A small panel keeps it topped up, and Texas sun is reliable."))),
      sec("Control that people actually use",
        p("Remote and wall switch get used. App control gets used if it is set up properly at "
          "install. Scheduling is the feature people report they would not give up, because the "
          "shades handle the afternoon sun without anyone thinking about it.")),
      sec("What to ask before you buy",
        li("Is the motor serviceable, and by whom",
           "What is the warranty on the motor specifically",
           "Who programs it, and do they come back if it needs re-pairing",
           "Battery life on the openings you use most")),
      sec("What motorization costs you beyond the money",
        p("Motors need power, and power needs a plan. Battery packs get recharged, hardwiring "
          "needs to happen before the walls close, and solar needs a window that genuinely gets "
          "sun. None of these are hard, but all of them are easier to decide before you order "
          "than after."),
        li("Battery: simplest retrofit, periodic recharging, no electrician",
           "Hardwired: nothing to recharge, but plan it during a remodel",
           "Solar: keeps itself topped up on any window with real sun",
           "All three should be paired and tested at install, not left to you")),
      CONSULT])
    X["solar-shades-vs-blackout-shades"] = compare("Solar shades","Blackout shades",
      "solar shades cut glare and heat while keeping the view. Blackout shades block light. They "
      "are not competing products, they belong in different rooms.",
      [["An open weave you can see through, so the room keeps its view","Openness factor is chosen per window, tighter for west sun, opener for a north porch",
        "Cut heat and glare without turning the room into a cave","Go transparent after dark once the lights are on inside, which surprises people"],
       ["Opaque fabric that blocks light rather than filtering it","Needs overlap or side channels, because an inside mount always leaks light at the edges",
        "The right answer for bedrooms, nurseries and media rooms","No view when closed, which is the entire point of the product"]],
      "Solar in living areas and anywhere with a view worth keeping. Blackout in bedrooms, "
      "nurseries and media rooms. A lot of houses need both, and that is normal.",
      [sec("The night time surprise",
        p("A solar shade that gives perfect daytime privacy can become see-through once the lights "
          "are on inside and it is dark out. If a window needs to work after dark, it needs a "
          "blackout or a layered treatment, not a tighter solar weave."))])
    X["interior-vs-exterior-shades-for-texas-sun"] = compare("Exterior shades","Interior shades",
      "exterior shades stop the sun before it hits the glass. Interior shades manage light that has "
      "already entered and heated the room. For Texas afternoon sun, exterior wins on performance.",
      [["Mounted outside the glass, over patios, porches and windows","Stop solar heat before it passes through the glass and into the room",
        "Keep a west facing patio usable at five in the afternoon in July","Should be retracted in high wind, which is the main argument for motorizing them"],
       ["Mounted inside, with far more choice of style, colour and texture","Manage glare, privacy and the look of the room all at once",
        "Cellular options insulate at the glass and cut heat transfer measurably","Never exposed to weather, so they last on looks rather than on durability"]],
      "Use exterior shading on the hardest sun and outdoor spaces, interior everywhere else. Most "
      "houses want both, and the west wall is where exterior shading earns its keep.",
      [sec("Why the order matters",
        p("Once sunlight is through the glass, the heat is in the room. An interior shade then "
          "blocks the light but the room has already gained the heat. That single fact is why "
          "exterior shading outperforms interior shading on a west wall, and it is the whole "
          "argument for patio shades in Texas."))])
    return X
