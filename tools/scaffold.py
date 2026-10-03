import sys,json,re
from pathlib import Path
u,n,k=sys.argv[1:4]; R=Path(__file__).parents[1]; fn=re.sub(r'[^a-zA-Z0-9_-]+','_',k)+'.js'; c=re.sub(r'[^A-Za-z0-9]','',n.title()) or 'GeneratedSource'
(R/fn).write_text(f'class {c} extends ComicSource {{ name="{n}"; key="{k}"; version="0.1.0"; minAppVersion="1.6.0"; url="https://raw.githubusercontent.com/YOUR_USER/YOUR_REPO/main/sources/{fn}"; baseUrl="{u}"; search={{load:async()=>{{throw "TODO"}}}}; comic={{load:async()=>{{throw "TODO"}}}}; chapter={{load:async()=>{{throw "TODO"}}}}; }} new {c}();\n')
a=json.loads((R/'index.json').read_text()); a.append({'name':n,'fileName':fn,'key':k,'version':'0.1.0'}); (R/'index.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)); print('generated',fn)
