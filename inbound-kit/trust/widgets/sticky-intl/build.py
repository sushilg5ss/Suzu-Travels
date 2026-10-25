#!/usr/bin/env python3
"""TRUST_BACKLOG row 11 — sticky-enquiry-bar-intl.
The site already has a mobile sticky bar (#szcta: Get Free Quote popup · Book a Call · WhatsApp · Call) on every page.
On the inbound pages its WhatsApp button pre-fills 'I would like a Himachal quote' — wrong for a foreign visitor on
/india-tours/, /golden-triangle-tour/ or /char-dham-yatra-for-nri/. This block only RE-LABELS that one link on its own page:
page-specific India message + visitor's city from the browser time zone (nothing stored, nothing sent anywhere) and keeps the
site's '[Ref: DR-<slug>]' tag. No new bar, no CSS, no clash. Rules: no '&', no '//' in the JS, IIFE, degrades to the old link."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
MSG = {
 11411: "Hello Suzu Travels, I am planning a trip to India",
 11412: "Hello Suzu Travels, I am interested in a private Golden Triangle tour (Delhi, Agra, Jaipur)",
 11413: "Hello Suzu Travels, I am interested in the Char Dham Yatra (Yamunotri, Gangotri, Kedarnath, Badrinath)",
}
TAIL = ". Please send me ideas and a US$ quote."

def widget(pid):
    js = ('(function(){'
          'var M="' + MSG[pid] + '";'
          'var T="' + TAIL + '";'
          'var c="";try{var y=Intl.DateTimeFormat().resolvedOptions().timeZone||"";'
          'if(y!=="Asia/Kolkata"){if(y!=="Asia/Calcutta"){c=(y.split("/").pop()||"").split("_").join(" ");}}}catch(e){}'
          'function fx(){var a=document.querySelector("#szcta a.w");if(!a){return;}'
          'if(a.getAttribute("data-szt")==="1"){return;}'
          'var h=a.getAttribute("href")||"";var q=h.indexOf("?text=");if(q<0){return;}'
          'var old="";try{old=decodeURIComponent(h.slice(q+6));}catch(e){}'
          'var r="";var i=old.indexOf("[Ref:");if(i>-1){var j=old.indexOf("]",i);if(j>i){r=" "+old.slice(i,j+1);}}'
          'var m=M+(c?" (I am in "+c+")":"")+T+r;'
          'a.setAttribute("href",h.slice(0,q)+"?text="+encodeURIComponent(m));'
          'a.setAttribute("aria-label","WhatsApp Suzu Travels about your India trip");a.setAttribute("data-szt","1");}'
          'fx();document.addEventListener("DOMContentLoaded",fx);window.addEventListener("load",fx);setTimeout(fx,1500);setTimeout(fx,4000);'
          'document.addEventListener("click",function(e){var t=e.target;if(t){if(t.closest){if(t.closest("#szcta a.w")){fx();}}}},true);'
          '})();')
    assert '&' not in js and '//' not in js, 'banned chars'
    return '<!--szt:sticky-intl--><script>' + js + '</script><!--/szt:sticky-intl-->'

if __name__ == '__main__':
    for pid in MSG:
        open(os.path.join(HERE, 'widget-%d.html' % pid), 'w').write(widget(pid))
        print(pid, len(widget(pid)))
