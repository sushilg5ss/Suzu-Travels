# Builds widget.html for <!--szt:planner-matches--> on hub 11411 (inserted right after <!--/szv:skin-->).
# Guide links come only from live.json paths; tour titles + "from" prices are READ from the page's own .lp-card (no numbers typed).
import json, os, re
H = os.path.dirname(os.path.abspath(__file__))
live = json.load(open(os.path.join(H, '..', '..', '..', 'live.json')))
def g(slug):
    v = live[slug]; return [v['path'], v['label'].replace(' & ', ' and ')]
# chip value first word -> [card keyword regex source, [guides]]
M = {
 'Golden':   ['Golden Triangle|Agra', [g('taj-mahal-tour-from-delhi'), g('agra-to-jaipur'), g('golden-triangle-tour')]],
 'Himachal': ['Shimla|Manali|Dharamshala', [g('best-time-to-visit-himachal'), g('india-2-week-itinerary')]],
 'Kashmir':  ['Kashmir|Srinagar', [g('best-time-to-visit-kashmir'), g('gulmarg-ski-holiday')]],
 'Rishikesh':['Rishikesh|Haridwar', [g('rishikesh-yoga-retreat-guide'), g('kumbh-mela-tour')]],
 'Char':     ['Char Dham', [g('char-dham-yatra-for-nri')]],
 'Varanasi': ['Varanasi', [g('best-places-to-visit-in-india')]],
 'Rajasthan':['Udaipur|Jodhpur|Jaisalmer|Rajasthan', [g('rajasthan-tour'), g('tiger-safari-india')]],
 'Amritsar': ['Amritsar', [g('india-2-week-itinerary'), g('best-places-to-visit-in-india')]],
 'Ladakh':   ['Ladakh|Leh', [g('best-places-to-visit-in-india')]],
 'Kerala':   ['Kerala', [g('kerala-tour')]],
 'Goa':      ['Goa', [g('goa-holiday')]],
 'Not':      ['', [g('first-time-india-travel-guide'), g('best-time-to-visit-india'), g('best-places-to-visit-in-india')]],
}
css = ("<style>.szj{margin:0 0 12px;padding:10px 12px;border-radius:14px;background:#F4EEDD;border:1px solid #E6DCC0;font-family:'Plus Jakarta Sans',system-ui,sans-serif}"
"#szpForm .szj b.t{display:block;font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#8A6A12;margin:0 0 6px}"
".szj .szj-l{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 6px}.szj .szj-l:last-child{margin:0}"
".szj a{display:inline-block;max-width:100%;font-size:12.5px;font-weight:700;line-height:1.3;text-decoration:none;border-radius:10px;padding:6px 9px}"
".szj a.tr{background:#0E1B14;color:#F0D57A}.szj a.tr i{font-style:normal;color:#fff;font-weight:600}"
".szj a.gd{background:#fff;color:#0E1B14;border:1px solid #DCD6C6}.szj a:hover{opacity:.88}"
".szj em{display:block;font-style:normal;font-size:12px;color:#55645A;line-height:1.4}"
".lp-card.szj-hi{outline:3px solid #E2C158;outline-offset:3px;transition:outline-color .4s}</style>")
js = """<script>(function(){var f=document.getElementById('szpForm');if(!f){return;}var ch=f.querySelector('.szp-chips');if(!ch){return;}var M=%s;var box=document.createElement('div');box.className='szj';box.setAttribute('aria-live','polite');ch.parentNode.insertBefore(box,ch.nextSibling);var cards=[];function el(t,c,x){var e=document.createElement(t);if(c){e.className=c;}if(x){e.textContent=x;}return e;}function draw(){var c=f.querySelectorAll('input[name=r]'),keys=[];for(var i=0;i<c.length;i++){if(c[i].checked){keys.push(String(c[i].value).split(' ')[0]);}}box.innerHTML='';cards=document.querySelectorAll('.lp-card');if(!keys.length){keys=['Not'];}var tours=[],seen={},gds=[],gs={};for(var k=0;k<keys.length;k++){var m=M[keys[k]];if(!m){continue;}if(m[0]){var re=new RegExp(m[0]);for(var j=0;j<cards.length;j++){var h=cards[j].querySelector('h3');var p=cards[j].querySelector('h3 + p, .in > p');var txt=(h?h.textContent:'')+' '+(p?p.textContent:'');if(re.test(txt)){if(!seen[j]){seen[j]=1;tours.push(j);}}}}}for(var q=0;q<3;q++){for(var k2=0;k2<keys.length;k2++){var m2=M[keys[k2]];if(!m2){continue;}var it=m2[1][q];if(!it){continue;}if(!gs[it[0]]){gs[it[0]]=1;gds.push(it);}}}box.appendChild(el('b','t','Matching tours on this page'));var l1=el('div','szj-l');if(tours.length){for(var t=0;t<tours.length;t++){(function(n){var cd=cards[n],h=cd.querySelector('h3'),pr=cd.querySelector('.lp-price b'),a=el('a','tr',h?h.textContent.trim():'Tour');a.href='#';if(pr){var s=el('i','',' · from '+pr.textContent.trim());a.appendChild(s);}a.addEventListener('click',function(e){e.preventDefault();cd.scrollIntoView({behavior:'smooth',block:'center'});cd.classList.add('szj-hi');setTimeout(function(){cd.classList.remove('szj-hi');},2600);});l1.appendChild(a);})(tours[t]);}box.appendChild(l1);}else{box.appendChild(el('em','','No ready-made tour for this mix yet. Send it to us and we plan it from scratch, with a US$ quote.'));}if(gds.length){box.appendChild(el('b','t','Read before you go'));var l2=el('div','szj-l');for(var r=0;r<gds.length;r++){if(r>3){break;}var a2=el('a','gd',gds[r][1]);a2.href=gds[r][0];l2.appendChild(a2);}box.appendChild(l2);}}f.addEventListener('change',draw);draw();document.addEventListener('DOMContentLoaded',draw);})();</script>""" % json.dumps(M, ensure_ascii=False)
out = '<!--szt:planner-matches-->' + css + js + '<!--/szt:planner-matches-->'
assert '&' not in out and '//' not in out, 'wpautop trap'
open(os.path.join(H, 'widget.html'), 'w').write(out)
print(len(out))
