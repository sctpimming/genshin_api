from bs4 import BeautifulSoup
from requests_html import HTMLSession
import time

def get_characters():
    with open("html_doc/main_raw.html", 'r', encoding="utf-8") as file:
        doc = file.read()
    soup = BeautifulSoup(doc, "lxml")
    res = soup(class_="sea_charname")
    return [char.contents[0] for char in res]

    
characters = get_characters()
session = HTMLSession()
for hero in characters:
    if hero == "Traveler (Anemo)":
        hero = "Traveler_Anemo"
    elif hero == "Traveler (Geo)":
        hero = "Traveler_Geo"
    print(f"scraping {hero}....")
    url = f"https://genshin.honeyhunterworld.com/db/char/{hero}/"
    r = session.get(url)
    r.html.render()
    with open(f"html_doc/{hero}_raw.html",'w',encoding='utf-8') as file:
        file.write(r.html.html)
    print(f"{hero} data complete.")
    time.sleep(2)
