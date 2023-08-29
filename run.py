# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from simple_term_menu import TerminalMenu
import emoji
import time

name = 'str'
credit = 200
bet = 1
deck = []
player_cards = []
player_total = 0
dealer_cards = []
dealer_total = 0
pay_type = 'undecided'

def request_bet():
    """
    The player is asked to provide an integer to place a bet with from their 
    credit. The number is validated to be an integer and checked to be within
    thier credit available. Then the bet value updated if valid
    """
    global bet
    print('Please place your bet as a whole number.')
    print(f'It must be less than your credit, which is {credit} units')
    print('For example, if you want to bet 50 units, type 50 and press enter')
    in_bet = input()
    if validate_number(in_bet) and check_credit(in_bet):
        bet = int(in_bet)
    else: 
        request_bet()

def validate_number(input):
    """
    Validate to check if the input was an integer, not a float / letter / 
    speical character etc.
    """
    try:
        value = int(input)
        print(f'you have bet {input} credits')
        return True
    except ValueError:
        print('this is either not a number or not a whole number')
        return False
        #request_bet()

def check_credit(suggest):
    """
    Checks that the integer put in is within the credit of the person 
    placing the bet
    """
    suggested = int(suggest)
    if suggested <= credit:
        print('This bet is within your credit')
        return True
    else:
        print(f'Your bet exceeds your credit of {credit}')
        return False
        #request_bet()

def subtract_credit(minus):
    """
    Subtracts the bet from the credit
    """
    global credit
    credit -= minus

def place_bet():
    """
    Brings all the functions required to place a bet and subtract it from
    credit together along with the text to inform the user
    """
    global credit
    request_bet()
    print(credit)
    subtract_credit(bet)
    print(f' end of place bet. bet: {bet} credit: {credit}')

def generate_cards():
    """
    Builds a deck of cards into a dictionary in a list.
    """
    suits = ["spade", "diamond", "heart", "club"]
    names = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 'Jack', 'Queen', 'King']
    cards = [{'suit': suit, 'name': name} for suit in suits for 
    name in names]
    return cards

def generate_deck():
    """
    Randomises a deck of cards so that the last one can be taken
    as though after a shuffle. Returns the random deck
    """
    random_deck = random.sample(generate_cards(), 48)
    return random_deck

def enough_cards():
    """
    Checks that there are enough cards left in the pack to continue dealing
    """
    global deck
    if len(deck) > 1:
        pass
    else:
        new_deck = generate_deck()
        deck.extend(new_deck)

def deal(stack, who):
    """
    Takes the last card from the deck that is being dealt from and places
    it either in the player or dealers list of cards
    """
    enough_cards()
    last_card = stack.pop()
    who.append(last_card)
    print(who)

def initial_deal(active_cards):
    """
    Carries out the function of the dealer initially dealing the cards
    to the table before the user has interaction with the cards
    """
    global dealer_cards
    global player_cards
    print('Dealing cards..........')
    print('players card')
    deal(active_cards, player_cards)
    print('dealers card')
    deal(active_cards, dealer_cards)
    print('players cards')
    deal(active_cards, player_cards)
    print('dealers cards')
    deal(active_cards, dealer_cards)

def ace(hands):
    print('ace')
    return 11

def change_court_to_num(string, hands):
    if string == 'Jack':
        num = 10
        print('jack')
    elif string == 'Queen':
        num = 10
        print('queen')
    elif string == 'King':
        num = 10
        print('King')
    elif string == 'Ace':
        num = ace(hands)
        print('Ace')
    else:
        num = int(string)
    return num

def calculate_total(hands):
    """
    Calculates the numerical value of the cards added together
    """
    # print(hands)
    individual = [hand['name'] for hand in hands]
    print(f'this is individual {individual}')
    total = 0
    for ind in individual:
        individuals = change_court_to_num(ind, hands)
        """if ind == 'Jack':
            individuals = 10
            print('jack')
        elif ind == 'Queen':
            individuals = 10
            print('queen')
        elif ind == 'King':
            individuals = 10
            print('King')
        elif ind == 'Ace':
            individuals = ace(hands)
            print('Ace')
        else:
            individuals = int(ind)"""
        total += individuals
    print(total)

def check_instant_end(total):
    """
    Checks if the hand totals 21 or over which would mean an instant payout
    or / and end of game
    """
    global pay_type
    if total == 21:
        pay_type = 'blackjack'
        print('blackjack in instant end')
    elif total > 21:
        pay_type = 'bust'
        print('bust in instant end')

def user_action():
    """
    Asks the user what action they wish to take now they have their cards.
    Do they want to hit or stick?
    """
    print('Please choose whether to Hit (get one more card) or  Stick (No more cards)')
    print('move up or down until you have selected what you want to do')
    print('then press enter')
    choices = ["[H] Hit", "[S] Stick"]
    terminal_menu = TerminalMenu(choices)
    chosen = terminal_menu.show()
    print(f'You have chosen {choices[chosen]}!')
    return chosen

def proceed(choice):
    """
    Carries out the action that the user has chosen to either hit or stick
    """
    global deck
    if choice == 0:
        print('hit')
        deal(deck, player_cards)
        player_time()
    elif choice == 1:
        print('stick')

def player_time():
    """
    performs the functions that are required during the players interaction
    with the cards
    """
    player_total = calculate_total(player_cards)
    check_instant_end(player_total)
    if pay_type == 'undecided':
        print('undecided')
        action = user_action()
        proceed(action)
    elif pay_type == 'blackjack':
        print('blackjack')
    elif pay_type == 'bust':
        print('bust')

def who_won():
    print('who won')
    if dealer_total > 21:
        print('dealer bust')
        pay_type = 'even'    
    elif dealer_total > player_total:
        print('dealer won')
        pay_type = 'no'
    elif dealer_total < player_total:
        print('player won')
        pay_type = 'even'
    elif dealer_total == player_total:
        pay_type = 'back'
    print(f'pay_type equals {pay_type}')
    pay_winnings()

def pay_winnings():
    global bet
    global credit
    global pay_type
    if pay_type == 'blackjack':
        pay = ((bet/2)*3)+bet
    elif pay_type == 'bust' or 'no':
        pay = 0
    elif pay_type == 'even':
        pay = 2 * bet
    elif pay_type == 'back':
        pay = bet
    print(f'pay is {pay}')
    credit += pay
    print(f'credit is now {credit}!!!')

def dealer_time():
    """
    Performs the actions required during the time the dealer is interacting 
    with the cards after the play has completed their turn
    """
    if pay_type == 'undecided':
        print('dealer time')
        dealer_total = calculate_total(dealer_cards)
        print(dealer_total)
        for num in range (2,17):
            if dealer_total <= 17:
                print('need to deal')
                deal(deck, dealer_cards)
                dealer_total = calculate_total(dealer_cards)
            elif dealer_total > 17 :
                break

def clear_for_round():
    """
    Clears variables that need to be empty at the beginning of a round, 
    so the game can continue a the end of a round
    """
    global pay_type
    global player_cards
    global player_total
    global dealer_cards
    global dealer_total
    pay_type = 'undecided'
    player_cards.clear()
    player_total = 0
    dealer_cards.clear()
    dealer_total = 0

def continue_playing():
    """
    Allows the user to decide if they want to continue playing at the end
    of the round with another round
    """
    print('Do you want to continue playing another round?')
    contnue = ["[Y] Yes", "[N] No"]
    terminal_menu = TerminalMenu(contnue)
    chosen = terminal_menu.show()
    print(f'You have chosen {contnue[chosen]}!')
    if chosen == 1:
        print('Thank you for playing')
        print(f'your final credit was {credit}')
    elif chosen == 0:
        clear_for_round()
        main()

def main():
    """
    Functions overall
    """
    global deck
    print('Welcome to Black Jack')
    print(f'Your credit is {credit} units')
    #place_bet()
    initial_deal(deck)
    calculate_total(player_cards)
    calculate_total(dealer_cards)
    """player_time()
    dealer_time()
    who_won()
    continue_playing()"""

main()