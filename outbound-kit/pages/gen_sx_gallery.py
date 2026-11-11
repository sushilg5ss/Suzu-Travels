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
 'bali': dict(
   title='Bali in real photos',
   sub='Six places that feature in the Bali trips we plan — sea temples on the coast, the volcano at Kintamani, the forest in Ubud, a boat day to Nusa Penida and the temple gates of east Bali. Tap any photo to open it full size.',
   slugs=[('bali-g1','-1024x684'),('bali-g2','-768x1150'),('bali-g3','-1024x768'),
          ('bali-g4','-1024x512'),('bali-g5','-768x1150'),('bali-g6','-1024x768')]),
 'maldives': dict(
   title='The Maldives in real photos',
   sub='What a Maldives trip actually looks like on the way in and once you arrive — the capital island, the seaplane jetty, a resort island from the air, water villas, a sandbank and a manta on the reef. Tap any photo to open it full size.',
   slugs=[('maldives-g1','-1024x577'),('maldives-g2','-1024x547'),('maldives-g3','-1024x638'),
          ('maldives-g4','-1024x522'),('maldives-g5','-1024x768'),('maldives-g6','-1024x683')]),
 'srilanka': dict(
   title='Sri Lanka in real photos',
   sub='Six stops from the classic first-time Sri Lanka loop — the rock fortress at Sigiriya, the Dambulla cave temple, the Temple of the Tooth in Kandy, Galle Fort, an elephant safari at Udawalawe and the beaches of the south coast. Tap any photo to open it full size.',
   slugs=[('srilanka-g1','-1024x683'),('srilanka-g2','-1024x734'),('srilanka-g3','-686x1024'),
          ('srilanka-g4','-957x1024'),('srilanka-g5','-1024x576'),('srilanka-g6','-1024x683')]),
 'vietnam': dict(
   title='Vietnam in real photos',
   sub='Six stops from north to south — the lake in Hanoi\u2019s old quarter, the rice terraces of Sapa, the imperial gate at Hue, the old covered bridge in Hoi An, the Golden Bridge above Da Nang and colonial Saigon. Tap any photo to open it full size.',
   slugs=[('vietnam-g1','-1024x683'),('vietnam-g2','-1024x683'),('vietnam-g3','-1024x768'),
          ('vietnam-g4','-1024x768'),('vietnam-g5','-1024x683'),('vietnam-g6','-1024x683')]),
 'singapore': dict(
   title='Singapore in real photos',
   sub='Six places most Singapore trips we plan include \u2014 the Merlion and Marina Bay, the Cloud Forest at Gardens by the Bay, a beach afternoon on Sentosa, Little India and Chinatown, and the indoor waterfall at Changi before the flight home. Tap any photo to open it full size.',
   slugs=[('singapore-g1','-1024x576'),('singapore-g2','-1024x1024'),('singapore-g3','-1024x781'),
          ('singapore-g4','-731x1024'),('singapore-g5','-1024x673'),('singapore-g6','-1024x683')]),
 'malaysia': dict(
   title='Malaysia in real photos',
   sub='Six stops from the classic Malaysia loop \u2014 the Petronas Towers and Batu Caves in Kuala Lumpur, the cable car up to Genting Highlands, the Sky Bridge on Langkawi and the heritage of George Town and Kek Lok Si on Penang. Tap any photo to open it full size.',
   slugs=[('malaysia-g1','-768x1616','50% 12%'),('malaysia-g2','-768x1152','50% 18%'),('malaysia-g3','-1024x768'),
          ('malaysia-g4','-768x1152'),('malaysia-g5','-1024x819'),('malaysia-g6','-1024x778')]),
 'bhutan': dict(
   title='Bhutan in real photos',
   sub='Six stops from the classic Paro\u2013Thimphu\u2013Punakha loop \u2014 the dzong and covered bridge in Paro, Tashichho Dzong and the Buddha Dordenma in Thimphu, the 108 chortens at Dochula, the suspension bridge in Punakha and the open Phobjikha valley. Tap any photo to open it full size.',
   slugs=[('bhutan-g1','-1024x768'),('bhutan-g2','-1024x683'),('bhutan-g3','-1024x683','62% 50%'),
          ('bhutan-g4','-1024x680'),('bhutan-g5','-1024x568'),('bhutan-g6','-1024x768')]),
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
    for t in g['slugs']:
        slug, size = t[0], t[1]
        pos = (' style="object-position:%s"' % t[2]) if len(t) > 2 else ''
        v = M[slug]
        full = v['url']; base, ext = full.rsplit('.', 1)
        base = base.replace('-scaled', '')
        thumb = base + size + '.' + ext
        figs.append('<figure><a href="%s" target="_blank" rel="noopener"><img src="%s" alt="%s" width="1024" height="768" loading="lazy" decoding="async"%s></a><figcaption><b>%s</b><span>%s</span></figcaption></figure>'
                    % (full, thumb, html.escape(v['alt'], quote=True), pos, html.escape(v['cap']), html.escape(v['note'])))
        cr.append('%s — <a href="%s" target="_blank" rel="noopener nofollow">%s</a>, %s' % (html.escape(v['cap']), v['src'], html.escape(v['credit']), html.escape(v['license'])))
    return ('<section id="%s-in-photos" class="sx-sec sxg"><style>%s</style><span class="sx-eyebrow">Real photos</span><h2>%s</h2><p class="si-sub">%s</p><div class="sxg-grid">%s</div><p class="sxg-cr">Photos: %s.</p></section>'
            % (country, CSS, html.escape(g['title']), html.escape(g['sub']), ''.join(figs), ' · '.join(cr)))

if __name__ == '__main__':
    c = sys.argv[1]
    out = build(c)
    assert '\n' not in out
    open(os.path.join(HERE, 'sx-gallery-%s.html' % c), 'w').write(out)
    print(len(out.encode()))
