from typing import Dict, List
import requests
from dotenv import dotenv_values
import json
import urllib.parse

config = dotenv_values()
app_id = config["EDAMAM_APP_ID"]
app_key = config["EDAMAM_APP_KEY"]

headers = {
    "Accept": "application/json"
}

def get_recipe(items: List) -> Dict:
    """
    Accepts a list of items.\n
    Returns JSON data in dict from Edamam API for recipes.
    """
    for i in range(5, 0, -1):
        items_tmp = items[:i]
        items_str = "&".join(items_tmp)
        url = f"https://api.edamam.com/api/recipes/v2?type=public&app_id={app_id}&app_key={app_key}&q={urllib.parse.quote_plus(items_str)}"
        res = requests.get(url)
        hits = json.loads(res.text)["hits"]
        if len(hits) > 1:
            break
    recipe_list = []
    for i in hits:
        recipe = i["recipe"]
        recipe_entry = {}
        recipe_entry["url"] = recipe["url"]
        recipe_entry["image"] = recipe["image"]
        recipe_entry["servings"] = recipe["yield"]
        recipe_entry["name"] = recipe["label"]
        recipe_entry["calories"] = str(round(float(recipe["calories"])))
        recipe_list.append(recipe_entry)
    return recipe_list

# print(get_recipe(["chicken"]))