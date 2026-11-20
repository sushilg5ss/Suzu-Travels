#!/usr/bin/env python3
"""python3 getmedia.py <slug> <sheet-tag> "n:role-k:cap:alt" ...  -> ranking-kit/media/<slug>/suzu-<slug>-<role>-<k>.webp + manifest.json"""
import io, json, sys, time, urllib.parse, urllib.request, os
from PIL import Image
UA="SuzuTravelsPhotoPicker/1.0 (https://suzutravels.com)"
def get(u,tries=6):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=60) as r: return r.read()
        except Exception as e:
            print(' wait',e,flush=True); time.sleep(10*(i+1))
slug,tag=sys.argv[1],sys.argv[2]
items=json.load(open(f'/tmp/claude-0/dh/cs-{tag}.json'))
out=f'/home/claude/rk/ranking-kit/media/{slug}'; os.makedirs(out,exist_ok=True)
man=[]
mp=json.load(open(out+'/manifest.json')) if os.path.exists(out+'/manifest.json') else []
for spec in sys.argv[3:]:
    n,rk,cap,alt=spec.split('|')
    it=items[int(n)]; role,k=rk.split('-')
    fn=f'suzu-{slug}-{role}-{k}.webp'
    if not os.path.exists(f'{out}/{fn}'):
        p=dict(action='query',format='json',titles=it['title'],prop='imageinfo',iiprop='url|extmetadata',iiurlwidth=1920)
        j=json.loads(get('https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(p)))
        ii=list(j['query']['pages'].values())[0]['imageinfo'][0]
        raw=get(ii['thumburl']); im=Image.open(io.BytesIO(raw)).convert('RGB')
        if im.width>1920: im=im.resize((1920,round(im.height*1920/im.width)))
        im.save(f'{out}/{fn}','WEBP',quality=80)
        lu=ii['extmetadata'].get('LicenseUrl',{}).get('value','')
        time.sleep(2)
    else: lu=''
    man.append(dict(fn=fn,role=role,n=int(k),file='https://commons.wikimedia.org/wiki/'+it['title'].replace(' ','_'),by=it['artist'],lic=it['lic'],licurl=lu,cap=cap,alt=alt,slug=slug))
    print(fn,os.path.getsize(f'{out}/{fn}'))
json.dump(man,open(out+'/manifest.json','w'),ensure_ascii=False,indent=0)
