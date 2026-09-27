<?php
/**
 * Plugin Name: Suzu Payments
 * Description: "Pay online" form for the Payment page. The guest enters name, phone, email, trip reference and amount; the plugin creates a WooCommerce order for that amount and sends them to the secure WooCommerce pay page, where the site's existing Razorpay / PhonePe gateways take the payment. Shortcode: [suzu_payment_form]
 * Version: 1.1.0
 * Author: Suzu Travels
 * Requires PHP: 7.4
 * Requires Plugins: woocommerce
 * License: GPLv2 or later
 */

if (!defined('ABSPATH')) {
    exit;
}

final class Suzu_Payments
{
    const VERSION = '1.1.0';
    const VIA = 'suzu-pay';
    const MIN = 100;
    const MAX = 500000;
    const CRON = 'suzu_pay_cleanup';
    const TYPES = ['token' => 'Token / advance', 'balance' => 'Balance payment', 'full' => 'Full payment', 'other' => 'Other (cab, hotel, add-on)'];

    public static function init()
    {
        add_shortcode('suzu_payment_form', [__CLASS__, 'shortcode']);
        add_shortcode('suzu_payment_accounts', [__CLASS__, 'accounts_shortcode']);
        add_action('admin_menu', function () {
            add_options_page('Suzu Payments', 'Suzu Payments', 'manage_options', 'suzu-payments', [__CLASS__, 'admin_page']);
        });
        add_action('admin_post_suzu_pay_accounts_save', [__CLASS__, 'admin_save']);
        add_filter('plugin_action_links_' . plugin_basename(__FILE__), function ($l) {
            array_unshift($l, '<a href="' . esc_url(admin_url('options-general.php?page=suzu-payments')) . '">Bank &amp; UPI details</a>');
            return $l;
        });
        add_action('admin_post_nopriv_suzu_pay_submit', [__CLASS__, 'submit']);
        add_action('admin_post_suzu_pay_submit', [__CLASS__, 'submit']);
        add_action(self::CRON, [__CLASS__, 'cleanup']);
        // guest orders created by this form open straight on the pay page (no email re-check step)
        add_filter('woocommerce_order_email_verification_required', function ($required, $order = null) {
            if ($order instanceof WC_Order && $order->get_created_via() === self::VIA) {
                return false;
            }
            return $required;
        }, 10, 2);
        // a form payment has no products, so hide the empty "Subtotal ₹0" row on the pay / thank-you pages and emails
        add_filter('woocommerce_get_order_item_totals', function ($rows, $order) {
            if ($order instanceof WC_Order && $order->get_created_via() === self::VIA) {
                unset($rows['cart_subtotal']);
            }
            return $rows;
        }, 10, 2);
        add_action('init', function () {
            if (!wp_next_scheduled(self::CRON)) {
                wp_schedule_event(time() + HOUR_IN_SECONDS, 'daily', self::CRON);
            }
        });
    }

    public static function deactivate()
    {
        wp_clear_scheduled_hook(self::CRON);
    }

    /* ------------------------------------------------------------ form */

    public static function shortcode()
    {
        if (!function_exists('wc_create_order')) {
            return '<p>Online payment is temporarily unavailable. Please WhatsApp us on +91 70874 88961.</p>';
        }
        $err = isset($_GET['pay_error']) ? sanitize_key(wp_unslash($_GET['pay_error'])) : '';
        $msgs = [
            'name' => 'Please enter your full name.', 'phone' => 'Please enter a valid mobile number.', 'email' => 'Please enter a valid email address.',
            'amount' => 'Please enter an amount between ₹' . self::inr(self::MIN) . ' and ₹' . self::inr(self::MAX) . '.',
            'busy' => 'Too many attempts from this connection. Please try again in a while or WhatsApp us.', 'order' => 'We could not start the payment. Please try again or WhatsApp us.',
        ];
        $types = '';
        foreach (self::TYPES as $k => $v) {
            $types .= '<option value="' . esc_attr($k) . '">' . esc_html($v) . '</option>';
        }
        self::enqueue_js();
        ob_start(); ?>
        <form class="sp-form" method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>" novalidate>
            <input type="hidden" name="action" value="suzu_pay_submit">
            <input type="hidden" name="sp_t" value="" class="sp-t">
            <div class="sp-hp" aria-hidden="true"><label>Leave empty<input type="text" name="sp_website" tabindex="-1" autocomplete="off"></label></div>
            <?php if ($err && isset($msgs[$err])) : ?><div class="sp-err" role="alert"><?php echo esc_html($msgs[$err]); ?></div><?php endif; ?>
            <div class="sp-row">
                <label class="sp-f"><span>Full name *</span><input type="text" name="sp_name" required maxlength="80" autocomplete="name" placeholder="As on your booking"></label>
                <label class="sp-f"><span>Mobile (WhatsApp) *</span><input type="tel" name="sp_phone" required maxlength="20" autocomplete="tel" placeholder="+91 98xxx xxxxx" inputmode="tel"></label>
            </div>
            <div class="sp-row">
                <label class="sp-f"><span>Email *</span><input type="email" name="sp_email" required maxlength="100" autocomplete="email" placeholder="Receipt is sent here"></label>
                <label class="sp-f"><span>Payment for</span><select name="sp_type"><?php echo $types; // phpcs:ignore ?></select></label>
            </div>
            <label class="sp-f"><span>Trip / booking reference</span><input type="text" name="sp_ref" maxlength="120" placeholder="e.g. Kashmir 6D/5N, 12 Oct, tour manager Anshul"></label>
            <label class="sp-f sp-amt"><span>Amount (₹) *</span><div class="sp-amt-in"><b>₹</b><input type="number" name="sp_amount" required min="<?php echo (int) self::MIN; ?>" max="<?php echo (int) self::MAX; ?>" step="1" inputmode="numeric" placeholder="Agreed amount"></div></label>
            <button type="submit" class="sp-btn">Continue to secure payment <span aria-hidden="true">→</span></button>
            <p class="sp-note">You will pay on the next screen through <b>Razorpay</b> or <b>PhonePe</b> (UPI, cards, net banking, wallets). Suzu Travels never sees your card or UPI PIN. A receipt is emailed to you and your tour manager confirms on WhatsApp.</p>
        </form>
        <?php
        return ob_get_clean();
    }

    public static function inr($n)
    {
        $n = (string) (int) round($n);
        if (strlen($n) <= 3) {
            return $n;
        }
        $last3 = substr($n, -3);
        $rest = substr($n, 0, -3);
        return preg_replace('/\B(?=(\d{2})+(?!\d))/', ',', $rest) . ',' . $last3;
    }

    private static function enqueue_js()
    {
        static $done = false;
        if ($done) {
            return;
        }
        $done = true;
        wp_register_script('suzu-pay', false, [], self::VERSION, true);
        wp_enqueue_script('suzu-pay');
        wp_add_inline_script('suzu-pay', "(function(){var forms=document.querySelectorAll('.sp-form');for(var i=0;i<forms.length;i++)(function(f){var mark=function(){var t=f.querySelector('.sp-t');if(!t||t.value)return;t.value='h-'+Math.random().toString(36).slice(2);};f.addEventListener('input',mark);f.addEventListener('focusin',mark);f.addEventListener('pointerdown',mark);})(forms[i]);})();");
    }

    /* ------------------------------------------- bank & UPI details (owner-entered) */

    const OPT_ACC = 'suzu_pay_accounts';
    const ACC_FIELDS = ['bank' => 'Bank name', 'name' => 'Account name', 'number' => 'Account number', 'ifsc' => 'IFSC code', 'branch' => 'Branch', 'type' => 'Account type', 'upi' => 'UPI ID', 'qr' => 'QR code image URL (optional)'];

    public static function accounts()
    {
        $a = get_option(self::OPT_ACC);
        $def = [['bank' => 'State Bank of India', 'color' => '#0066cc'], ['bank' => 'HDFC Bank', 'color' => '#004b8e']];
        $out = [];
        for ($i = 0; $i < 2; $i++) {
            $row = is_array($a) && isset($a[$i]) && is_array($a[$i]) ? $a[$i] : [];
            $out[] = array_merge(['bank' => $def[$i]['bank'], 'name' => '', 'number' => '', 'ifsc' => '', 'branch' => '', 'type' => '', 'upi' => '', 'qr' => '', 'color' => $def[$i]['color']], $row);
        }
        return $out;
    }

    public static function accounts_shortcode()
    {
        $accs = array_filter(self::accounts(), function ($a) {
            return trim($a['number']) !== '' || trim($a['upi']) !== '' || trim($a['qr']) !== '';
        });
        if (!$accs) {
            return '';
        }
        $needs_qr = false;
        $html = '<div class="spa-grid">';
        foreach ($accs as $a) {
            $html .= '<div class="spa-card" style="--bank:' . esc_attr($a['color']) . '"><div class="spa-bank">' . esc_html($a['bank']) . '</div>';
            if (trim($a['number']) !== '') {
                foreach (['name', 'number', 'ifsc', 'branch', 'type'] as $k) {
                    if (trim($a[$k]) === '') {
                        continue;
                    }
                    $copy = in_array($k, ['number', 'ifsc'], true) ? '<button type="button" class="spa-copy" data-copy="' . esc_attr($a[$k]) . '">Copy</button>' : '';
                    $html .= '<div class="spa-row"><span>' . esc_html(self::ACC_FIELDS[$k]) . '</span><b>' . esc_html($a[$k]) . $copy . '</b></div>';
                }
            }
            $upi = trim($a['upi']);
            if ($upi !== '' || trim($a['qr']) !== '') {
                $html .= '<div class="spa-upi">';
                if (trim($a['qr']) !== '') {
                    $html .= '<img class="spa-qr" src="' . esc_url($a['qr']) . '" alt="' . esc_attr($a['bank'] . ' UPI QR code') . '" loading="lazy">';
                } elseif ($upi !== '') {
                    $needs_qr = true;
                    $uri = 'upi://pay?pa=' . rawurlencode($upi) . '&pn=' . rawurlencode('Suzu Travels') . '&cu=INR';
                    $html .= '<div class="spa-qr" data-upi="' . esc_attr($uri) . '" role="img" aria-label="' . esc_attr($a['bank'] . ' UPI QR code') . '"></div>';
                }
                if ($upi !== '') {
                    $uri = 'upi://pay?pa=' . rawurlencode($upi) . '&pn=' . rawurlencode('Suzu Travels') . '&cu=INR';
                    $html .= '<div class="spa-upi-id"><span>UPI ID</span><b>' . esc_html($upi) . '<button type="button" class="spa-copy" data-copy="' . esc_attr($upi) . '">Copy</button></b></div>'
                        . '<a class="spa-app" href="' . esc_attr($uri) . '">Open in UPI app</a>';
                }
                $html .= '</div>';
            }
            $html .= '</div>';
        }
        $html .= '</div>';
        wp_register_script('suzu-pay-acc', false, [], self::VERSION, true);
        if ($needs_qr) {
            wp_enqueue_script('suzu-qrcode', plugins_url('assets/qrcode.min.js', __FILE__), [], '1.4.4', true);
            wp_register_script('suzu-pay-acc', false, ['suzu-qrcode'], self::VERSION, true);
        }
        wp_enqueue_script('suzu-pay-acc');
        wp_add_inline_script('suzu-pay-acc', "(function(){var q=document.querySelectorAll('.spa-qr[data-upi]');for(var i=0;i<q.length;i++){if(typeof qrcode!=='function')break;var c=qrcode(0,'M');c.addData(q[i].getAttribute('data-upi'));c.make();q[i].innerHTML=c.createSvgTag({cellSize:5,margin:2,scalable:true});}var b=document.querySelectorAll('.spa-copy');for(var j=0;j<b.length;j++)b[j].addEventListener('click',function(e){var t=e.currentTarget,v=t.getAttribute('data-copy');var done=function(){t.textContent='Copied';setTimeout(function(){t.textContent='Copy';},1600);};if(navigator.clipboard){navigator.clipboard.writeText(v).then(done,done);}else{var x=document.createElement('textarea');x.value=v;document.body.appendChild(x);x.select();try{document.execCommand('copy');}catch(err){}document.body.removeChild(x);done();}});})();");
        return $html;
    }

    public static function admin_page()
    {
        if (!current_user_can('manage_options')) {
            return;
        }
        $accs = self::accounts(); ?>
        <div class="wrap"><h1>Suzu Payments — bank &amp; UPI details</h1>
        <p>These details appear on the <a href="<?php echo esc_url(home_url('/payment/')); ?>" target="_blank">Payment page</a> under “Bank transfer &amp; UPI”. Leave an account empty to hide it. If you give a UPI ID and no QR image, a QR code is generated automatically on the page. <b>Please double-check every digit — customers will pay to exactly what is shown here.</b></p>
        <?php if (isset($_GET['saved'])) : ?><div class="notice notice-success"><p>Saved.</p></div><?php endif; ?>
        <form method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>">
        <input type="hidden" name="action" value="suzu_pay_accounts_save"><?php wp_nonce_field('suzu_pay_accounts'); ?>
        <?php foreach ($accs as $i => $a) : ?>
            <h2>Account <?php echo (int) $i + 1; ?></h2>
            <table class="form-table" role="presentation">
            <?php foreach (self::ACC_FIELDS as $k => $label) : ?>
                <tr><th scope="row"><label for="acc<?php echo (int) $i . esc_attr($k); ?>"><?php echo esc_html($label); ?></label></th>
                <td><input class="regular-text" id="acc<?php echo (int) $i . esc_attr($k); ?>" name="acc[<?php echo (int) $i; ?>][<?php echo esc_attr($k); ?>]" value="<?php echo esc_attr($a[$k]); ?>" autocomplete="off"></td></tr>
            <?php endforeach; ?>
            </table>
        <?php endforeach; ?>
        <?php submit_button('Save details'); ?></form></div>
        <?php
    }

    public static function admin_save()
    {
        if (!current_user_can('manage_options')) {
            wp_die('Not allowed');
        }
        check_admin_referer('suzu_pay_accounts');
        $in = isset($_POST['acc']) && is_array($_POST['acc']) ? wp_unslash($_POST['acc']) : [];
        $cur = self::accounts();
        $save = [];
        for ($i = 0; $i < 2; $i++) {
            $row = ['color' => $cur[$i]['color']];
            foreach (array_keys(self::ACC_FIELDS) as $k) {
                $v = isset($in[$i][$k]) ? trim(sanitize_text_field($in[$i][$k])) : '';
                $row[$k] = $k === 'qr' ? esc_url_raw($v) : $v;
            }
            $save[] = $row;
        }
        update_option(self::OPT_ACC, $save, 'no');
        if (function_exists('rocket_clean_post')) {
            $p = get_page_by_path('payment');
            if ($p) {
                rocket_clean_post($p->ID);
            }
        }
        wp_safe_redirect(add_query_arg(['page' => 'suzu-payments', 'saved' => 1], admin_url('options-general.php')));
        exit;
    }

    /* ---------------------------------------------------------- submit */

    private static function back($code)
    {
        $url = wp_get_referer() ?: home_url('/payment/');
        wp_safe_redirect(add_query_arg('pay_error', $code, remove_query_arg('pay_error', $url)) . '#pay-online');
        exit;
    }

    public static function submit()
    {
        if (!function_exists('wc_create_order')) {
            self::back('order');
        }
        // bots: honeypot filled, or no human interaction recorded by the form's script (no client clock involved)
        $t = isset($_POST['sp_t']) ? sanitize_text_field(wp_unslash($_POST['sp_t'])) : '';
        if (!empty($_POST['sp_website']) || strpos($t, 'h-') !== 0) {
            self::back('order');
        }
        $ip = isset($_SERVER['REMOTE_ADDR']) ? sanitize_text_field(wp_unslash($_SERVER['REMOTE_ADDR'])) : '0';
        $rk = 'suzu_pay_rl_' . md5($ip);
        $n = (int) get_transient($rk);
        if ($n >= 8) {
            self::back('busy');
        }
        set_transient($rk, $n + 1, HOUR_IN_SECONDS);

        $name = trim(sanitize_text_field(wp_unslash($_POST['sp_name'] ?? '')));
        $phone = trim(sanitize_text_field(wp_unslash($_POST['sp_phone'] ?? '')));
        $email = sanitize_email(wp_unslash($_POST['sp_email'] ?? ''));
        $ref = trim(sanitize_text_field(wp_unslash($_POST['sp_ref'] ?? '')));
        $type = sanitize_key(wp_unslash($_POST['sp_type'] ?? 'token'));
        $amount = (float) preg_replace('/[^0-9.]/', '', (string) wp_unslash($_POST['sp_amount'] ?? ''));
        $digits = preg_replace('/\D/', '', $phone);

        if (mb_strlen($name) < 2) self::back('name');
        if (strlen($digits) < 10 || strlen($digits) > 15) self::back('phone');
        if (!is_email($email)) self::back('email');
        if ($amount < self::MIN || $amount > self::MAX) self::back('amount');
        if (!isset(self::TYPES[$type])) $type = 'other';
        $amount = round($amount, 2);

        try {
            $order = wc_create_order(['status' => 'pending', 'created_via' => self::VIA]);
            if (is_wp_error($order)) {
                self::back('order');
            }
            $label = 'Suzu Travels tour payment' . ($ref !== '' ? ' — ' . $ref : '');
            $fee = new WC_Order_Item_Fee();
            $fee->set_name(mb_substr($label, 0, 180));
            $fee->set_amount($amount);
            $fee->set_total($amount);
            $fee->set_tax_status('none');
            $order->add_item($fee);
            $parts = preg_split('/\s+/', $name, 2);
            $order->set_billing_first_name($parts[0]);
            $order->set_billing_last_name($parts[1] ?? '');
            $order->set_billing_phone($phone);
            $order->set_billing_email($email);
            $order->set_billing_country('IN');
            $order->set_created_via(self::VIA);
            $order->set_customer_note('Payment for: ' . self::TYPES[$type] . ($ref !== '' ? "\nReference: " . $ref : ''));
            $order->update_meta_data('_suzu_pay_type', $type);
            $order->update_meta_data('_suzu_pay_ref', $ref);
            $order->calculate_totals(false);
            $order->save();
            $order->add_order_note(sprintf('Created from the Payment page form (%s). Amount ₹%s. Reference: %s', self::TYPES[$type], self::inr($amount), $ref !== '' ? $ref : '—'));
        } catch (\Throwable $e) {
            self::back('order');
        }
        wp_safe_redirect($order->get_checkout_payment_url());
        exit;
    }

    /* -------------------------------------------------------- cleanup */

    /** Unpaid form orders older than three days are cancelled so the order list stays clean. */
    public static function cleanup()
    {
        if (!function_exists('wc_get_orders')) {
            return;
        }
        $old = wc_get_orders(['status' => 'pending', 'created_via' => self::VIA, 'date_created' => '<' . (time() - 3 * DAY_IN_SECONDS), 'limit' => 50, 'return' => 'objects']);
        foreach ($old as $o) {
            if ($o->get_created_via() === self::VIA && !$o->is_paid()) {
                $o->update_status('cancelled', 'Unpaid payment-page order auto-cancelled after 3 days.');
            }
        }
    }
}

register_deactivation_hook(__FILE__, ['Suzu_Payments', 'deactivate']);
Suzu_Payments::init();
