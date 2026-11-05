#!/usr/bin/env python3
"""TRUST_BACKLOG row 22 — season-strip-gt on /golden-triangle-tour/ (11412), right after the hand-built
'Best Time for a Golden Triangle Tour' table (inserted before <section class="lp-sec" id="what-every-tour-includes").
Month strip for the Golden Triangle + the page's own extensions (Rishikesh, Himalayas = Shimla/Manali, Kashmir).
NO NEW FACTS: rows, notes, Kashmir advisory and sources are imported from ../season-heatmap/build.py (the hub chart, live 20 Oct 2026).
Kashmir gets no colours, only the dated advisory line (same as the hub). No prices. Nothing stored, no fetch, no third-party JS.
Inline JS: no ampersand, no double slash, no HTML in JS strings (createElement only). JS off: full strip + notes, buttons hidden.
Prefix .szt-sg (free on the site, checked 5 Nov 2026)."""
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'season-heatmap'))
import build as hub  # noqa: E402

R = {n: (sub, r, t) for n, sub, r, t in hub.ROWS}
assert R['Shimla · Dharamshala'][1] == R['Manali'][1]
# (label, which package card it belongs to, hub row name, note taken from hub row(s))
ROWS = [
    ('Delhi · Agra · Jaipur', 'Every Golden Triangle tour', 'Delhi · Agra · Jaipur', R['Delhi · Agra · Jaipur'][2]),
    ('Haridwar · Rishikesh', 'Golden Triangle + Rishikesh', 'Rishikesh · Haridwar', R['Rishikesh · Haridwar'][2]),
    ('Shimla · Manali', 'Golden Triangle + Himalayas', 'Manali',
     R['Manali'][2] + ' ' + R['Shimla · Dharamshala'][2].split('.')[0].replace('in Dharamshala', 'in the Himachal hills') + '.'),
]
B, S, M, O = 'b', 's', 'm', 'o'
LBL = hub.LBL
MON, FULL = hub.MON, hub.FULL
WA = 'https://wa.me/917087488961?text='
WA_DEFAULT = 'Hello%20Suzu%20Travels%2C%20I%20would%20like%20help%20choosing%20the%20best%20month%20for%20my%20Golden%20Triangle%20tour.'

CSS = (".szt-sg{font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;color:#0E1B14;padding-top:8px!important}"
       ".szt-sg *{box-sizing:border-box}.szt-sg p:empty,.szt-sg br{display:none}"
       ".szt-sg-card{background:#fff;border:1px solid #E8DFC8;border-radius:20px;box-shadow:0 10px 28px rgba(14,27,20,.07);overflow:hidden}"
       ".szt-sg-h{background:#0E1B14;color:#F4EEDD;padding:18px 20px}"
       ".szt-sg-k{display:block;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#E2C158;font-weight:800;margin-bottom:6px}"
       ".szt-sg-h b{display:block;font-size:21px;line-height:1.25;color:#fff;font-family:Sora,'Plus Jakarta Sans',sans-serif}"
       ".szt-sg-h span.szt-sg-s{display:block;font-size:14px;line-height:1.55;color:#DCD3BC;margin-top:6px;max-width:760px}"
       ".szt-sg-in{padding:16px 20px 18px}"
       ".szt-sg-bar{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 12px}.szt-sg-bar[hidden]{display:none}"
       ".szt-sg-bar button{min-width:44px;min-height:40px;padding:8px 10px;border-radius:10px;border:1px solid #DCD6C6;background:#fff;color:#0E1B14;font-family:inherit;font-weight:700;font-size:13px;line-height:1;cursor:pointer}"
       ".szt-sg-bar button[aria-pressed=true]{background:#0E1B14;color:#E2C158;border-color:#0E1B14}"
       ".szt-sg-bar button:focus-visible{outline:2px solid #B8860B;outline-offset:2px}"
       ".szt-sg-sum{background:#FBF8EF;border:1px dashed #D9CFB4;border-radius:14px;padding:12px 14px;margin:0 0 12px;font-size:14px;line-height:1.6;color:#3D4A40}.szt-sg-sum[hidden]{display:none}"
       ".szt-sg-sum strong{color:#0E1B14;display:block}.szt-sg-sum b{color:#0E1B14}"
       ".szt-sg-sum a{display:inline-flex;align-items:center;min-height:44px;margin-top:10px;padding:10px 16px;border-radius:12px;background:#E2C158;color:#0E1B14!important;font-weight:800;font-size:14px;text-decoration:none!important}"
       ".szt-sg-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%}"
       ".szt-sg table{border-collapse:separate;border-spacing:3px;width:100%;min-width:600px;margin:0;font-size:13px;border:0}"
       ".szt-sg th,.szt-sg td{border:0;padding:0;text-align:center;vertical-align:middle;background:none}"
       ".szt-sg thead th{font-size:11.5px;font-weight:800;color:#56645A;padding:6px 0;text-transform:uppercase;letter-spacing:.02em}"
       ".szt-sg tbody th{text-align:left;padding:6px 8px 6px 4px;min-width:150px;position:sticky;left:0;background:#fff;z-index:1;font-size:13.5px;line-height:1.25}"
       ".szt-sg tbody th small{display:block;font-weight:500;color:#6B776E;font-size:11.5px}"
       ".szt-sg tbody td{height:30px;border-radius:7px;font-size:11px;font-weight:800;line-height:30px}"
       ".szt-sg td.b,.szt-sg-leg .b{background:#E2C158;color:#3d2e00}.szt-sg td.s,.szt-sg-leg .s{background:#C9D8E8;color:#1d3550}.szt-sg td.m,.szt-sg-leg .m{background:#8F9C94;color:#fff}.szt-sg td.o,.szt-sg-leg .o{background:#F4EEDD;color:#8a826c}"
       ".szt-sg td.on,.szt-sg thead th.on{box-shadow:inset 0 0 0 2px #0E1B14}.szt-sg thead th.on{border-radius:7px;color:#0E1B14}"
       ".szt-sg-kr td{padding:8px 6px!important;text-align:left!important;font-size:12.5px;line-height:1.45;color:#46524A;background:#FBF8EF!important;border-radius:8px}"
       ".szt-sg-leg{display:flex;flex-wrap:wrap;gap:8px 16px;margin:12px 0 0;padding:0;list-style:none;font-size:13px;color:#46524A}"
       ".szt-sg-leg li{display:flex;align-items:center;gap:6px;margin:0}.szt-sg-leg i{width:18px;height:18px;border-radius:5px;display:inline-block}"
       ".szt-sg-notes{margin:14px 0 0;padding:0;list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:8px 18px}"
       ".szt-sg-notes li{font-size:13.5px;line-height:1.5;color:#46524A;margin:0}.szt-sg-notes b{color:#0E1B14}"
       ".szt-sg-src{font-size:12px;line-height:1.5;color:#6B776E;margin:12px 0 0;max-width:90ch}"
       ".szt-sg-src a{color:#8a6400;font-weight:700}"
       ".szt-sg-vh{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}"
       "@media(max-width:700px){.szt-sg-notes{grid-template-columns:1fr}.szt-sg tbody th{min-width:112px;font-size:12.5px}.szt-sg table{min-width:540px}"
       ".szt-sg-bar button{min-width:0;flex:1 0 14%;padding:8px 4px}.szt-sg-h,.szt-sg-in{padding-left:14px;padding-right:14px}.szt-sg-h b{font-size:19px}}")

SYM = {B: '★', S: '❄', M: '☔', O: '·'}

def cell(c, m):
    return '<td class="%s" data-m="%d" title="%s">%s</td>' % (c, m, LBL[c], SYM[c])

def html():
    head = '<thead><tr><th scope="col"><span class="szt-sg-vh">Tour</span></th>' + ''.join(
        '<th scope="col" data-m="%d">%s</th>' % (i, m) for i, m in enumerate(MON)) + '</tr></thead>'
    body = ''
    for name, tour, key, _ in ROWS:
        body += '<tr><th scope="row">%s<small>%s</small></th>%s</tr>' % (name, tour, ''.join(cell(c, i) for i, c in enumerate(R[key][1])))
    body += ('<tr class="szt-sg-kr"><th scope="row">Srinagar · Gulmarg<small>Golden Triangle + Kashmir</small></th>'
             '<td colspan="12">No colours — please read the travel advice below first.</td></tr>')
    bar = '<div class="szt-sg-bar" role="group" aria-label="Pick your travel month" hidden>' + ''.join(
        '<button type="button" data-m="%d" aria-pressed="false" aria-label="%s">%s</button>' % (i, FULL[i], m) for i, m in enumerate(MON)) + '</div>'
    summ = ('<div class="szt-sg-sum" id="szt-sg-sum" aria-live="polite" hidden></div>'
            '<a id="szt-sg-wa" hidden href="' + WA + WA_DEFAULT + '" target="_blank" rel="noopener" data-base="' + WA + '">Ask about my month on WhatsApp</a>')
    leg = ('<ul class="szt-sg-leg"><li><i class="b"></i>★ Best months</li><li><i class="s"></i>❄ Snow season (Himalaya)</li>'
           '<li><i class="m"></i>☔ Monsoon rain</li><li><i class="o"></i>Possible — ask us</li></ul>')
    notes = ('<ul class="szt-sg-notes">' + ''.join('<li><b>%s:</b> %s</li>' % (n, t) for n, _, _, t in ROWS)
             + '<li><b>Kashmir:</b> ' + hub.KASHMIR + '</li></ul>')
    data = json.dumps([[n, t, R[k][1]] for n, t, k, _ in ROWS], ensure_ascii=False, separators=(',', ':'))
    js = ('<script>(function(){var D=' + data + ';var F=' + json.dumps(FULL, separators=(',', ':')) + ';'
          'var L={b:"Best",s:"Snow season",m:"Monsoon",o:"Possible — ask us"};'
          'var R=document.getElementById("szt-sg");if(!R){return;}'
          'var bar=R.querySelector(".szt-sg-bar"),sum=document.getElementById("szt-sg-sum"),wa=document.getElementById("szt-sg-wa");'
          'if(!bar){return;}if(!sum){return;}'
          'function pick(m){var bs=bar.querySelectorAll("button");for(var i=0;i<bs.length;i++){bs[i].setAttribute("aria-pressed",String(i===m));}'
          'var cs=R.querySelectorAll("td[data-m],th[data-m]");for(var j=0;j<cs.length;j++){cs[j].classList.toggle("on",cs[j].getAttribute("data-m")===String(m));}'
          'sum.textContent="";var hd=document.createElement("strong");hd.textContent=F[m]+" on this page’s tours";sum.appendChild(hd);var best=[];'
          'for(var x=0;x<D.length;x++){var c=D[x][2].charAt(m);if(c==="b"){best.push(D[x][1]);}var dv=document.createElement("div"),bb=document.createElement("b");'
          'bb.textContent=D[x][0]+": ";dv.appendChild(bb);dv.appendChild(document.createTextNode(L[c]));sum.appendChild(dv);}'
          'var kd=document.createElement("div"),kb=document.createElement("b");kb.textContent="Kashmir: ";kd.appendChild(kb);'
          'kd.appendChild(document.createTextNode("read the travel advice below"));sum.appendChild(kd);'
          'if(wa){var t="Hello Suzu Travels, I am thinking of a Golden Triangle tour in "+F[m]+". Best that month on your chart: "+(best.join("; ")||"none of the listed tours")+". Which tour would you suggest?";'
          'wa.href=wa.getAttribute("data-base")+encodeURIComponent(t);wa.textContent="Ask about a "+F[m]+" trip on WhatsApp";sum.appendChild(wa);wa.hidden=false;}}'
          'bar.addEventListener("click",function(e){var b=e.target.closest("button");if(b){pick(parseInt(b.getAttribute("data-m"),10));}});'
          'bar.hidden=false;sum.hidden=false;pick(new Date().getMonth());})();</script>')
    return ('<!--szt:season-strip-gt--><section class="lp-sec alt szt-sg" id="szt-sg" style="scroll-margin-top:90px"><style>' + CSS + '</style>'
            '<div class="lp-wrap"><div class="szt-sg-card"><div class="szt-sg-h"><span class="szt-sg-k">Adding the hills?</span>'
            '<b>Month by month: the Golden Triangle and its add-ons</b>'
            '<span class="szt-sg-s">October to March suits Delhi, Agra and Jaipur, but Rishikesh, Shimla, Manali and Kashmir run on different seasons. '
            'Pick your month to see how each add-on fits.</span></div><div class="szt-sg-in">'
            + bar + summ +
            '<div class="szt-sg-scroll" role="region" aria-label="Season strip, scroll sideways" tabindex="0"><table><caption class="szt-sg-vh">Best months for the Golden Triangle and its add-on regions</caption>'
            + head + '<tbody>' + body + '</tbody></table></div>' + leg + notes +
            '<p class="szt-sg-src">' + hub.SRC + ' <a href="/india-tours/#szt-season">See every region of India month by month</a>.</p>' + js +
            '</div></div></div></section><!--/szt:season-strip-gt-->')

if __name__ == '__main__':
    h = html()
    assert '\n' not in h
    js = h[h.find('<script>'):h.find('</script>')]
    assert '&' not in js and '//' not in js, 'JS must not contain & or //'
    assert not any('<' in lit for lit in re.findall(r'"(?:[^"\\]|\\.)*"', js)), 'no HTML tags inside JS strings'
    assert '&' not in h.replace('&amp;', ''), 'raw ampersand'
    assert 'US$' not in h and '$' not in h.replace('US$', ''), 'no prices in this widget'
    low = h.lower()
    for b in hub.BANNED:
        assert b.lower() not in low, b
    p = os.path.join(HERE, 'widget.html')
    open(p, 'w').write(h)
    print('widget.html', len(h))
