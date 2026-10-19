/* Suzu Trip Planner — Hindi UI (EN / हिं), v0.8, 19 Oct 2026.
   A display-only layer: it translates what is on screen (and the print/PDF document) and never touches
   the data, the price engine or the lead message (the team always receives English).
   How: exact dictionary + pattern rules on text nodes and placeholder/aria-label/optgroup labels, re-applied
   by a MutationObserver after every render. Place and trip-idea names come from the data's own `hi` fields.
   Sight names, notes and region tips stay in English for now (phase 2). */
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
    'Travel agent mode — your branding on the PDF & link': 'ट्रैवल एजेंट मोड — PDF और लिंक पर आपकी ब्रांडिंग', 'Agency name': 'एजेंसी का नाम', 'Agency phone': 'एजेंसी फ़ोन', 'Your markup %': 'आपका मार्कअप %', 'Agency email': 'एजेंसी ईमेल',
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
  function cat(s) { return EX[s] || s; }
  function tier(s) { return EX[s] || EX[s.split(' (')[0]] && (EX[s.split(' (')[0]] + s.slice(s.split(' (')[0].length)) || s; }
  function noDot(s) { return s.replace(/\.$/, ''); }

  /* pattern rules: [regex, fn(match) -> hindi] — tried in order after the exact dictionary */
  var RX = [
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
    [/^🏨 Night in (.+)$/, function (m) { return '🏨 ' + pn(m[1]) + ' में रात'; }],
    [/^Day (\d+)$/, function (m) { return 'दिन ' + m[1]; }],
    [/^Day (\d+): (.+) → (.+) is a long drive \((.+)\)\. Consider a night halt on the way\.$/, function (m) { return 'दिन ' + m[1] + ': ' + pn(m[2]) + ' → ' + pn(m[3]) + ' लंबा सफ़र है (' + hrs(m[4]) + ')। रास्ते में एक रात रुकने पर विचार करें।'; }],
    [/^Last day: (.+) → (.+) is a long drive \((.+)\)\. Many guests add a night on the way\.$/, function (m) { return 'आख़िरी दिन: ' + pn(m[1]) + ' → ' + pn(m[2]) + ' लंबा सफ़र है (' + hrs(m[3]) + ')। कई मेहमान रास्ते में एक रात जोड़ते हैं।'; }],
    [/^Peak-season hotel rates applied for (\d+) nights? \(mid-Mar–Jun, October, Christmas–New Year\)\.$/, function (m) { return m[1] + ' रातों के लिए पीक-सीज़न होटल रेट लगाए गए हैं (मध्य मार्च–जून, अक्टूबर, क्रिसमस–नया साल)।'; }],
    [/^Kedarnath needs 2 nights at (.+) \(trek up, darshan, trek down — or helicopter, subject to tickets\)\. You have (\d+) nights? here; add a night for a relaxed darshan\.$/, function (m) { return 'केदारनाथ के लिए ' + pn(m[1]) + ' में 2 रातें चाहिए (चढ़ाई, दर्शन, उतराई — या हेलिकॉप्टर, टिकट मिलने पर)। आपकी यहाँ ' + m[2] + ' रात है; आराम से दर्शन के लिए एक रात जोड़ें।'; }],
    [/^Spiti, Lahaul, Chitkul and Ladakh roads need an SUV \(Innova Crysta or bigger\)\. Your estimate uses (.+) — our team will suggest the right car\.$/, function (m) { return 'स्पीति, लाहौल, चितकुल और लद्दाख की सड़कों के लिए SUV (इनोवा क्रिस्टा या बड़ी) चाहिए। आपके अनुमान में ' + m[1] + ' है — हमारी टीम सही गाड़ी बताएगी।'; }],
    [/^(.+) is usually closed \/ snowbound in (\w+) \(open about (\w+)–(\w+)\)\. Pick other dates or swap this stop\.$/, function (m) { return pn(m[1]) + ' ' + dt(m[2]) + ' में आम तौर पर बंद / बर्फ़ से ढका रहता है (लगभग ' + dt(m[3]) + '–' + dt(m[4]) + ' खुला)। दूसरी तारीख चुनें या यह जगह बदलें।'; }],
    [/^(.+) is usually closed in (\w+) \(open about (\w+)–(\w+)\), so it is left out of your day plan\.(.*)$/, function (m) { return m[1] + ' ' + dt(m[2]) + ' में आम तौर पर बंद रहता है (लगभग ' + dt(m[3]) + '–' + dt(m[4]) + ' खुला), इसलिए इसे आपके प्लान से हटाया गया है।' + (/Solang/.test(m[5]) ? ' सर्दियों में बर्फ़ का मज़ा सोलंग वैली में; सड़क खुली हो तो अटल टनल और सिस्सू।' : m[5]); }],
    [/^Your (.+) darshan falls in (.+?) \((.+?)\): very big crowds, long darshan queues and hotels fill early\. We plan darshan for early morning and keep extra time on these days\.(.*)$/, function (m) { var rest = m[4].trim().replace(/[^.]+\./g, function (x) { x = x.trim(); return (EX[x] || x) + ' '; }).trim(); return 'आपका ' + pn(m[1]) + ' दर्शन ' + m[2].replace('Chaitra Navratri', 'चैत्र नवरात्रि').replace('Sharad Navratri', 'शारदीय नवरात्रि') + ' (' + dt(m[3]) + ') में पड़ रहा है: बहुत भीड़, दर्शन की लंबी लाइनें और होटल जल्दी भर जाते हैं। इन दिनों हम दर्शन सुबह जल्दी रखते हैं और ज़्यादा समय रखते हैं।' + (rest ? ' ' + rest : ''); }],
    [/^Pickup in (.+?)( \((.+)\))?, then drive to (.+)\.$/, function (m) { return pn(m[1]) + ' से पिकअप' + (m[2] || '') + ', फिर ' + pn(m[4]) + ' के लिए रवाना।'; }],
    [/^After breakfast, drive to (.+)\.$/, function (m) { return 'नाश्ते के बाद ' + pn(m[1]) + ' के लिए रवाना।'; }],
    [/^🛕 Darshan at (.+?)( — (.+))? on the way\.$/, function (m) { return '🛕 रास्ते में ' + pn(m[1]) + ' दर्शन' + (m[3] ? ' — ' + m[3] : '') + '।'; }],
    [/^Stop at (.+?)( — (.+))? on the way\.$/, function (m) { return 'रास्ते में ' + pn(m[1]) + ' पर रुकें' + (m[3] ? ' — ' + m[3] : '') + '।'; }],
    [/^Evening: (.+)$/, function (m) { return 'शाम: ' + m[1]; }],
    [/^Tip: (.+)$/, function (m) { return 'सुझाव: ' + m[1]; }],
    [/^Also possible: (.+)$/, function (m) { return 'यह भी हो सकता है: ' + m[1]; }],
    [/^Drop at (.+) — journey ends with happy memories\.$/, function (m) { return pn(m[1]) + ' पर ड्रॉप — सुखद यादों के साथ यात्रा पूरी।'; }],
    [/^Arrive in (.+)$/, function (m) { return pn(m[1]) + ' पहुँचें'; }],
    [/^Departure from (.+)$/, function (m) { return pn(m[1]) + ' से वापसी'; }],
    [/^(.+) → (.+) · departure$/, function (m) { return pn(m[1]) + ' → ' + pn(m[2]) + ' · वापसी'; }],
    [/^(.+?) — (.+)$/, function (m) { return isPlace(m[1]) ? pn(m[1]) + ' — ' + m[2] : null; }],
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
    [/^(.+) · (\d+) seats$/, function (m) { return m[1] + ' · ' + m[2] + ' सीट'; }]
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
