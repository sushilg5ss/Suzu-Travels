#!/usr/bin/env python3
"""Build the three policy pages (post_content HTML, one line, safe for wpautop) + a local preview shell."""
import json, os, re
from content import ALL, UPDATED, PHONE, PHONE_TEL, EMAIL, WA, L_PAY

HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)

I = {  # 24px stroke icons
    'lock': '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    'x': '<circle cx="12" cy="12" r="9"/><path d="M15 9l-6 6M9 9l6 6"/>',
    'cal': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18M9 15l2 2 4-4"/>',
    'back': '<path d="M9 14L4 9l5-5"/><path d="M4 9h11a5 5 0 0 1 0 10h-3"/>',
    'doc': '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
    'id': '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M6 16c.6-1.5 1.7-2 3-2s2.4.5 3 2M14 10h4M14 13h3"/>',
    'help': '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    'shield': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    'card': '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h4"/>',
    'share': '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 13.5l6.8 4M15.4 6.5l-6.8 4"/>',
    'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>',
}
WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2s.2-1.1.2-1.2-.2-.2-.4-.3z"/></svg>'


def icon(k):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[k]}</svg>'


CSS = '''
.pl{--g:#122615;--g2:#1B5E20;--gold:#D4AF37;--gold2:#B8860B;--cream:#F9FAF5;--line:#E3E9E3;--ink:#1f2a22;--mut:#4A5D4E;font-family:'Plus Jakarta Sans','Sora',system-ui,-apple-system,'Segoe UI',sans-serif;color:var(--ink);font-size:16.5px;line-height:1.75}
.pl *{box-sizing:border-box}.pl br.x{display:none}.pl p:empty{display:none}
.pl a{color:var(--g2);text-decoration:underline;text-decoration-color:rgba(27,94,32,.35);text-underline-offset:3px}
.pl a:hover{text-decoration-color:var(--g2)}
.pl .pl-top{background:linear-gradient(180deg,#18401f 0%,#1B5E20 100%);color:#E6EFE8;border-radius:0 0 26px 26px;padding:6px 40px 34px;margin:0 0 26px}
.pl .pl-intro{font-size:17.5px;max-width:74ch;margin:0 0 18px;color:#E6EFE8}
.pl .pl-meta{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 20px}
.pl .pl-meta span{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.09);border:1px solid rgba(212,175,55,.45);color:#fff;padding:6px 12px;border-radius:999px;font-size:13px;font-weight:600;line-height:1.2}
.pl .pl-meta span:before{content:"";width:6px;height:6px;border-radius:50%;background:var(--gold)}
.pl .pl-tabs{display:flex;flex-wrap:wrap;gap:8px}
.pl .pl-tabs a{flex:none;text-decoration:none;font-size:14px;font-weight:700;padding:9px 16px;border-radius:12px;color:#fff;border:1.5px solid rgba(255,255,255,.3);background:rgba(255,255,255,.06);transition:background .2s,border-color .2s}
.pl .pl-tabs a:hover{background:rgba(255,255,255,.14)}
.pl .pl-tabs a[aria-current]{background:var(--gold);border-color:var(--gold);color:#122615}
.pl .pl-glance{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;margin:0 0 34px}
.pl .pl-card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;box-shadow:0 2px 10px rgba(18,38,21,.05)}
.pl .pl-card svg{width:38px;height:38px;padding:8px;border-radius:11px;background:rgba(46,125,50,.09);color:var(--g2);display:block;margin:0 0 10px}
.pl .pl-card b{display:block;color:var(--g);font-family:'Sora','Plus Jakarta Sans',sans-serif;font-size:15.5px;line-height:1.35;margin:0 0 4px}
.pl .pl-card span{display:block;color:var(--mut);font-size:14px;line-height:1.55}
.pl .pl-grid{display:grid;grid-template-columns:250px minmax(0,1fr);gap:40px;align-items:start}
.pl .pl-toc{position:sticky;top:110px;background:var(--cream);border:1px solid var(--line);border-radius:16px;padding:16px 10px 12px}
.pl .pl-toc b{display:block;font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);margin:0 8px 8px;font-weight:800}
.pl .pl-toc a{display:flex;gap:8px;text-decoration:none;color:var(--g);font-size:14px;font-weight:600;line-height:1.35;padding:7px 8px;border-radius:9px}
.pl .pl-toc a i{font-style:normal;color:var(--gold2);font-weight:800;min-width:20px}
.pl .pl-toc a:hover{background:#fff}
.pl .pl-body{max-width:780px}
.pl .pl-sec{padding:0 0 28px;margin:0 0 28px;border-bottom:1px solid var(--line);scroll-margin-top:110px}
.pl .pl-sec:last-child{border-bottom:0}
.pl .pl-sec h2{display:flex;align-items:baseline;gap:12px;font-family:'Sora','Plus Jakarta Sans',sans-serif;color:var(--g);font-size:clamp(21px,2.2vw,26px);line-height:1.25;letter-spacing:-.02em;margin:0 0 12px;font-weight:800}
.pl .pl-sec h2 span{flex:none;font-size:13px;font-weight:800;color:var(--gold2);background:#FFF8E6;border:1px solid #EBD9A3;border-radius:8px;padding:3px 8px;letter-spacing:.04em;position:relative;top:-3px}
.pl .pl-sec h3{font-family:'Sora','Plus Jakarta Sans',sans-serif;color:var(--g);font-size:17px;margin:18px 0 8px;font-weight:700}
.pl .pl-sec p{margin:0 0 12px;color:#2c3a30}
.pl .pl-sec ul{list-style:none;margin:0 0 12px;padding:0}
.pl .pl-sec li{position:relative;padding:0 0 0 24px;margin:0 0 9px;color:#2c3a30}
.pl .pl-sec li:before{content:"";position:absolute;left:4px;top:.72em;width:7px;height:7px;border-radius:50%;background:var(--gold)}
.pl .pl-sec b{color:var(--g)}
.pl .pl-note{background:#FFF8E6;border:1px solid #EBD9A3;border-left:4px solid var(--gold);border-radius:12px;padding:14px 16px;margin:14px 0 0;font-size:15px;color:#5f501a}
.pl .pl-note b{color:#5f501a}
.pl .pl-help{background:radial-gradient(120% 140% at 10% 0%,#1B5E20 0%,#122615 60%);color:#fff;border-radius:24px;padding:36px 32px;margin:18px 0 8px;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:22px;align-items:center}
.pl .pl-help h2{color:#fff;font-family:'Sora','Plus Jakarta Sans',sans-serif;font-size:clamp(22px,2.4vw,28px);margin:0 0 6px;line-height:1.2}
.pl .pl-help p{margin:0;color:#E4EDE6;max-width:56ch}
.pl .pl-ctas{display:flex;flex-wrap:wrap;gap:10px}
.pl .pl-ctas a{display:inline-flex;align-items:center;gap:8px;text-decoration:none;font-weight:800;font-size:15px;padding:13px 20px;border-radius:14px;line-height:1.2}
.pl .pl-ctas a svg{width:19px;height:19px}
.pl .pl-ctas .wa{background:#1FA855;color:#fff}
.pl .pl-ctas .call{background:linear-gradient(135deg,#D4AF37,#B8860B);color:#122615}
.pl .pl-ctas .mail{background:rgba(255,255,255,.1);border:1.5px solid rgba(255,255,255,.35);color:#fff}
@media(max-width:1100px){.pl .pl-glance{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:900px){.pl .pl-top{padding:4px 20px 26px}.pl .pl-grid{grid-template-columns:1fr;gap:0}
.pl .pl-toc{position:static;display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;background:none;border:0;border-bottom:1px solid var(--line);border-radius:0;padding:0 0 14px;margin:0 0 24px}
.pl .pl-toc::-webkit-scrollbar{display:none}.pl .pl-toc b{display:none}
.pl .pl-toc a{flex:none;border:1px solid var(--line);background:#fff;border-radius:999px;padding:8px 14px}
.pl .pl-help{grid-template-columns:1fr;padding:28px 20px}}
@media(max-width:600px){.pl{font-size:16px}.pl .pl-glance{grid-template-columns:1fr}.pl .pl-card{display:grid;grid-template-columns:38px 1fr;gap:0 12px}.pl .pl-card svg{grid-row:span 2;margin:0}
.pl .pl-tabs a{flex:1 1 auto;text-align:center}.pl .pl-ctas a{flex:1 1 auto;justify-content:center}}
'''.replace('\n', '')


def header_css(pid, eyebrow):
    b = f'body.page-id-{pid}'
    return (f'{b} .page-content{{padding-top:22px!important}}'
            f'{b} .page-header{{background:linear-gradient(180deg,#122615 0%,#18401f 100%);border-radius:26px 26px 0 0;padding:44px 40px 18px;margin:0!important;display:flex;flex-direction:column;align-items:flex-start}}'
            f'{b} .page-header:before{{content:"Legal \\00B7  {eyebrow}";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.16em;text-transform:uppercase;color:#122615;background:#D4AF37;padding:7px 12px;border-radius:999px;margin-bottom:14px}}'
            f'{b} .page-header .entry-title{{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(30px,3.8vw,48px)!important;line-height:1.1!important;letter-spacing:-.03em!important;margin:0!important;font-weight:800!important}}'
            f'{b} .entry-content{{margin-top:0!important}}{b} .entry-content>p:empty{{display:none}}'
            f'@media(max-width:900px){{{b} .page-header{{padding:28px 20px 12px;border-radius:20px 20px 0 0}}{b} .page-content{{padding-left:14px!important;padding-right:14px!important}}}}')


def oneline(s):
    return re.sub(r'\s*\n\s*', ' ', s).strip()


def build(p):
    tabs = ''.join(f'<a href="https://suzutravels.com/{q["slug"]}/"' + (' aria-current="page"' if q is p else '') + f'>{q["short"]}</a>' for q in ALL)
    tabs += f'<a href="{L_PAY}">Payments</a>'
    glance = ''.join(f'<div class="pl-card">{icon(k)}<b>{t}</b><span>{d}</span></div>' for k, t, d in p['glance'])
    toc = ''.join(f'<a href="#{sid}"><i>{n:02d}</i>{t}</a>' for n, (sid, t, _) in enumerate(p['sections'], 1))
    secs = ''.join(f'<section class="pl-sec" id="{sid}"><h2><span>{n:02d}</span>{t}</h2>{oneline(body)}</section>'
                   for n, (sid, t, body) in enumerate(p['sections'], 1))
    help_ = (f'<section class="pl-help"><div><h2>Questions about this policy?</h2><p>Talk to the Suzu Travels team on WhatsApp, '
             f'by phone or by email. We are happy to explain anything before you book.</p></div><div class="pl-ctas">'
             f'<a class="wa" href="{WA}" target="_blank" rel="noopener">{WA_ICON}WhatsApp</a>'
             f'<a class="call" href="tel:{PHONE_TEL}">Call {PHONE}</a><a class="mail" href="mailto:{EMAIL}">Email us</a></div></section>')
    html = (f'<div class="pl"><style>{CSS}{header_css(p["pid"], p["eyebrow"])}</style>'
            f'<section class="pl-top"><p class="pl-intro">{p["intro"]}</p>'
            f'<div class="pl-meta"><span>Last updated {UPDATED}</span><span>Suzu Travels, Himachal Pradesh</span></div>'
            f'<nav class="pl-tabs" aria-label="Policies">{tabs}</nav></section>'
            f'<div class="pl-glance">{glance}</div>'
            f'<div class="pl-grid"><nav class="pl-toc" aria-label="On this page"><b>On this page</b>{toc}</nav>'
            f'<div class="pl-body">{secs}</div></div>{help_}</div>')
    assert '\n' not in html
    return html


if __name__ == '__main__':
    meta = {}
    for p in ALL:
        h = build(p)
        open(os.path.join(HERE, 'out', f'{p["pid"]}.html'), 'w').write(h)
        meta[p['pid']] = dict(slug=p['slug'], title=p['title'], seo_title=p['seo_title'], seo_desc=p['seo_desc'])
        print(p['pid'], p['slug'], len(h), 'sections', len(p['sections']), 'desc', len(p['seo_desc']))
    json.dump(meta, open(os.path.join(HERE, 'out', 'meta.json'), 'w'), indent=1, ensure_ascii=False)
