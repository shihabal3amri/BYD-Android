"""Render all three static language pages from content and release.json."""
from pathlib import Path
import html,json
ROOT=Path(__file__).resolve().parents[1]
REPO='https://github.com/shihabal3amri/BYD-Android'
SITE='https://shihabal3amri.github.io/BYD-Android/'
ISSUES=REPO+'/issues/new?template=bug-report.yml'
def esc(v):return html.escape(str(v),quote=True)

def render_supporters(items, content, prefix):
    esc = lambda value: html.escape(str(value), quote=True)
    cards = []
    for item in items:
        cards.append(f'''<li><a class="supporter" href="{esc(item['url'])}" target="_blank" rel="noopener noreferrer">
<img class="supporter-logo" src="{prefix}{esc(item['logo'])}" width="{item['width']}" height="{item['height']}" alt="{esc(item['name'])}" loading="lazy">
<div class="supporter-info"><span class="supporter-label">{esc(content['supporter_label'])}</span><h3><bdi dir="ltr">{esc(item['name'])}</bdi></h3></div>
<span class="supporter-follow">{esc(content['supporter_follow'])}<span aria-hidden="true">↗</span></span>
</a></li>''')
    return f'''<section class="supporters" id="supporters" aria-labelledby="supporters-heading">
<h2 id="supporters-heading">{esc(content['supporters_heading'])}</h2>
<p>{esc(content['supporters_intro'])}</p>
<ul class="supporter-list">{''.join(cards)}</ul>
</section>'''

def main():
    release=json.loads((ROOT/'release.json').read_text(encoding='utf-8'))
    tag=release['tag'];download=REPO+'/releases/download/'+tag+'/'+release['file']
    release_url=REPO+'/releases/tag/'+tag
    languages=[('en','English',''),('ar','العربية','ar/'),('ru','Русский','ru/')]
    supporters=json.loads((ROOT/'supporters.json').read_text(encoding='utf-8'))
    notes=[]
    for lang,label,sub in languages:
        c=json.loads((ROOT/'content'/f'{lang}.json').read_text(encoding='utf-8'));prefix='../' if sub else ''
        nav='\n'.join(f'<a href="{prefix}{s or "./"}" lang="{l}" hreflang="{l}" dir="auto"'+(' aria-current="page"' if l==lang else '')+f'>{t}</a>' for l,t,s in languages)
        alternate='\n'.join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{s}">' for l,t,s in languages)
        gallery='\n'.join(f'<figure><a href="{prefix}assets/{f}"><img src="{prefix}assets/{f}" width="1080" height="2354" loading="lazy" alt="{esc(alt)}"></a><figcaption><strong>{esc(title)}</strong>{esc(body)}</figcaption></figure>' for f,alt,title,body in c['screens'])
        lis=lambda key:'\n'.join('<li>'+esc(v)+'</li>' for v in c[key])
        page=f'''<!doctype html>
<html lang="{lang}" dir="{c['dir']}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(c['title'])}</title><meta name="description" content="{esc(c['description'])}">
<meta name="theme-color" content="#e60012"><link rel="icon" href="{prefix}assets/icon.png">
<link rel="stylesheet" href="{prefix}assets/site.css"><link rel="canonical" href="{SITE}{sub}">
{alternate}<link rel="alternate" hreflang="x-default" href="{SITE}">
<meta property="og:type" content="website"><meta property="og:title" content="{esc(c['title'])}">
<meta property="og:description" content="{esc(c['description'])}"><meta property="og:url" content="{SITE}{sub}">
</head>
<body><main>
<header><div class="brand"><img src="{prefix}assets/icon.png" width="64" height="64" alt="BYD"><div><strong dir="ltr">BYD Android Localized</strong><p>{esc(c['community'])}</p></div></div>
<nav class="languages" aria-label="{esc(c['language'])}">{nav}</nav></header>
<span class="badge">{esc(c['badge'])} · <bdi>9.16.1 · v2.1</bdi></span>
<h1>{c['headline']}</h1><p class="intro">{esc(c['intro'])}</p>
<div class="actions"><a class="button" id="download" href="{download}">{esc(c['download'])} · <bdi>{round(release['bytes']/1000000)} MB</bdi></a><a class="button secondary" href="#install">{esc(c['installLink'])}</a></div>
<p class="note">{esc(c['free'])}</p><p class="note">{esc(c['updateNote'])}</p>
<section class="gallery" aria-labelledby="screenshots"><h2 id="screenshots">{esc(c['galleryTitle'])}</h2><p class="note">{esc(c['galleryNote'])}</p><div class="screens">{gallery}</div></section>
<section class="card" id="install" aria-labelledby="install-heading"><h2 id="install-heading">{esc(c['installTitle'])}</h2><ol>{lis('installSteps')}</ol><p>{esc(c['existing'])}</p><p class="note">{esc(c['original'])}</p></section>
<section class="card" id="walkup" aria-labelledby="walkup-heading"><h2 id="walkup-heading">{esc(c['setupTitle'])}</h2><ol>{lis('setupSteps')}</ol><p class="note">{esc(c['setupNote'])}</p></section>
<div class="grid"><section class="card" aria-labelledby="release-heading"><h2 id="release-heading">{esc(c['newTitle'])}</h2><ul>{lis('features')}</ul><a href="{release_url}">{esc(c['notes'])}</a></section>
<section class="card" aria-labelledby="feedback-heading"><h2 id="feedback-heading">{esc(c['compatTitle'])}</h2><p>{esc(c['compat'])}</p><p class="note">{esc(c['limitations'])}</p><p class="note">{esc(c['feedback'])}</p><a class="button secondary" href="{ISSUES}">{esc(c['report'])}</a></section></div>
{render_supporters(supporters, c, prefix)}
<footer><p><a href="{REPO}/blob/main/{c['readme']}">{esc(c['repository'])}</a> · <a href="{release_url}">{esc(c['notes'])}</a> · <a href="https://shihabal3amri.github.io/BYD-iOS/">{esc(c['ios'])}</a></p><p>{esc(c['footer'])}</p></footer>
</main></body></html>'''
        dest=ROOT/sub;dest.mkdir(parents=True,exist_ok=True);(dest/'index.html').write_text(page+'\n',encoding='utf-8',newline='\n')
        bullets=lambda key:'\n'.join('- '+v for v in c[key])
        steps=lambda key:'\n'.join(f'{i}. {v}' for i,v in enumerate(c[key],1))
        readme=f'''# BYD Android Localized

[English](README.md) · [العربية](README.ar.md) · [Русский](README.ru.md)

**{c['releaseTitle']}**

{c['notesIntro']}

[**{c['download']}**]({download}) · [{c['title']}]({SITE}{sub}) · [{c['report']}]({ISSUES})

## {c['newTitle']}

{bullets('features')}

## {c['galleryTitle']}

'''+ '\n'.join(f'<a href="assets/{f}"><img src="assets/{f}" alt="{esc(alt)}" width="190"></a>' for f,alt,title,body in c['screens'])+f'''

## {c['installTitle']}

{steps('installSteps')}

{c['existing']}

{c['original']}

## {c['setupTitle']}

{steps('setupSteps')}

{c['setupNote']}

## {c['compatTitle']}

{c['compat']}

{c['limitations']}

{c['feedback']}

## {c['checksum']}

[{c['notes']}]({release_url}) · [release.json](release.json)

`{release['file']}` · {release['bytes']:,} bytes

SHA-256: `{release['sha256']}`

## {c['maintainer']}

Update `release.json` and `content/*.json`, then run:

```sh
python scripts/build_site.py
python scripts/validate_site.py
```

APK downloads belong in GitHub Releases. This repository contains the download
page, screenshots, instructions and issue templates. It does not contain the
original BYD app source, signing keys, user logs or account data.

{c['footer']}
'''
        (ROOT/c['readme']).write_text(readme,encoding='utf-8',newline='\n')
        notes.append(f"## {label}\n\n{c['notesIntro']}\n\n{bullets('features')}\n\n{c['updateNote']}\n\n{c['original']}\n\n[{c['installLink']}]({SITE}{sub}#install) · [{c['report']}]({ISSUES})\n")
    (ROOT/'CHANGELOG.md').write_text(f"# {release['title']}\n\n"+'\n'.join(notes),encoding='utf-8',newline='\n')
    print('Rendered EN, AR, RU pages, READMEs and release notes')
if __name__=='__main__':main()
