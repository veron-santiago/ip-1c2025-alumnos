# Filtra una lista de cartas por nombre
def filterCardsListByName(name, cardsList):
    filtered_cards = []

    for card in cardsList:
        if name.lower() in card.name.lower():
            filtered_cards.append(card)
    
    return filtered_cards