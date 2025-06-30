import random
from ..transport import transport
from ...config import config
from ..persistence import repositories
from ..utilities import translator
from ..utilities import filters
from django.contrib.auth import get_user

# función que devuelve un listado de cards. Cada card representa una imagen de la API de Pokemon
def getAllImages():
    raw_pokemons = transport.getAllImages()
    cards = []

    for poke_data in raw_pokemons:
        alternative_names = poke_data.get('alternative_names', [])

        if alternative_names:
            chosen_name = random.choice(alternative_names)
            print(f"Se eligió el nombre alternativo '{chosen_name}' para {poke_data.get('name', 'pokemon')}")
            poke_data['name'] = chosen_name

        card = translator.fromRequestIntoCard(poke_data)
        cards.append(card)

    return cards

# función que filtra según el nombre del pokemon.
def filterByCharacter(name):
    return filters.filterCardsListByName(name, getAllImages())

# función que filtra las cards favoritas según el nombre del pokemon.
def filterFavoritesByCharacter(request, name):
    return filters.filterCardsListByName(name, getAllFavorites(request))

# función que filtra las cards según su tipo.
def filterByType(type_filter):
    filtered_cards = []

    type_filter = type_filter.lower()  # Convertir a minúsculas para comparación

    for card in getAllImages():
        if type_filter in [t.lower() for t in card.types]:
            filtered_cards.append(card)

    return filtered_cards

# función que filtra las cards en favoritas según su tipo.
def filterFavoritesByType(request, type_filter):
    filtered_cards = []

    type_filter = type_filter.lower()  # Convertir a minúsculas para comparación

    for card in getAllFavorites(request):
        if type_filter in [t.lower() for t in card.types]:
            filtered_cards.append(card)

    return filtered_cards

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = translator.fromTemplateIntoCard(request)  # esta función convierte el POST en una Card
    fav.user = get_user(request)
    return repositories.save_favourite(fav)

# usados desde el template 'favourites.html'
def getAllFavorites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)
        favourite_list = repositories.get_all_favourites(user)

        mapped_favourites = []
        for favourite in favourite_list:
            card = translator.fromRepositoryIntoCard(favourite)  # convertimos cada favorito en una Card
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.delete_favourite(favId)  # borramos un favorito por su ID

# obtenemos de TYPE_ID_MAP el id correspondiente a un tipo segun su nombre
def get_type_icon_url_by_name(type_name):
    type_id = config.TYPE_ID_MAP.get(type_name.lower())
    if not type_id:
        return None
    return transport.get_type_icon_url_by_id(type_id)