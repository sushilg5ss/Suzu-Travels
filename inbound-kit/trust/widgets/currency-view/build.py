#!/usr/bin/env python3
"""Builds trust/widgets/currency-view/widget.html (TRUST_BACKLOG row 3, pages 11412 + 11413).
Currency toggle US$ / GBP / EUR / AUD / CAD for the package cards (.lp-price b). Approximate only; quotes and payment stay in US$.
Rates: ECB reference rates via api.frankfurter.dev (free, keyless, CORS *), fetched on first click, 7 s timeout,
fallback = US$ only. No storage, no cookies, no third-party JS. Inline JS has no ampersand and no double slash."""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
PRICES = json.load(open(os.path.join(HERE, '..', '..', '..', 'data', 'prices.json')))['allowed']

CSS = (".szt-cur{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:4px 0 18px;padding:12px 14px;background:#F4EEDD;border:1px solid #E6DCC0;border-radius:14px;font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;max-width:100%;box-sizing:border-box}"
       ".szt-cur br{display:none}.szt-cur p{margin:0;display:contents}"
       ".szt-cur .szt-cl{font-size:13px;font-weight:800;color:#0E1B14;margin-right:4px}"
       ".szt-cur button{border:1px solid #DCD6C6;background:#fff;color:#0E1B14;font:800 13px/1 'Plus Jakarta Sans',system-ui,sans-serif;padding:9px 12px;border-radius:999px;cursor:pointer;min-height:36px}"
       ".szt-cur button[aria-pressed=true]{background:#0E1B14;color:#E2C158;border-color:#0E1B14}"
       ".szt-cur button:focus-visible{outline:2px solid #B8860B;outline-offset:2px}"
       ".szt-cur .szt-cn{font-style:normal;font-size:12px;line-height:1.5;color:#5B5440;flex-basis:100%}"
       ".lp-price .szt-cx{display:block;font-size:13px;color:#6B6248;font-weight:700;margin-top:2px}"
       "@media(max-width:520px){.szt-cur button{padding:8px 10px;font-size:12.5px}}")

JS = r"""(function(){var box=document.getElementById('sztCur');if(!box){return;}var S={USD:'US$',GBP:'£',EUR:'€',AUD:'A$',CAD:'C$'};var R=null,D='',busy=false;var note=box.querySelector('.szt-cn');var base=note.textContent;function each(fn){var b=document.querySelectorAll('.lp-price b');for(var i=0;i<b.length;i++){fn(b[i]);}}function press(c){var btn=box.querySelectorAll('button');for(var i=0;i<btn.length;i++){btn[i].setAttribute('aria-pressed',btn[i].getAttribute('data-c')===c?'true':'false');}}function show(c){press(c);each(function(b){var p=b.parentNode;var x=p.querySelector('.szt-cx');if(!x){x=document.createElement('span');x.className='szt-cx';p.appendChild(x);}var n=parseFloat((b.textContent||'').replace(/[^0-9.]/g,''));if(c==='USD'||!R||!R[c]||!n){x.textContent='';return;}x.textContent='≈ '+S[c]+Math.round(n*R[c]).toLocaleString('en-GB')+' (approx.)';});note.textContent=(c==='USD'||!D)?base:base+' Rates of '+D+'.';}function fail(){busy=false;press('USD');show('USD');note.textContent='Live rates unavailable right now. All quotes and payments are in US$.';}box.addEventListener('click',function(e){var t=e.target;var c=t.getAttribute?t.getAttribute('data-c'):null;if(!c||busy){return;}if(R||c==='USD'){show(c);return;}busy=true;note.textContent='Loading rates…';var done=false;var timer=setTimeout(function(){if(!done){done=true;fail();}},7000);var u='https:'+String.fromCharCode(47,47)+'api.frankfurter.dev/v1/latest?base=USD';fetch(u).then(function(r){return r.json();}).then(function(j){if(done){return;}done=true;clearTimeout(timer);if(!j||!j.rates){fail();return;}R=j.rates;D=j.date||'';busy=false;show(c);}).catch(function(){if(done){return;}done=true;clearTimeout(timer);fail();});});})();"""

def widget(page):
    btns = ''.join('<button type="button" data-c="%s" aria-pressed="%s">%s</button>' % (c, 'true' if c == 'USD' else 'false', l)
                   for c, l in [('USD', 'US$'), ('GBP', '£ GBP'), ('EUR', '€ EUR'), ('AUD', 'A$ AUD'), ('CAD', 'C$ CAD')])
    html = ('<!--szt:currency-view--><div class="szt-cur" id="sztCur" role="group" aria-label="Show approximate prices in your currency"><style>' + CSS +
            '</style><span class="szt-cl">Show prices in</span>' + btns +
            '<em class="szt-cn">Approximate conversions at the European Central Bank reference rate (via frankfurter.dev). Quotes and payment are in US$.</em>'
            '<script>' + JS + '</script></div><!--/szt:currency-view-->')
    js = html[html.find('<script>'):]
    assert '&' not in html and '//' not in js, 'ampersand or double slash'
    assert '\n' not in html
    return html

if __name__ == '__main__':
    w = widget(0)
    open(os.path.join(HERE, 'widget.html'), 'w').write(w)
    print('widget.html', len(w), 'bytes (same block on 11412 + 11413)')
    print('allowed prices', PRICES)
