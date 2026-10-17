'''diff_ops.py <slug> <dir-with-previous-build>  (Experience Enhancer, 17 Oct 2026)
Turns the difference between the previously published build (e.g. a copy of out/ made before editing the kit, or a
rebuild from the previous commit) and the current out/<slug>.min.html into a short list of unique find/replace pairs
for wp_replace_in_page (expected_count 1). Writes diff-<slug>.json next to this file and prints the op sizes.
Apply the ops in order; the final stored content_length must equal the byte size of out/<slug>.min.html.'''
import difflib, pathlib, json, re, sys
def diffs(old,new,ctx=60):
    tok=lambda s: re.findall(r'[^<;{}]+|[<;{}]', s)
    A,B=tok(old),tok(new)
    sm=difflib.SequenceMatcher(None,A,B,autojunk=False)
    ops=[o for o in sm.get_opcodes() if o[0]!='equal']
    # char offsets
    offA=[0];
    for t in A: offA.append(offA[-1]+len(t))
    offB=[0]
    for t in B: offB.append(offB[-1]+len(t))
    spans=[(offA[i1],offA[i2],offB[j1],offB[j2]) for _,i1,i2,j1,j2 in ops]
    merged=[]
    for i1,i2,j1,j2 in spans:
        if merged and i1-merged[-1][1]<ctx*2:
            merged[-1]=(merged[-1][0],i2,merged[-1][2],j2)
        else: merged.append((i1,i2,j1,j2))
    out=[]
    for i1,i2,j1,j2 in merged:
        c=ctx
        while True:
            lo=max(0,i1-c); hi=min(len(old),i2+c)
            seg=old[lo:hi]
            if old.count(seg)==1: break
            c+=60
            if c>3000: raise SystemExit('no unique ctx')
        out.append((old[lo:hi], new[j1-(i1-lo):j2+(hi-i2)]))
    return out
if __name__=='__main__':
    slug=sys.argv[1]; base=sys.argv[2]
    old=pathlib.Path(f'{base}/{slug}.min.html').read_text(); new=pathlib.Path(str(pathlib.Path(__file__).parent / 'out' / f'{slug}.min.html')).read_text()
    d=diffs(old,new)
    t=old
    for a,b in d:
        assert t.count(a)==1; t=t.replace(a,b)
    assert t==new
    json.dump(d,open(pathlib.Path(__file__).parent / f'diff-{slug}.json','w'),ensure_ascii=False)
    print(slug,len(old.encode()),len(new.encode()),'ops',len(d),[(len(a),len(b)) for a,b in d])
