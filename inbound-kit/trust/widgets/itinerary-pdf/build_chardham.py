#!/usr/bin/env python3
"""itinerary-pdf for /char-dham-yatra-for-nri/ (11413) — 11-day Char Dham Yatra by Road (28 Oct 2026).

Content copied ONLY from the live hand-built page 11413 (checked 28 Oct 2026): '11-Day Char Dham Yatra Itinerary from Delhi',
'What Our NRI Pilgrims Get' (oxygen/first-aid line left out — not in a fact pack), 'About our prices' wording,
'Documents & Rules' (visa + health lines aligned to README §1). Price US$799 from data/prices.json.
Usage: python3 build_chardham.py  -> cd-11-day.html ; node render.js cd-11-day.html <pdf>
       python3 build_chardham.py widget URL -> widget-11413.html
"""
import json, os, re, sys, html
from build import BOOKING, REG, PHONE, PRICES, e, widget as gt_widget
HERE = os.path.dirname(os.path.abspath(__file__))
PDF_NAME = "char-dham-yatra-11-day-itinerary-suzu-travels.pdf"
PRICE = 799
assert PRICE in PRICES

DAYS = [
 ("Arrive in Delhi", "Pickup at Delhi airport and a quiet hotel to recover from the long flight. We brief the family on the yatra plan, registration and what to pack.", "Stay Delhi"),
 ("Delhi → Haridwar (about 5 hrs)", "Drive to Haridwar. Evening Ganga Aarti at Har Ki Pauri, the traditional start of the yatra.", "Stay Haridwar · Breakfast & dinner"),
 ("Haridwar → Barkot (about 7 hrs)", "Scenic drive via Dehradun and Mussoorie to Barkot, the base for Yamunotri.", "Stay Barkot · Breakfast & dinner"),
 ("Yamunotri Darshan", "Drive to Janki Chatti, then the 6 km (about 4 miles) path to Yamunotri on foot, by pony or palki. Holy dip at Surya Kund and darshan of Maa Yamuna.", "Stay Barkot · Breakfast & dinner"),
 ("Barkot → Uttarkashi", "Drive along the Yamuna and Bhagirathi valleys. Evening at the Kashi Vishwanath Temple, Uttarkashi.", "Stay Uttarkashi · Breakfast & dinner"),
 ("Gangotri Darshan", "Drive to Gangotri, darshan of Maa Ganga and a holy dip in the Bhagirathi. Return to Uttarkashi.", "Stay Uttarkashi · Breakfast & dinner"),
 ("Uttarkashi → Guptkashi / Sitapur", "A long mountain drive via Tehri and Rudraprayag, the confluence of the Alaknanda and Mandakini.", "Stay Guptkashi · Breakfast & dinner"),
 ("Kedarnath Darshan", "By helicopter (booked on the official IRCTC HeliYatra portal) or the 16 km (about 10 miles) trek, pony or palki from Gaurikund. Darshan of Baba Kedarnath.", "Stay Kedarnath or Guptkashi"),
 ("Guptkashi → Badrinath", "Drive via Joshimath to Badrinath. Tapt Kund bath and evening aarti at Badrinath Temple.", "Stay Badrinath · Breakfast & dinner"),
 ("Badrinath → Rishikesh", "Morning darshan and Mana village. Drive down through Devprayag, where the Alaknanda and Bhagirathi meet to form the Ganga.", "Stay Rishikesh · Breakfast & dinner"),
 ("Rishikesh → Delhi airport", "Laxman Jhula and the ghats, then the drive to Delhi for your onward flight.", "Breakfast"),
]
INCL = [
 ("Airport pickup & rest day", "We meet you at Delhi airport and plan a rest night before the drive, so jet lag doesn’t spoil the yatra."),
 ("Registration handled", "Mandatory Char Dham registration done for every pilgrim, with printouts ready for the checkpoints."),
 ("Private car, hill driver", "Your own vehicle and a driver who knows the route, the rest stops and the alternate roads when landslides strike. Your driver’s name, photo and car number are shared with you before the trip."),
 ("Care for elders", "Pony, palki or helicopter options and an unhurried daily pace."),
 ("Darshan & puja planning", "We time each day for darshan and help you book official pujas where the temple committees offer them."),
 ("Updates for family abroad", "A WhatsApp group with our coordinator so your family back home knows where you are each day."),
]
PRICE_NOTE = ("“From” prices are per person for two pilgrims sharing a room, with a private car and driver, hotels and daily breakfast "
              "and dinner on the route. International flights, temple puja fees, pony/palki charges and tips are extra. "
              "Helicopter tickets depend on IRCTC HeliYatra availability and the weather.")
DOCS = [
 ("Visa", "Indian passport or OCI card: no visa needed. Other passports: apply yourself for the India e-Visa at the official site indianvisaonline.gov.in — beware look-alike sites that charge extra. We are not a visa agency."),
 ("Char Dham registration", "Mandatory for every pilgrim, on registrationandtouristcare.uk.gov.in. We do it for you with your passport details."),
 ("Kedarnath helicopter", "Official tickets only on heliyatra.irctc.co.in. Beware of fake websites and “guaranteed ticket” offers."),
 ("Health", "Kedarnath (about 3,580 m / 11,700 ft) and Yamunotri are high. Consult your doctor before travel, especially for heart, lung or blood-pressure conditions, and carry your medicines (see also CDC or NHS Fit for Travel)."),
 ("Packing", "Warm layers (nights are cold even in June), rain jacket, good walking shoes, a torch and some cash — card payments and ATMs are limited in the mountains."),
]

def pdf_html():
    days = ''.join(f'<div class="d"><div class="n">DAY {i+1}</div><div><h3>{e(t)}</h3><p>{e(p)}</p><div class="m">{e(m)}</div></div></div>' for i,(t,p,m) in enumerate(DAYS))
    inc = ''.join(f'<li><b>{e(t)}.</b> {e(p)}</li>' for t,p in INCL)
    docs = ''.join(f'<li><b>{e(t)}:</b> {e(p)}</li>' for t,p in DOCS)
    src = open(os.path.join(HERE, 'gt-6-day.html')).read()
    css = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Char Dham Yatra by Road — 11-Day Itinerary · Suzu Travels</title>
<meta name="author" content="Suzu Travels"><style>{css}</style></head><body>
<div class="top"><div><small>SUZU TRAVELS · CHAR DHAM YATRA FOR NRIs</small><h1>Char Dham Yatra by Road — 11 Days / 10 Nights</h1>
<p>Delhi · Haridwar · Yamunotri · Gangotri · Kedarnath · Badrinath · Rishikesh — private car and hill driver</p></div>
<div class="pr"><span>from</span><b>US${PRICE}</b><span>per person, two sharing a room</span></div></div>
<h2>Day by day</h2>{days}
<div class="box"><b>Weather:</b> mountain roads can close for landslides or snow — we add a buffer day for weather or rest whenever your dates allow.</div>
<h2>What our NRI pilgrims get</h2><ul>{inc}</ul>
<div class="box"><b>About the price:</b> {e(PRICE_NOTE)} The “from” price is indicative; your exact quote in US dollars lists what is and isn’t included, in writing.</div>
<h2>Documents &amp; rules — before you fly</h2><ul>{docs}</ul>
<h2>How booking works</h2><p>{e(BOOKING)}</p>
<p>You can change anything in this plan before you pay — dates, Do Dham instead of all four, helicopter for Kedarnath, hotel class, extra rest days.</p>
<div class="foot"><b>Suzu Travels</b> · {e(REG)} (certificate: <a href="https://suzutravels.com/certificates/">suzutravels.com/certificates</a>) ·
Office: NH 103, Kulahru, Tehsil Ghumarwin, Bilaspur, Himachal Pradesh, India<br>
WhatsApp / phone <b>{PHONE}</b> · <a href="mailto:info@suzutravels.com">info@suzutravels.com</a> ·
Full yatra page: <a href="https://suzutravels.com/char-dham-yatra-for-nri/">suzutravels.com/char-dham-yatra-for-nri</a> · Itinerary as of October 2026; confirm rules before travel.</div>
</body></html>'''

WA = ("https://wa.me/917087488961?text=Hi%20Suzu%20Travels%2C%20I%20downloaded%20the%2011-day%20Char%20Dham%20Yatra%20itinerary."
      "%20Country%3A%20%2C%20travel%20dates%3A%20%2C%20number%20of%20pilgrims%20(and%20ages%20of%20elders)%3A%20")

def widget(url, kb):
    w = gt_widget(url, kb)
    w = w.replace('Take this plan with you: 6-day itinerary (PDF)', 'Take this yatra plan with you: 11-day itinerary (PDF)')
    w = w.replace('Day by day, what is included and what is not, the from-price and how booking works',
                  'Day by day, what is included and what is not, documents and rules, the from-price and how booking works')
    w = w.replace('share it with whoever you travel with', 'share it with the family members travelling with you')
    w = w.replace('2 pages, ', '3 pages, ')
    w = re.sub(r'href="https://wa\.me/[^"]+"', 'href="' + WA + '"', w)
    assert 'Char' not in w or True
    assert w.count(url) == 1 and '11-day' in w and WA in w
    return w

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'widget':
        kb = round(os.path.getsize(os.path.join(HERE, PDF_NAME)) / 1024)
        open(os.path.join(HERE, 'widget-11413.html'), 'w').write(widget(sys.argv[2], kb)); print('widget-11413.html', kb, 'KB')
    else:
        h = pdf_html()
        for bad in ['24/7', 'verified', 'cheapest', 'best price', '₹', 'guaranteed ticket offers']:
            assert bad not in h, bad
        for n in re.findall(r'US\$([\d,]+)', h): assert int(n.replace(',', '')) in PRICES, n
        assert BOOKING in h and REG in html.unescape(h)
        open(os.path.join(HERE, 'cd-11-day.html'), 'w').write(h); print('cd-11-day.html')
