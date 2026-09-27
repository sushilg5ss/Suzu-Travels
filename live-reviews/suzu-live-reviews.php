<?php
/**
 * Plugin Name: Suzu Live Reviews
 * Description: One Google rating everywhere. Pulls the rating, review count and latest reviews from Google once a day and keeps the homepage and every WordPress page in sync. Settings → Suzu Live Reviews.
 * Version: 1.0.0
 * Author: Suzu Travels
 * Requires PHP: 7.4
 * Requires at least: 6.0
 * License: GPLv2 or later
 */

if (!defined('ABSPATH')) {
    exit;
}

final class Suzu_Live_Reviews
{
    const VERSION = '1.0.0';
    const OPT_DATA = 'suzu_lr_data';
    const OPT_KEY = 'suzu_lr_api_key';
    const OPT_PLACE = 'suzu_lr_place_id';
    const OPT_MIN = 'suzu_lr_min_stars';
    const OPT_LOG = 'suzu_lr_log';
    const CRON = 'suzu_lr_daily_refresh';
    const LOCK = 'suzu_lr_lock';
    const PLACE_DEFAULT = 'ChIJfTs2BR87BTkRCsaF7I2KXtA';
    const JSON_FILE = 'suzu-reviews.json';
    const HOME_FILE = 'index.html';
    const HOME_BACKUP = 'index.html.suzu-live-reviews-bak';
    const STALE_AFTER = 82800; // 23 hours

    /* ------------------------------------------------------------------ boot */

    public static function init()
    {
        add_action(self::CRON, [__CLASS__, 'cron_refresh']);
        add_action('rest_api_init', [__CLASS__, 'rest_routes']);
        add_action('admin_menu', [__CLASS__, 'admin_menu']);
        add_action('admin_post_suzu_lr_save', [__CLASS__, 'admin_save']);
        add_action('admin_post_suzu_lr_refresh', [__CLASS__, 'admin_refresh']);
        add_filter('plugin_action_links_' . plugin_basename(__FILE__), [__CLASS__, 'action_links']);

        if (!is_admin()) {
            add_action('template_redirect', [__CLASS__, 'start_buffer'], 1);
            add_action('wp_enqueue_scripts', [__CLASS__, 'enqueue']);
        }
        // self-heal: if the daily event went missing, put it back
        add_action('init', function () {
            if (!wp_next_scheduled(self::CRON)) {
                self::schedule();
            }
        });
    }

    public static function activate()
    {
        if (!get_option(self::OPT_DATA)) {
            add_option(self::OPT_DATA, self::seed(), '', 'yes');
        }
        if (!get_option(self::OPT_PLACE)) {
            add_option(self::OPT_PLACE, self::PLACE_DEFAULT, '', 'no');
        }
        if (!get_option(self::OPT_MIN)) {
            add_option(self::OPT_MIN, 4, '', 'no');
        }
        self::schedule();
        self::publish(self::data(), true); // true: clear WP Rocket so cached pages pick up the unified numbers
        self::log('Plugin activated. Showing ' . self::fmt_rating(self::data()['rating']) . ' / ' . self::data()['count'] . '.');
    }

    public static function deactivate()
    {
        wp_clear_scheduled_hook(self::CRON);
    }

    private static function schedule()
    {
        wp_clear_scheduled_hook(self::CRON);
        // next 06:10 IST (00:40 UTC), clear of the other daily agents
        $now = time();
        $next = strtotime(gmdate('Y-m-d', $now) . ' 00:40:00 UTC');
        if ($next <= $now) {
            $next += DAY_IN_SECONDS;
        }
        wp_schedule_event($next, 'daily', self::CRON);
    }

    private static function seed()
    {
        return [
            'rating' => 4.7,
            'count' => 377,
            'reviews' => [],
            'maps_url' => 'https://www.google.com/maps/place/?q=place_id:' . self::PLACE_DEFAULT,
            'updated_at' => '2026-09-27T18:00:00+00:00',
            'source' => 'seed',
        ];
    }

    /* ------------------------------------------------------------------ data */

    public static function data()
    {
        $d = get_option(self::OPT_DATA);
        if (!is_array($d) || empty($d['rating']) || empty($d['count'])) {
            $d = self::seed();
        }
        return $d;
    }

    public static function public_data()
    {
        $d = self::data();
        $min = (int) get_option(self::OPT_MIN, 4);
        $reviews = array_values(array_filter((array) $d['reviews'], function ($r) use ($min) {
            return isset($r['rating']) && (int) $r['rating'] >= $min && !empty($r['text']);
        }));
        return [
            'rating' => (float) $d['rating'],
            'rating_text' => self::fmt_rating($d['rating']),
            'count' => (int) $d['count'],
            'count_rounded' => self::fmt_rounded($d['count']),
            'reviews' => $reviews,
            'maps_url' => $d['maps_url'],
            'updated_at' => $d['updated_at'],
            'source' => $d['source'],
        ];
    }

    public static function fmt_rating($r)
    {
        return number_format((float) $r, 1, '.', '');
    }

    public static function fmt_rounded($n)
    {
        $n = (int) $n;
        return ($n >= 20 ? (int) (floor($n / 10) * 10) : $n) . '+';
    }

    /* --------------------------------------------------------------- refresh */

    public static function cron_refresh()
    {
        self::refresh('daily');
    }

    /**
     * Fetch from Google Places (New). Keeps the last good data on any problem.
     * @return array [bool ok, string message]
     */
    public static function refresh($why = 'manual')
    {
        $key = trim((string) get_option(self::OPT_KEY, ''));
        if ($key === '') {
            self::log('Skipped (' . $why . '): no Google API key saved yet. Showing the saved numbers.');
            return [false, 'No Google API key saved yet.'];
        }
        if (get_transient(self::LOCK)) {
            return [false, 'A refresh is already running.'];
        }
        set_transient(self::LOCK, 1, 120);

        $place = trim((string) get_option(self::OPT_PLACE, self::PLACE_DEFAULT)) ?: self::PLACE_DEFAULT;
        $res = wp_remote_get('https://places.googleapis.com/v1/places/' . rawurlencode($place) . '?languageCode=en', [
            'timeout' => 20,
            'headers' => [
                'X-Goog-Api-Key' => $key,
                'X-Goog-FieldMask' => 'rating,userRatingCount,reviews,googleMapsUri',
            ],
        ]);
        delete_transient(self::LOCK);

        if (is_wp_error($res)) {
            return self::fail($why, 'network error: ' . $res->get_error_message());
        }
        $code = (int) wp_remote_retrieve_response_code($res);
        $body = json_decode(wp_remote_retrieve_body($res), true);
        if ($code !== 200 || !is_array($body)) {
            $msg = is_array($body) && isset($body['error']['message']) ? $body['error']['message'] : 'HTTP ' . $code;
            return self::fail($why, 'Google said: ' . rtrim($msg, '. '));
        }

        $rating = isset($body['rating']) ? (float) $body['rating'] : 0;
        $count = isset($body['userRatingCount']) ? (int) $body['userRatingCount'] : 0;
        $old = self::data();
        if ($rating < 1 || $rating > 5 || $count < 1) {
            return self::fail($why, 'response had no usable rating/count');
        }
        if ($old['source'] === 'google' && $count < (int) floor($old['count'] * 0.9)) {
            return self::fail($why, 'count dropped from ' . $old['count'] . ' to ' . $count . ' (over 10%) — kept the old numbers; check the listing');
        }

        $reviews = [];
        foreach ((array) ($body['reviews'] ?? []) as $r) {
            $text = $r['text']['text'] ?? ($r['originalText']['text'] ?? '');
            $reviews[] = [
                'author' => (string) ($r['authorAttribution']['displayName'] ?? 'Google user'),
                'author_url' => esc_url_raw($r['authorAttribution']['uri'] ?? ''),
                'photo' => esc_url_raw($r['authorAttribution']['photoUri'] ?? ''),
                'rating' => (int) ($r['rating'] ?? 0),
                'text' => wp_strip_all_tags((string) $text),
                'relative' => (string) ($r['relativePublishTimeDescription'] ?? ''),
                'time' => (string) ($r['publishTime'] ?? ''),
            ];
        }
        if (!$reviews && !empty($old['reviews'])) {
            $reviews = $old['reviews']; // keep the last good set rather than showing none
        }

        $new = [
            'rating' => round($rating, 1),
            'count' => $count,
            'reviews' => $reviews,
            'maps_url' => esc_url_raw($body['googleMapsUri'] ?? $old['maps_url']),
            'updated_at' => gmdate('c'),
            'source' => 'google',
        ];
        $changed = self::fmt_rating($new['rating']) !== self::fmt_rating($old['rating'])
            || (int) $new['count'] !== (int) $old['count']
            || wp_json_encode($new['reviews']) !== wp_json_encode($old['reviews']);
        update_option(self::OPT_DATA, $new, 'yes');
        $pub = self::publish($new, $changed);
        $msg = 'Updated from Google (' . $why . '): ' . self::fmt_rating($new['rating']) . ' from ' . $count . ' reviews, '
            . count($reviews) . ' latest reviews. ' . ($changed ? 'Changed. ' : 'No change. ') . $pub;
        self::log($msg);
        return [true, $msg];
    }

    private static function fail($why, $msg)
    {
        self::log('Refresh failed (' . $why . '): ' . $msg . '. Still showing the last good numbers.');
        return [false, $msg];
    }

    /** Write the public JSON, sync the static homepage, purge page cache if numbers changed. */
    private static function publish($d, $changed)
    {
        $notes = [];
        $pub = self::public_data();
        $json = wp_json_encode($pub, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
        if ($json && self::atomic_write(ABSPATH . self::JSON_FILE, $json)) {
            $notes[] = 'JSON saved';
        } else {
            $notes[] = 'JSON NOT saved';
        }
        $notes[] = self::sync_homepage($d);
        if ($changed && function_exists('rocket_clean_domain')) {
            rocket_clean_domain();
            $notes[] = 'page cache cleared';
        }
        return implode(', ', $notes) . '.';
    }

    private static function atomic_write($path, $content)
    {
        $tmp = $path . '.tmp-' . wp_generate_password(6, false);
        if (@file_put_contents($tmp, $content) === false) {
            return false;
        }
        @chmod($tmp, 0644);
        if (!@rename($tmp, $path)) {
            @unlink($tmp);
            return false;
        }
        return true;
    }

    /** The homepage is a static index.html in front of WordPress: rewrite only the rating numbers in it. */
    public static function sync_homepage($d)
    {
        $path = ABSPATH . self::HOME_FILE;
        if (!is_readable($path) || !is_writable($path)) {
            return 'homepage file not found/writable';
        }
        $html = file_get_contents($path);
        if (!is_string($html) || stripos($html, '</html>') === false) {
            return 'homepage skipped (unexpected content)';
        }
        $out = self::apply_rules($html, $d, true);
        if ($out === $html) {
            return 'homepage already up to date';
        }
        if (!is_string($out) || stripos($out, '</html>') === false || abs(strlen($out) - strlen($html)) > 400) {
            return 'homepage NOT changed (safety check)';
        }
        @copy($path, ABSPATH . self::HOME_BACKUP);
        return self::atomic_write($path, $out) ? 'homepage updated' : 'homepage write failed';
    }

    /* ----------------------------------------------------------- the engine */

    /**
     * Replace every known way the site writes the Google rating / review count.
     * Pure function (no WordPress calls) so it can be tested on its own.
     */
    public static function apply_rules($html, $d, $with_schema = false)
    {
        $R = number_format((float) $d['rating'], 1, '.', '');
        $N = (string) (int) $d['count'];
        $P = self::fmt_rounded($d['count']);
        $num = '[1-5]\.\d';
        $cnt = '\d{2,5}';

        $rules = [
            // popup: ★ 4.7 · 377 Google reviews
            ['~(&#9733;|&starf;|★)(\s*)' . $num . '(\s*(?:&middot;|·)\s*)' . $cnt . '(\s*Google reviews)~u', '${1}${2}' . $R . '${3}' . $N . '${4}'],
            // reviews box: Based on <strong>377 reviews</strong>
            ['~(Based on\s*<strong>\s*)' . $cnt . '(\s*reviews\s*</strong>)~i', '${1}' . $N . '${2}'],
            // gallery: <b>4.7★</b><span>on Google (377 reviews)</span>
            ['~(<b>\s*)' . $num . '(\s*(?:★|&#9733;)\s*</b>\s*<span>\s*on Google \()' . $cnt . '(\s*reviews\))~u', '${1}' . $R . '${2}' . $N . '${3}'],
            // contact: <b>4.7</b><span>average rating from 377 Google reviews
            ['~(<b>\s*)' . $num . '(\s*</b>\s*<span>\s*average rating from\s*)' . $cnt . '(\s*Google reviews)~', '${1}' . $R . '${2}' . $N . '${3}'],
            // 4.7 from 377 Google reviews
            ['~\b' . $num . '( from )' . $cnt . '( Google reviews)~', $R . '${1}' . $N . '${2}'],
            // rated 4.7 across 377 Google reviews
            ['~(rated\s+)' . $num . '(\s+across\s+)' . $cnt . '(\s+Google reviews)~', '${1}' . $R . '${2}' . $N . '${3}'],
            // 4.7 / 377 ... Google reviews (quote page)
            ['~\b' . $num . '(\s*/\s*)' . $cnt . '((?:\s*<[^>]+>)*\s*Google reviews)~', $R . '${1}' . $N . '${2}'],
            // Our 4.7/5 rating on Google
            ['~(Our\s+)' . $num . '(/5 rating on Google)~', '${1}' . $R . '${2}'],
            // about badge: </i> 4.7&#9733; Google </div>
            ['~(</i>\s*)' . $num . '(\s*(?:&#9733;|★)\s*Google\s*</div>)~u', '${1}' . $R . '${2}'],
            // big stat: 4.7&#9733;</div><div ...>Google Rating
            ['~(>\s*)' . $num . '((?:&#9733;|★)\s*</div>\s*<div[^>]*>\s*Google Rating)~u', '${1}' . $R . '${2}'],
            // homepage stat: <h3>4.7<span>&#9733;</span></h3> <p>Google Rating</p>
            ['~(<h3>\s*)' . $num . '(\s*<span>\s*(?:&#9733;|★)\s*</span>\s*</h3>\s*<p>\s*Google Rating)~u', '${1}' . $R . '${2}'],
            // prose: 4.7-star Google rating from 370+ reviews
            ['~\b' . $num . '(-star Google rating from )' . $cnt . '\+?( reviews)~', $R . '${1}' . $P . '${2}'],
        ];
        $out = $html;
        foreach ($rules as $r) {
            $next = preg_replace($r[0], $r[1], $out);
            if (is_string($next)) {
                $out = $next;
            }
        }
        if ($with_schema) {
            // JSON-LD AggregateRating block of the business (homepage only)
            $next = preg_replace_callback('~"aggregateRating"\s*:\s*\{[^{}]*\}~', function ($m) use ($R, $N) {
                $b = $m[0];
                $b = preg_replace('~("ratingValue"\s*:\s*")[\d.]+(")~', '${1}' . $R . '${2}', $b);
                $b = preg_replace('~("ratingCount"\s*:\s*")\d+(")~', '${1}' . $N . '${2}', $b);
                $b = preg_replace('~("reviewCount"\s*:\s*")\d+(")~', '${1}' . $N . '${2}', $b);
                return $b;
            }, $out);
            if (is_string($next)) {
                $out = $next;
            }
        }
        return $out;
    }

    /* ---------------------------------------------------------- front end */

    public static function start_buffer()
    {
        if (is_feed() || is_robots() || is_trackback() || wp_doing_ajax() || (defined('REST_REQUEST') && REST_REQUEST)) {
            return;
        }
        ob_start([__CLASS__, 'filter_html']);
    }

    public static function filter_html($buf)
    {
        if (!is_string($buf) || strlen($buf) < 200 || stripos($buf, '<html') === false) {
            return $buf;
        }
        try {
            $out = self::apply_rules($buf, self::data(), false);
        } catch (\Throwable $e) {
            return $buf;
        }
        return (is_string($out) && $out !== '') ? $out : $buf;
    }

    public static function enqueue()
    {
        wp_enqueue_script('suzu-live-reviews', plugins_url('assets/live-reviews.js', __FILE__), [], self::VERSION, true);
        wp_add_inline_script('suzu-live-reviews', 'window.SUZU_REVIEWS=' . wp_json_encode(self::public_data(), JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . ';', 'before');
    }

    /* --------------------------------------------------------------- REST */

    public static function rest_routes()
    {
        register_rest_route('suzu-lr/v1', '/data', [
            'methods' => 'GET',
            'permission_callback' => '__return_true',
            'callback' => function () {
                return rest_ensure_response(self::public_data());
            },
        ]);
        // called by the static homepage at most once per visitor per day: refresh if the data is stale
        register_rest_route('suzu-lr/v1', '/tick', [
            'methods' => 'POST',
            'permission_callback' => '__return_true',
            'callback' => function () {
                $d = self::data();
                $age = time() - (int) strtotime($d['updated_at']);
                $ran = false;
                if ($age > self::STALE_AFTER && trim((string) get_option(self::OPT_KEY, '')) !== '' && !get_transient('suzu_lr_tick_gate')) {
                    set_transient('suzu_lr_tick_gate', 1, HOUR_IN_SECONDS);
                    self::refresh('stale-check');
                    $ran = true;
                }
                return rest_ensure_response(['ok' => true, 'refreshed' => $ran]);
            },
        ]);
    }

    /* -------------------------------------------------------------- admin */

    public static function action_links($links)
    {
        array_unshift($links, '<a href="' . esc_url(admin_url('options-general.php?page=suzu-live-reviews')) . '">Settings</a>');
        return $links;
    }

    public static function admin_menu()
    {
        add_options_page('Suzu Live Reviews', 'Suzu Live Reviews', 'manage_options', 'suzu-live-reviews', [__CLASS__, 'admin_page']);
    }

    public static function admin_save()
    {
        if (!current_user_can('manage_options')) {
            wp_die('Not allowed');
        }
        check_admin_referer('suzu_lr_save');
        $key = isset($_POST['suzu_lr_key']) ? trim(sanitize_text_field(wp_unslash($_POST['suzu_lr_key']))) : '';
        if ($key !== '') {
            update_option(self::OPT_KEY, $key, 'no');
        }
        if (!empty($_POST['suzu_lr_clear_key'])) {
            delete_option(self::OPT_KEY);
        }
        $place = isset($_POST['suzu_lr_place']) ? trim(sanitize_text_field(wp_unslash($_POST['suzu_lr_place']))) : '';
        update_option(self::OPT_PLACE, $place !== '' ? $place : self::PLACE_DEFAULT, 'no');
        $min = isset($_POST['suzu_lr_min']) ? max(1, min(5, (int) $_POST['suzu_lr_min'])) : 4;
        update_option(self::OPT_MIN, $min, 'no');
        $msg = 'saved';
        if ($key !== '') {
            $r = self::refresh('key saved');
            $msg = $r[0] ? 'saved_ok' : 'saved_fail';
        } else {
            self::publish(self::data(), false);
        }
        wp_safe_redirect(add_query_arg(['page' => 'suzu-live-reviews', 'msg' => $msg], admin_url('options-general.php')));
        exit;
    }

    public static function admin_refresh()
    {
        if (!current_user_can('manage_options')) {
            wp_die('Not allowed');
        }
        check_admin_referer('suzu_lr_refresh');
        $r = self::refresh('manual');
        wp_safe_redirect(add_query_arg(['page' => 'suzu-live-reviews', 'msg' => $r[0] ? 'refreshed' : 'refresh_fail'], admin_url('options-general.php')));
        exit;
    }

    public static function admin_page()
    {
        if (!current_user_can('manage_options')) {
            return;
        }
        $d = self::public_data();
        $key = (string) get_option(self::OPT_KEY, '');
        $place = (string) get_option(self::OPT_PLACE, self::PLACE_DEFAULT);
        $min = (int) get_option(self::OPT_MIN, 4);
        $log = (array) get_option(self::OPT_LOG, []);
        $next = wp_next_scheduled(self::CRON);
        $msgs = [
            'saved' => ['success', 'Settings saved.'],
            'saved_ok' => ['success', 'Key saved and Google data fetched. Everything is live.'],
            'saved_fail' => ['error', 'Key saved, but the first fetch failed — see the log below.'],
            'refreshed' => ['success', 'Fetched fresh data from Google.'],
            'refresh_fail' => ['error', 'Refresh failed — see the log below. The site keeps showing the last good numbers.'],
        ];
        $m = isset($_GET['msg'], $msgs[$_GET['msg']]) ? $msgs[$_GET['msg']] : null;
        ?>
        <div class="wrap">
            <h1>Suzu Live Reviews</h1>
            <p>One Google rating everywhere. Once a day this pulls the rating, review count and latest reviews from Google and updates the homepage and every WordPress page.</p>
            <?php if ($m) : ?><div class="notice notice-<?php echo esc_attr($m[0]); ?> is-dismissible"><p><?php echo esc_html($m[1]); ?></p></div><?php endif; ?>

            <h2>Showing right now</h2>
            <table class="widefat striped" style="max-width:720px">
                <tr><th style="width:220px">Google rating</th><td><strong style="font-size:18px"><?php echo esc_html($d['rating_text']); ?> ★</strong></td></tr>
                <tr><th>Review count</th><td><?php echo esc_html($d['count']); ?> (prose uses “<?php echo esc_html($d['count_rounded']); ?>”)</td></tr>
                <tr><th>Latest reviews shown</th><td><?php echo esc_html(count($d['reviews'])); ?> (only <?php echo esc_html($min); ?>★ and above)</td></tr>
                <tr><th>Source</th><td><?php echo $d['source'] === 'google' ? 'Google (automatic)' : 'Saved numbers — add the API key to go automatic'; ?></td></tr>
                <tr><th>Last updated</th><td><?php echo esc_html(get_date_from_gmt(gmdate('Y-m-d H:i:s', strtotime($d['updated_at'])), 'j M Y, g:i a')); ?></td></tr>
                <tr><th>Next automatic update</th><td><?php echo $next ? esc_html(get_date_from_gmt(gmdate('Y-m-d H:i:s', $next), 'j M Y, g:i a')) : 'not scheduled'; ?></td></tr>
                <tr><th>Public data file</th><td><a href="<?php echo esc_url(home_url('/' . self::JSON_FILE)); ?>" target="_blank"><?php echo esc_html(home_url('/' . self::JSON_FILE)); ?></a></td></tr>
            </table>

            <form method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>" style="margin-top:14px">
                <input type="hidden" name="action" value="suzu_lr_refresh">
                <?php wp_nonce_field('suzu_lr_refresh'); ?>
                <?php submit_button('Update from Google now', 'secondary', 'submit', false, $key === '' ? ['disabled' => 'disabled'] : []); ?>
            </form>

            <h2 style="margin-top:28px">Settings</h2>
            <form method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>">
                <input type="hidden" name="action" value="suzu_lr_save">
                <?php wp_nonce_field('suzu_lr_save'); ?>
                <table class="form-table" role="presentation">
                    <tr>
                        <th scope="row"><label for="suzu_lr_key">Google Places API key</label></th>
                        <td>
                            <input type="password" id="suzu_lr_key" name="suzu_lr_key" class="regular-text" autocomplete="new-password"
                                   placeholder="<?php echo $key !== '' ? esc_attr('Saved (ends in ' . substr($key, -4) . ') — leave empty to keep') : 'Paste your key here'; ?>">
                            <?php if ($key !== '') : ?><label style="margin-left:10px"><input type="checkbox" name="suzu_lr_clear_key" value="1"> Remove saved key</label><?php endif; ?>
                            <p class="description">Google Cloud → APIs &amp; Services → enable <b>Places API (New)</b> → Credentials → Create API key → restrict it to <b>Places API (New)</b>. One call a day stays inside Google’s free monthly allowance.</p>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row"><label for="suzu_lr_place">Google Place ID</label></th>
                        <td><input type="text" id="suzu_lr_place" name="suzu_lr_place" class="regular-text" value="<?php echo esc_attr($place); ?>">
                            <p class="description">Suzu Travels, Kulahru (Ghumarwin). Change only if the Google listing changes.</p></td>
                    </tr>
                    <tr>
                        <th scope="row"><label for="suzu_lr_min">Show reviews with at least</label></th>
                        <td><select id="suzu_lr_min" name="suzu_lr_min"><?php for ($i = 5; $i >= 1; $i--) {
                            echo '<option value="' . $i . '"' . selected($min, $i, false) . '>' . $i . ' stars</option>';
                        } ?></select></td>
                    </tr>
                </table>
                <?php submit_button('Save settings'); ?>
            </form>

            <h2>Log</h2>
            <div style="max-width:900px;background:#fff;border:1px solid #ccd0d4;padding:10px 14px;font-family:monospace;font-size:12px;line-height:1.7">
                <?php echo $log ? implode('<br>', array_map('esc_html', array_reverse($log))) : 'Nothing yet.'; ?>
            </div>
        </div>
        <?php
    }

    private static function log($line)
    {
        $log = (array) get_option(self::OPT_LOG, []);
        $log[] = wp_date('Y-m-d H:i') . '  ' . $line;
        update_option(self::OPT_LOG, array_slice($log, -30), 'no');
    }
}

register_activation_hook(__FILE__, ['Suzu_Live_Reviews', 'activate']);
register_deactivation_hook(__FILE__, ['Suzu_Live_Reviews', 'deactivate']);
Suzu_Live_Reviews::init();
