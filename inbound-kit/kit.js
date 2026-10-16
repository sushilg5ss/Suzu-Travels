/* Suzu Inbound Kit JS v1.1 — lazy videos, reduced-motion hero, story reveal, map of light, table filters, menu highlight. No dependencies. */
(function () {
  var d = document;
  function each(l, f) { Array.prototype.forEach.call(l, f); }
  var rm = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var IO = 'IntersectionObserver' in window;
  // 0) accessibility (WCAG 2.2.2): with prefers-reduced-motion the autoplaying hero stays on its poster frame
  if (rm) each(d.querySelectorAll('.szi-hero video[autoplay]'), function (v) { v.removeAttribute('autoplay'); try { v.pause(); } catch (e) {} });
  // 1) lazy videos: <video data-lazy> with <source data-src>
  function load(v) {
    if (v.getAttribute('data-done')) return; v.setAttribute('data-done', '1');
    each(v.querySelectorAll('source[data-src]'), function (s) { s.src = s.getAttribute('data-src'); });
    v.load(); if (!rm) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
  }
  var vs = d.querySelectorAll('.szi video[data-lazy]');
  if (IO) { var io = new IntersectionObserver(function (es) { es.forEach(function (x) { if (x.isIntersecting) { load(x.target); io.unobserve(x.target); } }); }, { rootMargin: '250px' }); each(vs, function (v) { io.observe(v); }); }
  else each(vs, load);
  // 2) story beats reveal
  var st = d.querySelectorAll('.szi-story');
  if (IO && !rm) { var so = new IntersectionObserver(function (es) { es.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); so.unobserve(x.target); } }); }, { threshold: .25 }); each(st, function (s) { so.observe(s); }); }
  else each(st, function (s) { s.classList.add('in'); });
  // 3) map of light: <g class="pt" data-i> + <script type="application/json" class="szi-mapdata">
  each(d.querySelectorAll('.szi-map'), function (m) {
    var js = m.querySelector('.szi-mapdata'), card = m.querySelector('.szi-mapcard'); if (!js || !card) return;
    var data; try { data = JSON.parse(js.textContent); } catch (e) { return; }
    function show(i) {
      var x = data[i]; if (!x) return;
      each(m.querySelectorAll('.pt'), function (p) { p.classList.toggle('on', p.getAttribute('data-i') == i); });
      // built with DOM calls: WordPress' wpautop breaks block-level tags written inside JS strings
      while (card.firstChild) card.removeChild(card.firstChild);
      function add(tag, cls, html) { var n = d.createElement(tag); if (cls) n.className = cls; n.innerHTML = html; card.appendChild(n); return n; }
      add('span', 'k', x.k); add('span', 'dv', x.dv).style.display = 'block'; add('strong', 'nm', x.n); add('span', 'meta', x.m).style.display = 'block'; add('span', 'p', x.p).style.display = 'block';
      if (x.u) { var a = d.createElement('a'); a.href = x.u; a.innerHTML = x.ul + ' →'; a.className = 'go'; card.appendChild(a); }
    }
    each(m.querySelectorAll('.pt'), function (p) {
      p.setAttribute('tabindex', '0'); p.setAttribute('role', 'button');
      p.addEventListener('click', function () { show(p.getAttribute('data-i')); });
      p.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); show(p.getAttribute('data-i')); } });
    });
  });
  // 4) shrine table: search + filter buttons (data-k / data-v) on rows with data-<k>
  each(d.querySelectorAll('.szi-data'), function (t) {
    var wrap = t.closest('.szi-sec') || d, q = wrap.querySelector('.szi-q'), cnt = wrap.querySelector('.szi-count'), f = {};
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
    each(wrap.querySelectorAll('.szi-filt button'), function (b) {
      b.addEventListener('click', function () {
        var key = b.getAttribute('data-k'); f[key] = b.getAttribute('data-v');
        each(wrap.querySelectorAll('.szi-filt button[data-k="' + key + '"]'), function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        apply();
      });
    });
    if (q) q.addEventListener('input', apply);
  });
  // 5) in-page menu: highlight the section in view
  var nav = d.querySelector('.szi-nav'); if (!nav || !IO) return;
  var links = {}; each(nav.querySelectorAll('a[href^="#"]'), function (a) { links[a.getAttribute('href').slice(1)] = a; });
  var no = new IntersectionObserver(function (es) {
    es.forEach(function (x) { if (x.isIntersecting && links[x.target.id]) { each(nav.querySelectorAll('a.on'), function (a) { a.classList.remove('on'); }); links[x.target.id].classList.add('on'); } });
  }, { rootMargin: '-45% 0px -50% 0px' });
  for (var id in links) { var el = d.getElementById(id); if (el) no.observe(el); }
})();
