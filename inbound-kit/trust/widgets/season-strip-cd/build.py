#!/usr/bin/env python3
"""TRUST_BACKLOG row 25 — season-strip-cd on /char-dham-yatra-for-nri/ (11413).
'When to go: the Char Dham year at a glance' — a 12-month strip for the yatra, inserted right before
<section class="lp-sec" id="trek-pony-palki-or-helicopter" (after the itinerary + itinerary-PDF card).
NO NEW FACTS: every line comes from 11413's own hand-built text (FAQ 'When is the best time for NRIs to do the
Char Dham Yatra?', the packing line 'nights are cold even in June', the registration FAQ). No dates for 2027
(announced by the temple committees in early 2027) -> 'confirm before travel'. No prices. Nothing stored, no fetch,
no third-party JS, no cookies. Inline JS: no ampersand, no double slash, no HTML in JS strings.
JS off: full 12-month strip with labels + notes; month buttons/summary hidden. Prefix .szt-sc (free on the site, checked 8 Nov 2026)."""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
FULL = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# c = temples closed for winter, p = opening / closing month, b = best window, m = monsoon landslides
CODE = 'cccpbbmmbbpc'
LBL = {'c': 'Temples closed', 'p': 'Opening / closing', 'b': 'Best window', 'm': 'Monsoon'}
SYM = {'c': '❄', 'p': '◐', 'b': '★', 'm': '☔'}
OPEN_TXT = 'The temples usually open in late April or May. The temple committees announce the exact dates early each year, and we plan your trip around them.'
CLOSE_TXT = 'The temples close in October or November for winter. Please confirm the closing dates before you book a late-season yatra.'
SUM = {
    'c': 'The four temples are closed for winter. They usually open in late April or May — a good time to start planning.',
    'p_open': OPEN_TXT,
    'p_close': CLOSE_TXT,
    'b_early': 'One of the two best windows (May–June). Nights are cold even in June, so pack warm layers.',
    'b_late': 'One of the two best windows (September–October). ' + CLOSE_TXT,
    'm': 'July and August bring monsoon landslides in the mountains. We suggest May–June or September–October instead.',
}
KEY = ['c', 'c', 'c', 'p_open', 'b_early', 'b_early', 'm', 'm', 'b_late', 'b_late', 'p_close', 'c']
WA = 'https://wa.me/917087488961?text='
WA_DEFAULT = 'Hello%20Suzu%20Travels%2C%20we%20would%20like%20help%20choosing%20the%20best%20month%20for%20our%20Char%20Dham%20Yatra.'
FAQ = '#char-dham-yatra-for-nris-frequently-aske'

CSS = (".szt-sc{font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;color:#0E1B14;padding-top:8px!important}"
       ".szt-sc *{box-sizing:border-box}.szt-sc p:empty,.szt-sc br{display:none}"
       ".szt-sc-card{background:#fff;border:1px solid #E8DFC8;border-radius:20px;box-shadow:0 10px 28px rgba(14,27,20,.07);overflow:hidden}"
       ".szt-sc-h{background:#0E1B14;color:#F4EEDD;padding:18px 20px}"
       ".szt-sc-k{display:block;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#E2C158;font-weight:800;margin-bottom:6px}"
       ".szt-sc-h b{display:block;font-size:21px;line-height:1.25;color:#fff;font-family:Sora,'Plus Jakarta Sans',sans-serif}"
       ".szt-sc-h span.szt-sc-s{display:block;font-size:14px;line-height:1.55;color:#DCD3BC;margin-top:6px;max-width:760px}"
       ".szt-sc-in{padding:16px 20px 18px}"
       ".szt-sc-grid{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:6px;margin:0 0 12px;padding:0;list-style:none}"
       ".szt-sc-grid li{margin:0;padding:0}"
       ".szt-sc-m{display:flex;flex-direction:column;align-items:center;justify-content:center;width:100%;min-height:74px;padding:8px 2px;border-radius:12px;border:2px solid transparent;font-family:inherit;line-height:1.15;text-align:center;cursor:default}"
       ".szt-sc-js .szt-sc-m{cursor:pointer}"
       ".szt-sc-m strong{font-size:13.5px;font-weight:800}.szt-sc-m i{font-style:normal;font-size:17px;margin:3px 0 2px}.szt-sc-m small{font-size:10.5px;font-weight:700;opacity:.9}"
       ".szt-sc .b{background:#E2C158;color:#3d2e00}.szt-sc .p{background:#C9D8E8;color:#1d3550}.szt-sc .m{background:#8F9C94;color:#fff}.szt-sc .c{background:#F4EEDD;color:#7a725c}"
       ".szt-sc-m[aria-pressed=true]{border-color:#0E1B14;box-shadow:0 4px 12px rgba(14,27,20,.18)}"
       ".szt-sc-m:focus-visible{outline:2px solid #B8860B;outline-offset:2px}"
       ".szt-sc-sum{background:#FBF8EF;border:1px dashed #D9CFB4;border-radius:14px;padding:12px 14px;margin:0 0 12px;font-size:14.5px;line-height:1.6;color:#3D4A40}.szt-sc-sum[hidden]{display:none}"
       ".szt-sc-sum strong{color:#0E1B14;display:block}"
       ".szt-sc-sum a{display:inline-flex;align-items:center;min-height:44px;margin-top:10px;padding:10px 16px;border-radius:12px;background:#E2C158;color:#0E1B14!important;font-weight:800;font-size:14px;text-decoration:none!important}"
       ".szt-sc-leg{display:flex;flex-wrap:wrap;gap:8px 16px;margin:0;padding:0;list-style:none;font-size:13px;color:#46524A}"
       ".szt-sc-leg li{display:flex;align-items:center;gap:6px;margin:0}.szt-sc-leg i{width:18px;height:18px;border-radius:5px;display:inline-block}"
       ".szt-sc-notes{margin:14px 0 0;padding:0;list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:8px 18px}"
       ".szt-sc-notes li{font-size:13.5px;line-height:1.5;color:#46524A;margin:0}.szt-sc-notes b{color:#0E1B14}"
       ".szt-sc-src{font-size:12px;line-height:1.5;color:#6B776E;margin:12px 0 0;max-width:90ch}.szt-sc-src a{color:#8a6400;font-weight:700}"
       ".szt-sc-vh{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}"
       "@media(max-width:900px){.szt-sc-grid{grid-template-columns:repeat(6,minmax(0,1fr))}}"
       "@media(max-width:700px){.szt-sc-notes{grid-template-columns:1fr}.szt-sc-grid{grid-template-columns:repeat(4,minmax(0,1fr))}"
       ".szt-sc-h,.szt-sc-in{padding-left:14px;padding-right:14px}.szt-sc-h b{font-size:19px}.szt-sc-m{min-height:66px}}")

BANNED = ['verified', 'government approved', 'registered DMC', '24/7', '24x7', '₹', 'guarantee', 'safest', 'perfectly safe', 'cheapest', 'most foreigners']

def html():
    tiles = ''.join('<li><button type="button" class="szt-sc-m %s" data-m="%d" aria-pressed="false" disabled aria-label="%s: %s">'
                    '<strong>%s</strong><i aria-hidden="true">%s</i><small>%s</small></button></li>'
                    % (c, i, FULL[i], LBL[c], MON[i], SYM[c], LBL[c]) for i, c in enumerate(CODE))
    grid = '<ul class="szt-sc-grid" aria-label="Char Dham Yatra months">' + tiles + '</ul>'
    summ = ('<div class="szt-sc-sum" id="szt-sc-sum" aria-live="polite" hidden></div>'
            '<a id="szt-sc-wa" hidden href="' + WA + WA_DEFAULT + '" target="_blank" rel="noopener" data-base="' + WA + '">Ask about my month on WhatsApp</a>')
    leg = ('<ul class="szt-sc-leg"><li><i class="b"></i>★ Best window</li><li><i class="p"></i>◐ Temples open or close this month</li>'
           '<li><i class="m"></i>☔ Monsoon landslides</li><li><i class="c"></i>❄ Temples closed for winter</li></ul>')
    notes = ('<ul class="szt-sc-notes">'
             '<li><b>Best windows:</b> May–June and September–October.</li>'
             '<li><b>Avoid:</b> July and August — monsoon landslides.</li>'
             '<li><b>Opening:</b> ' + OPEN_TXT + '</li>'
             '<li><b>Closing:</b> ' + CLOSE_TXT + '</li>'
             '<li><b>Packing:</b> nights are cold even in June — bring warm layers and a rain jacket.</li>'
             '<li><b>Registration:</b> every pilgrim registers on the official portal registrationandtouristcare.uk.gov.in — we complete it for our guests.</li>'
             '</ul>')
    data = json.dumps({'c': CODE, 'k': KEY, 's': SUM, 'f': FULL}, ensure_ascii=False, separators=(',', ':'))
    js = ('<script>(function(){var D=' + data + ';'
          'var R=document.getElementById("szt-sc");if(!R){return;}'
          'var sum=document.getElementById("szt-sc-sum"),wa=document.getElementById("szt-sc-wa"),bs=R.querySelectorAll(".szt-sc-m");'
          'if(!sum){return;}if(bs.length!==12){return;}R.classList.add("szt-sc-js");'
          'function pick(m){for(var i=0;i<bs.length;i++){bs[i].setAttribute("aria-pressed",String(i===m));}'
          'sum.textContent="";var hd=document.createElement("strong");hd.textContent=D.f[m]+" for the Char Dham Yatra";sum.appendChild(hd);'
          'sum.appendChild(document.createTextNode(D.s[D.k[m]]));'
          'if(wa){var t="Hello Suzu Travels, we are thinking of a Char Dham Yatra in "+D.f[m]+". Could you suggest the best dates and a yatra for our family?";'
          'wa.href=wa.getAttribute("data-base")+encodeURIComponent(t);wa.textContent="Ask about a "+D.f[m]+" yatra on WhatsApp";sum.appendChild(document.createElement("br"));sum.appendChild(wa);wa.hidden=false;}}'
          'for(var j=0;j<bs.length;j++){bs[j].disabled=false;bs[j].addEventListener("click",function(){pick(parseInt(this.getAttribute("data-m"),10));});}'
          'sum.hidden=false;pick(new Date().getMonth());})();</script>')
    return ('<!--szt:season-strip-cd--><section class="lp-sec alt szt-sc" id="szt-sc" style="scroll-margin-top:90px"><style>' + CSS + '</style>'
            '<div class="lp-wrap"><div class="szt-sc-card"><div class="szt-sc-h"><span class="szt-sc-k">Planning around school holidays?</span>'
            '<b>When to go: the Char Dham year at a glance</b>'
            '<span class="szt-sc-s">The four temples open in late April or May and close in October or November. Tap a month to see what it means for your family’s yatra.</span></div>'
            '<div class="szt-sc-in">' + grid + summ + leg + notes +
            '<p class="szt-sc-src">From this page’s own guidance (see <a href="' + FAQ + '">the FAQ below</a>). Opening and closing dates change every year '
            'and are announced by the temple committees — please confirm before travel.</p>' + js +
            '</div></div></div></section><!--/szt:season-strip-cd-->')

if __name__ == '__main__':
    h = html()
    assert '\n' not in h
    js = h[h.find('<script>'):h.find('</script>')]
    assert '&' not in js and '//' not in js, 'JS must not contain & or //'
    assert not any('<' in lit for lit in re.findall(r'"(?:[^"\\]|\\.)*"', js)), 'no HTML tags inside JS strings'
    assert '&' not in h.replace('&amp;', ''), 'raw ampersand'
    assert '$' not in h, 'no prices in this widget'
    low = h.lower()
    for b in BANNED:
        assert b.lower() not in low, b
    open(os.path.join(HERE, 'widget.html'), 'w').write(h)
    print('widget.html', len(h))
