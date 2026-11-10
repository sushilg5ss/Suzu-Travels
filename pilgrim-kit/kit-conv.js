/* Suzu Pilgrim Kit — conversion add-on JS (10 Nov 2026). Only on pages with "conv": true.
   Short lead forms (form.szp-lf) post to the site's existing lead endpoint (admin-ajax suzu_submit_landing_form, the same one
   the site pop-up uses: lead saved in Suzu Bookings + e-mail/WhatsApp alerts). Package-card buttons pre-select the package.
   The sticky bar's "Get Free Quote" scrolls to this page's form instead of opening the long pop-up; its WhatsApp link gets
   this page's message. GA4 events: click_call, click_whatsapp, form_submit, package_card_click, brochure_download.
   DOM is built with createElement only (WordPress wpautop breaks block-level HTML written inside JS strings). */
(function () {
  var d = document, root = d.querySelector('.szp');
  if (!root) return;
  function each(l, f) { Array.prototype.forEach.call(l, f); }
  function gt(n, p) { try { if (typeof window.gtag === 'function') window.gtag('event', n, p || {}); } catch (x) {} }
  var page = location.pathname.replace(/\/+$/, '').split('/').pop() || 'page';
  var forms = d.querySelectorAll('form.szp-lf');
  var t0 = Date.now();
  var M = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  function months(sel) {
    if (!sel || sel.getAttribute('data-done')) return;
    sel.setAttribute('data-done', '1');
    var now = new Date();
    for (var i = 0; 12 > i; i++) {
      var dt = new Date(now.getFullYear(), now.getMonth() + i, 1), o = d.createElement('option');
      o.value = o.textContent = M[dt.getMonth()] + ' ' + dt.getFullYear();
      sel.appendChild(o);
    }
    var o2 = d.createElement('option');
    o2.value = o2.textContent = 'Not decided yet';
    sel.appendChild(o2);
  }
  function setPkg(name) {
    each(forms, function (f) {
      var h = f.querySelector('input[name=pkg]'), b = f.querySelector('.pk');
      if (h) h.value = name;
      if (b) { b.textContent = 'Package: ' + name; b.className = 'pk on'; }
    });
  }
  function area(a) {
    if (a.closest('#szcta')) return 'sticky';
    var s = a.closest('[data-area]');
    if (s) return s.getAttribute('data-area');
    var sec = a.closest('section[id]');
    return sec ? sec.id : 'page';
  }
  each(forms, function (f) {
    months(f.querySelector('select[name=month]'));
    var ph = f.querySelector('input[name=phone]');
    if (ph) ph.addEventListener('input', function () { ph.value = ph.value.replace(/\D/g, '').slice(0, 10); });
    f.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (f.getAttribute('data-busy')) return;
      var kind = f.getAttribute('data-lf') || 'plan';
      var nm = f.querySelector('input[name=name]'), mo = f.querySelector('select[name=month]'), gs = f.querySelector('input[name=group]');
      var pk = f.querySelector('input[name=pkg]'), hp = f.querySelector('input[name=website]');
      var v = { name: nm ? nm.value.trim() : '', phone: ph ? ph.value.trim() : '', month: mo ? mo.value : '', group: gs ? gs.value.trim() : '', pkg: pk ? pk.value : '' };
      var bad = null;
      if (nm) { var e1 = !v.name; nm.className = e1 ? 'bad' : ''; if (e1) bad = bad || nm; }
      var e2 = !/^[6-9]\d{9}$/.test(v.phone);
      if (ph) { ph.className = e2 ? 'bad' : ''; if (e2) bad = bad || ph; }
      if (bad) { bad.focus(); return; }
      if (hp && hp.value) return;
      if (2500 > Date.now() - t0) return;
      f.setAttribute('data-busy', '1');
      var btn = f.querySelector('button[type=submit]');
      if (btn) { btn.disabled = true; btn.textContent = 'Sending...'; }
      var src = 'DIRECT';
      try { src = localStorage.getItem('szl_src') || src; } catch (x) {}
      var ref = 'SZ-' + String(Date.now()).slice(-6);
      var what = kind === 'checklist' ? 'Shakti Peeth yatra checklist (PDF) request' : 'Shakti Peeth yatra' + (v.pkg ? ' - ' + v.pkg : '');
      var parts = [what];
      if (v.month) parts.push('Travel: ' + v.month);
      if (v.group) parts.push('Group: ' + v.group);
      parts.push('Form: ' + kind);
      parts.push('Source: ' + src);
      parts.push('Page: ' + location.pathname);
      parts.push('Ref: ' + ref);
      var L = [what, 'Travel month: ' + (v.month || '-'), 'Group size: ' + (v.group || '-'), 'Package interest: ' + (v.pkg || '-'),
        'Form: ' + kind + ' (' + page + ')', 'Source: ' + src + ' | Page: ' + location.pathname + ' | Ref: ' + ref];
      if (kind === 'checklist') L.push('Please send the Shakti Peeth checklist PDF on WhatsApp.');
      var fd = new FormData();
      fd.append('action', 'suzu_submit_landing_form');
      fd.append('name', v.name || 'Checklist request');
      fd.append('contact', v.phone);
      fd.append('email', '');
      fd.append('destination', parts.join('  -  '));
      fd.append('travel_date', '');
      fd.append('message', L.join('\n'));
      var done = function () {
        if (kind === 'checklist') {
          gt('brochure_download', { delivery: 'whatsapp', page_slug: page });
        } else {
          gt('form_submit', { form_id: 'sp51_' + kind, package_interest: v.pkg || '-', travel_month: v.month || '-', group_size: v.group || '-' });
          gt('conversion', { send_to: 'AW-17212172485/SPBwCPbf_9saEMXRs49A' });
        }
        var r = f.querySelector('.ref');
        if (r) r.textContent = ref;
        var w = f.querySelector('a.okwa');
        if (w) {
          var txt = kind === 'checklist'
            ? 'Namaste Suzu Travels, please send me the Shakti Peeth yatra checklist. Ref ' + ref + '.'
            : 'Namaste Suzu Travels, I just sent enquiry ' + ref + ' from your 51 Shakti Peeth page. ' + (v.name ? v.name + ', ' : '') + v.phone + (v.pkg ? '. Package: ' + v.pkg : '') + (v.month ? '. Month: ' + v.month : '') + (v.group ? '. Group: ' + v.group : '') + '.';
          w.href = 'https://wa.me/917087488961?text=' + encodeURIComponent(txt);
        }
        f.className += ' sent';
      };
      fetch('/wp-admin/admin-ajax.php', { method: 'POST', body: fd }).then(function (r) { return r.json(); }).then(done).catch(done);
    });
  });
  each(root.querySelectorAll('[data-pkg]'), function (a) {
    a.addEventListener('click', function () {
      var n = a.getAttribute('data-pkg');
      if (a.getAttribute('data-cta') === 'quote') setPkg(n);
      gt('package_card_click', { package_name: n, card_position: a.getAttribute('data-pos') || '', cta: a.getAttribute('data-cta') || '' });
    });
  });
  each(root.querySelectorAll('a[href="#plan"],a[href="#plan-form"]'), function (a) {
    a.addEventListener('click', function () {
      setTimeout(function () { var x = d.querySelector('#plan-form input[name=name]'); if (x) try { x.focus({ preventScroll: true }); } catch (y) { x.focus(); } }, 450);
    });
  });
  var waMain = root.querySelector('a[data-wa-main]'), waHref = waMain ? waMain.getAttribute('href') : '';
  window.addEventListener('click', function (ev) {
    var a = ev.target && ev.target.closest ? ev.target.closest('a') : null;
    if (!a) return;
    var h = a.getAttribute('href') || '';
    if (a.matches('#szcta a.q') && d.getElementById('plan-form')) {
      ev.preventDefault();
      ev.stopImmediatePropagation();
      d.getElementById('plan-form').scrollIntoView({ behavior: 'smooth', block: 'start' });
      setTimeout(function () { var x = d.querySelector('#plan-form input[name=name]'); if (x) try { x.focus({ preventScroll: true }); } catch (y) { x.focus(); } }, 600);
      gt('package_card_click', { package_name: '-', card_position: 'sticky', cta: 'quote' });
      return;
    }
    if (a.matches('#szcta a.w') && waHref) a.href = waHref;
    if (h.indexOf('tel:') === 0) gt('click_call', { link_location: area(a), page_slug: page });
    else if (h.indexOf('wa.me') > -1 || h.indexOf('api.whatsapp.com') > -1) gt('click_whatsapp', { link_location: area(a), page_slug: page });
  }, true);
  // Rating + count come from the site's live Google feed (Suzu Live Reviews plugin, refreshed hourly).
  var gs = root.querySelector('[data-gcount]');
  if (gs && window.fetch) fetch('/suzu-reviews.json', { credentials: 'omit' }).then(function (r) { return r.json(); }).then(function (j) {
    var rt = parseFloat(j && j.rating), n = parseInt(j && j.count, 10);
    if (rt >= 1 && 5 >= rt && n > 0) gs.textContent = rt.toFixed(1) + '★ Google rating · ' + n + ' reviews';
  }).catch(function () {});
})();
