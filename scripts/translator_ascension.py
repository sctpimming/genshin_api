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
# characters = ["Beidou"]

for character_name in characters:
    print(f"Translates {character_name} ... ")
    with open(f"html_doc/{character_name}.html", 'r', encoding='utf-8') as file:
        doc = file.read()

    soup = BeautifulSoup(doc, "lxml")
    data = soup("table")

    ######## data[2] Part 2: Ascension Material###############
    stat_table = data[2]
    material_list = []
    res = stat_table.find_all(rowspan = "2")
    for ascend in res:
        item_url_list = [item["href"] for item in ascend.find_all("a")]
        amount_list = [item.contents[0][2:] for item in ascend.find_all(class_ = "asc_amount")]
        item_list = [(url.split("/"))[5] for url in item_url_list]
        material_list.append(
            [{item_list[i]: amount_list[i]} for i in range(len(item_list))] 
        )
    material_dict = {"level_ascd" : material_list}
    outpath = f"api/characters/{character_name}/lv_ascension.json"
    with open(outpath, 'w', encoding='utf-8') as file:
        file.write(json.dumps(material_dict))   
    print(f"Translates {character_name} ascension material complete.")
