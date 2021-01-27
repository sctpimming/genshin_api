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
        char_list.append(hero)
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
    cons_table = data[3 + (skill_num*2) + 1 + 1]
    cons_dict = {}
    rows = cons_table("tr")
    
    for index in range(0, len(rows), 2):
        cons_name = " ".join((rows[index].text).split())
        cons_desc = " ".join((rows[index + 1].text).split())
        cons_dict[cons_name] = cons_desc

    with open(f"api/characters/{character_name}/constellation.json", 'w', encoding="utf-8") as file:
        file.write(json.dumps(cons_dict))
    
    print(f"{character_name} constellation data complete. ")

    