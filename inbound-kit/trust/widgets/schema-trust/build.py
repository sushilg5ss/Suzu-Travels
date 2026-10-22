"""schema-trust (TRUST_BACKLOG row 9): JSON-LD for hub /india-tours/ (11411).
Adds to Rank Math's existing graph WITHOUT a second Organization: one untyped node with the SAME @id as Rank Math's
TravelAgency (https://suzutravels.com/#organization) carrying the registration credential, foundingDate and areaServed,
plus an OfferCatalog of the 6 hub tour cards (TouristTrip + Offer, US$ 'from' prices only from data/prices.json).
Writes widget.html (one line, no '&'). Run: python3 build.py"""
import json, pathlib
H = pathlib.Path(__file__).resolve().parent
KIT = H.parents[2]
allowed = set(json.load(open(KIT / 'data/prices.json'))['allowed'])
S = 'https://suzutravels.com'
ORG = S + '/#organization'
HUB = S + '/india-tours/'
CARDS = HUB + '#north-india-tour-packages-in-us-dollars'
PRICE_NOTE = ('From price per person for two travellers sharing a room in 3-star hotels, with a private car and driver and daily '
              'breakfast. International flights and the Delhi to Srinagar flight are not included. Final price confirmed on quote in US$.')
BOOKING = ('20% deposit locks your dates and price; full refund if cancelled within 48 hours of paying; balance before the trip; '
           'pay by card via Razorpay (international cards accepted) or PayPal.')
# (name, days/nights, places, price, url, image) — copied from the live hub cards 22 Oct 2026
TOURS = [
 ('Classic Golden Triangle', 6, 5, ['Delhi', 'Agra', 'Jaipur'], 449, S + '/golden-triangle-tour/', '2026/07/Amer-fort-jaipur.webp'),
 ('Golden Triangle + Rishikesh and Haridwar', 8, 7, ['Delhi', 'Agra', 'Jaipur', 'Haridwar', 'Rishikesh'], 649, CARDS, '2026/04/Dashing-Rishikesh-scaled.webp'),
 ('Golden Triangle + Kashmir', 10, 9, ['Delhi', 'Agra', 'Jaipur', 'Srinagar', 'Gulmarg', 'Pahalgam'], 899, CARDS, '2026/10/kashmir-shikara-ride-dal-lake-srinagar-winter.webp'),
 ('Golden Triangle + Himalayas', 12, 11, ['Delhi', 'Agra', 'Jaipur', 'Shimla', 'Manali'], 1099, CARDS, '2026/04/Manali-Tour-By-Suzu-Travels-scaled.webp'),
 ('Golden Temple and the Himalayas', 10, 9, ['Delhi', 'Amritsar', 'Dharamshala', 'Manali'], 949, CARDS, '2026/04/Amritsar-by-suzu-Travels.webp'),
 ('Char Dham Yatra for NRI and overseas pilgrims', 11, 10, ['Yamunotri', 'Gangotri', 'Kedarnath', 'Badrinath'], 799, S + '/char-dham-yatra-for-nri/', '2026/05/Char-Dham-Yatra-scaled.webp'),
]
items = []
for i, (name, d, n, places, price, url, img) in enumerate(TOURS, 1):
    assert price in allowed, (name, price)
    items.append({'@type': 'Offer', 'position': i, 'price': price, 'priceCurrency': 'USD', 'description': PRICE_NOTE,
                  'url': url, 'seller': {'@id': ORG},
                  'itemOffered': {'@type': 'TouristTrip', 'name': f'{name} ({d} days / {n} nights)',
                                  'touristType': 'International travellers', 'image': S + '/wp-content/uploads/' + img,
                                  'itinerary': {'@type': 'ItemList', 'itemListElement': [
                                      {'@type': 'ListItem', 'position': k, 'item': {'@type': 'City', 'name': p}} for k, p in enumerate(places, 1)]},
                                  'provider': {'@id': ORG}}})
graph = [
 {'@id': ORG, 'foundingDate': '2019', 'areaServed': {'@type': 'Country', 'name': 'India'},
  'knowsLanguage': 'en',
  'hasCredential': {'@type': 'EducationalOccupationalCredential', 'name': 'HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022',
                    'credentialCategory': 'Travel agent registration', 'identifier': 'DTO-MND-11-243/2022',
                    'recognizedBy': {'@type': 'Organization', 'name': 'HP Tourism'}, 'url': S + '/certificates/'},
  'hasOfferCatalog': {'@id': HUB + '#tours'}},
 {'@type': 'OfferCatalog', '@id': HUB + '#tours', 'name': 'Private India tours in US dollars', 'url': CARDS,
  'description': 'Private tours with car, driver and hotels, quoted in US$. Booking: ' + BOOKING,
  'numberOfItems': len(items), 'itemListElement': items},
]
js = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':'))
assert '&' not in js and '<' not in js and '\n' not in js
out = '<!--szt:schema-trust--><script type="application/ld+json">' + js + '</script><!--/szt:schema-trust-->'
(H / 'widget.html').write_text(out)
print(len(out), 'bytes')
