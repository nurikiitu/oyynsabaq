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
g=rep(g,"<div class=\"s\">8 ойын: көбейту мен бөлу</div>","<div class=\"s\">${window.KB_N||8} ойын: көбейту мен бөлу</div>",'games')
FILTER_G="""
/* платформа: орталыққа рұқсат етілген ойындар */
window.OS_filter=c=>{if(c.demo){const d=el('div','demo-note',`🎁 Демо-нұсқа: әр сыныпта 1–2 ойын. Толық нұсқада — 25-тен астам ойын! <a href="https://wa.me/77471091600" target="_blank">WhatsApp: 8 747 109 16 00</a>`);document.querySelector('.home-head').after(d)}
  const a=c.allow;if(!a)return;for(let i=GAMES.length-1;i>=0;i--){const g=GAMES[i];if(a[g.grade]&&!a[g.grade].includes(g.id))GAMES.splice(i,1)}
  if(a[3])window.KB_N=a[3].length;
  document.querySelectorAll('#grades .gradecard .gc').forEach((e,i)=>{const n=GRADES[i].n,k=n===3?(window.KB_N||8):GAMES.filter(g=>g.grade===n).length;e.textContent=k?k+' ойын':'жақында'});
  if(curGrade)openGrade(curGrade)};
"""
g=rep(g,"\n</script>\n</body>",FILTER_G+"</script>\n</body>",'games')
g=rep(g,"</style>\n</head>",".demo-note{max-width:1100px;margin:6px auto 0;background:#fff;color:#1a2a5a;border-radius:18px;padding:10px 18px;font-weight:900;font-size:clamp(15px,1.6vw,20px);text-align:center;box-shadow:0 5px 0 rgba(0,0,0,.15)}.demo-note a{color:#43a047;white-space:nowrap}</style>\n</head>",'games')
assert 'neuroUstaz' not in g,'games: neuroUstaz қалды'
open(os.path.join(root,'games.html'),'w',encoding='utf-8').write(g)
k=open(src_kb,encoding='utf-8').read()
k=rep(k,'<title>Көбейту әлемі · neuroUstaz</title>','<title>Көбейту әлемі</title>\n<script src="brand.js"></script>','kobeytu')
k=rep(k,'href="https://nurikiitu.github.io/neuroustaz-games/" style="text-decoration:none">⬅ neuroUstaz</a>','href="games.html" style="text-decoration:none">⬅ Басты бет</a>','kobeytu')
k=rep(k,'<div class="foot">neuroUstaz · ойнап үйренеміз!</div>','<div class="foot"><span data-brand-logo></span> <span data-brand-name></span> · <span data-brand-slogan></span></div>','kobeytu')
k=rep(k,"const c=el('button','card',","const c=el('button','card',",'kobeytu')
k=rep(k,"c.onclick=()=>{beep('tap');start(x)};cs.append(c)","c.dataset.id=x.id;c.onclick=()=>{beep('tap');start(x)};cs.append(c)",'kobeytu')
FILTER_K="""
window.OS_filter=c=>{const a=c.allow&&c.allow[3];if(!a)return;document.querySelectorAll('.card[data-id]').forEach(e=>{if(!a.includes(e.dataset.id))e.remove()});
  document.querySelectorAll('#groups .sec').forEach(s=>{if(!s.querySelector('.card'))s.remove()})};
"""
k=rep(k,"\n</script>\n</body>",FILTER_K+"</script>\n</body>",'kobeytu')
assert 'neuroUstaz' not in k,'kobeytu: neuroUstaz қалды'
open(os.path.join(root,'kobeytu.html'),'w',encoding='utf-8').write(k)
print('games.html, kobeytu.html дайын')
