#!/usr/bin/env python3
"""Ойын сайттарынан платформа беттерін жинау.
Қолдану: python3 tools/build.py ../neuroustaz-games/index.html ../kobeytu-alemi/index.html
"""
import sys,os
src_games,src_kb=sys.argv[1],sys.argv[2]
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rep(s,a,b,name):
    assert s.count(a)==1,f'{name}: табылмады → {a[:60]}'
    return s.replace(a,b)
BG='<style>body{background:linear-gradient(160deg,var(--b1,#29a3f5),var(--b2,#1565c0))}@media(max-width:700px){.home-head{padding-top:62px}}</style>'
g=open(src_games,encoding='utf-8').read()
g=rep(g,'<title>neuroUstaz · Ойындар</title>','<title>Ойындар</title>\n<script src="brand.js"></script>','games')
g=rep(g,'</head>',BG+'\n</head>','games')
g=rep(g,'<h1>🧠 neuroUstaz</h1>','<h1><span data-brand-logo></span> <span data-brand-name></span></h1>','games')
g=rep(g,'<p>Ойнап үйренеміз!</p>','<p data-brand-slogan></p>\n    <button class="tbtn" style="position:absolute;left:24px;top:24px" onclick="OS.logout()">🚪 Шығу</button>','games')
g=rep(g,"c.href='https://nurikiitu.github.io/kobeytu-alemi/'","c.href='kobeytu.html'",'games')
assert 'neuroUstaz' not in g,'games: neuroUstaz қалды'
open(os.path.join(root,'games.html'),'w',encoding='utf-8').write(g)
k=open(src_kb,encoding='utf-8').read()
k=rep(k,'<title>Көбейту әлемі · neuroUstaz</title>','<title>Көбейту әлемі</title>\n<script src="brand.js"></script>','kobeytu')
k=rep(k,'href="https://nurikiitu.github.io/neuroustaz-games/" style="text-decoration:none">⬅ neuroUstaz</a>','href="games.html" style="text-decoration:none">⬅ Басты бет</a>','kobeytu')
k=rep(k,'<div class="foot">neuroUstaz · ойнап үйренеміз!</div>','<div class="foot"><span data-brand-logo></span> <span data-brand-name></span> · <span data-brand-slogan></span></div>','kobeytu')
assert 'neuroUstaz' not in k,'kobeytu: neuroUstaz қалды'
open(os.path.join(root,'kobeytu.html'),'w',encoding='utf-8').write(k)
print('games.html, kobeytu.html дайын')
