import os
from time import sleep
from colorama import Fore


def total_clear():
    """clears whole screen without adding a title unlike clear terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def enter_to_continue():
    """
    Waits for user to press enter so that can continue to next screen
    when ready.
    """
    while True:
        is_enter = input("Press Enter to continue...")
        if is_enter == "":
            break
        else:
            print("Please don't use other keys, just press Enter to continue.")
    total_clear()  # leaves screen completely clear for next information


def str_instructions():
    total_clear()  # removes everything including title to give space
    print("")
    print(f"""Initially you enter your {Fore.CYAN}{Fore.WHITE}name
using letters
""")
    sleep(1)
    print(f"""Then you place a {Fore.RED}bet{Fore.WHITE}, by typing
a whole number, which is less than or equal to
your {Fore.GREEN}credit{Fore.WHITE}.
""")
    sleep(1)
    print("The cards will then be dealt. Two each for you and the dealer")
    # - If you have two identical value cards you can then split.
    sleep(1)
    print(f"""You can {Fore.CYAN}Hit{Fore.WHITE} - get one more card,
then you decide again,
{Fore.CYAN}Stick{Fore.WHITE} - stay where you are
{Fore.CYAN}Double down{Fore.WHITE} - bet doubles
and gives you only one more card.
""")
    sleep(1)
    print(f"""Your cards are worth their face value if they are a number card.
{Fore.CYAN}Jack, Queen{Fore.WHITE} and {Fore.CYAN}King{Fore.WHITE}
are worth {Fore.CYAN}10{Fore.WHITE}
and {Fore.CYAN}Ace{Fore.WHITE} can be worth
{Fore.CYAN}1{Fore.WHITE} or {Fore.CYAN}11{Fore.WHITE}.
""")
    sleep(1)
    enter_to_continue()  # awaits user to click enter for next screen
    print(f"""
If you exceed {Fore.CYAN}21{Fore.WHITE} then you will lose.
If you get {Fore.CYAN}21{Fore.WHITE} there is an instant payout.
If you {Fore.CYAN}stick{Fore.WHITE} or {Fore.CYAN}double down{Fore.WHITE} then
it is the dealers turn
""")
    sleep(1)
    print(f"""You will now get to see all the dealers cards
and any additional cards he deals himself.

If the dealer gets higher than you without
exceeding {Fore.CYAN}21{Fore.WHITE} he wins

If he exceeds {Fore.CYAN}21{Fore.WHITE} you win

If at the end you have the higher value - you win.

{Fore.CYAN}21{Fore.WHITE} gets a higher return than just beating the dealer.
""")
    sleep(1)
    enter_to_continue()


def str_instructions_query():
    print(f"""Please choose whether to
   {Fore.CYAN}Play the game{Fore.WHITE}
or {Fore.CYAN}Read instructions{Fore.WHITE}
or {Fore.CYAN}Quit - this will remove you from program{Fore.WHITE}.
move up or down to select then press enter""")


def str_request_bet():
    print(f"""If you wanted to bet {Fore.RED}50{Fore.WHITE} units,
you would type {Fore.RED}50{Fore.WHITE} and press enter
Please input your bet""")


def str_player_action():
    print(f"""Please choose whether to
{Fore.CYAN}Hit{Fore.WHITE} (get one more card)
or {Fore.CYAN}Stick{Fore.WHITE} (No more cards)
or {Fore.CYAN}Double down{Fore.WHITE} (get one more card and double bet)
or {Fore.CYAN}Quit round{Fore.WHITE} (loose bet and end round)
move up or down to select then press enter""")
