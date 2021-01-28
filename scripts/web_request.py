from requests_html import HTMLSession

url = "https://genshin.honeyhunterworld.com/db/char/beidou/"
session = HTMLSession()
r = session.get(url)
r.html.render()
f = open('beidou.html','w',encoding='utf-8')
f.write(r.html.html)
f.close()