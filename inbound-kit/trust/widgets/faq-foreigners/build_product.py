#!/usr/bin/env python3
"""TRUST_BACKLOG row 34 — faq-foreigners-product-pages: compact 'First time in India?' Q&A block on /golden-triangle-tour/ (11412)
and /char-dham-yatra-for-nri/ (11413), placed right after each page's hand-built FAQ (before <section class="lp-sec" id="more-tours">).

Reuses the hub's sourced Q&As (build.py, row 10) — only the ones that do NOT repeat a question the page's own FAQ already answers:
  11412 already asks: visa, car or train, best time, safety  -> drop 'car or train' and 'monsoon'
  11413 already asks: visa, best time, insurance, reach from abroad -> drop 'first trip' and 'car or train'
Facts re-checked 18 Nov 2026 (curl): indianvisaonline.gov.in tvoa (4 days, six months, GRANTED, no intermediary, no express fee,
e-Arrival 72 h, yellow-fever card); gov.uk content API FCDO India (updated 7 Oct 2026: J&K except air to/from and within Jammu city;
10 km India-Pakistan border except Wagah-Attari; all but essential travel to Manipur; scam/tout, Uber/Ola, night/fog quotes).
US State Dept: Level 2 (issued 16 Jun 2025) + J&K Level 4 re-checked 14 Nov 2026 (manali-vs-kashmir fact pack; 403 to curl today).
Visitor Visa note: PIB PRID 2335182 (11 Nov 2026) — same sentence the Reviewer added to 5 guides on 16-17 Nov.
Class prefix .szu (0 hits on 11411/11412/11413 and the homepage, 18 Nov 2026; .szk is taken on 11412/11413 by check-us).
No JS, no schema (the page's hand-built FAQPage stays the only FAQPage), nothing stored."""
import os, re, json, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build as B  # regenerates the hub widget.html byte-identically

a = B.a
Q = {q: ans for q, ans in B.QA}
K_FIRST, K_VISA, K_ARR, K_GOV, K_SCAM, K_CAR, K_PAY, K_VAX, K_MON = [q for q, _ in B.QA]

VISITOR = ('<p>Coming change: India is renaming the Tourist Visa the Visitor Visa (PIB, 11 Nov 2026); the official site still shows '
           'the e-Tourist Visa — until it changes, apply there only.</p>')
OCI = '<p>Holders of an OCI card need no visa. Travelling on an Indian passport? No visa is needed either.</p>'
GOV = ('<p>The US State Department rates India <strong>Level 2 – Exercise increased caution</strong> “due to crime and terrorism. Some '
       'areas have increased risk.” It rates Jammu and Kashmir Level 4: Do not travel, except eastern Ladakh and Leh (advisory issued '
       '16 Jun 2025, still the current advisory when checked 20 Nov 2026).</p><p>The UK FCDO advises against all travel to Jammu and Kashmir except air '
       'travel to and from, and travel within, the city of Jammu; against all travel within 10 km (6 mi) of the India–Pakistan border '
       'except the Wagah–Attari crossing; and against all but essential travel to Manipur (page updated 7 Oct 2026, checked 18 Nov 2026).'
       '</p><p><em>What this means for you:</em> read the current advice for your passport before you book, and ask your insurer whether '
       'you are covered in any area your government advises against. More: ' + a('/india-tours/is-india-safe-for-solo-female-travellers/', 'is India safe for solo female travellers?')
       + '</p>')
SCAM_MORE = (' Before you pay any company, see ' + a('/india-tours/how-to-choose-a-travel-agency-in-india/', 'how to choose a travel agency in India') + '.</p>')
PAY_MORE = (' More: ' + a('/india-tours/upi-and-money-in-india-for-tourists/', 'UPI and money in India for tourists') + ' · ' +
            a('/india-tours/sim-card-india-tourist/', 'SIM card for tourists') + '.</p>')
VAX_MORE = (' Cover for medical care abroad: our ' + a('/india-tours/india-travel-insurance/', 'India travel insurance guide') + '.</p>')

def visa_ans():
    s = Q[K_VISA].replace('(checked 18 Oct 2026)', '(checked 18 Nov 2026)')
    return s + VISITOR

def with_more(k, more):
    s = Q[k]
    assert s.endswith('</p>')
    return s[:-4] + more

def items(pid):
    base = [(K_VISA, visa_ans() + (OCI if pid == 11413 else '')),
            (K_ARR, Q[K_ARR].replace('checked 18 Oct 2026', 'official site re-checked 18 Nov 2026')),
            (K_GOV, GOV),
            (K_SCAM, with_more(K_SCAM, SCAM_MORE)),
            (K_PAY, with_more(K_PAY, PAY_MORE)),
            (K_VAX, with_more(K_VAX, VAX_MORE))]
    if pid == 11412:
        return [(K_FIRST, Q[K_FIRST])] + base
    # Char Dham: monsoon timing matters for the yatra roads
    return base + [(K_MON, Q[K_MON])]

LEAD = {
    11412: 'Your Golden Triangle questions are answered above. These are the ones first-time visitors from the US, UK, Europe, '
           'Australia and Canada ask about India itself — dated and sourced to official sites.',
    11413: 'Your yatra questions are answered above. These are the ones overseas pilgrims and foreign-passport NRIs ask about '
           'arriving in India — dated and sourced to official sites.',
}
WA = {
    11412: B.WA.replace('travelling%20in%20India%3A%20', 'my%20Golden%20Triangle%20trip%3A%20'),
    11413: B.WA.replace('travelling%20in%20India%3A%20', 'my%20Char%20Dham%20Yatra%3A%20'),
}
SRC = ('Sources: indianvisaonline.gov.in (e-Visa page and e-Arrival notice, checked 18 Nov 2026); PIB press release 2335182 (11 Nov 2026); '
       'US Department of State India travel advisory (issued 16 Jun 2025, checked 20 Nov 2026); UK FCDO India travel advice (updated 7 Oct 2026, checked '
       '18 Nov 2026); India Meteorological Department (PR 804). Rules change — confirm before travel.')

def make(pid):
    css = B.CSS.replace('.szk', '.szu')
    its = items(pid)
    body = ''.join('<details><summary>%s</summary><div class="szu-a">%s</div></details>' % (q, ans) for q, ans in its)
    h = ('<section class="szu" id="first-time-in-india" style="scroll-margin-top:90px"><div class="szu-in">'
         '<span class="szu-eb">First time in India?</span>'
         '<h2>Questions International Travellers Ask</h2>'
         '<p class="szu-lead">' + LEAD[pid] + '</p>' + body +
         '<div class="szu-cta"><span><strong>Another question?</strong> Ask our team in Himachal — a real person answers, in English.</span>'
         '<a class="szu-wa" href="' + WA[pid] + '" target="_blank" rel="noopener">WhatsApp +91 70874 88961</a>'
         '<a class="szu-em" href="mailto:info@suzutravels.com?subject=Question%20about%20travelling%20in%20India">Email us</a></div>'
         '<p class="szu-src">' + SRC + '</p></div></section>')
    return '<!--szt:faq-foreigners--><style>' + css + '</style>' + h + '<!--/szt:faq-foreigners-->', len(its)

if __name__ == '__main__':
    prices = json.load(open(os.path.join(HERE, '../../../data/prices.json')))['allowed']
    for pid in (11412, 11413):
        out, n = make(pid)
        assert '\n' not in out and '<script' not in out and 'szk' not in out
        assert out.count('<details>') == n == 7
        assert B.BOOKING in out and B.REG in out and B.VISA in out and '+91 70874 88961' in out
        assert '&' not in out.replace('&amp;', ''), 'raw ampersand'
        low = re.sub('<[^>]+>', ' ', out).lower()
        for bad in ('verified', 'vetted', 'background-check', 'guarantee', 'india is safe', 'cheapest', 'best price',
                    'government approved', 'registered dmc', '24/7', 'visa on arrival', '₹', 'tipping', 'malaria', 'online now'):
            assert bad not in low, bad
        for p in re.findall(r'US\$\s?([\d,]+)', out):
            assert int(p.replace(',', '')) in prices
        qs = re.findall(r'<summary>(.*?)</summary>', out)
        assert len(set(qs)) == n
        open(os.path.join(HERE, 'widget-%d.html' % pid), 'w').write(out)
        print(pid, n, 'Qs', len(out), 'bytes')
