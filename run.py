# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
from time import sleep
import numpy
from simple_term_menu import TerminalMenu
import emoji
from colorama import Fore
import ascii
import cards


class Hand:
    """Hand class"""
    def __init__(self, who, when, cards):
        #  instance attribute
        self.who = who
        self.cards = cards
        self.when = when


name = None
credit = 200
bet = 1
deck = []
player = Hand("player", "initial", [])
player_total = 0
dealer = Hand("dealer", "initial", [])
dealer_total = 0
pay_type = 'undecided'


def instructions():
    total_clear()
    print(f"""
Initially you enter your {Fore.CYAN}{Fore.WHITE}name using letters
""")
    sleep(1)
    print(f"""Then you place a {Fore.RED}bet{Fore.WHITE}, by typing
a whole number,which is less than or equal to
your {Fore.GREEN}credit{Fore.WHITE}.
""")
    sleep(2)
    print('The cards will then be dealt. Two each for you and the dealer')
    # - If you have two identical value cards you can then split.
    sleep(1)
    print(f"""You can {Fore.CYAN}Hit{Fore.WHITE} - get one more card,
then you decide again,
{Fore.CYAN}Stick{Fore.WHITE} - stay where you are
{Fore.CYAN}Double down{Fore.WHITE} - bet doubles
and gives you only one more card.
""")
    sleep(3)
    print(f"""Your cards are worth their face value if they are a number card.
{Fore.CYAN}Jack, Queen{Fore.WHITE} and {Fore.CYAN}King{Fore.WHITE}
are worth {Fore.CYAN}10{Fore.WHITE}
and {Fore.CYAN}Ace{Fore.WHITE} can be worth
{Fore.CYAN}1{Fore.WHITE} or {Fore.CYAN}11{Fore.WHITE}.
""")
    sleep(2)
    enter_to_continue()
    print(f"""
If you exceed {Fore.CYAN}21{Fore.WHITE} then you will lose.
If you get {Fore.CYAN}21{Fore.WHITE} there is an instant payout.
If you {Fore.CYAN}stick{Fore.WHITE} or {Fore.CYAN}double down{Fore.WHITE} then
it is the dealers turn
""")
    sleep(3)
    print(f"""You will now get to see all the dealers cards
and any additional cards he deals himself.

If the dealer gets higher than you without
exceeding {Fore.CYAN}21{Fore.WHITE} he wins

If he exceeds {Fore.CYAN}21{Fore.WHITE} you win

If at the end you have the higher value - you win.

{Fore.CYAN}21{Fore.WHITE} gets a higher return than just beating the dealer.
""")
    sleep(2)
    enter_to_continue()
    clear_terminal()
    instructions_query()


def enter_to_continue():
    while True:
        is_enter = input("Press Enter to continue...")
        if is_enter == "":
            break
        else:
            print("Please don't use other keys, just press Enter to continue.")
    total_clear()


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
    print(f"""You have chosen {choices[chosen]}!""")
    if chosen == 0:
        instructions()
    elif chosen == 2:
        clear_terminal()
        print(f"""Thank you for playing
        Your final credit was {Fore.GREEN}{credit}{Fore.WHITE} units""")
        ascii.goodbye()


def clear_terminal():
    """
    Clears terminal so that previous text isn't visible and put the title
    and credit on the screen in the same place
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii.title()
    print(f"""Your credit is {Fore.GREEN}{credit}{Fore.WHITE} units""")


def change_suit_to_uni(string):
    """
    Makes names and values on the cards more readable with colours and
    symbols from the string value
    """
    if string == 'spade':
        image = '\u2660'
    elif string == 'heart':
        image = f"""{Fore.RED}\u2665{Fore.WHITE}"""
    elif string == 'club':
        image = '\u2663'
    elif string == 'diamond':
        image = f"""{Fore.RED}\u2666{Fore.WHITE}"""
    return image


def change_value_to_uni(string):
    """
    Makes values on the cards more readable with colours and
    symbols from the string value
    """
    if string == 'Queen':
        image = f"""{Fore.CYAN}Queen{Fore.WHITE} \U0001F451 """
    elif string == 'King':
        image = f"""{Fore.CYAN}King{Fore.WHITE} \U0001F451 """
    elif string == 'Jack':
        image = f"""{Fore.CYAN}Jack{Fore.WHITE} \U0001F451 """
    elif string == 'Ace':
        image = f"""{Fore.CYAN}Ace{Fore.WHITE}"""
    else:
        image = f"""{Fore.CYAN}{string}{Fore.WHITE}"""
    return image


def cards_to_screen(who, when, cards):
    length = len(cards)
    nparray = numpy.array(cards)
    if when == "initial":
        for x in range(0, length):
            print(f"""{print_cards(nparray[x])}""")
    elif when == "playing" and who == "player":
        print(f"""
Dealer cards  : """)
        cards_to_screen(dealer.who, dealer.when, dealer.cards)
        print("")
        print('Your current cards : ', end="")
        for x in range(0, (length - 1)):
            one_line = print_cards(nparray[x])
            print(one_line, end=", ")
        print(f"""
New card is : {print_cards(nparray[-1])}
""")


def print_cards(hand):
    """Prints a user readable version of the cards to the terminal"""
    suit_image = change_suit_to_uni(hand['suit'])
    name_image = change_value_to_uni(hand['name'])
    image = f"""{name_image} {Fore.YELLOW}of{Fore.WHITE} {suit_image}"""
    return image


def request_bet():
    """
    The player is asked to provide an integer to place a bet with from their
    credit. The number is validated to be an integer and checked to be within
    thier credit available. Then the bet value updated if valid
    """
    global bet
    print(f"""{name}, it is time to place your bet.......
Your bet must not exceed your credit: {Fore.GREEN}{credit}{Fore.WHITE} units
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


def enough_cards():
    """
    Checks that there are enough cards left in the pack to
    continue dealing
    """
    if len(deck) > 1:
        pass
    else:
        new_deck = cards.generate_deck()
        deck.extend(new_deck)


def deal(stack, self):
    """
    Takes the last card from the deck that is being dealt from and places
    it either in the player or dealers list of cards
    """
    enough_cards()
    last_card = stack.pop()
    self.cards.append(last_card)
    cards_to_screen(self.who, self.when, self.cards)


def initial_deal(active_cards):
    """
    Carries out the function of the dealer initially dealing the cards
    to the table before the user has interaction with the cards
    """
    print(f"""Your bet is {Fore.RED}{bet}{Fore.WHITE}""")
    print('Dealing cards..........')
    sleep(2)
    print("Your first card is:")
    deal(active_cards, player)
    sleep(1)
    print('The dealers first card is:')
    deal(active_cards, dealer)
    sleep(1)
    ingame_screen()
    print('Dealing cards..........')
    sleep(2)
    print("Your cards:")
    deal(active_cards, player)
    sleep(1)
    print('The dealers cards:')
    deal(active_cards, dealer)
    player.when = "playing"


def ace(total, aces):
    """
    Checks if there are aces - which can be 1 or 11.
    If there are aces if calculate what their values added
    together equals
    """
    value = 0
    if aces > 0:
        if total < (12 - aces):
            value = (10 + aces)
        else:
            value = aces
    return value


def change_court_to_num(string):
    """Changes the string name of the card to an integer """
    if string == 'Jack' or string == 'Queen' or string == 'King':
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
    elif total > 21:
        pay_type = 'bust'


def double_down():
    global bet
    global credit
    credit -= bet
    bet *= 2
    deal(deck, player)
    dealer_time()


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
    print(f"""You have chosen {choices[chosen]}!""")
    return chosen


def progress_player_choice(choice):
    """
    Carries out the action that the user has chosen to either hit or stick
    """
    if choice == 0:
        ingame_screen()
        deal(deck, player)
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
    print(f"""{name} - Your bet is {Fore.RED}{bet}{Fore.WHITE}""")


def player_time():
    """
    performs the functions that are required during the players interaction
    with the cards. If there is an instant winner/bust moves player to
    that route
    """
    global player_total
    player_total = calculate_total(player.cards)
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
    global pay_type
    if dealer_total > 21 or dealer_total < player_total:
        pay_type = 'even'
    elif (dealer_total > player_total):  # and (dealer_total < 22):
        pay_type = 'no'
    elif dealer_total == player_total:
        pay_type = 'back'
    pay_winnings()


def amount_winnings():
    """
    Calculates what the winnings/if there are winnings depending on what
    the outcome of the game was
    """
    print(pay_type)
    pay = 0
    if pay_type == 'blackjack':
        pay = ((bet/2)*3)+bet
    elif pay_type == 'bust' or pay_type == 'no':
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
    print(f"""credit is now {Fore.GREEN}{credit}{Fore.WHITE}!!!""")
    continue_playing()


def dealer_time():
    """
    Performs the actions required during the time the dealer is interacting
    with the cards after the play has completed their turn
    """
    global dealer_total
    if pay_type == 'undecided':
        ingame_screen()
        dealer_total = calculate_total(dealer.cards)
        dealer.when = "playing"
        for x in range(2, 17):
            if dealer_total <= 17:
                deal(deck, dealer)
                dealer_total = calculate_total(dealer.cards)
                sleep(2)
            elif dealer_total > 17:
                break
        who_won()


def clear_for_round():
    """
    Clears variables that need to be empty at the beginning of a round,
    so the game can continue a the end of a round
    """
    global pay_type
    global player_total
    global dealer_total
    pay_type = 'undecided'
    player.cards.clear()
    player_total = 0
    dealer.cards.clear()
    dealer_total = 0
    dealer.when = "initial"
    player.when = "initial"


def continue_playing():
    """
    Allows the user to decide if they want to continue playing at the end
    of the round with another round
    """
    if credit >= 1:
        print('Do you want to continue playing another round?')
        contnue = ["[Y] Yes", "[N] No"]
        terminal_menu = TerminalMenu(contnue)
        chosen = terminal_menu.show()
        print(f"""You have chosen {contnue[chosen]}!""")
        if chosen == 1:
            clear_terminal()
            print(f"""Thank you for playing
Your final credit was {Fore.GREEN}{credit}{Fore.WHITE} units""")
            ascii.goodbye()
        elif chosen == 0:
            clear_for_round()
            main()
    else:
        clear_terminal()
        print(f"""{name} thank you for playing""")
        print('You are out of credit so we have to say GOODBYE!!!')
        ascii.goodbye()


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
        if validate_name(cap_name) and len(cap_name) < 10:
            name = (cap_name)
        elif validate_name(cap_name) and len(cap_name) > 9:
            name = cap_name[:9]
            print(f"""the name you entered is too long.
It has been shortened to {name}.
If this is unacceptable you can quit in next menu.
Then when you restart you can choose a different name""")
            sleep(7)
        else:
            print(f"""you entered {Fore.RED}{in_name}{Fore.WHITE}
This is not a name consisting of only of letters.
Please re-enter your name using letters only""")
            request_name()


def total_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """The main run through of the program for an entire players hand"""
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
