#!/usr/bin/env python3
"""compare-hub-tours (TRUST_BACKLOG row 23) — 'Compare the six India tours at a glance' on the hub /india-tours/ (11411).
Reuses the compare-gt (row 19) CSS. Rows are built in the browser FROM the hub's own package cards (.lp-card with .lp-price):
tag (style + days/nights), h3 name, location line (h3 + p), 'from' price text. Nothing typed — no names, no prices.
The hub has no quote helper, so 'Quote this one' is a link whose href is COPIED from the card's own 'Get Free Quote' WhatsApp
link (a.q); 'See tour' scrolls to the card and outlines it in gold. No fetch, no third-party JS, no cookies, nothing stored.
JS has no '&', no '//', no backslash. Without JS / fewer than 2 cards the section stays hidden (cards remain)."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'compare-gt'))
import build as gt  # noqa: E402
PID = 11411
EXTRA = (".szg a.szg-q{display:inline-flex;align-items:center;justify-content:center;min-height:42px;padding:10px 14px;border-radius:11px;background:#E2C158;color:#0E1B14!important;font-weight:800;font-size:14px;text-decoration:none!important;white-space:nowrap;line-height:1}"
         ".szg a.szg-q:hover{background:#F0D27A}.szg a.szg-q:focus{outline:2px solid #B8860B;outline-offset:2px}"
         ".szg button.szg-v{background:none!important;border:0;padding:6px 2px;margin-left:8px;color:#0E1B14;font:700 13px/1.2 inherit;font-family:inherit;text-decoration:underline;cursor:pointer;box-shadow:none!important;text-transform:none;letter-spacing:0;min-height:36px}"
         ".szg td.szg-d{white-space:nowrap}.lp-card.szg-hi{outline:3px solid #E2C158;outline-offset:4px}"
         "@media(max-width:760px){.szg td.szg-b{display:flex;align-items:center;gap:8px}.szg a.szg-q{flex:1}}")

def build():
    js = ('<script>(function(){'
          'var S=document.getElementById("compare-hub-tours");if(!S){return;}var T=S.querySelector("tbody");if(!T){return;}'
          'function tx(e){if(!e){return "";}var s=String(e.textContent||"");var W=[10,9,13,160];for(var j=0;j<W.length;j++){s=s.split(String.fromCharCode(W[j])).join(" ");}return s.replace(/ +/g," ").trim();}'
          'var C=document.querySelectorAll(".lp-card");var n=0;var K=[];'
          'for(var i=0;i<C.length;i++){var c=C[i];if(S.contains(c)){continue;}var pr=c.querySelector(".lp-price");var h=c.querySelector("h3");if(!pr){continue;}if(!h){continue;}'
          'var tag=tx(c.querySelector(".lp-tag")).split(" · ");var style=tag.length>1?tag[0]:"";var len=tag.length>1?tag[1]:tag[0];'
          'var route=tx(c.querySelector("h3 + p"));'
          'var b=pr.querySelector("b");var price=b?tx(b):"";var us=pr.querySelector("span");var unit=us?tx(us):"";if(!price){price=tx(pr).replace(unit,"").trim();}'
          'var tr=document.createElement("tr");'
          'function td(k,l){var d=document.createElement("td");d.className="szg-"+k;if(l){d.setAttribute("data-l",l);}tr.appendChild(d);return d;}'
          'var a=td("n");var nb=document.createElement("b");nb.textContent=tx(h);a.appendChild(nb);if(style){var sm=document.createElement("small");sm.textContent=style;a.appendChild(sm);}'
          'td("d","Length").textContent=len;td("r","Places").textContent=route;'
          'var p=td("p");p.appendChild(document.createTextNode(/[0-9]/.test(price)?"from "+price:price));if(unit){var u=document.createElement("small");u.textContent=unit;p.appendChild(u);}'
          'var q=td("b");var qa=c.querySelector(".foot a.q");'
          'if(qa){var l=document.createElement("a");l.className="szg-q";l.href=qa.href;l.target="_blank";l.rel="noopener";l.textContent="Quote this one";l.setAttribute("aria-label","Quote this one on WhatsApp: "+tx(h));q.appendChild(l);}'
          'var v=document.createElement("button");v.type="button";v.className="szg-v";v.textContent="See tour";v.setAttribute("data-i",String(K.length));v.setAttribute("aria-label","See the tour card: "+tx(h));q.appendChild(v);'
          'K.push(c);T.appendChild(tr);n++;}'
          'if(n<2){return;}S.hidden=false;'
          'S.addEventListener("click",function(e){var t=e.target;if(!t||!t.getAttribute){return;}var ix=t.getAttribute("data-i");if(ix===null){return;}var c=K[parseInt(ix,10)];if(!c){return;}'
          'for(var k=0;k<K.length;k++){K[k].classList.remove("szg-hi");}c.classList.add("szg-hi");c.scrollIntoView({behavior:"smooth",block:"center"});'
          'setTimeout(function(){c.classList.remove("szg-hi");},2600);});'
          '})();</script>')
    return ('<!--szt:compare-hub--><section class="szg" id="compare-hub-tours" hidden aria-label="Compare our India tours"><style>' + gt.CSS + EXTRA +
            '</style><div class="szg-c"><div class="szg-h"><span class="szg-k">Compare at a glance</span><b>Which India tour fits your trip?</b>'
            '<span class="szg-s">The same tours as the cards above, side by side: length, places and the “from” price. Every tour is private and can be changed — pick the closest one and we adjust it to your dates, pace and hotels.</span></div>'
            '<div class="szg-w"><table><thead><tr><th scope="col">Tour</th><th scope="col">Length</th><th scope="col">Places</th><th scope="col">Price</th><th scope="col"><span style="position:absolute;left:-9999px">Quote</span></th></tr></thead><tbody></tbody></table></div>'
            '<p class="szg-fine">Read straight from the tour cards on this page. “From” prices are per person; what is included and excluded is listed under “About our prices” above. “Quote this one” opens WhatsApp with the tour name filled in — your quote is exact, in US$.</p>'
            + js + '</div></section><!--/szt:compare-hub-->')

if __name__ == '__main__':
    h = build()
    js = h[h.find('<script>'):h.find('</script>')]
    assert '&' not in js and '//' not in js and '\\' not in js, 'JS must not contain & // or backslash'
    assert '\n' not in h
    low = h.lower()
    for bad in ['verified', '24/7', '₹', 'cheapest', 'guarantee', 'government approved', 'dmc', 'best price']:
        assert bad not in low, bad
    assert not re.search(r'US\$\s?\d', h), 'no typed prices'
    assert h.count('<!--szt:compare-hub-->') == 1
    out = os.path.join(HERE, 'widget-11411.html')
    open(out, 'w').write(h)
    print(out, len(h))
