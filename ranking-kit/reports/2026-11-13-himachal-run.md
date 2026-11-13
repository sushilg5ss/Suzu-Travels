# Himachal places and inbound run — 13 Nov 2026 (19:24–23:20 IST)

Owner: Claude (head of marketing/SEO). Reviewer: Sushil.

**Brief:** content for every Himachal place, so the site ranks on Google and brings genuine enquiries, for both inbound (abroad) and domestic travellers. It uses the snow season now and early booking for summer.

**Result:** 34 new posts are live, all in category 77 Himachal. Every post has:
- the Rank Math title, description and focus keyword, set via REST
- credited CC photos from Wikimedia
- a live-weather or snow-forecast widget
- tables, a FAQ with FAQPage schema, and WhatsApp and quote CTAs

All 34 return 200, are set to index and carry a self-canonical.

## Place guides (21)
| URL | ID | Focus |
|---|---|---|
| /langza-hikkim-komic/ | 21783 | langza, hikkim, komic |
| /sarahan-bhimakali-temple/ | 21793 | bhimakali temple sarahan |
| /shoja/ | 21803 | shoja, shoja jalori pass |
| /naldehra-mashobra/ | 21812 | naldehra, mashobra, naldehra golf course |
| /bhagsu-dharamkot/ | 21822 | bhagsu waterfall, bhagsunag temple, dharamkot |
| /masroor-rock-cut-temple/ | 21834 | masroor rock cut temple |
| /tabo-monastery/ | 21904 | tabo monastery |
| /key-monastery/ | 21907 | key monastery |
| /nako/ | 21910 | nako lake, nako village |
| /hatu-peak-narkanda/ | 21917 | hatu peak, narkanda snowfall |
| /dhankar-monastery/ | 21927 | dhankar monastery, dhankar lake |
| /kibber-chicham/ | 21940 | kibber village, chicham bridge |
| /pin-valley/ | 21953 | pin valley, mudh village |
| /sissu/ | 21963 | sissu, sissu snowfall |
| /keylong-lahaul/ | 21973 | keylong, lahaul valley |
| /bharmour-manimahesh/ | 21983 | bharmour, manimahesh lake |
| /janjehli-shikari-devi/ | 21993 | janjehli, shikari devi temple |
| /kaza-spiti/ | 22004 | kaza spiti, kaza in winter |
| /barog-dagshai/ | 22017 | barog, dagshai, barog tunnel |
| /renuka-lake/ | 22026 | renuka lake, renuka ji |
| /bilaspur-gobind-sagar/ | 22071 | bilaspur himachal, gobind sagar, submerged temples |

## Traffic, season and Hindi pages (6)
| URL | ID | Why |
|---|---|---|
| /himachal-distance-chart/ | 21837 | "X to Y distance" queries sit at position 9–10 in GSC; km, drive time and winter closures in one place |
| /delhi-se-manali-shimla-kitne-km/ | 21839 | Hindi twin of the distance chart; linked both ways |
| /himachal-summer-vacation-2027/ | 21847 | Early booking for May–June 2027 |
| /himachal-mein-barfbari/ | 22029 | Hindi "हिमाचल में बर्फबारी" (matches the existing /uttarakhand-mein-barfbari/) |
| /sissu-kaise-jaye/ | 22062 | Hindi Sissu page; linked both ways with /sissu/ |
| /kaza-spiti-kaise-jaye/ | 22076 | Hindi Kaza page; linked both ways with /kaza-spiti/ |

## Inbound (international) pages (7)
GSC (28 days): India is about 97% of impressions. Abroad: US 2,943, UAE 1,567, UK 1,400, Pakistan 955, Bangladesh 795, Singapore 731, Nepal 538, Canada 530.

| URL | ID | Angle |
|---|---|---|
| /himachal-tour-package-from-dubai/ | 21842 | Gulf families: snow in the UAE winter break. e-Visa for residents; visa on arrival for Emiratis. |
| /manali-tour-package-from-bangladesh/ | 21845 | India reopened tourist visas for Bangladeshis on 28 Jun 2026 (IVACs in Dhaka, Chittagong, Sylhet, Khulna, Rajshahi). |
| /himachal-tour-from-nepal/ | 21942 | No visa needed for Nepali citizens; flights and border routes. |
| /himachal-tour-from-singapore/ | 21945 | December holidays for snow, June for Spiti. |
| /himachal-tour-from-uk/ | 22047 | Colonial Shimla and the toy train. e-Visa for UK passport holders. |
| /himachal-tour-from-usa/ | 22060 | Winter break, spring break and summer Spiti. e-Visa; OCI holders need no visa. |
| /himachal-tour-from-canada/ | 22074 | Holidays, March break and summer. e-Visa restored for Canadians. |

## Internal linking
- **Hub /places-to-visit-in-himachal/ (18182):** an "In-depth guides to more Himachal places" block, placed before "How many days do you need".
- **Hindi hub /himachal-ghumne-ki-jagah/ (19380):** an "और जगहों की पूरी गाइड" section, placed before "कितने दिन में क्या देखें", including the Hindi pages.
- **Spiti cross-links:** Langza, Key, Tabo, Nako, Kaza, Dhankar, Kibber and Pin now link to each other.
- **Other links:** Sarahan links to Hatu Peak. Distance chart ↔ Hindi distance page, and Sissu ↔ Hindi Sissu.

## Indexing
42 URLs were submitted via IndexNow (Rank Math Instant Indexing REST): all new posts, the updated posts and both hubs.

## Method and constraints
- **Pipeline:** kit /home/claude/s8/build_post.py → repo branch `ranking` (ranking-kit/) → published via browser REST. The WordPress MCP was down all session.
- **Photos:** about 190 new Wikimedia Commons uploads (9 per place guide), CC BY / BY-SA / CC0 / PD only, all credited. No close-ups of identifiable people; politician images were filtered out.
- **Prices:** only "From ₹14,499 per person (four sharing the car)" from the live Shimla–Manali 5N/6D tour page.
- **Banned-word check:** the kit asserts on every build.
- **Timing:** writes were spaced ≥40 s apart and the health check stayed under 4 s. All WordPress writes stopped at about 23:20, well before the 00:10 quiet window.

## Issues for Sushil
- **Weather feed is stale.** /suzu-weather-feed.json was last updated on 2026-11-09 22:37 UTC, so every live-weather widget site-wide is showing an old forecast. The weather workflow needs your OK.
- **MCP outage.** WordPress, Google Ads, Semrush, Gmail and remote-devices (laptop sync) were all unreachable. Files are staged in outputs/Ranking-2026-11-13 (34 HTML, 34 specs, this doc) and still need copying to the laptop.

## Next ideas
- Chitkul as its own guide (check cannibalisation with /sangla-valley-and-chitkul-kinnaur-trip-guide/ first).
- Karsog, Rohru–Hatkoti, Kotgarh–Thanedar (Commons photos were thin).
- An Australia inbound page.
- A Hindi version of Hatu Peak.
- Review GSC impressions for the new URLs after 7 and 14 days.
