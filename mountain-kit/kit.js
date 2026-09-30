/* Suzu Mountain Kit JS v1.0 — lazy videos + peak table (filter, search, sort, #hash filters). No dependencies. */
(function () {
  var d = document;
  function each(l, f) { Array.prototype.forEach.call(l, f); }
  // 1) lazy videos: <video data-lazy> with <source data-src>
  var rm = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function load(v) {
    if (v.getAttribute('data-done')) return; v.setAttribute('data-done', '1');
    each(v.querySelectorAll('source[data-src]'), function (s) { s.src = s.getAttribute('data-src'); });
    v.load(); if (!rm) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
  }
  var vs = d.querySelectorAll('video[data-lazy]');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (x) { if (x.isIntersecting) { load(x.target); io.unobserve(x.target); } }); }, { rootMargin: '250px' });
    each(vs, function (v) { io.observe(v); });
  } else each(vs, load);
  // 2) peak table
  var t = d.querySelector('.szm-data'); if (!t) return;
  var body = t.tBodies[0], rows = Array.prototype.slice.call(body.rows), q = d.getElementById('szm-q'), cnt = d.getElementById('szm-count');
  var f = { band: '', state: '', status: '' };
  function apply() {
    var s = (q && q.value || '').toLowerCase().trim(), k = 0;
    rows.forEach(function (r) {
      var ok = (!f.band || r.getAttribute('data-band') === f.band) && (!f.state || r.getAttribute('data-state') === f.state) &&
        (!f.status || r.getAttribute('data-status') === f.status) && (!s || r.getAttribute('data-q').indexOf(s) > -1);
      r.hidden = !ok; if (ok) k++;
    });
    if (cnt) cnt.textContent = 'Showing ' + k + ' of ' + rows.length + ' peaks';
  }
  function setF(key, val) {
    f[key] = val;
    each(d.querySelectorAll('.szm-filt button[data-k="' + key + '"]'), function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-v') === val ? 'true' : 'false'); });
  }
  each(d.querySelectorAll('.szm-filt button'), function (b) {
    b.addEventListener('click', function () { setF(b.getAttribute('data-k'), b.getAttribute('data-v')); apply(); });
  });
  if (q) q.addEventListener('input', apply);
  each(t.querySelectorAll('th[data-sort] button'), function (btn) {
    btn.addEventListener('click', function () {
      var th = btn.parentNode, key = th.getAttribute('data-sort'), cur = th.getAttribute('aria-sort');
      var dir = cur === 'descending' ? 1 : (cur === 'ascending' ? -1 : (key === 'name' ? 1 : -1));
      each(t.querySelectorAll('th[data-sort]'), function (x) { x.removeAttribute('aria-sort'); });
      th.setAttribute('aria-sort', dir > 0 ? 'ascending' : 'descending');
      rows.sort(function (a, b) {
        var x = a.getAttribute('data-' + key), y = b.getAttribute('data-' + key);
        if (x === '' && y !== '') return 1; if (y === '' && x !== '') return -1;
        var nx = parseFloat(x), ny = parseFloat(y);
        var c = (!isNaN(nx) && !isNaN(ny)) ? nx - ny : x.localeCompare(y);
        return c * dir;
      });
      rows.forEach(function (r) { body.appendChild(r); });
    });
  });
  // 3) #band-7000  #state-ladakh  #status-unclimbed  #peak-kamet
  function fromHash() {
    var h = decodeURIComponent(location.hash.slice(1)); if (!h) return;
    var m = h.match(/^(band|state|status)-(.+)$/);
    if (m) { setF('band', ''); setF('state', ''); setF('status', ''); if (q) q.value = ''; setF(m[1], m[2]); apply(); var L = d.getElementById('list'); if (L) L.scrollIntoView(); return; }
    if (h.indexOf('peak-') === 0) {
      var r = d.getElementById(h); if (!r) return;
      setF('band', ''); setF('state', ''); setF('status', ''); if (q) q.value = ''; apply();
      each(t.querySelectorAll('tr.hl'), function (x) { x.className = ''; }); r.className = 'hl';
      r.scrollIntoView({ block: 'center' });
    }
  }
  window.addEventListener('hashchange', fromHash); fromHash();
})();
