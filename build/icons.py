"""Line icons for the product-type cards.

58 distinct type names across the six products, so icons are matched on
keywords rather than named one by one. Everything is inline SVG: no extra
requests, no icon font, and it inherits currentColor so it themes with the
rest of the page.
"""
import re

_S = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">')

ICONS = {
 # blinds: horizontal slats in a frame
 "blinds": '<rect x="3" y="4" width="18" height="16" rx="1.5"/><path d="M3 9h18M3 13h18M3 17h18"/>',
 # shutters: framed panel with louvres and a centre rail
 "shutter": '<rect x="3" y="3" width="18" height="18" rx="1.5"/><path d="M12 3v18M6 8h3M6 12h3M6 16h3M15 8h3M15 12h3M15 16h3"/>',
 # roller shade: roll at top, fabric pulled part way down
 "shade": '<rect x="3" y="3" width="18" height="18" rx="1.5"/><path d="M3 6h18"/><path d="M6 6v8h12V6"/><path d="M12 14v3"/>',
 # cellular: honeycomb cells
 "cell": '<path d="M7 4h6l3 4-3 4H7L4 8Z"/><path d="M13 12h6"/><path d="M7 12h2l3 4-3 4H7l-3-4Z"/>',
 # sun: solar screen, glare, heat
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/>',
 # moon: blackout, bedrooms
 "moon": '<path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5Z"/>',
 # outdoor: pergola / awning over a deck
 "outdoor": '<path d="M3 10 12 4l9 6"/><path d="M5 10v10M19 10v10"/><path d="M5 14h14"/><path d="M9 20v-4h6v4"/>',
 # motor: remote control
 "motor": '<rect x="8" y="2" width="8" height="20" rx="2"/><path d="M11 6h2"/><circle cx="12" cy="11" r="1.2"/><path d="M10 16h4"/>',
 # sliding door
 "door": '<rect x="3" y="3" width="18" height="18" rx="1.5"/><path d="M12 3v18"/><path d="M9 12h.01M15 12h.01"/>',
 # arched / bay / tall window
 "arch": '<path d="M5 21V11a7 7 0 0 1 14 0v10Z"/><path d="M12 4v17M5 13h14"/>',
 # droplet: bathrooms, kitchens, moisture
 "drop": '<path d="M12 3s6 6.4 6 10.2A6 6 0 0 1 6 13.2C6 9.4 12 3 12 3Z"/>',
}

# first match wins, so put the specific words above the generic ones
RULES = [
 ("motor",   ("motoriz", "app and voice", "battery", "hardwired", "scheduling", "retrofit", "hub", "remote", "cordless", "smart")),
 ("outdoor", ("patio", "porch", "pergola", "pool", "outdoor", "exterior", "awning", "retractable")),
 ("sun",     ("solar", "sun", "glare", "uv", "light filtering", "sheer")),
 ("moon",    ("blackout", "bedroom", "room darken")),
 ("drop",    ("bath", "kitchen", "moisture", "humid")),
 ("door",    ("sliding", "slider", "french door", "patio door")),
 ("arch",    ("arch", "bay", "angled", "tall window", "specialty")),
 ("cell",    ("cellular", "honeycomb", "dual", "day-night", "banded")),
 ("shutter", ("shutter", "louver", "louvre", "panel", "cafe", "divider", "full height", "half height")),
 ("blinds",  ("blind", "wood", "faux", "composite", "mini", "micro", "venetian", "aluminum", "aluminium")),
 ("shade",   ("shade", "roller", "roman", "woven", "drape", "curtain")),
]


def icon_for(name, used=None):
    """Pick an icon, avoiding one already used in the same block.

    Three cards about motorization sat side by side with the identical remote
    icon, which reads as a rendering bug rather than a design choice. `used` is
    a set the caller mutates, so each card in a block gets a different glyph
    even when the topic words overlap.
    """
    t = name.lower()
    order = [k for k, words in RULES if any(w in t for w in words)]
    order += [k for k in ICONS if k not in order]
    for key in order:
        if used is None or key not in used:
            if used is not None:
                used.add(key)
            return '<span class="tico">' + _S + ICONS[key] + '</svg></span>'
    return '<span class="tico">' + _S + ICONS[order[0]] + '</svg></span>'


# The five guarantees. Keyed by id because these are fixed, named things
# rather than the 58 free-text product types the keyword rules handle.
GUARANTEE_ICONS = {
 "lifetime":     '<path d="M12 3 4 6v6c0 4.4 3.2 7.9 8 9 4.8-1.1 8-4.6 8-9V6Z"/><path d="m9 12 2 2 4-4"/>',
 "price-match":  '<path d="M3 6h13l-1.5 8H5Z"/><circle cx="9" cy="19" r="1.4"/><circle cx="15" cy="19" r="1.4"/><path d="M17 3h4v4"/><path d="m21 3-5 5"/>',
 "guaranten":    '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5V15"/><path d="M13 12a2 2 0 0 1 4 0v3a2 2 0 0 1-4 0Z"/>',
 "service":      '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "transferable": '<path d="M4 9h13l-3-3"/><path d="M20 15H7l3 3"/>',
}


def guarantee_icon(gid):
    p = GUARANTEE_ICONS.get(gid, GUARANTEE_ICONS["lifetime"])
    return '<span class="tico">' + _S + p + '</svg></span>'
