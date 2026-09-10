"""Check public page links, locales, assets and APK metadata without dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set();self.lang=None;self.direction=None;self.downloads=[];self.images=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.lang=a.get('lang');self.direction=a.get('dir')
        if 'id' in a:
            assert a['id'] not in self.ids,'Duplicate id';self.ids.add(a['id'])
        if tag in ('a','link') and 'href' in a:self.links.append(a['href'])
        if tag=='a' and a.get('id')=='download':self.downloads.append(a['href'])
        if tag=='img':
            assert a.get('alt') and a.get('width') and a.get('height')
            self.links.append(a['src']);self.images+=1
def main():
    r=json.loads((ROOT/'release.json').read_text(encoding='utf-8'))
    assert r['status']=='public' and re.fullmatch('[0-9a-f]{64}',r['sha256'])
    expected='https://github.com/shihabal3amri/BYD-Android/releases/download/'+r['tag']+'/'+r['file']
    for sub,lang in [('', 'en'),('ar','ar'),('ru','ru')]:
        f=ROOT/sub/'index.html';s=f.read_text(encoding='utf-8');p=Page();p.feed(s)
        assert p.lang==lang and p.direction==('rtl' if lang=='ar' else 'ltr')
        assert p.downloads==[expected] and p.images==5
        assert not re.search(r'AltStore|Impactor|\.ipa|altstore:|Compatibility test build|PUBLIC BETA',s,re.I)
        for link in p.links:
            u=urlsplit(link)
            if u.scheme:assert u.scheme=='https';continue
            target=(f.parent/unquote(u.path)).resolve() if u.path else f
            if target.is_dir():target=target/'index.html'
            assert target.is_file(),(f,link)
            if u.fragment and target==f:assert u.fragment in p.ids,(f,link)
    assert not list(ROOT.glob('*.apk')),'APK must be a Release asset, not Git content'
    if len(sys.argv)>1:
        a=Path(sys.argv[1]);assert a.name==r['file'] and a.stat().st_size==r['bytes']
        assert hashlib.sha256(a.read_bytes()).hexdigest()==r['sha256']
    print('PASS: EN/AR/RU, RTL, download targets, local links, image metadata and release metadata')
if __name__=='__main__':main()
