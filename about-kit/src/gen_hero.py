# HyperFrames composition: "Born in the Himalaya" — seamless 16 s hero loop for /about-suzu-travels/
import random, math, os, json
R=random.Random(2019)
W,H,D=1920,1080,16.0
out='hf/hero'; os.makedirs(out+'/assets',exist_ok=True)

from shapely.geometry import Polygon, box
def ridge(y_base, amp, rough, n=9, seed=0, width=2400, x0=-240, peaks=7, snow=0):
    r=random.Random(seed)
    xs=[x0+i*4 for i in range(int(width/4)+1)]
    base=[y_base]*len(xs)
    pk=[]
    for k in range(peaks):
        px=x0+(k+.5)*width/peaks+r.uniform(-.3,.3)*width/peaks
        ph=amp*r.uniform(.55,1.0); pw=ph*r.uniform(1.1,1.7)
        pk.append((px,ph,pw))
    ys=[]
    for i,x in enumerate(xs):
        h=0
        for px,ph,pw in pk:
            d=abs(x-px)/pw
            if d<1: h=max(h,ph*(1-d)**1.15)
        ys.append(y_base-h)
    # jagged noise (two octaves)
    def noise(sc,a):
        pts=[r.uniform(-a,a) for _ in range(int(width/sc)+3)]
        return [pts[int((x-x0)/sc)]+(pts[int((x-x0)/sc)+1]-pts[int((x-x0)/sc)])*(((x-x0)/sc)%1) for x in xs]
    n1=noise(60,amp*.06); n2=noise(16,amp*.025)
    ys=[y+a+b for y,a,b in zip(ys,n1,n2)]
    pts=list(zip(xs,ys))
    d='M%d %d '%(x0,H+40)+' '.join('L%.0f %.0f'%p for p in pts)+' L%d %d Z'%(x0+width,H+40)
    extra=''
    if snow:
        poly=Polygon([(x0,H+40)]+pts+[(x0+width,H+40)]).buffer(0)
        # jagged snowline polygon
        zz=[(x0-10,-50),(x0+width+10,-50)]
        line=[]
        for i in range(0,int(width/22)+2):
            x=x0+width+10-i*22
            line.append((x, snow+r.uniform(-28,28)+ (18 if i%2 else -10)))
        cap=Polygon(zz+line).buffer(0)
        sn=poly.intersection(cap)
        gs=sn.geoms if hasattr(sn,'geoms') else [sn]
        extra=''.join('M'+' L'.join('%.0f %.0f'%c for c in list(g.exterior.coords)[:-1])+'Z' for g in gs if g.area>900)
    # shadow facets: left side of each peak (sun on the right)
    sh=''
    for px,ph,pw in pk:
        ax,ay=px,y_base-ph
        sh+=f'M{ax:.0f} {ay:.0f} L{ax-pw*.62:.0f} {y_base+20:.0f} L{ax-pw*.08:.0f} {y_base+20:.0f}Z'
    top=min(ys)
    return d, top, extra, sh

layers=[ # y_base, amp, peaks, color, snowline y, parallax amp, seed
 (700,430,6,'#7d84ad',470,8,11),
 (760,330,8,'#5d6896',560,14,23),
 (820,230,9,'#43517f',0,22,37),
 (880,150,10,'#2e3f68',0,34,41),
 (950,100,12,'#1d2c4e',0,50,53),
 (1010,70,14,'#111d37',0,70,67),
]
defs=[]; svg_layers=[]
for i,(yb,amp,pks,col,snow,par,seed) in enumerate(layers):
    d,top,cap,sh=ridge(yb,amp,0,seed=seed,peaks=pks,snow=snow)
    svg_layers.append((i,d,col,par,cap,sh))

# mist band tile (two identical halves for seamless scroll)
def mist(y,op,seed):
    r=random.Random(seed); e=[]
    for k in range(7):
        cx=r.uniform(0,1920); rx=r.uniform(260,520); ry=r.uniform(26,60)
        for off in (0,1920): e.append(f'<ellipse cx="{cx+off:.0f}" cy="{y+r.uniform(-30,30):.0f}" rx="{rx:.0f}" ry="{ry:.0f}"/>')
    return f'<g fill="#f3e9f0" opacity="{op}" filter="url(#blur)">'+''.join(e)+'</g>'

# road on layer 4 slope: S-curve points (screen coords), car follows
road=[(-80,1000),(200,990),(420,960),(600,975),(760,1010),(900,1000),(1040,955),(1180,930),(1320,950),(1440,985),(1580,975),(1720,940),(1860,925),(2000,935)]
road_d='M'+' L'.join(f'{x} {y}' for x,y in road)

# stars
stars=[]
for k in range(90):
    x=R.uniform(0,1920); y=R.uniform(0,420)**1.0; rr=R.choice([1.1,1.4,1.8,2.2])
    stars.append((k,x,y,rr,R.choice([2,4,8]),R.uniform(0,1)))
# snow flakes
flakes=[]
for k in range(110):
    flakes.append((k,R.uniform(0,1920),R.uniform(-20,1100),R.choice([1.6,2.2,2.8,3.4,4.2]),R.choice([8,16,16]),R.uniform(10,40),R.choice([4,8])))
# village lights on layer 3 hills
lights=[(R.uniform(980,1500),R.uniform(800,860),R.choice([2,4])) for _ in range(26)]

S=[]
S.append(f'''<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=1920, height=1080">
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1920px;height:1080px;overflow:hidden;background:#0a1830}}
#root{{position:relative;width:1920px;height:1080px;overflow:hidden}}.lay{{position:absolute;inset:0;width:1920px;height:1080px}}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{D}" data-width="1920" data-height="1080">
<svg class="lay" data-start="0" data-duration="{D}" data-track-index="0" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#071225"/><stop offset=".38" stop-color="#1c2b55"/><stop offset=".62" stop-color="#6b4f7d"/><stop offset=".8" stop-color="#d98a6f"/><stop offset="1" stop-color="#f4c27a"/></linearGradient>
<radialGradient id="sun" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(1260 610) scale(520)"><stop offset="0" stop-color="#fff4d6" stop-opacity="1"/><stop offset=".12" stop-color="#ffd89a" stop-opacity=".95"/><stop offset=".4" stop-color="#f3a86a" stop-opacity=".45"/><stop offset="1" stop-color="#f3a86a" stop-opacity="0"/></radialGradient>
<radialGradient id="vig" cx=".5" cy=".55" r=".75"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#020814" stop-opacity=".72"/></radialGradient>
<linearGradient id="lft" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#050d1c" stop-opacity=".62"/><stop offset=".48" stop-color="#050d1c" stop-opacity="0"/></linearGradient>
<filter id="blur" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="22"/></filter>
<filter id="rblur" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="14"/></filter><filter id="glow" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="5"/></filter>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="7"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .55 0"/></filter>
<linearGradient id="snowg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#cfd2ea"/><stop offset=".55" stop-color="#f6eef0"/><stop offset="1" stop-color="#ffe9cf"/></linearGradient>
</defs>
<rect width="1920" height="1080" fill="url(#sky)"/>
<g id="stars">''')
for k,x,y,rr,p,ph in stars:
    S.append(f'<circle id="s{k}" cx="{x:.0f}" cy="{y:.0f}" r="{rr}" fill="#fff8e8" opacity=".8"/>')
S.append('</g>')
S.append('<g id="rays" style="transform-origin:1260px 610px" opacity=".10" filter="url(#rblur)">'+''.join(f'<path d="M1260 610 L{1260+1500*math.cos(math.radians(a-1.6)):.0f} {610+1500*math.sin(math.radians(a-1.6)):.0f} L{1260+1500*math.cos(math.radians(a+1.6)):.0f} {610+1500*math.sin(math.radians(a+1.6)):.0f}Z" fill="#ffe2a8"/>' for a in range(-170,-9,20))+'</g>')
S.append('<circle id="sunc" cx="1260" cy="610" r="520" fill="url(#sun)"/>')
# plane + contrail
S.append('<path id="trail" d="M1880 250 C1500 120 1050 110 640 230" fill="none" stroke="#f2cf86" stroke-width="3" stroke-dasharray="10 14" stroke-linecap="round" opacity="0"/>')
S.append('<g id="plane" opacity="0"><path d="M-24 0 C-24 -2 -20 -3 -14 -3 L-4 -3 L8 -20 L13 -20 L6 -3 L18 -3 L23 -9 L26 -9 L23 0 L26 9 L23 9 L18 3 L6 3 L13 20 L8 20 L-4 3 L-14 3 C-20 3 -24 2 -24 0Z" fill="#f6d58d" transform="scale(1.5) rotate(180)"/></g>')
S.append('<g id="world" style="transform-origin:1100px 760px">')
for i,d,fill,par,cap,sh in svg_layers:
    S.append(f'<g id="L{i}"><path d="{d}" fill="{fill}"/>')
    S.append(f'<clipPath id="c{i}"><path d="{d}"/></clipPath><path d="{sh}" fill="#0a1430" opacity="{.28 if i<2 else .16}" clip-path="url(#c{i})"/>')
    if cap: S.append(f'<path d="{cap}" fill="url(#snowg)"/><path d="{sh}" fill="#6a6f9c" opacity=".35" clip-path="url(#c{i})"/>')
    if i==1: S.append(f'<g id="m1">{mist(700,.22,5)}</g>')
    if i==2:
        S.append(f'<g id="m2">{mist(800,.20,9)}</g>')
    if i==3:
        S.append('<g id="vl">'+''.join(f'<circle id="v{n}" cx="{x:.0f}" cy="{y:.0f}" r="2.6" fill="#ffcf7a" filter="url(#glow)" opacity=".9"/><circle cx="{x:.0f}" cy="{y:.0f}" r="1.6" fill="#fff1c9"/>' for n,(x,y,p) in enumerate(lights))+'</g>')
    if i==4:
        S.append(f'<path d="{road_d}" fill="none" stroke="#0c1730" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/><path d="{road_d}" fill="none" stroke="#f0d9a8" stroke-opacity=".35" stroke-width="2" stroke-dasharray="14 18"/>')
        S.append('<g id="car" opacity="0"><circle r="16" fill="#ffd27a" opacity=".55" filter="url(#glow)"/><circle r="4.5" fill="#fff6dc"/><circle cx="-12" r="3" fill="#ff6a5a" opacity=".9"/></g>')
    S.append('</g>')
# foreground deodars
def deodar(x,base,h,w):
    p=[f'M{x} {base-h}']
    tiers=7
    for t in range(tiers):
        yy=base-h+(t+1)*h/tiers; ww=w*(t+1)/tiers
        p.append(f'L{x+ww/2:.0f} {yy:.0f} L{x+ww/5:.0f} {yy-4:.0f}')
    for t in range(tiers-1,-1,-1):
        yy=base-h+(t+1)*h/tiers; ww=w*(t+1)/tiers
        p.append(f'L{x-ww/5:.0f} {yy-4:.0f} L{x-ww/2:.0f} {yy:.0f}')
    return ''.join(p)+'Z'
trees=''.join(f'<path d="{deodar(x,1100,h,w)}"/>' for x,h,w in [(40,420,170),(150,330,140),(250,260,110),(1720,300,130),(1820,400,160),(1905,340,140),(1630,220,95)])
S.append(f'<g id="fg" fill="#070f22">{trees}<rect x="-100" y="1060" width="2120" height="60"/></g>')
S.append('</g>')  # world
S.append('<g id="snow">'+''.join(f'<circle id="f{k}" cx="{x:.0f}" cy="0" r="{r}" fill="#fff" opacity="{.55 if r<3 else .85}"/>' for k,x,y0,r,T,sw,sp in flakes)+'</g>')
S.append('<rect width="1920" height="1080" fill="url(#lft)"/><rect width="1920" height="1080" fill="url(#vig)"/><rect width="1920" height="1080" filter="url(#grain)" opacity=".06"/>')
S.append('</svg></div><script>const tl=gsap.timeline({paused:true});')
J=[]
half=D/2
J.append(f'tl.fromTo("#world",{{scale:1}},{{scale:1.05,duration:{half},ease:"sine.inOut"}},0);tl.to("#world",{{scale:1,duration:{half},ease:"sine.inOut"}},{half});')
for i,d,fill,par,cap,sh in svg_layers:
    J.append(f'tl.fromTo("#L{i}",{{x:{par}}},{{x:{-par},duration:{half},ease:"sine.inOut"}},0);tl.to("#L{i}",{{x:{par},duration:{half},ease:"sine.inOut"}},{half});')
J.append('tl.fromTo("#m1",{x:0},{x:-1920,duration:16,ease:"none"},0);tl.fromTo("#m2",{x:-1920},{x:0,duration:16,ease:"none"},0);')
J.append(f'tl.fromTo("#rays",{{rotation:-4}},{{rotation:4,duration:{half},ease:"sine.inOut"}},0);tl.to("#rays",{{rotation:-4,duration:{half},ease:"sine.inOut"}},{half});')
J.append('tl.fromTo("#sunc",{opacity:.86},{opacity:1,duration:4,ease:"sine.inOut",yoyo:true,repeat:3},0);')
for k,x,y,rr,p,ph in stars:
    n=int(16/p)
    J.append(f'tl.fromTo("#s{k}",{{opacity:{.25+.5*ph:.2f}}},{{opacity:{.95-.4*ph:.2f},duration:{p/2},ease:"sine.inOut",yoyo:true,repeat:{2*n-1}}},0);')
for n,(x,y,p) in enumerate(lights):
    J.append(f'tl.fromTo("#v{n}",{{opacity:.35}},{{opacity:1,duration:{p/2},ease:"sine.inOut",yoyo:true,repeat:{int(16/p)*2-1}}},{(n%4)*0:.1f});')
for k,x,y0,r,T,sw,sp in flakes:
    v=(1120)/T; t1=(1100-y0)/v
    J.append(f'tl.fromTo("#f{k}",{{y:{y0:.0f}}},{{y:1100,duration:{t1:.3f},ease:"none"}},0);')
    t=t1; 
    while t+T<=D+1e-6:
        J.append(f'tl.fromTo("#f{k}",{{y:-20}},{{y:1100,duration:{T},ease:"none",immediateRender:false}},{t:.3f});'); t+=T
    if t<D-1e-3:
        J.append(f'tl.fromTo("#f{k}",{{y:-20}},{{y:{y0:.0f},duration:{D-t:.3f},ease:"none",immediateRender:false}},{t:.3f});')
    J.append(f'tl.fromTo("#f{k}",{{x:{-sw/2:.0f}}},{{x:{sw/2:.0f},duration:{sp/2},ease:"sine.inOut",yoyo:true,repeat:{int(16/sp)*2-1}}},0);')
# car path keyframes (constant speed approx)
segs=[]; tot=0
for a,b in zip(road,road[1:]):
    l=math.dist(a,b); segs.append((b,l)); tot+=l
t0,t1=0.6,14.6
kf=[]
for b,l in segs:
    kf.append(f'{{x:{b[0]},y:{b[1]-6},duration:{(t1-t0)*l/tot:.3f},ease:"none"}}')
J.append(f'tl.set("#car",{{x:{road[0][0]},y:{road[0][1]-6}}},0);tl.to("#car",{{opacity:1,duration:.6}},{t0});tl.to("#car",{{keyframes:[{",".join(kf)}]}},{t0});tl.to("#car",{{opacity:0,duration:.6}},{t1-.6});')
# plane along trail (bezier sampled)
P0,P1,P2,P3=(1880,250),(1500,120),(1050,110),(640,230)
def bz(t):
    return tuple((1-t)**3*a+3*(1-t)**2*t*b+3*(1-t)*t*t*c+t**3*d for a,b,c,d in zip(P0,P1,P2,P3))
pk=[]; N=24
for i in range(1,N+1):
    x,y=bz(i/N); x0,y0=bz((i-1)/N); ang=math.degrees(math.atan2(y-y0,x-x0))+180
    pk.append(f'{{x:{x:.0f},y:{y:.0f},rotation:{ang-180+0:.1f},duration:{8/N:.3f},ease:"none"}}')
J.append(f'tl.set("#plane",{{x:{P0[0]},y:{P0[1]}}},0);tl.to("#plane",{{opacity:1,duration:.5}},3);tl.to("#plane",{{keyframes:[{",".join(pk)}]}},3);tl.to("#plane",{{opacity:0,duration:.6}},10.6);')
J.append('tl.set("#trail",{strokeDashoffset:0},0);tl.fromTo("#trail",{opacity:0},{opacity:.55,duration:2},4);tl.to("#trail",{opacity:0,duration:2.5},11);')
S.append(''.join(J))
S.append('window.__timelines=window.__timelines||{};window.__timelines["main"]=tl;tl.seek(0);</script></body></html>')
open(out+'/index.html','w').write('\n'.join(S))
json.dump({"$schema":"https://hyperframes.heygen.com/schema/hyperframes.json","paths":{"blocks":"compositions","components":"compositions/components","assets":"assets"},"media":{"autoProxy":True}},open(out+'/hyperframes.json','w'))
print(os.path.getsize(out+'/index.html'))
