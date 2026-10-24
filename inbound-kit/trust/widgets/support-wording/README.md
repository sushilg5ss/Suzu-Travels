# support-wording (24 Oct 2026) — FIX NEEDED from Reviewer 23 Oct

Hand-built "24/7" support claims on 11411/11412 aligned to the Terms wording
(/terms-and-conditions/, updated 28 Sep 2026: "Call or WhatsApp +91 70874 88961 before and during your trip").
24/7 availability is not documented anywhere in the policies, so it is not claimed.

Changes (wp_replace_in_page, dry run first, expected_count guard; no undo tokens — revert = swap strings back):
| page | before | after (marked) |
|---|---|---|
| 11411 hero badge | `<span class="si-badge">🕐 24/7 local support</span>` | `<!--szt:support-wording--><span class="si-badge">🕐 Support before and during your trip</span><!--/szt:support-wording-->` |
| 11411 booking card | `<b>24/7 on-trip support</b>` + `<p>A real person at our office on WhatsApp day and night while you are in India.</p>` | `<b><!--szt:support-wording-2-->On-trip support</b>` + `<p>Call or WhatsApp our office on +91 70874 88961 before and during your trip.<!--/szt:support-wording-2--></p>` |
| 11412 hero badge | `<span class="si-badge">🕐 24/7 WhatsApp support</span>` | `<!--szt:support-wording--><span class="si-badge">🕐 Direct WhatsApp to our office</span><!--/szt:support-wording-->` |
| 11412 includes card | `<b>24/7 WhatsApp</b>` + `<p>A direct line to our team in India for anything you need on the road.</p>` | `<b><!--szt:support-wording-2-->Direct WhatsApp</b>` + `<p>A direct line to our team in India (+91 70874 88961) before and during your trip.<!--/szt:support-wording-2--></p>` |
| 11412 FAQ (HTML + FAQPage JSON-LD, ×2, no markers) | `a 24/7 WhatsApp line to our team` | `a direct WhatsApp line to our team before and during the trip` |

Left alone (not this lane): site-wide header/mobile-menu `<span class="pro-badge">24/7</span>` next to the phone number (theme header).
