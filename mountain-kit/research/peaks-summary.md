# Mountains of India – dataset summary (peaks.json)

Compiled 1 Oct 2026. The data comes mainly from Wikipedia. Most first-ascent facts were checked against a second source: the Himalayan Journal (himalayanclub.org), the AAC, Explorersweb, and news reports for events in 2019–2026.

## Scope
- **156 peaks.** The file covers only Indian-administered territory. Border peaks shared with Nepal, Tibet/China or Pakistan (along the AGPL) are included.
- **Schema.** Every record has all the requested fields. There is one extra field, `height_alternates_m`, which lists other heights that sources give.
- **`india_rank`** is the national rank in Wikipedia's "Highest major summits in India" table, which only ranks summits with at least 500 m prominence. It is filled for the top-50 entries only and is `null` otherwise. K12 is missing from that table, so its rank is `null`.
- **`status`** has four values:
  - `closed`: formally closed to climbing.
  - `restricted`: in a military zone (Siachen/AGPL), treated as sacred, or a Sikkim border peak where permits are generally not issued.
  - `unclimbed`: a source states that no ascent is recorded.
  - `climbed`: everything else.

  The first ascent is still recorded for restricted peaks where one exists.
- **`difficulty = "trekking peak"`** also covers non-technical hiking summits in the 3,000–4,000 m bands.

## Counts in this dataset

| Band | Count |
|---|---|
| 8000+ | 1 |
| 7000–7999 | 48 |
| 6000–6999 | 74 |
| 5000–5999 | 18 |
| 4000–4999 | 6 |
| 3000–3999 | 9 |
| **Total** | **156** |

| State / UT | Peaks | climbed | restricted | unclimbed | closed |
|---|---|---|---|---|---|
| Uttarakhand | 60 | 57 | 2 | 0 | 1 (Nanda Devi) |
| Ladakh | 34 | 23 | 9 | 1 | 1 (Stok Kangri) |
| Himachal Pradesh | 26 | 23 | 1 | 2 | 0 |
| Sikkim | 19 | 4 | 12 | 3 | 0 |
| Jammu & Kashmir | 10 | 9 | 1 | 0 | 0 |
| Arunachal Pradesh | 5 | 3 | 0 | 2 | 0 |
| West Bengal | 2 | 2 | 0 | 0 | 0 |
| **Total** | **156** | **121** | **25** | **8** | **2** |

- Two peaks straddle a boundary. Nun is counted under J&K and Chiling I under Ladakh.
- 111 of the 156 entries have a first-ascent year. The other 45 are `null`. These are mostly trekking peaks where no first-ascent record was found, plus the unclimbed and sacred peaks.
- By difficulty: 93 technical, 27 moderate, 24 trekking peak, 12 extreme.
- Open to foreigners: 105 yes, 46 restricted, 5 no.

## Authoritative totals found (not counts of this dataset)
- **Wikipedia "List of mountains in India"** ranks 38 summits of 7,000 m or more that have at least 500 m prominence (Kangchenjunga down to Chong Kumdan Ri II, 7,004 m). Lower-prominence 7,000 m points such as Abi Gamin, Gimmigela and Talung are excluded from that count.
- **Wikipedia "List of highest mountains on Earth"** says India has **27 of the world's peaks over 7,200 m**, counting subsidiary and border peaks. By comparison, China has 50, Pakistan 42 and Nepal 34.
- **Wikipedia state lists** (partial lists, not official counts):
  - Uttarakhand list: 204 peaks, of which 15 are at least 7,000 m and 188 are 6,000–6,999 m.
  - Ladakh list: 25 at least 7,000 m and 18 of 6,000 m or more (clearly incomplete).
  - Himachal list: about 51 of 6,000 m or more.
- **MHA/IMF, August 2019.** 137 peaks were opened to foreign climbers, who can now apply directly to the IMF: Uttarakhand 51, Himachal 47, Sikkim 24, J&K (then including Ladakh) 15. IMF then said it would not issue permits for Sikkim's sacred peaks, including Kangchenjunga.
- **Uttarakhand, 3 Feb 2026.** 83 peaks were opened with government fees waived for Indian climbers; foreigners still pay IMF fees. Named peaks: Kamet, Nanda Devi **East**, the Chaukhamba and Trisul groups, Shivling, Satopanth, Changabang, Panchachuli and Nilkantha. The main Nanda Devi summit was not named.
- **Not found:** an authoritative total for India's 6,000 m peaks, or a single official IMF count of all open peaks.

## Key facts
- **Highest in India:** Kangchenjunga, 8,586 m, on the Sikkim–Nepal border. It is the world's 3rd highest.
- **Highest entirely within India:** Nanda Devi, 7,816 m (some sources give 7,817 m). It has been closed since 1983.
- **Highest in each state or UT:**
  - Sikkim: Kangchenjunga, 8,586 m.
  - Uttarakhand: Nanda Devi, 7,816 m.
  - Ladakh: Saltoro Kangri, 7,742 m. It sits on the India–Pakistan AGPL in the Siachen conflict zone. India also claims K2 (8,611 m), which is administered by Pakistan. The highest summit fully under Indian control is Saser Kangri I, 7,672 m.
  - Jammu & Kashmir: Nun, 7,135 m, per Wikipedia. The Nun Kun massif straddles the J&K–Ladakh boundary and is reached from the Suru valley in Kargil. The highest point in the Kishtwar region is Sickle Moon, 6,574 m.
  - Arunachal Pradesh: Kangto. Wikipedia gives 7,090 m; other sources give 7,060 or 7,042 m.
  - Himachal Pradesh: Reo Purgyil, 6,816 m.
  - West Bengal: Sandakphu, 3,636 m.
- **Unclimbed peaks, backed by a source:**
  - Apsarasas Kangri II and III, 7,239 m (IMF lists them as "virgin").
  - Shudu Tsenpa, 7,024 m (Sikkim; no recorded attempts).
  - Zemu Gap Peak, about 7,780 m (a Sikkim subsidiary summit; no known attempts).
  - Nyegyi Kansang, 7,047 m. A 1995 Indian Army claim is disputed, and Wikipedia says the peak remains unclimbed.
  - Chiumo, 6,890 m (Arunachal; no documented ascents).
  - Chombu, 6,362 m (Sikkim; no documented ascents).
  - Manimahesh Kailash, 5,653 m (sacred; described as a "virgin peak").
  - Parvati Parbat, 6,633 m. No documented ascent was found, so treat this one as uncertain.
- **Recently climbed for the first time:**
  - Kangto, late 2025 (Indian Army).
  - Tsangyang Gyatso, 2024 (NIMAS).
  - Shahi Kangri, 2022.
  - Janhukut, 2018.
  - Plateau Peak and Chamshen Kangri, 2013.
  - Saser Kangri II East, 2011 (Piolet d'Or).
- **Sacred or not climbed by tradition:** Kangchenjunga (summiteers stop just short of the top), Pandim, Om Parvat, Adi Kailash, Amarnath, Manimahesh and Shrikhand.
- **Hardest and most technical:**
  - Changabang
  - Thalay Sagar
  - Meru Central (Shark's Fin, first climbed 2011)
  - Shivling
  - Saser Kangri II East
  - Bhagirathi III (west face)
  - Kalanka (north face)
  - Janhukut
  - Talung (NNW pillar)
  - Nanda Devi (south ridge)

  Kamet, Satopanth, Trisul and Kedar Dome are, by contrast, relatively straightforward for their height.
- **Other records:**
  - Trisul, 1907, was the first 7,000 m summit ever climbed.
  - Kamet, 1931, was the first summit over 25,000 ft.
  - Pauhunri, 1911, was the highest summit climbed until 1928.
  - Jongsong was the highest summit climbed from 1930 to 1931.
  - Draupadi Ka Danda II was the site of an avalanche that killed 29 NIM climbers in 2022.
  - Stok Kangri has been closed since 2020.

## Caveats and uncertain values
1. **Heights disagree between sources.** Where they differ, the most-cited figure is used and the others are listed:
   - Nanda Devi 7,816/7,817 m.
   - Kangto 7,090/7,060/7,042 m.
   - Hardeol 7,151/7,161 m.
   - Thalay Sagar 6,904 m. The India list's 6,984 m looks like an error.
   - Kedarnath 6,940/6,968 m.
   - Satopanth 7,075/7,084 m.
   - Hanuman Tibba 5,982/5,932/5,860 m.
   - Shrikhand Mahadev 5,227/5,182/5,660 m.
   - Stok Kangri 6,153/6,136/6,155 m.
   - Kang Yatse I 6,400/6,496 m.
   - Kangchenjau 6,889/6,913 m.
   - Chamshen Kangri 7,017/6,950 m.
   - Pangarchulla 4,575/4,590 m.
   - Patalsu 4,470/4,250 m.
   - Dzo Jongo 6,280/6,240 m.
   - Zemu Gap Peak's height of about 7,780 m comes from Wikipedia only.
2. **Status can change.** Stok Kangri closure: operators report it still closed in 2025–26, but no formal reopening or extension date was found. The Sikkim sacred-peak restrictions (2001 ban; some peaks reopened in 2005–06) should be checked with the IMF or Sikkim before publishing. Siachen/AGPL peaks need Army/MHA clearance.
3. **Disputed ascents:**
   - Nyegyi Kansang: the 1995 claim is disputed.
   - Gurudongmar: the 1936 party may have climbed only the west summit; otherwise the first ascent was in 1991.
   - Nilkantha: a 1961 claim was discredited, so 1974 is used.
   - Gya: earlier claims were on subsidiary summits; 1998 is accepted.
   - Nanda Khat: Wikipedia contradicts itself (1931 vs 1972). 1972 is used.
   - Vasuki Parbat: the 1980 ITBP ascent is only a claim.
   - Chiling I: the 1977 ascent is "probable".
   - Shikar Beh: the 1973 Japanese ascent is only a claim.
   - Kabru: the 1883 claim is disputed. C.R. Cooke soloed the 7,338 m summit in 1935. The Indian Army climbed 7,412 m Kabru North in 1994.
   - Apsarasas: sources disagree on which summit is highest.
4. **Weak sourcing:**
   - Pandim and Om Parvat: no first-ascent record was found. They are marked restricted, not "unclimbed".
   - Shilla: the often-quoted 1860 surveyor ascent was not verified.
   - Lungser Kangri 1995 comes from a Wikipedia infobox only.
   - Gorichen: 2024 is described as the first *civilian* ascent. Earlier army ascents were not found, so the first-ascent year is `null`.
5. **Deliberately left out:** Kangju Kangri, Papsura, Dharamsura, Rishi Pahar, Sakang, Mt Hardinge, Langpo, Chorten Nyima Ri, Golep Kangri and Kinnaur Kailash. Their status or first-ascent facts could not be verified.
6. **Band counts.** The 4,000 m and 5,000 m bands have fewer entries than targeted (6 and 18), because many "4,000 m summits" marketed on treks are actually passes or ridges.
7. **Other judgement calls:**
   - `best_season`, `base` and `difficulty` are editorial generalisations, not sourced facts.
   - `open_to_foreigners` reflects general IMF/MHA practice. Most Ladakh and Karakoram peaks need an Inner Line/Protected Area Permit and often a joint expedition. Always check the current IMF list.
