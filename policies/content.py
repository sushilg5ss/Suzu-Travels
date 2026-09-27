# -*- coding: utf-8 -*-
"""Policy text for suzutravels.com. Business terms confirmed by Sushil on 28 Sep 2026:
advance is non-refundable (one date change within 6 months), balance is paid before the trip starts,
Terms & Conditions are for tour bookings (the old holiday-membership terms are removed)."""

UPDATED = '28 September 2026'
PHONE, PHONE_TEL, EMAIL, WA = '+91 70874 88961', '+917087488961', 'info@suzutravels.com', 'https://wa.me/917087488961'
ADDRESS = 'Suzu Travels, NH103 Roadside, Ghumarwin, District Bilaspur, Himachal Pradesh 174021, India'
U = 'https://suzutravels.com'
L_CANCEL, L_TERMS, L_PRIVACY, L_PAY = U + '/cancellation-and-refund-policy/', U + '/terms-and-conditions/', U + '/privacy-policy/', U + '/payment/'

GRIEVANCE = (f'<p><b>Grievance Officer, Suzu Travels</b><br>{ADDRESS}<br>'
             f'Email: <a href="mailto:{EMAIL}">{EMAIL}</a> &middot; Phone / WhatsApp: <a href="tel:{PHONE_TEL}">{PHONE}</a></p>'
             '<p>We acknowledge every complaint within 48 hours and aim to resolve it within 30 days.</p>')

# ---------------------------------------------------------------- Cancellation & Refund
CANCEL = dict(
    pid=570, slug='cancellation-and-refund-policy', title='Cancellation and Refund Policy', short='Cancellation & Refund',
    eyebrow='Bookings & payments',
    intro=('This policy explains how you confirm a trip with Suzu Travels, what happens if you need to cancel or change it, '
           'and how refunds are paid. It applies to every tour package, hotel, cab and sightseeing booking made with us, '
           'online or offline.'),
    glance=[
        ('lock', 'Advance confirms your trip', 'Your booking is confirmed once the advance is received and we send the confirmation in writing.'),
        ('x', 'Advance is non-refundable', 'If you cancel, the advance is not refunded, whatever the reason.'),
        ('cal', 'One free date change', 'Instead of cancelling, move your trip once to a new date within 6 months.'),
        ('back', 'Refunds in 5&ndash;7 working days', 'Approved refunds go back to your original payment method.'),
    ],
    sections=[
        ('booking', 'Booking and payment', f'''
<ul>
<li>There is no contract between Suzu Travels and you until we have received the advance for your package.</li>
<li>The advance amount is written in your quotation. It confirms the booking and locks the rate quoted to you.</li>
<li>Once the advance is received, we send a written confirmation with your hotels, cab details, dates and service contact numbers. Please carry it on your trip.</li>
<li>The balance is paid before your trip starts, on the date written in your confirmation. If the advance or the balance is not paid, Suzu Travels may stop or withhold the services.</li>
<li>Final confirmations are accepted in writing only. No discount is given after the confirmation has been issued.</li>
<li>GST and other taxes are charged as shown in your quotation.</li>
</ul>
<h3>How to pay</h3>
<ul>
<li><b>Online:</b> on our <a href="{L_PAY}">Payment page</a> through Razorpay &mdash; UPI, debit and credit cards, net banking and wallets. You get a receipt by email.</li>
<li><b>Bank transfer or UPI:</b> only to the official Suzu Travels accounts listed on the <a href="{L_PAY}">Payment page</a>.</li>
</ul>
<div class="pl-note"><b>Pay safely.</b> We never ask you to pay into a personal account. If anyone gives you different account details, confirm them with us on {PHONE} before paying.</div>'''),
        ('cancel-by-you', 'If you cancel', f'''
<ul>
<li>Please send your cancellation in writing, by email to <a href="mailto:{EMAIL}">{EMAIL}</a> or on WhatsApp at <a href="{WA}">{PHONE}</a>, from the phone number or email used for the booking. The date we receive it is the cancellation date.</li>
<li><b>The advance is non-refundable</b> in every case, including accident, illness or any other personal reason.</li>
<li>If you have paid more than the advance, we refund the extra amount after deducting any costs already committed to hotels, transporters, airlines or railways that they do not refund to us. We share the details of any deduction with you.</li>
<li>No refund is due for a no-show, for leaving a tour midway, or for services on the itinerary that you choose not to use (meals, sightseeing, nights).</li>
</ul>'''),
        ('date-change', 'Changing your travel date', '''
<p>Instead of cancelling, you can move your trip to a new date.</p>
<ul>
<li>One date change is allowed per booking, to a date within 6 months of the original travel date. Please ask before your original start date.</li>
<li>Your advance is carried forward to the new date.</li>
<li>Hotel and transport rates change with the season. If the new date costs more, you pay the difference; if it costs less, we adjust it against your balance.</li>
<li>If the rescheduled trip is later cancelled, the advance is not refunded.</li>
</ul>'''),
        ('cancel-by-us', 'If we cancel or change your trip', '''
<ul>
<li>If Suzu Travels cancels your trip for a reason within our control, we refund everything you have paid, or offer you another date or trip if you prefer.</li>
<li>If a hotel on your itinerary becomes unavailable, we book another of a similar or higher category, as close to the original as possible.</li>
<li>We may re-order sightseeing days, for example when a monument or road is closed on a given day, so that the tour runs smoothly.</li>
</ul>
<h3>Weather, roads and other events beyond our control</h3>
<p>Mountain travel can be affected by snow, landslides, road closures, heavy traffic, strikes, curfews, government orders, technical faults or natural calamities. In such cases:</p>
<ul>
<li>we do our best to re-route or reschedule your trip;</li>
<li>extra costs (for example an extra night or a longer route) are paid by the guest directly;</li>
<li>unused services are refunded only to the extent that the hotel or transporter refunds them to us.</li>
</ul>'''),
        ('refunds', 'How refunds are paid', f'''
<ul>
<li>To ask for a refund, email <a href="mailto:{EMAIL}">{EMAIL}</a> or message us on WhatsApp with your booking reference, payment details and the reason.</li>
<li>Approved refunds are processed within <b>5&ndash;7 working days</b> of approval, to the original payment method (card, UPI or bank account).</li>
<li>After we process a refund, your bank or payment provider may take a few more days to show it. Suzu Travels is not responsible for delays caused by banks or payment gateways.</li>
<li>If a refund is delayed for any other reason, we will tell you promptly.</li>
</ul>'''),
        ('service-notes', 'Good to know before you travel', '''
<ul>
<li>Packages can be customised to your requirements before confirmation.</li>
<li>Air-conditioning is not used in vehicles in hill areas (most of North India and the North East).</li>
<li>Vehicles are booked point to point, as per the itinerary, and are not at disposal.</li>
<li>Standard hotel check-in is 12:00 noon and check-out is 10:00 AM; timings vary by hotel. Early check-in depends on availability.</li>
<li>Meals are served at the hotel&rsquo;s set timings. We are not responsible for meals not taken.</li>
<li>In Himachal and other hill destinations, hotels are graded by location, services and cost rather than by star rating, and facilities may be simpler than in big cities.</li>
<li>All travellers, including children, must carry a valid government photo ID. Foreign nationals must carry their passport and visa.</li>
</ul>'''),
        ('contact', 'Questions and complaints', f'''
<p>For any question about a booking, cancellation or refund, contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="tel:{PHONE_TEL}">{PHONE}</a> (calls and WhatsApp).</p>
{GRIEVANCE}
<p>Please also read our <a href="{L_TERMS}">Terms and Conditions</a> and <a href="{L_PRIVACY}">Privacy Policy</a>.</p>'''),
    ],
    seo_title='Cancellation and Refund Policy | Suzu Travels',
    seo_desc=('Suzu Travels cancellation and refund policy: payment terms, the non-refundable advance, '
              'one free date change, cancellations by us and refunds in 5–7 days.'),
)

# ---------------------------------------------------------------- Terms & Conditions
TERMS = dict(
    pid=564, slug='terms-and-conditions', title='Terms and Conditions', short='Terms & Conditions',
    eyebrow='Tour bookings',
    intro=('These terms apply when you book a tour package, hotel, cab or any other travel service with Suzu Travels, '
           'and when you use suzutravels.com. By confirming a booking or paying an advance, you agree to them.'),
    glance=[
        ('doc', 'What you book is in writing', 'Your quotation and confirmation list exactly what is included.'),
        ('lock', 'Advance confirms, balance before travel', 'Payment and cancellation follow our Cancellation &amp; Refund Policy.'),
        ('id', 'Carry valid ID', 'Government photo ID for every traveller; passport and visa for foreign nationals.'),
        ('help', 'We are reachable', f'Call or WhatsApp {PHONE} before and during your trip.'),
    ],
    sections=[
        ('about', 'About Suzu Travels', f'''
<p>Suzu Travels is a destination management company based in Ghumarwin, Himachal Pradesh. We plan and arrange holidays across India and to selected international destinations: tour packages, hotel stays, cabs, sightseeing and related services.</p>
<p>Hotels, transporters, airlines, railways and activity operators are independent suppliers. We choose them with care and coordinate your trip with them, and each supplier is also bound by its own rules (for example hotel check-in rules).</p>
<p>&ldquo;We&rdquo;, &ldquo;us&rdquo; and &ldquo;Suzu Travels&rdquo; mean Suzu Travels, {ADDRESS.split(", ", 1)[1]}. &ldquo;You&rdquo; means the person making the booking and every traveller on it.</p>'''),
        ('quotes', 'Quotes, prices and inclusions', '''
<ul>
<li>A quotation is valid for the period written on it and depends on availability until the booking is confirmed.</li>
<li>Your package includes only the services listed as inclusions in your quotation and confirmation. Anything not listed is excluded, for example: flights or train tickets (unless stated), monument and park entry fees, adventure activities, permits (unless stated), personal expenses, tips, and meals outside the chosen meal plan.</li>
<li>Meal plans (EP, CP, MAP or AP) are as stated in your confirmation. In a few places meal plans are not available and you buy your own meals.</li>
<li>Until the booking is confirmed, prices may change if taxes, fuel prices or government charges change. GST is charged as shown in your quotation.</li>
<li>Photos on our website and in brochures show typical scenes and properties; actual rooms and views can differ.</li>
</ul>'''),
        ('payment', 'Booking, payment and cancellation', f'''
<ul>
<li>Your booking is confirmed when the advance is received and we send you the confirmation in writing.</li>
<li>The balance is paid before your trip starts, on the date written in your confirmation.</li>
<li>Pay only through our <a href="{L_PAY}">Payment page</a> or to the official Suzu Travels accounts listed there.</li>
<li>Cancellations, date changes and refunds follow our <a href="{L_CANCEL}">Cancellation and Refund Policy</a>. The advance is non-refundable, and one date change within 6 months is allowed.</li>
</ul>'''),
        ('documents', 'Travel documents and permits', '''
<ul>
<li>Every traveller, including children, must carry a valid government photo ID. Hotels may refuse check-in without it.</li>
<li>Foreign nationals must carry a valid passport and visa, and are responsible for meeting India&rsquo;s entry rules. For international trips, each traveller is responsible for their own passport, visa and entry requirements.</li>
<li>Some areas need permits (for example parts of Spiti, Ladakh and the North East). We help arrange them when they are part of your package; permit rules and fees are set by the authorities and can change.</li>
<li>Please give us correct names and details. We are not responsible for problems caused by wrong or incomplete information.</li>
</ul>'''),
        ('stays', 'Hotels and stays', '''
<ul>
<li>Standard check-in is 12:00 noon and check-out is 10:00 AM; timings vary by hotel. Early check-in and late check-out depend on availability.</li>
<li>In hill destinations, hotels are graded by location, services and cost rather than star rating.</li>
<li>If a booked hotel becomes unavailable, we arrange another of a similar or higher category.</li>
<li>Guests must follow each hotel&rsquo;s rules. Any damage or extra charges at the hotel (minibar, room service, extra bed) are paid by the guest directly.</li>
</ul>'''),
        ('transport', 'Cabs and transport', '''
<ul>
<li>Vehicles are booked as per your itinerary, point to point, and are not at disposal. Extra kilometres or extra days are charged separately.</li>
<li>Air-conditioning is not used in vehicles in hill areas.</li>
<li>At some destinations, local rules allow only local taxis to certain sightseeing points; when this applies, it is noted in your itinerary.</li>
<li>For safety, drivers may decline to drive at night on mountain roads or in bad weather.</li>
</ul>'''),
        ('safety', 'Health, safety and conduct', '''
<ul>
<li>High-altitude places such as Ladakh, Spiti, Kedarnath and Rohtang can affect health. Please check with your doctor before travelling, especially with children, older travellers or medical conditions.</li>
<li>Adventure activities (paragliding, rafting, skiing, treks and similar) are run by independent operators, and you take part at your own risk.</li>
<li>We recommend travel insurance for every trip.</li>
<li>Please follow the advice of drivers, guides and local authorities, and respect local customs and the environment.</li>
</ul>'''),
        ('liability', 'Events beyond our control and liability', '''
<ul>
<li>Suzu Travels is not responsible for delays, changes or cancellations caused by events beyond our control, such as bad weather, landslides, road closures, traffic, strikes, curfews, government orders, epidemics, technical faults or natural calamities. Extra costs arising from such events are paid by the guest.</li>
<li>We are not responsible for loss of or damage to personal belongings.</li>
<li>Our liability for any claim is limited to the amount you paid us for the service concerned.</li>
</ul>'''),
        ('photos', 'Photos, videos and reviews', f'''
<p>If you send us photos or videos from your trip, or post a review, you allow Suzu Travels to use them on our website and social media without payment. We will remove any of them if you ask us at <a href="mailto:{EMAIL}">{EMAIL}</a>. Please send only material you have the right to share.</p>'''),
        ('website', 'Using our website', f'''
<ul>
<li>The content of suzutravels.com (text, photos, videos and design) belongs to Suzu Travels or is used with permission, and may not be copied for commercial use.</li>
<li>We try to keep the website accurate, but itineraries, prices and availability are confirmed only in your written quotation and confirmation.</li>
<li>Our <a href="{L_PRIVACY}">Privacy Policy</a> explains how we handle your personal information.</li>
</ul>'''),
        ('changes', 'Changes to these terms', f'''
<p>We may update these terms from time to time. The terms on this page on the date your booking is confirmed apply to that booking. Last updated: {UPDATED}.</p>'''),
        ('complaints', 'Complaints, law and jurisdiction', f'''
<p>If something goes wrong during your trip, please tell us straight away on <a href="tel:{PHONE_TEL}">{PHONE}</a> so we can fix it on the spot.</p>
{GRIEVANCE}
<p>These terms are governed by the laws of India. Any dispute is subject to the jurisdiction of the courts at Bilaspur, Himachal Pradesh.</p>'''),
    ],
    seo_title='Terms and Conditions for Tour Bookings | Suzu Travels',
    seo_desc=('Terms for booking tour packages, hotels and cabs with Suzu Travels: inclusions, payments, ID and permits, '
              'hotels, transport, safety, liability and complaints.'),
)

# ---------------------------------------------------------------- Privacy
PRIVACY = dict(
    pid=579, slug='privacy-policy', title='Privacy Policy', short='Privacy Policy',
    eyebrow='Your data',
    intro=('This policy explains what personal information Suzu Travels collects when you enquire, book or use suzutravels.com, '
           'why we collect it, who we share it with, and the choices and rights you have.'),
    glance=[
        ('shield', 'Only what your trip needs', 'We collect what is needed to plan, book and run your trip.'),
        ('card', 'We never see your card or UPI PIN', 'Online payments are handled by Razorpay.'),
        ('share', 'No selling of your data', 'We share details only with the hotels, drivers and partners serving your trip.'),
        ('user', 'You stay in control', 'Ask us to see, correct or delete your data at any time.'),
    ],
    sections=[
        ('who', 'Who we are', f'''
<p>Suzu Travels ({ADDRESS.split(", ", 1)[1]}) is responsible for the personal information described in this policy. Questions about it can be sent to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'''),
        ('collect', 'Information we collect', '''
<ul>
<li><b>Contact details:</b> name, phone number, email address and city or address.</li>
<li><b>Trip details:</b> travel dates, number and ages of travellers, destinations, hotel and meal preferences, and any special needs you choose to tell us (for example accessibility or dietary needs).</li>
<li><b>Identity documents</b>, only when a hotel, permit or ticket requires them: Aadhaar, driving licence, voter ID or passport, and visa details for foreign nationals.</li>
<li><b>Payment information:</b> the amount, date and transaction reference. Card numbers, UPI PINs and banking passwords are entered on Razorpay&rsquo;s secure page and are never seen or stored by us.</li>
<li><b>Website data:</b> IP address, browser and device type, pages visited and how you arrived, collected through cookies (see below).</li>
</ul>'''),
        ('how', 'How we collect it', '''
<ul>
<li>When you fill in an enquiry, booking or payment form on our website.</li>
<li>When you call, WhatsApp or email us, or contact us on Facebook, Instagram or through our ads.</li>
<li>From the person who books for you, for example a family member or group leader. They confirm that they have your consent to share your details with us.</li>
<li>Automatically, through cookies, when you browse our website.</li>
</ul>'''),
        ('use', 'How we use it', '''
<ul>
<li>To prepare quotations and plan, book and run your trip.</li>
<li>To contact you about your enquiry or booking by phone, WhatsApp, SMS or email, including during the trip.</li>
<li>To take payments, send receipts and process refunds.</li>
<li>To meet legal, tax and accounting requirements, and to prevent fraud.</li>
<li>To improve our website and services.</li>
<li>To send you offers and travel ideas. You can opt out at any time by replying &ldquo;STOP&rdquo; or writing to us.</li>
</ul>'''),
        ('share', 'Who we share it with', '''
<p>We do not sell or rent your personal information. We share it only as needed:</p>
<ul>
<li><b>Travel suppliers</b> serving your trip: hotels, drivers and transporters, guides, airlines, railways and activity operators. They also have their own privacy policies.</li>
<li><b>Razorpay</b>, to process online payments.</li>
<li><b>Service providers</b> who run our website, email, WhatsApp and records for us, under confidentiality.</li>
<li><b>Authorities</b>, when the law requires it, for example for permits or when a court or government agency asks.</li>
</ul>'''),
        ('cookies', 'Cookies and analytics', '''
<ul>
<li>Our website uses cookies: small files stored by your browser that help the site work and help us understand how it is used.</li>
<li>We use Google Analytics to measure visits and Google Ads to measure and show our ads. These services may set their own cookies and receive your IP address and browsing information on our site. Learn more in <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">how Google uses information from sites that use its services</a>.</li>
<li>Pages may show content from Google (reviews and maps) and YouTube, and link to our Facebook, Instagram and YouTube pages. These services may also set cookies.</li>
<li>You can block or delete cookies in your browser settings. Some parts of the site may not work properly without them.</li>
</ul>'''),
        ('keep', 'How long we keep it', '''
<ul>
<li>We keep booking and payment records for as long as tax and accounting laws require.</li>
<li>We keep enquiry details for as long as they are useful for your trip or future trips, unless you ask us to delete them sooner.</li>
<li>Copies of identity documents are kept only as long as needed for the booking they were collected for.</li>
</ul>'''),
        ('secure', 'How we protect it', '''
<p>We use reasonable technical and organisational measures to protect your information: an encrypted (HTTPS) website, secure payments through Razorpay, and access limited to the staff who need it. No method of storing or sending data over the internet is completely secure, so we cannot guarantee absolute security. If a breach affects you, we will tell you and the authorities as the law requires.</p>'''),
        ('rights', 'Your rights and choices', f'''
<p>Under Indian law, including the Digital Personal Data Protection Act, 2023, you can:</p>
<ul>
<li>ask for a summary of the personal information we hold about you;</li>
<li>ask us to correct, complete or update it;</li>
<li>ask us to delete it, unless we must keep it by law or to complete a booking;</li>
<li>withdraw your consent to marketing messages at any time;</li>
<li>nominate someone to exercise these rights for you in case of death or incapacity;</li>
<li>raise a complaint with our Grievance Officer and, if it is not resolved, with the Data Protection Board of India.</li>
</ul>
<p>To use any of these rights, email <a href="mailto:{EMAIL}">{EMAIL}</a> from the email address or phone number you used with us.</p>'''),
        ('children', 'Children', '''
<p>Bookings for children are made by a parent or guardian, who provides the child&rsquo;s details and consents on their behalf. We do not knowingly collect personal information directly from children.</p>'''),
        ('photos', 'Photos, videos and reviews', f'''
<p>If you send us trip photos or videos, or post a review, we may show them on our website and social media. Tell us at <a href="mailto:{EMAIL}">{EMAIL}</a> and we will remove them.</p>'''),
        ('links', 'Other websites', '''
<p>Our website links to other sites and services, such as Google, WhatsApp, Razorpay, Facebook, Instagram and YouTube. Their privacy practices are their own; please read their policies.</p>'''),
        ('changes', 'Changes to this policy', f'''
<p>We may update this policy from time to time. The latest version is always on this page, with the date it was last updated. Last updated: {UPDATED}.</p>'''),
        ('contact', 'Contact and grievance officer', f'''
<p>For privacy questions or requests:</p>
{GRIEVANCE}
<p>Please also read our <a href="{L_TERMS}">Terms and Conditions</a> and <a href="{L_CANCEL}">Cancellation and Refund Policy</a>.</p>'''),
    ],
    seo_title='Privacy Policy: Your Data and Cookies | Suzu Travels',
    seo_desc=('How Suzu Travels collects, uses, shares and protects your personal data, how cookies work on '
              'our website, and your rights under Indian law.'),
)

ALL = [CANCEL, TERMS, PRIVACY]
