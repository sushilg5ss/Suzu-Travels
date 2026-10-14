#!/usr/bin/env python3
"""Homepage parity guard for suzutravels.com.
Usage: python3 parity.py BEFORE.html AFTER.html
Exit 0 = safe to deploy, 1 = blocked. Prints a report.
Rule: an enhancement may ADD things, but must never remove or change
links, headings, SEO head tags, JSON-LD, or any non-'nz' script/style block."""
import re, sys, json, hashlib, html

def load(p):
    return open(p, encoding='utf-8', errors='replace').read()

def links(s):
    return set(html.unescape(h).strip() for h in re.findall(r'<a\b[^>]*\bhref="([^"]*)"', s, re.I))

def headings(s):
    out = []
    for lvl, body in re.findall(r'<h([1-4])\b[^>]*>(.*?)</h\1>', s, re.I | re.S):
        t = re.sub(r'<[^>]+>', ' ', body)
        t = re.sub(r'\s+', ' ', html.unescape(t)).strip()
        out.append((lvl, t))
    return out

def head_tags(s):
    d = {}
    m = re.search(r'<title>(.*?)</title>', s, re.S | re.I); d['title'] = m and m.group(1).strip()
    for name in ['description', 'robots']:
        m = re.search(r'<meta\s+name="%s"\s+content="([^"]*)"' % name, s, re.I); d[name] = m and m.group(1)
    m = re.search(r'<link\s+rel="canonical"\s+href="([^"]*)"', s, re.I); d['canonical'] = m and m.group(1)
    d['og'] = sorted(re.findall(r'<meta\s+property="og:[^"]+"\s+content="[^"]*"', s, re.I))
    return d

def jsonld(s):
    return [hashlib.md5(re.sub(r'\s+', '', b).encode()).hexdigest()
            for b in re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', s, re.S | re.I)]

def legacy_blocks(s, tag):
    """script/style blocks NOT owned by the nature layer (ids starting nz / suzu-nature)."""
    out = []
    for attrs, body in re.findall(r'<%s\b([^>]*)>(.*?)</%s>' % (tag, tag), s, re.S | re.I):
        if re.search(r'id="(nz|suzu-nature)', attrs) or 'ld+json' in attrs:
            continue
        out.append(hashlib.md5((attrs + body).encode()).hexdigest())
    return out

def phones(s):
    return set(re.sub(r'\D', '', p)[-10:] for p in re.findall(r'(?:\+?91[\s-]?)?[6-9]\d{4}[\s-]?\d{5}', s))

def main(a, b):
    A, B = load(a), load(b)
    fails, notes = [], []
    miss = links(A) - links(B)
    if miss: fails.append('links removed: %d e.g. %s' % (len(miss), list(miss)[:5]))
    hb = headings(B); hset = set(hb)
    mh = [h for h in headings(A) if h not in hset]
    if mh: fails.append('headings removed/changed: %s' % mh[:5])
    if sum(1 for l, _ in hb if l == '1') != 1: fails.append('H1 count != 1')
    if head_tags(A) != head_tags(B): fails.append('title/meta/canonical/OG changed')
    ja, jb = jsonld(A), jsonld(B)
    if not set(ja) <= set(jb): fails.append('JSON-LD block changed/removed')
    for tag in ('script', 'style'):
        la, lb = legacy_blocks(A, tag), legacy_blocks(B, tag)
        if not set(la) <= set(lb): fails.append('legacy <%s> block changed/removed (%d missing)' % (tag, len(set(la) - set(lb))))
    newp = phones(B) - phones(A)
    if newp: fails.append('new phone numbers appeared: %s' % newp)
    for pat, why in [(r'line-through', 'strike-through price styling'), (r'seats? left|only \d+ left', 'fake scarcity text')]:
        if len(re.findall(pat, B, re.I)) > len(re.findall(pat, A, re.I)):
            fails.append('new %s' % why)
    if 'suzu_submit_landing_form' in A and 'suzu_submit_landing_form' not in B: fails.append('lead endpoint removed')
    for lab in ('AW-17212172485', 'SPBwCPbf_9saEMXRs49A', 'K5j-CJKugvUcEMXRs49A', 'WFnaCILDjfUcEMXRs49A'):
        if lab in A and lab not in B: fails.append('Google Ads tag/label removed: ' + lab)
    notes.append('size %d -> %d bytes' % (len(A.encode()), len(B.encode())))
    notes.append('links %d -> %d, headings %d -> %d, json-ld %d -> %d' % (len(links(A)), len(links(B)), len(headings(A)), len(hb), len(ja), len(jb)))
    print('PARITY', 'FAIL' if fails else 'PASS')
    for f in fails: print('  x', f)
    for n in notes: print('  -', n)
    return 1 if fails else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
