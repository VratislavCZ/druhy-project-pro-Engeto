"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Vratislav Martin
email: abbadc@gmail.com
discord: Vratislav M (dříve: abbadc#8421)

"""
# import moduls from python
import random
import os

# import play_board not work :(
from play_board import *

# Define separator variables
separator_b = "=" * 44
separator_s = "-" * 44

# Print a welcome message
print("Welcome to Tic Tac Toe")
print(separator_b)

# Print game rules
print("""GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:\n""")

# Set the color code
red_code = '\033[31m'   
print(red_code + "* horizontal,")
print("* vertical or")
print("* diagonal row")
print('\033[0m', end='')
print()

print(separator_b)

# Print a message to start the game
print("Let's start the game")
print(separator_s)

print()
print(f"This is your board\n")
helping()
print()

# Function to print the game board
def printing_board(board):
    print("+---+---+---+")
    for i in range(3):
        print("| {} | {} | {} |".format(*board[i*3:i*3+3]))
        print("+---+---+---+")

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Possible action, for select game type: with pc or with player
def select_game_type():
    while True:
        typ = input("Select game type: 1 - against player, 2 - against computer: ")
        if typ in ["1", "2"]:
            symbol = "O"
            if typ == "2":
                return create_computer(symbol)
            return create_player(symbol)
        print("Invalid choice. Please enter 1 or 2.")

# Action for player vs player
def create_player(symbol):
    return {"type": "player", "symbol": symbol}

# Action for player vs computer
def create_computer(symbol):
    return {"type": "computer", "symbol": symbol}

player = select_game_type()

# Function for player's move
def player_move(board, symbol):
    while True:
        position = input("Enter a position for your move (1-9): ")

        # Check if the input is valid and the position is empty
        if position.isdigit() and 1 <= int(position) <= 9:
            index = int(position) - 1
            if board[index] == " ":
                board[index] = symbol
                break
            else:
                print("Position is already occupied. Please select another position.")
        else:
            print("Invalid move. Enter a number from 1 to 9 and select an empty position.")

# Function for computer's move
def computer_move(board, symbol):
    available_positions = [i for i, cell in enumerate(board) if cell == " "]
    position = random.choice(available_positions)
    board[position] = symbol

