from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"asdasd":"Welcome to genshin api."}

@app.get("/characters/{character_name}/details")
def get_character_details(character_name):
    file_path = f"characters/{character_name}/details.json"
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.loads(file.read()) 

@app.get("/characters/{character_name}/attack")
def get_character_atk(character_name):
    file_path = f"characters/{character_name}/atk.json"
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.loads(file.read()) 

@app.get("/characters/{character_name}/constellation")
def get_character_cons(character_name):
    file_path = f"characters/{character_name}/constellation.json"
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.loads(file.read()) 

@app.get("/characters/{character_name}/lv_ascension_material")
def get_character_lvasc(character_name):
    file_path = f"characters/{character_name}/lv_ascension.json"
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.loads(file.read())

@app.get("/characters/{character_name}/stats")
def get_character_stat(character_name):
    file_path = f"characters/{character_name}/stats.json"
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.loads(file.read()) 

@app.get("/characters/{character_name}/passive")
def get_character_passive(character_name):
    file_path = f"characters/{character_name}/passive.json"
    with open(file_path, 'r') as file:
        return json.loads(file.read()) 