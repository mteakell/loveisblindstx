"""Additional product types and FAQs, so each city page shows a different
subset rather than the whole list. Widens the pool from 6 types / 6 FAQs to
10 / 10, with 6 and 6 shown per page selected by city index."""

EXTRA_TYPES = {
"blinds": [
 ("Wood blinds for wide windows","Wider slats and a reinforced headrail keep a long run from sagging across a big opening."),
 ("Bathroom and kitchen blinds","Composite or faux wood only. Real wood over a sink warps within a couple of seasons."),
 ("Blinds for sliding doors","Vertical slats or a panel track, so the treatment stacks clear of the door rather than fighting it."),
 ("Blackout blinds for bedrooms","A tighter slat and an outside mount with overlap, because an inside mount always leaks at the edges."),
],
"shades": [
 ("Blackout roller shades","Opaque fabric plus overlap or side channels, which is what actually makes a bedroom dark."),
 ("Top down bottom up shades","Open from the top for daylight while the lower half stays closed for privacy."),
 ("Shades for sliding doors","Panel track or a wide roller sized for the span, stacking to one side of the opening."),
 ("Outdoor rated shade fabrics","Weaves specified for sun exposure, for sunrooms and heavily glazed rooms."),
],
"plantation-shutters": [
 ("Shutters for bathrooms","Composite rather than hardwood, because steam and real wood do not get along."),
 ("Kitchen shutters","Easy to wipe down and no fabric to hold cooking smells, which is why they suit a kitchen window."),
 ("Shutters for tall windows","Split into stacked panels with their own rails so the upper section stays reachable."),
 ("Shutters over a stairwell","Fixed louvers or a motorized alternative, since nothing there gets adjusted by hand twice."),
],
"shutters": [
 ("Bay window shutters","Each panel measured to its own angle, with the joints between them taken on site."),
 ("Shutters for arched openings","Fixed or operable arch panels templated from the actual curve, not from a drawing."),
 ("Half height shutters","Lower panels only, for a street facing room that still needs its daylight."),
 ("Shutters for wide sliders","Bypass or bi-fold panels that clear the door track and stack tight."),
],
"patio-shades": [
 ("Pergola shades","Sized to the beams rather than the opening, so the fabric runs clean between posts."),
 ("Wind rated hardware","Heavier tubes and brackets on exposed sites, and a retract plan for when weather turns."),
 ("Shades for outdoor kitchens","Fabrics that shrug off cooking heat and clean easily, in an area that takes real use."),
 ("Poolside shades","Shade over seating rather than water, specified for chlorine exposure and constant sun."),
],
"motorized-shades": [
 ("Retrofit motorization","Adding a motor to an existing treatment where the hardware allows it, rather than replacing it."),
 ("Whole room scenes","One action moves every shade in a room, which is what makes a media room work."),
 ("Motorized patio shades","Exterior spans where hand operation stops happening within a season."),
 ("Hub free options","Direct remote and wall switch control, for anyone who does not want another app."),
],
}

EXTRA_FAQ = {
"blinds": [
 ("How long do custom blinds last?","With the right material for the room, a decade or more. What shortens that is putting real wood in a bathroom or vinyl on a west facing window."),
 ("Can I get blinds for an arched window?","Yes, though arches are templated on site rather than measured from numbers, and the arch itself is usually fixed rather than operable."),
 ("Do you remove the old blinds?","Yes, and we take them away if you want them gone. There is no separate charge for it."),
 ("What is the difference between a slat and a vane?","A slat is horizontal, a vane is vertical. Vanes suit sliding doors and very tall openings, slats suit everything else."),
],
"shades": [
 ("Can shades be cleaned?","Vacuum brush for dust, a barely damp cloth for marks, and leave them fully down until dry. Rolling a damp shade is how you get mildew."),
 ("Do cellular shades really save energy?","They slow heat transfer at the glass, which is measurable on a hot wall. They are not insulation in the way a wall is, but on a west bedroom the difference is noticeable."),
 ("What is top down bottom up?","A shade that opens from the top as well as the bottom, so you can take daylight in high while the lower half stays closed."),
 ("Can I layer shades with drapes?","Yes, and it is what most bedrooms end up with. The shade handles light, the drape handles the edges and softens the room."),
],
"plantation-shutters": [
 ("Can shutters be painted later?","They can be refinished, but it is a job. Better to choose the finish carefully at the consultation, where you can hold samples against your own trim."),
 ("Do shutters block more light than blinds?","Closed louvers block more than a tilted slat, and a solid panel blocks more again. None of them are blackout unless the frame seals the edges."),
 ("Are shutters good for bathrooms?","Yes, in composite. They wipe clean, they tolerate steam, and unlike a fabric shade they do not hold moisture."),
 ("How do you clean shutters?","A dry cloth or a vacuum brush along the louvers. No fabric means no dust trap, which is part of why people choose them."),
],
"shutters": [
 ("Which shutter style blocks the most light?","Solid panels, because there are no louvers and therefore no gaps. A plantation shutter with closed louvers is next."),
 ("Can I shutter a door?","Yes. Door and sidelight panels are built slim with hardware that clears the handle so the door still works normally."),
 ("Do shutters work on very wide windows?","Split into multiple panels, or on a sliding track for the widest openings. A single wide panel is not the answer."),
 ("Are shutters worth it in a rental?","Usually not. They stay with the property, so they suit a home you are keeping rather than one you are letting."),
],
"patio-shades": [
 ("Can patio shades be left down permanently?","Not in wind. Fabric left out through a storm is how shades wear out early, which is the practical argument for motorizing a large span."),
 ("Do they keep rain out?","They cut sun, glare and some wind driven spray. They are not a wall, and a track guided screen seals better than a free hanging shade."),
 ("What colour fabric should I pick?","Darker fabrics cut glare and preserve the view. Lighter ones reflect heat but scatter light, which can make glare worse."),
 ("How long do outdoor shade fabrics last?","Longer if they are retracted when not in use. Sun and wind are what age them, not time."),
],
"motorized-shades": [
 ("How long does a battery last?","It depends on how often the shade moves and how heavy it is. Solar charging removes the question on any window that gets real sun."),
 ("Can you motorize shades I already have?","Sometimes, where the existing hardware allows it. We check at the consultation rather than promising it in advance."),
 ("What happens in a power cut?","Battery and solar shades keep working. Hardwired ones do not, which is worth knowing before you choose."),
 ("Is it noisy?","Modern motors are quiet enough that a bedroom schedule does not wake anyone. You can hear them, but only just."),
],
}
