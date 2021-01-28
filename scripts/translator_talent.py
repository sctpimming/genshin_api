from bs4 import BeautifulSoup
import os
import json

def get_characters():
    with open("html_doc/main_raw.html", 'r', encoding="utf-8") as file:
        doc = file.read()
    soup = BeautifulSoup(doc, "lxml")
    res = soup(class_="sea_charname")
    char_list = []
    for char in res:
        hero = char.contents[0]
        if hero == "Traveler (Anemo)":
            hero = "Traveler_Anemo"
        elif hero == "Traveler (Geo)":
            hero = "Traveler_Geo"
        char_list.append(hero.lower())
    return char_list

    
characters = get_characters()

for character_name in characters:
    print(f"Translates {character_name} ... ")
    with open(f"html_doc/{character_name}.html", 'r', encoding='utf-8') as file:
        doc = file.read()

    soup = BeautifulSoup(doc, "lxml")
    data = soup("table")

    ######## data[2]: Stat Progression ###############