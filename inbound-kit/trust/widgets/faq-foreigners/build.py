#!/usr/bin/env python3
"""TRUST_BACKLOG row 10 — faq-for-foreigners-hub (hub 11411, own section right after the hand-built FAQ, before #more-tours).
Visible Q&A only (no JS, no second FAQPage JSON-LD — the hand-built FAQPage stays the single FAQ schema on the page).
Every answer comes from a fact pack with source + as-of:
  first-time-india-travel-guide.md facts 1-16 + legal notes (FCDO 7 Oct 2026, State Dept 16 Jun 2025, checked 23 Oct 2026)
  india-e-visa-guide.md facts 1,3,4,6,8,11,12 (checked 18 Oct 2026)
  best-time-to-visit-india.md facts 1-2 (IMD PR 804)
Not said (fact packs' 'Do not say'): visa fees, processing times, tipping, dress code, SIM/eSIM, UPI limits, vaccine lists, 'India is safe'."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
WA = 'https://wa.me/917087488961?text=Hello%20Suzu%20Travels%2C%20I%20have%20a%20question%20about%20travelling%20in%20India%3A%20'
BOOKING = ('20% deposit locks your dates and price; full refund if cancelled within 48 hours of paying; balance before the trip; '
           'pay by card via Razorpay (international cards accepted) or PayPal.')
REG = 'HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022'
DRIVER = 'your driver’s name, photo and car number are shared with you before the trip'
VISA = ('We are not a visa agency. Apply yourself, only at the official site indianvisaonline.gov.in — beware look-alike sites that '
        'charge extra. Rules and fees change; confirm on the official site before you pay.')

def a(href, txt):
    return '<a href="%s">%s</a>' % (href, txt)

QA = [
 ('What should I know before my first trip to India?',
  '<p>Five things matter most: apply for your e-Visa only on the official site, at least 4 days before you arrive; travel between '
  'October and March for Delhi, Agra, Jaipur, Rajasthan, Kerala and Goa (the UK FCDO says the monsoon season usually runs from June '
  'to October); start with Delhi, Agra and Jaipur plus one more region; avoid driving at night and in fog; and buy tickets only '
  'through official sites and counters.</p><p>Our ' + a('/india-tours/first-time-india-travel-guide/', 'first-time India travel guide') +
  ' turns this into a 10-step checklist, with every line sourced.</p>'),
 ('How do I get an Indian e-Visa without being overcharged?',
  '<p>Apply yourself on ' + a('https://indianvisaonline.gov.in/evisa/tvoa.html', 'indianvisaonline.gov.in') + '. The Government of '
  'India says no agent is needed and it charges no express or emergency fee. Your passport needs at least six months’ validity. '
  'Apply at least 4 days before arrival, carry the printed ETA showing “GRANTED”, and enter through one of the designated airports '
  'or seaports on the official list.</p><p><strong>' + VISA + '</strong> Step by step: our ' +
  a('/india-tours/india-e-visa-guide/', 'India e-Visa guide') + ' (checked 18 Oct 2026).</p>'),
 ('Do I need to fill in an arrival card?',
  '<p>Yes. Since 1 October 2025, foreign nationals and OCI card holders submit the e-Arrival card within 72 hours before arrival — '
  'on boi.gov.in, indianvisaonline.gov.in or the “Indian Visa Su-Swagatam” app. It is arrival information, not a visa '
  '(Embassy of India notice; checked 18 Oct 2026).</p>'),
 ('What do the US and UK governments advise about travel in India?',
  '<p>The US State Department rates India <strong>Level 2 – Exercise increased caution</strong> “due to crime and terrorism. Some '
  'areas have increased risk.” Its Level 4 areas are Jammu and Kashmir (except eastern Ladakh and Leh), the India–Pakistan border '
  'area, parts of central and east India, and Manipur (issued 16 Jun 2025, checked 23 Oct 2026).</p><p>The UK FCDO advises against '
  'all travel to Jammu and Kashmir, except air travel to and within Jammu city, and within 10 km (6 mi) of the India–Pakistan border '
  '(page updated 7 Oct 2026).</p><p><em>What this means for you:</em> read the current advice for your passport before you book, '
  'and ask your insurer whether you are covered in any area your government advises against. We plan around it with you.</p>'),
 ('How do I avoid scams and ticket touts?',
  '<p>The UK FCDO says: “Be cautious in tourist areas, where scammers, pickpockets and ticket touts target foreign nationals” and '
  '“avoid people at railway stations offering tickets and tours as you may be scammed.” It also notes that “app-based taxis like '
  'Uber and Ola are widely available, including in all airport terminal buildings” (updated 7 Oct 2026).</p><p><em>In practice:</em> '
  'buy monument and train tickets only on official sites or at official counters, and book with a registered company on written terms. '
  'Ours: ' + a('/certificates/', REG) + '. ' + BOOKING + '</p>'),
 ('Should I travel by car and driver or by train?',
  '<p>Both work. Foreign tourists can book reserved train seats under the Foreign Tourist Quota up to 365 days ahead, online with a '
  'passport number and an international card (general bookings open 60 days ahead). For touring door to door, a private car with an '
  'English-speaking driver is the simplest — ' + DRIVER + '.</p><p>The UK FCDO advises: “Avoid travelling at night and in fog as '
  'accidents are common due to low visibility”, so plan long drives in daylight. More: ' +
  a('/india-tours/private-driver-india/', 'private car and driver in India') + '.</p>'),
 ('Can I pay by card or UPI in India?',
  '<p>UPI options for visitors exist — check the official NPCI site (npci.org.in) for the current rules, and carry a card and some '
  'cash as well. For your tour with us, quotes are in US$: ' + BOOKING + '</p>'),
 ('Do I need vaccinations for India?',
  '<p>The official e-Visa site says travellers arriving from or through yellow-fever countries need a yellow-fever vaccination '
  'card or may face quarantine. For everything else, talk to your doctor or a travel clinic well before you go, and see CDC (US) '
  'or NHS Fit for Travel (UK). We do not give medical advice.</p>'),
 ('When does the monsoon arrive?',
  '<p>India Meteorological Department normals: the monsoon reaches Kerala around 1 June and New Delhi around 27 June, and withdraws '
  'from Delhi around 25 September. Weather varies year to year. Month by month, region by region: our ' +
  a('/india-tours/best-time-to-visit-india/', 'best time to visit India guide') + '.</p>'),
]
SRC = ('Sources: indianvisaonline.gov.in (e-Visa page, checked 18 Oct 2026); Embassy of India e-Arrival card notice; US Department of '
       'State India travel advisory (issued 16 Jun 2025); UK FCDO India travel advice (updated 7 Oct 2026); IRCTC Foreign Tourist Quota '
       '(High Commission of India); India Meteorological Department (PR 804). Checked 18–23 Oct 2026 — rules change, confirm before travel.')

CSS = (".szk{background:#F4EEDD;padding:56px 16px;font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;color:#0E1B14}"
       ".szk *{box-sizing:border-box}.szk p:empty,.szk>br,.szk-in>br{display:none}"
       ".szk-in{max-width:880px;margin:0 auto}.szk-eb{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#B8860B;margin:0 0 6px}"
       ".szk h2{margin:0 0 10px;color:#0E1B14}.szk-lead{color:#46524A;font-size:16px;line-height:1.6;margin:0 0 18px;max-width:64ch}"
       ".szk details{background:#fff;border:1px solid #E8DFC8;border-radius:14px;margin:0 0 10px;overflow:hidden}"
       ".szk details[open]{border-color:#E2C158;box-shadow:0 2px 10px rgba(14,27,20,.06)}"
       ".szk summary{cursor:pointer;list-style:none;padding:16px 48px 16px 18px;font-weight:800;font-size:16.5px;line-height:1.4;position:relative;min-height:48px}"
       ".szk summary::-webkit-details-marker{display:none}"
       ".szk summary::after{content:'+';position:absolute;right:16px;top:50%;transform:translateY(-50%);width:26px;height:26px;border-radius:50%;background:#0E1B14;color:#E2C158;font-size:18px;line-height:26px;text-align:center;font-weight:700}"
       ".szk details[open] summary::after{content:'−'}"
       ".szk summary:focus-visible{outline:2px solid #B8860B;outline-offset:-2px}"
       ".szk-a{padding:0 18px 14px;font-size:15.5px;line-height:1.65;color:#2E3A33}.szk-a p{margin:0 0 10px;color:#2E3A33}.szk-a strong{color:#0E1B14}"
       ".szk-a a{color:#8a6408;font-weight:700;text-decoration:underline}"
       ".szk-cta{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px;background:#0E1B14;color:#F4EEDD;border-radius:16px;padding:16px 18px;margin:18px 0 0}"
       ".szk-cta strong{color:#E2C158;font-size:16px}.szk-cta span{flex:1 1 260px;font-size:14.5px;line-height:1.5}"
       ".szk-cta a{display:inline-flex;align-items:center;min-height:44px;padding:10px 16px;border-radius:12px;font-weight:800;font-size:14px;text-decoration:none!important}"
       ".szk-wa{background:#25D366;color:#0b2414!important}.szk-em{background:#E2C158;color:#0E1B14!important}"
       ".szk-src{font-size:12px;line-height:1.5;color:#6B776E;margin:12px 0 0}"
       "@media(max-width:600px){.szk{padding:40px 16px}.szk summary{font-size:15.5px;padding:14px 46px 14px 14px}.szk-a{padding:0 14px 12px}.szk-cta a{flex:1 1 100%;justify-content:center}}")

def html():
    items = ''.join('<details><summary>%s</summary><div class="szk-a">%s</div></details>' % (q, ans) for q, ans in QA)
    body = ('<section class="szk" id="questions-from-international-travellers" style="scroll-margin-top:90px"><div class="szk-in">'
            '<span class="szk-eb">Before you go</span>'
            '<h2>Questions International Travellers Ask</h2>'
            '<p class="szk-lead">Practical answers for first-time visitors from the US, UK, Europe, Australia and Canada — visa, arrival card, '
            'government advice, scams, getting around, money and health. Every answer is dated and sourced to official sites.</p>'
            + items +
            '<div class="szk-cta"><span><strong>Another question?</strong> Ask our team in Himachal — a real person answers, in English.</span>'
            '<a class="szk-wa" href="' + WA + '" target="_blank" rel="noopener">WhatsApp +91 70874 88961</a>'
            '<a class="szk-em" href="mailto:info@suzutravels.com?subject=Question%20about%20travelling%20in%20India">Email us</a></div>'
            '<p class="szk-src">' + SRC + '</p></div></section>')
    return '<!--szt:faq-foreigners--><style>' + CSS + '</style>' + body + '<!--/szt:faq-foreigners-->'

out = html()
assert ' 100% ' not in re.sub('<[^>]+>', ' ', out)
# guards
assert '\n' not in out
assert out.count('<details>') == len(QA) == 9
assert BOOKING in out and REG in out and '+91 70874 88961' in out
low = re.sub('<[^>]+>', ' ', out).lower()
for bad in ('verified', 'vetted', 'background-check', 'guarantee', 'india is safe', 'cheapest', 'best price', 'government approved',
            'registered dmc', '24/7', 'visa on arrival', '₹', 'tip ', 'tipping', 'sim card', 'esim', 'malaria'):
    assert bad not in low, bad
for p in re.findall(r'US\$\s?([\d,]+)', out):
    assert int(p.replace(',', '')) in json.load(open(os.path.join(HERE, '../../../data/prices.json')))['allowed']
assert '<script' not in out
open(os.path.join(HERE, 'widget.html'), 'w').write(out)
print('ok', len(out), 'bytes')
