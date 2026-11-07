#!/usr/bin/env python3
"""before-you-fly (TRUST_BACKLOG row 24) — 'Before you fly' checklist card on /golden-triangle-tour/ (11412) and
/char-dham-yatra-for-nri/ (11413), linking the live practical guides in /india-tours/.
Text = each guide's own label + blurb from live.json (no new facts) + the README §1 visa line. Tick boxes are plain
checkboxes; JS only counts them (nothing stored, no fetch, no 3rd-party JS, no cookies). JS has no '&' and no '//'.
Prefix .szy (free on the site, checked 7 Nov 2026). Placed right after <!--/szt:call-time-->."""
import os, json
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
LIVE = json.load(open(os.path.join(KIT, 'live.json')))
SLUGS = ['india-e-visa-guide', 'india-travel-insurance', 'sim-card-india-tourist',
         'upi-and-money-in-india-for-tourists', 'trains-vs-flights-in-india', 'first-time-india-travel-guide']
PAGES = {
    '11412': dict(trip='Golden Triangle tour', k='Before you fly to Delhi'),
    '11413': dict(trip='Char Dham Yatra', k='Before you fly for the yatra'),
}

CSS = (".szy{font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;margin:0;padding:30px 16px;background:#F4EEDD}"
       ".szy *{box-sizing:border-box}.szy p:empty,.szy br{display:none}"
       ".szy-c{max-width:1100px;margin:0 auto;background:#fff;border:1px solid #E6DCC0;border-radius:20px;box-shadow:0 10px 28px rgba(14,27,20,.08);padding:24px}"
       ".szy-k{display:block;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#B8860B;font-weight:800;margin-bottom:6px}"
       ".szy-h{display:block;font-size:22px;line-height:1.25;color:#0E1B14;font-weight:800;font-family:Sora,'Plus Jakarta Sans',sans-serif}"
       ".szy-s{display:block;font-size:14.5px;line-height:1.55;color:#4A5249;margin:6px 0 14px}"
       ".szy-l{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}"
       ".szy-l li{margin:0;padding:0;list-style:none}"
       ".szy-i{display:flex;gap:12px;align-items:flex-start;padding:12px 14px;border:1px solid #E6DCC0;border-radius:14px;background:#FBF8EF;height:100%}"
       ".szy-i input{flex:0 0 auto;width:20px;height:20px;margin:2px 0 0;accent-color:#B8860B;cursor:pointer}"
       ".szy-i>div{min-width:0}.szy-i label{cursor:pointer;display:block}"
       ".szy-i b{display:block;font-size:15px;color:#0E1B14;line-height:1.3}"
       ".szy-i span{display:block;font-size:13.5px;line-height:1.5;color:#4A5249;margin-top:2px}"
       ".szy-i a{display:inline-block;margin-top:6px;font-size:13.5px;font-weight:800;color:#8A6408!important;text-decoration:underline}"
       ".szy-i:has(input:checked){background:#0E1B14;border-color:#0E1B14}"
       ".szy-i:has(input:checked) b{color:#E2C158;text-decoration:line-through}"
       ".szy-i:has(input:checked) span{color:#DCD3BC}.szy-i:has(input:checked) a{color:#E2C158!important}"
       ".szy-f{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;margin-top:14px;font-size:13.5px;color:#4A5249}"
       ".szy-n{font-weight:800;color:#0E1B14}"
       ".szy .szy-r{font-family:inherit!important;border:1px solid #B8860B!important;background:transparent!important;color:#8A6408!important;border-radius:10px!important;padding:8px 12px!important;font-weight:800;cursor:pointer;font-size:13px!important;box-shadow:none!important;text-transform:none!important;min-height:0;width:auto}"
       ".szy-w{font-weight:800;color:#8A6408!important}"
       ".szy-d{font-size:12.5px;line-height:1.55;color:#6B6F66;margin:12px 0 0}"
       ".szy-nojs .szy-js{display:none!important}"
       "@media(max-width:720px){.szy-l{grid-template-columns:minmax(0,1fr)}}"
       "@media(max-width:560px){.szy{padding:24px 12px}.szy-c{padding:18px 14px}.szy-h{font-size:19px}}")

JS = ('(function(){var R=document.getElementById("szy");if(!R){return;}R.className=R.className.replace(" szy-nojs","");'
      'var B=R.querySelectorAll("input[type=checkbox]"),N=document.getElementById("szy-n"),X=document.getElementById("szy-r");'
      'function u(){var c=0,i;for(i=0;i<B.length;i++){if(B[i].checked){c++;}}'
      'if(N){N.textContent=(c===B.length)?"All "+B.length+" done — you are ready to plan.":c+" of "+B.length+" done";}}'
      'var i;for(i=0;i<B.length;i++){B[i].addEventListener("change",u);}'
      'if(X){X.addEventListener("click",function(){var j;for(j=0;j<B.length;j++){B[j].checked=false;}u();});}u();})();')

def build(pid):
    p = PAGES[pid]
    items = []
    for n, s in enumerate(SLUGS, 1):
        v = dict(LIVE[s]); v['label'] = v['label'].replace('&', '&amp;')
        reason = v['blurb'].replace('&', '&amp;')
        if s == 'india-e-visa-guide':
            reason += '. Apply yourself on the official site; we are not a visa agency.'
        items.append('<li><div class="szy-i"><input type="checkbox" id="szy-' + str(n) + '"><div><label for="szy-' + str(n) + '"><b>' +
                     v['label'] + '</b><span>' + reason + '</span></label><a href="https://suzutravels.com' + v['path'] +
                     '" aria-label="Read the guide: ' + v['label'] + '">Read the guide</a></div></div></li>')
    wa = 'https://wa.me/917087488961?text=' + quote('Hello Suzu Travels, I have a question before I book the ' + p['trip'] + ':')
    html = ('<!--szt:before-you-fly--><section class="szy szy-nojs" id="szy" aria-label="Before you fly: checklist">'
            '<style>' + CSS + '</style><div class="szy-c"><span class="szy-k">' + p['k'] + '</span>'
            '<span class="szy-h">Your before-you-fly checklist</span>'
            '<span class="szy-s">Six things foreign visitors sort out before an India trip. Each links to our free guide; tick them off as you go.</span>'
            '<ul class="szy-l">' + ''.join(items) + '</ul>'
            '<div class="szy-f"><span class="szy-n szy-js" id="szy-n" aria-live="polite"></span>'
            '<button type="button" class="szy-r szy-js" id="szy-r">Clear ticks</button>'
            '<a class="szy-w" href="' + wa + '" target="_blank" rel="noopener">A question before you book? WhatsApp +91 70874 88961</a></div>'
            '<p class="szy-d">Information only — rules change, so confirm visa, insurance and money rules on the official sites before you travel. '
            'Your ticks stay on this screen only: nothing is saved or sent.</p>'
            '<script>' + JS + '</script></div></section><!--/szt:before-you-fly-->')
    return html

if __name__ == '__main__':
    assert '&' not in JS and '//' not in JS, 'JS must not contain & or //'
    for pid in PAGES:
        body = build(pid).replace('\n', ' ')
        low = body.lower()
        for bad in ['verified', '24/7', '₹', 'cheapest', 'guarantee', 'government approved', 'dmc', 'online now', 'seats left', 'us$']:
            assert bad not in low, (pid, bad)
        assert body.count('<!--szt:before-you-fly-->') == 1 and body.count('indianvisaonline.gov.in') >= 1 and 'look-alike' in body
        out = os.path.join(HERE, 'widget-' + pid + '.html')
        open(out, 'w').write(body)
        print(out, len(body))
