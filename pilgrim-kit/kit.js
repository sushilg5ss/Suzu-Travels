/* Suzu Pilgrim Kit JS v1.0 — lazy videos, story reveal, map of light, shrine table filters, menu highlight. No dependencies. */
(function () {
  var d = document;
  function each(l, f) { Array.prototype.forEach.call(l, f); }
  var rm = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var IO = 'IntersectionObserver' in window;
  // 1) lazy videos: <video data-lazy> with <source data-src>
  function load(v) {
    if (v.getAttribute('data-done')) return; v.setAttribute('data-done', '1');
    each(v.querySelectorAll('source[data-src]'), function (s) { s.src = s.getAttribute('data-src'); });
    v.load(); if (!rm) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
  }
  var vs = d.querySelectorAll('.szp video[data-lazy]');
  if (IO) { var io = new IntersectionObserver(function (es) { es.forEach(function (x) { if (x.isIntersecting) { load(x.target); io.unobserve(x.target); } }); }, { rootMargin: '250px' }); each(vs, function (v) { io.observe(v); }); }
  else each(vs, load);
  // 2) story beats reveal
  var st = d.querySelectorAll('.szp-story');
  if (IO && !rm) { var so = new IntersectionObserver(function (es) { es.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); so.unobserve(x.target); } }); }, { threshold: .25 }); each(st, function (s) { so.observe(s); }); }
  else each(st, function (s) { s.classList.add('in'); });
  // 3) map of light: <g class="pt" data-i> + <script type="application/json" class="szp-mapdata">
  each(d.querySelectorAll('.szp-map'), function (m) {
    var js = m.querySelector('.szp-mapdata'), card = m.querySelector('.szp-mapcard'); if (!js || !card) return;
    var data; try { data = JSON.parse(js.textContent); } catch (e) { return; }
    function show(i) {
      var x = data[i]; if (!x) return;
      each(m.querySelectorAll('.pt'), function (p) { p.classList.toggle('on', p.getAttribute('data-i') == i); });
      card.innerHTML = '<span class="k">' + x.k + '</span><div class="dv">' + x.dv + '</div><h3>' + x.n + '</h3><div class="meta">' + x.m + '</div><p>' + x.p + '</p>' + (x.u ? '<p><a href="' + x.u + '">' + x.ul + ' →</a></p>' : '');
    }
    each(m.querySelectorAll('.pt'), function (p) {
      p.setAttribute('tabindex', '0'); p.setAttribute('role', 'button');
      p.addEventListener('click', function () { show(p.getAttribute('data-i')); });
      p.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); show(p.getAttribute('data-i')); } });
    });
  });
  // 4) shrine table: search + filter buttons (data-k / data-v) on rows with data-<k>
  each(d.querySelectorAll('.szp-data'), function (t) {
    var wrap = t.closest('.szp-sec') || d, q = wrap.querySelector('.szp-q'), cnt = wrap.querySelector('.szp-count'), f = {};
    var rows = Array.prototype.slice.call(t.tBodies[0].rows);
    rows.forEach(function (r) { r._q = r.textContent.toLowerCase(); });
    function apply() {
      var s = (q && q.value || '').toLowerCase().trim(), k = 0;
      rows.forEach(function (r) {
        var ok = !s || r._q.indexOf(s) > -1;
        for (var key in f) if (f[key] && r.getAttribute('data-' + key) !== f[key]) ok = false;
        r.hidden = !ok; if (ok) k++;
      });
      if (cnt) cnt.textContent = 'Showing ' + k + ' of ' + rows.length;
    }
    each(wrap.querySelectorAll('.szp-filt button'), function (b) {
      b.addEventListener('click', function () {
        var key = b.getAttribute('data-k'); f[key] = b.getAttribute('data-v');
        each(wrap.querySelectorAll('.szp-filt button[data-k="' + key + '"]'), function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        apply();
      });
    });
    if (q) q.addEventListener('input', apply);
  });
  // 5) in-page menu: highlight the section in view
  var nav = d.querySelector('.szp-nav'); if (!nav || !IO) return;
  var links = {}; each(nav.querySelectorAll('a[href^="#"]'), function (a) { links[a.getAttribute('href').slice(1)] = a; });
  var no = new IntersectionObserver(function (es) {
    es.forEach(function (x) { if (x.isIntersecting && links[x.target.id]) { each(nav.querySelectorAll('a.on'), function (a) { a.classList.remove('on'); }); links[x.target.id].classList.add('on'); } });
  }, { rootMargin: '-45% 0px -50% 0px' });
  for (var id in links) { var el = d.getElementById(id); if (el) no.observe(el); }
})();
