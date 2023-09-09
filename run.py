# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
import random
from time import sleep
from simple_term_menu import TerminalMenu
import emoji
from colorama import Fore, Back, Style

name = None
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
    print(f'{name}, your credit is {Fore.GREEN}{credit}{Fore.WHITE} units')


def title():
    """ASCII title so the user knows name of program"""
    print(f"""
    ╔╗ ┬  ┌─┐┌─┐┬┌─ ╦┌─┐┌─┐┬┌─
    ╠╩╗│  ├─┤│  ├┴┐ ║├─┤│  ├┴┐
    ╚═╝┴─┘┴ ┴└─┘┴ ┴╚╝┴ ┴└─┘┴ ┴""")


def goodbye():
    """ASCII writing to say goodbye to user"""
    print(f"""
    ╔═╗┌─┐┌─┐┌┬┐┌┐ ┬ ┬┌─┐
    ║ ╦│ ││ │ ││├┴┐└┬┘├┤
    ╚═╝└─┘└─┘─┴┘└─┘ ┴ └─┘""")
    quit()


def change_suit_to_uni(string):
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
    return image


def change_value_to_uni(string):
    """
    Makes values on the cards more readable with colours and
    symbols from the string value
    """
    if string == 'Queen':
        image = f'{Fore.CYAN}Queen{Fore.WHITE} \U0001F451 '
    elif string == 'King':
        image = f'{Fore.CYAN}King{Fore.WHITE} \U0001F451 '
    elif string == 'Jack':
        image = f'{Fore.CYAN}Jack{Fore.WHITE} \U0001F451 '
    elif string == 'Ace':
        image = f'{Fore.CYAN}Ace{Fore.WHITE}'
    else:
        image = f'{Fore.CYAN}{string}{Fore.WHITE}'
    return image


def print_cards(hand):
    """Prints a user readable version of the cards to the terminal
    """
    for sub in hand:
        suit = sub['suit']
        name = sub['name']
        suit_image = change_suit_to_uni(suit)
        name_image = change_value_to_uni(name)
        print(f'{name_image} {Fore.YELLOW}of{Fore.WHITE} {suit_image}')


def request_bet():
    """
    The player is asked to provide an integer to place a bet with from their
    credit. The number is validated to be an integer and checked to be within
    thier credit available. Then the bet value updated if valid
    """
    global bet
    print(f"""{name}, it is time to place your bet.......
Your bet must be less than your credit: {Fore.GREEN}{credit}{Fore.WHITE} units
If you wanted to bet {Fore.RED}50{Fore.WHITE} units,
you would type {Fore.RED}50{Fore.WHITE} and press enter
Please input your bet""")
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
        value = (int(input))
        if value > 0:
            return True
        else:
            print('The bet does not appear to be a positive number')
            return False
    except ValueError:
        print('The bet is either not a number or not a whole number')
        return False


def check_credit(suggest):
    """
    Checks that the integer put in is within the credit of the person
    placing the bet
    """
    suggested = int(suggest)
    if suggested <= credit:
        return True
    else:
        print(f"""Your bet -{Fore.RED}{suggested}{Fore.WHITE}
exceeds your credit : {Fore.GREEN}{credit}{Fore.WHITE}""")
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
    request_bet()
    subtract_credit(bet)


def generate_cards():
    """Builds a deck of cards into a dictionary in a list."""
    suits = ["spade", "diamond", "heart", "club"]
    names = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 'Jack', 'Queen', 'King']
    cards = [{'suit': suit, 'name': name} for suit in suits for name in names]
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
    Checks that there are enough cards left in the pack to
    continue dealing
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
    sleep(2)
    print("Your first card is:")
    deal(active_cards, player_cards)
    sleep(1)
    print('The dealers first card is:')
    deal(active_cards, dealer_cards)
    sleep(1)
    ingame_screen()
    print('Dealing cards..........')
    sleep(2)
    print("Your cards:")
    deal(active_cards, player_cards)
    sleep(1)
    print('The dealers cards:')
    deal(active_cards, dealer_cards)


def ace(total, aces):
    """
    Checks if there are aces - which can be 1 or 11.
    If there are aces if calculate what their values added
    together equals
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
    #elif aces == 0:
        #pass
    return value


def change_court_to_num(string):
    """Changes the string name of the card to an integer """
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
    """Calculates how much the cards in the hand adds up to"""
    individual = [hand['name'] for hand in hands]
    aces = 0
    total = 0
    for ind in individual:
        if ind == 'Ace':
            aces += 1
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


def double_down():
    global bet
    global credit
    global deck
    credit -= bet
    bet *= 2
    deal(deck, player_cards)
    dealer_time()


def instructions_query():
    """
    Asks the user if they want to read the instructions,
    or continue to play or quit
    """
    print(f"""{name}, please choose whether to
   {Fore.CYAN}Read instructions{Fore.WHITE}
or {Fore.CYAN}Play the game{Fore.WHITE}
or {Fore.CYAN}Quit{Fore.WHITE}
move up or down to select then press enter""")
    choices = ["Instructions", "Game", "Quit"]
    terminal_menu = TerminalMenu(choices)
    chosen = terminal_menu.show()
    print(f'You have chosen {choices[chosen]}!')
    if chosen == 0:
        instructions()
    elif chosen == 2:
        clear_terminal()
        print(f"""Thank you for playing
        Your final credit was {Fore.GREEN}{credit}{Fore.WHITE} units""")
        goodbye()


def player_action():
    """
    Asks the user what action they wish to take now they have their cards.
    Do they want to hit or stick or double down or quit?
    """
    print(f"""Please choose whether to
   {Fore.CYAN}Hit{Fore.WHITE} (get one more card)
or {Fore.CYAN}Stick{Fore.WHITE} (No more cards)
or {Fore.CYAN}Double down{Fore.WHITE} (get one more card and double bet)
or {Fore.CYAN}Quit round{Fore.WHITE} (loose bet and end round)
move up or down to select then press enter""")
    choices = ["Hit", "Stick", "Double down", "Quit round"]
    terminal_menu = TerminalMenu(choices)
    chosen = terminal_menu.show()
    print(f'You have chosen {choices[chosen]}!')
    return chosen


def progress_player_choice(choice):
    """
    Carries out the action that the user has chosen to either hit or stick
    """
    global deck
    if choice == 0:
        ingame_screen()
        deal(deck, player_cards)
        player_time()
    elif choice == 1:
        dealer_time()
    elif choice == 2:
        double_down()
    elif choice == 3:
        quit_round()


def quit_round():
    clear_for_round()
    continue_playing()


def ingame_screen():
    clear_terminal()
    print(f'{name} - Your bet is {Fore.RED}{bet}{Fore.WHITE}')


def player_time():
    """
    performs the functions that are required during the players interaction
    with the cards. If there is an instant winner/bust moves player to
    that route
    """
    global player_total
    player_total = calculate_total(player_cards)
    print(f'player total going into instant win {player_total}')
    check_instant_end(player_total)
    if pay_type == 'undecided':
        action = player_action()
        progress_player_choice(action)
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
    elif (dealer_total > player_total):  # and (dealer_total < 22):
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
    elif pay_type == 'bust':
        pay = 0
    elif pay_type == 'no':
        pay = 0
    elif pay_type == 'even':
        pay = 2 * bet
    elif pay_type == 'back':
        pay = bet
    return pay


def pay_winnings():
    """
    Puts winnings into the credit pot of the player
    """
    global credit
    pay = amount_winnings()
    decimal = credit + pay
    credit = int(decimal)
    print(f'credit is now {Fore.GREEN}{credit}{Fore.WHITE}!!!')
    continue_playing()


def dealer_time():
    """
    Performs the actions required during the time the dealer is interacting
    with the cards after the play has completed their turn
    """
    global dealer_total
    if pay_type == 'undecided':
        ingame_screen()
        dealer_total = calculate_total(dealer_cards)
        for num in range(2, 17):
            if dealer_total <= 17:
                deal(deck, dealer_cards)
                dealer_total = calculate_total(dealer_cards)
            elif dealer_total > 17:
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
            print(f"""Thank you for playing
Your final credit was {Fore.GREEN}{credit}{Fore.WHITE} units""")
            goodbye()
        elif chosen == 0:
            clear_for_round()
            main()
    else:
        clear_terminal()
        print('{name} thank you for playing')
        print('You are out of credit so we have to say GOODBYE!!!')
        goodbye()


def validate_name(in_name):
    """Checks that the input for the name is letters -  not spaces numbers
    or special characters"""
    try:
        if in_name.isalpha():
            return True
    except ValueError:
        return False


def request_name():
    """gets the users name"""
    global name
    if name is None:
        print('What is your name?')
        print('Type your name and press enter')
        in_name = input()
        strip = in_name.strip()
        cap_name = strip.capitalize()
        if validate_name(cap_name):
            name = (cap_name)
        else:
            print(f"""you entered {Fore.RED}{in_name}{Fore.WHITE}
This is not a name consisting of only of letters.
Please re-enter your name using letters only""")
            request_name()


def instructions():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Initially you enter your name using letters')
    sleep(1)
    print(f'Then you place a bet by typing a whole number')
    print('which is less than or equal to your credit.')
    sleep(2)
    print('The cards will then be dealt. Two each for you and the dealer')
    # - If you have two identical value cards you can then split.
    sleep(1)
    print('You can Hit - get one more card then decide again')
    print('Stick - stay where you are')
    print('double down - bet doubles and gives you only one more card.')
    sleep(3)
    print('Your cards are worth their face value if they are a number card.')
    print('Jack, Queen and King are worth 10 and Ace can be worth 1 or 11.')
    sleep(2)
    print('If you exceed 21 then you will lose.')
    print('If you get 21 there is an instant payout.')
    print('If you stick or doubled down then it is the dealers turn')
    sleep(3)
    print('You will get to see the dealers cards and any additional cards.')
    print('If the dealer gets higher than you without exceeding 21 he wins')
    print('if he exceeds 21 you get your money back')
    print('if at the end you have the higher value - you win.')
    print('21 gets a higher return than just beating the dealer.')
    sleep(2)
    input("Press Enter to continue:")
    clear_terminal()


def main():
    """The main run through of the program for an entire players hand"""
    global deck
    clear_terminal()
    request_name()
    clear_terminal()
    instructions_query()
    clear_terminal()
    place_bet()
    clear_terminal()
    initial_deal(deck)
    player_time()


main()
