# 12 Jyotirlingas: research notes for the hub page

Prepared for suzutravels.com. Research date: **8 Oct 2026**. Per-temple data is in `jyotirlinga.json` (same folder).
Timings and dates change, so recheck everything marked *as of* before you publish. Lines marked **(editorial)** are our own planning estimates and do not come from a source.

---

## 1. What is a Jyotirlinga?

- **Meaning.** *Jyotirlinga* means "linga of light", from *jyotis* (radiance) and *linga* (sign or emblem). It is a shrine where, by tradition, Shiva revealed himself as an endless column of light. [Wikipedia: Jyotirlinga](https://en.wikipedia.org/wiki/Jyotirlinga)
- **The pillar-of-light story (Lingodbhava).** Brahma and Vishnu once argued over which of them was supreme. A blazing pillar with no visible end then appeared between them. Vishnu took the form of a boar and dug downward, and Brahma took the form of a swan and flew upward, each trying to find where it ended. Vishnu came back and admitted that he had failed. Brahma claimed he had reached the top and offered a *ketaki* flower as false proof. Shiva then emerged from the pillar. He blessed Vishnu for being honest and declared that Brahma would not be worshipped for his lie. Temple sculpture calls this scene **Lingodbhava**, "the emergence from the linga". [Wikipedia: Jyotirlinga](https://en.wikipedia.org/wiki/Jyotirlinga) · [Wikipedia: Kashi Vishwanath](https://en.wikipedia.org/wiki/Kashi_Vishwanath_Temple)
- **64 shrines, of which 12 are pre-eminent.** Tradition says there were once 64 jyotirlinga sites and that 12 of them are especially holy. [Wikipedia](https://en.wikipedia.org/wiki/Jyotirlinga)
- **Scriptural basis.** The Shiva Mahapurana names the 12 shrines in the **Shatarudra Samhita (ch. 42)** and again in the **Koti Rudra Samhita, ch. 1, vv. 21–23**. It tells each shrine's story in Koti Rudra Samhita **chs. 14–33**. [Wikipedia](https://en.wikipedia.org/wiki/Jyotirlinga) · [Koti Rudra Samhita text](https://sanskritdocuments.org/doc_purana/shivapurANam4koTirudrasaMhitA.html)

### The Shiva Purana list, which sets the order used in our JSON

The sequence in `jyotirlinga.json` (Somnath → … → Kedarnath at no. 5 → … → Grishneshwar at no. 12) follows **Koti Rudra Samhita 1.21–23**:

> सौराष्ट्रे सोमनाथं च श्रीशैले मल्लिकार्जुनम् ।
> उज्जयिन्यां महाकालमोङ्कारे परमेश्वरम् ॥ २१॥
> केदारं हिमवत्पृष्ठे डाकिन्यां भीमशङ्करम् ।
> वाराणस्यां च विश्वेशं त्र्यम्बकं गौतमीतटे ॥ २२॥
> वैद्यनाथं चिताभूमौ नागेशं दारुकावने ।
> सेतुबन्धे च रामेशं घुश्मेशं च शिवालये ॥ २३॥

Source: [sanskritdocuments.org, Shiva Mahapurana 4 (Koti Rudra Samhita)](https://sanskritdocuments.org/doc_purana/shivapurANam4koTirudrasaMhitA.html)

---

## 2. Dvadasha Jyotirlinga Stotram (the popular smaranam)

The short verse below is the one most people recite. Its order **is different from** the Shiva Purana list above. Here Vaidyanath comes 5th, written as "at Parli", and Kedarnath comes 11th. The Sanskrit is public domain. Text source: [Wikipedia: Jyotirlinga](https://en.wikipedia.org/wiki/Jyotirlinga). The meanings are our own paraphrases.

| # | Sanskrit (Devanagari) | One-line meaning (our words) |
|---|---|---|
| 1 | सौराष्ट्रे सोमनाथं च श्रीशैले मल्लिकार्जुनम् । | Somnath in Saurashtra, and Mallikarjuna on the holy Shrishaila hill. |
| 2 | उज्जयिन्यां महाकालमोङ्कारममलेश्वरम् ॥ | Mahakala in Ujjain, and Amaleshwar at Omkara on the Narmada. |
| 3 | परल्यां वैद्यनाथं च डाकिन्यां भीमशङ्करम् । | Vaidyanath at Parli, and Bhimashankar in the land of Dakini. |
| 4 | सेतुबन्धे तु रामेशं नागेशं दारुकावने ॥ | Rameshwara where Rama's bridge began, and Nagesha in the Daruka forest. |
| 5 | वाराणस्यां तु विश्वेशं त्र्यम्बकं गौतमीतटे । | Vishwesha in Varanasi, and Tryambaka on the bank of the Gautami (Godavari). |
| 6 | हिमालये तु केदारं घुश्मेशं च शिवालये ॥ | Kedara in the Himalaya, and Ghushmesha at Shivalaya. |
| 7 | एतानि ज्योतिर्लिङ्गानि सायं प्रातः पठेन्नरः । | Whoever recites these Jyotirlinga names at dusk and at dawn… |
| 8 | सप्तजन्मकृतं पापं स्मरणेन विनश्यति ॥ | …has the sins of seven lifetimes wiped away just by remembering them. |
| 9 | एतेषां दर्शनादेव पातकं नैव तिष्ठति । | Simply beholding these shrines leaves no wrongdoing standing. |
| 10 | कर्मक्षयो भवेत्तस्य यस्य तुष्टो महेश्वरः ॥ | For the one with whom Maheshwara is pleased, the bonds of karma wear away. |

*Text notes.* Wikipedia's copy ends line 10 with "महेश्वराः"; the common reading is "महेश्वरः". A separate and longer *Dvadasha Jyotirlinga Stotram*, attributed to Adi Shankaracharya, also exists. It has 13 verses in yet another order, and we have not reproduced or checked it here.

---

## 3. Planning the full 12-Jyotirlinga circuit

### Regional groupings

| Cluster | Jyotirlingas | Hub / gateway | Key verified link |
|---|---|---|---|
| **Gujarat (2)** | Somnath, Nageshwar | Fly to Rajkot / Diu / Porbandar / Jamnagar | Somnath → Dwarka is 230 km ([Somnath Trust FAQ](https://somnath.org/faq/)); Nageshwar is about 16–18 km beyond Dwarka |
| **Madhya Pradesh (2)** | Mahakaleshwar, Omkareshwar | Indore | Ujjain → Omkareshwar is 140 km; Indore airport → Omkareshwar is 77 km ([Omkareshwar Trust](https://www.shriomkareshwar.org/HowToReach.aspx)) |
| **Maharashtra (3)** | Trimbakeshwar, Bhimashankar, Grishneshwar | Mumbai / Nashik / Pune / Chh. Sambhajinagar | Trimbak is 40 km from Nashik Road; Bhimashankar is about 110 km from Pune; Grishneshwar is about 30 km from Chh. Sambhajinagar (Wikipedia) |
| Maharashtra alternates (+2) | Parli Vaijnath (Beed), Aundha Nagnath (Hingoli) | Chh. Sambhajinagar / Nanded / Parli rail | Add these if your group follows the Maharashtra tradition |
| **South (2)** | Mallikarjuna (Srisailam), Rameshwaram | Hyderabad; Madurai | Srisailam is about 213 km from Hyderabad (Wikipedia); Rameswaram is reached via Madurai |
| **North (2)** | Kedarnath, Kashi Vishwanath | Dehradun/Rishikesh; Varanasi | Kedarnath is seasonal, with a 16–17 km trek or a helicopter from Guptkashi/Phata/Sirsi |
| **East (1)** | Vaidyanath (Deoghar) | Deoghar airport (9 km) / Jasidih (7 km) | Very crowded in Shravan |

### Realistic total days (editorial)

| Plan | Days | Notes |
|---|---|---|
| Flights between clusters, road within each cluster, helicopter for Kedarnath | **18–22 days** | The most realistic plan for a single trip |
| Very tight flights and no rest days | **15–16 days** | Only possible when Kedarnath is open. It leaves no buffer for weather, Bhasma Aarti slots or the Bhimashankar pass system, so treat it as an aggressive plan |
| Mostly train/road | **25–30 days** | |
| Split into 3–4 shorter trips | 4–6 days each | Gujarat+MP, Maharashtra, South, and North+East. Many pilgrims do it this way |

Per-cluster rough estimates (editorial): Gujarat 3 days · MP 2 · Maharashtra 3–4 (plus 2 for Parli and Aundha) · South 4–5 including flights · Kashi 1–2 · Kedarnath 4–5 from Haridwar/Rishikesh by road and trek (2–3 with a helicopter) · Deoghar 1–2.

### Best season (editorial, based on the constraints below)

- **Kedarnath sets the window.** In 2026 it opened on **22 April**. It closes around Bhai Dooj (Oct/Nov) on a date announced on Vijayadashami. A full 12-temple circuit is therefore only possible from about **late April/May to the end of October**.
- **Best sub-windows:** **May–June** (Kedarnath is open but the plains are hot), or **late September–October** (after the monsoon, with cooler plains, before Kedarnath closes; Rameswaram can get north-east-monsoon showers).
- **Avoid July–August for Kedarnath.** Landslide risk and IMD alerts pause the yatra.
- **Shravan** is the holiest month, but crowds are extreme at Deoghar (Shravani Mela), Ujjain, Kashi and Somnath.
- If you skip Kedarnath (or do it on a separate summer trip), **October–March** suits the other 11.

### Key calendar dates

**Shravan (Sawan) month.** Dates differ by calendar. North India uses the *Purnimanta* calendar; Gujarat, Maharashtra and the South use the *Amanta* calendar.

| Year | Purnimanta (North: UP, MP, Bihar, Jharkhand, Uttarakhand…) | Amanta (Gujarat, Maharashtra, AP, Telangana, TN…) | Source |
|---|---|---|---|
| **2026** (already over) | 30 Jul – 28 Aug 2026; Mondays 3, 10, 17, 24 Aug | 13 Aug – 11 Sep 2026; Mondays 17, 24, 31 Aug, 7 Sep | [Outlook India](https://www.outlookindia.com/brand-studio/sawan-2026-calendar-all-mondays-festivals-and-important-dates-in-one-place) (Drik Panchang for a US location shows the Purnimanta end as 27 Aug) |
| **2027** | 19 Jul – 16 Aug 2027; Mondays 19, 26 Jul, 2, 9, 16 Aug | 2 Aug – 31 Aug 2027; Mondays 2, 9, 16, 23, 30 Aug | [Drik Panchang](https://www.drikpanchang.com/festivals/sawan/sawan-somwar-vrat-dates.html?year=2027). **Caveat:** these were computed for a US location, so India dates may shift by a day. Recheck for New Delhi before publishing |

The solar Sawan used in Nepal and parts of Uttarakhand/Himachal starts on 16 Jul 2026 and 16 Jul 2027.

**Mahashivratri 2027: Saturday, 6 March 2027.** The Nishita (midnight) puja falls on the night of 6–7 March. Sources: [Drik Panchang](https://www.drikpanchang.com/festivals/maha-shivaratri/maha-shivaratri-date-time.html?year=2027) (Houston calculation: Chaturdashi runs from 6 Mar to 7 Mar, which converts to about midday 6 Mar to about 1:45 pm 7 Mar IST, so the India date is also 6 Mar) and [AstroSight](https://astrosight.ai/festivals/maha-shivratri/2027).

**Other useful 2026–27 dates**
- Vijayadashami 2026 is **20 Oct 2026**, when the Kedarnath closing date is expected to be announced ([Drik Panchang](https://www.drikpanchang.com/festivals/vijayadashami/vijayadashami-date-time.html?year=2026)).
- Bhai Dooj 2026 is **11 Nov 2026** for New Delhi ([Dekho Panchang](https://dekhopanchang.com/en/festivals/bhai-dooj/2026)). Some panchangs and US calculations give 10 Nov, so wait for the official BKTC announcement.
- The Nashik–Trimbakeshwar Simhastha Kumbh begins with flag hoisting on **31 Oct 2026**. Amrit Snan dates are **2 Aug, 31 Aug and 12 Sep 2027** at Trimbakeshwar (11 Sep at Nashik), and the Kumbh closes on 24 Jul 2028 ([The Week/PTI](https://www.theweek.in/wire-updates/national/2025/06/01/bom14-mh-ld-kumbh-mela.html)).

### Booking and logistics checklist (from official sources)

- **Kedarnath:** Uttarakhand registration ([registrationandtouristcare.uk.gov.in](https://registrationandtouristcare.uk.gov.in)) is mandatory. Book the helicopter only on [IRCTC HeliYatra](https://www.heliyatra.irctc.co.in/), and book pujas on [BKTC](https://www.badrinath-kedarnath.gov.in).
- **Mahakaleshwar:** book the Bhasma Aarti online about a month ahead. Since June 2026 each mobile number gets one permission per 90 days. Men wear a dhoti and women a saree ([MP Tourism](https://www.mptourism.com/bhasm-aarti-at-mahakaleshwar-and-ujjain.html)).
- **Kashi:** the Mangala Aarti is at 3 AM (report at 2:30 AM, Gate 1). Sugam Darshan costs Rs 300 ([KV Trust FAQ](https://shrikashivishwanath.org/pdffile/FAQ_SHRI_KASHI_VISHWANTH_TEMPLE_2_0_pdf.pdf)).
- **Bhimashankar:** an online pass system began in June 2026. Check [shreebhimashankar.com](https://shreebhimashankar.com/en/) for the current rules.
- **Srisailam:** Sparsha (touch) darshan is sold online only. On Sat/Sun/Mon only the night slot is available (Aug 2026).
- **Phones:** not allowed inside Somnath, Mahakal or Kashi. All three have free lockers.

---

## 4. Ten FAQs people search (hub page)

1. **Which Jyotirlinga is the first?** Somnath in Gujarat is listed first in both the Shiva Purana list and the popular stotra.
2. **Which is the 12th (last) Jyotirlinga?** Grishneshwar (Ghushmeshwar) at Verul, near Ellora, Maharashtra.
3. **Which Jyotirlinga is in the south of India?** Rameshwaram (Ramanathaswamy) in Tamil Nadu is the southernmost. Mallikarjuna at Srisailam, Andhra Pradesh, is the other southern one.
4. **Can we visit all 12 Jyotirlingas in 15 days?** Only while Kedarnath is open (about late April to Oct/Nov), with flights between regions and ideally a Kedarnath helicopter. 18–22 days is more realistic, and many pilgrims split it into 3–4 trips. (editorial)
5. **Which state has the most Jyotirlingas?** Maharashtra, with 3 in the mainstream list (Trimbakeshwar, Bhimashankar, Grishneshwar). Maharashtra tradition counts 5 by adding Parli Vaijnath and Aundha Nagnath.
6. **Which is the highest Jyotirlinga?** Kedarnath, at about 3,583 m (11,755 ft).
7. **Which Jyotirlinga closes in winter?** Only Kedarnath. From Bhai Dooj until spring, the deity is worshipped at Omkareshwar Temple, Ukhimath.
8. **Which Jyotirlinga faces south?** Mahakaleshwar in Ujjain, the only *dakshinamukhi* one of the 12. It is also famous for the pre-dawn Bhasma Aarti.
9. **Which Jyotirlingas are on islands?** Omkareshwar is on Mandhata island in the Narmada, and Rameshwaram is on Pamban island.
10. **What is the best time for a 12 Jyotirlinga yatra?** May–June or late September–October if you include Kedarnath; October–March for the other 11. (editorial)

Bonus questions: *Which Jyotirlinga is in Jharkhand?* Baba Baidyanath, Deoghar. *Which two are in Gujarat?* Somnath and Nageshwar. *Which two are in MP?* Mahakaleshwar and Omkareshwar.

---

## 5. FACT TRAPS: things commonly stated wrong online

| # | Common claim | Correct version | Source |
|---|---|---|---|
| 1 | "Kedarnath opens on Akshaya Tritiya." | Gangotri and Yamunotri open on Akshaya Tritiya, which was 19 Apr in 2026. Kedarnath's date is fixed separately at Ukhimath on Mahashivratri; in 2026 it opened on **22 Apr** at about 8 AM. | [ETV Bharat, 15 Feb 2026](https://www.etvbharat.com/en/state/mahashivratri-2026-kedarnath-temple-opening-announced-enn26021501713) |
| 2 | "Kedarnath 2026 closing date confirmed: 11 November." | **Not announced as of 8 Oct 2026.** It closes by custom on Bhai Dooj (10 or 11 Nov 2026 depending on the panchang), and BKTC announces the date on Vijayadashami (20 Oct 2026). In 2025 the doors closed on 23 Oct. | [Times Now Hindi, 2 Sep 2026](https://www.timesnowhindi.com/spirituality/kedarnath-closing-date-2026-kedarnath-ke-kapat-kab-band-honge-2026-winter-seat-ukhimath-article-156029922) · [News On Air 2025](https://www.newsonair.gov.in/uttarakhand-announces-winter-closing-dates-for-kedarnath-badrinath-gangotri-and-yamunotri-temples/) |
| 3 | "The Dwadasha Jyotirlinga Stotram order is Somnath, Mallikarjuna, Mahakal, Omkar, Kedar, Bhimashankar…" | That sequence is the **Shiva Purana (Koti Rudra Samhita 1.21–23)** order. The popular smaranam stotra lists Vaidyanath (Parli) 5th, then Bhimashankar, Rameshwaram, Nageshwar, Vishwanath, Tryambak, Kedar, Ghushmesh. So "Kedarnath is the 5th Jyotirlinga" and "Kedarnath is the 11th" are both seen online, depending on the list. Say which list you are using. | [Shiva Purana text](https://sanskritdocuments.org/doc_purana/shivapurANam4koTirudrasaMhitA.html) · [Wikipedia stotra](https://en.wikipedia.org/wiki/Jyotirlinga) |
| 4 | "The scriptures say Vaidyanath is at Parli." | "परल्यां वैद्यनाथं" (Parli) appears only in the popular smaranam. The Shiva Purana list says **"वैद्यनाथं चिताभूमौ"** ("in the cremation-ground land"), which tradition links to Deoghar. Present both neutrally. | Same as #3 |
| 5 | "Mahmud of Ghazni attacked Somnath in 1025." | The raid was in **January 1026** (two Persian sources say 1027). The 1,000-year "Somnath Swabhiman Parv" was held on 10–11 Jan 2026. | [Wikipedia](https://en.wikipedia.org/wiki/Somnath_Temple) · [The Week](https://www.theweek.in/news/india/2026/01/10/what-is-the-somnath-swabhiman-parv-inside-the-grand-event-attended-by-pm-modi.amp.html) |
| 6 | "Somnath was rebuilt and inaugurated by Nehru / in 1950." | The Pran-Pratishtha was performed by **President Dr Rajendra Prasad on 11 May 1951**. Sardar Patel's resolve dates to Nov 1947: the Trust says 13 Nov and Wikipedia says 12 Nov. | [Somnath Trust](https://somnath.org/somnath-darshan/) |
| 7 | "Mahakal's Bhasma Aarti uses ash from cremation pyres." | That was historically said. The ash is **now prepared from cow dung**. | [MP Tourism](https://www.mptourism.com/bhasm-aarti-at-mahakaleshwar-and-ujjain.html) |
| 8 | "You can join the Bhasma Aarti any day via an offline queue / book as often as you like." | Prior online booking is required (about a month ahead). From June 2026 one mobile number gets **one permission every 90 days**. Agency claims about offline or "tatkal" queues are unverified. | [MP Tourism](https://www.mptourism.com/bhasm-aarti-at-mahakaleshwar-and-ujjain.html) · [Navbharat Live, 22 Jun 2026](https://navbharatlive.com/madhya-pradesh/ujjain/mahakal-temple-implements-new-booking-rule-for-bhasma-aarti-devotees-1815340.html) |
| 9 | "Bhimashankar is open as usual." | The temple was **closed 9 Jan – 14 Jun 2026** for construction. It reopened on 15 Jun with **compulsory online passes (1,000/day)**, and Shravan hours were 5 AM – 9:30 PM. Many 2026 travel blogs ignore this. | [Punekar News](https://www.punekarnews.in/bhimashankar-darshan-resumes-from-june-15-online-registration-now-compulsory/) · [Bridge Chronicle](https://www.thebridgechronicle.com/pune/bhimashankar-temple-open-throughout-shravan-darshan-timings-extended-agn97) |
| 10 | "Bhimashankar Jyotirlinga is in Assam" (or "only in Pune"). | This is a live tradition dispute. The Pune-district temple is the most widely accepted. Assam identifies Bhimeswar Dham at Pamohi, Guwahati, and the Assam CM asserted this in Feb 2023. State both. | [Outlook, 20 Feb 2023](https://www.outlookindia.com/amp/story/national/-bhimashankar-jyotirlinga-located-in-assam-s-kamrup-himanta-news-263538) |
| 11 | "Kashi Vishwanath corridor opened in 2022" / "Mangala Aarti is at 4 AM." | The corridor was inaugurated on **13 Dec 2021**. The Mangala Aarti runs **3:00–4:00 AM**, with reporting at 2:30 AM. | [narendramodi.in](https://narendramodi.in/prime-minister-narendra-modi-to-visit-varanasi-and-inaugurate-shri-kashi-vishwanath-dham-on-13-december) · [KV Trust FAQ](https://shrikashivishwanath.org/pdffile/FAQ_SHRI_KASHI_VISHWANTH_TEMPLE_2_0_pdf.pdf) |
| 12 | "Ahilyabai Holkar built the present Grishneshwar temple." | Wikipedia credits the 1729 rebuild to **Gautama Bai Holkar** (Ahilyabai's mother-in-law), with Maloji Bhosale's restoration in the 16th century. Say "rebuilt by the Holkars in the 18th century" unless you have a better source. | [Wikipedia](https://en.wikipedia.org/wiki/Ghrishneshwar_Temple) |
| 13 | "The Kedarnath trek is 14 km." | Older guides cite about 14 km (the pre-2013 route). IRCTC HeliYatra now gives **about 16 km** from Gaurikund and Wikipedia gives 17 km. | [IRCTC HeliYatra](https://www.heliyatra.irctc.co.in/) · [Wikipedia](https://en.wikipedia.org/wiki/Kedarnath_Temple) |
| 14 | "Kedarnath is closed during the monsoon" (this even appears on BKTC's own About page). | The temple stays open from opening to Bhai Dooj. The **yatra** is paused only temporarily for weather alerts, as happened in 2026. Don't tell pilgrims the temple is shut in July–August. | [BKTC page](https://www.badrinath-kedarnath.gov.in/AboutUs/shri-kedarnath.aspx) · [Navbharat Live (2026 halt)](https://navbharatlive.com/uttarakhand/kedarnath-yatra-2026-halted-after-imd-warning-orange-alert-raises-pilgrims-concerns-1766201.html) |
| 15 | "Book a Kedarnath helicopter / Somnath room via WhatsApp or an agent link." | Book helicopters only on **IRCTC HeliYatra**, and only after Char Dham registration. The Somnath Trust explicitly warns about WhatsApp/phone booking frauds. | [ETV Bharat, 31 Mar 2026](https://www.etvbharat.com/en/state/8-helicopter-companies-to-operate-heli-service-to-kedarnath-dham-know-fares-enn26033106782) · [somnath.org](https://somnath.org/) |
| 16 | "Shravan starts on the same day everywhere." | Purnimanta (North) and Amanta (Gujarat, Maharashtra, South) Shravan start about **two weeks apart**. In 2026 that was 30 Jul vs 13 Aug. Use the local calendar for each temple. | [Outlook India](https://www.outlookindia.com/brand-studio/sawan-2026-calendar-all-mondays-festivals-and-important-dates-in-one-place) |
| 17 | "Mahashivratri 2027 is on 7 March." | It is **Saturday 6 March 2027**, with the Nishita puja on the night of 6–7 March. | [Drik Panchang](https://www.drikpanchang.com/festivals/maha-shivaratri/maha-shivaratri-date-time.html?year=2027) |
| 18 | "Mamleshwar isn't part of the Omkareshwar Jyotirlinga." | Tradition, and the popular stotra line "ओङ्कारममलेश्वरम्", treats Omkareshwar and Amaleshwar/Mamleshwar as one Jyotirlinga in two aspects. Pilgrims visit both. | [Wikipedia](https://en.wikipedia.org/wiki/Omkareshwar_Temple) |
| 19 | "Rameswaram has the world's longest temple corridor." | India's official tourism site describes the third corridor as **Asia's** longest (197 m east–west, 133 m north–south). Avoid saying "world's". | [Incredible India](https://www.incredibleindia.gov.in/en/tamil-nadu/rameswaram/sri-ramanathaswamy-temple) |
| 20 | Inconsistencies on official sites | Somnath gives two Sound & Light Show slots (8–9 PM in the FAQ, 7:45–8:45 PM on the Darshan page). Trimbakeshwar's daily programme prints the evening puja as "7.00 AM to 8.30 AM", an obvious typo. babadham.org shows "4 AM–9 PM" in its header but a schedule that closes at 8 PM. Wikipedia's Baijnath (HP) temple coordinates disagree with the town's coordinates. Don't copy these without checking. | [Somnath FAQ](https://somnath.org/faq/) · [Trimbak daily programme](https://trimbakeshwartrust.com/daily_programme) · [babadham.org timings](https://babadham.org/timings/) |

---

## 6. Items we could NOT verify (all left `null` or flagged in the JSON)

- **Mahakaleshwar:** official daily timings. The official sites failed TLS on 8 Oct 2026. Only the 4 AM Bhasma Aarti start is government-verified (MP Tourism). The other aarti times come from agencies and are flagged.
- **Kedarnath:** daily darshan hours. BKTC does not publish them.
- **Srisailam:** official seva and aarti schedule and dress code. The site is JavaScript-only, so we used news reports from Dec 2024 and Aug 2026.
- **Bhimashankar:** timings and pass status after Shravan 2026.
- **Nageshwar:** no official temple website found. Timings are from Incredible India ("dawn to dusk") plus an unverified agency figure (6 AM–9 PM).
- **Rameswaram:** HRCE site unreachable. Hours are from Incredible India; the pooja schedule, Spadika Linga time and ticket prices are unverified.
- **Baidyanath:** whether babadham.org is the government-constituted board's site.
- **Distances:** many "approx." distances are editorial road estimates. Only those cited to temple FAQs or Wikipedia are sourced.
- **Sawan 2027:** dates from Drik Panchang were computed for a US location. Recheck them for India.
