from bs4 import BeautifulSoup
import re
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
    with open(f"api/characters/{character_name}/atk.json", 'r') as file:
        skill = json.loads(file.read())
    skill_num = len(skill['atk'])

    ## data[3 + (skill_num*2) + 1] ##
    passive_table = data[3 + (skill_num*2) + 1]
    passive_dict = {}
    rows = passive_table("tr")
    
    for index in range(0, len(rows), 2):
        passive_name = " ".join((rows[index].text).split())
        passive_desc = " ".join((rows[index + 1].text).split())
        passive_dict[passive_name] = passive_desc

    with open(f"api/characters/{character_name}/passive.json", 'w', encoding="utf-8") as file:
        file.write(json.dumps(passive_dict))
    
    print(f"{character_name} passive data complete. ")

    