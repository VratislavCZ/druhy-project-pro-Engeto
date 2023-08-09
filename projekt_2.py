"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Vratislav Martin
email: abbadc@gmail.com
discord: Vratislav M (dříve: abbadc#8421)

"""
import random

oddelovac_v = "============================================"
oddelovac_m = "--------------------------------------------"

# helpful game board
def help_board():
    for i in range(3):
        print("+---+---+---+")
        for j in range(3):
            print("| {} ".format(i*3 + j + 1), end="")
        print("|")
    print("+---+---+---+")

    return help_board

# game board during the game
def print_board():
    for i in range(3):
        print("+---+---+---+")
        for j in range(3):
            print("|   ", end="")
        print("|")
    print("+---+---+---+")

# Print a welcome message
print("Welcome to Tic Tac Toe")
print(oddelovac_v)

# Print game rules
print("""GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a: """)

# Set the color code
red_code = '\033[31m'   
print(red_code +"* horizontal,")
print("* vertical or")
print("* diagonal row")
print('\033[0m', end='')

print(oddelovac_v)

# Print a message to start the game
print("Let's start the game")

print(oddelovac_m)

# possible action, pc or user
def select_game_type():
    while True:
        typ = input("Select game type: 1 - against player, 2 - against computer: ")
        if typ == "1":
            player2 = create_player("O")
            break
        elif typ == "2":
            player2 = create_computer("O")  
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
# action for player vs player
def create_player(symbol):
    return {"type": "player", "symbol": symbol}
# action for player vs computer
def create_computer(symbol):
    return {"type": "computer", "symbol": symbol}

select_game_type()

help_board()