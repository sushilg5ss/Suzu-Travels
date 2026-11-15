#!/usr/bin/env python3
"""check-us (TRUST_BACKLOG row 31) — 'How to check us before you pay' strip on the hub /india-tours/ (11411).
Four checks taken from the live guide /india-tours/how-to-choose-a-travel-agency-in-india/ (its own checklist headings,
src/pages/how-to-choose-a-travel-agency-in-india.json section 'checklist'), each answered with OUR proof — text copied from the
same guide's 'how-we-do-it' cards (registration, office, written plan, payment) and the exact README §1 lines. No new facts,
no prices, no reviews, no JS, nothing stored. Proof links: /certificates/, Google Maps search of the office address, WhatsApp,
the two pinned itinerary PDFs (same URLs as pdf-hub-cards), #booking-protected on the hub, and the full guide.
Prefix .szq (unused on 11411 — 15 Nov 2026 curl). Placed right after <!--/szt:booking-protected--> on 11411."""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
LIVE = json.load(open(os.path.join(KIT, 'live.json')))
GUIDE = json.load(open(os.path.join(KIT, 'src', 'pages', 'how-to-choose-a-travel-agency-in-india.json')))
CHECK = {i[0]: i[1] for i in next(s for s in GUIDE['sections'] if s['id'] == 'checklist')['items']}
OURS = {i[0]: i[1] for i in next(s for s in GUIDE['sections'] if s['id'] == 'how-we-do-it')['items']}
REG = 'HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022'
BOOK = ('20% deposit locks your dates and price; full refund if cancelled within 48 hours of paying; balance before the trip; '
        'pay by card via Razorpay (international cards accepted) or PayPal.')
G = 'https://suzutravels.com' + LIVE['how-to-choose-a-travel-agency-in-india']['path']
PDF_GT = 'https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@ccf7eb01e4b8eb964380cc492eabace05375e4e1/inbound-kit/trust/widgets/itinerary-pdf/golden-triangle-6-day-itinerary-suzu-travels.pdf'
PDF_CD = 'https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@bc61aa787f9c445478f091cd6498207ef49a886b/inbound-kit/trust/widgets/itinerary-pdf/char-dham-yatra-11-day-itinerary-suzu-travels.pdf'
MAP = 'https://www.google.com/maps/search/?api=1&amp;query=NH+103+Kulahru+Ghumarwin+Bilaspur+Himachal+Pradesh'
WA = 'https://wa.me/917087488961?text=Hello%20Suzu%20Travels%2C%20please%20send%20me%20a%20copy%20of%20your%20registration%20certificate.'

ROWS = [
    ('Ask for the registration — and check it',
     REG + '. Our registration is with the state of Himachal Pradesh under its Act; we do not claim Ministry of Tourism recognition.',
     [('https://suzutravels.com/certificates/', 'See the certificate'), (WA, 'Ask for a copy on WhatsApp')]),
    ('Find the office on a map',
     OURS['An office you can find'],
     [(MAP, 'Open the address in Google Maps')]),
    ('Get a written, day-by-day plan',
     OURS['Everything in writing'],
     [(PDF_GT, 'Sample: Golden Triangle 6 days (PDF)'), (PDF_CD, 'Sample: Char Dham 11 days (PDF)')]),
    ('Know the deposit and the refund rule before you pay',
     BOOK,
     [('#booking-protected', 'How your booking is protected')]),
]
for q, _, _ in ROWS:
    assert q in CHECK, q  # headings must stay the guide's own

CSS = (".szq{font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;margin:0;padding:30px 16px;background:#F4EEDD;scroll-margin-top:90px}"
       ".szq *{box-sizing:border-box}.szq p:empty,.szq br{display:none}"
       ".szq-c{max-width:1100px;margin:0 auto;background:#fff;border:1px solid #E6DCC0;border-radius:20px;box-shadow:0 10px 28px rgba(14,27,20,.08);overflow:hidden}"
       ".szq-h{background:#0E1B14;color:#F4EEDD;padding:20px 22px}"
       ".szq-k{display:block;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#E2C158;font-weight:800;margin-bottom:6px}"
       ".szq-t{display:block;font-size:22px;line-height:1.25;color:#fff;font-weight:800;font-family:Sora,'Plus Jakarta Sans',sans-serif}"
       ".szq-s{display:block;font-size:14.5px;line-height:1.55;color:#DCD3BC;margin-top:6px}"
       ".szq-l{list-style:none;margin:0;padding:18px 22px 6px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;counter-reset:q}"
       ".szq-l li{margin:0;list-style:none;background:#FBF8EF;border:1px solid #E6DCC0;border-radius:16px;padding:14px 16px;counter-increment:q;min-width:0}"
       ".szq-q{display:flex;gap:10px;align-items:flex-start;font-size:15px;line-height:1.35;color:#0E1B14;font-weight:800}"
       ".szq-q:before{content:counter(q);flex:0 0 26px;display:flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;background:#0E1B14;color:#E2C158;font-size:13px}"
       ".szq-a{display:block;font-size:13.5px;line-height:1.55;color:#4A5249;margin:8px 0 0}"
       ".szq-a em{font-style:normal;font-weight:800;color:#8A6408}"
       ".szq-p{display:flex;flex-wrap:wrap;gap:6px 14px;margin-top:8px}"
       ".szq-p a{font-size:13.5px;font-weight:800;color:#8A6408!important;text-decoration:underline;overflow-wrap:anywhere}"
       ".szq-f{display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center;padding:12px 22px 20px;font-size:14px;line-height:1.5;color:#4A5249}"
       ".szq-f a{display:inline-block;padding:10px 16px;border-radius:999px;background:#0E1B14;color:#E2C158!important;font-weight:800;text-decoration:none!important}"
       "@media(max-width:760px){.szq{padding:24px 12px}.szq-h{padding:18px 16px}.szq-t{font-size:19px}.szq-l{grid-template-columns:minmax(0,1fr);padding:14px 14px 4px}.szq-f{padding:10px 14px 18px}}")

def esc(s):
    return s.replace('&', '&amp;').replace('&amp;amp;', '&amp;')

def row(q, a, links):
    p = ''.join('<a href="' + h + '"' + ('' if h.startswith('#') or 'suzutravels.com' in h else ' target="_blank" rel="noopener"') +
                '>' + esc(t) + '</a>' for h, t in links)
    return '<li><span class="szq-q">' + esc(q) + '</span><span class="szq-a"><em>Us:</em> ' + esc(a) + '</span><span class="szq-p">' + p + '</span></li>'

def build():
    return ('<!--szt:check-us--><section class="szq" id="check-us" aria-label="How to check us before you pay">'
            '<style>' + CSS + '</style><div class="szq-c"><div class="szq-h"><span class="szq-k">Check us before you pay</span>'
            '<span class="szq-t">Four checks to run on any India travel company — and our answers</span>'
            '<span class="szq-s">From our guide to choosing a travel agency. Run the same checks on every company you compare, us included.</span></div>'
            '<ol class="szq-l">' + ''.join(row(*r) for r in ROWS) + '</ol>'
            '<div class="szq-f"><span>The full 8-point checklist and the red flags to watch for:</span>'
            '<a href="' + G + '">Read: How to check an Indian tour company</a></div>'
            '</div></section><!--/szt:check-us-->')

if __name__ == '__main__':
    body = build().replace('\n', ' ')
    low = body.lower()
    for bad in ['verified', '24/7', '₹', 'cheapest', 'guarantee', 'government approved', 'registered dmc', 'online now', 'seats left', 'us$', '<script', '//"']:
        assert bad not in low, bad
    assert '&' not in body.replace('&amp;', ''), 'raw ampersand'
    assert body.count('<!--szt:check-us-->') == 1 and REG in body and BOOK in body
    open(os.path.join(HERE, 'widget.html'), 'w').write(body)
    print(len(body))
