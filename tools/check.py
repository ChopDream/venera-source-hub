import json,re,subprocess,sys
from pathlib import Path
R=Path(__file__).parents[1]
NODE=None
for cand in ('/opt/milkcode/node/bin/node','node','nodejs'):
    try:
        if subprocess.run([cand,'--version'],capture_output=True).returncode==0:
            NODE=cand; break
    except Exception: pass

def strip_js(t):
    """Remove comments and string/regex literals so delimiter counting is meaningful."""
    out=[];i=0;n=len(t)
    while i<n:
        c=t[i]
        if c=='/' and i+1<n and t[i+1]=='/':
            while i<n and t[i]!='\n': i+=1
        elif c=='/' and i+1<n and t[i+1]=='*':
            i+=2
            while i+1<n and not (t[i]=='*' and t[i+1]=='/'): i+=1
            i+=2
        elif c in '"\'':
            q=c;i+=1
            while i<n and t[i]!=q:
                i+=2 if t[i]=='\\' else 1
            i+=1
        elif c=='`':
            depth=0;i+=1
            while i<n:
                if t[i]=='\\': i+=2; continue
                if t[i]=='`' and depth==0: i+=1; break
                if t[i]=='$' and i+1<n and t[i+1]=='{': depth+=1; i+=2; continue
                if depth>0 and t[i]=='}': depth-=1
                i+=1
        else:
            out.append(c); i+=1
    return ''.join(out)

a=json.loads((R/'index.json').read_text()); e=[]; keys={}
for x in a:
    p=R/x['fileName']
    if not p.exists():
        e.append('missing '+str(p)); continue
    t=p.read_text(errors='ignore')
    m={}
    for k in ('name','key','version'):
        mm=re.search(r'^\s*'+k+r'\s*=\s*["\']([^"\']*)["\']',t,re.M)
        m[k]=mm.group(1) if mm else None
        if m[k]!=x[k]: e.append(f"{p}: {k}={m[k]!r} != index {x[k]!r}")
    if x['key'] in keys: e.append(f"duplicate key: {x['key']}")
    keys[x['key']]=1
    first=None
    for line in t.replace('\r\n','\n').split('\n'):
        if line.strip().startswith('class '): first=line; break
    if first is None: e.append(f'{p}: no class declaration -> Venera "Invalid Content"')
    elif not first.startswith('class '): e.append(f'{p}: indented class line -> Venera "Invalid Content"')
    elif 'extends ComicSource' not in first: e.append(f'{p}: missing "extends ComicSource" -> Venera "Invalid Content"')
    if NODE:
        r=subprocess.run([NODE,'--check',str(p)],capture_output=True,text=True)
        if r.returncode!=0:
            e.append(f'{p}: JS syntax error -> {r.stderr.strip().splitlines()[:3]}')
    else:
        print('  warn: node not found, skipped JS syntax check')
    print('CHECK OK',p)
if e:
    print('\n'.join('ERROR '+x for x in e)); sys.exit(1)
print('PASS',len(a))
