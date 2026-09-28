# Trust documents — suzutravels.com/certificates/

Published 29 Sep 2026 at Sushil's request ("upload them on the website with a link, to build trust").

| File | What | Used on |
|---|---|---|
| `suzu-travels-hp-tourism-registration-certificate.webp` | HP Tourism "Certificate of Registration of Travel Agent" (Dept. of Tourism & Civil Aviation, Govt. of HP). Cert. No. 060925/58761 dated 04-12-2025, Permanent Reg. No. DTO-MND-11-243/2022, renewal due 03-12-2028 | /certificates/ |
| `suzu-travels-gst-registration-certificate.webp` | GST REG-06 page 1 (GSTIN 02BLPPK1401E1ZR, Regular, valid from 13-01-2021). Annexures A/B left out — they add nothing | /certificates/ |
| `suzu-travels-certificates-og.jpg` | 1200×630 share / featured image | /certificates/ (featured + OG) |

- Rendered from the original PDFs at 200 dpi (`pdftoppm`), resized, with a light diagonal watermark
  "suzutravels.com · for verification only" and a credit strip (`src/watermark.py`). The original PDFs are NOT
  in this repo and are not published anywhere.
- Official verification: HP Tourism https://eservices.himachaltourism.gov.in/certificate-validation ·
  GST https://services.gst.gov.in/services/searchtp
- When the HP Tourism registration is renewed (due 03-12-2028), re-render the new certificate with
  `src/watermark.py`, upload it, and swap the image + dates on /certificates/.
