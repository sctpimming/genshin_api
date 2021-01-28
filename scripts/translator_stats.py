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

    output_dict = {}
    stat_dict = {}
    stat_table = data[2]

    props = ([prop.contents[0].lower() for prop in stat_table("tr")[0].find_all("td")])[1:-1]
    print(props)
    value_list = []
    for item in stat_table("tr")[1:]:
        row = ([prop.contents for prop in item.find_all("td")])
        if len(row) == len(props) + 2:
            row = row[:-1]
        print(row)
        lv = row[0][0]
        value_list = [value[0] for value in row[1:len(props)+1]]
        output_dict[lv] = value_list

    for key in output_dict:
        # Tweak dict keys for more intuitive api
        stat_dict[f"lv{key}"] = [{props[i] : output_dict[key][i]} for i in range(0, len(props))]

    outpath = f"api/characters/{character_name}/stats.json"
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, 'w', encoding='utf-8') as file:
        json.dump(stat_dict, file, ensure_ascii=False)
    print(f"{character_name} details complete. ")
