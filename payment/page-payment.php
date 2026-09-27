<?php
/**
 * Template Name: Payment & Booking Page
 *
 * Redesigned 28 Sep 2026. The "Pay online" form comes from the Suzu Payments plugin ([suzu_payment_form]):
 * it creates a WooCommerce order for the amount entered and opens the secure pay page, where the
 * site's Razorpay gateway takes the payment. Previous version: page-payment.php.bak-2026-09-28
 */
get_header();

$suzu_wa_pay  = 'https://wa.me/917087488961?text=' . rawurlencode('Hi Suzu Travels, please share your verified bank / UPI details for my booking payment.');
$suzu_wa_help = 'https://wa.me/917087488961?text=' . rawurlencode('Hi Suzu Travels, I need help with a payment.');
$suzu_faqs = array(
	array( 'Is paying online on this page safe?', 'Yes. The payment itself happens on the secure Razorpay payment screen. Your card details, UPI PIN and banking passwords go only to Razorpay — Suzu Travels never sees or stores them.' ),
	array( 'How much should I pay?', 'Pay the amount your trip planner has confirmed with you. Usually that is a small token or advance to confirm the booking and lock the rate, and the balance before travel, as agreed in writing.' ),
	array( 'Will I get a receipt?', 'Yes. As soon as the payment succeeds you see a confirmation page and get a receipt by email, and your tour manager confirms the payment on WhatsApp.' ),
	array( 'My payment failed but money was deducted. What now?', 'A failed payment that was debited is normally reversed to your account automatically within a few working days. Send us a screenshot on WhatsApp and we will check it with the payment gateway straight away.' ),
	array( 'Can I pay by bank transfer or UPI instead?', 'Yes. Message us on WhatsApp or call +91 70874 88961 and we will share our verified account details. Please always confirm account details with our office before you transfer.' ),
);
?>
<main id="primary" class="sxp">
<style>
.sxp{--g:#122615;--g2:#1B5E20;--g3:#2E7D32;--gold:#D4AF37;--gold2:#B8860B;--cream:#F9FAF5;--line:#E3E9E3;--ink:#1f2a22;--mut:#4A5D4E;font-family:'Plus Jakarta Sans','Sora',system-ui,-apple-system,'Segoe UI',sans-serif;color:var(--ink);background:var(--cream);padding:28px 20px 70px}
.sxp *{box-sizing:border-box}
.sxp-in{max-width:1180px;margin:0 auto}
.sxp h1,.sxp h2,.sxp h3{font-family:'Sora','Plus Jakarta Sans',sans-serif;color:var(--g);letter-spacing:-.02em;margin:0}
.sxp-hero{background:radial-gradient(120% 140% at 0% 0%,#1B5E20 0%,#122615 62%);border-radius:26px;padding:48px 44px 44px;color:#fff;position:relative;overflow:hidden}
.sxp-eyebrow{display:inline-block;font:800 12px/1 'Plus Jakarta Sans',sans-serif;letter-spacing:.16em;text-transform:uppercase;color:var(--g);background:var(--gold);padding:7px 12px;border-radius:999px;margin-bottom:16px}
.sxp-hero h1{color:#fff;font-size:clamp(30px,4vw,48px);line-height:1.08;font-weight:800;max-width:18ch}
.sxp-hero p{color:#E4EDE6;font-size:17px;line-height:1.7;max-width:60ch;margin:14px 0 22px}
.sxp-chips{display:flex;flex-wrap:wrap;gap:8px}
.sxp-chips span{display:inline-flex;align-items:center;gap:7px;background:rgba(255,255,255,.09);border:1px solid rgba(212,175,55,.45);color:#fff;padding:8px 13px;border-radius:999px;font-size:13.5px;font-weight:600}
.sxp-chips span:before{content:"";width:6px;height:6px;border-radius:50%;background:var(--gold)}
.sxp-lock{position:absolute;right:44px;top:44px;width:120px;height:120px;border-radius:30px;background:rgba(255,255,255,.06);border:1px solid rgba(212,175,55,.35);display:flex;align-items:center;justify-content:center}
.sxp-lock svg{width:56px;height:56px}
.sxp-grid{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:22px;margin-top:22px;align-items:start}
.sxp-card{background:#fff;border:1px solid var(--line);border-radius:22px;padding:30px;box-shadow:0 2px 8px rgba(18,38,21,.04),0 14px 34px rgba(18,38,21,.06)}
.sxp-card h2{font-size:clamp(22px,2.3vw,28px);font-weight:800;margin-bottom:6px}
.sxp-card>p{color:var(--mut);margin:0 0 18px;font-size:15.5px;line-height:1.65}
.sxp-methods{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 20px}
.sxp-methods span{font-size:12.5px;font-weight:700;color:var(--g2);background:rgba(46,125,50,.08);border:1px solid rgba(46,125,50,.18);padding:5px 10px;border-radius:8px}
.sp-form{display:flex;flex-direction:column;gap:14px}
.sp-row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.sp-f{display:flex;flex-direction:column;gap:6px;margin:0}
.sp-f>span{font-size:13px;font-weight:700;color:var(--mut)}
.sp-f input,.sp-f select{width:100%;font:500 16px/1.3 'Plus Jakarta Sans',sans-serif;color:var(--ink);background:#F7F9F6;border:1.5px solid var(--line);border-radius:12px;padding:13px 14px;outline:none;transition:border-color .2s,box-shadow .2s;min-height:50px}
.sp-f input:focus,.sp-f select:focus{border-color:var(--g3);box-shadow:0 0 0 4px rgba(46,125,50,.12);background:#fff}
.sp-amt-in{display:flex;align-items:center;background:#F7F9F6;border:1.5px solid var(--line);border-radius:12px;padding-left:16px;transition:border-color .2s,box-shadow .2s}
.sp-amt-in:focus-within{border-color:var(--g3);box-shadow:0 0 0 4px rgba(46,125,50,.12);background:#fff}
.sp-amt-in b{font:800 22px/1 'Sora',sans-serif;color:var(--g)}
.sp-amt-in input{border:0!important;background:transparent!important;box-shadow:none!important;font:800 22px/1.2 'Sora',sans-serif!important}
.sp-btn{margin-top:4px;display:flex;align-items:center;justify-content:center;gap:10px;width:100%;border:0;cursor:pointer;background:linear-gradient(135deg,#D4AF37,#B8860B);color:#122615;font:800 17px/1 'Sora',sans-serif;padding:18px 22px;border-radius:14px;box-shadow:0 12px 26px rgba(184,134,11,.3);transition:transform .2s,box-shadow .2s}
.sp-btn:hover{transform:translateY(-2px);box-shadow:0 16px 32px rgba(184,134,11,.38)}
.sp-note{font-size:13.5px;color:var(--mut);line-height:1.6;margin:2px 0 0}
.sp-err{background:#FDECEC;border:1px solid #F3B7B7;color:#8A1C1C;border-radius:12px;padding:12px 14px;font-size:14.5px;font-weight:600}
.sp-hp{position:absolute!important;left:-9999px!important;width:1px;height:1px;overflow:hidden}
.sxp-side{display:flex;flex-direction:column;gap:22px}
.sxp-steps{list-style:none;margin:14px 0 0;padding:0;display:flex;flex-direction:column;gap:14px;counter-reset:s}
.sxp-steps li{display:grid;grid-template-columns:34px 1fr;gap:12px;align-items:start;font-size:15px;color:var(--mut);line-height:1.55}
.sxp-steps li:before{counter-increment:s;content:counter(s);width:34px;height:34px;border-radius:50%;background:var(--g);color:var(--gold);display:flex;align-items:center;justify-content:center;font-weight:800;font-family:'Sora',sans-serif}
.sxp-steps b{color:var(--g);display:block;font-size:15.5px}
.sxp-safe{background:#FFF8E6;border-color:#EBD9A3}
.sxp-safe ul{margin:12px 0 0;padding-left:18px;color:#6B5A1E;font-size:14.5px;line-height:1.6}
.sxp-safe li{margin-bottom:6px}
.sxp-sec{margin-top:40px}
.sxp-sec>h2{font-size:clamp(24px,2.6vw,32px);font-weight:800;margin-bottom:8px}
.sxp-sec>p{color:var(--mut);font-size:16px;margin:0 0 16px}
.sxp-ways{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.sxp-way{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px}
.sxp-way h3{font-size:18px;margin-bottom:6px}
.sxp-way p{color:var(--mut);font-size:14.5px;line-height:1.6;margin:0 0 14px}
.sxp-way a{display:inline-flex;align-items:center;gap:8px;font-weight:700;font-size:14.5px;color:var(--g2)!important;text-decoration:none!important;border-bottom:2px solid var(--gold);padding-bottom:2px}
.spa-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px;margin-bottom:16px}
.spa-card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px 22px 18px;position:relative;overflow:hidden}
.spa-card:before{content:"";position:absolute;left:0;top:0;right:0;height:5px;background:var(--bank,#1B5E20)}
.spa-bank{font:800 20px/1.2 'Sora',sans-serif;color:var(--bank,#122615);margin:4px 0 12px}
.spa-row,.spa-upi-id{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:10px 0;border-bottom:1px dashed rgba(18,38,21,.12);font-size:14.5px}
.spa-row span,.spa-upi-id span{color:var(--mut)}
.spa-row b,.spa-upi-id b{color:var(--ink);font-weight:700;text-align:right;display:inline-flex;align-items:center;gap:8px;word-break:break-all}
.spa-copy{border:1px solid var(--line);background:var(--cream);color:var(--g2);font:700 12px/1 'Plus Jakarta Sans',sans-serif;padding:6px 9px;border-radius:8px;cursor:pointer}
.spa-copy:hover{background:var(--g);color:#fff}
.spa-upi{display:flex;flex-direction:column;align-items:center;gap:8px;margin-top:14px}
.spa-qr{width:190px;height:190px;padding:10px;background:#fff;border:1px solid var(--line);border-radius:14px}
.spa-qr svg{width:100%;height:100%;display:block}
.spa-upi-id{width:100%;border-bottom:0}
.spa-app{display:none;font-weight:800;font-size:14.5px;color:#fff!important;background:var(--g2);padding:11px 18px;border-radius:12px;text-decoration:none!important}
@media(hover:none) and (pointer:coarse){.spa-app{display:inline-flex}}
.sxp-terms{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.sxp-term{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 20px}
.sxp-term h3{font-size:16.5px;margin-bottom:6px}
.sxp-term p{color:var(--mut);font-size:14.5px;line-height:1.6;margin:0}
.sxp-faqs{background:#fff;border:1px solid var(--line);border-radius:18px;padding:6px 22px}
.sxp-faqs details{border-bottom:1px solid var(--line)}
.sxp-faqs details:last-child{border-bottom:0}
.sxp-faqs summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:18px 0;font-weight:700;color:var(--g);font-size:16px}
.sxp-faqs summary::-webkit-details-marker{display:none}
.sxp-faqs summary:after{content:"+";flex:none;width:30px;height:30px;border-radius:50%;background:var(--cream);border:1px solid var(--line);display:flex;align-items:center;justify-content:center;color:var(--gold2);font-size:20px;transition:transform .2s}
.sxp-faqs details[open] summary:after{transform:rotate(45deg)}
.sxp-faqs details p{margin:0 0 18px;color:var(--mut);font-size:15px;line-height:1.65}
.sxp-links{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}
.sxp-links a{font-size:14px;font-weight:700;color:var(--g)!important;text-decoration:none!important;padding:10px 16px;border-radius:999px;border:1px solid var(--line);background:#fff}
.sxp-links a:hover{background:var(--g);color:#fff!important}
@media(max-width:980px){.sxp-grid{grid-template-columns:1fr}.sxp-ways{grid-template-columns:1fr}.sxp-terms{grid-template-columns:1fr}.sxp-lock{display:none}}
@media(max-width:600px){.sxp{padding:16px 12px 50px}.sxp-hero{padding:30px 20px}.sxp-card{padding:22px 18px}.sp-row{grid-template-columns:1fr}}
</style>
<div class="sxp-in">
  <section class="sxp-hero">
    <span class="sxp-eyebrow">Payments</span>
    <h1>Secure Booking &amp; Payments</h1>
    <p>Pay your token, advance or balance online in a minute. The payment is processed securely by Razorpay, and you get an instant receipt by email.</p>
    <div class="sxp-chips"><span>UPI · Cards · Net banking · Wallets</span><span>Secured by Razorpay</span><span>Instant email receipt</span><span>A small token locks today&rsquo;s rate</span></div>
    <div class="sxp-lock" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="10" width="16" height="11" rx="2.5"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/><circle cx="12" cy="15.5" r="1.4"/></svg></div>
  </section>

  <section class="sxp-grid" id="pay-online">
    <div class="sxp-card">
      <h2>Pay online</h2>
      <p>Enter the amount confirmed by your trip planner. On the next screen choose UPI, card, net banking or wallet.</p>
      <div class="sxp-methods"><span>UPI</span><span>Google Pay</span><span>PhonePe</span><span>Paytm</span><span>Visa</span><span>Mastercard</span><span>RuPay</span><span>Net banking</span></div>
      <?php
      if ( shortcode_exists( 'suzu_payment_form' ) ) {
          echo do_shortcode( '[suzu_payment_form]' );
      } else {
          echo '<p><a class="sp-btn" href="' . esc_url( $suzu_wa_help ) . '" target="_blank" rel="noopener">Get your payment link on WhatsApp →</a></p>';
      }
      ?>
    </div>
    <aside class="sxp-side">
      <div class="sxp-card">
        <h3>How it works</h3>
        <ol class="sxp-steps">
          <li><div><b>Enter your details and amount</b>Name, mobile, email, your trip and the amount agreed with your planner.</div></li>
          <li><div><b>Pay on the secure screen</b>Razorpay opens with UPI, cards, net banking and wallets.</div></li>
          <li><div><b>Get your confirmation</b>An email receipt instantly, and your tour manager confirms on WhatsApp.</div></li>
        </ol>
      </div>
      <div class="sxp-card sxp-safe">
        <h3>Pay safely</h3>
        <ul>
          <li>Online payments on this page go only to Suzu Travels, through Razorpay.</li>
          <li>We never ask for your OTP, UPI PIN or card CVV on a call or message.</li>
          <li>Before any bank or UPI transfer, confirm the account details with our office on <b>+91 70874 88961</b>.</li>
        </ul>
      </div>
    </aside>
  </section>

  <?php $suzu_accounts = shortcode_exists( 'suzu_payment_accounts' ) ? do_shortcode( '[suzu_payment_accounts]' ) : ''; ?>
  <section class="sxp-sec" id="bank-upi">
    <?php if ( $suzu_accounts ) : ?>
    <h2>Bank transfer &amp; UPI</h2>
    <p>Pay by NEFT, IMPS, RTGS or any UPI app to our official accounts below. After paying, send the screenshot on WhatsApp so we can match it to your booking.</p>
    <?php echo $suzu_accounts; // phpcs:ignore -- escaped inside the plugin ?>
    <div class="sxp-ways" style="grid-template-columns:repeat(2,1fr)">
      <div class="sxp-way"><h3>Paid by transfer or UPI?</h3><p>Share the payment screenshot with your name and trip so your tour manager can confirm it.</p><a href="<?php echo esc_url( 'https://wa.me/917087488961?text=' . rawurlencode( 'Hi Suzu Travels, I have paid for my booking. Sharing the screenshot.' ) ); ?>" target="_blank" rel="noopener">Send screenshot on WhatsApp →</a></div>
      <div class="sxp-way"><h3>Paying from abroad</h3><p>Travelling from outside India? Tell us your country and we will suggest the easiest way to pay for your trip.</p><a href="<?php echo esc_url( $suzu_wa_help ); ?>" target="_blank" rel="noopener">Ask on WhatsApp →</a></div>
    </div>
    <?php else : ?>
    <h2>Other ways to pay</h2>
    <p>Prefer a transfer, or paying from outside India? We will share verified details directly with you.</p>
    <div class="sxp-ways">
      <div class="sxp-way"><h3>Bank transfer (NEFT / IMPS / RTGS)</h3><p>Ask us for our current account details on WhatsApp. Share the transfer screenshot afterwards so we can match it to your booking.</p><a href="<?php echo esc_url( $suzu_wa_pay ); ?>" target="_blank" rel="noopener">Get bank details on WhatsApp →</a></div>
      <div class="sxp-way"><h3>UPI or QR code</h3><p>We can send our UPI ID or QR code on WhatsApp, confirmed by our office for your booking.</p><a href="<?php echo esc_url( $suzu_wa_pay ); ?>" target="_blank" rel="noopener">Get UPI details on WhatsApp →</a></div>
      <div class="sxp-way"><h3>Paying from abroad</h3><p>Travelling from outside India? Tell us your country and we will suggest the easiest way to pay for your trip.</p><a href="<?php echo esc_url( $suzu_wa_help ); ?>" target="_blank" rel="noopener">Ask on WhatsApp →</a></div>
    </div>
    <?php endif; ?>
  </section>

  <section class="sxp-sec" id="payment-terms">
    <h2>Payment terms</h2>
    <p>Simple rules, so there are no surprises. Your written booking confirmation always has the final details for your trip.</p>
    <div class="sxp-terms">
      <div class="sxp-term"><h3>Confirming your booking</h3><p>Your booking is confirmed when your token or advance is received and we send you the confirmation in writing, with hotels and dates named. The token holds the rate quoted to you.</p></div>
      <div class="sxp-term"><h3>Balance payment</h3><p>The balance is paid before your trip starts, on the date written in your booking confirmation. You can pay it on this page, by bank transfer or by UPI.</p></div>
      <div class="sxp-term"><h3>Receipts</h3><p>Every online payment gets an email receipt straight away. For transfers and UPI, we confirm receipt on WhatsApp once the amount reaches our account. A detailed invoice is available on request.</p></div>
      <div class="sxp-term"><h3>Cancellations and refunds</h3><p>Cancellations and refunds follow our <a href="<?php echo esc_url( home_url( '/cancellation-and-refund-policy/' ) ); ?>">Cancellation &amp; Refund Policy</a>. Approved refunds are returned to the original payment method.</p></div>
      <div class="sxp-term"><h3>Official accounts only</h3><p>Pay only through this page or to the accounts shown here. We never ask you to pay into a personal account. If anyone does, call us on +91 70874 88961 before paying.</p></div>
      <div class="sxp-term"><h3>Charges and currency</h3><p>Prices and payments are in Indian rupees unless your quote says otherwise. Any charges your own bank or card adds are separate from your trip cost.</p></div>
    </div>
  </section>

  <section class="sxp-sec">
    <h2>Payment questions</h2>
    <div class="sxp-faqs">
      <?php foreach ( $suzu_faqs as $f ) : ?>
        <details><summary><?php echo esc_html( $f[0] ); ?></summary><p><?php echo esc_html( $f[1] ); ?></p></details>
      <?php endforeach; ?>
    </div>
    <div class="sxp-links">
      <a href="<?php echo esc_url( home_url( '/cancellation-and-refund-policy/' ) ); ?>">Cancellation &amp; refund policy</a>
      <a href="<?php echo esc_url( home_url( '/terms-and-conditions/' ) ); ?>">Terms &amp; conditions</a>
      <a href="<?php echo esc_url( home_url( '/privacy-policy/' ) ); ?>">Privacy policy</a>
      <a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>">Contact us</a>
    </div>
  </section>
</div>
<script type="application/ld+json"><?php
echo wp_json_encode( array(
	'@context'   => 'https://schema.org',
	'@type'      => 'FAQPage',
	'mainEntity' => array_map( function ( $f ) {
		return array( '@type' => 'Question', 'name' => $f[0], 'acceptedAnswer' => array( '@type' => 'Answer', 'text' => $f[1] ) );
	}, $suzu_faqs ),
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
?></script>
</main>
<?php get_footer(); ?>
