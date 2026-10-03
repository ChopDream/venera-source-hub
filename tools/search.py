import sys,json,re
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import quote,urlparse
u,k=sys.argv[1:3]; h=urlopen(Request(u,headers={'User-Agent':'venera-source-hub'}),timeout=20).read().decode('utf8','ignore'); s=u.rstrip('/')+'/search?keyword='+quote(k)
try: sh=urlopen(Request(s,headers={'User-Agent':'venera-source-hub'}),timeout=20).read().decode('utf8','ignore')
except Exception as e: sh=''; print('search fetch failed:',e)
out=Path(__file__).parents[1]/'evidence'/urlparse(u).netloc; out.mkdir(parents=True,exist_ok=True); (out/'home.html').write_text(h); (out/'search.html').write_text(sh)
r={'url':u,'keyword':k,'links':re.findall(r'<a[^>]+href=["\']([^"\']+)',sh,re.I)}; (out/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)); print(json.dumps(r,ensure_ascii=False,indent=2))
