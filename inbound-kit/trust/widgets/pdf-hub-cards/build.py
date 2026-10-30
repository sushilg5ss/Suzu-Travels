"""pdf-hub-cards (TRUST_BACKLOG row 16): 'Itinerary PDF' link on the hub 11411 Golden Triangle + Char Dham package cards.
Points to the two pinned PDFs made by trust/widgets/itinerary-pdf/. No JS, no third party, nothing stored.
python3 build.py  -> widget-gt.html, widget-cd.html (one line each)."""
import json, pathlib, re
H = pathlib.Path(__file__).parent
CDN = 'https://cdn.jsdelivr.net/gh/sushilg5ss/suzu-travels@'
CARDS = {
 'gt': dict(url=CDN+'ccf7eb01e4b8eb964380cc492eabace05375e4e1/inbound-kit/trust/widgets/itinerary-pdf/golden-triangle-6-day-itinerary-suzu-travels.pdf',
            label='6-day itinerary (PDF)', meta='Day by day · 2 pages · 219 KB · no sign-up', aria='Download the 6-day Classic Golden Triangle itinerary as a PDF'),
 'cd': dict(url=CDN+'bc61aa787f9c445478f091cd6498207ef49a886b/inbound-kit/trust/widgets/itinerary-pdf/char-dham-yatra-11-day-itinerary-suzu-travels.pdf',
            label='11-day yatra itinerary (PDF)', meta='Day by day · 3 pages · 105 KB · no sign-up', aria='Download the 11-day Char Dham Yatra itinerary as a PDF'),
}
ICON = ('<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
        'stroke-linejoin="round" aria-hidden="true" style="flex:none"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/>'
        '<path d="M14 3v5h5"/><path d="M12 11v6"/><path d="M9.5 14.5L12 17l2.5-2.5"/></svg>')
for k, c in CARDS.items():
    html = (f'<!--szt:pdf-hub-{k}--><div class="szy" style="margin:-6px 0 16px">'
            f'<a class="szy-a" href="{c["url"]}" download target="_blank" rel="noopener" aria-label="{c["aria"]}" '
            'style="display:flex;gap:10px;align-items:center;padding:10px 12px;border:1px dashed #B8860B;border-radius:12px;'
            'background:#F4EEDD;color:#0E1B14!important;text-decoration:none!important;line-height:1.3;min-height:44px">'
            f'<span style="color:#B8860B;display:flex">{ICON}</span><span style="min-width:0"><b style="display:block;font-size:14px;color:#0E1B14">'
            f'{c["label"]}</b><span style="display:block;font-size:12px;color:#5C574A">{c["meta"]}</span></span></a></div><!--/szt:pdf-hub-{k}-->')
    assert '&' not in html and '//' not in html.replace('https://', '') and '\n' not in html
    assert not re.search(r'US\$|24/7|verified|₹', html)
    (H / f'widget-{k}.html').write_text(html)
    print(k, len(html))
