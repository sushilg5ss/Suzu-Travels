#!/usr/bin/env python3
"""India Tours hub (11411) v2 skin — three marked inserts, no rebuild (hand-built page rule).
A  <!--szv:skin-->     style block + 'Plan my India trip' card, placed inside .sx-hero before .sx-media
B  <!--szv:currency--> currency view above the signature-tour cards
C  <!--szv:dest-->     'Where in India?' photo destination grid, before the 'Fly to Delhi' section
"""
import html, json, os
U = 'https://suzutravels.com/wp-content/uploads/'
P = 11411

SKIN_CSS = r"""
body.page-id-PID{--teal:#0E1B14;--teal-deep:#0E1B14;--teal-light:#F4EEDD}
body.page-id-PID .sx{--g:#0E1B14;--g2:#8A6A12;--g3:#B8860B}
body.page-id-PID .page-content{position:relative;padding-top:22px!important}
body.page-id-PID .page-header{position:absolute!important;z-index:6;top:22px;left:24px;right:24px;min-height:0!important;margin:0!important;background:none!important;padding:54px 52px 0!important;pointer-events:none;border-radius:0!important;display:block!important}
body.page-id-PID .page-header:before{background:#E2C158!important;color:#1a1606!important;margin-bottom:16px!important}
body.page-id-PID .page-header .entry-title{font-size:clamp(34px,4.1vw,56px)!important;max-width:17ch!important;line-height:1.05!important;text-shadow:0 2px 26px rgba(0,0,0,.45)!important}
body.page-id-PID .sx .sx-hero{position:relative;isolation:isolate;overflow:hidden;border-radius:28px!important;min-height:740px;padding:262px 52px 92px!important;background:#0b1510!important;grid-template-columns:minmax(0,1.12fr) minmax(0,.88fr)!important;gap:36px!important;align-items:end!important;margin-top:0!important}
body.page-id-PID .sx .sx-hero .sx-media{position:absolute!important;inset:0!important;z-index:-2;border-radius:0!important;aspect-ratio:auto!important;box-shadow:none!important;border:0!important;margin:0!important;width:auto!important;height:auto!important}
body.page-id-PID .sx .sx-hero:after{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;background:linear-gradient(180deg,rgba(6,12,9,.74) 0%,rgba(6,12,9,.22) 30%,rgba(6,12,9,.40) 58%,rgba(6,12,9,.92) 100%),linear-gradient(90deg,rgba(6,12,9,.62) 0%,rgba(6,12,9,0) 64%)}
body.page-id-PID .sx-hero .szs:after{display:none}
body.page-id-PID .sx-hero .szs figcaption{left:auto!important;right:22px;top:22px;bottom:auto!important}
body.page-id-PID .sx-hero .sx-crumb{color:#cfd8d1}
body.page-id-PID .sx-hero .sx-crumb a{color:#F0D57A!important}
body.page-id-PID .sx-hero .sx-lede{font-size:18.5px!important;line-height:1.62!important;color:#F2F5F1!important;text-shadow:0 1px 14px rgba(0,0,0,.4);max-width:56ch}
body.page-id-PID .sx-hero .si-badge{background:rgba(255,255,255,.12)!important;border:1px solid rgba(255,255,255,.24)!important;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
body.page-id-PID .lp-facts{position:relative;z-index:3;margin-top:-58px!important}
body.page-id-PID .lp-sec.alt{background:#FAF8F3!important}
body.page-id-PID .lp-card{border-radius:20px!important;overflow:hidden;box-shadow:0 10px 28px rgba(14,27,20,.08)!important;transition:transform .25s,box-shadow .25s}
body.page-id-PID .lp-card:hover{transform:translateY(-4px);box-shadow:0 20px 40px rgba(14,27,20,.14)!important}
body.page-id-PID .lp-card img{transition:transform .6s}
body.page-id-PID .lp-card:hover img{transform:scale(1.04)}
body.page-id-PID .lp-card .foot .q{background:linear-gradient(135deg,#E2C158,#B8860B)!important;color:#1a1606!important;font-weight:800!important}
body.page-id-PID .lp-card .foot .d{background:#fff!important;color:#0E1B14!important;border:1px solid #DCD6C6}
body.page-id-PID .lp-tag{background:#F4EEDD!important;color:#5c4708!important}
body.page-id-PID .lp-price b{color:#0E1B14!important}
body.page-id-PID .lp-day .n{background:#0E1B14!important;color:#E2C158!important}
body.page-id-PID .lp-table th{background:#0E1B14!important}
body.page-id-PID .lp-why div{background:#0E1B14!important}
body.page-id-PID .lp-mapwrap{background:radial-gradient(at 62% 38%,#1b2a3a,#0a1220 72%)!important}
body.page-id-PID .lp-map .land{fill:#2b3d52!important;fill-opacity:.75!important;stroke:#5a7390!important;stroke-opacity:.45!important}
body.page-id-PID .lp-map .lb{fill:#e6edf5!important}
body.page-id-PID .lp-cta{position:relative;isolation:isolate;overflow:hidden;background:#0b1510 url("UPLD2026/10/suzu-india-manali-himalaya.webp") center 40%/cover no-repeat!important;padding:56px 48px!important}
body.page-id-PID .lp-cta:before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(6,12,9,.88) 0%,rgba(6,12,9,.55) 60%,rgba(6,12,9,.35) 100%)}
body.page-id-PID .lp-btn.line{border-color:#fff!important;background:rgba(255,255,255,.1)!important;color:#fff!important}
body.page-id-PID .szt-ic{background:#F4EEDD!important;color:#8A6A12!important}
body.page-id-PID .szt-talk{background:#0E1B14!important}
/* planner card */
.szp{position:relative;z-index:2;background:rgba(255,255,255,.96);color:#1E2A22;border-radius:22px;padding:22px 22px 18px;box-shadow:0 30px 60px rgba(0,0,0,.35);border:1px solid rgba(255,255,255,.6);font-family:'Plus Jakarta Sans',system-ui,sans-serif}
.szp *{box-sizing:border-box}.szp br{display:none}.szp p:empty{display:none}
.szp h3{font-family:'Sora','Plus Jakarta Sans',sans-serif;font-size:19px;color:#0E1B14;margin:0 0 4px;font-weight:800}
.szp .szp-sub{font-size:13.5px;color:#55645A;margin:0 0 12px;line-height:1.5}
.szp .szp-chips{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 12px}
.szp .szp-chips label{cursor:pointer;font-size:12.5px;font-weight:700;color:#0E1B14;border:1px solid #DCD6C6;border-radius:999px;padding:6px 10px;user-select:none;transition:all .15s;background:#fff}
.szp .szp-chips input{position:absolute;opacity:0;pointer-events:none}
.szp .szp-chips label:has(input:checked){background:#0E1B14;color:#F0D57A;border-color:#0E1B14}
.szp .szp-f{display:grid;grid-template-columns:1fr 1fr;gap:9px}
.szp .szp-f label.f{display:block;font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#55645A}
.szp .szp-f select,.szp .szp-f input{display:block;width:100%;margin-top:4px;font:600 14.5px/1.2 'Plus Jakarta Sans',system-ui,sans-serif;color:#0E1B14;background:#F4F5F1;border:1px solid #E3E7E1;border-radius:11px;padding:11px;min-height:44px}
.szp .szp-go{display:flex;gap:8px;margin-top:12px}
.szp .szp-go button{flex:1;display:inline-flex;align-items:center;justify-content:center;gap:7px;border:0;border-radius:12px;padding:14px 12px;font:800 14.5px/1 'Plus Jakarta Sans',sans-serif;cursor:pointer}
.szp .szp-wa{background:linear-gradient(135deg,#25D366,#128C4A);color:#fff}
.szp .szp-em{background:#0E1B14;color:#fff;flex:0 0 auto!important;padding:14px 16px!important}
.szp small{display:block;text-align:center;color:#6B776E;font-size:11.5px;margin-top:8px;line-height:1.4}
@media(max-width:1100px){body.page-id-PID .sx .sx-hero{grid-template-columns:1fr!important;align-items:start!important}.szp{max-width:560px}}
@media(max-width:700px){body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0!important}body.page-id-PID .page-header .entry-title{font-size:32px!important}body.page-id-PID .page-header:before{font-size:10px!important;letter-spacing:.1em!important}body.page-id-PID .sx .sx-hero{padding:250px 18px 70px!important;border-radius:22px!important;min-height:0}body.page-id-PID .sx-hero .sx-lede{font-size:16px!important}body.page-id-PID .sx-hero .szs figcaption{display:none}.szp{padding:18px 15px 14px;border-radius:18px}body.page-id-PID .lp-cta{padding:30px 20px!important}}
@media(max-width:768px){body.page-id-PID{max-width:none!important}}
""".replace('PID', str(P)).replace('UPLD', U)

PLACES = ['Golden Triangle', 'Himachal (Shimla · Manali)', 'Kashmir', 'Rishikesh & Haridwar', 'Char Dham', 'Varanasi', 'Rajasthan', 'Amritsar', 'Ladakh', 'Kerala', 'Goa', 'Not sure yet']

def planner():
    chips = ''.join(f'<label><input type="checkbox" name="r" value="{html.escape(p)}"{" checked" if i == 0 else ""}>{html.escape(p)}</label>' for i, p in enumerate(PLACES))
    months = ['Not sure yet'] + [f'{m} {y}' for y, ms in ((2026, ['November', 'December']), (2027, ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])) for m in ms]
    mo = ''.join(f'<option>{m}</option>' for m in months)
    days = ''.join(f'<option{" selected" if d == "10–12 days" else ""}>{d}</option>' for d in ['5–7 days', '8–9 days', '10–12 days', '13–15 days', '16+ days'])
    hotel = ''.join(f'<option>{h}</option>' for h in ['Comfortable 3★', 'Premium 4★', 'Luxury 5★ / heritage'])
    trav = ''.join(f'<option{" selected" if t == "2" else ""}>{t}</option>' for t in ['1', '2', '3', '4', '5–6', '7–10', '11+'])
    return ('<form class="szp" id="szpForm" aria-label="Plan my India trip">'
            '<h3>Plan my India trip</h3><p class="szp-sub">Pick what you would like to see. We reply with a day-by-day plan and a US$ quote, usually within 24 hours.</p>'
            f'<div class="szp-chips">{chips}</div>'
            '<div class="szp-f">'
            f'<label class="f">Arrival month<select name="m">{mo}</select></label>'
            f'<label class="f">Trip length<select name="d">{days}</select></label>'
            f'<label class="f">Travellers<select name="t">{trav}</select></label>'
            f'<label class="f">Hotels<select name="h">{hotel}</select></label>'
            '</div>'
            '<div class="szp-go"><button class="szp-wa" type="submit" name="via" value="wa">WhatsApp my plan</button><button class="szp-em" type="button" id="szpEm">Email</button></div>'
            '<small>Opens WhatsApp or your email with the details filled in. Nothing is stored on this page.</small>'
            '</form>')

PLANNER_JS = ("(function(){var f=document.getElementById('szpForm');if(!f){return;}"
              "function msg(){var r=[],c=f.querySelectorAll('input[name=r]');for(var i=0;i<c.length;i++){if(c[i].checked){r.push(c[i].value);}}"
              "var N=String.fromCharCode(10);var tz='';try{tz=Intl.DateTimeFormat().resolvedOptions().timeZone||'';}catch(e){}"
              "var t='Hello Suzu Travels, please plan my India trip.'+N+'Places: '+(r.length?r.join(', '):'Not sure yet')+''+N+'Arrival: '+f.querySelector('[name=m]').value+''+N+'Length: '+f.querySelector('[name=d]').value+''+N+'Travellers: '+f.querySelector('[name=t]').value+''+N+'Hotels: '+f.querySelector('[name=h]').value;"
              "if(tz){t=t+''+N+'My time zone: '+tz;}return t;}"
              "f.addEventListener('submit',function(e){e.preventDefault();window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(msg()),'_blank','noopener');});"
              "var em=document.getElementById('szpEm');if(em){em.addEventListener('click',function(){location.href='mailto:info@suzutravels.com?subject='+encodeURIComponent('India trip plan')+String.fromCharCode(38)+'body='+encodeURIComponent(msg());});}"
              "function fit(){var h=document.querySelector('body.page-id-PID .page-header'),s=document.querySelector('body.page-id-PID .sx-hero');if(h){if(s){s.style.setProperty('padding-top',(h.offsetHeight+30)+'px','important');}}}"
              "fit();window.addEventListener('load',fit);window.addEventListener('resize',fit);"
              "})();").replace('PID', str(P))

def block_skin():
    css = ' '.join(l.strip() for l in SKIN_CSS.strip().splitlines() if l.strip() and not l.strip().startswith('/*'))
    return ('<!--szv:skin--><style>' + css + '</style>' + planner() + '<script>' + PLANNER_JS + '</script><!--/szv:skin-->')

# ---------- B: currency
CUR_CSS = (".szx{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:6px 0 18px;font-family:'Plus Jakarta Sans',system-ui,sans-serif}"
           ".szx span{font-size:13px;font-weight:700;color:#55645A;margin-right:4px}"
           ".szx button{border:1px solid #DCD6C6;background:#fff;color:#0E1B14;font:800 13px/1 'Plus Jakarta Sans',sans-serif;padding:9px 12px;border-radius:999px;cursor:pointer}"
           ".szx button[aria-pressed=true]{background:#0E1B14;color:#F0D57A;border-color:#0E1B14}"
           ".szx em{font-style:normal;font-size:12px;color:#6B776E;flex-basis:100%}"
           ".lp-price .szc-x{display:block;font-size:13px;color:#6B776E;font-weight:600;margin-top:2px}")
CUR_JS = ("(function(){var box=document.getElementById('szCur');if(!box){return;}"
          "var S={USD:'US$',GBP:'£',EUR:'€',AUD:'A$',CAD:'C$'};var R=null;"
          "function each(fn){var b=document.querySelectorAll('.lp-price b');for(var i=0;i<b.length;i++){fn(b[i]);}}"
          "function show(c){var btn=box.querySelectorAll('button');for(var i=0;i<btn.length;i++){btn[i].setAttribute('aria-pressed',btn[i].getAttribute('data-c')===c?'true':'false');}"
          "each(function(b){var p=b.parentNode;var x=p.querySelector('.szc-x');if(!x){x=document.createElement('span');x.className='szc-x';p.appendChild(x);}"
          "var n=parseFloat((b.textContent||'').replace(/[^0-9.]/g,''));if(c==='USD'||!R||!R[c]||!n){x.textContent='';return;}"
          "x.textContent='≈ '+S[c]+Math.round(n*R[c]).toLocaleString('en-GB')+' (approx.)';});}"
          "box.addEventListener('click',function(e){var c=e.target.getAttribute('data-c');if(!c){return;}"
          "if(R||c==='USD'){show(c);return;}"
          "var u='https:'+String.fromCharCode(47,47)+'api.frankfurter.dev/v1/latest?base=USD';"
          "fetch(u).then(function(r){return r.json();}).then(function(j){R=j.rates;show(c);}).catch(function(){box.querySelector('em').textContent='Live rates unavailable right now — all quotes are in US$.';});});"
          "})();")

def block_currency():
    btns = ''.join(f'<button type="button" data-c="{c}" aria-pressed="{"true" if c == "USD" else "false"}">{s}</button>' for c, s in (('USD', 'US$'), ('GBP', '£ GBP'), ('EUR', '€ EUR'), ('AUD', 'A$ AUD'), ('CAD', 'C$ CAD')))
    return ('<!--szv:currency--><div class="szx" id="szCur"><style>' + CUR_CSS + '</style><span>Show prices in</span>' + btns +
            '<em>Approximate conversions at today\'s European Central Bank rate. Quotes and payment are in US$.</em>'
            '<script>' + CUR_JS + '</script></div><!--/szv:currency-->')

# ---------- C: destinations
WA = 'https://wa.me/917087488961?text='
def wa(t):
    from urllib.parse import quote
    return WA + quote(t, safe='')

DEST = [
    ('Golden Triangle', 'Delhi · Agra · Jaipur', U + '2026/10/suzu-india-taj-mahal-sunrise-768x553.webp', 'Taj Mahal at sunrise reflected in the long pool, Agra', 'https://suzutravels.com/golden-triangle-tour/', 'from US$299', 'See tours'),
    ('Himachal Himalayas', 'Shimla · Manali · Dharamshala', U + '2026/10/suzu-india-manali-himalaya-768x412.webp', 'Manali town below snow-covered Himalayan peaks, Himachal Pradesh', '#north-india-tour-packages-in-us-dollars', 'Our home state', 'See tours'),
    ('Kashmir', 'Srinagar · Gulmarg · Pahalgam', U + '2026/10/kashmir-shikara-ride-dal-lake-srinagar-winter-768x576.webp', 'Shikara ride on Dal Lake, Srinagar, in winter — Suzu Travels guests', '#north-india-tour-packages-in-us-dollars', 'Own ground team', 'See tours'),
    ('Rishikesh & Haridwar', 'Yoga, Ganga Aarti, ashrams', U + '2026/04/Dashing-Rishikesh-768x512.webp', 'Rishikesh on the Ganges, Uttarakhand', '#north-india-tour-packages-in-us-dollars', 'from US$649', 'See tours'),
    ('Char Dham Yatra', 'For NRIs & overseas pilgrims', U + '2026/05/Char-Dham-Yatra-768x512.webp', 'Badrinath temple, Char Dham Yatra, Uttarakhand', 'https://suzutravels.com/char-dham-yatra-for-nri/', 'from US$799', 'See the yatra'),
    ('Private car & driver', 'Your own car for the whole trip', U + '2026/09/guests/suzu-travels-tempo-traveller-road-trip.webp', 'Suzu Travels guests on a road trip by tempo traveller', 'https://suzutravels.com/india-tours/private-driver-india/', 'English-speaking driver', 'How it works'),
    ('Varanasi', 'Ghats, boats and the Ganga Aarti', U + '2026/10/suzu-india-varanasi-ghats-768x512.webp', 'Boats on the Ganges below the ghats of Varanasi', None, 'Add-on or own trip', 'Ask for a plan'),
    ('Rajasthan', 'Jaipur · Udaipur · Jodhpur · Jaisalmer', U + '2026/10/suzu-india-hawa-mahal-jaipur-768x512.webp', 'Decorated horses passing Hawa Mahal, Jaipur', None, 'Forts & palaces', 'Ask for a plan'),
    ('Ladakh', 'Leh · Nubra · Pangong (May–Sep)', U + '2026/10/suzu-india-ladakh-pangong.webp', 'Pangong Tso lake and mountains, Ladakh', None, 'High Himalaya', 'Ask for a plan'),
    ('Kerala', 'Backwaters · Munnar · Kochi', U + '2026/10/suzu-india-kerala-backwaters.webp', 'Houseboat on the Alappuzha backwaters, Kerala', None, 'We arrange', 'Ask for a plan'),
    ('Goa', 'Beaches and old Portuguese towns', U + '2026/10/suzu-india-goa-baga-beach.webp', 'Yellow beach umbrellas and loungers on Baga beach, Goa', None, 'We arrange', 'Ask for a plan'),
    ('Amritsar', 'Golden Temple · Wagah border', U + '2026/04/Amritsar-by-suzu-Travels.webp', 'Golden Temple, Amritsar, lit up at night', '#north-india-tour-packages-in-us-dollars', 'from US$949', 'See tours'),
]
DEST_CSS = (".szd{font-family:'Plus Jakarta Sans',system-ui,sans-serif}.szd *{box-sizing:border-box}.szd br{display:none}.szd p:empty{display:none}"
            ".szd-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:22px}"
            ".szd a.szd-c{position:relative;display:block;border-radius:20px;overflow:hidden;aspect-ratio:4/5;color:#fff!important;text-decoration:none!important;background:#0b1510;isolation:isolate;box-shadow:0 10px 26px rgba(14,27,20,.14)}"
            ".szd a.szd-c img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;margin:0;z-index:-2;transition:transform .7s cubic-bezier(.2,.7,.2,1)}"
            ".szd a.szd-c:after{content:'';position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(0,0,0,0) 38%,rgba(5,10,7,.88) 100%)}"
            ".szd a.szd-c:hover img{transform:scale(1.07)}"
            ".szd .szd-t{position:absolute;top:12px;left:12px;background:rgba(255,255,255,.93);color:#0E1B14;font-size:11.5px;font-weight:800;padding:6px 10px;border-radius:999px}"
            ".szd .szd-b{position:absolute;left:16px;right:16px;bottom:14px}"
            ".szd .szd-b b{display:block;font-family:'Sora','Plus Jakarta Sans',sans-serif;font-size:21px;line-height:1.15;font-weight:800;letter-spacing:-.02em}"
            ".szd .szd-b em{display:block;font-style:normal;font-size:13px;color:#E6EBE6;margin-top:3px;line-height:1.4}"
            ".szd .szd-b i{display:inline-block;font-style:normal;font-size:12.5px;font-weight:800;color:#F0D57A;margin-top:7px}"
            ".szd .szd-note{font-size:13px;color:#6B776E;margin-top:14px}"
            "@media(max-width:1000px){.szd-grid{grid-template-columns:repeat(3,minmax(0,1fr))}}"
            "@media(max-width:700px){.szd-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.szd a.szd-c{border-radius:16px}.szd .szd-b{left:11px;right:11px;bottom:11px}.szd .szd-b b{font-size:16.5px}.szd .szd-b em{font-size:11.5px}.szd .szd-b i{display:none}.szd .szd-t{font-size:10px;padding:5px 8px;top:9px;left:9px}}")

def block_dest():
    cards = []
    for name, sub, img, alt, link, tag, cta in DEST:
        href = link or wa(f'Hello Suzu Travels, I would like a private tour plan and a US$ quote for {name}. My dates: ___ , travellers: ___ , country: ___')
        ext = '' if link else ' target="_blank" rel="noopener"'
        cards.append(f'<a class="szd-c" href="{html.escape(href, quote=True)}"{ext}><img src="{img}" alt="{html.escape(alt, quote=True)}" width="600" height="750" loading="lazy" decoding="async"><span class="szd-t">{html.escape(tag)}</span><span class="szd-b"><b>{html.escape(name)}</b><em>{html.escape(sub)}</em><i>{html.escape(cta)} →</i></span></a>')
    return ('<!--szv:dest--><section class="lp-sec szd" id="where-in-india" style="scroll-margin-top:90px"><style>' + DEST_CSS + '</style><div class="lp-wrap">'
            '<span class="lp-eyebrow">Where in India?</span><h2>Choose Your India: From the Taj Mahal to the Himalayas</h2>'
            '<p class="lp-lead">Start with the Golden Triangle, then add mountains, spirituality or the coast. Our own team runs the North; for Kerala and Goa we arrange trusted local partners and stay your single point of contact.</p>'
            '<div class="szd-grid">' + ''.join(cards) + '</div>'
            '<p class="szd-note">Not sure how to combine them? Use “Plan my India trip” at the top of this page, or WhatsApp +91 70874 88961 — a real person in our Himachal office replies.</p>'
            '</div></section><!--/szv:dest-->')

if __name__ == '__main__':
    out = {'skin': block_skin(), 'currency': block_currency(), 'dest': block_dest()}
    for k, v in out.items():
        assert '\n' not in v
        for s in v.split('<script>')[1:]:
            js = s.split('</script>')[0]
            assert '&' not in js and '//' not in js, (k, 'JS must not contain & or //')
        open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{k}.html'), 'w').write(v)
        print(k, len(v))
