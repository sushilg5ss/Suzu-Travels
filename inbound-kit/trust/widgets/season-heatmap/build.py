#!/usr/bin/env python3
"""TRUST_BACKLOG row 6 — season-heatmap (hub 11411, right after the hand-built 'Best Time to Visit North India' table).
Month x region grid. Data ONLY from fact packs (research/pages/*.md, as-of in SRC) — the season table in
best-places-to-visit-in-india.md + kerala-tour.md facts 11/12 + goa-holiday.md facts 1/4/5/7 + rishikesh pack fact 10.
Months not covered by a source are 'possible — ask us' (never 'avoid' without a source). Kashmir: no season colours, only the
dated advisory line. Inline JS: no ampersand, no double slash; works with JS off (full grid, toolbar hidden)."""
import os, json

B, S, M, O = 'b', 's', 'm', 'o'   # best / snow season / monsoon / possible — ask us
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
FULL = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def row(best=(), snow=(), mon=()):
    return ''.join(B if m in best else S if m in snow else M if m in mon else O for m in range(1, 13))

ROWS = [
 ('Delhi · Agra · Jaipur', 'Golden Triangle plains', row(best=(10, 11, 12, 1, 2, 3), mon=(7, 8, 9)),
  'Monsoon usually reaches Delhi around 27 June (IMD normal). The Taj Mahal is closed on Fridays.'),
 ('Varanasi', 'Ganga ghats', row(best=(10, 11, 12, 1, 2, 3), mon=(7, 8, 9)),
  'Dev Deepavali, 15 days after Diwali, lights the ghats with thousands of lamps.'),
 ('Amritsar', 'Golden Temple', row(best=(10, 11, 12, 1, 2, 3)),
  'Our planning experience — we found no official season for Amritsar.'),
 ('Rishikesh · Haridwar', 'Yoga and the Ganga', row(best=(10, 11, 12, 1, 2, 3, 4), mon=(7, 8)),
  'International Yoga Festival each February–March. Rafting usually pauses in July and August.'),
 ('Shimla · Dharamshala', 'Himachal hills', row(best=(3, 4, 5, 6, 9, 10, 11), snow=(12, 1, 2), mon=(7, 8)),
  'Winter snowfall is common in Dharamshala. Our home region — our own team plans it.'),
 ('Manali', 'Himachal high valley', row(best=(3, 4, 5, 6, 9, 10, 11), snow=(12, 1, 2), mon=(7, 8)),
  'Rohtang Pass is closed by snow from late November and reopens by May (HP Tourism). Atal Tunnel to Lahaul is open year-round.'),
 ('Ladakh (Leh)', 'High-altitude desert', row(best=(6, 7, 8, 9)),
  'Summer trip. No official month source: roads from Manali and Srinagar are seasonal — confirm before you book.'),
 ('Kerala', 'Backwaters and tea hills', row(best=(10, 11, 12, 1, 2), mon=(6, 7, 8)),
  'Kerala Tourism: November–February is peak season, October–February is best for houseboats, June–August is monsoon; March–May is hot and humid.'),
 ('Goa', 'Beaches', row(best=(11, 12, 1, 2, 3), mon=(6, 7, 8, 9)),
  'Foreign visitors come in winter (Govt of Goa). No sea swimming in the monsoon — follow the lifeguard flags.'),
]
KASHMIR = ('The UK FCDO advises against all travel to Jammu and Kashmir except Jammu city, and the US State Department says '
           '‘Do not travel’ to J&amp;K except eastern Ladakh and Leh (advice checked 19 Oct 2026). Check the latest before you book.')
SRC = ('Sources: IMD monsoon normals; tajmahal.gov.in; Incredible India (Varanasi, Dharamshala, Leh); HP Tourism (Manali); '
       'Kerala Tourism; Govt of Goa and Goa Tourism; UK FCDO (updated 7 Oct 2026); US State Department. Checked 17–20 Oct 2026. '
       'Weather varies year to year — confirm before travel.')
LBL = {B: 'Best', S: 'Snow season', M: 'Monsoon', O: 'Possible — ask us'}
WA = 'https://wa.me/917087488961?text='
WA_DEFAULT = 'Hello%20Suzu%20Travels%2C%20I%20would%20like%20help%20choosing%20the%20best%20months%20for%20my%20India%20trip.'

CSS = (".szt-sh{font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;color:#0E1B14}"
       ".szt-sh *{box-sizing:border-box}.szt-sh p:empty,.szt-sh br{display:none}"
       ".szt-sh h2{margin:4px 0 8px}.szt-sh-lead{max-width:64ch;color:#46524A;font-size:16px;line-height:1.6;margin:0 0 16px}"
       ".szt-sh-bar{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 12px}.szt-sh-bar[hidden]{display:none}"
       ".szt-sh-bar button{min-width:44px;min-height:40px;padding:8px 10px;border-radius:10px;border:1px solid #DCD6C6;background:#fff;color:#0E1B14;font-family:inherit;font-weight:700;font-size:13px;line-height:1;cursor:pointer}"
       ".szt-sh-bar button[aria-pressed=true]{background:#0E1B14;color:#E2C158;border-color:#0E1B14}"
       ".szt-sh-bar button:focus-visible{outline:2px solid #B8860B;outline-offset:2px}"
       ".szt-sh-sum{background:#0E1B14;color:#F4EEDD;border-radius:16px;padding:14px 16px;margin:0 0 14px;font-size:14.5px;line-height:1.6}.szt-sh-sum[hidden]{display:none}"
       ".szt-sh-sum strong{color:#E2C158}.szt-sh-sum b{color:#fff}.szt-sh-sum div{margin-top:4px}"
       ".szt-sh-sum a{display:inline-flex;align-items:center;min-height:44px;margin-top:10px;padding:10px 16px;border-radius:12px;background:#25D366;color:#0b2414!important;font-weight:800;font-size:14px;text-decoration:none!important}"
       ".szt-sh-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch;border:1px solid #E8DFC8;border-radius:16px;background:#fff;max-width:100%}"
       ".szt-sh table{border-collapse:separate;border-spacing:3px;width:100%;min-width:640px;margin:0;font-size:13px}"
       ".szt-sh th,.szt-sh td{border:0;padding:0;text-align:center;vertical-align:middle}.szt-sh thead th{background:none}"
       ".szt-sh thead th{font-size:11.5px;font-weight:800;color:#56645A;padding:6px 0;text-transform:uppercase;letter-spacing:.02em}"
       ".szt-sh tbody th{text-align:left;padding:6px 8px 6px 6px;min-width:150px;position:sticky;left:0;background:#fff;z-index:1;font-size:13.5px;line-height:1.25}"
       ".szt-sh tbody th small{display:block;font-weight:500;color:#6B776E;font-size:11.5px}"
       ".szt-sh tbody td{height:30px;border-radius:7px;font-size:11px;font-weight:800;line-height:30px}"
       ".szt-sh td.b,.szt-sh-leg .b{background:#E2C158;color:#3d2e00}.szt-sh td.s,.szt-sh-leg .s{background:#C9D8E8;color:#1d3550}.szt-sh td.m,.szt-sh-leg .m{background:#8F9C94;color:#fff}.szt-sh td.o,.szt-sh-leg .o{background:#F4EEDD;color:#8a826c}"
       ".szt-sh td.on,.szt-sh thead th.on{box-shadow:inset 0 0 0 2px #0E1B14}.szt-sh thead th.on{border-radius:7px;color:#0E1B14}"
       ".szt-sh-k td{padding:8px 6px!important;text-align:left!important;font-size:12.5px;line-height:1.45;color:#46524A;background:#FBF8EF!important;border-radius:8px}"
       ".szt-sh-leg{display:flex;flex-wrap:wrap;gap:8px 16px;margin:12px 0 0;padding:0;list-style:none;font-size:13px;color:#46524A}"
       ".szt-sh-leg li{display:flex;align-items:center;gap:6px}.szt-sh-leg i{width:18px;height:18px;border-radius:5px;display:inline-block}"
       ".szt-sh-notes{margin:14px 0 0;padding:0;list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:8px 18px}"
       ".szt-sh-notes li{font-size:13.5px;line-height:1.5;color:#46524A}.szt-sh-notes b{color:#0E1B14}"
       ".szt-sh-src{font-size:12px;line-height:1.5;color:#6B776E;margin:12px 0 0;max-width:90ch}"
       ".szt-sh-vh{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}"
       "@media(max-width:700px){.szt-sh-notes{grid-template-columns:1fr}.szt-sh tbody th{min-width:118px;font-size:12.5px}.szt-sh table{min-width:560px}.szt-sh-bar button{min-width:0;flex:1 0 14%;padding:8px 4px}}")

def cell(c, m):
    return '<td class="%s" data-m="%d" title="%s">%s</td>' % (c, m, LBL[c], {B: '\u2605', S: '\u2744', M: '\u2614', O: '\u00b7'}[c])

def html():
    head = '<thead><tr><th scope="col"><span class="szt-sh-vh">Region</span></th>' + ''.join(
        '<th scope="col" data-m="%d">%s</th>' % (i, m) for i, m in enumerate(MON)) + '</tr></thead>'
    body = ''
    for name, sub, r, _ in ROWS:
        body += '<tr data-n="%s"><th scope="row">%s<small>%s</small></th>%s</tr>' % (name, name, sub, ''.join(cell(c, i) for i, c in enumerate(r)))
    body += ('<tr class="szt-sh-k"><th scope="row">Kashmir<small>Srinagar · Gulmarg</small></th><td colspan="12">No colours — see travel advice below.</td></tr>')
    bar = '<div class="szt-sh-bar" role="group" aria-label="Pick your travel month" hidden>' + ''.join(
        '<button type="button" data-m="%d" aria-pressed="false" aria-label="%s">%s</button>' % (i, FULL[i], m) for i, m in enumerate(MON)) + '</div>'
    summ = ('<div class="szt-sh-sum" id="szt-sh-sum" aria-live="polite" hidden></div>'
            '<a id="szt-sh-wa" hidden href="' + WA + WA_DEFAULT + '" target="_blank" rel="noopener" data-base="' + WA + '">Plan my trip on WhatsApp</a>')
    leg = ('<ul class="szt-sh-leg"><li><i class="b"></i>★ Best months</li><li><i class="s"></i>❄ Snow season (Himalaya)</li>'
           '<li><i class="m"></i>☔ Monsoon rain</li><li><i class="o"></i>Possible — ask us</li></ul>')
    notes = '<ul class="szt-sh-notes">' + ''.join('<li><b>%s:</b> %s</li>' % (n, t) for n, _, _, t in ROWS) + '<li><b>Kashmir:</b> ' + KASHMIR + '</li></ul>'
    data = json.dumps({n: r for n, _, r, _ in ROWS}, ensure_ascii=False, separators=(',', ':'))
    js = ('<script>(function(){var D=' + data + ';var F=' + json.dumps(FULL, separators=(',', ':')) + ';'
          'var L={b:"Best",s:"Snow season",m:"Monsoon",o:"Possible — ask us"};'
          'var R=document.getElementById("szt-season");if(!R){return;}'
          'var bar=R.querySelector(".szt-sh-bar"),sum=document.getElementById("szt-sh-sum"),wa=document.getElementById("szt-sh-wa");'
          'if(!bar){return;}if(!sum){return;}'
          'function pick(m){var bs=bar.querySelectorAll("button");for(var i=0;i<bs.length;i++){bs[i].setAttribute("aria-pressed",String(i===m));}'
          'var cs=R.querySelectorAll("[data-m]");for(var j=0;j<cs.length;j++){if(cs[j].tagName!=="BUTTON"){cs[j].classList.toggle("on",cs[j].getAttribute("data-m")===String(m));}}'
          'var g={b:[],s:[],m:[],o:[]};for(var k in D){if(D.hasOwnProperty(k)){g[D[k].charAt(m)].push(k);}}'
          'sum.textContent="";var hd=document.createElement("strong");hd.textContent=F[m]+" in India";sum.appendChild(hd);var o=["b","s","m","o"];'
          'for(var x=0;x<o.length;x++){if(g[o[x]].length){var dv=document.createElement("div"),bb=document.createElement("b");bb.textContent=L[o[x]]+": ";dv.appendChild(bb);dv.appendChild(document.createTextNode(g[o[x]].join(", ")));sum.appendChild(dv);}}'
          'if(wa){var t="Hello Suzu Travels, I am thinking of travelling to India in "+F[m]+". Best for that month on your chart: "+(g.b.join(", ")||"none")+". Can you suggest a plan?";'
          'wa.href=wa.getAttribute("data-base")+encodeURIComponent(t);wa.textContent="Plan a "+F[m]+" trip on WhatsApp";sum.appendChild(wa);wa.hidden=false;}}'
          'bar.addEventListener("click",function(e){var b=e.target.closest("button");if(b){pick(parseInt(b.getAttribute("data-m"),10));}});'
          'bar.hidden=false;sum.hidden=false;pick(new Date().getMonth());})();</script>')
    return ('<!--szt:season-heatmap--><section class="lp-sec alt szt-sh" id="szt-season" style="scroll-margin-top:90px"><style>' + CSS + '</style>'
            '<div class="lp-wrap"><span class="lp-eyebrow">Month by month</span>'
            '<h2>India Season Chart: Where to Go Each Month</h2>'
            '<p class="szt-sh-lead">India is big enough that somewhere is in season every month. Pick your travel month to see which regions are at their best, '
            'which are under snow or monsoon rain, and where we would need to talk it through with you.</p>'
            + bar + summ +
            '<div class="szt-sh-scroll" role="region" aria-label="Season chart, scroll sideways" tabindex="0"><table><caption class="szt-sh-vh">Best months to visit regions of India</caption>'
            + head + '<tbody>' + body + '</tbody></table></div>' + leg + notes +
            '<p class="szt-sh-src">' + SRC + '</p>' + js +
            '</div></section><!--/szt:season-heatmap-->')

BANNED = ['verified', 'government approved', 'registered DMC', '24/7', '24x7', '₹', 'guarantee', 'safest', 'perfectly safe', 'cheapest', 'most foreigners']

if __name__ == '__main__':
    h = html()
    assert '\n' not in h
    js = h[h.find('<script>'):h.find('</script>')]
    assert '&' not in js and '//' not in js, 'JS must not contain & or //'
    import re
    assert not any('<' in lit for lit in re.findall(r'"(?:[^"\\]|\\.)*"', js)), 'no HTML tags inside JS strings: wpautop rewrites them, and backslash escapes get doubled by the MCP - build nodes with createElement'
    assert '&' not in h.replace('&amp;', ''), 'raw ampersand'
    low = h.lower()
    for b in BANNED:
        assert b.lower() not in low, b
    for _, _, r, _ in ROWS:
        assert len(r) == 12
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'widget.html')
    open(p, 'w').write(h)
    print('widget.html', len(h))
