#!/usr/bin/env python3
"""cd-guides (TRUST_BACKLOG row 30) — 'Plan the rest of your trip' guide cards on /char-dham-yatra-for-nri/ (11413).
Reuses the gt-guides (row 29) build with a page switch: Char Dham / pilgrim add-ons instead of Golden Triangle ones.
11413 links only the 7 before-you-fly guides + private-driver (curl 12 Nov 2026) — none of these pilgrim-journey pages.
Text = each page's own label + blurb from live.json only (no new facts, no prices). Plus one trust line: the
agency-checking guide + /certificates/ with the exact registration line. No JS at all (nothing stored, no fetch).
Prefix .szw (same as gt-guides; the two never share a page — gt on 11412, cd on 11413). Placed right after
<!--/szt:itinerary-pdf--> on 11413 (after the 11-day Char Dham itinerary + its PDF card), mirroring gt-guides on 11412."""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
LIVE = json.load(open(os.path.join(KIT, 'live.json')))
GROUPS = [
    ('More of sacred India', ['varanasi-trip-guide', 'kumbh-mela-tour', 'rishikesh-yoga-retreat-guide']),
    ('Add to your yatra', ['amritsar-golden-temple-tour', 'best-time-to-visit-himachal']),
]
TRUST = 'how-to-choose-a-travel-agency-in-india'
REG = 'HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022'
KICKER = 'Plan the rest of your trip'
TITLE = 'Free guides for your Char Dham yatra'
SUB = 'Practical plans for your pilgrimage and the sacred places around it. Free to read — no sign-up.'

CSS = (".szw{font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;margin:0;padding:30px 16px;background:#F4EEDD}"
       ".szw *{box-sizing:border-box}.szw p:empty,.szw br{display:none}"
       ".szw-c{max-width:1100px;margin:0 auto;background:#fff;border:1px solid #E6DCC0;border-radius:20px;box-shadow:0 10px 28px rgba(14,27,20,.08);padding:24px}"
       ".szw-k{display:block;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#B8860B;font-weight:800;margin-bottom:6px}"
       ".szw-h{display:block;font-size:22px;line-height:1.25;color:#0E1B14;font-weight:800;font-family:Sora,'Plus Jakarta Sans',sans-serif}"
       ".szw-s{display:block;font-size:14.5px;line-height:1.55;color:#4A5249;margin:6px 0 4px}"
       ".szw-g{display:block;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:#0E1B14;font-weight:800;margin:16px 0 8px}"
       ".szw-l{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}"
       ".szw-l li{margin:0;padding:0;list-style:none}"
       ".szw-a{display:flex;flex-direction:column;height:100%;padding:12px 14px;border:1px solid #E6DCC0;border-radius:14px;background:#FBF8EF;text-decoration:none!important;transition:border-color .15s,box-shadow .15s}"
       ".szw-a:hover,.szw-a:focus{border-color:#B8860B;box-shadow:0 6px 16px rgba(14,27,20,.10)}"
       ".szw-a b{display:block;font-size:15px;color:#0E1B14;line-height:1.3}"
       ".szw-a span{display:block;font-size:13.5px;line-height:1.5;color:#4A5249;margin-top:4px;flex:1 1 auto}"
       ".szw-a i{display:block;font-style:normal;margin-top:8px;font-size:13.5px;font-weight:800;color:#8A6408;text-decoration:underline}"
       ".szw-t{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;margin-top:16px;padding:12px 14px;border-radius:14px;background:#0E1B14;color:#DCD3BC;font-size:13.5px;line-height:1.5}"
       ".szw-t b{color:#E2C158}.szw-t a{color:#E2C158!important;font-weight:800;text-decoration:underline}"
       "@media(max-width:980px){.szw-l{grid-template-columns:repeat(2,minmax(0,1fr))}}"
       "@media(max-width:560px){.szw{padding:24px 12px}.szw-c{padding:18px 14px}.szw-h{font-size:19px}.szw-l{grid-template-columns:minmax(0,1fr)}}")

def esc(s):
    return s.replace('&', '&amp;')

def card(s):
    v = LIVE[s]
    return ('<li><a class="szw-a" href="https://suzutravels.com' + v['path'] + '"><b>' + esc(v['label']) + '</b><span>' +
            esc(v['blurb']) + '</span><i>Read the guide</i></a></li>')

def build():
    g = ''.join('<span class="szw-g">' + esc(t) + '</span><ul class="szw-l">' + ''.join(card(s) for s in sl) + '</ul>' for t, sl in GROUPS)
    t = LIVE[TRUST]
    return ('<!--szt:cd-guides--><section class="szw" id="szw" aria-label="Char Dham planning guides">'
            '<style>' + CSS + '</style><div class="szw-c"><span class="szw-k">' + esc(KICKER) + '</span>'
            '<span class="szw-h">' + esc(TITLE) + '</span>'
            '<span class="szw-s">' + esc(SUB) + '</span>'
            + g +
            '<div class="szw-t"><b>Comparing companies?</b><span>' + esc(t['blurb']) + ' — check us the same way.</span>'
            '<a href="https://suzutravels.com' + t['path'] + '">Read: ' + esc(t['label']) + '</a>'
            '<a href="https://suzutravels.com/certificates/">' + REG + '</a></div>'
            '</div></section><!--/szt:cd-guides-->')

if __name__ == '__main__':
    body = build().replace('\n', ' ')
    low = body.lower()
    for bad in ['verified', '24/7', '₹', 'cheapest', 'guarantee', 'government approved', 'dmc', 'online now', 'seats left', 'us$', '<script']:
        assert bad not in low, bad
    assert '&' not in body.replace('&amp;', ''), 'raw ampersand'
    assert body.count('<!--szt:cd-guides-->') == 1 and REG in body
    out = os.path.join(HERE, 'widget.html')
    open(out, 'w').write(body)
    print(out, len(body))
