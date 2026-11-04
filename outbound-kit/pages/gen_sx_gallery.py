"""Real-photo gallery block for the older `.sx` country pages (BACKLOG #7).
Usage: python3 gen_sx_gallery.py thailand  -> pages/sx-gallery-thailand.html (one line)
Inserted before the second <section> of the page with wp_replace_in_page (expected_count 1).
"""
import json, sys, html, os
HERE = os.path.dirname(os.path.abspath(__file__))
M = json.load(open(os.path.join(HERE, '..', 'photos', 'wp_map.json')))

GAL = {
 'thailand': dict(
   title='Thailand in real photos',
   sub='Six places that come up in almost every Thailand plan we write — from the Krabi coast to the temples of Bangkok and the far north. Tap any photo to open it full size.',
   slugs=[('thailand-g1','-1024x683'),('thailand-g2','-1024x673'),('thailand-g3','-683x1024'),
          ('thailand-g4','-1024x681'),('thailand-g5','-1024x683'),('thailand-g6','-768x960')]),
}

CSS = (".sxg{margin:22px 0 0}"
 ".sxg .sxg-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}"
 ".sxg figure{margin:0;background:#fff;border:1px solid #E3E9E3;border-radius:16px;overflow:hidden;box-shadow:0 2px 8px rgba(18,38,21,.05);transition:transform .25s,box-shadow .25s;position:relative}"
 ".sxg figure:hover{transform:translateY(-3px);box-shadow:0 14px 30px rgba(18,38,21,.12)}"
 ".sxg figure:before{content:'';position:absolute;left:0;right:0;top:0;height:3px;background:#D4AF37;z-index:1}"
 ".sxg a{display:block;text-decoration:none!important}"
 ".sxg img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;margin:0;height:auto}"
 ".sxg figcaption{padding:11px 14px 13px;font-size:14px;line-height:1.4;color:#4A5D4E}"
 ".sxg figcaption b{display:block;color:#122615;font-size:15px;font-family:'Sora','Plus Jakarta Sans',sans-serif}"
 ".sx .sxg p.sxg-cr{margin:12px 0 0;font-size:12px;line-height:1.6;color:#7A867D}"
 ".sx .sxg p.sxg-cr a{color:#7A867D;display:inline}"
 "@media(max-width:900px){.sxg .sxg-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}"
 "@media(max-width:600px){.sxg .sxg-grid{gap:10px}.sxg figcaption{padding:9px 10px 11px;font-size:13px}.sxg figcaption b{font-size:14px}.sxg figcaption span{display:none}}")

def build(country):
    g = GAL[country]
    figs, cr = [], []
    for slug, size in g['slugs']:
        v = M[slug]
        full = v['url']; base, ext = full.rsplit('.', 1)
        base = base.replace('-scaled', '')
        thumb = base + size + '.' + ext
        figs.append('<figure><a href="%s" target="_blank" rel="noopener"><img src="%s" alt="%s" width="1024" height="768" loading="lazy" decoding="async"></a><figcaption><b>%s</b><span>%s</span></figcaption></figure>'
                    % (full, thumb, html.escape(v['alt'], quote=True), html.escape(v['cap']), html.escape(v['note'])))
        cr.append('%s — <a href="%s" target="_blank" rel="noopener nofollow">%s</a>, %s' % (html.escape(v['cap']), v['src'], html.escape(v['credit']), html.escape(v['license'])))
    return ('<section id="%s-in-photos" class="sx-sec sxg"><style>%s</style><span class="sx-eyebrow">Real photos</span><h2>%s</h2><p class="si-sub">%s</p><div class="sxg-grid">%s</div><p class="sxg-cr">Photos: %s.</p></section>'
            % (country, CSS, html.escape(g['title']), html.escape(g['sub']), ''.join(figs), ' · '.join(cr)))

if __name__ == '__main__':
    c = sys.argv[1]
    out = build(c)
    assert '\n' not in out
    open(os.path.join(HERE, 'sx-gallery-%s.html' % c), 'w').write(out)
    print(len(out.encode()))
