import json,re,sys
from pathlib import Path
R=Path(__file__).parents[1]
a=json.loads((R/'index.json').read_text()); e=[]
keys={}
for x in a:
    p=R/x['fileName']
    if not p.exists():
        e.append('missing '+str(p)); continue
    t=p.read_text(errors='ignore')
    for k in ('name','key','version'):
        m=re.search(r'\b'+k+r'\s*=\s*["\']([^"\']*)',t)
        if not m or m.group(1)!=x[k]: e.append(f'{p}: {k} mismatch with index')
    if x['key'] in keys: e.append(f"duplicate key in index: {x['key']}")
    keys[x['key']]=1
    # Venera ComicSourceParser.parse rule: first line whose trim starts with "class "
    # must start at column 0 and contain "extends ComicSource", else "Invalid Content"
    first=None
    for line in t.replace('\r\n','\n').split('\n'):
        if line.strip().startswith('class '): first=line; break
    if first is None:
        e.append(f'{p}: no class declaration -> Venera: "Invalid Content"')
    elif not first.startswith('class '):
        e.append(f'{p}: first class line is indented -> Venera: "Invalid Content"')
    elif 'extends ComicSource' not in first:
        e.append(f'{p}: first class line lacks "extends ComicSource" -> Venera: "Invalid Content"')
    if t.count('{')!=t.count('}'): e.append(str(p)+': braces unbalanced')
    if t.count('(')!=t.count(')'): e.append(str(p)+': parens unbalanced')
    print('CHECK OK',p)
if e:
    print('\n'.join('ERROR '+x for x in e)); sys.exit(1)
print('PASS',len(a))
