"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Vratislav Martin
email: abbadc@gmail.com
discord: Vratislav M (dříve: abbadc#8421)

"""
import random


oddelovac_v = "============================================"
oddelovac_m = "--------------------------------------------"

plocha ="+---+---+---+\n" \
        "| | | |\n" \
        "+---+---+---+\n" \
        "| | | | \n" \
        "+---+---+---+\n" \
        "| | | |\n" \
        "+---+---+---+\n" \

# hezci_plocha: "   |   |   \n" \
#          "-----------\n" \
#          "   |   |   \n" \
#          "-----------\n" \
#          "   |   |   "

print("Welcome to Tic Tac Toe")
print(oddelovac_v)
print("""GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a: """)
red_code = '\033[31m'   
print(red_code +"* horizontal,")
print("* vertical or")
print("* diagonal row")
print('\033[0m', end='')
print(oddelovac_v)
print("Let's start the game")
print(oddelovac_m)

print(plocha)