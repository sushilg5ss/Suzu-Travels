#!/usr/bin/env python3
"""Suzu Mountain Kit — page generator.

    python3 gen_pages.py <slug|all>        -> out/<slug>.html   (then: python3 build.py <slug> -> out/<slug>.min.html)

Every number on a page (heights, counts, first-ascent years) comes from data/peaks.json — never type one by hand.
Pages: mountains-of-india (hub) · highest-peaks-in-india (master list) · himalayan-peak-expeditions (enquiry page, under /adventure/)
New page kinds (peak / band / state / guide) are added here by the Mountain Page Builder agent, one function each,
re-using the blocks below. Copy is original English; facts must trace to research/*.md or a source listed on the page.
"""
import html, json, pathlib, random, sys, urllib.parse

KIT = pathlib.Path(__file__).resolve().parent
P = json.loads((KIT / "data" / "peaks.json").read_text(encoding="utf-8"))
BY = {p["id"]: p for p in P}
MEDIA = json.loads((KIT / "media.json").read_text()) if (KIT / "media.json").exists() else {}
LIVE = json.loads((KIT / "live.json").read_text()) if (KIT / "live.json").exists() else {}
VERIFIED = "1 Oct 2026"
REPO = "sushilg5ss/suzu-travels"
HUB = "/mountains-of-india/"
LIST = "/mountains-of-india/highest-peaks-in-india/"
EXP = "/adventure/himalayan-peak-expeditions/"
WA = "https://wa.me/917087488961?text="
QUOTE = "/himachal-tour-packages-quote/"
REG = "HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022"
STATE_ORDER = ["sikkim", "uttarakhand", "ladakh", "jammu-kashmir", "himachal-pradesh", "arunachal-pradesh", "west-bengal"]
BAND_LABEL = {"8000": "8,000 m +", "7000": "7,000–7,999 m", "6000": "6,000–6,999 m", "5000": "5,000–5,999 m", "4000": "4,000–4,999 m", "3000": "3,000–3,999 m"}
STATUS_LABEL = {"climbed": "Climbed", "unclimbed": "Unclimbed", "closed": "Closed", "restricted": "Restricted"}
GRADE_LABEL = {"trekking peak": "Trekking peak", "moderate": "Moderate", "technical": "Technical", "extreme": "Extreme"}


def e(s):
    return html.escape(str(s), quote=True)


def n(x):
    return f"{x:,}"


def pk(pid):
    return BY[pid]


def hm(pid):
    """'8,586 m' for a peak id (single source of truth)."""
    return f"{n(BY[pid]['m'])} m"


def wa(text):
    return WA + urllib.parse.quote(text)


def link(path, text):
    return f'<a href="{path}">{text}</a>'


def ext(url, text):
    return f'<a href="{e(url)}" target="_blank" rel="noopener">{text}</a>'


def pill(status):
    return f'<span class="szm-st {status}">{STATUS_LABEL[status]}</span>'


def media_url(slug, fname):
    sha = MEDIA.get(slug)
    if not sha:
        raise SystemExit(f"media.json has no commit pinned for '{slug}' — run make_media.sh, push, then pin_media.py")
    return f"https://cdn.jsdelivr.net/gh/{REPO}@{sha}/mountain-kit/media/{slug}/{fname}"


def data_url(fname):
    sha = MEDIA.get("data")
    if not sha:
        raise SystemExit("media.json has no commit pinned for 'data'")
    return f"https://cdn.jsdelivr.net/gh/{REPO}@{sha}/mountain-kit/data/{fname}"


def hero_video(slug, comp, alt):
    u = lambda f: media_url(slug, f)
    return (f'<video autoplay muted loop playsinline preload="metadata" poster="{u(comp + "-poster.webp")}" aria-label="{e(alt)}">'
            f'<source media="(max-width: 640px)" src="{u(comp + "-m.webm")}" type="video/webm">'
            f'<source media="(max-width: 640px)" src="{u(comp + "-m.mp4")}" type="video/mp4">'
            f'<source src="{u(comp + ".webm")}" type="video/webm"><source src="{u(comp + ".mp4")}" type="video/mp4"></video>')


def lazy_video(slug, comp, alt):
    u = lambda f: media_url(slug, f)
    return (f'<video data-lazy muted loop playsinline preload="none" poster="{u(comp + "-poster.webp")}" aria-label="{e(alt)}">'
            f'<source data-src="{u(comp + ".webm")}" type="video/webm"><source data-src="{u(comp + ".mp4")}" type="video/mp4"></video>')


def nav(items, cta_href):
    a = "".join(f'<a href="#{i}">{t}</a>' for i, t in items)
    return f'<nav class="szm-nav" aria-label="On this page"><div class="szm-nav-in">{a}<a class="cta" href="{cta_href}">Get Quote</a></div></nav>'


def faq(items):
    h = "".join(f"<details><summary>{e(q)}</summary><p>{a}</p></details>" for q, a in items)
    return f'<div class="szm-faq">{h}</div>'


def faq_ld(items):
    import re
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(strip(a))}} for q, a in items]}


def ld(*objs):
    g = {"@context": "https://schema.org", "@graph": list(objs)}
    return '<script type="application/ld+json">' + json.dumps(g, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def ridge(seed, m):
    """Tiny decorative ridge for a peak card (apex height follows the peak's altitude)."""
    r = random.Random(seed)
    top = 8 + max(0, (8600 - m)) / 5600 * 34
    ax = r.uniform(110, 190)
    pts = [(0, 60 + r.uniform(-6, 6)), (ax * .45, 40 + r.uniform(0, 14)), (ax * .75, 30 + r.uniform(0, 10)), (ax, top), (ax + 45, 28 + r.uniform(0, 12)), (ax + 85, 44 + r.uniform(0, 10)), (300, 50 + r.uniform(-6, 8))]
    d = "M0 78 " + " ".join(f"L{x:.0f} {y:.0f}" for x, y in pts) + " L300 78Z"
    cap = f"M{ax - 18:.0f} {top + 14:.0f}L{ax:.0f} {top:.0f}L{ax + 16:.0f} {top + 12:.0f}L{ax + 6:.0f} {top + 10:.0f}L{ax - 4:.0f} {top + 16:.0f}Z"
    return f'<svg viewBox="0 0 300 78" preserveAspectRatio="none" aria-hidden="true"><path d="{d}" fill="#1c4468"/><path d="{cap}" fill="#eef6fb"/></svg>'


def peak_card(p, badge, extra=""):
    fa = f"First ascent <b>{p['fa']}</b>" if p["fa"] else "First ascent <b>not recorded</b>"
    return (f'<li class="szm-peak"><div class="top"><span class="rk">{badge}</span><div class="h num">{n(p["m"])} m<small>{n(p["ft"])} ft</small></div>{ridge(p["id"], p["m"])}</div>'
            f'<div class="body"><h3>{e(p["name"])}</h3><div class="meta">{e(p["where"])}</div><div class="meta">{fa} · {pill(p["status"])}</div>'
            f'{extra}<div class="go"><a href="{LIST}#peak-{p["id"]}">In the full list →</a></div></div></li>')


def quote_block(title, text, wa_text, second=None):
    s = second or (QUOTE, "Send a quote request")
    return (f'<div class="szm-quote"><div><span class="k">Plan it with Suzu</span><h2>{title}</h2><p>{text}</p></div>'
            f'<div class="szm-btns"><a class="szm-btn gold" href="{wa(wa_text)}" target="_blank" rel="noopener">WhatsApp +91 70874 88961</a>'
            f'<a class="szm-btn ghost" href="{s[0]}">{s[1]}</a></div></div>')


def trust(extra=""):
    return (f'<div class="szm-trust"><span><a href="/certificates/">{REG}</a></span>'
            f'<span>Facts checked {VERIFIED}</span><span>Sources listed on the page</span>{extra}</div>')


def sources(items):
    return '<ol class="szm-src">' + "".join(f"<li>{ext(u, e(t))}</li>" for t, u in items) + "</ol>"


def page(body, js=True):
    return f'<div class="szm">{body}</div>' + ('<script>/*KITJS*/</script>' if js else "")


# ------------------------------------------------------------------------------------------------ stats
def counts():
    by_band, by_state, by_status = {}, {}, {}
    for p in P:
        by_band[p["band"]] = by_band.get(p["band"], 0) + 1
        by_state[p["state"]] = by_state.get(p["state"], 0) + 1
        by_status[p["status"]] = by_status.get(p["status"], 0) + 1
    return by_band, by_state, by_status


BB, BS, BST = counts()
TOTAL = len(P)
N7000 = sum(1 for p in P if p["m"] >= 7000)
TOP10 = sorted([p for p in P if p["rank"] and p["rank"] <= 10], key=lambda p: p["rank"])
STATE_HI = {s: max((p for p in P if p["state"] == s), key=lambda p: p["m"]) for s in STATE_ORDER}
STATE_NAME = {p["state"]: p["state_label"] for p in P}

SRC_CORE = [
    ("Indian Mountaineering Foundation — peak fees for foreign expeditions", "https://www.indmount.org/IMF/peakfee"),
    ("Indian Mountaineering Foundation — expedition application rules", "https://www.indmount.org/IMF/expeapp"),
    ("PIB, 21 Aug 2019 — 137 peaks opened to foreigners", "https://www.pib.gov.in/newsite/PrintRelease.aspx?relid=192750&reg=48&lang=2"),
    ("The News Mill, Feb 2026 — Uttarakhand opens 83 peaks", "https://thenewsmill.com/2026/02/uttarakhand-opens-83-himalayan-peaks-for-mountaineering-expeditions/"),
    ("ThePrint — Sikkim ban on climbing Kangchenjunga", "https://theprint.in/india/sikkim-bhutia-lepcha-apex-committee-urges-govt-to-uphold-ban-on-climbing-mt-kanchenjunga/2638144/"),
    ("Wikipedia — List of mountains in India", "https://en.wikipedia.org/wiki/List_of_mountains_in_India"),
    ("Wikipedia — Indian states and territories by highest point", "https://en.wikipedia.org/wiki/List_of_Indian_states_and_territories_by_highest_point"),
    ("Wikipedia — Nanda Devi", "https://en.wikipedia.org/wiki/Nanda_Devi"),
    ("Wikipedia — Stok Kangri", "https://en.wikipedia.org/wiki/Stok_Kangri"),
    ("Free Press Journal — Indian Army's first ascent of Kangto (2025)", "https://www.freepressjournal.in/india/indian-army-mountaineers-make-historic-first-ascent-of-arunachal-pradeshs-mount-kangto"),
    ("HP Miscellaneous Adventure Activities (Amendment) Rules 2021", "https://www.legitquest.com/act/himachal-pradesh-miscellaneous-adventure-activities-amendment-rules-2021/A36F"),
    ("The Tribune — Kangra makes trekker registration compulsory (2026)", "https://www.tribuneindia.com/news/himachal/kangra-administration-makes-registration-compulsory-for-trekkers/"),
    ("CDC Yellow Book — high-altitude travel and altitude illness", "https://www.cdc.gov/yellow-book/hcp/environmental-hazards-risks/high-altitude-travel-and-altitude-illness.html"),
    ("Wikipedia — 1965 Indian Everest Expedition", "https://en.wikipedia.org/wiki/1965_Indian_Everest_Expedition"),
    ("Wikipedia — Nanda Devi plutonium mission", "https://en.wikipedia.org/wiki/Nanda_Devi_Plutonium_Mission"),
]


# ------------------------------------------------------------------------------------------------ HUB
def hub():
    kc, nd, kt, rp = pk("kangchenjunga"), pk("nanda-devi"), pk("kamet"), pk("reo-purgyil")
    faqs = [
        ("What is the highest mountain in India?",
         f"Kangchenjunga, {n(kc['m'])} m ({n(kc['ft'])} ft), on the Sikkim–Nepal border. It is the third-highest mountain on Earth. India's official map also places K2 (8,611 m) inside Ladakh, but K2 stands in Gilgit-Baltistan, which Pakistan administers, so Kangchenjunga is the highest peak on ground India controls."),
        ("Is K2 in India?",
         "India claims it. The official map of India shows K2 (8,611 m) as part of the Union Territory of Ladakh, but the mountain lies in Gilgit-Baltistan, which is administered by Pakistan, and every expedition reaches it from Pakistan. That is why most lists name Kangchenjunga as India's highest peak."),
        ("Which is the highest peak that lies entirely inside India?",
         f"Nanda Devi, {n(nd['m'])} m, in Uttarakhand's Chamoli district. It has been closed to climbers since 1983. Uttarakhand's February 2026 list of open peaks includes Nanda Devi East ({hm('nanda-devi-east')}), not the main summit."),
        ("How many 7,000 m peaks does India have?",
         f"Wikipedia's list of Indian summits with at least 500 m of prominence counts 38 above 7,000 m. Count subsidiary tops and border summits as well and the number is higher: our dataset lists {N7000} summits of 7,000 m or more, Kangchenjunga included."),
        ("What is the highest peak in Himachal Pradesh?",
         f"Reo Purgyil, {n(rp['m'])} m, on the Kinnaur–Tibet border above Nako. It was first climbed in {rp['fa']}. Foreigners need a protected-area permit for this border belt."),
        ("Can foreigners climb mountains in India?",
         "Yes. Foreign teams apply to the Indian Mountaineering Foundation (IMF) at least 90 days ahead, climb with an IMF liaison officer and pay a peak fee in US dollars. In 2019 the government opened 137 peaks to foreign climbers, and border areas also need a protected-area permit. Sacred and military-zone peaks stay closed."),
        ("Is Stok Kangri open in 2026?",
         f"No. Stok Kangri ({hm('stok-kangri')}) in Ladakh has been closed to climbing since 2020 and no reopening has been announced. Popular alternatives are Yunam ({hm('mount-yunam')}) and Friendship Peak ({hm('friendship-peak')}) in Himachal, or Kang Yatse II in Ladakh."),
        ("When is the best season to climb in the Indian Himalaya?",
         "In Himachal and Uttarakhand: May–June and September–October, either side of the monsoon. In the rain-shadow of Ladakh, Zanskar, Lahaul and Spiti: July–September. Sikkim's government suggests May–October, but most operators prefer April–May and October–November there."),
    ]
    # ladder rows
    bex = {
        "8000": f"{link(LIST + '#peak-kangchenjunga', 'Kangchenjunga')} — India's only 8,000 m summit. Sacred in Sikkim and closed to climbing from the Indian side.",
        "7000": f"Expedition giants such as {link(LIST + '#peak-kamet', 'Kamet')}, Saser Kangri, Nun and Trisul. Plan on three to five weeks, prior high-altitude experience and an IMF permit.",
        "6000": f"The big step up: Deo Tibba, Reo Purgyil, Shivling, Changabang. A few are non-technical, like {link(LIST + '#peak-mount-yunam', 'Yunam')}; most need rope work.",
        "5000": f"First real summits: {link(LIST + '#peak-friendship-peak', 'Friendship Peak')}, Ladakhi, Hanuman Tibba, Kanamo. Snow slopes, ice axe and crampons — usually with a guide.",
        "4000": "High trekking tops such as Chanshal, Patalsu and Pangarchulla — long days, no ropes.",
        "3000": f"Hill summits and trek tops: {link(LIST + '#peak-churdhar', 'Churdhar')}, Kedarkantha, Chandrashila, Sandakphu.",
    }
    mx = max(BB.values())
    rows = "".join(
        f'<li><div class="b">{BAND_LABEL[b]}<small>{BB[b]} peak{"s" if BB[b] != 1 else ""}</small></div>'
        f'<div><div class="bar"><i style="width:{max(3, round(BB[b] / mx * 100))}%"></i></div><div class="d">{bex[b]} {link(LIST + "#band-" + b, "See the list →")}</div></div></li>'
        for b in ["8000", "7000", "6000", "5000", "4000", "3000"])
    top_cards = "".join(peak_card(p, f"#{p['rank']}", f'<p class="meta">{e(p["notable"])}</p>' if p["notable"] else "") for p in TOP10)
    state_notes = {
        "ladakh": "Stands on the Siachen ground-position line, a military zone; the highest summit fully under Indian control is Saser Kangri I, " + hm("saser-kangri-i") + ".",
        "jammu-kashmir": "Nun sits on the J&K–Ladakh boundary above the Suru valley.",
        "arunachal-pradesh": "Heights quoted from 7,042 to 7,090 m; first climbed in late 2025.",
        "sikkim": "Sacred: climbing it from Sikkim has been banned since 2001.",
        "uttarakhand": "Closed since 1983 — the highest peak wholly inside India.",
        "himachal-pradesh": "On the Kinnaur–Tibet border above Nako.",
        "west-bengal": "Trek summit on the Singalila ridge with views of Kangchenjunga.",
    }
    tiles = "".join(
        f'<a class="szm-state" href="{LIST}#state-{s}"><span class="n">{e(STATE_NAME[s])}</span><span class="h num">{n(STATE_HI[s]["m"])} m</span>'
        f'<span class="p"><b>{e(STATE_HI[s]["name"])}</b> — {state_notes[s]}</span><span class="c">{BS[s]} peaks in our list →</span></a>'
        for s in STATE_ORDER)

    def li(pid, text):
        p = pk(pid)
        return f"<li><b>{e(p['name'])}</b> ({n(p['m'])} m) — {text}</li>"
    closed = (li("nanda-devi", "Uttarakhand. The Nanda Devi Sanctuary and main summit have been closed since 1983; only Nanda Devi East is on the state's 2026 open list.")
              + li("stok-kangri", "Ladakh. Closed since 2020 over crowding and glacier damage; no reopening announced for 2026."))
    sacred = (li("kangchenjunga", "Sikkim banned climbing it in 2001 (Notification 70/HOME/2001). Climbers who reach it from Nepal stop short of the summit, a promise first made in 1955.")
              + li("manimahesh-kailash", "Chamba, Himachal. Pilgrims circle the lake below; the summit itself has no confirmed ascent.")
              + li("shrikhand-mahadev", "Kullu, Himachal. A July pilgrim trek to the rock lingam, not a climbing objective.")
              + "<li><b>Siachen and border peaks</b> — Saltoro Kangri, K12, Ghent Kangri and the Teram Kangri group sit in a military zone and are not normally open to civilian teams.</li>")
    unclimbed = (li("apsarasas-kangri-ii", "Siachen; listed as virgin by the IMF.")
                 + li("nyegyi-kansang", "Arunachal; a 1995 claim is disputed.")
                 + li("shudu-tsenpa", "Sikkim; no recorded attempts.")
                 + li("chiumo", "Arunachal; no documented ascent.")
                 + li("chombu", "North Sikkim; no documented ascent.")
                 + li("parvati-parbat", "Kullu, Himachal; no documented ascent found (treat as uncertain).")
                 + f"<li><b>Recently climbed:</b> Kangto ({hm('kangto')}), Arunachal's highest, got its first recorded ascent in late 2025.</li>")
    hard = [
        ("changabang", "A granite fang above the Bagini glacier. First climbed in 1974 by an Indo-British team; Peter Boardman and Joe Tasker's 1976 West Wall is a landmark of Himalayan big-wall climbing."),
        ("thalay-sagar", "A steep rock-and-ice pyramid above Kedar Tal, first climbed in 1979. Several of its routes have won the Piolet d'Or."),
        ("meru-central", "The central summit was reached in 2001, but the Shark's Fin line waited until 2011 — Conrad Anker, Jimmy Chin and Renan Ozturk's climb, told in the film Meru (2015)."),
        ("shivling", "The 'Matterhorn of the Himalaya' above Gaumukh. First climbed by an ITBP team in 1974; its ridges and faces are still prized technical lines."),
        ("saser-kangri-ii-east", "Until 2011 it was the world's second-highest unclimbed peak. Mark Richey, Steve Swenson and Freddie Wilkinson's first ascent won the Piolet d'Or."),
        ("janhukut", "A steep Gangotri summit that stayed unclimbed until 2018, when Malcolm Bass, Paul Figg and Guy Buckingham reached the top."),
    ]
    hard_cards = "".join(f'<div class="szm-card"><div class="h num">{hm(pid)}</div><h3>{e(pk(pid)["name"])}</h3><p>{t}</p></div>' for pid, t in hard)
    tl = [
        ("1907", "Trisul — the first 7,000 m summit ever climbed", f"Tom Longstaff, the Brocherel brothers and Karbir reached the top of Trisul ({hm('trisul-i')}) on 12 June 1907."),
        ("1911", "Pauhunri", f"Alexander Kellas and two Sherpas climbed Pauhunri ({hm('pauhunri')}) in Sikkim — the highest summit climbed at the time, a record that stood until 1928."),
        ("1931", "Kamet — the first summit above 25,000 ft", f"Frank Smythe's team, with Lewa Sherpa, topped Kamet ({hm('kamet')}) on 21 June 1931."),
        ("1936", "Nanda Devi", f"Bill Tilman and Noel Odell reached the summit ({hm('nanda-devi')}) on 29 August 1936. No higher peak was climbed until Annapurna in 1950."),
        ("1955", "Kangchenjunga — and a promise", "George Band and Joe Brown stopped just short of the summit, honouring Sikkim's reverence for the mountain. Most climbers still do."),
        ("1965", "India's first Everest success", "Avtar Singh Cheema and Nawang Gombu summited on 20 May; Capt. M.S. Kohli's expedition put nine climbers on top, a record that stood for 13 years."),
        ("1974", "Changabang and Shivling", "The two Garhwal icons were first climbed on consecutive days, 3 and 4 June 1974."),
        ("1977", "Kangchenjunga from Sikkim", "An Indian Army team led by Col. Narendra Kumar made the second ascent, via the north-east spur."),
        ("1984", "Bachendri Pal", "On 23 May she became the first Indian woman to stand on Everest."),
        ("2011", "Shark's Fin and Saser Kangri II East", "Two of the great unsolved Indian Himalayan problems fell in the same year."),
        ("2013", "Arunima Sinha", "The first woman amputee to summit Everest, on 21 May."),
        ("2022", "Baljeet Kaur of Himachal", "The Solan climber summited a string of 8,000 m peaks in one season, including Manaslu without supplementary oxygen — a first for an Indian woman."),
        ("2025", "Kangto climbed", "An Indian Army team made the first recorded ascent of Arunachal Pradesh's highest peak."),
        ("2026", "83 Uttarakhand peaks opened", "In February the state opened 83 peaks from 5,700 m to 7,756 m and waived its own fees for Indian climbers."),
    ]
    tl_html = "".join(f'<li><div class="y">{y}</div><div><div class="t">{t}</div><div class="x">{x}</div></div></li>' for y, t, x in tl)
    insts = [
        ("ABVIMAS", "Manali, Himachal Pradesh", "26 days; batches May–October", "Indians and foreigners, 16–45"),
        ("NIM", "Uttarkashi, Uttarakhand", "28 days; spring and autumn batches", "Indians and foreigners, 16–40"),
        ("HMI", "Darjeeling, West Bengal", "28 days", "Indians and foreigners, 17–45"),
        ("JIM&amp;WS", "Pahalgam, Jammu &amp; Kashmir", "24 days; May–August", "Ages 17–40"),
        ("NIMAS", "Dirang, Arunachal Pradesh", "Basic and advanced courses", "Check the institute's site"),
    ]
    inst_rows = "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in insts)
    watxt = "Hi Suzu Travels, I want to plan a guided peak climb in Himachal. Peak: ___ , dates: ___ , people: ___"
    body = f'''
<section class="szm-hero">{hero_video("mountains-of-india", "mountains-hero", "Climbers on Himalayan snow slopes, with an altitude read-out rising from 3,000 m to 8,586 m")}
<div class="szm-hero-in"><span class="k">Mountains of India · 3,000 m to {n(kc['m'])} m</span>
<p class="szm-tag">India's Himalaya, peak by peak.</p>
<p class="szm-sub">{TOTAL} summits across seven states, from Churdhar to Kangchenjunga — how high they are, who climbed them first, which ones are open, and how permits work. Ready to climb one? We plan it with you from Himachal.</p>
<ul class="szm-chips"><li><b>{n(kc['m'])} m</b> Kangchenjunga</li><li><b>{n(nd['m'])} m</b> Nanda Devi</li><li><b>38</b> major 7,000 m summits</li><li><b>137</b> peaks opened to foreigners (2019)</li><li><b>83</b> Uttarakhand peaks opened (2026)</li></ul>
<div class="szm-btns"><a class="szm-btn gold" href="{LIST}">See all {TOTAL} peaks</a><a class="szm-btn ghost" href="{EXP}">Plan a guided climb</a></div>
{trust()}</div></section>
{nav([("overview", "Overview"), ("ladder", "Height ladder"), ("top10", "Top 10"), ("states", "By state"), ("status", "Open or closed"), ("hardest", "Hardest"), ("records", "Records"), ("permits", "Permits"), ("training", "Training"), ("faq", "FAQ")], wa(watxt))}
<section class="szm-sec" id="overview"><span class="szm-verified">Last verified {VERIFIED}</span>
<h2>What is the highest mountain in India?</h2>
<div class="szm-answer"><p><b>Kangchenjunga ({n(kc['m'])} m / {n(kc['ft'])} ft)</b>, on the Sikkim–Nepal border, is the highest mountain in India and the third-highest on Earth. India's official map also shows <b>K2 (8,611 m)</b> inside Ladakh, but K2 stands in Gilgit-Baltistan, which Pakistan administers. The highest peak that lies entirely inside India is <b>Nanda Devi ({n(nd['m'])} m)</b> in Uttarakhand.</p></div>
<div class="szm-stats"><div class="szm-stat"><b>{n(kc['m'])} m</b><span>Kangchenjunga — India's highest, world's 3rd</span></div><div class="szm-stat"><b>{n(nd['m'])} m</b><span>Nanda Devi — highest wholly inside India</span></div><div class="szm-stat"><b>38</b><span>major summits above 7,000 m (500 m+ prominence)</span></div><div class="szm-stat"><b>{TOTAL}</b><span>peaks in our dataset, 3,000 m and up</span></div></div>
<p class="lead">India holds the eastern end of the Karakoram and a long arc of the Great Himalaya, from Ladakh through Himachal Pradesh, Uttarakhand and Sikkim to Arunachal Pradesh. This guide covers {TOTAL} of its most notable peaks. For each we give the height in metres and feet, the first recorded ascent, and whether you can climb it today. Where sources disagree on a height we use the most-cited figure and say so. Every fact traces to a source listed at the foot of the page.</p>
</section>
<section class="szm-sec dark" id="ladder"><span class="k">The height ladder</span><h2>India's mountains, from 3,000 m to {n(kc['m'])} m</h2>
<p class="lead">Each band of altitude is a different kind of trip. The animation places India's landmark summits at their true heights, from Churdhar to Kangchenjunga.</p>
<div class="szm-media">{lazy_video("mountains-of-india", "height-ladder", "Animated chart of Indian summits at their true heights: Churdhar, Friendship Peak, Deo Tibba, Reo Purgyil, Kamet, Nanda Devi and Kangchenjunga")}
<div><p style="color:rgba(232,241,248,.85)">Above 3,000 m you are on hill summits and trek tops. From 5,000 m you are on snow with an ice axe and crampons. Above 6,000 m most routes need rope work and a proper expedition. Above 7,000 m you need weeks, a permit and real high-altitude experience.</p><p class="szm-note" style="color:rgba(232,241,248,.6)">Counts below are for the {TOTAL} peaks in our dataset, not every summit in India.</p></div></div>
<ul class="szm-ladder">{rows}</ul></section>
<section class="szm-sec szm-cv" id="top10"><span class="k">Ranked by height</span><h2>The 10 highest mountains in India</h2>
<p class="lead">Ranked among major summits (at least 500 m of prominence), so subsidiary tops like Zemu Gap Peak are left out. Four of the ten stand in the Siachen or Sikkim border zones where civilian climbing is not allowed.</p>
<ul class="szm-peaks">{top_cards}</ul>
<p style="margin-top:22px"><a class="szm-btn navy" href="{LIST}">Filter all {TOTAL} peaks by height, state and status →</a></p></section>
<section class="szm-sec alt szm-cv" id="states"><span class="k">By state</span><h2>Highest peak in each Himalayan state</h2>
<p class="lead">Seven states and union territories hold India's big mountains. Tap one to filter the full list.</p>
<div class="szm-states">{tiles}</div></section>
<section class="szm-sec szm-cv" id="status"><span class="k">Can you climb it?</span><h2>Which peaks are closed, sacred or still unclimbed?</h2>
<p class="lead">Of the {TOTAL} peaks in our list, {BST.get('climbed', 0)} have recorded ascents and are generally climbable with the right permits. {BST.get('restricted', 0)} are restricted (sacred, military or border zones), {BST.get('closed', 0)} are formally closed, and {BST.get('unclimbed', 0)} have no confirmed ascent.</p>
<div class="szm-cols"><div class="szm-col"><h3>{pill("closed")} Closed</h3><ul>{closed}</ul></div>
<div class="szm-col"><h3>{pill("restricted")} Sacred or restricted</h3><ul>{sacred}</ul></div>
<div class="szm-col"><h3>{pill("unclimbed")} No recorded ascent</h3><ul>{unclimbed}</ul></div></div></section>
<section class="szm-sec alt szm-cv" id="hardest"><span class="k">For experienced alpinists</span><h2>The hardest peaks in India</h2>
<p class="lead">Height isn't everything. These Garhwal and Karakoram summits are famous for steep granite, hard ice and objective danger. Several have won alpinism's top award, the Piolet d'Or.</p>
<div class="szm-cards">{hard_cards}</div></section>
<section class="szm-sec dark szm-cv" id="records"><span class="k">Records and firsts</span><h2>A timeline of the Indian Himalaya</h2>
<p class="lead">From the first 7,000 m summit ever climbed to the peaks opened this year.</p>
<ol class="szm-tl">{tl_html}</ol>
<div class="szm-call" style="background:rgba(255,255,255,.06);border-color:rgba(207,230,245,.18);color:#e8f1f8"><p><b>Did you know?</b> In October 1965 an Indian and American team tried to place a plutonium-powered sensor on Nanda Devi to watch Chinese missile tests. A blizzard forced them to leave it at Camp IV, and the 1966 search never found it. The story became public in 1978.</p></div></section>
<section class="szm-sec szm-cv" id="permits"><span class="k">Rules, permits and fees</span><h2>How to get permission to climb in India</h2>
<div class="szm-answer"><p>Foreign teams apply to the <b>Indian Mountaineering Foundation (IMF)</b> at least <b>90 days</b> ahead. They climb with an IMF liaison officer and pay a peak fee that starts at <b>US$500</b> for peaks up to 6,500 m, plus per-member charges. Indian teams book peaks through the IMF too. Border areas need a protected-area permit, and sacred or military-zone peaks are off-limits.</p></div>
<ol class="szm-steps"><li><b>Pick an open peak</b>In 2019 the government opened 137 peaks to foreigners: 47 in Himachal, 51 in Uttarakhand, 24 in Sikkim and 15 in J&amp;K. Uttarakhand added its own list of 83 in 2026.</li>
<li><b>Apply to the IMF</b>Apply online at least 90 days before you go. Open-area permits usually come through fast; restricted areas can take two to six months.</li>
<li><b>Visa and local permits</b>A tourist visa covers open areas; restricted areas need a mountaineering (X) visa, so confirm with the Indian mission. Kinnaur beyond Jangi, parts of Spiti and much of Ladakh also need a protected-area permit.</li>
<li><b>Insurance</b>Your policy must cover ground and helicopter search and rescue plus altitude illness. Support staff must be insured too.</li>
<li><b>Leave no trace</b>Carry all non-biodegradable waste down, retrieve ropes and gear, and include photo proof in your expedition report.</li></ol>
<div class="szm-scroll"><table class="szm-tbl"><thead><tr><th>Peak height</th><th>IMF base fee (foreign team of 2)</th><th>Also payable</th></tr></thead><tbody>
<tr><td>Up to 6,500 m</td><td class="n">US$500</td><td rowspan="3">Per-member charge for bigger teams, plus US$500 hire of the liaison officer's equipment and the LO's travel from Delhi</td></tr>
<tr><td>6,501–7,000 m</td><td class="n">US$700</td></tr><tr><td>Above 7,000 m</td><td class="n">US$1,000</td></tr></tbody></table></div>
<p class="szm-note">Source: IMF peak-fee page, checked {VERIFIED}. Fees change, so confirm with the IMF before you budget.</p>
<h3 style="margin-top:28px">Climbing in Himachal Pradesh</h3>
<p>Himachal requires trekking and mountaineering outfitters and their guides to register with HP Tourism, and only guides with a Method of Instruction course may lead difficult routes. Participants must be insured for at least two lakh rupees of life cover plus two lakh rupees of rescue cover. In <b>Kangra district, from 8 July to 15 October 2026</b>, trekkers on ten Dhauladhar routes must register at check posts, and anyone who skips registration can be billed for their own rescue. Our {link(EXP, "guided peak climbs")} include this paperwork.</p></section>
<section class="szm-sec alt szm-cv" id="training"><span class="k">Learn first</span><h2>Mountaineering courses in India</h2>
<p class="lead">For technical peaks, start with a Basic Mountaineering Course. The usual ladder runs Basic, then Advanced (which needs an 'A' grade in Basic), then Method of Instruction and Search &amp; Rescue. On Indian expeditions at least half the members must hold the Advanced course.</p>
<div class="szm-scroll"><table class="szm-tbl"><thead><tr><th>Institute</th><th>Where</th><th>Basic course</th><th>Who can join</th></tr></thead><tbody>{inst_rows}</tbody></table></div>
<p class="szm-note">Fees and batch dates change every season — apply directly on each institute's official site.</p></section>
<section class="szm-sec szm-cv" id="plan">{quote_block("Want to climb one? We'll plan it from Himachal", f"Suzu Travels is an HP Tourism-registered travel agent based in Himachal. For guided climbs, from Friendship Peak ({hm('friendship-peak')}) to Deo Tibba ({hm('deo-tibba')}), we pair you with registered local mountaineering outfitters and certified guides. Permits, hotels, transfers and acclimatisation days all go into one plan and one quote.", watxt, (EXP, "See guided peak climbs"))}</section>
<section class="szm-sec szm-cv" id="faq"><span class="k">FAQ</span><h2>Questions people ask about India's mountains</h2>{faq(faqs)}</section>
<section class="szm-sec szm-cv" id="more"><h2>Keep exploring</h2><div class="szm-links">
<a class="szm-link" href="{LIST}"><span class="n">Highest peaks in India</span><span class="c">Full list of {TOTAL} peaks with filters</span></a>
<a class="szm-link" href="{EXP}"><span class="n">Guided peak climbs</span><span class="c">Friendship Peak, Yunam, Deo Tibba &amp; more</span></a>
<a class="szm-link" href="/adventure/"><span class="n">Adventure in Himachal</span><span class="c">Paragliding, rafting, snow and more</span></a>
<a class="szm-link" href="/adventure/snow-activities-manali/"><span class="n">Snow activities in Manali</span><span class="c">Solang, Gulaba, Sissu</span></a>
<a class="szm-link" href="/spiti-dmc/"><span class="n">Spiti Valley trips</span><span class="c">Kaza, Kibber, Chandratal</span></a>
<a class="szm-link" href="/ladakh-dmc/"><span class="n">Ladakh trips</span><span class="c">Leh, Nubra, Pangong</span></a></div>
<h3 style="margin-top:34px">Sources</h3>{sources(SRC_CORE)}
<p class="szm-note">Heights follow the most-cited survey figure; alternate heights are listed in the downloadable dataset. Photos in the video are free-licence stock and do not show a named peak unless the caption says so.</p></section>'''
    schema = ld(
        {"@type": "CollectionPage", "@id": "https://suzutravels.com" + HUB + "#page", "name": "Mountains of India: Peaks, Permits & Mountaineering Guide", "url": "https://suzutravels.com" + HUB, "dateModified": "2026-10-01", "inLanguage": "en",
         "about": [{"@type": "Mountain", "name": p["name"], "url": f"https://suzutravels.com{LIST}#peak-{p['id']}"} for p in TOP10],
         "publisher": {"@type": "TravelAgency", "name": "Suzu Travels", "url": "https://suzutravels.com/", "telephone": "+91-7087488961"}},
        {"@type": "ItemList", "name": "The 10 highest mountains in India", "itemListOrder": "https://schema.org/ItemListOrderDescending", "numberOfItems": len(TOP10),
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": {"@type": "Mountain", "name": p["name"], "description": f"{n(p['m'])} m ({n(p['ft'])} ft), {p['where']}"}} for i, p in enumerate(TOP10)]},
        faq_ld(faqs))
    return page(body + schema)


# ------------------------------------------------------------------------------------------------ LIST
def list_page():
    kc = pk("kangchenjunga")
    faqs = [
        ("What are the 10 highest mountains in India?",
         ", ".join(f"{p['name']} ({n(p['m'])} m)" for p in TOP10[:-1]) + f" and {TOP10[-1]['name']} ({n(TOP10[-1]['m'])} m) — ranked among major summits with at least 500 m of prominence."),
        ("Why isn't K2 listed as India's highest peak here?",
         "K2 (8,611 m) is shown inside Ladakh on India's official map, but it stands in Gilgit-Baltistan, which Pakistan administers, and is climbed only from Pakistan. This list covers peaks on ground India administers, so Kangchenjunga (8,586 m) comes first."),
        ("How many peaks above 6,000 m are there in India?",
         f"No official total exists; estimates run to several hundred. Wikipedia's Uttarakhand list alone names 188 peaks between 6,000 and 6,999 m. Our list covers {BB['6000'] + BB['7000'] + BB['8000']} notable summits above 6,000 m."),
        ("Which Indian peaks have never been climbed?",
         "Peaks with no confirmed ascent include Apsarasas Kangri II and III in the Siachen, Shudu Tsenpa and Chombu in Sikkim, Nyegyi Kansang and Chiumo in Arunachal Pradesh, and the sacred Manimahesh Kailash in Himachal. Filter the table by 'Unclimbed' to see them all."),
        ("Can I download this list?",
         "Yes. The full dataset is free to reuse under CC BY 4.0 with credit to Suzu Travels (suzutravels.com). Use the CSV link in the Method section."),
        ("How accurate are the heights?",
         "Heights follow the most-cited survey figure. Where sources disagree — for example Hanuman Tibba (5,860–5,982 m) or Kangto (7,042–7,090 m) — the CSV lists the alternate values."),
    ]
    rows = []
    for i, p in enumerate(P):
        q = " ".join([p["name"], *p["alt"], p["state_label"], p["range"], p["where"]]).lower()
        fa = str(p["fa"]) if p["fa"] else "—"
        note = p["notable"] or p["status_note"]
        note = (note[:170].rsplit(" ", 1)[0] + "…") if len(note) > 175 else note
        rows.append(
            f'<tr id="peak-{p["id"]}" data-band="{p["band"]}" data-state="{p["state"]}" data-status="{p["status"]}" data-m="{p["m"]}" data-fa="{p["fa"] or ""}" data-name="{e(p["name"].lower())}" data-q="{e(q)}">'
            f'<td class="rk">{i + 1}</td><td class="pk"><span class="pn">{e(p["name"])}</span>{"<small>" + e(note) + "</small>" if note else ""}</td>'
            f'<td class="ht n">{n(p["m"])} m<span class="ft">{n(p["ft"])} ft</span></td><td class="sta">{e(p["state_label"])}</td><td class="rg">{e(p["range"])}</td>'
            f'<td class="fa n">{fa}</td><td class="stt">{pill(p["status"])}</td><td class="gr">{GRADE_LABEL[p["grade"]]}</td></tr>')
    bands = [("", "All")] + [(b, BAND_LABEL[b].replace("–", "–")) for b in ["8000", "7000", "6000", "5000", "4000", "3000"]]
    states = [("", "All")] + [(s, STATE_NAME[s]) for s in STATE_ORDER]
    stats = [("", "All")] + [(k, STATUS_LABEL[k]) for k in ["climbed", "unclimbed", "closed", "restricted"]]

    def fb(k, opts):
        return f'<div class="szm-filt" role="group" aria-label="{k}"><b>{k}</b>' + "".join(
            f'<button type="button" data-k="{k}" data-v="{v}" aria-pressed="{"true" if v == "" else "false"}">{t}</button>' for v, t in opts) + "</div>"
    band_rows = "".join(
        f"<tr><td><b>{BAND_LABEL[b]}</b></td><td class='n'>{BB[b]}</td><td>{e(max((p for p in P if p['band'] == b), key=lambda p: p['m'])['name'])} ({n(max(p['m'] for p in P if p['band'] == b))} m)</td><td><a href='#band-{b}'>Show</a></td></tr>"
        for b in ["8000", "7000", "6000", "5000", "4000", "3000"])
    state_rows = "".join(
        f"<tr><td><b>{e(STATE_NAME[s])}</b></td><td class='n'>{BS[s]}</td><td>{e(STATE_HI[s]['name'])} ({n(STATE_HI[s]['m'])} m)</td><td><a href='#state-{s}'>Show</a></td></tr>" for s in STATE_ORDER)
    top_ol = "".join(f"<li><b>{e(p['name'])}</b> — {n(p['m'])} m ({n(p['ft'])} ft), {e(p['state_label'])}</li>" for p in TOP10)
    csv_url = data_url("india-peaks.csv")
    watxt = "Hi Suzu Travels, I saw your list of Indian peaks and want to plan a climb. Peak: ___ , dates: ___ , people: ___"
    body = f'''
<section class="szm-split"><div class="szm-split-in"><div><span class="k" style="color:var(--gold2)">Dataset · {TOTAL} peaks · verified {VERIFIED}</span>
<p class="szm-tag" style="font-size:clamp(28px,3.8vw,48px)">Every major peak in India, ranked by height.</p>
<p class="szm-sub">Filter by height band, state or status. Each peak has its height in metres and feet, first recorded ascent and grade — and whether you can actually climb it today.</p>
<div class="szm-btns"><a class="szm-btn gold" href="#list">Jump to the table</a><a class="szm-btn ghost" href="{csv_url}">Download CSV</a></div>{trust()}</div>
<div>{lazy_video("mountains-of-india", "height-ladder", "Animated chart of Indian summits at their true heights, from Churdhar to Kangchenjunga")}</div></div></section>
{nav([("top10", "Top 10"), ("list", "Full list"), ("bands", "By height"), ("states", "By state"), ("method", "Method &amp; CSV"), ("faq", "FAQ")], wa(watxt))}
<section class="szm-sec" id="top10"><span class="k">Quick answer</span><h2>The 10 highest mountains in India</h2>
<div class="szm-answer"><ol style="margin:0;padding-left:22px">{top_ol}</ol></div>
<div class="szm-call"><p><b>What about K2?</b> India's official map shows K2 (8,611 m) inside Ladakh, but it stands in Pakistan-administered Gilgit-Baltistan and is climbed from Pakistan. This list covers peaks on ground India administers, so Kangchenjunga ({n(kc['m'])} m) comes first. The highest peak wholly inside India is Nanda Devi ({hm('nanda-devi')}).</p></div></section>
<section class="szm-sec alt" id="list"><span class="k">Full list</span><h2>All {TOTAL} peaks, highest first</h2>
<p class="lead">Status means: <b>Climbed</b> — at least one recorded ascent. <b>Unclimbed</b> — no confirmed ascent. <b>Closed</b> — shut to climbers by the authorities. <b>Restricted</b> — sacred, military or border-zone peaks where permits are not normally issued.</p>
<div class="szm-tools"><input id="szm-q" type="search" placeholder="Search a peak, state or range…" aria-label="Search peaks"></div>
{fb("band", bands)}{fb("state", states)}{fb("status", stats)}
<p class="szm-count" id="szm-count" aria-live="polite">Showing {TOTAL} of {TOTAL} peaks</p>
<div class="szm-scroll"><table class="szm-tbl szm-data"><thead><tr><th>#</th><th data-sort="name"><button type="button">Peak</button></th><th data-sort="m" aria-sort="descending"><button type="button">Height</button></th><th>State</th><th>Range</th><th data-sort="fa"><button type="button">First ascent</button></th><th>Status</th><th>Grade</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table></div></section>
<section class="szm-sec szm-cv" id="bands"><span class="k">By height</span><h2>How many peaks in each altitude band?</h2>
<div class="szm-scroll"><table class="szm-tbl"><thead><tr><th>Band</th><th>Peaks in list</th><th>Highest</th><th></th></tr></thead><tbody>{band_rows}</tbody></table></div>
<p class="szm-note">Wikipedia counts 38 major Indian summits (500 m+ prominence) above 7,000 m; we also list subsidiary and border summits, so our 7,000 m band is larger.</p></section>
<section class="szm-sec alt szm-cv" id="states"><span class="k">By state</span><h2>Peaks by state and union territory</h2>
<div class="szm-scroll"><table class="szm-tbl"><thead><tr><th>State / UT</th><th>Peaks in list</th><th>Highest</th><th></th></tr></thead><tbody>{state_rows}</tbody></table></div>
<p class="szm-note">Border summits are counted under the Indian state they are reached from; Nun (on the J&amp;K–Ladakh boundary) is counted under Jammu &amp; Kashmir.</p></section>
<section class="szm-sec szm-cv" id="method"><span class="k">Method</span><h2>How we built this list</h2>
<p>We started from the Wikipedia lists of Indian peaks by state, then checked first ascents against the Himalayan Journal, the American Alpine Journal, Explorersweb and news reports for 2019–2026 events. Climbing status reflects IMF, state government and news sources as of {VERIFIED}. Seasons, bases and grades are general guidance, not guarantees. First ascents are left blank where no reliable record was found; we never guess.</p>
<p><a class="szm-btn navy" href="{csv_url}">Download the dataset (CSV)</a></p>
<p class="szm-note">Free to reuse under CC BY 4.0 — please credit "Suzu Travels, suzutravels.com". Spotted an error? Tell us on WhatsApp and we will fix it.</p>
<h3 style="margin-top:22px">Main sources</h3>{sources(SRC_CORE[5:10] + [("American Alpine Journal", "https://publications.americanalpineclub.org/"), ("The Himalayan Club — Himalayan Journal", "https://www.himalayanclub.org/")])}</section>
<section class="szm-sec szm-cv">{quote_block("Found a peak you want to climb?", f"We plan guided climbs of Himachal peaks with registered local outfitters and certified guides — permits, stays, transfers and acclimatisation in one quote.", watxt, (EXP, "See guided peak climbs"))}</section>
<section class="szm-sec szm-cv" id="faq"><span class="k">FAQ</span><h2>About this list</h2>{faq(faqs)}
<div class="szm-links" style="margin-top:30px"><a class="szm-link" href="{HUB}"><span class="n">Mountains of India guide</span><span class="c">Records, permits, training</span></a><a class="szm-link" href="{EXP}"><span class="n">Guided peak climbs</span><span class="c">From Friendship Peak to Deo Tibba</span></a><a class="szm-link" href="/adventure/"><span class="n">Adventure in Himachal</span><span class="c">All activities</span></a></div></section>'''
    schema = ld(
        {"@type": "Dataset", "name": "Highest peaks in India (Suzu Travels mountain dataset)", "description": f"{TOTAL} notable peaks in India from 3,000 m to 8,586 m with height (m/ft), state, range, first ascent, climbing status and grade.",
         "url": "https://suzutravels.com" + LIST, "license": "https://creativecommons.org/licenses/by/4.0/", "isAccessibleForFree": True, "dateModified": "2026-10-01",
         "creator": {"@type": "Organization", "name": "Suzu Travels", "url": "https://suzutravels.com/"}, "spatialCoverage": {"@type": "Place", "name": "India"},
         "keywords": ["mountains of India", "highest peaks in India", "Himalaya", "mountaineering"],
         "distribution": [{"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": csv_url}]},
        {"@type": "ItemList", "name": "Highest mountains in India", "itemListOrder": "https://schema.org/ItemListOrderDescending", "numberOfItems": 20,
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"https://suzutravels.com{LIST}#peak-{p['id']}", "name": f"{p['name']} ({n(p['m'])} m)"} for i, p in enumerate(P[:20])]},
        faq_ld(faqs))
    return page(body + schema)


# ------------------------------------------------------------------------------------------------ EXPEDITIONS (commercial, under /adventure/)
CLIMBS = [  # id, typical days, start, level, what it takes, season  (research/rules-records.md §7)
    ("friendship-peak", "About 8 days from Manali", "Manali → Solang → Bakarthach → Lady Leg", "First summit", "Snow slopes and a short steep section; basic ice-axe and rope skills are taught on the way.", "May–June, Sept–Oct"),
    ("shitidhar", "About 7 days from Manali", "Manali → Lohali → Lady Leg", "First summit", "An entry-level snow climb in the Solang basin. Summit height is quoted at 5,250–5,294 m.", "Apr–May, Sept–Oct"),
    ("ladakhi-peak", "8–12 days from Manali", "Dhundi → Bakarthach → Beas Kund", "First summit", "Some loose rock and cornices on the upper ridge; basic climbing skills needed.", "Summer and autumn"),
    ("mount-yunam", "About 8 days", "Manali → Bharatpur (Baralacha La)", "First 6,000er", "Non-technical, but the summit day is long and steep, often around 12 hours. A popular first 6,000 m peak.", "July–Sept"),
    ("hanuman-tibba", "About 13 days", "Solang → Beas Kund → Tentu Pass", "Technical", "Glacier travel and fixed ropes. Height is quoted between 5,860 and 5,982 m.", "June–Oct"),
    ("deo-tibba", "13–15 days", "Manali → Jagatsukh → Chika → Duhangan Col", "Technical", "Crampons, fixed rope and a big snow dome on summit day.", "May–June, Sept–Oct"),
    ("manirang", "2–3 weeks", "Mane (Spiti)", "Big mountain", "A big but largely non-technical peak on the Spiti–Kinnaur divide; foreigners need a protected-area permit.", "July–Sept"),
    ("menthosa", "About 3 weeks from Delhi", "Udaipur (Lahaul) → Miyar valley", "Advanced", "Strenuous, with avalanche and rockfall exposure — for climbers with previous expeditions.", "June–Sept"),
    ("mulkila", "About 3 weeks from Delhi", "Lahaul, Milang valley", "Advanced", "Lahaul's highest peak, with a long glacier approach; for experienced teams.", "Aug–Oct"),
    ("indrasan", "2–3 weeks", "Manali (Deo Tibba approach)", "Expert", "Called the hardest peak in the Pir Panjal. Experienced climbers only.", "June, Sept–Oct"),
]


def expeditions():
    faqs = [
        ("Do I need climbing experience for Friendship Peak?",
         f"Not formal training — good fitness and some high-altitude trekking are enough for Friendship Peak ({hm('friendship-peak')}). Guides teach ice-axe, crampon and rope basics on the way. Technical peaks like Deo Tibba or Hanuman Tibba need previous summits or a Basic Mountaineering Course."),
        ("Which is the easiest 6,000 m peak in Himachal?",
         f"Yunam ({hm('mount-yunam')}) near Baralacha La is the usual first 6,000er. It is non-technical, but the summit day is long and the altitude is serious, so it suits fit trekkers who have been above 5,000 m."),
        ("What is the best season for peak climbing in Himachal?",
         "Around Manali (Friendship Peak, Deo Tibba, Hanuman Tibba): May–June and September–October. In rain-shadow Lahaul and Spiti (Yunam, Manirang, Mulkila): July to September. July and August bring monsoon landslides on the Kullu side."),
        ("How much does a guided climb cost?",
         "It depends on the peak, the number of days, group size and nationality, so we quote each climb. The quote covers guides and support staff, camps, meals, permits, transfers and your hotel. Foreign nationals also pay IMF fees (from US$500 per team) and liaison officer charges; we show these separately."),
        ("Do foreigners need a liaison officer?",
         "Yes, on IMF-permitted peaks every foreign expedition climbs with an IMF-appointed liaison officer. Apply at least 90 days ahead. Kinnaur and Spiti border areas also need a protected-area permit."),
        ("Is Stok Kangri open? What should I climb instead?",
         f"Stok Kangri in Ladakh has been closed since 2020. The nearest like-for-like climbs are Yunam ({hm('mount-yunam')}) and Friendship Peak ({hm('friendship-peak')}) in Himachal."),
        ("What insurance do I need?",
         "Cover for the altitude you will reach, including helicopter search and rescue and altitude illness. Himachal rules also require outfitters to insure every participant for life and rescue."),
        ("Can you book a mountaineering course for me?",
         "Courses at ABVIMAS Manali, NIM Uttarkashi and HMI Darjeeling are booked directly with the institute. We can arrange your travel, stay and a warm-up trek around the course dates."),
    ]
    cards = []
    for pid, days, start, level, what, season in CLIMBS:
        p = pk(pid)
        cards.append(
            f'<li class="szm-peak"><div class="top"><span class="rk">{level}</span><div class="h num">{n(p["m"])} m<small>{n(p["ft"])} ft</small></div>{ridge(pid, p["m"])}</div>'
            f'<div class="body"><h3>{e(p["name"])}</h3><div class="meta"><b>Duration:</b> {days}</div><div class="meta"><b>Route:</b> {e(start)}</div>'
            f'<div class="meta"><b>Season:</b> {season}</div><p class="meta">{what}</p>'
            f'<div class="go"><a style="color:#1a7f37!important" href="{wa("Hi Suzu Travels, I want a quote for a guided climb of " + p["name"] + ". Dates: ___ , people: ___ , nationality: ___")}" target="_blank" rel="noopener">Get Quote →</a> · <a href="{LIST}#peak-{pid}">Peak facts</a></div></div></li>')
    watxt = "Hi Suzu Travels, I want to plan a guided peak climb in Himachal. Peak: ___ , dates: ___ , people: ___ , nationality: ___"
    body = f'''
<section class="szm-hero">{hero_video("himalayan-peak-expeditions", "expeditions-hero", "Guided climbers roped up on snow, a tent at high camp and a summit ridge")}
<div class="szm-hero-in"><span class="k">Peak climbing · Himachal Pradesh</span>
<p class="szm-tag">Your first 5,000er. Your first 6,000er. Planned properly.</p>
<p class="szm-sub">Tell us the peak and your dates. We pair you with a registered Himachal mountaineering outfitter and certified guides, sort the permits, and add hotel, transfers and acclimatisation days — one plan, one quote.</p>
<ul class="szm-chips"><li><b>{hm('friendship-peak')}</b> Friendship Peak</li><li><b>{hm('mount-yunam')}</b> Yunam</li><li><b>{hm('deo-tibba')}</b> Deo Tibba</li><li><b>Season</b> May–Oct</li><li><b>Price</b> Get Quote</li></ul>
<div class="szm-btns"><a class="szm-btn gold" href="{wa(watxt)}" target="_blank" rel="noopener">Get a quote on WhatsApp</a><a class="szm-btn ghost" href="{QUOTE}">Send an enquiry</a></div>
{trust()}</div></section>
{nav([("peaks", "Peaks we arrange"), ("choose", "Which peak?"), ("how", "How it works"), ("safety", "Safety"), ("permits", "Permits"), ("faq", "FAQ")], wa(watxt))}
<section class="szm-sec" id="peaks"><span class="k">Guided climbs from Himachal</span><h2>Peaks we arrange</h2>
<div class="szm-answer"><p>Suzu Travels arranges guided climbs of Himachal Pradesh peaks, from <b>Friendship Peak ({hm('friendship-peak')})</b> near Manali to <b>Deo Tibba ({hm('deo-tibba')})</b> and <b>Yunam ({hm('mount-yunam')})</b>. Every climb runs with a registered local mountaineering outfitter and certified guides. We handle permits, hotel, transfers and acclimatisation, and you get one quote.</p></div>
<ul class="szm-peaks">{"".join(cards)}</ul>
<p class="szm-note" style="margin-top:14px">Durations are typical ones from the road-head and vary with the itinerary and weather. Prices are quoted per climb — tell us your dates and group size.</p></section>
<section class="szm-sec alt szm-cv" id="choose"><span class="k">Pick the right step</span><h2>Which peak is right for you?</h2>
<ol class="szm-steps"><li><b>First summit (5,000 m+)</b>Friendship Peak, Shitidhar or Ladakhi. Good fitness plus a high trek or two behind you.</li>
<li><b>First 6,000er</b>Yunam — long and high, but non-technical. Best for people who have already been above 5,000 m.</li>
<li><b>Technical 6,000 m</b>Deo Tibba or Hanuman Tibba. You'll use fixed ropes and cross glaciers; a Basic Mountaineering Course helps.</li>
<li><b>Advanced</b>Menthosa, Mulkila or Indrasan, for climbers with previous expeditions and rope skills.</li>
<li><b>Beyond Himachal</b>Big 7,000 m peaks such as Satopanth, Nun or Kamet are planned on request with experienced expedition teams.</li></ol>
<div class="szm-call"><p><b>Wanted Stok Kangri?</b> It has been closed since 2020. Yunam ({hm('mount-yunam')}) and Friendship Peak ({hm('friendship-peak')}) are the nearest like-for-like climbs, and both are in Himachal.</p></div></section>
<section class="szm-sec szm-cv" id="how"><span class="k">How it works</span><h2>From enquiry to summit</h2>
<ol class="szm-steps"><li><b>Tell us</b>Peak, dates, group size, nationality and your climbing experience.</li>
<li><b>We check the fit</b>Season, route conditions and whether the peak suits your experience. If it doesn't, we'll say so and suggest one that does.</li>
<li><b>We match your team</b>A registered Himachal outfitter with certified guides, cooks and support staff for your dates.</li>
<li><b>One quote</b>Guides, camps, meals, permits, hotel in Manali or Kaza, and transfers from Delhi or Chandigarh.</li>
<li><b>Acclimatise, climb, come home</b>Rest days are built in before any summit push. The guide decides the turnaround time.</li></ol></section>
<section class="szm-band" id="safety"><div class="szm-band-in"><span class="k">Safety first</span><h2>What we check before we book a climb</h2>
<p class="lead">Mountains don't negotiate, so these checks happen before anyone signs up.</p>
<ul class="szm-checks"><li><b>Registered outfitter</b>The outfitter and its guides are registered with HP Tourism, as Himachal's adventure rules require.</li>
<li><b>Qualified guides</b>Technical and difficult routes are led by guides with advanced mountaineering or Method of Instruction training.</li>
<li><b>Acclimatisation</b>Above 3,000 m, plans raise sleeping altitude by roughly 500 m a night at most, with rest days.</li>
<li><b>Rescue plan and insurance</b>Every participant is insured, and the plan covers evacuation, including by helicopter.</li>
<li><b>Weather and turnaround</b>Summit pushes follow forecast windows, with fixed turnaround times.</li>
<li><b>Leave no trace</b>All non-biodegradable waste comes down the mountain, as IMF and state rules require.</li></ul></div></section>
<section class="szm-sec szm-cv" id="permits"><span class="k">Permits and paperwork</span><h2>Permits for climbing in Himachal</h2>
<p><b>Indian climbers</b> need the peak booked with the Indian Mountaineering Foundation (IMF) and the local forest and police formalities, which the outfitter handles. <b>Foreign climbers</b> need an IMF permit, applied for at least 90 days ahead. The IMF peak fee starts at US$500 for peaks up to 6,500 m, and a liaison officer must go with the team. Kinnaur beyond Jangi and parts of Spiti also need a protected-area permit.</p>
<p>In <b>Kangra district, from 8 July to 15 October 2026</b>, trekkers on ten Dhauladhar routes must register at check posts. Full details are in our {link(HUB + "#permits", "guide to climbing permits in India")}.</p></section>
<section class="szm-sec alt szm-cv" id="add"><span class="k">Make it one trip</span><h2>Add the rest of your Himachal trip</h2>
<div class="szm-links"><a class="szm-link" href="/cabs/delhi-to-manali-taxi/"><span class="n">Delhi to Manali taxi</span><span class="c">Door to door, one-way or round trip</span></a>
<a class="szm-link" href="/cabs/manali-taxi-service/"><span class="n">Manali taxi service</span><span class="c">Road-head drops and pickups</span></a>
<a class="szm-link" href="/manali/"><span class="n">Manali</span><span class="c">Stay, sightseeing and rest days</span></a>
<a class="szm-link" href="/spiti-dmc/"><span class="n">Spiti Valley</span><span class="c">Kaza, Kibber and the high villages</span></a></div></section>
<section class="szm-sec szm-cv">{quote_block("Tell us your peak and your dates", "We reply with the right peak for your experience, a day-by-day plan and one quote — guides, permits, stay and transfers included.", watxt)}</section>
<section class="szm-sec szm-cv" id="faq"><span class="k">FAQ</span><h2>Peak climbing in Himachal: your questions</h2>{faq(faqs)}</section>
<section class="szm-sec szm-cv" id="more"><h2>Learn about the mountains first</h2><div class="szm-links">
<a class="szm-link" href="{HUB}"><span class="n">Mountains of India</span><span class="c">Records, permits and training</span></a>
<a class="szm-link" href="{LIST}"><span class="n">Highest peaks in India</span><span class="c">Full list of {TOTAL} peaks</span></a>
<a class="szm-link" href="/adventure/"><span class="n">Adventure in Himachal</span><span class="c">All activities</span></a>
<a class="szm-link" href="/adventure/snow-activities-manali/"><span class="n">Snow activities in Manali</span><span class="c">Solang, Gulaba, Sissu</span></a></div>
<h3 style="margin-top:30px">Sources</h3>{sources([SRC_CORE[0], SRC_CORE[1], SRC_CORE[10], SRC_CORE[11], SRC_CORE[12], ("ABVIMAS Manali — Basic Mountaineering Course", "https://www.abvimas.org/course/basic-mountaineering-course/")])}</section>'''
    trips = [{"@type": "TouristTrip", "name": f"Guided climb of {pk(pid)['name']} ({n(pk(pid)['m'])} m)", "touristType": "Mountaineers",
              "description": f"{what} Typical duration: {days}. Season: {season}.", "provider": {"@type": "TravelAgency", "name": "Suzu Travels", "url": "https://suzutravels.com/"}}
             for pid, days, start, level, what, season in CLIMBS]
    schema = ld({"@type": "ItemList", "name": "Guided Himalayan peak climbs from Himachal", "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": t} for i, t in enumerate(trips)]}, faq_ld(faqs))
    return page(body + schema)


PAGES = {"mountains-of-india": hub, "highest-peaks-in-india": list_page, "himalayan-peak-expeditions": expeditions}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    (KIT / "out").mkdir(exist_ok=True)
    for slug, fn in PAGES.items():
        if which in (slug, "all"):
            (KIT / "out" / f"{slug}.html").write_text(fn(), encoding="utf-8")
            print("out/%s.html" % slug)
