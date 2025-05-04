# translator: se refiere a un componente o conjunto de funciones que se utiliza para convertir o "mapear" datos de un formato o estructura a otro. Esta conversión se realiza típicamente cuando se trabaja con diferentes capas de una aplicación, como por ejemplo, entre la capa de datos y la capa de presentación, o entre dos modelos de datos diferentes.
import ast
from app.layers.utilities.card import Card

# Usado cuando la información viene de la API, para transformarla en una Card.
def fromRequestIntoCard(poke_data):
    card = Card(
        id=poke_data.get('id'),
        name=poke_data.get('name'),
        height=poke_data.get('height'),
        weight=poke_data.get('weight'),
        base=poke_data.get('base_experience'),
        image=safe_get(poke_data, 'sprites', 'other', 'official-artwork', 'front_default'),
        types=getTypes(poke_data)
    )
    return card

# recupera los tipos del JSON
def getTypes(poke_data):
    types = []
    for type in poke_data.get('types'):
        t = safe_get(type, 'type','name' )
        types.append(t)
    return types

# Usado cuando la información viene del template, para transformarla en una Card antes de guardarla en la base de datos.
def fromTemplateIntoCard(templ): 
    card = Card(
        name=templ.POST.get("name"),
        id=templ.POST.get("id"),
        height=templ.POST.get("height"),
        weight=templ.POST.get("weight"),
        types=templ.POST.get("types"),
        base=templ.POST.get("base"),
        image=templ.POST.get("image")
    )
    return card


# Cuando la información viene de la base de datos, para transformarla en una Card antes de mostrarla.
def fromRepositoryIntoCard(repo_dict):
    types_list = ast.literal_eval(repo_dict['types'])
    return Card(
        id=repo_dict.get('id'),
        name=repo_dict.get('name'),
        height=repo_dict.get('height'),
        weight=repo_dict.get('weight'),
        base=repo_dict.get('base_experience'),
        types=types_list,
        image=repo_dict.get('image')
    )

def safe_get(dic, *keys):
    for key in keys:
        if not isinstance(dic, dict):
            return None
        dic = dic.get(key, {})
    return dic if dic else None