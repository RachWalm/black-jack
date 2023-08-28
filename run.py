# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from simple_term_menu import TerminalMenu

name = 'str'
credit = 200
bet = 1
deck = []
player_cards = []
player_total = 0
dealer_cards = []
dealer_total = 0

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
    if suggested <= credit:
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

def deal(stack, who):
    last_card = stack.pop()
    who.append(last_card)
    print(who)

def initial_deal(active_cards):
    global dealer_cards
    global player_cards
    print('Dealing cards..........')
    print('players cards')
    deal(active_cards, player_cards)
    print('dealers cards')
    deal(active_cards, dealer_cards)
    print('players cards')
    deal(active_cards, player_cards)
    print('dealers cards')
    deal(active_cards, dealer_cards)

def ace():
    print('ace')
    return 11

def calculate_total(hands):
    print(hands)
    individual = [hand['name'] for hand in hands]
    print(f'this is individual {individual}')
    total = 0
    for ind in individual:
        try:
            individuals = int(ind)
            total += individuals
        except ValueError:
            if ind == 'Jack' or 'Queen' or 'King':
                print('court')
                individuals = 10
            elif ind == 'Ace':
                individuals = ace()
            total += individuals
    return total

def check_blackjack(total, who):
    if total == 21:
        pay_type = 'blackjack'
        print('blackjack')


def user_action():
    print('Please choose whether to Hit (get one more card) or  Stick (No more cards)')
    print('move up or down until you have selected what you want to do')
    print('then press enter')
    choices = ["[H] Hit", "[S] Stick"]
    terminal_menu = TerminalMenu(choices)
    chosen = terminal_menu.show()
    print(f'You have chosen {choices[chosen]}!')
    return chosen

def proceed(choice):
    global deck
    if choice == 0:
        print('hit')
        deal(deck, player_cards)
        player_time()
    elif choice == 1:
        print('stick')

def player_time():
    player_total = calculate_total(player_cards)
    check_blackjack(player_total, 'P')
    action = user_action()
    proceed(action)

def dealer_time():
    dealer_total = calculate_total(dealer_cards)
    print(dealer_total)
    for num in range (2,17):
        if dealer_total <= 17:
            print('need to deal')
            deal(deck, dealer_cards)
            dealer_total = calculate_total(dealer_cards)
        elif dealer_total > 17 :
            break
        
def continue_playing():
    print('Do you want to continue playing?')
    contnue = ["[Y] Yes", "[N] No"]
    terminal_menu = TerminalMenu(contnue)
    chosen = terminal_menu.show()
    print(f'You have chosen {contnue[chosen]}!')
    if chosen == 1:
        print('Thank you for playing')
        print(f'your final credit was {credit}')
    elif chosen == 0:
        #clear variables
        main()

def main():
    global deck
    print('Welcome to Black Jack')
    print(f'Your credit is {credit} units')
    # place_bet()
    deck = generate_deck()
    initial_deal(deck)
    player_time()
    dealer_time()
    continue_playing()

main()