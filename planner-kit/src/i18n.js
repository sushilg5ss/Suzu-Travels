/* Suzu Trip Planner — Hindi UI (EN / हिं), v0.8, 19 Oct 2026.
   A display-only layer: it translates what is on screen (and the print/PDF document) and never touches
   the data, the price engine or the lead message (the team always receives English).
   How: exact dictionary + pattern rules on text nodes and placeholder/aria-label/optgroup labels, re-applied
   by a MutationObserver after every render. Place and trip-idea names come from the data's own `hi` fields.
   v0.9 (20 Oct 2026): place tips, sight notes and region/season packing tips in Hindi too (TIPHI). Sight names stay English.
   v1.0 (21 Oct 2026): sight names in Hindi too (SIGHTHI). */
(function () {
  'use strict';
  var W = window, D = document, LANG = 'en', OBS = null, BUSY = false;
  var ORIG = new WeakMap(), DONE = new WeakMap(), AORIG = new WeakMap();
  var PN = {}, TN = {};

  var EX = {
    'Trip Planner': 'ट्रिप प्लानर', 'Traveller': 'यात्री', 'Travel agent': 'ट्रैवल एजेंट', 'Home': 'होम',
    'Plan your trip.': 'अपनी यात्रा प्लान करें।', 'Create your own itinerary.': 'अपना यात्रा कार्यक्रम खुद बनाएँ।',
    'Pick your places, nights, hotel and car — see the road map, a day-by-day plan and the estimated cost instantly. Download it free, share it, or ask our team for today\'s best price.': 'जगहें, रातें, होटल और गाड़ी चुनें — तुरंत रोड मैप, दिन-ब-दिन प्लान और अनुमानित खर्च देखें। मुफ़्त डाउनलोड करें, शेयर करें, या हमारी टीम से आज की सबसे अच्छी कीमत पूछें।',
    'Holiday planner': 'हॉलिडे प्लानर', 'Yatra & Mata darshan': 'यात्रा और माता दर्शन', 'Cabs': 'टैक्सी', 'Hotels': 'होटल',
    'Starting from': 'कहाँ से', 'Pickup city': 'पिकअप शहर', 'Going to': 'कहाँ जाना है', 'Place or ready trip idea': 'जगह या तैयार ट्रिप',
    'Start date': 'यात्रा की तारीख', 'Travellers': 'यात्री', 'Children & rooms next': 'बच्चे और कमरे अगले चरण में', 'Plan my trip': 'मेरी यात्रा प्लान करें',
    'Popular:': 'लोकप्रिय:', 'Customise →': 'बदलें →', '/adult': '/वयस्क', '/ adult': '/ वयस्क',
    'Ready pilgrim circuits — open one, then change nights, hotels and car as you like.': 'तैयार तीर्थ यात्राएँ — कोई भी खोलें, फिर रातें, होटल और गाड़ी अपनी मर्ज़ी से बदलें।',
    'From': 'कहाँ से', 'To': 'कहाँ तक', 'Trip': 'यात्रा', 'One way drop': 'एक तरफ़ (ड्रॉप)', 'Round trip': 'आना-जाना (राउंड ट्रिप)', 'Car': 'गाड़ी', 'Get fare': 'किराया देखें',
    'Destination': 'जगह', 'Check-in': 'चेक-इन', 'Nights': 'रातें', 'Rooms': 'कमरे', 'Hotel class': 'होटल श्रेणी', 'Check price': 'कीमत देखें',
    'Start from a ready idea': 'तैयार ट्रिप से शुरू करें', 'One tap loads the route — then make it yours.': 'एक टैप में रूट तैयार — फिर अपने हिसाब से बदलें।',
    'All': 'सभी', 'Himachal': 'हिमाचल', 'Mata darshan': 'माता दर्शन', 'Char Dham & yatra': 'चार धाम और यात्रा', 'Honeymoon': 'हनीमून', 'Kashmir': 'कश्मीर', 'Ladakh': 'लद्दाख',
    'Uttarakhand': 'उत्तराखंड', 'Rajasthan & Agra': 'राजस्थान और आगरा', 'Rajasthan': 'राजस्थान', 'Agra & Mathura': 'आगरा और मथुरा', 'Punjab': 'पंजाब', 'City': 'शहर', 'Cities & airports': 'शहर और एयरपोर्ट', 'Other': 'अन्य',
    'HIMACHAL': 'हिमाचल', 'KASHMIR': 'कश्मीर', 'LADAKH': 'लद्दाख', 'UTTARAKHAND': 'उत्तराखंड', 'PUNJAB': 'पंजाब', 'RAJASTHAN': 'राजस्थान', 'DELHI': 'दिल्ली',
    'Route & nights': 'रूट और रातें', 'Pickup': 'पिकअप', 'Drop': 'ड्रॉप', '⇅ Best order': '⇅ सबसे छोटा रूट', 'Clear': 'सब हटाएँ',
    'Dates & travellers': 'तारीख और यात्री', 'Adults': 'वयस्क', '12+ years': '12+ साल', 'Children': 'बच्चे', '5–11 years': '5–11 साल', 'Infants': 'शिशु', 'under 5, free': '5 साल से कम, मुफ़्त', 'auto': 'अपने आप',
    'Hotel, meals & car': 'होटल, खाना और गाड़ी', 'Meals': 'खाना', 'Breakfast + dinner': 'नाश्ता + रात का खाना', 'Breakfast only': 'सिर्फ़ नाश्ता',
    'Add-ons': 'अतिरिक्त सेवाएँ', '(price on request)': '(कीमत पूछने पर)', 'Best for group': 'ग्रुप के हिसाब से सबसे सही',
    'breakfast + dinner': 'नाश्ता + रात का खाना', 'breakfast': 'नाश्ता', 'Visit on the way · no night': 'रास्ते में दर्शन · रात नहीं',
    'Travel agent mode — your branding on the PDF & link': 'ट्रैवल एजेंट मोड — PDF और लिंक पर आपकी ब्रांडिंग', 'Agency name': 'एजेंसी का नाम', 'Agency phone': 'एजेंसी फ़ोन', 'Your markup %': 'आपका मार्कअप %', 'Agency email': 'एजेंसी ईमेल', 'Agency GSTIN (optional)': 'एजेंसी GSTIN (वैकल्पिक)', 'Agency logo for your PDF (optional)': 'आपके PDF के लिए एजेंसी लोगो (वैकल्पिक)', 'Add logo': 'लोगो जोड़ें', 'Change logo': 'लोगो बदलें', 'Remove logo': 'लोगो हटाएँ', 'Your agency details and logo stay in this browser only — never uploaded. Suzu\'s B2B estimate already includes 5% GST; add your GSTIN and our team uses it for your agency\'s invoice.': 'आपकी एजेंसी की जानकारी और लोगो सिर्फ़ इसी ब्राउज़र में रहते हैं — कभी अपलोड नहीं होते। Suzu के B2B अनुमान में 5% GST पहले से शामिल है; अपना GSTIN डालें, हमारी टीम इसे आपकी एजेंसी के इनवॉइस के लिए इस्तेमाल करेगी।', 'Request Suzu B2B rate card': 'Suzu B2B रेट कार्ड मँगाएँ', 'Get the Suzu B2B rate card': 'Suzu B2B रेट कार्ड पाएँ', 'Net rates for travel agents — hotels, cabs and packages in Himachal and North India. Our team sends it on WhatsApp / email.': 'ट्रैवल एजेंटों के लिए नेट रेट — हिमाचल और उत्तर भारत के होटल, कैब और पैकेज। हमारी टीम इसे WhatsApp / ईमेल पर भेजती है।', 'Logo added — it shows on your PDF': 'लोगो जुड़ गया — यह आपके PDF पर दिखेगा', 'Logo removed': 'लोगो हटा दिया', 'Please choose a PNG, JPG or WebP image': 'कृपया PNG, JPG या WebP इमेज चुनें', 'Logo file is over 5 MB — please choose a smaller one': 'लोगो फ़ाइल 5 MB से बड़ी है — छोटी फ़ाइल चुनें', 'Could not read this image': 'यह इमेज पढ़ी नहीं जा सकी', 'Logo too big to remember — it works until you close this tab': 'लोगो याद रखने के लिए बड़ा है — यह टैब बंद होने तक काम करेगा',
    'Your trip': 'आपकी यात्रा', 'Add places to see the route': 'रूट देखने के लिए जगहें जोड़ें', '▶ Play my trip': '▶ मेरी यात्रा चलाएँ', '❚❚ Pause': '❚❚ रोकें', 'Real map': 'असली नक्शा', 'Day-by-day plan': 'दिन-ब-दिन प्लान',
    'Add your first place on the left — or pick a ready idea above.': 'बाईं ओर अपनी पहली जगह जोड़ें — या ऊपर से कोई तैयार ट्रिप चुनें।',
    'DAY': 'दिन', 'Long drive': 'लंबा सफ़र', 'Free day — relax, cafés, local markets': 'खाली दिन — आराम, कैफ़े, लोकल बाज़ार',
    'Check out and drop at the airport / station.': 'चेक-आउट और एयरपोर्ट / स्टेशन पर ड्रॉप।',
    'Estimated price': 'अनुमानित कीमत', 'Trip price': 'यात्रा की कीमत', 'Service & GST (5%)': 'सर्विस और GST (5%)', 'Estimated total': 'अनुमानित कुल',
    'Get best price & availability': 'सबसे अच्छी कीमत और उपलब्धता पाएँ', 'Get B2B rates & availability': 'B2B रेट और उपलब्धता पाएँ', 'Download itinerary (PDF)': 'यात्रा कार्यक्रम डाउनलोड करें (PDF)',
    'Share link': 'लिंक शेयर करें', 'Client link (your branding)': 'क्लाइंट लिंक (आपकी ब्रांडिंग)', 'Chat on WhatsApp': 'WhatsApp पर बात करें', '⬇ Download PDF': '⬇ PDF डाउनलोड करें',
    'Estimate, not a quote.': 'यह अनुमान है, फ़ाइनल कोटेशन नहीं।', 'Agent view': 'एजेंट व्यू',
    'Why plan with Suzu Travels': 'सुज़ू ट्रैवल्स के साथ क्यों प्लान करें', 'Local Himachal team': 'हिमाचल की लोकल टीम', 'Own office in Himachal, planning trips since 2019': 'हिमाचल में अपना ऑफ़िस, 2019 से यात्राएँ प्लान कर रहे हैं',
    'HP Tourism registered': 'HP टूरिज़्म में रजिस्टर्ड', 'Private car, experienced hill drivers': 'प्राइवेट गाड़ी, पहाड़ों के अनुभवी ड्राइवर', 'Sedan to Tempo Traveller, all North India': 'सेडान से टेम्पो ट्रैवलर तक, पूरे उत्तर भारत में',
    'Pay a small token': 'थोड़ा टोकन दें', 'Lock today\'s rate, pay the balance before the trip': 'आज का रेट लॉक करें, बाकी पैसे यात्रा से पहले दें',
    'Questions': 'सवाल-जवाब',
    'Is the price shown final?': 'क्या दिखाई गई कीमत फ़ाइनल है?',
    'No — it is an estimate built from 2026 market rates for cars and hotels, kept on the safe (higher) side. Hotel availability and the exact rate depend on your dates. Our team checks availability and usually confirms at or below the estimate, with any discounts going on top.': 'नहीं — यह गाड़ी और होटल के 2026 के बाज़ार रेट से बना अनुमान है, जो सुरक्षित (ऊँची) तरफ़ रखा गया है। होटल की उपलब्धता और सही रेट आपकी तारीखों पर निर्भर करते हैं। हमारी टीम उपलब्धता देखकर आम तौर पर इसी अनुमान या उससे कम में कन्फ़र्म करती है, और कोई भी छूट उसके ऊपर से मिलती है।',
    'Do you save my itinerary?': 'क्या आप मेरा यात्रा कार्यक्रम सेव करते हैं?',
    'No. Your whole plan lives inside the link itself — nothing is stored on our servers. Keep the link or download the PDF. We only receive your name and number if you ask for the best price or download.': 'नहीं। आपका पूरा प्लान लिंक के अंदर ही रहता है — हमारे सर्वर पर कुछ भी सेव नहीं होता। लिंक संभालकर रखें या PDF डाउनलोड करें। हमें आपका नाम और नंबर तभी मिलता है जब आप सबसे अच्छी कीमत माँगते हैं या डाउनलोड करते हैं।',
    'I\'m a travel agent. Can I use this for my clients?': 'मैं ट्रैवल एजेंट हूँ। क्या मैं इसे अपने क्लाइंट के लिए इस्तेमाल कर सकता हूँ?',
    'Yes. Switch to "Travel agent" at the top, add your agency name and markup, and download a PDF or share a link with your branding. Ground handling is done by Suzu Travels as your DMC — send us the link to get B2B rates and availability.': 'हाँ। ऊपर "ट्रैवल एजेंट" चुनें, अपनी एजेंसी का नाम और मार्कअप डालें, और अपनी ब्रांडिंग के साथ PDF डाउनलोड करें या लिंक शेयर करें। ज़मीनी इंतज़ाम सुज़ू ट्रैवल्स आपके DMC के रूप में करता है — B2B रेट और उपलब्धता के लिए हमें लिंक भेजें।',
    'How do I book?': 'बुकिंग कैसे करें?',
    'Send us your itinerary (the "Get best price" button). After we confirm hotels and car, a small token advance locks the rate and the balance is paid before the trip. The advance is non-refundable, but you can change the travel date once within 6 months. Pay online by Razorpay, or by bank transfer / UPI.': 'हमें अपना यात्रा कार्यक्रम भेजें ("सबसे अच्छी कीमत" बटन)। होटल और गाड़ी कन्फ़र्म होने के बाद थोड़ा टोकन एडवांस रेट लॉक करता है और बाकी पैसे यात्रा से पहले दिए जाते हैं। एडवांस वापस नहीं होता, लेकिन आप यात्रा की तारीख 6 महीने के अंदर एक बार बदल सकते हैं। Razorpay से ऑनलाइन, या बैंक ट्रांसफ़र / UPI से भुगतान करें।',
    'What is not included in the estimate?': 'अनुमान में क्या शामिल नहीं है?',
    'Flights and trains, entry tickets, adventure activities, ropeway / gondola / helicopter tickets, Rohtang and other permits, pony or palki charges, and personal expenses. Tolls, parking and driver allowance are included as an estimate.': 'फ़्लाइट और ट्रेन, एंट्री टिकट, एडवेंचर एक्टिविटी, रोपवे / गोंडोला / हेलिकॉप्टर टिकट, रोहतांग व अन्य परमिट, पिट्ठू/पालकी का खर्च और निजी खर्च। टोल, पार्किंग और ड्राइवर भत्ता अनुमान में शामिल हैं।',
    '· Road distances © OpenStreetMap contributors (OSRM)': '· सड़क दूरी © OpenStreetMap contributors (OSRM)',
    'Estimated, per adult': 'अनुमानित, प्रति वयस्क', 'Get best price': 'सबसे अच्छी कीमत',
    'Get your itinerary': 'अपना यात्रा कार्यक्रम पाएँ', 'We\'ll send today\'s best price on WhatsApp.': 'हम आज की सबसे अच्छी कीमत WhatsApp पर भेजेंगे।',
    'Get today\'s best price': 'आज की सबसे अच्छी कीमत पाएँ', 'Our team checks your dates and sends the best price on WhatsApp — usually within 30 minutes (10 AM – 9 PM).': 'हमारी टीम आपकी तारीखें देखकर WhatsApp पर सबसे अच्छी कीमत भेजती है — आम तौर पर 30 मिनट में (सुबह 10 – रात 9 बजे)।',
    'Download your itinerary': 'अपना यात्रा कार्यक्रम डाउनलोड करें', 'Free PDF with day plan, map and estimate. We may WhatsApp you a better price.': 'दिन-ब-दिन प्लान, नक्शे और अनुमान के साथ मुफ़्त PDF। हम WhatsApp पर बेहतर कीमत भी भेज सकते हैं।',
    'Get your share link': 'अपना शेयर लिंक पाएँ', 'Your plan lives in the link — nothing is stored. We may WhatsApp you a better price.': 'आपका प्लान लिंक में ही रहता है — कुछ भी सेव नहीं होता। हम WhatsApp पर बेहतर कीमत भी भेज सकते हैं।',
    'Book this cab': 'यह टैक्सी बुक करें', 'We confirm the car and final fare on WhatsApp.': 'हम गाड़ी और फ़ाइनल किराया WhatsApp पर कन्फ़र्म करते हैं।',
    'Get hotel options': 'होटल के विकल्प पाएँ', 'We send 2–3 hotel options with photos and today\'s rate.': 'हम फ़ोटो और आज के रेट के साथ 2–3 होटल विकल्प भेजते हैं।', 'Your details': 'आपकी जानकारी',
    '+ Make it a trip': '+ पूरी यात्रा बनाएँ', 'All cab routes': 'सभी टैक्सी रूट', 'Pick two different places.': 'दो अलग-अलग जगहें चुनें।',
    'Your name': 'आपका नाम', 'WhatsApp number': 'WhatsApp नंबर', 'Email': 'ईमेल', '(optional)': '(ज़रूरी नहीं)', 'Agency / company': 'एजेंसी / कंपनी',
    'Continue': 'आगे बढ़ें', 'Send': 'भेजें', 'Download PDF': 'PDF डाउनलोड करें', 'Create link': 'लिंक बनाएँ', 'We contact you only about this trip. No spam.': 'हम सिर्फ़ इसी यात्रा के बारे में संपर्क करेंगे। कोई स्पैम नहीं।',
    'Please enter your name.': 'कृपया अपना नाम लिखें।', 'Please enter a valid WhatsApp number (10 digits, or +country code).': 'कृपया सही WhatsApp नंबर लिखें (10 अंक, या +देश कोड)।', 'Please check the email, or leave it empty.': 'कृपया ईमेल जाँचें, या खाली छोड़ दें।',
    'Our team will WhatsApp you on': 'हमारी टीम आपको इस नंबर पर WhatsApp करेगी:', 'with availability and the best price.': '— उपलब्धता और सबसे अच्छी कीमत के साथ।',
    'Chat on WhatsApp now': 'अभी WhatsApp पर बात करें', '⬇ Download PDF too': '⬇ PDF भी डाउनलोड करें',
    'Your link is ready': 'आपका लिंक तैयार है', 'Client link ready': 'क्लाइंट लिंक तैयार है', 'Anyone with the link sees this exact plan.': 'लिंक वाला कोई भी व्यक्ति यही प्लान देखेगा।',
    'Your client sees your agency name and client price only.': 'आपके क्लाइंट को सिर्फ़ आपकी एजेंसी का नाम और क्लाइंट कीमत दिखेगी।', 'Copy': 'कॉपी', 'Share…': 'शेयर…',
    'Link copied': 'लिंक कॉपी हो गया', 'Select and copy the link': 'लिंक चुनकर कॉपी करें', 'Keep at least one night': 'कम से कम एक रात रखें', 'Add a place to start again': 'फिर से शुरू करने के लिए जगह जोड़ें',
    'Stops re-ordered for the shortest drive': 'सबसे छोटे सफ़र के लिए जगहों का क्रम बदला गया', 'Max 14 stops — call us for longer tours': 'ज़्यादा से ज़्यादा 14 जगहें — लंबे टूर के लिए हमें कॉल करें',
    'Opening your itinerary in a new tab…': 'आपका यात्रा कार्यक्रम नए टैब में खुल रहा है…', 'Real map could not load — showing the route sketch': 'असली नक्शा नहीं खुला — रूट का स्केच दिखा रहे हैं',
    'Agent mode: add your agency & markup in the builder': 'एजेंट मोड: बिल्डर में अपनी एजेंसी और मार्कअप जोड़ें',
    'Have a budget?': 'बजट तय है?', 'per adult, optional': 'प्रति वयस्क, अपनी मर्ज़ी से', 'Fit my budget': 'मेरे बजट में बनाओ', 'e.g. 20000': 'जैसे 20000',
    'Enter your budget per adult in rupees, e.g. 20000.': 'प्रति वयस्क अपना बजट रुपये में लिखें, जैसे 20000।',
    'Standard': 'स्टैंडर्ड', 'Deluxe': 'डीलक्स', 'Super Deluxe': 'सुपर डीलक्स', 'Luxury': 'लग्ज़री', '2★ / homestay': '2★ / होमस्टे',
    'Standard (2★ / homestay)': 'स्टैंडर्ड (2★ / होमस्टे)', 'Deluxe (3★)': 'डीलक्स (3★)', 'Super Deluxe (3★+ / 4★)': 'सुपर डीलक्स (3★+ / 4★)', 'Luxury (4★–5★)': 'लग्ज़री (4★–5★)',
    'Paragliding': 'पैराग्लाइडिंग', 'River rafting': 'रिवर राफ़्टिंग', 'Snow activities & gear': 'बर्फ़ की एक्टिविटी और सामान', 'Rohtang Pass permit': 'रोहतांग पास परमिट', 'Gulmarg Gondola tickets': 'गुलमर्ग गोंडोला टिकट',
    'Houseboat night': 'हाउसबोट में एक रात', 'Kedarnath helicopter': 'केदारनाथ हेलिकॉप्टर', 'Vaishno Devi helicopter': 'वैष्णो देवी हेलिकॉप्टर', 'Jungle safari': 'जंगल सफ़ारी', 'Riverside camping': 'नदी किनारे कैंपिंग',
    'Pony / palki': 'घोड़ा / पालकी', 'Local guide': 'लोकल गाइड', 'Trip photographer': 'ट्रिप फ़ोटोग्राफ़र', 'Honeymoon decor & cake': 'हनीमून सजावट और केक',
    /* PDF */
    'Day': 'दिन', 'Plan': 'प्लान', 'Night stay': 'रात का ठहराव', 'Please note': 'कृपया ध्यान दें', 'Place': 'जगह', 'Category': 'श्रेणी', 'Route at a glance': 'रूट एक नज़र में',
    'Leg': 'सफ़र', 'Road': 'सड़क', 'Drive': 'ड्राइव', 'Total': 'कुल', 'Included': 'शामिल', 'Not included': 'शामिल नहीं', 'How to book': 'बुकिंग कैसे करें', 'All applicable taxes': 'सभी लागू टैक्स',
    'Dates:': 'तारीख:', 'Travellers:': 'यात्री:', 'Pickup:': 'पिकअप:', 'Drop:': 'ड्रॉप:', 'Car:': 'गाड़ी:', 'Hotels:': 'होटल:', 'Road distance:': 'सड़क दूरी:',
    'Flights / trains, entry tickets, ropeway, gondola and helicopter tickets': 'फ़्लाइट / ट्रेन, एंट्री टिकट, रोपवे, गोंडोला और हेलिकॉप्टर टिकट',
    'Adventure activities, Rohtang and other permits, pony / palki, local union taxis where mandatory': 'एडवेंचर एक्टिविटी, रोहतांग व अन्य परमिट, घोड़ा / पालकी, जहाँ ज़रूरी हो वहाँ लोकल यूनियन टैक्सी',
    'Personal expenses, room heaters, anything not listed as included': 'निजी खर्च, रूम हीटर, और जो कुछ "शामिल" में नहीं लिखा',
    'A small token advance confirms the booking and locks the rate; the balance is paid before the trip starts.': 'थोड़ा टोकन एडवांस बुकिंग कन्फ़र्म करता है और रेट लॉक करता है; बाकी पैसे यात्रा शुरू होने से पहले दिए जाते हैं।',
    'The advance is non-refundable; instead of cancelling, the travel date can be changed once, to a date within 6 months.': 'एडवांस वापस नहीं होता; कैंसल करने की जगह यात्रा की तारीख एक बार, 6 महीने के अंदर की किसी तारीख पर बदली जा सकती है।',
    'Pay online via Razorpay, or by bank transfer / UPI.': 'Razorpay से ऑनलाइन, या बैंक ट्रांसफ़र / UPI से भुगतान करें।',
    'Good to know & packing': 'काम की बातें और सामान', 'Place notes': 'जगहों के बारे में', 'On the trip — useful numbers': 'यात्रा में — ज़रूरी नंबर',
    'Suzu Travels 24×7 trip desk · WhatsApp / call': 'सुज़ू ट्रैवल्स 24×7 ट्रिप डेस्क · WhatsApp / कॉल', '· Emergency': '· इमरजेंसी', '· Ambulance': '· एम्बुलेंस', '· India Tourist Helpline': '· इंडिया टूरिस्ट हेल्पलाइन',
    'Estimate from 2026 market rates (higher side). Final price after availability check — usually at or below this estimate.': '2026 के बाज़ार रेट से अनुमान (ऊँची तरफ़)। फ़ाइनल कीमत उपलब्धता देखकर — आम तौर पर इसी अनुमान या इससे कम।',
    'Subject to hotel and car availability on your dates.': 'आपकी तारीखों पर होटल और गाड़ी की उपलब्धता के अनुसार।',
    'In Kashmir and Ladakh sightseeing runs on local union taxis; the estimate already includes their higher rates.': 'कश्मीर और लद्दाख में घूमना लोकल यूनियन टैक्सी से होता है; अनुमान में उनके ऊँचे रेट पहले से शामिल हैं।',
    'April–June is very hot in Rajasthan and Agra (40 °C+ afternoons). We schedule forts and the Taj for early morning; October–March is the comfortable season.': 'अप्रैल–जून में राजस्थान और आगरा बहुत गर्म रहते हैं (दोपहर 40 °C+)। हम किले और ताज सुबह जल्दी रखते हैं; अक्टूबर–मार्च आरामदायक मौसम है।',
    'Taj Mahal is closed on Fridays and your Agra day falls on a Friday — shift the trip by a day or we plan the Taj for the next morning.': 'ताजमहल शुक्रवार को बंद रहता है और आपका आगरा वाला दिन शुक्रवार है — यात्रा एक दिन आगे-पीछे करें, या हम ताज अगली सुबह रखेंगे।',
    'Vaishno Devi needs a Yatra registration (RFID card) — register early.': 'वैष्णो देवी के लिए यात्रा रजिस्ट्रेशन (RFID कार्ड) ज़रूरी है — जल्दी रजिस्टर करें।',
    'Our team confirms hotel availability before you book.': 'बुकिंग से पहले हमारी टीम होटल की उपलब्धता कन्फ़र्म करती है।',
    'Your personalised itinerary · आपकी अपनी यात्रा योजना': 'आपकी अपनी यात्रा योजना', 'Your personalised itinerary · आपकी अपनी यात्रा योजना · Hill roads, realistic drive times': 'आपकी अपनी यात्रा योजना · पहाड़ी सड़कें, असली ड्राइव समय'
    , '📌 Keep this as Plan A & compare': '📌 इसे Plan A रखें और तुलना करें', 'Change hotels, car, nights or places — see both prices side by side.': 'होटल, गाड़ी, रातें या जगहें बदलें — दोनों के दाम साथ-साथ देखें।', 'Compare plans': 'प्लान की तुलना', 'This plan': 'यह प्लान', 'Days': 'दिन', 'Start': 'शुरुआत', 'Travellers': 'यात्री', 'Road km': 'सड़क किमी', 'Per adult': 'प्रति वयस्क', '⇄ Go back to Plan A': '⇄ Plan A पर वापस जाएँ', '📌 Keep this as Plan A': '📌 इसे Plan A रखें', '✕ Close compare': '✕ तुलना बंद करें', 'Both plans cost about the same per adult.': 'दोनों प्लान का दाम प्रति वयस्क लगभग बराबर है।', 'Saved as Plan A — now change anything to compare': 'Plan A सेव हुआ — अब कुछ भी बदलकर तुलना करें', 'Back to Plan A — your other plan is now Plan A': 'Plan A पर वापस — आपका दूसरा प्लान अब Plan A है'
  };
  var MS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], MH = ['जन', 'फ़र', 'मार्च', 'अप्रै', 'मई', 'जून', 'जुला', 'अग', 'सित', 'अक्टू', 'नवं', 'दिस'];
  var WD = { Sun: 'रवि', Mon: 'सोम', Tue: 'मंगल', Wed: 'बुध', Thu: 'गुरु', Fri: 'शुक्र', Sat: 'शनि' };
  var MFULL = { January: 'जनवरी', February: 'फ़रवरी', March: 'मार्च', April: 'अप्रैल', June: 'जून', July: 'जुलाई', August: 'अगस्त', September: 'सितंबर', October: 'अक्टूबर', November: 'नवंबर', December: 'दिसंबर' };
  function dt(s) {
    return s.replace(/\b(Sun|Mon|Tue|Wed|Thu|Fri|Sat)\b/g, function (m) { return WD[m]; })
      .replace(/\b(\d{1,2})[ –-]+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b/g, function (m, d, mo) { return d + ' ' + MH[MS.indexOf(mo)]; })
      .replace(/\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b/g, function (m) { return MH[MS.indexOf(m)]; });
  }
  var DATE_RX = /^((Sun|Mon|Tue|Wed|Thu|Fri|Sat),? )?\d{1,2} (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)( \d{4})?( – \d{1,2} (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)( \d{4})?)?$|^(Sun|Mon|Tue|Wed|Thu|Fri|Sat)$/;
  function pn(s) {
    s = String(s).trim();
    if (PN[s]) return PN[s];
    var b = s.split(' (')[0]; if (PN[b]) return PN[b] + s.slice(b.length);
    return s;
  }
  function pnAny(s) { var r = pn(s); return r !== s ? r : (TN[s] || s); }
  function isPlace(s) { s = String(s).trim(); return !!(PN[s] || PN[s.split(' (')[0]]); }
  function hrs(s) { return s.replace(/(\d+(?:\.\d+)?) h\b/g, '$1 घंटे').replace(/(\d+) min\b/g, '$1 मिनट').replace(/(\d[\d,]*) km\b/g, '$1 किमी'); }
  function pax(s) {
    var m = s.match(/^(\d+) adults?(, (\d+) child(?:ren)?)?(, (\d+) infants?)?$/); if (!m) return null;
    return m[1] + ' वयस्क' + (m[3] ? ', ' + m[3] + ' बच्चे' : '') + (m[5] ? ', ' + m[5] + ' शिशु' : '');
  }
  /* phase 2 (v0.9, 20 Oct 2026): place tips, sight notes, region / season packing tips (PDF "Good to know") */
  var TIPHI = {
    'night in yatra tents': 'यात्रा टेंट में रात',
    'Car drops you at the Chandanwari road-head; nights in yatra tents at Sheshnag and Panchtarni': 'गाड़ी आपको चंदनवाड़ी में सड़क के आख़िरी छोर पर छोड़ेगी; शेषनाग और पंचतरणी में यात्रा टेंट में रातें',
    'Amarnath Yatra permit (route + date) and Compulsory Health Certificate needed; age 13–70': 'अमरनाथ यात्रा परमिट (रूट + तारीख़) और अनिवार्य स्वास्थ्य प्रमाणपत्र ज़रूरी; उम्र 13–70 वर्ष',
    'start before dawn, back at camp by evening': 'सुबह होने से पहले निकलें, शाम तक कैंप वापस',
    'closed Mondays': 'सोमवार बंद',
    'IGI Airport / NDLS railway station pickup': 'IGI एयरपोर्ट / नई दिल्ली रेलवे स्टेशन से पिकअप',
    'Airport / railway station / ISBT pickup': 'एयरपोर्ट / रेलवे स्टेशन / ISBT से पिकअप',
    'Railway station pickup': 'रेलवे स्टेशन से पिकअप',
    'Jolly Grant airport pickup': 'जॉली ग्रांट एयरपोर्ट से पिकअप',
    'SUV recommended. Altitude 3,800 m — take it slow on day 1': 'SUV बेहतर है। ऊँचाई 3,800 मी — पहले दिन आराम से रहें',
    'Camps only, open about mid-June to mid-October': 'सिर्फ़ कैंप, लगभग मध्य जून से मध्य अक्टूबर तक खुले',
    'Ropeway or 1.5 km climb to the shrine': 'मंदिर तक रोपवे या 1.5 किमी चढ़ाई',
    'Navratri brings 2–4 hour queues': 'नवरात्रि में 2–4 घंटे की लाइनें लगती हैं',
    'Keep a full day for the Bhawan trek': 'भवन यात्रा (ट्रेक) के लिए पूरा एक दिन रखें',
    'One night on a houseboat is a classic': 'एक रात हाउसबोट में ठहरना ख़ास अनुभव है',
    'Rest day on arrival (3,500 m) is a must': 'पहुँचने के दिन आराम ज़रूरी है (3,500 मी)',
    'Camps/cottages, very cold nights': 'कैंप/कॉटेज, रातें बहुत ठंडी',
    'Kedarnath needs 2 nights here: trek up, darshan, trek down': 'केदारनाथ के लिए यहाँ 2 रातें चाहिए: चढ़ाई, दर्शन, उतराई',
    'Agra Cantt railway / Yamuna Expressway from Delhi (~3.5 h)': 'आगरा कैंट रेलवे / दिल्ली से यमुना एक्सप्रेसवे (~3.5 घंटे)',
    'Keep phones/leather items out at Janmabhoomi; evening Prem Mandir lights': 'जन्मभूमि में फ़ोन/चमड़े का सामान न ले जाएँ; शाम को प्रेम मंदिर की रोशनी',
    'Jaipur airport / railway station pickup': 'जयपुर एयरपोर्ट / रेलवे स्टेशन से पिकअप',
    'Camel fair in Kartik (Oct/Nov) — hotels fill up': 'कार्तिक (अक्टूबर/नवंबर) में ऊँट मेला — होटल भर जाते हैं',
    'Park closed July–September for monsoon; safaris book out 30+ days ahead': 'मानसून में जुलाई–सितंबर पार्क बंद; सफ़ारी 30+ दिन पहले बुक हो जाती है',
    'Desert camp night at Sam is the highlight; very hot Apr–Jun': 'सम के डेज़र्ट कैंप की रात सबसे ख़ास; अप्रैल–जून बहुत गर्मी',
    'Railhead for Nainital & Kumaon (Shatabdi / Ranikhet Express)': 'नैनीताल और कुमाऊँ का रेलवे स्टेशन (शताब्दी / रानीखेत एक्सप्रेस)',
    'Usually a stop on the way to Nainital / Almora; stays are limited': 'आमतौर पर नैनीताल / अल्मोड़ा के रास्ते में रुकते हैं; ठहरने की जगहें कम हैं',
    'Camps and small lodges; heavy snow Jan–Feb, road often shut': 'कैंप और छोटे लॉज; जनवरी–फ़रवरी भारी बर्फ़, सड़क अक्सर बंद',
    'Via Joshimath; SUV advised. Snow Dec–Mar, meadows Apr–Jun': 'जोशीमठ होकर; SUV बेहतर। दिसंबर–मार्च बर्फ़, अप्रैल–जून हरे बुग्याल',
    'Road from Dalhousie can close after heavy snow (Jan–Feb)': 'भारी बर्फ़ के बाद डलहौज़ी से सड़क बंद हो सकती है (जनवरी–फ़रवरी)',
    'Usually a 1-hour stop between Palampur and Bir/Mandi': 'आमतौर पर पालमपुर और बीड़/मंडी के बीच 1 घंटे का पड़ाव',
    'Jalori Pass closes in heavy snow (Jan–Feb)': 'भारी बर्फ़ में जलोड़ी दर्रा बंद हो जाता है (जनवरी–फ़रवरी)',
    '2 h from Katra — a cool break after the Vaishno Devi trek': 'कटरा से 2 घंटे — वैष्णो देवी यात्रा के बाद ठंडी जगह पर आराम',
    '4,500 m — only after 2+ nights in Leh; Inner Line Permit': '4,500 मी — लेह में 2+ रातों के बाद ही; इनर लाइन परमिट ज़रूरी',
    'Online permit needed; closed in winter': 'ऑनलाइन परमिट ज़रूरी; सर्दियों में बंद',
    'Yatra registration (RFID card) required': 'यात्रा पंजीकरण (RFID कार्ड) ज़रूरी',
    'Char Dham registration required': 'चार धाम पंजीकरण ज़रूरी',
    'Buy tickets online; closed on Fridays': 'टिकट ऑनलाइन लें; शुक्रवार को बंद',
    'No photography inside; big crowd on 15 June bhandara': 'अंदर फ़ोटो मना है; 15 जून के भंडारे पर भारी भीड़',
    'Trek starts at dawn; temple open ~May–Nov': 'ट्रेक सुबह-सवेरे शुरू; मंदिर लगभग मई–नवंबर खुला',
    'Carry a warm layer even in summer — hill evenings are 10–15 °C cooler than the plains.': 'गर्मियों में भी एक गर्म कपड़ा साथ रखें — पहाड़ों की शाम मैदानों से 10–15 °C ठंडी होती है।',
    'Hill roads: 30–40 km/h average; keep motion-sickness tablets handy for children.': 'पहाड़ी सड़कें: औसत 30–40 किमी/घंटा; बच्चों के लिए उल्टी (मोशन-सिकनेस) की गोली साथ रखें।',
    'Sightseeing in Gulmarg, Pahalgam and Sonamarg runs on local union taxis / ponies — included in the estimate, but keep small change.': 'गुलमर्ग, पहलगाम और सोनमर्ग में घूमना लोकल यूनियन टैक्सी / घोड़ों से होता है — अनुमान में शामिल है, पर खुले पैसे साथ रखें।',
    'Book the Gulmarg Gondola online a few days ahead in peak season.': 'पीक सीज़न में गुलमर्ग गोंडोला कुछ दिन पहले ऑनलाइन बुक करें।',
    'Carry a valid photo ID; mobile prepaid SIMs from other states may not work in J&K (postpaid works).': 'वैध फ़ोटो ID साथ रखें; दूसरे राज्यों के प्रीपेड सिम J&K में शायद न चलें (पोस्टपेड चलता है)।',
    'Rest completely on day 1 in Leh (3,500 m): no sightseeing, lots of water, no alcohol. Consult your doctor about altitude medicine.': 'लेह (3,500 मी) में पहले दिन पूरा आराम करें: घूमना नहीं, खूब पानी, शराब नहीं। ऊँचाई की दवा के बारे में अपने डॉक्टर से पूछें।',
    'Inner Line Permits for Nubra, Pangong and Tso Moriri are arranged by us — carry 4 passport photos and ID copies.': 'नुब्रा, पैंगोंग और त्सो मोरीरी के इनर लाइन परमिट हम बनवाते हैं — 4 पासपोर्ट फ़ोटो और ID की कॉपी साथ रखें।',
    'Nights at Pangong / Tso Moriri drop below 0 °C even in summer; carry a down jacket.': 'पैंगोंग / त्सो मोरीरी में गर्मियों में भी रात 0 °C से नीचे जाती है; डाउन जैकेट साथ रखें।',
    'Char Dham: online yatra registration is mandatory; carry the printout and a photo ID.': 'चार धाम: ऑनलाइन यात्रा पंजीकरण अनिवार्य है; उसका प्रिंट और फ़ोटो ID साथ रखें।',
    'Kedarnath / Yamunotri treks start early morning; ponies, palki and helicopters are on request.': 'केदारनाथ / यमुनोत्री की चढ़ाई सुबह जल्दी शुरू होती है; घोड़ा, पालकी और हेलिकॉप्टर अनुरोध पर।',
    'Hill roads can close briefly after rain in July–August — keep one buffer day if possible.': 'जुलाई–अगस्त में बारिश के बाद पहाड़ी सड़कें कुछ देर बंद हो सकती हैं — हो सके तो एक दिन अतिरिक्त रखें।',
    'Temples open early (5–6 AM) and close for 1–2 hours midday; plan darshan before 11 AM.': 'मंदिर सुबह जल्दी (5–6 बजे) खुलते हैं और दोपहर में 1–2 घंटे बंद रहते हैं; दर्शन 11 बजे से पहले करें।',
    'Navratri and weekends bring long queues — carry water, and leave leather items and cameras in the car.': 'नवरात्रि और वीकेंड पर लंबी लाइनें लगती हैं — पानी साथ रखें, चमड़े का सामान और कैमरा गाड़ी में छोड़ें।',
    'Dress modestly; cover shoulders and knees at shrines.': 'मंदिरों में शालीन कपड़े पहनें; कंधे और घुटने ढके रहें।',
    'Forts and palaces open ~9 AM–5 PM; start early to beat the heat.': 'किले और महल लगभग सुबह 9 से शाम 5 बजे तक खुलते हैं; गर्मी से बचने के लिए जल्दी निकलें।',
    'October to March is the comfortable season; summer afternoons cross 40 °C — carry a cap, sunscreen and 2 litres of water per person.': 'अक्टूबर से मार्च आरामदायक मौसम है; गर्मियों की दोपहर 40 °C से ऊपर — टोपी, सनस्क्रीन और हर व्यक्ति के लिए 2 लीटर पानी रखें।',
    'Monument tickets are cheaper online; Taj Mahal is closed on Fridays.': 'स्मारकों के टिकट ऑनलाइन सस्ते मिलते हैं; ताजमहल शुक्रवार को बंद रहता है।',
    'Taj Mahal is closed on Fridays; sunrise entry has the shortest queues.': 'ताजमहल शुक्रवार को बंद रहता है; सूर्योदय के समय सबसे छोटी लाइन होती है।',
    'Mathura–Vrindavan temples close in the afternoon (approx. 12–4 PM); plan darshan morning and evening.': 'मथुरा–वृंदावन के मंदिर दोपहर (लगभग 12–4 बजे) बंद रहते हैं; दर्शन सुबह और शाम करें।',
    'Cover your head and remove shoes at gurudwaras; the langar is open to everyone.': 'गुरुद्वारे में सिर ढकें और जूते उतारें; लंगर सबके लिए खुला है।',
    'ATMs are scarce in Spiti, Kinnaur and Lahaul — carry cash; mobile network is patchy beyond Kaza.': 'स्पीति, किन्नौर और लाहौल में ATM कम हैं — नकद साथ रखें; काज़ा से आगे मोबाइल नेटवर्क कमज़ोर है।',
    'Winter trip: carry heavy woollens, gloves and waterproof shoes; snow can close high roads for a day — the driver will suggest alternatives.': 'सर्दियों की यात्रा: भारी ऊनी कपड़े, दस्ताने और वाटरप्रूफ़ जूते रखें; बर्फ़ से ऊँची सड़कें एक दिन बंद हो सकती हैं — ड्राइवर दूसरा रास्ता/जगह सुझाएगा।',
    'Monsoon season: landslides can delay hill roads; keep plans flexible and start drives early.': 'मानसून: भूस्खलन से पहाड़ी सड़कों पर देरी हो सकती है; प्लान लचीला रखें और सफ़र जल्दी शुरू करें।'
  };
  /* v1.0 (21 Oct 2026): sight names in Hindi (day plan, 'also possible', closed-sight warnings, PDF) */
  var SIGHTHI = {"Trek Chandanwari → Pissu Top → Sheshnag camp": "पैदल यात्रा: चंदनवाड़ी → पिस्सू टॉप → शेषनाग कैंप", "Trek Sheshnag → Mahagunas Pass (4,276 m) → Panchtarni camp": "पैदल यात्रा: शेषनाग → महागुनस दर्रा (4,276 मी) → पंचतरणी कैंप", "Trek Sheshnag → Mahagunas Pass": "पैदल यात्रा: शेषनाग → महागुनस दर्रा", "Shri Amarnath cave darshan (trek, pony or palki on request)": "श्री अमरनाथ गुफा दर्शन (पैदल, घोड़ा या पालकी — अनुरोध पर)", "Shri Amarnath cave darshan": "श्री अमरनाथ गुफा दर्शन", "300 km Himalayan panorama — Trishul, Nanda Devi": "300 किमी हिमालय नज़ारा — त्रिशूल, नंदा देवी", "Achalgarh": "अचलगढ़", "Agra Fort": "आगरा किला", "Ajmer Sharif Dargah": "अजमेर शरीफ़ दरगाह", "Akshardham": "अक्षरधाम", "Alchi Monastery": "अल्ची मठ", "Amber Fort & Jal Mahal": "आमेर किला और जल महल", "Anandpur Sahib Gurudwara": "आनंदपुर साहिब गुरुद्वारा", "Anasakti (Gandhi) Ashram": "अनासक्ति (गांधी) आश्रम", "Andretta artists' village": "अंद्रेटा कलाकार गाँव", "Apple orchards of Thanedhar": "ठानेधार के सेब बागान", "Aru, Betaab & Chandanwari valleys (local union taxi)": "अरु, बेताब और चंदनवाड़ी घाटियाँ (लोकल यूनियन टैक्सी)", "Atal Tunnel & Sissu": "अटल टनल और सिस्सू", "Auli (ropeway / road)": "औली (रोपवे / सड़क)", "Auli ropeway & Gorson Bugyal": "औली रोपवे और गोरसों बुग्याल", "Badrinath Dham darshan & Tapt Kund": "बद्रीनाथ धाम दर्शन और तप्त कुंड", "Badrinath day trip (May–Oct)": "बद्रीनाथ एक दिन की यात्रा (मई–अक्टूबर)", "Baijnath Shiva Temple (1204 AD)": "बैजनाथ शिव मंदिर (1204 ई.)", "Baijnath Temple": "बैजनाथ मंदिर", "Baijnath Temple, Garur": "बैजनाथ मंदिर, गरुड़", "Baisaran meadow (pony)": "बैसरन घास का मैदान (घोड़ा)", "Banke Bihari & Prem Mandir, Vrindavan": "बाँके बिहारी और प्रेम मंदिर, वृंदावन", "Barsana & Nandgaon": "बरसाना और नंदगाँव", "Baspa river walk": "बस्पा नदी किनारे सैर", "Baspa riverside & Mathi temple": "बस्पा नदी किनारा और माथी मंदिर", "Bhaga riverside": "भागा नदी किनारा", "Bhagsu Nag & waterfall": "भागसू नाग और झरना", "Bhimakali Temple": "भीमाकाली मंदिर", "Bhimtal Lake & island aquarium": "भीमताल झील और टापू एक्वेरियम", "Bhimtal, Sattal & Naukuchiatal": "भीमताल, सातताल और नौकुचियाताल", "Bhootnath & Panchvaktra temples": "भूतनाथ और पंचवक्त्र मंदिर", "Bhuri Singh Museum": "भूरी सिंह संग्रहालय", "Bijli Mahadev": "बिजली महादेव", "Binsar Wildlife Sanctuary & Zero Point": "बिनसर वन्यजीव अभयारण्य और ज़ीरो पॉइंट", "Bir Tibetan colony": "बीर तिब्बती कॉलोनी", "Birla Mandir & Albert Hall": "बिड़ला मंदिर और अल्बर्ट हॉल", "Blue City walk & Clock Tower market": "ब्लू सिटी सैर और घंटाघर बाज़ार", "Brahma Temple & Pushkar Lake ghats": "ब्रह्मा मंदिर और पुष्कर झील घाट", "Camel Research Centre": "ऊँट अनुसंधान केंद्र", "Camp evening": "कैंप में शाम", "Camp stay on the Manali–Leh highway": "मनाली–लेह हाईवे पर कैंप में ठहराव", "Chail Palace": "चायल पैलेस", "Chalal walk": "छलाल तक सैर", "Chamunda & Lakshmi Narayan temples": "चामुंडा और लक्ष्मी नारायण मंदिर", "Chamunda Nandikeshwar Dham darshan": "चामुंडा नंदिकेश्वर धाम दर्शन", "Chandratal Lake walk": "चंद्रताल झील सैर", "Chehni Kothi": "चेहनी कोठी", "Chitai Golu Devta": "चितई गोलू देवता", "Chitkul — last village": "चितकुल — आख़िरी गाँव", "Chittorgarh Fort": "चित्तौड़गढ़ किला", "Chokhi Dhani evening": "चोखी ढाणी में शाम", "City Palace & Lake Pichola boat ride": "सिटी पैलेस और पिछोला झील में नाव की सैर", "Dainkund Peak": "डैनकुंड चोटी", "Dal Lake shikara ride": "डल झील शिकारा सैर", "Dalai Lama Temple, McLeodganj": "दलाई लामा मंदिर, मैक्लोडगंज", "Deoria Tal": "देवरिया ताल", "Dhanaulti": "धनौल्टी", "Dhankar Monastery": "धनकर मठ", "Dhankar Monastery & lake": "धनकर मठ और झील", "Dilwara Jain Temples": "दिलवाड़ा जैन मंदिर", "Diskit Monastery": "दिस्कित मठ", "Doodhpathri": "दूधपथरी", "Eco Park & Surkanda Devi (ropeway)": "इको पार्क और सुरकंडा देवी (रोपवे)", "Eklingji & Nathdwara (Shrinathji)": "एकलिंगजी और नाथद्वारा (श्रीनाथजी)", "Fatehpur Sikri": "फ़तेहपुर सीकरी", "Fotu La view": "फ़ोतू ला नज़ारा", "Fruit orchards & Bhalu Gaad waterfall": "फलों के बागान और भालू गाड़ झरना", "Gadisar Lake sunrise": "गड़ीसर झील पर सूर्योदय", "Gangotri Dham": "गंगोत्री धाम", "Garjiya Devi Temple": "गर्जिया देवी मंदिर", "Gobind Sagar Lake view": "गोबिंद सागर झील नज़ारा", "Golden Fort & Patwon ki Haveli": "सोनार किला और पटवों की हवेली", "Golden Temple": "स्वर्ण मंदिर", "Golf course & KRC Museum": "गोल्फ़ कोर्स और KRC संग्रहालय", "Gorakh Dibbi": "गोरख डिब्बी", "Govardhan parikrama (21 km, optional)": "गोवर्धन परिक्रमा (21 किमी, वैकल्पिक)", "Great Himalayan National Park gate": "ग्रेट हिमालयन नेशनल पार्क गेट", "Gulmarg Gondola (book online)": "गुलमर्ग गोंडोला (ऑनलाइन बुक करें)", "Guru Shikhar": "गुरु शिखर", "HPCA Stadium": "HPCA स्टेडियम", "Hadimba Temple & Old Manali": "हिडिंबा मंदिर और ओल्ड मनाली", "Hall of Fame & Magnetic Hill": "हॉल ऑफ़ फ़ेम और मैग्नेटिक हिल", "Har Ki Pauri Ganga Aarti": "हर की पौड़ी गंगा आरती", "Hatu Peak & temple": "हाटू पीक और मंदिर", "Hawa Mahal, City Palace & Jantar Mantar": "हवा महल, सिटी पैलेस और जंतर मंतर", "Himalayan sunrise view": "हिमालय पर सूर्योदय का नज़ारा", "Hunder sand dunes & Bactrian camels": "हुंडर रेत के टीले और दो कूबड़ वाले ऊँट", "ISKCON Vrindavan": "इस्कॉन वृंदावन", "India Gate & Kartavya Path": "इंडिया गेट और कर्तव्य पथ", "Itimad-ud-Daulah (Baby Taj)": "एतमाद-उद-दौला (बेबी ताज)", "Jagdish Temple & Bagore ki Haveli dance show": "जगदीश मंदिर और बागोर की हवेली नृत्य शो", "Jageshwar Dham (124 temples)": "जागेश्वर धाम (124 मंदिर)", "Jakhu Temple": "जाखू मंदिर", "Jallianwala Bagh": "जलियाँवाला बाग़", "Jalori Pass & Serolsar Lake": "जलोड़ी पास और सेरोलसर झील", "Jalori Pass & Serolsar Lake (5 km walk)": "जलोड़ी पास और सेरोलसर झील (5 किमी पैदल)", "Jhula Devi Temple & Chaubatia Gardens": "झूला देवी मंदिर और चौबटिया गार्डन", "Jibhi waterfall": "जीभी झरना", "Joshimath Narsingh Temple": "जोशीमठ नरसिंह मंदिर", "Junagarh Fort": "जूनागढ़ किला", "Jungle safari — Bijrani / Jhirna / Dhikala (book online)": "जंगल सफ़ारी — बिजरानी / झिरना / ढिकाला (ऑनलाइन बुक करें)", "Jungle safari — morning / afternoon (book online, Get Quote)": "जंगल सफ़ारी — सुबह / दोपहर (ऑनलाइन बुक करें, कोटेशन लें)", "Jwalamukhi Devi darshan (eternal flames)": "ज्वालामुखी देवी दर्शन (अखंड ज्योति)", "Kainchi Dham (Neem Karoli Baba)": "कैंची धाम (नीम करोली बाबा)", "Kalatop Wildlife Sanctuary": "कालाटोप वन्यजीव अभयारण्य", "Kali Ka Tibba": "काली का टिब्बा", "Kamru Fort": "कामरू किला", "Kangra Fort": "कांगड़ा किला", "Kargil War Memorial, Drass": "कारगिल युद्ध स्मारक, द्रास", "Karni Mata Temple, Deshnok": "करणी माता मंदिर, देशनोक", "Kasar Devi Temple": "कसार देवी मंदिर", "Kashi Vishwanath, Uttarkashi": "काशी विश्वनाथ, उत्तरकाशी", "Kedarnath Dham (16 km trek from Gaurikund / helicopter)": "केदारनाथ धाम (गौरीकुंड से 16 किमी ट्रेक / हेलिकॉप्टर)", "Kempty Falls": "केम्प्टी फ़ॉल्स", "Key Monastery & Kibber": "की मठ और किब्बर", "Keylong & Kardang Monastery": "केलांग और कारदंग मठ", "Khajjiar meadow & lake — Mini Switzerland": "खज्जियार मैदान और झील — मिनी स्विट्ज़रलैंड", "Khajjiar — Mini Switzerland": "खज्जियार — मिनी स्विट्ज़रलैंड", "Khilanmarg walk": "खिलनमर्ग सैर", "Kinner Kailash sunrise view": "किन्नर कैलाश पर सूर्योदय का नज़ारा", "Kufri & Fagu snow point": "कुफ़री और फागू स्नो पॉइंट", "Kuldhara & Longewala war memorial": "कुलधरा और लोंगेवाला युद्ध स्मारक", "Kullu shawl factories": "कुल्लू शॉल फ़ैक्ट्रियाँ", "Kumbhalgarh Fort — 36 km wall": "कुंभलगढ़ किला — 36 किमी दीवार", "Lamayuru Monastery & moonland": "लामायुरु मठ और मूनलैंड", "Landour & Char Dukan": "लंढौर और चार दुकान", "Langza, Hikkim & Komic": "लांगज़ा, हिक्किम और कॉमिक", "Lohardi & Rajgundha": "लोहारडी और राजगुंधा", "Maa Brajeshwari Devi darshan": "माँ बज्रेश्वरी देवी दर्शन", "Maa Chintpurni darshan": "माँ चिंतपूर्णी दर्शन", "Majkhali view point": "मजखाली व्यू पॉइंट", "Mall Road & Christ Church": "मॉल रोड और क्राइस्ट चर्च", "Mall Road & Gun Hill": "मॉल रोड और गन हिल", "Mall Road, Ridge & Christ Church": "मॉल रोड, रिज और क्राइस्ट चर्च", "Mana — first Indian village": "माणा — भारत का पहला गाँव", "Manikaran Sahib & hot springs": "मणिकरण साहिब और गर्म पानी के कुंड", "Mansa Devi & Chandi Devi (ropeway)": "मनसा देवी और चंडी देवी (रोपवे)", "Mansa Devi Temple, Panchkula": "मनसा देवी मंदिर, पंचकूला", "Mashobra & Naldehra": "मशोबरा और नालदेहरा", "Masroor rock-cut temples": "मसरूर रॉक-कट मंदिर", "Mata Vaishno Devi Bhawan (13 km trek / helicopter)": "माता वैष्णो देवी भवन (13 किमी ट्रेक / हेलिकॉप्टर)", "Mehrangarh Fort & Jaswant Thada": "मेहरानगढ़ किला और जसवंत थड़ा", "Mehtab Bagh sunset view": "मेहताब बाग़ से सूर्यास्त", "Monkey Point": "मंकी पॉइंट", "Mughal Gardens — Nishat, Shalimar, Chashme Shahi": "मुग़ल गार्डन — निशात, शालीमार, चश्मे शाही", "Mukteshwar Mahadev & Chauli ki Jali": "मुक्तेश्वर महादेव और चौली की जाली", "Naag Mandir & pine walks": "नाग मंदिर और चीड़ के जंगल में सैर", "Naddi & Dal Lake": "नड्डी और डल झील", "Naggar Castle": "नग्गर कैसल", "Nahargarh sunset": "नाहरगढ़ से सूर्यास्त", "Naina Devi (Rewalsar) & seven lakes": "नैना देवी (रिवालसर) और सात झीलें", "Naina Devi (ropeway)": "नैना देवी (रोपवे)", "Naini Lake boating & Mall Road": "नैनी झील में नौका विहार और मॉल रोड", "Nakki Lake & Sunset Point": "नक्की झील और सनसेट पॉइंट", "Nako Lake & monastery": "नाको झील और मठ", "Nargu Wildlife Sanctuary walk": "नरगू वन्यजीव अभयारण्य सैर", "Nathatop & Sanasar meadow (paragliding, Get Quote)": "नत्थाटॉप और सनासर मैदान (पैराग्लाइडिंग, कोटेशन लें)", "Naukuchiatal": "नौकुचियाताल", "Neelkanth Mahadev": "नीलकंठ महादेव", "Neem Karoli Baba ashram darshan": "नीम करोली बाबा आश्रम दर्शन", "Osian temples": "ओसियाँ मंदिर", "Panchpula": "पंचपुला", "Pangong lakeside sunrise": "पैंगोंग झील किनारे सूर्योदय", "Paragliding from Billing (Get Quote)": "बिलिंग से पैराग्लाइडिंग (कोटेशन लें)", "Patnitop skyview gondola": "पटनीटॉप स्काईव्यू गोंडोला", "Pin Valley & Mud": "पिन घाटी और मुद", "Prashar Lake": "पराशर झील", "Puga hot springs & Tso Kar": "पूगा गर्म कुंड और सो कार", "Qutub Minar": "क़ुतुब मीनार", "Raghunath Temple": "रघुनाथ मंदिर", "Raghupur Fort meadow": "रघुपुर किला मैदान", "Ram Jhula, Laxman Jhula & Beatles Ashram": "राम झूला, लक्ष्मण झूला और बीटल्स आश्रम", "Ranakpur Jain Temple": "रणकपुर जैन मंदिर", "Ranthambore Fort & Trinetra Ganesh": "रणथंभौर किला और त्रिनेत्र गणेश", "Reckong Peo market": "रिकांग पिओ बाज़ार", "Rewalsar Lake": "रिवालसर झील", "Rewalsar Lake — Padmasambhava statue, gurudwara & temples": "रिवालसर झील — पद्मसंभव प्रतिमा, गुरुद्वारा और मंदिर", "River rafting at Babeli/Pirdi": "बबेली/पिरडी पर रिवर राफ़्टिंग", "River rafting at Shivpuri (Get Quote)": "शिवपुरी पर रिवर राफ़्टिंग (कोटेशन लें)", "Robber's Cave": "रॉबर्स केव (गुच्चूपानी)", "Rock Garden": "रॉक गार्डन", "Roghi village & Suicide Point": "रोघी गाँव और सुसाइड पॉइंट", "Rohtang Pass (permit, May–Nov)": "रोहतांग पास (परमिट, मई–नवंबर)", "Sahastradhara": "सहस्त्रधारा", "Sajjangarh (Monsoon Palace) sunset": "सज्जनगढ़ (मानसून पैलेस) से सूर्यास्त", "Sam sand dunes — camel ride & desert camp": "सम रेत के टीले — ऊँट सवारी और डेज़र्ट कैंप", "Sangam — Indus & Zanskar": "संगम — सिंधु और ज़ांस्कर", "Sattal birding & boating": "सातताल पक्षी दर्शन और नौका विहार", "Savitri Mata ropeway": "सावित्री माता रोपवे", "Shankaracharya Temple": "शंकराचार्य मंदिर", "Shanti Stupa & Leh Palace": "शांति स्तूप और लेह पैलेस", "Shiv Khori": "शिव खोड़ी", "Shri Krishna Janmabhoomi darshan": "श्री कृष्ण जन्मभूमि दर्शन", "Shri Naina Devi Ji darshan (ropeway)": "श्री नैना देवी जी दर्शन (रोपवे)", "Sissu waterfall & lake": "सिस्सू झरना और झील", "Skiing / snow play Jan–Mar (Get Quote)": "स्कीइंग / बर्फ़ में खेल जनवरी–मार्च (कोटेशन लें)", "Solang Valley": "सोलंग घाटी", "St John's Church": "सेंट जॉन चर्च", "St Mary's Church & War Memorial": "सेंट मैरी चर्च और युद्ध स्मारक", "Strawberry valley": "स्ट्रॉबेरी घाटी", "Sukhna Lake": "सुखना झील", "Sunset Point": "सनसेट पॉइंट", "Tabo Monastery (996 AD)": "ताबो मठ (996 ई.)", "Taj Mahal at sunrise (closed Fridays)": "सूर्योदय पर ताज महल (शुक्रवार बंद)", "Takht Sri Kesgarh Sahib": "तख़्त श्री केसगढ़ साहिब", "Tarkeshwar Mahadev": "ताड़केश्वर महादेव", "Tea estate": "चाय बागान", "Tea gardens": "चाय के बागान", "Tehri Lake water sports (Get Quote)": "टिहरी झील वॉटर स्पोर्ट्स (कोटेशन लें)", "Thajiwas Glacier (pony)": "थाजिवास ग्लेशियर (घोड़ा)", "Thiksey, Shey & Hemis monasteries": "थिकसे, शे और हेमिस मठ", "Tibetan colony & monasteries": "तिब्बती कॉलोनी और मठ", "Tip-n-Top & Bhulla Tal": "टिप-एन-टॉप और भुल्ला ताल", "Tosh & Kalga villages": "तोष और कलगा गाँव", "Triund trek (Get Quote)": "त्रिउंड ट्रेक (कोटेशन लें)", "Triveni Ghat aarti": "त्रिवेणी घाट आरती", "Trout farms & river walk": "ट्राउट फ़ार्म और नदी किनारे सैर", "Tso Moriri lakeside & Korzok Monastery": "सो मोरीरी झील किनारा और कोरज़ोक मठ", "Tungnath Temple & Chandrashila trek (4 km, 3,680 m)": "तुंगनाथ मंदिर और चंद्रशिला ट्रेक (4 किमी, 3,680 मी)", "Turtuk village": "तुरतुक गाँव", "Uhl river & trout fishing": "ऊहल नदी और ट्राउट फ़िशिंग", "Ukhimath Omkareshwar": "ऊखीमठ ओंकारेश्वर", "Umaid Bhawan Palace museum": "उम्मेद भवन पैलेस संग्रहालय", "Vashisht hot springs": "वशिष्ठ गर्म कुंड", "Viceregal Lodge": "वाइसरीगल लॉज", "Virasat-e-Khalsa museum (closed Mondays)": "विरासत-ए-ख़ालसा संग्रहालय (सोमवार बंद)", "Wagah Border ceremony": "वाघा बॉर्डर समारोह", "Waterfall point": "वॉटरफ़ॉल पॉइंट", "World's highest cricket ground": "दुनिया का सबसे ऊँचा क्रिकेट मैदान", "Yamunotri Dham (6 km trek from Janki Chatti)": "यमुनोत्री धाम (जानकी चट्टी से 6 किमी ट्रेक)", "Yusmarg": "यूसमर्ग", "Zero Point, Zojila (local taxi)": "ज़ीरो पॉइंट, ज़ोजिला (लोकल टैक्सी)", "Zorbing & horse ride (Get Quote)": "ज़ॉर्बिंग और घुड़सवारी (कोटेशन लें)", "Free day — relax, cafés, local markets": "खाली दिन — आराम, कैफ़े, लोकल बाज़ार", "Aru, Betaab & Chandanwari valleys": "अरु, बेताब और चंदनवाड़ी घाटियाँ", "Auli": "औली", "Badrinath day trip": "बद्रीनाथ एक दिन की यात्रा", "Baijnath Shiva Temple": "बैजनाथ शिव मंदिर", "Baisaran meadow": "बैसरन घास का मैदान", "Eco Park & Surkanda Devi": "इको पार्क और सुरकंडा देवी", "Eklingji & Nathdwara": "एकलिंगजी और नाथद्वारा", "Govardhan parikrama": "गोवर्धन परिक्रमा", "Gulmarg Gondola": "गुलमर्ग गोंडोला", "Itimad-ud-Daulah": "एतमाद-उद-दौला", "Jageshwar Dham": "जागेश्वर धाम", "Jungle safari — Bijrani / Jhirna / Dhikala": "जंगल सफ़ारी — बिजरानी / झिरना / ढिकाला", "Jungle safari — morning / afternoon": "जंगल सफ़ारी — सुबह / दोपहर", "Jwalamukhi Devi darshan": "ज्वालामुखी देवी दर्शन", "Kainchi Dham": "कैंची धाम", "Kedarnath Dham": "केदारनाथ धाम", "Mansa Devi & Chandi Devi": "मनसा देवी और चंडी देवी", "Mata Vaishno Devi Bhawan": "माता वैष्णो देवी भवन", "Naina Devi": "नैना देवी", "Nathatop & Sanasar meadow": "नत्थाटॉप और सनासर मैदान", "Paragliding from Billing": "बिलिंग से पैराग्लाइडिंग", "River rafting at Shivpuri": "शिवपुरी पर रिवर राफ़्टिंग", "Rohtang Pass": "रोहतांग पास", "Shri Naina Devi Ji darshan": "श्री नैना देवी जी दर्शन", "Skiing / snow play Jan–Mar": "स्कीइंग / बर्फ़ में खेल जनवरी–मार्च", "Tabo Monastery": "ताबो मठ", "Taj Mahal at sunrise": "सूर्योदय पर ताज महल", "Tehri Lake water sports": "टिहरी झील वॉटर स्पोर्ट्स", "Thajiwas Glacier": "थाजिवास ग्लेशियर", "Triund trek": "त्रिउंड ट्रेक", "Tungnath Temple & Chandrashila trek": "तुंगनाथ मंदिर और चंद्रशिला ट्रेक", "Virasat-e-Khalsa museum": "विरासत-ए-ख़ालसा संग्रहालय", "Yamunotri Dham": "यमुनोत्री धाम", "Zero Point, Zojila": "ज़ीरो पॉइंट, ज़ोजिला", "Zorbing & horse ride": "ज़ॉर्बिंग और घुड़सवारी", "Anasakti": "अनासक्ति", "Sajjangarh": "सज्जनगढ़"};
  var SKEYS = Object.keys(SIGHTHI).sort(function (a, b) { return b.length - a.length; });
  function sn(s) { return SIGHTHI[s] || s; }
  function snAll(s) { var tok = []; SKEYS.forEach(function (k) { if (s.indexOf(k) > -1) { s = s.split(k).join('\u0001' + tok.length + '\u0002'); tok.push(SIGHTHI[k]); } }); return s.replace(/\u0001(\d+)\u0002/g, function (x, i) { return tok[+i]; }); }
  function sightEX() { Object.keys(SIGHTHI).forEach(function (k) { if (EX[k] == null && !PN[k]) EX[k] = SIGHTHI[k]; }); }
  function tipT(s) { var d = /\.$/.test(s) && !TIPHI[s] ? '.' : '', k = d ? s.slice(0, -1) : s; return TIPHI[k] ? TIPHI[k] + (d ? '।' : '') : s; }
  Object.keys(TIPHI).forEach(function (k) { if (EX[k] == null) EX[k] = TIPHI[k]; if (!/\.$/.test(k) && EX[k + '.'] == null) EX[k + '.'] = TIPHI[k] + '।'; });
  function cat(s) { return EX[s] || s; }
  function tier(s) { return EX[s] || EX[s.split(' (')[0]] && (EX[s.split(' (')[0]] + s.slice(s.split(' (')[0].length)) || s; }
  function noDot(s) { return s.replace(/\.$/, ''); }

  /* pattern rules: [regex, fn(match) -> hindi] — tried in order after the exact dictionary */
  var RX = [
    [/^(.+) is closed on (\w+)s and your (.+) day falls on a \w+, so it is left out of your day plan — shift your dates by a day to include it\.$/, function (m) { var D = { Sunday: 'रविवार', Monday: 'सोमवार', Tuesday: 'मंगलवार', Wednesday: 'बुधवार', Thursday: 'गुरुवार', Friday: 'शुक्रवार', Saturday: 'शनिवार' }[m[2]] || m[2]; return sn(m[1]) + ' ' + D + ' को बंद रहता है और आपका ' + pn(m[3]) + ' वाला दिन ' + D + ' है, इसलिए इसे प्लान से हटाया गया है — इसे शामिल करने के लिए तारीख़ एक दिन आगे-पीछे करें।'; }],
    [/^Fits your budget: (.+?) hotels, (breakfast \+ dinner|breakfast only) — about (₹[\d,]+) per adult\.$/, function (m) { return 'आपके बजट में: ' + (EX[m[1]] || m[1]) + ' होटल, ' + (m[2] === 'breakfast only' ? 'सिर्फ़ नाश्ता' : 'नाश्ता + रात का खाना') + ' — लगभग ' + m[3] + ' प्रति वयस्क।'; }],
    [/^Car changed to (.+) \(right size for your group\) to bring the price down\.$/, function (m) { return 'कीमत कम करने के लिए गाड़ी बदलकर ' + (EX[m[1]] || m[1]) + ' की गई (आपके ग्रुप के हिसाब से सही साइज़)।'; }],
    [/^Lowest estimate for this route is about (₹[\d,]+) per adult \((.+?), (breakfast \+ dinner|breakfast only)\)\. .+$/, function (m) { return 'इस रूट का सबसे कम अनुमान लगभग ' + m[1] + ' प्रति वयस्क है (' + (EX[m[2]] || m[2]) + ', ' + (m[3] === 'breakfast only' ? 'सिर्फ़ नाश्ता' : 'नाश्ता + रात का खाना') + ')। कम रातें, छोटा रूट या ज़्यादा लोग एक गाड़ी में — इससे कीमत घटती है। या हमसे पूछें, टीम अक्सर इससे कम में कर देती है।'; }],
    [/^([+✓]) (.+)$/, function (m) { var x = EX[m[2]] || pn(m[2]); return x === m[2] ? null : m[1] + ' ' + x; }],
    [/^(\d+) Adults?$/, function (m) { return m[1] + ' वयस्क'; }],
    [/^(\d+) nights?$/, function (m) { return m[1] + ' रात'; }],
    [/^(\d+) rooms?$/, function (m) { return m[1] + ' कमरा'; }],
    [/^(\d+) rooms? \+ (\d+) extra bed$/, function (m) { return m[1] + ' कमरा + ' + m[2] + ' एक्स्ट्रा बेड'; }],
    [/^(\d+) seats$/, function (m) { return m[1] + ' सीट'; }],
    [/^(\d+)D\/(\d+)N$/, function (m) { return m[1] + ' दिन/' + m[2] + ' रात'; }],
    [/^est\. (₹[\d,]+)$/, function (m) { return 'लगभग ' + m[1]; }],
    [/^Near (.+):$/, function (m) { return pn(m[1]) + ' के पास:'; }],
    [/^(\d+) days \/ (\d+) nights$/, function (m) { return m[1] + ' दिन / ' + m[2] + ' रात'; }],
    [/^(.+) — (\d+) Days \/ (\d+) Nights$/, function (m) { return pnAny(m[1]) + ' — ' + m[2] + ' दिन / ' + m[3] + ' रात'; }],
    [/^🛣 ([\d,]+) km road trip$/, function (m) { return '🛣 ' + m[1] + ' किमी सड़क यात्रा'; }],
    [/^🌙 (\d+) nights?$/, function (m) { return '🌙 ' + m[1] + ' रात'; }],
    [/^🛣 (.+)$/, function (m) { return '🛣 ' + hrs(m[1]); }],
    [/^~?[\d,.]+ (km|h|min)$/, function (m) { return hrs(m[0]); }],
    [/^~([\d,]+) km$/, function (m) { return '~' + m[1] + ' किमी'; }],
    [/^🏨 Night in (Sheshnag|Panchtarni) camp( \(rest day\))?$/, function (m) { return '🏨 ' + (m[1] === 'Sheshnag' ? 'शेषनाग' : 'पंचतरणी') + ' कैंप में रात' + (m[2] ? ' (आराम का दिन)' : ''); }],
    [/^🚗 car (.+)$/, function (m) { return '🚗 गाड़ी ' + hrs(m[1]); }],
    [/^Panchtarni → Amarnath cave → (.+)$/, function (m) { return 'पंचतरणी → अमरनाथ गुफा → ' + pn(m[1]); }],
    [/^🛕 Start before dawn: trek Panchtarni → Shri Amarnath cave \(about 6 km\) for darshan, then walk down to (.+) \(about 14 km\)\.$/, function (m) { return '🛕 भोर से पहले निकलें: पंचतरणी → श्री अमरनाथ गुफा (लगभग 6 किमी) पैदल, दर्शन के बाद ' + pn(m[1]) + ' तक उतराई (लगभग 14 किमी)।'; }],
    [/^Your car goes round by road via Srinagar and meets you at (.+)\.$/, function (m) { return 'आपकी गाड़ी सड़क से श्रीनगर होकर ' + pn(m[1]) + ' पहुँचकर आपसे मिलेगी।'; }],
    [/^Pahalgam route: keep 2 nights on the trail — Sheshnag camp, then Panchtarni camp over Mahagunas Pass \(4,276 m\) — before the cave darshan\. You have (\d+) nights? here\.$/, function (m) { return 'पहलगाम रूट: गुफा दर्शन से पहले रास्ते में 2 रातें रखें — शेषनाग कैंप, फिर महागुनस दर्रा (4,276 मी) पार करके पंचतरणी कैंप। आपकी यहाँ ' + m[1] + ' रात है।'; }],
    [/^After the darshan, Pahalgam-route yatris walk down to Baltal — keep Baltal as the next stop so your car can meet you there\.$/, function () { return 'दर्शन के बाद पहलगाम रूट के यात्री बालटाल उतरते हैं — अगला पड़ाव बालटाल रखें ताकि आपकी गाड़ी वहाँ आपसे मिल सके।'; }],
    [/^🏨 Night in (.+)$/, function (m) { return '🏨 ' + pn(m[1]) + ' में रात'; }],
    [/^Day (\d+)$/, function (m) { return 'दिन ' + m[1]; }],
    [/^Day (\d+): (.+) → (.+) is a long drive \((.+)\)\. Consider a night halt on the way\.$/, function (m) { return 'दिन ' + m[1] + ': ' + pn(m[2]) + ' → ' + pn(m[3]) + ' लंबा सफ़र है (' + hrs(m[4]) + ')। रास्ते में एक रात रुकने पर विचार करें।'; }],
    [/^Last day: (.+) → (.+) is a long drive \((.+)\)\. Many guests add a night on the way\.$/, function (m) { return 'आख़िरी दिन: ' + pn(m[1]) + ' → ' + pn(m[2]) + ' लंबा सफ़र है (' + hrs(m[3]) + ')। कई मेहमान रास्ते में एक रात जोड़ते हैं।'; }],
    [/^Peak-season hotel rates applied for (\d+) nights? \(mid-Mar–Jun, October, Christmas–New Year\)\.$/, function (m) { return m[1] + ' रातों के लिए पीक-सीज़न होटल रेट लगाए गए हैं (मध्य मार्च–जून, अक्टूबर, क्रिसमस–नया साल)।'; }],
    [/^Amarnath Yatra: every yatri needs a Shri Amarnathji Shrine Board yatra permit for the route \(Baltal or Pahalgam\) and date \(advance registration with Aadhaar\), a Compulsory Health Certificate from an authorised doctor, and must be 13–70 years old \(no pregnancy beyond 6 weeks\)\. The yatra runs only in its July–August window — 2027 dates are not announced yet\. Helicopter is not assured; pony and palki are on request\.$/, function () { return 'अमरनाथ यात्रा: हर यात्री को रूट (बालटाल या पहलगाम) और तारीख़ के लिए श्री अमरनाथजी श्राइन बोर्ड का यात्रा परमिट (आधार से अग्रिम पंजीकरण), अधिकृत डॉक्टर का अनिवार्य स्वास्थ्य प्रमाणपत्र चाहिए, और उम्र 13–70 वर्ष होनी चाहिए (6 सप्ताह से अधिक की गर्भावस्था में नहीं)। यात्रा केवल जुलाई–अगस्त में चलती है — 2027 की तारीख़ें अभी घोषित नहीं हुई हैं। हेलिकॉप्टर तय नहीं है; घोड़ा और पालकी अनुरोध पर।'; }],
    [/^Keep 2 nights at (.+): arrive the day before, then a full day for the cave darshan \(about 14 km steep trek each way\)\. You have (\d+) nights? here\.$/, function (m) { return pn(m[1]) + ' में 2 रातें रखें: एक दिन पहले पहुँचें, फिर गुफा दर्शन के लिए पूरा एक दिन (हर तरफ़ लगभग 14 किमी की खड़ी चढ़ाई)। आपकी यहाँ ' + m[2] + ' रात है।'; }],
    [/^Kedarnath needs 2 nights at (.+) \(trek up, darshan, trek down — or helicopter, subject to tickets\)\. You have (\d+) nights? here; add a night for a relaxed darshan\.$/, function (m) { return 'केदारनाथ के लिए ' + pn(m[1]) + ' में 2 रातें चाहिए (चढ़ाई, दर्शन, उतराई — या हेलिकॉप्टर, टिकट मिलने पर)। आपकी यहाँ ' + m[2] + ' रात है; आराम से दर्शन के लिए एक रात जोड़ें।'; }],
    [/^Spiti, Lahaul, Chitkul and Ladakh roads need an SUV \(Innova Crysta or bigger\)\. Your estimate uses (.+) — our team will suggest the right car\.$/, function (m) { return 'स्पीति, लाहौल, चितकुल और लद्दाख की सड़कों के लिए SUV (इनोवा क्रिस्टा या बड़ी) चाहिए। आपके अनुमान में ' + m[1] + ' है — हमारी टीम सही गाड़ी बताएगी।'; }],
    [/^(.+) is usually closed \/ snowbound in (\w+) \(open about (\w+)–(\w+)\)\. Pick other dates or swap this stop\.$/, function (m) { return pn(m[1]) + ' ' + dt(m[2]) + ' में आम तौर पर बंद / बर्फ़ से ढका रहता है (लगभग ' + dt(m[3]) + '–' + dt(m[4]) + ' खुला)। दूसरी तारीख चुनें या यह जगह बदलें।'; }],
    [/^(.+) is usually closed in (\w+) \(open about (\w+)–(\w+)\), so it is left out of your day plan\.(.*)$/, function (m) { return sn(m[1]) + ' ' + dt(m[2]) + ' में आम तौर पर बंद रहता है (लगभग ' + dt(m[3]) + '–' + dt(m[4]) + ' खुला), इसलिए इसे आपके प्लान से हटाया गया है।' + (/Solang/.test(m[5]) ? ' सर्दियों में बर्फ़ का मज़ा सोलंग वैली में; सड़क खुली हो तो अटल टनल और सिस्सू।' : m[5]); }],
    [/^Your (.+) darshan falls in (.+?) \((.+?)\): very big crowds, long darshan queues and hotels fill early\. We plan darshan for early morning and keep extra time on these days\.(.*)$/, function (m) { var rest = m[4].trim().replace(/[^.]+\./g, function (x) { x = x.trim(); return (EX[x] || x) + ' '; }).trim(); return 'आपका ' + pn(m[1]) + ' दर्शन ' + m[2].replace('Chaitra Navratri', 'चैत्र नवरात्रि').replace('Sharad Navratri', 'शारदीय नवरात्रि') + ' (' + dt(m[3]) + ') में पड़ रहा है: बहुत भीड़, दर्शन की लंबी लाइनें और होटल जल्दी भर जाते हैं। इन दिनों हम दर्शन सुबह जल्दी रखते हैं और ज़्यादा समय रखते हैं।' + (rest ? ' ' + rest : ''); }],
    [/^Pickup in (.+?)( \((.+)\))?, then drive to (.+)\.$/, function (m) { return pn(m[1]) + ' से पिकअप' + (m[3] ? ' (' + tipT(m[3]) + ')' : '') + ', फिर ' + pn(m[4]) + ' के लिए रवाना।'; }],
    [/^After breakfast, drive to (.+)\.$/, function (m) { return 'नाश्ते के बाद ' + pn(m[1]) + ' के लिए रवाना।'; }],
    [/^🛕 Darshan at (.+?)( — (.+))? on the way\.$/, function (m) { return '🛕 रास्ते में ' + pn(m[1]) + ' दर्शन' + (m[3] ? ' — ' + sn(m[3]) : '') + '।'; }],
    [/^Stop at (.+?)( — (.+))? on the way\.$/, function (m) { return 'रास्ते में ' + pn(m[1]) + ' पर रुकें' + (m[3] ? ' — ' + sn(m[3]) : '') + '।'; }],
    [/^(Evening: )?(.+)\.$/, function (m) { return SIGHTHI[m[2]] ? (m[1] ? 'शाम: ' : '') + SIGHTHI[m[2]] + '।' : null; }],
    [/^(Evening: )?(.+) \(([^()]+)\)\.$/, function (m) { return TIPHI[m[3]] || SIGHTHI[m[2]] ? (m[1] ? 'शाम: ' : '') + sn(m[2]) + ' (' + (TIPHI[m[3]] || m[3]) + ')।' : null; }],
    [/^([^:]+):$/, function (m) { return PN[m[1]] ? PN[m[1]] + ':' : null; }],
    [/^Evening: (.+)$/, function (m) { return 'शाम: ' + snAll(m[1]); }],
    [/^Tip: (.+)$/, function (m) { return 'सुझाव: ' + tipT(m[1]); }],
    [/^Also possible: (.+)$/, function (m) { return 'यह भी हो सकता है: ' + snAll(m[1]).replace(/\.$/, '।'); }],
    [/^Drop at (.+) — journey ends with happy memories\.$/, function (m) { return pn(m[1]) + ' पर ड्रॉप — सुखद यादों के साथ यात्रा पूरी।'; }],
    [/^Arrive in (.+)$/, function (m) { return pn(m[1]) + ' पहुँचें'; }],
    [/^Departure from (.+)$/, function (m) { return pn(m[1]) + ' से वापसी'; }],
    [/^(.+) → (.+) · departure$/, function (m) { return pn(m[1]) + ' → ' + pn(m[2]) + ' · वापसी'; }],
    [/^(.+?) — (.+)$/, function (m) { return isPlace(m[1]) ? pn(m[1]) + ' — ' + snAll(m[2]) : null; }],
    [/^Pickup · (.+)$/, function (m) { return 'पिकअप · ' + dt(m[1]); }],
    [/^Range (₹[\d,]+) – (₹[\d,]+) · Total (₹[\d,]+)$/, function (m) { return 'रेंज ' + m[1] + ' – ' + m[2] + ' · कुल ' + m[3]; }],
    [/^Total (₹[\d,]+) for (.+)$/, function (m) { return 'कुल ' + m[1] + ' — ' + (pax(m[2]) || m[2]); }],
    [/^· total (₹[\d,]+) for (.+)$/, function (m) { return '· कुल ' + m[1] + ' — ' + (pax(m[2]) || m[2]); }],
    [/^(Estimated price|Package price): (₹[\d,]+) per adult$/, function (m) { return (m[1] === 'Package price' ? 'पैकेज कीमत: ' : 'अनुमानित कीमत: ') + m[2] + ' प्रति वयस्क'; }],
    [/^Private (.+) with driver for all transfers and sightseeing as per the plan; fuel, tolls, parking and driver allowance$/, function (m) { return 'प्लान के हिसाब से सभी ट्रांसफ़र और घूमने के लिए ड्राइवर सहित प्राइवेट ' + m[1] + '; डीज़ल/पेट्रोल, टोल, पार्किंग और ड्राइवर भत्ता'; }],
    [/^Private (.+?)( × (\d+))?$/, function (m) { return 'प्राइवेट ' + m[1] + (m[2] || ''); }],
    [/^Hotels · (.+)$/, function (m) { return 'होटल · ' + tier(m[1]); }],
    [/^([\d,]+) km incl\. sightseeing · driver, tolls, parking$/, function (m) { return m[1] + ' किमी (घूमना शामिल) · ड्राइवर, टोल, पार्किंग'; }],
    [/^Built from 2026 market rates for private cars and (.+) hotels, kept on the higher side\. Final price after we check your dates — our team often beats it, and any discounts are added on top\. Flights\/trains, entry tickets, activities and permits are extra\.$/, function (m) { return 'प्राइवेट गाड़ी और ' + tier(m[1]) + ' होटलों के 2026 के बाज़ार रेट से बना, ऊँची तरफ़ रखा गया। आपकी तारीखें देखकर फ़ाइनल कीमत — अक्सर हमारी टीम इससे कम देती है, और छूट ऊपर से। फ़्लाइट/ट्रेन, एंट्री टिकट, एक्टिविटी और परमिट अलग से।'; }],
    [/^Includes private car with driver, (\d+) nights hotel \((.+), (breakfast \+ dinner|breakfast)\), tolls, parking and taxes\. Prepared by$/, function (m) { return 'ड्राइवर सहित प्राइवेट गाड़ी, ' + m[1] + ' रात होटल (' + tier(m[2]) + ', ' + (m[3] === 'breakfast' ? 'नाश्ता' : 'नाश्ता + रात का खाना') + '), टोल, पार्किंग और टैक्स शामिल। तैयार किया:'; }],
    [/^Add-ons on request: (.+)$/, function (m) { return 'अतिरिक्त सेवाएँ (कीमत पूछने पर): ' + m[1].split(', ').map(function (x) { return EX[x] || x; }).join(', '); }],
    [/^Suzu B2B estimate: (₹[\d,]+)$/, function (m) { return 'सुज़ू B2B अनुमान: ' + m[1]; }],
    [/^Your client price \(\+(\d+)%\):$/, function (m) { return 'आपके क्लाइंट की कीमत (+' + m[1] + '%):'; }],
    [/^· (₹[\d,]+)\/adult$/, function (m) { return '· ' + m[1] + '/वयस्क'; }],
    [/^Book with (.+)$/, function (m) { return m[1] + ' के साथ बुक करें'; }],
    [/^Thank you, (.+)! 🙏$/, function (m) { return 'धन्यवाद, ' + m[1] + '! 🙏'; }],
    [/^Ref (TP-\d+) · preview mode: not sent$/, function (m) { return 'Ref ' + m[1] + ' · प्रीव्यू मोड: नहीं भेजा गया'; }],
    [/^Itinerary · (.+)$/, function (m) { return 'यात्रा कार्यक्रम · ' + dt(m[1]); }],
    [/^(.+) or similar$/, function (m) { return tier(m[1]) + ' या समान'; }],
    [/^(.+), (breakfast \+ dinner|breakfast)$/, function (m) { var t = tier(m[1]); return t === m[1] ? null : t + ', ' + (m[2] === 'breakfast' ? 'नाश्ता' : 'नाश्ता + रात का खाना'); }],
    [/^(\d+) nights in (.+) hotels \((\d+) rooms?\) with (breakfast and dinner|breakfast)$/, function (m) { return tier(m[2]) + ' होटलों में ' + m[1] + ' रातें (' + m[3] + ' कमरा), ' + (m[4] === 'breakfast' ? 'नाश्ते' : 'नाश्ते और रात के खाने') + ' के साथ'; }],
    [/^Date moved to (.+) — (.+) is a seasonal trip$/, function (m) { return 'तारीख ' + dt(m[1]) + ' कर दी गई — ' + pnAny(m[2]) + ' मौसमी यात्रा है'; }],
    [/^Pickup set to (.+?)( — now add places| \(nearest\))$/, function (m) { return 'पिकअप ' + pn(m[1]) + (m[2] === ' (nearest)' ? ' (सबसे नज़दीक)' : ' — अब जगहें जोड़ें'); }],
    [/^Itinerary prepared by (.+)$/, function (m) { return 'यात्रा कार्यक्रम ' + m[1] + ' ने तैयार किया'; }],
    [/^(One-way drop|Round trip) · (.+?) · driver(?: night charges)?,? tolls & parking included \(estimate\)\. Final fare on WhatsApp in minutes\.$/, function (m) { return (m[1] === 'One-way drop' ? 'एक तरफ़ ड्रॉप' : 'राउंड ट्रिप') + ' · ' + hrs(m[2]).replace(/(\d+) days/, '$1 दिन').replace('+ local', '+ लोकल') + ' · ड्राइवर, टोल और पार्किंग शामिल (अनुमान)। फ़ाइनल किराया WhatsApp पर कुछ ही मिनटों में।'; }],
    [/^(.+) in (.+), breakfast \+ dinner, taxes \(estimate\)( · peak-season rate)?\. About (₹[\d,]+) per room-night\. We send 2–3 hotel options with photos\.$/, function (m) { return pn(m[2]) + ' में ' + tier(m[1]) + ', नाश्ता + रात का खाना, टैक्स (अनुमान)' + (m[3] ? ' · पीक-सीज़न रेट' : '') + '। लगभग ' + m[4] + ' प्रति कमरा-रात। हम फ़ोटो के साथ 2–3 होटल विकल्प भेजते हैं।'; }],
    [/^(.+) · (\d+) seats$/, function (m) { return m[1] + ' · ' + m[2] + ' सीट'; }],
    [/^This plan is (₹[\d,]+) per adult (cheaper|costlier) than Plan A\.$/, function (m) { return 'यह प्लान Plan A से ' + m[1] + ' प्रति वयस्क ' + (m[2] === 'cheaper' ? 'सस्ता' : 'महँगा') + ' है।'; }],
  ];

  function tr(t) {
    if (EX[t] != null) return EX[t];
    if (PN[t]) return PN[t];
    if (TN[t]) return TN[t];
    if (DATE_RX.test(t)) return dt(t);
    var p = pax(t); if (p) return p;
    for (var i = 0; i < RX.length; i++) { var m = t.match(RX[i][0]); if (m) { var r = RX[i][1](m); if (r != null) return r; } }
    /* compound strings: translate each part */
    var seps = [' · ', ' → '];
    for (var j = 0; j < seps.length; j++) {
      if (t.indexOf(seps[j]) > 0) {
        var parts = t.split(seps[j]), any = false, out = parts.map(function (x) { var y = tr(x); if (y !== x) any = true; return y; });
        if (any) return out.join(seps[j]);
      }
    }
    return t;
  }
  function skip(n) {
    var e = n.parentNode; if (!e || e.nodeType !== 1) return true;
    if (/^(SCRIPT|STYLE|TEXTAREA|CODE)$/.test(e.nodeName) || e.closest('[data-noi18n]')) return true;
    return false;
  }
  function hasDv(n) { var e = n.parentNode; return e && e.parentNode && e.parentNode.querySelector && !!e.parentNode.querySelector(':scope > .dv, :scope > small.dv'); }
  function doText(n) {
    if (skip(n)) return;
    var cur = n.nodeValue;
    if (DONE.get(n) === cur) return;
    var raw = cur, lead = raw.match(/^\s*/)[0], tail = raw.match(/\s*$/)[0], t = raw.trim();
    if (!t || !/[A-Za-z]/.test(t)) return;
    var h = tr(t);
    if (h !== t && hasDv(n) && (PN[t] || TN[t])) h = t; /* Hindi name already shown next to it */
    if (h === t) return;
    ORIG.set(n, raw);
    var v = lead + h + tail; n.nodeValue = v; DONE.set(n, v);
  }
  var ATTR = ['placeholder', 'aria-label', 'label', 'title'];
  var AEX = {
    'Manali, Shimla, Mata darshan, Char Dham…': 'मनाली, शिमला, माता दर्शन, चार धाम…', 'Add a place (e.g. Kasol, Chamunda Devi)': 'जगह जोड़ें (जैसे कसोल, चामुंडा देवी)', 'Add a place': 'जगह जोड़ें',
    'Who is planning': 'कौन प्लान कर रहा है', 'What do you want to plan': 'आप क्या प्लान करना चाहते हैं', 'Trip type': 'यात्रा का प्रकार', 'Your itinerary': 'आपका यात्रा कार्यक्रम', 'Trip builder': 'ट्रिप बिल्डर',
    'Stops in order': 'क्रम से जगहें', 'Fewer adults': 'वयस्क कम करें', 'More adults': 'वयस्क बढ़ाएँ', 'Fewer children': 'बच्चे कम करें', 'More children': 'बच्चे बढ़ाएँ', 'Fewer infants': 'शिशु कम करें', 'More infants': 'शिशु बढ़ाएँ',
    'Fewer rooms': 'कमरे कम करें', 'More rooms': 'कमरे बढ़ाएँ', 'Hotel class': 'होटल श्रेणी', 'Route map of your trip': 'आपकी यात्रा का रूट मैप', 'Estimated price': 'अनुमानित कीमत', 'Close': 'बंद करें',
    'One night less': 'एक रात कम', 'One night more': 'एक रात ज़्यादा', 'Move up': 'ऊपर करें', 'Share link': 'शेयर लिंक', 'Close planner and go back to the homepage': 'प्लानर बंद करके होमपेज पर जाएँ',
    'e.g. Shubh Yatra Holidays': 'जैसे शुभ यात्रा हॉलिडेज़', 'Language': 'भाषा'
  };
  function doAttrs(e) {
    ATTR.forEach(function (a) {
      if (!e.hasAttribute(a)) return;
      var v = e.getAttribute(a), o = AORIG.get(e) || {};
      if (o[a] && o[a].h === v) return;
      var h = AEX[v] || (a === 'label' ? tr(v) : null);
      if (!h) { var m = v.match(/^(Nights at|Remove) (.+)$/); if (m) h = (m[1] === 'Remove' ? pn(m[2]) + ' हटाएँ' : pn(m[2]) + ' में रातें'); }
      if (!h || h === v) return;
      o[a] = { e: v, h: h }; AORIG.set(e, o); e.setAttribute(a, h);
    });
  }
  function walk(root) {
    if (root.nodeType === 3) { doText(root); return; }
    if (root.nodeType !== 1) return;
    if (/^(SCRIPT|STYLE)$/.test(root.nodeName)) return;
    doAttrs(root);
    var w = D.createTreeWalker(root, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT), n;
    while ((n = w.nextNode())) { if (n.nodeType === 3) doText(n); else doAttrs(n); }
  }
  function restore(root) {
    var w = D.createTreeWalker(root, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT), n;
    while ((n = w.nextNode())) {
      if (n.nodeType === 3) { if (ORIG.has(n) && DONE.get(n) === n.nodeValue) n.nodeValue = ORIG.get(n); DONE.delete(n); }
      else { var o = AORIG.get(n); if (o) { Object.keys(o).forEach(function (a) { if (n.getAttribute(a) === o[a].h) n.setAttribute(a, o[a].e); }); AORIG.delete(n); } }
    }
  }
  function observe() {
    OBS = new MutationObserver(function (list) {
      if (LANG !== 'hi' || BUSY) return; BUSY = true;
      try { list.forEach(function (m) { if (m.type === 'characterData') doText(m.target); else if (m.type === 'attributes') doAttrs(m.target); else m.addedNodes.forEach(walk); }); } finally { BUSY = false; }
    });
    OBS.observe(D.body, { subtree: true, childList: true, characterData: true, attributes: true, attributeFilter: ATTR });
  }
  function setBtn() {
    var b = D.getElementById('tp-lang'); if (!b) return;
    b.textContent = LANG === 'hi' ? 'EN' : 'हिं';
    b.setAttribute('aria-label', LANG === 'hi' ? 'View in English' : 'हिंदी में देखें');
    b.setAttribute('lang', LANG === 'hi' ? 'en' : 'hi');
  }
  function setLang(l, quiet) {
    l = l === 'hi' ? 'hi' : 'en'; if (l === LANG && quiet) return;
    LANG = l; W.__tpLang = l;
    D.documentElement.lang = l === 'hi' ? 'hi-IN' : 'en-IN';
    if (l === 'hi') { BUSY = true; try { walk(D.body); } finally { BUSY = false; } } else restore(D.body);
    setBtn();
    try { localStorage.setItem('suzuTpLang', l); } catch (e) {}
    try { if (!quiet && W.SuzuTripPlanner && W.SuzuTripPlanner.pushHash) W.SuzuTripPlanner.pushHash(); } catch (e) {}
    try { if (!quiet && typeof gtag === 'function') gtag('event', 'trip_planner', { step: 'lang_' + l }); } catch (e) {}
  }
  function init() {
    var TP = W.SuzuTripPlanner; if (!TP || !TP.data) return;
    TP.data.places.forEach(function (p) { if (!p.hi) return; PN[p.name] = p.hi; var b = p.name.split(' (')[0]; if (!PN[b]) PN[b] = p.hi.split(' (')[0]; var c = b.split(' / ')[0]; if (!PN[c]) PN[c] = p.hi.split(' (')[0].split(' / ')[0]; });
    sightEX();
    TP.data.templates.forEach(function (t) { if (!t.hi) return; TN[t.name] = t.hi; var sh = t.name.replace(' (summer)', '').replace(' (fly-in)', ''); if (!TN[sh]) TN[sh] = t.hi.replace(/ \([^)]*\)$/, ''); });
    var top = D.querySelector('.tp-top .in'), md = D.querySelector('.tp-mode');
    if (top && !D.getElementById('tp-lang')) {
      var b = D.createElement('button'); b.type = 'button'; b.id = 'tp-lang'; b.className = 'tp-lang'; b.setAttribute('data-noi18n', '');
      b.addEventListener('click', function () { setLang(LANG === 'hi' ? 'en' : 'hi'); });
      top.insertBefore(b, md || top.lastChild);
    }
    observe();
    var q = new URLSearchParams(location.search).get('lang'), st = null;
    try { st = localStorage.getItem('suzuTpLang'); } catch (e) {}
    var want = q === 'hi' || q === 'en' ? q : (W.__tpLinkLang === 'hi' ? 'hi' : st);
    setBtn();
    if (want === 'hi') setLang('hi', true);
    W.SuzuTripPlannerLang = { set: setLang, get: function () { return LANG; }, tr: tr };
  }
  if (D.readyState === 'loading') D.addEventListener('DOMContentLoaded', init); else init();
})();
