"""Original flat side-view vehicle illustrations for Suzu Cab Kit (no third-party imagery).
Each vehicle faces right. viewBox 0 0 320 140. Returns an inline <svg> string.
"""

def _pts(p):
    return " ".join(f"{x},{y}" for x, y in p)

# body silhouette, windows (list of polygons), wheel centres x, body colour pair, label
V = {
    "hatch": dict(body=[(44,106),(42,80),(50,72),(96,66),(126,44),(206,42),(238,64),(270,70),(282,80),(282,106)],
                  win=[[(104,66),(130,49),(162,48),(162,66)],[(168,66),(168,48),(202,47),(226,66)]],
                  wheels=[92,236], col=("#ffffff","#dfe5e1"), stripe=(60,86,214)),
    "sedan": dict(body=[(24,106),(22,84),(30,76),(86,72),(124,48),(198,46),(236,70),(284,76),(296,88),(296,106)],
                  win=[[(96,72),(128,52),(160,51),(160,72)],[(166,72),(166,51),(196,50),(222,72)]],
                  wheels=[80,244], col=("#f4f6f5","#d6ddd8"), stripe=(40,90,256)),
    "ertiga": dict(body=[(26,106),(24,70),(34,50),(56,42),(192,40),(230,64),(280,70),(294,84),(294,106)],
                   win=[[(42,64),(50,50),(94,47),(94,64)],[(100,64),(100,47),(148,46),(148,64)],[(154,64),(154,46),(188,45),(214,64)]],
                   wheels=[78,240], col=("#6b4a3a","#4d3429"), stripe=(36,84,254)),
    "carens": dict(body=[(24,106),(22,68),(30,48),(54,40),(196,38),(232,62),(282,68),(296,82),(296,106)],
                   win=[[(40,62),(46,48),(92,45),(92,62)],[(98,62),(98,45),(150,44),(150,62)],[(156,62),(156,44),(192,43),(216,62)]],
                   wheels=[78,242], col=("#ffffff","#dde3df"), stripe=(34,82,258)),
    "crysta": dict(body=[(22,106),(20,64),(28,42),(52,34),(196,32),(236,58),(284,66),(298,80),(298,106)],
                   win=[[(38,58),(44,42),(92,40),(92,58)],[(98,58),(98,40),(150,39),(150,58)],[(156,58),(156,39),(194,38),(220,58)]],
                   wheels=[76,244], col=("#e9ecea","#c8d0cb"), stripe=(30,80,262)),
    "tempo": dict(body=[(10,108),(10,34),(18,24),(248,22),(266,26),(288,56),(306,68),(310,80),(310,108)],
                  win=[[(24,54),(24,34),(70,33),(70,54)],[(76,54),(76,33),(122,32),(122,54)],[(128,54),(128,32),(174,31),(174,54)],[(180,54),(180,31),(226,30),(226,54)],[(234,56),(234,32),(262,32),(282,58)]],
                  wheels=[62,262], col=("#ffffff","#dfe5e1"), stripe=(16,76,290)),
    "urbania": dict(body=[(10,108),(10,36),(20,22),(236,20),(268,30),(296,60),(308,74),(312,86),(312,108)],
                    win=[[(24,52),(24,33),(76,32),(76,52)],[(82,52),(82,32),(134,31),(134,52)],[(140,52),(140,31),(192,30),(192,52)],[(198,52),(198,30),(236,30),(250,52)],[(258,54),(258,34),(270,36),(290,60)]],
                    wheels=[64,264], col=("#1f2a24","#101714"), stripe=(16,78,292)),
}


def svg(kind, uid=None, brand=True, width=None):
    v = V[kind]
    u = uid or kind
    c1, c2 = v["col"]
    _, y0, _ = v["stripe"]
    x0, x1 = v["wheels"][0] + 24, v["wheels"][1] - 24
    arches = "".join(f'<circle cx="{wx}" cy="106" r="24" fill="#0f1a13" opacity=".9"/>' for wx in v["wheels"])
    ymin = min(p[1] for p in v["body"])
    xs = [p[0] for p in v["body"]]
    bx0, bx1 = min(xs), max(xs)
    doors = "".join(f'<line x1="{w[0][0]-3}" y1="{w[0][1]}" x2="{w[0][0]-3}" y2="100" stroke="#122615" stroke-opacity=".18" stroke-width="1.2"/>' for w in v["win"][1:])
    trim = (f'<rect x="{bx0+2}" y="99" width="{bx1-bx0-4}" height="7" rx="3" fill="#1b2620" opacity=".85"/>'
            f'<line x1="{bx0+6}" y1="{v["win"][0][0][1]+3}" x2="{bx1-30}" y2="{v["win"][0][0][1]+3}" stroke="#fff" stroke-opacity=".55" stroke-width="1.5"/>')
    wheels = "".join(
        f'<g transform="translate({wx} 106)"><circle r="19" fill="#161b18"/><circle r="11" fill="#9aa39d"/>'
        f'<circle r="11" fill="none" stroke="#6d756f" stroke-width="2"/><path d="M0-10V10M-10 0H10M-7-7L7 7M-7 7L7-7" stroke="#6d756f" stroke-width="2"/><circle r="3.5" fill="#d4af37"/></g>'
        for wx in v["wheels"])
    wins = "".join(f'<polygon points="{_pts(w)}" fill="url(#g{u})"/>' for w in v["win"])
    label = ""
    if brand:
        label = (f'<text x="{(x0+x1)/2:.0f}" y="{y0+12}" text-anchor="middle" font-family="Plus Jakarta Sans,Arial,sans-serif" '
                 f'font-size="9" font-weight="800" letter-spacing="2" fill="#122615">SUZU TRAVELS</text>')
    w = f' width="{width}"' if width else ''
    lamp_x = max(p[0] for p in v["body"]) - 6
    return (f'<svg viewBox="0 0 320 140"{w} role="img" aria-label="{kind} illustration" xmlns="http://www.w3.org/2000/svg">'
            f'<defs><linearGradient id="b{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'
            f'<linearGradient id="g{u}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2d4a52"/><stop offset=".55" stop-color="#16262b"/><stop offset="1" stop-color="#3b5b63"/></linearGradient></defs>'
            f'<ellipse cx="160" cy="124" rx="150" ry="7" fill="#122615" opacity=".14"/>'
            f'<polygon points="{_pts(v["body"])}" fill="url(#b{u})" stroke="#122615" stroke-opacity=".25" stroke-width="1.5" stroke-linejoin="round"/>'
            f'{trim}{arches}{wins}{doors}'
            f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="15" rx="3" fill="#d4af37"/>{label}'
            f'<rect x="{lamp_x-8}" y="{y0-10}" width="12" height="6" rx="2" fill="#ffe8a3"/>'
            f'{wheels}</svg>')


if __name__ == "__main__":
    import sys
    out = ['<html><body style="background:#fff;display:grid;grid-template-columns:repeat(4,320px);gap:20px;padding:20px">']
    for k in V:
        out.append(f'<div>{svg(k)}<p style="font:14px sans-serif">{k}</p></div>')
    out.append('</body></html>')
    open(sys.argv[1] if len(sys.argv) > 1 else "vehicles.html", "w").write("".join(out))
