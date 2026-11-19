#!/usr/bin/env python3
"""TRUST_BACKLOG row 35 — faq-foreigners-hub-refresh: the hub (11411) row-10 block brought up to the product-page version (row 34).
Same 9 questions, same .szk prefix, same id/placement. Changes vs widget.html (kept as the old live text = the 'find' string):
  - visa: checked 18 Nov 2026 + dated Visitor Visa note (PIB 2335182, 11 Nov 2026)
  - e-Arrival: official site re-checked 18 Nov 2026
  - government advice: US line unchanged (issued 16 Jun 2025); FCDO line complete — J&K except air to/from + within Jammu city,
    10 km border except Wagah-Attari, all but essential travel to Manipur (gov.uk content API: updated 7 Oct 2026, text re-checked
    19 Nov 2026) + link to the solo-female safety guide
  - scams -> choose-an-agency guide; money -> UPI + SIM guides; vaccinations -> insurance guide (all in live.json)
Output: widget-11411.html. No JS, no schema, nothing stored."""
import os, re, json, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build as B
import build_product as P

Q = dict(B.QA)
K = [q for q, _ in B.QA]
GOV = Q[P.K_GOV]
old_fcdo = ('<p>The UK FCDO advises against all travel to Jammu and Kashmir, except air travel to and within Jammu city, and within '
            '10 km (6 mi) of the India–Pakistan border (page updated 7 Oct 2026).</p>')
assert old_fcdo in GOV
new_fcdo = ('<p>The UK FCDO advises against all travel to Jammu and Kashmir except air travel to and from, and travel within, the city '
            'of Jammu; against all travel within 10 km (6 mi) of the India–Pakistan border except the Wagah–Attari crossing; and against '
            'all but essential travel to Manipur (page updated 7 Oct 2026, checked 19 Nov 2026).</p>')
GOV = GOV.replace(old_fcdo, new_fcdo).replace('We plan around it with you.</p>',
      'We plan around it with you. More: ' + B.a('/india-tours/is-india-safe-for-solo-female-travellers/', 'is India safe for solo female travellers?') + '</p>')
NEW = {
  P.K_VISA: P.visa_ans(),
  P.K_ARR: Q[P.K_ARR].replace('checked 18 Oct 2026', 'official site re-checked 18 Nov 2026'),
  P.K_GOV: GOV,
  P.K_SCAM: P.with_more(P.K_SCAM, P.SCAM_MORE),
  P.K_PAY: P.with_more(P.K_PAY, P.PAY_MORE),
  P.K_VAX: P.with_more(P.K_VAX, P.VAX_MORE),
}
SRC_OLD = B.SRC
SRC_NEW = ('Sources: indianvisaonline.gov.in (e-Visa page and e-Arrival notice, checked 18 Nov 2026); Embassy of India e-Arrival card notice; '
           'PIB press release 2335182 (11 Nov 2026); '
           'US Department of State India travel advisory (issued 16 Jun 2025); UK FCDO India travel advice (updated 7 Oct 2026, checked '
           '19 Nov 2026); IRCTC Foreign Tourist Quota (High Commission of India); India Meteorological Department (PR 804). '
           'US advisory checked 23 Oct 2026 — rules change, confirm before travel.')
old = B.html()
out = old
for q, ans in B.QA:
    if q in NEW:
        frag = '<summary>%s</summary><div class="szk-a">%s</div>' % (q, ans)
        assert out.count(frag) == 1, q
        out = out.replace(frag, '<summary>%s</summary><div class="szk-a">%s</div>' % (q, NEW[q]))
assert out.count(SRC_OLD) == 1
out = out.replace(SRC_OLD, SRC_NEW)
# guards
prices = json.load(open(os.path.join(HERE, '../../../data/prices.json')))['allowed']
assert '\n' not in out and '<script' not in out and out.count('<details>') == 9
assert B.BOOKING in out and B.REG in out and B.VISA in out and '+91 70874 88961' in out
assert 'Wagah' in out and 'Manipur' in out and 'Visitor Visa' in out
assert '&' not in out.replace('&amp;', '')
low = re.sub('<[^>]+>', ' ', out).lower()
for bad in ('verified', 'vetted', 'background-check', 'guarantee', 'india is safe', 'cheapest', 'best price', 'government approved',
            'registered dmc', '24/7', 'visa on arrival', '₹', 'tipping', 'malaria', 'online now'):
    assert bad not in low, bad
for p in re.findall(r'US\$\s?([\d,]+)', out):
    assert int(p.replace(',', '')) in prices
live = json.dumps(json.load(open(os.path.join(HERE, '../../../live.json'))))
for href in re.findall(r'href="(/india-tours/[^"/]+/)"', out):
    assert href.split('/')[2] in live, href
open(os.path.join(HERE, 'widget-11411.html'), 'w').write(out)
# minimal replace ops for wp_replace_in_page (hub content already holds widget.html)
nxt = lambda q: '</div></details><details><summary>' + q
OPS = [
 ('India e-Visa guide</a> (checked 18 Oct 2026).</p>', 'India e-Visa guide</a> (checked 18 Nov 2026).</p>' + P.VISITOR),
 ('(Embassy of India notice; checked 18 Oct 2026)', '(Embassy of India notice; official site re-checked 18 Nov 2026)'),
 (old_fcdo, new_fcdo),
 ('We plan around it with you.</p>', 'We plan around it with you. More: ' + B.a('/india-tours/is-india-safe-for-solo-female-travellers/', 'is India safe for solo female travellers?') + '</p>'),
 ('or PayPal.</p>' + nxt(K[5]), 'or PayPal.' + P.SCAM_MORE + nxt(K[5])),
 ('or PayPal.</p>' + nxt(K[7]), 'or PayPal.' + P.PAY_MORE + nxt(K[7])),
 ('We do not give medical advice.</p>' + nxt(K[8]), 'We do not give medical advice.' + P.VAX_MORE + nxt(K[8])),
 (SRC_OLD, SRC_NEW),
]
chk = old
for f, r in OPS:
    assert chk.count(f) == 1, f
    chk = chk.replace(f, r)
assert chk == out, 'ops do not reproduce widget-11411.html'
json.dump(OPS, open(os.path.join(HERE, 'ops-11411.json'), 'w'), ensure_ascii=False, indent=1)
print('ok', len(old), '->', len(out))
