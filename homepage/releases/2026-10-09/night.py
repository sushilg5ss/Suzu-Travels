#!/usr/bin/env python3
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
assert 'id="nz-recent"' not in s, 'already applied'
anchor = '<div class="nz-regions" role="group" aria-label="Region">'
assert s.count(anchor) == 1
strip = ('<div class="nz-recent" id="nz-recent" hidden>'
         '<div class="nz-rc-top"><span class="nz-rc-h" id="nz-rc-h">Recently viewed '
         '<span lang="hi">· हाल में देखे</span></span>'
         '<button type="button" class="nz-rc-clear" aria-label="Clear recently viewed trips">Clear</button></div>'
         '<ul class="nz-rc-list" aria-labelledby="nz-rc-h"></ul></div>\n')
s = s.replace(anchor, strip + anchor, 1)
css = r"""
/* 2026-10-09 night: recently viewed strip + deep-link landing offset */
.nz-tk,#nz-recent,#tour-packages{scroll-margin-top:80px}
.nz-recent{margin:0 0 18px;padding:12px 14px 14px;background:var(--nz-card);border:1px solid var(--nz-line);border-radius:18px;box-shadow:var(--nz-shadow);min-width:0}
.nz-rc-top{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:10px}
.nz-rc-h{font-family:var(--nz-display);font-weight:700;font-size:.95rem;color:var(--nz-ink)}
.nz-rc-h [lang=hi]{font-family:var(--nz-deva);font-weight:400;color:var(--nz-muted)}
.nz-rc-clear{min-height:44px;min-width:44px;padding:0 14px;border:0;background:transparent;color:var(--nz-forest);font:600 .85rem var(--nz-body);text-decoration:underline;text-underline-offset:3px;cursor:pointer;border-radius:12px}
.nz-rc-clear:hover{background:var(--nz-mint)}
.nz-rc-list{list-style:none;margin:0;padding:2px 2px 6px;display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;scrollbar-width:thin}
.nz-rc-list li{flex:0 0 auto;scroll-snap-align:start}
.nz-rc{display:flex;align-items:center;gap:10px;width:248px;min-height:64px;padding:8px 12px 8px 8px;border:1px solid var(--nz-line);border-radius:14px;background:var(--nz-snow);text-decoration:none;color:var(--nz-text);transition:transform .2s ease,border-color .2s ease}
.nz-rc:hover{transform:translateY(-2px);border-color:var(--c,var(--nz-emerald))}
.nz-rc img{width:52px;height:52px;border-radius:10px;object-fit:cover;flex:0 0 52px;background:var(--nz-mint)}
.nz-rc b{display:block;font:700 .84rem/1.25 var(--nz-display);color:var(--nz-ink);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.nz-rc small{display:block;margin-top:3px;font-size:.76rem;color:var(--nz-muted)}
.nz-rc small em{font-style:normal;font-weight:700;color:var(--nz-forest)}
@media (prefers-reduced-motion:reduce){.nz-rc{transition:none}.nz-rc:hover{transform:none}}
"""
m = s.find('<style id="suzu-nature-2026-10">'); e = s.find('</style>', m); assert m > 0 and e > m
s = s[:e] + css + s[e:]
js = r"""<script id="nz-recent-js">
(function(){
  var KEY='suzu-recent',MAX=6,BY=null,box,list;
  function get(){try{var a=JSON.parse(localStorage.getItem(KEY)||'[]');return Array.isArray(a)?a.filter(function(x){return typeof x==='string'}).slice(0,MAX):[]}catch(e){return []}}
  function put(a){try{localStorage.setItem(KEY,JSON.stringify(a.slice(0,MAX)))}catch(e){}}
  function data(){if(BY)return BY;BY={};try{var el=document.getElementById('nz-data');(JSON.parse(el.textContent).trips||[]).forEach(function(t){BY[t.slug]=t})}catch(e){}return BY}
  function esc(x){return String(x==null?'':x).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  function inr(n){return '₹'+Math.round(n).toLocaleString('en-IN')}
  function paint(){
    if(!box)return;var a=get();if(!a.length){box.hidden=true;list.innerHTML='';return}
    var B=data(),h='';
    a.forEach(function(sl){var t=B[sl];if(!t)return;
      h+='<li><a class="nz-rc" href="#trip-'+esc(t.slug)+'" style="--c:'+esc(t.color||'var(--nz-emerald)')+'">'+
         '<img src="'+esc(t.img)+'" alt="" width="52" height="52" loading="lazy" decoding="async">'+
         '<span><b>'+esc(t.title)+'</b><small>'+t.days+'D/'+t.nights+'N · '+esc(t.regionName)+' · '+
         (t.price?'from <em>'+inr(t.price)+'</em>':'Price on request')+'</small></span></a></li>'});
    list.innerHTML=h;box.hidden=!h;
  }
  function seen(slug){if(!data()[slug])return;var a=get().filter(function(x){return x!==slug});a.unshift(slug);put(a);paint()}
  function init(){
    box=document.getElementById('nz-recent');if(!box)return;list=box.querySelector('.nz-rc-list');
    box.querySelector('.nz-rc-clear').addEventListener('click',function(){put([]);paint();var g=document.getElementById('nz-pk-h');if(g&&g.focus){g.setAttribute('tabindex','-1');g.focus()}});
    var sh=document.getElementById('nz-sheet');
    if(sh&&window.MutationObserver){new MutationObserver(function(){
      if(sh.hidden||!sh.classList.contains('on'))return;
      var m=/^#trip[-=]([a-z0-9-]+)$/.exec(location.hash||'');if(m)seen(m[1]);
    }).observe(sh,{attributes:true,attributeFilter:['class','hidden']})}
    if(get().length)paint();
  }
  function idle(f){if('requestIdleCallback' in window)requestIdleCallback(f,{timeout:3000});else setTimeout(f,1200)}
  if(document.readyState==='complete')idle(init);else window.addEventListener('load',function(){idle(init)});
})();
</script>
"""
a = s.find('<script id="suzu-nature-2026-10-js">'); b = s.find('</script>', a) + len('</script>'); assert a > 0
s = s[:b] + '\n' + js + s[b:]
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s.encode()))
