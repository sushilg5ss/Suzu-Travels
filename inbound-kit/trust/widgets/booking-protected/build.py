#!/usr/bin/env python3
"""TRUST_BACKLOG row 5 — how-booking-is-protected. One-line, self-contained, NO JavaScript (works with JS off).
Facts only from: README §1 booking line (exact), registration line (exact), approved driver wording, and the site's own
published policies (/terms-and-conditions/ §01/§08, /cancellation-and-refund-policy/ §01/§04, last updated 28 Sep 2026).
hub 11411  -> protection panel + 'what if' answers (the hub already has its own '4 easy steps' block, so no steps here)
gt  11412  -> 4 steps + protection panel + 'what if' answers"""
import os

BOOKING = ("20% deposit locks your dates and price; full refund if cancelled within 48 hours of paying; balance before the trip; "
           "pay by card via Razorpay (international cards accepted) or PayPal.")
REG = 'HP Tourism registered travel agent · Reg. No. DTO-MND-11-243/2022'
WA = 'https://wa.me/917087488961?text=Hello%20Suzu%20Travels%2C%20I%20have%20a%20question%20about%20booking%20an%20India%20trip.'

CSS = (".szt-bk{font-family:'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',sans-serif;color:#0E1B14}"
       ".szt-bk *{box-sizing:border-box}.szt-bk p:empty,.szt-bk br{display:none}"
       ".szt-bk h2{margin:4px 0 8px}.szt-bk-lead{max-width:62ch;color:#46524A;font-size:16px;line-height:1.6;margin:0 0 20px}"
       ".szt-bk-steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:0 0 18px;padding:0;list-style:none;counter-reset:s}"
       ".szt-bk-steps li{position:relative;background:#fff;border:1px solid #E8DFC8;border-radius:18px;padding:18px 16px 16px;counter-increment:s}"
       ".szt-bk-steps li:before{content:counter(s);display:flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:50%;background:#0E1B14;color:#E2C158;font-weight:800;font-size:15px;margin-bottom:10px}"
       ".szt-bk-steps b{display:block;font-size:15px;line-height:1.3;margin-bottom:4px}"
       ".szt-bk-steps span{display:block;font-size:13.5px;line-height:1.5;color:#56645A}"
       ".szt-bk-line{display:flex;gap:12px;align-items:flex-start;background:#0E1B14;color:#F4EEDD;border-radius:18px;padding:16px 18px;margin:0 0 14px;font-size:15px;line-height:1.55}"
       ".szt-bk-line strong{color:#E2C158;white-space:nowrap}"
       ".szt-bk-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}"
       ".szt-bk-c{background:#FBF8EF;border:1px solid #E8DFC8;border-radius:18px;padding:16px}"
       ".szt-bk-c b{display:block;font-size:15px;line-height:1.3;margin-bottom:5px;color:#0E1B14}"
       ".szt-bk-c span{display:block;font-size:13.5px;line-height:1.55;color:#46524A}"
       ".szt-bk-c a{color:#8A6A12!important;font-weight:700;text-decoration:underline}"
       ".szt-bk-q{margin-top:16px;border-top:1px solid #E8DFC8}"
       ".szt-bk-q details{border-bottom:1px solid #E8DFC8}"
       ".szt-bk-q summary{cursor:pointer;list-style:none;padding:14px 34px 14px 2px;font-weight:700;font-size:15px;position:relative;min-height:44px}"
       ".szt-bk-q summary::-webkit-details-marker{display:none}"
       ".szt-bk-q summary:after{content:'+';position:absolute;right:6px;top:10px;font-size:22px;color:#B8860B;font-weight:400}"
       ".szt-bk-q details[open] summary:after{content:'\\2212'}"
       ".szt-bk-q summary:focus-visible{outline:2px solid #B8860B;outline-offset:2px}"
       ".szt-bk-q .a{margin:0 0 14px;font-size:14.5px;line-height:1.6;color:#46524A;max-width:75ch}"
       ".szt-bk-cta{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-top:16px}"
       ".szt-bk-cta a{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:11px 18px;border-radius:12px;font-weight:800;font-size:14px;text-decoration:none!important;line-height:1}"
       ".szt-bk-wa{background:#25D366;color:#0b2414!important}.szt-bk-em{background:#fff;border:1px solid #DCD6C6;color:#0E1B14!important}"
       ".szt-bk-cta small{font-size:12.5px;color:#6B776E}"
       "@media(max-width:900px){.szt-bk-steps{grid-template-columns:1fr 1fr}.szt-bk-grid{grid-template-columns:1fr 1fr}}"
       "@media(max-width:560px){.szt-bk-steps,.szt-bk-grid{grid-template-columns:1fr}.szt-bk-line{display:block}.szt-bk-line strong{display:block;margin-bottom:4px}.szt-bk-cta a{flex:1 1 auto}.szt-bk-steps li{padding:14px 14px 14px 58px}.szt-bk-steps li:before{position:absolute;left:14px;top:14px;margin:0}.szt-bk-c{padding:13px 14px}}")

STEPS = ('<ol class="szt-bk-steps">'
         '<li><b>Message us</b><span>WhatsApp or email your dates, group size and wishes. A person in our Himachal office replies, usually within 2 hours.</span></li>'
         '<li><b>Get your plan and US$ quote</b><span>A day-by-day plan with what is included and what is not. Change anything — nothing to pay yet.</span></li>'
         '<li><b>Pay the 20% deposit</b><span>By card via Razorpay or by PayPal. You get a receipt by email and our written confirmation.</span></li>'
         '<li><b>Before you fly</b><span>Pay the balance before the trip. Your driver\'s name, photo and car number are shared with you before the trip.</span></li>'
         '</ol>')

CARDS = ('<div class="szt-bk-grid">'
         '<div class="szt-bk-c"><b>Everything in writing</b><span>Your quote and confirmation list exactly what is included. After the deposit we send a written confirmation with your hotels, car details, dates and contact numbers.</span></div>'
         '<div class="szt-bk-c"><b>Only 20% up front</b><span>The balance is paid before the trip, on the date written in your confirmation.</span></div>'
         '<div class="szt-bk-c"><b>Official payment channels only</b><span>Card via Razorpay (international cards accepted) or PayPal. We never ask you to pay into a personal account — if anyone sends you other bank details, check with us on +91 70874 88961 first.</span></div>'
         '<div class="szt-bk-c"><b>A registered local company</b><span>' + REG + ' · <a href="https://suzutravels.com/certificates/">see certificate</a>. GST-registered. Office at NH 103, Kulahru, Tehsil Ghumarwin, Bilaspur, Himachal Pradesh.</span></div>'
         '<div class="szt-bk-c"><b>Know your driver first</b><span>Your driver\'s name, photo and car number are shared with you before the trip.</span></div>'
         '<div class="szt-bk-c"><b>Reachable before and during the trip</b><span>Call or WhatsApp our office on +91 70874 88961 before and during your trip, or email info@suzutravels.com.</span></div>'
         '</div>')

QA = [("My flight is delayed — what happens?",
       "Send us your new arrival time on WhatsApp and we re-time your airport pick-up."),
      ("A road or monument is closed on the day.",
       "We may re-order sightseeing days, for example when a monument or road is closed on a given day, and we talk the options through with you. "
       "As our <a href=\"https://suzutravels.com/terms-and-conditions/\">terms</a> say, we are not responsible for delays or changes caused by events beyond our control "
       "(bad weather, landslides, road closures, strikes, government orders), and extra costs from such events are paid by the guest. Travel insurance is worth considering."),
      ("What if I need to cancel?",
       "Tell us in writing (email or WhatsApp). Full refund if you cancel within 48 hours of paying the deposit. After that, the cancellation terms written in your confirmation apply — read them before you pay."),
      ("What if you cancel my trip?",
       "If we cancel your trip for a reason within our control, we refund everything you have paid, or offer you another date or trip if you prefer."),
      ("How do I know I am paying the real Suzu Travels?",
       "Pay only on our <a href=\"https://suzutravels.com/payment/\">Payment page</a> or by a payment request we send you from info@suzutravels.com. We never ask you to pay into a personal account. Our registration certificate is on the "
       "<a href=\"https://suzutravels.com/certificates/\">certificates page</a>.")]

def qa():
    return '<div class="szt-bk-q">' + ''.join('<details><summary>%s</summary><p class="a">%s</p></details>' % q for q in QA) + '</div>'

def block(steps, sec_cls):
    return ('<!--szt:booking-protected--><section class="' + sec_cls + ' szt-bk" id="booking-protected" style="scroll-margin-top:90px"><style>' + CSS + '</style>'
            '<div class="lp-wrap"><span class="lp-eyebrow">Booking and payment</span>'
            '<h2>How Your Booking Is Protected</h2>'
            '<p class="szt-bk-lead">Booking a trip with a company on the other side of the world takes trust. Here is exactly what happens after you enquire, and how your money is handled.</p>'
            + (STEPS if steps else '') +
            '<div class="szt-bk-line"><strong>Booking terms</strong><span>' + BOOKING + '</span></div>'
            + CARDS + qa() +
            '<div class="szt-bk-cta"><a class="szt-bk-wa" href="' + WA + '" target="_blank" rel="noopener">Ask us on WhatsApp</a>'
            '<a class="szt-bk-em" href="mailto:info@suzutravels.com?subject=Question%20about%20booking%20an%20India%20trip">Email us</a>'
            '<small>Your message goes only to our team and is used only to answer it.</small></div>'
            '</div></section><!--/szt:booking-protected-->')

BANNED = ['verified', 'background-checked', 'government approved', 'registered DMC', '24/7', '24x7', '24×7', '₹', 'insured', 'guarantee']

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    for name, steps, cls in [('widget-11411.html', False, 'lp-sec'), ('widget-11412.html', True, 'lp-sec alt')]:
        h = block(steps, cls)
        assert '\n' not in h and '<script' not in h
        assert h.count(BOOKING) == 1 and REG in h
        low = h.lower()
        for b in BANNED:
            assert b.lower() not in low, b
        open(os.path.join(here, name), 'w').write(h)
        print(name, len(h))
