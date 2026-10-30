'''seatmap_svg.py — original top-view seat + luggage layouts for every FLEET class (Experience Enhancer, 30 Oct 2026).
python3 seatmap_svg.py  →  media/seatmaps/<id>.svg  (front of the vehicle on the right, India = right-hand drive,
so the driver sits at the bottom of the front column). Layouts are TYPICAL for the class, drawn by us (no third-party art);
the viewer caption says so. Bags = the class's "bags" figure; coaches show the under-floor luggage hold.'''
import pathlib, re
from cabs_data import FLEET

OUT = pathlib.Path(__file__).parent / "media" / "seatmaps"
EM, GR, GO, INK = "#122615", "#2e7d32", "#d4af37", "#56675b"

# seat columns from the back to the front (front passenger column excluded); "|" = aisle
LAYOUT = {
    "hatch": ["3"], "sedan": ["3"], "ertiga": ["2", "3"], "carens": ["3", "2"], "crysta": ["3", "3"],
    "hycross": ["3", "3"], "fortuner": ["2", "3"],
}

def cols_for(v):
    s = v["seats"]
    if v["id"] in ("hatch", "sedan"):
        return ["3"], 1
    if v["id"] in LAYOUT and v["type"] not in ("tempo", "van", "bus"):
        return LAYOUT[v["id"]], 1
    if v["type"] in ("tempo", "van"):          # 1 front + rows of 2|1 + a rear bench
        rows = (s - 1 - (4 if s >= 16 else 2)) // 3
        rear = s - 1 - rows * 3
        return [str(rear)] + ["2|1"] * rows, 1
    rows = (s - 5) // 4                         # coaches: 2|2 rows + a rear bench of 5, rest beside the driver
    return ["5"] + ["2|2"] * rows, s - 5 - rows * 4

def bags_of(v):
    m = re.match(r"(\d+)", str(v.get("bags", "")))
    return int(m.group(1)) if m else 0

def seat(x, y, w=22, h=20, fill=GR, op="1"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" opacity="{op}"/>'
            f'<rect x="{x}" y="{y}" width="5" height="{h}" rx="2.5" fill="{EM}" opacity=".35"/>')

def build(v):
    cols, front = cols_for(v)
    bus = v["type"] == "bus"
    nb = bags_of(v)
    lane = 26                                  # px per seat slot across
    width_slots = 5 if bus else (3 if v["type"] in ("tempo", "van") else 3)
    inner_h = width_slots * lane + (12 if "|" in "".join(cols) else 0)
    boot_w = 0 if bus else (34 if nb <= 3 else (46 if nb <= 5 else 58))
    colw = 30
    body_w = boot_w + len(cols) * colw + colw + 34      # + front column + bonnet/cab
    W, H = body_w + 40, inner_h + 64 + (20 if bus else 0)
    x0, y0 = 20, 22
    g = []
    g.append(f'<rect x="{x0}" y="{y0}" width="{body_w}" height="{inner_h + 16}" rx="{14 if not bus else 10}" fill="#fff" stroke="{EM}" stroke-width="2.5"/>')
    if not bus:   # bonnet curve
        g.append(f'<path d="M{x0 + body_w - 30} {y0 + 3}q26 {inner_h / 2 + 5} 0 {inner_h + 10}" fill="none" stroke="{EM}" stroke-opacity=".25" stroke-width="2"/>')
    cx = x0 + 8
    if boot_w:     # boot with bags
        g.append(f'<rect x="{cx}" y="{y0 + 6}" width="{boot_w - 6}" height="{inner_h + 4}" rx="7" fill="#f6f4ec" stroke="{GO}" stroke-dasharray="3 3"/>')
        per_col = 4 if inner_h > 90 else 3
        nb_draw = min(nb, 14)
        bw, bh = 12, (inner_h - 8) / per_col - 4
        for i in range(nb_draw):
            c, r = divmod(i, per_col)
            bx = cx + 4 + c * (bw + 3)
            if bx + bw > cx + boot_w - 6:
                break
            g.append(f'<rect x="{bx}" y="{y0 + 10 + r * (bh + 4):.1f}" width="{bw}" height="{bh:.1f}" rx="3" fill="{GO}"/>')
        cx += boot_w
    if bus:        # luggage hold under the floor
        g.append(f'<rect x="{x0 + 10}" y="{y0 + inner_h + 22}" width="{body_w - 20}" height="12" rx="4" fill="#f6f4ec" stroke="{GO}" stroke-dasharray="3 3"/>')
    def column(spec, x):
        parts = spec.split("|")
        slots = []
        if len(parts) == 1:
            n = int(parts[0]); gap = (inner_h - n * 22) / (n + 1) if n < width_slots else 2
            y = y0 + 8 + max(gap, 1)
            for _ in range(n):
                slots.append(y); y += 22 + max(gap, 1) if n < width_slots else 22 + 2
        else:
            a, b = int(parts[0]), int(parts[1])   # a seats at the top, aisle, b seats at the bottom
            y = y0 + 8
            for _ in range(a):
                slots.append(y); y += 24
            y = y0 + 8 + inner_h - b * 24
            for _ in range(b):
                slots.append(y); y += 24
        for y in slots:
            g.append(seat(x, round(y, 1)))
    for spec in cols:
        column(spec, cx + 4); cx += colw
    # front column: passengers at the top, driver (grey + wheel) at the bottom
    fx = cx + 4
    yb = y0 + 8 + inner_h - 22
    for i in range(front):
        g.append(seat(fx, y0 + 8 + i * 24))
    g.append(seat(fx, yb, fill="#9aa59c"))
    g.append(f'<circle cx="{fx + 30}" cy="{yb + 10}" r="7" fill="none" stroke="{EM}" stroke-width="2.5"/>')
    # legend + front arrow
    ly = H - 12
    leg = (f'<rect x="20" y="{ly - 9}" width="11" height="10" rx="2" fill="{GR}"/><text x="35" y="{ly}">Seat</text>'
           f'<rect x="72" y="{ly - 9}" width="11" height="10" rx="2" fill="#9aa59c"/><text x="87" y="{ly}">Driver</text>')
    leg += (f'<rect x="132" y="{ly - 9}" width="11" height="10" rx="2" fill="{GO}"/><text x="147" y="{ly}">{"Luggage hold" if bus else "Bags"}</text>')
    arrow = f'<text x="{W - 20}" y="15" text-anchor="end" font-weight="700" fill="{EM}">FRONT →</text>'
    total = sum(sum(int(p) for p in c.split("|")) for c in cols) + front
    assert total == v["seats"], (v["id"], total, v["seats"])
    W = max(W, 210)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
            f'font-family="Plus Jakarta Sans,Arial,sans-serif" font-size="11" fill="{INK}" role="img" aria-label="Top view seat layout: {v["seats"]} passenger seats">'
            + "".join(g) + leg + arrow + "</svg>"), W, H

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for v in FLEET:
        svg, w, h = build(v)
        (OUT / f"{v['id']}.svg").write_text(svg, encoding="utf-8")
        print(v["id"], v["seats"], w, h, len(svg))
