import json,re,sys
from pathlib import Path
R=Path(__file__).parents[1]; a=json.loads((R/'index.json').read_text()); e=[]
for x in a:
 p=R/x['fileName']
 if not p.exists(): e.append('missing '+str(p)); continue
 t=p.read_text(errors='ignore')
 for k in ('name','key','version'):
  m=re.search(r'\b'+k+r'\s*=\s*["\']([^"\']*)',t)
  if not m or m.group(1)!=x[k]: e.append(f'{p}: {k} mismatch')
 if not re.search(r'class\s+\w+\s+extends\s+ComicSource',t): e.append(str(p)+': no ComicSource')
 if t.count('{')!=t.count('}'): e.append(str(p)+': braces')
 print('CHECK OK',p)
if e:
 print('\n'.join('ERROR '+x for x in e)); sys.exit(1)
print('PASS',len(a));
