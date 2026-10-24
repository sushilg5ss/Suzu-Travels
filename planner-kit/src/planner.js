/*! Suzu Trip Planner v0.1 — 15 Oct 2026 — suzutravels.com/plan-your-trip/
 * Build-your-own itinerary: places + nights -> road route, day plan, cab + hotel estimate, PDF, share link.
 * No server storage: the whole plan lives in the URL hash (#t=...). Leads go to the same WordPress
 * handler as the homepage (action suzu_submit_landing_form), only when running on suzutravels.com.
 */
(function () {
  'use strict';
  var VER = '1.3';
  var D = document, W = window;
  var DATA = JSON.parse(D.getElementById('tp-data').textContent);
  var R = DATA.rates, ROADS = DATA.roads, TPL = DATA.templates;
  var PL = {}, IDX = {};
  DATA.places.forEach(function (p) { PL[p.id] = p; });
  ROADS.ids.forEach(function (id, i) { IDX[id] = i; });
  if (!ROADS.geo) ROADS.geo = {};
  /* road geometry arrives after first paint (roads-geo.json); until then legs draw as straight lines */
  function loadGeo() {
    if (ROADS.geoLoaded || !W.fetch) return;
    var u = location.pathname.replace(/[^\/]*$/, '') + 'roads-geo.json?v=' + (DATA.geo_v || VER);
    W.fetch(u, { credentials: 'same-origin' }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      if (!d || !d.geo) return; ROADS.geo = d.geo; ROADS.geoLoaded = true; GC = {}; ADJ = null;
      if (LAST) { renderMap(LAST, false); if (leafOn && W.L) drawLeaf(LAST); }
    }).catch(function () {});
  }
  var WA = '917087488961', PHONE = '+91 70874 88961';
  var LIVE = /(^|\.)suzutravels\.com$/.test(location.hostname);
  var ADDONS = [
    { id: 'para', n: 'Paragliding', at: ['bir', 'manali', 'dharamshala'] },
    { id: 'raft', n: 'River rafting', at: ['kullu', 'rishikesh', 'manali'] },
    { id: 'snow', n: 'Snow activities & gear', at: ['manali', 'shimla', 'gulmarg', 'sonamarg', 'sissu'] },
    { id: 'rohtang', n: 'Rohtang Pass permit', at: ['manali'] },
    { id: 'gondola', n: 'Gulmarg Gondola tickets', at: ['gulmarg'] },
    { id: 'houseboat', n: 'Houseboat night', at: ['srinagar'] },
    { id: 'heli-ked', n: 'Kedarnath helicopter', at: ['guptkashi'] },
    { id: 'heli-vd', n: 'Vaishno Devi helicopter', at: ['katra'] },
    { id: 'safari', n: 'Jungle safari', at: ['corbett'] },
    { id: 'camp', n: 'Riverside camping', at: ['kasol', 'rishikesh', 'jibhi', 'tirthan'] },
    { id: 'pony', n: 'Pony / palki', at: ['katra', 'guptkashi', 'barkot', 'pahalgam', 'sonamarg', 'nainadevi'] },
    { id: 'guide', n: 'Local guide', at: [] },
    { id: 'photo', n: 'Trip photographer', at: [] },
    { id: 'cake', n: 'Honeymoon decor & cake', at: [] }
  ];
  var CATS = [['all', 'All'], ['himachal', 'Himachal'], ['mata', 'Mata darshan'], ['pilgrim', 'Char Dham & yatra'], ['honeymoon', 'Honeymoon'], ['kashmir', 'Kashmir'], ['ladakh', 'Ladakh'], ['uttarakhand', 'Uttarakhand'], ['rajasthan', 'Rajasthan & Agra']];
  var REGLBL = { himachal: 'Himachal', pilgrim: 'Mata darshan', kashmir: 'Kashmir', ladakh: 'Ladakh', uttarakhand: 'Uttarakhand', hub: 'City', punjab: 'Punjab', rajasthan: 'Rajasthan', up: 'Agra & Mathura' };
  var HILL = { himachal: 1, pilgrim: 1, kashmir: 1, ladakh: 1, uttarakhand: 1 };

  /* ---------------- helpers ---------------- */
  function $(s, r) { return (r || D).querySelector(s); }
  function $$(s, r) { return [].slice.call((r || D).querySelectorAll(s)); }
  function esc(x) { return String(x == null ? '' : x).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function inr(n) { return '₹' + Math.round(n).toLocaleString('en-IN'); }
  function r100(n) { return Math.ceil(n / 100) * 100; }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function iso(d) { return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate()); }
  function parseD(s) { var a = String(s || '').split('-'); return a.length === 3 ? new Date(+a[0], +a[1] - 1, +a[2]) : null; }
  function addD(d, n) { var x = new Date(d.getTime()); x.setDate(x.getDate() + n); return x; }
  var MS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var WD = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  function fmtD(d) { return WD[d.getDay()] + ', ' + d.getDate() + ' ' + MS[d.getMonth()]; }
  function fmtLong(d) { return d.getDate() + ' ' + MS[d.getMonth()] + ' ' + d.getFullYear(); }
  function hrs(m) { if (m < 50) return Math.max(10, Math.round(m / 5) * 5) + ' min'; var h = m / 60; return '~' + (h < 10 ? Math.round(h * 2) / 2 : Math.round(h)) + ' h'; }
  function ev(n, p) { try { if (typeof gtag === 'function') gtag('event', n, p || {}); } catch (e) {} }
  function toast(t) { var x = $('#toast'); x.textContent = t; x.classList.add('on'); clearTimeout(toast.t); toast.t = setTimeout(function () { x.classList.remove('on'); }, 2600); }
  function srcTag() { try { return localStorage.getItem('szl_src') || 'DR'; } catch (e) { return 'DR'; } }

  /* ---------------- roads ---------------- */
  function km(a, b) { if (a === b) return 0; return ROADS.km[IDX[a]][IDX[b]] || 0; }
  function hillF(a, b) { return (HILL[PL[a].region] || HILL[PL[b].region]) ? 1.3 : 1.1; }
  function mins(a, b) { if (a === b) return 0; return Math.round((ROADS.min[IDX[a]][IDX[b]] || 0) * hillF(a, b)); }
  function dec(s) {
    var pts = [], i = 0, lat = 0, lon = 0;
    while (i < s.length) {
      for (var k = 0; k < 2; k++) {
        var sh = 0, res = 0, b;
        do { b = s.charCodeAt(i++) - 63; res |= (b & 31) << sh; sh += 5; } while (b >= 32);
        var dv = (res & 1) ? ~(res >> 1) : (res >> 1);
        if (k === 0) lat += dv; else lon += dv;
      }
      pts.push([lat / 1e5, lon / 1e5]);
    }
    return pts;
  }
  var GC = {};
  function geom(a, b) {
    if (a === b) return [[PL[a].lat, PL[a].lon]];
    var k1 = a + '|' + b, k2 = b + '|' + a, g;
    if (GC[k1]) return GC[k1];
    if (ROADS.geo[k1]) g = dec(ROADS.geo[k1]);
    else if (ROADS.geo[k2]) g = dec(ROADS.geo[k2]).reverse();
    else {
      /* no stored geometry for this pair: chain stored road legs (shortest path by road km) */
      var hops = viaGraph(a, b);
      if (hops) { g = []; for (var i = 0; i < hops.length - 1; i++) g = g.concat(geom(hops[i], hops[i + 1])); }
      else g = [[PL[a].lat, PL[a].lon], [PL[b].lat, PL[b].lon]];
    }
    GC[k1] = g; return g;
  }
  var ADJ = null;
  function viaGraph(a, b) {
    if (!ADJ) { ADJ = {}; Object.keys(ROADS.geo).forEach(function (k) { var x = k.split('|'); (ADJ[x[0]] = ADJ[x[0]] || []).push(x[1]); (ADJ[x[1]] = ADJ[x[1]] || []).push(x[0]); }); }
    var dist = {}, prev = {}, done = {}, Q = [a]; dist[a] = 0;
    while (Q.length) {
      Q.sort(function (x, y) { return dist[x] - dist[y]; }); var u = Q.shift(); if (done[u]) continue; done[u] = 1;
      if (u === b) break;
      (ADJ[u] || []).forEach(function (v) { var d = dist[u] + km(u, v); if (dist[v] == null || d < dist[v]) { dist[v] = d; prev[v] = u; Q.push(v); } });
    }
    if (dist[b] == null || dist[b] > km(a, b) * 1.25 + 30) return null;
    var path = [b]; while (path[0] !== a) path.unshift(prev[path[0]]);
    return path;
  }

  /* ---------------- state ---------------- */
  var today = new Date(); today.setHours(0, 0, 0, 0);
  function defDate() { var d = addD(today, 21); return iso(d); }
  var S = { s: 'chandigarh', e: 'chandigarh', d: defDate(), a: 2, c: 0, i: 0, r: 0, t: 'deluxe', m: 'MAP', k: 'auto', p: [], x: [], g: null, cv: 0, tp: '' };
  var MODE = 'guest', LEAD = null;
  try { LEAD = JSON.parse(sessionStorage.getItem('suzuTpLead') || 'null'); } catch (e) {}

  function b64e(str) { var b = btoa(unescape(encodeURIComponent(str))); return b.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, ''); }
  function b64d(s) { s = s.replace(/-/g, '+').replace(/_/g, '/'); while (s.length % 4) s += '='; return decodeURIComponent(escape(atob(s))); }
  function encState(clientView) {
    var o = { v: 1, s: S.s, e: S.e, d: S.d, a: S.a, c: S.c, i: S.i, r: S.r, t: S.t, m: S.m, k: S.k, p: S.p.map(function (x) { return [x.id, x.n]; }), x: S.x, tp: S.tp };
    if (MODE === 'agent' && S.g) { o.g = S.g; if (clientView) o.cv = 1; }
    if (W.__tpLang === 'hi') o.l = 'hi'; /* v0.8: optional viewer language, still v:1 */
    return b64e(JSON.stringify(o));
  }
  function loadHash() {
    var m = location.hash.match(/[#&]t=([A-Za-z0-9_-]+)/); if (!m) return false;
    try {
      var o = JSON.parse(b64d(m[1])); if (!o || o.v !== 1) return false;
      if (PL[o.s]) S.s = o.s; if (PL[o.e]) S.e = o.e;
      if (/^\d{4}-\d\d-\d\d$/.test(o.d)) S.d = o.d;
      S.a = clamp(+o.a || 2, 1, 40); S.c = clamp(+o.c || 0, 0, 20); S.i = clamp(+o.i || 0, 0, 10); S.r = clamp(+o.r || 0, 0, 20);
      if (R.hotel.tiers.some(function (t) { return t.id === o.t; })) S.t = o.t;
      S.m = o.m === 'CP' ? 'CP' : 'MAP';
      S.k = (o.k === 'auto' || R.cab.vehicles.some(function (v) { return v.id === o.k; })) ? o.k : 'auto';
      S.p = (o.p || []).filter(function (x) { return PL[x[0]]; }).slice(0, 14).map(function (x) { return { id: x[0], n: clamp(+x[1] || 0, 0, 9) }; });
      S.x = (o.x || []).filter(function (x) { return ADDONS.some(function (a) { return a.id === x; }); });
      S.tp = typeof o.tp === 'string' ? o.tp.slice(0, 40) : '';
      if (o.g && typeof o.g === 'object') { S.g = { n: String(o.g.n || '').slice(0, 60), p: String(o.g.p || '').slice(0, 16), e: String(o.g.e || '').slice(0, 80), k: clamp(+o.g.k || 0, 0, 60) }; MODE = 'agent'; }
      S.cv = o.cv ? 1 : 0;
      if (o.l === 'hi') W.__tpLinkLang = 'hi';
      return S.p.length > 0;
    } catch (e) { return false; }
  }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }

  /* ---------------- engine ---------------- */
  function isPeak(d) {
    var md = pad(d.getMonth() + 1) + '-' + pad(d.getDate());
    return R.hotel.peak.windows.some(function (w) { return w[0] <= w[1] ? (md >= w[0] && md <= w[1]) : (md >= w[0] || md <= w[1]); });
  }
  function tier(id) { return R.hotel.tiers.filter(function (t) { return t.id === id; })[0] || R.hotel.tiers[1]; }
  function veh(id) { return R.cab.vehicles.filter(function (v) { return v.id === id; })[0]; }
  function seatsNeeded() { return S.a + S.c; }
  function autoVeh(route) {
    var n = seatsNeeded(), suv = route.some(function (id) { return R.cab.suv_places.indexOf(id) > -1; });
    var list = R.cab.vehicles;
    for (var i = 0; i < list.length; i++) {
      if (suv && (list[i].id === 'sedan' || list[i].id === 'ertiga')) continue;
      if (list[i].seats >= n) return { v: list[i], c: 1 };
    }
    var big = list[list.length - 1]; return { v: big, c: Math.ceil(n / big.seats) };
  }
  function roomsCalc() {
    var auto = S.a === 1 ? 1 : Math.floor(S.a / 2);
    var rooms = S.r > 0 ? Math.max(S.r, Math.ceil(S.a / 3)) : Math.max(1, auto);
    var extra = Math.max(0, S.a - rooms * 2);
    if (extra > rooms) { rooms = Math.ceil(S.a / 3); extra = Math.max(0, S.a - rooms * 2); }
    return { rooms: rooms, extra: extra, auto: S.r === 0 };
  }

  function compute() {
    var out = { days: [], warn: [], legs: [], route: [] };
    var d0 = parseD(S.d) || addD(today, 21);
    var stops = S.p.filter(function (x) { return PL[x.id]; });
    if (!stops.length) return null;
    var cur = S.s, dayNo = 0, date = d0, nights = [], kmDrive = 0, kmLocal = 0;
    var pending = { from: cur, via: [], km: 0, min: 0, path: [cur] };
    var visited = [cur];
    function sightsOf(id, dt) {
      var mo = dt.getMonth() + 1;
      return (PL[id].sights || []).filter(function (s) {
        if (!s.m || s.m.indexOf(mo) > -1) return true;
        var key = 'sight-' + s.n; if (!out.warn.some(function (w) { return w.k === key; }))
          out.warn.push({ r: 0, k: key, t: s.n.replace(/ \(.*\)$/, '') + ' is usually closed in ' + MS[mo - 1] + ' (open about ' + MS[s.m[0] - 1] + '–' + MS[s.m[s.m.length - 1] - 1] + '), so it is left out of your day plan.' + (id === 'manali' ? ' Snow fun in winter is at Solang Valley; Atal Tunnel & Sissu when the road is open.' : '') });
        return false;
      }).map(function (s) { return { n: s.n, km: s.km, note: s.note }; });
    }
    var left = {};
    stops.forEach(function (st, si) {
      var p = PL[st.id];
      var k = km(cur, st.id), m = mins(cur, st.id);
      pending.km += k; pending.min += m; pending.path.push(st.id);
      if (k > 0) out.legs.push([cur, st.id]);
      cur = st.id; visited.push(st.id);
      if (!left[st.id]) left[st.id] = sightsOf(st.id, date);
      if (st.n === 0) {
        var s0 = left[st.id].shift();
        pending.via.push({ id: st.id, sight: s0 });
        pending.km += s0 ? Math.min(s0.km, 20) : 0;
        return;
      }
      /* travel day ending here */
      dayNo++;
      var day = { no: dayNo, date: date, type: pending.km > 0 ? 'travel' : 'arrive', from: pending.from, to: st.id, via: pending.via, km: pending.km, min: pending.min, path: pending.path.slice(), stay: st.id, sights: [], opt: [] };
      if (dayNo === 1 && pending.km === 0) day.type = 'arrive';
      var lk = pending.km === 0 ? 25 : 10;
      if (pending.min <= 270 || pending.km === 0) {
        var short = left[st.id].filter(function (s) { return s.km <= 15; })[0];
        if (short) { day.sights.push(short); left[st.id].splice(left[st.id].indexOf(short), 1); lk += short.km; }
      }
      kmDrive += pending.km; kmLocal += lk; day.localKm = lk;
      if (pending.min > 600) out.warn.push({ r: 0, t: 'Day ' + dayNo + ': ' + PL[day.from].name + ' → ' + p.name + ' is a long drive (' + hrs(pending.min) + '). Consider a night halt on the way.' });
      out.days.push(day);
      nights.push({ id: st.id, date: date });
      date = addD(date, 1);
      for (var j = 1; j < st.n; j++) {
        dayNo++;
        var ld = { no: dayNo, date: date, type: 'local', from: st.id, to: st.id, via: [], km: 0, min: 0, path: [st.id], stay: st.id, sights: [], opt: [] };
        var budget = 0;
        while (left[st.id].length) {
          var s = left[st.id][0];
          if (ld.sights.length && (budget + s.km > 130 || s.km >= 80 || ld.sights.length >= 3)) break;
          ld.sights.push(left[st.id].shift()); budget += s.km;
          if (s.km >= 80) break;
        }
        if (!ld.sights.length) ld.sights.push({ n: 'Free day — relax, cafés, local markets', km: 15 });
        ld.localKm = Math.max(budget, 20); kmLocal += ld.localKm;
        out.days.push(ld); nights.push({ id: st.id, date: date });
        date = addD(date, 1);
      }
      var lastLocal = out.days[out.days.length - 1];
      lastLocal.opt = left[st.id].slice(0, 3);
      pending = { from: st.id, via: [], km: 0, min: 0, path: [st.id] };
    });
    /* departure day */
    dayNo++;
    var kE = km(cur, S.e), mE = mins(cur, S.e);
    pending.km += kE; pending.min += mE; pending.path.push(S.e);
    if (kE > 0) out.legs.push([cur, S.e]);
    var dep = { no: dayNo, date: date, type: 'depart', from: pending.from, to: S.e, via: pending.via, km: pending.km, min: pending.min, path: pending.path, stay: null, sights: [], opt: [], localKm: 20 };
    kmDrive += pending.km; kmLocal += 20;
    if (pending.min > 600) out.warn.push({ r: 0, t: 'Last day: ' + PL[dep.from].name + ' → ' + PL[S.e].name + ' is a long drive (' + hrs(pending.min) + '). Many guests add a night on the way.' });
    out.days.push(dep);
    out.route = visited.concat([S.e]);

    /* Kedarnath: trek up, darshan, trek down = 2 nights at Guptkashi / Sitapur */
    stops.forEach(function (st) {
      if (st.id === 'guptkashi' && st.n < 2 && !out.warn.some(function (w) { return w.k === 'kedar'; }))
        out.warn.push({ r: 1, k: 'kedar', t: 'Kedarnath needs 2 nights at ' + PL.guptkashi.name + ' (trek up, darshan, trek down — or helicopter, subject to tickets). You have ' + st.n + ' night' + (st.n === 1 ? '' : 's') + ' here; add a night for a relaxed darshan.' });
    });
    /* seasons */
    out.days.forEach(function (dy) {
      [dy.to].concat(dy.via.map(function (v) { return v.id; })).forEach(function (id) {
        var p = PL[id]; if (!p || !p.months) return;
        if (p.months.indexOf(dy.date.getMonth() + 1) < 0) {
          var key = 'season-' + id; if (out.warn.some(function (w) { return w.k === key; })) return;
          out.warn.push({ r: 1, k: key, t: p.name + ' is usually closed / snowbound in ' + MS[dy.date.getMonth()] + ' (open about ' + MS[p.months[0] - 1] + '–' + MS[p.months[p.months.length - 1] - 1] + '). Pick other dates or swap this stop.' });
        }
      });
    });

    /* Rajasthan / Agra heat (Apr–Jun) and Taj Friday closure */
    (function () {
      var hot = out.days.some(function (dy) { var m = dy.date.getMonth() + 1; return m >= 4 && m <= 6 && ['rajasthan', 'up'].indexOf(PL[dy.to].region) > -1; });
      if (hot) out.warn.push({ k: 'heat', t: 'April–June is very hot in Rajasthan and Agra (40 °C+ afternoons). We schedule forts and the Taj for early morning; October–March is the comfortable season.' });
      out.days.forEach(function (dy) { if ((dy.to === 'agra' || dy.stay === 'agra') && dy.date.getDay() === 5 && !out.warn.some(function (w) { return w.k === 'taj'; })) out.warn.push({ r: 1, k: 'taj', t: 'Taj Mahal is closed on Fridays and your Agra day falls on a Friday — shift the trip by a day or we plan the Taj for the next morning.' }); });
    })();
    /* Navratri crowds at Mata temples (dates: research/festivals.md) */
    (function () {
      var NAV = [['Sharad Navratri', '2026-10-11', '2026-10-20', '11–20 Oct 2026'], ['Chaitra Navratri', '2027-04-07', '2027-04-15', '7–15 Apr 2027'], ['Sharad Navratri', '2027-09-30', '2027-10-09', '30 Sep–9 Oct 2027']];
      var MATA = ['nainadevi', 'chintpurni', 'jwalaji', 'kangra', 'chamunda', 'katra'];
      out.days.some(function (dy) {
        var ids = [dy.to, dy.stay].concat(dy.via.map(function (v) { return v.id; }));
        var hit = ids.filter(function (id) { return MATA.indexOf(id) > -1; })[0]; if (!hit) return false;
        var t = dy.date.getTime(), f = NAV.filter(function (n) { return t >= parseD(n[1]).getTime() && t < parseD(n[2]).getTime() + 864e5; })[0];
        if (!f) return false;
        out.warn.push({ r: 0, k: 'navratri', t: 'Your ' + PL[hit].name + ' darshan falls in ' + f[0] + ' (' + f[3] + '): very big crowds, long darshan queues and hotels fill early. We plan darshan for early morning and keep extra time on these days.' + (hit === 'katra' ? ' Vaishno Devi needs a Yatra registration (RFID card) — register early.' : '') + ' Our team confirms hotel availability before you book.' });
        return true;
      });
    })();
    /* ---- cab ---- */
    var totalDays = out.days.length, nNights = nights.length;
    var av = autoVeh(out.route), v, cnt;
    if (S.k === 'auto') { v = av.v; cnt = av.c; }
    else {
      v = veh(S.k) || av.v; cnt = Math.max(1, Math.ceil(seatsNeeded() / v.seats));
      var suvNeed = out.route.some(function (id) { return R.cab.suv_places.indexOf(id) > -1; });
      if (suvNeed && (v.id === 'sedan' || v.id === 'ertiga')) out.warn.push({ r: 1, t: 'Spiti, Lahaul, Chitkul and Ladakh roads need an SUV (Innova Crysta or bigger). Your estimate uses ' + v.name + ' — our team will suggest the right car.' });
    }
    var unionDays = 0, unionF = 1, minKm = 0;
    out.days.forEach(function (dy) { var reg = PL[dy.stay || dy.to].region; var f = R.cab.local_union_factor[reg]; if (f) { unionDays++; unionF = Math.max(unionF, f); minKm += R.cab.union_min_km_per_day; } else minKm += R.cab.min_km_per_day; });
    var actual = kmDrive + kmLocal, billable = Math.max(actual, minKm);
    var uf = 1 + (unionF - 1) * (unionDays / totalDays);
    var cabBase = billable * v.rate * uf * cnt, allow = nNights * v.allow * cnt, toll = actual * R.cab.toll_parking_per_km * cnt;
    out.cab = { v: v, cnt: cnt, actual: actual, billable: billable, uf: uf, cost: cabBase + allow + toll, base: cabBase, allow: allow, toll: toll };
    if (uf > 1) out.warn.push({ r: 0, k: 'union', t: R.cab.local_union_note });

    /* ---- hotels ---- */
    var rc = roomsCalc(), tr = tier(S.t), hotel = 0, peakN = 0, rows = {};
    nights.forEach(function (nt) {
      var p = PL[nt.id], base = R.hotel.classes[p.cls].deluxe, f = tr.f;
      if (p.cls === 'remote' && f > 1.8) f = 1.8;
      var pk = isPeak(nt.date); if (pk) peakN++;
      var rate = base * f * (S.m === 'CP' ? 0.88 : 1) * (pk ? R.hotel.peak.f : 1);
      var cost = rate * rc.rooms + rate * R.hotel.extra_adult_f * rc.extra + rate * R.hotel.child_bed_f * S.c;
      hotel += cost;
      var key = nt.id;
      if (!rows[key]) rows[key] = { id: nt.id, n: 0, cost: 0, cls: p.cls, from: nt.date };
      rows[key].n++; rows[key].cost += cost;
    });
    out.hotel = { cost: hotel, rooms: rc, peakN: peakN, rows: Object.keys(rows).map(function (k) { return rows[k]; }), nights: nNights, tier: tr };
    if (peakN) out.warn.push({ r: 0, k: 'peak', t: 'Peak-season hotel rates applied for ' + peakN + ' night' + (peakN > 1 ? 's' : '') + ' (mid-Mar–Jun, October, Christmas–New Year).' });

    var sub = out.cab.cost + hotel, handling = sub * R.service.handling_f, gst = (sub + handling) * R.service.gst_f;
    var total = r100(sub + handling + gst), high = r100(total * R.service.range_high_f);
    var heads = S.a + S.c * 0.5;
    out.price = { sub: sub, handling: handling, gst: gst, total: total, high: high, pp: r100(total / heads), pph: r100(high / heads) };
    if (MODE === 'agent' && S.g) { var mk = 1 + (S.g.k || 0) / 100; out.price.client = r100(total * mk); out.price.clientPP = r100(total * mk / heads); }
    out.nights = nNights; out.totalDays = totalDays; out.kmDrive = kmDrive; out.kmTotal = actual;
    out.title = S.tp || titleFor(stops);
    return out;
  }
  function titleFor(stops) {
    var names = []; stops.forEach(function (s) { var nm = PL[s.id].name.split(' (')[0].split(' / ')[0]; if (names.indexOf(nm) < 0) names.push(nm); });
    if (names.length > 4) return names.slice(0, 3).join(' – ') + ' & more';
    return names.join(' – ');
  }

  /* ---------------- search (destinations + ideas) ---------------- */
  var KEYS = { mata: 'mata devi shakti peeth darshan naina chintpurni jwala kangra chamunda vaishno navratri माता देवी', pilgrim: 'yatra char dham kedarnath badrinath gangotri yamunotri pilgrimage golden temple तीर्थ धाम', honeymoon: 'honeymoon couple romantic हनीमून', kashmir: 'kashmir srinagar gulmarg pahalgam कश्मीर', ladakh: 'ladakh leh pangong nubra bike लद्दाख', himachal: 'himachal shimla manali spiti kinnaur dharamshala हिमाचल', uttarakhand: 'uttarakhand rishikesh mussoorie nainital corbett kumaon auli chopta kainchi उत्तराखंड', rajasthan: 'rajasthan jaipur jodhpur jaisalmer udaipur agra taj mahal golden triangle mathura vrindavan desert heritage राजस्थान आगरा' };
  function search(q, onlyPlaces) {
    q = q.trim().toLowerCase();
    var res = [];
    if (!onlyPlaces) TPL.forEach(function (t) {
      var hay = (t.name + ' ' + t.hi + ' ' + (KEYS[t.cat] || '') + ' ' + t.stops.map(function (s) { return PL[s[0]].name; }).join(' ')).toLowerCase();
      var sc = !q ? 1 : (t.name.toLowerCase().indexOf(q) > -1 ? 3 : hay.indexOf(q) > -1 ? 2 : 0);
      if (sc) res.push({ k: 'tpl', t: t, sc: sc + 0.5 });
    });
    DATA.places.forEach(function (p) {
      if (p.kind === 'hub' && onlyPlaces !== 'all') { if (!q) return; }
      var hay = (p.name + ' ' + p.hi + ' ' + (REGLBL[p.region] || '') + ' ' + p.sights.map(function (s) { return s.n; }).join(' ')).toLowerCase();
      var sc = !q ? (p.kind === 'hub' ? 0 : 0.5) : (p.name.toLowerCase().indexOf(q) === 0 ? 4 : p.name.toLowerCase().indexOf(q) > -1 || p.hi.indexOf(q) > -1 ? 3 : hay.indexOf(q) > -1 ? 1 : 0);
      if (sc) res.push({ k: 'place', p: p, sc: sc });
    });
    res.sort(function (a, b) { return b.sc - a.sc; });
    return res.slice(0, q ? 12 : 10);
  }
  function ddRender(box, items, onPick) {
    if (!items.length) { box.innerHTML = '<div class="hd">No match — try another place</div>'; box.hidden = false; return; }
    var h = '', lastK = '';
    items.forEach(function (it, i) {
      if (it.k !== lastK) { h += '<div class="hd">' + (it.k === 'tpl' ? 'Ready trip ideas' : 'Places') + '</div>'; lastK = it.k; }
      if (it.k === 'tpl') {
        var n = it.t.stops.reduce(function (a, s) { return a + s[1]; }, 0);
        h += '<button type="button" role="option" data-i="' + i + '"><span class="ic">' + (it.t.cat === 'mata' ? '🛕' : it.t.cat === 'pilgrim' ? '🙏' : it.t.cat === 'honeymoon' ? '💑' : '🗺️') + '</span><span><b>' + esc(it.t.name) + '</b><small>' + (n + 1) + ' days · from ' + esc(PL[it.t.start].name) + '</small></span></button>';
      } else {
        h += '<button type="button" role="option" data-i="' + i + '"><span class="ic">' + (it.p.kind === 'temple' ? '🛕' : it.p.kind === 'hub' ? '🏙️' : '⛰️') + '</span><span><b>' + esc(it.p.name) + ' <span class="dv" style="font-weight:400;color:var(--mut)">' + esc(it.p.hi) + '</span></b><small>' + esc(REGLBL[it.p.region] || '') + (it.p.sights[0] ? ' · ' + esc(it.p.sights[0].n) : '') + '</small></span></button>';
      }
    });
    box.innerHTML = h; box.hidden = false;
    box.onclick = function (e) { var b = e.target.closest('button[data-i]'); if (!b) return; box.hidden = true; onPick(items[+b.dataset.i]); };
  }
  function wireSearch(input, box, onPick, onlyPlaces) {
    var items = [], act = -1;
    function upd() { items = search(input.value, onlyPlaces); act = -1; ddRender(box, items, onPick); input.setAttribute('aria-expanded', 'true'); }
    input.addEventListener('focus', upd); input.addEventListener('input', upd);
    input.addEventListener('keydown', function (e) {
      var bs = $$('button[data-i]', box);
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') { e.preventDefault(); act = clamp(act + (e.key === 'ArrowDown' ? 1 : -1), 0, bs.length - 1); bs.forEach(function (b, i) { b.classList.toggle('on', i === act); }); }
      else if (e.key === 'Enter') { e.preventDefault(); var i = act >= 0 ? act : 0; if (items[i]) { box.hidden = true; onPick(items[i]); } }
      else if (e.key === 'Escape') { box.hidden = true; }
    });
    D.addEventListener('click', function (e) { if (!box.contains(e.target) && e.target !== input) { box.hidden = true; input.setAttribute('aria-expanded', 'false'); } });
  }

  /* ---------------- plan loading ---------------- */
  function loadTpl(t, from) {
    S.s = from && PL[from] && t.start === 'chandigarh' && PL[from].kind === 'hub' ? from : t.start;
    S.e = S.s === t.start ? t.end : S.s;
    S.p = t.stops.map(function (s) { return { id: s[0], n: s[1] }; });
    S.tp = t.name; S.x = [];
    if (t.months) {
      var d = parseD(S.d) || today;
      if (t.months.indexOf(d.getMonth() + 1) < 0) {
        for (var i = 0; i < 12; i++) { var c = new Date(d.getFullYear(), d.getMonth() + i, 10); if (t.months.indexOf(c.getMonth() + 1) > -1 && c > today) { S.d = iso(c); toast('Date moved to ' + fmtLong(c) + ' — ' + t.name + ' is a seasonal trip'); break; } }
      }
    }
    ev('trip_planner', { step: 'template', id: t.id });
    openWs();
  }
  function loadPlace(p, from) {
    if (p.kind === 'hub' && !from) { S.s = p.id; S.e = p.id; toast('Pickup set to ' + p.name + ' — now add places'); openWs(); return; }
    S.s = from && PL[from] ? from : nearestHub(p.id);
    S.e = S.s; S.tp = '';
    S.p = [{ id: p.id, n: p.kind === 'temple' ? 1 : 3 }];
    ev('trip_planner', { step: 'place', id: p.id });
    openWs();
  }
  function nearestHub(id) {
    var best = 'chandigarh', bk = 1e9;
    DATA.places.forEach(function (h) { if (h.kind !== 'hub') return; var k = km(h.id, id); if (k > 0 && k < bk) { bk = k; best = h.id; } });
    return best;
  }
  var wsOpen = false;
  function openWs() {
    var ws = $('#ws'); ws.hidden = false; $('#mbar').hidden = false;
    renderAll(true);
    if (!wsOpen) { wsOpen = true; setTimeout(function () { ws.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 60); }
    else ws.scrollIntoView({ behavior: 'smooth', block: 'start' });
    pushHash();
  }
  function pushHash() { try { history.replaceState(null, '', '#t=' + encState(!!S.cv)); } catch (e) {} }

  /* ---------------- render: builder ---------------- */
  function placeOptions(sel, val, filter) {
    var groups = {};
    DATA.places.forEach(function (p) { if (filter && !filter(p)) return; var g = p.kind === 'hub' ? 'Cities & airports' : (REGLBL[p.region] || 'Other'); (groups[g] = groups[g] || []).push(p); });
    var order = ['Cities & airports', 'Himachal', 'Mata darshan', 'Kashmir', 'Ladakh', 'Uttarakhand', 'Rajasthan', 'Agra & Mathura', 'Punjab'];
    sel.innerHTML = order.filter(function (g) { return groups[g]; }).map(function (g) {
      return '<optgroup label="' + g + '">' + groups[g].map(function (p) { return '<option value="' + p.id + '"' + (p.id === val ? ' selected' : '') + '>' + esc(p.name) + '</option>'; }).join('') + '</optgroup>';
    }).join('');
  }
  function renderBuilder() {
    placeOptions($('#b-start'), S.s); placeOptions($('#b-end'), S.e);
    var ol = $('#b-stops'), h = '';
    h += '<li class="stop hub"><span class="dot">S</span><span class="nm"><b>' + esc(PL[S.s].name) + '</b><small>Pickup · ' + fmtD(parseD(S.d)) + '</small></span><span></span></li>';
    S.p.forEach(function (st, i) {
      var p = PL[st.id];
      h += '<li class="stop' + (st.n === 0 ? ' pass' : '') + '" data-i="' + i + '"><span class="dot">' + (i + 1) + '</span><span class="nm"><b>' + esc(p.name) + '</b><small>' + (st.n === 0 ? 'Visit on the way · no night' : st.n + ' night' + (st.n > 1 ? 's' : '')) + '</small></span>' +
        '<span class="ctl"><span class="nights" aria-label="Nights at ' + esc(p.name) + '"><button type="button" data-a="dn" aria-label="One night less">−</button><output>' + st.n + 'N</output><button type="button" data-a="up" aria-label="One night more">+</button></span>' +
        '<button type="button" class="ib" data-a="mu" aria-label="Move up"' + (i === 0 ? ' disabled' : '') + '>↑</button><button type="button" class="ib" data-a="rm" aria-label="Remove ' + esc(p.name) + '">×</button></span></li>';
    });
    h += '<li class="stop hub"><span class="dot">E</span><span class="nm"><b>' + esc(PL[S.e].name) + '</b><small>Drop</small></span><span></span></li>';
    ol.innerHTML = h;
    /* suggestions: near the last stop, not yet in plan */
    var last = S.p.length ? S.p[S.p.length - 1].id : S.s, have = S.p.map(function (x) { return x.id; });
    var near = DATA.places.filter(function (p) { return p.kind !== 'hub' && have.indexOf(p.id) < 0 && km(last, p.id) > 0; })
      .map(function (p) { return [km(last, p.id), p]; }).sort(function (a, b) { return a[0] - b[0]; }).slice(0, 5);
    $('#b-sugg').innerHTML = near.length ? '<small style="width:100%;color:var(--mut);font-weight:700;font-size:12px">Near ' + esc(PL[last].name) + ':</small>' + near.map(function (x) { return '<button type="button" class="chip" data-add="' + x[1].id + '">+ ' + esc(x[1].name.split(' (')[0]) + ' <small style="color:var(--mut)">' + x[0] + ' km</small></button>'; }).join('') : '';
    $('#b-date').value = S.d; $('#b-date').min = iso(today);
    $$('.step').forEach(function (st) {
      var k = st.dataset.k, v = k === 'rooms' ? roomsCalc().rooms : S[k[0] === 'a' ? 'a' : k === 'ch' ? 'c' : k === 'inf' ? 'i' : 'r'];
      st.querySelector('output').textContent = v;
      st.querySelector('button').disabled = (k === 'ad' && S.a <= 1) || (k === 'ch' && S.c <= 0) || (k === 'inf' && S.i <= 0) || (k === 'rooms' && v <= 1);
    });
    $('#b-rooms-s').textContent = roomsCalc().auto ? 'auto' : 'set by you';
    $('#b-tiers').innerHTML = R.hotel.tiers.map(function (t) { return '<button type="button" data-t="' + t.id + '" aria-pressed="' + (S.t === t.id) + '"><b>' + esc(t.name.split(' (')[0]) + '</b><small>' + esc((t.name.match(/\((.*)\)/) || ['', ''])[1]) + '</small></button>'; }).join('');
    $('#b-meal').value = S.m;
    var vs = $('#b-veh'); vs.innerHTML = '<option value="auto">Best for group</option>' + R.cab.vehicles.map(function (v) { return '<option value="' + v.id + '">' + esc(v.name) + ' · ' + v.seats + ' seats</option>'; }).join(''); vs.value = S.k;
    var near2 = S.p.map(function (x) { return x.id; });
    $('#b-adds').innerHTML = ADDONS.filter(function (a) { return !a.at.length || a.at.some(function (id) { return near2.indexOf(id) > -1; }); })
      .map(function (a) { return '<button type="button" class="chip" data-x="' + a.id + '" aria-pressed="' + (S.x.indexOf(a.id) > -1) + '">' + (S.x.indexOf(a.id) > -1 ? '✓ ' : '+ ') + esc(a.n) + '</button>'; }).join('');
    var ab = $('#b-agent'); ab.hidden = MODE !== 'agent' || !!S.cv;
    if (MODE === 'agent' && !S.cv) { S.g = S.g || { n: '', p: '', e: '', k: R.b2b.default_markup_pct }; $('#ag-name').value = S.g.n; $('#ag-phone').value = S.g.p; $('#ag-email').value = S.g.e; $('#ag-mk').value = S.g.k; }
  }

  /* ---------------- render: map (animated SVG) ---------------- */
  var MAP = { segs: [] };
  function renderMap(plan, animate) {
    var svg = $('#rm'), box = $('#mapbox'), Wd = box.clientWidth || 800, Ht = box.clientHeight || 420;
    svg.setAttribute('viewBox', '0 0 ' + Wd + ' ' + Ht);
    var pts = [];
    plan.days.forEach(function (dy) { for (var i = 0; i < dy.path.length - 1; i++) pts = pts.concat(geom(dy.path[i], dy.path[i + 1])); });
    plan.route.forEach(function (id) { pts.push([PL[id].lat, PL[id].lon]); });
    var la = pts.map(function (p) { return p[0]; }), lo = pts.map(function (p) { return p[1]; });
    var mnLa = Math.min.apply(0, la), mxLa = Math.max.apply(0, la), mnLo = Math.min.apply(0, lo), mxLo = Math.max.apply(0, lo);
    var cLa = (mnLa + mxLa) / 2, cos = Math.cos(cLa * Math.PI / 180);
    var spLa = Math.max(mxLa - mnLa, 0.9), spLo = Math.max((mxLo - mnLo) * cos, 0.9);
    var sc = Math.min((Wd * 0.8) / spLo, (Ht * 0.74) / spLa);
    var cx = (mnLo + mxLo) / 2;
    function P(lat, lon) { return [Wd / 2 + (lon - cx) * cos * sc, Ht / 2 - (lat - cLa) * sc + 8]; }
    function inView(x, y) { return x > -20 && x < Wd + 20 && y > -20 && y < Ht + 20; }
    var h = '<defs><pattern id="hx" width="22" height="22" patternUnits="userSpaceOnUse" patternTransform="rotate(30)"><path d="M0 11h22" stroke="#dfeae3" stroke-width="1"/></pattern>' +
      '<radialGradient id="glow"><stop offset="0" stop-color="#c9962b" stop-opacity=".5"/><stop offset="1" stop-color="#c9962b" stop-opacity="0"/></radialGradient></defs>' +
      '<rect width="100%" height="100%" fill="url(#hx)"/>';
    [['HIMACHAL', 31.75, 77.3], ['JAMMU & KASHMIR', 33.55, 75.1], ['LADAKH', 34.35, 77.9], ['UTTARAKHAND', 30.15, 79.15], ['PUNJAB', 30.95, 75.35], ['HARYANA', 29.4, 76.4], ['RAJASTHAN', 26.6, 73.6], ['UTTAR PRADESH', 27.4, 78.9]].forEach(function (r) {
      var q = P(r[1], r[2]), wR = r[0].length * 13; if (q[0] - wR / 2 > 8 && q[0] + wR / 2 < Wd - 8 && q[1] > 30 && q[1] < Ht - 40) h += '<text class="reg" x="' + q[0].toFixed(1) + '" y="' + q[1].toFixed(1) + '" text-anchor="middle">' + r[0] + '</text>';
    });
    var onRoute = {}; plan.route.forEach(function (id) { onRoute[id] = 1; });
    var dimLbl = spLa < 4.5, boxes = [], dimH = '';
    function free(x, y, w, hh) { if (x < 2 || x + w > Wd - 2 || y < 2 || y + hh > Ht - 2) return false; for (var i = 0; i < boxes.length; i++) { var b = boxes[i]; if (x < b[0] + b[2] && x + w > b[0] && y < b[1] + b[3] && y + hh > b[1]) return false; } boxes.push([x, y, w, hh]); return true; }
    var DIMS = [];
    DATA.places.forEach(function (p) {
      if (onRoute[p.id]) return; var q = P(p.lat, p.lon); if (!inView(q[0], q[1])) return;
      h += '<circle class="dim" cx="' + q[0].toFixed(1) + '" cy="' + q[1].toFixed(1) + '" r="3"/>';
      if (dimLbl) DIMS.push([p, q]);
    });
    /* per-day path segments */
    MAP.segs = [];
    var all = '';
    plan.days.forEach(function (dy, di) {
      var g = [];
      for (var i = 0; i < dy.path.length - 1; i++) g = g.concat(geom(dy.path[i], dy.path[i + 1]));
      if (g.length < 2) { MAP.segs.push(null); return; }
      var d = g.map(function (p, i) { var q = P(p[0], p[1]); return (i ? 'L' : 'M') + q[0].toFixed(1) + ' ' + q[1].toFixed(1); }).join('');
      MAP.segs.push(d); all += d;
    });
    h += '<path class="route-bg" d="' + all + '"/><path class="route" id="rm-route" d="' + all + '"/>';
    MAP.segs.forEach(function (d, i) { if (d) h += '<path id="rm-seg-' + i + '" d="' + d + '" fill="none" stroke="none"/>'; });
    /* pins */
    var stopN = {}; S.p.forEach(function (st, i) { if (!stopN[st.id]) stopN[st.id] = []; stopN[st.id].push(i + 1); });
    var pinsH = '', lblH = '';
    function pin(id, label, cls, big) {
      var p = PL[id], q = P(p.lat, p.lon), nm = p.name.split(' (')[0].split(' / ')[0], w = nm.length * 7.6 + 4;
      var right = q[0] + 16 + w < Wd - 4, x = right ? q[0] + 16 : q[0] - 16 - w, y = q[1] - 9;
      if (!free(x, y, w, 16)) { if (free(x, y + 16, w, 16)) y += 16; else if (free(x, y - 16, w, 16)) y -= 16; else boxes.push([x, y, w, 16]); }
      boxes.push([q[0] - 12, q[1] - 12, 24, 24]);
      pinsH += '<g class="pin ' + cls + '" data-id="' + id + '" transform="translate(' + q[0].toFixed(1) + ' ' + q[1].toFixed(1) + ')"><circle r="' + (big ? 12 : 10) + '"/><text>' + label + '</text></g>';
      lblH += '<text class="lbl big" x="' + x.toFixed(1) + '" y="' + (y + 12).toFixed(1) + '">' + esc(nm) + '</text>';
    }
    if (S.s === S.e) pin(S.s, '★', 'hub', 1); else { pin(S.s, 'S', 'hub', 1); pin(S.e, 'E', 'hub', 1); }
    Object.keys(stopN).forEach(function (id) { if (id === S.s || id === S.e) return; pin(id, stopN[id].join(','), '', 0); });
    DIMS.forEach(function (d) { var nm = d[0].name.split(' (')[0].split(' / ')[0], w = nm.length * 6.4 + 2, x = d[1][0] + 6, y = d[1][1] - 6; if (free(x, y, w, 13)) dimH += '<text class="lbl" x="' + x.toFixed(1) + '" y="' + (y + 10).toFixed(1) + '" style="fill:#8aa496;font-weight:600">' + esc(nm) + '</text>'; });
    h += dimH + pinsH + lblH;
    h += '<circle id="rm-glow" r="26" fill="url(#glow)" opacity="0"/><g class="car" id="rm-car" opacity="0"><circle r="11" fill="#c9962b" stroke="#fff" stroke-width="3"/><path d="M-5 2v-3l1.5-3h7l1.5 3v3z M-4 2v1.5 M4 2v1.5" stroke="#2b1d02" stroke-width="1.4" fill="#fff"/></g>';
    svg.innerHTML = h;
    var rt = $('#rm-route');
    if (animate && rt && rt.getTotalLength && !W.matchMedia('(prefers-reduced-motion:reduce)').matches) {
      var L = rt.getTotalLength(); rt.style.strokeDasharray = L; rt.style.strokeDashoffset = L;
      rt.getBoundingClientRect(); rt.style.transition = 'stroke-dashoffset 1.6s ease'; rt.style.strokeDashoffset = '0';
    }
    $('#m-stat').innerHTML = '<span>🛣 ' + plan.kmDrive.toLocaleString('en-IN') + ' km road trip</span><span>🌙 ' + plan.nights + ' nights</span><span>🚗 ' + esc(plan.cab.v.name.split(' (')[0]) + (plan.cab.cnt > 1 ? ' × ' + plan.cab.cnt : '') + '</span>';
    MAP.P = P;
    if (leafOn) drawLeaf(plan);
  }
  var playing = 0;
  function play() {
    var plan = LAST; if (!plan) return;
    if (playing) { playing = 0; return; }
    playing = 1; $('#m-play').textContent = '■ Stop';
    var car = $('#rm-car'), glow = $('#rm-glow'), di = 0;
    car.setAttribute('opacity', '1');
    ev('trip_planner', { step: 'play' });
    function hi(i) { $$('.tl-day').forEach(function (x, j) { x.classList.toggle('on', j === i); }); $$('#rm .pin').forEach(function (g) { g.classList.toggle('on', plan.days[i] && (g.dataset.id === plan.days[i].to)); }); }
    function moveTo(x, y) { car.setAttribute('transform', 'translate(' + x.toFixed(1) + ' ' + y.toFixed(1) + ')'); glow.setAttribute('cx', x); glow.setAttribute('cy', y); }
    function next() {
      if (!playing || di >= plan.days.length) { stop(); return; }
      hi(di);
      var seg = $('#rm-seg-' + di), dy = plan.days[di];
      if (seg && seg.getTotalLength) {
        var L = seg.getTotalLength(), dur = clamp(dy.km * 6, 900, 3200), t0 = 0;
        var step = function (ts) {
          if (!playing) return stop();
          if (!t0) t0 = ts; var k = Math.min(1, (ts - t0) / dur), e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;
          var pt = seg.getPointAtLength(L * e); moveTo(pt.x, pt.y);
          if (k < 1) requestAnimationFrame(step); else { di++; setTimeout(next, 450); }
        };
        requestAnimationFrame(step);
      } else {
        var p = PL[dy.stay || dy.to], q = MAP.P(p.lat, p.lon); moveTo(q[0], q[1]);
        glow.setAttribute('opacity', '1'); setTimeout(function () { glow.setAttribute('opacity', '0'); di++; next(); }, 900);
      }
    }
    function stop() { playing = 0; $('#m-play').textContent = '▶ Play my trip'; setTimeout(function () { if (!playing) { car.setAttribute('opacity', '0'); hi(-1); } }, 1200); }
    next();
  }

  /* real map (Leaflet, lazy) */
  var leafOn = false, LMAP = null, LLAY = null;
  function loadLeaflet(cb) {
    if (W.L) return cb();
    var css = D.createElement('link'); css.rel = 'stylesheet'; css.href = 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css'; D.head.appendChild(css);
    var s = D.createElement('script'); s.src = 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js'; s.onload = cb; s.onerror = function () { toast('Real map could not load — showing the route sketch'); leafToggle(false); }; D.head.appendChild(s);
  }
  function drawLeaf(plan) {
    if (!W.L) return;
    if (!LMAP) {
      LMAP = W.L.map('leaf', { zoomControl: true, attributionControl: true, scrollWheelZoom: false });
      W.L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', { maxZoom: 15, subdomains: 'abcd', attribution: '© OpenStreetMap, © CARTO' }).addTo(LMAP);
    }
    if (LLAY) LMAP.removeLayer(LLAY);
    LLAY = W.L.layerGroup().addTo(LMAP);
    var line = [];
    plan.days.forEach(function (dy) { for (var i = 0; i < dy.path.length - 1; i++) line = line.concat(geom(dy.path[i], dy.path[i + 1])); });
    if (line.length > 1) W.L.polyline(line, { color: '#1f7a45', weight: 5, opacity: .9 }).addTo(LLAY);
    var seen = {};
    plan.route.forEach(function (id, i) {
      if (seen[id]) return; seen[id] = 1;
      var p = PL[id], hub = id === S.s || id === S.e;
      W.L.circleMarker([p.lat, p.lon], { radius: hub ? 9 : 7, color: hub ? '#c9962b' : '#1f7a45', weight: 3, fillColor: '#fff', fillOpacity: 1 }).bindTooltip(p.name, { permanent: true, direction: 'right', offset: [8, 0] }).addTo(LLAY);
    });
    var b = W.L.latLngBounds(line.length ? line : plan.route.map(function (id) { return [PL[id].lat, PL[id].lon]; }));
    LMAP.invalidateSize(); LMAP.fitBounds(b, { padding: [30, 30] });
  }
  function leafToggle(on) {
    leafOn = on; $('#leaf').hidden = !on; $('#m-real').setAttribute('aria-pressed', on); $('#m-real').textContent = on ? 'Route sketch' : 'Real map';
    $('#m-play').hidden = on;
    if (on) loadLeaflet(function () { if (LAST) drawLeaf(LAST); });
  }

  /* ---------------- render: timeline ---------------- */
  function dayTitle(dy) {
    var f = PL[dy.from], t = PL[dy.to];
    if (dy.type === 'arrive') return 'Arrive in ' + t.name;
    if (dy.type === 'local') return t.name.split(' (')[0] + ' — ' + (dy.sights[0] ? dy.sights[0].n.split(' (')[0] : 'sightseeing');
    if (dy.type === 'depart') return dy.km ? f.name.split(' (')[0] + ' → ' + t.name + ' · departure' : 'Departure from ' + t.name;
    return f.name.split(' (')[0] + ' → ' + t.name.split(' (')[0];
  }
  function dayLines(dy) {
    var L = [];
    if (dy.type === 'travel' || (dy.type === 'depart' && dy.km)) {
      var pick = dy.no === 1 ? 'Pickup in ' + PL[dy.from].name + (PL[dy.from].tip ? ' (' + PL[dy.from].tip + ')' : '') + ', then drive' : 'After breakfast, drive';
      L.push(pick + ' to ' + PL[dy.to].name + '.');
    }
    dy.via.forEach(function (v) { L.push((PL[v.id].kind === 'temple' ? '🛕 Darshan at ' : 'Stop at ') + PL[v.id].name + (v.sight ? ' — ' + v.sight.n : '') + ' on the way.'); });
    dy.sights.forEach(function (s, i) { L.push((dy.type === 'local' ? '' : 'Evening: ') + s.n + (s.note ? ' (' + s.note + ')' : '') + '.'); });
    if (dy.type === 'arrive' && PL[dy.to].tip) L.push(PL[dy.to].tip + '.');
    if (dy.type === 'travel' && PL[dy.to].tip) L.push('Tip: ' + PL[dy.to].tip + '.');
    if (dy.type === 'depart') L.push(dy.km ? 'Drop at ' + PL[dy.to].name + ' — journey ends with happy memories.' : 'Check out and drop at the airport / station.');
    if (dy.opt && dy.opt.length) L.push('Also possible: ' + dy.opt.map(function (s) { return s.n.split(' (')[0]; }).join(', ') + '.');
    return L;
  }
  function renderTimeline(plan) {
    var h = '';
    plan.days.forEach(function (dy) {
      var meta = [];
      if (dy.km) meta.push('<span>🛣 ' + dy.km + ' km · ' + hrs(dy.min) + '</span>');
      if (dy.stay) meta.push('<span class="st">🏨 Night in ' + esc(PL[dy.stay].name.split(' (')[0]) + '</span>');
      if (dy.min > 600) meta.push('<span class="w">Long drive</span>');
      h += '<div class="tl-day" data-d="' + (dy.no - 1) + '"><div class="dn"><b><span>' + dy.no + '</span>DAY</b><small>' + fmtD(dy.date) + '</small></div><div><h4>' + esc(dayTitle(dy)) + '</h4><div class="meta">' + meta.join('') + '</div><ul>' + dayLines(dy).map(function (l) { return '<li>' + esc(l) + '</li>'; }).join('') + '</ul></div></div>';
    });
    $('#tl').innerHTML = h;
    $('#warns').innerHTML = plan.warn.map(function (w) { return '<div class="warn' + (w.r ? ' r' : '') + '">' + esc(w.t) + '</div>'; }).join('');
    $('#m-title').textContent = plan.title;
    $('#m-sub').textContent = plan.totalDays + ' days / ' + plan.nights + ' nights · ' + fmtLong(plan.days[0].date) + ' – ' + fmtLong(plan.days[plan.days.length - 1].date) + ' · ' + paxText();
  }
  function paxText() { return S.a + ' adult' + (S.a > 1 ? 's' : '') + (S.c ? ', ' + S.c + ' child' + (S.c > 1 ? 'ren' : '') : '') + (S.i ? ', ' + S.i + ' infant' + (S.i > 1 ? 's' : '') : ''); }

  /* ---------------- render: price ---------------- */
  function renderPrice(plan) {
    var p = plan.price, c = plan.cab, ho = plan.hotel, cv = S.cv && S.g;
    var h = '<div class="hd"><small>' + (cv ? 'Trip price' : 'Estimated price') + '</small>';
    if (cv) h += '<div class="big">' + inr(p.clientPP) + ' <span>/ adult</span></div><div class="rng">Total ' + inr(p.client) + ' for ' + esc(paxText()) + '</div>';
    else h += '<div class="big">' + inr(p.pp) + ' <span>/ adult</span></div><div class="rng">Range ' + inr(p.pp) + ' – ' + inr(p.pph) + ' · Total ' + inr(p.total) + '</div>';
    h += '</div><div class="bd">';
    if (!cv) {
      h += '<table><tr><td>Private ' + esc(c.v.name.split(' (')[0]) + (c.cnt > 1 ? ' × ' + c.cnt : '') + '<small>' + plan.kmTotal.toLocaleString('en-IN') + ' km incl. sightseeing · driver, tolls, parking</small></td><td>' + inr(c.cost) + '</td></tr>' +
        '<tr><td>Hotels · ' + esc(ho.tier.name.split(' (')[0]) + '<small>' + ho.nights + ' nights · ' + ho.rooms.rooms + ' room' + (ho.rooms.rooms > 1 ? 's' : '') + (ho.rooms.extra ? ' + ' + ho.rooms.extra + ' extra bed' : '') + ' · ' + (S.m === 'MAP' ? 'breakfast + dinner' : 'breakfast') + '</small></td><td>' + inr(ho.cost) + '</td></tr>' +
        '<tr><td>Service &amp; GST (5%)</td><td>' + inr(p.handling + p.gst) + '</td></tr>' +
        '<tr class="tot"><td>Estimated total</td><td>' + inr(p.total) + '</td></tr></table>';
      if (S.x.length) h += '<p style="font-size:12.5px;color:var(--mut);margin:8px 0 0">Add-ons on request: ' + esc(S.x.map(function (x) { return ADDONS.filter(function (a) { return a.id === x; })[0].n; }).join(', ')) + '</p>';
      if (MODE === 'agent' && S.g) h += '<div class="agent"><b>Agent view</b><br>Suzu B2B estimate: ' + inr(p.total) + '<br>Your client price (+' + S.g.k + '%): <b>' + inr(p.client) + '</b> · ' + inr(p.clientPP) + '/adult</div>';
    } else {
      h += '<p style="margin:0;font-size:13.5px">Includes private car with driver, ' + plan.nights + ' nights hotel (' + esc(ho.tier.name) + ', ' + (S.m === 'MAP' ? 'breakfast + dinner' : 'breakfast') + '), tolls, parking and taxes. Prepared by <b>' + esc(S.g.n || 'your travel agent') + '</b>.</p>';
    }
    h += '</div><div class="ctas">';
    if (cv) {
      var ph = (S.g.p || '').replace(/\D/g, '');
      if (ph) h += '<a class="btn w" href="https://wa.me/' + (ph.length === 10 ? '91' + ph : ph) + '?text=' + encodeURIComponent('Hi, I want to book this trip: ' + plan.title + ' — ' + location.href) + '" target="_blank" rel="noopener">Book with ' + esc(S.g.n || 'agent') + '</a>';
      h += '<button type="button" class="btn s" data-act="pdf">⬇ Download PDF</button>';
    } else {
      h += '<button type="button" class="btn p" data-act="price">' + (MODE === 'agent' ? 'Get B2B rates & availability' : 'Get best price & availability') + '</button>' +
        '<button type="button" class="btn d" data-act="pdf"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>Download itinerary (PDF)</button>' +
        '<button type="button" class="btn s" data-act="share"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg>' + (MODE === 'agent' ? 'Client link (your branding)' : 'Share link') + '</button>' +
        '<a class="btn w" href="' + waLink(plan) + '" target="_blank" rel="noopener" data-act="wa">Chat on WhatsApp</a>';
    }
    h += '</div>';
    if (!cv) h += cmpHtml(plan);
    if (!cv) h += '<p class="fine"><b>Estimate, not a quote.</b> Built from 2026 market rates for private cars and ' + esc(ho.tier.name) + ' hotels, kept on the higher side. Final price after we check your dates — our team often beats it, and any discounts are added on top. Flights/trains, entry tickets, activities and permits are extra.</p>';
    $('#price').innerHTML = h;
    $('#mb-pp').textContent = inr(cv ? p.clientPP : p.pp);
  }

  /* ---------------- compare 2 plans (v1.3) — kept in this browser tab only ---------------- */
  var CMP = null, CMPK = ['s', 'e', 'd', 'a', 'c', 'i', 'r', 't', 'm', 'k', 'x', 'tp'];
  function snapS() { var o = {}; CMPK.forEach(function (k) { o[k] = Array.isArray(S[k]) ? S[k].slice() : S[k]; }); o.p = S.p.map(function (x) { return { id: x.id, n: x.n }; }); return o; }
  function sumOf(plan) {
    var ag = MODE === 'agent' && S.g && S.g.k;
    return { title: plan.title, dn: plan.totalDays + 'D / ' + plan.nights + 'N', from: fmtD(plan.days[0].date), hotel: plan.hotel.tier.name.split(' (')[0], meal: S.m === 'MAP' ? 'Breakfast + dinner' : 'Breakfast only', car: (plan.cab.cnt > 1 ? plan.cab.cnt + ' × ' : '') + plan.cab.v.name.split(' (')[0], km: plan.kmTotal, pp: ag ? plan.price.clientPP : plan.price.pp, total: ag ? plan.price.client : plan.price.total, pax: paxText() };
  }
  function cmpHtml(plan) {
    if (!CMP) return '<div class="cmp"><button type="button" class="chip" data-cmp="keep">📌 Keep this as Plan A &amp; compare</button><small>Change hotels, car, nights or places — see both prices side by side.</small></div>';
    var a = CMP.sum, b = sumOf(plan), rows = [['Trip', a.title, b.title], ['Days', a.dn, b.dn], ['Start', a.from, b.from], ['Travellers', a.pax, b.pax], ['Hotels', a.hotel, b.hotel], ['Meals', a.meal, b.meal], ['Car', a.car, b.car], ['Road km', a.km.toLocaleString('en-IN'), b.km.toLocaleString('en-IN')], ['Per adult', inr(a.pp), inr(b.pp)], ['Total', inr(a.total), inr(b.total)]];
    var d = b.pp - a.pp, dt = Math.abs(d) < 100 ? 'Both plans cost about the same per adult.' : 'This plan is ' + inr(Math.abs(d)) + ' per adult ' + (d < 0 ? 'cheaper' : 'costlier') + ' than Plan A.';
    return '<div class="cmp on"><b class="cmp-h">Compare plans</b><table><tr><th></th><th>Plan A</th><th>This plan</th></tr>' + rows.map(function (r) { return '<tr' + (r[1] !== r[2] ? ' class="df"' : '') + '><td>' + r[0] + '</td><td>' + esc(r[1]) + '</td><td>' + esc(r[2]) + '</td></tr>'; }).join('') + '</table><p class="cmp-d' + (d < -99 ? ' lo' : '') + '">' + dt + '</p><div class="cmp-b"><button type="button" class="chip" data-cmp="swap">⇄ Go back to Plan A</button><button type="button" class="chip" data-cmp="keep">📌 Keep this as Plan A</button><button type="button" class="chip" data-cmp="clr">✕ Close compare</button></div></div>';
  }
  function cmpAct(a) {
    if (!LAST) return;
    if (a === 'keep') { CMP = { st: snapS(), sum: sumOf(LAST) }; toast('Saved as Plan A — now change anything to compare'); ev('trip_planner', { step: 'compare_keep' }); renderPrice(LAST); return; }
    if (a === 'clr') { CMP = null; renderPrice(LAST); return; }
    if (a === 'swap' && CMP) {
      var cur = { st: snapS(), sum: sumOf(LAST) };
      Object.keys(CMP.st).forEach(function (k) { S[k] = CMP.st[k]; });
      CMP = cur; $('#b-veh').value = S.k; $('#b-meal').value = S.m;
      toast('Back to Plan A — your other plan is now Plan A'); ev('trip_planner', { step: 'compare_swap' }); change(true);
    }
  }

  /* ---------------- budget fit (v1.1) ---------------- */
  var BUD = 0;
  function budgetFit() {
    var b = Math.round(+$('#b-bud').value || 0), msg = $('#b-bud-msg');
    if (b < 1000) { msg.className = 'bud-m no'; msg.textContent = 'Enter your budget per adult in rupees, e.g. 20000.'; $('#b-bud').focus(); return; }
    BUD = b;
    var keepT = S.t, keepM = S.m, keepK = S.k, ag = MODE === 'agent' && S.g && S.g.k;
    var tiers = R.hotel.tiers.slice().reverse();
    /* v1.2: try the chosen car first; if the guest picked a bigger car than the group needs, also try 'Best for group' */
    function scan(k) {
      var best = null, low = null; S.k = k;
      tiers.forEach(function (t) { ['MAP', 'CP'].forEach(function (m) {
        S.t = t.id; S.m = m; var pl = compute(); if (!pl) return;
        var pp = ag ? pl.price.clientPP : pl.price.pp;
        if (!best && pp <= b) best = { t: t, m: m, k: k, pp: pp, cab: pl.cab };
        if (!low || pp < low.pp) low = { t: t, m: m, k: k, pp: pp, cab: pl.cab };
      }); });
      return { best: best, low: low };
    }
    var A = scan(keepK), B = keepK !== 'auto' ? scan('auto') : null;
    var best = A.best || (B && B.best), low = A.low;
    if (B && B.low && (!low || B.low.pp < low.pp)) low = B.low;
    var pick = best || low;
    if (!pick) { S.t = keepT; S.m = keepM; S.k = keepK; return; }
    S.t = pick.t.id; S.m = pick.m; S.k = pick.k;
    $('#b-meal').value = S.m; $('#b-veh').value = S.k;
    var tn = pick.t.name.split(' (')[0], mn = pick.m === 'MAP' ? 'breakfast + dinner' : 'breakfast only';
    var carTxt = pick.k !== keepK ? 'Car changed to ' + (pick.cab.cnt > 1 ? pick.cab.cnt + ' × ' : '') + pick.cab.v.name.split(' (')[0] + ' (right size for your group) to bring the price down.' : '';
    if (best) { msg.className = 'bud-m'; msg.textContent = 'Fits your budget: ' + tn + ' hotels, ' + mn + ' — about ' + inr(pick.pp) + ' per adult.'; }
    else { msg.className = 'bud-m no'; msg.textContent = 'Lowest estimate for this route is about ' + inr(pick.pp) + ' per adult (' + tn + ', ' + mn + '). Fewer nights, a shorter route or more people sharing the car brings it down — or ask us, the team often beats the estimate.'; }
    if (carTxt) { var cs = document.createElement('span'); cs.className = 'bud-car'; cs.textContent = carTxt; msg.appendChild(document.createTextNode(' ')); msg.appendChild(cs); }
    change(false);
  }

  var LAST = null;
  function renderAll(animate) {
    if (!S.p.length) {
      LAST = null; $('#mbar').hidden = true;
      if (!wsOpen) { $('#ws').hidden = true; return; }
      renderBuilder(); $('#rm').innerHTML = ''; $('#m-stat').innerHTML = ''; $('#warns').innerHTML = '';
      $('#m-title').textContent = 'Your trip'; $('#m-sub').textContent = 'Add places to see the route';
      $('#tl').innerHTML = '<p style="color:var(--mut);padding:10px 0">Add your first place on the left — or pick a ready idea above.</p>'; $('#price').innerHTML = '';
      return;
    }
    renderBuilder();
    var plan = compute(); LAST = plan;
    renderTimeline(plan); renderPrice(plan); renderMap(plan, animate);
    $('#mbar .btn').hidden = !!S.cv;
  }
  var rt = 0;
  function change(anim) { clearTimeout(rt); rt = setTimeout(function () { renderAll(anim); pushHash(); }, 30); }

  /* ---------------- builder events ---------------- */
  function wireBuilder() {
    $('#b-stops').addEventListener('click', function (e) {
      var b = e.target.closest('button[data-a]'); if (!b) return;
      var li = b.closest('li[data-i]'), i = +li.dataset.i, st = S.p[i];
      if (b.dataset.a === 'up') st.n = clamp(st.n + 1, 0, 9);
      if (b.dataset.a === 'dn') { st.n = clamp(st.n - 1, 0, 9); if (st.n === 0 && S.p.filter(function (x) { return x.n > 0; }).length === 0) { st.n = 1; toast('Keep at least one night'); } }
      if (b.dataset.a === 'mu' && i > 0) { S.p.splice(i - 1, 0, S.p.splice(i, 1)[0]); }
      if (b.dataset.a === 'rm') { S.p.splice(i, 1); }
      S.tp = '';
      if (!S.p.length) { renderAll(false); toast('Add a place to start again'); return; }
      change(b.dataset.a === 'mu' || b.dataset.a === 'rm');
    });
    $('#b-sugg').addEventListener('click', function (e) { var b = e.target.closest('[data-add]'); if (b) addStop(b.dataset.add); });
    wireSearch($('#b-add'), $('#b-dd'), function (it) {
      if (it.k === 'place') addStop(it.p.id); $('#b-add').value = '';
    }, 'all');
    $('#b-opt').addEventListener('click', function () { optimise(); toast('Stops re-ordered for the shortest drive'); change(true); });
    $('#b-clear').addEventListener('click', function () { S.p = []; S.tp = ''; renderAll(false); pushHash(); $('#b-add').focus(); });
    $('#b-start').addEventListener('change', function (e) { var same = S.e === S.s; S.s = e.target.value; if (same) S.e = S.s; change(true); });
    $('#b-end').addEventListener('change', function (e) { S.e = e.target.value; change(true); });
    $('#b-date').addEventListener('change', function (e) { if (e.target.value) { S.d = e.target.value; change(false); } });
    $$('.step').forEach(function (st) {
      st.addEventListener('click', function (e) {
        var b = e.target.closest('button'); if (!b) return; var plus = b === st.lastElementChild, k = st.dataset.k;
        if (k === 'ad') S.a = clamp(S.a + (plus ? 1 : -1), 1, 40);
        if (k === 'ch') S.c = clamp(S.c + (plus ? 1 : -1), 0, 20);
        if (k === 'inf') S.i = clamp(S.i + (plus ? 1 : -1), 0, 10);
        if (k === 'rooms') S.r = clamp(roomsCalc().rooms + (plus ? 1 : -1), 1, 20);
        change(false);
      });
    });
    $('#b-tiers').addEventListener('click', function (e) { var b = e.target.closest('[data-t]'); if (b) { S.t = b.dataset.t; change(false); } });
    $('#b-meal').addEventListener('change', function (e) { S.m = e.target.value; change(false); });
    $('#b-fit').addEventListener('click', budgetFit);
    $('#price').addEventListener('click', function (e) { var b = e.target.closest('[data-cmp]'); if (b) cmpAct(b.dataset.cmp); });
    $('#b-bud').addEventListener('input', function (e) { if (!e.target.value) { BUD = 0; $('#b-bud-msg').textContent = ''; } });
    $('#b-bud').addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); budgetFit(); } });
    $('#b-veh').addEventListener('change', function (e) { S.k = e.target.value; change(false); });
    $('#b-adds').addEventListener('click', function (e) { var b = e.target.closest('[data-x]'); if (!b) return; var i = S.x.indexOf(b.dataset.x); if (i > -1) S.x.splice(i, 1); else S.x.push(b.dataset.x); change(false); });
    ['ag-name', 'ag-phone', 'ag-email', 'ag-mk'].forEach(function (id) {
      $('#' + id).addEventListener('input', function () { S.g = S.g || {}; S.g.n = $('#ag-name').value.trim(); S.g.p = $('#ag-phone').value.trim(); S.g.e = $('#ag-email').value.trim(); S.g.k = clamp(+$('#ag-mk').value || 0, 0, 60); clearTimeout(rt); rt = setTimeout(function () { var plan = compute(); LAST = plan; renderPrice(plan); pushHash(); }, 200); });
    });
    $('#m-play').addEventListener('click', play);
    $('#m-real').addEventListener('click', function () { leafToggle(!leafOn); });
    W.addEventListener('resize', function () { clearTimeout(W.__tpR); W.__tpR = setTimeout(function () { if (LAST) renderMap(LAST, false); }, 200); });
  }
  function addStop(id) {
    if (S.p.length >= 14) { toast('Max 14 stops — call us for longer tours'); return; }
    var p = PL[id]; S.p.push({ id: id, n: p.kind === 'temple' ? 1 : 2 }); S.tp = '';
    if (S.p.length === 1 && S.s === S.e && km(S.s, id) > 700) { S.s = nearestHub(id); S.e = S.s; toast('Pickup set to ' + PL[S.s].name + ' (nearest)'); }
    ev('trip_planner', { step: 'add', id: id });
    if ($('#ws').hidden) openWs(); else change(true);
  }
  function optimise() {
    /* nearest neighbour from start, then 2-opt; keeps stops' nights */
    var rest = S.p.slice(), order = [], cur = S.s;
    while (rest.length) { var bi = 0, bk = 1e9; rest.forEach(function (st, i) { var k = km(cur, st.id); if (k < bk) { bk = k; bi = i; } }); cur = rest[bi].id; order.push(rest.splice(bi, 1)[0]); }
    function len(o) { var c = S.s, t = 0; o.forEach(function (st) { t += km(c, st.id); c = st.id; }); return t + km(c, S.e); }
    var improved = true, guard = 0;
    while (improved && guard++ < 50) {
      improved = false;
      for (var i = 0; i < order.length - 1; i++) for (var j = i + 1; j < order.length; j++) {
        var n = order.slice(0, i).concat(order.slice(i, j + 1).reverse(), order.slice(j + 1));
        if (len(n) + 1 < len(order)) { order = n; improved = true; }
      }
    }
    S.p = order;
  }

  /* ---------------- hero search + tabs ---------------- */
  function selTab(t) { var tabs = $$('.tp-tabs [role=tab]'); tabs.forEach(function (x) { var on = x === t; x.setAttribute('aria-selected', on); x.tabIndex = on ? 0 : -1; $('#' + x.getAttribute('aria-controls')).hidden = !on; }); ev('trip_planner', { step: 'tab', tab: t.id }); }
  function wireHero() {
    placeOptions($('#q-from'), 'chandigarh', function (p) { return p.kind === 'hub' || ['srinagar', 'leh', 'haridwar', 'shimla', 'manali', 'dharamshala', 'kullu', 'agra', 'udaipur', 'jodhpur', 'nainital'].indexOf(p.id) > -1; });
    $('#q-date').value = S.d; $('#q-date').min = iso(today);
    var qd = function () { var d = parseD($('#q-date').value); $('#q-date-s').textContent = d ? WD[d.getDay()] + (isPeak(d) ? ' · peak season' : '') : ''; }; qd();
    $('#q-date').addEventListener('change', function (e) { if (e.target.value) S.d = e.target.value; qd(); });
    var pax = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20];
    $('#q-pax').innerHTML = pax.map(function (n) { return '<option value="' + n + '"' + (n === 2 ? ' selected' : '') + '>' + n + ' Adult' + (n > 1 ? 's' : '') + '</option>'; }).join('');
    $('#q-pax').addEventListener('change', function (e) { S.a = +e.target.value; S.r = 0; });
    $('#q-from').addEventListener('change', function (e) { var p = PL[e.target.value]; $('#q-from-s').textContent = p.tip || 'Pickup city'; });
    var chosen = null;
    wireSearch($('#q-to'), $('#q-dd'), function (it) { chosen = it; $('#q-to').value = it.k === 'tpl' ? it.t.name : it.p.name; $('#q-to-s').textContent = it.k === 'tpl' ? 'Ready idea · you can edit everything' : (REGLBL[it.p.region] || ''); go(); });
    function go() {
      S.d = $('#q-date').value || S.d; S.a = +$('#q-pax').value || 2;
      var from = $('#q-from').value;
      var it = chosen;
      if (!it) { var r = search($('#q-to').value); it = r[0]; }
      if (!it) { it = { k: 'tpl', t: TPL[0] }; }
      if (it.k === 'tpl') loadTpl(it.t, from); else { S.s = from; loadPlace(it.p, from); }
      chosen = null;
    }
    $('#q-go').addEventListener('click', go);
    var pop = ['shimla-manali', 'nau-devi', 'char-dham', 'kashmir-classic', 'golden-triangle', 'spiti-circuit', 'kumaon-kainchi', 'dharamshala-dalhousie', 'vaishno-devi', 'rajasthan-royal', 'ladakh-fly'];
    $('#q-quick').insertAdjacentHTML('beforeend', pop.map(function (id) { var t = TPL.filter(function (x) { return x.id === id; })[0]; return t ? '<button type="button" class="chip" data-tpl="' + id + '">' + esc(t.name.replace(' (summer)', '').replace(' (fly-in)', '')) + '</button>' : ''; }).join(''));
    D.addEventListener('click', function (e) {
      var b = e.target.closest('[data-tpl]'); if (b) { var t = TPL.filter(function (x) { return x.id === b.dataset.tpl; })[0]; if (t) loadTpl(t); return; }
      var a = e.target.closest('[data-act]'); if (a) action(a.dataset.act, e, a);
    });
    /* tabs */
    var tabs = $$('.tp-tabs [role=tab]');
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { selTab(t); });
      t.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { var n = tabs[(i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length]; selTab(n); n.focus(); } });
    });
    /* mode */
    $$('.tp-mode button').forEach(function (b) { b.addEventListener('click', function () { setMode(b.dataset.mode); }); });
  }
  function setMode(m) {
    if (S.cv && m !== 'agent') return;
    MODE = m; $$('.tp-mode button').forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.mode === m); });
    if (m === 'agent') { S.g = S.g || { n: '', p: '', e: '', k: R.b2b.default_markup_pct }; toast('Agent mode: add your agency & markup in the builder'); }
    else { S.g = null; S.cv = 0; }
    ev('trip_planner', { step: 'mode', mode: m });
    if (S.p.length) change(false); else renderTemplates();
  }

  /* ---------------- template cards ---------------- */
  var CAT = 'all';
  function tplEstimate(t) {
    var keep = JSON.stringify(S);
    S.s = t.start; S.e = t.end; S.p = t.stops.map(function (s) { return { id: s[0], n: s[1] }; }); S.a = 2; S.c = 0; S.i = 0; S.r = 0; S.t = 'deluxe'; S.k = 'auto'; S.m = 'MAP';
    if (t.months) { var d = parseD(S.d) || today; if (t.months.indexOf(d.getMonth() + 1) < 0) S.d = iso(new Date(d.getFullYear() + (t.months[0] < d.getMonth() + 1 ? 1 : 0), t.months[0] - 1, 15)); }
    var mm = MODE; MODE = 'guest'; var p = compute(); MODE = mm;
    var o = JSON.parse(keep); Object.keys(o).forEach(function (k) { S[k] = o[k]; });
    return p;
  }
  function tplCard(t) {
    var p = tplEstimate(t), n = t.stops.reduce(function (a, s) { return a + s[1]; }, 0);
    var rt = [t.start].concat(t.stops.map(function (s) { return s[0]; })).map(function (id) { return PL[id].name.split(' (')[0].split(' / ')[0]; }).filter(function (x, i, a) { return a.indexOf(x) === i; }).join(' → ');
    return '<button type="button" class="tpl" data-tpl="' + t.id + '"><span class="spark"></span><span class="k">' + esc((CATS.filter(function (c) { return c[0] === t.cat; })[0] || ['', ''])[1]) + ' · ' + (n + 1) + 'D/' + n + 'N</span><b>' + esc(t.name) + '</b><span class="dv" style="color:var(--mut);font-size:13px">' + esc(t.hi) + '</span><span class="rt">' + esc(rt) + '</span><span class="ft"><span>est. ' + (p ? inr(p.price.pp) : '—') + '<small style="color:var(--mut);font-weight:600"> /adult</small></span><span>Customise →</span></span></button>';
  }
  function renderTemplates() {
    $('#tpl-cats').innerHTML = CATS.map(function (c) { return '<button type="button" class="chip" data-cat="' + c[0] + '" aria-pressed="' + (CAT === c[0]) + '">' + c[1] + '</button>'; }).join('');
    $('#tpl-row').innerHTML = TPL.filter(function (t) { return CAT === 'all' || t.cat === CAT; }).map(tplCard).join('');
    $('#yatra-grid').innerHTML = TPL.filter(function (t) { return t.cat === 'mata' || t.cat === 'pilgrim'; }).map(tplCard).join('');
  }
  function wireTemplates() { $('#tpl-cats').addEventListener('click', function (e) { var b = e.target.closest('[data-cat]'); if (b) { CAT = b.dataset.cat; renderTemplates(); } }); }

  /* ---------------- cabs tab ---------------- */
  function wireCab() {
    placeOptions($('#c-from'), 'delhi'); placeOptions($('#c-to'), 'manali');
    $('#c-veh').innerHTML = R.cab.vehicles.map(function (v) { return '<option value="' + v.id + '">' + esc(v.name.split(' (')[0]) + ' · ' + v.seats + ' seats</option>'; }).join('');
    $('#c-go').addEventListener('click', function () {
      var a = $('#c-from').value, b = $('#c-to').value, v = veh($('#c-veh').value), type = $('#c-type').value;
      var res = $('#c-res'); res.hidden = false;
      if (a === b) { res.innerHTML = '<div><p>Pick two different places.</p></div>'; return; }
      var k = km(a, b), m = mins(a, b), fare, note;
      var uf = R.cab.local_union_factor[PL[b].region] || R.cab.local_union_factor[PL[a].region] || 1;
      if (type === 'one') {
        fare = Math.max(k * v.rate * 1.15, 2400 * v.rate / 12) * uf + (m > 540 ? v.allow : 0) + k * R.cab.toll_parking_per_km;
        note = 'One-way drop · ' + k + ' km · ' + hrs(m) + ' · driver, tolls & parking included (estimate)';
      } else {
        var days = Math.max(2, Math.ceil((2 * k) / 300) + 1);
        fare = Math.max(2 * k + 60 * (days - 2), R.cab.min_km_per_day * days) * v.rate * uf + (days - 1) * v.allow + 2 * k * R.cab.toll_parking_per_km;
        note = 'Round trip · ' + days + ' days · ' + (2 * k) + ' km + local · driver night charges, tolls & parking included (estimate)';
      }
      fare = r100(fare * 1.05);
      res.innerHTML = '<div><div class="v">' + inr(fare) + ' <small>' + esc(v.name.split(' (')[0]) + '</small></div><p>' + esc(note) + '. Final fare on WhatsApp in minutes. <a href="https://suzutravels.com/cabs/">All cab routes</a></p></div>' +
        '<div class="act"><button type="button" class="btn p" data-act="cablead">Book this cab</button><a class="btn w" target="_blank" rel="noopener" href="https://wa.me/' + WA + '?text=' + encodeURIComponent('Hi Suzu Travels, I need a ' + v.name + ' ' + (type === 'one' ? 'one-way' : 'round trip') + ' from ' + PL[a].name + ' to ' + PL[b].name + '. Estimate seen: ' + inr(fare) + ' (Trip Planner)') + '">WhatsApp</a></div>';
      CABQ = { a: a, b: b, v: v.name, type: type, fare: fare };
      ev('trip_planner', { step: 'cab_fare' });
    });
  }
  var CABQ = null, HOTQ = null;

  /* ---------------- hotels tab ---------------- */
  function wireHotel() {
    placeOptions($('#h-place'), 'manali', function (p) { return p.stay; });
    $('#h-in').value = S.d; $('#h-in').min = iso(today);
    $('#h-n').innerHTML = [1, 2, 3, 4, 5, 6, 7].map(function (n) { return '<option value="' + n + '"' + (n === 2 ? ' selected' : '') + '>' + n + ' night' + (n > 1 ? 's' : '') + '</option>'; }).join('');
    $('#h-rooms').innerHTML = [1, 2, 3, 4, 5, 6, 8, 10].map(function (n) { return '<option value="' + n + '">' + n + ' room' + (n > 1 ? 's' : '') + '</option>'; }).join('');
    $('#h-tier').innerHTML = R.hotel.tiers.map(function (t) { return '<option value="' + t.id + '"' + (t.id === 'deluxe' ? ' selected' : '') + '>' + esc(t.name) + '</option>'; }).join('');
    $('#h-go').addEventListener('click', function () {
      var p = PL[$('#h-place').value], n = +$('#h-n').value, rooms = +$('#h-rooms').value, t = tier($('#h-tier').value), d0 = parseD($('#h-in').value) || today;
      var tot = 0, pk = 0;
      for (var i = 0; i < n; i++) { var dd = addD(d0, i), f = t.f; if (p.cls === 'remote' && f > 1.8) f = 1.8; var peak = isPeak(dd); if (peak) pk++; tot += R.hotel.classes[p.cls].deluxe * f * (peak ? R.hotel.peak.f : 1) * rooms; }
      tot = r100(tot * 1.12);
      var res = $('#h-res'); res.hidden = false;
      res.innerHTML = '<div><div class="v">' + inr(tot) + ' <small>' + n + ' night' + (n > 1 ? 's' : '') + ' · ' + rooms + ' room' + (rooms > 1 ? 's' : '') + '</small></div><p>' + esc(t.name) + ' in ' + esc(p.name) + ', breakfast + dinner, taxes (estimate)' + (pk ? ' · peak-season rate' : '') + '. About ' + inr(r100(tot / n / rooms)) + ' per room-night. We send 2–3 hotel options with photos.</p></div>' +
        '<div class="act"><button type="button" class="btn p" data-act="hotlead">Get hotel options</button><button type="button" class="btn s" data-act="hotadd">+ Make it a trip</button></div>';
      HOTQ = { id: p.id, n: n, rooms: rooms, tier: t.id, total: tot, date: iso(d0) };
      ev('trip_planner', { step: 'hotel_price' });
    });
  }

  /* ---------------- actions: lead, pdf, share ---------------- */
  var PENDING = null;
  function action(act, e, el) {
    if (act === 'wa') { ev('trip_planner', { step: 'whatsapp' }); return; }
    if (act === 'hotadd' && HOTQ) { S.p = [{ id: HOTQ.id, n: HOTQ.n }]; S.d = HOTQ.date; S.t = HOTQ.tier; S.s = nearestHub(HOTQ.id); S.e = S.s; S.tp = ''; openWs(); return; }
    if (act === 'pdf' && S.cv) { doPdf(); return; }
    e && e.preventDefault();
    PENDING = act;
    if (LEAD && (act === 'pdf' || act === 'share')) { sendLead(LEAD, act); finish(act); return; }
    openModal(act);
  }
  function openModal(act) {
    var m = $('#mod'), t = { price: [MODE === 'agent' ? 'Get B2B rates & availability' : 'Get today\'s best price', 'Our team checks your dates and sends the best price on WhatsApp — usually within 30 minutes (10 AM – 9 PM).'], pdf: ['Download your itinerary', 'Free PDF with day plan, map and estimate. We may WhatsApp you a better price.'], share: ['Get your share link', 'Your plan lives in the link — nothing is stored. We may WhatsApp you a better price.'], cablead: ['Book this cab', 'We confirm the car and final fare on WhatsApp.'], hotlead: ['Get hotel options', 'We send 2–3 hotel options with photos and today\'s rate.'] }[act] || ['Your details', ''];
    $('#mod-t').textContent = t[0]; $('#mod-s').textContent = t[1];
    $('#lead-f').hidden = false; $('#mod-ok').hidden = true; $('#ld-er').hidden = true;
    $('#ld-ag-w').hidden = MODE !== 'agent'; if (MODE === 'agent' && S.g) $('#ld-ag').value = S.g.n || '';
    $('#ld-go').textContent = act === 'pdf' ? 'Download PDF' : act === 'share' ? 'Create link' : 'Send';
    if (LEAD) { $('#ld-name').value = LEAD.name || ''; $('#ld-ph').value = LEAD.phone || ''; $('#ld-em').value = LEAD.email || ''; }
    m.hidden = false; setTimeout(function () { $('#ld-name').focus(); }, 30);
    ev('trip_planner', { step: 'lead_open', act: act });
  }
  function closeModal() { $('#mod').hidden = true; }
  function wireModal() {
    $('#mod .x').addEventListener('click', closeModal);
    $('#mod').addEventListener('click', function (e) { if (e.target.id === 'mod') closeModal(); });
    D.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !$('#mod').hidden) closeModal(); });
    $('#lead-f').addEventListener('submit', function (e) {
      e.preventDefault();
      var nm = $('#ld-name').value.trim(), ph = $('#ld-ph').value.replace(/\D/g, ''), em = $('#ld-em').value.trim(), er = $('#ld-er');
      if (ph.length === 12 && ph.indexOf('91') === 0) ph = ph.slice(2);
      if (ph.length === 11 && ph[0] === '0') ph = ph.slice(1);
      if (nm.length < 2) { er.textContent = 'Please enter your name.'; er.hidden = false; return; }
      if (!/^[6-9]\d{9}$/.test(ph) && !(ph.length >= 8 && ph.length <= 15 && $('#ld-ph').value.trim()[0] === '+')) { er.textContent = 'Please enter a valid WhatsApp number (10 digits, or +country code).'; er.hidden = false; return; }
      if (em && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em)) { er.textContent = 'Please check the email, or leave it empty.'; er.hidden = false; return; }
      if ($('#ld-hp').value) { closeModal(); return; }
      LEAD = { name: nm, phone: ph, email: em, ag: MODE === 'agent' ? $('#ld-ag').value.trim() : '' };
      try { sessionStorage.setItem('suzuTpLead', JSON.stringify(LEAD)); } catch (x) {}
      var ref = sendLead(LEAD, PENDING);
      if (PENDING === 'pdf' || PENDING === 'share') { closeModal(); finish(PENDING); return; }
      $('#lead-f').hidden = true; var ok = $('#mod-ok'); ok.hidden = false;
      ok.innerHTML = '<p style="font-size:17px;font-weight:800;color:var(--f);margin:0 0 6px">Thank you, ' + esc(nm.split(' ')[0]) + '! 🙏</p><p style="margin:0 0 6px">Our team will WhatsApp you on <b>' + esc(ph) + '</b> with availability and the best price.</p><p class="ref">Ref ' + ref + (LIVE ? '' : ' · preview mode: not sent') + '</p><div style="display:grid;gap:8px;margin-top:12px"><a class="btn w" target="_blank" rel="noopener" href="' + waLink(LAST, ref) + '">Chat on WhatsApp now</a><button type="button" class="btn s" data-act="pdf">⬇ Download PDF too</button></div>';
    });
  }
  function finish(act) { if (act === 'pdf') doPdf(); else if (act === 'share') showShare(); }
  function shareUrl(cv) { return location.origin + location.pathname + '#t=' + encState(cv); }
  function showShare() {
    var url = shareUrl(MODE === 'agent'), m = $('#mod');
    $('#mod-t').textContent = MODE === 'agent' ? 'Client link ready' : 'Your link is ready';
    $('#mod-s').textContent = MODE === 'agent' ? 'Your client sees your agency name and client price only.' : 'Anyone with the link sees this exact plan.';
    $('#lead-f').hidden = true; var ok = $('#mod-ok'); ok.hidden = false;
    ok.innerHTML = '<div class="linkbox"><input id="sh-url" readonly value="' + esc(url) + '" aria-label="Share link"><button type="button" class="btn d" id="sh-copy" style="min-height:44px">Copy</button></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:8px"><a class="btn w" target="_blank" rel="noopener" href="https://wa.me/?text=' + encodeURIComponent((LAST ? LAST.title + ' — ' + LAST.totalDays + ' day itinerary: ' : 'My itinerary: ') + url) + '">WhatsApp</a>' + (navigator.share ? '<button type="button" class="btn s" id="sh-native">More…</button>' : '<a class="btn s" href="mailto:?subject=' + encodeURIComponent('Trip itinerary') + '&body=' + encodeURIComponent(url) + '">Email</a>') + '</div>';
    m.hidden = false;
    $('#sh-copy').addEventListener('click', function () { var i = $('#sh-url'); i.select(); try { (navigator.clipboard ? navigator.clipboard.writeText(url) : Promise.reject()).then(function () { toast('Link copied'); }, function () { D.execCommand('copy'); toast('Link copied'); }); } catch (e) { toast('Select and copy the link'); } });
    if ($('#sh-native')) $('#sh-native').addEventListener('click', function () { navigator.share({ title: 'Trip itinerary', url: url }).catch(function () {}); });
    ev('trip_planner', { step: 'share' });
  }
  function waLink(plan, ref) {
    var t = 'Hi Suzu Travels, I made this itinerary on your Trip Planner: ' + (plan ? plan.title + ' — ' + plan.totalDays + 'D/' + plan.nights + 'N, ' + paxText() + ', from ' + fmtLong(plan.days[0].date) + ', est. ' + inr(plan.price.total) : '') + (ref ? ' (Ref ' + ref + ')' : '') + '. Link: ' + shareUrl(false);
    return 'https://wa.me/' + WA + '?text=' + encodeURIComponent(t);
  }
  function itinText(plan) {
    if (!plan) return '';
    var L = [plan.title + ' — ' + plan.totalDays + 'D/' + plan.nights + 'N', 'Dates: ' + fmtLong(plan.days[0].date) + ' to ' + fmtLong(plan.days[plan.days.length - 1].date), 'Travellers: ' + paxText() + ' · rooms ' + plan.hotel.rooms.rooms, 'Hotel: ' + plan.hotel.tier.name + ' · meals ' + S.m + ' · car ' + plan.cab.v.name + (plan.cab.cnt > 1 ? ' x' + plan.cab.cnt : ''), 'Pickup ' + PL[S.s].name + ' → drop ' + PL[S.e].name];
    plan.days.forEach(function (d) { L.push('D' + d.no + ' ' + fmtD(d.date) + ': ' + dayTitle(d) + (d.km ? ' (' + d.km + ' km)' : '') + (d.stay ? ' · night ' + PL[d.stay].name : '')); });
    L.push('Estimate: ' + inr(plan.price.total) + ' (' + inr(plan.price.pp) + '/adult), range to ' + inr(plan.price.high));
    if (S.x.length) L.push('Add-ons wanted: ' + S.x.map(function (x) { return ADDONS.filter(function (a) { return a.id === x; })[0].n; }).join(', '));
    if (plan.warn.length) L.push('Warnings shown: ' + plan.warn.map(function (w) { return w.t; }).join(' | '));
    if (BUD) L.push('Guest budget: ' + inr(BUD) + ' per adult');
    if (CMP) { var ca = CMP.sum; L.push('Also compared (Plan A): ' + ca.title + ' ' + ca.dn + ', ' + ca.hotel + ', ' + ca.meal + ', ' + ca.car + ' — est. ' + inr(ca.total) + ' (' + inr(ca.pp) + '/adult)'); }
    if (W.__tpLang === 'hi') L.push('Guest language: Hindi (हिंदी) — reply in Hindi');
    if (MODE === 'agent' && S.g) L.push('AGENT: ' + (S.g.n || '') + ' · ' + (S.g.p || '') + ' · ' + (S.g.e || '') + ' · markup ' + S.g.k + '%');
    L.push('Link: ' + shareUrl(false));
    return L.join('\n');
  }
  function sendLead(ld, act) {
    var ref = 'TP-' + String(Date.now()).slice(-6), src = srcTag(), plan = LAST, dest, msg, tdate = '';
    if (act === 'cablead' && CABQ) { dest = 'CAB ' + PL[CABQ.a].name + ' → ' + PL[CABQ.b].name + ' · ' + CABQ.v + ' · ' + CABQ.type + ' · est ' + inr(CABQ.fare); msg = 'Trip Planner cab fare request\n' + dest; }
    else if (act === 'hotlead' && HOTQ) { dest = 'HOTEL ' + PL[HOTQ.id].name + ' · ' + HOTQ.n + 'N · ' + HOTQ.rooms + ' room · ' + tier(HOTQ.tier).name + ' · est ' + inr(HOTQ.total); msg = 'Trip Planner hotel request\n' + dest + '\nCheck-in ' + HOTQ.date; tdate = HOTQ.date; }
    else { dest = plan ? plan.title + ' · ' + plan.totalDays + 'D · ' + (S.a + S.c) + ' pax · est ' + inr(plan.price.total) : 'Trip'; msg = itinText(plan); tdate = S.d; }
    msg = 'Suzu Trip Planner v' + VER + ' · action: ' + act + (ld.email ? '\nEmail: ' + ld.email : '') + (ld.ag ? '\nAgency: ' + ld.ag : '') + '\n' + msg + '\nSource: ' + src + ' | Page: ' + location.pathname + ' | Ref: ' + ref;
    var tag = (MODE === 'agent' ? 'B2B AGENT 🧳 ' : '') + 'TRIP PLANNER 🗺️ ';
    if (LIVE) {
      try {
        var fd = new FormData();
        fd.append('action', 'suzu_submit_landing_form'); fd.append('name', ld.name); fd.append('contact', ld.phone); fd.append('email', ld.email || '');
        fd.append('destination', tag + dest + '  •  Source: ' + src + '  •  Ref: ' + ref);
        fd.append('travel_date', tdate); fd.append('message', msg.slice(0, 4000));
        if (!(navigator.sendBeacon && navigator.sendBeacon('/wp-admin/admin-ajax.php', fd))) fetch('/wp-admin/admin-ajax.php', { method: 'POST', body: fd, keepalive: true }).catch(function () {});
        if (typeof gtag === 'function') gtag('event', 'conversion', { 'send_to': 'AW-17212172485/SPBwCPbf_9saEMXRs49A' });
      } catch (e) {}
    } else { try { console.info('[Trip Planner preview] lead not sent', { name: ld.name, phone: ld.phone, destination: tag + dest, message: msg }); } catch (e) {} }
    ev('generate_lead', { method: 'trip_planner', act: act });
    W.__tpLastLead = { destination: tag + dest, message: msg, ref: ref };
    return ref;
  }

  /* ---------------- PDF (print) ---------------- */
  var TIPS = {
    himachal: ['Carry a warm layer even in summer — hill evenings are 10–15 °C cooler than the plains.', 'Hill roads: 30–40 km/h average; keep motion-sickness tablets handy for children.'],
    kashmir: ['Sightseeing in Gulmarg, Pahalgam and Sonamarg runs on local union taxis / ponies — included in the estimate, but keep small change.', 'Book the Gulmarg Gondola online a few days ahead in peak season.', 'Carry a valid photo ID; mobile prepaid SIMs from other states may not work in J&K (postpaid works).'],
    ladakh: ['Rest completely on day 1 in Leh (3,500 m): no sightseeing, lots of water, no alcohol. Consult your doctor about altitude medicine.', 'Inner Line Permits for Nubra, Pangong and Tso Moriri are arranged by us — carry 4 passport photos and ID copies.', 'Nights at Pangong / Tso Moriri drop below 0 °C even in summer; carry a down jacket.'],
    uttarakhand: ['Char Dham: online yatra registration is mandatory; carry the printout and a photo ID.', 'Kedarnath / Yamunotri treks start early morning; ponies, palki and helicopters are on request.', 'Hill roads can close briefly after rain in July–August — keep one buffer day if possible.'],
    pilgrim: ['Temples open early (5–6 AM) and close for 1–2 hours midday; plan darshan before 11 AM.', 'Navratri and weekends bring long queues — carry water, and leave leather items and cameras in the car.', 'Dress modestly; cover shoulders and knees at shrines.'],
    rajasthan: ['Forts and palaces open ~9 AM–5 PM; start early to beat the heat.', 'October to March is the comfortable season; summer afternoons cross 40 °C — carry a cap, sunscreen and 2 litres of water per person.', 'Monument tickets are cheaper online; Taj Mahal is closed on Fridays.'],
    up: ['Taj Mahal is closed on Fridays; sunrise entry has the shortest queues.', 'Mathura–Vrindavan temples close in the afternoon (approx. 12–4 PM); plan darshan morning and evening.'],
    punjab: ['Cover your head and remove shoes at gurudwaras; the langar is open to everyone.']
  };
  function regionTips(plan) {
    var out = [], seen = {};
    plan.route.forEach(function (id) { var r = PL[id].region; if (seen[r]) return; seen[r] = 1; (TIPS[r] || []).forEach(function (t) { if (out.indexOf(t) < 0) out.push(t); }); });
    var mo = plan.days[0].date.getMonth() + 1, hills = plan.route.some(function (id) { return HILL[PL[id].region]; });
    if (plan.route.some(function (id) { return PL[id].cls === 'remote' && PL[id].region === 'himachal'; })) out.push('ATMs are scarce in Spiti, Kinnaur and Lahaul — carry cash; mobile network is patchy beyond Kaza.');
    if (hills && (mo >= 11 || mo <= 2)) out.unshift('Winter trip: carry heavy woollens, gloves and waterproof shoes; snow can close high roads for a day — the driver will suggest alternatives.');
    if (hills && mo >= 7 && mo <= 8) out.unshift('Monsoon season: landslides can delay hill roads; keep plans flexible and start drives early.');
    return out.slice(0, 7);
  }
  function placeNotes(plan) {
    var out = [], seen = {};
    plan.route.forEach(function (id) { var p = PL[id]; if (seen[id] || !p.tip) return; seen[id] = 1; out.push([p.name.split(' (')[0], p.tip]); });
    return out;
  }
  function qrInto(el, text, cb) {
    var done = false, fin = function () { if (!done) { done = true; cb(); } };
    function draw() { try { el.innerHTML = ''; new W.QRCode(el, { text: text, width: 96, height: 96, correctLevel: W.QRCode.CorrectLevel.M }); } catch (e) {} fin(); }
    if (W.QRCode) { draw(); return; }
    var s = D.createElement('script'); s.src = 'https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js'; s.onload = draw; s.onerror = fin; D.head.appendChild(s);
    setTimeout(fin, 1800);
  }
  function doPdf() {
    var plan = LAST; if (!plan) return;
    if (EMBED && /iPhone|iPad|iPod/i.test(navigator.userAgent) && !Q.has('pdf')) {
      var u = location.origin + location.pathname + '?pdf=1#t=' + encState(!!S.cv);
      var wn = W.open(u, '_blank'); if (wn) { toast('Opening your itinerary in a new tab…'); return; }
    }
    var cv = S.cv && S.g, ag = MODE === 'agent' && S.g && S.g.n ? S.g : null;
    var svg = $('#rm').cloneNode(true); svg.removeAttribute('id');
    $$('#rm-car,#rm-glow', svg).forEach(function (x) { x.remove(); });
    var rtp = svg.querySelector('.route'); if (rtp) { rtp.removeAttribute('style'); rtp.removeAttribute('id'); }
    var who = ag ? '<b>' + esc(ag.n) + '</b><small>' + esc([ag.p, ag.e].filter(Boolean).join(' · ')) + '</small>' : '<b>Suzu Travels</b><small>DMC of India · +91 70874 88961 · info@suzutravels.com · HP Tourism Reg. No. DTO-MND-11-243/2022</small>';
    var price = cv || ag ? (plan.price.client || plan.price.total) : plan.price.total, pp = cv || ag ? (plan.price.clientPP || plan.price.pp) : plan.price.pp;
    var h = '<div class="dh"><div>' + who + '</div><div style="text-align:right"><small>Itinerary · ' + fmtLong(today) + '</small><small>Ref ' + (W.__tpLastLead ? W.__tpLastLead.ref : '—') + '</small></div></div>' +
      '<h2>' + esc(plan.title) + ' — ' + plan.totalDays + ' Days / ' + plan.nights + ' Nights</h2><p class="tag">Your personalised itinerary · आपकी अपनी यात्रा योजना' + (plan.route.some(function (id) { return HILL[PL[id].region]; }) ? ' · Hill roads, realistic drive times' : '') + '</p>' +
      '<div class="sum"><span><b>Dates:</b> ' + fmtLong(plan.days[0].date) + ' – ' + fmtLong(plan.days[plan.days.length - 1].date) + '</span><span><b>Travellers:</b> ' + esc(paxText()) + '</span><span><b>Pickup:</b> ' + esc(PL[S.s].name) + '</span><span><b>Drop:</b> ' + esc(PL[S.e].name) + '</span><span><b>Car:</b> ' + esc(plan.cab.v.name) + (plan.cab.cnt > 1 ? ' × ' + plan.cab.cnt : '') + '</span><span><b>Hotels:</b> ' + esc(plan.hotel.tier.name) + ', ' + (S.m === 'MAP' ? 'breakfast + dinner' : 'breakfast') + '</span><span><b>Road distance:</b> ~' + plan.kmDrive.toLocaleString('en-IN') + ' km</span></div>' +
      '<div class="mp">' + svg.outerHTML + '</div>' +
      '<h3>Day-by-day plan</h3><table><tr><th style="width:15%">Day</th><th>Plan</th><th style="width:20%">Night stay</th></tr>' +
      plan.days.map(function (d) { return '<tr><td><b>Day ' + d.no + '</b><br>' + fmtD(d.date) + (d.km ? '<br>' + d.km + ' km · ' + hrs(d.min) : '') + '</td><td><b>' + esc(dayTitle(d)) + '</b><ul>' + dayLines(d).map(function (l) { return '<li>' + esc(l) + '</li>'; }).join('') + '</ul></td><td>' + (d.stay ? esc(PL[d.stay].name) + '<br><small class="dv">' + esc(PL[d.stay].hi) + '</small>' : '—') + '</td></tr>'; }).join('') + '</table>' +
      (plan.warn.length ? '<div class="gk"><b>Please note</b><ul>' + plan.warn.map(function (w) { return '<li>' + esc(w.t) + '</li>'; }).join('') + '</ul></div>' : '') +
      '<h3>Hotels</h3><table><tr><th>Place</th><th>Nights</th><th>Category</th></tr>' + plan.hotel.rows.map(function (r) { return '<tr><td>' + esc(PL[r.id].name) + '</td><td>' + r.n + '</td><td>' + esc(plan.hotel.tier.name) + ' or similar</td></tr>'; }).join('') + '</table>' +
      '<h3>Route at a glance</h3><table><tr><th>Leg</th><th style="width:18%">Road</th><th style="width:18%">Drive</th></tr>' + plan.days.filter(function (d) { return d.km; }).map(function (d) { return '<tr><td>Day ' + d.no + ' · ' + esc(PL[d.from].name.split(' (')[0]) + ' → ' + esc(PL[d.to].name.split(' (')[0]) + (d.via.length ? ' <small>via ' + esc(d.via.map(function (v) { return PL[v.id].name.split(' (')[0]; }).join(', ')) + '</small>' : '') + '</td><td>' + d.km + ' km</td><td>' + hrs(d.min) + '</td></tr>'; }).join('') + '<tr><td><b>Total</b></td><td><b>~' + plan.kmDrive.toLocaleString('en-IN') + ' km</b></td><td></td></tr></table>' +
      '<div class="pr"><b>' + (cv || ag ? 'Package price: ' : 'Estimated price: ') + inr(pp) + ' per adult</b> · total ' + inr(price) + ' for ' + esc(paxText()) + '<br><small>' + (cv || ag ? 'Subject to hotel and car availability on your dates.' : 'Estimate from 2026 market rates (higher side). Final price after availability check — usually at or below this estimate.') + '</small></div>' +
      '<h3>Included</h3><ul><li>Private ' + esc(plan.cab.v.name) + ' with driver for all transfers and sightseeing as per the plan; fuel, tolls, parking and driver allowance</li><li>' + plan.nights + ' nights in ' + esc(plan.hotel.tier.name) + ' hotels (' + plan.hotel.rooms.rooms + ' room' + (plan.hotel.rooms.rooms > 1 ? 's' : '') + ')' + (S.m === 'MAP' ? ' with breakfast and dinner' : ' with breakfast') + '</li><li>All applicable taxes</li></ul>' +
      '<h3>Not included</h3><ul><li>Flights / trains, entry tickets, ropeway, gondola and helicopter tickets</li><li>Adventure activities, Rohtang and other permits, pony / palki, local union taxis where mandatory</li><li>Personal expenses, room heaters, anything not listed as included</li>' + (S.x.length ? '<li>Add-ons requested (price on request): ' + esc(S.x.map(function (x) { return ADDONS.filter(function (a) { return a.id === x; })[0].n; }).join(', ')) + '</li>' : '') + '</ul>' +
      (ag ? '' : '<h3>How to book</h3><ul><li>A small token advance confirms the booking and locks the rate; the balance is paid before the trip starts.</li><li>The advance is non-refundable; instead of cancelling, the travel date can be changed once, to a date within 6 months.</li><li>Pay online via Razorpay, or by bank transfer / UPI.</li></ul>') +
      (function () { var tips = regionTips(plan), notes = placeNotes(plan); return (tips.length ? '<h3>Good to know &amp; packing</h3><ul class="two">' + tips.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' : '') + (notes.length ? '<h3>Place notes</h3><ul class="two">' + notes.map(function (n) { return '<li><b>' + esc(n[0]) + ':</b> ' + esc(n[1]) + '</li>'; }).join('') + '</ul>' : ''); })() +
      '<h3>On the trip — useful numbers</h3><p class="nums">' + (ag ? esc(ag.n) + (ag.p ? ' · ' + esc(ag.p) : '') : 'Suzu Travels 24×7 trip desk · WhatsApp / call <b>+91 70874 88961</b>') + ' · Emergency <b>112</b> · Ambulance <b>108</b> · India Tourist Helpline <b>1800-11-1363</b>' + '</p>' +
      '<div class="ft"><div class="qr" id="doc-qr"></div><div>' + (ag ? 'Prepared by ' + esc(ag.n) + '. Ground arrangements by Suzu Travels (DMC).' : 'Suzu Travels · NH 103, Ghumarwin, Bilaspur, HP 174021 · WhatsApp +91 70874 88961 · suzutravels.com') + '<br>Your plan link (scan or open to edit): ' + esc(shareUrl(!!ag)) + '</div></div>';
    $('#doc').innerHTML = h;
    var t0 = D.title; D.title = (ag ? ag.n.replace(/[^\w]+/g, '-') : 'Suzu-Travels') + '-Itinerary-' + plan.title.replace(/[^\w]+/g, '-') + '-' + plan.totalDays + 'D';
    ev('trip_planner', { step: 'pdf' });
    qrInto($('#doc-qr'), shareUrl(!!ag), function () { setTimeout(function () { W.print(); setTimeout(function () { D.title = t0; }, 800); }, 80); });
  }

  /* ---------------- boot ---------------- */
  /* ---------------- embedded in the homepage (iframe overlay) ---------------- */
  var Q = new URLSearchParams(location.search), EMBED = Q.get('embed') === '1';
  function closeEmbed() { try { if (W.parent && W.parent !== W) { W.parent.postMessage({ type: 'tp-close' }, location.origin); return; } } catch (e) {} location.href = '/'; }
  function setupEmbed() {
    D.documentElement.classList.add('tp-embed');
    var top = $('.tp-top .in'), b = D.createElement('button');
    b.type = 'button'; b.className = 'tp-close'; b.setAttribute('aria-label', 'Close planner and go back to the homepage');
    b.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg><span>Home</span>';
    b.addEventListener('click', closeEmbed); top.insertBefore(b, top.firstChild);
    var lg = $('.tp-logo'); if (lg) { lg.removeAttribute('href'); lg.setAttribute('role', 'presentation'); }
    D.addEventListener('keydown', function (e) { if (e.key === 'Escape' && $('#mod').hidden) closeEmbed(); });
  }
  function applyParams() {
    if (/^\d{4}-\d\d-\d\d$/.test(Q.get('date') || '')) S.d = Q.get('date');
    if (+Q.get('ad') > 0) S.a = clamp(+Q.get('ad'), 1, 40);
    var from = PL[Q.get('from')] ? Q.get('from') : null, tab = Q.get('tab');
    if (Q.get('tpl')) { var t = TPL.filter(function (x) { return x.id === Q.get('tpl'); })[0]; if (t) { loadTpl(t, from); return true; } }
    if (Q.get('place') && PL[Q.get('place')]) { if (from) S.s = from; loadPlace(PL[Q.get('place')], from); return true; }
    if (tab === 'cab') {
      selTab($('#tab-cab'));
      if (PL[Q.get('cf')]) $('#c-from').value = Q.get('cf'); if (PL[Q.get('ct')]) $('#c-to').value = Q.get('ct');
      if (Q.get('ctype') === 'round') $('#c-type').value = 'round'; if (veh(Q.get('cv'))) $('#c-veh').value = Q.get('cv');
      if (Q.get('cf') && Q.get('ct')) $('#c-go').click();
      return true;
    }
    if (tab === 'hotel') {
      selTab($('#tab-hotel'));
      if (PL[Q.get('hp')]) $('#h-place').value = Q.get('hp'); if (/^\d{4}-\d\d-\d\d$/.test(Q.get('hin') || '')) $('#h-in').value = Q.get('hin');
      if (+Q.get('hn')) $('#h-n').value = String(clamp(+Q.get('hn'), 1, 7)); if (+Q.get('hr')) $('#h-rooms').value = Q.get('hr'); if (tier(Q.get('ht')).id === Q.get('ht')) $('#h-tier').value = Q.get('ht');
      if (Q.get('hp')) $('#h-go').click();
      return true;
    }
    if (tab === 'yatra') { selTab($('#tab-yatra')); return true; }
    return false;
  }
  function boot() {
    if (EMBED) setupEmbed();
    wireHero(); wireTemplates(); wireBuilder(); wireCab(); wireHotel(); wireModal();
    var fromLink = loadHash();
    if (!fromLink && (EMBED || Q.has('tpl') || Q.has('place') || Q.has('tab'))) { $('#q-date').value = S.d; applyParams(); }
    if (MODE === 'agent') setMode('agent');
    renderTemplates();
    if (S.cv) { var md = $('.tp-mode'); if (md) md.hidden = true; }
    if (fromLink) { openWs(); if (S.cv && S.g && S.g.n) toast('Itinerary prepared by ' + S.g.n); if (Q.get('pdf') === '1') setTimeout(function () { if (LAST) doPdf(); }, 1200); }
    W.SuzuTripPlanner = { state: S, compute: compute, geo: function () { return !!ROADS.geoLoaded; }, data: DATA, pushHash: function () { if (S.p.length) pushHash(); }, load: function (id) { var t = TPL.filter(function (x) { return x.id === id; })[0]; if (t) loadTpl(t); }, version: VER };
  }
  if (D.readyState === 'loading') D.addEventListener('DOMContentLoaded', boot); else boot();
  if (W.requestIdleCallback) W.requestIdleCallback(loadGeo, { timeout: 1500 }); else setTimeout(loadGeo, 300);
})();
