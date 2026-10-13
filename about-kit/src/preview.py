# Wrap the built content in a copy of a live default-template page (theme header/footer/CSS) for screenshots
import re,sys
base=open(sys.argv[1]).read(); content=open(sys.argv[2]).read(); out=sys.argv[3]
s=base
s=re.sub(r'(<h1 class="entry-title"[^>]*>).*?(</h1>)', r'\1About Suzu Travels\2', s, count=1, flags=re.S)
i=s.find('<div class="entry-content"'); i=s.find('>',i)+1
j=s.find('</main>'); k=s.rfind('</div>',0,j); k=s.rfind('</div>',0,k)
s=s[:i]+content+s[k:]
s=s.replace('type="text/rocketlazyloadscript"','type="text/plain"')  # keep WP Rocket-delayed scripts inert, as on first paint
s=re.sub(r'<title>.*?</title>','<title>About Suzu Travels</title>',s,flags=re.S)
s=s.replace('<head>','<head><base href="file:///home/claude/about/">',1) if '--base' in sys.argv else s
open(out,'w').write(s)
