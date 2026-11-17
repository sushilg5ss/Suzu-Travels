#!/usr/bin/env python3
"""check-us on the product pages (TRUST_BACKLOG row 32): same four checks/answers as the hub strip (build.py, row 31),
placed on /golden-triangle-tour/ (11412) and /char-dham-yatra-for-nri/ (11413) right after <!--/szt:before-you-fly-->.
Differences from the hub: prefix .szk (.szq is already used on 11412/11413 by itinerary-pdf — 16 Nov 2026 curl; .szk 0 hits),
check 3 links only the page's OWN itinerary PDF, check 4 links #booking-protected on both pages (11413 got its own panel 17 Nov 2026, row 33; was the hub's
panel before). No JS, no prices, no reviews, nothing stored."""
import os, re
import build as B

PAGES = {
    11412: {'pdf': (B.PDF_GT, 'Sample: Golden Triangle 6 days (PDF)'), 'book': '#booking-protected'},
    11413: {'pdf': (B.PDF_CD, 'Sample: Char Dham Yatra 11 days (PDF)'), 'book': '#booking-protected'},
}

def make(pid):
    cfg = PAGES[pid]
    rows = [list(r) for r in B.ROWS]
    rows[2][2] = [cfg['pdf']]
    rows[3][2] = [(cfg['book'], 'How your booking is protected')]
    old_rows = B.ROWS
    B.ROWS = [tuple(r) for r in rows]
    html = B.build()
    B.ROWS = old_rows
    html = html.replace('szq', 'szk')
    return html

if __name__ == '__main__':
    for pid in PAGES:
        body = make(pid)
        low = body.lower()
        for bad in ['verified', '24/7', '₹', 'cheapest', 'guarantee', 'government approved', 'registered dmc', 'online now', 'seats left', 'us$', '<script', '//"', 'szq']:
            assert bad not in low, bad
        assert '&' not in body.replace('&amp;', ''), 'raw ampersand'
        assert body.count('<!--szt:check-us-->') == 1 and B.REG in body and B.BOOK in body
        assert body.count('.pdf"') == 1
        open(os.path.join(B.HERE, 'widget-%d.html' % pid), 'w').write(body)
        print(pid, len(body))
