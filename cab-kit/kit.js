(function(){
var P='917087488961';
function r99(x){return Math.ceil(x/100)*100-1;}
function inr(n){return '₹'+Math.round(n).toLocaleString('en-IN');}
function wa(t){return 'https://wa.me/'+P+'?text='+encodeURIComponent(t);}
function $(i){return document.getElementById(i);}
var c=$('szc-calc');
if(c){
 var cfg=JSON.parse(c.getAttribute('data-cfg'));
 var mode='one';
 var V={};cfg.v.forEach(function(v){V[v.id]=v;});
 var segs=c.querySelectorAll('.szc-seg button');
 function calc(){
  var d=cfg.d[+$('szc-cd').value]||cfg.d[0];var v=V[$('szc-cv').value];
  var days=Math.max(1,Math.min(20,parseInt($('szc-cn').value,10)||1));
  var amt,brk,label;
  if(mode==='one'){amt=Math.max(v.m,r99(d.km*v.ow*d.f));brk='One-way drop · '+d.km+' km · fuel, driver and driver allowance included';label='one-way';}
  else{var km=Math.max(2*d.km,250*days);var nights=Math.max(0,days-1);amt=r99(km*v.h)+nights*v.nt;brk='Round trip · about '+km+' km × ₹'+v.h+'/km'+(nights?' + '+nights+' night'+(nights>1?'s':'')+' driver allowance':'');label='round trip, '+days+' day'+(days>1?'s':'');}
  $('szc-ca').textContent=inr(amt);$('szc-cb').textContent=brk;
  $('szc-cw').href=wa('Hi Suzu Travels, I want to book '+d.l+' ('+label+') in '+v.n+'. Estimate on your site: '+inr(amt)+'. Date: ___ , people: ___ (page: '+cfg.s+')');
 }
 segs.forEach(function(b){b.addEventListener('click',function(){segs.forEach(function(x){x.classList.remove('on');});b.classList.add('on');mode=b.getAttribute('data-m');$('szc-cn').disabled=(mode==='one');calc();});});
 ['szc-cd','szc-cv','szc-cn'].forEach(function(i){$(i).addEventListener('change',calc);$(i).addEventListener('input',calc);});
 calc();
}
var f=$('szc-qf');
if(f){
 try{var t=new Date();t.setDate(t.getDate()+1);$('szc-qt').min=new Date().toISOString().slice(0,10);if(!$('szc-qt').value){$('szc-qt').value=t.toISOString().slice(0,10);}}catch(e){}
 var send=function(){
  var m='Hi Suzu Travels, I need a cab.\nPickup: '+($('szc-qp').value||'___')+'\nDrop: '+($('szc-qd').value||'___')+'\nDate: '+($('szc-qt').value||'___')+'\nPeople: '+($('szc-qx').value||'___')+'\nCar: '+$('szc-qv').value+'\nTrip: '+$('szc-qr').value+'\n(page: '+f.getAttribute('data-slug')+')';
  window.open(wa(m),'_blank');
 };
 f.addEventListener('submit',function(e){e.preventDefault();send();});
}
var fd=$('szc-find');
if(fd){
 var map=JSON.parse(fd.getAttribute('data-map'));
 fd.addEventListener('submit',function(e){e.preventDefault();
  var a=$('szc-fa').value,b=$('szc-fb').value;var k=a+'>'+b,k2=b+'>'+a;
  if(map[k]){location.href=map[k];return;}
  if(map[k2]){location.href=map[k2];return;}
  window.open(wa('Hi Suzu Travels, I need a taxi from '+a+' to '+b+'. Date: ___ , people: ___ (page: cabs finder)'),'_blank');
 });
}
})();
