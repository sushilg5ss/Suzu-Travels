#!/usr/bin/env python3
"""Homepage: add the Devotional (pilgrimage) entry points — 8 Oct 2026, at Sushil's request.
Usage: python3 enh-devotional.py LIVE.html AFTER.html   (asserts every anchor; run parity.py after)
1) Top nav: 'Devotional' dropdown after Mountains (<!--szpil--> ... <!--/szpil-->) + tighter nav CSS for 12 items (#szpil-nav)
2) Destinations dropdown > Pilgrimages column: + 'All pilgrimage tours' and '12 Jyotirlinga'
3) Experience tile 'Pilgrimage' -> /pilgrimage-tours/ (copy updated)
4) Trip-finder chips: + 'Devotional tours' chip"""
import sys
s = open(sys.argv[1], encoding="utf-8").read()
assert "szpil" not in s, "already applied"
H = "https://suzutravels.com/pilgrimage-tours/"
def one(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:90])
    s = s.replace(old, new)
link = lambda href, icon, color, text: f'<a class="simple-link" href="{href}"><div class="simple-link-icon"><i class="ph-fill {icon}" style="color:{color};"></i></div>{text}</a>'
nav = ('<!--szpil--><li class="nav-dropdown-wrapper szpil"><a href="' + H + '"><span class="nav-pill-icon"><i class="ph ph-hands-praying"></i></span> Devotional'
       '<svg class="chevron" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="4 6 8 10 12 6"/></svg></a>'
       '<div class="dropdown-menu" style="min-width:0;width:max-content;"><div class="dropdown-menu-inner" style="grid-template-columns:230px 210px;">'
       '<div class="dropdown-col"><div class="dropdown-col-title">Tirth Yatra</div>'
       + link(H, "ph-hands-praying", "var(--amber-deep)", "All pilgrimage tours")
       + link(H + "12-jyotirlinga/", "ph-sun", "var(--amber)", "12 Jyotirlinga")
       + link(H + "#shakti", "ph-flower-lotus", "var(--teal-deep)", "Shakti Peeths of Himachal")
       + link(H + "#naudevi", "ph-flame", "var(--amber-deep)", "Nau Devi Yatra")
       + '</div><div class="dropdown-col"><div class="dropdown-col-title">Yatras</div>'
       + link(H + "#chardham", "ph-mountains", "var(--teal)", "Char Dham Yatra")
       + link(H + "#amarnath", "ph-snowflake", "var(--teal-deep)", "Amarnath Yatra")
       + link(H + "#vaishno", "ph-path", "var(--amber)", "Vaishno Devi")
       + link(H + "#kashi", "ph-drop", "var(--teal)", "Kashi &amp; Ayodhya")
       + '</div></div></div></li><!--/szpil-->')
one("<!--/szmnt-->", "<!--/szmnt-->" + nav)
css = ('\n<style id="szpil-nav">\n/* szpil (8 Oct 2026): 12 top-level items incl. Devotional — tighter desktop nav so the right-hand buttons stay visible */\n'
       '@media (min-width:1181px) and (max-width:1250px){nav ul.nav-links{margin-left:2px!important}nav ul.nav-links>li>a{padding:6px 3px!important;font-size:11.2px!important}}\n'
       '@media (min-width:1251px) and (max-width:1320px){nav ul.nav-links{margin-left:4px!important}nav ul.nav-links>li>a{padding:6px 3px!important;font-size:11.8px!important}}\n'
       '@media (min-width:1321px) and (max-width:1500px){nav ul.nav-links{margin-left:4px!important}nav ul.nav-links>li>a{padding:6px 3px!important;font-size:12px!important}}\n'
       '@media (min-width:1501px) and (max-width:1680px){nav ul.nav-links{margin-left:6px!important}nav ul.nav-links>li>a{padding:6px 3px!important;font-size:12.4px!important}}\n'
       '@media (min-width:1681px){nav ul.nav-links>li>a{padding-left:7px!important;padding-right:7px!important}nav ul.nav-links .szpil .nav-pill-icon{display:none!important}}\n'
       '.szpil-pill{background:#fff1de;color:#9a4a07!important;font-weight:600}.szpil .dropdown-col-title{color:#a8530a}\n</style>')
i = s.find('<style id="szmnt-nav">'); j = s.find("</style>", i) + len("</style>")
assert i > 0
s = s[:j] + css + s[j:]
# 2) Destinations > Pilgrimages column
old = ('<div class="dropdown-col-title">Pilgrimages</div>')
assert s.count(old) == 1
s = s.replace(old, old + link(H, "ph-hands-praying", "var(--amber-deep)", "All pilgrimage tours") + link(H + "12-jyotirlinga/", "ph-sun", "var(--amber)", "12 Jyotirlinga"))
# 3) experience tile
k = s.find('<span class="tag">Pilgrimage</span>'); assert k > 0
a = s.rfind('<a class="nz-xp', 0, k)
seg = s[a:k]
assert 'href="https://suzutravels.com/destination/chardham-tour-packages/"' in seg
s = s[:a] + seg.replace('href="https://suzutravels.com/destination/chardham-tour-packages/"', f'href="{H}"') + s[k:]
one("<h3>Pilgrimage</h3><p>Char Dham, Amarnath, Shakti Peeth, Jyotirlinga</p>", "<h3>Pilgrimage</h3><p>12 Jyotirlinga, Shakti Peeths, Char Dham, Amarnath</p>")
# 4) chip
chip = '<i class="ph ph-hands-praying" aria-hidden="true"></i>Char Dham &amp; pilgrimage</a>'
one(chip, chip + f'<a class="szx-chip" href="{H}"><i class="ph ph-flower-lotus" aria-hidden="true"></i>Devotional tours</a>')
open(sys.argv[2], "w", encoding="utf-8").write(s)
print("ok", len(s.encode()))
