#!/usr/bin/env python3
"""compare-char-dham-yatras (TRUST_BACKLOG row 20) — 'Compare the yatras at a glance' on /char-dham-yatra-for-nri/ (11413).
Reuses the compare-gt (row 19) CSS + table logic. The rows are built in the browser FROM the page's own yatra cards
(.lp-card with .lp-price): tag (style + days/nights), h3 name, route line, 'from' price text. Nothing typed — no names, no prices.
'Quote this one' selects the matching yatra in the 11413 quote helper (#szr-tour; names compared with '&' read as 'and',
built with fromCharCode so the JS stays free of the ampersand), fires 'change' and scrolls there.
No fetch, no third-party JS, no cookies, nothing stored. JS has no '&', no '//'. Without JS the section stays hidden (cards remain)."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'compare-gt'))
import build as gt  # noqa: E402  (CSS shared with row 19)
PID = 11413

def build():
    js = ('<script>(function(){'
          'var S=document.getElementById("compare-yatras");if(!S){return;}var T=S.querySelector("tbody");if(!T){return;}'
          'function tx(e){if(!e){return "";}var s=String(e.textContent||"");var W=[10,9,13,160];for(var j=0;j<W.length;j++){s=s.split(String.fromCharCode(W[j])).join(" ");}return s.replace(/ +/g," ").trim();}'
          'function nz(s){return String(s).toLowerCase().split(String.fromCharCode(38)).join(" and ").replace(/ +/g," ").trim();}'
          'var C=document.querySelectorAll(".lp-card");var n=0;'
          'for(var i=0;i<C.length;i++){var c=C[i];var pr=c.querySelector(".lp-price");var h=c.querySelector("h3");if(!pr){continue;}if(!h){continue;}'
          'var tag=tx(c.querySelector(".lp-tag")).split(" · ");var style=tag.length>1?tag[0]:"";var len=tag.length>1?tag[1]:tag[0];'
          'var rt=c.querySelector("h3 + p");var route=tx(rt);'
          'var b=pr.querySelector("b");var price=b?tx(b):"";var unit=tx(pr.querySelector("span"));if(!price){price=tx(pr).replace(unit,"").trim();}'
          'var tr=document.createElement("tr");'
          'function td(k,l){var d=document.createElement("td");d.className="szg-"+k;if(l){d.setAttribute("data-l",l);}tr.appendChild(d);return d;}'
          'var a=td("n");var nb=document.createElement("b");nb.textContent=tx(h);a.appendChild(nb);if(style){var sm=document.createElement("small");sm.textContent=style;a.appendChild(sm);}'
          'td("d","Length").textContent=len;td("r","Route").textContent=route;'
          'var p=td("p");p.appendChild(document.createTextNode(/[0-9]/.test(price)?"from "+price:price));if(unit){var u=document.createElement("small");u.textContent=unit;p.appendChild(u);}'
          'var q=td("b");var bt=document.createElement("button");bt.type="button";bt.className="szg-q";bt.textContent="Quote this one";bt.setAttribute("data-t",tx(h));'
          'bt.setAttribute("aria-label","Quote this one: "+tx(h));q.appendChild(bt);T.appendChild(tr);n++;}'
          'if(n<2){return;}S.hidden=false;'
          'S.addEventListener("click",function(e){var t=e.target;if(!t||!t.getAttribute){return;}var nm=t.getAttribute("data-t");if(!nm){return;}'
          'var sel=document.getElementById("szr-tour");var Q=document.getElementById("quote-helper");if(!sel){if(Q){Q.scrollIntoView({behavior:"smooth"});}return;}'
          'var key=nz(nm);for(var k=0;k<sel.options.length;k++){if(nz(sel.options[k].text).indexOf(key)===0){sel.selectedIndex=k;break;}}'
          'var ev;try{ev=new Event("change",{bubbles:true});}catch(x){ev=document.createEvent("Event");ev.initEvent("change",true,true);}sel.dispatchEvent(ev);'
          'if(Q){Q.scrollIntoView({behavior:"smooth",block:"start"});}try{sel.focus({preventScroll:true});}catch(x){}});'
          '})();</script>')
    return ('<!--szt:compare-cd--><section class="szg" id="compare-yatras" hidden aria-label="Compare the Char Dham yatras"><style>' + gt.CSS +
            ('@media(max-width:768px){body.page-id-%d{max-width:none!important}}' % PID) + '</style>'
            '<div class="szg-c"><div class="szg-h"><span class="szg-k">Compare at a glance</span><b>Which yatra fits your family?</b>'
            '<span class="szg-s">The same four yatras as the cards above, side by side. Every yatra is private and can be changed — pick the closest one and we adjust it to your dates and your elders’ pace.</span></div>'
            '<div class="szg-w"><table><thead><tr><th scope="col">Yatra</th><th scope="col">Length</th><th scope="col">Route</th><th scope="col">Price</th><th scope="col"><span style="position:absolute;left:-9999px">Quote</span></th></tr></thead><tbody></tbody></table></div>'
            '<p class="szg-fine">Read straight from the yatra cards on this page. “From” prices are per person for two pilgrims sharing a room; what is included and excluded is listed under “About our prices”. Helicopter seats depend on availability and weather. Your quote is exact, in US$.</p>'
            + js + '</div></section><!--/szt:compare-cd-->')

if __name__ == '__main__':
    h = build()
    js = h[h.find('<script>'):h.find('</script>')]
    assert '&' not in js and '//' not in js and '\\' not in js, 'JS must not contain & // or backslash'
    assert '\n' not in h
    low = h.lower()
    for bad in ['verified', '24/7', '₹', 'cheapest', 'guarantee', 'government approved', 'dmc', 'best price']:
        assert bad not in low, bad
    assert not re.search(r'US\$\s?\d', h), 'no typed prices'
    assert h.count('<!--szt:compare-cd-->') == 1
    out = os.path.join(HERE, 'widget-%d.html' % PID)
    open(out, 'w').write(h)
    print(out, len(h))
