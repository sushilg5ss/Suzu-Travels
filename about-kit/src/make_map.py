# Builds india-map.json (projected, simplified SVG paths) from DataMeet India boundaries.
# Outline: Country/india-composite.geojson (CC0, official boundary of India per Survey of India)
# States:  States/Admin2.shp (DataMeet India community, CC BY 4.0)
import json, shapefile, math, sys
from shapely.geometry import shape
from shapely.ops import unary_union
import shapely
K=36.0; C=math.cos(math.radians(23)); LON0=68.0; LAT0=37.3
def P(lon,lat): return ((lon-LON0)*C*K, (LAT0-lat)*K)
def proj(g): return shapely.transform(g, lambda a: __import__('numpy').column_stack(((a[:,0]-LON0)*C*K,(LAT0-a[:,1])*K)))
def path(g, tol, minarea):
    g=g.simplify(tol, preserve_topology=True)
    polys=g.geoms if hasattr(g,'geoms') else [g]
    out=[]
    for p in polys:
        if p.area<minarea: continue
        for ring in [p.exterior]+[i for i in p.interiors if Polygon_area(i)>minarea*4]:
            cs=[(round(x),round(y)) for x,y in list(ring.coords)[:-1]]
            ded=[cs[0]]
            for c in cs[1:]:
                if c!=ded[-1]: ded.append(c)
            if len(ded)<3: continue
            x0,y0=ded[0]; s=f'M{x0} {y0}'
            px,py=x0,y0; rel=[]
            for x,y in ded[1:]:
                rel.append(f'{x-px} {y-py}'); px,py=x,y
            out.append(s+'l'+' '.join(rel).replace(' -','-')+'z')
    return ''.join(out)
def Polygon_area(ring):
    from shapely.geometry import Polygon
    return Polygon(ring).area
src=sys.argv[1]
comp=json.load(open(src+'/Country/india-composite.geojson'))
cg=proj(unary_union([shape(f['geometry']) for f in comp['features']]))
r=shapefile.Reader(src+'/States/Admin2')
data={'w':980,'h':1106,'outline':path(cg,0.9,2.0),'states':{}}
for sr in r.shapeRecords():
    n=sr.record[0]; g=proj(shape(sr.shape.__geo_interface__).buffer(0))
    small = n in ('Lakshadweep','Andaman & Nicobar','Puducherry','Dadra and Nagar Haveli and Daman and Diu','Goa','Chandigarh','Delhi')
    rp=g.representative_point()
    data['states'][n]={'d':path(g,0.5 if n=='Lakshadweep' else 0.9,0.02 if n=='Lakshadweep' else (0.6 if small else 3.0)),'lx':round(rp.x),'ly':round(rp.y)}
cities={'Ghumarwin':(76.71,31.44),'Delhi':(77.21,28.61),'Chandigarh':(76.78,30.73),'Mumbai':(72.88,19.08),'Jaipur':(75.79,26.91),'Bengaluru':(77.59,12.97),'Kolkata':(88.36,22.57),'Hyderabad':(78.49,17.39),'Pune':(73.86,18.52),'Lucknow':(80.95,26.85),'Chennai':(80.27,13.08),'Ahmedabad':(72.57,23.02),'Amritsar':(74.87,31.63)}
data['cities']={k:[round(v) for v in P(*ll)] for k,ll in cities.items()}
json.dump(data,open('india-map.json','w'))
print(len(json.dumps(data)))
