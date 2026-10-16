#!/usr/bin/env python3
"""Sync the LIVE homepage's #tp-engine blocks with the current planner data (places, templates, from-cities)
and apply small engine fixes, editing only our own blocks. Usage: python3 sync_engine.py <live_index.html> <out.html>"""
import json, os, re, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hero_engine as HE

def sync(src, dst):
    h = open(src, encoding='utf-8').read()
    assert 'id="tp-engine"' in h, 'tp-engine missing'
    data = json.dumps(HE.DATA, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    n = 0
    def sub(pat, rep, count=1, flags=re.S):
        nonlocal h, n
        m = len(re.findall(pat, h, flags)); assert m == count, (pat[:70], m)
        h = re.sub(pat, lambda _: rep, h, flags=flags); n += 1
    # 1. data
    sub(r'(<script id="tpe-data" type="application/json">).*?(</script>)', r'<script id="tpe-data" type="application/json">' + data.replace('\\', '\\\\') + '</script>')
    h = h.replace(data.replace('\\', '\\\\'), data, 1) if data.replace('\\', '\\\\') in h else h
    # 2. JS: regions, keys, order, emoji, popular chips
    sub(r"var REG=\{himachal:'Himachal',pilgrim:'Mata darshan',kashmir:'Kashmir',ladakh:'Ladakh',uttarakhand:'Uttarakhand',hub:'City',punjab:'Punjab'\};",
        "var REG={himachal:'Himachal',pilgrim:'Mata darshan',kashmir:'Kashmir',ladakh:'Ladakh',uttarakhand:'Uttarakhand',hub:'City',punjab:'Punjab',rajasthan:'Rajasthan',up:'Agra & Mathura'};")
    sub(r"uttarakhand:'uttarakhand rishikesh mussoorie nainital corbett'\};",
        "uttarakhand:'uttarakhand rishikesh mussoorie nainital corbett kumaon auli chopta kainchi',rajasthan:'rajasthan jaipur jodhpur jaisalmer udaipur agra taj mahal golden triangle mathura vrindavan desert heritage राजस्थान आगरा'};")
    sub(r"order=\['City','Himachal','Mata darshan','Kashmir','Ladakh','Uttarakhand','Punjab'\]",
        "order=['City','Himachal','Mata darshan','Kashmir','Ladakh','Uttarakhand','Rajasthan','Agra & Mathura','Punjab']")
    sub(r"var CAT=\{himachal:'🏔',mata:'🛕',pilgrim:'🙏',honeymoon:'💑',kashmir:'🌷',ladakh:'🏍',uttarakhand:'🌊'\};",
        "var CAT={himachal:'🏔',mata:'🛕',pilgrim:'🙏',honeymoon:'💑',kashmir:'🌷',ladakh:'🏍',uttarakhand:'🌊',rajasthan:'🏰'};")
    sub(r"var POP=\['shimla-manali','nau-devi','char-dham','kashmir-classic','spiti-circuit','vaishno-devi','dharamshala-dalhousie','ladakh-fly'\];",
        "var POP=['shimla-manali','nau-devi','char-dham','kashmir-classic','golden-triangle','spiti-circuit','kumaon-kainchi','vaishno-devi','rajasthan-royal','dharamshala-dalhousie','ladakh-fly'];")
    # 3. dropdown above fixed widgets: lift #tp-engine while the list is open
    sub(r"box\.innerHTML=h;box\.hidden=false;inp\.setAttribute\('aria-expanded','true'\)\}",
        "box.innerHTML=h;box.hidden=false;E.classList.add('dd-open');inp.setAttribute('aria-expanded','true')}")
    sub(r"function pick\(it\)\{chosen=it;box\.hidden=true;", "function pick(it){chosen=it;box.hidden=true;E.classList.remove('dd-open');")
    sub(r"else if\(e\.key==='Escape'\)\{box\.hidden=true\}", "else if(e.key==='Escape'){box.hidden=true;E.classList.remove('dd-open')}")
    sub(r"if\(!box\.contains\(e\.target\)&&e\.target!==inp\)\{box\.hidden=true;", "if(!box.contains(e.target)&&e.target!==inp){box.hidden=true;E.classList.remove('dd-open');")
    sub(r"box\.innerHTML='<div class=\"hd\">No match — try another place</div>';box\.hidden=false;return\}",
        "box.innerHTML='<div class=\"hd\">No match — try another place</div>';box.hidden=false;E.classList.add('dd-open');return}")
    sub(r"#tp-engine\{position:relative;z-index:2;", "#nz-hero.dd-open{z-index:99999}#tp-engine.dd-open{z-index:99999}\n#tp-engine{position:relative;z-index:2;")
    # toggle the class on the hero too (#nz-hero is isolation:isolate, so #tp-engine alone cannot rise above fixed widgets)
    h = h.replace("E.classList.add('dd-open')", "E.classList.add('dd-open');HERO&&HERO.classList.add('dd-open')").replace("E.classList.remove('dd-open')", "E.classList.remove('dd-open');HERO&&HERO.classList.remove('dd-open')")
    # the hero clips its overflow: cap the list height to the space left inside the hero (scrolls inside)
    h = h.replace("box.innerHTML=h;box.hidden=false;E.classList.add('dd-open');HERO&&HERO.classList.add('dd-open');inp.setAttribute('aria-expanded','true')}",
                  "box.innerHTML=h;box.hidden=false;E.classList.add('dd-open');HERO&&HERO.classList.add('dd-open');fitDD();inp.setAttribute('aria-expanded','true')}")
    assert 'fitDD();' in h
    sub(r"var D=document,W=window,E=D\.getElementById\('tp-engine'\);if\(!E\)return;", "var D=document,W=window,E=D.getElementById('tp-engine');if(!E)return;var HERO=D.getElementById('nz-hero');function fitDD(){var b=D.getElementById('tpe-dd');if(!b||!HERO)return;var room=HERO.getBoundingClientRect().bottom-b.getBoundingClientRect().top-14;b.style.maxHeight=Math.max(150,Math.min(330,room))+'px'}")
    open(dst, 'w', encoding='utf-8').write(h)
    b = h.encode('utf-8'); print(dst, len(b), hashlib.sha256(b).hexdigest()[:16], 'edits', n)

if __name__ == '__main__':
    sync(sys.argv[1], sys.argv[2])
