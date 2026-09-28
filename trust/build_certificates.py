#!/usr/bin/env python3
"""Build post_content for suzutravels.com/certificates/ (page 11527) in the same 'Legal' design family
as the policy pages (reuses policies/build.py CSS + header). Output: one line, safe for wpautop.
Facts come ONLY from the two certificates Sushil shared on 29 Sep 2026 (see README.md)."""
import os, sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'policies'))
from build import CSS, header_css, icon, WA_ICON, oneline  # noqa: E402

PID = 11527
UPDATED = '29 September 2026'
U = 'https://suzutravels.com'
IMG_HPT = U + '/wp-content/uploads/2026/09/suzu-travels-hp-tourism-registration-certificate.webp'
IMG_GST = U + '/wp-content/uploads/2026/09/suzu-travels-gst-registration-certificate.webp'
V_HPT = 'https://eservices.himachaltourism.gov.in/certificate-validation'
V_GST = 'https://services.gst.gov.in/services/searchtp'
PHONE, PHONE_TEL, EMAIL = '+91 70874 88961', '+917087488961', 'info@suzutravels.com'
REG, CERT, GSTIN = 'DTO-MND-11-243/2022', '060925/58761', '02BLPPK1401E1ZR'
ADDRESS = 'NH103 Roadside, Kulahru, Tehsil Ghumarwin, District Bilaspur, Himachal Pradesh 174021, India'


def wa(text):
    return 'https://wa.me/917087488961?text=' + quote(text)


WA_QUOTE = wa('Hi Suzu Travels, I want a quote for a Himachal trip. Travel date: ___ , people: ___ (page: certificates)')
WA_DOCS = wa('Hi Suzu Travels, please share your business documents (GST certificate, HP Tourism registration) '
             'for vendor onboarding. Company: ___ (page: certificates)')
EXT = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
       'stroke-linejoin="round" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>')

EXTRA_CSS = '''
.pl .pl-cert{margin:4px 0 16px;background:var(--cream);border:1px solid var(--line);border-radius:16px;padding:14px}
.pl .pl-cert.tall{max-width:560px}
.pl .pl-cert a{display:block;border-radius:10px;overflow:hidden;background:#fff;box-shadow:0 8px 26px rgba(18,38,21,.13);text-decoration:none}
.pl .pl-cert img{display:block;width:100%;height:auto;margin:0}
.pl .pl-cert figcaption{display:flex;flex-wrap:wrap;justify-content:space-between;gap:6px 12px;font-size:13.5px;line-height:1.4;color:var(--mut);margin:10px 2px 0}
.pl .pl-kv{width:100%;border-collapse:separate;border-spacing:0;margin:4px 0 16px;font-size:15px;line-height:1.5;background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden}
.pl .pl-kv th,.pl .pl-kv td{text-align:left;vertical-align:top;padding:10px 14px;border:0;border-bottom:1px solid var(--line)}
.pl .pl-kv th{width:36%;color:var(--mut);font-weight:700;background:var(--cream)}
.pl .pl-kv td{color:var(--ink);font-weight:600}
.pl .pl-kv tr:last-child th,.pl .pl-kv tr:last-child td{border-bottom:0}
.pl .pl-kv code{font-family:inherit;font-size:inherit;font-weight:800;color:var(--g);background:#FFF8E6;border:1px solid #EBD9A3;border-radius:6px;padding:1px 7px;white-space:nowrap}
.pl .pl-btns{display:flex;flex-wrap:wrap;gap:10px;margin:2px 0 6px}
.pl .pl-btn{display:inline-flex;align-items:center;gap:8px;text-decoration:none!important;font-weight:800;font-size:15px;line-height:1.2;padding:12px 18px;border-radius:12px;background:var(--g2);color:#fff!important;transition:background .2s}
.pl .pl-btn:hover{background:var(--g)}
.pl .pl-btn.ghost{background:#fff;color:var(--g)!important;border:1.5px solid var(--line)}
.pl .pl-btn.ghost:hover{border-color:var(--g2)}
.pl .pl-btn svg{width:18px;height:18px;flex:none}
@media(max-width:600px){.pl .pl-kv th,.pl .pl-kv td{display:block;width:100%}.pl .pl-kv th{border-bottom:0;padding:10px 14px 2px}
.pl .pl-kv td{padding:0 14px 10px}.pl .pl-btn{flex:1 1 auto;justify-content:center}.pl .pl-cert{padding:10px}}
'''.replace('\n', '')


def kv(rows):
    return '<table class="pl-kv"><tbody>' + ''.join(f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in rows) + '</tbody></table>'


def btn(href, label, cls=''):
    c = f'pl-btn {cls}'.strip()
    return f'<a class="{c}" href="{href}" target="_blank" rel="noopener">{label}{EXT}</a>'


GLANCE = [
    ('shield', 'Registered with HP Tourism', f'Travel Agent, Reg. No. {REG}, Government of Himachal Pradesh.'),
    ('doc', 'GST registered', f'GSTIN {GSTIN}, a regular registration since 13 January 2021.'),
    ('cal', 'Valid till December 2028', 'Renewed on 4 December 2025; next renewal due 3 December 2028.'),
    ('id', 'Check it yourself', 'Both registrations can be verified on official government portals.'),
]

SECTIONS = [
    ('hp-tourism', 'HP Tourism: Travel Agent registration', f'''
<p>Suzu Travels is registered with the <b>Department of Tourism &amp; Civil Aviation, Government of Himachal Pradesh</b>,
to carry on the business of a Travel Agent in Himachal Pradesh, under the Himachal Pradesh Tourism Development and
Registration Act, 2002.</p>
<figure class="pl-cert"><a href="{IMG_HPT}" target="_blank" rel="noopener"><img src="{IMG_HPT}" width="1800" height="1320"
loading="lazy" decoding="async" alt="Suzu Travels certificate of registration as a Travel Agent, Department of Tourism and
Civil Aviation, Government of Himachal Pradesh, Reg. No. {REG}"></a><figcaption><span>Certificate of Registration of
Travel Agent &middot; Government of Himachal Pradesh</span><span>Tap to open full size</span></figcaption></figure>
{kv([
    ('Issued by', 'Prescribed Authority, Mandi &amp; Bilaspur at Mandi &mdash; Department of Tourism &amp; Civil Aviation, Himachal Pradesh'),
    ('Registered as', 'Travel Agent in Himachal Pradesh'),
    ('Name and style', 'Suzu Travels, NH 103, Road Side, Kulahru, Tehsil Ghumarwin, District Bilaspur, Himachal Pradesh'),
    ('Proprietor', 'Sushil Kumar'),
    ('Permanent registration no.', f'<code>{REG}</code>'),
    ('Certificate no.', f'<code>{CERT}</code>, dated 4 December 2025'),
    ('Renewal due', '3 December 2028'),
])}
<div class="pl-btns">{btn(V_HPT, 'Verify on HP Tourism eServices')}</div>
<p>The certificate itself names this portal for verification. Keep the certificate number and registration number
above handy when you check.</p>'''),
    ('gst', 'GST registration', f'''
<p>Suzu Travels is registered under GST as a regular taxpayer, with Himachal Pradesh as the state of registration.</p>
<figure class="pl-cert tall"><a href="{IMG_GST}" target="_blank" rel="noopener"><img src="{IMG_GST}" width="1300" height="1876"
loading="lazy" decoding="async" alt="Suzu Travels GST registration certificate, Form GST REG-06, GSTIN {GSTIN}, valid
from 13 January 2021"></a><figcaption><span>Form GST REG-06 &middot; Government of India</span><span>Tap to open full size</span></figcaption></figure>
{kv([
    ('GSTIN', f'<code>{GSTIN}</code>'),
    ('Legal name', 'Sushil Kumar'),
    ('Trade name', 'Suzu Travels'),
    ('Constitution', 'Proprietorship'),
    ('Type of registration', 'Regular'),
    ('Valid from', '13 January 2021 (no end date)'),
    ('Principal place of business', 'Near Hamsafar Guest House, Kullaru, Abdhanighat, Bilaspur, Himachal Pradesh 174021'),
    ('Jurisdiction', 'Ghumarwin Circle (Centre)'),
])}
<div class="pl-btns">{btn(V_GST, 'Search this GSTIN on the GST portal')}</div>
<p class="pl-note"><b>About the &ldquo;Signature Not Verified&rdquo; mark:</b> downloaded GST certificates are digitally
signed by the GST Network, and most PDF viewers show this mark when the signing certificate is not installed on the
device. The quickest check is the GSTIN search on the official GST portal.</p>'''),
    ('for-you', 'What registration means for you', f'''
<p>Himachal Pradesh asks travel agents who do business in the state to register with its Tourism Department. When you
book with a registered agent, you know who you are dealing with.</p>
<ul>
<li><b>A traceable business.</b> Our proprietor, trade name and office address are on record with the Government of
Himachal Pradesh and the GST department.</li>
<li><b>A local office in Himachal.</b> We are based on NH103 at Ghumarwin, District Bilaspur, and plan trips across the state.</li>
<li><b>Transparent taxes.</b> GST and other taxes are shown in your quotation. See our
<a href="{U}/cancellation-and-refund-policy/">Cancellation &amp; Refund Policy</a> for payment terms.</li>
<li><b>Registered adventure operators.</b> Activities such as paragliding and rafting are run by operators registered for
that activity in Himachal. Ask us and we will share the operator&rsquo;s details for your booking.</li>
<li><b>A clear complaints path.</b> Our grievance officer&rsquo;s details are in the
<a href="{U}/terms-and-conditions/">Terms &amp; Conditions</a>.</li>
</ul>'''),
    ('business', 'Business details', f'''
{kv([
    ('Trade name', 'Suzu Travels'),
    ('Proprietor', 'Sushil Kumar'),
    ('Constitution', 'Proprietorship'),
    ('Office', ADDRESS),
    ('HP Tourism registration', f'<code>{REG}</code> (Travel Agent)'),
    ('GSTIN', f'<code>{GSTIN}</code>'),
    ('Phone / WhatsApp', f'<a href="tel:{PHONE_TEL}">{PHONE}</a>'),
    ('Email', f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
])}
<p><b>Travel agents and companies:</b> need our documents for vendor registration or a B2B tie-up? Message us and we
will send the full set.</p>
<div class="pl-btns">{btn(WA_DOCS, 'Request documents on WhatsApp', 'ghost')}</div>'''),
    ('misuse', 'Beware of misuse', f'''
<p>These copies are published only so that you can verify Suzu Travels, and they carry our watermark. We take bookings
only through suzutravels.com, <a href="tel:{PHONE_TEL}">{PHONE}</a> and <a href="mailto:{EMAIL}">{EMAIL}</a>, and we
accept payments only through our <a href="{U}/payment/">Payment page</a> or the official Suzu Travels accounts listed there.</p>
<p class="pl-note"><b>If anyone else shows you these certificates</b>, or asks you to pay a personal account in the name
of Suzu Travels, call us on <a href="tel:{PHONE_TEL}">{PHONE}</a> before you pay.</p>'''),
]


HEADER = header_css(PID, 'Certificates').replace('Legal \\00B7  Certificates', 'Verified \\00B7  HP Tourism & GST')


def build():
    tabs = ''.join(f'<a href="{U}/{s}/">{t}</a>' for s, t in [
        ('cancellation-and-refund-policy', 'Cancellation &amp; Refund'), ('terms-and-conditions', 'Terms &amp; Conditions'),
        ('privacy-policy', 'Privacy Policy'), ('payment', 'Payments')])
    tabs += f'<a href="{U}/certificates/" aria-current="page">Certificates</a>'
    glance = ''.join(f'<div class="pl-card">{icon(k)}<b>{t}</b><span>{d}</span></div>' for k, t, d in GLANCE)
    toc = ''.join(f'<a href="#{sid}"><i>{n:02d}</i>{t}</a>' for n, (sid, t, _) in enumerate(SECTIONS, 1))
    secs = ''.join(f'<section class="pl-sec" id="{sid}"><h2><span>{n:02d}</span>{t}</h2>{oneline(body)}</section>'
                   for n, (sid, t, body) in enumerate(SECTIONS, 1))
    help_ = ('<section class="pl-help"><div><h2>Plan your trip with a registered Himachal travel agent</h2>'
             '<p>Tell us your dates and group size. We send a custom quote with hotels, cab and sightseeing, and one '
             'person looks after your trip from start to finish.</p></div><div class="pl-ctas">'
             f'<a class="wa" href="{WA_QUOTE}" target="_blank" rel="noopener">{WA_ICON}WhatsApp</a>'
             f'<a class="call" href="tel:{PHONE_TEL}">Call {PHONE}</a>'
             f'<a class="mail" href="{U}/himachal-tour-packages-quote/">Get a quote</a></div></section>')
    intro = ('Suzu Travels is registered with the Department of Tourism &amp; Civil Aviation, Government of Himachal '
             'Pradesh, as a Travel Agent, and holds a regular GST registration. Both certificates are below, so you can see '
             'exactly who you are booking with and check them yourself on the official government portals.')
    html = (f'<div class="pl"><style>{CSS}{HEADER}{EXTRA_CSS}</style>'
            f'<section class="pl-top"><p class="pl-intro">{intro}</p>'
            f'<div class="pl-meta"><span>Last updated {UPDATED}</span><span>Suzu Travels, Himachal Pradesh</span></div>'
            f'<nav class="pl-tabs" aria-label="Policies and certificates">{tabs}</nav></section>'
            f'<div class="pl-glance">{glance}</div>'
            f'<div class="pl-grid"><nav class="pl-toc" aria-label="On this page"><b>On this page</b>{toc}</nav>'
            f'<div class="pl-body">{secs}</div></div>{help_}</div>')
    assert '\n' not in html
    for bad in ('₹', 'Rs.', 'INR'):
        assert bad not in html, bad
    return html


if __name__ == '__main__':
    h = build()
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    open(os.path.join(HERE, 'out', 'certificates.html'), 'w').write(h)
    print(len(h), 'bytes')
