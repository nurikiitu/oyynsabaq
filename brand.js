/* ОйынСабақ: кіру коды және орталық брендингі */
(function(){
const SALT='oyynsabaq:',KEY='os_session';
const me=document.currentScript,isLogin=me&&me.dataset.login==='1';
if(!isLogin)document.documentElement.style.visibility='hidden';
const sha=async s=>{const b=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(SALT+String(s).trim().toUpperCase()));return[...new Uint8Array(b)].map(x=>x.toString(16).padStart(2,'0')).join('')};
async function centers(){try{const r=await fetch('centers.json?t='+Date.now(),{cache:'no-store'});if(!r.ok)throw 0;const j=await r.json();try{localStorage.setItem('os_centers',JSON.stringify(j))}catch(e){}return j}
  catch(e){try{return JSON.parse(localStorage.getItem('os_centers'))||[]}catch(_){return[]}}}
const today=()=>new Date().toISOString().slice(0,10);
const valid=c=>!!c&&(!c.until||c.until>=today());
const logoHTML=l=>/^(https?:|\.?\/|logos\/)|\.(png|jpe?g|svg|webp)$/i.test(l||'')?`<img src="${l}" alt="" style="height:1em;width:auto;vertical-align:-.12em;border-radius:.15em">`:(l||'🎲');
function apply(c){const r=document.documentElement.style;r.setProperty('--b1',c.c1||'#29a3f5');r.setProperty('--b2',c.c2||'#1565c0');
  document.querySelectorAll('[data-brand-name]').forEach(e=>e.textContent=c.name);
  document.querySelectorAll('[data-brand-slogan]').forEach(e=>e.textContent=c.slogan||'Ойнап үйренеміз!');
  document.querySelectorAll('[data-brand-logo]').forEach(e=>e.innerHTML=logoHTML(c.logo));
  document.title=document.title+' · '+c.name;
  if(c.demo){const d=document.createElement('div');d.textContent='ДЕМО';d.style.cssText='position:fixed;right:-46px;bottom:26px;rotate:-45deg;background:#ff4757;color:#fff;font:900 18px Nunito,sans-serif;padding:6px 60px;z-index:99;pointer-events:none;box-shadow:0 3px 8px rgba(0,0,0,.3)';document.body.append(d)}}
window.OS={sha,centers,valid,apply,logoHTML,
  async login(code){const h=await sha(code),list=await centers(),c=list.find(x=>x.hash===h);if(!c)return{err:'Код қате. Қайта тексеріңіз.'};if(!valid(c))return{err:'Қолжетімділік мерзімі аяқталған.'};try{localStorage.setItem(KEY,h)}catch(e){}return{c}},
  logout(){try{localStorage.removeItem(KEY)}catch(e){}location.href='index.html'},
  async current(){let h=null;try{h=localStorage.getItem(KEY)}catch(e){}if(!h)return null;const c=(await centers()).find(x=>x.hash===h);return valid(c)?c:null}};
if(!isLogin)window.OS.current().then(c=>{if(!c){location.replace('index.html?out=1');return}window.OS.center=c;
  const go=()=>{apply(c);try{window.OS_filter&&window.OS_filter(c)}catch(e){console.error(e)}document.documentElement.style.visibility=''};document.readyState==='loading'?document.addEventListener('DOMContentLoaded',go):go()});
})();
