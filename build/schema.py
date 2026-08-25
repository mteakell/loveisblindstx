"""JSON-LD @graph builders for Love Is Blinds Texas.

Rules this module enforces, deliberately:
  * A city page never claims a street address it does not have. Cities without a
    verified address get areaServed only, and defer identity to the parent brand.
  * Every distinct location gets its own @id, telephone and sameAs, so the two
    Fort Worth, Grapevine and Corsicana operators never collapse into one entity.
  * No aggregateRating and no Review nodes on our own business. Google treats
    self-serving review markup as ineligible and it can draw a manual action.
    Reviews still render as visible page content.
"""
import json

SITE  = "https://www.loveisblindstx.com"
BIZID = SITE + "/#business"
ORGID = SITE + "/#organization"
WEBID = SITE + "/#website"

def _clean(o):
    """Drop None, '' and empty containers so no literal nulls reach the page."""
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()
                if v is not None and v != "" and v != [] and v != {}}
    if isinstance(o, list):
        return [_clean(v) for v in o if v is not None and v != ""]
    return o

def tel(d):
    d = "".join(ch for ch in (d or "") if ch.isdigit())
    return "+1" + d if len(d) == 10 else ("+" + d if d else None)

def pretty(d):
    d = "".join(ch for ch in (d or "") if ch.isdigit())
    return f"({d[:3]}) {d[3:6]}-{d[6:]}" if len(d) == 10 else ""

def organization(biz):
    return {
        "@type": "Organization", "@id": ORGID, "name": biz["name"],
        "url": SITE + "/", "logo": {"@type": "ImageObject",
            "url": SITE + "/images/lib-logo.png", "width": 512, "height": 512},
        "email": biz["email"], "telephone": tel(biz["tel"]),
        "areaServed": {"@type": "AdministrativeArea", "name": "Texas"},
    }

def website(biz):
    return {
        "@type": "WebSite", "@id": WEBID, "name": biz["name"], "url": SITE + "/",
        "publisher": {"@id": ORGID}, "inLanguage": "en-US",
        "potentialAction": {"@type": "SearchAction",
            "target": {"@type": "EntryPoint",
                       "urlTemplate": SITE + "/search?q={search_term_string}"},
            "query-input": "required name=search_term_string"},
    }

def business(biz, city=None):
    """Parent brand, or one specific location when `city` is supplied."""
    if city is None:
        hq = biz["hq"]
        return _clean({
            "@type": "HomeAndConstructionBusiness", "@id": BIZID, "name": biz["name"],
            "url": SITE + "/", "telephone": tel(biz["tel"]), "email": biz["email"],
            "priceRange": "$$", "currenciesAccepted": "USD",
            "image": {"@type": "ImageObject", "url": SITE + "/images/shutters.jpg",
                      "width": 1200, "height": 800},
            "description": ("Custom blinds, shades, plantation shutters and motorized "
                            "window treatments across North Texas, East Texas, Waco and "
                            "the Austin metro. Free in-home consultations and "
                            "professional installation."),
            "address": {"@type": "PostalAddress", "streetAddress": hq["street"],
                        "addressLocality": hq["locality"], "addressRegion": hq["region"],
                        "postalCode": hq["postal"], "addressCountry": "US"},
            "geo": {"@type": "GeoCoordinates", "latitude": hq["lat"], "longitude": hq["lng"]},
            "parentOrganization": {"@id": ORGID},
            "areaServed": {"@type": "AdministrativeArea", "name": "Texas"},
            "openingHoursSpecification": [{
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
                "opens": "08:00", "closes": "18:00"}],
        })

    phone = city["phone"] or biz["tel"]
    node = {
        "@type": "HomeAndConstructionBusiness",
        "@id": f"{SITE}{city['url']}#business",
        "name": f"{biz['name']} - {city['label']}",
        "url": SITE + city["url"], "telephone": tel(phone), "email": biz["email"],
        "priceRange": "$$", "currenciesAccepted": "USD",
        "image": {"@type": "ImageObject", "url": SITE + "/images/shutters.jpg",
                  "width": 1200, "height": 800},
        "parentOrganization": {"@id": ORGID},
        "areaServed": {"@type": "City", "name": city["locality"],
                       "containedInPlace": {"@type": "AdministrativeArea", "name": "Texas"}},
        "sameAs": city.get("gbp") or None,
    }
    # Only claim a postal address when a real street address is on file.
    if city.get("street"):
        node["address"] = {"@type": "PostalAddress", "streetAddress": city["street"],
                           "addressLocality": city["locality"], "addressRegion": "TX",
                           "postalCode": city.get("postal"), "addressCountry": "US"}
    else:
        node["address"] = {"@type": "PostalAddress", "addressLocality": city["locality"],
                           "addressRegion": "TX", "addressCountry": "US"}
    if city.get("lat") and city.get("lng"):
        node["geo"] = {"@type": "GeoCoordinates",
                       "latitude": city["lat"], "longitude": city["lng"]}
    return _clean(node)

def webpage(url, name, desc, kind="WebPage", about=None, primary=None):
    return _clean({
        "@type": kind, "@id": SITE + url + "#webpage", "url": SITE + url,
        "name": name, "description": desc, "isPartOf": {"@id": WEBID},
        "about": {"@id": about or BIZID}, "inLanguage": "en-US",
        "primaryImageOfPage": ({"@type": "ImageObject", "url": SITE + primary}
                               if primary else None),
    })

def breadcrumbs(trail):
    return {"@type": "BreadcrumbList", "@id": SITE + trail[-1][1] + "#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": i, "name": n, "item": SITE + u}
                for i, (n, u) in enumerate(trail, 1)]}

def faq(url, pairs):
    if not pairs:
        return None
    return {"@type": "FAQPage", "@id": SITE + url + "#faq",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}}
                           for q, a in pairs]}

def service(url, name, desc, provider_id, area=None, catalog=None):
    """Service, not Product: we publish no prices, and a priceless Offer is noise."""
    return _clean({
        "@type": "Service", "@id": SITE + url + "#service", "name": name,
        "description": desc, "serviceType": name, "provider": {"@id": provider_id},
        "areaServed": area or {"@type": "AdministrativeArea", "name": "Texas"},
        "hasOfferCatalog": ({"@type": "OfferCatalog", "name": name,
            "itemListElement": [{"@type": "Offer", "itemOffered":
                {"@type": "Service", "name": c}} for c in catalog]} if catalog else None),
    })

def person(name, role, url=None, image=None):
    return _clean({"@type": "Person", "name": name, "jobTitle": role,
                   "worksFor": {"@id": ORGID},
                   "url": SITE + url if url else None,
                   "image": SITE + image if image else None})

def blogposting(url, title, desc, published, modified=None, image=None, author=None):
    return _clean({
        "@type": "BlogPosting", "@id": SITE + url + "#post",
        "mainEntityOfPage": {"@id": SITE + url + "#webpage"},
        "headline": title[:110], "description": desc,
        "datePublished": published, "dateModified": modified or published,
        "author": {"@id": ORGID} if not author else person(author, "Author"),
        "publisher": {"@id": ORGID},
        "image": ({"@type": "ImageObject", "url": SITE + image,
                   "width": 1200, "height": 800} if image else None),
        "inLanguage": "en-US",
    })

def render(nodes):
    g = [n for n in nodes if n]
    return ('<script type="application/ld+json">\n'
            + json.dumps(_clean({"@context": "https://schema.org", "@graph": g}),
                         indent=1, ensure_ascii=False)
            + '\n</script>')
