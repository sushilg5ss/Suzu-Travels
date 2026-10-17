"""Photo slideshow that drops into an existing .sx-media box (16:9, position:relative)."""
import html

def slideshow(items, label):
    """items: list of (src, alt, caption). Pure CSS crossfade + slow zoom, one line, no JS."""
    n = len(items)
    per = 5  # seconds per slide
    total = n * per
    vis = 100.0 / n
    css = (".szs{position:absolute;inset:0;overflow:hidden;background:#0b1510}"
           ".szs figure{position:absolute;inset:0;margin:0;opacity:0;animation:szsF %ds infinite}"
           ".szs figure:first-child{opacity:1}"
           ".szs img{position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover;margin:0;animation:szsK %ds infinite}"
           ".szs figcaption{position:absolute;left:14px;bottom:12px;background:rgba(8,14,10,.62);color:#fff;font:700 12.5px/1 'Plus Jakarta Sans',system-ui,sans-serif;padding:8px 12px;border-radius:999px;letter-spacing:.02em;-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}"
           ".szs figcaption:before{content:'\\25CF';color:#D4AF37;margin-right:6px;font-size:9px}"
           ".szs:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 60%%,rgba(0,0,0,.35));pointer-events:none}"
           "@keyframes szsF{0%%{opacity:0}%.2f%%{opacity:1}%.2f%%{opacity:1}%.2f%%{opacity:0}100%%{opacity:0}}"
           "@keyframes szsK{0%%{transform:scale(1.02)}%.2f%%{transform:scale(1.13)}100%%{transform:scale(1.13)}}"
           "@media(prefers-reduced-motion:reduce){.szs figure,.szs img{animation:none}}"
           ) % (total, total, vis * 0.15, vis, vis * 1.15, vis * 1.15)
    css += ''.join(".szs figure:nth-child(%d),.szs figure:nth-child(%d) img{animation-delay:%ds}" % (i + 1, i + 1, i * per) for i in range(n))
    figs = ''.join(
        '<figure><img src="%s" alt="%s" width="1280" height="720" %s decoding="async"><figcaption>%s</figcaption></figure>'
        % (src, html.escape(a, quote=True), 'fetchpriority="high"' if i == 0 else 'loading="lazy"', html.escape(c))
        for i, (src, a, c) in enumerate(items))
    return '<div class="sx-media"><style>%s</style><div class="szs" aria-label="%s">%s</div></div>' % (css, html.escape(label, quote=True), figs)
