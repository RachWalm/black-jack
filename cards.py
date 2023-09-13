import random


def generate_cards():
    """
    Builds a deck of cards into a dictionary in a list. 
    Using list comprehension to go through nested for loops
    of suit and number outputting the dictionary to a list for
    each cards
    """
    suits = ["spade", "diamond", "heart", "club"]
    names = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 'Jack', 'Queen', 'King']
    cards = [{'suit': suit, 'name': name} for suit in suits for name in names]
    return cards


def generate_deck():
    """
    Randomises a deck of cards so that the last one can be taken
    as though after a shuffle. Returns the random deck
    """
    random_deck = random.sample(cards, 48)  # 48 cards in deck
    return random_deck


cards = generate_cards()
