import emoji
from colorama import Fore

images = {"spade": "\u2660",
          "heart": f"""{Fore.RED}\u2665{Fore.WHITE}""",
          "club": "\u2663",
          "diamond": f"""{Fore.RED}\u2666{Fore.WHITE}""",
          "Queen": f"""{Fore.CYAN}Queen{Fore.WHITE} \U0001F451 """,
          "King": f"""{Fore.CYAN}King{Fore.WHITE} \U0001F451 """,
          "Jack": f"""{Fore.CYAN}Jack{Fore.WHITE} \U0001F451 """,
          "Ace": f"""{Fore.CYAN}Ace{Fore.WHITE}""",
          }


def change_to_uni(string):
    emoj = images[string]
    return emoj
