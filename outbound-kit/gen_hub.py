#!/usr/bin/env python3
"""Build the redesigned Holidays Abroad hub (WP page 11347) as ONE line of HTML.
Reads photos/wp_map.json  {slug: {"url": ..., "alt": ..., "credit": ..., "license": ..., "src": ...}}
Writes hub.html (one line) ready for wp_update_page.
"""
import json, html, re, sys

M = json.load(open('photos/wp_map.json'))
PID = 11347
WA = "https://wa.me/917087488961?text="

def u(slug):
    return M[slug]['url']

def m(slug):
    return M[slug].get('med') or M[slug]['url']

def alt(slug):
    return html.escape(M[slug]['alt'], quote=True)

def wa(text):
    from urllib.parse import quote
    return WA + quote(text, safe='')

CSS = r"""
.hx{--ink:#0E1B14;--ink2:#14261B;--g:#1B5E20;--gold:#D4AF37;--gold2:#B8860B;--cream:#F8F7F2;--line:#E6E8E2;--mut:#55645A;--txt:#1E2A22;font-family:'Plus Jakarta Sans','Sora',system-ui,-apple-system,'Segoe UI',sans-serif;color:var(--txt);line-height:1.7;font-size:16.5px}
.hx *{box-sizing:border-box}.hx br{display:none}.hx p:empty{display:none}
.hx h2{font-family:'Sora','Plus Jakarta Sans',sans-serif;color:var(--ink);font-size:clamp(26px,3vw,38px);line-height:1.15;letter-spacing:-.025em;margin:0 0 10px;font-weight:800}
.hx h3{font-family:'Sora','Plus Jakarta Sans',sans-serif;color:var(--ink);font-size:19px;line-height:1.3;margin:0 0 8px;font-weight:700}
.hx a{color:var(--g)}
.hx .hx-eye{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--gold2);margin:0 0 10px}
.hx .hx-eye:before{content:"";width:22px;height:2px;background:var(--gold);border-radius:2px}
.hx .hx-sub{color:var(--mut);margin:0 0 18px;font-size:16.5px;max-width:72ch}
/* hero */
.hx .hx-hero{position:relative;border-radius:28px;overflow:hidden;min-height:700px;padding:236px 52px 48px;color:#fff;background:#0b1510;isolation:isolate;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:36px;align-items:end}
.hx .hx-slides{position:absolute;inset:0;z-index:-2}
.hx .hx-slide{position:absolute;inset:0;opacity:0;animation:hxFade 36s infinite}
.hx .hx-slide img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;margin:0;animation:hxKen 36s infinite;transform-origin:60% 40%}
.hx .hx-slide:nth-child(1),.hx .hx-slide:nth-child(1) img{animation-delay:0s}
.hx .hx-slide:nth-child(2),.hx .hx-slide:nth-child(2) img{animation-delay:6s}
.hx .hx-slide:nth-child(3),.hx .hx-slide:nth-child(3) img{animation-delay:12s}
.hx .hx-slide:nth-child(4),.hx .hx-slide:nth-child(4) img{animation-delay:18s}
.hx .hx-slide:nth-child(5),.hx .hx-slide:nth-child(5) img{animation-delay:24s}
.hx .hx-slide:nth-child(6),.hx .hx-slide:nth-child(6) img{animation-delay:30s}
.hx .hx-slide:first-child{opacity:1}
.hx .hx-cap{position:absolute;right:22px;top:22px;background:rgba(10,18,14,.55);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,.18);color:#fff;font-size:12.5px;font-weight:700;padding:7px 12px;border-radius:999px;letter-spacing:.02em}
.hx .hx-cap:before{content:"\25CF";color:var(--gold);margin-right:6px;font-size:10px}
@keyframes hxFade{0%{opacity:0}3%{opacity:1}17%{opacity:1}20%{opacity:0}100%{opacity:0}}
@keyframes hxKen{0%{transform:scale(1.02)}20%{transform:scale(1.12)}100%{transform:scale(1.12)}}
.hx .hx-hero:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(6,12,9,.70) 0%,rgba(6,12,9,.30) 32%,rgba(6,12,9,.38) 55%,rgba(6,12,9,.88) 100%),linear-gradient(90deg,rgba(6,12,9,.55) 0%,rgba(6,12,9,0) 60%)}
.hx .hx-lede{font-size:18.5px;line-height:1.65;color:#F1F4EF;margin:0 0 18px;max-width:58ch;text-shadow:0 1px 12px rgba(0,0,0,.35)}
.hx .hx-who{font-size:14.5px;color:#D9E2DB;margin:0 0 18px;max-width:62ch}
.hx .hx-who b{color:#fff;font-weight:700}
.hx .hx-badges{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 22px}
.hx .hx-badge{display:inline-flex;align-items:center;gap:7px;background:rgba(255,255,255,.12);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.22);color:#fff;padding:7px 13px;border-radius:999px;font-size:13.5px;font-weight:600;line-height:1.2}
.hx .hx-badge svg{width:15px;height:15px;color:var(--gold);flex:none}
.hx .hx-ctas{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.hx .hx-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(135deg,#E2C158,#B8860B);color:#14200F!important;font-weight:800;padding:15px 26px;border-radius:14px;text-decoration:none!important;font-size:15.5px;box-shadow:0 12px 26px rgba(184,134,11,.35);transition:transform .2s,box-shadow .2s;line-height:1.2;border:0;cursor:pointer;font-family:inherit}
.hx .hx-btn:hover{transform:translateY(-2px);box-shadow:0 16px 30px rgba(184,134,11,.45)}
.hx .hx-ghost{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.12);border:1.5px solid rgba(255,255,255,.4);color:#fff!important;font-weight:700;padding:14px 22px;border-radius:14px;text-decoration:none!important;font-size:15.5px;line-height:1.2;transition:background .2s,border-color .2s;backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
.hx .hx-ghost:hover{background:#1FA855;border-color:#1FA855}
.hx .hx-ghost svg,.hx .hx-btn svg{width:19px;height:19px;flex:none}
/* planner */
.hx .hx-plan{background:rgba(255,255,255,.96);color:var(--txt);border-radius:22px;padding:22px 22px 18px;box-shadow:0 30px 60px rgba(0,0,0,.35);border:1px solid rgba(255,255,255,.6)}
.hx .hx-plan h3{font-size:18px;margin:0 0 4px}
.hx .hx-plan p{font-size:13.5px;color:var(--mut);margin:0 0 14px;line-height:1.5}
.hx .hx-f{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.hx .hx-f label{display:block;font-size:11.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--mut)}
.hx .hx-f .hx-full{grid-column:1/-1}
.hx .hx-f select,.hx .hx-f input{display:block;width:100%;margin-top:5px;font:600 15px/1.2 'Plus Jakarta Sans',system-ui,sans-serif;color:var(--ink);background:#F4F5F1;border:1px solid var(--line);border-radius:12px;padding:12px 12px;appearance:auto;min-height:46px}
.hx .hx-f select:focus,.hx .hx-f input:focus{outline:2px solid var(--gold);outline-offset:1px;background:#fff}
.hx .hx-plan .hx-btn{width:100%;margin-top:14px;background:linear-gradient(135deg,#25D366,#128C4A);color:#fff!important;box-shadow:0 12px 24px rgba(18,140,74,.3)}
.hx .hx-plan small{display:block;text-align:center;color:var(--mut);font-size:12px;margin-top:9px;line-height:1.4}
/* trust strip */
.hx .hx-trust{position:relative;z-index:2;margin:-34px 28px 0;background:#fff;border:1px solid var(--line);border-radius:20px;box-shadow:0 18px 40px rgba(14,27,20,.10);display:grid;grid-template-columns:repeat(4,minmax(0,1fr))}
.hx .hx-trust div{padding:18px 20px;display:flex;gap:12px;align-items:center;border-right:1px solid var(--line)}
.hx .hx-trust div:last-child{border-right:0}
.hx .hx-trust svg{width:34px;height:34px;flex:none;color:var(--g);background:#EEF5EC;border-radius:10px;padding:7px}
.hx .hx-trust b{display:block;color:var(--ink);font-size:15px;line-height:1.25}
.hx .hx-trust span{display:block;color:var(--mut);font-size:12.5px;line-height:1.35}
/* toc */
.hx .hx-toc{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding:26px 2px 14px;margin:0 0 6px;border-bottom:1px solid var(--line)}
.hx .hx-toc::-webkit-scrollbar{display:none}
.hx .hx-toc a{flex:none;font-size:14px;font-weight:700;color:var(--ink)!important;text-decoration:none!important;padding:9px 16px;border-radius:999px;border:1px solid var(--line);background:#fff;transition:all .2s}
.hx .hx-toc a:hover{background:var(--ink);color:#fff!important;border-color:var(--ink)}
.hx .hx-sec{padding:44px 0 6px;scroll-margin-top:90px}
.hx .hx-intro{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:26px;align-items:start;margin:0 0 6px}
.hx .hx-intro p{color:var(--mut);margin:0}
/* region */
.hx .hx-region{margin:34px 0 0}
.hx .hx-rhead{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;flex-wrap:wrap;margin:0 0 14px}
.hx .hx-rhead h3{display:flex;align-items:center;gap:10px;flex-wrap:wrap;font-size:22px;margin:0 0 4px}
.hx .hx-tag{background:var(--gold);color:#1a1606;font-size:11px;font-weight:800;padding:4px 10px;border-radius:999px;letter-spacing:.08em;text-transform:uppercase;font-family:'Plus Jakarta Sans',sans-serif}
.hx .hx-rnote{color:var(--mut);font-size:15px;margin:0;max-width:70ch}
.hx .hx-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.hx .hx-grid.hx-g5{grid-template-columns:repeat(6,minmax(0,1fr))}
.hx .hx-grid.hx-g5 .hx-dc{grid-column:span 2;aspect-ratio:1/1.1}
.hx .hx-grid.hx-g5 .hx-dc:nth-child(4),.hx .hx-grid.hx-g5 .hx-dc:nth-child(5){grid-column:span 3;aspect-ratio:16/10}
.hx a.hx-dc{position:relative;display:block;border-radius:20px;overflow:hidden;aspect-ratio:4/5;text-decoration:none!important;color:#fff!important;background:#0b1510;box-shadow:0 10px 26px rgba(14,27,20,.14);isolation:isolate}
.hx a.hx-dc img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;margin:0;transition:transform .7s cubic-bezier(.2,.7,.2,1);z-index:-2}
.hx a.hx-dc:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(0,0,0,0) 35%,rgba(5,10,7,.86) 100%)}
.hx a.hx-dc:hover img{transform:scale(1.07)}
.hx .hx-dc .hx-best{position:absolute;top:14px;left:14px;background:rgba(255,255,255,.92);color:var(--ink);font-size:11.5px;font-weight:800;padding:6px 10px;border-radius:999px;letter-spacing:.02em}
.hx .hx-dc .hx-dt{position:absolute;left:18px;right:18px;bottom:16px}
.hx .hx-dc b{display:block;font-family:'Sora','Plus Jakarta Sans',sans-serif;font-size:24px;line-height:1.1;font-weight:800;letter-spacing:-.02em;margin:0 0 4px}
.hx .hx-dc em{display:block;font-style:normal;font-size:13.5px;line-height:1.45;color:#E6EBE6}
.hx .hx-dc i{display:inline-flex;align-items:center;gap:6px;font-style:normal;font-size:13px;font-weight:800;color:var(--gold);margin-top:8px}
.hx .hx-mini{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.hx a.hx-mc{position:relative;display:block;border-radius:16px;overflow:hidden;aspect-ratio:4/3;text-decoration:none!important;color:#fff!important;background:#0b1510;isolation:isolate}
.hx a.hx-mc img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;margin:0;transition:transform .6s;z-index:-2}
.hx a.hx-mc:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(5,10,7,.85) 100%)}
.hx a.hx-mc:hover img{transform:scale(1.06)}
.hx .hx-mc span{position:absolute;left:14px;right:14px;bottom:12px}
.hx .hx-mc b{display:block;font-size:17px;line-height:1.2;font-weight:800}
.hx .hx-mc em{display:block;font-style:normal;font-size:12.5px;color:var(--gold);font-weight:700;margin-top:2px}
/* styles */
.hx .hx-styles{background:var(--ink);border-radius:26px;padding:38px 34px;color:#fff;margin-top:44px;position:relative;overflow:hidden}
.hx .hx-styles h2{color:#fff}
.hx .hx-styles .hx-sub{color:#C9D4CC}
.hx .hx-styles .hx-eye{color:var(--gold)}
.hx .hx-tabs{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 18px}
.hx .hx-tabs label{cursor:pointer;font-weight:700;font-size:14.5px;padding:10px 16px;border-radius:999px;border:1px solid rgba(255,255,255,.22);color:#E8EEE9;transition:all .2s;user-select:none}
.hx .hx-tabs label:hover{border-color:var(--gold)}
.hx input.hx-r{position:absolute;opacity:0;pointer-events:none}
.hx .hx-pane{display:none;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.hx #hxs1:checked~.hx-tabs label[for=hxs1],.hx #hxs2:checked~.hx-tabs label[for=hxs2],.hx #hxs3:checked~.hx-tabs label[for=hxs3],.hx #hxs4:checked~.hx-tabs label[for=hxs4]{background:var(--gold);border-color:var(--gold);color:#1a1606}
.hx #hxs1:checked~.hx-panes .hx-p1,.hx #hxs2:checked~.hx-panes .hx-p2,.hx #hxs3:checked~.hx-panes .hx-p3,.hx #hxs4:checked~.hx-panes .hx-p4{display:grid}
.hx a.hx-sc{display:flex;gap:14px;align-items:center;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:16px;padding:12px;text-decoration:none!important;color:#fff!important;transition:background .2s,transform .2s}
.hx a.hx-sc:hover{background:rgba(255,255,255,.12);transform:translateY(-2px)}
.hx a.hx-sc img{width:84px;height:84px;border-radius:12px;object-fit:cover;flex:none;margin:0}
.hx a.hx-sc b{display:block;font-size:16.5px;line-height:1.25}
.hx a.hx-sc em{display:block;font-style:normal;font-size:13.5px;line-height:1.45;color:#C9D4CC;margin-top:3px}
/* guests */
.hx .hx-gal{display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:200px 200px;gap:12px;margin-top:16px}
.hx .hx-gal figure{position:relative;margin:0;border-radius:16px;overflow:hidden;background:#ddd}
.hx .hx-gal figure:first-child{grid-row:span 2}
.hx .hx-gal img{width:100%;height:100%;object-fit:cover;display:block;margin:0;transition:transform .6s}
.hx .hx-gal figure:hover img{transform:scale(1.05)}
.hx .hx-gal figcaption{position:absolute;left:10px;bottom:10px;background:rgba(10,18,14,.7);color:#fff;font-size:12px;font-weight:700;padding:5px 10px;border-radius:999px}
/* steps */
.hx .hx-steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:18px;counter-reset:st;position:relative}
.hx .hx-step{position:relative;background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px 20px 20px;box-shadow:0 4px 14px rgba(14,27,20,.04)}
.hx .hx-step .hx-n{width:44px;height:44px;border-radius:14px;background:var(--ink);color:var(--gold);display:flex;align-items:center;justify-content:center;margin-bottom:12px}
.hx .hx-step .hx-n svg{width:22px;height:22px}
.hx .hx-step b{display:block;color:var(--ink);margin-bottom:4px;font-size:16.5px}
.hx .hx-step b:before{counter-increment:st;content:counter(st) ". ";color:var(--gold2)}
.hx .hx-step p{margin:0;font-size:14.5px;color:var(--mut);line-height:1.6}
/* why */
.hx .hx-why{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:18px}
.hx .hx-why>div{background:var(--cream);border-radius:18px;padding:22px 20px;border:1px solid var(--line)}
.hx .hx-why svg{width:40px;height:40px;color:var(--g);background:#fff;border:1px solid var(--line);border-radius:12px;padding:8px;margin-bottom:12px}
.hx .hx-why b{color:var(--ink);display:block;margin-bottom:6px;font-size:16.5px}
.hx .hx-why p{margin:0;font-size:14.5px;color:var(--mut);line-height:1.6}
/* faq */
.hx .hx-faqs{margin-top:10px;border-top:1px solid var(--line)}
.hx details.hx-faq{border-bottom:1px solid var(--line)}
.hx details.hx-faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:19px 2px;font-weight:700;color:var(--ink);font-size:16.5px;line-height:1.4}
.hx details.hx-faq summary::-webkit-details-marker{display:none}
.hx details.hx-faq summary:after{content:"+";flex:none;width:32px;height:32px;border-radius:50%;background:var(--cream);border:1px solid var(--line);display:flex;align-items:center;justify-content:center;color:var(--gold2);font-size:20px;font-weight:700;transition:transform .2s}
.hx details.hx-faq[open] summary:after{transform:rotate(45deg)}
.hx details.hx-faq .hx-ans{padding:0 2px 19px;color:var(--mut);font-size:15.5px}
.hx details.hx-faq .hx-ans p{margin:0}
/* final */
.hx .hx-final{position:relative;border-radius:28px;overflow:hidden;padding:72px 32px;margin:52px 0 0;text-align:center;color:#fff;isolation:isolate}
.hx .hx-final img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;margin:0;z-index:-2}
.hx .hx-final:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(6,12,9,.55),rgba(6,12,9,.78))}
.hx .hx-final h2{color:#fff;margin:0 0 10px}
.hx .hx-final p{color:#E8EEE9;max-width:60ch;margin:0 auto 20px}
.hx .hx-final .hx-ctas{justify-content:center}
.hx .hx-final .hx-contact{margin:18px 0 0;font-size:15px;color:#E8EEE9}
.hx .hx-final .hx-contact a,.hx .hx-final .hx-contact strong{color:#F0D57A}
.hx .hx-credits{margin:18px 0 0;font-size:12px;color:#7A867D}
.hx .hx-credits summary{cursor:pointer}
.hx .hx-credits p{margin:6px 0 0;line-height:1.6}
.hx .hx-credits a{color:#7A867D}
/* page header over hero */
body.page-id-PID .page-content{position:relative;padding-top:22px!important}
body.page-id-PID .page-header{position:absolute;z-index:6;top:22px;left:24px;right:24px;margin:0!important;padding:58px 52px 0;background:none;pointer-events:none}
body.page-id-PID .page-header:before{content:"Holidays abroad \00B7 Suzu Travels";display:inline-block;font:800 12px/1 "Plus Jakarta Sans",sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1606;background:#E2C158;padding:8px 13px;border-radius:999px;margin-bottom:16px}
body.page-id-PID .page-header .entry-title{color:#fff!important;font-family:"Sora","Plus Jakarta Sans",sans-serif!important;font-size:clamp(34px,4.2vw,58px)!important;line-height:1.06!important;letter-spacing:-.035em!important;margin:0!important;font-weight:800!important;max-width:15ch;text-shadow:0 2px 24px rgba(0,0,0,.35)}
@media(max-width:1100px){.hx .hx-hero{grid-template-columns:1fr;align-items:start}.hx .hx-plan{max-width:560px}.hx .hx-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-grid.hx-g5{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-grid.hx-g5 .hx-dc,.hx .hx-grid.hx-g5 .hx-dc:nth-child(4),.hx .hx-grid.hx-g5 .hx-dc:nth-child(5){grid-column:auto;aspect-ratio:4/5}.hx .hx-grid.hx-g5 .hx-dc:nth-child(5){grid-column:1/-1;aspect-ratio:16/9}.hx .hx-mini{grid-template-columns:repeat(3,minmax(0,1fr))}.hx .hx-steps,.hx .hx-why{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-trust{grid-template-columns:repeat(2,minmax(0,1fr))}.hx .hx-trust div:nth-child(2){border-right:0}.hx .hx-trust div:nth-child(-n+2){border-bottom:1px solid var(--line)}.hx .hx-pane{grid-template-columns:1fr 1fr}}
@media(max-width:700px){.hx{font-size:16px}.hx .hx-hero{padding:206px 18px 22px;border-radius:22px;min-height:0}body.page-id-PID .page-header{left:14px;right:14px;padding:26px 18px 0}body.page-id-PID .page-header:before{font-size:10.5px;padding:7px 11px;margin-bottom:12px}body.page-id-PID .page-header .entry-title{font-size:33px!important}.hx .hx-lede{font-size:16.5px}.hx .hx-who{display:none}.hx .hx-ctas a{flex:1 1 auto;justify-content:center}.hx .hx-plan{padding:18px 16px 14px;border-radius:18px}.hx .hx-trust{margin:-18px 8px 0}.hx .hx-trust div{padding:13px 12px;gap:9px}.hx .hx-trust svg{width:28px;height:28px;padding:5px}.hx .hx-trust b{font-size:13.5px}.hx .hx-trust span{font-size:11.5px}.hx .hx-intro{grid-template-columns:1fr;gap:12px}.hx .hx-grid{gap:10px}.hx a.hx-dc{border-radius:16px}.hx .hx-dc b{font-size:19px}.hx .hx-dc em{font-size:12px}.hx .hx-dc .hx-dt{left:12px;right:12px;bottom:12px}.hx .hx-dc .hx-best{top:10px;left:10px;font-size:10.5px;padding:5px 8px}.hx .hx-dc i{display:none}.hx .hx-cap{display:none}.hx .hx-lede{font-size:16px;line-height:1.6}.hx .hx-mini{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.hx .hx-mc b{font-size:15px}.hx .hx-styles{padding:28px 16px;border-radius:20px}.hx .hx-pane{grid-template-columns:1fr}.hx .hx-gal{grid-template-columns:1fr 1fr;grid-template-rows:180px 130px 130px}.hx .hx-gal figure:first-child{grid-row:auto;grid-column:1/-1}.hx .hx-gal figure:nth-child(n+6){display:none}.hx .hx-steps,.hx .hx-why{grid-template-columns:1fr}.hx .hx-final{padding:48px 18px;border-radius:22px}}
.hx .hx-styles:has(#hxs1:checked) label[for=hxs1],.hx .hx-styles:has(#hxs2:checked) label[for=hxs2],.hx .hx-styles:has(#hxs3:checked) label[for=hxs3],.hx .hx-styles:has(#hxs4:checked) label[for=hxs4]{background:var(--gold);border-color:var(--gold);color:#1a1606}
.hx .hx-styles:has(#hxs1:checked) .hx-p1,.hx .hx-styles:has(#hxs2:checked) .hx-p2,.hx .hx-styles:has(#hxs3:checked) .hx-p3,.hx .hx-styles:has(#hxs4:checked) .hx-p4{display:grid}
.hx .hx-styles p:has(>input.hx-r){margin:0;height:0;overflow:hidden}
.hx .hx-final p:has(>img){margin:0}
@media(prefers-reduced-motion:reduce){.hx .hx-slide,.hx .hx-slide img{animation:none}.hx .hx-slide{opacity:0}.hx .hx-slide:first-child{opacity:1}}
""".replace('PID', str(PID))

def svg(name):
    P = {
        'shield': '<path d="M12 3l7 3v6c0 4.5-3 7.6-7 9-4-1.4-7-4.5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/>',
        'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
        'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/>',
        'team': '<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M15 14.5c3 0 6 1.8 6 5"/>',
        'chat': '<path d="M4 5h16v11H8l-4 4z"/><path d="M8 9h8M8 12h5"/>',
        'doc': '<path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4M9 12h7M9 16h7"/>',
        'sliders': '<path d="M4 7h10M18 7h2M4 17h2M10 17h10"/><circle cx="16" cy="7" r="2"/><circle cx="8" cy="17" r="2"/>',
        'lock': '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 018 0v3"/>',
        'pin': '<path d="M12 21s7-6.2 7-12a7 7 0 10-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
        'award': '<circle cx="12" cy="9" r="6"/><path d="M8.5 14l-1.5 7 5-3 5 3-1.5-7"/>',
        'food': '<path d="M7 3v8M5 3v5a2 2 0 004 0V3M7 11v10M16 3c-1.7 0-3 2-3 5s1 4 3 4v9"/>',
        'phone': '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a1 1 0 01-1 1C10.7 20 4 13.3 4 5a1 1 0 011-1z"/>',
        'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
        'check': '<path d="M5 12.5l4.5 4.5L19 7"/>',
    }
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + P[name] + '</svg>'

WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2.1-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3zM12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2z"/></svg>'

DEST = [
    # slug, page slug, name, places, days, best
    ('nepal', 'nepal-tour-packages', 'Nepal', 'Kathmandu, Pokhara, Chitwan', '4–8 days', 'Oct–Nov, Mar–Apr'),
    ('bhutan', 'bhutan-tour-packages', 'Bhutan', 'Paro, Thimphu, Punakha', '5–7 days', 'Mar–May, Sep–Nov'),
    ('srilanka', 'sri-lanka-tour-packages', 'Sri Lanka', 'Colombo, Kandy, Ella, Bentota', '5–8 days', 'Dec–Mar'),
    ('maldives', 'maldives-tour-packages', 'Maldives', 'Male, resort islands', '4–6 days', 'Nov–Apr'),
    ('thailand', 'thailand-tour-packages', 'Thailand', 'Bangkok, Pattaya, Phuket, Krabi', '5–8 days', 'Nov–Feb'),
    ('singapore', 'singapore-tour-packages', 'Singapore', 'City, Sentosa, Universal', '4–6 days', 'Year-round'),
    ('malaysia', 'malaysia-tour-packages', 'Malaysia', 'Kuala Lumpur, Langkawi, Genting', '5–7 days', 'Dec–Apr'),
    ('vietnam', 'vietnam-tour-packages', 'Vietnam', 'Hanoi, Ha Long, Da Nang, Ho Chi Minh', '6–9 days', 'Varies by region'),
    ('bali', 'bali-tour-packages', 'Bali, Indonesia', 'Kuta, Ubud, Nusa Penida', '5–8 days', 'Apr–Oct'),
]
D = {d[0]: d for d in DEST}

ONREQ_ME = [('dubai', 'Dubai & UAE'), ('turkey', 'Turkey'), ('georgia', 'Georgia'), ('azerbaijan', 'Azerbaijan'), ('armenia', 'Armenia'), ('uzbekistan', 'Uzbekistan')]
ONREQ_EU = [('europe', 'Europe (Multi-Country)'), ('switzerland', 'Switzerland'), ('uk', 'United Kingdom'), ('japan', 'Japan'), ('mauritius', 'Mauritius'), ('egypt', 'Egypt'), ('australia', 'Australia & New Zealand'), ('kazakhstan', 'Kazakhstan & Kyrgyzstan')]

def dcard(slug, eager=False, n=1):
    s, page, name, places, days, best = D[slug]
    key = f'{slug}-{n}' if f'{slug}-{n}' in M else slug
    return (f'<a class="hx-dc" href="https://suzutravels.com/{page}/">'
            f'<img src="{u(key)}" alt="{alt(key)}" width="800" height="1000" loading="{"eager" if eager else "lazy"}" decoding="async">'
            f'<span class="hx-best">Best: {html.escape(best)}</span>'
            f'<span class="hx-dt"><b>{html.escape(name)}</b><em>{html.escape(places)} · {days}</em><i>View {html.escape(name.split(",")[0])} trips {svg("arrow").replace("<svg ", "<svg width=\"15\" height=\"15\" ")}</i></span></a>')

LIVE_PAGES = {'dubai': ('dubai-tour-packages', 'View Dubai trips →'), 'turkey': ('turkey-tour-packages', 'View Turkey trips →'), 'georgia': ('georgia-tour-packages', 'View Georgia trips →'), 'azerbaijan': ('azerbaijan-tour-packages', 'View Azerbaijan trips →'), 'japan': ('japan-tour-packages', 'View Japan trips →'), 'europe': ('europe-tour-packages', 'View Europe trips →'), 'switzerland': ('switzerland-tour-packages', 'View Switzerland trips →'), 'mauritius': ('mauritius-tour-packages', 'View Mauritius trips →'), 'uk': ('uk-tour-packages', 'View UK trips →'), 'egypt': ('egypt-tour-packages', 'View Egypt trips →'), 'australia': ('australia-tour-packages', 'View Australia trips →'), 'uzbekistan': ('uzbekistan-tour-packages', 'View Uzbekistan trips →')}  # on-request tiles that now have their own page

def mcard(slug, name):
    if slug in LIVE_PAGES:
        p, lab = LIVE_PAGES[slug]
        return (f'<a class="hx-mc" href="https://suzutravels.com/{p}/">'
                f'<img src="{m(slug)}" alt="{alt(slug)}" width="640" height="480" loading="lazy" decoding="async">'
                f'<span><b>{html.escape(name)}</b><em>{lab}</em></span></a>')
    return (f'<a class="hx-mc" href="{wa("Hi Suzu Travels, I would like a custom quote for a " + name + " holiday.")}" target="_blank" rel="noopener">'
            f'<img src="{m(slug)}" alt="{alt(slug)}" width="640" height="480" loading="lazy" decoding="async">'
            f'<span><b>{html.escape(name)}</b><em>Quote on WhatsApp →</em></span></a>')

def sc(slug, why, n=2):
    s, page, name, *_ = D[slug]
    key = f'{slug}-{n}' if f'{slug}-{n}' in M else (f'{slug}-1' if f'{slug}-1' in M else slug)
    return (f'<a class="hx-sc" href="https://suzutravels.com/{page}/"><img src="{m(key)}" alt="{alt(key)}" width="168" height="168" loading="lazy" decoding="async">'
            f'<span><b>{html.escape(name)}</b><em>{html.escape(why)}</em></span></a>')

FAQ = [
    ("Do you handle visas?", "We guide you through the documentation and process for each destination and tell you honestly what the current requirements and timelines are. Visa approval is always the decision of the issuing country, and we never promise an outcome we do not control."),
    ("Are flights included?", "Your choice. We can quote land-only (hotels, transfers, sightseeing) or a full package including flights from your nearest airport. Say which you prefer when you enquire."),
    ("Can I customise an international tour package from India?", "Yes. Suzu Travels can customise your international holiday based on your destination, travel dates, number of travellers, hotel preference, sightseeing requirements and budget. You can request a land-only package or include flights in the itinerary."),
    ("Why are there no prices on this page?", "Because an honest international quote depends on your dates, group size, hotel category and current airfare. A fixed number on a web page is usually a starting figure that changes once you ask. We would rather send you a real one."),
    ("Can you handle groups and corporate trips?", "Yes. We regularly run group departures and MICE movements, and we work with travel agents on a B2B basis. Tell us the group size and we will quote accordingly."),
    ("How far in advance should I plan?", "For Nepal, Bhutan, Sri Lanka and Southeast Asia, four to six weeks is comfortable. For Europe, the UK, Japan, Australia and the USA, start at least two to three months ahead because visa appointments drive the timeline."),
]

HERO_SLIDES = [('hero-abroad', 'Holidays abroad'), ('maldives-1', 'Maldives'), ('bali-1', 'Bali, Indonesia'), ('nepal-1', 'Pokhara, Nepal'), ('singapore-1', 'Singapore'), ('thailand-1', 'Phi Phi, Thailand')]

# planner JS: single line, no ampersand, no double-slash comments
JS = ("(function(){var f=document.getElementById('hxPlan');if(!f){return;}f.addEventListener('submit',function(e){e.preventDefault();"
      "var d=f.querySelector('[name=d]').value,m=f.querySelector('[name=m]').value,a=f.querySelector('[name=a]').value,k=f.querySelector('[name=k]').value,c=f.querySelector('[name=c]').value;"
      "var t='Hi Suzu Travels, please send me a costed itinerary.\\nDestination: '+d+'\\nTravel month: '+m+'\\nAdults: '+a+'\\nChildren: '+k;"
      "if(c){t=t+'\\nDeparting from: '+c;}"
      "window.open('https:'+String.fromCharCode(47,47)+'wa.me/917087488961?text='+encodeURIComponent(t),'_blank','noopener');});})();")

def months():
    import datetime
    names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    opts = ['<option>Not sure yet</option>']
    y, mth = 2026, 11
    for i in range(14):
        opts.append(f'<option>{names[mth-1]} {y}</option>')
        mth += 1
        if mth > 12:
            mth = 1; y += 1
    return ''.join(opts)

# Season planner (30 Oct 2026). Months come ONLY from the "Best season" fact on each live country page
# (.hx pages: pages/gen_*.py facts; .sx pages: live fact box, read 30 Oct 2026). Vietnam ("varies by region") is not
# placed in any month; Singapore ("year-round; Feb–Apr driest") shows Feb–Apr. Snow months marked separately.
# Kept out of CSS so country generators that import G.CSS do not inherit it.
WHEN = [  # slug, label, best months, snow months
    ('nepal-tour-packages', 'Nepal', [3, 4, 10, 11], []),
    ('bhutan-tour-packages', 'Bhutan', [3, 4, 5, 9, 10, 11], []),
    ('sri-lanka-tour-packages', 'Sri Lanka', [12, 1, 2, 3], []),
    ('maldives-tour-packages', 'Maldives', [11, 12, 1, 2, 3, 4], []),
    ('thailand-tour-packages', 'Thailand', [11, 12, 1, 2], []),
    ('singapore-tour-packages', 'Singapore', [2, 3, 4], []),
    ('malaysia-tour-packages', 'Malaysia', [12, 1, 2, 3, 4], []),
    ('bali-tour-packages', 'Bali', [4, 5, 6, 7, 8, 9, 10], []),
    ('dubai-tour-packages', 'Dubai', [11, 12, 1, 2, 3], []),
    ('turkey-tour-packages', 'Turkey', [4, 5, 6, 9, 10, 11], []),
    ('georgia-tour-packages', 'Georgia', [5, 6, 9, 10], [12, 1, 2, 3]),
    ('azerbaijan-tour-packages', 'Azerbaijan', [4, 5, 6, 9, 10], [12, 1, 2, 3]),
    ('uzbekistan-tour-packages', 'Uzbekistan', [4, 5, 6, 9, 10], []),
    ('egypt-tour-packages', 'Egypt', [10, 11, 12, 1, 2, 3, 4], []),
    ('europe-tour-packages', 'Europe', [4, 5, 6, 9, 10], []),
    ('switzerland-tour-packages', 'Switzerland', [6, 7, 8, 9], [12, 1, 2, 3]),
    ('uk-tour-packages', 'UK', [5, 6, 7, 8, 9], []),
    ('japan-tour-packages', 'Japan', [3, 4, 5, 10, 11], []),
    ('mauritius-tour-packages', 'Mauritius', [4, 5, 6, 9, 10, 11], []),
    ('australia-tour-packages', 'Australia &amp; NZ', [3, 4, 5, 9, 10, 11], []),
]
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
WHEN_NOTE = {3: 'Japan: late March onwards', 5: 'UK: late May onwards', 6: 'Uzbekistan: early June', 9: 'UK: early September', 10: 'Europe: early October'}
WHEN_CSS = ('.hx .hx-when{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-top:18px}'
            '.hx .hx-mo{background:#fff;border:1px solid var(--line);border-radius:18px;padding:16px 16px 14px;position:relative;overflow:hidden}'
            '.hx .hx-mo:before{content:"";position:absolute;left:0;right:0;top:0;height:4px;background:var(--gold)}'
            '.hx .hx-mo b{display:block;font-family:"Sora","Plus Jakarta Sans",sans-serif;color:var(--ink);font-size:17px;margin:2px 0 10px}'
            '.hx .hx-mo a{display:inline-block;margin:0 6px 7px 0;padding:5px 10px;border-radius:999px;background:var(--cream);border:1px solid var(--line);color:var(--ink);font-size:13.5px;font-weight:700;text-decoration:none;line-height:1.3}'
            '.hx .hx-mo a:hover{border-color:var(--gold);background:#FFF8E6}'
            '.hx .hx-mo a.hx-snow{background:#EEF4FB;border-color:#C9DBEF}'
            '.hx .hx-mo small{display:block;color:var(--mut);font-size:12px;line-height:1.45;margin-top:3px}'
            '.hx .hx-wkey{font-size:13px;color:var(--mut);margin-top:12px}'
            '.hx .hx-when p{margin:0}'
            '@media(max-width:1100px){.hx .hx-when{grid-template-columns:repeat(3,minmax(0,1fr))}}'
            '@media(max-width:700px){.hx .hx-when{grid-template-columns:1fr 1fr;gap:10px}.hx .hx-mo{padding:14px 12px 10px}.hx .hx-mo a{font-size:12.5px;padding:4px 8px;margin:0 4px 6px 0}}'
            '@media(max-width:420px){.hx .hx-when{grid-template-columns:1fr}}')

def when_block():
    cards = []
    for i, mname in enumerate(MONTHS, 1):
        chips = ''.join(f'<a href="https://suzutravels.com/{p}/">{n}</a>' for p, n, best, snow in WHEN if i in best)
        chips += ''.join(f'<a class="hx-snow" href="https://suzutravels.com/{p}/">{n} · snow</a>' for p, n, best, snow in WHEN if i in snow)
        note = f'<small>{WHEN_NOTE[i]}</small>' if i in WHEN_NOTE else ''
        cards.append(f'<div class="hx-mo" id="hx-m{i}"><b>{mname}</b>{chips}{note}</div>')
    return ('<section id="where-to-go-by-month" class="hx-sec"><style>' + WHEN_CSS + '</style><span class="hx-eye">Season planner</span>'
            '<h2>Where to go abroad, month by month</h2>'
            '<p class="hx-sub">Picked from the best-season advice on each of our destination pages. A month that is not listed can still work — weather, festivals, school holidays and flight prices all matter, so we check them against your dates before we quote.</p>'
            '<div class="hx-when">' + ''.join(cards) + '</div>'
            '<p class="hx-wkey">Blue chips = the snow season. Vietnam has different seasons in the north, centre and south, so we suggest the best region for your month. Singapore can be visited all year; February to April is usually the driest.</p></section>')

def build():
    h = []
    h.append(f'<div class="suzu-intl hx"><style>{" ".join(l.strip() for l in CSS.strip().splitlines() if not l.strip().startswith("/*"))}</style>')
    # HERO
    slides = ''.join(
        f'<div class="hx-slide"><img src="{u(s)}" alt="{alt(s)}" width="1600" height="1000" {"fetchpriority=\"high\" loading=\"eager\"" if i == 0 else "loading=\"lazy\""} decoding="async"><span class="hx-cap">{html.escape(c)}</span></div>'
        for i, (s, c) in enumerate(HERO_SLIDES))
    destopts = ''.join(f'<option>{html.escape(d[2])}</option>' for d in DEST) + ''.join(f'<option>{html.escape(n)}</option>' for _, n in ONREQ_ME + ONREQ_EU) + '<option>Other / multi-country</option>'
    h.append('<section class="hx-hero" aria-label="International holidays from India">'
             f'<div class="hx-slides">{slides}</div>'
             '<div class="hx-copy">'
             '<p class="hx-lede">Planning a trip abroad? Suzu Travels builds custom international holidays for Indian travellers — families, couples, groups and corporate teams. Every itinerary is quoted to your dates, your budget and your pace, not sold off a shelf.</p>'
             '<div class="hx-badges">'
             f'<span class="hx-badge">{svg("shield")}HP Tourism registered travel agent</span>'
             f'<span class="hx-badge">{svg("award")}Operating since 2019</span>'
             f'<span class="hx-badge">{svg("team")}Own Ground Team</span></div>'
             '<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Get a Custom Quote ' + svg('arrow') + '</a>'
             f'<a class="hx-ghost" href="{wa("Hi Suzu Travels, I would like a quote for an international trip.")}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
             '</div>'
             '<form class="hx-plan" id="hxPlan" aria-label="Get a costed itinerary on WhatsApp">'
             '<h3>Plan my trip abroad</h3><p>Pick a destination and month — we reply on WhatsApp with a costed, day-by-day plan, usually within 24 hours.</p>'
             '<div class="hx-f">'
             f'<label class="hx-full">Destination<select name="d">{destopts}</select></label>'
             f'<label>Travel month<select name="m">{months()}</select></label>'
             '<label>Departing from<input name="c" type="text" placeholder="e.g. Delhi" autocomplete="address-level2"></label>'
             '<label>Adults<select name="a"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7–10</option><option>11–20</option><option>20+</option></select></label>'
             '<label>Children<select name="k"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option></select></label>'
             '</div>'
             f'<button class="hx-btn" type="submit">{WA_SVG}Get my itinerary on WhatsApp</button>'
             '<small>Opens WhatsApp with your details filled in. We do not store anything on this page.</small>'
             '</form></section>')
    # TRUST
    h.append('<div class="hx-trust">'
             f'<div>{svg("globe")}<span><b>9 country guides</b><span>30+ destinations on request</span></span></div>'
             f'<div>{svg("clock")}<span><b>Quote in ~24 hours</b><span>Costed, day by day</span></span></div>'
             f'<div>{svg("shield")}<span><b>HP Tourism registered</b><span>Reg. DTO-MND-11-243/2022</span></span></div>'
             f'<div>{svg("chat")}<span><b>One team, start to finish</b><span>On WhatsApp while you travel</span></span></div>'
             '</div>')
    # TOC
    h.append('<nav class="hx-toc" aria-label="On this page"><a href="#where-do-you-want-to-go">Destinations</a><a href="#trip-styles">Trip styles</a><a href="#where-to-go-by-month">When to go</a><a href="#real-trips">Real trips</a><a href="#how-booking-works">How booking works</a><a href="#why-book-your-international-trip-with-su">Why Suzu</a><a href="#common-questions">FAQ</a></nav>')
    # DESTINATIONS
    h.append('<section id="where-do-you-want-to-go" class="hx-sec">'
             '<span class="hx-eye">Destinations</span><h2>Where do you want to go?</h2>'
             '<p class="hx-sub">Browse by region. Tell us your dates and group size and we will send a costed, day-by-day itinerary — usually within 24 hours.</p>'
             '<div class="hx-intro"><div><h3>Which International Destinations Can You Book With Suzu Travels?</h3>'
             '<p>Suzu Travels arranges international holidays across Asia, the Middle East, Europe and other destinations, including Nepal, Bhutan, Sri Lanka, Maldives, Thailand, Singapore, Malaysia, Vietnam, Dubai, Turkey, Georgia, Azerbaijan, Switzerland, France, the UK, Japan, Mauritius, Egypt, Australia and New Zealand.</p></div>'
             '<div><h3>Who Are Our International Tour Packages For?</h3>'
             '<p>Our international tour packages are designed for Indian families, couples, honeymooners, groups, senior citizens and corporate travellers. Whether you are planning your first international holiday or a multi-country trip, Suzu Travels can create a customised itinerary based on your destination, travel dates, group size and budget.</p></div></div>')
    h.append('<div class="hx-region"><div class="hx-rhead"><div><h3>Himalayan Neighbours &amp; South Asia <span class="hx-tag">Easiest to plan</span></h3>'
             '<p class="hx-rnote">Short flights or overland routes, familiar food, rupee-friendly budgets. The simplest first trip abroad for most Indian families.</p></div></div>'
             '<div class="hx-grid">' + ''.join(dcard(s, eager=(i < 2)) for i, s in enumerate(['nepal', 'bhutan', 'srilanka', 'maldives'])) + '</div></div>')
    h.append('<div class="hx-region"><div class="hx-rhead"><div><h3>Southeast Asia <span class="hx-tag">Best value</span></h3>'
             '<p class="hx-rnote">The most booked international region for Indian travellers — strong value, easy visas and plenty of vegetarian and Indian food options.</p></div></div>'
             '<div class="hx-grid hx-g5">' + ''.join(dcard(s) for s in ['thailand', 'singapore', 'malaysia', 'vietnam', 'bali']) + '</div></div>')
    h.append('<div class="hx-region"><div class="hx-rhead"><div><h3>Middle East &amp; Caucasus</h3>'
             '<p class="hx-rnote">Short flights from North India, excellent for families and first-time international travellers. Also arranged on request.</p></div></div>'
             '<div class="hx-mini">' + ''.join(mcard(s, n) for s, n in ONREQ_ME) + '</div></div>')
    h.append('<div class="hx-region"><div class="hx-rhead"><div><h3>Europe, Far East &amp; Beyond</h3>'
             '<p class="hx-rnote">Longer trips that need more planning lead time, especially for visa appointments. Talk to us early.</p></div></div>'
             '<div class="hx-mini">' + ''.join(mcard(s, n) for s, n in ONREQ_EU) + '</div></div></section>')
    # TRIP STYLES
    h.append('<section id="trip-styles" class="hx-styles hx-sec"><span class="hx-eye">Find your fit</span><h2>Pick a destination by trip style</h2>'
             '<p class="hx-sub">Not sure where to go? Start from the kind of trip you want — we will fine-tune it to your dates and budget.</p>'
             '<input class="hx-r" type="radio" name="hxs" id="hxs1" checked><input class="hx-r" type="radio" name="hxs" id="hxs2"><input class="hx-r" type="radio" name="hxs" id="hxs3"><input class="hx-r" type="radio" name="hxs" id="hxs4">'
             '<div class="hx-tabs"><label for="hxs1">First trip abroad</label><label for="hxs2">Honeymoon &amp; couples</label><label for="hxs3">Families with kids</label><label for="hxs4">Groups &amp; corporate</label></div>'
             '<div class="hx-panes">'
             '<div class="hx-pane hx-p1">' + sc('nepal', 'No visa needed for Indian citizens; Hindi widely understood, familiar food.') + sc('bhutan', 'No visa for Indians — we arrange the entry permit. Calm, green and unhurried.') + sc('singapore', 'Clean, safe and organised — removes almost every friction point of travelling abroad.') + '</div>'
             '<div class="hx-pane hx-p2">' + sc('maldives', 'Overwater villas, house reefs and the clearest water — 3–4 hours from most metros.') + sc('bali', 'Rice terraces, clifftop temples and villas with private pools.') + sc('vietnam', 'Ha Long Bay cruises and the lantern-lit streets of Hoi An.') + '</div>'
             '<div class="hx-pane hx-p3">' + sc('singapore', 'Sentosa, Universal Studios and the zoo — easy days with children.', 1) + sc('malaysia', 'Kuala Lumpur, Genting Highlands and Langkawi — great value for families.') + sc('nepal', 'Add Chitwan for jeep safaris and canoe rides — children love it.') + '</div>'
             '<div class="hx-pane hx-p4">' + sc('thailand', 'Strong value, short flights and plenty of Indian food — easy for big groups.') + sc('srilanka', 'Beaches, tea country and ancient cities, a short flight from South India.') + sc('malaysia', 'Kuala Lumpur city plus Langkawi beaches for team trips.', 1) + '</div>'
             '</div></section>')
    # WHERE TO GO, MONTH BY MONTH (added 30 Oct 2026) — built only from the "Best season" line of each live country page
    h.append(when_block())
    # REAL TRIPS (Suzu guest photos, Nepal)
    G = [('https://suzutravels.com/wp-content/uploads/2026/10/patan-durbar-square-temples.webp', 'Patan Durbar Square, Lalitpur'),
         ('https://suzutravels.com/wp-content/uploads/2026/10/nepal-pagoda-group-tour.webp', 'Our group at a pagoda temple'),
         ('https://suzutravels.com/wp-content/uploads/2026/10/chitwan-national-park-viewpoint.webp', 'Chitwan National Park'),
         ('https://suzutravels.com/wp-content/uploads/2026/10/kathmandu-palace-suzu-travels.webp', 'Kathmandu'),
         ('https://suzutravels.com/wp-content/uploads/2026/10/nepal-tour-group-temple-gate.webp', 'Group tour, Nepal'),
         ('https://suzutravels.com/wp-content/uploads/2026/10/chitwan-lake-suzu-travels.webp', 'Chitwan')]
    h.append('<section id="real-trips" class="hx-sec"><span class="hx-eye">Real trips · real photos</span><h2>Our guests abroad</h2>'
             '<p class="hx-sub">Not stock photos — these were taken on Suzu Travels group tours in Nepal by our guests and our team. <a href="https://suzutravels.com/nepal-tour-packages/">See the Nepal trips →</a></p>'
             '<div class="hx-gal">' + ''.join(f'<figure><img src="{src}" alt="{html.escape(c)} — Suzu Travels guests" loading="lazy" decoding="async" width="800" height="600"><figcaption>{html.escape(c)}</figcaption></figure>' for src, c in G[:5]) + '</div></section>')
    # HOW BOOKING WORKS
    steps = [('chat', 'Tell us the basics', 'Destination, rough dates, how many travellers and the kind of trip you want. A WhatsApp message is enough.'),
             ('doc', 'Get a costed itinerary', 'We send a day-by-day plan with hotels, transfers, sightseeing and a clear per-person price. Usually within 24 hours.'),
             ('sliders', 'Adjust until it fits', 'Change hotels, add or drop days, shift the budget up or down. We re-quote as many times as you need.'),
             ('lock', 'Confirm with a token', 'Lock your rate with a small token amount. The balance is paid later, as agreed in writing.')]
    h.append('<section id="how-booking-works" class="hx-sec"><span class="hx-eye">Simple process</span><h2>How booking works</h2><div class="hx-steps">' +
             ''.join(f'<div class="hx-step"><div class="hx-n">{svg(i)}</div><b>{t}</b><p>{d}</p></div>' for i, t, d in steps) + '</div></section>')
    # WHY
    why = [('pin', 'A real operator, not a listing site', 'We have run ground operations since 2019 with our own office in Himachal, our own vehicles and our own staff. You deal with the people responsible for your trip.'),
           ('shield', 'Properly accredited', 'Registered as a travel agent with the Department of Tourism &amp; Civil Aviation, Government of Himachal Pradesh (Reg. No. DTO-MND-11-243/2022), and GST-registered since January 2021, with a registered office and a named team you can call. <a href="https://suzutravels.com/certificates/">See the certificates</a>.'),
           ('food', 'Built for Indian travellers', 'Vegetarian and Jain meal planning, Indian-food-friendly hotels, family and senior-citizen pacing, and honest advice on what to skip.'),
           ('team', 'One team, start to finish', 'The same team quotes your trip, books it and stays reachable on WhatsApp while you are travelling — including from a different time zone.')]
    h.append('<section id="why-book-your-international-trip-with-su" class="hx-sec"><span class="hx-eye">Why Suzu</span><h2>Why book your international trip with Suzu Travels</h2><div class="hx-why">' +
             ''.join(f'<div>{svg(i)}<b>{t}</b><p>{d}</p></div>' for i, t, d in why) + '</div></section>')
    # FAQ
    h.append('<section id="common-questions" class="hx-sec"><span class="hx-eye">FAQ</span><h2>Common questions</h2><div class="hx-faqs">' +
             ''.join(f'<details class="hx-faq"{" open" if k == 0 else ""}><summary>{html.escape(q)}</summary><div class="hx-ans"><p>{html.escape(a)}</p></div></details>' for k, (q, a) in enumerate(FAQ)) + '</div></section>')
    # FINAL
    h.append('<div class="hx-final">'
             f'<img src="{u("final")}" alt="{alt("final")}" width="1600" height="900" loading="lazy" decoding="async">'
             '<h2>Tell us where you want to go</h2><p>Send us your destination and rough dates. We will come back with a costed, day-by-day itinerary you can actually compare — no obligation.</p>'
             '<div class="hx-ctas"><a class="hx-btn" href="https://suzutravels.com/contact/">Request a Custom Quote ' + svg('arrow') + '</a>'
             f'<a class="hx-ghost" href="{wa("Hi Suzu Travels, I would like a quote for an international trip.")}" target="_blank" rel="noopener">{WA_SVG}WhatsApp us</a></div>'
             '<p class="hx-contact">Or call <strong>+91 70874 88961</strong> · <a href="mailto:info@suzutravels.com">info@suzutravels.com</a></p></div>')
    # credits
    seen = []
    for k, v in M.items():
        c = v.get('credit')
        if c and (c, v.get('license'), v.get('src')) not in seen:
            seen.append((c, v.get('license'), v.get('src')))
    cr = ' · '.join(f'<a href="{html.escape(s or "#", quote=True)}" rel="nofollow noopener" target="_blank">{html.escape(c)}</a> ({html.escape(l or "")})' for c, l, s in seen)
    h.append(f'<details class="hx-credits"><summary>Destination photo credits</summary><p>{cr}</p></details>')
    # schema
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    h.append('<script type="application/ld+json">' + json.dumps(faq_ld, ensure_ascii=False) + '</script>')
    h.append('<script>' + JS + '</script>')
    h.append('</div>')
    out = ''.join(h)
    assert '\n' not in out.replace('\\n', '')
    js = out[out.rfind('<script>'):]
    assert '&' not in js and '//' not in js, 'JS must not contain & or //'
    return out

if __name__ == '__main__':
    out = build()
    open('hub.html', 'w').write(out)
    print('hub.html', len(out))
