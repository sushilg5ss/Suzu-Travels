#!/usr/bin/env python3
"""quote-request-helper (TRUST_BACKLOG row 14) — 'What to send us for a US$ quote' on 11412 + 11413.
Visitor picks tour / dates / travellers / hotels / arrival airport -> one prefilled WhatsApp or email message.
Nothing stored, nothing sent by the page itself (the message opens in the visitor's own WhatsApp / mail app).
No third-party JS, no fetch, no cookies. JS has no '&' and no '//' (URL bases live in data-b attributes; '&' via fromCharCode)."""
import os, json, re

HERE = os.path.dirname(os.path.abspath(__file__))
ALLOWED = json.load(open(os.path.join(HERE, '..', '..', '..', 'data', 'prices.json')))['allowed']

CSS = (".szr{font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;margin:0;padding:34px 16px;background:#F4EEDD;scroll-margin-top:90px}"
       ".szr *{box-sizing:border-box}.szr p:empty,.szr br{display:none}"
       ".szr-c{max-width:1100px;margin:0 auto;background:#fff;border:1px solid #E8DFC8;border-radius:20px;box-shadow:0 10px 28px rgba(14,27,20,.08);overflow:hidden}"
       ".szr-h{background:#0E1B14;color:#F4EEDD;padding:20px 22px}"
       ".szr-k{display:block;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#E2C158;font-weight:800;margin-bottom:6px}"
       ".szr-h b{display:block;font-size:22px;line-height:1.25;color:#fff;font-family:Sora,'Plus Jakarta Sans',sans-serif}"
       ".szr-h span.szr-s{display:block;font-size:14px;line-height:1.55;color:#DCD3BC;margin-top:6px;max-width:760px}"
       ".szr-f{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px 16px;padding:20px 22px 6px}"
       ".szr-f label{display:flex;flex-direction:column;gap:6px;font-size:13px;font-weight:700;color:#0E1B14;min-width:0}"
       ".szr-f label i{font-style:normal;font-weight:800;color:#B8860B;margin-right:4px}"
       ".szr-f input,.szr-f select{width:100%;min-height:44px;padding:10px 12px;border:1px solid #D9CFB4;border-radius:11px;background:#FFFDF7;color:#0E1B14;font:500 15px/1.3 inherit;font-family:inherit}"
       ".szr-f input:focus,.szr-f select:focus{outline:2px solid #E2C158;outline-offset:1px;border-color:#B8860B}"
       ".szr-pair{display:flex;gap:10px}.szr-pair select{flex:1 1 0;min-width:0}"
       ".szr-pv{margin:12px 22px 0;padding:14px 16px;border-radius:14px;background:#FBF8EF;border:1px dashed #D9CFB4;font-size:13.5px;line-height:1.55;color:#3D4A40;white-space:pre-line;word-break:break-word}"
       ".szr-pv b{display:block;color:#0E1B14;font-size:12px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:4px}"
       ".szr-b{display:flex;gap:10px;flex-wrap:wrap;padding:16px 22px 6px}"
       ".szr-b a{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:13px 18px;border-radius:12px;font-weight:800;font-size:15px;line-height:1;text-decoration:none!important;min-height:46px}"
       ".szr-wa{background:#E2C158;color:#0E1B14!important}.szr-wa:hover{background:#F0D27A}"
       ".szr-em{background:#0E1B14;color:#fff!important}.szr-em:hover{background:#22342A}"
       ".szr-fine{font-size:12.5px;line-height:1.55;color:#6B776E;padding:6px 22px 20px;margin:0}"
       "@media(max-width:900px){.szr-f{grid-template-columns:1fr 1fr}}"
       "@media(max-width:560px){.szr{padding:26px 12px}.szr-f{grid-template-columns:1fr;padding:16px 16px 4px}.szr-h{padding:18px 16px}.szr-h b{font-size:19px}"
       ".szr-pv{margin:10px 16px 0}.szr-b{padding:14px 16px 4px}.szr-b a{flex:1 1 100%}.szr-fine{padding:6px 16px 18px}}")

WA = ('<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm5.5 12.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2.1-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5 2.4 1 2.9.8 3.6.7.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3z"/></svg>')

def esc(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;')

def sel(fid, label, opts, num):
    o = ''.join('<option>%s</option>' % esc(x) for x in opts)
    return '<label for="%s"><span><i>%d</i>%s</span><select id="%s" data-q="%s">%s</select></label>' % (fid, num, label, fid, esc(label), o)

def inp(fid, label, ph, num):
    return ('<label for="%s"><span><i>%d</i>%s</span><input id="%s" data-q="%s" type="text" maxlength="80" autocomplete="off" placeholder="%s"></label>'
            % (fid, num, label, fid, esc(label), esc(ph)))

PAGES = {
    11412: dict(
        slug='golden-triangle-tour', kicker='Your US$ quote in 24 hours',
        title='What to send us for an exact US$ quote',
        sub='Six details are all we need for a day-by-day plan and a quote in US dollars. Pick what you know and leave the rest as "Not sure yet" — the message below writes itself.',
        hello='Hi Suzu Travels, please send me a day-by-day plan and a US$ quote for a private Golden Triangle tour.',
        subject='Golden Triangle tour - quote request',
        fields=[
            ('sel', 'szr-tour', 'Which tour', ['Classic Golden Triangle (6 days)', 'Golden Triangle Express (4 days)', 'Golden Triangle + Rishikesh (8 days)', 'Golden Triangle + Kashmir (10 days)', 'Golden Triangle + Himalayas (12 days)', 'Taj Mahal day trip from Delhi', 'Not sure yet']),
            ('inp', 'szr-from', 'Flying in from (country / city)', 'e.g. USA, Chicago'),
            ('inp', 'szr-date', 'Travel dates or month', 'e.g. 12–18 February 2027'),
            ('pax', 'szr-pax', 'Travellers', None),
            ('sel', 'szr-hot', 'Hotel class', ['Not sure yet', '3-star', '4-star', '5-star']),
            ('sel', 'szr-air', 'Arrival airport', ['Delhi (DEL)', 'Jaipur (JAI)', 'Other / not booked yet']),
        ]),
    11413: dict(
        slug='char-dham-yatra-for-nri', kicker='Your US$ quote in 24 hours',
        title='What to send us for an exact US$ yatra quote',
        sub='These details let us plan the right pace and the right car for your family, and quote in US dollars. Pick what you know and leave the rest as "Not sure yet" — the message below writes itself.',
        hello='Namaste Suzu Travels, please send me a day-by-day plan and a US$ quote for the Char Dham Yatra.',
        subject='Char Dham Yatra (NRI) - quote request',
        fields=[
            ('sel', 'szr-tour', 'Which yatra', ['Char Dham Yatra by Road (11 days)', 'Do Dham: Kedarnath and Badrinath (7 days)', 'Char Dham Comfort Yatra (12 days, senior-friendly)', 'Char Dham by Helicopter (6 days)', 'Not sure yet']),
            ('inp', 'szr-from', 'Flying in from (country / city)', 'e.g. UK, Leicester'),
            ('inp', 'szr-date', 'Travel month or dates', 'e.g. May 2027'),
            ('pax', 'szr-pax', 'Pilgrims', None),
            ('inp', 'szr-age', 'Ages of the elders travelling', 'e.g. 68 and 72'),
            ('sel', 'szr-air', 'Arrival airport', ['Delhi (DEL)', 'Dehradun (DED)', 'Other / not booked yet']),
        ]),
}

def build(pid):
    p = PAGES[pid]
    f = ''
    for n, (kind, fid, label, x) in enumerate(p['fields'], 1):
        if kind == 'sel':
            f += sel(fid, label, x, n)
        elif kind == 'inp':
            f += inp(fid, label, x, n)
        else:
            ad = ''.join('<option>%d adult%s</option>' % (i, '' if i == 1 else 's') for i in range(1, 11)) + '<option>More than 10 adults</option>'
            ch = ''.join('<option>%d child%s</option>' % (i, '' if i == 1 else 'ren') for i in range(0, 7))
            f += ('<label for="szr-ad"><span><i>%d</i>%s</span><span class="szr-pair"><select id="szr-ad" data-q="Adults" aria-label="Adults">'
                  '<option>2 adults</option>%s</select><select id="szr-ch" data-q="Children" aria-label="Children (under 12)">%s</select></span></label>'
                  % (n, label, ad.replace('<option>2 adults</option>', ''), ch))
    src = 'sent from the quote helper on suzutravels.com/%s/' % p['slug']
    static_msg = p['hello'] + ' ' + ' / '.join(lbl + ':' for _, _, lbl, _ in p['fields'])
    from urllib.parse import quote
    wa_base = 'https://wa.me/917087488961?text='
    em_base = 'mailto:info@suzutravels.com?subject=' + quote(p['subject'])
    html = ('<!--szt:quote-helper--><section class="szr" id="quote-helper" aria-label="What to send us for a US$ quote"><style>' + CSS +
            ('@media(max-width:768px){body.page-id-%d{max-width:none!important}}' % pid) + '</style>'
            '<div class="szr-c"><div class="szr-h"><span class="szr-k">' + p['kicker'] + '</span><b>' + p['title'] + '</b>'
            '<span class="szr-s">' + esc(p['sub']) + '</span></div>'
            '<div class="szr-f">' + f + '</div>'
            '<div class="szr-pv" aria-live="polite"><b>Your message</b><span id="szr-msg">' + esc(static_msg) + '</span></div>'
            '<div class="szr-b"><a class="szr-wa" id="szr-wa" data-b="' + wa_base + '" href="' + wa_base + quote(static_msg) + '" target="_blank" rel="noopener">' + WA + 'Send on WhatsApp</a>'
            '<a class="szr-em" id="szr-em" data-b="' + em_base + '" href="' + em_base + '">Send by email</a></div>'
            '<p class="szr-fine">Nothing you type here is saved or sent by this page — the message opens in your own WhatsApp or email app and goes only to the Suzu Travels team '
            '(+91 70874 88961 · info@suzutravels.com), who use it only to answer your enquiry. Prices on this page are “from” rates; your quote is exact, in US$.</p>'
            '<script>(function(){'
            'var H=' + json.dumps(p['hello']) + ',S=' + json.dumps(src) + ';'
                        'function g(){var L=[H,""];var F=document.querySelectorAll(".szr [data-q]");var ad="",ch="";'
            'for(var i=0;i<F.length;i++){var e=F[i],q=e.getAttribute("data-q"),x=String(e.value||"").trim();'
            'if(e.id==="szr-ad"){ad=x;continue;}if(e.id==="szr-ch"){ch=x;L.push(' + json.dumps([l for k,_,l,_ in p['fields'] if k=='pax'][0]) + '+": "+ad+(ch.indexOf("0 ")===0?"":", "+ch+" (under 12)"));continue;}'
            'L.push(q+": "+(x||"Not sure yet"));}'
            'L.push("");L.push("("+S+")");return L.join(String.fromCharCode(10));}'
            'function u(){var m=g();var p=document.getElementById("szr-msg");if(p){p.textContent=m;}'
            'var w=document.getElementById("szr-wa");if(w){w.href=w.getAttribute("data-b")+encodeURIComponent(m);}'
            'var em=document.getElementById("szr-em");if(em){em.href=em.getAttribute("data-b")+String.fromCharCode(38)+"body="+encodeURIComponent(m);}}'
            'var y="";try{y=Intl.DateTimeFormat().resolvedOptions().timeZone||"";}catch(e){}'
            'var c=y.indexOf("/")>0?y.split("/").pop().replace(/_/g," "):"";var fr=document.getElementById("szr-from");'
            'if(fr){if(c){if(y.indexOf("Asia/Kolkata")<0){if(y.indexOf("Asia/Calcutta")<0){fr.placeholder="e.g. "+c;}}}}'
            'var R=document.querySelector(".szr");if(R){R.addEventListener("input",u);R.addEventListener("change",u);'
            'var B=R.querySelectorAll(".szr-b a");for(var k=0;k<B.length;k++){B[k].addEventListener("click",u,true);}}'
            'u();})();</script></div></section><!--/szt:quote-helper-->')
    return html

if __name__ == '__main__':
    for pid in PAGES:
        h = build(pid)
        js = h[h.find('<script>'):h.find('</script>')]
        assert '&' not in js and '//' not in js, 'JS must not contain & or //'
        assert '\n' not in h
        low = h.lower()
        for bad in ['verified', '24/7', '₹', 'cheapest', 'guarantee', 'government approved', 'dmc']:
            assert bad not in low, bad
        for n in re.findall(r'US\$\s?([\d,]+)', h):
            assert int(n.replace(',', '')) in ALLOWED, n
        assert h.count('<!--szt:quote-helper-->') == 1
        out = os.path.join(HERE, 'widget-%d.html' % pid)
        open(out, 'w').write(h)
        print(out, len(h))
