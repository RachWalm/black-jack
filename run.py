# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

name = 'str'
credit = 200
bet = 1
player_cards = []
dealer_cards = []

def request_bet():
    print(f'Please place your bet as a whole number. It must be less than your credit which is {credit} units')

def validate_number(input):
    try:
        value = int(input)
        print(f'validate number has {input}')
    except ValueError:
        print('this is either not a number or not a whole number')

def place_bet():
    request_bet()
    validate_number()

def generate_cards():
    suits = ["spade", "diamond", "heart", "club"]
    values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 'Jack', 'Queen', 'King']
    cards = [{'suit': suit, 'value': value} for suit in suits for 
    value in values]
    return cards

def generate_deck():
    random_deck = random.sample(generate_cards(), 48)
    return random_deck

def main():
    print('Welcome to Black Jack')
    print(f'Your credit is {credit} units')
    place_bet()
    deck = generate_deck()
    print(deck)
  
main()