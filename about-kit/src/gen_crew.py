# HyperFrames composition: "The Crew" — opening-credits film of the Suzu Travels team (27 s)
import os, random, json
from team import TEAM
R=random.Random(7)
D=27.0; out='hf/crew'
S=[]
S.append('''<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=1920, height=1080">
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
@font-face{font-family:"CG";src:url("assets/cg-700.woff2") format("woff2");font-weight:700}
@font-face{font-family:"CG";src:url("assets/cg-600.woff2") format("woff2");font-weight:600}
@font-face{font-family:"SZ";src:url("assets/pjs-800.woff2") format("woff2");font-weight:800}
@font-face{font-family:"SZ";src:url("assets/pjs-700.woff2") format("woff2");font-weight:700}
@font-face{font-family:"SZ";src:url("assets/pjs-500.woff2") format("woff2");font-weight:500}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1920px;height:1080px;overflow:hidden;background:#05101e}
#root{position:relative;width:1920px;height:1080px;overflow:hidden;font-family:"SZ",sans-serif;background:radial-gradient(120% 90% at 70% 40%,#13284a 0%,#081427 55%,#040b16 100%)}
.ab{position:absolute}
.bok{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(242,198,110,.55),rgba(242,198,110,0) 70%)}
.bar{position:absolute;left:0;width:1920px;height:84px;background:#000;z-index:50}
.leak{position:absolute;inset:-200px;background:linear-gradient(105deg,rgba(255,170,80,0) 30%,rgba(255,190,110,.55) 45%,rgba(255,236,190,.85) 50%,rgba(255,150,90,.45) 56%,rgba(255,170,80,0) 70%);mix-blend-mode:screen;z-index:40}
.kick{font:800 24px "SZ";letter-spacing:.42em;color:#e7bf6a;text-transform:uppercase}
.title{font:700 210px/0.9 "CG",serif;letter-spacing:.04em;background:linear-gradient(180deg,#fff6dc 0%,#f0cf86 48%,#c98f3a 100%);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 10px 40px rgba(240,180,90,.25))}
.sub{font:600 40px "CG",serif;color:#f4ead7;font-style:italic}
.pc{position:absolute;width:600px;height:750px;overflow:hidden;border-radius:6px;box-shadow:0 40px 90px rgba(0,0,0,.55),0 0 0 1px rgba(231,191,106,.35)}
.pc img{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(1.06) contrast(1.05)}
.pc:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,16,30,0) 55%,rgba(5,16,30,.55) 100%)}
.nm{position:absolute;width:820px}
.nm .ix{font:800 20px "SZ";letter-spacing:.3em;color:#e7bf6a;margin-bottom:22px}
.nm .ix i{display:inline-block;width:60px;height:2px;background:#e7bf6a;vertical-align:middle;margin-left:16px;font-style:normal}
.nm h2{font:700 118px/0.95 "CG",serif;color:#fff8ea;letter-spacing:.005em}
.nm .rl{font:800 25px "SZ";letter-spacing:.2em;text-transform:uppercase;color:#f0cf86;margin-top:26px}
.nm .fc{font:500 30px "SZ";color:#c9d4e6;margin-top:16px}
.nm .sq{display:inline-block;margin-top:26px;font:800 18px "SZ";letter-spacing:.24em;text-transform:uppercase;color:#0b1f33;background:#e7bf6a;padding:10px 18px;border-radius:40px}
.th{position:absolute;width:150px;height:188px;overflow:hidden;border-radius:6px;box-shadow:0 14px 34px rgba(0,0,0,.5),0 0 0 1px rgba(231,191,106,.4)}
.th img{width:100%;height:100%;object-fit:cover}
.end1{font:700 104px/1 "CG",serif;color:#fff8ea;text-align:center;width:1920px}
.end2{font:500 34px "SZ";color:#e7bf6a;text-align:center;width:1920px;letter-spacing:.06em}
.grain{position:absolute;inset:0;z-index:45;opacity:.07;pointer-events:none}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="27" data-width="1920" data-height="1080">
<div id="stage" class="ab" style="inset:0" data-start="0" data-duration="27" data-track-index="0">''')
# bokeh
for k in range(26):
    s=R.uniform(40,180); S.append(f'<div class="bok" id="b{k}" style="left:{R.uniform(-80,1900):.0f}px;top:{R.uniform(60,1000):.0f}px;width:{s:.0f}px;height:{s:.0f}px;opacity:{R.uniform(.15,.6):.2f}"></div>')
# intro
S.append('<div id="intro" class="ab" style="left:0;top:0;width:1920px;height:1080px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">'
 '<div class="kick" id="ik">Suzu Travels &nbsp;presents</div><div class="title" id="it" style="margin-top:34px">THE CREW</div>'
 '<div class="sub" id="is" style="margin-top:26px">The people behind every Suzu trip</div></div>')
# per-person scenes
N=len(TEAM)
times=[]; t=3.4
for i,m in enumerate(TEAM):
    dur=2.7 if m['grp']=='lead' else 1.32
    times.append((t,dur)); t+=dur
END=t  # mosaic start
for i,m in enumerate(TEAM):
    right = (i%2==0)
    px = 1150 if right else 170
    nx = 170 if right else 900
    sq=f'<div class="sq">Team {m["squad"]}</div>' if m.get('squad') else ''
    S.append(f'<div class="pc" id="p{i}" style="left:{px}px;top:165px;opacity:0"><img src="assets/suzu-team-{m["slug"]}.webp" alt=""></div>')
    S.append(f'<div class="nm" id="n{i}" style="left:{nx}px;top:330px;opacity:0"><div class="ix">{i+1:02d} / {N:02d}<i></i></div><h2>{m["name"]}</h2><div class="rl">{m["role"]}</div><div class="fc">{m["focus"]}</div>{sq}</div>')
# mosaic thumbs (7 + 6)
pos=[]
for i in range(N):
    row=0 if i<7 else 1; col=i if i<7 else i-7; n=7 if row==0 else 6
    x=960-(n*150+(n-1)*22)/2+col*172; y=150+row*210
    pos.append((x,y))
    m=TEAM[i]
    S.append(f'<div class="th" id="t{i}" style="left:{x:.0f}px;top:{y:.0f}px;opacity:0"><img src="assets/suzu-team-{m["slug"]}.webp" alt=""></div>')
S.append('<div class="ab" id="e1" style="left:0;top:640px;opacity:0"><div class="end1">13 people. One promise.</div></div>')
S.append('<div class="ab" id="e2" style="left:0;top:770px;opacity:0"><div class="end2">Your trip, handled end to end &nbsp;·&nbsp; Since 2019 &nbsp;·&nbsp; Ghumarwin, Himachal Pradesh</div></div>')
S.append('<img id="logo" class="ab" src="assets/logo.png" style="left:1700px;top:860px;width:150px;height:150px;opacity:0" alt="">')
S.append('<div class="leak" id="lk" style="opacity:0"></div>')
S.append('<svg class="grain" viewBox="0 0 1920 1080"><filter id="gr"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="3"/><feColorMatrix values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 .7 0"/></filter><rect width="1920" height="1080" filter="url(#gr)"/></svg>')
S.append('<div class="bar" id="bt" style="top:0"></div><div class="bar" id="bb" style="bottom:0"></div>')
S.append('</div></div><script>const tl=gsap.timeline({paused:true});')
J=[]
for k in range(26):
    J.append(f'tl.fromTo("#b{k}",{{x:0,y:0}},{{x:{R.uniform(-160,160):.0f},y:{R.uniform(-90,90):.0f},duration:27,ease:"sine.inOut"}},0);')
# letterbox in
J.append('tl.fromTo("#bt",{height:540},{height:84,duration:1.1,ease:"power3.inOut"},0.1);tl.fromTo("#bb",{height:540},{height:84,duration:1.1,ease:"power3.inOut"},0.1);')
J.append('tl.fromTo("#lk",{opacity:0,x:-900},{opacity:1,x:900,duration:1.6,ease:"power2.inOut"},0.5);tl.to("#lk",{opacity:0,duration:.4},2.1);')
J.append('tl.fromTo("#ik",{opacity:0,letterSpacing:"0.9em"},{opacity:1,letterSpacing:"0.42em",duration:1.0,ease:"power2.out"},0.6);')
J.append('tl.fromTo("#it",{opacity:0,scale:1.18,filter:"blur(14px)"},{opacity:1,scale:1,filter:"blur(0px)",duration:1.2,ease:"power3.out"},0.9);')
J.append('tl.fromTo("#is",{opacity:0,y:20},{opacity:1,y:0,duration:.7},1.6);tl.to("#intro",{opacity:0,scale:.96,duration:.5,ease:"power2.in"},2.9);')
for i,(t0,dur) in enumerate(times):
    right=(i%2==0); dx=80 if right else -80
    J.append(f'tl.fromTo("#p{i}",{{opacity:0,clipPath:"inset(0 0 100% 0)",x:{dx}}},{{opacity:1,clipPath:"inset(0 0 0% 0)",x:0,duration:.5,ease:"power3.out"}},{t0:.2f});')
    J.append(f'tl.fromTo("#p{i} img",{{scale:1.12}},{{scale:1.0,duration:{dur+.3:.2f},ease:"none"}},{t0:.2f});')
    J.append(f'tl.fromTo("#n{i}",{{opacity:0,x:{-dx}}},{{opacity:1,x:0,duration:.45,ease:"power3.out"}},{t0+.12:.2f});')
    J.append(f'tl.to("#p{i}",{{opacity:0,x:{-dx/2},duration:.28,ease:"power2.in"}},{t0+dur-.26:.2f});tl.to("#n{i}",{{opacity:0,duration:.24}},{t0+dur-.24:.2f});')
# mosaic
for i,(x,y) in enumerate(pos):
    J.append(f'tl.fromTo("#t{i}",{{opacity:0,y:60,scale:.8}},{{opacity:1,y:0,scale:1,duration:.55,ease:"back.out(1.6)"}},{END+.05*i:.2f});')
J.append(f'tl.fromTo("#e1",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.7,ease:"power3.out"}},{END+.8:.2f});tl.fromTo("#e2",{{opacity:0}},{{opacity:1,duration:.7}},{END+1.3:.2f});tl.fromTo("#logo",{{opacity:0,scale:.7}},{{opacity:1,scale:1,duration:.6,ease:"back.out(1.7)"}},{END+1.5:.2f});')
J.append(f'tl.fromTo("#lk",{{opacity:0,x:-900}},{{opacity:.8,x:900,duration:1.4,ease:"power2.inOut"}},{END+.4:.2f});tl.to("#lk",{{opacity:0,duration:.3}},{END+1.8:.2f});')
J.append(f'tl.to("#stage",{{opacity:0,duration:.6}},{D-.6});')
S.append(''.join(J))
S.append('window.__timelines=window.__timelines||{};window.__timelines["main"]=tl;tl.seek(0);</script></body></html>')
open(out+'/index.html','w').write('\n'.join(S))
json.dump({"$schema":"https://hyperframes.heygen.com/schema/hyperframes.json","paths":{"blocks":"compositions","components":"compositions/components","assets":"assets"},"media":{"autoProxy":True}},open(out+'/hyperframes.json','w'))
print('mosaic at',END)
