#!/usr/bin/env python3
"""share-trip (TRUST_BACKLOG row 18 share-this-trip) — 'Send this to your travel partner' on hub /india-tours/ (11411),
/golden-triangle-tour/ (11412) and /char-dham-yatra-for-nri/ (11413).
Foreign trips are decided by couples/families: one tap shares the page (+ the pinned itinerary PDF on 11412/11413) via the
visitor's own WhatsApp (api.whatsapp.com/send — NOT wa.me, so the site's #szwap lead popup does not intercept a share to a friend),
email (mailto with no recipient), copy link, or the device share sheet (navigator.share, shown only when supported).
Static canonical URLs (no tracking params). No fetch, no third-party JS, no cookies, nothing stored, no prices.
JS has no '&' and no '//'. Prefix .szh (free on the site, checked 1 Nov 2026)."""
import os, json
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
PDF = 'https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@{}/inbound-kit/trust/widgets/itinerary-pdf/{}'
PAGES = {
    '11411': dict(url='https://suzutravels.com/india-tours/', name='Private India tours with a local team — Suzu Travels',
                  what='this page', pdf=None),
    '11412': dict(url='https://suzutravels.com/golden-triangle-tour/', name='Golden Triangle Tour: Delhi, Agra and Jaipur — Suzu Travels',
                  what='this tour', pdf=PDF.format('ccf7eb01e4b8eb964380cc492eabace05375e4e1', 'golden-triangle-6-day-itinerary-suzu-travels.pdf'),
                  pdfl='6-day itinerary (PDF)'),
    '11413': dict(url='https://suzutravels.com/char-dham-yatra-for-nri/', name='Char Dham Yatra for NRIs — Suzu Travels',
                  what='this yatra', pdf=PDF.format('bc61aa787f9c445478f091cd6498207ef49a886b', 'char-dham-yatra-11-day-itinerary-suzu-travels.pdf'),
                  pdfl='11-day yatra itinerary (PDF)'),
}

CSS = (".szh{font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;margin:0;padding:30px 16px;background:#F4EEDD}"
       ".szh *{box-sizing:border-box}.szh p:empty,.szh br{display:none}"
       ".szh-c{max-width:1100px;margin:0 auto;background:#0E1B14;color:#F4EEDD;border-radius:20px;box-shadow:0 10px 28px rgba(14,27,20,.12);padding:22px;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:18px 26px;align-items:center}"
       ".szh-k{display:block;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#E2C158;font-weight:800;margin-bottom:6px}"
       ".szh-t b{display:block;font-size:22px;line-height:1.25;color:#fff;font-family:Sora,'Plus Jakarta Sans',sans-serif}"
       ".szh-s{display:block;font-size:14px;line-height:1.55;color:#DCD3BC;margin-top:6px}"
       ".szh-b{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}"
       ".szh-b a,.szh-b button{font-family:inherit;display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:12px 14px;border-radius:12px;font-weight:800;font-size:14.5px;line-height:1.15;text-decoration:none!important;min-height:46px;cursor:pointer;border:1px solid #3A4B40;background:#18291F;color:#F4EEDD!important;text-align:center}"
       ".szh-b a:hover,.szh-b button:hover{background:#22342A}"
       ".szh-b .szh-wa{background:#E2C158;border-color:#E2C158;color:#0E1B14!important}.szh-b .szh-wa:hover{background:#F0D27A}"
       ".szh-b .szh-pdf{grid-column:1/-1;background:transparent;border-color:#B8860B;color:#E2C158!important}"
       ".szh-b a:focus-visible,.szh-b button:focus-visible{outline:2px solid #E2C158;outline-offset:2px}"
       ".szh-u{grid-column:1/-1;display:block;font-size:12.5px;color:#DCD3BC;word-break:break-all;padding:2px 2px 0}"
       ".szh-u code{font-family:inherit;color:#fff;background:#18291F;border-radius:6px;padding:2px 6px;user-select:all}"
       ".szh-f{grid-column:1/-1;font-size:12.5px;line-height:1.55;color:#AFA78F;margin:0}"
       ".szh-nojs .szh-js{display:none!important}.szh [hidden]{display:none!important}"
       "@media(max-width:820px){.szh-c{grid-template-columns:minmax(0,1fr)}}"
       "@media(max-width:560px){.szh{padding:24px 12px}.szh-c{padding:18px 16px}.szh-t b{font-size:19px}.szh-b{grid-template-columns:minmax(0,1fr)}}")

WA = ('<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm5.5 12.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2.1-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5 2.4 1 2.9.8 3.6.7.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3z"/></svg>')

JS = ('(function(){var R=document.getElementById("szh");if(!R){return;}R.className=R.className.replace(" szh-nojs","");'
      'var U=R.getAttribute("data-u"),N=R.getAttribute("data-n"),T=R.getAttribute("data-t");'
      'var C=document.getElementById("szh-cp"),S=document.getElementById("szh-sh");'
      'function ok(){if(C){C.textContent="Link copied";setTimeout(function(){C.textContent="Copy link";},2500);}}'
      'function fb(){try{var i=document.createElement("textarea");i.value=U;i.setAttribute("readonly","");i.style.position="fixed";i.style.opacity="0";'
      'document.body.appendChild(i);i.select();document.execCommand("copy");document.body.removeChild(i);ok();}catch(e){if(C){C.textContent="Copy the link below";}}}'
      'if(C){C.addEventListener("click",function(){try{if(navigator.clipboard){navigator.clipboard.writeText(U).then(ok,fb);return;}}catch(e){}fb();});}'
      'if(S){if(navigator.share){S.hidden=false;S.addEventListener("click",function(){try{navigator.share({title:N,text:T,url:U}).catch(function(){});}catch(e){}});}}'
      '})();')

def build(pid):
    p = PAGES[pid]
    NL = '\n'
    text = 'Have a look at ' + p['what'] + ' for our India trip: ' + p['name']
    lines = [text, p['url']]
    if p['pdf']:
        lines += ['Day-by-day plan (PDF): ' + p['pdf']]
    msg = NL.join(lines)
    wa = 'https://api.whatsapp.com/send?text=' + quote(msg)
    em = 'mailto:?subject=' + quote('India trip idea: ' + p['name']) + '&amp;body=' + quote(msg + NL + NL)
    sub = ('Most India trips are decided together — with a partner, family or friends. Send them ' + p['what'] +
           (' and the day-by-day PDF' if p['pdf'] else '') + ' in one tap, then plan it with us when you are both ready.')
    pdfa = ('<a class="szh-pdf" href="' + p['pdf'] + '" target="_blank" rel="noopener">Open the ' + p['pdfl'] + ' to forward</a>') if p['pdf'] else ''
    html = ('<!--szt:share-trip--><section class="szh szh-nojs" id="szh" aria-label="Send this trip to your travel partner" data-u="' + p['url'] +
            '" data-n="' + p['name'] + '" data-t="' + text + '"><style>' + CSS + '</style><div class="szh-c">'
            '<div class="szh-t"><span class="szh-k">Planning with someone?</span><b>Send this to your travel partner</b>'
            '<span class="szh-s">' + sub + '</span></div>'
            '<div class="szh-b"><a class="szh-wa" href="' + wa + '" target="_blank" rel="noopener">' + WA + 'Share on WhatsApp</a>'
            '<a href="' + em + '">Email it</a>'
            '<button type="button" class="szh-js" id="szh-cp">Copy link</button>'
            '<button type="button" class="szh-js" id="szh-sh" hidden>More ways to share</button>' + pdfa +
            '<span class="szh-u">Link: <code>' + p['url'] + '</code></span></div>'
            '<p class="szh-f">These buttons open your own WhatsApp, email app or share menu and you choose who gets it — '
            'nothing is sent to Suzu Travels and nothing is saved by this page.</p>'
            '<script>' + JS + '</script></div></section><!--/szt:share-trip-->')
    return html

if __name__ == '__main__':
    js = JS
    assert '&' not in js and '//' not in js.replace('https:', ''), 'JS must not contain & or //'
    assert '//' not in js
    for pid in PAGES:
        body = build(pid).replace('\n', ' ')
        low = body.lower()
        for bad in ['verified', '24/7', '₹', 'cheapest', 'guarantee', 'government approved', 'dmc', 'online now', 'seats left', 'us$', 'wa.me']:
            assert bad not in low, (pid, bad)
        assert body.count('<!--szt:share-trip-->') == 1
        out = os.path.join(HERE, 'widget-' + pid + '.html')
        open(out, 'w').write(body)
        print(out, len(body))
