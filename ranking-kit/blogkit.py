#!/usr/bin/env python3
"""Suzu blog kit (szb) — designed, one-line post content for WordPress (wpautop-safe).

    import blogkit as K; html = K.render(spec)

spec keys: kicker, tag, sub, chips[(b,txt)], hero(item), quick[(b,txt)], updated, sections[...], gallery{h2,lead,items},
           snow{ids, h2, lead}, spots{h2, lead, items[(name, meta, text, link)]}, ctas{h2, lead, items[(href, title, text, badge)]},
           faqs[(q,a)], sources[(title,url)], wa (WhatsApp prefill)
Photo items come from the WP media library (suzu-<slug>-<role>-<n>) — see wp_items().
"""
import html, json, re, urllib.parse, urllib.request

WA = "https://wa.me/917087488961?text="
REG = "HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022"
LIC_URL = {"CC BY-SA 4.0": "https://creativecommons.org/licenses/by-sa/4.0/", "CC BY-SA 3.0": "https://creativecommons.org/licenses/by-sa/3.0/",
           "CC BY-SA 2.5": "https://creativecommons.org/licenses/by-sa/2.5/", "CC BY-SA 2.0": "https://creativecommons.org/licenses/by-sa/2.0/",
           "CC BY 4.0": "https://creativecommons.org/licenses/by/4.0/", "CC BY 3.0": "https://creativecommons.org/licenses/by/3.0/",
           "CC BY 2.0": "https://creativecommons.org/licenses/by/2.0/", "CC0": "https://creativecommons.org/publicdomain/zero/1.0/"}

CSS = """
.szb{--ink:#13202d;--mid:#566575;--navy:#0b1f33;--navy2:#14324f;--ice:#eaf4fb;--ice2:#f5f9fc;--gold:#d4a24c;--gold2:#f3d98f;--sky:#2f78b7;--line:#dfe7ee;font-size:17px;line-height:1.7;color:var(--ink)}
.szb *{box-sizing:border-box}.szb img{max-width:100%;height:auto}
.szb h2{font-size:clamp(24px,2.6vw,32px);line-height:1.2;margin:0 0 14px;color:var(--navy);letter-spacing:-.01em}
.szb h3{font-size:19px;margin:18px 0 8px;color:var(--navy)}
.szb a{color:var(--sky);text-decoration:underline;text-underline-offset:3px;text-decoration-color:rgba(47,120,183,.35);font-weight:600}
.szb .k{display:inline-block;font-size:12.5px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:8px}
.szb-hero{position:relative;border-radius:26px;overflow:hidden;min-height:min(78vh,620px);display:flex;align-items:flex-end;background:var(--navy);color:#fff;margin:0 0 28px;isolation:isolate}
.szb-hero>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;margin:0;animation:szbKB 28s ease-in-out infinite alternate}
@keyframes szbKB{from{transform:scale(1.03)}to{transform:scale(1.15) translate(-1.5%,-1%)}}
.szb-hero:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(6,18,31,.10),rgba(6,18,31,.25) 40%,rgba(6,18,31,.92)),linear-gradient(90deg,rgba(6,18,31,.6),rgba(6,18,31,0) 60%)}
.szb-flakes{position:absolute;inset:0;z-index:-1;pointer-events:none;background-image:radial-gradient(2px 2px at 10% 10%,#fff,transparent),radial-gradient(2px 2px at 30% 40%,#fff,transparent),radial-gradient(3px 3px at 55% 20%,#fff,transparent),radial-gradient(2px 2px at 75% 55%,#fff,transparent),radial-gradient(2px 2px at 90% 15%,#fff,transparent),radial-gradient(2px 2px at 45% 70%,#fff,transparent);background-size:420px 420px;animation:szbSnow 14s linear infinite;opacity:.75}
@keyframes szbSnow{from{background-position:0 0}to{background-position:-60px 420px}}
.szb-hero-in{padding:36px 36px 30px;max-width:760px}
.szb-hero .k{color:var(--gold2)}
.szb-tag{font-size:clamp(30px,4vw,48px);line-height:1.08;font-weight:800;margin:0 0 12px;letter-spacing:-.02em;color:#fff}.szb .szb-hero p.szb-tag,.szb .szb-hero .szb-chips li{color:#fff!important}.szb .szb-hero p.szb-sub{color:rgba(255,255,255,.9)!important}.szb .szb-quote p{color:rgba(255,255,255,.86)!important}
.szb-sub{font-size:17px;color:rgba(255,255,255,.88);margin:0 0 16px}
.szb-chips{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 18px;padding:0;list-style:none}
.szb-chips li{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.25);backdrop-filter:blur(6px);border-radius:99px;padding:6px 12px;font-size:14px;margin:0}
.szb-chips b{color:var(--gold2)}
.szb-btns{display:flex;flex-wrap:wrap;gap:10px}
.szb-btn{display:inline-block;padding:12px 20px;border-radius:99px;font-weight:800;text-decoration:none!important;font-size:15.5px}
.szb-btn.gold{background:var(--gold);color:#1a1205!important}.szb-btn.ghost{border:1.5px solid rgba(255,255,255,.7);color:#fff!important}
.szb-cr{display:block;font-size:11.5px;font-weight:400;opacity:.75;margin-top:4px}.szb-cr a{color:inherit!important;font-weight:400!important}
.szb-hero .szb-cr{position:absolute;right:14px;bottom:10px;background:rgba(6,18,31,.45);padding:2px 9px;border-radius:99px;color:#fff;margin:0;max-width:60%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.szb-upd{font-size:14px;color:var(--mid);margin:0 0 10px}
.szb-qa{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:18px 0 30px;padding:0;list-style:none}
.szb-qa li{background:var(--ice);border:1px solid #d3e6f3;border-radius:18px;padding:16px 18px;margin:0;font-size:15.5px;line-height:1.55}
.szb-qa li b{display:block;color:var(--navy);font-size:13px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:4px}
.szb-answer{border-left:4px solid var(--gold);background:#fffaf0;padding:16px 20px;border-radius:0 16px 16px 0;font-size:18px;margin:0 0 8px}
.szb-sec{margin:44px 0}
.szb-row{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:44px;align-items:center}
.szb-row figure{margin:0}.szb-row img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:20px;box-shadow:0 22px 50px -22px rgba(11,31,51,.55);margin:0}
.szb-row figcaption{font-size:13.5px;color:var(--mid);margin-top:8px}
.szb-tbl{width:100%;border-collapse:separate;border-spacing:0;border:1px solid var(--line);border-radius:16px;overflow:hidden;font-size:15.5px;margin:14px 0}
.szb-tbl th{background:var(--navy);color:#fff;text-align:left;padding:11px 14px;font-size:13.5px;letter-spacing:.04em}
.szb-tbl td{padding:11px 14px;border-top:1px solid var(--line);vertical-align:top}.szb-tbl tr:nth-child(even) td{background:var(--ice2)}
.szb-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}
.szb-gal{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-auto-rows:210px;grid-auto-flow:dense;gap:12px;margin-top:18px}
.szb-gal figure{position:relative;margin:0;border-radius:18px;overflow:hidden;background:var(--navy)}
.szb-gal figure:first-child{grid-column:span 2;grid-row:span 2}.szb-gal figure.w{grid-column:span 2}
.szb-gal img{width:100%;height:100%;object-fit:cover;margin:0;transition:transform 1.2s cubic-bezier(.2,.7,.2,1)}.szb-gal figure:hover img{transform:scale(1.07)}
.szb-gal figcaption{position:absolute;left:0;right:0;bottom:0;padding:28px 12px 9px;color:#fff;font-weight:700;font-size:13.5px;line-height:1.35;background:linear-gradient(180deg,rgba(6,18,31,0),rgba(6,18,31,.85))}
.szb-gal figcaption .szb-cr{color:rgba(255,255,255,.75)}
.szb-snow{background:radial-gradient(ellipse at 80% 0%,#1d4a74,var(--navy) 55%,#06121f);color:#eaf4fb;border-radius:24px;padding:26px;margin:18px 0;position:relative;overflow:hidden;isolation:isolate}
.szb-snow h3{color:#fff;margin-top:0}
.szb-snow .rows{display:grid;gap:12px}
.szb-sp{display:grid;grid-template-columns:200px minmax(0,1fr) 120px;gap:16px;align-items:center;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:16px;padding:12px 16px}
.szb-sp .nm{font-weight:800;color:#fff;line-height:1.2}.szb-sp .nm small{display:block;font-weight:500;color:rgba(234,244,251,.7);font-size:12.5px}
.szb-sp .bars{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;align-items:end;height:64px}
.szb-sp .bar{position:relative;background:rgba(255,255,255,.08);border-radius:6px 6px 3px 3px;height:100%;display:flex;flex-direction:column;justify-content:flex-end;overflow:hidden}
.szb-sp .bar i{display:block;background:linear-gradient(180deg,#fff,#a9d4f2);border-radius:5px 5px 2px 2px;min-height:2px;transition:height 1s cubic-bezier(.2,.7,.2,1)}
.szb-sp .bar span{position:absolute;left:0;right:0;top:3px;text-align:center;font-size:10.5px;color:rgba(234,244,251,.75)}
.szb-sp .wk{text-align:right;font-weight:800;font-size:22px;color:#fff;line-height:1}.szb-sp .wk small{display:block;font-size:11.5px;font-weight:600;color:rgba(234,244,251,.7);margin-top:4px}
.szb-sp.yes{border-color:rgba(243,217,143,.6);box-shadow:0 0 0 1px rgba(243,217,143,.25) inset}
.szb .szb-snow .note,.szb .szb-snow .rows>p{font-size:12.5px;color:rgba(234,244,251,.78)!important;margin:12px 0 0}
.szb-snow .note a{color:var(--gold2)}
.szb-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:16px}
.szb-card{position:relative;display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:18px;padding:18px;text-decoration:none!important;color:var(--ink)!important;transition:transform .2s,box-shadow .2s;font-weight:400!important}
.szb-card:hover{transform:translateY(-3px);box-shadow:0 18px 40px -18px rgba(11,31,51,.35)}
.szb-card .b{align-self:flex-start;font-size:11.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--sky);background:var(--ice);padding:3px 9px;border-radius:99px;margin-bottom:8px}
.szb-card .t{font-weight:800;color:var(--navy)!important;font-size:17px;line-height:1.3;text-decoration:none!important}.szb-card .t:after{content:"";position:absolute;inset:0;border-radius:18px;z-index:2}.szb-card .c{font-size:14.5px;color:var(--mid);margin-top:6px}
.szb-card .go{margin-top:auto;padding-top:10px;font-weight:800;color:var(--sky);font-size:14px}
.szb-spots{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin-top:16px}
.szb-spot{background:var(--ice2);border:1px solid var(--line);border-radius:18px;padding:18px;position:relative;overflow:hidden}
.szb-spot:before{content:"";position:absolute;inset:0 0 auto 0;height:4px;background:linear-gradient(90deg,var(--sky),var(--gold))}
.szb-spot h3{margin:0 0 4px}.szb-spot .m{font-size:13px;font-weight:700;color:var(--sky);margin-bottom:6px}.szb-spot p{font-size:15px;margin:0}
.szb-quote{background:linear-gradient(135deg,var(--navy),var(--navy2));color:#fff;border-radius:24px;padding:30px;display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:24px;align-items:center;margin:44px 0}
.szb-quote h2{color:#fff}.szb-quote p{color:rgba(255,255,255,.85);margin:0}.szb-quote .szb-btns{justify-content:flex-end}
.szb-faq details{border:1px solid var(--line);border-radius:14px;padding:12px 16px;margin:0 0 10px;background:#fff}
.szb-faq summary{cursor:pointer;font-weight:800;color:var(--navy)}.szb-faq details p{margin:10px 0 0}
.szb-src{font-size:14px;color:var(--mid)}.szb-src li{margin:0 0 4px}
@media(max-width:900px){.szb-row,.szb-quote{grid-template-columns:1fr;gap:20px}.szb-quote .szb-btns{justify-content:flex-start}.szb-gal{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:160px}.szb-sp{grid-template-columns:1fr;gap:8px}.szb-sp .wk{text-align:left}.szb-hero-in{padding:26px 20px 34px}.szb-hero:after{background:linear-gradient(180deg,rgba(6,18,31,.55),rgba(6,18,31,.72) 35%,rgba(6,18,31,.95))}.szb-hero-in{text-shadow:0 1px 12px rgba(0,0,0,.45)}.szb-hero .szb-cr{max-width:90%}}
@media(max-width:640px){.szb-tbl,.szb-tbl tbody,.szb-tbl tr,.szb-tbl td{display:block;width:100%}.szb-tbl thead{display:none}.szb-tbl{border:0;border-radius:0}.szb-tbl tr{border:1px solid var(--line);border-radius:14px;overflow:hidden;margin:0 0 10px;background:#fff}.szb-tbl td{border-top:1px solid var(--line);padding:8px 14px;background:#fff!important}.szb-tbl td:first-child{border-top:0;background:var(--navy)!important;color:#fff;font-weight:800}.szb-tbl td:not(:first-child):before{content:attr(data-l);display:block;font-size:11.5px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--sky);margin-bottom:2px}}\n@media(prefers-reduced-motion:reduce){.szb-hero>img,.szb-flakes{animation:none}}
"""

JS = """(function(){var d=document;function el(t,c,x){var n=d.createElement(t);if(c)n.className=c;if(x!=null)n.textContent=x;return n}
var W=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
var boxes=d.querySelectorAll('.szb-snow[data-ids]');if(!boxes.length)return;
fetch('/suzu-snow.php').then(function(r){return r.json()}).then(function(j){
Array.prototype.forEach.call(boxes,function(b){var ids=b.getAttribute('data-ids').split(','),rows=b.querySelector('.rows');if(!rows)return;rows.textContent='';
var max=1;j.places.forEach(function(p){p.days.forEach(function(x){if(x.snow_cm>max)max=x.snow_cm})});
ids.forEach(function(id){var p=null;j.places.forEach(function(q){if(q.id===id)p=q});if(!p)return;
var r=el('div','szb-sp'+(p.week_cm>0?' yes':''));var nm=el('div','nm',p.name);nm.appendChild(el('small',null,p.alt.toLocaleString('en-IN')+' m · '+(p.now&&p.now.t!=null?Math.round(p.now.t)+'°C now':'')));r.appendChild(nm);
var bars=el('div','bars');p.days.forEach(function(x){var bar=el('div','bar');var i=el('i');i.style.height='2px';bar.appendChild(i);var dt=new Date(x.d+'T00:00:00');bar.appendChild(el('span',null,W[dt.getDay()]));bar.title=x.d+': '+x.snow_cm+' cm snow, '+x.lo+' to '+x.hi+'°C';bars.appendChild(bar);setTimeout(function(){i.style.height=Math.max(2,Math.round(100*x.snow_cm/max))+'%'},120)});r.appendChild(bars);
var wk=el('div','wk',p.week_cm>0?p.week_cm+' cm':'No snow');wk.appendChild(el('small',null,p.next?'next: '+new Date(p.next.d+'T00:00:00').toLocaleDateString('en-IN',{weekday:'short',day:'numeric',month:'short'}):'next 7 days'));r.appendChild(wk);rows.appendChild(r)});
var u=b.querySelector('.upd');if(u&&j.updated)u.textContent=new Date(j.updated).toLocaleString('en-IN',{day:'numeric',month:'short',hour:'2-digit',minute:'2-digit'})});
}).catch(function(){Array.prototype.forEach.call(boxes,function(b){var s=b.closest('section')||b;s.style.display='none'})})})();"""


def e(s):
    return html.escape(str(s), quote=True)


def credit(it):
    lic = it.get("lic", "")
    licl = f'<a href="{LIC_URL[lic]}" target="_blank" rel="noopener license">{e(lic)}</a>' if lic in LIC_URL else e(lic)
    return f'Photo: <a href="{e(it["file"])}" target="_blank" rel="noopener">{e(it["by"] or "Wikimedia Commons")}</a>, {licl}'


def img(it, eager=False, sizes="100vw"):
    ss = f' srcset="{e(it["srcset"])}" sizes="{sizes}"' if it.get("srcset") else ""
    ld = ' fetchpriority="high" data-no-lazy="1"' if eager else ' loading="lazy"'
    return f'<img src="{e(it["src"])}"{ss} alt="{e(it["alt"])}" width="{it["w"]}" height="{it["h"]}"{ld} decoding="async" />'


def wp_items(slug):
    """Photos uploaded as suzu-<slug>-<role>-<n> with JSON description {file,by,lic,cap}."""
    q = urllib.parse.urlencode({"search": f"suzu-{slug}-", "per_page": 50, "_fields": "id,source_url,alt_text,media_details,description"})
    d = json.loads(urllib.request.urlopen(urllib.request.Request(f"https://suzutravels.com/wp-json/wp/v2/media?{q}", headers={"User-Agent": "SuzuKit/1.0"}), timeout=60).read())
    out = []
    for m in d:
        fn = m["source_url"].rsplit("/", 1)[-1]
        mm = re.match(rf"suzu-{re.escape(slug)}-(hero|fig|g|bg|side)-(\d+)(?:-scaled)?\.", fn)
        if not mm:
            continue
        desc = html.unescape(re.sub(r"<[^>]+>", "", m["description"]["rendered"]))
        for a, b in (("“", '"'), ("”", '"'), ("″", '"'), ("′", "'"), ("’", "'"), ("‘", "'")):
            desc = desc.replace(a, b)
        meta = json.loads(desc[desc.find("{"):desc.rfind("}") + 1])
        by = re.sub(r"\s+", " ", meta.get("by", "")).strip()
        if len(by) > 60:
            mt = re.search(r"(?:taken|photographed|shot|uploaded) by ([A-Z][a-z'-]+(?: [A-Z]\.)*(?: [A-Z][a-z'-]+){0,3})", by)
            by = mt.group(1) if mt else re.split(r"[;(]|\. ", by)[0][:60]
        md = m["media_details"]; sz = md.get("sizes", {})
        ss = [f'{sz[k]["source_url"]} {sz[k]["width"]}w' for k in ("medium_large", "large", "1536x1536") if k in sz] + [f'{m["source_url"]} {md["width"]}w']
        out.append({"role": mm.group(1), "n": int(mm.group(2)), "id": m["id"], "src": m["source_url"], "srcset": ", ".join(ss), "w": md["width"], "h": md["height"],
                    "alt": m["alt_text"], "cap": meta.get("cap", ""), "by": by, "lic": meta.get("lic", ""), "file": meta.get("file", ""),
                    "thumb": sz.get("medium_large", {"source_url": m["source_url"]})["source_url"]})
    return sorted(out, key=lambda x: x["n"])


def role(items, r):
    return next((x for x in items if x["role"] == r), None)


def render(s):
    P = s["photos"]
    hero, fig = role(P, "hero"), role(P, "fig")
    gal = [x for x in P if x["role"] == "g"]
    wa = WA + urllib.parse.quote(s["wa"])
    out = [f"<style>{min_css(CSS)}</style><div class=\"szb\">"]
    chips = "".join(f"<li><b>{e(a)}</b> {e(b)}</li>" for a, b in s.get("chips", []))
    out.append(f'<section class="szb-hero">{img(hero, True)}{"<div class=szb-flakes></div>" if s.get("flakes") else ""}<div class="szb-hero-in"><span class="k">{e(s["kicker"])}</span>'
               f'<p class="szb-tag">{e(s["tag"])}</p><p class="szb-sub">{s["sub"]}</p><ul class="szb-chips">{chips}</ul>'
               f'<div class="szb-btns"><a class="szb-btn gold" href="{wa}" target="_blank" rel="noopener">WhatsApp +91 70874 88961</a><a class="szb-btn ghost" href="{s.get("cta2", ("/himachal-tour-packages-quote/", "Get a free quote"))[0]}">{e(s.get("cta2", ("", "Get a free quote"))[1])}</a></div></div>'
               f'<span class="szb-cr">{credit(hero)}</span></section>')
    out.append(f'<p class="szb-upd">Updated {e(s["updated"])} · {REG} · <a href="/certificates/">certificates</a></p>')
    out.append(f'<div class="szb-answer"><p>{s["answer"]}</p></div>')
    if s.get("quick"):
        out.append('<ul class="szb-qa">' + "".join(f"<li><b>{e(a)}</b>{b}</li>" for a, b in s["quick"]) + "</ul>")
    for sec in s["sections"]:
        out.append(section(sec, fig if sec.get("fig") else None, s))
    if s.get("snow"):
        sn = s["snow"]
        out.append(f'<section class="szb-sec" id="forecast"><span class="k">Live forecast</span><h2>{e(sn["h2"])}</h2><p>{sn["lead"]}</p>'
                   f'<div class="szb-snow" data-ids="{e(",".join(sn["ids"]))}"><h3>Snow in the next 7 days</h3><div class="rows"><p>Loading the latest forecast…</p></div>'
                   f'<p class="note">Forecast data: <a href="https://api.met.no/" target="_blank" rel="noopener">MET Norway</a> (CC BY 4.0), refreshed through the day — last update <span class="upd">—</span>. Snow in cm is estimated from forecast precipitation (1 mm ≈ 1 cm) when it falls as snow; treat it as a guide, not a promise.</p></div></section>')
    if gal:
        cls = ["big"] + [""] * 4 + ["w", "w", "", ""]
        figs = "".join(f'<figure{" class=w" if k == "w" else ""}>{img(it, sizes="(max-width:900px) 50vw, 25vw")}<figcaption>{e(it["cap"])}<span class="szb-cr">{credit(it)}</span></figcaption></figure>'
                       for it, k in zip(gal, cls))
        g = s["gallery"]
        out.append(f'<section class="szb-sec" id="photos"><span class="k">In pictures</span><h2>{e(g["h2"])}</h2><p>{g["lead"]}</p><div class="szb-gal">{figs}</div></section>')
    if s.get("spots"):
        sp = s["spots"]
        cards = "".join(f'<div class="szb-spot"><h3>{e(n)}</h3><div class="m">{e(m)}</div><p>{t}</p></div>' for n, m, t in sp["items"])
        out.append(f'<section class="szb-sec" id="spots"><span class="k">{e(sp.get("kicker", "Where to go"))}</span><h2>{e(sp["h2"])}</h2><p>{sp["lead"]}</p><div class="szb-spots">{cards}</div></section>')
    for sec in s.get("sections2", []):
        out.append(section(sec, None, s))
    c = s["ctas"]
    cards = "".join(f'<div class="szb-card"><span class="b">{e(b)}</span><a class="t" href="{h}">{e(t)}</a><span class="c">{x}</span><span class="go">See the plan →</span></div>' for h, t, x, b in c["items"])
    out.append(f'<section class="szb-sec" id="plan"><span class="k">Plan it with Suzu</span><h2>{e(c["h2"])}</h2><p>{c["lead"]}</p><div class="szb-cards">{cards}</div></section>')
    out.append(f'<div class="szb-quote"><div><h2>{e(s["quote_h2"])}</h2><p>{s["quote_text"]}</p></div><div class="szb-btns"><a class="szb-btn gold" href="{wa}" target="_blank" rel="noopener">WhatsApp us</a>'
               f'<a class="szb-btn ghost" href="tel:+917087488961">Call +91 70874 88961</a></div></div>')
    out.append('<section class="szb-sec szb-faq" id="faq"><span class="k">FAQ</span><h2>' + e(s.get("faq_h2", "Questions travellers ask")) + "</h2>"
               + "".join(f"<details><summary>{e(q)}</summary><p>{a}</p></details>" for q, a in s["faqs"]) + "</section>")
    src = "".join(f'<li><a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a></li>' for t, u in s["sources"])
    seen, cr = set(), []
    for it in P:
        if it["file"] in seen:
            continue
        seen.add(it["file"]); cr.append(f'{e(it["cap"])} — {credit(it)}')
    out.append(f'<section class="szb-sec szb-src"><h3>Sources</h3><ol>{src}</ol><h3>Photo credits</h3><p>{" · ".join(cr)}</p></section>')
    out.append("</div>")
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(re.sub(r"<[^>]+>", "", a))}} for q, a in s["faqs"]]}
    out.append('<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False).replace("</", "<\\/") + "</script>")
    if s.get("snow"):
        out.append(f"<script>{JS}</script>")
    h = "".join(out)
    h = re.sub(r">\s+<", "><", h)
    return re.sub(r"\s+", " ", h).strip()


def section(sec, fig, s):
    body = "".join(f"<p>{p}</p>" for p in sec.get("ps", []))
    if sec.get("table"):
        hd, rows = sec["table"]
        body += '<div class="szb-scroll"><table class="szb-tbl"><thead><tr>' + "".join(f"<th>{e(x)}</th>" for x in hd) + "</tr></thead><tbody>" + \
                "".join("<tr>" + "".join(f'<td data-l="{e(hd[i])}">{x}</td>' for i, x in enumerate(r)) + "</tr>" for r in rows) + "</tbody></table></div>"
    body += "".join(f"<p>{p}</p>" for p in sec.get("after", []))
    head = f'<span class="k">{e(sec.get("kicker", ""))}</span><h2>{e(sec["h2"])}</h2>'
    if fig:
        return (f'<section class="szb-sec" id="{sec["id"]}">{head}<div class="szb-row"><div>{body}</div><figure>{img(fig, sizes="(max-width:900px) 100vw, 40vw")}'
                f'<figcaption><b>{e(fig["cap"])}</b><span class="szb-cr">{credit(fig)}</span></figcaption></figure></div></section>')
    return f'<section class="szb-sec" id="{sec["id"]}">{head}{body}</section>'


def min_css(c):
    c = re.sub(r"\s+", " ", c)
    return re.sub(r"\s*([{}:;,>])\s*", r"\1", c).replace(";}", "}").strip()
