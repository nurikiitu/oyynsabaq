"""Бөлек беттегі ойындар (2-сынып): games.html тізіміне сілтеме-карточка ретінде қосылады.
build.py games.html-ды қайта жинағанда осы функцияны шақырады."""
EXTRA = """
/* бөлек беттегі ойындар: карточка басылғанда сол бетке өтеді */
GAMES.push(
 {id:'kuzsoz',grade:2,title:'Күзгі сөздер',icon:'🍂',bg:'#ffe0b2',sub:'М. Дулатұлы «Күз»: қаптап, сіркіреп, қурау, астық',href:'kuzgi-sozder.html'},
 {id:'gylym',grade:2,title:'Ғылым кілті',icon:'🗝️',bg:'#fff3c4',sub:'Абай «Ғылымға көңіл бөлсеңіз»: 10 ұяшық, 10 сұрақ',href:'gylym-kilti.html'});
"""
def rep(s, a, b):
    assert s.count(a) == 1, f'extra: табылмады → {a[:60]}'
    return s.replace(a, b)
def add_extra(g):
    if "id:'kuzsoz'" in g:
        return g
    g = rep(g, "\n/* home: сыныптар */", EXTRA + "\n/* home: сыныптар */")
    g = rep(g, "c.onclick=()=>{beep('tap');startGame(g)};grid.append(c)})}",
               "c.onclick=()=>{beep('tap');if(g.href)location.href=g.href;else startGame(g)};grid.append(c)})}")
    return g
if __name__ == '__main__':
    import os
    p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'games.html')
    s = open(p, encoding='utf-8').read()
    open(p, 'w', encoding='utf-8').write(add_extra(s))
    print('games.html: 2 ойын қосылды')
