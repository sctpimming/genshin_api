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
    skill_dmg_table = soup(class_ = "skilldmgwrapper")
    skill_num = len(skill_dmg_table)
    skill_name_list = []
    skill_table_list = []
    ######## data[3: 3+number_of_skill]: Attack talent ###############

    for index in range(3, 3+(skill_num*2), 2):
        skill_card = data[index]

        ## find skill name##
        skill_title = skill_card.find_all("td")[1].contents[0]
        skill_name = (skill_title["href"].split("/"))[5]
        skill_name_list.append(skill_name)
    
    for index in range(4, 3+(skill_num*2), 2):
        skill_dict = {}
        skill_table = data[index]
        table_rows = skill_table("tr")[1:]
        for row in table_rows:
            item_list = [item.text for item in row("td")]
            skill_dict[item_list[0]] = item_list[1:]
        skill_table_list.append(skill_dict)
    
    atk_list = [{skill_name_list[i]:skill_table_list[i]} for i in range(skill_num)]
    atk_dict = {"atk" : atk_list}

    outpath = f"api/characters/{character_name}/atk.json"
    with open(outpath, 'w', encoding='utf-8') as file:
        file.write(json.dumps(atk_dict))  
    print(f"{character_name} atk data complete. ")
    
 


    