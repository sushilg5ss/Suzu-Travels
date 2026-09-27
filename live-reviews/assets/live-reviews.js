/* Suzu Live Reviews — puts the latest Google reviews into every reviews box (.ti-reviews). Numbers are already correct in the HTML. */
(function () {
  var STAR = 'M12 .587l3.668 7.431 8.2 1.192-5.934 5.787 1.402 8.168L12 18.896l-7.336 3.869 1.402-8.168-5.934-5.787 8.2-1.192z';
  var COLORS = ['#0F5132', '#1B5E20', '#B8860B', '#6A1B9A', '#1565C0', '#AD1457', '#00695C'];

  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function stars(n) {
    var h = '';
    for (var i = 1; i <= 5; i++) h += '<svg class="ti-card-star" viewBox="0 0 24 24"' + (i > n ? ' style="fill:#ccc"' : '') + '><path d="' + STAR + '"/></svg>';
    return h;
  }
  function card(r, i) {
    var name = esc(r.author || 'Google user');
    var initial = esc((r.author || 'G').trim().charAt(0).toUpperCase());
    var avatar = r.photo
      ? '<img class="ti-avatar" src="' + esc(r.photo) + '" alt="" loading="lazy" referrerpolicy="no-referrer" style="object-fit:cover" onerror="this.outerHTML=\'<div class=&quot;ti-avatar&quot; style=&quot;background:' + COLORS[i % COLORS.length] + '&quot;>' + initial + '</div>\'">'
      : '<div class="ti-avatar" style="background:' + COLORS[i % COLORS.length] + ';">' + initial + '</div>';
    var nameHtml = r.author_url ? '<a href="' + esc(r.author_url) + '" target="_blank" rel="noopener nofollow" style="color:inherit;text-decoration:none">' + name + '</a>' : name;
    return '<div class="ti-card sz-live-card">' +
      '<div class="ti-header">' + avatar +
      '<div class="ti-name-box"><div class="ti-name">' + nameHtml + '</div><div class="ti-date">' + esc(r.relative || '') + '</div></div>' +
      '<img class="ti-g-icon" src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google" loading="lazy"></div>' +
      '<div class="ti-card-stars">' + stars(r.rating || 5) + '</div>' +
      '<div class="ti-text">' + esc(r.text) + '</div></div>';
  }

  function render(d) {
    if (!d || !d.reviews || d.reviews.length < 3) return; // too few live reviews: keep the existing cards
    var boxes = document.querySelectorAll('.ti-reviews');
    for (var b = 0; b < boxes.length; b++) {
      var box = boxes[b];
      if (box.getAttribute('data-sz-live')) continue;
      box.setAttribute('data-sz-live', '1');
      box.innerHTML = d.reviews.map(card).join('');
      box.scrollLeft = 0;
      var wrap = box.closest ? box.closest('.trustindex-reviews-wrapper, .ti-widget') : null;
      if (wrap && d.maps_url && !wrap.querySelector('.sz-live-all')) {
        var a = document.createElement('a');
        a.className = 'sz-live-all';
        a.href = d.maps_url; a.target = '_blank'; a.rel = 'noopener';
        a.textContent = 'Read all ' + d.count + ' reviews on Google →';
        a.style.cssText = 'display:inline-block;margin:14px 0 0 4px;font-weight:700;font-size:14px;color:#1B5E20;text-decoration:none;border-bottom:2px solid #D4AF37';
        (wrap.classList.contains('ti-widget') ? wrap.parentNode : wrap).appendChild(a);
      }
    }
  }

  function today() { var t = new Date(); return t.getFullYear() + '' + (t.getMonth() + 1) + '' + t.getDate(); }

  function go() {
    if (window.SUZU_REVIEWS) { render(window.SUZU_REVIEWS); return; }
    // static homepage: read the daily data file, and nudge WordPress once a day so the data never goes stale
    fetch('/suzu-reviews.json?d=' + today(), { cache: 'default' })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(render)
      .catch(function () {});
    try {
      if (localStorage.getItem('szlr_tick') !== today()) {
        localStorage.setItem('szlr_tick', today());
        fetch('/wp-json/suzu-lr/v1/tick', { method: 'POST', keepalive: true }).catch(function () {});
      }
    } catch (e) {}
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go();
})();
