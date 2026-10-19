// Dev helper: collect visible text nodes + placeholders/aria-labels across planner states (for the Hindi dictionary)
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await (await b.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
  await p.addInitScript(() => { navigator.sendBeacon = () => true; window.print = () => {}; });
  await p.route('**/admin-ajax.php', r => r.fulfill({ status: 200, body: '{}' }));
  await p.goto(process.argv[2], { waitUntil: 'load' });
  const S = new Set();
  const grab = async () => (await p.evaluate(() => { const o = []; const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n; while ((n = w.nextNode())) { if (/SCRIPT|STYLE/.test(n.parentNode.nodeName)) continue; const t = n.nodeValue.trim(); if (t && /[A-Za-z]/.test(t)) o.push(t); } document.querySelectorAll('[placeholder],[aria-label]').forEach(e => { ['placeholder', 'aria-label'].forEach(a => { if (e.getAttribute(a)) o.push('@' + a + ':' + e.getAttribute(a)); }); }); document.querySelectorAll('optgroup').forEach(g=>o.push('@label:'+g.label)); return o; })).forEach(x => S.add(x));
  await grab();
  for (const t of ['#tab-yatra', '#tab-cab', '#tab-hotel']) { await p.click(t); await grab(); }
  await p.click('#tab-cab'); await p.click('#c-go'); await p.waitForTimeout(300); await grab();
  await p.click('#tab-hotel'); await p.click('#h-go'); await p.waitForTimeout(300); await grab();
  for (const id of process.argv[3].split(',')) { await p.evaluate(x => SuzuTripPlanner.load(x), id); await p.waitForTimeout(500); await grab(); }
  await p.click('#price [data-act="price"]'); await p.waitForTimeout(200); await grab();
  await p.fill('#ld-name', 'TEST'); await p.fill('#ld-ph', '9876543210'); await p.click('#ld-go'); await p.waitForTimeout(300); await grab();
  await p.click('#mod .x'); await p.click('#price [data-act="pdf"]'); await p.waitForTimeout(2500); await grab();
  await p.click('#price [data-act="share"]'); await p.waitForTimeout(300); await grab();
  await p.click('#mod .x'); await p.click('[data-mode="agent"]'); await p.waitForTimeout(300); await grab();
  console.log(JSON.stringify([...S], null, 0));
  await b.close();
})();
