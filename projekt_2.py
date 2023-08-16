"""
projekt_2.py: second project for Engeto Online Python Akademie
author: Vratislav Martin
email: abbadc@gmail.com
discord: Vratislav M (dříve: abbadc#8421)

"""
# import moduls from python
import random
import os

# import play_board 
from play_board import helping_board, printing_board

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



# Function to print the game board
def printing_board(board):
    print("+---+---+---+")
    for i in range(3):
        print("| {} | {} | {} |".format(*board[i*3:i*3+3]))
        print("+---+---+---+")

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Action for create players
def create_player(number):
    symbol = "X" if number == "1" else "O"
    return {"type": "player", "symbol": symbol}

# Function for player's move
def player_move(board, symbol):
    while True:
        position = input(f"Player {symbol}, enter a position for your move (1-9): ")

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

# Main game loop 
def player_vs_player():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = [create_player("1"), create_player("2")]
    current_player = players[0]

    print()
    print("This is your board")
    print()
    helping_board()

    move_count = 1

    while True:
          
        # After the seventh move, print game board
        if move_count > 1:
            printing_board(board)

        # Player's move
        player_move(board, current_player["symbol"])

        # Check if the player wins
        if check_winner(board, current_player["symbol"]):
            clear_console()
            printing_board(board)
            print(f"Player {current_player['symbol']} wins!")
            break

        # Check for a draw
        if is_board_full(board):
            clear_console()
            printing_board(board)
            print("This is a Draw!")
            break

        # Switch to the other player
        current_player = players[1] if current_player == players[0] else players[0]
        move_count += 1

        # Clear the console
        clear_console()

# Function to check for a win
def check_winner(board, symbol):
    # Check rows
    for i in range(0, 9, 3):
        if all(cell == symbol for cell in board[i:i+3]):
            return True
    
    # Check columns
    for i in range(3):
        if all(board[i+j*3] == symbol for j in range(3)):
            return True
    
    # Check diagonals
    if all(board[i] == symbol for i in [0, 4, 8]) or all(board[i] == symbol for i in [2, 4, 6]):
        return True

# Function to check for a full board
def is_board_full(board):
    return all(cell != " " for cell in board)

# Start the game (player vs player)
player_vs_player()
