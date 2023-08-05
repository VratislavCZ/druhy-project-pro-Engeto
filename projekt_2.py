"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Vratislav Martin
email: abbadc@gmail.com
discord: Vratislav M (dříve: abbadc#8421)

"""
import random

oddelovac_v = "============================================"
oddelovac_m = "--------------------------------------------"

def print_board():
    for i in range(3):
        print("+---+---+---+")
        for j in range(3):
            print("| {} ".format(i*3 + j + 1), end="")
        print("|")
    print("+---+---+---+")

    return print_board


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

print_board()

# possible action, pc or user
def vselect_game_type():
    while True:
        typ = input("Select game type: 1 - against player, 2 - against computer: ")
        if typ == "1":
            self.player2 = player("O")
            break
        elif typ == "2":
            self.player2 = computer("O")  
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

vselect_game_type()