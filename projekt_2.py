"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Vratislav Martin
email: abbadc@gmail.com
discord: Vratislav M (dříve: abbadc#8421)

"""
# import moduls from python
import random
import os

# import play_board 
from play_board import helping, printing_board

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

# Function to create players.
def create_players():
    return [
        {"type": "player", "symbol": "O"},
        {"type": "player", "symbol": "X"}
    ]

# Main game loop
def game_loop():
    # Initialize the board
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = create_players()

    # Action for player vs player
    def create_player(symbol):
        return {"type": "player", "symbol": symbol}

    # Function for a player's move
    def player_move(board, players, player_number):
        while True:
            position = input(f"Player {player_number}: Enter a position for your move (1-9): ")

            # Check if the input is valid and the position is empty
            if position.isdigit() and 1 <= int(position) <= 9:
                index = int(position) - 1
                if board[index] == " ":
                    board[index] = players["symbol"]
                    break
                else:
                    print("Position is already occupied. Please select another position.")
            else:
                print("Invalid move. Enter a number from 1 to 9 and select an empty position.")

    # Game loop until there's a winner or a draw
    while True:
        player_move(board, players, 1)
        printing_board(board)

        if check_winner(board, players.get("symbol")):
            clear_console()
            printing_board(board)
            print("Player wins!")
            break

        if is_board_full(board):
            clear_console()
            printing_board(board)
            print("The match ended in a tie!")
            break

        player_move(board, players, 2)
        printing_board(board)

        if check_winner(board, players.get("symbol")):
            clear_console()
            printing_board(board)
            print("Player 2 wins!")
            break

        if is_board_full(board):
            clear_console()
            printing_board(board)
            print("The match ended in a tie!")
            break

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
    return False

# Function to check for a full board
def is_board_full(board):
    return all(cell != " " for cell in board)

# Start the game
game_loop()
