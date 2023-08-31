# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
import random
from simple_term_menu import TerminalMenu
import emoji
import time
from colorama import Fore, Back, Style

name = 'str'
credit = 200
bet = 1
deck = []
player_cards = []
player_total = 0
dealer_cards = []
dealer_total = 0
pay_type = 'undecided'

def clear_terminal():
    """
    Clears terminal so that previous text isn't visible and put the title
    and credit on the screen in the same place
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    print(f'Your credit is {Fore.GREEN}{credit}{Fore.WHITE} units')

def title():
    """
    ASCII title so the user knows name of program
    """
    print('  ____  _            _       _            _    ____  _ ')
    print(' | __ )| | __ _  ___| | __  | | __ _  ___| | _|___ \/ |')
    print(' |  _ \| |/ _` |/ __| |/ /  | |/ _` |/ __| |/ / __) | |')
    print(" | |_) | | (_| | (__|   < |_| | (_| | (__|   < / __/| |")
    print(' |____/|_|\__,_|\___|_|\_\___/ \__,_|\___|_|\_\_____|_|')

def goodbye():
    """
    ASCII writing to say goodbye to user
    """
    print('   ____                 _ _                ')
    print(' / ___| ___   ___   __| | |__  _   _   ___')
    print('| |  _ / _ \ / _ \ / _  | |_ \| | | | | _ |')
    print('| |_| | (_) | (_) | (_| | |_) | |_| | | __/')
    print(' \____|\___/ \___/ \__,_|_.__/ \__, | \___|')
    print('                               |___/      ')

def change_str_to_uni(string):
    """
    Makes names and values on the cards more readable with colours and 
    symbols from the string value
    """
    if string == 'spade':
        image = '\u2660'
    elif string == 'heart':
        image = f'{Fore.RED}\u2665 {Fore.WHITE}'
    elif string == 'club':
        image = '\u2663'
    elif string == 'diamond':
        image = f'{Fore.RED}\u2666 {Fore.WHITE}'
    elif string == 'Queen':
        image = f'{Fore.CYAN}Queen {Fore.WHITE} \U0001F451 '
    elif string == 'King':
        image = f'{Fore.CYAN}King {Fore.WHITE} \U0001F451 '
    elif string == 'Jack':
        image = f'{Fore.CYAN}Jack {Fore.WHITE} \U0001F451 '
    elif string == 'Ace':
        image = f'{Fore.CYAN}Ace{Fore.WHITE}'
    else:
        image = f'{Fore.CYAN}{string}{Fore.WHITE}'
    return image
    
def print_cards(hand):
    """
    Prints a user readable version of the cards to the terminal
    """
    for sub in hand:
        suit = sub['suit']
        name = sub['name']
        suit_image = change_str_to_uni(suit)
        name_image = change_str_to_uni(name)
        print(f'{name_image} {Fore.YELLOW}of{Fore.WHITE} {suit_image}')

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
    symbol = who
    #print(symbol)
    print_cards(symbol)
    
def initial_deal(active_cards):
    """
    Carries out the function of the dealer initially dealing the cards
    to the table before the user has interaction with the cards
    """
    global dealer_cards
    global player_cards
    print(f'Your bet is {Fore.RED}{bet}{Fore.WHITE}')
    print('Dealing cards..........')
    print('The players first card is:')
    deal(active_cards, player_cards)
    print('The dealers first card is:')
    deal(active_cards, dealer_cards)
    print('The players cards:')
    deal(active_cards, player_cards)
    print('The dealers cards:')
    deal(active_cards, dealer_cards)

def ace(total, aces):
    """
    Calculates if there are aces what their values added together should be
    """
    value = 0
    if aces == 1:
        if total < 10:
            value = 11
        else:
            value = 1
    elif aces == 2:
        if total < 9:
            value = 12
        else:
            value = 2
    elif aces == 3:
        if total < 8:
            value = 13
        else:
            value = 3
    elif aces == 4:
        if total < 7:
            value = 14
        else:
            value = 4
    elif aces == 0:
        pass
    return value
    #print(value)

def change_court_to_num(string):
    """
    Changes the string name of the card to an integer 
    """
    if string == 'Jack':
        num = 10
    elif string == 'Queen':
        num = 10
    elif string == 'King':
        num = 10
    elif string == 'Ace':
        num = 0
    else:
        num = int(string)
    return num

def calculate_total(hands):
    """
    Calculates how much the cards in the hand adds up to
    """
    individual = [hand['name'] for hand in hands]
    aces = 0
    total = 0
    for ind in individual:
        if ind == 'Ace':
            aces +=1
            individuals = 0
        else:
            individuals = change_court_to_num(ind)
        total += individuals
        aced = 0 
        aced = ace(total, aces)
        aced_total = aced + total
        
    return aced_total

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
    print('Please choose whether to Hit (get one more card)')
    print('or Stick (No more cards)')
    print('move up or down to select then press enter')
    choices = ["Hit", "Stick"]
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
        clear_terminal()
        print(f'Your bet is {Fore.RED}{bet}{Fore.WHITE}')
        deal(deck, player_cards)
        player_time()
    elif choice == 1:
        #print('stick')
        dealer_time()

def player_time():
    """
    performs the functions that are required during the players interaction
    with the cards. If there is an instant winner/bust moves player to 
    that route
    """
    global player_total
    player_total = calculate_total(player_cards)
    check_instant_end(player_total)
    if pay_type == 'undecided':
        action = user_action()
        proceed(action)
    elif pay_type == 'blackjack':
        pay_winnings()
    elif pay_type == 'bust':
        pay_winnings()

def who_won():
    """
    Applies the rules of blackJack to determine who won after the dealer has
    decided what action to take
    """
    global player_total
    global dealer_total
    global pay_type
    if dealer_total > 21:
        print('dealer bust')
        pay_type = 'even'    
    elif (dealer_total > player_total): # and (dealer_total < 22):
        print('dealer won')
        pay_type = 'no'
    elif dealer_total < player_total:
        print('player won')
        pay_type = 'even'
    elif dealer_total == player_total:
        pay_type = 'back'
    print(f'pay_type equals {pay_type}')
    pay_winnings()

def amount_winnings():
    """
    Calculates what the winnings/if there are winnings depending on what 
    the outcome of the game was
    """
    global bet
    global pay_type
    print(pay_type)
    pay = 0
    if pay_type == 'blackjack':
        pay = ((bet/2)*3)+bet
        #print('blackjan')
    elif pay_type == 'bust': 
        pay = 0
        #print('no pay')
    elif pay_type == 'no':
        pay = 0
        #print('no pay')
    elif pay_type == 'even':
        pay = 2 * bet
        #print('even stephen')
    elif pay_type == 'back':
        pay = bet
        #print('backsies')
    #print('pay equals')
    #print(pay)
    return pay

def pay_winnings():
    """
    Puts winnings into the credit pot of the player
    """
    global credit
    pay = amount_winnings()
    decimal = credit + pay
    credit = int(decimal)
    print(f'credit is now {credit}!!!')
    continue_playing()

def dealer_time():
    """
    Performs the actions required during the time the dealer is interacting 
    with the cards after the play has completed their turn
    """
    global dealer_total
    if pay_type == 'undecided':
        clear_terminal()
        dealer_total = calculate_total(dealer_cards)
        for num in range (2,17):
            if dealer_total <= 17:
                deal(deck, dealer_cards)
                dealer_total = calculate_total(dealer_cards)
            elif dealer_total > 17 :
                break
        who_won()

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
    global credit
    if credit >= 1:
        print('Do you want to continue playing another round?')
        contnue = ["[Y] Yes", "[N] No"]
        terminal_menu = TerminalMenu(contnue)
        chosen = terminal_menu.show()
        print(f'You have chosen {contnue[chosen]}!')
        if chosen == 1:
            clear_terminal()
            print('Thank you for playing')
            print(f'Your final credit was {Fore.GREEN}{credit}{Fore.WHITE} units')
            goodbye()
        elif chosen == 0:
            clear_for_round()
            main()
    else:
        clear_terminal()
        print('Thank you for playing')
        print('You are out of credit so we have to say GOODBYE!!!')
        goodbye()

def main():
    """
    Functions overall
    """
    global deck
    clear_terminal()
    place_bet()
    clear_terminal()
    initial_deal(deck)
    player_time()
    
main()