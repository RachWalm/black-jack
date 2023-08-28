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
    print('Please place your bet as a whole number.')
    print(f'It must be less than your credit, which is {credit} units')
    print('For example, if you want to bet 50 units, type 50 and press enter')
    bet = input()
    # if input a letter then a number goes through whole thing again after with the letter
    validate_number(bet)
    check_credit(bet)
    return bet

def validate_number(input):
    try:
        value = int(input)
        print(f'you have bet {input} credits')
    except ValueError:
        print('this is either not a number or not a whole number')
        request_bet()

def check_credit(suggest):
    suggested = int(suggest)
    if suggested < credit:
        print('This bet is within your credit')
    else:
        print(f'Your bet exceeds your credit of {credit}')
        request_bet()

def subtract_credit(minus):
    global credit
    credit -= minus
    
    

def place_bet():
    global credit
    string_bet = request_bet()
    bet = int(string_bet)
    print(credit)
    subtract_credit(bet)
    print(f' end of place bet. bet: {bet} credit: {credit}')

def generate_cards():
    suits = ["spade", "diamond", "heart", "club"]
    names = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 'Jack', 'Queen', 'King']
    cards = [{'suit': suit, 'name': name} for suit in suits for 
    name in names]
    return cards

def generate_deck():
    random_deck = random.sample(generate_cards(), 48)
    return random_deck

def main():
    print('Welcome to Black Jack')
    print(f'Your credit is {credit} units')
    place_bet()
    deck = generate_deck()

main()