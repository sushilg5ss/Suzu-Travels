#!/usr/bin/env python3
"""itinerary-pdf (TRUST_BACKLOG row 8) — printable itinerary PDFs + download card.

Content is copied ONLY from the live hand-built page (11412 /golden-triangle-tour/, checked 21 Oct 2026):
day-by-day section, 'What every tour includes', the exclusions line from the price cards, the FAQ price answer.
Price only from data/prices.json (449). Booking line + registration line exact (README §1).
No '24/7' wording (Trust lane keeps 'before and during your trip').

Usage: python3 build.py            -> gt-6-day.html + golden-triangle-6-day-itinerary-suzu-travels.pdf
       python3 build.py widget URL -> widget-11412.html (download card pointing at URL)
"""
import json, os, re, sys, html
HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PRICES = json.load(open(os.path.join(KIT, 'data', 'prices.json')))['allowed']

BOOKING = ("20% deposit locks your dates and price; full refund if cancelled within 48 hours of paying; "
           "balance before the trip; pay by card via Razorpay (international cards accepted) or PayPal.")
REG = "HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022"
PHONE = "+91 70874 88961"
PDF_NAME = "golden-triangle-6-day-itinerary-suzu-travels.pdf"

PRICE = 449
assert PRICE in PRICES

DAYS = [  # verbatim from 11412 '6-Day Golden Triangle Itinerary from Delhi'
 ("Arrive in Delhi", "Our driver meets you at Delhi airport (DEL) and takes you to your hotel. The rest of the day is free to recover from the flight.", "Stay Delhi"),
 ("Old & New Delhi", "Old Delhi by cycle rickshaw: Chandni Chowk and Jama Masjid. Then New Delhi: Humayun’s Tomb, Qutub Minar, India Gate and the government quarter, with a licensed guide.", "Stay Delhi · Breakfast"),
 ("Delhi → Agra (about 3–4 hrs)", "Drive by the Yamuna Expressway. Afternoon at Agra Fort, then Mehtab Bagh across the river to watch the sun set behind the Taj Mahal.", "Stay Agra · Breakfast"),
 ("Taj Mahal at sunrise → Jaipur", "Early visit to the Taj Mahal when the light is soft and the crowds are small. Back for breakfast, then drive to Jaipur, stopping at Fatehpur Sikri, the abandoned Mughal capital.", "Stay Jaipur · Breakfast"),
 ("Jaipur, the Pink City", "Amber Fort on the hill, a photo stop at Jal Mahal, then the City Palace, Jantar Mantar and Hawa Mahal. Evening free for the bazaars.", "Stay Jaipur · Breakfast"),
 ("Jaipur → Delhi airport (about 5 hrs)", "Drive back to Delhi for your flight home, or continue to Rishikesh, Kashmir or the Himalayas with us.", "Breakfast"),
]
INCL = [  # from 'What Every Tour Includes' (24/7 card left out on purpose)
 ("Airport pickup & drop", "We meet you at Delhi airport with your name board, day or night."),
 ("Private car & driver", "Air-conditioned car and an English-speaking driver for the whole tour. Fuel, tolls and parking included."),
 ("Handpicked hotels", "3-, 4- or 5-star hotels with daily breakfast, chosen for location and cleanliness."),
 ("Licensed guides", "Local guides at the Taj Mahal, Agra Fort, Amber Fort and in Delhi."),
 ("Clear USD pricing", "One quote in US dollars, with what is and isn’t included in writing."),
]
EXCL = "International flights, visa fees, monument entry tickets and tips are extra."
TAJ = "The Taj Mahal is closed to visitors every Friday — we never plan your Agra day on a Friday."

def e(s): return html.escape(s, quote=False)

def pdf_html():
    days = ''.join(f'<div class="d"><div class="n">DAY {i+1}</div><div><h3>{e(t)}</h3><p>{e(p)}</p><div class="m">{e(m)}</div></div></div>'
                   for i, (t, p, m) in enumerate(DAYS))
    inc = ''.join(f'<li><b>{e(t)}.</b> {e(p)}</li>' for t, p in INCL)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Golden Triangle Tour — 6-Day Itinerary · Suzu Travels</title>
<meta name="author" content="Suzu Travels"><style>
@page{{size:A4;margin:16mm 15mm 16mm}}*{{box-sizing:border-box}}
body{{font-family:Inter,'DejaVu Sans',sans-serif;color:#0E1B14;font-size:10.4pt;line-height:1.45;margin:0}}
.top{{background:#0E1B14;color:#F4EEDD;border-radius:10px;padding:16px 18px;display:flex;justify-content:space-between;gap:12px;align-items:flex-end}}
.top small{{color:#E2C158;letter-spacing:.12em;font-weight:700;font-size:8pt}}.top h1{{margin:4px 0 2px;font-size:19pt;line-height:1.15;color:#fff}}
.top p{{margin:0;color:#DCD3BC;font-size:9.5pt}}.pr{{text-align:right;white-space:nowrap}}.pr b{{display:block;font-size:17pt;color:#E2C158}}
.pr span{{font-size:8.2pt;color:#DCD3BC}}h2{{font-size:12.5pt;margin:16px 0 8px;color:#0E1B14;border-bottom:2px solid #E2C158;padding-bottom:4px}}
.d{{display:flex;gap:12px;padding:8px 0;border-bottom:1px solid #E8E1CC;page-break-inside:avoid}}.n{{flex:none;width:52px;font-weight:800;color:#B8860B;font-size:9pt;padding-top:2px}}
.d h3{{margin:0 0 2px;font-size:11pt}}.d p{{margin:0}}.m{{font-size:8.8pt;color:#6b6450;margin-top:3px}}
ul{{margin:0;padding-left:16px}}li{{margin:3px 0}}.box{{background:#F4EEDD;border-radius:8px;padding:10px 12px;margin-top:8px;page-break-inside:avoid}}
.box b{{color:#0E1B14}}.foot{{margin-top:14px;font-size:8.8pt;color:#4b5249;border-top:1px solid #E8E1CC;padding-top:8px}}
a{{color:#8a6508}}</style></head><body>
<div class="top"><div><small>SUZU TRAVELS · PRIVATE TOUR OF INDIA</small><h1>Classic Golden Triangle — 6 Days / 5 Nights</h1>
<p>Delhi · Agra · Jaipur · Delhi — private car, driver and local guides</p></div>
<div class="pr"><span>from</span><b>US${PRICE}</b><span>per person, two sharing a room</span></div></div>
<h2>Day by day</h2>{days}
<div class="box"><b>Taj Mahal tip:</b> {e(TAJ)}</div>
<h2>What the price includes</h2><ul>{inc}</ul>
<div class="box"><b>Not included:</b> {e(EXCL)} The "from" price is indicative; your exact quote in US dollars lists what is and isn’t included, in writing.</div>
<h2>How booking works</h2><p>{e(BOOKING)}</p>
<p>You can change anything in this plan before you pay — dates, hotel class, extra days in Rishikesh, Kashmir or the Himalayas.</p>
<div class="foot"><b>Suzu Travels</b> · {e(REG)} (certificate: <a href="https://suzutravels.com/certificates/">suzutravels.com/certificates</a>) ·
Office: NH 103, Kulahru, Tehsil Ghumarwin, Bilaspur, Himachal Pradesh, India<br>
WhatsApp / phone <b>{PHONE}</b> · <a href="mailto:info@suzutravels.com">info@suzutravels.com</a> ·
Full tour page: <a href="https://suzutravels.com/golden-triangle-tour/">suzutravels.com/golden-triangle-tour</a> · Itinerary as of October 2026.</div>
</body></html>'''

WA = ("https://wa.me/917087488961?text=Hi%20Suzu%20Travels%2C%20I%20downloaded%20the%206-day%20Golden%20Triangle%20itinerary."
      "%20Country%3A%20%2C%20travel%20dates%3A%20%2C%20number%20of%20travellers%3A%20")

def widget(url, size_kb):
    css = ('.szq{font-family:\'Plus Jakarta Sans\',system-ui,-apple-system,\'Segoe UI\',sans-serif;margin:0;padding:26px 16px;background:#F4EEDD}'
           '.szq *{box-sizing:border-box}.szq p:empty,.szq br{display:none}'
           '.szq-c{max-width:1100px;margin:0 auto;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between;'
           'background:#0E1B14;color:#F4EEDD;border-radius:18px;padding:18px 20px;box-shadow:0 10px 28px rgba(14,27,20,.12)}'
           '.szq-t{display:flex;gap:14px;align-items:center;min-width:0;flex:1 1 380px}'
           '.szq-t .szq-ic{flex:none;width:46px;height:46px;border-radius:12px;background:rgba(226,193,88,.16);color:#E2C158;display:flex;align-items:center;justify-content:center}'
           '.szq-ic svg{width:24px;height:24px}.szq-t b{display:block;color:#fff;font-size:16px;line-height:1.3}'
           '.szq-t span{display:block;color:#DCD3BC;font-size:13px;line-height:1.45;margin-top:3px}'
           '.szq-b{display:flex;gap:10px;flex-wrap:wrap}.szq-b a{display:inline-flex;align-items:center;justify-content:center;gap:7px;padding:12px 16px;'
           'border-radius:12px;font-weight:800;font-size:14px;line-height:1;text-decoration:none!important;min-height:44px}'
           '.szq-dl{background:#E2C158;color:#0E1B14!important}.szq-dl:hover{background:#F0D27A}'
           '.szq-wa{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.3);color:#fff!important}'
           '@media(max-width:520px){.szq-ic{display:none}.szq-b{width:100%}.szq-b a{flex:1 1 auto}}')
    svg = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
           '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M12 11v6"/><path d="M9.5 14.5L12 17l2.5-2.5"/></svg>')
    w = (f'<!--szt:itinerary-pdf--><section class="szq" id="itinerary-pdf" aria-label="Download the itinerary"><style>{css}</style>'
         f'<div class="szq-c"><div class="szq-t"><span class="szq-ic">{svg}</span><span><b>Take this plan with you: 6-day itinerary (PDF)</b>'
         f'<span>Day by day, what is included and what is not, the from-price and how booking works — 2 pages, {size_kb} KB. '
         f'No email or sign-up needed; print it or share it with whoever you travel with.</span></span></div>'
         f'<div class="szq-b"><a class="szq-dl" href="{url}" download target="_blank" rel="noopener">Download PDF</a>'
         f'<a class="szq-wa" href="{WA}" target="_blank" rel="noopener">Ask about this plan</a></div></div></section><!--/szt:itinerary-pdf-->')
    assert '\n' not in w and '<script' not in w
    for bad in ['24/7', 'verified', 'cheapest', 'best price', 'only ', 'left!']:
        assert bad not in w.lower(), bad
    return w

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'widget':
        kb = round(os.path.getsize(os.path.join(HERE, PDF_NAME)) / 1024)
        open(os.path.join(HERE, 'widget-11412.html'), 'w').write(widget(sys.argv[2], kb))
        print('widget-11412.html', kb, 'KB')
    else:
        h = pdf_html()
        for bad in ['24/7', 'verified', 'cheapest', 'best price', '₹']:
            assert bad not in h, bad
        for n in re.findall(r'US\$([\d,]+)', h):
            assert int(n.replace(',', '')) in PRICES, n
        assert BOOKING in h and REG in html.unescape(h)
        open(os.path.join(HERE, 'gt-6-day.html'), 'w').write(h)
        print('gt-6-day.html written; render with: node -e (see README)')
