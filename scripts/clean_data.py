from bs4 import BeautifulSoup

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
    print(f"Cleaning {character_name} ... ")
    with open(f"html_doc/{character_name}_raw.html", 'r', encoding='utf-8') as file:
        doc = file.read()

    soup = BeautifulSoup(doc, 'lxml')

    filtered_data = soup(id="live_data")[0].contents
    with open(f"html_doc/{character_name}.html", 'w', encoding='utf-8') as file:
        for items in filtered_data:
            file.writelines(str(items))
    print(f"{character_name} data complete.")