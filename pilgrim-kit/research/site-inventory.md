# Pilgrimage section: existing site inventory and cannibalisation check

**Site:** suzutravels.com · **Checked:** 8 Oct 2026 · **Method:** WordPress MCP (`wp_search` on 24 terms, `wp_get_posts` for `product` + `suzu_package`, `wp_get_seo_meta`, `wp_get_terms`), WebFetch of `/packages/` and `/destination/chardham-tour-packages/`, live `curl` for status codes, robots and canonical tags, and a scan of all 282 sitemap URLs. **Read only. Nothing was changed.**

Search terms run: jyotirlinga, shakti, devi, char dham, chardham, kedarnath, badrinath, amarnath, vaishno, ayodhya, varanasi, kashi, prayagraj, pilgrimage, yatra, temple, darshan, manimahesh, kainchi, tirupati, golden temple, dwarka, somnath, plus spiritual, devotional, jwala, chintpurni, haridwar.
**No content exists** for: Manimahesh (only a mention on mountain pages), Shrikhand, Panch Kedar, Adi Kailash, Kailash Mansarovar (only a mention on the Nepal page), Tirupati (mentions only), Dwarka (none), Somnath (only inside the 12-Jyotirlinga product), Ayodhya (only the combo product), or any single Himachal temple.

"Bookable" means the URL is a package page with the enquiry form and the MWB booking widget (both `product` /tours/ and `suzu_package` /packages/ use the same template).

---

## 1. Relevant URLs

### 1a. Package pages (bookable)

| Type | ID | URL | SEO title (Rank Math) | Focus keyword (Rank Math) | Index | Notes |
|---|---|---|---|---|---|---|
| product | 10876 | /tours/12-jyotirlinga-tour-package/ | 12 Jyotirlinga Tour Package: All 12 Temples in 23 Days | `12 jyotirlinga tour package` | index | `/12-jyotirlinga/` and `/12-jyotirlinga-tour-package/` 301 here |
| product | 10861 | /tours/5-shakti-peeth-tour-package-himachal-5-days-4-nights/ | 5 Shakti Peeth Tour Package Himachal \| Suzu Travels | `5 Shakti Peeth Tour Package Himachal` | index | Naina Devi, Chintpurni, Jwala Ji, Brajeshwari, Chamunda |
| product | 10584 | /tours/spiritual-journey-varanasi-ayodhya-prayagraj-tour-package/ | Varanasi Ayodhya Prayagraj Tour Package \| 6 Days | `Varanasi Ayodhya Prayagraj Tour Package` | index | **Meta description empty**. Not attached to the "Varanasi" destination term. |
| product | 9467 | /tours/holiest-himalayan-pilgrimage-tour/ | *(empty, falls back to "Holiest Himalayan Pilgrimage Tour - Suzu Travels")* | `Holiest Himalayan Pilgrimage Tour, suzu travels` | index | Itinerary is **Kedarnath + Badrinath do dham from Haridwar**, but the focus keyword is a made-up name with no search demand. **Title and description empty.** |
| product | 9483 | /tours/do-dham-gangotri-kedarnath-tour-from-haridwar/ | *(empty)* | `do dham, do dham tour, gangotri kedarnath tour, kedarnath tour from haridwar` | index | **Title and description empty.** Generic "do dham" overlaps 9467. |
| product | 9473 | /tours/do-dham-gangotri-badrinath-tour/ | 6-Day Do Dham Gangotri Badrinath Tour \| Book Now | `Do Dham Gangotri Badrinath Tour, Suzu Travels` | index | Brand name included in the focus keyword list |
| suzu_package | 9905 | /packages/ultimate-char-dham-yatra/ | Char Dham Yatra Package 12 Days from Haridwar \| Suzu | `char dham yatra package` | index | `/char-dham-yatra-packages/` 301s here. Labelled "Bestseller 2026" on /packages/. |
| suzu_package | 9763 | /packages/kashmir-amarnath-by-helicopter/ | Amarnath Yatra by Helicopter 4 Days \| Baltal Route | `amarnath yatra by helicopter` | index | |
| product | 9367 | /tours/amazing-kashmir-vaishno-devi-package/ | Kashmir with Vaishno Devi Tour \| 7 Days \| Suzu Travels | `kashmir vaishno devi, kashmir with vaishno devi` | index | |
| product | 9215 | /tours/panoramic-kashmir-vaishnodevi-economy/ | *(empty)* | `Panoramic Kashmir Vaishnodevi Economy` | index | **Title and description empty.** Near-duplicate of 9367 (economy variant). |
| suzu_package | 9600 | /packages/temple-kerala-tour/ | Kerala Temple Tour \| Guruvayur & Padmanabhaswamy Darshan | `kerala temple tour` | index | |
| suzu_package | 9637 | /packages/guruvayoor-temple-tour-kerala/ | Guruvayoor Temple Tour Package Kerala \| Suzu Travels | `guruvayoor temple tour package` | index | |
| product | 9484 | /tours/rishikesh-adventure-tour-package-4-days/ | *(empty)* | `Dashing Rishikesh, Suzu Travels` | index | Marginal (Ganga Aarti). Out of scope. |
| product | 9189 / 9193 | /tours/impressive-himachal-tour-package-with-amritsar-from-delhi/ · /tours/himachal-amritsar-package-from-chandigarh/ | – | – | index | Include a Golden Temple stop. Link targets for a future Golden Temple page. |

### 1b. Pages, posts and archives (not bookable)

| Type | ID | URL | SEO title | Focus keyword | Index | Notes |
|---|---|---|---|---|---|---|
| page | 11413 | /char-dham-yatra-for-nri/ | Char Dham Yatra for NRIs 2027 \| Packages in USD from Delhi | `char dham yatra for nri` | index | **`/char-dham-yatra/` 301s here** (see issue 1). Also in the International menu. |
| post | 12021 | /char-dham-closing-dates-2026/ | Char Dham Closing Dates 2026: Is October Too Late? | `char dham closing dates 2026` | index | |
| post | 11449 | /char-dham-yatra-status-27-september-2026/ | Char Dham Yatra Status: Resumed 28 Sep 2026, Kedarnath Info | `char dham yatra status` | index | |
| post | 12284 | /uttarakhand-winter-packages-travel-agents/ | Uttarakhand Winter Packages 2026-27: B2B Guide for Agents | `uttarakhand winter packages` | index | Mentions Char Dham closing |
| post | 12444 | /kainchi-dham-registration-2026-new-rules-and-crowd-cap/ | Kainchi Dham Registration 2026: New Rules & Daily Cap | `kainchi dham registration` | index | Published 8 Oct and not yet in post-sitemap. `/kainchi-dham/` 301-guesses here. |
| post | 8623 | /varanasi-spiritual-cultural-guide-2026/ | Varanasi Spiritual and Cultural Guide 2026 \| Suzu Travels | `varanasi spiritual and cultural guide` | index | `/varanasi/` 301-guesses here |
| post | 9786 | /south-india-temple-tour-circuit-guide-2026-steps/ | South India Temple Tour 2026: Packages, Itinerary & Cost | `south india temple tour guide 2026` | index | **Overlaps post 9780** |
| post | 9780 | /south-india-temple-tour-essential-guide-2026-steps/ | South India Temple Tour 2026: 7-Step Planning Guide | `south india temple tour` | index | **Overlaps post 9786** |
| page | 5856 | /uttarakhand/ | Best Uttarakhand Tour Packages 2026 \| Suzu Travels | `uttarakhand tour packages` | index | Lists Char Dham |
| page | 11410 | /uttarakhand-dmc/ | Uttarakhand DMC for Travel Agents \| B2B Char Dham & Corbett | `uttarakhand dmc` | index | B2B |
| page | 11408 | /kashmir-dmc/ | (B2B Kashmir) | – | index | Mentions Amarnath and Vaishno Devi |
| page | 4492 | /char-dham-yatra-packages/ | Browse Best Char Dham Yatra Packages | `char Dham yatra packages` | **noindex** | Live URL 301s to 9905, so the WP page is a leftover |
| page | 10202 | /char-dham-tour-packages-2/ | *(empty)* "Char Dham Tour Packages" | – | **noindex** | **Empty page (0 bytes) returning 200** |
| page | 1078 | /dharamshala/ | Dharamshala Tour Package from Delhi… | `Dharamshala Tour Package` | **noindex** | No conflict |
| tax archive | term 68 | /destination/chardham-tour-packages/ | Chardham Tour Packages: 4 Yatra Trips \| Suzu | – | index | Lists 9473, 9483, 9467, 9905. In the main Destinations menu. |
| tax archive | term 212 | /destination/jyotirlinga-tour-packages/ | Jyotirlinga Tour Packages \| Suzu Travels | – | **index** | **Only 1 item (10876)**: a thin duplicate of the product |
| tax archive | term 97 | /destination/varanasi-tour-packages/ | Varanasi Tour Packages \| Suzu Travels | – | noindex | **Empty** ("No packages found") |
| tax archive | term 75 | /destination/amritsar-tour-packages/ | – | – | index | 2 items |
| product_cat | 83 | /product-category/chardham-tour-packages/ | – | – | noindex | 1 item |

### 1c. Slug availability (live HTTP check)

| Path | Status | Meaning |
|---|---|---|
| /pilgrimage-tours/, /devotional-tours/, /tirth-yatra/, /spiritual-tours/, /teerth-yatra/, /religious-tours/, /pilgrimage/ | 404 | Free |
| /amarnath-yatra/, /shakti-peeth/, /vaishno-devi-yatra/, /kedarnath/, /kedarnath-yatra/, /jyotirlinga/, /manimahesh-yatra/, /nau-devi-yatra/, /do-dham-yatra/, /ayodhya/, /chardham/ | 404 | Free |
| /char-dham-yatra/ | **301 → /char-dham-yatra-for-nri/** | Head-term slug is used up by a redirect |
| /char-dham-tour-packages/ | **301 → homepage** | Treated as a soft 404 by Google |
| /char-dham-yatra-packages/ | 301 → /packages/ultimate-char-dham-yatra/ | OK |
| /12-jyotirlinga/ | 301 → 12-Jyotirlinga product | OK |
| /kainchi-dham/, /varanasi/ | 301 (WordPress slug-guess) → posts 12444 / 8623 | A new page at that slug would override the guess |

---

## 2. Issues found (fix before or with the launch)

1. **`/char-dham-yatra/` redirects to the NRI page.** The 90,500/mo head term's natural slug points at a niche page (`char dham yatra for nri`). When the new Char Dham guide launches, point this redirect at the guide. Check GSC first for which page currently gets impressions for "char dham yatra".
2. **`/char-dham-tour-packages/` 301s to the homepage.** Point it at `/destination/chardham-tour-packages/`.
3. **Empty page 10202** `/char-dham-tour-packages-2/` returns 200 (noindex). Trash it and 301 it to the Chardham archive. Page 4492 is a leftover behind a working redirect and can be trashed safely.
4. **`/destination/jyotirlinga-tour-packages/` is indexable with one package.** It competes with product 10876 for "jyotirlinga tour package". Set it to noindex until it holds 3 or more packages, or canonical it to the product.
5. **`/destination/varanasi-tour-packages/` is empty.** Attach product 10584 to term 97, or delete the term.
6. **Empty SEO titles/descriptions on bookable pilgrimage pages:** 9467, 9483, 9215 (title + description) and 10584 (description).
7. **Focus-keyword hygiene:** 9467's focus keyword "Holiest Himalayan Pilgrimage Tour" has no demand. Retarget it to **`badrinath kedarnath tour package`** (1,600, M) / **`do dham yatra`** (1,000), because that is what the itinerary is. 9483 should drop the generic "do dham" and keep **`gangotri kedarnath tour`**. Remove "Suzu Travels" from the focus-keyword lists of 9473 and 9467.
8. **Two South India temple posts (9780 and 9786) target near-identical terms.** Consolidate one into the other with a 301.
9. **9215 vs 9367** (Kashmir + Vaishno Devi standard vs economy). Give 9215 its own title and focus keyword (e.g. "kashmir vaishno devi budget package") or canonical it to 9367.
10. **The Chardham archive (`/destination/chardham-tour-packages/`) and 9905 both read as "Char Dham packages".** Keep 9905 as owner of `char dham yatra package`. Make the archive title clearly a listing ("All Char Dham & Do Dham Yatra Packages 2027"), and keep the archive out of the new guide's keyword set.

---

## 3. Keyword ownership: who owns what

### 3a. Keywords that existing URLs must keep (new pages link to these and never use them as a focus keyword)

| Keyword(s) (India vol) | Owner URL (ID) | How new pages should use it |
|---|---|---|
| 12 jyotirlinga tour package (3,600) · jyotirlinga tour package (880) · 12 jyotirlinga package (480) · 12 jyotirlinga darshan package (260) | /tours/12-jyotirlinga-tour-package/ (10876) | 12-Jyotirlinga guide and all 11 temple pages use a "Book the complete yatra" CTA with anchor "12 Jyotirlinga tour package" |
| 5 shakti peeth tour package himachal · shakti peeth tour package · himachal devi darshan tour/package (≤30) | /tours/5-shakti-peeth-…/ (10861) | Shakti-Peeth-Himachal guide + 7 Devi temple pages link with that anchor |
| varanasi ayodhya prayagraj tour package (390) · varanasi ayodhya tour package (720) · ayodhya varanasi tour package (480) · kashi ayodhya prayagraj tour package (170) | /tours/spiritual-journey-varanasi-ayodhya-prayagraj-tour-package/ (10584) | Kashi Vishwanath and Ayodhya pages link to it. **The new pages target single-city terms only.** |
| varanasi spiritual/cultural guide, things to do in Varanasi | /varanasi-spiritual-cultural-guide-2026/ (8623) | Kashi Vishwanath page links to it for "what to do in Varanasi" |
| char dham yatra package (33,100) · chardham yatra tour package (8,100) · 4 dham yatra package (4,400) · chardham tour package (2,400) · char dham yatra package from <city> | /packages/ultimate-char-dham-yatra/ (9905); the Chardham archive serves as the listing | Char Dham guide's main CTA |
| char dham yatra for nri | /char-dham-yatra-for-nri/ (11413) | Linked from the Char Dham guide ("Travelling from abroad?") |
| char dham closing dates 2026 · kedarnath closing date (1,600) | /char-dham-closing-dates-2026/ (12021) | Char Dham and Kedarnath pages link to it. They target **2027 opening** dates instead. |
| char dham yatra status | /char-dham-yatra-status-27-september-2026/ (11449) | Linked from a "live status" box |
| do dham gangotri kedarnath · gangotri kedarnath tour · kedarnath tour from haridwar | /tours/do-dham-gangotri-kedarnath-tour-from-haridwar/ (9483) | Kedarnath page CTA |
| do dham gangotri badrinath tour | /tours/do-dham-gangotri-badrinath-tour/ (9473) | Badrinath page CTA |
| badrinath kedarnath tour package (1,600) · do dham yatra (1,000) · kedarnath badrinath package (880) | /tours/holiest-himalayan-pilgrimage-tour/ (9467), **after the retarget in issue 7** | Kedarnath + Badrinath pages CTA |
| amarnath yatra by helicopter (1,600) · amarnath helicopter package (480) · amarnath yatra by helicopter price (1,300) | /packages/kashmir-amarnath-by-helicopter/ (9763) | Amarnath guide's helicopter section links here |
| kashmir vaishno devi package · kashmir with vaishno devi | /tours/amazing-kashmir-vaishno-devi-package/ (9367) | Vaishno Devi guide links as "Add Kashmir" |
| kainchi dham registration | /kainchi-dham-registration-2026-…/ (12444) | New Kainchi Dham page links to it for registration news |
| kerala temple tour · guruvayoor temple tour package · south india temple tour | 9600 · 9637 · 9780/9786 | Hub links to them under "South India" |
| uttarakhand tour packages · uttarakhand dmc | /uttarakhand/ (5856) · /uttarakhand-dmc/ (11410) | Hub and Char Dham guide link up to these |

### 3b. Keywords that are free for the new pages (no existing URL targets them)

| Keyword (India vol) | New owner |
|---|---|
| pilgrimage tours india (110) · tirth yatra (3,600) · teerth yatra (880) · pilgrimage places in india (1,300) · devotional / religious / spiritual tour packages | Hub `/pilgrimage-tours/` |
| 12 jyotirlinga (450,000) · jyotirlingas (165,000) · 12 jyotirlinga name and place (40,500) · 12 jyotirlinga list/map (33,100 each) · jyotirlinga yatra (1,600) | 12 Jyotirlinga guide |
| char dham yatra (90,500) · char dham yatra registration (60,500) · chardham yatra by helicopter (6,600) · char dham yatra 2027 · char dham yatra itinerary (480) | Char Dham Yatra guide |
| kedarnath yatra (8,100) · kedarnath temple (135,000) · kedarnath helicopter booking (49,500) · how to reach kedarnath (3,600) · kedarnath opening date 2027 (1,000) | Kedarnath page |
| badrinath temple (90,500) · badrinath pilgrimage (1,600) · badrinath opening (590) | Badrinath page |
| amarnath yatra (74,000) · amarnath yatra registration (33,100) · amarnath yatra 2027 (210) · amarnath yatra package (1,600) | Amarnath guide |
| vaishno devi yatra (9,900) · vaishno devi tour package (2,400) · vaishno devi helicopter booking (33,100) · vaishno devi darshan (1,600) | Vaishno Devi guide |
| shakti peeth in himachal pradesh (2,400) · shakti peeth in himachal (1,600) · nau devi yatra (90) · 9 devi yatra (140) · himachal devi darshan (260) · 5 devi darshan in himachal (210) | Shakti Peeth Himachal / Nau Devi guide |
| shakti peeth (40,500) · 51 shakti peeth / list (27,100) | 51 Shakti Peeth page |
| panch kedar (40,500) · tungnath (165,000) · rudranath trek (14,800) | Panch Kedar page (cross-link with the adventure section for the trek intent) |
| manimahesh yatra (2,900; "…2026" 4,400) · shrikhand mahadev yatra (880) · adi kailash yatra (2,900) · kailash mansarovar yatra (18,100) | Their own yatra pages |
| kainchi dham (201,000) · baba neem karoli dham (1,600) · kainchi dham tour package (320) | Kainchi Dham page |
| ayodhya tour package (2,900) · ayodhya ram mandir darshan timing (1,300) | Ayodhya page |
| kashi vishwanath temple (cluster 673,000) · kashi vishwanath darshan timing (2,400) · varanasi tour package (4,400) · kashi tour package (3,600) | Kashi Vishwanath page |
| Every individual temple head term (Somnath, Mahakaleshwar, Omkareshwar, …, Naina Devi, Jwalamukhi, Chintpurni, Chamunda, Kangra Devi, Baglamukhi, Mansa Devi, Baijnath, Hidimba, Bhimakali, Baba Balak Nath, Jakhu, Golden Temple) | One temple page each (see keyword-plan.md §4) |

### 3c. Internal-linking rules for launch
- Hub → every circuit page → its temple pages. Every temple page links back up to its circuit and the hub.
- Every guide and temple page links **across** to the package that owns the commercial keyword (table 3a), using that package's focus keyword as the anchor. Package pages get a reciprocal "Read the full guide" link.
- Add the hub to the main menu (Destinations → "Pilgrimage Tours"). Keep the existing "Chardham Tour Packages" archive under it.
