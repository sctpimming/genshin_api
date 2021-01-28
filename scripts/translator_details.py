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
        char_list.append(hero)
    return char_list

    
characters = get_characters()

for character_name in characters:
    
    print(f"Translates {character_name} ... ")
    with open(f"html_doc/{character_name}.html", 'r', encoding='utf-8') as file:
        doc = file.read()

    soup = BeautifulSoup(doc, "lxml")
    data = soup("table")

    ######## data[0]: Characters Detail ###############

    detail_dict = {}
    detail_table = data[0]
    elements = ["hydro", "pyro", "electro", "geo", "cryo", "anemo", "dendro"]

    for rows in detail_table("tr")[1:]: #skip image which is the first item
        item = rows("td")
        prop = str(item[0].contents[0]).lower()
        if prop == "weapon type":
            prop = "weapon"
            value = str(item[1].contents[0].contents[0])
        elif prop == "rarity":
            value = str(len(item[1]("div")))
        elif prop == "element":
            value_str = str(item[1].contents[0])
            for element in elements:
                if element in value_str:
                    value = element
        else:
            if(len (item[1].contents) == 0):
                value = "-"
            else:
                value = str(item[1].contents[0])
        
        detail_dict[prop] = value

    # Tweak dict keys for more intuitive api
    detail_dict["constellation"] = detail_dict.pop("astrolabe name")
    detail_dict["chinese_VA"] = detail_dict.pop("chinese seiyuu")
    detail_dict["japanese_VA"] = detail_dict.pop("japanese seiyuu") 
    detail_dict["english_VA"] = detail_dict.pop("english seiyuu") 
    detail_dict["korean_VA"] = detail_dict.pop("korean seiyuu") 
    detail_dict["description"] = detail_dict.pop("in-game description")

    outpath = f"api/characters/{character_name}/details.json"
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, 'w', encoding='utf-8') as file:
        json.dump(detail_dict, file, ensure_ascii=False)
    print(f"{character_name} details complete. ")


    