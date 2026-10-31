#!/usr/bin/env python3
"""call-time (TRUST_BACKLOG row 17) — 'Pick a call time in YOUR time zone' on hub /india-tours/ (11411).
Shows the next call slots inside the team's hours (9 am-9 pm IST, UTC+5:30 — same wording as the kit's 'talk' strip, gen_pages.py)
converted to the visitor's own clock; picking one writes a call request that opens in the visitor's own WhatsApp / email app.
Slots start at least 2 hours from now (the published 'usually within 2 hours' reply time). Not a booking system: the team confirms.
No fetch, no third-party JS, no cookies, nothing stored. JS has no '&' and no '//'. Prefix .szo (free on the site, checked 31 Oct 2026)."""
import os, json, re
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))

CSS = (".szo{font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;margin:0;padding:34px 16px;background:#F4EEDD;scroll-margin-top:90px}"
       ".szo *{box-sizing:border-box}.szo p:empty,.szo br{display:none}"
       ".szo-c{max-width:1100px;margin:0 auto;background:#fff;border:1px solid #E8DFC8;border-radius:20px;box-shadow:0 10px 28px rgba(14,27,20,.08);overflow:hidden}"
       ".szo-h{background:#0E1B14;color:#F4EEDD;padding:20px 22px}"
       ".szo-k{display:block;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#E2C158;font-weight:800;margin-bottom:6px}"
       ".szo-h b{display:block;font-size:22px;line-height:1.25;color:#fff;font-family:Sora,'Plus Jakarta Sans',sans-serif}"
       ".szo-s{display:block;font-size:14px;line-height:1.55;color:#DCD3BC;margin-top:6px;max-width:780px}"
       ".szo-tz{padding:16px 22px 0;font-size:13.5px;color:#3D4A40;line-height:1.5}.szo-tz strong{color:#0E1B14}"
       ".szo-d{display:flex;gap:8px;flex-wrap:wrap;padding:12px 22px 0}"
       ".szo-d button,.szo-g button{font-family:inherit;cursor:pointer;border:1px solid #D9CFB4;background:#FFFDF7;color:#0E1B14;border-radius:11px}"
       ".szo-d button{padding:10px 14px;font-weight:800;font-size:14px;min-height:44px}"
       ".szo-d button[aria-pressed=true]{background:#0E1B14;color:#fff;border-color:#0E1B14}"
       ".szo-g{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:8px;padding:14px 22px 0}"
       ".szo-g button{padding:9px 6px;min-height:52px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}"
       ".szo-g button b{font-size:15px;font-weight:800;line-height:1.1}.szo-g button small{font-size:11.5px;color:#6B776E;line-height:1.1}"
       ".szo-g button[aria-pressed=true]{background:#E2C158;border-color:#B8860B}.szo-g button[aria-pressed=true] small{color:#3D4A40}"
       ".szo-g button:focus-visible,.szo-d button:focus-visible{outline:2px solid #B8860B;outline-offset:1px}"
       ".szo-e{grid-column:1/-1;font-size:13.5px;color:#6B776E;padding:6px 0}"
       ".szo-pv{margin:14px 22px 0;padding:14px 16px;border-radius:14px;background:#FBF8EF;border:1px dashed #D9CFB4;font-size:13.5px;line-height:1.55;color:#3D4A40;white-space:pre-line;word-break:break-word}"
       ".szo-pv b{display:block;color:#0E1B14;font-size:12px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:4px}"
       ".szo-b{display:flex;gap:10px;flex-wrap:wrap;padding:16px 22px 6px}"
       ".szo-b a{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:13px 18px;border-radius:12px;font-weight:800;font-size:15px;line-height:1;text-decoration:none!important;min-height:46px}"
       ".szo-wa{background:#E2C158;color:#0E1B14!important}.szo-wa:hover{background:#F0D27A}"
       ".szo-em{background:#0E1B14;color:#fff!important}.szo-em:hover{background:#22342A}"
       ".szo-fine{font-size:12.5px;line-height:1.55;color:#6B776E;padding:6px 22px 20px;margin:0}"
       ".szo-nojs .szo-d,.szo-nojs .szo-g{display:none}"
       "@media(max-width:900px){.szo-g{grid-template-columns:repeat(4,minmax(0,1fr))}}"
       "@media(max-width:560px){.szo{padding:26px 12px}.szo-h{padding:18px 16px}.szo-h b{font-size:19px}.szo-tz,.szo-d,.szo-g{padding-left:16px;padding-right:16px}"
       ".szo-g{grid-template-columns:repeat(3,minmax(0,1fr))}.szo-pv{margin:12px 16px 0}.szo-b{padding:14px 16px 4px}.szo-b a{flex:1 1 100%}.szo-fine{padding:6px 16px 18px}}")

WA = ('<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm5.5 12.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2.1-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5 2.4 1 2.9.8 3.6.7.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3z"/></svg>')

HELLO = 'Hi Suzu Travels, I am planning a trip to India and would like a call to talk it through.'
STATIC = HELLO + ' A good time for me (please say it in IST too): '
SRC = 'sent from the call-time picker on suzutravels.com/india-tours/'
WA_BASE = 'https://wa.me/917087488961?text='
EM_BASE = 'mailto:info@suzutravels.com?subject=' + quote('Call request - India trip')

# JS: IST = UTC+5:30, no daylight saving. Slots 9:00-20:00 IST start times (team answers 9 am-9 pm IST).
JS = ('(function(){var R=document.getElementById("szo");if(!R){return;}R.className=R.className.replace(" szo-nojs","");'
      'var H=' + json.dumps(HELLO) + ',S=' + json.dumps(SRC) + ',OFF=19800000,HR=3600000;'
      'var D=R.querySelector(".szo-d"),G=R.querySelector(".szo-g"),P=document.getElementById("szo-msg"),T=document.getElementById("szo-tzn");'
      'var tz="";try{tz=Intl.DateTimeFormat().resolvedOptions().timeZone||"";}catch(e){}'
      'var inIndia=(tz==="Asia/Kolkata"||tz==="Asia/Calcutta");'
      'function lt(t){try{return new Date(t).toLocaleTimeString([],{hour:"numeric",minute:"2-digit"});}catch(e){return new Date(t).toTimeString().slice(0,5);}}'
      'function ld(t){try{return new Date(t).toLocaleDateString([],{weekday:"short",day:"numeric",month:"short"});}catch(e){return new Date(t).toDateString();}}'
      'function ist(t){var d=new Date(t+OFF);var h=d.getUTCHours(),m=d.getUTCMinutes();var ap=h<12?"am":"pm";var h12=h%12;if(h12===0){h12=12;}'
      'return h12+(m?":"+(m<10?"0":"")+m:"")+" "+ap+" IST";}'
      'function istd(t){var d=new Date(t+OFF);var W=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],M=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];return W[d.getUTCDay()]+" "+d.getUTCDate()+" "+M[d.getUTCMonth()];}'
      'if(T){T.textContent=inIndia?"India Standard Time (you are in India)":(tz?tz.replace(/_/g," "):"your device time zone");}'
      'var now=Date.now(),earliest=now+2*HR;var n=new Date(now+OFF);var base=Date.UTC(n.getUTCFullYear(),n.getUTCMonth(),n.getUTCDate())-OFF;'
      'var days=[],lab="";for(var k=0;k<5;k++){for(var h=9;h<=20;h++){var t=base+k*24*HR+h*HR;if(t>=earliest){var l=ld(t);'
      'if(l!==lab){if(days.length===3){k=9;break;}days.push([]);lab=l;}days[days.length-1].push(t);}}}'
      'var cur=0,pick=0;'
      'function msg(){var L=[H,""];if(pick){L.push("Please call me on WhatsApp on: "+ld(pick)+", "+lt(pick)+" my time ("+(tz||"my time zone")+")");'
      'L.push("= "+istd(pick)+", "+ist(pick));}else{L.push("A good time to call me: (please pick one)");}'
      'L.push("");L.push("My trip in one line: ");L.push("");L.push("("+S+")");return L.join(String.fromCharCode(10));}'
      'function upd(){var m=msg();if(P){P.textContent=m;}var w=document.getElementById("szo-wa");if(w){w.href=w.getAttribute("data-b")+encodeURIComponent(m);}'
      'var em=document.getElementById("szo-em");if(em){em.href=em.getAttribute("data-b")+String.fromCharCode(38)+"body="+encodeURIComponent(m);}}'
      'function grid(){G.innerHTML="";var sl=days[cur]||[];for(var i=0;i<sl.length;i++){(function(t){var b=document.createElement("button");b.type="button";'
      'b.setAttribute("aria-pressed",t===pick?"true":"false");b.setAttribute("aria-label",ld(t)+" "+lt(t)+" your time, "+ist(t));'
      'var x=document.createElement("b");x.textContent=lt(t);var y=document.createElement("small");y.textContent=inIndia?"IST":ist(t);b.appendChild(x);b.appendChild(y);'
      'b.addEventListener("click",function(){pick=t;grid();upd();});G.appendChild(b);})(sl[i]);}'
      'if(!sl.length){var e=document.createElement("p");e.className="szo-e";e.textContent="No slots left today - pick another day.";G.appendChild(e);}}'
      'function tabs(){D.innerHTML="";for(var i=0;i<days.length;i++){(function(j){var b=document.createElement("button");b.type="button";'
      'b.setAttribute("aria-pressed",j===cur?"true":"false");b.textContent=ld(days[j][0]);b.addEventListener("click",function(){cur=j;tabs();grid();});D.appendChild(b);})(i);}}'
      'tabs();grid();upd();'
      'var B=R.querySelectorAll(".szo-b a");for(var q=0;q<B.length;q++){B[q].addEventListener("click",upd,true);}'
      '})();')

def build():
    static_msg = STATIC + '\n\n(' + SRC + ')'
    html = ('<!--szt:call-time--><section class="szo szo-nojs" id="szo" aria-label="Pick a call time in your time zone"><style>' + CSS +
            '@media(max-width:768px){body.page-id-11411{max-width:none!important}}</style>'
            '<div class="szo-c"><div class="szo-h"><span class="szo-k">Talk to a real person</span><b>Pick a call time — shown in your own time zone</b>'
            '<span class="szo-s">Our team in Himachal answers 9 am–9 pm IST (UTC+5:30). Choose a time that suits you and send it to us; '
            'we confirm by WhatsApp or email, usually within 2 hours, and call you on WhatsApp. Bring your questions about India — dates, routes, visas, hotels.</span></div>'
            '<p class="szo-tz">Times below are in <strong id="szo-tzn">your device time zone</strong>. India does not change its clocks for daylight saving.</p>'
            '<div class="szo-d" role="group" aria-label="Day"></div><div class="szo-g" role="group" aria-label="Call time"></div>'
            '<div class="szo-pv" aria-live="polite"><b>Your message</b><span id="szo-msg">' + static_msg.replace('&', '&amp;').replace('<', '&lt;') + '</span></div>'
            '<div class="szo-b"><a class="szo-wa" id="szo-wa" data-b="' + WA_BASE + '" href="' + WA_BASE + quote(static_msg) + '" target="_blank" rel="noopener">' + WA + 'Send on WhatsApp</a>'
            '<a class="szo-em" id="szo-em" data-b="' + EM_BASE + '" href="' + EM_BASE + '">Send by email</a></div>'
            '<p class="szo-fine">This is a request, not a booked slot — we reply to confirm the time. Nothing you pick here is saved or sent by this page; '
            'the message opens in your own WhatsApp or email app and goes only to the Suzu Travels team (+91 70874 88961 · info@suzutravels.com), '
            'who use it only to answer your enquiry.</p>'
            '<script>' + JS + '</script></div></section><!--/szt:call-time-->')
    return html.replace('\n', ' ') if False else html

if __name__ == '__main__':
    h = build()
    js = h[h.find('<script>'):h.find('</script>')]
    assert '&' not in js and '//' not in js, 'JS must not contain & or //'
    # the static message carries newlines inside the encoded href only; the HTML itself must be one line
    h = h.replace('(' + SRC + ')</span>', '(' + SRC + ')</span>')
    body = h.replace('\n', ' ')
    low = body.lower()
    for bad in ['verified', '24/7', '₹', 'cheapest', 'guarantee', 'government approved', 'dmc', 'online now', 'seats left']:
        assert bad not in low, bad
    assert body.count('<!--szt:call-time-->') == 1
    assert 'US$' not in body
    out = os.path.join(HERE, 'widget.html')
    open(out, 'w').write(body)
    print(out, len(body))
