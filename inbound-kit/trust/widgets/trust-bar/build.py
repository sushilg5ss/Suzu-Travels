#!/usr/bin/env python3
"""Builds trust/widgets/trust-bar/widget.html — one line, self-contained (rows 1+2 of TRUST_BACKLOG).
Trust strip + "talk to a real person" bar with live IST vs visitor-local clock.
Review count is NOT typed here: JS mirrors the Trustindex widget already on the page (.ti-sub strong) and hides the
item if the widget is absent."""
import os

BOOKING = ("20% deposit locks your dates and price; full refund if cancelled within 48 hours of paying; balance before the trip; "
           "pay by card via Razorpay (international cards accepted) or PayPal.")

CSS = (".szt{font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;margin:22px 0 6px}"
       ".szt *{box-sizing:border-box}.szt p:empty,.szt br{display:none}"
       ".szt-row{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));background:#fff;border:1px solid #E3E7E1;border-radius:18px;box-shadow:0 10px 28px rgba(18,38,21,.07);overflow:hidden}"
       ".szt-i{display:flex;gap:11px;align-items:flex-start;padding:16px 16px;border-right:1px solid #EDF0EB;text-decoration:none!important;color:#122615!important;transition:background .2s}"
       ".szt-i:last-child{border-right:0}a.szt-i:hover{background:#F7F9F4}"
       ".szt-ic{flex:none;width:36px;height:36px;border-radius:11px;background:#EEF5EC;color:#1B5E20;display:flex;align-items:center;justify-content:center}"
       ".szt-ic svg{width:20px;height:20px}"
       ".szt-i b{display:block;font-size:14.5px;line-height:1.3;color:#122615}"
       ".szt-i span{display:block;font-size:12.5px;line-height:1.4;color:#56645A;margin-top:2px}"
       ".szt-i u{text-decoration:none;color:#B8860B;font-weight:700}"
       ".szt-talk{margin-top:12px;display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between;background:#122615;color:#fff;border-radius:18px;padding:14px 18px}"
       ".szt-clock{display:flex;gap:18px;flex-wrap:wrap;align-items:center;font-size:14px;color:#DDE6DF}"
       ".szt-clock b{color:#fff;font-size:17px;font-variant-numeric:tabular-nums}"
       ".szt-dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:#D4AF37;margin-right:6px}"
       ".szt-btns{display:flex;gap:10px;flex-wrap:wrap}"
       ".szt-btns a{display:inline-flex;align-items:center;gap:7px;padding:11px 16px;border-radius:12px;font-weight:800;font-size:14px;text-decoration:none!important;line-height:1}"
       ".szt-wa{background:#25D366;color:#0b2414!important}.szt-em{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.3);color:#fff!important}"
       ".szt-fine{font-size:12px;color:#6B776E;margin:8px 4px 0;line-height:1.5}"
       "@media(max-width:900px){.szt-row{grid-template-columns:1fr 1fr}.szt-i:nth-child(2){border-right:0}.szt-i:nth-child(-n+2){border-bottom:1px solid #EDF0EB}}"
       "@media(max-width:520px){.szt-ic{display:none}.szt-i{padding:12px}.szt-i b{font-size:13.5px}.szt-i span{font-size:11.5px}.szt-ic{width:30px;height:30px}.szt-btns a{flex:1 1 auto;justify-content:center}}")

def svg(p):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">' + p + '</svg>')

SH = svg('<path d="M12 3l7 3v6c0 4.5-3 7.6-7 9-4-1.4-7-4.5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/>')
ST = svg('<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>')
CD = svg('<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18M7 15h4"/>')
HM = svg('<path d="M3 11l9-7 9 7v9H3z"/><path d="M9 20v-6h6v6"/>')
WA = ('<svg viewBox="0 0 24 24" width="17" height="17" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm5.5 12.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2.1-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5 2.4 1 2.9.8 3.6.7.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3z"/></svg>')

HTML = ('<!--szt:trust-bar--><div class="szt" id="szt-trust"><style>' + CSS + '</style>'
        '<div class="szt-row">'
        '<a class="szt-i" href="https://suzutravels.com/certificates/"><span class="szt-ic">' + SH + '</span><span><b>HP Tourism registered travel agent</b><span>Reg. No. DTO-MND-11-243/2022 · <u>see certificate</u></span></span></a>'
        '<a class="szt-i" id="szt-rev" href="#reviews"><span class="szt-ic">' + ST + '</span><span><b>Google reviews</b><span id="szt-rev-n">Read what our guests say</span></span></a>'
        '<div class="szt-i"><span class="szt-ic">' + CD + '</span><span><b>Pay by card or PayPal</b><span>Razorpay (international cards accepted) or PayPal · 20% deposit</span></span></div>'
        '<div class="szt-i"><span class="szt-ic">' + HM + '</span><span><b>Local company since 2019</b><span>Own office and team in Himachal Pradesh, GST-registered</span></span></div>'
        '</div>'
        '<div class="szt-talk"><div class="szt-clock"><span><span class="szt-dot"></span>Our office (India, IST): <b id="szt-ist">—</b></span>'
        '<span id="szt-you-w">Your time: <b id="szt-you">—</b></span><span>We usually reply within 2 hours.</span></div>'
        '<div class="szt-btns"><a class="szt-wa" id="szt-wa" href="https://wa.me/917087488961?text=Hello%20Suzu%20Travels%2C%20I%27m%20planning%20a%20trip%20to%20India." target="_blank" rel="noopener">' + WA + 'WhatsApp a real person</a>'
        '<a class="szt-em" href="mailto:info@suzutravels.com?subject=India%20trip%20enquiry">Email us</a></div></div>'
        '<p class="szt-fine">' + BOOKING + '</p>'
        '<script>(function(){'
        'function f(z){try{return new Date().toLocaleTimeString("en-GB",{hour:"2-digit",minute:"2-digit",timeZone:z});}catch(e){return "";}}'
        'var y=Intl.DateTimeFormat().resolvedOptions().timeZone||"";'
        'function t(){var a=document.getElementById("szt-ist"),b=document.getElementById("szt-you");if(a){a.textContent=f("Asia/Kolkata");}'
        'if(b){if(y==="Asia/Kolkata"||y==="Asia/Calcutta"||!y){var w=document.getElementById("szt-you-w");if(w){w.style.display="none";}}else{b.textContent=f(y);}}}'
        't();setInterval(t,30000);'
        'function rv(){var s=document.querySelector(".ti-sub strong");var n=document.getElementById("szt-rev-n");'
        'if(s){if(n){n.textContent=s.textContent.trim()+" on Google · read them";}}'
        'var g=null;var L=document.querySelectorAll("a[href*=\\"google\\"]");for(var k=0;k<L.length;k++){if(/review/i.test(L[k].textContent)){g=L[k];break;}}var r=document.getElementById("szt-rev");'
        'if(r){if(g){r.href=g.href;r.target="_blank";r.rel="noopener";}else{var w2=document.querySelector(".ti-widget");if(w2){if(!w2.id){w2.id="reviews";}}else{r.style.display="none";}}}}'
        'document.addEventListener("DOMContentLoaded",rv);window.addEventListener("load",rv);setTimeout(rv,4000);'
        'var c=y.split("/")[1]||"";var wa=document.getElementById("szt-wa");'
        'if(wa){if(c){wa.href=wa.href.replace("trip%20to%20India.","trip%20to%20India%20(I%27m%20in%20"+encodeURIComponent(c.replace("_"," "))+").");}}'
        '})();</script></div><!--/szt:trust-bar-->')

# Gold/ink variant (v2 look, 17 Oct) for pages without the hub skin, e.g. 11412 — plus the mobile width fix for the
# site-wide html{zoom:.9} (blank strip on the right of phones), scoped to that page id.
GOLD = (".szt-row{border-color:#E8DFC8;box-shadow:0 10px 28px rgba(14,27,20,.08)}.szt-i{color:#0E1B14!important}a.szt-i:hover{background:#FBF8EF}"
        ".szt-ic{background:#F4EEDD;color:#8A6A12}.szt-i b{color:#0E1B14}.szt-talk{background:#0E1B14}.szt-dot{background:#E2C158}")

def variant(page_id):
    fix = "@media(max-width:768px){body.page-id-%d{max-width:none!important}}" % page_id
    return HTML.replace('</style>', GOLD + fix + '</style>', 1)

if __name__ == '__main__':
    js = HTML[HTML.find('<script>'):]
    assert '&' not in js and '//' not in js, 'JS must not contain & or //'
    assert '\n' not in HTML
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, 'widget.html'), 'w').write(HTML)
    print('widget.html', len(HTML))
    v = variant(11412)
    assert '\n' not in v
    open(os.path.join(here, 'widget-11412.html'), 'w').write(v)
    print('widget-11412.html', len(v))
